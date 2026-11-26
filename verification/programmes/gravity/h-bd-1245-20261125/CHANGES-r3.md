# #1245 H-BD report: change map r2 -> r3

Base: r2 at `a00e1dd61934c936697c8d6fc7ed9aaad6c33e13` (`verification/programmes/gravity/h-bd-1245-20261125/REPORT-r2.md`). Delta review of r2: PR #1564 comment 7167216051 (verdict ACCEPT-WITH-NITS; Findings 1 and 2, nits 1-8). P3 evidence: #1245 comment 6818702013, preserved as P3-EVIDENCE.md (body SHA-256 `8fadfe1bef1eb42b1d6469930ef1036a4dd60f9c1fd1cd4c544e1c34122ad573`).

Owner decision (amaybaum, 2026-11-25, coordinating session), quoted: "Preserve the exact P3 evidence in the version-controlled research package, with its provenance and original reference. Verify that the two classifications genuinely follow from that evidence. If either classification cannot be independently supported, narrow it or mark it unresolved. Ensure that all evidence supporting the final report will be present on `main` when the package lands. Obtain a bounded independent delta review and complete CI on the corrected head. Do not reopen the accepted mathematical results or expand the H-BD investigation."

Scope kept: no mathematical result, proof, number or condition of r2 is changed; no section outside those listed below is edited. No manuscript, Lean, premise, git or GitHub change.

***

## 1. Verification of the two classifications that rest on P3

### R1, "Contribution relative to P3": **narrowed** (linear case kept; general nonlinear case unresolved)

- *r2 classification.* "the conflict of H-BD with (xi) at site-local cuts with D-to-B dependence is already recorded in P3"; output class ELABORATING (P3).
- *P3 sentences relied on* (P3-EVIDENCE.md):
  - "It conflicts with Main ledger items (vii), (x), (xi) and (xiii) at site-local cuts with D→B dependence." (verdict on the preserved-list criterion).
  - "Under (vii), H-BD with τ_BD > 2Δt therefore holds iff L = 0."
  - "Local nonlinear rules need σ ≳ 1.4–4×10² for τ_BD ~ 1/H. This assumes σ = ln q_c (GR:98 and :160 state only σ ≤ ln q), H-link (GR:104) and one cell per step."
  - "Main derives no slow D→B influence time, and the selected model excludes one at site-local cuts."
- *What the text supports.* A conflict with the four ledger items jointly, at site-local cuts with D→B dependence, derived in the text for affine rules under (vii) (the linear dichotomy) and illustrated on the 1D ring. For local nonlinear rules the text records only a required size of σ under stated assumptions, not an exclusion, and it does not attribute any conflict to (xi) separately from (vii).
- *What it does not support.* That a conflict with (xi) for general nonlinear site-local rules without (vii), which is what R1 proves, is already recorded in P3. Whether P3's full check contained it cannot be determined: the check is not in the repository.
- *Outcome.* The "already recorded" statement is narrowed to the joint four-item conflict and the linear derivation. The output class ELABORATING (P3) is kept for the linear special case (q prime, L != 0), which the text records; for general nonlinear rules the class relative to P3 is marked unresolved. R1's mathematics is unchanged.

### R2(a), "reproduces the upper end of P3(d)'s threshold and is not new": **numerical agreement kept; "not new" unresolved**

- *P3 sentence relied on* (P3-EVIDENCE.md): "Local nonlinear rules need σ ≳ 1.4–4×10² for τ_BD ~ 1/H. This assumes σ = ln q_c (GR:98 and :160 state only σ ≤ ln q), H-link (GR:104) and one cell per step."
- *What the text supports.* R2(a)'s ln q ~ 420 agrees, to the precision P3 states, with the upper end 4×10² of that threshold, read with σ = ln q_c.
- *What it does not support.* That R2(a) reproduces P3's result: the text gives neither P3's derivation nor its counting of independent boundary sites, and its assumptions (σ = ln q_c, H-link, one cell per step) are not R2(a)'s ((viii), (ix), (x), (xi), disjoint read sets, N' ~ (A/4)/6). The agreement may be a common order-of-magnitude outcome rather than the same result.
- *Outcome.* The numerical agreement is kept and stated with P3's assumptions; "is not new" is marked unresolved. R2(a)'s derivation and numbers are unchanged. The sec. 4 R2 row (NEW) concerns the transfer (b)-(d) and is unchanged.

