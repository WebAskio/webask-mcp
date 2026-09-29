<sub><a href="../README.md">WebAsk MCP</a> › Навыки</sub>

# Навыки WebAsk

Навык — папка с файлом `SKILL.md`: инструкция для ассистента обычным языком, как решать задачу инструментами
WebAsk MCP. Ассистент читает навык сам, когда просьба под него подходит, — называть навык не нужно.

Кода в навыках нет, ничего не исполняется. Навыку нужен только доступ к WebAsk, его даёт
[MCP-сервер](../README.md#быстрый-старт).

### Собрать и раздать

| Навык | Что даёт | Скачать |
|---|---|:-:|
| [Сборка опроса по описанию](webask-quiz-from-brief/) | Опишите задачу словами — получите готовый опрос, а не список вопросов | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-quiz-from-brief.zip) |
| [Переписать формулировки](webask-quiz-copy/) | Переписывает вопросы так, чтобы опрос дочитывали, — и начинает с данных, а не со вкуса | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-quiz-copy.zip) |
| [Логика показа и маршруты](webask-quiz-logic/) | Собирает ветвление так, чтобы ни один респондент не упёрся в тупик | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-quiz-logic.zip) |
| [Материалы для запуска](webask-launch-kit/) | Собирает всё для запуска разом: ссылки с метками, тексты анонса и QR-код | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-launch-kit.zip) |
| [Раздача опроса](webask-quiz-distribution/) | Готовит опрос к раздаче так, чтобы потом было видно, из какого канала пришли ответы | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-quiz-distribution.zip) |

### Проверить перед запуском

| Навык | Что даёт | Скачать |
|---|---|:-:|
| [Проверка опроса перед запуском](webask-prelaunch-check/) | Находит то, что сломается на живых респондентах, пока ссылку ещё никому не отправили | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-prelaunch-check.zip) |
| [Качество собранных данных](webask-data-quality/) | Отвечает, можно ли верить этим данным, до того как на них построят выводы | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-data-quality.zip) |

### Понять результаты

| Навык | Что даёт | Скачать |
|---|---|:-:|
| [Разбор результатов опроса](webask-results-digest/) | Отвечает на «ну и что там по опросу» цифрами с выводом, а не выгрузкой сырых ответов | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-results-digest.zip) |
| [Анализ A/B-вариантов](webask-ab-significance/) | Отвечает, реальна разница между вариантами или это случайность | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-ab-significance.zip) |
| [Сравнение с собой прошлым](webask-benchmark/) | Сравнивает опрос с ним же прошлым: отдельная цифра ничего не значит, разница — значит | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-benchmark.zip) |
| [Разбор свободных ответов](webask-open-answers/) | Превращает сотню строк свободного текста в несколько тем с числами и цитатами | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-open-answers.zip) |
| [Воронка прохождения](webask-response-funnel/) | Показывает, на каком вопросе люди закрывают вкладку — и почему | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-response-funnel.zip) |
| [Сколько ответов нужно](webask-sample-oracle/) | Отвечает, хватает ли уже собранного и сколько ещё нужно, чтобы выводы не развернулись | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-sample-oracle.zip) |
| [Хронология опроса](webask-quiz-timeline/) | Отвечает на «почему перестали приходить ответы», сопоставляя сбор с историей правок | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-quiz-timeline.zip) |
| [Сравнение источников](webask-source-dashboard/) | Показывает, какой канал привёл людей, а какой — только цифры | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-source-dashboard.zip) |
| [Результаты — заказчику](webask-results-sharing/) | Собирает результаты в то, что можно отправить: ссылку, файл или отчёт с выводами | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-results-sharing.zip) |
| [Оформление отчётов и тема опроса](webask-report-appearance/) | Приводит в порядок то, что видят снаружи: тему опроса, палитру отчётов и логотип | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-report-appearance.zip) |

### Довести заявки

| Навык | Что даёт | Скачать |
|---|---|:-:|
| [Уведомления о новых ответах](webask-answer-notifications/) | Настраивает, куда сообщать о новых ответах, и чинит, когда сообщать перестало | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-answer-notifications.zip) |
| [Настройка вебхука](webask-webhook-setup/) | Заводит отправку ответов на ваш адрес и сразу проверяет, что приёмник их принял | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-webhook-setup.zip) |
| [Почему ответы не уходят](webask-integration-triage/) | Находит, почему заявки не доходят до CRM, Telegram или таблицы — и что с этим делать | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-integration-triage.zip) |
| [Качество заявок](webask-lead-quality/) | Считает не завершаемость, а сколько людей оставили пригодный контакт | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-lead-quality.zip) |

### Порядок в аккаунте

| Навык | Что даёт | Скачать |
|---|---|:-:|
| [Аудит аккаунта](webask-account-audit/) | Показывает одним отчётом, где аккаунт теряет ответы, место и деньги | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-account-audit.zip) |
| [Порядок в ответах](webask-answers-cleanup/) | Убирает тестовые прохождения и дубли, но сначала показывает, что именно попадёт под чистку | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-answers-cleanup.zip) |
| [Порядок в аккаунте](webask-workspace-housekeeping/) | Навык разберёт накопившиеся опросы, сохранит ответы и покажет план изменений до того, как что-либо поменяет. | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-workspace-housekeeping.zip) |
| [Участники и доступы](webask-workspace-access/) | Разбирается, почему участник не видит опросы, и выдаёт ровно те права, что нужны | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-workspace-access.zip) |

## Как установить

**Claude Code — плагином.** Ставит все навыки и MCP-сервер сразу, ключ спросит сам:

```text
/plugin marketplace add WebAskio/webask-mcp
/plugin install webask@webask
```

**Любой ассистент — архивом.** Скачайте ZIP нужного навыка из таблицы выше или все сразу —
[webask-skills-ru.zip](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-skills-ru.zip). Распакуйте в папку, из которой ассистент читает навыки, и
перезапустите его:

| Ассистент | Папка в проекте |
|---|---|
| Claude Code | `.claude/skills/` |
| Codex, Cursor | `.agents/skills/` |
| Gemini CLI | `.gemini/skills/` |

Должно получиться так:

```text
ваш-проект/
└── .claude/
    └── skills/
        └── webask-quiz-from-brief/
            ├── SKILL.md
            └── references/
```

## Что внутри папки навыка

| Файл | Зачем |
|---|---|
| `SKILL.md` | сам навык: когда применять, шаги по порядку, чего не делать |
| `references/` | справочники, которые навык подгружает по ссылке, когда они нужны |
| `agents/openai.yaml` | список инструментов MCP, от которых навык зависит |
| `README.md` | описание для GitHub; ассистенту не нужен |

## Версии

Версия навыка стоит в его `README.md`, история — в [CHANGELOG.md](../CHANGELOG.md).

- **Третья цифра** — поправили формулировку. Скачивать заново не обязательно.
- **Вторая цифра** — добавили шаг, правило или справочник. Стоит обновить.
- **Первая цифра** — навык переписан. Прежний файл лучше удалить.

Навыки здесь — те же, что на витрине [webask.io/skills](https://webask.io/skills), и обновляются вместе с ней.
