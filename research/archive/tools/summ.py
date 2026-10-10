import re, sys, collections
src, out = sys.argv[1], sys.argv[2]
lines = [re.sub(r'^\d{4}-\d\d-\d\dT[\d:.]+Z ?', '', l) for l in open(src, encoding='utf-8').read().split('\n')]
mods = ['RelcSelectParity','RelcSelectBlock','RelcSelectSqueeze','RelcSelectC5']
status_re = re.compile(r'^\S+ \[\d+/\d+\] (Built|Building|Replayed|Compiled) ')
res = {}; summary = []
for m in mods:
    idx = [i for i,l in enumerate(lines) if status_re.match(l) and l.rstrip().split(' ')[3] == 'OIBridge.'+m]
    assert len(idx) == 1, (m, idx)
    s = idx[0]; e = s+1
    while e < len(lines) and not status_re.match(lines[e]): e += 1
    block = lines[s+1:e]
    # split into messages
    msgs = []; cur = None
    for l in block:
        if re.match(r'^(warning|error|info): ', l):
            cur = [l]; msgs.append(cur)
        elif cur is not None: cur.append(l)
    for mm in msgs:
        while mm and mm[-1] == '': mm.pop()
    warns = [mm for mm in msgs if mm[0].startswith('warning:')]
    errs = [mm for mm in msgs if mm[0].startswith('error:')]
    infos = [mm for mm in msgs if mm[0].startswith('info:')]
    for mm in msgs: assert mm[0].startswith(('warning:', 'error:', 'info:')) and 'OIBridge/'+m+'.lean' in mm[0], mm[0]
    kinds = collections.Counter()
    for w in warns:
        k = re.search(r'linter\.(\w+) false', '\n'.join(w))
        kinds[k.group(1) if k else 'unknown'] += 1
    axbad = [i[0] for i in infos if 'depends on axioms' in i[0] and re.search(r'\[(.*)\]', i[0]).group(1) != 'propext, Classical.choice, Quot.sound']
    nonax = [i for i in infos if 'depends on axioms' not in i[0]]
    res[m] = (lines[s], errs, warns, infos, kinds, axbad, nonax)
o = []
o.append('# Build diagnostics: OIBridge.RelcSelect{Parity,Block,Squeeze,C5}\n')
o.append('Source: GitHub Actions job 113040684292, repo amaybaum/incompleteness (last 5000 log lines, fetched via get_job_logs). Runner timestamps stripped; message text otherwise verbatim. Warnings are listed in log order.\n')
o.append('## Summary\n')
o.append('| Module | Status line | errors | warnings | by linter | axiom lines | non-standard axioms |')
o.append('|---|---|---|---|---|---|---|')
for m in mods:
    st, errs, warns, infos, kinds, axbad, nonax = res[m]
    o.append(f'| {m} | `{st}` | {len(errs)} | {len(warns)} | ' + ', '.join(f'{k}: {v}' for k,v in sorted(kinds.items())) + f' | {len(infos)} | {len(axbad)} |')
o.append('')
for m in mods:
    st, errs, warns, infos, kinds, axbad, nonax = res[m]
    o.append(f'## OIBridge.{m}\n')
    o.append('Status line:\n\n```\n' + st + '\n```\n')
    o.append(f'### errors ({len(errs)})\n')
    if errs: o.append('```\n' + '\n\n'.join('\n'.join(x) for x in errs) + '\n```\n')
    else: o.append('None.\n')
    o.append(f'### warnings ({len(warns)})\n')
    o.append('Counts by linter: ' + ', '.join(f'{k}: {v}' for k,v in sorted(kinds.items())) + '\n')
    for n, w in enumerate(warns, 1):
        o.append(f'{n}.\n\n```\n' + '\n'.join(w) + '\n```\n')
    o.append(f'### axiom lines ({len(infos)})\n')
    o.append('```\n' + '\n'.join('\n'.join(x) for x in infos) + '\n```\n')
    o.append('Axiom sets other than `[propext, Classical.choice, Quot.sound]`: ' + (str(len(axbad)) if axbad else 'none') + '.\n')
open(out, 'w', encoding='utf-8').write('\n'.join(o))
for m in mods: print(m, res[m][0], len(res[m][1]), len(res[m][2]), dict(res[m][4]), len(res[m][3]), res[m][5], len(res[m][6]))
