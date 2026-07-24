1. Run the existing Django test suite and report how many tests pass.

2. From the repository root, run this exact command once:

```bash
npx --yes skills add https://github.com/astral-sh/claude-code-plugins --skill ruff ty --agent cursor --yes
```

3. Verify that `ruff` and `ty` were installed project-locally from `astral-sh/claude-code-plugins`, and that the only repository additions are:

```text
.agents/skills/ruff/SKILL.md
.agents/skills/ty/SKILL.md
skills-lock.json
```

Do not change any existing repository files, install Ruff or ty as Python dependencies, or run either tool.

Finish by telling me to reload Cursor and open a new Agent chat so the skills can be discovered.
