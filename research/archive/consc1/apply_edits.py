import json, re, sys
ROOT, NOTE, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
FULL = 'book/The-Incompleteness-of-Observation-FULL.md'
CH = {'B1': 'book/ch01-observation.md', 'B2': 'book/ch01-observation.md', 'B3': 'book/ch01-observation.md',
      'B4': 'book/ch03-structural-realism.md', 'B5': 'book/ch03-structural-realism.md',
      'B6': 'book/ch03-structural-realism.md', 'B7': 'book/ch03-structural-realism.md',
      'B8': 'book/ch18-beyond.md', 'B9': 'book/glossary.md', 'P1': 'papers/Main.md', 'P2': 'papers/Main.md'}
sec = open(NOTE, encoding='utf-8').read().split('## 7. COBS-6')[1].split('## 8.')[0]
blocks = re.split(r'\n\*\*(B\d|P\d) — ', sec)[1:]
edits = []
for k, body in zip(blocks[0::2], blocks[1::2]):
    for o, n1, n2 in re.findall(r'old: `(.+?)`(?:\s*→\s*new: `(.+?)`|\s*\n\s*(?:- )?\s*new: `(.+?)`)', body):
        edits.append({'id': k, 'old': o, 'new': n1 or n2})
inst = []
for i, e in enumerate(edits):
    files = [CH[e['id']]] + ([FULL] if e['id'].startswith('B') else [])
    for f in files:
        inst.append({'item': e['id'], 'file': f, 'old': e['old'], 'new': e['new']})
for x in inst:
    p = f"{ROOT}/{x['file']}"
    t = open(p, encoding='utf-8').read()
    assert t.count(x['old']) == 1 and t.count(x['new']) == 0, (x['item'], x['file'])
    open(p, 'w', encoding='utf-8').write(t.replace(x['old'], x['new'], 1))
json.dump(inst, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(edits), 'pairs ->', len(inst), 'instances applied')
