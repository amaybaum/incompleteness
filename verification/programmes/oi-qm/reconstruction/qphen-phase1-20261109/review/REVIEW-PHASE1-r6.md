# QPHEN Phase 1 r6: independent full-text review

## Standing

- **Reviewer.** This is an independent, model-written review. It is read-only on the repository, git and GitHub, and
  it writes only three files: this one, the probe `review/probes/p12_r6rev_checks.py` and its output
  `p12_r6rev_checks.out`.
- **Files reviewed.** Each sha256 was verified before reading, and all match the brief and DISPOSITIONS-r6.

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `01f8a44d64334d01…` |
  | `QX4-INCOMPATIBILITY-LG.md` | `df4def7192b7d822…` |
  | `QX6-BELL-CHSH.md` | `1243cea4e052a487…` |
  | `SHARED-MECHANISM.md` | `67b3f5b54f25fdba…` |
  | `DISPOSITIONS-r6.md` | `468d188d56f75066…` |

  The r5 texts under `r5/` match the hashes that DISPOSITIONS-r6 lists. `REVIEW-PHASE1-r5.md` is `fa7fd9fe…`.
- **Corpus.** `git fetch origin main` was run without depth, gc or prune. It gives
  `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade`, and `papers/Main.md` at that commit equals `main_fd.md`
  (`6144cd4a…`). The following were read at that commit:
  - Main:56, :406-414, :421, :652 and :726 (all thirteen posit items);
  - Substratum:48, :98, :100, :131, :270-272, :467 and :481;
  - SM:240;
  - AP1 (`apparatus-1-20261107/DESIGN.md`):280-330.
- **Method.**
  - All four specifications and DISPOSITIONS-r6 were read in full, and `diff r5/ r6` was read for every file.
  - The writer's `p11_r6_checks.py` (`d8026111…`) was re-run with `python3 -I` from a separate directory. It exited
    with 0, and its output is byte-identical to `p11_r6_checks.out` (`bc9bc1e4…`).
  - The new probe `p12_r6rev_checks.py` imports no earlier probe and uses only the standard library (`itertools`,
    `fractions`, `sys`, `collections`). It acts only on generic objects: matrices over `F_2` and `F_3`, `±1` response
    tables, and small graphs. It passes 37 of 37 checks.
  - No computation was run on any OI mechanism.

## Verdict: **REVISE**

r6 fixes B1, N1–N20 and the optional ABL-G item of the r5 review. Q4-P19 (ii) and Q6-P12 are correct as stated at
their literal scope. Both were checked independently: by hand, and by p12 (sections 1, 3 and 4), which uses a
construction of `Sp(4, F_2)` different from those of p9, p10 and p11. Main:726 supports B1's column (ii) entries, item
by item.

One blocker remains. It is new in r6, and it enters through the N4 route that the r5 review itself proposed:
- **B1 (r6).** Q4-P19 (ii) proves that `x` changes on *some* state with `c = 0`, over the whole meter space. The r6
  text reads this as null-result invasiveness, `K_null ≠ id`, which is a property of the silent branch of an actual
  run. The step from one to the other needs the meter's ready law to give positive weight to such a state.
- **What fails without that.** With a sharp meter the step fails. The reciprocal coupling records occupation and has
  `K_null = id`. In all, 144 of the 288 recording maps do so (p12 (2)). AP1:320-323 says the same: "With a known
  meter slot the shift would be a known displacement and no disturbance."
- **What holds with it.** Under SA-1(c) meters, every readable recorder is null-result invasive (p12 (2e)).
- **Consequence.** The M16 route is therefore conditional on SA-1(c), which §9 types **QM-only**. SHARED §1 M16, §2
  M16 × QX-4, §9's null-result row (column (ii) and standing), QX-4 R4.9, T2 and A4.4's Consequence state it without
  that condition. This is the pattern the owner's three-question rule bars: column (ii) claims more than its support.

Four must-fix nits and seven precision items follow. No theorem in the four files is false at its stated scope.
Every fix is a sentence, a cell or a ledger entry.

***

## Blocker

### B1 (r6). The N4 route for M16 omits the meter's supply condition (SA-1(c))

