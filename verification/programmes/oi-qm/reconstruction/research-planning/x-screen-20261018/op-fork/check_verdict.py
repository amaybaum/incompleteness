#!/usr/bin/env python3
"""check_verdict.py -- consistency check of the op-fork verdict against its recorded measurements.  Research only.

Separate from probes/replay.py: it imports nothing from the replay or the probes and writes no file.  It
  1. authenticates the frozen records against pinned digests (runs/SHA256SUMS, ../runs/SHA256SUMS,
     audit-931d5eda/runs/SHA256SUMS, and runs/replay.log, which no manifest covers);
  2. re-applies the frozen rule of PREREG.md section 3 to the recorded RESULT labels (domain, classification,
     existence E, U-weak, distinctness), requiring each GREEN label to have its supporting line in the record;
  3. derives the assertion "OP-weak => OP-strong is false on the domain" from the recorded U-strong values and
     their exact witness lines, instead of taking it as a fixed sentence;
  4. compares the derived branch, cone list, U-strong values and assertion with runs/verdict.out, and the
     U-strong values with the independent audit's output (corroboration only; it does not enter the rule).

It certifies consistency between records and verdict text, nothing more.  It re-derives no mathematics: a GREEN
label at level [WA] remains a written argument.  The level printed beside each label is the one the record itself
and the audit (audit-931d5eda/AUDIT.md, F3) assign.

Usage:
  python3 -I -B check_verdict.py              # last line: CHECK CONSISTENT | CHECK INCONSISTENT | CHECK VOID
  python3 -I -B check_verdict.py --self-test  # mutation controls on in-memory copies; last line SELFTEST GREEN|RED
"""
import hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sha = lambda b: hashlib.sha256(b).hexdigest()

PINS = {
    'runs/SHA256SUMS': '949194ce9e88e5465f582ff4ca1278ee3c82e118b3a3a1632e6386c77000f6f2',
    'runs/replay.log': '8decc98b9fae75a1fc67c8bf8bb25a44cba133dc397adb689c425eaa3cbde345',
    '../runs/SHA256SUMS': '2b700e9467c62e85d06dfe9697a19c5b5fb63e80acd95343435686e4b24dbf4b',
    'audit-931d5eda/runs/SHA256SUMS': '28dc9c43806868b8d4a72dd21386d9325ba38fac9278ef1c3552ebd034246220',
}
Q1, Q2, Q3F, P3, VERD, LOG = ('runs/q1_maxcone_extreme.out', 'runs/q2_zf_cones.out', 'runs/q3_fixture_table.out',
                              'runs/upstream_p3_fixtures_op.out', 'runs/verdict.out', 'runs/replay.log')
AUD = 'audit-931d5eda/runs/final/audit_exact.out'
RECORDS = (Q1, Q2, Q3F, P3, VERD)

CANDS = (('N3_KZF', 'K(Z_F) = (Q3 n Z_F*) + cone(Z_F)'),
         ('N4_L', 'L = Q3 n Z_F*'),
         ('N5_KGamma', 'K_Gamma = Q3 + R+ Gamma(B)'))
REQ = (('domain', '(i) domain inclusions', '[EC + WA]'),
       ('pure_classification', '(ii) pure-state classification', '[WA on EC inputs]'),
       ('existence_all_marginals', '(iii) existence E at every marginal', '[EC identity + WA]'),
       ('uweak_all_marginals', '(iv) U-weak at every marginal', '[WA: N2, Uhlmann L]'),
       ('distinct', '(v) K != Q3, K != Gamma(Q3)', '[EC]'))
US_LEVEL = '[EC witness + WA: uniqueness of the relating map]'
LEVEL_OVERRIDE = {('N5_KGamma', 'pure_classification'): '[WA on N1 EC inputs]',
                  ('N5_KGamma', 'existence_all_marginals'): '[EC instance + WA: Q3 canonical purification]'}

