# Notion access

Notion is reached through its hosted MCP server, configured in `.mcp.json`. No key lives
in the repo. The two docs in `docs/` were imported from Notion on 2026-09-25; the repo
copies are the working versions from here on.

## Setup

- **Claude Code on the web / in the app:** the Notion connector on David's claude.ai
  account is available in every session. Nothing to do.
- **Claude Code locally:** `.mcp.json` points at `https://mcp.notion.com/mcp` and
  `.claude/settings.json` enables it. The first use opens a Notion OAuth login in the
  browser; `/mcp` shows its status. Auth is stored per machine, never in the repo.

If a session cannot reach Notion, say so. Do not guess at page contents.

## Source pages

| Page | Notion |
|---|---|
| Promise ledger: scoring the decadal and P5 bets | [55db6500](https://app.notion.com/p/55db65007f7e4876900d939fae3928c9) → `docs/promise-ledger.md` |
| Trust graph or promise ledger: which to build | [d6b662a1](https://app.notion.com/p/d6b662a172104f00a6c65cc7d41f4106) → `docs/trust-graph-or-ledger.md` |
| Trust graph POC (the long-term design) | [c231e4e6](https://app.notion.com/p/c231e4e6dec04385acb0b6e8adef649b) |
| Applying Paul's approach to physics and astronomy (origin, proposal A) | [8a68006a](https://app.notion.com/p/8a68006af42e44bbb9a0778c8014f711) |
| Metascience & AI for Science: Landscape Map (parent) | [f54163d9](https://app.notion.com/p/f54163d9d85e4af196017b401ead0246) |

## Rules

- **Read Notion freely. Ask before writing to it.** The pages above belong to David's
  Planning workspace.
- **If a Notion page and its repo copy diverge, ask which wins.** Do not silently re-import.
