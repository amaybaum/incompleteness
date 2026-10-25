"""Targeted mutants for the re-check-4 nits: one per new check plus the review's T3. Not a full campaign (AGENTS
section A.40). Each mutant is written to a temporary directory with the checker's location substituted, run with
python3 -I -B, and counts as caught only if it exits 2 and its first line begins with VOID and the targeted label.
The unmodified checker is covered by the replay commands, not rerun here."""
import hashlib
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.normpath(os.path.join(HERE, '..'))
LOCATION = 'HERE = os.path.dirname(os.path.abspath(__file__))'


def main():
    src = open(os.path.join(TARGET, 'checks.py')).read()
    plan = open(os.path.join(TARGET, 'PLAN.md')).read()
    prov = json.load(open(os.path.join(TARGET, 'PROVENANCE.json')))
    lines, ok = [], True
    with tempfile.TemporaryDirectory() as tmp:
        # a consistently edited preregistration: PLAN.md rescoped to k = 1..15 with its pin updated to match
        p2 = plan.replace('k = 1..16**', 'k = 1..15**')
        if p2 == plan:
            print('VOID: targeted mutant setup did not apply')
            sys.exit(2)
        plan_path = os.path.join(tmp, 'PLAN.md')
        open(plan_path, 'w').write(p2)
        h2 = hashlib.sha256(p2.encode()).hexdigest()
        prov2 = dict(prov, plan_sha256=h2)
        prov_path = os.path.join(tmp, 'PROVENANCE.json')
        open(prov_path, 'w').write(json.dumps(prov2))
        rescope = [('def family(Bs=(2, 3, 4), kmax=16):', 'def family(Bs=(2, 3, 4), kmax=15):'),
                   ('def independent_audit(fam, encl, Bs=(2, 3, 4), kmax=16):',
                    'def independent_audit(fam, encl, Bs=(2, 3, 4), kmax=15):'),
                   ("PLAN = os.path.join(HERE, 'PLAN.md')", f'PLAN = {plan_path!r}'),
                   ("PLAN_SHA256 = 'b7f7eaae58de13b9eb348bb4e31e92a7bce6741be64553c9ba496af9a2c6a275'",
                    f'PLAN_SHA256 = {h2!r}')]
        mutants = [
            ('T3_label_remap_k_plus_1', 'record-length check (review T3)',
             [('            law = block_law(B, k)\n', '            law = block_law(B, k + 1 if k < 16 else k)\n')],
             'scope: block-law record length equals member k'),
            ('MT2_plan_and_pin_edited', 'PROVENANCE cross-check', rescope,
             'scope: plan pin equals PROVENANCE plan_sha256'),
            ('MT3_plan_pin_and_provenance_edited', 'plan-commit blob cross-check',
             rescope + [("PROVENANCE = os.path.join(HERE, 'PROVENANCE.json')", f'PROVENANCE = {prov_path!r}')],
             'scope: plan pin equals the PLAN.md blob of 1dfec979'),
        ]
        for name, control, pairs, label in mutants:
            m = src
            for o, n in pairs:
                if m.count(o) != 1:
                    print(f'VOID: mutant {name} does not apply exactly once')
                    sys.exit(2)
                m = m.replace(o, n)
            m = m.replace(LOCATION, f'HERE = {TARGET!r}')
            path = os.path.join(tmp, name + '.py')
            open(path, 'w').write(m)
            p = subprocess.run([sys.executable, '-I', '-B', path], capture_output=True, text=True)
            first = p.stdout.splitlines()[0] if p.stdout else ''
            caught = p.returncode == 2 and first.startswith('VOID: ' + label)
            ok &= caught
            lines.append(f'{name}: targets {control}; exit {p.returncode}; {first[:120]}; '
                         + ('CAUGHT' if caught else 'NOT CAUGHT'))
    lines.append('all targeted mutants caught' if ok else 'SOME TARGETED MUTANT NOT CAUGHT')
    print('\n'.join(lines))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
