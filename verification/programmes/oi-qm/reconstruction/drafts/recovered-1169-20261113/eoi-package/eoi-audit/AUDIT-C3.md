# EOI audit, phase 2: cluster C3, inaccessibility and hidden-sector modelling (A2, A3, A4), revision r3

Snapshot: `origin/main` = `5ce4f98ec3a76aee6fdd17ed1bad7b278f1d9732`. Read-only and paper-only. No repository
edit, build, computation or GitHub write was made. r1 and r2 are kept as `AUDIT-C3-r1.md` and
`AUDIT-C3-r2.md`. r2 applied `REVIEW-C3.md` (B1–B6, N1–N12). r3 applies `REVIEW-C3-r2.md` (B1–B2, N1–N4).
Both dispositions are in the final tables.

**Hand-checks.** §0 contains pencil algebra over `F_2` on the records' own definitions. It is not evidence and
is not committed. No outcome, classification or over-reading flag below rests on §0 alone. Where a §0 item
bears on a statement, the record-level source is cited beside it. Where no record-level source exists, the item
is marked "(rests on a hand-check)" and is offered only as a pointer.

**Abbreviations.**
- `R/` = `verification/programmes/oi-qm/reconstruction/`.
- MI-D, MI-R, MI-A1, MI-A3 = `R/minacc-1-20261108/{DESIGN,RESULT}.md`, `amendments/A1-prereg-review.md` and
  `amendments/A3-post-result-prot-r.md`.
- QA = `R/quarter-phase-native-20261107/DESIGN.md`; QA-PR = its `PROOF-RECOVERY.md`.
- FB = `R/quarter-phase-feedback-20261107/RESULT.md`.
- AP1 = `R/apparatus-1-20261107/DESIGN.md`.
- M2D = `R/mechanism-2-20261108/DESIGN.md`; M1D = `R/mechanism-1-20261107/DESIGN.md`.
- OA = `R/observer-access-20261106/ASSESSMENT.md`; CR = `R/correlation-recombination-20261107/DESIGN.md`.
- Main, GR, Cplx = `papers/{Main,GR,Complexity}.md`; FULL = `book/The-Incompleteness-of-Observation-FULL.md`.

Every line number was re-read at the snapshot. MI-D, MI-R and the MI amendments are themselves
**WIP / UNVERIFIED**, reviewed by a model only (MI-D:3-4; MI-R:3-7; MI-A3:9).

**Outcome rule, applied to protection and exposure alike.** The outcome concerns the result as stated. A
citing text that reads it more strongly is recorded separately and does not change the outcome.
- **1:** the statement lists, or is explicitly scoped by, every hypothesis its proof uses, and its conclusion
  does not go beyond them.
- **2:** the proof uses a hypothesis that is absent from the statement, or the conclusion is phrased beyond its
  hypotheses. Each missing item is named, with the proof step that uses it.
- **3:** a questionable assumption materially affects a claim, and no record decides it.

**Central answer.** The inaccessibility proved in this cluster (AP1 Lemma 3, QA Lemma Q(iii)) is a joint
property of two things, and neither suffices alone.
- *The native step.* This is the symmetric, center-free linear second-order step at `q = 2`. It is necessary:
  under the same P1/P2 interface, `G_σ` exposes while `N_1` and `N_0` protect (MI-R:64-66, 310-314), and
  allowing center terms breaks the protection (QA:518-521).
- *The supplied SA-1 interface.* P2 (one known slot per ready cell, with full joint support of the unknowns,
  QA:499-501), together with the symplectic step, gives single-time isotropy (AP1:539-541, 547). P1 terminal
  registration makes that isotropy survive retention across time (AP1:335-336, 560-561; S-L7 at AP1:252).
  Each is load-bearing (QA:779-780; MI-R:373-374). P1 is supplied, and the native rule does not enforce it
  (AP1:338-343).
- *Measure.* Determination depends on the support of the hidden law. Only non-bias and the per-state bounds
  need the product-uniform law (N2 with H-PS).

