"""Fill the CONSC-2 preregistration template. argv: controls_blob predicted_section_file out_file"""
import json, sys
SP = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad'
FULL = 'book/The-Incompleteness-of-Observation-FULL.md'
inst = json.load(open(SP + '/consc1/edits.json', encoding='utf-8'))
pairs, seen = [], set()
for x in inst:
    k = (x['item'], x['old'])
    if k in seen:
        continue
    seen.add(k)
    files = [y['file'] for y in inst if (y['item'], y['old']) == k]
    pairs.append((x['item'], files, x['old'], x['new']))
out = []
for n, (item, files, old, new) in enumerate(pairs, 1):
    where = ' and '.join(f'`{f}`' for f in files)
    out.append(f'**{item}.{sum(1 for p in pairs[:n] if p[0] == item)}** — {where}\n\nold:\n\n```text\n{old}\n```\n\nnew:\n\n```text\n{new}\n```\n')
table = '\n'.join(out)
src = open(SP + '/consc1/controls_consc2.py', encoding='utf-8').read()
reg = json.loads(src.split("REGREP = json.loads(r'''")[1].split("''')")[0])
rows = '\n'.join(f'| {p} | {d} | {e} |' for p, (d, e) in reg.items())
t = open(SP + '/consc1/consc2-preregistration.template.md', encoding='utf-8').read()
t = (t.replace('@@TABLE@@', table).replace('@@REGREP@@', rows).replace('@@CONTROLS_BLOB@@', sys.argv[1])
      .replace('@@PREDICTED@@', open(sys.argv[2], encoding='utf-8').read().rstrip('\n')))
assert '@@' not in t
open(sys.argv[3], 'w', encoding='utf-8').write(t)
print(len(pairs), 'pairs,', len(inst), 'instances')