# Supporting lines: each GREEN label (or U-strong FAIL label) must be backed by these lines of its record.
SUPPORT = {
    ('N3_KZF', 'domain'): [(Q2, 'PASS DOM SEP <= Z_F*'), (Q2, 'PASS DOM L <= Q3 <= maxCone and cone(Z_F) <= maxCone')],
    ('N3_KZF', 'pure_classification'): [(Q2, 'PASS W1  each I/2 - z_k is a rank-one projector'),
                                        (Q2, 'PASS W2  sum_k <m_k|X|m_k> = Tr X')],
    ('N3_KZF', 'existence_all_marginals'): [(Q2, 'PASS W4  identity: 1/2 - |<m|psi_rho>|^2'),
                                            (Q2, '[WA] with alpha >= |beta| and alpha^2+beta^2 = 1/2')],
    ('N3_KZF', 'uweak_all_marginals'): [(Q2, 'U-weak at every marginal [WA on EC inputs]'), (Q3F, 'PASS A2  Gamma(Ad_{I(x)u} H)')],
    ('N3_KZF', 'distinct'): [(Q2, 'PASS NEQ z_k not in Q3'), (Q2, 'PASS NEQ Phi+ not in Gamma(Q3)')],
    ('N3_KZF', 'ustrong'): [(Q2, 'PASS US  psi2 = (I(x)diag(1,i))Phi+ is a pure state of L'),
                            (Q2, 'PASS US  witness x = (I(x)v^dag) m_k lies in L while Ad_{I(x)v} x = P_{m_k} lies outside L and outside K(Z_F)')],
    ('N4_L', 'domain'): [(Q2, 'PASS DOM SEP <= Z_F*'), (Q2, 'PASS DOM L <= Q3 <= maxCone')],
    ('N4_L', 'pure_classification'): [(Q2, 'PASS W2  sum_k <m_k|X|m_k> = Tr X')],
    ('N4_L', 'existence_all_marginals'): [(Q2, 'PASS W4  identity: 1/2 - |<m|psi_rho>|^2'),
                                          (Q2, '[WA] with alpha >= |beta| and alpha^2+beta^2 = 1/2')],
    ('N4_L', 'uweak_all_marginals'): [(Q2, 'U-weak at every marginal [WA on EC inputs]'), (Q3F, 'PASS A2  Gamma(Ad_{I(x)u} H)')],
    ('N4_L', 'distinct'): [(Q2, 'PASS NEQ m_k in Q3 but Tr(P_{m_k} z_k) = -1/2 < 0'), (Q2, 'PASS NEQ Phi+ not in Gamma(Q3)')],
    ('N4_L', 'ustrong'): [(Q2, 'PASS US  psi2 = (I(x)diag(1,i))Phi+ is a pure state of L'),
                          (Q2, 'PASS US  witness x = (I(x)v^dag) m_k lies in L while Ad_{I(x)v} x = P_{m_k} lies outside L and outside K(Z_F)')],
    ('N5_KGamma', 'domain'): [(Q3F, 'PASS N5  Gamma(B) in maxCone')],
    ('N5_KGamma', 'pure_classification'): [(Q3F, '[WA] Ext(K_Gamma) = {rank-one PSD} u {Gamma(B)}')],
    ('N5_KGamma', 'existence_all_marginals'): [(Q3F, 'E: canonical purifications.'),
                                               (Q3F, 'PASS C1  Q3: canonical purification of a non-diagonal rho')],
    ('N5_KGamma', 'uweak_all_marginals'): [(Q3F, 'U-weak by A2: at rho != I/2 only purifications'), (Q3F, 'PASS A2  Gamma(Ad_{I(x)u} H)')],
    ('N5_KGamma', 'distinct'): [(Q3F, 'PASS N5  Gamma(B) not PSD (=> K_Gamma != Q3) and Phi+ not in Gamma(Q3)')],
    ('N5_KGamma', 'ustrong'): [(Q3F, 'PASS N5  W = P_singlet + P00 is PSD and Tr(W Gamma(B)) = 0'),
                               (Q3F, 'PASS N5  Tr(W Gamma(chi_ab chi_ab^T)) = a(a-b) < 0'),
                               (Q3F, '[WA] U-strong FAILS for K_Gamma')],
}
# Independent audit's U-strong failure lines (corroboration only).
AUDIT_US = {'N3_KZF': ['[I/2] L and KZ fail U-strong', '[rho_A] L and KZ fail U-strong'],
            'N4_L': ['[I/2] L and KZ fail U-strong', '[rho_A] L and KZ fail U-strong'],
            'N5_KGamma': ['KG fails U-strong']}
