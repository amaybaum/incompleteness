# QPHEN Phase 1 r7: dispositions of `review/REVIEW-PHASE1-r6.md` (`86b69048…`)

## Scope and standing

- Paper only and model-written. There are no repository, git or GitHub writes.
- No computation is run on any OI mechanism. The one new check, `review/probes/p13_r7_meter_supply.py`, is an exact
  check of paper claims on generic objects (affine maps of `F_2⁴` and `F_3⁴`; "Allowed: generic checks", #1210
  c.6739250392, owner, 2026-11-09). It imports no earlier probe and uses only the standard library.
- Q-C2-1's D19–D23 remain separate. No freeze, dispatch, construction or implementation approval follows from this
  revision.
- **Inputs.**
  - The r6 review, sha256 `86b69048d3bb53231b914e6638ebae960f4e5bcd49beb933bec35107bb54ec18` (verified before
    reading), verdict REVISE: blocker B1 (r6), must-fix nits N1–N4, precision nits N5–N11, optional items.
  - Its probe `p12_r6rev_checks.py` (`876497e1b442b13c…`). Re-run with `python3 -I` from a separate directory: exit 0,
    37 of 37 checks pass, output byte-identical to `p12_r6rev_checks.out` (`a09612867ffa8743…`).
  - The owner rules still in force (last section).
