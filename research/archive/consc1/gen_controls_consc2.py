"""Fill controls_consc2.py.template from the predicted tree (run from inside the repository)."""
import json, subprocess, sys
SP = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad'
D = '1a5752d07057895dfa7d793d11a197691bf27a0d'
PRED = sys.argv[1]          # a commit carrying the predicted execution files
inst = json.load(open(SP + '/consc1/edits.json', encoding='utf-8'))
SOURCES = ['papers/Main.md', 'papers/GR.md', 'papers/Structure.md', 'book/ch01-observation.md',
           'book/ch03-structural-realism.md', 'book/ch18-beyond.md', 'book/glossary.md',
           'book/The-Incompleteness-of-Observation-FULL.md']
TEX = ['papers/Main.tex', 'papers/GR.tex', 'papers/Structure.tex', 'book/The-Incompleteness-of-Observation-FULL.tex']
rp = lambda c, p: subprocess.run(['git', 'rev-parse', f'{c}:{p}'], capture_output=True, text=True).stdout.strip()
src = {p: rp(PRED, p) for p in SOURCES}
tex = {p: rp(PRED, p) for p in TEX}
PH = ['a doubting *I*', 'empirical fact that observation occurs', 'foundational empirical commitment',
      'is an open question — one that bears on how the framework describes the minimality',
      'nothing it is like to be the cosmological horizon', 'consciousness as structural necessary condition',
      'is not speculative addition to an empirical base', 'who is a substructure of the system they are trying to describe',
      'The axiom thus commits', 'without its thinking subject', 'nothing in the definition requires',
      'C1–C4 selection condition', 'two-axiom', 'two axioms', 'Seven items', 'posit ledger', 'third axiom', 'cogito']
def corpus(c):
    names = [n for n in subprocess.run(['git', 'ls-tree', '-r', '--name-only', c, 'papers', 'book'],
             capture_output=True, text=True).stdout.split() if n.endswith('.md') and n.count('/') == 1]
    return {n: subprocess.run(['git', 'show', f'{c}:{n}'], capture_output=True).stdout.decode() for n in names}
cd, ce = corpus(D), corpus(PRED)
reg = {p: [sum(t.count(p) for t in cd.values()), sum(t.count(p) for t in ce.values())] for p in PH}
t = open(SP + '/consc1/controls_consc2.py.template', encoding='utf-8').read()
t = (t.replace('@@D@@', D).replace('@@INSTANCES@@', json.dumps(inst, ensure_ascii=False, indent=1))
      .replace('@@SOURCE_BLOBS@@', json.dumps(src, indent=1)).replace('@@TEX_BLOBS@@', json.dumps(tex, indent=1))
      .replace('@@REGREP@@', json.dumps(reg, ensure_ascii=False, indent=1)))
assert '@@' not in t
open(SP + '/consc1/controls_consc2.py', 'w', encoding='utf-8').write(t)
for p, v in reg.items():
    print(f'{v[0]:4d} {v[1]:4d}  {p}')