JOBS = ('q1_maxcone_extreme', 'q2_zf_cones', 'q3_fixture_table', 'upstream_p3_fixtures_op')


def load():
    raw = {}
    for p in set(PINS) | set(RECORDS) | {AUD}:
        with open(os.path.join(HERE, p), 'rb') as f:
            raw[p] = f.read()
    return raw


def manifest(b):
    m = {}
    for line in b.decode().splitlines():
        if line.strip():
            d, name = line.split('  ', 1); m[name] = d
    return m


def authenticate(raw):
    """Digest gate.  Returns (failures, p3_digest)."""
    bad = ['%s: digest does not match its pin' % p for p, d in sorted(PINS.items()) if sha(raw[p]) != d]
    m = manifest(raw['runs/SHA256SUMS'])
    bad += ['%s: digest does not match runs/SHA256SUMS' % p for p in RECORDS if m.get(p) != sha(raw[p])]
    ma = manifest(raw['audit-931d5eda/runs/SHA256SUMS'])
    if ma.get('runs/final/audit_exact.out') != sha(raw[AUD]):
        bad.append('%s: digest does not match the audit manifest' % AUD)
    p3 = manifest(raw['../runs/SHA256SUMS']).get('runs/p3_fixtures_op.out')
    return bad, p3


def results(txt, R, conflicts, src):
    for line in txt.splitlines():
        if not line.startswith('RESULT '):
            continue
        parts = line.split()[1:]
        if '=' in parts[0]:
            new = dict(p.split('=', 1) for p in parts)
        else:
            new = {parts[0]: dict(p.split('=', 1) for p in parts[1:])}
        for k, v in new.items():
            if k in R and R[k] != v:
                conflicts.append('RESULT key %s recorded twice with different values (%s)' % (k, src))
            R[k] = v


def has_line(txt, needle):
    for line in txt.splitlines():
        s = line.strip()
        if needle in s and (s.startswith('PASS ') or s.startswith('[WA]') or s.startswith('VERDICT ')):
            return True
    return False


