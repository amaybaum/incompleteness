# Issue #1556: change map, REPORT r1 -> r2

Inputs: r1 = `verification/audits/foundations/oi-string-bridge-1556-20261125/REPORT.md` at a39ea0e3d6accd2721f90a8e3fda591a328aaa32; the independent review (PR #1563, comment 7166923987, verdict REVISE); the owner decision of 2026-11-25 (`amaybaum`); corpus at `main` e2e2a623265187a28ebec604ab8bcc672742888f. No repository, git, GitHub or manuscript writes were made.

**How the owner decision was read.** The scope item says "state the result for the infinite lattice with and a unit coefficient", which appears to have lost a word. It is read as: the infinite lattice, dimension d ≥ 2, with a coefficient alpha that is a unit modulo every prime factor of q. The condition d ≥ 2 is stated explicitly because d = 1 fails (r2 section 5.5).

## Owner-decision items

| Owner item | Change in r2 |
|---|---|
| Proof repair: verify the reviewer's argument step by step; address the shrinking transient and the false one-dimensional case | Section 5.3, Steps 1-7, writes out the reviewer's argument with each step checked. Step 1: CRT and p-adic reduction, with the reviewer's clarification. Step 3: integrality over the UFD R, λ a unit, P with at most two monomials, irreducibility including p = 2. Step 4: closed form and nonzero coefficients via the norm N ≠ 0. Step 5: a direct root-valuation argument, equivalent to the Newton polygon. Step 6, beyond the review: a transient bound T*_u = width_u(D)/c(u) + 3/2, derived from N ≠ 0 (the "Liouville-type" step, now proved on paper). Section 5.4 explains the shrinking transient; section 5.5 explains d = 1 (alpha^2 ≡ 1 gives λ = alpha·x in K; the glider has N = 0). Section 5.7 records the exact computations, with countercontrols |
| Scope: infinite lattice, unit coefficient; do not identify the rule with the general OI dynamics | Sections 5.1 and 5.2 state the rule and the conditions d ≥ 2, alpha a unit mod every prime factor of q, infinite lattice. The SM citation is corrected to line 224 (form), line 232 (alpha = 1/d at observer level) and line 106 (general f, not covered). "3 does not divide q" is identified as incidental. The S1 row (section 2), the Q1 row (section 4) and the section 6 row are restated for "this rule only" |
| Consistency: reconcile section 7 with section 5 | Section 7 defines T_max precisely: the tube, both initial slices inside it, initial time 0, every slice up to t inside it. With Step 6 proved, Corollary 2 gives T_max(r) ≤ 4r + 3 uniformly, and the reversed point source gives T_max of order r; the r1 question is therefore answered for this rule, subject to review. The cases left open are stated. The finite-torus caveat is kept (section 5.6) |
| Bridge assessment: S1' is the earliest unsupported OI -> strings step | Section 2 (S1, S1' rows and the conclusion), section 4 Q1, section 5.6 "Observer level", section 6 and section 7. Each place that concludes on S1 states that the result excludes confined excitations only for this microscopic linear rule and does not establish the absence of emergent string-like excitations at the observer level |
| Novelty: ELABORATING, not NEW | Section 5.8 |
| Manuscript findings: M1 conditions; narrow M10; remove M11, M12 from confirmed | Section 9.1 M1 (conditions added, section 7.5.4 point narrowed) and M10 (narrowed); section 9.2 lists M11 and M12 as not confirmed, with the reviewer's reasons. The section 1 table T-duality row no longer cites M12 as a finding |
| External literature: verified versus background | Section 0 "External literature" (verified with what was retrieved / [background]); section 3 R1 ('t Hooft: abstract-level claim verified, the rest [background]); M2, M12 and section 5.8 background markers |
| Change map; do not expand; no manuscript edits | This file. No new investigation beyond the computations needed to check the proof repair; no manuscripts edited |

## Review findings

| Review item | Disposition | r2 location |
|---|---|---|
| R1 (blocking): step 3 gap; reversed point source; d = 1 glider; reviewer's repair; transient "by the diameter" unproved | Applied. The repair is verified, and the gap (cancellation between the two terms) is named. The transient is now proved as T*_u ≤ diam_1(D) + 3/2 (Step 6), not as r1's unqualified "bounded by the diameter" | 5.2, 5.3, 5.4, 5.5, 5.6 |
| R2 (blocking): misattribution to "the OI update" with alpha = 1/d; SM line citations; result holds for unit alpha; alpha ≡ 0 fails | Applied. alpha ≡ 0 is used as a countercontrol (period 4, confined; 364 checker violations) | 5.1, 5.2, 5.7, 2 (S1), 4 (Q1), 6 |
| R3 (blocking): section 7 inconsistent with section 5; T_max undefined | Applied: T_max defined; question answered for this rule given Step 6 | 7 |
| R4 (non-blocking): finite-lattice condition; tube claim broader than step 5; p dividing L_z spot checks | Applied (scope items). Torus wrap-around condition in 5.6. The tube claim is narrowed to gcd(L_z, q) = 1 (Corollary 3, Step 7); finitely supported data in tubes are handled by Corollary 2. p dividing L_z is recorded as unproved, with this record's spot checks (163 runs, 0 violations) | 5.2, 5.3 Step 7, 5.6, 5.7 |
| R5 (non-blocking): ELABORATING; S1 carries little weight; S1' is substantive | Applied (owner items) | 5.8, 2, 6 |
| R6 (non-blocking): 't Hooft details beyond the abstract | Applied: marked [background] | 3 (R1), 0 |
| R7 (non-blocking): section 0 "nothing was written to the repository" | Applied: now describes the agent's own runs. "Nothing was computed" is also removed, because r2 ran computations | 0 |
| Review: support classes and earliest steps (S1' effective earliest; H3/H4/H5/H6 and R2/R3 confirmed) | S1' adopted; the rest needed no change | 2 |
| Review: Q6 could add Born-by-definition and the classical interface (#1558) | Not changed. This is a strengthening suggestion, not a factual correction inside the owner's items | — |
| Review: #1558 kernel identifiers exist on `main` | Recorded as confirmed by the review | 0 |

## Manuscript-finding verdicts

| Finding | Review verdict | r2 disposition |
|---|---|---|
| M1 | Confirmed, with conditions | 9.1: conditions added (Ooguri-Vafa conjecture and vacuum stability; "possibly unjustified" attributed to the review's reading). "Minimal Majorana case" made dependent on OI's light spectrum. The section 7.5.4 point narrowed to the AdS-criteria-applicability point. Line citations 403 and 431 added; the quoted sentence is from 7.5.5 |
| M2 | Confirmed | 9.1: wording tightened to "constrains a scalar potential" (review's reason). Otherwise unchanged |
| M3 | Confirmed | 9.1: added that the SM area scaling comes from range-1 locality plus the uniform state class (review's sentence). Otherwise unchanged |
| M4 | Confirmed | 9.1: "omits sigma" now cites SM line 90 |
| M5 | Confirmed | 9.1: lines 239 and 243 cited; the quote is completed ("not a testable one at present") |
| M6 | Confirmed | Unchanged in substance |
| M7 | Confirmed | 9.1: contrast references corrected to the abstract and sections 14.4/14.6 (r1 said 14.4/14.5); quote "the specific gauge group transports" |
| M8 | Confirmed | Unchanged |
| M9 | Confirmed, every sub-item | Unchanged except "(against Structure section 6.5)" on A5 |
| M10 | Partly confirmed | 9.1: narrowed. The claim that ch09 omits the extremal qualifier is dropped (ch09 line 224 already says "for extremal black holes"); the residual is "different horizons". ch09 line 328 cited for "consistency relation" |
| M11 | Not confirmed | Moved to 9.2 (not findings), with the reviewer's reason |
| M12 | Not confirmed | Moved to 9.2, with the reviewer's reason; section 1 T-duality row and section 8 limitation updated accordingly |

## Nits

| Nit | Disposition |
|---|---|
| "No such witness is exhibited" should end with "here" | Applied (section 1 table, section 3 R2; Structure line 536 cited) |
| Haar pushforward should cite SM line 809 | Applied (section 4 Q1) |
| "Unit speed" is the ℓ1 light cone; support grows by max_j \|u_j\| | Applied (5.1, 5.2) |
| H2 bound is on mutual information, not entropy; say so in the H5 contrast | Not changed. A clarification already implied by the H2 row, and not a correction inside the owner's items |

## Other changes and observations

- Section 0 now carries the section A.46 item 4 verification status and the remediation pointer.
- Section 8 (limitations) is updated. It also notes, without auditing it or adding it to section 9, that SM line 92 calls alpha = 1/d the "substratum normalisation" while SM line 232 places it at observer level. Section 5 does not depend on which reading is right.
- Computations run for the proof repair: three scratch scripts, not in the repository, listed with sha256 digests in r2 section 5.7. Exact integer arithmetic mod q, bounded runs; all in-hypothesis checks showed 0 violations, and every countercontrol flagged violations as required.
