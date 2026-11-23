from pathlib import Path
import csv, re, sys
P=Path(__file__).resolve().parent
sl=(P/'index.html').read_text(encoding='utf-8')
ids={f'S{i:02d}' for i in range(1,6)}
assert len(re.findall(r'<section class="slide',sl))==14, 'Must have 14 slides'
assert all((P/'ingest'/p).exists() for p in ['S01_ibm.md','S02_openai.md','S03_nist.md','S04_google-cloud.md','S05_anthropic.md'])
assert len(list((P/'wiki'/'concepts').glob('*.md')))==5
assert len(list((P/'wiki'/'sources').glob('*.md')))==5
with (P/'docs'/'source-mapping.csv').open(encoding='utf-8',newline='') as file:
    rows=list(csv.DictReader(file))
for row in rows:
    assert (P/row['wiki_page']).exists(), f'Missing wiki: {row}'
    assert set(row['source_ids'].split(';'))<=ids
for sid in ids: assert f'{sid} ↗' in sl, f'Missing citation {sid}'
for p in ['index.html','wiki.html','workflow.html','README.md','docs/workflow.md','docs/prompts.md','docs/verification-log.md']:
    assert (P/p).exists(),f'Missing {p}'
for token in ['id="prev"','id="next"','class="quiz-option"','id="pagecount"','ArrowRight','ArrowLeft']:
    assert token in sl,f'Missing UI element {token}'
print('PASS: 14 slides; 5 source notes; 5 source pages; 5 concept pages; source-to-slide links; controls; supporting documents.')
print('Note: Static check only. Complete real LLM Wiki ingest, browser tests and GitHub Pages publication separately.')
