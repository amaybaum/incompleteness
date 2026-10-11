"""Count '#print axioms' results per module in a saved job log, joining wrapped lines.
Usage: python3 -I -B count_prints.py <saved-log> <module> [<module> ...]
"""
import re, sys, json
path = sys.argv[1]; mods = sys.argv[2:]
raw = open(path, encoding='utf-8', errors='replace').read()
if raw.lstrip().startswith('{'):
    try:
        raw = json.loads(raw)['logs_content']
    except Exception:
        raw = raw.replace('\\n', '\n')
elif raw.count('\n') < 50 and '\\n' in raw:
    raw = raw.replace('\\n', '\n')
lines = [re.sub(r'^\S*\d{4}-\d{2}-\d{2}T[\d:.]+Z\s?', '', ln) for ln in raw.split('\n')]
text = '\n'.join(lines)
# join wrapped prints: a print result is "'<name>' depends on axioms: [<list>]" possibly broken by newlines
pat = re.compile(r"'([^']+)'\s+depends\s+on\s+axioms:\s*\[([^\]]*)\]", re.S)
found = pat.findall(text)
print('total prints found (joined):', len(found))
for mod in mods:
    rows = [(n, re.sub(r'\s+', ' ', a).strip()) for n, a in found if n.startswith(f'OIBridge.{mod}.') or n.startswith(f'{mod}.') or f'.{mod}.' in n]
    std = [r for r in rows if r[1] == 'propext, Classical.choice, Quot.sound']
    other = [r for r in rows if r[1] != 'propext, Classical.choice, Quot.sound']
    print(f'MODULE {mod}: prints={len(rows)} standard={len(std)} other={len(other)}')
    for n, a in other:
        print('   OTHER', n, '[', a, ']')
    wrapped = [n for n, a in found if (n.startswith(f'OIBridge.{mod}.') or f'.{mod}.' in n)]
# also report which print names carry no module prefix (to catch prints printed without namespace)
nopfx = [n for n, a in found if '.' not in n]
print('prints without namespace prefix:', len(nopfx), nopfx[:20])
# wrapped-line detection: count raw lines containing 'depends on axioms' vs joined count
rawcount = sum(1 for ln in lines if 'depends on axioms' in ln)
print('raw lines with "depends on axioms":', rawcount, ' (joined total above; difference = wrapped-name prints)')
# a print whose axiom list continues on the next line: raw lines with 'depends on axioms' but no closing bracket
openl = [ln for ln in lines if 'depends on axioms' in ln and ']' not in ln]
print('raw print lines without closing bracket (wrapped lists):', len(openl))
for ln in openl: print('   WRAPPED', ln[:200])