### Other statements about P3 checked against the preserved text (unchanged)

- Sec. 1 P3 row items (a)-(f): (a) "ε = Δt/τ_BD per substratum step" and "bijectivity of φ suffices"; (b) "ε ∈ {1 − 1/|im L|, 1}. If L ≠ 0, then ε ≥ 1 − 1/p ≥ 1/2", "at every B thickness and for every power φ^N", "holds iff L = 0"; (c) "ε = 1/2"; (d) as above; (e) "H-BD bounds T_ij only, not A.5's ‖D_V^{(D)}‖ or A.7's purity"; (f) "Cone form. It rests on Main:362 alone and has no parameter". Verdict line: "Posited with τ_BD ~ 1/H: ad hoc. With τ_BD left open: a conditional placeholder". Supported.
- Sec. 1 Routes 1 and 5: "Cone form ..." and "Independent fix of τ_BD | Not found." Supported.
- Sec. 2 "It agrees with P3" (linear dichotomy) and sec. 4 "CONFIRMING (extends P3)": supported by the dichotomy text and "Main derives no slow D→B influence time".

***

## 2. Changes, with old and new text

### Change 1. Title

- *Task item:* Status record.
- *Reason:* Revision label.

Old:

```text
revision r2
```

New:

```text
revision r3
```

### Change 2. Status, pin, sources: new bullet after "Review status"

- *Task item:* Status record.
- *Reason:* Status line recording r3 and the owner decision (task item: one status line).

Old:

```text
(none: new bullet)
```

New:

```text
- **Revision r3.** Revision r2 (commit `a00e1dd6`) was independently delta-reviewed at PR #1564 comment 7167216051 (verdict ACCEPT-WITH-NITS); the statements in this section and in sec. 7 that the r2 corrections are not yet independently reviewed describe r2 before that review. r3 applies the owner's decision (amaybaum, 2026-11-25, coordinating session), quoted: "Preserve the exact P3 evidence in the version-controlled research package, with its provenance and original reference. Verify that the two classifications genuinely follow from that evidence. If either classification cannot be independently supported, narrow it or mark it unresolved. Ensure that all evidence supporting the final report will be present on `main` when the package lands. Obtain a bounded independent delta review and complete CI on the corrected head. Do not reopen the accepted mathematical results or expand the H-BD investigation." The P3 comment is preserved verbatim in P3-EVIDENCE.md. r3 changes only the passages that rest on P3 (sec. 1 P3 row and off-`main` references; sec. 2 C-4; sec. 3 R1 contribution and R2(a) comparison; sec. 4 R1 output class), restores r1's qualifier in sec. 8 item 4 and applies citation nit 6 of the delta review; no mathematical result is changed. The r3 changes are not yet independently reviewed.
```

### Change 3. Status, pin, sources: "Review status" bullet

- *Task item:* (e) nit 6.
- *Reason:* Delta-review nit 6: owner decision cited with its comment id and time (sec. A.42 item 7).

Old:

```text
bounded revision decision (amaybaum, 2026-11-25: "Proceed
```

New:

```text
bounded revision decision (amaybaum, #1245 comment 7166798992, 2026-11-25T15:24:39Z: "Proceed
```

### Change 4. Status, pin, sources: "Sources read"

- *Task item:* (e) nit 6.
- *Reason:* Delta-review nit 6, second part: "all 11 comments" predates comment 7166798992; the comments read for r2 and r3 are named.

Old:

```text
- #1245 body and all 11 comments.
```

New:

```text
- #1245 body and all 11 comments (as read for r1); comment 7166798992 (owner decision on r2); comment 6818702013 re-read in full for r3 (P3-EVIDENCE.md).
```

### Change 5. Sec. 1, table row P3, column "Where"

- *Task item:* (a).
- *Reason:* Consequence of (a): the P3 comment is now in the package; the full check is stated as not in the repository (search result in P3-EVIDENCE.md).

Old:

```text
| #1245 c.6818702013; the full check is session material, not on `main` |
```

New:

```text
| #1245 c.6818702013, preserved verbatim in P3-EVIDENCE.md; the full check it mentions is session material and is not in the repository |
```

### Change 6. Sec. 1, "Off-`main` references", P3 bullet

