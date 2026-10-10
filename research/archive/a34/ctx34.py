"""usage: ctx34.py <logfile> <n_ctx_lines> : the error list, then each error's context from the contexts section, then sorry lines."""
import sys, re
t = open(sys.argv[1]).read(); t = t.replace('\\n', '\n') if t.count('\n') < 5 else t
lines = [re.sub(r'^\S+ ', '', l) for l in t.split('\n')]
n = int(sys.argv[2])
ci = [i for i, l in enumerate(lines) if '=== ERROR CONTEXTS ===' in l and 'echo' not in l]
errs = [l for l in lines if l.startswith('error: OIBridge/ProductStratum')]
seen = set()
print('--- %d error lines ---' % len(errs))
for e in errs: print(e[:200])
if ci:
    sub = lines[ci[0]:]
    for e in errs:
        key = e.split(':')[1] + ':' + e.split(':')[2] + ':' + e.split(':')[3]
        if key in seen: continue
        seen.add(key)
        for i, l in enumerate(sub):
            if key in l and 'error' in l:
                print('\n#### ' + key); print('\n'.join(x[:240] for x in sub[i:i + n] if 'linter' not in x and 'Hint:' not in x and 'Omit it' not in x and 'This simp argument' not in x and x.strip())); break
si = [i for i, l in enumerate(lines) if '=== SORRY ===' in l and 'echo' not in l]
if si:
    print('\n--- SORRY ---'); print('\n'.join(x[:160] for x in lines[si[0]:si[0] + 40] if 'sorryAx' in x))