The converse direction runs on the same interface. M-INACC-1's exposures `E_A` and `E_B` are configuration-level
identities that hold pointwise in every branch (MI-R:160-164, 250-256). `E_A′` exposes only on a 1/16 branch
(MI-R:283-285). They use P2 half-known cells (a known-1 cell through H-PREP, or `E_A′`'s branch) and P1
registration. The alternative baseline, the programme's earlier passive
two-slice interface, determines `Q* = 1` functionals (QA:512-516). It is a stronger access idealization
(AP1:331-333; CR:52-62), not Main's observer.

So protection and exposure are both statements about supplied interfaces on a given native step. Neither
transfers to a physically sourced embedded observer. The proofs are sound at their stated scope. The
over-readings sit in the labels "native protection" / "Derived from A4" / "native instance" and in the words
"never" / "permanently", applied to information that has moved to archived cells. On the manuscript side, the
over-reading is GR's "theorem of Part I".

## 0. Hand-checks (pencil algebra; not evidence)

**0.1 `E_A` identities.** These are the identities MI-R:229-256 states.
- The `t = 0` cells are those of MI-R:222-228. Step 1 gives `u_{−1}(1) = 1+x`, `u_0(1) = y+1` and `v_0(1) = x`.
- After the refills of MI-R:236-242, step 2 gives `u_{−1}(2) = y`, `u_0(2) = x+1` and `v_0(2) = y+1`.
- These hold for every assignment. The record itself states the per-branch identity
  `(u_0(2), v_0(2)) = (r_1, r_2+1)` "in every record branch" (MI-R:250-252), and self-check c1 reports it "in
  all 65 536 assignments" (MI-R:593).
- So the determination needs no prior. MI-R:255's "every full-support prior" is weaker than the record's own
  identities support.

**0.2 One-tick variant without gate-write refills (rests on a hand-check).**
- Set-up: `R = {−2,…,2}`.
  - Cell 0 is ready, with known `v = 0` and unknown `u = x`.
  - Cell −1 is ready, with known `v = 0` and unknown `α`.
  - Cell −2 has known `u = 1` (H-PREP).
  - Cells 1 and 2 have known `u = 0`.
- One tick of `G_σ` gives `u_{−1}(1) = 1+x`, `u_0(1) = OR(α,1)+OR(0,0) = 1` and `v_0(1) = x`.
- Registering `u_{−1}(1)` makes the active, unregistered cell 0 sharp in every branch. Under `N_1`,
  `u_0(1) = α`, so cell 0 stays masked.
- `Π_A` still performs the refill that accompanies every registration (MI-D:361-362). What this variant omits is
  the use of refills *as gate writes* (MI-A1:203-207).
- It therefore suggests that gate-write refills are not necessary for a `Π_A` exposure when a known-1 cell is
  available. This is a pointer only.

**0.3 Support, not independence, is what carries determination (confirms QA:499-501).**
- Set-up: a source cell `h = (a, b)` and a meter `m = (w, 0)` with known `v_m = 0`.
- *Exact correlation.* Take `w = b` exactly: a support restriction of the kind CR:91-103 constructs. A native
  minimal X read of `h` registers `b`, and the untouched cell `m` is then sharp. Its `u+v` is determined, and the
  known set `{v_m, u_m + v_h}` has `ω = 1`.
- *Full-support correlation.* Take `P(w = b) = 3/4`. The same read leaves `u_m+v_m = w` with conditional law
  `(3/4, 1/4)`. It is biased, not determined. (Provenance only: the review note REVIEW-C3 B3 reports the same.)
- So the load-bearing part of P2's "unknown, uniformly distributed, independently of everything else"
  (AP1:297-299) for determination is the support condition. This is what QA:499-501 and the definition
  "constant on the support" (MI-D:135-137) already say. Under SA-1 the record-level instance is C-P2, a
  degenerate-support supply: "A supplied cell with known `u + v` has that functional determined while active,
  under any rule" (MI-R:374; also QA:780).
- Independence and uniformity carry non-bias only.

## 1. M-INACC-1 (INV-RECON row 2): exposure under `G_σ`, outcome pair (B, B)

- **Statement as made.** "Within the registered scope (`G_σ`, the stated classes, P1, P2), the symmetric
  state-dependent graph does not preserve Lemma Q(iii)'s protection" (MI-R:91-93). "The negative concerns `G_σ`
  and these classes only" (MI-R:96).
  - `Π_A`: (B-D) by `E_A` (MI-R:50-53, 220-256).
  - `Π_B`: (B-D) by `E_B` (MI-R:44-49, 129-165).
  - `E_A′` (known-0 supplies only): (B-D) on a 1/16 branch, with bias in the other branches on c2's instance
    (MI-R:258-295).
- **Where proved.** The explicit protocols in MI-R §§2-3; the controls in MI-R:365-382; the linear limits in
  MI-R:394-433. Standing: WIP / UNVERIFIED (MI-R:3-7).
- **Hypotheses and where each enters.**
  - `G_σ`, a proposal that is neither adopted nor physically sourced (MI-D:167-181, 239-242). It enters every
    tick.
  - `q = 2` (MI-D:595).
  - P2 ready cells (MI-D:297-301). They supply the readers and the gate saturators at MI-R:225-228.
  - P1 registration with archive (MI-D:351-365). It produces `r_1` and `r_2` at MI-R:236-246.
  - Archive-swap refills used as supplied gate writes (MI-A1:203-213). They reset the OR terms at MI-R:236-242
    and :305.
  - Registration and swap take place "between ticks" (MI-D:355).
  - H-NW and a finite ring (MI-R:531-532).
  - N2 and H-PS enter only `E_A′`'s branch probability and bias count (MI-R:533; MI-A1:301-306).
  - `E_B` additionally uses P3, E-iso and the A2.2 conventions (MI-R:167-177).
- **A2/A3/A4.**
  - A2: N. No unknown slot is read (MI-D:400-404).
  - A3: N for determination, which is pointwise (MI-R:250-252). Y only for `E_A′`'s probabilities.
  - A4: Y. The protocols use fresh known cells, instantaneous archive and refill, and the complete joint record,
    all named in MI-R:297-318 and :546-553.
- **Symmetric scrutiny.**
  - The exposure uses the supplied capabilities P2, P1 and H-PREP or refills. It shows that within the SA-1
    interface `G_σ`'s gate defeats Lemma Q(iii) (CC-OFF green, MI-R:310-314, 367-368).
  - It does not show that a physically sourced observer could expose. It also says nothing about other graphs
    or access posits (MI-D:478-479; MI-R:618-622).
  - The PROT-R defect made outcome (A) unreachable (MI-R:71-76, 435-452). The (B-D) verdicts rest on PROT-D and
    PROT-B, with C-LIN green (MI-R:370, 454-455).
- **Outcome: 1.** The conclusion is scoped and its hypotheses are carried (MI-R:530-535, 616-624). **Class:
  conditional** (configuration-level; no import, MI-R:491-503).
- **Over-reading texts.**
  - None found in the direction of reading the negative more strongly.
  - MI-R:255 understates the result: the identities are pointwise (§0.1).
  - MI-R:84-85 and :526-529 list "archive-swap refills" among the minimal `Π_A` resources used as gate settings.
    This may be stronger than necessary when a known-1 cell is available (rests on a hand-check, §0.2).

## 2. M-INACC as a premise, and the reading of Lemma Q as its "native instance" (M2D)

- **Statement as made.**
  - M-INACC has three clauses (M2D:832-840): (a) "the fixed rule uses it, so later statistics depend on it";
    (b) "no permitted preparation, read, reuse or recombination determines it or changes its conditional law";
    (c) the inaccessibility "follows from a structure stated without reference to the quantum target".
  - "Native class N has a native instance: Lemma Q protects every functional with `Q* = 1`" (M2D:853-854).
  - "Non-reciprocal state dependence escapes native protection arguments" (M2D:947).
- **Findings.**
  - MI-A1:59-70 records that clauses (a) and (b) "cannot both hold under these readings". The readings are a
    statistical reading of (a) and a reading of (b) as retrodictive non-change of the conditional law. The record
    calls this "a definitional observation, not a result". Any later use of M-INACC as a premise must state its
    reading, or use the USE-ctx form (MI-A1:78-103).
  - Lemma Q meets (b) only under P1 and P2 (QA:472-474, 779-780), only for functionals on currently active cells
    (§3), and for non-bias only under N2/H-PS.
  - Clause (c) is doubtful for P2. Its stated motivation is "closure plus the E-AR obstruction, and the latter is
    a programme-internal reason. This is the weakest link" (AP1:347-349). E-AR is the `C²` bound "at most two
    perfectly distinguishable preparations" (AP1:439, 677).
- **Outcome for the claim M2D:853-854 ("native instance"): 3.**
  - The claim is stronger than Lemma Q's proof. Whether any form of it holds once the supplied archive isolation
    is relaxed is decided by no record.
  - The follow-up below is named and not adopted.
- **Named follow-up, M-ARC (not adopted, not run).**
  - *Model.*
    - Ring `Z_L` under the always-on linear rule `N_1` at `q = 2`.
    - Fixed visible window `V` of `w` sites; `H` = the rest.
    - At `t = 0` every site of `V` holds a P2 ready cell (known value 0, or 1 through H-PREP). Every site of `H`
      holds a source cell.
    - Registration happens between ticks: at most one slot of one `V` cell per tick, and each cell at most once.
    - No refills and no swaps.
    - *Archive, variant D (de-isolated):* a registered cell stays at its site under the always-on rule. Its
      site leaves `V` and joins `H`, and it is never registered again.
    - *Archive, variant I (isolated):* the registered cell is removed from the ring and takes free ticks, as in
      MI's archive (MI-D:357-358). Its site is left decoupled.
  - *Question.* In variant D, is any `Q* = 1` linear functional on the cells of the current `V` determined in a
    positive-probability branch within the horizon?
  - *Controls.*
    - **CC-ISO** (countercontrol; makes "protection holds" reachable): variant I must give PROT-D, reproducing
      Lemma Q(iii) as in MI-R:394-428.
    - **C-NV** (non-vacuity): in both variants some `Q* = 0` functional on `V` must be determinable, e.g. one
      carrier slot read through a meter.
    - **C-SUPP:** in variant I, a supplied pair with an exact relation (a support restriction, §0.3 type) must
      expose. A full-support correlated pair must give at most bias.
    - **C9:** in variant I, re-coupling a registered cell must expose (AP1:682).
    - **Horizon and size:** fix `T ≤ |H|`. At one site per tick this means no influence leaves `V`, travels
      through `H` and re-enters `V` from the other side within `T` (no wrap-around through `H`). In variant D the
      archived site is adjacent to `V` and couples back within one tick, which is the de-isolation under test.
      AP1:338-341 is cited only for the separate point that archive isolation is relative to a budget.
      Repeat at `|H|` and `|H| + 2`.
  - *Parameters.* `w = 3`, `T = 4`, `|H| ∈ {4, 6}`, hence `L ∈ {7, 9}`.
  - *Method.* Exact linear algebra over `F_2`.
    - Enumerate every registration schedule up to `T`: at most one registration per tick, a choice of `V` cell
      and slot, each cell at most once. An adaptive schedule is a fixed schedule within each record branch.
    - For each schedule, transport the known functionals `I_t` and the registered functionals `R_t` through the
      linear steps, and form the span restricted to functionals supported on the current `V`.
    - Under a full-support law, determination in a branch is membership in `span(I_t ∪ R_t)`. That is the
      same in every branch of a fixed schedule, and the known values (0 or 1) only translate it. N2 does not
      enter.
    - The controls are evaluated by the same method. C-SUPP adds the exact relation to `I`. Its full-support
      part (bias) needs the conditional law under a stated non-uniform law.
  - *Decision rule (to be preregistered before any run).*
    - **Exposure:** some schedule and tick give a `Q* = 1` functional on the current `V` in the span, at both
      `|H|` values, with CC-ISO, C-NV, C-SUPP and C9 green.
    - **Survival:** no schedule up to `T` gives one, at both `|H|` values, with the same controls green.
    - **Size-dependent:** the two `|H|` values disagree. This is reported and is neither label.
    - **Void:** any control fails.
  - *What each result would show.* All of this is subject to the decision rule.
    - An exposure in D within `T`, stable in `|H|`: this de-isolated interface does not protect at that size and
      horizon. Lemma Q's protection then needs archive isolation beyond the fixed partition.
    - Survival: protection within that finite model. It stays conditional on P2's support clause, on H-PREP for
      known 1, and on the supplied registration.
    - Determination does not use N2. Any bias statement would.
    - Neither result is universal.
- **Class: conditional.** M-INACC is "Supplied" (M2D:779).
- **Over-reading texts.**
  - M2D:853-854 "native instance" and M2D:947 "native protection arguments". The proof supports protection of
    currently active functionals under the supplied P1/P2 on the native symmetric center-free step, with non-bias
    under N2/H-PS.
  - M2D:728-729 ("Every nonclassical route at `q = 2` needs an ontic functional … the observer can never
    access"): routed to the MECH-2 cluster (AW-EOI-1), scoped at M2D:109-113.

## 3. Q-A, Lemma Q(iii): protection of `Q* = 1` functionals (INV-RECON row 3)

- **Statement as made.** "Under P1 and P2, every functional on active cells that the observer can determine has
  `Q* = 0`. This holds for every process in N, adaptive or not, and for NNB couplings" (QA:472-474).
  - Result: "A functional with `Q* = 1` is therefore never determined, whatever the reuse, recombination,
    ancillas or records" (QA:51-53).
  - Verdict: "Natively (A4, at `q = 2`), and given the supplied P1 and P2, a functional with `Q* = 1` is
    permanently undetermined for the observer, whatever the protocol" (QA:523-525).
- **Where proved.** QA:476-495, through AP1 Lemma 3 (AP1:533-561). C-LIN extension at MI-R:394-433 (WIP).
- **Hypotheses and where each enters.**
  - *Symmetric, center-free linear step over `F_2`.* Stated at QA:462-464. Used at QA:478-486. Necessary: C-EX
    breaks with center terms (QA:518-521).
  - *P1.* Stated. Used at QA:492 through AP1:543-545. Load-bearing for retention: without it, the proof fails at
    `ω(ρ₁, f') = 0` (AP1:560-561; QA:512-516, 779).
  - *P2.* Stated. Used at QA:491 as "I is isotropic" (AP1:539-541). Load-bearing (QA:780; MI-R:374).
  - *Full joint support of the unknowns.* Used at AP1:547 ("determined iff `f = κ + ρ`").
    - It appears in Lemma Q only under "Properties" ("any full-support prior on the unknown slots will do",
      QA:499-501), not among the hypotheses (QA:460-474).
    - QA defines P2 without a law: "one known slot … fixes which functional is known, not its value"
      (QA:142-144). It assigns the law to N2 and says "Lemmas G1, G2 and Q do not use it" (QA:777).
    - It is necessary under SA-1: C-P2, a degenerate-support supply, exposes (MI-R:374; QA:780). §0.3 is
      consistent with this.
  - *N2 / H-PS (product-uniform).* Not used by (iii) (QA:777). Used by the non-bias claims: "uniform under N2"
    (QA:554) and C-LEAK's "nor biased" (QA:207).
- **A2/A3/A4.**
  - A2: N (QA:147-148, 484-486).
  - A3: Y. Support is needed for determination; the product law is needed for non-bias.
  - A4: Y. P1's archive isolation is not enforced natively (AP1:338-343). Complete-record retention is
    conservative for this claim.
- **Retrodiction.** Lemma Q bounds functionals on cells active at the time of determination.
  - A past value whose information has moved to an archived cell can be determined later, even in N. The
    countercase is "trivial: the ready cell's own unknown slot" (MI-R:446-448; MI-A3:21-38).
  - Retrodiction of information still held by active cells (PROT-R′) does hold in both linear limits
    (MI-A3:60-84).
  - Both records are WIP / UNVERIFIED.
- **Outcome: 2.** On QA's own terms, the proof uses a support hypothesis (AP1:547) that is not among the
  statement's hypotheses (QA:460-474). QA's P2 carries no law (QA:142-144), and QA assigns the law to N2, which
  Lemma Q is said not to use (QA:777).
  - *Counter-reading:* QA:48-50 and QA:780 cite apparatus-1's P2, whose SA-1(c) includes "uniformly distributed,
    independently" (AP1:297-299). On that reading the statement would carry support, and the outcome would be 1,
    as for AP1 Lemma 3.
  - **Class: conditional.**
- **Over-reading texts.**
  - QA:46, heading "A native protection of an absolute parity". The same paragraph qualifies it: "Under
    apparatus-1's supplied access posits P1 (terminal registration) and P2 (half-known ready cells)" (QA:48-50).
    The over-read is confined to the heading.
  - QA:799. In the §4.1 outcome table (QA:794-803), the capability cell reads "Holds as a selection rule (Lemma
    Q), given P1 and P2". The Status cell reads "Derived from A4 at `q = 2`". The Status cell is stronger than the
    proof: A4 is necessary, not sufficient, and the §3 ledger (QA:779-780) marks P1 and P2 load-bearing.
  - QA:51-53 "never determined" and QA:523-525 "permanently undetermined … whatever the protocol". The proof
    supports present-tense determination of functionals on active cells. "Never/permanently" fails only for
    information that has moved to archived cells (MI-A3:21-38). It holds for information still on active cells
    in the linear limits (MI-A3:60-84).
  - M2D:853, :947 (§2).
  - M1D:1048-1050 is qualified ("under P1 and P2") and is not an over-reading.

## 4. Q-A secondary results: Lemma G2 and the R1 C-CP recovery

- **Statements.**
  - Lemma G2 (QA:342-385): no non-adaptive encoded `S` with native X reads and comparator statistics, "with a
    hidden sector of any size, finite or not" (QA:36-40).
  - R1 C-CP: holds "under R1 on the fixed active carrier and the stated non-adaptive product-ready instrument
    inputs" (QA-PR:140-143).
- **Hypotheses.**
  - G2 is a pointwise identity (QA:366-368). It "uses no measure, so it holds for any hidden prior and any
    hidden-sector size" (QA:374-375). It needs non-adaptivity (QA:375-380) and supplied native minimal reads
    (QA:347-351).
  - The C-CP recovery uses the independent uniform product law. It excludes correlated or
    preparation-dependent backgrounds (QA-PR:12-25, 77-80, 140-143).
- **A3.** G2: N. C-CP: Y, declared.
- **Outcome: 1** for both. **Class: conditional.** C-CP uses an imported comparator (I1).
- **Over-reading texts.** None found. QA-PR:187-197 keeps the adaptive and distributed routes open.

## 5. FB: record feedback, quarter phase and C-CP (INV-RECON row 4)

- **Statement as made.** "For the homogeneous linear Pauli encodings and common preparation lift defined below,
  the answer is no as long as all constant slot translations remain available" (FB:16-19). FB adds that it
  proves no "general impossibility for OI" (FB:27-29).
- **Hypotheses and where each enters.**
  - H-L, full-support level-set preparations. Used at FB:97.
  - H-C, a common hidden lift. Used at FB:100. Without it, (1) at FB:104 fails.
  - H-T, all translations available. Used for `p ≠ 0` only (FB:117). It is "not derived physical availability"
    (FB:63-67).
  - C-CP, an imported target criterion (FB:78-83, 141-142).
- **A2/A3/A4.**
  - A2: N.
  - A3: Y. H-C excludes preparation-dependent lifts, which FB explicitly does not rule out physically
    (FB:58-61).
  - A4: Y. H-T is heralded, with the record retained (FB:67-69).
- **Symmetric scrutiny.** The `p = 0` branch uses only H-L and H-C. The `p ≠ 0` branch is a limit of an
  interface that has H-T. FB says that removing H-T without a source would repeat premise I, and it leaves bare
  adaptive S open (FB:152-161).
- **Outcome: 1.** **Class: conditional.** No over-reading in FB. Its reuse as H-LIFT belongs to the MECH-2
  cluster (M2D:319-321, 776; AW-EOI-1).

## 6. AP1: terminal registration, Lemma 3 isotropy and the apparatus ceilings (INV-RECON row 5)

- **Statements and hypotheses.**
  - **Lemma 2** (AP1:153-163): a bijective apparatus with fixed-law fresh cells and marginalization lies in the
    class ceiling. These are mathematical hypotheses. The physical reading requires the carrier to be the
    configuration basis.
  - **Lemma 3** (AP1:533-537), scoped "Under SA-1".
    - SA-1(a): the symplectic step (AP1:541-542).
    - (b) P1, used at the commutation step (AP1:543-545). It gives retention across time (AP1:335-336,
      560-561). It is not enforced natively (AP1:338-343).
    - (c) P2, giving single-time isotropy (AP1:539-541).
    - (c)'s "unknown, uniformly distributed, independently of everything else" (AP1:297-299) includes the
      support used at AP1:547.
    - The per-state form (AP1:557-560) uses the uniform law, which is also part of (c).
  - **Lemma 4** (AP1:689-696): "C-IS holds for SA-1". It uses (c)'s uniform law. AP1's marker says "a
    non-maximal-entropy hidden prior moves the same apparatus beyond the disk" (AP1:837-841, with the biased kick
    at AP1:824).
  - **Lemma 5** (AP1:731-733): "for any ancillas, adaptive record-conditioned corrections or input states".
    - The proof uses "Ancillas are attached in fixed laws independent of the carrier" (AP1:735).
    - That independence is not in the statement. It is a common-lift (H-C-type) hypothesis.
  - **Level 3** (AP1:72-75, 961-977): "excludes every finite carrier". The proof uses one stochastic matrix Γ
    applied `j` times, "as in Lemma 5" (AP1:962-963). That is a time-homogeneous action with fresh, independent
    ancillas, which the statement does not state.
  - **D1** (AP1:580-594, 686-687): on the declared domain, the three-record law equals the Lüders comparator.
    It uses P1, P2 with heralds, P3, E-iso and N2 (AP1:398-401, 413-423).
