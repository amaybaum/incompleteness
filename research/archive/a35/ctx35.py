import sys, re
t = open(sys.argv[1], encoding='utf-8', errors='replace').read().replace('\\n', '\n').replace('\\u001b', '').replace('\\"', '"')
t = re.sub(r'\d{4}-\d\d-\d\dT[\d:.]+Z ', '', t)
lines = t.split('\n')
want = set(int(x) for x in sys.argv[2].split(',')) if len(sys.argv) > 2 else None
n = int(sys.argv[3]) if len(sys.argv) > 3 else 30
seen = set()
for i, l in enumerate(lines):
    m = re.match(r'error: OIBridge/DitaHull\.lean:(\d+):(\d+):', l)
    if not m: continue
    ln = int(m.group(1))
    if ln in seen or (want and ln not in want): continue
    seen.add(ln)
    print('=' * 20, ln)
    for k in range(i, min(i + n, len(lines))):
        if k > i and re.match(r'(error|warning|info): OIBridge', lines[k]): break
        print(lines[k][:230])
