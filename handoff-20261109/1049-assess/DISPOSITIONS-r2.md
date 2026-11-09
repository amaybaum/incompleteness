# ASSESS-1049 r2: dispositions of REVIEW-1049

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Maps each finding of
`review/REVIEW-1049.md` (sha256 `d56512e5533b497867b2f38f752dc7c86bf05f40e991ce80bb3bd36430765344`,
REVISE) to its change in `ASSESS-1049.md` r2, from r1 = `r1/ASSESS-1049.md`
(`9e60b0ae881bd6e1dd1bd307fb0baaecccba5b3ef5207f61178960f34ab0e040`). Every finding was checked
against its source at `fd539e15` (or the cited draft) before it was applied. The reviewer's
`rv_p1.py` and `rv_p2.py` were re-run with `python3 -I`: exit 0, byte-identical outputs. No finding
was refused.

| Finding | Verified against | Disposition | Change in r2 |
|---|---|---|---|
| B1 (§A.19/§A.25 search incomplete: Structure:219, :259, :301) | `git show fd539e15:papers/Structure.md` :217, :219, :259, :301; A5 N10; SM:94; `.tex` mirrors by `git grep` | Accepted | §2.1: Structure:219 and :259 added to the overstating sites; new paragraph "The one other corpus argument against non-affine rules" disposes of Structure:219/:301 (SM:94 correspondence not constructed; Structure:217 "posed for linear dynamics"; A5 N10 "Undetermined"; not evaluated on P1); "No corpus source" restated with that disposition; search scope extended to `.tex` and the new phrases; `.tex` mirror line list added. §0 item 1, §6 Q1 site lists extended. Owner-direction table GA8 (§2.3) |
| B2 (Q-NEXT "Equivalently" one-directional) | §A.34; Q-NEXT text | Accepted | §5: "Equivalently" removed; exclusion of P1's class stated as a necessary condition (screen), not sufficient; "P1 already reduces it to one function class" removed; "Why it is small" restated (a negative answer by P1-type witnesses; a passing principle still has to be shown to imply the base-point form). §0 item 6 |
| B3 ("b = 0 only at four sites" omits A5 D7, D12, D13, D15) | A5 rows D7 (:130), D12 (:135), D13 (:136), D15 (:138); SM:92; SM:1416 | Accepted | §3 table: rows D7 (not examined), D12, D13 (kernel under A5 as stated; affine extensions [D] in A5, unreviewed), D15 (conditional on A5 as stated). §3.1 restated "among the rows examined"; §0 item 4 list extended; §0 item 5 and §3.3 scope bullet: the one-sector statement covers the dynamical rows, not D12/D13/D15. Pressure test item 1 |
| N1 ((R-uni) forces κ ≡ 2; κ-general form) | rv_p1 part B (re-run) | Accepted | §2.1 (R-uni) bullet: κ = 2 consequence and the κ-independent form with the α = 1 witness; GA2 row "κ = 2 form; also the κ-general form" |
| N2 ("d ≥ 2" → "d = 2, 3") | P1 header and constructions | Accepted | §0 item 1, §2.1 consequence, §4 O-A, §7 F-1 and pressure test 4 now read "d = 2, 3"; §2.1 adds "No construction for d ≥ 4 is given" |
| N3 (owner Q2 extension labelled) | #1049 c.6624263637 as quoted in r1 | Accepted | New label [O-ext] in the header; §1 owner row; §2.1 (R-rel); §0 item 1; GA1 row |
| N4 (d = 1 holds at every odd q with reflection; "G linear" fails at composite q) | rv_p1 part E; paper argument (λ = −1 odd, reflection even, 2 a unit) | Accepted | §2.1 d = 1 bullet: proof via λ = −1 and reflection, at every odd q; odd-prime linearity of G stated separately; composite counts 27, 225 cited from rv_p1 E |
| N5 (short forms carry centre-free, NN, odd q) | §2.1 hypotheses | Accepted | §2.1 d = 1 heading and the two-read-variable and q = 2 remarks; §2.2 "New input"; §7 F-1 |
| N6 ("fails only when" follows from [A], not P3) | QP G1 induction | Accepted | Row 3a and §3.2: attributed to the contrapositive of the [A] induction |
| N7 (node 9 / PR §5 is separate availability) | `git show fd539e15:<QP>/DESIGN.md` :736–741 ("the available `t_{−a}` cancels its fixed offset and recovers L") | Accepted | Row 3b: cited as context only; G2's run difference rests on B0.1. §7 F-3 now cites node 6 for Q(iii) |
| N8 ("Step 3 fails in general" → "not available") | QP:362–369 | Accepted | Row 3b, "Without affinity": "Step 3's identity is not available" |
| N9 ("misattributes" too strong) | MECH-2:40, :532 as quoted by the review; BRIDGE r3 §10 | Accepted | §3.2 "Bearing on MECH-2:532": reviewer's wording ("attributes to nonlinearity what, under product priors, requires the same-colour read"), with the shared-term observation |
| N10 (α ≡ 1/d needs gcd(d, q) = 1) | κ = 2dα ≡ 2 ⇔ dα ≡ 1 | Accepted | §3.3 and §0 item 5: "odd q with gcd(d, q) = 1"; "at d = 3, q = 3 the locus κ ≡ 2 is empty" |
| N11 (SA-1(a) proposal presupposes "(a posit)" and drops form/symmetry/symplecticity) | SHARED r5 §9 SA-1(a) row ("the step's form, symmetry and symplecticity") | Accepted | §4 O-D: reviewer's wording plus the form, symmetric coefficients and symplecticity; SHARED cited at r5 |
| S1 (non-affinity at every prime q ≥ 5, one-line proof) | paper check; r2 G5 (exact, every prime 5 ≤ q < 200) | Accepted | §2.1 d = 3 bullet: proof added; §0 item 1; §8 paper list |
| Item 4 (P2(A), P2(C), P3 boundary; owner question) | review §4; coordinator instruction | Applied as directed: dropped as support | Rows 3a, 3b: [X: P2(A)], [X: P2(C)], [X: P3] removed, [A] only; §0 item 4 tags; §8 new "Non-evidential records" paragraph labelling P2(A), P2(C) and P3 as kept, unchanged, and not evidence; P2(B) kept as support (one-step identity, exhaustive). Owner question 4 removed |
| Register | — | No change needed | — |

