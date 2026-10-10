import json, sys
d = json.load(open('props32.json', encoding='utf-8'))
P = d['props']
order = ['P_R', 'P_N', 'S_EXIST', 'S_ISO', 'S_SEP', 'S_OVL', 'S_MOVE', 'S_GLOBAL', 'S_ID', 'S_QUARTER']
checks = [(k, P[k]) for k in order] + [('C_exclusive : P_N → ¬ P_R', '(%s) →\n¬ (%s)' % (P['P_N'], P['P_R']))]
bad = sys.argv[2] == 'counter'
out = [d['header'], '/-!', '# Act 32 — elaboration of the frozen propositions, before the freeze', '',
       'Disposable design evidence on a branch that is never landed. Each `#check` elaborates one',
       "frozen proposition, or the frozen corollary, at the frozen module's header and opens.",
       'Nothing here is a theorem, a proof or a verdict.', '-/', '', 'namespace OIBridge',
       'namespace OrbitIsometryClassification', '', d['open']]
for name, body in checks:
    if bad and name == 'P_R':
        assert body.count('(fun i => (G (π i)).submatrix τ τ))') == 1
        body = body.replace('(fun i => (G (π i)).submatrix τ τ))', '(fun i => (G (π i)).submatrix τ))')
        name += ', COUNTERCONTROL: the first shape relabels rows only; this must not elaborate'
    out.append('-- ' + name)
    out.append('#check (' + '\n'.join(('  ' + l) if i else l for i, l in enumerate(body.split('\n'))) + ' : Prop)')
    out.append('')
out += ['end OrbitIsometryClassification', 'end OIBridge', '']
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out))