**The sites.**
- SHARED §8.2, Q4-P19 (ii): "… changes the carrier conjugate `x` on some state with `c = 0`: it acts on the system on
  its silent branch (`K_null ≠ id`)."
- SHARED §1, M16 type cell: "In the affine-symplectic class every location-preserving coupling that records occupation
  has it (Q4-P19, at its scope), so a detector coupling that is an SA-1(a) step has it on the SA-1(a) row's condition."
- SHARED §2, the M16 × QX-4 cell: "a property of affine-symplectic location detectors, Q4-P19".
- SHARED §9, the null-result row:
  - column (ii) reads "conditional: yes for location-preserving detector couplings that are SA-1(a) steps, on the
    SA-1(a) row's condition, since every such coupling that records occupation is null-result invasive";
  - the standing reads "QM-only for non-affine couplings".
- QX-4 R4.9:
  - "Every location-preserving affine-symplectic coupling whose meter write depends on occupation changes the carrier
    conjugate `x` on its silent branch, so it is null-result invasive (SHARED Q4-P19 (ii), on `F_2⁴`)";
  - the r5 sentence "That kick acts on both branches, so the reciprocal coupling is null-result invasive (A4.4)".
- SHARED T2 and QX-4 A4.4's Consequence: "for example by keeping the reciprocal, outcome-independent kick".
- DISPOSITIONS-r6 also records "T2 and A4.4 … `K_null ≠ id`, which (ii) now supports" (N3 row; "Checked and left
  unchanged").

**What the proof gives.**
- The proof of (ii) shows the contrapositive of "fixes `x` on all of `{c = 0}`". It quantifies over every meter value
  `(m, m′)`.
- `K_null` is "the kernel `K_null` of its silent branch" (QX-4 §1, validation layer), and (H3) is `K_null = id`.
  Both concern the runs in which the detector does not fire, so they concern the states with `c = 0` in the support
  of the meter's ready law.
- The meter's ready law is a supply restriction: sharp, SA-1(c) half-known, or unknown.

**Counterexample: a sharp meter.**
- The coupling is the reciprocal coupling `(c, x, m, m′) ↦ (c, x + m′, m + c, m′)`, with the meter supplied in
  `(0, 0)`.
- It is affine-symplectic (by hand, and p12 (2a)) and location-preserving.
- Its meter write `m + c` depends on `c` and is read without noise.
- On the silent branch, `c = 0` and `m′ = 0`, so `x′ = x`: `K_null = id` (p12 (2b)).
- Exhaustively, for each of the four sharp meter states, 144 of the 288 location-preserving affine-symplectic maps
  record readably with `K_null = id` (p12 (2), (2d)).
- Membership in the class of the M16 cell's claim:
  - the coupling is affine-symplectic and location-preserving;
  - it records occupation;
  - the claim places no condition on the meter's supply.

  A sharp meter is in fact admitted by `A_4` and by ABL-SA1c. QX-4's ABL-SA1c says so: "4a: some reads record without
  kicking".
- AP1:320-323 states the mechanism: "Given (c) and N2, that slot is unknown and uniform, so the shift is a
  disturbance. With a known meter slot the shift would be a known displacement and no disturbance."

**The conditional form holds** (computation-supported; this review's probe only).
- Take an SA-1(c) meter: one slot known, at either value, and the other uniform, whichever slot is the known one.
- Every location-preserving affine-symplectic map that records occupation readably, in some meter functional, has
  `K_null ≠ id`: 0 of 192 for each of the four SA-1(c) laws (p12 (2e)).
- With both meter slots unknown, no map records readably (p12 (2f)).
- QX-3 A3.2 already states the mechanism: "a kick from the meter's unknown slot". R4.3 types backaction as "EN
  reciprocity with CS SA-1(c)".

**Why it is a blocker.**
- Column (ii) answers "conditional: yes" on SA-1(a)'s posits alone. The route also needs SA-1(c), with N2, for the
  meter's ready cells, and §9 types SA-1(c) "**QM-only**: a hypothesis under test", with "none identified" in its own
  column (ii).
- A route through a QM-only hypothesis supplies no support independent of agreement with QM. Column (ii) therefore
  states more than its support: the owner's rule (c.6738337450, c.6739286623) and the Code Review Rules' conditional →
  unconditional pattern.
- The M16 type cell states a universal claim that the sharp-meter case refutes.

**Required fix.**
1. **Q4-P19 (ii).**
   - Keep the proved statement ("changes `x` on some state with `c = 0`").
   - Replace the gloss with a conditional one: "`K_null ≠ id` on the silent branch when the meter's ready law gives
     positive weight to such a state".
   - Add the sharp-meter countercontrol: the reciprocal coupling with meter `(0, 0)` records and has `K_null = id`.
2. **The SA-1(c) form.** Record it as computation-supported (p12 (2e)), or as X once the writer reproduces it
   independently, or with a paper proof: "with an SA-1(c) meter, every location-preserving affine-symplectic map that
   records occupation in a readable meter functional has `K_null ≠ id`". A paper proof should be short. Readability
   forces the read functional to pull back to `c` plus the known slot, and symplecticity then forces the unknown slot
   into `x`'s row.
3. **§8 ledger.** Add a disproved entry:
   - the refuted statement is the M16 cell's unconditional form;
   - the counterexample is the reciprocal coupling with a sharp meter;
   - the membership line is as above;
   - the restated claim is the SA-1(c) form, with the narrower claim open unless separately established.
4. **SHARED §1 M16, §2 M16 × QX-4, and §9's null-result row.**
   - Column (ii): "conditional on SA-1(a)'s posits and on SA-1(c), with N2, for the meter's ready cells. SA-1(c) has no
     identified support other than agreement with QM (its row), so this route gives no QM-independent support. None
     identified for non-affine couplings (open)."
   - Standing: "a hypothesis under test (O1); **QM-only**". The route can be recorded as a further consequence of
     SA-1(c), in the manner of AW-QX4-1. It is not a justification of SA-1(c).
5. **QX-4 R4.9.** Add "when the meter's conjugate slot is unknown (SA-1(c))" to both sentences.
6. **T2 and A4.4's Consequence.** Write "the reciprocal kick from the meter's unknown slot (SA-1(c))".
7. **DISPOSITIONS.** Correct the N3/N4 record accordingly.

M15 is not affected as a property of the coupling map: Q4-P19 (i) is map-level. Its operational consequence, that a
record carries a disturbance, needs SA-1(c), as AP1:320-323 and M3's row ("carries complementarity's universality")
already state. A clause in M15's §9 cell would make that explicit (precision).

***

## Nits

**Must fix before freeze consideration** (summary and dependency-table scope, c.6739311717; the owner's
necessary-against-designed rule)

- **N1. The residue of r5 N18: A6.2's title and the §2 matrix cell M12 × QX-6.**
  - Both still state Obligation C as necessary or required for "QM-matching settings with stabilizer pair states".
    They do not carry the premise that A6.2's necessity uses: settings identified as local read directions, with
    Clifford-class local operations.
  - DISPOSITIONS-r6 left them unchanged because "they carry A6.1's hypotheses". A6.1's hypotheses govern A6.2's *not
    sufficient* half, not its *necessary* half.
  - The r5 review named both sites in N18's finding.
  - Add "when settings are identified as local read directions" to both.
- **N2. "Given the design assumptions" at QX-6 §8 item 2, QX-6 A6.2 "For #1210" and SHARED §5 QX-6 (second
  prerequisite).**
  - Throughout the files, "the design assumptions" denotes (L′) and (R). Under (D), (MI), (L′) and (R), A6.1 gives
    `|S| ≤ 2`, so the conditional "a Bell excess … needs one through an edge outside the designed reference graph" is
    vacuous as written.
  - Q6-P12's second bullet uses (L′) and separation in `G_ref`.
  - Write "given (L′) and separation in the designed reference graph", as SHARED §3 "Counting" and §8.4 already do.
- **N3. SHARED §5, QX-3 proposals: "They need M14 …; They need the M15 control."**
  - These are dependency-table "needs" with design bases:
    - M14 is needed for the *creditable* arm `B_3-route`. On `B_3-enc`, `α = 0` is fixed by L-PORT and is not
      creditable (QX-3 §8);
    - M15 is a control by programme rule (QX-3 A3.2: "§A.29; programme rule 1").
  - Label each basis: "for W2 credit on `B_3-route` (QX-3 §8)" and "a control, by programme rule (A3.2)".
- **N4. SHARED §2 M12 × QX-4: "R (… ; 4b's quantum value)".**
  - 4b's quantum value needs non-stabilizer preparations *or* non-Pauli reads (QX-4 §2; R4.5; Q4-P12).
  - QX-4 §6 has C-NONSTABILIZER with "no non-Clifford fixed operation" and "4b may be posable with non-stabilizer
    preparations".
  - So a non-Clifford operation (M12) is not shown to be required for 4b. Write "4b's quantum value with stabilizer
    preparations (Q4-P12)", or mark it "?". This is pre-existing.

**Precision**

- **N5. Q6-P12, second bullet.** Add (R)'s readout clause to the hypotheses: each outcome is a `±1` function of the
  configuration on `R_A` after `T_A`, and symmetrically. Then "(R) fails" is the failure of the distance clause, which
  the conclusion about a `G_B`-path presupposes. p12 (4j) checks the graph step on every pair of graphs on four
  vertices (2,620 cases).
- **N6. Q6-P12, third bullet: "the point mass at `Ω`".**
  - (MI)'s `Ω` is "a function of `x_0`", while preparation laws are laws of the supplies or of `x_0`.
  - Either take `Ω = x_0`, or read "the point mass at `Ω`" as any admitted law concentrated on `Ω`'s fiber. The
    argument then holds unchanged, since `Ω` fixes each outcome.
  - p12 (4g)–(4i) checks the lemma on tables. Over a small universe of 4 tables and laws with weights in
    `{0, 1/2, 1}`, it checks every no-signalling class of 1 to 3 laws. Some member reaches `|S| > 2` in 7 cases, and in
    each of them some point mass in that member's support lies outside the affine hull.
- **N7. QX-6 R6.2 against §3.2.**
  - R6.2 types "separated … in `G_B` and `G_A`" as the design assumption.
  - §3.2 says that what the design guarantees is separation in `G_ref`, and that the case
    `d_{G_B} ≤ T_A − t_B < d_{G_ref}` is R6.7, not a design failure. Read literally, R6.2 also excludes R6.7.
  - State in R6.2 that the design guarantees separation in `G_ref`, and that (R) on `G_B` is the assumption whose
    failure through edges outside `G_ref` is R6.7.
- **N8. Sites citing Q6-P12 "under (D) and (MI)" without the `⊥` rule.** These are QX-6 §3.2, A6.2 "For #1210", A6.4,
  §8 items 2 and 4, and SHARED §5. Q6-P12 lists the `⊥` rule as a hypothesis. The omission is harmless, because QX-6 §1
  defines `S` under the `⊥` rule, but adding "with the `⊥` rule" would make the sites uniform with SHARED §3 and §8.4.
- **N9. QX-4 §7 item 5: "Intermediate incompatibility (off the line `V + D = 1`) needs C's resource".** This rests on
  `DESIGN-DS.md` §5 finding 4 [D] (R4.5), which is open by §8's rule. Label it accordingly. It is pre-existing.
- **N10. SHARED §3, H-SDC obstacle 3: "M2D Theorem U2 (W) bars … so M18 must come from outside that scope".** The
  necessity rests on a W record that Q6-O8 lists as open. Write "if U2 (W) holds, …". It is pre-existing.
- **N11. SHARED §9, SA-1(a) row: "the coefficient symmetry from isotropy (E4; (vi))".** This holds for the native
  translation-invariant rule. For detector couplings on armed edges, the symmetric coefficient comes from per-edge
  arming, one coefficient per undirected edge (SA-1(a′), P3), which is a design posit. One clause would separate the
  two.

**Optional**

- p12 (4) reproduces `p11_r6_checks.py` (3)–(4) independently. Q6-P12's computational checks therefore meet §8's X
  rule at their scope, if the writer wishes to cite p12; Q6-P12 itself stays [A].
- p12 (1) is a third independent reproduction of Q4-P19 (i)–(ii) and its counts.
- p12 (3) checks (ii) over `F_3⁴` beyond its stated scope: 1,728 recording maps, none an exception. This is consistent
  with the proof being independent of the field.
- If p12 is cited, §8's X rule should add "P12" to the reviewers' list.

***

## The r5 findings: verification

| r5 item | present in r6 | correct | notes |
| --- | --- | --- | --- |
| **B1**, N2 row | yes | yes | Column (ii) reads "no: a posit in Main", quoting Main:56 (Lemma 3) and Main:726 (iv), "a standard but substantive epistemic postulate, not derived", and (v)'s shared conditional. The standing reads "posit in Main (iv); application conditional on H-PREP". QX-3 R3.2 has been propagated |
| **B1**, MI row | yes | yes | Main:406-412 and Main:726 (v), "one conditional wearing three hats", verified verbatim |
| **B1**, SA-1(a) row | yes | yes; precision N11 | Checked item by item against Main:726: (xiii) "not derived and not an axiom of OI", stated relative to (viii); (xi) = A4 (Substratum:98); (vi) = E4; (vii) with the affine restriction in first-difference form (SM:240; Substratum:100, :270-272, "an operational input …, not a theorem"); (x) for the nearest-neighbour form (Substratum:48). Column (ii) claims no more than Main's posit list. The symmetry ⇔ symplecticity step: `MᵀJM = [[0, I], [−I, F − Fᵀ]]` re-derived by hand. p12 (5) checks it from the vector-pair definition at `(2,2)`, `(3,2)` and `(2,3)`, and by basis pairs at `(3,3)` and `(5,2)`; the counts equal `q^{n(n+1)/2}` (8, 27, 64, 729, 125). Translations do not change the linear part (5t). On a ring, a translation-invariant nearest-neighbour rule is symmetric iff it is reflection-symmetric (5r) |
| N1 | yes, at every site | yes | A grep of "A6.1" finds no site citing the lemma without its hypotheses or "A6.1's hypotheses" |
| N2 | yes (`G_ref` in §3.2; Q6-P12) | yes; precision N5, N7 | §3.2's three cases now partition the failures of (R)'s distance clause. Q6-P12's first bullet is A6.1 step 6 in contrapositive and uses only (D), (MI) and `±1` outcomes. It was re-derived, and p12 (4c)–(4f) checks it |
| N3 | yes (Q4-P19 (i)/(ii)) | the statement yes; the gloss **no** | The proof of (ii) was re-derived by hand: location-preserving gives row `c` = `e_cᵀ`; fixing `x` on `{c = 0}` gives row `x` = (·, 1, 0, 0) with `b_x = 0`; `det B = ω(Me_m, Me_m′) = 1`; and `(γ, β)B = 0`. p12 (1): 384 location-preserving maps, 288 that record, 0 exceptions; the weak-reading translation `m ← m + 1` is confirmed. The gloss `K_null ≠ id`: B1 (r6) |
| N4 | yes | **no**: B1 (r6) | The route needs SA-1(c) for the meter's ready cells |
| N5 | yes | yes | M15 is map-level (Q4-P19 (i)). The encoded-meter W support is labelled (Q3-O5) |
| N6 | yes | yes | R6.5/R6.7 → `A_6`/`B_6-loc`; R6.8 → no Level-2 credit; R6.10 → no Level-3 credit |
| N7 | yes | yes | |
| N14 | yes | yes | |
| N15 | yes (Q6-P12, third bullet; §3.2; A6.4; §8 item 4) | yes; precision N6 | The argument is correct: no-signalling is linear in the law, and a deterministic outcome under a setting-independent law is setting-independent. The countercontrol was reproduced (p12 (4h)). A6.4's "must" is now conditional on R6.7 and Level 2's target |
| N16 | yes | yes | |
| N17 | yes | yes, with N2 above | The bases are labelled. "Given the design assumptions" names the wrong pair (N2) |
| N18 | three sites | partly: N1 above | §8 item 6, §5 and §3 "Counting" are fixed. A6.2's title and the M12 × QX-6 cell are not |
| N8 | yes | yes | Boxworld is locally tomographic and contains PR boxes (L). Main:652 and Substratum:481 quoted correctly |
| N9 | yes | yes | |
| N10 | yes | yes | |
| N11 | yes | yes | |
| N12 | yes | yes | |
| N13 | yes | yes | |
| N19 | yes | yes | |
| N20 | yes | yes | |
| ABL-G (optional) | yes | yes | |
| own-pass item 3 (QX-4 §4 "has to") | yes | yes | A grep finds no remaining "has to" or "have to" |

## Owner requirements

| requirement | status | basis |
| --- | --- | --- |
| Verify all corrections and re-read the complete documents | **done** | Full read of all four files; diffs read; probes re-run and new probe written |
| Summary and dependency-table conclusions match the scope and status of their proofs | **not met**: B1 (r6), N1, N2, N4 | All other summary sites were checked; see below |
| Necessary physical conditions kept distinct from design assumptions | **not met**: N3; precision N7, N9–N11 | All 123 "needs", "must", "required", "requires", "has to" and "necessary" sites in the four files were read. The rest are proved under stated hypotheses, or labelled as a protocol, target, programme rule or comparator |
| Three questions; column (iii) never supports (ii); (ii) no stronger than Main:726 | **not met for M16** (B1 (r6)). Met for N2, MI and SA-1(a) | No (iii) → (ii) citation was found. M16's column (ii) leans on SA-1(c) without naming it |
| A6.1 conditional on (D), (MI), (L′), (R); (L′) and (R) design assumptions | **met**; N2 concerns the phrase used for Q6-P12's different pair | |
| Membership lines; narrower claims open unless separately established | **met** for all 11 entries; B1 (r6) needs a new entry | The table is below |
| Exact generic checks labelled; probe-only results computation-supported; no computation on an OI mechanism | **met** | p11 and p12 act on generic objects only. Q6-P12 is [A] with the writer's checks named. The SA-1(c) form in B1 is computation-supported by p12 alone |
| The three pairs (configuration vs encoded carriers; available vs derived; coherent mixing vs full rules) | **met**, apart from B1 (r6) | M15 and M16 separate location detectors from encoded meters. B1 (r6) is an "available vs derived" slip: the route derives M16 from a QM-only supply restriction |
| No D19–D23, freeze, dispatch or construction implied | **met** | Every rule is an outline. DISPOSITIONS-r6 keeps D19–D23 separate |

## Membership check of every disproved entry

All 11 entries are unchanged from r5. Each was re-read against its refuted claim.

| entry | verdict |
| --- | --- |
| Q3-D1 | valid: `L` is linear, routes on the ready support, uses own-cell reads, and conserves weight 1→1 and 2→2 |
| Q4-D1 | valid: (H1) and (H4) hold and (H2) fails as the claim requires; the mixture gives `3/2`; the `t₂` kick misses `z₃`. The INM form is open (Q4-O8) |
| Q4-D2 | valid: the witness was checked symplectic by hand on all six basis pairings; two modes; sharp mediator admitted |
| Q4-D3 | valid: the copy coupling is linear and records; the claim's class is affine maps |
| Q4-D4 | valid: trace-preserving dichotomic `Z` instruments, `G = X`, two-read correlators |
| Q4-D5 | valid |
| Q4-D6 | valid: Clifford `G`, Lüders reads, non-stabilizer preparation admitted |
| Q4-D7 | valid |
| Q6-D1 | valid |
| Q6-D2 | valid |
| Q6-D3 | valid |
| (new, required by B1 (r6)) | the unconditional M16 cell; the counterexample is the reciprocal coupling with a sharp meter; the membership line is given in B1 (r6) |

## Summary-scope check (complete list of mismatches)

The check compared every summary-level statement with its supporting entry. It covered:
- the §0 blocks;
- witness tables and Consequence paragraphs;
- requirement tables (type and status columns);
- derivation titles;
- arm and ablation tables;
- decision trees;
- obstacle lists;
- ladder mappings;
- SHARED §§1–5, §8.4 and §9.

| # | site | as stated | support's scope | fix |
| --- | --- | --- | --- | --- |
| 1 | SHARED §1 M16; §2 M16 × QX-4; §9 null-result row; QX-4 R4.9; T2; A4.4 Consequence; Q4-P19 (ii)'s gloss | null-result invasiveness for every affine-symplectic location detector, on SA-1(a)'s posits | (ii) is over all meter states; `K_null ≠ id` needs an SA-1(c)-type meter (p12 (2)); with a sharp meter, `K_null = id` | B1 (r6) |
| 2 | QX-6 A6.2 title; SHARED §2 M12 × QX-6 | Obligation C necessary or required for QM-matching settings with stabilizer pairs | only with settings identified as local read directions (A6.2's body) | N1 |
| 3 | QX-6 §8 item 2; A6.2 "For #1210"; SHARED §5 QX-6 | H-Bell's form "given the design assumptions" | given (L′) and `G_ref` separation (Q6-P12); under (L′) and (R), `|S| ≤ 2` | N2 |
| 4 | SHARED §5 QX-3 | "need M14", "need the M15 control" | M14 for the creditable arm; M15 by programme rule | N3 |
| 5 | SHARED §2 M12 × QX-4 | R for 4b's quantum value | non-stabilizer preparations suffice without a non-Clifford operation (QX-4 §6) | N4 |

Checked and consistent:
- **QX-3:** §2 Consequence, R3.2, §5–§8.
- **QX-4:** A4.1–A4.6 apart from the B1 sentences, §5, §6, §7 items 1–4 and 6–8, §8.
- **QX-6:** §2, §3.1, §3.2 (apart from N7), A6.1, A6.4, §5, §6, §7, §9.
- **SHARED:** §1 rows other than M16, §3 apart from N10, T1 and T3–T9, the §4 controls, §5 QX-4 and QX-6 apart from N2,
  §8.4, and the §9 rows other than the null-result row.

## Register and authorization

- **§A.32 and §A.33.** The 169 r6-added lines were scanned. Four-letter capitals occur only in identifiers
  (`MECH-OPEN`, `NCONS`, `CHSH`, `H-PREP`, `QPHEN`, file names). No history phrase, reader instruction or
  self-assessment was found.
- **Authorization.** Nothing implies a D19–D23 decision, a freeze, a dispatch or a construction. "Frozen" occurs only in
  "not frozen" and in descriptions of records already frozen on `main`.

## Probes

| probe | sha256 | result |
| --- | --- | --- |
| `p11_r6_checks.py` (writer; re-run) | `d8026111baa43581…` | 11 of 11 pass; output identical to `.out` (`bc9bc1e4…`); exit 0 |
| `p12_r6rev_checks.py` (this review; imports no earlier probe; generic objects only) | `876497e1b442b13c…` | 37 of 37 pass; output `p12_r6rev_checks.out` (`a09612867ffa8743…`); exit 0; exact (integers mod `q`, `Fraction`) |

p12's sections:
1. Q4-P19 (i) and (ii) on `F_2⁴`.
   - `Sp(4, F_2)` is built by enumerating symplectic bases. It is cross-checked by brute force over all 65,536
     matrices, and against the definition `ω(Mu, Mv) = ω(u, v)` on all vector pairs.
   - The counts: 720, 11,520, 20,160, 6, 384 and 288. Neither statement has an exception.
2. `K_null` on the silent branch's support, for sharp, SA-1(c) and unknown meter laws (B1 (r6)).
3. Q4-P19 (ii) over `F_3⁴`: `|Sp(4, F_3)| = 51,840` from symplectic bases; 1,728 recording maps; 0 exceptions.
4. Q6-P12.
   - Bullet 1, on 256 tables and MI mixtures.
   - Bullet 3: point-mass no-signalling ⇔ local; the PR countercontrol; and the affine-hull lemma, exhaustively over a
     small universe.
   - Bullet 2, on all pairs of graphs on four vertices.
5. B1's SA-1(a) row: symplectic ⇔ symmetric, together with the translation and ring checks.
