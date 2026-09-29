<sub><a href="../README.md">WebAsk MCP</a> › Подключение</sub>

# Подключение к MCP-серверу WebAsk

| | |
|---|---|
| Адрес | `https://mcp.webask.io/mcp/v1` |
| Транспорт | Streamable HTTP |
| Авторизация | заголовок `Authorization: Bearer <ключ>` |

## 1. Ключ

1. Войдите в кабинет WebAsk.
2. Откройте **Настройки → API / MCP**.
3. Нажмите **«Создать API-ключ»** и сразу скопируйте его: ключ показывается один раз.

Ключ действует от вашего имени и с вашими правами в пространстве. Отзывается там же, в **Настройки → API / MCP**.

## 2. Клиент

### Claude Code

С навыками — плагином. Ключ Claude Code спросит при установке и сохранит в системном хранилище паролей:

```text
/plugin marketplace add WebAskio/webask-mcp
/plugin install webask@webask
```

Только сервер:

```bash
claude mcp add --transport http webask https://mcp.webask.io/mcp/v1 \
  --header "Authorization: Bearer YOUR_API_KEY"
```

Проверить: команда `/mcp` в Claude Code показывает сервер WebAsk подключённым.

### Claude Desktop

1. **Settings → Developer → Edit Config** откроет `claude_desktop_config.json`.
2. Вставьте содержимое [`clients/claude-desktop.json`](../clients/claude-desktop.json) и замените
   `YOUR_API_KEY` на ключ.
3. Перезапустите Claude Desktop.

Нужен Node.js: конфиг запускает [mcp-remote](https://github.com/geelen/mcp-remote), который передаёт ключ
серверу.

### Cursor

**Settings → MCP → Add new global MCP server**, вставьте [`clients/cursor.json`](../clients/cursor.json) и
замените `YOUR_API_KEY`. Тот же файл можно положить в `~/.cursor/mcp.json` для всех проектов или в
`.cursor/mcp.json` для одного.

### VS Code

Положите [`clients/vscode.json`](../clients/vscode.json) в проект как `.vscode/mcp.json`. При первом запуске
сервера VS Code спросит ключ и сохранит его у себя, в файле ключа не будет.

### Codex

Добавьте [`clients/codex.toml`](../clients/codex.toml) в `~/.codex/config.toml` и передайте ключ через
переменную окружения:

```bash
export WEBASK_API_KEY=YOUR_API_KEY
```

### Gemini CLI

Добавьте [`clients/gemini.json`](../clients/gemini.json) в `~/.gemini/settings.json` и замените `YOUR_API_KEY`.

### Другие клиенты

Подойдёт любой клиент, который умеет подключать удалённый MCP-сервер по HTTP с собственным заголовком. Адрес —
`https://mcp.webask.io/mcp/v1`, заголовок — `Authorization: Bearer <ключ>`.

## 3. Первая просьба

«Покажи мои опросы и сколько ответов пришло за неделю». Ассистент вызовет `get_quiz_list` и
`get_quiz_summary` и ответит списком. Ещё идеи — в [prompts.md](prompts.md).

## Если что-то не так

| Что видно | Что делать |
|---|---|
| Сервер отвечает `401` | Ключ не передан или отозван. Проверьте заголовок: `Authorization: Bearer <ключ>`, через пробел |
| «Недостаточно прав: для этого действия нужно право …» | Права участника урезаны. Выдать право может владелец пространства |
| Отказ со ссылкой на тариф | Возможность закрыта тарифом пространства. Ассистент подскажет, какие тарифы её дают |
| Ассистент упёрся в лимит запросов | Лимит — 180 запросов в минуту на пользователя, подождите минуту |
| Ссылка на выгрузку не открывается | Ссылки на выгрузки действуют час, попросите выгрузить заново |

Подробная документация по инструментам и протоколу — на [webask.io/dev/api/mcp](https://webask.io/dev/api/mcp).