def check(T, p3_digest):
    """Semantic layer.  T maps record path -> text.  Returns (status, lines)."""
    out, bad = [], []
    R, conflicts = {}, []
    for p in (Q1, Q2, Q3F):
        results(T[p], R, conflicts, p)
        summ = [l for l in T[p].splitlines() if l.startswith('SUMMARY ')]
        fails = [l for l in T[p].splitlines() if l.startswith('FAIL')]
        if len(summ) != 1 or not summ[0].endswith(' failed=0') or fails:
            bad.append('%s: SUMMARY is not failed=0, or a FAIL line is present' % p)
    bad += conflicts

    # Controls of PREREG section 5, read from the records.
    c6 = R.get('C6', {}) if isinstance(R.get('C6'), dict) else {}
    log = T[LOG].splitlines()
    det = all(any(l.startswith(j + ' ') and 'deterministic=True rc=0,0' in l for l in log) for j in JOBS)
    controls = [
        ('C1 positive (Q3, Gamma(Q3))', R.get('C1') == 'GREEN'),
        ('C2 existence can fail', R.get('C2_existence_fails') == 'GREEN' and R.get('C2_mutated_cut') == 'GREEN'),
        ('C3 U-weak can fail (K_mut)', R.get('C3_uweak_fails') == 'GREEN'),
        ('C4 nullspace countercontrol', R.get('C4') == 'GREEN'),
        ('C5 identification of R = O(3)', R.get('C5') == 'GREEN'),
        ('C6 U-strong can fail / can pass', c6.get('ustrong_fail_KGamma') == 'GREEN' and c6.get('ustrong_pass_Q3_GQ3') == 'GREEN'),
        ('C7 upstream p3 = ../runs/SHA256SUMS', p3_digest is not None and sha(T[P3].encode()) == p3_digest),
        ('determinism (runs/replay.log)', det),
        ('N1 maxCone extreme rays (input)', R.get('N1_maxcone_ext_rank1_and_gamma') == 'GREEN'),
    ]
    out.append('CONTROLS (read from the records)')
    for name, ok in controls:
        out.append('  %-38s %s' % (name, 'GREEN' if ok else 'RED'))
    allc = all(ok for _, ok in controls)

    # Frozen RETIRE condition per candidate, with supporting lines.
    out.append('RETIRE CONDITION PER CONE (PREREG section 3; label / supporting line / evidence level)')
    cands, witnesses = [], []
    for key, label in CANDS:
        d = R.get(key) if isinstance(R.get(key), dict) else {}
        out.append('  %s' % label)
        met = bool(d)
        for k, desc, lvl in REQ:
            sup = all(has_line(T[f], s) for f, s in SUPPORT[(key, k)])
            lab = d.get(k)
            if lab == 'GREEN' and sup:
                st = 'GREEN, supported'
            elif lab is None and sup:
                st = 'no RESULT key; written line present'
            elif lab == 'GREEN':
                st = 'GREEN, supporting line MISSING'; bad.append('%s %s: GREEN label without its supporting line' % (key, k))
            else:
                st = '%s%s' % (lab if lab else 'not recorded', '' if sup else ', no supporting line')
            ok = st.startswith('GREEN, supported') or st.startswith('no RESULT key')
            met &= ok
            out.append('    %-38s %-40s %s' % (desc, st, LEVEL_OVERRIDE.get((key, k), lvl)))
        us = d.get('ustrong')
        us_sup = all(has_line(T[f], s) for f, s in SUPPORT[(key, 'ustrong')])
        if us == 'FAIL' and not us_sup:
            bad.append('%s ustrong: FAIL label without its exact witness line' % key)
        if us == 'PASS' and us_sup:
            bad.append('%s ustrong: PASS label while its failure witness line is present' % key)
        out.append('    %-38s %-40s %s' % ('U-strong (not part of the rule)', '%s%s' % (us if us else 'not recorded', ', witness present' if us_sup else ''), US_LEVEL))
        out.append('    %-38s %s' % ('meets RETIRE condition', 'yes' if met and allc else 'no'))
        if met and allc:
            cands.append(key)
            if us == 'FAIL' and us_sup:
                witnesses.append(key)

    # Derived verdict and assertion.
    names = dict(CANDS)
    if not allc:
        branch = 'VOID'
    elif cands:
        branch = 'RETIRE'
    else:
        branch = 'UNDECIDED'
    out.append('DERIVED')
    out.append('  branch of the frozen rule: %s' % branch)
    out.append('  cones meeting the RETIRE condition: %d (%s)' % (len(cands), ', '.join(names[c] for c in cands) or 'none'))
    if branch == 'VOID':
        out.append('  OP-weak => OP-strong: no assertion (a control is RED; no verdict is rendered)')
    elif witnesses:
        out.append('  OP-weak => OP-strong: false on the domain; %d of %d such cones record U-strong FAIL with an exact witness line'
                   % (len(witnesses), len(cands)))
        out.append('    (%s)' % ', '.join(names[c] for c in witnesses))
    else:
        out.append('  OP-weak => OP-strong: not refuted by these records')
    if branch != 'VOID':
        out.append('  KEEP disjunct "OP-weak => K in {Q3, Gamma(Q3)}": %s' % ('refuted' if cands else 'not refuted'))
        out.append('  KEEP disjunct "OP-weak => OP-strong": %s' % ('refuted' if witnesses else 'not refuted'))
    m = R.get('N6_maxCone') if isinstance(R.get('N6_maxCone'), dict) else {}
    if branch != 'VOID' and m.get('ustrong') == 'PASS':
        out.append('  N6 record: maxCone U-strong=PASS, PC=%s.  maxCone is not Q3 or Gamma(Q3) and satisfies E and U-weak' % m.get('PC'))
        out.append('    [WA + L: N1, Stormer-Woronowicz, N2], so it meets the RETIRE condition without N3-N5; the branches are')
        out.append('    not exclusive.  It satisfies U-strong, so it does not bear on OP-weak => OP-strong.  Not counted above.')

    # Corroboration by the independent audit (does not enter the rule).
    A = T[AUD]
    aud_ok = any(l == 'SUMMARY checks=47 failed=0' for l in A.splitlines()) and 'RESULT c=GREEN' in A.splitlines()
    out.append('CORROBORATION (audit-931d5eda, independent exact code; not part of the rule)')
    for key, label in CANDS:
        cor = aud_ok and all(has_line(A, s) for s in AUDIT_US[key])
        rec = (R.get(key) or {}).get('ustrong') if isinstance(R.get(key), dict) else None
        out.append('  %-38s audit U-strong FAIL witness: %s' % (label, 'present' if cor else 'absent'))
        if cor and rec != 'FAIL':
            bad.append('%s: fork record U-strong=%s conflicts with the independent audit\'s failure witness' % (key, rec))

    # Comparison with the recorded verdict text.
    V = T[VERD].splitlines()
    fv = [l for l in V if l.startswith('FORK VERDICT: ')]
    vb = 'RETIRE' if fv and 'RETIRE branch' in fv[0] else 'VOID' if fv and 'VOID' in fv[0] else 'UNDECIDED' if fv and 'UNDECIDED' in fv[0] else None
    listed = {}
    for l in V:
        s = l.strip()
        if s.startswith('- ') and '[U-strong: ' in s:
            lab = s[2:s.index('[U-strong: ')].strip()
            listed[lab] = s[s.index('[U-strong: ') + 11:].split(']')[0].split(';')[0].strip()
    sentence = any('OP-weak => OP-strong is therefore false on the domain' in l for l in V)
    out.append('COMPARISON WITH runs/verdict.out')
    cmp = [('branch', vb == branch, '%s vs derived %s' % (vb, branch)),
           ('cone list', set(listed) == {names[c] for c in cands}, '%d listed vs %d derived' % (len(listed), len(cands))),
           ('U-strong values', all(listed.get(names[c]) == R[c].get('ustrong') for c in cands if names[c] in listed),
            'listed values vs records'),
           ('OP-weak => OP-strong sentence', sentence == bool(witnesses),
            'sentence %s; derived %s' % ('present' if sentence else 'absent',
                                         'no assertion' if branch == 'VOID' else 'refuted' if witnesses else 'not refuted'))]
    for name, ok, note in cmp:
        out.append('  %-38s %-6s %s' % (name, 'agrees' if ok else 'DIFFERS', note))
        if not ok:
            bad.append('verdict.out %s differs from the records (%s)' % (name, note))
    if not allc:
        status = 'VOID'
    elif bad:
        status = 'INCONSISTENT'
    else:
        status = 'CONSISTENT'
    for b in bad:
        out.append('  problem: %s' % b)
    return status, out, (branch, len(cands), len(witnesses))


