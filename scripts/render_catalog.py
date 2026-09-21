#!/usr/bin/env python3
"""Build the README and category pages from the project list."""
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
    index = ['# Complete project index', '', 'Last updated: **September 21, 2026**.', '',
             'Browse by category below. Descriptions come from project documentation; README links point to the versions used for this list. Some projects include Jev as an optional integration.', '',
             '| Category | Projects |', '|---|---:|']
    for key, label in categories.items():
        rows = [p for p in projects if p['category'] == key and p['license_status'] == 'recognized-license']
        index.append(f'| [{label}]({key}.md) | {len(rows)} |')
        lines = [f'# {label}', '', '[All categories](README.md) · [Curated selection](../README.md)', '',
                 'Last updated: **September 21, 2026**. Descriptions follow upstream documentation. The license column covers the repository; weights and datasets may have separate terms.', '',
                 '| Project | Description | Language | License | README |', '|---|---|---|---|---|']
        for p in rows:
            state = ' [archived]' if p['archived'] else ''
            state += ' [fork]' if p['fork'] else ''
            lines.append(f"| [{p['repository']}]({p['url']}){state} | {esc(p['summary']) if p['summary_kind'] != 'reference-only' else '—'} | {esc(p['language'])} | {esc(p['license'])} | [README]({p['evidence_url']}) |")
        files[f'catalog/{key}.md'] = '\n'.join(lines) + '\n'
    index += ['', f"**{status['recognized-license']} repositories** appear in the category pages above.", '',
              f"- [License pending](license-review.md): {status['license-review']} projects requiring a closer look at their license.",
              f"- [To review](metadata-only.md): {status['metadata-only']} projects awaiting README confirmation.",
              '', 'Entries in these two lists are kept separate from the licensed catalog.', '',
              '[JSON index](../data/projects.json) · [About the list](../docs/METHODOLOGY.md) · [References](../docs/SOURCES.md)']
    files['catalog/README.md'] = '\n'.join(index) + '\n'
    for kind,title,notice in [('license-review','License pending','These projects have relevant documentation, but their repository license needs checking. They are not included in the licensed catalog.'),('metadata-only','To review','These projects mention Jev in their repository description. Their README or implementation still needs checking before they can join the main catalog.')]:
        lines=[f'# {title}', '', '[Complete index](README.md)', '', notice, '',
               'Last updated: **September 21, 2026**. An unknown license means it was not identified in GitHub metadata; the repository may contain additional terms.', '',
               '| Project | Category | Description | License | Source |', '|---|---|---|---|---|']
        for p in projects:
            if p['license_status'] != kind: continue
            lines.append(f"| [{p['repository']}]({p['url']}) | {p['category_label']} | {esc(p['summary']) if p['summary_kind'] != 'reference-only' else '—'} | {esc(p['license'])} | [Source]({p['evidence_url']}) |")
        files[f'catalog/{kind}.md']='\n'.join(lines)+'\n'
    intro=(ROOT/'docs/OVERVIEW.md').read_text().rstrip()
    readme=['# Awesome Jev', '', 'Open models, libraries, tools, and applications for [Jev](https://typesafe.ai/) and System One decisions.', '',
            f"**{len(curated)} featured projects · {len(projects):,} repositories indexed · Updated September 21, 2026**", '',
            f"Start with the projects below, or browse **{status['recognized-license']} licensed repositories** in the full catalog. Projects with unclear licensing and those awaiting review are listed separately.", '',
            '**[Browse all projects](catalog/README.md)** · [Compare implementations](docs/MODELS.md) · [References](docs/SOURCES.md) · [Contribute](CONTRIBUTING.md)', '', intro, '', '## Featured projects', '',
            'Grouped by what they build. Source links point to project documentation; licenses cover code unless noted otherwise.', '']
    groups=list(dict.fromkeys(c['group'] for c in curated))
    for g in groups:
        anchor=re.sub(r'[^a-z0-9 -]','',g.lower()).replace(' ','-')
        readme.append(f'- [{g}](#{anchor})')
    for g in groups:
        readme += ['', f'### {g}', '', '| Project | Description | License | Source |', '|---|---|---|---|']
        for c in curated:
            if c['group'] != g: continue
            p=by_name[c['slug'].lower()]
            readme.append(f"| [{c['title']}]({p['url']}) | {c['summary']} | {esc(p['license'])} | [Source]({p['evidence_url']}) |")
    readme += ['', '## More projects', '',
               'The [complete index](catalog/README.md) adds community SDKs, agent plugins, security and moderation tools, document workflows, browser agents, games, robotics, productivity applications, and finance experiments. Full repository names disambiguate unrelated projects that share names such as `openjev`, `jev-mcp`, and `jev-go`.', '',
               '## About this list', '',
               'This is a community list, unaffiliated with TypeSafe AI. It includes both applications using the hosted Jev API and independent models that run locally.', '',
               'Found a useful project or a broken link? [Open an issue](https://github.com/KuzanJ/awesome-jev/issues) or send a pull request. See [how the list is maintained](docs/METHODOLOGY.md) and the [contribution guide](CONTRIBUTING.md).', '', 'Thanks to the project authors and the [community lists](docs/SOURCES.md) that helped make this directory possible.', '',
               '[MIT](LICENSE). Linked projects retain their own licenses.']
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
