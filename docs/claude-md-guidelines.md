# How to write CLAUDE.md

**TL;DR: keep CLAUDE.md to one screen. It holds rules that apply to every task and a
pointer table. Everything else goes in its own document, with one line in CLAUDE.md
pointing there. Never edit it without David's approval.**

**CLAUDE.md is loaded into every prompt.** Everything in it costs context on every task,
whether or not that task needs it. So the test for including something is not *is this
true* or *is this useful*. It is:

> **Would an agent get this wrong on a task that has nothing to do with it?**

If yes, it belongs. If it only matters once you are already doing X, it belongs in the
document about X, and CLAUDE.md gets one line pointing there.

## What earns a place

- **Rules that apply to every prompt.** Lead with the answer. No em dashes. Never merge to main without asking.
- **Rules whose violation is expensive and silent.** Publishing named-person scores,
  presenting a schema demo as evidence. An agent will not discover these by reading the
  repo, and by the time the mistake shows up it is in a commit or an email.
- **The failure modes this project actually hits**, one line each. Not a general theory of good work.
- **Commands**, one line each, once scripts exist.
- **A pointer table** so anything cut is one hop away.

## What does not

- **Reference material.** Source lists, schemas, seed rows, research method. Real and
  worth writing down, in their own file.
- **Things the repository already states.** `.gitignore` says what is ignored.
  `.mcp.json` says which servers are configured.
- **History.** What a weekend did, what was dropped. That is git and the docs.
- **Anything a competent agent does anyway.** Checking work, being careful. Instructions
  that describe the default are noise that dilutes the rules that do not.

## Rules of thumb

- **One screen.** If it does not fit, something in it is reference material.
- **Every section should answer: what breaks if this is missing?** If the answer is
  "nothing, the agent would just have to look it up," it is a pointer, not a section.
- **Prefer a rule to an explanation.** Put the why in the doc the pointer leads to.
- **A pointer is not a loss.** Moving something to its own file lets it grow and get
  better, because it no longer competes for space.
- **When you add a document, add its row to the pointer table.** That is usually the only edit CLAUDE.md needs.

## Changing it

**Do not edit CLAUDE.md without David's approval.** It shapes every future session, an
agent editing its own standing instructions is a change nobody reviews, and drift here is
invisible until something goes wrong. Propose the change, say what it would replace, and
say which document the detail goes in instead.