- **A2/A3/A4.**
  - A2: N. The controller loads coefficients as a supplied setting (AP1:288-291).
  - A3: Y (support and the uniform law in (c); ancilla independence in Lemma 5 and Level 3).
  - A4: Y (P1; P2 with heralds; E-iso; fresh meters, AP1:665-668).
- **Outcomes, by the rule at the head of this file.**
  - Lemma 2: **1**, class not applicable.
  - Lemma 3: **1**, conditional. Scoped "Under SA-1", which contains P1, P2 and (c)'s support.
  - Lemma 4: **1**, conditional. Scoped "for SA-1", whose (c) contains the uniform law.
  - Lemma 5: **2**, conditional. Missing from the statement: carrier-independent ancilla laws (AP1:735).
  - Level 3: **2**, conditional. Missing: a single time-homogeneous Γ with fresh independent ancillas
    (AP1:962-963).
  - D1: **1**, conditional, scoped to its declared domain (AP1:686).
- **Over-reading texts.**
  - AP1:732-733's own "for any ancillas" (see Lemma 5).
  - Downstream citations of Lemma 3's isotropy as a protection must carry "under SA-1". The uses found are QA
    Lemma Q (QA:487-492), which is qualified; M2D:853, which is not (§2); and M1D Theorem W (M1D:913-914), which
    is qualified in its ledger.
  - AP1:38-40 itself presents the restriction as holding under "posited access clauses".

