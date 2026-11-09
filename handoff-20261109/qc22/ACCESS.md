# ARP-3 (Q-C2-2): access analysis of the `G_SM`/P★ instance (paper, before any test) — r14a

**Standing.** WIP / UNVERIFIED preparation note for ARP-3 under #1169. Model-written. Paper analysis only: no LP was
solved by the writer, F1 was not built, and no `G_SM` read census was computed.
- **Review.** r1 (`048aa005…`, kept as `r1/ACCESS-r1.md`) was independently reviewed: `review/REVIEW-ACCESS.md`, verdict
  REVISE.
- **What the review confirmed.** Its exact probes (`review/probes/`; reviewer controls, not evidence) confirm
  Proposition F0, Lemma NC-F, the dual gbit, fixture H3 and CC-OFF's paper prediction.
- **What r2 changed.** It applied every finding of that review, B1–B7 and N1–N13 (r2 kept as `r2/ACCESS-r2.md`).
- **Re-review of r2.** `review/REVIEW-ACCESS-r2.md`, ACCEPT WITH CHANGES, with two blockers. Its independent exact
  controls are in `review/probes2/`. r3 applied B1, B2 (in the preregistration) and N1–N9 (r3 kept as `r3/ACCESS-r3.md`).
- **Review of r3.** `review/REVIEW-ACCESS-r3.md` (`86c6c8ad…`), REVISE, with four blockers. Its independent exact
  probes are in `review/probes3/`. It confirms the five frozen fixture tokens, F-10 and the completeness of the step-4
  certificates. r4 applies B1 here, B2–B4 in the preregistration, and N1–N7. It also follows the owner's direction
  c.6724832474 (r4 kept as `r4/ACCESS-r4.md`).
- **Review of r4.** `review/REVIEW-ACCESS-r4.md` (`91934582…`), REVISE, with three blockers. Its probes are in
  `review/probes4/`. It confirms the tokens for G, X, Q and H3, R-Uc's separation of single-cause cases, and
  certificate independence. r5 applies B1 here and in the preregistration, B2 and B3 in the preregistration, and
  N1–N7 (r5 kept as `r5/ACCESS-r5.md`).
- **Review of r5.** `review/REVIEW-ACCESS-r5.md` (`5fe0ec53…`), ACCEPT WITH NITS, with no blocker. Its N1–N4 concern
  the preregistration only. r6 of this note changed no analysis; it only recorded the disposition (§11).
- **Review of r6.** `review/REVIEW-ACCESS-r6.md` (`d44ecc06…`), REVISE, with one blocker present since r1. It concerns
  the preregistration's workflow (F1 computed by pull-request runs) and is fixed there. r7 of this note changes no
  analysis (r6 kept as `r6/ACCESS-r6.md`).
- **Review of r7.** `review/REVIEW-ACCESS-r7.md` (`947bd3b0…`), REVISE. Its findings concern the preregistration only:
  re-run attempts, other refs, the guard's static rule and the `mode` check. r8 of this note changes no analysis (r7
  kept as `r7/ACCESS-r7.md`).
- **Review of r8.** `review/REVIEW-ACCESS-r8.md` (`553e90bb…`), REVISE. Its findings concern the preregistration only:
  the guard's whitelist and second key, the enumeration's completeness, fixture mode's exit rule and the deleted-run
  residual. r9 of this note changed no analysis (r8 kept as `r8/ACCESS-r8.md`).
