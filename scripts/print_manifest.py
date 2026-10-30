"""Check freshness before delivering a PDF separately from the website."""
import hashlib
import json
import re


def checked_prints(root):
    manifest_path = root/'textbook/print/manifest.json'
    if not manifest_path.exists(): return {}
    manifest = json.loads(manifest_path.read_text())
    figures = json.loads((root/'textbook/assets/figures/manifest.json').read_text())
    for key, record in manifest.items():
        assert re.fullmatch(r'CH\d\d', key), 'Invalid print chapter ID'
        assert re.fullmatch(r'[A-Za-z0-9.-]+\.pdf', record['file']), 'Invalid print filename'
        source = (root/record['source']).read_text()
        assert re.search(r'^> 版本：'+re.escape(record['version'])+r'$', source,re.M), 'Print version differs: '+key
        path = root/'textbook/print'/record['file']
        data = path.read_bytes()
        assert data.startswith(b'%PDF-') and len(data)==record['bytes'], 'Invalid print PDF: '+key
        assert hashlib.sha256(data).hexdigest()==record['sha256'], 'Print PDF digest differs: '+key
        chapter_figures = [f for f in figures if f['id'].startswith('AG-'+key[2:]+'-')]
        digest = hashlib.sha256(json.dumps(chapter_figures,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
        assert digest==record['figureMetadataSha256'], 'Print figure metadata changed; rebuild '+key
        for relative, expected in record['inputs'].items():
            target = (root/relative).resolve()
            assert target.is_relative_to(root.resolve()), 'Invalid print input path'
            assert hashlib.sha256(target.read_bytes()).hexdigest()==expected, 'Print is stale; rebuild after changing '+relative
        assert isinstance(record['pages'],int) and record['pages']>0
    return manifest


if __name__ == "__main__":
    from pathlib import Path
    records = checked_prints(Path(__file__).resolve().parents[1])
    print("PASS: " + ", ".join(records) + " print sources and PDF digests")
