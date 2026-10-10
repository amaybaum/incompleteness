b=open('a38/_body.txt',encoding='utf-8').read()
def rep(s,old,new,cnt=1):
    assert s.count(old)==cnt,(old,s.count(old))
    return s.replace(old,new)
b=rep(b,"PARTS = ('REAL', 'EXCL_k1', 'EXCL_k2', 'EXCL_k3', 'EXCL_k4', 'EXCL_e1', 'EXCL_e2', 'EXCL_t1', 'EXCL_t2', 'EXCL_t3')","PARTS = ('REAL',)")
i=b.index('SOURCE_TABLE = tuple('); j=b.index('def duality_ok')
b=b[:i]+'''SOURCE_TABLE = tuple(
    [(k, 'HEAD', 1) for k in PARTS + ('BASE', 'DIAG', 'P_R', 'P_N')]
    + [(k, k, 1) for k in PARTS + ('BASE', 'DIAG')]
    + [('P_R', 'PKG', 1)] + [('P_R', k, 1) for k in PARTS] + [('P_N', k, 1) for k in PARTS]
    + [('REAL', 'BASE', 0), ('REAL', 'DIAG', 0), ('P_R', 'BASE', 0), ('P_N', 'BASE', 0), ('P_R', 'DIAG', 0), ('P_N', 'DIAG', 0)])


'''+b[j:]
b=rep(b,'''    """P_R is the conjunction of the ten package statements over one head and P_N the disjunction of
    their negations, so each verdict is the other's negation; every other statement carries the one
    head; the head is act 37's frozen head followed by this round's objects."""''','''    """P_R is the package statement over one head and P_N its negation, so each verdict is the
    other's negation; every other statement carries the one head; the head is act 38's frozen head
    followed by this round's objects."""''')
b=rep(b,"f.append('duality:PKG-is-not-the-conjunction-of-the-ten')","f.append('duality:PKG-is-not-the-package')")
b=rep(b,"""    if comps['HEAD36'] + comps['HEAD37'] != A37_HEAD or comps['HEAD'] != comps['HEAD36'] + comps['HEAD37'] + comps['HEAD38']:
        f.append('source:head-is-not-act-37s-head-followed-by-this-rounds-objects')""","""    if comps['HEAD38'] != A38_HEAD or comps['HEAD'] != comps['HEAD38'] + comps['HEAD39']:
        f.append('source:head-is-not-act-38s-head-followed-by-this-rounds-objects')""")
b=rep(b,"'dita_local_escape_probe: OK' not in note","'dita_torus_probe: OK' not in note")
b=rep(b,"P0_STANDING_38 + ' |'","P0_STANDING_39 + ' |'")
b=rep(b,"return [] if wf_e == w else ['workflow:not-D-with-the-shard-inserted']","return [] if wf_e == w else ['workflow:not-D-with-the-probe-added']")
b=rep(b,"th('a38_shared_x', 'True')","th('a39_shared_x', 'True')")
b=rep(b,"'\\n\\ndita_local_escape_probe: OK -- x\\n'","'\\n\\ndita_torus_probe: OK -- x\\n'")
b=rep(b,"WORKFLOW: 'jobs:\\n  a36:\\n' + SHARD_ANCHOR + ''.join(old for old, new in WORKFLOW_EDITS[1:])}","WORKFLOW: 'jobs:\\n  a38:\\n    run: |\\n' + PROBE_ANCHOR + '\\n  foundations:\\n'}")
b=rep(b,"c['families'].append({'name': 'act 38', ","c['families'].append({'name': 'act 39', ")
assert 'a38_' not in b and 'A38-' not in b and 'dita_local' not in b and 'A37' not in b and 'HEAD36' not in b
open('a39/_body39.txt','w',encoding='utf-8').write(b)
print('ok')
