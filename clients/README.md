<sub><a href="../README.md">WebAsk MCP</a> › Конфиги</sub>

# Готовые конфиги

Скопируйте нужный файл или его содержимое в настройки клиента и замените `YOUR_API_KEY` на ключ из
кабинета WebAsk (**Настройки → API / MCP**). В VS Code и Codex ключ в файл писать не нужно.

| Файл | Куда | Ключ |
|---|---|---|
| [`claude-desktop.json`](claude-desktop.json) | Claude Desktop → Settings → Developer → Edit Config | в `env`, нужен Node.js |
| [`cursor.json`](cursor.json) | Cursor → Settings → MCP, или `~/.cursor/mcp.json` | в `headers` |
| [`vscode.json`](vscode.json) | `.vscode/mcp.json` в проекте | VS Code спросит сам |
| [`codex.toml`](codex.toml) | `~/.codex/config.toml` | из `WEBASK_API_KEY` |
| [`gemini.json`](gemini.json) | `~/.gemini/settings.json` | в `headers` |

Claude Code подключается одной командой, а с навыками — плагином:

```bash
claude mcp add --transport http webask https://mcp.webask.io/mcp/v1 \
  --header "Authorization: Bearer YOUR_API_KEY"
```

Подробности — в [`../docs/connect.md`](../docs/connect.md).
