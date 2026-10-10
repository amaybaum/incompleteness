import json, re, sys
raw = open(sys.argv[1], encoding='utf-8').read()
try:
    d = json.loads(raw); s = d.get('logs_content') or raw
except Exception:
    s = raw
lines = s.split('\n')
mod = sys.argv[2] if len(sys.argv) > 2 else 'K2Guard'
pr = [l for l in lines if mod + '.lean' in l and 'depends on axioms' in l]
print('prints', len(pr), 'all standard', all('[propext, Classical.choice, Quot.sound]' in l for l in pr))
for l in pr:
    m = re.search(r"'([^']+)' depends on axioms: (\[.*\])", l)
    if m and m.group(2) != '[propext, Classical.choice, Quot.sound]':
        print('  NONSTANDARD', m.group(1), m.group(2))
for l in lines:
    if re.search(r'lean-axioms|lean-manuscript |legacy-records|v3-receipts|release gate:|Build completed|error:', l):
        print('>>', l[:170])
print('module warnings', sum(('warning:' in l and mod + '.lean' in l) for l in lines))
for l in lines:
    if 'warning:' in l and mod + '.lean' in l:
        print('  W', l[:200])