- **Corpus check.** `git fetch origin main` (no depth, gc or prune): `origin/main` =
  `fd539e150759a6ea51ab279aeeac80fc06050ade`; `git show fd539e15:papers/Main.md` equals `main_fd.md` (`6144cd4a…`).
  Read at that commit before applying any finding: AP1
  (`verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md`):278-362, in particular SA-1(a),
  (a′), (c) at :281-299 and the mechanism at :320-323 ("Given (c) and N2, that slot is unknown and uniform, so the
  shift is a disturbance. With a known meter slot the shift would be a known displacement and no disturbance.");
  Main:726 (the posit ledger, items (i)–(xii) as quoted in the SA-1(a) row).
- **The r6 texts** are copied unchanged into `r6/`:

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `01f8a44d64334d01923ee6c499dd4f59df9be341c0035148573e35bcd6e421da` |
  | `QX4-INCOMPATIBILITY-LG.md` | `df4def7192b7d8226eb339330fc764a91a2ec062d42aa58748e24afae6647e0e` |
  | `QX6-BELL-CHSH.md` | `1243cea4e052a48730969f9a6f2f161ea67754a502088af396fa2ac78a9d2874` |
  | `SHARED-MECHANISM.md` | `67b3f5b54f25fdba3f65dedb9346c892d8833223711b8edb03f8352c2ea66327` |
  | `DISPOSITIONS-r6.md` | `468d188d56f7506627d637801d731c8c29f890ecf87580e60363d75b56e536a7` |

  These match the hashes the r6 review lists. `DISPOSITIONS-r6.md` is a record and is not edited (also kept unchanged
  at the top level).

## The new check

`p13_r7_meter_supply.py` (exact integer arithmetic mod `q`; run with `python3 -I` from a separate directory; exit 0;
27 of 27 checks pass; output `p13_r7_meter_supply.out`). Definitions match Q4-P20's hypotheses: SA-1(c) meter laws are
uniform on a whole line `{ℓ = k}` for every nonzero known functional `ℓ` (`m`, `m′` and `m + m′` over `F_2`; four
projective classes over `F_3`), sharp laws are points, and the carrier's `x` ranges over all of `F_q`.
1. `Sp(4, F_2)` (720) by filtering `MᵀJM = J` over all 65,536 matrices; the 648 location-preserving symplectic linear
   parts of `F_3⁴` by filtering 531,441 candidates; the bracket-preservation identity `MJ⁻¹Mᵀ = J⁻¹` used in Q4-P20's
   proof, on every enumerated `M`.
2. **Q4-P20.** Under every SA-1(c) law, readable recorders exist and none has `K_null = id`: over all 11,520
   affine-symplectic maps of `F_2⁴` (4,608 readable per law), the 384 location-preserving ones (192 per law), and the
   17,496 location-preserving affine-symplectic maps of `F_3⁴` (11,664 per law). Countercontrol: under every sharp law
   some readable recorder has `K_null = id` (144 of 288 at `F_2`, location-preserving; 5,184 of 15,552 at `F_3`). With
   both meter slots unknown, no location-preserving map records readably.
3. **Q4-D8.** The reciprocal coupling (`x ← x − m′`, which is `x + m′` over `F_2`) is symplectic and
   location-preserving at `q = 2, 3`; with a sharp meter `(0, 0)` it records readably with `K_null = id`; with an
   SA-1(c) meter (`m` known) it records readably with `K_null ≠ id`.
4. Countercontrol on the symplectic hypothesis: the copy coupling `m ← m + c` is not symplectic and, under an SA-1(c)
   meter, records readably with `K_null = id`.

p13 reproduces p12 (2) at p12's scope (location-preserving maps of `F_2⁴`, a known meter slot), so Q4-P20's counts
are X there; the `m + m′` laws, the non-location-preserving maps of `F_2⁴` and the `F_3⁴` counts are writer-only and
are marked computation-supported. Q4-P20 itself rests on the paper proof [A, unreviewed].

## Blocker

| finding | verified against | change made (r7) |
| --- | --- | --- |
| **B1 (r6)** (the M16 route omits the meter's supply condition SA-1(c)) | yes. AP1:320-323, verbatim. The reciprocal coupling `(c, x, m, m′) ↦ (c, x + m′, m + c, m′)` was checked by hand: symplectic over `F_2` (the six basis pairings), location-preserving, meter write `m + c`, and with `m′ = 0` on the silent branch `x′ = x`. p12 (2) re-run, and reproduced independently by p13 (2)–(3). `K_null` is defined on the silent branch of a run (QX-4 §1 validation layer; (H3)), so it concerns the support of the meter's ready law | **1. Q4-P19 (ii)**: the proved statement is kept; the gloss now reads "This is `K_null ≠ id` on the silent branch when the meter's ready law gives positive weight to such a state, as an SA-1(c) meter does for every map that records readably (Q4-P20). With a sharp meter it need not be: the reciprocal coupling with meter `(0, 0)` records occupation and has `K_null = id` (Q4-D8)." **2. The SA-1(c) form, proved on paper**: new **Q4-P20** [A: paper proof, unreviewed; X at p12's scope; computation-supported beyond it by p13 alone]. Hypotheses: affine-symplectic `T` on `F_q⁴`, `q` prime; meter uniform on `{ℓ = k}` for any nonzero known functional `ℓ` (SA-1(c), as AP1:297-299 states it: "exactly one known linear functional"); `x` takes at least two values on each branch; `T` records readably (a linear meter functional with a `c`-only value differing between branches). Proof: symplectic maps preserve the bracket of linear functionals; readability gives `f∘M = αc + λℓ` with `α ≠ 0`; `K_null = id` gives `x∘M = rc + x + ρℓ`; then `0 = {x, f} = α{x, c}`, a contradiction. This follows the review's sketch (readability pulls the read functional back to `c` plus the known functional; symplecticity then forces the unknown slot into `x`'s row) and covers every known functional, not only a known slot. The proof uses neither location preservation nor `q = 2`; it uses that the known functionals commute, which fails for a sharp meter (`{m, m′} ≠ 0`). **3. §8 ledger**: new disproved entry **Q4-D8**: the refuted claim (the unconditional M16 form); the counterexample (reciprocal coupling, sharp meter `(0, 0)`); the membership line (affine, symplectic with the basis pairings stated, location-preserving, records occupation, sharp meters admitted by `A_4` and ABL-SA1c, `K_null = id`); AP1:320-323; the 144 / 288 counts; the restatement (Q4-P20), with the forms for non-affine couplings and for meter supplies outside Q4-P20's hypotheses open unless separately established (Q4-O3). **4. SHARED §1 M16** type cell, **§2 M16 × QX-4** cell and **§9's null-result row**: column (ii) "conditional on SA-1(a)'s posits and on SA-1(c), with N2, for the meter's ready cells …; SA-1(c) has no identified support other than agreement with QM (its row), so this route gives no QM-independent support. It is a further consequence of SA-1(c), in the manner of AW-QX4-1, not a justification of SA-1(c) …; none identified for non-affine couplings (open)". Standing: "a hypothesis under test (O1); **QM-only**". The §2 cell reads "for affine-symplectic location detectors a consequence of SA-1(c), Q4-P20; QM-only, §9". **5. QX-4 R4.9**: both sentences carry "when the meter's conjugate slot is unknown (SA-1(c))", with the sharp-meter case (Q4-D8) and Q4-P20 cited. **6. SHARED T2** and **QX-4 A4.4's Consequence**: "the reciprocal kick from the meter's unknown slot (SA-1(c); Q4-P20)", and "With a sharp meter that kick is a known displacement and `K_null = id` (Q4-D8)". **7. DISPOSITIONS**: see "Correction of the r6 record" below. **M15 (the review's precision remark under B1)**: §9's M15 row adds "As a property of the coupling map it does not depend on the meter's supply (Q4-P19 (i)); its operational consequence, that a record carries a disturbance, rests on the meter's conjugate slot being unknown, as SA-1(c) supplies: with a known meter slot the reciprocal shift is a known displacement (AP1:320-323; Q4-D8)" |

**Propagation of B1 (§A.25).** A grep of the four files for `K_null`, `null-result`, `silent`, `outcome-independent`,
`Q4-P19` and "SA-1(a) row's condition" finds no other site stating M16 without SA-1(c). Two further sites are made
consistent with the new dependency:
- §9's SA-1(c) row, "where used", adds "M16's affine route (Q4-P20)";
- §3's list of what the epistemic restrictions carry adds "the null-result invasiveness of affine-symplectic location
  detectors (M16; Q4-P20), a hypothesis under test".

QX-4 §10 and SHARED §7 carry the new references (below).

**Correction of the r6 record.** DISPOSITIONS-r6 is a record and is not edited. Two of its entries are superseded:
- the N4 row's change ("a detector coupling that is an SA-1(a) step has it on the SA-1(a) row's condition"; standing
  "**QM-only** for non-affine couplings") stated M16's affine route without SA-1(c);
- the N3 row's and "Checked and left unchanged" entry's statement that T2 and A4.4 use `K_null ≠ id` "which (ii) now
  supports" read Q4-P19 (ii) as a statement about the silent branch of a run.

Both are corrected by B1's changes above: (ii) supports `K_null ≠ id` only given a meter law that weights a state on
which `x` changes, which SA-1(c) gives (Q4-P20) and a sharp meter does not (Q4-D8).

## Must-fix nits

| finding | verified | change made (r7) |
| --- | --- | --- |
| **N1** (A6.2's title and §2 M12 × QX-6 omit the read-direction identification) | yes. A6.2's "Necessary, qualified" half assumes settings identified as local read directions; A6.1's hypotheses govern only the "not sufficient" half | **QX-6 A6.2 title**: "necessary for QM-matching settings with stabilizer pair states when settings are identified as local read directions, and not sufficient (…)". **SHARED §2 M12 × QX-6**: "r (QM-matching settings with stabilizer pairs, when settings are identified as local read directions; not sufficient …)" |
| **N2** ("given the design assumptions" for Q6-P12's pair) | yes. "The design assumptions" are (L′) and (R) throughout; under (D), (MI), (L′) and (R), A6.1 gives `|S| ≤ 2`, so the conditional was vacuous. Q6-P12's second bullet uses (L′) and separation in `G_ref` | **QX-6 §8 item 2**, **QX-6 A6.2 "For #1210"** and **SHARED §5 QX-6** (second prerequisite): "given (L′) and separation in the designed reference graph" |
| **N3** (SHARED §5 QX-3 "need M14", "need the M15 control" without bases) | yes, against QX-3 §5 (`B_3-enc`: `α` fixed by L-PORT), §8 (Level 2 is W2 on `B_3-route`; `B_3-enc` not creditable) and A3.2 ("§A.29; programme rule 1") | "For credit on `B_3-route` they need M14 (QX-3 §8; on `B_3-enc`, `α = 0` is fixed by L-PORT and is not creditable): …"; "They carry the M15 control, a control by programme rule (QX-3 A3.2)". The basis is stated for W1 and W2 together, since neither is creditable on `B_3-enc` |
| **N4** (M12 × QX-4: "4b's quantum value") | yes. QX-4 §2 and R4.5: 4b's value needs non-stabilizer preparations or non-Pauli reads; QX-4 §6 C-NONSTABILIZER: "4b may be posable with non-stabilizer preparations"; Q4-P12 bounds stabilizer preparations with Pauli reads by `3/4` | "4b's quantum value with stabilizer preparations, Q4-P12" |

## Precision nits

| finding | verified | change made (r7) |
| --- | --- | --- |
| **N5** (Q6-P12 second bullet lacks (R)'s readout clause) | yes, against A6.1's (R) (outcome a fixed `±1` function of the configuration on `R_A` after `T_A`) and step 5 | Q6-P12's second bullet adds the readout clause as a hypothesis, and its conclusion reads "(R)'s distance clause fails by A6.1". The evidence line cites p12 (4j) for the graph step |
| **N6** ("the point mass at `Ω`" while `Ω` is a function of `x_0`) | yes, against (MI) | Q6-P12's third bullet defines "the point mass at `Ω`" as any preparation law concentrated on `Ω`'s fiber, which the hull contains when it contains some such law; under it each outcome is deterministic, since `Ω` fixes each outcome (MI). The argument is otherwise unchanged |
| **N7** (R6.2 against §3.2) | yes | **QX-6 R6.2** type cell: "The design guarantees separation in the designed reference graph `G_ref` (§3.2); (R) on `G_B` and `G_A` is the assumption whose failure through edges outside `G_ref` is R6.7" |
| **N8** (Q6-P12 cited without the `⊥` rule) | yes; Q6-P12 lists the `⊥` rule as a hypothesis | "with the `⊥` rule" added at **QX-6 §3.2**, **A6.2 "For #1210"**, **A6.4**, **§8 items 2 and 4**, and **SHARED §5 QX-6** |
| **N9** (QX-4 §7 item 5 rests on a D record) | yes: R4.5 cites `DESIGN-DS.md` §5 finding 4 [D] | "needs C's resource, on `DESIGN-DS.md` §5 finding 4 [D], open (R4.5; SHARED Q4-O4)". **Propagation**: SHARED Q4-O4 lists R4.5's statement that native intermediate values lie only on `V + D = 1`, so the claim appears in the open list as §8's rules require |
| **N10** (H-SDC obstacle 3 rests on a W record) | yes; Q6-O8 lists M2D Theorem U2 as open | "If M2D Theorem U2 (W; open, Q6-O8) holds, it bars … and M18 must then come from outside that scope" |
| **N11** (SA-1(a) row: symmetry from isotropy) | yes. AP1:288-291: "The coefficient `k` on each edge is loaded classically per tick from a controller … per-tick, per-edge arming is not native" (posit P3) | §9's SA-1(a) row: "the coefficient symmetry, from isotropy for the native translation-invariant rule (E4; (vi)), and for detector couplings on armed edges from per-edge arming, one coefficient per undirected edge (SA-1(a′), P3), a design posit" |

## Optional items

- **p12 (4) as an independent reproduction of Q6-P12's checks**: applied. Q6-P12's evidence line reads "X: … in
  `p11_r6_checks.py` (3)–(4), reproduced independently by `p12_r6rev_checks.py` (4); the second bullet's graph step …
  (4j)". Q6-P12 itself stays [A].
- **"P12" in §8's X rule**: applied, with P13 added to the writer's list.
- p12 (1) and (3) (a third reproduction of Q4-P19 and the `F_3⁴` check): noted. Not cited, since Q4-P19's support is
  already X at its scope and its statement is not extended.

## Changes not traced to a finding

1. Housekeeping from the instruction to revise in place as r7 and keep r6 under `r6/`: titles "(draft r7)"; "§0 (r7)"
   and "specifications (r7)"; §0 "Revisions" pointers name `r6/` and `DISPOSITIONS-r7.md`; the §0 probe ranges become
   "P1–P13" (QX-4, SHARED) and "P1–P6, P11 and P12" (QX-6), since those files now cite p12 or p13; QX-3 keeps
   "P1–P6".
2. §A.42 item 8 rows for the new citations: SHARED §7 rows for the r6 review with p12 and for p13; QX-4 §10's R4.9 row
   adds Q4-P20, Q4-D8, the r6 review, p12 and p13; QX-6 §11's Q6-P12 row adds the r6 review with p12.
3. The B1 propagation sites listed above (§9 SA-1(c) "where used"; §3's list) and N9's Q4-O4 entry.

Every added line was scanned for necessity words ("needs", "must", "required", "requires", "necessary"). Each is
proved under stated hypotheses (Q4-P20, Q6-P12, A6.2's qualified half), labelled as open (N9, N10), or labelled as a
credit condition or programme rule (N3). The M15 clause was first drafted with "needs SA-1(c)" and is stated as
"rests on the meter's conjugate slot being unknown", with the reciprocal coupling's known-displacement case as the
evidence, since necessity was not shown for every affine-symplectic map.

## Checked and left unchanged

- SHARED §3 "Counting" (M19 item): "Given the design assumptions, (L′) and separation in the designed reference
  graph" names the pair Q6-P12 uses, as the review states, and R6.2 now says the design guarantees `G_ref`
  separation.
- SHARED §1 M15 and §2 M15 cells: map-level (Q4-P19 (i)), unaffected by B1, as the review states.
- QX-4 §7 item 3, R4.10, §2's INM row and §4 "Shared with QX-3": each states null-result invasiveness as a condition
  for matching the comparator protocol under (H1), (H2), (H4) (A4.4), not as a property derived from SA-1(a).
- SHARED §5 QX-4: already "M16, which is a hypothesis under test (§9)".

## Register

A scan of the 135 added lines (§A.32, §A.33) finds four-letter capitals only in identifiers (`SHARED`, `REVIEW`,
`DISPOSITIONS`, `MECH-OPEN`, `DESIGN-DS`, `H-LIFT`, `L-PORT`, `CHSH`, `QPHEN`, file names) and no history phrase,
reader instruction or self-assessment. No revision narration was added to the specification bodies.

## The owner rules still in force

| rule | status in r7 |
| --- | --- |
| The three-column restrictions table; column (iii) never supports column (ii); column (ii) no stronger than Main's posit list (Main:726) | B1: M16's column (ii) now names SA-1(c), whose own column (ii) is "open; none identified", and the standing is **QM-only**. N11 separates Main's isotropy posit from the P3 design posit in the SA-1(a) row. No column (ii) cites column (iii) |
| A6.1 conditional on (D), (MI), (L′), (R); (L′) and (R) design assumptions | unchanged; N2 removes the phrase that applied "the design assumptions" to Q6-P12's different pair; N7 states what the design guarantees |
| Disproved entries carry membership lines; narrower claims open unless separately established | Q4-D8 added with its membership line; its restatement is proved (Q4-P20), and the forms outside Q4-P20's hypotheses are open (Q4-O3). The other 11 entries are unchanged |
| Summary and dependency-table conclusions match the scope and status of their proofs | B1 (§1, §2, §9, T2, R4.9, A4.4), N1, N2, N4, N8 |
| Necessary physical conditions kept distinct from design assumptions | N3, N7, N9, N10, N11; the M15 clause's wording (above) |
| Exact generic checks labelled; probe-only results computation-supported; no computation on an OI mechanism | p13 acts on generic affine maps of `F_2⁴` and `F_3⁴` only. Q4-P20 is A (paper proof) with X at p12's scope and the writer-only counts marked computation-supported |
| No implied D19–D23 decisions, freeze, dispatch or construction | none added; all rules remain outlines |

## Refusals and deviations

- **None refused.**
- **B1 item 2.** A paper proof is given (Q4-P20) in place of a computation-supported entry. It is stated over
  `F_q⁴` and for any known linear functional of the meter, which is how AP1:297-299 states SA-1(c); the review's
  probe covered a known coordinate slot over `F_2`. The writer-only extensions are labelled.
- **B1 item 7.** DISPOSITIONS-r6 is not edited (it is a record); its N3 and N4 entries are corrected here.
- **The M15 remark under B1.** Applied with "rests on" rather than "needs" (see "Changes not traced to a finding").
- **N3.** The credit basis is stated for W1 and W2 together, not for W2 alone as the review's wording suggested,
  since the sentence's subject is both witnesses and neither is creditable on `B_3-enc`.

## r7 file hashes (sha256)

| file | sha256 |
| --- | --- |
| `QX3-ANTIBUNCHING.md` | `b6effd8a8a7364648c70250cc7258e2531a1317913eb109870837af1ee059b90` |
| `QX4-INCOMPATIBILITY-LG.md` | `6497d64efae0cedacd2ebc7e316c22c6797d0f798dd326dc34a5d47b295a0627` |
| `QX6-BELL-CHSH.md` | `33b01deb08aec45f6f3da18a6005ff86f9c244fe87fcd8bc265b562bdaeaaa3c` |
| `SHARED-MECHANISM.md` | `1aad26d1c5db83962c918ba76106d8548cc815c3fa66dfa982b589615131331a` |
| `review/probes/p13_r7_meter_supply.py` | `08b68a95ad8ba755455cfdfb4d47abed6a6d96e104c227819b8f9299ca570882` |
| `review/probes/p13_r7_meter_supply.out` | `b59f9d1d40c192ea1e56cfebdf1ca499f16eb13d8a48413320251ffa0ca825b1` |
