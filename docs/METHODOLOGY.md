# About the list

[Back to Awesome Jev](../README.md)

The directory covers projects using TypeSafe's Jev API, local decision models, inference engines, and related benchmarks. It also includes SDKs, tutorials, and larger projects with an optional Jev integration.

## What belongs here

A project needs a public repository and documentation showing how it relates to Jev or System One decisions. Use the full `owner/repository` name: several unrelated projects are called `openjev`, `jev-mcp`, or `jev-go`.

The main catalog lists repositories with an identified software or public-domain license. Projects with unclear terms go in [License pending](../catalog/license-review.md); entries supported only by a repository description go in [To review](../catalog/metadata-only.md). GitHub's license detection can miss custom terms, so check the project itself before reusing its code. Model weights and datasets may have separate licenses.

Descriptions follow project documentation. Inclusion does not mean the project has been run or its benchmark results reproduced. Categories in the full index are assigned from repository metadata and README content and may need corrections.

## Sources

The September 21, 2026 update started with 1,473 candidate repositories from GitHub searches and community directories. After checking references, resolving renamed repositories, and removing unrelated results and duplicate promotional pages, 1,219 entries remained.

[References](SOURCES.md) lists the search queries and community directories. Each project record includes a repository URL and, where available, a link to the README at a specific commit. This keeps the cited documentation accessible after upstream changes.

## Repository layout

| Path | Contents |
|---|---|
| `data/projects.json` | Full project list, categories, licenses, and source links |
| `data/curated.json` | Projects featured in the README |
| `data/categories.json` | Category names |
| `docs/OVERVIEW.md` | Jev introduction used in the README |
| `catalog/` | Category pages and review lists |
| `scripts/` | Page builder and consistency checks |

The `summary_kind` field distinguishes descriptions written for this list (`editorial`), short upstream descriptions (`upstream-excerpt`), and entries without a description (`reference-only`). `evidence_level` records whether the reference comes from a README or repository metadata. `license_status` determines which catalog page includes the project.

## Updating the catalog

Edit the JSON files, then rebuild the pages:

```sh
python3 scripts/render_catalog.py
python3 scripts/validate.py
python3 scripts/render_catalog.py --check
```

The checks catch duplicate entries, missing local links, inconsistent fields, and stale pages. They run in GitHub Actions on pushes and pull requests. External links and project details need checking against upstream documentation when an entry is updated.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for submission guidelines.
