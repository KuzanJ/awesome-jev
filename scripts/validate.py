#!/usr/bin/env python3
"""Check project records and documentation links."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_LICENSES = {'MIT', 'Apache-2.0', 'AGPL-3.0', 'GPL-3.0', 'GPL-2.0', 'BSD-3-Clause', 'BSD-2-Clause', 'LGPL-3.0', 'Unlicense', 'CC0-1.0'}

def main():
    projects = json.loads((ROOT / 'data/projects.json').read_text())
    categories = json.loads((ROOT / 'data/categories.json').read_text())
    curated = json.loads((ROOT / 'data/curated.json').read_text())
    assert projects, 'Empty catalog'
    names = [p['repository'].lower() for p in projects]
    assert len(names) == len(set(names)), 'Duplicate canonical repository'
    by_name = {p['repository'].lower(): p for p in projects}
    for p in projects:
        name = p['repository']
        assert re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', name), name
        assert p['url'] == 'https://github.com/' + name, name
        assert p['category'] in categories, name
        assert p['category_label'] == categories[p['category']], name
        assert p['summary_kind'] in {'editorial', 'upstream-excerpt', 'reference-only'}, name
        assert not re.search(r'[\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af\u0400-\u052f\u0590-\u08ff]', p['summary']), name
        assert p['evidence_level'] in {'readme-reference', 'repository-metadata'}, name
        assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', p['checked_on']), name
        if p['evidence_level'] == 'readme-reference':
            assert re.fullmatch(r'[0-9a-f]{40}', p['commit'] or ''), name
            assert p['evidence_url'].startswith(p['url'] + '/blob/' + p['commit'] + '/'), name
            assert re.search(r'/[Rr][Ee][Aa][Dd][Mm][Ee]\.md#L[1-9][0-9]*$', p['evidence_url']), name
        else:
            assert p['license_status'] == 'metadata-only', name
        if p['license_status'] == 'recognized-license':
            assert p['license'] in ALLOWED_LICENSES and p['evidence_level'] == 'readme-reference', name
        if p['summary_kind'] == 'upstream-excerpt':
            assert len(p['summary'].removesuffix(' ...').split()) <= 22, name
    curated_names = [c['slug'].lower() for c in curated]
    assert len(curated_names) == len(set(curated_names)), 'Duplicate curated entry'
    for c in curated:
        assert c['slug'].lower() in by_name, c['slug']
        p = by_name[c['slug'].lower()]
        assert p['curated'] and p['summary'] == c['summary'], c['slug']
        assert p['license_status'] == 'recognized-license', c['slug']
    assert sum(p['curated'] for p in projects) == len(curated)
    # Check relative file links and local heading anchors in Markdown.
    for path in ROOT.rglob('*.md'):
        content = path.read_text()
        for target in re.findall(r'\]\(([^\s)]+)\)', content):
            if urlparse(target).scheme or target.startswith('//'): continue
            relative, _, anchor = unquote(target).partition('#')
            destination = (path.parent / relative).resolve() if relative else path
            assert destination.exists(), f'{path}: missing {target}'
            if anchor and destination.suffix == '.md':
                headings = re.findall(r'^#{1,6}\s+(.+)$', destination.read_text(), re.M)
                slugs = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
                assert anchor in slugs, f'{path}: missing anchor {target}'
    print(f'Validated {len(projects)} unique repositories, {len(curated)} curated entries, evidence links, English summaries, and local Markdown links.')

if __name__ == '__main__':
    main()
