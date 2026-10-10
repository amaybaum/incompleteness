import json, sys
d = json.load(open('props.json', encoding='utf-8'))
P = d['props']
def ind(s, n=4):
    return '\n'.join((' ' * n + l) if l else l for l in s.split('\n'))
checks = []
for k in ('P_S', 'P_T', 'P_N', 'P_0'):
    checks.append((f'{k}', f"({P[k]})"))
checks.append(('C_lift  : P_S → P_T → P_N', f"({P['P_S']}) →\n({P['P_T']}) →\n({P['P_N']})"))
checks.append(('C_admit : P_N → P_0', f"({P['P_N']}) →\n({P['P_0']})"))
checks.append(('C_restrict : P_0 → P_N', f"({P['P_0']}) →\n({P['P_N']})"))
out = [d['header'], '/-!',
       '# Act 30 — elaboration of the frozen propositions, before the freeze',
       '',
       'Disposable design evidence on a branch that is never landed. Each `#check` elaborates one',
       "frozen proposition, or one frozen corollary implication, at the frozen module's header and",
       'opens. Nothing here is a theorem, a proof or a verdict.',
       '-/', '', 'namespace OIBridge', 'namespace ProductStrictLift', '', d['open']]
for name, body in checks:
    out.append(f'-- {name}')
    out.append('#check (' + '\n'.join(('  ' + l) if i else l for i, l in enumerate(body.split('\n'))) + ' : Prop)')
    out.append('')
out += ['end ProductStrictLift', 'end OIBridge', '']
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out))
