#!/usr/bin/env python3
"""Render the English catalog from the checked-in, dated evidence snapshot."""
import argparse
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def esc(value):
    return str(value or 'Not detected').replace('|', '\\|').replace('\n', ' ').replace('<', '&lt;').replace('>', '&gt;')

def generate():
    projects = json.loads((ROOT / 'data/projects.json').read_text())
    categories = json.loads((ROOT / 'data/categories.json').read_text())
    curated = json.loads((ROOT / 'data/curated.json').read_text())
    by_name = {p['repository'].lower(): p for p in projects}
    status = collections.Counter(p['license_status'] for p in projects)
    files = {}
    index = ['# Complete project index', '', 'Snapshot: **2026-09-21**. This is a discovery index, not a ranking or a runtime certification.', '',
             'Repository summaries are short upstream excerpts unless marked editorial in the JSON. Each evidence link points to the inspected README revision. Category assignments outside the curated selection are heuristic; a README reference can indicate an optional integration or related research.', '',
             '| Category | README evidence and recognized license |', '|---|---:|']
    for key, label in categories.items():
        rows = [p for p in projects if p['category'] == key and p['license_status'] == 'recognized-license']
        index.append(f'| [{label}]({key}.md) | {len(rows)} |')
        lines = [f'# {label}', '', '[All categories](README.md) · [Curated selection](../README.md)', '',
                 'Snapshot: **2026-09-21**. A detected repository license does not establish the license of model weights, datasets, or dependencies. These repositories contain a relevant README reference; this does not establish a working implementation. Summaries without a curated entry are shortened upstream descriptions, not independently verified claims.', '',
                 '| Repository | Scope / upstream summary | Language | Repository license | Evidence |', '|---|---|---|---|---|']
        for p in rows:
            state = ' [archived]' if p['archived'] else ''
            state += ' [fork]' if p['fork'] else ''
            lines.append(f"| [{p['repository']}]({p['url']}){state} | {esc(p['summary'])} | {esc(p['language'])} | {esc(p['license'])} | [README]({p['evidence_url']}) |")
        files[f'catalog/{key}.md'] = '\n'.join(lines) + '\n'
    index += ['', f"**{status['recognized-license']} repositories** appear in the category pages above.", '',
              f"- [License review](license-review.md): **{status['license-review']}** related repositories with README evidence whose license was absent, custom, not automatically recognized, or outside this catalog's software/public-domain allowlist.",
              f"- [Metadata-only leads](metadata-only.md): **{status['metadata-only']}** related descriptions without a matching README reference in the inspected paths.",
              '', 'These appendices are discovery leads and are **not counted as verified open-source implementations**.', '',
              '[Machine-readable snapshot](../data/projects.json) · [Research method](../docs/METHODOLOGY.md) · [Discovery sources](../docs/SOURCES.md)']
    files['catalog/README.md'] = '\n'.join(index) + '\n'
    for kind,title,notice in [('license-review','License review','Do not infer permission to reuse code from public visibility. Inspect upstream licensing before reuse.'),('metadata-only','Metadata-only discovery leads','These repositories were not promoted to the README-evidence index. Their descriptions suggest relevance, but implementation evidence needs further inspection.')]:
        lines=[f'# {title}', '', '[Complete index](README.md)', '', notice, '',
               'Snapshot: **2026-09-21**. Descriptions below are shortened upstream excerpts unless editorially reviewed. Missing detection does not prove a license is absent.', '',
               '| Repository | Provisional category | Scope / upstream summary | License detected | Reference |', '|---|---|---|---|---|']
        for p in projects:
            if p['license_status'] != kind: continue
            lines.append(f"| [{p['repository']}]({p['url']}) | {p['category_label']} | {esc(p['summary'])} | {esc(p['license'])} | [Source]({p['evidence_url']}) |")
        files[f'catalog/{kind}.md']='\n'.join(lines)+'\n'
    intro=(ROOT/'docs/OVERVIEW.md').read_text().rstrip()
    readme=['# Awesome Jev', '', 'An English guide to TypeSafe Jev, independent decision-model implementations, and the software built around them.', '',
            f"**Snapshot: September 21, 2026 · {len(curated)} curated starting points · {len(projects):,} deduplicated related repositories**", '',
            f"The complete index separates **{status['recognized-license']} repositories with README evidence and a recognized license**, **{status['license-review']} license-review entries**, and **{status['metadata-only']} metadata-only leads**. The wider index is systematically collected; the curated selection below receives closer editorial attention. Neither count is a claim that every project has been executed or audited.", '',
            '**[Browse the complete index](catalog/README.md)** · [Model comparison](docs/MODELS.md) · [Research method](docs/METHODOLOGY.md) · [Contribute](CONTRIBUTING.md)', '', intro, '', '## Curated starting points', '',
            'Each row links to its project and a pinned primary-source reference. Licenses shown are for the repository, not automatically for its weights or data. Order groups related approaches; it does not rank quality.', '']
    groups=list(dict.fromkeys(c['group'] for c in curated))
    for g in groups:
        anchor=re.sub(r'[^a-z0-9 -]','',g.lower()).replace(' ','-')
        readme.append(f'- [{g}](#{anchor})')
    for g in groups:
        readme += ['', f'### {g}', '', '| Project | What to inspect | Code license | Evidence |', '|---|---|---|---|']
        for c in curated:
            if c['group'] != g: continue
            p=by_name[c['slug'].lower()]
            readme.append(f"| [{c['title']}]({p['url']}) | {c['summary']} | {esc(p['license'])} | [Source]({p['evidence_url']}) |")
    readme += ['', '## More projects', '',
               'The [complete index](catalog/README.md) adds community SDKs, agent plugins, security and moderation tools, document workflows, browser agents, games, robotics, productivity applications, and finance experiments. Full repository names disambiguate unrelated projects that share names such as `openjev`, `jev-mcp`, and `jev-go`.', '',
               '## Scope and maintenance', '',
               'Independent and unaffiliated with TypeSafe AI. Jev itself is a hosted proprietary model; a public client is not an open model. Independent implementations reproduce interfaces or behavior to varying degrees, not a disclosed TypeSafe training recipe.', '',
               'This is a dated research snapshot, not an exhaustive registry. Project state, naming, compatibility, and licensing can change. See the [methodology](docs/METHODOLOGY.md), [source acknowledgments](docs/SOURCES.md), and [contribution policy](CONTRIBUTING.md). Descriptions report upstream scope; performance and calibration claims require task-specific evaluation.', '',
               'Editorial content and maintenance scripts are available under the [MIT license](LICENSE). Linked projects and attributed upstream excerpts retain their respective authorship and licensing.']
    files['README.md']='\n'.join(readme)+'\n'
    return files

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    stale=[]
    for name,content in generate().items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text()!=content:stale.append(name)
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content)
    if stale:raise SystemExit('Stale generated files: '+', '.join(stale))
    print('Catalog is consistent.' if args.check else 'Rendered README and catalog pages.')
if __name__=='__main__':main()
