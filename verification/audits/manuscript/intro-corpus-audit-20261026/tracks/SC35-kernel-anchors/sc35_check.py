#!/usr/bin/env python3
"""SC-35 check: the kernel declarations Main now cites, read against the prose that cites them.

Run from the repository root:  python3 -I verification/audits/manuscript/intro-corpus-audit-20261026/tracks/SC35-kernel-anchors/sc35_check.py

1. Every identifier SC-35 cites is declared in the module named, and has a `#print axioms` line.
2. Each cited theorem's statement (flattened) carries the hypotheses and conclusion the prose states.
3. The census registry carries the four families as current, and every anchor is present in Main.
4. Re-grep: the superseded phrasings are gone and the new statements are present, with counts.
5. No Lean file differs from the base commit.
"""
import json
import os
import re
import subprocess
import sys

BASE = '0d917665d32287e5d0ce649012175f2c7bf75b09'
OI = 'verification/lean-mathlib/OIBridge/'
ok = True


def check(cond, msg):
    global ok
    print(('  PASS  ' if cond else '  FAIL  ') + msg)
    ok &= bool(cond)


def flat(s):
    return ' '.join(s.split())


def statement(mod, name):
    src = open(OI + mod + '.lean', encoding='utf-8').read()
    m = re.search(r'^theorem ' + re.escape(name) + r'\b(.*?)\s:=(?: by)?[ \t]*\n', src, re.S | re.M)
    return flat(m.group(0)) if m else None, src


CITED = {
    'RecurrenceHorizon': ['pIndivisible_of_rooted_identity_return_of_overlap',
                          'c4r_of_rooted_identity_return_of_overlap',
                          'pIndivisible_of_identity_return_of_overlap'],
    'PhysicalC4Discharge': ['routed_forces_return_indivisibility', 'routed_forces_indivisible_somewhere'],
    'PhysicalC4StorageReadback': ['routedAtStorage_forces_return_indivisibility',
                                  'routedAtStorage_forces_indivisible_somewhere',
                                  'storageReadback_not_implies_routedReadback',
                                  'routedReadback_not_implies_storageReadback'],
    'RootedClassification': ['pper_of_finiteRootedRealizable', 'rootedMap_periodic', 'rootedMap_zero'],
    'RootedClassificationAllTime': ['pper_has_responseRealization', 'finiteRootedRealizable_iff_pper'],
    'EquivalenceChain': ['isPermMatrix_of_stochastic_inverse'],
}
print('1. declarations and axiom reports')
stmts = {}
for mod, names in CITED.items():
    for n in names:
        st, src = statement(mod, n)
        stmts[n] = st
        has_ax = re.search(r'^#print axioms (?:OIBridge\.)?(?:\w+\.)*' + re.escape(n) + r'\s*$', src, re.M)
        check(st is not None and has_ax is not None, f'{mod}.{n}: declared, #print axioms present')

print('2. statements carry what the prose says')
EXPECT = {
    'pIndivisible_of_rooted_identity_return_of_overlap': [
        '(R : RootedRealization V H)', '(hsn : s < n)', '(hI : rootedMap R n = 1)', '(hab : a ≠ b)',
        '(hax : 0 < rootedMap R s a x)', '(hbx : 0 < rootedMap R s b x)', 'PIndivisibleWithin n (rootedMap R)'],
    'pIndivisible_of_identity_return_of_overlap': [
        '(hstoch : IsRowStochastic (Γ s))', '(hI : Γ n = 1)', 'PIndivisibleWithin n Γ'],
    'routed_forces_return_indivisibility': [
        '(h : RoutedReadback K R)', '∃ s, s < K ∧ ∀ n, s < n → rootedMap R n = 1 →',
        'PIndivisibleWithin n (rootedMap R)'],
    'routed_forces_indivisible_somewhere': ['(h : RoutedReadback K R)', '∃ n, PIndivisibleWithin n (rootedMap R)'],
    'routedAtStorage_forces_return_indivisibility': [
        '(h : RoutedReadbackAtStorage K R)', '∃ s, s < K ∧ ∀ n, s < n → rootedMap R n = 1 →'],
    'routedAtStorage_forces_indivisible_somewhere': [
        '(h : RoutedReadbackAtStorage K R)', '∃ n, PIndivisibleWithin n (rootedMap R)'],
    'storageReadback_not_implies_routedReadback': [
        '¬ ∀ (K : ℕ) (R : RootedRealization (Bool × Bool) Bool), RoutedReadbackAtStorage K R → RoutedReadback K R'],
    'routedReadback_not_implies_storageReadback': [
        '¬ ∀ (K : ℕ) (R : RootedRealization Bool (Bool × Bool)), RoutedReadback K R → RoutedReadbackAtStorage K R'],
    'pper_of_finiteRootedRealizable': ['(h : FiniteRootedRealizable (V := V) Γ) : PPer Γ'],
    'pper_has_responseRealization': ['(hΓ : PPer Γ)', '∀ t, rootedMap R t = Γ t'],
    'finiteRootedRealizable_iff_pper': ['FiniteRootedRealizable (V := V) Γ ↔ PPer Γ'],
}
for n, parts in EXPECT.items():
    for p in parts:
        check(stmts[n] is not None and p in stmts[n], f'{n} contains {p!r}')
# the definitions the prose transcribes
cr = flat(open(OI + 'CausalReadback.lean', encoding='utf-8').read())
for p in ['step : V × H ≃ V × H', 'prior_nonneg : ∀ h, 0 ≤ prior h', 'prior_sum : ∑ h, prior h = 1',
          'def PDivisible (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop := ∀ s t : ℕ, s < t → t ≤ K → ∃ Λ : Matrix V V ℝ, IsRowStochastic Λ ∧ Γ t = Γ s * Λ']:
    check(p in cr, f'CausalReadback carries {p!r}')
