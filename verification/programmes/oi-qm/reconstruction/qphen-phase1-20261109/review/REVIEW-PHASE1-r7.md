# QPHEN Phase 1 r7: independent full-text review

## Standing

- **Reviewer.** This is an independent, model-written review. It is read-only on the repository, git and GitHub. It
  writes three files: this review, the probe `review/probes/p14_r7rev_meter_supply.py` and its output
  `p14_r7rev_meter_supply.out`.
- **Files reviewed.** Each sha256 was verified before reading, and each matches the brief and DISPOSITIONS-r7.

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `b6effd8a8a736464…` |
  | `QX4-INCOMPATIBILITY-LG.md` | `6497d64efae0ceda…` |
  | `QX6-BELL-CHSH.md` | `33b01deb08aec45f…` |
  | `SHARED-MECHANISM.md` | `1aad26d1c5db8396…` |
  | `DISPOSITIONS-r7.md` | `98e17956d0dc7bfe…` |

  The r6 texts under `r6/` match the hashes that DISPOSITIONS-r7 lists. `REVIEW-PHASE1-r6.md` is `86b69048…`.
- **Corpus.**
  - `git fetch origin main` was run without depth, gc or prune. It gives `origin/main` = `fd539e15…`, and
    `papers/Main.md` at that commit equals `main_fd.md` (`6144cd4a…`).
  - AP1 (`apparatus-1-20261107/DESIGN.md`) was read at that commit at :270-335 and :416-418. Two passages matter here:
    - SA-1(c) at :297-299: "Its other slot is unknown and uniformly distributed, independently of everything else";
    - the mechanism at :320-323.
  - The owner records #1210 c.6739311717 and c.6741117489, and #1169 c.6740778880, were read through the GitHub API.
    The read was read-only.
- **Method.**
  - All four specifications and DISPOSITIONS-r7 were read in full, and `diff r6/ r7` was read for every file. It adds
    135 lines.
  - The writer's `p13_r7_meter_supply.py` (`08b68a95…`) was re-run with `python3 -I` from a separate directory. It
    exited with 0, and its output is byte-identical to `p13_r7_meter_supply.out` (`b59f9d1d…`).
  - Q4-P20's paper proof was checked line by line by hand (below).
  - The new probe `p14_r7rev_meter_supply.py` imports no earlier probe and uses only `itertools`, `random` and `sys`.
    It builds `Sp(4, F_q)` differently from p9–p13: as the breadth-first closure of a set of symplectic transvections.
    It passes 64 of 64 checks. It acts only on generic affine maps of `F_q⁴`.
  - No computation was run on any OI mechanism.

## Verdict: **ACCEPT WITH NITS**

r7 fixes the r6 blocker B1 and every r6 nit, N1–N11. The new **Q4-P20** is correct, and its paper proof is verified
here independently, under one hypothesis that it uses but does not state (N2 below). That hypothesis is part of
SA-1(c) as AP1 defines it. Q4-D8's membership line is valid. M16 carries **QM-only** at every site where its standing
is stated, and its column (ii) no longer claims support beyond SA-1(c)'s.

No blocker remains. Two must-fix nits remain, and both are clause-level:
- **N1.** A sentence added at three sites, "with a sharp meter the kick is a known displacement and `K_null = id`", is
  false at its stated scope. It holds only when the meter's conjugate slot is sharp at 0. Read after the sentence
  before it, it also suggests that SA-1(c) is necessary for `K_null ≠ id`, which is a design-against-necessary
  conflation.
- **N2.** Q4-P20's hypotheses do not state that the meter is independent of the carrier. The proof uses that
  independence, and without it the statement fails at its own stated scope, which does not require location
  preservation.

Freeze consideration needs N1 and N2 applied and confirmed. This verdict is not the unconditional ACCEPT that the owner's
freeze rule requires. Three precision nits (N3–N5) and four optional items (O1–O4) follow.

***

## The r6 findings: verification