## 7. Observer access (receiver assessment) as a cut (INV-RECON row 10)

- **Statement as made.** "a common uniform hidden background makes the immediate receiver law independent of it
  … Later access to the background can restore the signal exactly" (OA:11-14). Also: "forgetting K in a one-step
  marginal is not proof of lasting privacy" (OA:136-137).
- **Where proved and hypotheses.** Identity (2) at OA:103, with the controls at OA:112-137. Masking needs a
  uniform, independent incoming neighbour (OA:119-121). Recovery needs no independence (OA:133-134).
- **Bearing.** Under SA-1, the uniform kick `w` masks the conjugate at one time. Lasting privacy then requires
  that `w` never becomes accessible, and that is P1's role (C9, AP1:682; AP1:335-336). The masking is
  single-time. Its retention across time is supplied.
- **Outcome: 1.** **Class: conditional** (a bounded source verdict, OA:17-22). No over-reading found. AP1:250
  cites it accurately.

## 8. Correlation recombination as a cut (INV-RECON row 14)

- **Statement as made.** "two individually uniform hidden inputs can have a correlation that the native
  interaction turns into a definite receiver value. Neither input is first read" (CR:11-13). It is a
  "conditional classical correlation effect", with preparation and access not supplied (CR:15-19).
- **Where proved.** CR:118-140.
- **Hypotheses.**
  - The preparation `μ_b` is a conditional of counting measure with event mass `2^-87` (CR:91-107). It is
    support-restricted.
  - The receiver is a passive two-slice read, which CR itself calls not a complete embedded apparatus
    (CR:52-62).