- *Task item:* (a).
- *Reason:* Delta-review Finding 1; owner decision. P3 reclassified from provenance to support for the statements about what P3 records, preserved in P3-EVIDENCE.md so that it is on `main` when the package lands; provenance for the mathematics; the full check provenance only and not found.

Old:

```text
- P3 (#1245 c.6818702013; its full check is session material): **provenance** for R1 and R2. R2(a) is derived in full below; the statement that it reproduces P3(d)'s upper threshold is a comparison, not a premise. R1's relation to P3 (sec. 3, R1, "Contribution") is a claim about what the P3 comment records, attached only to the output classification, not to any derivation. The negative finding C-4 (sec. 2) rests on P3(e), which is off `main` (**support off `main`**). This report does not re-derive C-4 and uses it as no premise; it is listed in sec. 2 as P3's finding only.
```

New:

```text
- P3 (#1245 c.6818702013): **support** for the statements of this report about what P3 records, carried in this package as P3-EVIDENCE.md (the exact comment body, its SHA-256 and its provenance), so that it is on `main` no later than this report. These statements are limited to what that text records: R1's contribution relative to P3 and its output class (sec. 3, R1; sec. 4), narrowed in r3; R2(a)'s comparison with P3(d) (sec. 3, R2(a)), whose novelty relative to P3 is unresolved in r3; C-4, which sec. 2 reports as P3's finding and this report does not re-derive; and the P3 row, Routes 1 and 5, the agreement of GR:128 with P3 (sec. 2) and "extends P3" (sec. 4), each checked against the preserved text. For the mathematics P3 is **provenance**: R1 and R2 are derived in full below and use no P3 content as a premise. The full check that the comment calls session working material was not found in the repository (all branches and their history searched); no claim of this report uses it, so it is **provenance** only.
```

### Change 7. Sec. 2, "Negative findings that stand", C-4 bullet

- *Task item:* (c).
- *Reason:* Delta-review Finding 1: assertion removed; C-4 reported as P3's finding, with the preserved text as its support; not re-derived.

Old:

```text
- H-BD does not bound channel or purity terms (C-4; P3(e), off `main`, not re-derived here).
```

New:

```text
- P3 reports that H-BD does not bound channel or purity terms (C-4: an update with eps = 0 whose two-step V-channel fully dephases under Main:280's rho_H = I/m; P3(e), preserved in P3-EVIDENCE.md, not re-derived here).
```

### Change 8. Sec. 3, Q1, R1, "Contribution relative to P3"

- *Task item:* (b).
- *Reason:* Classification check (b) for R1: narrowed to what the preserved text records; nonlinear part marked unresolved.

Old:

```text
- *Contribution relative to P3.* Under (xi) the conflict of H-BD with (xi) at site-local cuts with D-to-B dependence is already recorded in P3 (#1245 c.6818702013, provenance), and R2(a) below gives a far stronger quantitative threshold. What R1 adds is the clean, exact 1/q threshold for general nonlinear site-local rules at the single GR cut, together with the non-translation-invariant case below. Output class: ELABORATING (P3).
```

New:

```text
- *Contribution relative to P3.* The preserved P3 text (P3-EVIDENCE.md) records, in its verdict on the preserved-list criterion for H-BD, "It conflicts with Main ledger items (vii), (x), (xi) and (xiii) at site-local cuts with D→B dependence": a conflict with the four items jointly. The derivations it records are the linear dichotomy for affine phi under (vii) ("Under (vii), H-BD with τ_BD > 2Δt therefore holds iff L = 0") and the 1D-ring example; for local nonlinear rules it records only a required size, "σ ≳ 1.4–4×10² for τ_BD ~ 1/H", under the assumptions σ = ln q_c, H-link and one cell per step. It does not record a conflict with (xi) for nonlinear rules without (vii). R2(a) below gives a far stronger quantitative threshold. What R1 adds is the exact 1/q threshold for general nonlinear site-local rules at the single GR cut, under (xi) without (vii), together with the non-translation-invariant case below. Output class: ELABORATING (P3) for the linear special case (q prime, L != 0), which P3 records; for general nonlinear rules the class relative to P3 is unresolved, because the preserved text does not record that case and P3's full check is not available.
```

### Change 9. Sec. 3, Q1, R2(a), last sentence

