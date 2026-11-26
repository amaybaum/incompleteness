# Changes r2 -> r3 (Issue #1556 report)

Input: REPORT-r2.md at commit 185a39639d84377c1371f71c2b50b37a209d488c. Trigger: the independent delta review of r2 (PR #1563 delta review, verdict ACCEPT-WITH-NITS) and the owner decision of 2026-11-25 (`amaybaum`), quoted in REPORT-r3 section 0. Nothing else in the report is changed; the observer-level scope sentences are kept as they stand. Each change is listed with its section, the r2 text and the r3 text.

## 1. title (revision label)

Old:

> # Issue #1556 (OI-STRING): paper-only bridge audit and dependency map (revision r2)

New:

> # Issue #1556 (OI-STRING): paper-only bridge audit and dependency map (revision r3)

## 2. §0 r3 status line (added) (status line recording r3 and the owner decision)

Old:

> (none; r3 inserts a new bullet after the Status bullet)

New:

> - **Revision r3:** a minimal revision after the independent delta review of r2 (PR #1563 delta review, verdict ACCEPT-WITH-NITS), made by owner decision (`amaybaum`, 2026-11-25): "Proceed with a minimal r3 addressing F2, F3 and the remaining nits. For F1, retain the transient bound and tube-exit corollary as independently reviewed mathematical results, explicitly distinguishing them from kernel-verified results. No additional formalization is required at this stage. Obtain a short independent delta review. Do not expand the investigation. The confinement result is now substantially better supported, but its physical scope remains limited to the specified microscopic dynamics. It does not exclude emergent observer-level string-like excitations." r3 changes only the status labels of section 5 (finding F1), the d = 1 glider wording (F2), the initial-data convention of the time-reversed point source (F3) and two wording nits; the agent that wrote r3 made no repository, git or GitHub writes, and r3 itself awaits the short independent delta review that the decision asks for.

## 3. §0 verification status (F1)

Old:

> the proposition of section 5 is a paper proof written for this record. It repairs r1's sketch along the reviewer's argument and adds a transient bound. It is not kernel-checked, and r2 has not yet had independent non-author review. The computations of section 5.7 are exact finite spot checks run in scratch scripts that are not in the repository; no conclusion rests on them alone. Accountable Issue: #1556. Remediation: independent review of section 5 and of the section 9 changes; the decision that would settle each gap is stated where the gap is stated.

New:

> the proposition of section 5 is a paper proof written for this record. It repairs r1's sketch along the reviewer's argument and adds a transient bound (Step 6) and the tube-exit and line-extended Corollaries 2-3. The whole of section 5.3, including Step 6 and Corollaries 2-3, has been checked on paper by one independent non-author review (PR #1563 delta review of r2). These are independently reviewed paper results, not kernel-verified results: no part of section 5 is kernel-checked. The computations of section 5.7 are exact finite spot checks run in scratch scripts that are not in the repository; no conclusion rests on them alone. Accountable Issue: #1556. Remediation: the PR #1563 delta review is the independent review of section 5 and of the section 9 changes; by owner decision no additional formalization is required at this stage, so kernel verification of section 5 remains open; the decision that would settle each other gap is stated where the gap is stated.

## 4. §2 S1 row (F1)

Old:

> (section 5; paper proof, unreviewed)

New:

> (section 5; paper proof checked by one independent review, PR #1563 delta review; not kernel-verified)

## 5. §4 table, row 1 (F1)

Old:

> Paper proof for the linear rule (unreviewed) plus corpus citations

New:

> Paper proof for the linear rule (checked by one independent review; not kernel-verified) plus corpus citations

## 6. §5.2 Corollary 2 (nit (Corollary 2 wording))

Old:

> then supp x(t) is not contained in Tube_r for some integer t ≤ 4r + 4.

New:

> then supp x(t) is not contained in Tube_r for every integer t ≥ 4r + 4.

## 7. §5.3 Step 6 (nit (sumset notation))

Old:

> The support of N lies in 2D + oct (Minkowski sum; oct contains 0 and supp P), so v(N) ≤ max{⟨a,−u⟩ : a ∈ 2D + oct} = 2h_D(−u) + c;

New:

> The support of N lies in the sumset D + D + ({0} ∪ {±e_j}) (the set {0} ∪ {±e_j} contains 0 and supp P), so v(N) ≤ max{⟨a,−u⟩ : a ∈ D + D + ({0} ∪ {±e_j})} = 2h_D(−u) + c;

## 8. §5.4 point source (F3)

Old:

> Run a point source to time T0 and use (x(T0+1), x(T0)) as data:

New:

> Run a point source, with initial data x(0) = 0 and x(1) = δ_0, to time T0 and use (x(T0+1), x(T0)) as data:

## 9. §5.4 width (F3)

Old:

> Here width_{e_1}(D) = 2T0, so

New:

> With this convention width_{e_1}(D) = 2T0 (it would be 2T0 + 2 for x(0) = δ_0), so

## 10. §5.5 glider (F2)

Old:

> gives N = 1 − (x + x^{-1})·x + x^2 = 0, hence A_+ = 0.

New:

> gives N = 1 − (x + x^{-1})·x + x^2 = 0, hence the coefficient of the root growing in direction −e_1 vanishes (for u = +e_1, where λ_+ = x, this is A_-, while A_+ = 1).

## 11. §5.6 (F1)

Old:

> Proved on paper here (unreviewed): (a)-(c) and Corollaries 1-3 under the stated conditions.

New:

> Proved on paper here and checked by one independent review (PR #1563 delta review of r2), not kernel-verified: (a)-(c) and Corollaries 1-3 under the stated conditions, including the transient bound of Step 6 and Corollaries 2-3.

## 12. §6 table (F1)

Old:

> | Paper proof (unreviewed) |

New:

> | Paper proof, checked by one independent review; not kernel-verified |

## 13. §7 reconciliation (F1)

Old:

> So the r1 question is answered for this rule, subject to independent review of section 5.

New:

> So the r1 question is answered for this rule, by a paper proof checked by one independent review (PR #1563 delta review), not by a kernel-verified result.

## 14. §8 limitations (F1)

Old:

> It follows the reviewer's repair for Steps 3-5 and adds Step 6. It is not kernel-checked, and r2 is unreviewed.

New:

> It follows the reviewer's repair for Steps 3-5 and adds Step 6. Steps 1-6 and Corollaries 1-3 have been checked by one independent review (PR #1563 delta review of r2); they are independently reviewed paper results, not kernel-verified results, and no additional formalization is required at this stage by owner decision.
