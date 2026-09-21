# Research and inclusion method

[Back to Awesome Jev](../README.md)

## Snapshot and scope

Research date: **September 21, 2026**. The initial discovery pool contained **1,473 repository candidates**. Sources included five existing community catalogs, GitHub repository searches, and web searches for model, inference, and evaluation projects. This produced **1,219 deduplicated related repositories**, including editorially checked runtimes whose relationship is supported by their implementation description rather than the automatic Jev-reference filter.

This is broad discovery, not a claim of completeness. GitHub search result caps, indexing delay, missing READMEs, renames, and private or deleted repositories limit coverage. Search hits were not treated as proof that a project works.

## Collection and review

1. Extract repository addresses from discovery sources; do not import their descriptions as editorial text.
2. Query GitHub for the canonical repository name, public URL, README text, default-branch commit, language, fork/archive status, dates, and detected license.
3. Look for TypeSafe API identifiers or Jev/model references in the README or repository description. Editorial review can also establish a relationship through an explicitly related runtime, such as Laya-MLX, or the documented candidate-scoring implementation. The inspected README paths were `README.md` and `readme.md`; other layouts may be missed.
4. Deduplicate by canonical `owner/repository`, resolving renamed repositories where GitHub supplies a redirect.
5. Remove near-duplicate promotional README repositories, then preserve a commit-pinned README line reference. For metadata-only leads, preserve the repository URL instead.
6. Separate recognized repository licenses, licensing that needs review, and metadata-only leads.
7. Write editorial descriptions for 76 selected starting points. Classify the broader index using repository names, upstream descriptions, and discovery-category hints; generic entries also use the beginning of the README to suggest a category.

**A README reference is evidence of a relationship, not evidence of executed code.** Some entries are tutorials, comparisons, optional integrations, or proposals. This research did not install dependencies, run every application, reproduce benchmarks, audit security, or independently certify model calibration.

## Evidence and license fields

| Field / label | Meaning |
|---|---|
| `readme-reference` | The inspected README contains a related reference, with a pinned source link |
| `repository-metadata` | The repository description suggests relevance; matching README evidence was not found in the inspected paths |
| `recognized-license` | README evidence plus a detected repository license in this catalog's software/public-domain allowlist |
| `license-review` | README evidence exists, but licensing is absent from metadata, custom, unrecognized, or outside the allowlist |
| `metadata-only` | A discovery lead, regardless of what license metadata says |
| `editorial` summary | Written for the selected reading guide |
| `upstream-excerpt` summary | At most 22 words from the repository owner's public description; attributed through the project link |
| `reference-only` summary | No suitable short English description was available; use the primary reference |

The allowlist is MIT, Apache-2.0, AGPL-3.0, GPL-3.0, GPL-2.0, BSD-3-Clause, BSD-2-Clause, LGPL-3.0, Unlicense, and CC0-1.0. CC0 entries can be documentation or directories, not necessarily software implementations. This is a collection rule, not a legal opinion or a comprehensive license taxonomy. `NOASSERTION` and missing metadata do not prove a license is absent.

A code license is separate from the license and availability of pretrained weights, training data, dependencies, and hosted services. We do not call public source code with unclear permissions verified open source.

## Descriptions and claims

The full index retains short upstream descriptions to support discovery. They may contain authors' marketing claims; inclusion does not endorse those claims. Editorial entries avoid treating latency numbers, accuracy percentages, or “calibrated” branding as independently reproduced results.

Categories outside the selected reading guide are provisional. Repository stars are deliberately not used as a quality ranking. Projects with very different hardware, datasets, training exposure, or hosted endpoints should not be ranked by headline numbers.

All catalog prose and field labels are English. Original repository names are retained. When an upstream description is not suitable for an English excerpt, the entry points to its source rather than supplying an unverified translation.

## Reproduce and maintain

The checked-in `data/projects.json` is the publication snapshot, not a live API cache. It contains canonical names, categories, summary provenance, license status, evidence links, and inspected commits; raw downloaded READMEs and account data are not published.

```sh
python3 scripts/validate.py
python3 scripts/render_catalog.py
python3 scripts/render_catalog.py --check
```

The checks run offline. They validate dataset consistency and generated Markdown, not live link availability. The initial source links were obtained from successful public GitHub metadata/README responses on the snapshot date. The workflow runs on repository changes and manual dispatch; it does not claim to perform recurring research.

For updates, re-open the primary repository, record the new inspected commit and license evidence, revise the data, and regenerate the pages. See [CONTRIBUTING.md](../CONTRIBUTING.md).
