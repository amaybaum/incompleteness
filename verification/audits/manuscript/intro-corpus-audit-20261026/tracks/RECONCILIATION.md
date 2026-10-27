# Reconciliation of Tracks B, C and D (coordinator; WIP)

Inputs: `B-sc16/REPORT.md` (base `6bc2c4af`), `D-c2-sc16/REPORT.md` (base `6bc2c4af`), `C-consistency/REPORT.md` and its
independent review `C-consistency/REVIEW.md` (base `a5168789`). The only change between the two bases is #951, which made
single-line in-place edits and moved no line cited here.

## 1. SC-16: B and D agree

Both tracks independently refute the reading "(C1)–(C4), with any form of (C2), imply P-indivisibility on an accessible
window". The definitions behind that verdict match, the countermodels were reproduced, and both report the same
missing condition.

| Point | Track B | Track D | Agreement |
|---|---|---|---|
| Rooted family Γ_t, shared prior, P-divisibility on {0..n} | Main :137 = Lean `PDivisible`, `rootedMap` | same | identical definitions |
| Readings of P-divisibility tested | R1–R4 (stochastic divisor; realized kernel; TV-monotone all p, q; root pairs) | R1 by exact LP + Farkas | B is strictly broader; all four refuted |
| (C4) | history-level gap, full-support visible prior | same | identical |
| (C2) forms | structural (hidden laws differ at gap order); slow only as static bath | structural, coarse, slow under (EM) BSC(1/50), RoutedReadbackAtStorage | D broader on (C2); both refuted |
| 6-state [0,3,4,1,5,2] | reproduced (own code): divisible {0..5}, Farkas at 6 | found | agree, incl. RoutedReadbackAtStorage at K = 2 |
| LFSR family | m = 1–5 + x^7+x+1; paper proof | m = 1–4; paper proof | agree |
| HMM / (EM) family | λ_t exact to t = 9, divisible {0..9}; routed readback at storage already at K = 2 | λ_t to t = 4; F4 at K = 4 | agree (K = 2 implies K = 4 by monotonicity) |
| Sufficient extra condition | C4e or C4r in the window (Lean `c4e_implies_pIndivisible`, `c4r_implies_pIndivisible`, hypothesis only `C4e`/`C4r`) | C4r | agree; both sufficient, neither necessary |
| Theorems refuted | none (Main :137 concerns n with Γ_n = I; readback lemma and characterization concern conditional memory; kernel lemmas consistent) | none | agree |

Additional results in one track only, checked against the other for conflict:
- B, converse: under a full-support visible prior, P-indivisibility on {0..n} implies a (C4) gap at some order ≤ n−1
  (paper proof; exact, 0 violations in 10,612 windows). Does not conflict with D.
- B, special case: if the visible trajectory is a function of the root (for example, a point-mass μ_H), a gap at order k
  is Lean's `C4e (k+1) Γ`, so the family is P-indivisible on {0..k+1}. D's search used full-support priors and saw no
  such case; no conflict.
- D, (C2-structural): automatic in every bijective realization; persistence half of (C2) necessity unconditional;
  unstated K_Σ^n premise at Main :754. B does not address these; no conflict.

### Classification under the owner's three outcomes
1. **Lean theorem contradicted under its formal hypotheses:** none, in either track.
2. **Correct theorem, manuscript reading too strong:** the SC-16 sites. They read the readback lemma (Main :167) or the
   recurrence theorem (Main :137) as giving P-indivisibility within accessible windows.
3. **Proposed implication unproved, or refuted as stated:** "C1–C4 ⇒ accessible-window P-indivisibility" is refuted by
   exact countermodels. "A weaker, physically motivated condition derived from OI's dynamics yields in-window revival"
   remains open; C4e and C4r are sufficient but are added hypotheses.

## 2. A disagreement found in reconciliation: Track B's E13/E14 inherit a false premise

Track B's proposed E13 and E14 attribute recurrence-cycle P-indivisibility to "C1 and finiteness". That repeats
appendix-b :420 = FULL :6187: "C1 and finiteness establish P-indivisibility only in principle … the recurrence argument
uses C1 and finiteness alone". The merged Main theorem (:137, after SC-3) requires a non-permutation rooted map. That map
comes from two positive-probability histories with a common endpoint, or from a non-deterministic visible step (Main
:141). (C1) as Main :74 defines it does not supply one in general.