| r6 item | present in r7 | correct | notes |
| --- | --- | --- | --- |
| **B1** item 1: Q4-P19 (ii) gloss | yes | yes | The statement is kept. The gloss is conditional on the ready law weighting a state on which `x` changes, with the sharp-meter countercontrol (meter `(0, 0)`, Q4-D8) |
| B1 item 2: the SA-1(c) form | yes, as **Q4-P20** [A] | yes, under N2 | Verified below. The paper proof is independently checked here. p14 (2), (3) and (4) reproduce every count, at `F_2⁴` and `F_3⁴`, with a different construction of `Sp(4, F_q)` |
| B1 item 3: a disproved entry | yes, **Q4-D8** | yes | Membership was checked by hand, and by p14 (6a)–(6c). See the membership table |
| B1 item 4: §1 M16, §2 M16 × QX-4, §9 null-result row | yes | yes | Column (ii) is "conditional on SA-1(a)'s posits and on SA-1(c) …; this route gives no QM-independent support … not a justification of SA-1(c)". The standing is "a hypothesis under test (O1); **QM-only**". §2 reads "QM-only, §9" |
| B1 item 5: R4.9, both sentences | yes | the SA-1(c) clauses yes; the added sharp-meter clause **no** (N1) | |
| B1 item 6: T2 and A4.4's Consequence | yes | the SA-1(c) clause yes; the added sharp-meter sentence **no** (N1) | |
| B1 item 7: the DISPOSITIONS record | yes | yes | DISPOSITIONS-r6 is unedited, and its N3 and N4 entries are corrected in DISPOSITIONS-r7 |
| M15 remark under B1 | yes (§9 M15 row) | yes; optional O2 | The clause says "rests on", not "needs", and makes no necessity claim beyond its cited case. Its support is in fact wider than cited (O2) |
| B1 propagation | yes | yes | §9's SA-1(c) "where used" gains "M16's affine route (Q4-P20)". §3's list of what M3, M7 and M8 carry gains M16 "a hypothesis under test". A grep for `SA-1(a) row's condition`, `null-result`, `K_null` and M16 finds no site stating M16 without SA-1(c) |
| N1 | A6.2 title; §2 M12 × QX-6 | yes | Both now say "when settings are identified as local read directions" |
| N2 | QX-6 §8 item 2; A6.2 "For #1210"; SHARED §5 QX-6 | yes | Each reads "given (L′) and separation in the designed reference graph" |
| N3 | SHARED §5 QX-3 | yes | The credit basis covers W1 and W2 together, with M15 as "a control by programme rule". That scope is justified, since neither witness is creditable on `B_3-enc` (QX-3 §8) |
| N4 | §2 M12 × QX-4 | yes | "4b's quantum value with stabilizer preparations, Q4-P12" |
| N5 | Q6-P12, second bullet | yes; optional O3 | The readout clause is a hypothesis, and "(R)'s distance clause fails by A6.1". Re-derived: a `G_B`-path of length `≤ T_A − t_B` that used only `G_ref` edges would give `d_{G_ref} ≤ T_A − t_B`. No inclusion `G_ref ⊆ G_B` is needed |
| N6 | Q6-P12, third bullet | yes | "The point mass at `Ω`" now means any law concentrated on `Ω`'s fiber. The contrapositive was re-derived with that reading: no-signalling is linear in the law, and under a law concentrated on the fiber each outcome is the deterministic value `F(Ω, a, b)` |
| N7 | R6.2 | yes | |
| N8 | QX-6 §3.2, A6.2, A6.4, §8 items 2 and 4, SHARED §5 | yes | Each carries "with the `⊥` rule" |
| N9 | QX-4 §7 item 5; Q4-O4 | yes | Labelled [D], open, and listed in Q4-O4 |
| N10 | H-SDC obstacle 3 | yes | "If M2D Theorem U2 (W; open, Q6-O8) holds" |
| N11 | §9 SA-1(a) row | yes; precision N3 | Main's isotropy posit (vi) is now separated from P3. P3, however, sits under a column-(ii) heading that names only Main:726's posits (N3) |
| optional items | Q6-P12 evidence line; P12 in §8's X rule | yes | P13 is added to the writer's list |

## Q4-P20: independent verification

