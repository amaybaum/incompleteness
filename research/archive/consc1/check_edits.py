"""Mechanical check of the CONSC-1 proposed change set against the tree at L.

For each edit: the old string occurs exactly once in the chapter source and exactly once in FULL.md (or exactly once
in the paper); applying old -> new changes nothing else. Read-only: works on in-memory copies."""
import re, sys

ROOT = sys.argv[1]
NOTE = sys.argv[2]
FULL = 'book/The-Incompleteness-of-Observation-FULL.md'
CH = {'B1': 'book/ch01-observation.md', 'B2': 'book/ch01-observation.md', 'B3': 'book/ch01-observation.md',
      'B4': 'book/ch03-structural-realism.md', 'B5': 'book/ch03-structural-realism.md',
      'B6': 'book/ch03-structural-realism.md', 'B7': 'book/ch03-structural-realism.md',
      'B8': 'book/ch18-beyond.md', 'B9': 'book/glossary.md', 'P1': 'papers/Main.md', 'P2': 'papers/Main.md'}

text = open(NOTE, encoding='utf-8').read()
sec = text.split('## 7. COBS-6')[1].split('## 8.')[0]
blocks = re.split(r'\n\*\*(B\d|P\d) — ', sec)[1:]
edits = []
for k, body in zip(blocks[0::2], blocks[1::2]):
    pairs = re.findall(r'old: `(.+?)`(?:\s*→\s*new: `(.+?)`|\s*\n\s*(?:- )?\s*new: `(.+?)`)', body)
    for o, n1, n2 in pairs:
        edits.append((k, o, n1 or n2))

files = {}
def get(p):
    if p not in files:
        files[p] = open(f'{ROOT}/{p}', encoding='utf-8').read()
    return files[p]

bad = 0
orig = {}
for k, o, n in edits:
    targets = [CH[k]] + ([FULL] if k.startswith('B') else [])
    for p in targets:
        t = get(p)
        orig.setdefault(p, t)
        c = t.count(o)
        if c != 1:
            print(f'FAIL {k} {p}: old occurs {c} times: {o[:70]}')
            bad += 1
            continue
        files[p] = t.replace(o, n, 1)
print(f'{len(edits)} edit pairs parsed; {sum(1 for k,_,_ in edits if k.startswith("B"))} book pairs applied to chapter and FULL')
for p, t in files.items():
    if p in orig:
        print(f'  {p}: {len(orig[p])} -> {len(t)} chars')
# chapter/FULL parity: every new string present once in both sides
for k, o, n in edits:
    if k.startswith('B'):
        a, b = files[CH[k]].count(n), files[FULL].count(n)
        if (a, b) != (1, 1):
            print(f'FAIL parity {k}: new in chapter {a}, in FULL {b}')
            bad += 1
print('check_edits: OK' if bad == 0 else f'check_edits: {bad} FAILURES')
sys.exit(1 if bad else 0)