- *Task item:* (b).
- *Reason:* Classification check (b) for R2(a): numerical agreement kept; "is not new" marked unresolved.

Old:

```text
This reproduces the upper end of P3(d)'s threshold and is not new.
```

New:

```text
The value ln q ~ 420 agrees with the upper end of the threshold that P3 records for local nonlinear rules ("σ ≳ 1.4–4×10² for τ_BD ~ 1/H", assuming σ = ln q_c, H-link and one cell per step; P3-EVIDENCE.md). The preserved text does not give P3's derivation, so whether R2(a) reproduces P3's result under the same hypotheses, and hence whether it is new relative to P3, is unresolved; R2(a) is derived in full here and does not rest on P3.
```

### Change 10. Sec. 4, row "R1 exact threshold at the single GR cut", output class

- *Task item:* (b).
- *Reason:* Propagation of change 8 within the report (sec. A.25).

Old:

```text
| ELABORATING (P3): adds the clean 1/q threshold |
```

New:

```text
| ELABORATING (P3) for the linear case (q prime, L != 0); relative to P3 unresolved for general nonlinear rules (sec. 3, R1) |
```

### Change 11. Sec. 8 item 4

- *Task item:* (d).
- *Reason:* Delta-review Finding 2: r1's qualifier "Under the motion reading" restored on the item-3-map sentence; r2's framing as a reviewer check, not a manuscript candidate, kept. Chosen over listing the change, because restoring removes the unreviewed new claim instead of adding it to the record.

Old:

```text
Under the influence reading, it inherits H-BD's status. Whether item 3's R2 map (deviation 1/M as t/tau_B^D goes to 0) bears on the displayed open order \|\|D_V^(D)\|\| = O(tau_S/tau_B^D) is a check for a reviewer, not a manuscript candidate.
```

New:

```text
Under the motion reading, whether item 3's R2 map (deviation 1/M as t/tau_B^D goes to 0) bears on the displayed open order \|\|D_V^(D)\|\| = O(tau_S/tau_B^D) is a check for a reviewer, not a manuscript candidate. Under the influence reading, it inherits H-BD's status.
```

***

## 3. Delta-review items

| Item | Disposition |
|---|---|
| Finding 1 (P3 attachment unclassified; C-4 asserted) | Applied: changes 5, 6, 7; classifications verified in sec. 1 above (changes 8, 9, 10). |
| Finding 2 (sec. 8 item 4 change outside the r2 change map) | Applied by restoring r1's qualifier (change 11). |
| Nit 1 ("and 6" in R1 without (xi)) | Not applied: outside the passages edited in r3. |
| Nit 2 (R1 step 2, "read component") | Not applied: outside the passages edited in r3. |
| Nit 3 (Setting, "site-wise gauge" versus Main's "gauge") | Not applied: outside the passages edited in r3. |
| Nit 4 (R2(a) N' ~ (A/4)/6 versus about (A/4)/11 under spacing-3 thinning) | Not applied: it would change R2(a)'s stated number (eps* looser by a factor of about 2-4), which the owner decision excludes; the reviewer notes ln q ~ 420 is unchanged, so the comparison in change 9 is unaffected. |
| Nit 5 (E3-VOL, appendix-c:106 wording) | Not applied: outside the passages edited in r3. |
| Nit 6 (owner decision citation; "all 11 comments") | Applied: changes 3 and 4. |
| Nit 7 (two meanings of "R2" in the Q4 A.7 row) | Not applied: the collision is in the Q4 row, which r3 does not edit; change 11 keeps r2's wording "item 3's R2 map" in sec. 8 item 4. |
| Nit 8 (PR #1564 description stale) | Not applied: outside the report; a description update is a GitHub write under sec. A.49, not made here. |

***

## 4. Not changed, noted

- The sentences in the "Review status" bullet and in sec. 7 (first bullet) that say the r2 corrections are not yet independently reviewed are left as r2 wrote them; the new r3 status line records the delta review and states that those sentences describe r2 before it.
- The r3 owner decision is quoted with author, date and session; no #1245 comment carrying it was found at retrieval (latest #1245 comment: 7166798992, 2026-11-25T15:24:39Z), so its comment id is not cited.
- Section 1's P1, P2, P4, P6 and P8 references keep their r2 class (provenance).
