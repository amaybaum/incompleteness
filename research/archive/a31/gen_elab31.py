import json, sys
d = json.load(open('props31.json', encoding='utf-8'))
P = d['props']
checks = [('P_N', P['P_N']), ('P_U', P['P_U']), ('S_W', P['S_W']), ('S_TAU', P['S_TAU']),
          ('S_PRE', P['S_PRE']), ('C_exclusive : P_N → ¬ P_U', '(%s) →\n¬ (%s)' % (P['P_N'], P['P_U']))]
bad = sys.argv[2] == 'counter'
out = [d['header'], '/-!', '# Act 31 — elaboration of the frozen propositions, before the freeze', '',
       'Disposable design evidence on a branch that is never landed. Each `#check` elaborates one',
       "frozen proposition, or the frozen corollary, at the frozen module's header and opens.",
       'Nothing here is a theorem, a proof or a verdict.', '-/', '', 'namespace OIBridge',
       'namespace ProductOffLocusUniqueness', '', d['open']]
for name, body in checks:
    if bad and name == 'P_U':
        body = body.replace("GramPhaseEquiv (Φ 0 G) (Φ' 0 G)", "GramPhaseEquiv (Φ 0 G) (Φ' G)")
        name += ', COUNTERCONTROL: the second law applied without its time index; this must not elaborate'
    out.append('-- ' + name)
    out.append('#check (' + '\n'.join(('  ' + l) if i else l for i, l in enumerate(body.split('\n'))) + ' : Prop)')
    out.append('')
out += ['end ProductOffLocusUniqueness', 'end OIBridge', '']
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out))
