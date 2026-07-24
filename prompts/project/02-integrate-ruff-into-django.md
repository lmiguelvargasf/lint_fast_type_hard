Integrate Ruff into this existing Django project now.

Work autonomously and do not stop for a plan or approval:

1. Run Ruff as a one-off check first and record the baseline statistics.
2. Add Ruff as a pinned uv development dependency.
3. Configure Ruff in pyproject.toml with:
   - migrations excluded
   - lint rules E4, E7, E9, F, I, B, UP, and SIM
4. Apply only safe automatic fixes.
5. Manually fix the remaining configured findings when behavior is
   unambiguous.
6. Do not use unsafe fixes, noqa comments, or repository-wide formatting.
7. Do not add ty yet.
8. Run Ruff and the existing Django tests until both pass.

Preserve the UI and application behavior. Return only the Ruff before/after
count, test result, and changed files.
