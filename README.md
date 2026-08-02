<div align="center">

# Lint Fast, Type Hard

### Elevate your code quality in Python with modern, ultra-fast tooling

Materials and live demos for a talk on how [Ruff](https://docs.astral.sh/ruff/), [ty](https://docs.astral.sh/ty/), and [uv](https://docs.astral.sh/uv/) make formatting, linting, and type checking fast enough that teams actually adopt them — locally, in pre-commit, and in CI.

<br />

[![Ruff](https://img.shields.io/badge/Ruff-formatter%20%26%20linter-261230?style=for-the-badge&logo=ruff&logoColor=D7FF64)](https://docs.astral.sh/ruff/)
[![ty](https://img.shields.io/badge/ty-type%20checker-261230?style=for-the-badge)](https://docs.astral.sh/ty/)
[![uv](https://img.shields.io/badge/uv-package%20manager-261230?style=for-the-badge)](https://docs.astral.sh/uv/)

<br />

**Speaker:** [Miguel Vargas](https://www.linkedin.com/in/lmiguelvargasf/)
&nbsp;·&nbsp;
**Slides:** [Lint Fast, Type Hard](https://gamma.app/docs/Lint-Fast-Type-Hard-PyCon-Colombia-2026-e56rcq4mjnzcgvl?mode=doc)

</div>

---

## Presented at

| Conference | Year | Location | Links |
| --- | :---: | --- | --- |
| [**PyCon Panamá**](https://pycon.pa/2025/) | 2025 | Panama City, Panama | [Website](https://pycon.pa/2025/) · [Agenda](https://pycon.pa/2025/agenda.html) |
| [**PyTexas**](https://pytexas.org/2026/) | 2026 | Austin, Texas, USA | [Website](https://pytexas.org/2026/) · [Schedule](https://pytexas.org/2026/schedule/) · [Talks](https://pytexas.org/2026/schedule/talks/) |
| [**PyCon Colombia**](https://2026.pycon.co/) | 2026 | Medellín, Colombia | [Website](https://2026.pycon.co/) · [Talk](https://2026.pycon.co/speakers/miguel-vargas/) |

---

## Abstract

Modern Python tooling turns code quality into a **speed advantage**.

This talk shows how fast, developer-friendly tools such as `ruff` and `ty` remove the usual friction around formatting, linting, and type checking — so teams can adopt reliable quality gates without slowing delivery.

It also explains why clean, well-typed code matters even more in AI-assisted development, and walks through a practical adoption path:

`pyproject.toml` → local workflows → pre-commit hooks → CI

---

## What's in this repo

| Path | Description |
| --- | --- |
| [`ruff_demo.py`](ruff_demo.py) | A deliberately messy script for demoing formatting and linting with Ruff |
| [`ty_demo.py`](ty_demo.py) | A script with intentional type errors for demoing type checking with ty |
| [`prompts/`](prompts/) | Ready-to-use prompts for running the demos with an AI coding agent |

---

## Try it yourself

The only requirement is [uv](https://docs.astral.sh/uv/) — `uvx` runs each tool without installing anything else.

<details open>
<summary><strong>1. Lint with Ruff</strong></summary>

```bash
uvx ruff check --fix ruff_demo.py
uvx ruff check --fix --unsafe-fixes ruff_demo.py
```

</details>

<details open>
<summary><strong>2. Format with Ruff</strong></summary>

```bash
uvx ruff format ruff_demo.py
```

</details>

<details open>
<summary><strong>3. Type check with ty</strong></summary>

```bash
uvx ty check ty_demo.py
```

</details>

Prefer an AI-assisted workflow? The [`prompts/`](prompts/) folder contains the exact prompts used during the talk to have a coding agent run these steps and explain every fix.

---

## Demo project: Mini Helpdesk

The main live demo is [**pycon-colombia-2026-mini-helpdesk**](https://github.com/lmiguelvargasf/pycon-colombia-2026-mini-helpdesk) — a small legacy Django helpdesk app used to show how to introduce Ruff and ty into an existing codebase.

It ships with everything you need to follow along:

- A `uv`-managed environment with locked dependencies
- Database migrations and a `seed_tickets` command for sample data
- A development server and a test suite to verify nothing breaks

→ [Setup instructions](https://github.com/lmiguelvargasf/pycon-colombia-2026-mini-helpdesk#setup)

---

## Tooling

| Tool | Role | Docs |
| --- | --- | --- |
| **Ruff** | Formatter & linter | [docs.astral.sh/ruff](https://docs.astral.sh/ruff/) |
| **ty** | Type checker | [docs.astral.sh/ty](https://docs.astral.sh/ty/) |
| **uv** | Package & project manager | [docs.astral.sh/uv](https://docs.astral.sh/uv/) |
| **Astral** | Builders of the toolchain | [astral.sh](https://astral.sh/) |

---

## Agent skills

Teach AI coding agents how to use these tools effectively:

| Skill | Link |
| --- | --- |
| Astral skills repository | [astral-sh/claude-code-plugins](https://github.com/astral-sh/claude-code-plugins) |
| Ruff skill | [skills.sh/astral-sh/claude-code-plugins/ruff](https://skills.sh/astral-sh/claude-code-plugins/ruff) |
| ty skill | [skills.sh/astral-sh/claude-code-plugins/ty](https://skills.sh/astral-sh/claude-code-plugins/ty) |
| uv skill | [skills.sh/astral-sh/claude-code-plugins/uv](https://skills.sh/astral-sh/claude-code-plugins/uv) |

---

<div align="center">

**Built for the Python community** · Presented across the Americas · 2025–2026

</div>
