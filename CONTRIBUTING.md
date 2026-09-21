# Contributing

Found a useful Jev project? Send a pull request or [open an issue](https://github.com/KuzanJ/awesome-jev/issues). Corrections and broken-link reports are welcome too.

## Adding a project

- Check the list for duplicates and renamed repositories.
- Use the full repository URL and a short English description of what the project does.
- Link to the relevant README or implementation, preferably at a specific commit.
- State whether it calls the hosted Jev API or runs an independent model locally.
- Check the repository license. Keep model and dataset terms separate; use `license-review` when the code license is unclear.
- Keep performance claims out of the description unless they are necessary to explain the project and link to a reproducible comparison.

Add the entry to `data/projects.json` and choose a category from `data/categories.json`. Projects awaiting a README check belong in `metadata-only`. For a README addition, also update `data/curated.json`.

Then run:

```sh
python3 scripts/render_catalog.py
python3 scripts/validate.py
python3 scripts/render_catalog.py --check
```

Please edit the data files rather than the generated tables. The introduction lives in `docs/OVERVIEW.md`.

## Keeping the list useful

Small experiments and negative results are welcome. Archived projects and forks should be marked. Distinguish an interface implementation from released model weights, and a task-specific benchmark from a general capability claim.

Leave out unrelated uses of the acronym JEV, duplicate promotional pages, and projects with no relevant documentation. If a category or description is wrong, a small correction is enough—there is no need to rewrite the whole entry.
