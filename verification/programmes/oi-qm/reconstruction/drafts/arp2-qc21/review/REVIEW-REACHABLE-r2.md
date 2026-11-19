# Re-review: REACHABLE r2 and the ARP-2 preregistration r2, against REVIEW-REACHABLE.md

**Objects reviewed (sha256).**
- `qc21/REACHABLE.md` (r2): `5429c7e4c82c2e6c18ab24fecbd7d7c207aea2c9c007e7197d416b963b3e9f7d`
- `qc21/preregistration.draft.md` (r2): `3864215c03e777a24344ab16b471063f3b83927c6ccaa3cd27da58a9944443a5`
- `qc21/PLAN.md` (r2; §9 holds the disposition table): `c18eae0a954fdb0eb10ad566e1b029764f9b59e696bbbd13a78d3d7c1c1c0dea`
- r1 copies used for diffing: `REACHABLE-r1.md` `c65a9d37…` (the object of REVIEW-REACHABLE.md);
  `preregistration-r1.draft.md` `17f40c84…`; `PLAN-r1.md` `d1a7db5e…`.
- Measured against `review/REVIEW-REACHABLE.md`, sha256 `ee726408…`.

**Standing.** Independent model re-review, read-only, 2026-11-08. It is not human verification. No reachable set was
computed under any rule, affine or not. Line references are to the r2 files: `R:` for REACHABLE, `P:` for the
preregistration and `PL:` for PLAN.

## Verdicts

- **REACHABLE r2: ACCEPT WITH CHANGES.** B1–B5 are closed. N1–N12 are applied. Five non-blocking defects are new
  (RN1–RN5). One of them, RN1, is a small slip in the proof that `α = 0`; the conclusion is unaffected and the
  repair takes one line.
- **Preregistration r2: REVISE.** Four findings block (PB1–PB4):
  - one detector has no positive control;
  - one control's frozen non-vacuity clause, on its natural per-rule reading, makes the round VOID by construction;
  - one frozen outcome text claims more than the measurements show;
  - the ledger says NNB is "not used", but the start set depends on it.

  None of the four touches the question, the rule family or the decision logic. Each fix is local.

## 1. Closure of B1–B5 (REACHABLE r2)

| r1 finding | closed? | where, and notes |
| --- | --- | --- |
| **B1** forward conditioning; decoupling | **Closed.** | R:38-49, R:100-108, R:138-140, R:190-194. The scope matches mine **exactly**: `q = 2`; U′ with R; exact induced maps; affine symplectic dynamics, centre terms harmless for (ii)–(iii); P1 terminal with registered cells decoupled from every cell, hidden sector included (P3/E-iso); P2 with N2; H-INF-μ as the uniform product; forward conditioning; bounded finite protocols for `Q³` only. Retrodiction and left-coupled registered cells are named as outside (R:48-49, R:179-183, R:273). |
| **B2** Lemma 4 attribution | **Closed.** | R:171-183. AP1 Lemma 3 is cited under SA-1, with SA-1's content listed. The extension to N, NNB, adaptive and hidden couplings is attributed to QA Lemma Q(iii) (QA:476-492) and MI-R §6.3. The `S_nat` extension is marked paper here. The r1 :189 error is corrected (R:211). MI-R is in Sources (R:31). See RN2 for one residual labelling gap. |
| **B3** NE consequence | **Closed.** | R:376-378. The consequence is stated for affine symplectic `G`. For non-symplectic affine `G` it needs NE-0, and then Prop D applies to pure supplies. NE-1's recorded-label mixtures meet Prop D's "full-record conditioning available" clause, because the label is a record. NE-2 (R:364-366) requires P1 terminality and forward time. NE-0 has been added (R:359). |
| **B4** NE-1 exactly native | **Closed**, apart from PB4/RN3. | R:112-119, R:360-363. `N_sup` is defined and tested structurally. Mixtures enter only with recorded labels. `S_nat` and real weights form a separate tier with exact-LP membership (R:125; NR-9 at P:424). Prop E is restricted to affine symplectic dynamics (R:240-244). Residual: `N_sup` lists the QA family without stating that `Λ_{y,b}` is natively available only under NNB (RN3, PB4). |
| **B5** test object | **Closed.** | "Keeps isotropy" is removed (R:416-420; P:145-148, P:232). Isotropy and `Q` are measured or reported fields (`nonaffine_branches`, `nonisotropic_branches`, `sharp_branches`; P:255-257). P★ and MI-R are cited, with how ARP-2 differs from each (R:330-353; P:141-144). The Prop D-like pattern is stated (R:344-345). INVALID rules report `nonstab_valid` (P:252-254). The redefinition is flagged for the owner (R:419-420; P:145-148; PL:152). |