## Owner-direction and cross-unit changes

| Source | Change in r2 |
|---|---|
| Owner direction 2026-11-09 (#1049): list every stated gauge assumption with its source, including the alphabet-size hypothesis at Structure:219/:301; say whether P1's class satisfies each; propose narrowings only where every stated assumption is satisfied, in the file only | New §2.3: inventory GA1–GA8 with sources and verdicts (GA1, GA2, GA3(a), GA6 yes; GA7 not excluded; GA3(b), GA4, GA5 no; GA8 undetermined); the per-site test; the proposals table (seven sites proposed; Structure:219, :259, :301 held on GA8). §0 item 2; §4 O-F; §6 Q1 asks whether the per-site reading is intended |
| Owner direction (all units): carriers, availability versus derivation, mixing versus full rules | §2 preamble (availability versus derivation); §3 preamble (configuration-level update; encoded-carrier rows named); row 3b "an encoded-carrier statement"; row 4 "a mathematically available complex structure, not an operation derived from OI". Mixing versus the full quantum rules does not arise in this unit's rows |
| Cross-unit: cite revisions by correct hash | Header: BRIDGE r3 `a5d7aad1…78c1`, REVIEW-UNIT1-r2 `3cdf7dc2…4eb3`, BRIDGE r2 `3905569b…103a`; QX3, QX4, SHARED at r5 with hashes (r1 said "r4" without hashes) |
| Cross-unit: FI-1 | Not cited in this unit; no change |

## Untraced changes (not from a review finding)

- **U1. BRIDGE r3 premise point.** §1 row and §3.2 updated: BRIDGE r3 now names the read pattern,
  not linearity. r1's "Correction to the #1211 premise claim" is retitled.
- **U2. F-7 (new finding).** SM:96, Sub:100, Sub:104 call the q-size → amplitude-scale entailment
  open; Sub:274 and Structure:301 answer it in the negative. Found while building §2.3.
- **U3. F-8 (new finding) and the Sub:272 proposal.** Sub:272's "a non-affine F induces
  amplitude-dependent emergent dispersion" is false for P1's class at the level of absolute
  amplitude (r2 G1, G2). §2.1 (R-site) notes that the circularity verdict holds with "affine"
  replaced by "uniformly covariant".
- **U4. Row 3d** cites QP node 6 explicitly, and notes that G_σ reads i ± 2 (from review §3).
- **U5. Pressure test item 5** (the inventory is the corpus's stated assumptions) added.
- **U6. Header, labels and §8** updated for r2 ([X] covers reviewer checks re-run here; new probe;
  re-runs; new reads).

## Probe added

`probes/r2_gauge_inventory.py` (sha256 `3ca85833990e1f35438296f7ef4d7ec3bad80311b2be53ac11221edd9eb2aef2`),
output `probes/r2_gauge_inventory.out` (`63c0c7f03f676f84a4786ee79369bc8ed108ad322c84bba0c4204e21db2855fa`),
exit 0. Exact modular arithmetic on one generic function and controls; iterates no dynamics and
computes no observable; imports no earlier probe. The reviewer-script re-runs were written to
`reassess/rerun-1049/`, outside the unit's directory (a first attempt that wrote beside the
reviewer's outputs and removed its temporaries was blocked by a safety check before it ran, so it left
nothing behind).
