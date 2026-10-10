import sys, json, re
t = open(sys.argv[1]).read()
try: t = json.loads(t)['logs_content']
except Exception: pass
lines = [re.sub(r'^\S+Z ', '', l) for l in t.split('\n')]
tags = [re.match(r'^  (PASS|FAIL)  ([^:]+):', l) for l in lines]
tags = [(m.group(1), m.group(2)) for m in tags if m]
dmap = [l.split()[1] for l in open(sys.argv[2]).read().split('\n') if l.strip()]
names = [n for _, n in tags]
for i in range(len(names)):
    if names[i] == dmap[0] and names[i + 1:i + 2] == dmap[1:2] and 'R7-FWD' in names[i:i + 8]:
        blk = tags[i:i + len(dmap)]
        print('guard block:', len(blk), 'checks;', sum(1 for s, _ in blk if s == 'PASS'), 'PASS;',
              [n for s, n in blk if s == 'FAIL'], 'FAIL;', 'map == D' if [n for _, n in blk] == dmap else 'MAP DIFFERS',
              '; next tag after block:', names[i + len(dmap)] if i + len(dmap) < len(names) else None)
        break