N1–N12: each disposition in PL §9 was checked against the cited text, and each is present. Exceptions are noted
under RN1–RN5.

## 2. The writer's new derivations

**Theorem C(iii) without NNB, by two columns (R:203-207).** Correct.
- `Λ_{z,b}` and `Λ_{x,b}` are a P2 ready cell (known `z_1` or known `x_1`, value 1 through H-PREP) times a uniform
  source cell. `Λ_0` is two source cells. So all three are in L without NNB.
- Since `Φ` maps `R(L)` into `R(L)`, `α ± v ∈ O` for `v = β e_z`.
- Then `2v = (α + v) + (v − α)`, so `ℓ1(v) ≤ 1`. With `|v| = 1` this gives `v = ±e_b`.
- The same holds for `β e_x`.
- Orthogonality makes `β e_y = ±(β e_z × β e_x)`, so `β` is a signed permutation.

**`α = 0` from `α ± v ∈ O` (R:205-206).** The conclusion is correct. As written, the last step does not prove it
(**RN1**). The *sum* `|α_b + 1| + |α_b − 1| + 2 Σ_{c≠b} |α_c| ≤ 2` gives only `α_c = 0` for `c ≠ b` and `|α_b| ≤ 1`.
For example, `α = ½ e_b` satisfies the sum. `α_b = 0` follows from the two inequalities taken separately:
`|α_b + 1| ≤ 1` and `|α_b − 1| ≤ 1`.
*Fix:* "the sum forces `α_c = 0` for `c ≠ b`; then `|α_b ± 1| ≤ 1` forces `α_b = 0`."

## 3. Preregistration: do the controls and the decision rule follow from REACHABLE r2, and can a label be reached over a failed control?

**What follows correctly.**
- **CC-NAT** (P:268) is Theorem C(i)–(iii) on the triangle. Its expectations are right:
  - every element of `L_scope` is a fully conditioned branch, because each round registers at most one slot and
    no coarse event is formed;
  - so every element lies in `V₀`;
  - the offset rules are covered through the translation clause;
  - XOR is `N_1` on a non-bipartite graph, that is, an NNB-type coupling.
- **CC-DYAD** (P:267) is Lemma 5. It holds for any dynamics with `reg = none`.
- **C-EMB** (a)–(d) implements NE-1 to NE-5.
- **NE-0** is enforced through `outside_ball = 0` in the category definitions. Every element of `L_scope` is a
  fully conditioned branch, except CC-MIX's label marginals, which are coarse events of records.
- **C-INV**, **C-XB**, **C-STEP** and **C-SCOPE** are adequate.
- **The decision rule** (P:282-290) returns VOID on a non-zero exit, missing or off-schema output, an incomplete
  run, any red control, or a disagreement between the checker's flags and `decide`. **No substantive label is
  reachable over a red control.**
- The ADA is kept out of `decide` (P:338).

**PB1. NO-VALID-ESCAPE and NONSTABILIZER are reachable over an untested detector (blocking).**
- The choice between NONSTABILIZER and NO-VALID-ESCAPE turns on `nonstab_valid` (`|r|² ≤ 1` and `ℓ1(r) > 1`;
  P:247-254). No control ever drives that counter positive.
  - PC-PLANT tests the induced-map routine.
  - C-INV tests `outside_ball`.
  - CC-NAT and CC-MIX expect `nonstab_valid = 0`.
