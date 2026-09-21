# Contributing

Please keep contributions in English and link to primary evidence.

## Add or update a project

1. Check `data/projects.json` for the canonical `owner/repository`, including old names and redirects.
2. Confirm the relationship to TypeSafe Jev, an independent decision implementation, or directly related research.
3. Link to a README or relevant implementation at an inspected commit. Do not submit a product name with no source.
4. Identify the repository license separately from weight and dataset licensing. If it is unclear, use `license-review`.
5. Write a factual, concise description. Say what decision is made or what artifact is released. Avoid unqualified “zero hallucination,” “fully calibrated,” and “beats every model” claims.
6. Choose a category and set the evidence and summary-provenance fields. Explain optional integrations and specialist training where relevant.
7. Regenerate and validate:

```sh
python3 scripts/render_catalog.py
python3 scripts/validate.py
python3 scripts/render_catalog.py --check
```

The README contains an editorial selection, not every submission. Update `data/curated.json` only when the project adds a useful reading path and its description has been checked. `docs/OVERVIEW.md` supplies the explanatory portion of the generated README.

## Inclusion boundaries

- Public repositories with concrete Jev references can enter the discovery index.
- A hosted-API application is not an open model. State the dependency accurately.
- Independent implementations must not be presented as TypeSafe's released architecture or weights.
- Public repositories without a detected reusable license belong in the licensing-review appendix.
- Metadata-only leads stay separate until primary evidence is found.
- Duplicated names are acceptable; duplicated canonical repositories are not.
- Archived projects, forks, research failures, and negative benchmark results may be useful when clearly identified.
- Spam, unrelated acronyms, unsupported affiliation claims, and links without a relevant artifact do not belong.

Please report broken links, wrong categories, renamed repositories, licensing corrections, and overstated summaries through an issue or pull request.
