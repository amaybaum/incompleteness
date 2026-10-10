import re, datetime, sys
t = open(sys.argv[1], encoding='utf-8').read()
lines = t.split('\\n') if '\\n' in t else t.split('\n')
def ts(l):
    m = re.match(r'(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)\.(\d+)Z', l)
    return datetime.datetime.strptime(m.group(1), '%Y-%m-%dT%H:%M:%S').timestamp() + float('0.' + m.group(2)) if m else None
marks = [(ts(l), l[l.index('==='):].strip()) for l in lines if '=== ' in l and '_probe.py ===' in l and '${p}' not in l]
end = max(ts(l) for l in lines if ts(l))
rows = []
for i, (t0, name) in enumerate(marks):
    t1 = marks[i + 1][0] if i + 1 < len(marks) else end
    rows.append((t1 - t0, name.replace('=== ', '').replace('_probe.py ===', '')))
for d, name in sorted(rows, reverse=True)[:12]: print('%6.0f s  %s' % (d, name))
print('probes total %.0f s; job first to last timestamp %.0f s' % (sum(d for d, _ in rows), end - min(ts(l) for l in lines if ts(l))))
