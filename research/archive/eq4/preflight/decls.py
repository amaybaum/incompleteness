import re, sys, os, json
ROOT = sys.argv[1]
start = sys.argv[2:]
def path_of(mod): return os.path.join(ROOT, *mod.split('.')) + '.lean'
seen = []
def closure(mod):
    if mod in seen: return
    p = path_of(mod)
    if not os.path.exists(p): return
    seen.append(mod)
    for line in open(p, encoding='utf-8'):
        m = re.match(r'^import\s+(OIBridge\.\S+)', line)
        if m: closure(m.group(1))
for s in start: closure(s)
decl_re = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)\s+)*(def|theorem|lemma|abbrev|structure|inductive|class|instance|opaque|axiom)\s+([^\s:(\[{]+)')
out = {}
for mod in seen:
    p = path_of(mod)
    ns = []
    stack = []  # entries ('ns', [parts]) or ('sec', name)
    priv = False
    for line in open(p, encoding='utf-8'):
        s = line.rstrip('\n')
        m = re.match(r'^namespace\s+(\S+)', s)
        if m:
            parts = m.group(1).split('.')
            stack.append(('ns', parts)); ns += parts; continue
        m = re.match(r'^(?:noncomputable\s+)?section(?:\s+(\S+))?', s)
        if m:
            stack.append(('sec', m.group(1))); continue
        m = re.match(r'^end(?:\s+(\S+))?\s*$', s)
        if m:
            if stack:
                k, v = stack.pop()
                if k == 'ns':
                    ns = ns[:len(ns)-len(v)]
            continue
        m = decl_re.match(s)
        if m:
            kind, name = m.group(1), m.group(2)
            if 'private' in s.split(kind)[0]: continue
            if name.startswith('_root_.'): full = name[len('_root_.'):]
            else: full = '.'.join(ns + [name])
            out.setdefault(full, []).append((mod, kind))
print(json.dumps({'modules': seen, 'decls': out}))