**Statement checked.**
- `T(y) = My + b` is affine-symplectic on `F_q⁴`, with `ω` as stated.
- The meter is uniform on a line `{ℓ = k}`.
- `x` takes at least two values on each branch.
- `f`, a nonzero linear functional of the output meter, is constant on each branch and differs between them.
- Conclusion: `T` changes `x` on some silent support state.

**Proof, step by step.**
1. *Bracket preservation.* `MᵀJM = J` gives `M⁻¹J⁻¹M⁻ᵀ = J⁻¹`, so `MJ⁻¹Mᵀ = J⁻¹`. For row functionals this gives
   `{φM, ψM} = φMJ⁻¹Mᵀψᵀ = {φ, ψ}`. `J⁻¹` is block-diagonal over the pairs `(c, x)` and `(m, m′)`, so `{x, f} = 0`.
   This is checked on every element of `Sp(4, F_2)` and `Sp(4, F_3)` (p14 (1e)–(1f)).
2. *Readability.* On one branch the support's differences span `e_x` and the direction `d` of the line, with
   `ℓ(d) = 0`. **This holds when the support is the product of the `x`-values and the line.** Constancy of `f∘T` then
   says that `fM` kills `e_x` and `d`. The annihilator of `span{e_x, d}` is `span{c, ℓ}`, so `fM = αc + λℓ`, and
   `α ≠ 0` because the two branch values differ.
3. *`K_null = id` on `x`.* `g = xM − x` is constant on the silent support (`b_x` cancels it), so by the same
   annihilator `g = rc + ρℓ`.