- **Bearing.** CR is a merged construction outside Lemma Q's class on both counts: restricted support and no
  P1. There, hidden relations become definite without decoding. It does not expose a `Q* = 1` functional under
  P1/P2 and does not refute Lemma Q. It shows what lies past the class boundary, which is consistent with §0.3.
- **Outcome: 1.** **Class: conditional.** No over-reading found. The phrase in Issue #1169's body, "exposes a
  hidden relation", is consistent with the record.

## 9. Marker AW-EOI-2: uniform independent hidden slots (N2 through H-PREP)

Verdict, by half.

- **Determination.** Lemma Q(iii), AP1 Lemma 3 and PROT-D need full joint support of the unknowns (QA:499-501;
  MI-D:135-137). They need neither uniformity nor independence beyond that. A support-restricting correlation
  can determine (§0.3; CR:91-103 constructs such laws). MI-A1:303-304's "full-support product prior" is the
  record's chosen scope, narrower than the definition requires.
- **Non-bias and per-state bounds.** QA's C-LEAK and (A1)(b), AP1 Lemma 4, D1 and the R1 C-CP recovery need the
  product-uniform law N2 with H-PS or H-INF-μ (QA:554; AP1:837-841; QA-PR:16-25; MI-A1:305). Any correlated or
  non-uniform law, including full-support ones, can bias.
