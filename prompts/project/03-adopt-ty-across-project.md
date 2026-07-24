Adopt ty across the whole project and finish with zero diagnostics.

Work autonomously; do not pause for a plan or approval.

1. Run `uvx ty check` from the repository root and record the project-wide
   baseline count.

2. Add ty as a uv development dependency.

3. Configure ty to check the whole project, excluding only generated Django
   migrations.

4. Fix every reported diagnostic. Correct annotations, handle optional values,
   declare Django's default manager explicitly where needed, and make
   heterogeneous seed-data conversions precise. Preserve intended behavior.

5. Add exactly one regression test proving that a missing assignee is handled
   safely.

6. Do not use ignore comments, replace imports with Any, exclude application
   files, or add a different type checker.

7. Finish by running Ruff, ty, and the Django tests. Fix failures and rerun
   until all three pass.

Return at most five lines: project-wide ty before/after, tests before/after,
the correctness issues fixed, and files changed.