4. *Contradiction.* `{rc + x + ρℓ, αc + λℓ} = α{x, c}`, because `{c, ℓ} = {x, ℓ} = {ℓ, ℓ} = 0`, and `{x, c} = ±1 ≠ 0` (the sign depends on the bracket's convention).
   So `α = 0`, a contradiction. ∎

**Findings on the proof.**
- **The proof is correct at its intended scope.** It needs no field property beyond invertibility of nonzero scalars,
  and it does not use location preservation. The remark under it is accurate: a sharp meter has two known functionals
  with `{m, m′} ≠ 0`, and the cross terms then cancel `α{x, c}`.
- **Step 2 uses a product support, and the hypotheses do not state it** (N2).
- **The proof gives more than the stated conclusion.** It excludes `g ∈ span{c, ℓ}`, and that is exactly "x′ − x is
  constant on the silent support". So under an SA-1(c) meter the silent action on `x` is never a known displacement.
  It is a non-constant kick, which is the property AP1:320-323 calls a disturbance (N5).

**Computation** (p14; generic objects; exact unless marked).
- (2) Explicit affine maps, every translation, under each SA-1(c) law. Each law's count of readable recorders matches
  the stated count; none has `K_null = id`, and none has a constant silent displacement.
  - All of `F_2⁴`: 4,608 of 11,520 per law, for all six laws (`ℓ ∈ {m, m′, m + m′}`).
  - Location-preserving maps of `F_2⁴`: 192 of 384.
  - Location-preserving maps of `F_3⁴`: 11,664 of 17,496, for all twelve laws.
- (2d) The same holds at `F_3`, location-preserving maps, with `x` restricted to each pair of values.
- (3) A reduction to linear parts was used for the full group at `F_3⁴`:
  - readability does not depend on `b`;
  - `K_null = id` is attainable iff `g` is constant.

  It was validated against explicit maps. Over all 51,840 × 81 affine-symplectic maps of `F_3⁴` and twelve laws, it
  finds 15,552 readable linear parts per law and no exception.
- (4) Random samples at `q = 5, 7` (1,500 matrices × 4 lines each; a sample only): 1,116 and 850 readable cases, no
  exception.
- (5) Countercontrols:
  - (5a) sharp meters reproduce 288 / 144 at `F_2` and 15,552 / 5,184 at `F_3`;
  - (5c) with both slots unknown, no location-preserving map records;
  - (5d) the copy coupling (not symplectic) records with `K_null = id`;
  - (5e)–(5f) independence is load-bearing (N2).

**Status.**
- With N2 applied, Q4-P20 holds at its stated scope.
- Its proof has now been independently reviewed.
- p13's writer-only counts are reproduced independently by p14. These are the `m + m′` laws, all 11,520 maps of `F_2⁴`,
  and the 17,496 location-preserving maps of `F_3⁴`. They are therefore X at those scopes if the writer cites p14
  (optional O1).

## Must-fix nits (before freeze consideration)

- **N1. The sharp-meter sentence at QX-4 R4.9, QX-4 A4.4's Consequence and SHARED T2.**
  - **As stated.** "With a sharp meter [that] kick is a known displacement and `K_null = id` (Q4-D8)."
  - **What the support gives.** Q4-D8 uses the meter `(0, 0)`. For the reciprocal coupling `x ← x + m′`, a sharp meter
    gives the silent action `x ↦ x + m′`. That is the identity only when `m′ = 0`.
  - **Counterexample.** With the meter `(0, 1)` the coupling records readably (output `m = c`), and its silent action
    is `x ↦ x + 1`, so `K_null ≠ id` (p14 (7a); also `(1, 1)`).
  - **Two consequences.**
    - The sentence is a universal claim wider than its counterexample's scope: the owner's summary-scope rule
      (c.6739311717).
    - Placed after "with its kick from the meter's unknown slot (SA-1(c))", it suggests that without SA-1(c) the
      reciprocal coupling fails M16, that is, that SA-1(c) is necessary for `K_null ≠ id`. It is not. It is a
      sufficient route (Q4-P20). The necessary-against-design rule (c.6741117489) applies.
  - **Fix**, at all three sites: "With a sharp meter that kick is a known displacement: the identity when the meter's
    conjugate slot is sharp at 0 (Q4-D8), and in no case a disturbance in AP1's sense (AP1:320-323)."
- **N2. Q4-P20's second hypothesis omits independence from the carrier.**
  - **As stated.** "Its ready law is uniform on the line `{ℓ = k}`". That is the meter's marginal only.
  - **What the proof uses.** The readability and `K_null` steps ("Varying `x` and then the meter along the line")
    need, on each branch, the product of the `x`-values and the line.
  - **The source includes it.** AP1:297-299 states it as part of SA-1(c): "unknown and uniformly distributed,
    independently of everything else".
  - **Without it the statement fails at its own scope.** Q4-P20 says "Location preservation is not used". Take a
    meter with `m` known and `m′ = s·x + t·c`, which is uniform on the line `{m = 0}` on each branch. Then readable
    symplectic linear parts admitting `K_null = id` on `(c, x)` exist: 108 at `q = 2` and 4,032 at `q = 3`, for every
    `(s, t)` tested (p14 (5e)).
  - **Location-preserving maps.** None of these is location-preserving (p14 (5f)). A paper argument explains why for
    this correlation family: `{c, m∘M} = {c, m′∘M} = 0` forces the meter rows to have no `x` coefficient, so `β = 0`,
    `δ = 0`, `α = 0`. So the summary cells that state the location-preserving case are not affected. Q4-P20's own
    scope is.
  - **Fix.** Write the hypothesis as "uniform on the line `{ℓ = k}`, independently of the carrier (SA-1(c),
    AP1:297-299), so that on each branch the support is the product of the carrier's `x`-values and that line". Also
    make the proof's step 2 cite it.

## Precision nits

- **N3. §9 SA-1(a) row after N11.**
  - The P3 clause sits inside "conditional on Main's posits for the selected lattice step (Main:726): …". The standing
    reads "native element of the selected lattice model, conditional on those posits".
  - P3 is not one of Main:726's posits, and AP1:290-291 says per-edge arming "is not native". The clause is labelled
    "a design posit", so nothing is disguised. But column (ii)'s heading, and the standing's "native", now cover a
    non-native design posit.
  - **Suggested.** End the Main list before P3, and add: "For detector couplings on armed edges the coefficient
    symmetry rests instead on per-edge arming, one coefficient per undirected edge (SA-1(a′), P3), a design posit, not
    an OI principle". In the standing, add "; for detector couplings on armed edges, conditional also on the design
    posit P3".
  - The M15 and null-result rows inherit the fix through "the SA-1(a) row's condition".