- **Exposures.**
  - `E_A` and `E_B` need neither condition: the identities are pointwise (MI-R:160-164, 250-252).
  - `E_A′` needs a positive-mass branch, and N2 for its bias count (MI-R:289-295).
- **Theorem W (M1D:66-69; odd `q`).** P2 is load-bearing (M1D:914).
  - Theorem W assumes that "every ancilla law has a quantum state as its R-W image" (M1D:473-474). That is a
    positivity condition on the law, not a determination condition.
  - Cross-cluster pointer for MECH-1: does a correlated or non-uniform hidden law, including a full-support one,
    preserve R-W positivity?
  - The `q = 2` sharp-cell argument of §0.3 does not transfer directly.
  - Provenance only: the r2 review's `q = 3` control reports a full-support law whose R-W image is not
    positive.
- **Related record (statistics half).** L3B defines H₀ (uniform product), H₁ (full-support Markov-correlated
  `v`) and H₂ (exact `u = v`) at
  `verification/programmes/oi-qm/interface/round-l3b-orthogonal-rule-controls/preregistration.md:164-168`.
  - Over-rank appears under H₁ in edge-permutive cells (`result.md:63-72`).
  - The ceiling is read at H₀ (`result.md:96`).
  - The quantity is a statistical rank, so this bears on the bias/statistics half, not on determination.

Classification (§A.31): **CONFIRMING.** The support/measure split is already in the records: QA:499-501 and
QA:777 for determination; QA:554, MI-A1:305 and AP1:837-841 for non-bias. **ELABORATING:** the exposure
side is prior-free, by the record's own pointwise identities (MI-R:250-252).

## 10. Marker AW-EOI-3: supplied access posits P1, P2, P3, E-iso and refills

Verdict.

- P2, with its support condition, and the symplectic step give single-time isotropy. P1 makes that isotropy
  survive retention. Each is load-bearing for Lemma 3, Lemma Q and Theorem W (QA:779-780; M1D:913-914;
  MI-R:373-374).
- P1's implementations are all supplied: P3 and E-iso arming in AP1 (AP1:342-343), and cell removal with swap in
  MI's `Π_A` (MI-A1:208-211).
- P2 and H-PREP supply both the protection and its defeat (MI-R:225-228). P3 and E-iso are not needed for the
  `Π_A` exposure (MI-R:306). Gate-write refills may not be needed when a known-1 cell is available (rests on a
  hand-check, §0.2).
- The native step is the other load-bearing factor (MI-R:310-314; QA:518-521).
- So the cluster's negatives (FB `p ≠ 0`; the MI exposures) and positives (Lemma Q) are all relative to supplied
  interfaces on a given step, as the records state (QA-PR:23-24; MI-D:117-119; MI-R:618-622; FB:27-29).

Classification: **CONFIRMING.**

## 11. MQ-33 (INV-MANUSCRIPT): GR:450, "inaccessibility … a theorem of Part I"

- **Statement as made.** "(ii-a) Construction-level invisibility (from Part I alone). The boundary modes
  comprising `S_dS` are hidden-sector degrees of freedom … By the trace-out structure, no hidden-sector degree of
  freedom maps to an operator on `H_V`. This is a theorem of Part I … the hidden sector is invisible to the
  emergent description by construction" (GR:450). Generated mirror: `papers/GR.tex:3016`.
- **Where it comes from.** It follows immediately from three definitions:
  - Main Lemma 2's partition, "not a modeling choice but the definition of embedded observation" (Main:50);
  - `H_V = ℂ^n` on the visible configurations (Main:268);
  - the partial trace in the Stinespring construction (Main:650).
  No Part I theorem states it.
- **Hypotheses not stated in the statement.**
  - The assignment of the boundary modes to `H` comes from the Part II horizon partition (GR:454).
  - The physical reading "invisible" also needs that no permitted dynamics carries boundary-mode information into
    `V`. That is not argued. Hidden memory is readout-relevant under (C4) (Main:594), and recovery under a fixed
    partition is possible (OA:132-137).
- **Flags.**
  - A1: Y, mild (the `ℂ^n` embedding, Main:268).
  - A2: N. Nothing reads hidden information.
  - Separate note under A3/A4: the inaccessibility is stipulated by the partition, not derived from the
    permitted interactions.
- **Outcome: 2.** The statement says "from Part I alone" but uses the Part II assignment (GR:454). **Class:**
  not applicable for the `H_V` operator statement, which is definitional. The dark-sector reading is
  conditional (GR:422).
- **Over-reading texts.**
  - GR:450 "This is a theorem of Part I": it is an immediate consequence of definitions.
  - GR:450 "(from Part I alone)": see GR:454.
  - "Invisible … by construction" holds in the sense "no `H_V` operator", not in the sense "no influence on
    visible statistics".
  - The book mirrors (`book/ch07-gravity.md:256`; FULL:2122; FULL:5261 = `book/ch19-open-problems.md:116`) say
    "invisible to the emergent quantum field theory" with "Conditional (… partly definitional …)". They do not
    repeat "theorem of Part I".

## 12. Marker HM: hidden priors and mixing

