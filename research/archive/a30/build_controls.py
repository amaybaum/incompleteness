import json, re, subprocess, sys
pre = open('preregistration.md', encoding='utf-8').read()
props = json.load(open('props.json', encoding='utf-8'))
ledger = json.load(open('retire-ledger.json', encoding='utf-8'))
labels = ['A30-S-HOLD','A30-S-FAILS','A30-S-UNDECIDED','A30-T-HOLD','A30-T-FAILS','A30-T-UNDECIDED',
          'A30-N-LIFTS','A30-N-NO-LIFT','A30-N-UNDECIDED','A30-0-ADMITS','A30-0-RESTRICTS','A30-0-UNDECIDED']
sent = {}
for lab in labels:
    m = re.search(r'(?m)^### `%s`\n\n((?:> .*\n)+)' % re.escape(lab), pre)
    sent[lab] = '\n'.join(l[2:] for l in m.group(1).rstrip('\n').split('\n'))
m = re.search(r'(?m)^> \*\*THE CLAUSE, carried at this mention — the control plane\.\*\*\n((?:> .*\n)+)', pre)
clause = '\n'.join(l[2:] for l in m.group(1).rstrip('\n').split('\n'))
m = re.search(r'(?m)^(Conjunct 8 places no constraint.*?knows the reading exists\.)$', pre, re.S)
watch = m.group(1)
def blob(p): return subprocess.run(['git','hash-object',p],capture_output=True,text=True).stdout.strip()
P0 = {
 'P0_PFR': 'At the product configuration, whether factorization restricts which pair of local class bijections can occur is undecided, with the obstruction named.',
 'P0_PRA': "At the product configuration, whether the ladder's conditions through factorization admit every pair of local class bijections is undecided, with the conjunct that is missing named.",
 'P0_STANDING': "`P0`'s threading part is untouched, no carrier is adopted as the physical one, no surviving law is adopted as the physical one, and nothing here names, endorses or excludes a selection principle.",
 'P0_ADMITS': "At the product configuration, the ladder's conditions through factorization admit every pair of local class bijections: each such pair is the class action of the factor families of a single law carrying all of them, so those conditions do not select among local behaviours.",
 'P0_RESTRICTS': "At the product configuration, the ladder's conditions through factorization do not admit every pair of local class bijections: for an exhibited pair, no law carrying all of them has factor families realizing it, the obstruction being representative-level gauge naturality at the product carrier.",
}
def lit(x):
    return json.dumps(x, ensure_ascii=False, indent=1)
t = open('controls.template.py', encoding='utf-8').read()
rep = {'@@GUARD_BLOB_D@@': blob('guard-D.py'), '@@GUARD_BLOB_RETIRED@@': blob('guard-retired.py'),
       '@@ROADMAP_BLOB_D@@': blob('road-D.md'), '@@OPEN@@': lit(props['open']),
       '@@PROPS@@': lit(props['props']), '@@SENTENCES@@': lit(sent), '@@CLAUSE@@': lit(clause),
       '@@WATCH@@': lit(watch), '@@LEDGER@@': lit(ledger)}
for k, v in P0.items(): rep['@@%s@@' % k] = lit(v)
for k, v in rep.items():
    assert t.count(k) == 1, k
    t = t.replace(k, v)
assert '@@' not in t
open(sys.argv[1], 'w', encoding='utf-8').write(t)
print('ok', {k: len(v) for k, v in sent.items()})