- **N4. Q4-D8's restatement points to an open entry that does not state the open forms.**
  - "Its forms for non-affine couplings, and for meter supplies outside Q4-P20's hypotheses, are open unless
    separately established (Q4-O3)". But Q4-O3 asks only whether OI's step supplies a location detector, and whether
    that detector is null-result invasive.
  - Under §8's rule ("an open entry states what is missing"), add both forms to Q4-O3 or to a new open entry.
- **N5. Assumption-watch (§A.31; classification NEW, scoped): `K_null ≠ id` does not separate a known displacement
  from a disturbance.**
  - **Sharp meters.** Every location-preserving affine-symplectic recorder acts on `x` by a known displacement on each
    branch. The paper argument: `c∘M = c` and `{c, x∘M} = {c, x}` force `x`'s coefficient in `x∘M` to be 1, so
    `x′ = x + rc + const` (p14 (5a): all readable maps, `F_2` and `F_3`).
  - **Two-thirds or half of them still have `K_null ≠ id`.** At `F_2`, 144 of 288 per sharp state; at `F_3`, 10,368
    of 15,552. For these, `K_null ≠ id` comes only from a nonzero known displacement.
  - **Consequences.**
    - (a) Q4-P20's conclusion can be stated in its stronger, proved form: "`x′ − x` is not constant on the silent
      support".
    - (b) M16 as defined is met without SA-1(c), by a design choice of meter value. Column (ii) is unaffected, since
      that choice is not an OI principle. It does mean that SA-1(c) is a sufficient route, not a necessary one (see N1).
    - (c) Whether a known silent displacement can serve A4.4's matching condition is not addressed. A4.4 gives only
      necessity.
  - Q4-D8's count line could add: "the other 144 have `K_null ≠ id` only by a nonzero known displacement".
## Optional

- **O1.** Q4-P20's label could read "[A, independently reviewed in `REVIEW-PHASE1-r7.md`; X: …]". The writer-only
  counts could become X with p14 (2), (3) cited. p14 (3) and (4) extend the computational support to all
  affine-symplectic maps of `F_3⁴` (exact) and to samples at `q = 5, 7` (a sample only). If p14 is cited, add "P14" to
  §8's list of reviewers' probes.
- **O2.** The M15 clause "rests on the meter's conjugate slot being unknown … with a known
  meter slot the reciprocal shift is a known displacement" cites one coupling. N5's paper argument supports it across
  the location-preserving affine-symplectic class: with a sharp meter, every such recorder's effect on `x` is a known
  displacement on both branches. That argument, with p14 (5a), could be cited.
- **O3.** Q6-P12's readout clause (r6 N5) is a hypothesis of Q6-P12 only. Several downstream
  sites say "given (L′) and separation in the designed reference graph": QX-6 A6.2 "For #1210" and §8 item 2, and
  SHARED §3 "Counting", §5 QX-6 and §8.4. Separation of the readout regions presupposes the clause, so this is
  harmless. "And (R)'s readout clause" would make the sites literal.
- **O4.** QX-3 §0's list of governing owner records, and SHARED §7, end at c.6739311717. Two later records govern this
  round and could be quoted with author and time:
  - #1210 c.6741117489 (amaybaum, 2026-11-09T13:22:24Z): "preserve the distinction between necessary physical
    conditions and assumptions built into the design";
  - #1169 c.6740778880 (amaybaum, 2026-11-09T13:05:46Z): the three distinctions.

## Owner requirements

