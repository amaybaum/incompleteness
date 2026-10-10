import json, re, subprocess, sys
t = open('prereg.template.md', encoding='utf-8').read()
dr = open('preregistration.draft1.md', encoding='utf-8').read()
props = json.load(open('props.json', encoding='utf-8'))
ledger = json.load(open('retire-ledger.json', encoding='utf-8'))
def blob(p): return subprocess.run(['git','hash-object',p],capture_output=True,text=True).stdout.strip()
def between(s, a, b):
    i = s.index(a); j = s.index(b, i); return s[i:j]
m = re.search(r'(?m)^> \*\*THE CLAUSE, carried at this mention — the control plane\.\*\*\n(?:> .*\n)+', dr)
clause_block = m.group(0).rstrip('\n')
watch = re.search(r'(?m)^(Conjunct 8 places no constraint.*?knows the reading exists\.)$', dr, re.S).group(1)
sent = between(dr, '### `A30-S-HOLD`', '### The corollaries, REQUIRED')
table = between(dr, '### The outcome-vector table', '***\n\n## The `P0` row')
rows = ['| entry | what it removes or rewrites | old text, SHA-256 | new text, SHA-256 |', '| --- | --- | --- | --- |']
for e in ledger:
    new = ('`%s`' % e['new_sha256']) if e['new'] else ('empty, `%s`' % e['new_sha256'])
    rows.append('| `%s` | %s | `%s` | %s |' % (e['id'], e['reason'], e['old_sha256'], new))
P0 = {}
exec(open('p0.py', encoding='utf-8').read(), P0)
rep = {
 '@@CLAUSE_BLOCK@@': clause_block, '@@WATCH@@': watch, '@@SENTENCES_SECTION@@': sent,
 '@@TABLE_SECTION@@': table, '@@OPEN@@': props['open'],
 '@@P_S@@': props['props']['P_S'], '@@P_T@@': props['props']['P_T'],
 '@@P_N@@': props['props']['P_N'], '@@P_0@@': props['props']['P_0'],
 '@@LEDGER_TABLE@@': '\n'.join(rows),
 '@@GUARD_BLOB_D@@': blob('guard-D.py'), '@@GUARD_BLOB_RETIRED@@': blob('guard-retired.py'),
 '@@ROADMAP_BLOB_D@@': blob('road-D.md'), '@@ROADMAP_BLOB_ADMITS@@': blob('road-admits.md'),
 '@@ROADMAP_BLOB_RESTRICTS@@': blob('road-restricts.md'),
 '@@CONTROLS_BLOB@@': blob('controls.py'),
 '@@EVIDENCE@@': open('evidence.md', encoding='utf-8').read().rstrip('\n'),
 '@@SELFTEST@@': open('selftest.md', encoding='utf-8').read().rstrip('\n'),
 '@@N_MUTATIONS@@': open('nmut.txt').read().strip(),
}
for k in ('P0_PFR','P0_PRA','P0_STANDING','P0_ADMITS','P0_RESTRICTS'):
    rep['@@%s@@' % k] = P0[k]
first = ('@@EVIDENCE@@', '@@SELFTEST@@')
for k in first + tuple(x for x in rep if x not in first):
    v = rep[k]
    assert k in t, k
    t = t.replace(k, v)
assert '@@' not in t, re.findall(r'@@\w+@@', t)
open('preregistration.md', 'w', encoding='utf-8').write(t)
print('written', blob('preregistration.md'))
