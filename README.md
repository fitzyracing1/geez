# geez

**Phone-first MCP tool that lets Claude (or any MCP client) call Grok.**

Minimal. Requests-only. Zero bloat. Built to run cleanly in Termux / proot-distro.

## Why "geez"
Because sometimes you just want Claude to be able to ask Grok without dragging the entire Super guard stack along.

## Quick start (phone or desktop)

```bash
pip install -e .
export XAI_API_KEY=your_xai_key_here   # get one at https://console.x.ai
geez
```

Then connect any MCP client (Claude Desktop, Cursor, etc.) to the `geez` stdio server.

### From Claude
```
call_grok(
  prompt="Explain quantum spin processors in plain English",
  system="You are Grok, built by xAI. Be direct and helpful.",
  model="grok-3",
  max_tokens=800
)
```

## Tools exposed

| Tool        | Description                                      |
|-------------|--------------------------------------------------|
| `call_grok` | Send a prompt to Grok and get the response back  |

## Environment

```bash
XAI_API_KEY=...          # required
# GROK_API_KEY=...       # alias also accepted
```

## Design principles
- Single dependency beyond stdlib: `requests` + `mcp`
- No guard pipelines, no Cisco, no Duo, no Stripe — just the call
- Phone-native: works in Termux with almost no setup
- Fully public and auditable

---

Made for the same phone-first workflow as the rest of the portfolio.