| requirement | status | basis |
| --- | --- | --- |
| Verify all corrections; re-read the complete documents | **done** | The four files and DISPOSITIONS-r7 were read in full and every diff was read. p13 was re-run; p14 was written |
| Summary and dependency-table conclusions match the scope and status of their proofs | **met, apart from N1 and N2** | See the scope check below |
| Necessary physical conditions kept distinct from design assumptions | **met, apart from N1** (implied necessity of SA-1(c)); precision N3 | Every necessity word in the four files was read (below) |
| Three columns; (iii) never supports (ii); (ii) no stronger than Main:726 | **met**; precision N3 | M16's column (ii) names SA-1(c) and states that the route gives no QM-independent support. No column-(ii) cell cites column (iii). N11's P3 clause is labelled as a design posit but sits under the Main:726 heading (N3) |
| A6.1 conditional on (D), (MI), (L′), (R); (L′) and (R) design assumptions | **met** | Every A6.1 citation carries its hypotheses, or "A6.1's hypotheses". R6.2 and R6.4 type (R) and (L′) as design assumptions. Q6-P12 sites use "(L′) and separation in the designed reference graph" (N2 of r6) |
| Membership line on every disproved entry; narrower claims open unless separately established | **met**; precision N4 | 12 entries; see the table below |
| Exact generic checks labelled; probe-only results computation-supported; no computation on an OI mechanism | **met** | Q4-P20 is [A] with X at p12's scope, and its writer-only counts are marked computation-supported. p13 and p14 act on generic affine maps only |
| The three distinctions: configuration vs encoded carriers; available vs derived; mixing vs full rules | **met** | See the next three items |
| — configuration vs encoded carriers | **met** | M15 and M16 distinguish location detectors (configuration) from encoded meters (W support, Q3-O5). R4.9 keeps INM not posable in the encoded setting |
| — available vs derived | **met** | M16's affine route is stated as a consequence of SA-1(c), which is QM-only, and not as derived from OI |
| — mixing vs full rules | **met** | A6.2 and A4.1(c) keep coherent mixing (M12) as necessary-not-sufficient |
| No D19–D23, freeze, dispatch or construction implied | **met** | "frozen" occurs only in "not frozen" and in descriptions of records already frozen on `main`. No D19–D23 occurs. DISPOSITIONS-r7 keeps them separate |

## Membership check of every disproved entry

| entry | verdict |
| --- | --- |
| **Q4-D8** (new) | **Valid.** The refuted claim is quoted exactly from r6's M16 cell, and it has no supply condition. The matrix is checked by hand: `Me_c = e_c + e_m`, `Me_x = e_x`, `Me_m = e_m`, `Me_m′ = e_x + e_m′`. Over `F_2`, `ω(Me_c, Me_x) = ω(Me_m, Me_m′) = 1`, and `ω(Me_c, Me_m′) = 1 + 1 = 0`; the other three pairings vanish (p14 (6a)–(6b)). The coupling is location-preserving. With the meter at `(0, 0)`, the output `m` equals `c` (readable), and on the silent branch `x′ = x` (p14 (6c)). The 144-of-288 count is reproduced, and the 288 readable recorders are exactly the 288 with meter write depending on `c` (p14 (5b)). The restatement is proved (Q4-P20, under N2). The open forms need an open entry (N4) |
| Q3-D1, Q4-D1–Q4-D7, Q6-D1–Q6-D3 | Unchanged from r6 (the diff confirms it). Each was re-read against its refuted claim; all 11 are valid, as in the r6 review |

## Summary-scope check

**Sites checked:**
- the §0 blocks;
- witness tables and Consequence paragraphs;
- requirement tables (type and status);
- derivation titles;
- arm and ablation tables;
- decision trees;
- obstacle lists;
- ladder mappings;
- SHARED §§1–5, §8.4 and §9, with every row.

**Mismatches found:**

