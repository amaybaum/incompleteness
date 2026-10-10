import json, sys, subprocess, re
sys.path.insert(0, '.')
import texts
fr = json.load(open('frozen.json'))
t = open('prereg_template.md', encoding='utf-8').read()
decls = '\n\n'.join((text + ' …') if kind == 'theorem' else text for kind, text in fr['declarations'].values())
design = open('designruns.md', encoding='utf-8').read().rstrip('\n')
selftest = open('selftest.txt').read().rstrip('\n') if len(sys.argv) > 1 else 'controls: (pending)'
nmut = sys.argv[1] if len(sys.argv) > 1 else 'N'
cblob = subprocess.run(['git', 'hash-object', 'controls.py'], capture_output=True, text=True).stdout.strip()
rep = {
 '{{CLAUSE}}': texts.CLAUSE, '{{SENT_P}}': texts.SENTENCES[texts.LABELS[0]], '{{SENT_U}}': texts.SENTENCES[texts.LABELS[1]],
 '{{HEADER}}': fr['header'].rstrip('\n'), '{{DECLARATIONS}}': decls, '{{REF_BLOB}}': fr['REFERENCE_BLOB'],
 '{{PROBE_BLOB}}': fr['PROBE_BLOB'], '{{PROBE_OK}}': texts.PROBE_OK_PREFIX, '{{FAMILY_NAME}}': fr['FAMILY']['name'],
 '{{FAMILY_NOTE}}': fr['FAMILY']['note'], '{{WORKFLOW_JOB}}': fr['WORKFLOW_JOB'], '{{CONTROLS_BLOB}}': cblob,
 '{{SELFTEST}}': selftest, '{{NMUT}}': nmut, '{{DESIGNRUNS}}': design,
}
for k, v in rep.items():
    assert k in t, k
    t = t.replace(k, v)
left = re.findall(r'\{\{[A-Z_]+\}\}', t)
assert not left, left
open('preregistration.md', 'w', encoding='utf-8').write(t)
print('prereg written', len(t.splitlines()), 'lines; controls blob', cblob)
