<sub><a href="../README.md">WebAsk MCP</a> › Connecting</sub>

# Connecting to the WebAsk MCP server

| | |
|---|---|
| URL | `https://mcp.webask.io/mcp/v1` |
| Transport | Streamable HTTP |
| Auth | header `Authorization: Bearer <key>` |

## 1. Key

1. Sign in to WebAsk.
2. Open **Settings → API / MCP**.
3. Click **Create API key** and copy it right away: the key is shown only once.

The key acts on your behalf with your workspace permissions. Revoke it in the same place.

## 2. Client

### Claude Code

With skills, as a plugin. Claude Code asks for the key during installation and keeps it in the system keychain:

```text
/plugin marketplace add WebAskio/webask-mcp
/plugin install webask-en@webask
```

Server only:

```bash
claude mcp add --transport http webask https://mcp.webask.io/mcp/v1 \
  --header "Authorization: Bearer YOUR_API_KEY"
```

To check: `/mcp` in Claude Code shows the WebAsk server as connected.

### Claude Desktop

1. **Settings → Developer → Edit Config** opens `claude_desktop_config.json`.
2. Paste [`clients/claude-desktop.json`](../../clients/claude-desktop.json) and replace `YOUR_API_KEY`.
3. Restart Claude Desktop.

Requires Node.js: the config runs [mcp-remote](https://github.com/geelen/mcp-remote), which passes the key to
the server.

### Cursor

**Settings → MCP → Add new global MCP server**, paste [`clients/cursor.json`](../../clients/cursor.json) and
replace `YOUR_API_KEY`. The same file works as `~/.cursor/mcp.json` for all projects or `.cursor/mcp.json`
for one.

### VS Code

Put [`clients/vscode.json`](../../clients/vscode.json) into your project as `.vscode/mcp.json`. VS Code asks
for the key the first time the server starts and stores it itself.

### Codex

Add [`clients/codex.toml`](../../clients/codex.toml) to `~/.codex/config.toml` and pass the key through the
environment:

```bash
export WEBASK_API_KEY=YOUR_API_KEY
```

### Gemini CLI

As an extension, with the server and the skills at once. Gemini asks for the key during installation and keeps
it in the system keychain:

```bash
gemini extensions install https://github.com/WebAskio/webask-mcp
```

Server only: add [`clients/gemini.json`](../../clients/gemini.json) to `~/.gemini/settings.json` and replace
`YOUR_API_KEY`.

### Other clients

Any client that can connect a remote MCP server over HTTP with a custom header will do. URL —
`https://mcp.webask.io/mcp/v1`, header — `Authorization: Bearer <key>`.

## 3. First request

“Show my surveys and how many answers came in this week.” The assistant calls `get_quiz_list` and
`get_quiz_summary` and replies with a list. More ideas in [prompts.md](prompts.md).

## Troubleshooting

| What you see | What to do |
|---|---|
| The server returns `401` | The key is missing or revoked. Check the header: `Authorization: Bearer <key>`, with a space |
| “Insufficient permissions: this action requires …” | Your member permissions are limited. The workspace owner can grant them |
| A refusal that mentions the plan | The feature isn't in the workspace plan. The assistant will tell you which plans include it |
| The assistant hit the request limit | The limit is 180 requests per minute per user, wait a minute |
| An export link doesn't open | Export links live for one hour, ask for a fresh export |
