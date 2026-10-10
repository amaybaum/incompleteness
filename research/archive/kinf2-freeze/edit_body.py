b=open('controls_body.py').read()
b=b.replace("n.startswith('kinf1_shared_')","n.startswith(SHARED_PREFIX)")
a=b.index("    mut('K-infinity-1 made a theorem'")
z=b.index("    mut('a definition added'")
new=open('mutations_new.txt').read()
b=b[:a]+new+b[z:]
b=b.replace("'theorem kinf1_other'","'theorem kinf2_other'")
old="""    mut('the probe shard left out of the aggregate', 'surface:' + WORKFLOW, P,
        edit_file(WORKFLOW, '          test "${KINF1_RESULT}" = success\\n', ''))"""
assert old in b
b=b.replace(old,"""    mut('the probe shard left out of the aggregate', 'surface:' + WORKFLOW, P,
        edit_file(WORKFLOW, '          test "${KINF2_RESULT}" = success\\n', ''))
    mut('the exact-algebra dependency unpinned', 'surface:' + WORKFLOW, P,
        edit_file(WORKFLOW, 'pip install sympy==1.14.0', 'pip install sympy'))""")
old="""    mut('the roadmap touched', 'paths', P, lambda e, ch: ch.__setitem__('verification/ROADMAP.md', 'M'))"""
assert old in b
b=b.replace(old, old+"""
    mut('the halted round KINF-1 record touched', 'paths', P,
        lambda e, ch: ch.__setitem__(KINF1_RECORD + 'result.md', 'M'))""")
old="mut('the note claims K-infinity-1 holds', 'note:forbidden-claim', U, append_note('\\nSo K∞-1 holds.\\n'))"
assert old in b
b=b.replace(old,"mut('the note claims K-infinity-1 holds for the completion', 'note:forbidden-claim', U,\n        append_note('\\nSo K∞-1 holds for the completion.\\n'))")
open('controls_body.py','w').write(b)