| # | site | as stated | support's scope | fix |
| --- | --- | --- | --- | --- |
| 1 | QX-4 R4.9; QX-4 A4.4 Consequence; SHARED T2 | sharp meter ⇒ known displacement and `K_null = id` | only when the meter's conjugate slot is sharp at 0 (Q4-D8); `(0, 1)` gives `K_null ≠ id` (p14 (7a)) | N1 |
| 2 | SHARED Q4-P20 (statement) | uniform marginal on the line suffices, at any location behaviour | the proof needs a product support (AP1:297-299's independence); fails without it for non-location-preserving maps (p14 (5e)) | N2 |

**Checked and consistent:**
- **SHARED §1.** M16: "every location-preserving coupling that records occupation readably from a meter supplied under
  SA-1(c) … (Q4-P20, at its scope)". This is narrower than Q4-P20 and correct even without N2, since location is
  preserved.
- **SHARED §2.** The M16 × QX-4 cell: "for affine-symplectic location detectors a consequence of SA-1(c)". Under
  SA-1(c) the carrier's `x` is uniform. Each branch's image is then an affine subspace, and recording at all is
  equivalent to linear readability, so the omitted "readably" changes nothing.
- **SHARED §3, §5 and §8.4.** The M16 item; QX-4's "M16, which is a hypothesis under test"; and §8.4's Counting
  conditions.
- **SHARED §9.** The null-result row ((ii) and the standing), the M15 row, and the SA-1(c) "where used".
- **Q4-P19 (ii).** The gloss.
- **QX-4.** §2, A4.1–A4.6 apart from N1, §§5–8 (item 5 now labelled), and §10.
- **QX-6.** A6.2's title, R6.2, §3.2, A6.4, §§7–9 and §11.
- **QX-3.** All sections; r7 changed only §0.

## Necessity words

- **Coverage.** Every "needs", "must", "required", "requires", "has to" and "necessary" in the four files was read:
  112 sites with this pattern, 17 of them on r7-added lines. "Necessary" in table headers and owner-question options
  is included.
- **The r7-added sites.** Each is one of the following:
  - proved under stated hypotheses (Q4-P20 sites; Q6-P12 sites with "(D) and (MI), with the `⊥` rule");
  - labelled as open (QX-4 §7 item 5 [D]; H-SDC obstacle 3, "if U2 holds");
  - a credit condition (SHARED §5 QX-3 "for credit on `B_3-route`");
  - conditional on matching the comparator under (H1), (H2) and (H4) (T2's "must").
- **The one exception** is N1's implied necessity, which carries no necessity word.
- **The pre-existing sites** are unchanged from r6, where they were found proved, labelled or protocol.

## Register and authorization

- **§A.32 and §A.33.** The 135 r7-added lines were scanned.
  - Four-letter capitals occur only in identifiers and file names (`SHARED`, `REVIEW`, `DISPOSITIONS`, `MECH-OPEN`,
    `DESIGN-DS`, `H-LIFT`, `L-PORT`, `CHSH`, `QPHEN`, `ANTIBUNCHING`).
  - No history phrase, reader instruction or self-assessment was found ("now", "no longer", "corrected", "the reader",
    "honest" and similar).
  - No revision narration appears in the specification bodies.
- **Authorization.** Nothing implies a D19–D23 decision, a freeze, a dispatch or a construction. Every rule remains an
  outline, and the §0 blocks state "no criterion is frozen".

## Probes

| probe | sha256 | result |
| --- | --- | --- |
| `p13_r7_meter_supply.py` (writer; re-run) | `08b68a95ad8ba755…` | 27 of 27; output byte-identical to `.out` (`b59f9d1d…`); exit 0 |
| `p14_r7rev_meter_supply.py` (this review; imports no earlier probe; standard library only; generic objects only) | `cd8be1e1f53f2e75…` | 64 of 64; output `p14_r7rev_meter_supply.out` (`d4064e3afb1ebe72…`); exit 0; exact (integers mod `q`) except the seeded random sample in (4) |

p14's sections:
1. `Sp(4, F_q)` by transvection closure. Orders 720 and 51,840; every element checked against the definition; at
   `F_2`, equal to a brute-force filter of 65,536 matrices; bracket preservation.
2. Q4-P20 by explicit affine maps over every translation, with the stated counts. Also the carrier restricted to two
   values at `F_3`.
3. A linear-part reduction, validated against explicit maps, then all 51,840 × 81 affine-symplectic maps of `F_3⁴`.
4. Random samples at `q = 5, 7` (not exhaustive).
5. Countercontrols:
   - sharp meters, with counts, and every readable location-preserving recorder a known displacement;
   - the 288 recorders;
   - both slots unknown;
   - the copy coupling;
   - correlated meters (N2).
6. Q4-D8's membership.
7. The sharp-meter sentence (N1).