- **MQ-07: FULL:4860-4862**, mirrored at `book/ch18-beyond.md:56, 58`, with the chapter ledger at `:52`.
  - The text: "Even after the hidden sector has equilibrated … the *structure* of the corrections is
    predicted" and "The framework predicts that this independence is approximate".
  - These lines use, without label, (i) equilibration to a stationary distribution and (ii) the slow-bath form of
    C2.
  - The section's ledger (FULL:4856) precedes these lines and does not list the late-time item. It calls
    equilibration a "structural commitment" of a mechanism proposal. FULL:4844 says that convergence does not
    follow from the recurrent substratum.
  - Main's C2 theorem is conditional on the mixing hypothesis (Main:455), with ETH as motivation only (Main:445).
- **MQ-31: Main:674**, generated mirror `papers/Main.tex:4848`.
  - "the hidden-sector *state*, which is dynamically resampled (the bath thermalizes)" is stated as fact. It is
    the conditional mixing hypothesis of Main:445 and :455.
  - The same sentence's "yields the memory-bearing non-Markovian statistics that quantum mechanics represents",
    and Cplx:236's identification of QM with read-write statistics, are routed to the A5 / memory-equals-quantumness
    cluster (INV-MANUSCRIPT:50).
- **MQ-34, MQ-35 and MQ-40 (also HM per INV-MANUSCRIPT:87)** were checked and carry their labels:
  - MQ-34: C2 slow form conditional on mixing (Main:455; INV-MANUSCRIPT:53).
  - MQ-35: "hidden sector initially uncorrelated and maximally mixed" in the statement (Main:318).
  - MQ-40: "conditional on the effective-mixing hypothesis (EM)" (Main:744).
  No change.
- **Outcomes (hidden-sector component).**
  - MQ-07, the late-time correction: **2**. Equilibration and C2 mixing are used but unlabelled at
    FULL:4860-4862 and ch18-beyond:56, 58.
  - MQ-31, the resampling clause at Main:674: **2**.
  - Class: conditional for both.
- **Over-reading texts.**
  - FULL:4860 "is predicted", FULL:4862 "The framework predicts", and the ch18-beyond:56, 58 mirrors. The
    support is a conditional consequence of a mechanism proposal.
  - Main:674 / Main.tex:4848 "dynamically resampled (the bath thermalizes)". The support is the hypothesis at
    Main:455.

## 13. Marker PR: pre-stored and perfect records

- **In this cluster's records.**
  - Complete joint records (MI-D:369-371; QA-PR:36-38) are conservative for protection claims.
  - P1's archive isolation is an access restriction on the observer's own apparatus, and the native rule does
    not supply it (AP1:338-343).
  - Refills (MI-D:345, 361-362) are a free-reset capability used by the MI exposures as written (§1).
- **In the manuscript constructions (MQ-01, MQ-17).**
  - The S ⇒ D carrier is "a clock with the complete trajectory record, whose initial law may correlate the hidden
    and visible coordinates" (Main:554).
  - The gluing realization keeps a hidden density register, a predecessor stack and "`K` pre-loaded seeds uniform"
    (Main:566). Outcomes are fixed by the seed against `Tr I_o(ρ̃)` (Main:580).
  - Both statements list these constructions.
  - *Auditor's inference, not stated in the records:* for the realized law to match its target, the seeds must
    also be independent of everything visible, and the registers must never be read. The second holds by the
    Lemma 2 stipulation (Main:50).
- **Outcome (C3 component): 1** (the existence theorems state their constructions). **Class: conditional.**
  Main:584 ("operational realization theorem, not a uniqueness theorem") is scoped. Physical-reach readings
  (Main:22) belong to the equivalence cluster.

## Summary (≤ 25 lines)

1. Outcomes, by one rule applied to both directions:
   - M-INACC-1 exposure **1**; QA Lemma Q(iii) **2** (support hypothesis used but not stated).
   - QA G2 and R1 C-CP **1**; FB **1**.
   - AP1 Lemmas 2, 3 and 4 and D1 **1**; Lemma 5 and Level 3 **2** (ancilla independence; single Γ).
   - Observer-access and correlation-recombination **1**.
   - MQ-33 **2**; HM sites (FULL:4860-4862 and mirrors; Main:674) **2**; PR (C3 component) **1**.
   - M2D:853 "native instance" **3**, with follow-up M-ARC named only.
2. Protection is a joint property of the native symmetric, center-free linear step (necessary: MI-R:310-314;
   QA:518-521) and the supplied SA-1 interface. It does not follow from the dynamics alone.
3. P2, with its support condition, and the step give single-time isotropy. P1 makes it survive retention
   (AP1:335-336, 560-561). Each is load-bearing (QA:779-780; MI-R:373-374). P1 is not enforced natively
   (AP1:338-343).
4. Determination rests on the support of the hidden law (QA:499-501; MI-D:135-137). Non-bias and the per-state
   bounds rest on the product-uniform law. M-INACC-1's `E_A` and `E_B` exposures are pointwise
   (MI-R:250-252).
5. The exposing alternatives, `G_σ` under SA-1 and the earlier passive two-slice read (an idealization,
   AP1:331-333; CR:52-62), are also supplied interfaces. Neither direction transfers to a physically sourced
   observer.
6. Over-readings: the QA:46 heading (qualified at QA:48-50); QA:799's Status cell; QA:51-53 and :523-525
   "never/permanently" for information moved to archived cells (PROT-R′ holds for active-held information,
   MI-A3:60-84; WIP); M2D:853 and :947; GR:450; FULL:4860-4862, ch18-beyond:56, 58 and Main:674 (+Main.tex:4848).
7. M2D's M-INACC clauses (a) and (b) cannot both hold under the readings of MI-A1:59-70, which the record itself
   calls a definitional observation. Clause (c) is doubtful for P2 (AP1:347-349).

## Cross-cluster assumption-watch markers

- **AW-C3-1 (single-time isotropy versus retention).** Claims citing AP1 Lemma 3, QA Lemma Q, M1D Theorem W or
  M-INACC as protection inherit three things:
  - the native symmetric, center-free linear step;
  - P2 with its support condition, which gives single-time isotropy;
  - P1, which is supplied and not enforced natively, for retention across time.
