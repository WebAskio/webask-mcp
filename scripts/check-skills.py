#!/usr/bin/env python3
"""Проверка набора перед публикацией: шапки SKILL.md, паритет языков, манифесты.

Запуск: python3 scripts/check-skills.py — без зависимостей, только стандартная библиотека.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm, key = {}, None
    for line in m.group(1).split("\n"):
        km = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if km:
            key = km.group(1)
            fm[key] = km.group(2).strip()
        elif key and line.startswith("  "):
            fm[key] += " " + line.strip()
    return fm


known_tools = set(re.findall(r"^\| `([a-z0-9_]+)` \|", (ROOT / "docs/tools.md").read_text(encoding="utf-8"), re.M))
sets = {}
for label, base in (("ru", ROOT / "skills"), ("en", ROOT / "en/skills")):
    names = []
    for d in sorted(p for p in base.iterdir() if p.is_dir()):
        names.append(d.name)
        skill = d / "SKILL.md"
        if not skill.exists():
            errors.append(f"{label}/{d.name}: нет SKILL.md")
            continue
        fm = frontmatter(skill.read_text(encoding="utf-8"))
        if fm is None:
            errors.append(f"{label}/{d.name}: нет шапки")
            continue
        extra = set(fm) - {"name", "description"}
        if extra:
            errors.append(f"{label}/{d.name}: лишние ключи в шапке: {', '.join(sorted(extra))}")
        name, desc = fm.get("name", ""), fm.get("description", "")
        if not desc.startswith('"') and re.search(r":\s|\s#", desc):
            errors.append(f"{label}/{d.name}: описание без кавычек содержит «: » или « #» — строгий YAML его не прочтёт")
        if len(desc) >= 2 and desc[0] == desc[-1] == '"':
            desc = desc[1:-1]
        if name != d.name:
            errors.append(f"{label}/{d.name}: name={name!r} не совпадает с папкой")
        if not re.fullmatch(r"[a-z0-9-]{1,64}", name) or re.search(r"anthropic|claude", name):
            errors.append(f"{label}/{d.name}: недопустимое имя")
        if not desc or len(desc) > 1024:
            errors.append(f"{label}/{d.name}: описание пустое или длиннее 1024 символов ({len(desc)})")
        yaml = d / "agents/openai.yaml"
        if yaml.exists():
            for t in re.findall(r'value:\s*"([a-z0-9_]+)"', yaml.read_text(encoding="utf-8")):
                if t not in known_tools:
                    errors.append(f"{label}/{d.name}: инструмента {t} нет в docs/tools.md")
    sets[label] = names

if sets["ru"] != sets["en"]:
    errors.append("русский и английский наборы разошлись: " + " ".join(sorted(set(sets["ru"]) ^ set(sets["en"]))))

for f in [*ROOT.glob(".claude-plugin/*.json"), ROOT / "en/.claude-plugin/plugin.json", ROOT / "server.json",
          *ROOT.glob("clients/*.json")]:
    try:
        json.loads(f.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"{f.relative_to(ROOT)}: {e}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: {len(sets['ru'])} навыков на двух языках, манифесты читаются")