- So a counter that never fires — a wrong ℓ1, a strict-versus-non-strict slip, a mask error — leaves every control
  green and yields NO-VALID-ESCAPE. That is a verdict over a vacuous detector (Code Review Rules, "Exactness and
  controls"; §A.21).
- The same gap covers the INVALID-with-`nonstab_valid` report, the P★-like pattern on which the ADA's E-BALL row
  depends.
- *Fix:* add a positive control, PC-NONSTAB.
  - Run rule `0` with `S_0` plus one planted N2-departing law, for example `z_1, x_1 ~ Bern(1/5)` with image
    `(3/5, 0, 3/5)` (R:130-131). It is green only when `nonstab_valid > 0` and the category is NONSTAB.
  - Add a second planted pair: one law with image `(1, 1, 0)` and one in `ball \ O`. It is green only when the
    category is INVALID and the invalid-rule `nonstab_valid` field is positive.
  - Both planted laws must fail NE-1 under C-EMB (a).

**PB2. CC-MIX's non-vacuity clause can void the round by construction (blocking).**
- "some `V` entry has a denominator divisible by 3" (P:269) does not say over which set.
- Rules `0` and `1` never couple the mediator to the carrier: `u_i' = v_i`, or `u_i' = 1 + v_i`. Under them no
  carrier law can carry the mediator's 1/3 weight.
- Read per rule, the clause is therefore red for `0` and `1` in every run, so CC-MIX is red and the round is VOID
  whatever the test rules do.
- *Fix:* freeze the quantifier: "over the union of the four affine rules' `V` sets" (or "for `XOR` and `XNOR`").
  Keep `outside_ball = 0` and `nonstab_valid = 0` per rule.

**PB3. The frozen CANDIDATE text claims more than the measurement shows (blocking).**
- P:307 reads "every reachable law has read statistics in the Bloch ball". The round checks only `L_scope(g)`:
  depth 2, `k ≤ 6`, one mediator.
- Laws reachable at greater depth are unmeasured. This is the finite test → universal pattern (Claim/evidence
  boundary).
- The NO-VALID-ESCAPE text (P:316-317) already says "every law of the bounded reachable set".
- *Fix:* replace the CANDIDATE phrase with "every law of the bounded reachable set has read statistics in the Bloch
  ball". NE-0 as tested here is NE-0 on `L_scope`. State that in the CANDIDATE text and in ADA question 4.

**PB4. NNB is used but typed "not used" (blocking).**
- `S_0` contains `Λ_{y,b}` (P:203). REACHABLE says it "is an H-PREP supply obtained under NNB" (R:423), and so does
  CC-NAT (P:268). Yet the kept/removed table lists "NNB … not used" (P:239), and the ledger has no NNB row.
- `N_sup` and NE-1 also admit "an H-PREP family law `Λ_{a,b}`" without that condition (R:113, R:361).
- Under the owner's assumption-dependence direction, an ADA that types a used supplied premise as unused is a
  ledger error. It also bears on the embedding question. `Λ_{y,b}` is a stabilizer law, but its known functional
  spans two cells, which is the kind of non-P2 supply that B4 narrowed NE-1 against. It is admissible here only
  through NNB plus H-PREP.
- *Fix:*
  - add ledger row L-NNB: supplied conditional premise (QA:443-450), used only to supply `Λ_{y,b}` through H-PREP;
  - remove NNB from the "not used" row;
  - qualify `N_sup` and NE-1 in REACHABLE: "`Λ_{y,b}` conditional on NNB (QA node 8)" (RN3);
  - optionally, record whether the result changes if `Λ_{y,b}` is dropped. Theorem C(iii) now needs only the `x`
    and `z` columns, but the induced-map routine at P:220 uses all three.

**Non-blocking (preregistration).**
- **PN1. The frozen texts fail their own phrase screen.** "What no outcome shows" (P:324) contains "establishes a
  quantum mechanism". That matches the S4 entry "quantum mechanism" (P:332), and "a hit fails V". The self-test
  would catch this before `F` (precondition 6), so it cannot yield a wrong label. Reword the sentence so that it
  avoids the phrase, for example "or establishes a mechanism that reproduces QM", or exempt it by exact match.
- **PN2. Runtime must be bounded independently of the outcome.**
  - Worst case, `|L_scope(g)| ≤ 23 + 23·150 + 23·150² ≈ 5.2 × 10⁵` per rule.
  - Checking the induced identity for 150 rounds over that set, at about 90 µs per propagation, is far beyond the
    30-minute step timeout. A timeout halts the round as VOID.
  - The runtime cannot be benched on test rules before `F`, so the bound must come from the design.
  - *Cheap exact fix:* with a constant herald, both `μ ↦ R(B_π μ)/q` and `μ ↦ α + β R(μ)` are affine in `μ`.
    Herald constancy and the identity on `L_scope(g)` are therefore equivalent to the same checks on an affine basis
    of `aff L_scope(g)`, which has at most 16 laws. That basis is found by an exact rank computation. Freeze it, and
    have C-XB or a self-test confirm the equivalence on the affine rules. Generating `L_scope` itself, about
    4 × 10⁶ propagations over all rules, remains and should be benched.
- **PN3. ADA attribution.** "CANDIDATE and NONSTABILIZER are evidence that L-AFF is essential in this model"
  (P:369-370). For the test rules, removing affinity also removes linear symplecticity and `Q` conservation (RC3),
  so the three cannot be separated in this family. *Fix:* "L-AFF, together with the linear symplecticity and `Q`
  conservation that go with it in this family".
- **PN4.** L-P1 (P:349) says P1 is "enforced by P3/E-iso". In this model P1 is implemented by removing the
  mediator at once (P:213-216), which is a supplied idealization. Say so in the row.

## 4. The key open question (PLAN §7, PL:133-141)

As a research question it is precise. Every term is defined in REACHABLE r2:
- bijective, centre-free, translation-invariant, neighbour-symmetric second-order rule over `F_2`;
- native supplies;
- forward conditioning on P1-terminal records;
- U′ with R;
- `ball \ O` with E-BALL on every reachable law.

It is the right precondition (R:302-304, Prop K).

**It is not decidable by ARP-2, in either direction, as quoted.**
- *Negative direction.* The question quantifies over all such rules, lattices and protocols. ARP-2 evaluates four
  rules on `Z_3`, depth 2, `k ≤ 6`, one mediator. NO-VALID-ESCAPE is a scoped finite search (witness principle).
  The prereg says this (P:128-129, P:316-319).
- *Positive direction.* "With every reachable law inside the ball" is checked only on `L_scope(g)`. A NONSTAB or
  CANDIDATE outcome exhibits valid non-stabilizer laws with no out-of-ball law **in the bounded set**. It does not
  exclude out-of-ball laws at greater depth (PB3).

*Fix (PL §7, R §5).* Add the decidable instance next to the general question: "ARP-2 decides, for the four
non-affine symmetric rules on `Z_3` with U′ on cells 0–1, one fresh mediator per round, `k ≤ 6` and depth 2: does
`L_scope(g)` contain a law in `ball \ O` while every law of `L_scope(g)` is in the ball?" Label the general question
open under every outcome. Read with this instance, the round's decision rule is complete and exact.

## 5. New non-blocking findings in REACHABLE r2

- **RN1.** The `α = 0` step (§2 above).
- **RN2.** Lemma 4 (R:171-173) states "with `Q* = 0` on it" "within Theorem C's hypotheses". Those hypotheses allow
  centre terms (R:191), and centre terms break `Q* = 0` (RC1(e)). Add "(without centre terms)", as Theorem C(i) does
  at R:197. The extension from class N to general affine symplectic steps, including centre terms, is **paper here**
  (AP1's proof uses only symplecticity). Label it so in Lemma 4's layer.
- **RN3.** `N_sup` and NE-1 (R:113, R:361): mark `Λ_{y,b}` as conditional on NNB (QA node 8), consistent with R:294 and
  R:423 (see PB4).
- **RN4.** The §2.5 row "forward conditioning, non-affine dynamics" (R:275) lists P★ as a lower bound. P★ is on a
  one-cell R1 carrier with P1 not implemented, so it is not a lower bound for `R(L)` on U′ in that class. Write
  "P★: a valid non-stabilizer law under a different carrier and without P1 (not a bound on U′)".
- **RN5.** R:5 says r2 "is not yet re-reviewed". After this review, record its verdict there and in precondition 2
  (P:576-579).

## 6. Summary

| item | status |
| --- | --- |
| B1–B5 (REACHABLE) | closed |
| Theorem C scope | matches the r1 review's statement exactly |
| Lemma 4 attribution | correct (RN2 adds one label) |
| NE-0, NE-1, NE-2; NR-9 tier | correctly defined; `Λ_{y,b}`'s NNB condition still to be stated (RN3/PB4) |
| B5 redefinition | done, with P★ and MI-R cited and their differences stated |
| C(iii) without NNB | correct |
| `α = 0` | conclusion correct; proof step needs the one-line repair (RN1) |
| controls and decision rule follow from REACHABLE | yes, with PB1 (no positive control for `nonstab_valid`) and PB2 (CC-MIX quantifier) |
| label over a failed control | not reachable; a label over an untested detector is reachable until PB1 is fixed |
| key open question | precise; not decidable by ARP-2 as quoted; add the bounded instance (§4) |
| REACHABLE r2 verdict | **ACCEPT WITH CHANGES** (RN1–RN5, none blocking) |
| preregistration r2 verdict | **REVISE** (PB1–PB4) |