Exact countermodel (coordinator check, `xcheck/c1perm.py`, logic reproduced here):
- Model: V = H = {0,1}, μ_H = δ_0, step (x,0) ↦ (x,1), (x,1) ↦ (1−x,0).
- (C1) holds literally: all four states are reachable from the roots, and the visible successor of (c,h) depends on h.
- Yet Γ_t cycles I, I, swap, swap, I. Every Γ_t is a permutation, so the family is P-divisible on every window and at
  recurrence.

Under a full-support hidden prior, (C1) does yield a non-deterministic visible step, and hence recurrence-cycle
indivisibility by Main :141. So the correct form is "(C1) with a full-support hidden prior, or a non-permutation rooted
map, plus finiteness". This is an SC-3 propagation miss at appendix-b :420 = FULL :6187, and E14's "(from C1 and
finiteness)" must not be adopted as written. Main :174 ("from a non-permutation one-step witness and finiteness alone")
is correct as a sufficient condition.

Status: exact computation (coordinator) plus paper argument. This needs independent confirmation before it enters a PR.

## 3. Site inventory for SC-16: union of B, C-review and D

Sites asserting the overclaim:
- From all sources: GR :589 (C, C-review; not in B's list); Explainer :892; ch01 :121, :129, :133 (each = FULL
  :465, :473, :477); appendix-b :420 (= FULL :6187); ch04 :178 (= FULL :1297); Complexity :478, :503.
- Listed on #946: Complexity :418; Explainer :294; ch17 :178 (= FULL :4757).
- Additional sites from B: Complexity :461 (= ch15 :112 = FULL :4073), :462 (= ch15 :114 = FULL :4075); ch18 :72
  (= FULL :4890); ch15 :83 (= FULL :4044); Computation :144; Explainer :581, :619; ch01 :127 (= FULL :471).
- Additional sites from the C-review: Complexity :414; ch15 :16 (= FULL :3977); ch00 :101 (= FULL :337); SM :306 (SM
  :236 milder).

Borderline sites: appendix-b :92 (= FULL :5859); appendix-c :102 (= FULL :6348); ch13 :20 (= FULL :3519); ch17 :192
(= FULL :4771); GR :90; Explainer :280.

Selector item, not this class: Explainer :767 (B's E7: selectors contradicted by SM :226, :228, :236, :240). It belongs in
its own unit.

Correctly scoped, per both B and the C-review: Main :141, :174, :716; ch01 :89; Medicine :13; Bioinformatics :14;
Explainer :351. The Introduction at `4a260ca9` makes no accessible-window claim (C-review: L12, L96, L104, L174,
L230–232).

## 4. Dependency order for the correction PRs

1. **SC-5 (Pinsker / "backflow" terminology) and SC-16 share the root cause B identifies.** "Information backflow" is
   used both for conditional memory (Main :334) and for distinguishability revival (Main :121, :149). B's E23 renames
   the Main :167 lemma and rewrites :153; those are SC-5 sites. Order: settle the terminology first (SC-5, or an SC-16
   PR that carries E23 explicitly with SC-5 cross-referenced). Otherwise the SC-16 site rewrites would cite a lemma
   name about to change.
2. **SC-16 site corrections** follow, using one fixed wording for "conditional memory on accessible windows; P-indivisibility
   across the recurrence cycle; in-window revival (C4e/C4r) a further, sufficient condition". ch01 :133 also carries an
   S-1 (C3) edit; the C3 PR and the SC-16 PR must be sequenced on that line.
3. **C2 necessity (D4)** and **(EM) / Main :754 (D6)** are independent of SC-16's definitions. The C2-structural
   rewording (D1, E1–E9) changes how (C2) is described. It changes no definition SC-16 uses: B's countermodels hold for
   every (C2) form. It may land before or after SC-16, but not in the same PR.
4. **appendix-b :420 premise (section 2)** is corrected inside the SC-16 PR, because the same sentence is an SC-16 site.

## 5. Not yet reviewed
- B's proposed_edits.md (E1–E23) and D's E1–E13 are drafts. Each PR built from them gets its own independent review.
- Section 2's counterexample needs independent confirmation.
- The final regression grep (owner item 4) runs after the corrections land. It covers every SC-16 wording pattern
  across the Introduction, Main, companion papers, book chapters, FULL and the Explainer, and records positive and
  negative results.