def run_records():
    raw = load()
    bad, p3 = authenticate(raw)
    out = ['AUTHENTICATION (pinned digests; runs/SHA256SUMS; audit manifest)']
    out += ['  %s' % b for b in bad] or ['  all records match']
    if bad:
        return 'VOID', out, None
    T = {p: b.decode() for p, b in raw.items()}
    st, lines, summary = check(T, p3)
    return st, out + lines, summary


def sub(t, old, new, count):
    if t.count(old) != count:
        raise SystemExit('HARNESS ERROR: mutation anchor %r found %d times, expected %d' % (old, t.count(old), count))
    return t.replace(old, new)


def drop_line(t, needle):
    lines = t.split('\n'); keep = [l for l in lines if needle not in l]
    if len(lines) - len(keep) != 1:
        raise SystemExit('HARNESS ERROR: line anchor %r matched %d lines' % (needle, len(lines) - len(keep)))
    return '\n'.join(keep)


def self_test():
    raw = load()
    bad, p3 = authenticate(raw)
    if bad:
        print('SELFTEST RED (records do not authenticate: %s)' % '; '.join(bad)); return 1
    base = {p: b.decode() for p, b in raw.items()}
    W2 = SUPPORT[('N3_KZF', 'ustrong')][1][1]

    def m_all_pass(T):
        T[Q2] = sub(T[Q2], 'ustrong=FAIL', 'ustrong=PASS', 2)
        T[Q3F] = sub(T[Q3F], 'distinct=GREEN ustrong=FAIL', 'distinct=GREEN ustrong=PASS', 1)

    def m_coherent_counterfactual(T):
        m_all_pass(T)
        for f, s in SUPPORT[('N3_KZF', 'ustrong')][1:] + SUPPORT[('N5_KGamma', 'ustrong')][1:]:
            T[f] = drop_line(T[f], s)
        T[AUD] = sub(T[AUD], 'RESULT c=GREEN', 'RESULT c=RED', 1)
        T[VERD] = sub(T[VERD], '[U-strong: FAIL', '[U-strong: PASS', 3)
        T[VERD] = drop_line(T[VERD], 'OP-weak => OP-strong is therefore false on the domain')

    def m_kgamma_pass(T):
        T[Q3F] = sub(T[Q3F], 'distinct=GREEN ustrong=FAIL', 'distinct=GREEN ustrong=PASS', 1)

    def m_drop_witness(T):
        T[Q2] = drop_line(T[Q2], W2)

    def m_c6_red(T):
        T[Q3F] = sub(T[Q3F], 'RESULT C6 ustrong_fail_KGamma=GREEN', 'RESULT C6 ustrong_fail_KGamma=RED', 1)

    def m_existence_fail(T):
        T[Q2] = sub(T[Q2], 'existence_all_marginals=GREEN', 'existence_all_marginals=FAIL', 2)
        T[Q3F] = sub(T[Q3F], 'existence_all_marginals=GREEN', 'existence_all_marginals=FAIL', 1)

    cases = [
        ('T0 unmutated records', None, ('CONSISTENT', 'RETIRE', 3, 3)),
        ('T1 U-strong PASS recorded for all three cones', m_all_pass, ('INCONSISTENT', 'RETIRE', 3, 0)),
        ('T2 coherent counterfactual: U-strong PASS, witnesses, audit and sentence removed', m_coherent_counterfactual,
         ('CONSISTENT', 'RETIRE', 3, 0)),
        ('T3 U-strong PASS recorded for K_Gamma only', m_kgamma_pass, ('INCONSISTENT', 'RETIRE', 3, 2)),
        ('T4 K(Z_F)/L U-strong witness line removed', m_drop_witness, ('INCONSISTENT', 'RETIRE', 3, 1)),
        ('T5 control C6 recorded RED', m_c6_red, ('VOID', 'VOID', 0, 0)),
        ('T6 existence recorded FAIL for all three cones', m_existence_fail, ('INCONSISTENT', 'UNDECIDED', 0, 0)),
    ]
    green = True
    for name, mut, exp in cases:
        T = dict(base)
        if mut:
            mut(T)
        st, lines, (br, nc, nw) = check(T, p3)
        got = (st, br, nc, nw)
        ok = got == exp
        green &= ok
        print('%s %s' % ('PASS' if ok else 'FAIL', name))
        print('     expected status=%s branch=%s cones=%d witnesses=%d' % exp)
        print('     got      status=%s branch=%s cones=%d witnesses=%d' % got)
        print('     derived: %s' % next(l.strip() for l in lines if l.strip().startswith('OP-weak => OP-strong:')))
        for l in lines:
            if l.startswith('  problem: '):
                print('     %s' % l.strip())
    # Digest gate: one byte changed in a copy of a record must stop the check before the semantic layer.
    r = dict(raw); r[Q2] = sub(raw[Q2].decode(), 'checks=21 failed=0', 'checks=21 failed=1', 1).encode()
    gb, _ = authenticate(r)
    ok = gb == ['%s: digest does not match runs/SHA256SUMS' % Q2]
    green &= ok
    print('%s T7 one byte of runs/q2_zf_cones.out changed: digest gate rejects (%s)' % ('PASS' if ok else 'FAIL', '; '.join(gb)))
    print('SELFTEST', 'GREEN' if green else 'RED')
    return 0 if green else 1


if __name__ == '__main__':
    if sys.argv[1:] == ['--self-test']:
        sys.exit(self_test())
    if sys.argv[1:]:
        sys.exit('usage: check_verdict.py [--self-test]')
    st, lines, _ = run_records()
    print('\n'.join(lines))
    print('CHECK', st)
    sys.exit(0 if st == 'CONSISTENT' else 1)