check('full' not in re.search(r'structure RootedRealization.*?prior_sum', cr).group(0).lower(),
      'RootedRealization imposes no support condition on the prior')
rc = flat(open(OI + 'RootedClassification.lean', encoding='utf-8').read())
check("def PPer (Γ : ℕ → Matrix V V ℝ) : Prop := Γ 0 = 1 ∧ (∀ t : ℕ, IsRowStochastic (Γ t)) ∧ PeriodicFamily Γ" in rc,
      'PPer is root identity, row-stochastic at every time, periodic')
check('def PeriodicFamily (Γ : ℕ → Matrix V V ℝ) : Prop := ∃ M : ℕ, 0 < M ∧ ∀ t : ℕ, Γ (t + M) = Γ t' in rc,
      'PeriodicFamily is a positive period')
d1 = flat(open(OI + 'PhysicalC4Discharge.lean', encoding='utf-8').read())
d2 = flat(open(OI + 'PhysicalC4StorageReadback.lean', encoding='utf-8').read())
for p in ['a ≠ b ∧ 0 < w ∧ w ≤ s ∧ s < t ∧ t ≤ K',
          '(∃ h : H, 0 < R.prior h ∧ ((⇑R.step)^[w] (a, h)).2 ≠ ((⇑R.step)^[w] (b, h)).2)',
          '0 < rootedMap R s a x ∧ 0 < rootedMap R s b x', 'rootedMap R t a ≠ rootedMap R t b',
          "((⇑R.step)^[t - s] (x, h)).1"]:
    check(p in d1, f'RoutedReadback carries {p!r}')
check('fun h => (if ((⇑R.step)^[s] (a, h)).1 = x then R.prior h else 0) / rootedMap R s a x' in d1,
      'rootedPosterior is the law of the initial seed given X_s = x, X_0 = a')
check('fun k => (∑ h : H, if (⇑R.step)^[s] (a, h) = (x, k) then R.prior h else 0) / rootedMap R s a x' in d2,
      'rootedStatePosterior is the law of H_s given X_s = x, X_0 = a')
check('theorem core_routedReadbackAtStorage_two' in d2 and 'RoutedReadbackAtStorage 2 R ∧ ∀ K, ¬ RoutedReadback K R' in d2,
      'CS5-a: the core satisfies the storage reading at K = 2 and the seed reading at no K')
check('theorem sep_routedReadback_two' in d2 and 'theorem sep_not_routedReadbackAtStorage_two' in d2,
      'CS5-b: the separating carrier satisfies the seed reading at K = 2 and not the storage reading at K = 2')

print('3. census registry')
reg = json.load(open('verification/lean-manuscript-census.json', encoding='utf-8'))
main = flat(open('papers/Main.md', encoding='utf-8').read())
for prefix in ('recurrence horizon:', 'physical C4 discharge:', 'physical C4 round 2:', 'rooted classification:'):
    fam = [f for f in reg['families'] if f['name'].startswith(prefix)]
    check(len(fam) == 1 and fam[0]['status'] == 'current' and fam[0]['manuscript'], f'{prefix} current, anchored')
    for a in fam[0]['manuscript']:
        check(a['file'] == 'papers/Main.md' and a['anchor'] in main, f'   anchor present: {a["anchor"][:70]!r}')
check('papers/Introduction.md' not in reg['manuscripts'], 'manuscripts list unchanged (no tool reads it)')

print('4. re-grep')
corpus = ['papers/' + f for f in sorted(os.listdir('papers')) if f.endswith('.md')] + \
         ['book/' + f for f in sorted(os.listdir('book')) if f.endswith('.md')] + ['verification/ROADMAP.md']
texts = {f: flat(open(f, encoding='utf-8').read()) for f in corpus}
GONE = ['its composition with P-divisibility and the step from two positive-probability histories',
        'exact gluing for recurrent target families', 'Recurrent-family gluing and pre-recurrence-window',
        'recurrent-family gluing and pre-recurrence window approximation open']
NOW = ['**Theorem (overlap and return).**', '*Routed readback.*',
       'exact all-time gluing for recurrent families of multi-time laws',
       'recurrent multi-time-law gluing and pre-recurrence window approximation open',
       'Recurrent multi-time-law gluing and pre-recurrence-window approximation remain open']
for g in GONE:
    n = sum(t.count(g) for t in texts.values())
    check(n == 0, f'gone: {g!r} ({n} hits)')
for g in NOW:
    hits = {f: t.count(g) for f, t in texts.items() if g in t}
    check(sum(hits.values()) == 1, f'present once: {g!r} {hits}')
for ident in ('pIndivisible_of_rooted_identity_return_of_overlap', 'routedAtStorage_forces_indivisible_somewhere',
              'routed_forces_indivisible_somewhere', 'finiteRootedRealizable_iff_pper'):
    hits = {f: t.count(ident) for f, t in texts.items() if ident in t}
    print(f'  count {ident}: {hits}')

print('5. Lean unchanged')
diff = subprocess.run(['git', 'diff', '--name-only', BASE, '--', 'verification/lean-mathlib', 'verification/lean/*.lean'],
                      capture_output=True, text=True).stdout.split()
check(diff == [], f'no Lean file differs from {BASE[:8]} ({diff})')

print('\nsc35_check: ' + ('OK' if ok else 'FAILED'))
sys.exit(0 if ok else 1)