- **AW-C3-2 (support versus measure).**
  - Determination needs full joint support of the unknowns.
  - Non-bias and the per-state bounds need the product-uniform law.
  - Pointwise exposures need neither.
  - Check which half a use relies on.
    - MECH-1 Theorem W (odd `q`) relies on a third condition: quantum R-W positivity of every ancilla law
      (M1D:473-474). Whether correlated or non-uniform laws, full-support ones included, keep it is a
      MECH-1-cluster check.
    - MECH-2 Theorem NC / H-LIFT and the L3B statistical ceilings belong to the bias/statistics half.
- **AW-C3-3 (retrodiction).** "Never" and "permanently" hold for information still held by active cells (PROT-R′
  in the linear limits). They fail for information moved to archived cells (MI-A3; WIP).
- **AW-C3-4 (reading of M-INACC).** Any use of M-INACC as a premise states its reading of clauses (a) and (b), or
  uses USE-ctx (MI-A1:59-103).
- **AW-C3-5 (common lift and independent ancillas).** AP1 Lemma 5 (:735), AP1 Level 3's single Γ (:962-963), FB
  H-C (:47-61) and MECH-2 H-LIFT all assume one preparation-independent hidden law (AW-EOI-1).
- **AW-C3-6 (definitional inaccessibility).** Main Lemma 2's partition (Main:50) is a definition. Physical
  "invisible" or "inaccessible" readings need OA:132-137's later-access check (GR:450).
- **AW-C3-7 (unlabelled hidden mixing).** "Thermalizes" and "resampled" are stated as fact at Main:674 /
  Main.tex:4848 and at FULL:4860-4862 / ch18-beyond:56, 58. They are conditional at Main:445 and 455 and at
  FULL:4844 and 4856.

## Disposition of REVIEW-C3 findings

| ID | Disposition | Where |
| --- | --- | --- |
| B1 | Accepted. The central answer now describes a joint property of the native step and the supplied interface, citing MI-R:64-66, 310-314 and QA:518-521 | Central answer; §10; Summary 2 |
| B2 | Accepted. "Sole source" is removed. One formulation is used throughout: P2 + step → single-time isotropy; P1 → retention; each load-bearing | Central answer; §§3, 6, 7, 10; AW-C3-1 |
| B3 | Accepted. §0.3 now confirms that support is load-bearing and that full-support correlation gives bias only. AW-C3-2 and §9 are restated. NEW is re-graded to CONFIRMING plus ELABORATING. The Theorem W pointer is restricted. The L3B H₀/H₁/H₂ attribution is corrected. "Not evidence" is enforced: no item rests on §0 alone | §§0.3, 9; AW-C3-2 |
| B4 | Accepted. The passive two-slice read is attributed to the programme's earlier interface, an idealization (AP1:331-333; CR:52-62), not to Main | Central answer; §§3, 8; Summary 5 |
| B5 | Accepted. One outcome rule is stated and applied to both directions. AP1 Lemmas 3 and 4 go to 1. Lemma Q stays at 2 for the stated reason. Lemma 5 and Level 3 stay at 2 under the same rule. PR goes to 1 | Head of file; §§3, 6, 13 |
| B6 | Accepted. The follow-up is M-ARC, named only. Archive variants, refill rule and registration count are defined. CC-ISO, C-NV, support-restricting C-SUPP, C9 and the horizon and `|H|` checks are added. "Why decisive" is scaled back | §2 |
| N1 | Accepted. WIP / UNVERIFIED labels; "trivial" (MI-R:446-448); PROT-R′ (MI-A3:60-84) | Header; §3; AW-C3-3 |
| N2 | Accepted. The §4.1 table is identified and the "given P1 and P2" qualifier quoted | §3 |
| N3 | Accepted. QA:48-50 qualifier noted | §3 |
| N4 | Accepted. Main, GR, Cplx and FULL defined | Header |
| N5 | Accepted. ch18-beyond:52, 56, 58 and Main.tex:4848 added | §12; AW-C3-7 |
| N6 | Accepted. The A2 flag is re-filed as a separate A3/A4 note; Main:650 replaces Main:270 | §11 |
| N7 | Accepted. "Gate-write refills" used throughout; the MI-R:84-85 flag is marked as resting on a hand-check | §§0.2, 1, 10 |
| N8 | Accepted. QA:46 and :799 are listed as over-readings of Lemma Q in the summary, separate from the outcome-3 item | Summary 1, 6 |
| N9 | Accepted. MQ-34, 35 and 40 checked and labelled; no change | §12 |
| N10 | Accepted. Seed independence is marked as the auditor's inference | §13 |
| N11 | Accepted. Main:674's identification clause is routed with Cplx:236 to the A5 cluster | §12 |
| N12 | Accepted. Both readings and the record's own label "definitional observation, not a result" are carried | §2; Summary 7 |

## Disposition of REVIEW-C3-r2 findings (r3)

| ID | Disposition | Where |
| --- | --- | --- |
| B1 | Accepted. M-ARC gains parameters (`w = 3`, `T = 4`, `|H| ∈ {4, 6}`), an exact `F_2` span method and a decision rule (exposure / survival / size-dependent / void; both labels need green controls). The horizon is reworded as no wrap-around through `H`, and AP1:338-341 is cited only for budget-relative isolation. Still named only | §2 |
| B2 | Accepted. The Theorem W pointer is restated as an odd-`q` R-W positivity hypothesis (M1D:473-474) and a MECH-1-cluster check; the `q = 2` sharp-cell argument is not transferred | §9; AW-C3-2 |
| N1 | Accepted. "Pointwise" is limited to `E_A` and `E_B`; `E_A′` is a 1/16 branch (MI-R:283-285) | Central answer |
| N2 | Accepted. Outcome 2 is grounded on QA:142-144 and QA:777, with the counter-reading stated | §3 |
| N3 | Accepted. MI-R:374 and QA:780 are cited as the record-level instance under SA-1 | §0.3; §3 |
| N4 | Accepted. The review note is marked as provenance only | §0.3; §9 |