- **Review of r9.** `review/REVIEW-ACCESS-r9.md` (`d7e95d74…`), REVISE, by a new reviewer. Its findings (the step-8
  regression, the whitelist, the enumeration's identification, and the scope of owner requirements 2 and 3) concern
  the preregistration only. r10 of this note changed no analysis (r9 kept as `r9/ACCESS-r9.md`).
- **Review of r10.** `review/REVIEW-ACCESS-r10.md` (`3431a98a…`), REVISE. Its findings (the allowlist's aliasing and
  `cwd`, the builder-reference contradiction, and the blob search's object-store gap) concern the preregistration only.
  So do the owner's decisions c.6726548830 (the Environment gate). r11 of this note changed no analysis (r10 kept as
  `r10/ACCESS-r10.md`).
- **Review of r11.** `review/REVIEW-ACCESS-r11.md` (`22d9cda8…`), REVISE. Its findings (the Environment's reader and
  channel, the identity limit, and nits N1–N9) concern the preregistration only. r12 of this note changed no analysis
  (r11 kept as `r11/ACCESS-r11.md`).
- **Review of r12.** `review/REVIEW-ACCESS-r12.md` (`ba2ac209…`), ACCEPT WITH NITS. Its nits concern the
  preregistration only. r13 of this note changes no analysis (r12 kept as `r12/ACCESS-r12.md`).
- **Full review of the r13 preregistration.** `review/REVIEW-QC22-r13-full.md` (`6d1a8f8a…`), REVISE. Its N19 concerns
  this note: the restriction arguments for H3 and GX disagreed. r14 of this note states the support condition once
  (§6.4) and uses it for both; no verdict changes (r13 kept as `r13/ACCESS.md`).
- **Review of the r14 preregistration.** `review/REVIEW-QC22-r14.md` (`d344e277…`), REVISE. Its N8 concerns this note:
  §6.3 justified GX's restriction by sums of point reads rather than §6.4's condition, and §6.4 said that the
  infeasibilities rest on the exact LP, which no LP has shown for GX+R-Y. r14a of this note corrects both; no verdict
  changes (r14 kept as `r14/ACCESS.md`).
- **Controls.** The writer's scratch scripts are controls on this note's reading and algebra, not evidence (§10).
  `ctl_r2_fixtures.py` imports the reviewer's LP and is not an independent check. `ctl_r3_fixtures.py` imports no
  reviewer code and uses no LP. `ctl_r4_fixtures.py` (the G, X and Q fixtures and the step-3/step-4 fixtures) does
  the same.

Nothing here is adopted, promoted or proposed for a manuscript.

**Snapshot.** `main` = `2cd49dc082ee7b2a026fd6d1fb4a6168f92fac51`, fetched 2026-11-08 without a shallow fetch, gc or prune.
No path under the source records, `tools/` or `.github/` changed from the audit snapshot `5ce4f98e` to it.

| Abbr. | Record (`R/` = `verification/programmes/oi-qm/reconstruction/`) | Blob at `2cd49dc0` |
| --- | --- | --- |
| M2D | `R/mechanism-2-20261108/DESIGN.md` | `9352d9da7da6a55a52e6ada235034219638b34d2` |
| M1D | `R/mechanism-1-20261107/DESIGN.md` | `7f8a142be31222b1aee74b05990bb58648387cae` |
| MID, MIR | `R/minacc-1-20261108/DESIGN.md`, `RESULT.md` | `737047be…`, `5adf76eb…` |
| AP1 | `R/apparatus-1-20261107/DESIGN.md` | `51c24aeb7b42a915b8942462435fd9fe129861de` |
| QA | `R/quarter-phase-native-20261107/DESIGN.md` | `fb21999b0d45750a465dda742589f0af11575326` |

- **Status of the records.** All five are WIP / UNVERIFIED, model-reviewed records. They are used for definitions and
  for the published instance P★, never as premises of a conclusion (§A.46 item 7).
- **Off-`main` inputs.** These are the accepted audit `AUDIT-C2.md` (§13, §17 Q-C2-2; with `REVIEW-C2*.md`) and the
  gate draft r4 (imitation rule, R3-B2 text). Both are model-written planning documents. They enter as the question's
  specification, not as support.

**Owner records bound here** (all amaybaum on #1169, each quoted verbatim):
- **c.6723571280** (2026-11-08T15:47:58Z):
  - "Q-C2-2: Require instance-specific witnesses. Distinguish genuine operational accessibility from an inability to
    certify it within a particular mathematical framework."
  - "One additional principle should guide interpretation: failure to construct a witness is not proof that no
    witness exists, unless a theorem establishes that impossibility within a clearly stated scope."
  - "Which apparent obstacles survive when we retain only native OI principles and genuinely observable quantum
    requirements?"
- **c.6723889799** (16:16:38Z):
  - "The accessible but uncertifiable functionals are equally interesting conceptually. They may reveal that requiring
    an observer to certify an operation is stronger than requiring the observer to experience its measurable
    consequences."
  - "Neither route is established yet, but both merit investigation."
- **c.6723585151** (15:49:15Z):
  - "Add a hidden-prior sensitivity requirement. When a result changes under correlated hidden distributions, its
    stated scope must identify that dependence."
  - "Hidden information can influence physical dynamics without being accessible to the embedded observer."
  - "A proof that excludes such memory is valid only within that restricted model; it cannot automatically establish
    a limitation of OI generally."

## 0. Summary

1. **Instance.** The instance is `G_SM` at `q = 2` (M2D:155-168) with P★ (M2D:630-670), reproduced exactly (§10).
   - P★'s background supplies `(0, 0)` cells with both slots known (M2D:637). SA-1(c) excludes such cells
     (AP1:297-299), although M2D's ledger files P★'s ready cells under P2 (M2D:207).
   - The herald is a non-terminal configuration record used as an H-PREP conditioning (M2D:692-694).
2. **The audit's literal check is decided on paper: feasible (Proposition F0, exact).** By the audit's own rule,
   "Feasibility closes the instance", the literal check is closed for its fragment.
   - That is the outcome of Q-C2-2 as specified, preserved as an outcome.
   - It is closed for the prepare-measure fragment only; transformation noncontextuality is not tested.
3. **F1 is a new question, not the audit's check enlarged.** It changes the preparations, the reads and the access
   notion:
   - **Preparations.** It drops the mechanism-off preparations and adds the `Z−`, `X±` inputs.
   - **Reads.** It adds 36 `G_SM`-mediated reads.
   - **Access notion.** It makes the access notion explicit.

   Contextuality is not monotone, so F1's verdict does not bear on the literal fragment. The owner decides at the
   freeze whether to run it.
4. **Access, made precise.**
   - **L1 is the audit's notion and the reference.** `g` is determined or biased in a positive-probability record
     branch.
   - **EXP, read-record dependence (correlational).** This round's operational reading of the owner's "experience
     its measurable consequences": a native read's outcome is statistically dependent on `g` within a native
     branch, on reachable laws only. It does not separate experiencing `g` from experiencing a correlate of `g`.
   - **P★ meets both inside F1, on paper.** Herald 1 determines `g = 1`. In the herald-0 branch, the frame-time `Z`
     read depends on `g`: `P(z = 0, g = 0) = 3/5`, while `P(z = 0)·P(g = 0) = 16/25`.
   - **Consequence.** Condition (a) is met in F1 in both senses before any run. By Lemma NC-F, (b) follows from (c).
     The audit's conjunction therefore reduces in F1 to (c). Its discriminating content is attribution: which
     supplied completion restores a noncontextual model. Physical absence is a further question (§7).
   - **Experience without certification is compatible with classical imitability (F-9).** The audit's literal
     fragment F0 already has EXP (the `Z` read depends on `g` in P★'s herald-0 branch) and no native read equal to
     `g` (¬X3), and it has an exact noncontextual model (Proposition F0). So, for this instance, an observer can
     experience `g`'s measurable consequences without certifying `g`, inside a fragment that is classically
     imitable. This bears directly on the owner's question in c.6723889799. "Experience without certification" is
     not by itself a sign of nonclassicality.
5. **Lemma NC-F (ELABORATING).** In any finite classical stochastic model, if the pairing between preparation span and
   read span on `Ω` is nondegenerate, the configuration model is noncontextual. Infeasibility therefore implies
   non-spanning on the chosen `Ω`. It is the standard "nonnegative representation ⇒ noncontextual" direction. It has
   no converse: four point laws with the `Z` read alone are degenerate (`d = 2 < r_S = 4`) yet feasible (control
   c-r3). F0 is nondegenerate (`d = r_S = r_E = 3`), so Lemma NC-F alone gives Proposition F0.
6. **The dual gbit is the gbit in other coordinates.**
   - No LP can tell missing reads from missing preparations; only the ontic description can.
   - The gate's R3-B2 text guards reads only (F-2).
   - With both guards, Lemma NC-F leaves the gate's "otherwise" branch empty for every construction that has a
     configuration model. G5 credit then always needs a physical-absence proof.
7. **F1 is not decided on paper.** Herald projection is linear and `Z+ + Z− = X+ + X−`. So one relation among the four
   branches holds for each herald, and `r_S ≤ 6` on a reachable space of 16 configurations. The likely degeneracy
   sits in never-varied hidden (switch-cell) laws, a fixed hidden law of M2D Proposition B's kind (M2D:561-587). The
   round therefore carries a switch-supply completion R-S.
8. **Specificity to `g` is tested against a decorrelation that keeps `g`'s joint law with `η` (R-Uc).** It is not
   tested against r3's marginal-only R-U′, which gave a misleading negative when `g`'s law is fixed conditionally on
   `η` (F-12; fixtures G, X and Q).
9. **Fixture H3 is classical and contextual. Its witness of `g` varied across preparations sits in a sector that is
   not contextual, while the contextual sector has only a fixed bias of `g`.**
   Patterns of the form "accessible, uncertified, contextual" are therefore reported only as measured conjunctions,
   per herald block, never as a refutation of the dichotomy.
10. **Physical absence** needs an invariant over the stated class, or an exhaustive enumeration that holds only within
   its finite scope. For `G_SM` no invariant is known: AP1's grading fails for it (M2D:530-535).

## 1. The instance, fixed

- **Rule.** `f_i(u) = u_{i−1} ⊕ u_{i+1} ⊕ u_{i+2} ⊕ u_{i+1}u_{i+2}`, `F(u, v) = (f(u) ⊕ v, u)` on a ring of `L`
  sites over `F_2` (M2D:161-164).
  - It is a fixed bijection. It is an independently motivated proposal, an example not selected by OI (M2D:199-209).
  - Mechanism off (`R ≡ i + 1`) gives class N (M2D:195-197).
- **P★** (M2D:632-640).
  - **Carrier:** site 0 in `Z_+`, so `u_0(0) = 0`, with `v_0(0)` uniform.
  - **Switch sites 1 and 2:** uniform current slots and previous slots 0, the `X_+` law.
  - **Every other site:** `(0, 0)`.
  - **Run:** three ticks. The herald is `h = u_3(−1)`, and the carrier frame at `τ = 3` is
    `(z, x) = (u_2(0), u_3(0))`.
- **Published values, reproduced (control c-pstar; reviewer re-run).** These are exact at `L = 9, 12, 13`.
  - Herald 0 has probability 5/8, law `(3/5, 1/5, 0, 1/5)` and `r = (3/5, 1/5, 3/5)`.
  - Herald 1 has probability 3/8, law `(0, 2/3, 1/3, 0)` and `r = (1/3, −1/3, −1)`.
  - Mechanism off gives `Z±`.
- **Supplies (the mixed class, disclosed).** The carrier and switches are P2-type, with one known slot. The background
  is sharp, with both slots known, which is outside SA-1(c).
  - The finding bears on M2D's ledger, which files these cells as P2 (M2D:207).
  - Supplying sharp carrier inputs would span the same carrier space as adding `Y±` inputs.
- **Reads (N10).** The herald and every read below are non-disturbing reads of a configuration function of a ring
  site: premise (P-c), or H-PREP-type conditioning. They are not SA-1(b) meter registrations, which concern meter
  cells and terminality (AP1:292-296).

## 2. The functional: readings and the declared departure

The audit's condition (a) concerns "a functional of an **active hidden cell** … used by the fixed rule", and requires
the witness "for the functional that `G_SM` uses in P★" (AUDIT-C2 §17; REVIEW-C2-r2 N5).

| reading | object | note |
| --- | --- | --- |
| **G-Y (drafting choice)** | `g = z + x`, the carrier's `Q* = 1` functional at `τ = 3` | Theorem NC's certification gap at `q = 2` is the `Y` read of this functional (M2D:69-71, :530-537), and P★'s herald determines or biases it (M2D:625-627). **Departure, declared:** it is a functional of the carrier, not of a hidden cell |
| G-H1 | the switch cells' `Q* = 1` functionals `u_1 + v_1` and `u_2 + v_2` at `τ` | active hidden cells used by the rule as gates. This is MID's protected class (`Q* = 1` on active cells, MID:429-432) and the reading closest to the audit's wording |
| G-H2 | the hidden lift: the switch cells' law conditional on the carrier, as in the H-C break (M2D:712-714) | the residue M2D's dichotomy names (M2D:729-733). It is a law, not a single functional |
| G-S | the switch values `u_1(0)`, `u_2(0)`, or their OR | single-slot and directly readable, so certifiable at once |

The round decides on G-Y, and reports L1 and EXP measurements for G-H1 beside it (preregistration). The choice
among G-Y, G-H1 and G-H2 is an owner decision at the freeze (O-1). Write `η` for every other slot of the
configuration at `τ`.

## 3. Reads: native content, supplied capability, imported reads

| class | what it reports | native or supplied | status for `g` |
| --- | --- | --- | --- |
| T0 comparator reads | encoded Pauli Lüders reads, `Y` included | **imported** (comparator I1, M2D:232-234; R1 is a dictionary, M2D:777) | test-only |
| T1 frame-time carrier slot | `z` (a `v`-slot read at `τ`) or `x` | content native (P-c); the reading capability is supplied | its `χ_y` Fourier component is 0, but its outcome can still be **statistically dependent** on `g` within a branch where `g` is correlated with `z` or `x` (§6.1) |
| T2 `G_SM`-mediated single-slot read | `u_s(t)`, `t ≥ 4`, or a neighbour at `τ` | content generated by `G_SM` (a proposal); reading supplied | open (O-4); AP1's grading fails for `G_SM` (M2D:530-535) |
| T3 joint non-terminal records (H-PREP) | several slots jointly, the carrier's two slots included | supplied (H-PREP) | joint carrier records read `g` directly; that drops the one-functional-per-cell clause, the C9 analogue (AP1:682) |
| T4 AP1 coupled read | meter coupling with kick | coupling native for class N; setting supplied (P3, E-iso, AP1:510-511) | not available under `G_SM` always on |

"Native read" below means T1 or T2 content, one read per run (O-2).

## 4. The audit's literal check: its outcome (B7)

**Proposition F0 (paper; exact control c-alg (1); reviewer probe: feasible, model verified).** The audit's fragment
consists of P★'s heralded branches and the mechanism-off `Z±`, with the carrier's frame-time `Z` and `X` reads. It
has an exact preparation- and measurement-noncontextual model.
- **Model.** The model sets `μ_s(z, x) = ¼(1 + a_s(−1)^z + b_s(−1)^x)` and `ξ_{Z±} = (1 ± (−1)^z)/2`,
  `ξ_{X±} = (1 ± (−1)^x)/2`.
- **Validity.** It is nonnegative because every state has `|a| + |b| ≤ 1`. It is linear in the state and effect
  vectors. ∎
- **The general form.** Every `Z`/`X`-read fragment whose `(⟨Z⟩, ⟨X⟩)` states lie in the diamond is noncontextual.

**As an outcome.** The audit's rule (AUDIT-C2 §17) is "Feasibility closes the instance". On that rule, the literal
check is decided on paper and closes the instance for its fragment. The closure is at the prepare-measure level:
transformation noncontextuality is not tested (F-3).
- This is the result of Q-C2-2 as specified. It is preserved as such (c.6723277401: "Preserve negative, inconclusive
  and vacuous results without reinterpretation").
- The round reproduces it in-run as control CC-F0, with a paper-predicted verdict.

**F1 is a new question.** It is not the audit's check with more reads. It changes four things:
- **Preparations.** The four P2 carrier inputs `Z±, X±` × herald, conditioned. The mechanism-off preparations are
  dropped.
- **Reads.** 36 single-slot reads.
- **The access notion.** L1 as the reference, with EXP reported (§6).
- **The functional's reading.** G-Y, with G-H1 reported (§2).

It is well posed and not decided on paper (§5.4). Whether to run it is the owner's decision at the freeze.

## 5. Spanning

### 5.1 The configuration-level read space

- **Input carrier.** At `t = 0`, with the environment in a fixed product law, the read space is the functions on
  `F_2²`: `1, χ_z, χ_x, χ_y`, with `χ_y = (−1)^{z+x}`.
- **Frame time.** At `τ = 3` the read space is the functions on `Ω_reach`, the reachable configurations: 16 for F1's
  inputs. The carrier is correlated with `η`, so H-LIFT fails on the carrier alone (M2D:319-321, :346-347).

### 5.2 Lemma NC-F (ELABORATING)

**Statement.** Take any finite `Ω`, laws `μ_s` on `Ω`, and responses `ξ_e: Ω → [0, 1]` whose outcomes sum to 1.
Let `P = span{μ_s}` and `R = span{ξ_e}`. If `P ∩ R^⊥ = 0` and `R ∩ P^⊥ = 0`, equivalently `d = r_S = r_E`, then the
configuration model is preparation- and measurement-noncontextual.

**Proof.** A statistical equivalence `Σ c_s μ_s ⊥ R` lies in `P ∩ R^⊥ = 0`. The same argument works for effects. ∎

**Scope (N1).**
- Dynamics, bijectivity, frame and H-LIFT are not used.
- The lemma is one-directional (§A.34). Four point laws with the `Z` read alone are degenerate yet feasible. r1 and
  r2 named F0 as the example, which was wrong: F0 is nondegenerate on `F_2²` (`d = r_S = r_E = 3`, control c-r3),
  so the lemma gives Proposition F0 directly.
- It is the "nonnegative representation ⇒ noncontextual" direction (Spekkens, PRL 101, 020401 (2008)). It is also
  the simplex-embedding picture (Schmid, Selby, Wolfe, Kunjwal and Spekkens, PRX Quantum 2, 010331 (2021)).
  Neither was read first-hand.
- It is M2D's Theorem NC (M2D:485-507) without the frame.

**Corollary.** An infeasible LP on a fragment written on `Ω` implies `P ∩ R^⊥ ≠ 0` or `R ∩ P^⊥ ≠ 0` **on that `Ω`**.
"Missing reads or preparations" means non-spanning on `Ω`. It does not mean that a native read or preparation exists
and was left out.

### 5.3 Missing reads and missing preparations

- **The gbit.** Four point laws with `Z`/`X` reads (M2D:521-527). It is contextual and classical (reviewer probe:
  infeasible, `W` verified; adding the `g` read restores feasibility).
- **The dual gbit.** `Z±, X±` with point reads, contextual and classical. Point reads restrict to the diamond's facets
  (control c-alg (3)), and preparation noncontextuality on `½Z+ + ½Z− ≡ ½X+ + ½X−` fails. Reviewer probe: infeasible.
  Adding `Y±` restores feasibility, and adding the `g` read does not.
- **Two names, one GPT (N5).** The dual gbit's accessible GPT, the diamond with its four facet effects, is linearly
  isomorphic to the gbit's square with its facets. No LP distinguishes them; only the ontic description does. For
  fragment artefacts of this kind see Selby et al., "Accessible fragments of generalized probabilistic theories, cone
  equivalence, and applications to witnessing nonclassicality", PRA 107, 062203 (2023), not read first-hand.
- **Bearing on the gate (F-2; finding, not an edit).** The R3-B2 text conditions on "the accessible reads do not span
  the configuration-level read space". In the dual gbit the reads span, so a failed imitation would count. The guard
  is needed for preparations too.
  - **Corollary.** With both guards, Lemma NC-F leaves the "otherwise" branch empty for every construction that has a
    configuration model. G5 credit then always requires a physical-absence proof, and the gate could say so directly.

### 5.4 F1 is not decided on paper (paper fact; reviewer-derived, from the frozen model; no census)

- **One relation per herald.** Only the carrier input varies, and the switch and background laws are fixed. The four
  input laws satisfy `Z+ + Z− = X+ + X−`, and herald projection is linear. For each `h`:
  `p(h|Z+)μ_{Z+,h} + p(h|Z−)μ_{Z−,h} = p(h|X+)μ_{X+,h} + p(h|X−)μ_{X−,h}`.
- **Rank bound.** Hence `r_S ≤ 6`, on a reachable space of 16 points. F1 is non-spanning on the preparation side.
  The two *ontic* relations above lie within herald blocks. Operational equivalences can be more, because with
  `d < r_S` the reads add equivalences, which can mix blocks. Degeneracy of the pairing in Lemma NC-F's sense is a
  further, measured question.
- **Where the degeneracy likely sits.** Contextuality, if present, is very likely of the effect-degenerate, dual-gbit
  kind, located largely in the switch-cell laws that are never varied: a fixed hidden law, as in M2D Proposition B and
  M-FIX (M2D:561-587).
- **What follows for the round.** The `g`-completions alone would then not restore feasibility. The round therefore
  carries R-S, a switch-supply completion (test-only), and reports the rank each completion adds.

| side | class | spans? | note |
| --- | --- | --- | --- |
| reads | T1 | no; `χ_y` is missing on the input carrier | definition |
| reads | T2 | open; measured in-run | — |
| reads | T3 joint carrier records | yes | drops the one-functional clause |
| preparations | P2 inputs `Z±, X±` | no; `⟨Y⟩ = 0`, rank 3 on the input carrier | SA-1(c) |
| preparations | F1 branches at `τ` | no; `r_S ≤ 6 < 16` | §5.4 |
| preparations | sharp carrier, or `Y±` inputs | yes on the input carrier | outside SA-1(c) |

## 6. Access versus certification

### 6.1 Access notions (B1)

All three notions below are fixed for the instance. The functional is `g` (G-Y), and the same definitions apply to
G-H1.

- **L1, the audit's notion and the reference** (MID:135-139; M2D:837-838). Some positive-probability record branch of
  a native protocol determines `g`, or makes its conditional law non-uniform, given `K`.
  - *Inside F1, P★ meets it:* herald 1 determines `g = 1`, and herald 0 gives `P(g = 0) = 4/5`.
- **EXP, read-record dependence (correlational).** This is this round's operational reading of the owner's
  "experience its measurable consequences" (c.6723889799): a dependence of record-branch statistics on `g` that is
  reachable natively. It is correlational.
  - *Definition.* There is a native branch `p` (input × herald) and a native read `e` with
    `P_p(e = 0, g = 0) ≠ P_p(e = 0)·P_p(g = 0)`.
  - *Equivalently,* registering `e` changes `g`'s conditional law. That implies L1 in the original branch or in a
    refined one. It is not equivalent to L1 in the refined branch: a branch already biased stays L1 under an
    independent read, and a dependent read can make one refined branch uniform (re-review r3 N1; §A.34).
  - *Computed on reachable laws only.* No counterfactual configuration enters.
  - *Inside F1, P★ meets it on paper.* The T1 `Z` read in the herald-0 branch of input `Z+` gives
    `P(z = 0, g = 0) = P(00) = 3/5`, while `P(z = 0) P(g = 0) = 16/25`.
  - *What it cannot do.* It cannot separate "depends on `g`" from "depends on what `g` is correlated with" (`z`, `x`,
    `η`). That is HC-1, and it is inherent: a `g`-specific consequence is definable only counterfactually (INT) or
    relative to a certification (X1–X3).
- **INT, an interventional dependence; a counterfactual diagnostic only.** `ξ̂_e(y | η) ≠ 0`, computed by setting the
  carrier to each `(z, x)` with `η` fixed. Unreachable configurations are included. It is an ontic-model decomposition,
  not a measurable statistic. The round reports it and decides nothing on it.

**Departure, declared.** The audit's (a) is L1, and r1's `acc_meas` was an undeclared departure; it is withdrawn. EXP
is reported beside L1 as this round's correlational reading of the owner's phrase.

**Experience without certification (F-9; ELABORATING; paper, exact control c-r3).**
- In F0, the audit's literal fragment:
  - EXP holds: `P(z = 0, g = 0) = 3/5`, while `P(z = 0)·P(g = 0) = 16/25`, in P★'s herald-0 branch;
  - no read equals `g` (¬X3);
  - the fragment is classically imitable (Proposition F0).
- So `EXP ∧ ¬X3`, the owner's "experience without certification", is compatible with an exact noncontextual model.
- What remains open for the owner's question is whether experience without certification ever coincides with
  contextuality that a completion of `g` removes. That is what F1's attribution measures, in Π_fin only.

**Consequence (F-7).** In F1, (a) holds in both senses on paper. Lemma NC-F makes (b) (¬X1) a consequence of (c). The
audit's conjunction in F1 therefore reduces to (c). The discriminating content is **attribution**: which supplied
completion restores a noncontextual model. Physical absence is a separate question (§7).

### 6.2 Certification within stated frameworks

- **X1** (Theorem NC, M2D:485-490): the reachable preparations and the reads span, on a carrier on which H-LIFT holds.
  Spanning implies a nondegenerate pairing, and hence noncontextuality by Lemma NC-F. The converse fails (§A.34):
  F0's pairing is nondegenerate on `F_2²`, yet its preparations and reads span only 3 of 4 dimensions. In F1, ¬X1 holds on paper (`r_S ≤ 6 < 16`). The
  preregistration's (b) is the degenerate pairing, which (c) implies.
- **X2** (gate draft r4): the reads span the configuration-level read space. §5.3 adds the preparation side.
- **X3** (sharp certification): some native read equals `g`, up to complement, on `Ω_reach`. This is the C-COMP-type
  demand for an exhibited operation (M1D:360-376).

**What separates "experience" from "certify".**
- EXP holds without X1 or X3 whenever `g` is correlated with natively read quantities. That is the case in P★.
- The owner's hypothesis, "certify is stronger than experience", is `EXP ∧ ¬X3` (or `∧ ¬X1`) on the observer's
  carrier.
- It bears on contextuality only through attribution: whether supplying the missing certification restores a
  noncontextual model.

### 6.3 Attribution completions (B2, B4), all supplied and test-only

Each completion is reported separately. They are never lumped together.
- **R-G.** Adds the read `g` at `τ`, one effect direction.
- **R-U′, a `g`-law-preserving decorrelation.** For each of P★'s own two branches (input `Z+`), it adds the law
  `μ_p(η) ⊗ [P_p(g = 0)·U_{Y+} + P_p(g = 1)·U_{Y−}]`. That is the same `η`-marginal, with the carrier decorrelated
  from `η`, `(⟨Z⟩, ⟨X⟩) = 0`, and `g`'s law kept.
  - It replaces r2's R-U, which gave false negatives in exactly the `g`-biased case, P★'s (re-review B1).
- **R-Uc, a `(g, η)`-law-preserving decorrelation** (re-review r3 B1). For the same branches, it adds
  `Σ_η μ_p(η) δ_η ⊗ [P_p(g = 0 | η)·U_{Y+} + P_p(g = 1 | η)·U_{Y−}]`. It keeps the joint law of `g` and `η` and
  decorrelates only the rest of the carrier.
- **R-Y.** For the same two branches, adds the two laws `μ_p(η) ⊗ U_{Y±}`. These vary `g`'s law, both marginal and
  conditional on `η`.
- **The derived fields.**
  - **`g_specific := RY ∧ ¬RUc`.** The contextuality depends on `g`'s law, marginal or conditional on `η`: keeping it
    does not restore, and varying it does.
  - **`g_eta := RU′ ∧ ¬RUc`.** The contextuality depends on `g`'s correlation with `η`.
  - **Why r3's definition failed.** r3 set `g_specific := RY ∧ ¬RU′`. That gave a misleading negative when `g`'s law
    is fixed *conditionally* on `η` (fixture Q below), because R-U′ keeps only `g`'s marginal and erases its
    correlation with `η`. In F1 the carrier is correlated with the switch cells inside each branch (§5.1), so this
    is the live case. The owner excluded such negatives (c.6724832474).
- **Fixtures** (`ACCESS.md` control c-r4: ranks and hull facts; reviewer's `review/probes3/sep3.out`: LP verdicts).

  | fixture | construction | R-U′ | R-Uc | R-Y | `g_specific` | `g_eta` | token |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | **G** | H3's block B alone: carrier rectangle at fixed `P(g = 0) = ¾`, `η = 1`; point reads | inf (centroid) | inf (centroid) | feas | true | false | `CONTEXTUAL-RY` |
  | **X** | the same rectangle on `(x, η)`, with `z` uniform: `P(g = 0) = ½` everywhere | feas | feas | inf | false | false | `CONTEXTUAL-RUP` |
  | **Q** | each law `½·(block-B law ⊗ δ_{η=1}) + ½·(its x-flip ⊗ δ_{η=0})`: `g` marginally uniform, `P(g = 0 \| η = 1) = ¾` | feas | inf (centroid) | feas | true | true | `CONTEXTUAL-RUP+RY` |

  | **GX** | G's sector at `η = 2` beside X's sector at `η ∈ {0, 1}`; point reads on 12 points | inf | inf | inf (by restriction to X's sector) | **no** | **no** | `CONTEXTUAL-NONE` |

  - G is the specific case, X the non-specific one and Q the conditional one.
  - **GX has two causes (re-review r4 B1; F-13).** G's sector depends on `g`'s fixed law, and X's on an `x ⊕ η`
    correlation. No single completion restores, so both tests read "no", although one cause is `g`'s law.
    - A "no" is therefore a test result, "R-Y restores and R-Uc does not: no", not a finding of independence from
      `g`. The preregistration renders it that way, with a frozen caveat.
    - Its NONE addendum says the degenerate directions "may lie in several of the completed directions at once, or
      in others".
    - Multiple causes are the likely case in F1 (F-11, §5.4). Paired completions (R-Y+R-S, R-Y+R-Uc) would measure
      `g`'s contribution beside a second cause. They are listed as an owner decision before `F`, and not adopted.
  - R-G restores none of them, because the `g` read is a sum of point reads.
  - X's "R-Y infeasible" is the reviewer's LP; it does not follow from ranks. GX's "R-Y infeasible" is the reviewer's
    restriction argument, valid under §6.4's support condition: X's and G's sectors charge disjoint points, and the
    reads are point reads with their complements and the unit, so a noncontextual model of GX+R-Y restricts to one of
    X+R-Y, which is infeasible.
  - Before `F`, the preregistration's confirmation run (precondition 6′) requires the writer's own solver and
    verifier to reproduce all of these: the base infeasibilities, X+R-Y and GX's completions included. So they no
    longer rest on reviewer code alone.
- **R-S.** Adds P★'s input with the switch cells supplied as a pair in `Z±` × `Z±` (`u` known), both herald
  branches. This varies the hidden switch laws that F1 never varies (§5.4).
  - **Scope (N7).** Each switch's `v` then becomes uniform, which adds hidden bits and new configurations. So
    F1+R-S lives on a larger `Ω` than F1's `Ω_reach`, and a restoration by R-S is not a completion of F1's
    `Ω_reach`.
  - Mixed patterns, `X+` with `Z±`, and other carrier inputs are not included.
  - Whether F1+R-S can be decided within the fixed budget is measured before `F` (stress fixture SF-3). The owner
    prefers declaring it out of scope if it cannot (c.6724832474). A narrower configuration may be proposed before
    `F` only with its scope and controls independently reviewed. After `F`, no narrowing and no additional budget is
    admissible, and an undecidable case is VOID. The formal decision is the owner's at the freeze.

### 6.4 Fixture H3 and the dichotomy (B3, N8, N9)

**Fixture H3.** Ontic space `(z, x, η)`, with `η` one bit. Block A (`η = 0`) holds the four point laws. Block B
(`η = 1`) holds the `⟨Y⟩ = ½` slice: the laws `(¾, ¼, 0, 0)`, `(¾, 0, ¼, 0)`, `(0, ¼, 0, ¾)` and `(0, 0, ¼, ¾)`. The
reads are point reads on all 8 configurations.

**What the reviewer's exact probes show.**
- H3 is infeasible.
- Block A alone is feasible, and block B alone is infeasible.
- Completing block B with `Y±` (R-Y) makes both spans full, so H3 becomes feasible by Lemma NC-F (control c-r3:
  preparation rank 8/8).
- R-U′ in block B is `(3/8, 1/8, 1/8, 3/8)`, the centroid of block B's four laws. It leaves the state cone unchanged,
  so H3 + R-U′ stays infeasible (control c-r3; the reviewer's independent LP agrees).
- **Under r4's definitions H3 is unchanged.** Each H3 preparation carries one value of `η`, so R-Uc = R-U′, which is
  again the centroid. H3 gives `CONTEXTUAL-RY` with `g_specific` true and `g_eta` false: its contextuality rests on
  `g`'s fixed law, which R-Y varies and R-Uc preserves.

**The restriction step and its support condition (R13-N19).** Removing preparations can coarsen the effect
equivalences, so restricting a noncontextual model to a sub-fragment needs a condition. It holds when the retained and
the removed preparations charge disjoint sets of points and the reads are point reads, with their complements and the
unit. Then:
- the retained preparations' equivalences are the same in the sub-fragment as in the whole, since every removed point
  read gives 0 on them;
- every relation among the sub-fragment's effects, with the unit rewritten as the sum of the retained point reads, is
  a relation among retained point reads, which also holds against the removed preparations, since those give 0 on
  every retained point read;
- so a noncontextual model of the whole, restricted to the ontic states the retained preparations charge, is one of
  the sub-fragment. On those states the removed point reads respond 0, so the unit equals the sum of the retained ones.

H3 meets the condition: blocks A and B charge disjoint points. N8's withdrawal of r1's step ("a noncontextual model
of the whole fragment restricts to one of block B") is therefore reversed: the step is valid. GX's "R-Y infeasible"
rests on the same condition for X's sector (§6.3). H3's, block B's and X+R-Y's infeasibilities are also the
reviewer's exact LP (`review/probes-full/p02.out`). No exact LP has been run on GX+R-Y itself, so its infeasibility
rests on the restriction alone until the preregistration's confirmation run (precondition 6′) decides it.

**What H3 shows.**
- The conjunction "L1/EXP witness, (b), (c)" can be met by **independent sectors**: block A carries a witness of
  `g` varied across preparations, and the contextuality lies in block B.
- Block B also meets L1, through its fixed bias `P(g = 0) = ¾`. So L1 inside a contextual block can come from a
  fixed law alone, and per-block fields are reported as facts, not as access.
- The property that sustains H3's contextuality, and the dual gbit's, is a **fixed conditional law** of `g` on a
  sector. That is M2D's Proposition B and M-FIX structure (M2D:561-587).
- H3 restates, for a prepare-measure fragment, M2D's counter-model to "fully fixed law is necessary" (M2D:568-583).
  Classification: ELABORATING.

**What follows for the round.**
- No label states that the dichotomy (M2D:728-733) fails.
- The round reports the measured conjunction **per herald block**: whether each block's sub-fragment is infeasible,
  and whether an L1 or EXP witness branch lies in an infeasible block. Block sub-fragments carry coarser effect
  equivalences, so these are reported facts about sub-fragments. They do not locate the whole fragment's contextuality.
- The dichotomy itself remains an enumeration (M2D:706-727), in agreement with the audit's outcome 3.

## 7. Physical absence of missing reads or preparations (M2D:528-529)

A proof that a missing read or preparation is physically absent needs all of the following:

1. **The class, stated.** Supplies, access posits, dynamics, adaptivity, reuse, composition and horizon.
2. **A universal statement.** Every read's response, or every reachable preparation, lies in a subspace that excludes
   the missing direction. A failed construction or an empty search is not this.
3. **A proof.**
   - An **invariant** preserved by every primitive of the class proves absence for the whole class. AP1's grading is
     the model (AP1:522-529).
   - An **exhaustive exact enumeration** proves absence within its finite class only, and the claim must carry its
     bounds. This follows the owner's c.6723571280: "failure to construct a witness is not proof that no witness
     exists, unless a theorem establishes that impossibility within a clearly stated scope".
4. **The reason, stated without the comparator** (M2D:839; MID:573).
5. **No target-motivated restriction** (CC-RECON, M2D:266).
6. **Robustness** under the class's composition, reuse and recombination.
7. **Typing.** Each item the absence depends on is typed native, empirical or imported (c.6723491138). Hidden-prior
   dependence is named in scope (c.6723585151).

**For `G_SM`.** No invariant is known. AP1's grading fails for it (M2D:531-535).

## 8. Findings for the coordinator (paper; not adopted)

| id | finding | class | bears on |
| --- | --- | --- | --- |
| F-1 | The audit's literal check is feasible by an explicit model (Proposition F0). Under the audit's rule it closes the instance for its prepare-measure fragment, an outcome to preserve | CONFIRMING (reviewer probe) | AUDIT-C2 §17; the ARP-3 freeze decision |
| F-2 | Missing preparations fake contextuality as missing reads do; the dual gbit is the gbit re-coordinatized; the gate's R3-B2 text guards reads only; with both guards G5 credit always needs a physical-absence proof | ELABORATING | gate draft r4 L75-79 |
| F-3 | A prepare-measure LP does not test transformation noncontextuality | — | AUDIT-C2 §17; gate L73-74 |
| F-4 | P★ supplies `(0, 0)` cells outside SA-1(c), which M2D's ledger files as P2 | NEW (ledger) | M2D:207; any P2-class use of P★ |
| F-5 | Under P2, native inputs never vary `g`; variation of `g` arises only through conditioning, with the carrier correlated with `η` (HC-1) | ELABORATING | where the question lives |
| F-6 | H3: a classical fixture meets "witness, (b), (c)" through independent sectors; the sustaining property is a fixed conditional law (Proposition B) | ELABORATING | M2D:728-733; the round's texts |
| F-7 | With the audit's own access notion, P★ meets (a) inside F1, and (b) follows from (c); the conjunction reduces to (c), so attribution and physical absence carry the content | ELABORATING | AUDIT-C2 §17 |
| F-8 | F1 has `r_S ≤ 6` from one relation per herald; its likely degeneracy sits in the fixed switch-cell laws | NEW (instance; reviewer) | the R-S completion |
| F-9 | "Experience without certification" (`EXP ∧ ¬X3`) is exhibited by the audit's literal fragment F0, which has an exact noncontextual model; it is compatible with classical imitability | ELABORATING (paper; control c-r3) | the owner's c.6723889799 question |
| F-10 | Lemma NC-F's example of no converse was wrong in r1/r2: F0 is nondegenerate (`d = r_S = r_E = 3`), so Proposition F0 also follows from Lemma NC-F; a correct degenerate-yet-feasible example is point laws with the `Z` read alone | correction | §5.2 |
| F-12 | r3's `g_specific := RY ∧ ¬RU′` gives a misleading negative when `g`'s law is fixed conditionally on `η` (fixture Q, the reviewer's exact counterexample). R-Uc, which keeps the joint law of `(g, η)`, repairs it: `g_specific := RY ∧ ¬RUc`, with `g_eta := RU′ ∧ ¬RUc` | correction (reviewer; control c-r4) | §6.3; the preregistration's derived fields |
| F-13 | With two independent causes (fixture GX: a fixed `g` law in one sector, an `x ⊕ η` correlation in another) no single completion restores, and both specificity tests read "no", although one cause is `g`'s law. A "no" is a test result, not independence; the NONE addendum does not locate the degeneracy | correction (reviewer r4 B1) | the preregistration's renderings, NONE addendum and ADA |
| F-11 | On F1's preparation structure, CONTEXTUAL is the generic LP outcome (`r_S ≤ 6` against 36 reads; all three reviewer synthetic F1-shaped fragments were contextual, illustrative only, not `G_SM`); the information is in the completion set `{S}` | ELABORATING (reviewer N9) | how a CONTEXTUAL token is read |

## 9. Open items

- **O-1.** The reading of the functional: G-Y, G-H1 or G-H2 (§2). The owner decides at the freeze.
- **O-2.** The read class: single reads per run, with no joint non-terminal records. Owner and reviewer question.
- **O-3.** The supply class: P★'s mixed class. Owner and reviewer question.
- **O-4.** Whether `G_SM` supplies a T2 read with INT, or with X3. This is measured in-run within Π_fin and was not
  computed here.
- **O-5.** The gate's preparation-side guard (F-2), an owner and reviewer question.
- **O-6.** Transformation noncontextuality and sequential fragments are not in the round (candidate new round).
- **O-7.** F1 versus the literal check, and whether to run F1 at all, are decided by the owner at the freeze.
- **O-8.** The physical status of a fixed conditional law of `g`, or of a switch law (N2, M2D:584-587), is outside
  the round.
- **O-9.** Literature. None of the following was read first-hand, and no verdict rests on any of them:
  - Spekkens 2008;
  - Schmid, Selby, Wolfe, Kunjwal and Spekkens 2021;
  - Schmid, Selby, Pusey and Spekkens, structure theorem;
  - Selby et al., PRA 107 (2023);
  - Selby et al., "Linear program for testing nonclassicality …", PRL 132 (2024);
  - Spekkens et al., parity-oblivious multiplexing, PRL 102, 010401 (2009), for POS-1's bound;
  - Spekkens' toy theory, PRA 75, 032110 (2007), for NEG-1;
  - Mazurek et al., Nat. Commun. 7, 11780 (2016), and the discussions of tomographic completeness (Schmid et al.;
    Müller and Garner 2023), for E-EQ.

  The round checks every certificate against the definition, with facets re-enumerated by the verifier.

## 10. Controls (scratch; not evidence)

| control | file | sha256 | result |
| --- | --- | --- | --- |
| c-pstar | `controls/ctl_pstar_table.py` | `71decb7ee05335de87cbc06edd900fddf06d12f99ce1291376898d3ed829a1e2` | P★ exact at `L = 9, 12, 13`; mechanism off gives `Z±` |
| c-alg | `controls/ctl_paper_algebra.py` | `fec92403223df38f3ae4e73bc135e59443c23c5f4b5649043669d4e096a6db0c` | Proposition F0's model; `Z`/`X` Fourier orthogonality; the dual gbit's facets; H3's block B is a rectangle with facet point reads; the POS threshold |
| reviewer probes | `review/probes/{nclp,probes}.py` | `4c37b49f…`, `c955b857…` | exact LP results quoted in §§4–6, including the facet-drop hazard (B5) |
| c-r2 | `controls/ctl_r2_fixtures.py` | `9c15f3d38a08fb645a683d61ccb77d98385dc2ad69c31b5a4f671bbd8d2e39f5` | r2's fixture claims. **Not independent:** it imports the reviewer's `nclp.py` |
| c-r3 | `controls/ctl_r3_fixtures.py` | `0227e23b6fcf71a179551502b0b7a2abe45e229c09b262ade0f4df477fc8de33` | no LP, no reviewer code: the R-U′ laws lie in the convex hull of existing preparations in GBIT, DUAL and H3 (in H3, the centroid of block B), so the cone is unchanged; H3 + R-Y preparation rank 8/8; the `g` read is a sum of point reads; fixture SW's switch preparation rank is 3 without R-S and 4 with it; F0's EXP and ¬X3; F0's ranks `d = r_S = r_E = 3`; the degenerate-yet-feasible example |
| c-r4 | `controls/ctl_r4_fixtures.py` | `19962f24e3c3ce7acd6be3c5cea116203803de8bdc7ef1af031a7b039f38c5b3` | no LP, no reviewer code: the ranks `(d, r_S, r_E)` on the charged points for G, X, Q and each completion, with the first applicable method step; R-Uc is the centroid in G and in Q; `g` is marginally uniform in Q and X, and `P(g = 0 \| η = 1) = ¾` in Q; F10 is degenerate with `r_S ≠ d`, so step 4 decides it; ZPT has `r_S = d < r_E`, so step 3 applies |
| reviewer probes3 | `review/probes3/` | see `REVIEW-ACCESS-r3.md` | the independent facet × facet LP: all fixture tokens, G/X/Q, F-10, and the mutated certificates |
| reviewer probes2 | `review/probes2/` | — | independent reduced exact method; fixture tokens with R-U′; scale timings (preregistration *Method*) |

The EXP arithmetic in §6.1 uses P★'s published law only.

## 11. Disposition of the reviews

### Review of r12 (`review/REVIEW-ACCESS-r12.md`) → r13

| finding | disposition |
| --- | --- |
| N1–N6 | Preregistration and PLAN only. No change to this note's analysis |

### Review of r11 (`review/REVIEW-ACCESS-r11.md`) → r12

| finding | disposition |
| --- | --- |
| B1–B2, N1–N9 | Preregistration and PLAN only (E-READ, E-ID and E-BIND as neutral owner decisions; GT-6, GT-6b, GT-7 and GT-2b; identity-qualified invariant rows). No change to this note's analysis |

### Review of r10 (`review/REVIEW-ACCESS-r10.md`) and owner decisions c.6726548830 → r11

| finding | disposition |
| --- | --- |
| B1–B3, N1–N5; c.6726548830 items 1–5 | Preregistration only (the Environment-gated job B, gate tests, allowlist closure, trees-API fallback). No change to this note's analysis |

### Review of r9 (`review/REVIEW-ACCESS-r9.md`) → r10

| finding | disposition |
| --- | --- |
| B1–B4, N1–N7 | Preregistration only. No change to this note's analysis |

### Review of r8 (`review/REVIEW-ACCESS-r8.md`) → r9

| finding | disposition |
| --- | --- |
| B1, B2, N1, N3 | Preregistration only. No change to this note's analysis |

### Review of r7 (`review/REVIEW-ACCESS-r7.md`) → r8

| finding | disposition |
| --- | --- |
| B1, B2, N1–N4 | Preregistration only. No change to this note's analysis |

### Review of r6 (`review/REVIEW-ACCESS-r6.md`) → r7

| finding | disposition |
| --- | --- |
| B1, N1, N2 | Preregistration only: the event guard on step 3, replay only on dispatch, the no-unapproved-F1 rule, control W's guard check and M-GUARD; C-STATELESS's evaluator and halt; the timeout inputs recomputed from `design-run.json` timestamps, with edge cases. No change to this note's analysis |

### Review of r5 (`review/REVIEW-ACCESS-r5.md`) → r6

| finding | disposition |
| --- | --- |
| N1–N4 | Preregistration only: 6′ verified mechanically by `check --freeze`; tree differences stated; 6′ records in S1; C-STATELESS; exact `σ` with `W_fix` counted twice; `DERIVED` keys named as tests; C-INDEP's full-`FunctionDef` coverage, runtime types and M-INDEP variants. No change to this note's analysis |

### Review of r4 (`review/REVIEW-ACCESS-r4.md`) → r5

| finding | disposition |
| --- | --- |
| B1 | §6.3: GX added to the fixture table, F-13 recorded, and paired completions named as an owner decision. The preregistration renders "R-Y restores and R-Uc does not: yes/no" with a frozen caveat on "no", rewords the NONE addendum, freezes GX (`CONTEXTUAL-NONE`), and adds an ADA row that marks a "no" as not attributed |
| B2 | Preregistration: the budget maxima are taken over every non-F1 fragment; `--fixture-output` exits 3 on any mismatch; `stress.json` v2; confirmation run 6′ of the exact S1 tree (one substitution), pinned. §6.3 notes that this removes the circularity |
| B3 | Preregistration: the common clause's hidden-law sentence has two frozen forms; A-SWITCH has two entries; the RS drop is limited to F1's alphabet, so SW and SW− keep R-S; the RS-dropped note path is self-tested |
| N1–N7 | Preregistration: `decide` recomputes the derived fields, and `verdict` prints a `DERIVED` line; C-INDEP whitelist and JSON-only certificates; mutations invalid by construction, with M-BUDGET on step 3 and in-loop; Q+RY named as step-4 feasible with `T > 0`, and C-NCF's step-4 runs verified; the timeout test includes steps 8–10, and `W` is called a proxy; the stress pin is linked to the design run's artifact; `PENDING` fields for the timeout inputs and the confirmation run |

### Review of r3 (`review/REVIEW-ACCESS-r3.md`) → r4

| finding | disposition |
| --- | --- |
| B1 | R-Uc added; `g_specific := RY ∧ ¬RUc`; `g_eta := RU′ ∧ ¬RUc`; fixtures G, X and Q frozen with their tokens; F-12; H3 unchanged (§6.3, §6.4; c-r4). The preregistration's derived fields, texts and ADA rows are updated |
| B2, B3, B4 | Preregistration: C-INDEP and the verifier's re-derivation; the mutations; the step-3/step-4 fixtures; `--stress`, `stress.json` and the step-7 marker; `timeout-minutes: 60`; the work budget; the mechanical freeze rule; the timeout test; the host-VOID definition; M-BUDGET; the RS-dropped texts; the review requirement for a narrowed R-S; no change after `F` |
| N1 | §6.1: "Equivalently" is restricted; it implies L1 in the original or a refined branch, not the converse |
| N2–N7 | Preregistration (ADA attributions, the ladder rows, SW's scope, field hygiene, the method's tie-breaks, the block rendering) |

### Re-review of r2 (`review/REVIEW-ACCESS-r2.md`) → r3

| finding | disposition |
| --- | --- |
| B1 | R-U replaced by the `g`-law-preserving R-U′; `g_specific := RY ∧ ¬RU′`; H3 now gives `CONTEXTUAL-RY` with `g_specific` true (§6.3, §6.4; control c-r3); the preregistration's tokens, texts and ADA rows are updated |
| B2 | Preregistration (the frozen scalable method, stress fixtures, deterministic budget, owner decision on R-S) |
| N1 | EXP renamed "read-record dependence (correlational)"; F-9 recorded in plain terms (§0 item 4, §6.1) |
| N2 | X1 → nondegeneracy, one direction only; the converse fails; (b) is fixed as the degenerate pairing (§6.2). This exposed F-10 |
| N3 | Per-herald claim restricted to ontic relations; "non-spanning" replaces "degenerate" (§5.4) |
| N4, N5, N6, N7 | Preregistration |
| N8 | PLAN §4 (16 effects) |
| N9 | F-11 |
| Independence | c-r2 marked not independent; c-r3 added |

### Review of r1 (`review/REVIEW-ACCESS.md`) → r2

| finding | disposition in this note |
| --- | --- |
| B1 | L1 is the reference access notion; EXP is the owner's notion on reachable laws; INT is a counterfactual diagnostic; the departure is declared; P★ meets L1 and EXP in F1 (§6.1, F-7). r1's `acc_meas` and HORN texts are withdrawn |
| B2 | R-U and R-Y are defined at `τ` on P★'s branches and differ by one pure-`g` direction per branch; the completions are reported separately (§6.3) |
| B3 | Per-herald-block conjunctions are reported; no dichotomy sentence; Proposition B cited (§6.4) |
| B4 | G-H1 and G-H2 added to the readings, with the declared departure (§2); R-S added (§6.3); `r_S ≤ 6` and the per-herald relations recorded (§5.4) |
| B5 | Verifier facet re-enumeration and the facet-drop mutation are in the preregistration; recorded in O-9 |
| B6 | The evaluator's positive control is in the preregistration (C-EVAL) |
| B7 | F0 is reported as the outcome of the literal check (§4, F-1); F1 is a new question with its changes declared |
| N1 | Scope, equivalence, one-directional, `Ω`-relative, ELABORATING (§5.2) |
| N2 | Preregistration (certificate orientation) |
| N3, N4 | Preregistration (texts; SIZE-DEPENDENT removed) |
| N5 | §5.3, F-2 |
| N6 | Preregistration (CC-OFF conditions) |
| N7 | Owner records quoted verbatim (header) |
| N8 | Restriction step withdrawn; LP cited (§6.4) |
| N9 | F-6 classified ELABORATING |
| N10 | §1, §3 |
| N11 | §1, F-4 |
| N12 | Preregistration (POS-1 realized as laws) |
| N13 | O-9 |
