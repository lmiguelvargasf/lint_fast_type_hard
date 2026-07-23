# Lint Fast, Type Hard ⚡

Materials and demos for **_Lint Fast, Type Hard: Elevate your code quality in Python with modern, ultra-fast tooling_**, a talk at **PyCon Colombia 2026**.

This repository shows how modern tools such as [Ruff](https://docs.astral.sh/ruff/), [ty](https://docs.astral.sh/ty/), and [uv](https://docs.astral.sh/uv/) make code quality faster to adopt across local development, pre-commit workflows, and CI.

|                     |                                                                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 🎤 **Speaker**      | [Miguel Vargas](https://www.linkedin.com/in/lmiguelvargasf/)                                                                          |
| 🐍 **Event**        | [PyCon Colombia 2026](https://2026.pycon.co)                                                                                          |
| 🗣️ **Talk**         | [Elevate your code quality in Python with modern, ultra-fast tooling](https://2026.pycon.co/speakers/miguel-vargas/)                  |
| 📑 **Slides**       | [Lint Fast, Type Hard](https://gamma.app/docs/Lint-Fast-Type-Hard-PyCon-Colombia-2026-e56rcq4mjnzcgvl?mode=doc)                       |
| 🎫 **Demo project** | [pycon-colombia-2026-mini-helpdesk](https://github.com/lmiguelvargasf/pycon-colombia-2026-mini-helpdesk)                              |

## Abstract 📝

This talk explores how modern Python tooling turns code quality into a speed advantage. It shows how fast, developer-friendly tools such as `ruff` and `ty` reduce the usual friction around formatting, linting, and type checking, making it easier for teams to adopt reliable quality gates without slowing delivery. It also explains why clean, well-typed code matters even more in AI-assisted development, and outlines a practical adoption path through `pyproject.toml`, local workflows, pre-commit hooks, and CI.

## Repository Contents 📦

| Path                       | Description                                                                  |
| -------------------------- | ---------------------------------------------------------------------------- |
| [`ruff_demo.py`](ruff_demo.py) | A deliberately messy script for demoing formatting and linting with Ruff. |
| [`ty_demo.py`](ty_demo.py)     | A script with intentional type errors for demoing type checking with ty.  |
| [`prompts/`](prompts/)         | Ready-to-use prompts for running the demos with an AI coding agent.       |

## Try It Yourself 🚀

The only requirement is [uv](https://docs.astral.sh/uv/) — `uvx` runs each tool without installing anything else.

1. Lint `ruff_demo.py` and let Ruff auto-fix what it can:

   ```bash
   uvx ruff check --fix ruff_demo.py
   uvx ruff check --fix --unsafe-fixes ruff_demo.py
   ```

2. Format the file with Ruff:

   ```bash
   uvx ruff format ruff_demo.py
   ```

3. Type check `ty_demo.py` with ty:

   ```bash
   uvx ty check ty_demo.py
   ```

Prefer an AI-assisted workflow? The [`prompts/`](prompts/) folder contains the exact prompts used during the talk to have a coding agent run these steps and explain every fix.

## Demo Project: Mini Helpdesk 🎫

The main live demo of the talk is [**pycon-colombia-2026-mini-helpdesk**](https://github.com/lmiguelvargasf/pycon-colombia-2026-mini-helpdesk), a small legacy Django helpdesk application used to show how to introduce Ruff and ty to an existing codebase.

The project ships with everything needed to follow along:

- A `uv`-managed environment with locked dependencies.
- Database migrations and a `seed_tickets` command to load sample tickets.
- A development server and a test suite to verify nothing breaks along the way.

Follow the [setup instructions in its README](https://github.com/lmiguelvargasf/pycon-colombia-2026-mini-helpdesk#setup) to get it running locally.

## Tooling References 🔗

- 🛠️ Astral: [astral.sh](https://astral.sh/)
- ⚡ Ruff: [docs.astral.sh/ruff](https://docs.astral.sh/ruff/)
- ✅ ty: [docs.astral.sh/ty](https://docs.astral.sh/ty/)
- 📦 uv: [docs.astral.sh/uv](https://docs.astral.sh/uv/)

## Agent Skills 🤖

Skills that teach AI coding agents how to use these tools effectively:

- 🧩 Astral skills repository: [astral-sh/claude-code-plugins](https://github.com/astral-sh/claude-code-plugins)
- ⚡ Ruff skill: [skills.sh/astral-sh/claude-code-plugins/ruff](https://skills.sh/astral-sh/claude-code-plugins/ruff)
- ✅ ty skill: [skills.sh/astral-sh/claude-code-plugins/ty](https://skills.sh/astral-sh/claude-code-plugins/ty)
- 📦 uv skill: [skills.sh/astral-sh/claude-code-plugins/uv](https://skills.sh/astral-sh/claude-code-plugins/uv)
