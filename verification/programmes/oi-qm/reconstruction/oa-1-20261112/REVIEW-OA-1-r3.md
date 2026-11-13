# Final re-check of OA-1 r3 (`OA-1-REPORT-r3.md`)

**Reviewer standing.** The same independent reviewer as `REVIEW-OA-1.md` and `REVIEW-OA-1-r2.md`. Read-only and
paper-only, with sources at `fb733b4a`. No computation on any OI rule and no commits, pushes or GitHub writes.
- r1 (17:00:43) and r2 (17:17:45) are unchanged.
- r3 has mtime 17:27:51 and is 649 lines long.

## Verdict: ACCEPT WITH NITS

R1–R7 and R5′ are applied correctly. The writer's narrowing of N1-S holds and is the right direction, though it is
incomplete in one term (nit 1). D8 and its run of the owner's test are sound. The owner's four additions are applied,
with one unqualified sentence under addition (a) (nit 2). No nit changes a verdict.

***

## 1. R1–R7 and R5′

| Item | Applied? | Evidence |
|---|---|---|
| R1 knowing / selecting split | yes | N1-K and N1-S defined (:123–124). "Held = function of present `V`" is stated as part of the no-go (:104–106, :141–142, :309–311). Selection is in the affine class and the μ-G failure is a retention failure resolved by MP-0a/MP-0b (:323–335). Propagated to §0.3, §4.1, §5 and §6. |
| R2 measure typing | yes | μ-O derived; μ-G and μ-R both posited via ledger (iv), quoting Main:54 (:92–101). "Native" is made relative to (iv) (:110–111). |
| R3 nits | yes | MP-0a "μ-G is not that law; ready cells cost D3" (:525). R3 in the configuration identification inherits R4's ceiling (:396–397, :497). |
| R4 N2 measure-free | yes | D5 "(i) and (ii) hold for every state"; (xiv) only for the operational reading, with the residual effect classed as correlation (:176–180, :351–354). "Earliest failure that holds under every measure" (:365, :495). |
| R5 D4 scope | yes | (a) any stationary law: deterministic on the support. (b) μ-G only, Main:147, with `T` the uniform-prior kernel (Main:88, :129) (:157–162). Edited at N4 (:383–384) and §10. |
| R5′ D8 | yes | §2 D8 (:202–228); AW-OA1-1 scoped to `X = V` (:577–579). |
| R6 routes | yes | native `Z`/`X` "undecided", not an escape route (:428–429); Shape 2 ↔ 5b/5c, Shape 3 ↔ 5e (:430–434). |
| R7 possible ingredients | yes | necessity only within NC, Main:558 [half imported] and TUNE-1 FAIL-CLASS [W]; sufficiency open; "growing carriers" (:422–426, :418, :541). |

***

## 2. The writer's narrowing of N1-S (:326–329)

- **The claim holds.** Under R-lin, `(y_i, x_i) ↦ (x_i, Σ_{j∈N(i)} x_j − y_i)` (ledger (xiii), Main:724). A value
  written from a neighbouring setting cell reaches the carrier's new slot added to the other neighbours' current
  values. It does not arrive as an exchange. So the generic affine-class statement, "a cell exchange writes `s`
  exactly", does not hold for R-lin's fixed coupling. Narrowing it is the correct skeptical move on a favourable
  branch (§A.31).
- **Nit 1 (incomplete).** The written value is masked by one more term: the carrier's **own previous slot**, `−y_i`.
  - Isolation does not remove that term. An isolated, armed cell gives `s − y_i`.
  - So R-lin selects only if the carrier's previous slot is known **and** the other neighbours are known or isolated.
  - The first condition is a blank (MP-0a) in every case. Isolation (E-iso) can replace only the second.
  - The conclusion "the obstacle is still blanks or isolation, not affinity" stands if it reads "blanks, with
    isolation as an alternative only for the neighbours". The translation bullet's "only if `Σ` starts known" (:325)
    already contains the point for the generic case. State it for R-lin at :326–329 and in the §6 row at :559.

***

## 3. D8 and the owner's test

- **(a) Sound.** Under μ-G, `H_t ⊥ (Y_t, R_t)` (D2). An inert readout update, `Y_{t+1} = f(Y_t, H_t)`, gives
  `P(Y_{t+1} | Y_t, R_t) = P(Y_{t+1} | Y_t)`. The data-processing step is valid because `Y_{t−k..t−1}` is a function
  of `R_t`.
- **(b) Sound.** With non-inert records, `P(Y_{t+1} | Y_t, R_t)` is the uniform-`h` pushforward of
  `f(Y_t, R_t, ·)`. Dependence on held history enters only through `f` reading the visible cells `R`. Hidden memory
  correlation contributes none, because `H_t` is independent of everything held.
- **(c) Example re-checked.**
  - `(y, r, h) ↦ (h, y, r)` cycles with period 3.
  - `r_t = y_{t−1}` and `y_{t+1} = y_{t−2}`.
  - Three consecutive `y` values are a permutation of the three initial bits, so they are independent: memory 0 at
    order 1 and 1 bit at order 2.
  - The four-cell version gives `y_{t+1} = y_{t−3}`.
- **(d) The owner's test is run on what the observer holds.** Under μ-G with inert records, the answer is no at the
  held orders. Hidden readback appears only for history beyond the window (Main:97). This meets the owner's
  requirement: it is a physical statement about held histories, not a relabelling of the state space, and it does
  not say hidden memory is absent (:226–228).
- **(e) The scope is correct:** μ-G only, dissolving under MP-0a, μ-O and μ-R. The status (candidate, unreviewed
  [W], ELABORATING of Main:97) is correctly stated at :561 and :608.

***

## 4. The owner's four additions

- **(a) A5 as a classical-control repair. Applied, one sentence over-strong.**
  - The gap-2 row (:488) is accurate: "Dropping A5 alone, keeping the affine form, does not restore control (D5).
    Lifting both is a Layer-0 revision." It also says the repair "does not by itself bear on gap 3".
  - The gap-3 row (:489) gives the scoped reason: non-affine rules at the configuration level stay inside the
    ceiling (D6, 5b).
  - §0.6 (:71–73) and §10 (:615–616) are suitably neutral.
  - **Nit 2.** MP-1 says "It is not a route to gap 3" (:539), with no qualifier. That is a negative claim wider than
    what is ruled out:
    - at the configuration level, D6 excludes it;
    - under NC's hypotheses, "no dynamics escapes" (MECH-2 §6.2);
    - in a changed identification (5c/5d) the rule's form remains a possible ingredient. MECH-2's nonlinear
      conditioning gives P★, and M-INACC is a functional "that the fixed rule uses", tested on the nonlinear `G_σ`.

    Write "not by itself a route to gap 3", matching :488. Optional: note that dropping the affine form means
    modifying the amplitude-scale gauge-invariance step from which ledger (vii) derives it.
- **(b) §2A. Applied.**
  - Typing is correct, and the caveat "success under one measure does not establish that OI physically selects that
    measure" is explicit (:241–244).
  - I checked every row against D1–D8: D4(a) holds for μ-O and μ-R because both are invariant, hence stationary;
    D2, D4(b) and D8 hold under μ-G only; N2 is measure-free as a map property; under μ-G, (xiv) holds for disjoint
    cells.
  - **Nit 3.** The N3 row (:263) marks backaction "native" under all three measures. In the body (:370) backaction is
    native **given half-known meters**, which are a posit (apparatus-1 SA-1(c), :298–303) and under μ-G cost D3. Put
    the qualifier in the table.
- **(c) The Fredkin scope. Applied** (§0.6, §4.1 :453 and :459–465, §5 :511–515, §6, §10). The failure is established
  for the configuration-level interface and is open under encoded or record-level representations. Pass cases there
  are limited to "known cases" with supplied access restrictions.
  - **Nit 4.** At :461 the citation `OB/FrozenSourcing.lean:74` (`nonnegBounded_of_bijectionLevel`) should be :79 or
    :84 (`permTheory_nonnegBounded` / `obsTheory_nonnegBounded`), with :99 and :327.
- **(d) The next question. Applied as non-authorized and outside OA-1** (§10A, :623–631).
  - **Nit 5 (provenance).** The quotation could not be verified. The phrase is in none of the #1169 comments since
    16:30Z on 2026-11-12 (API fetch). Mark it "owner's words as relayed by the coordinator, 2026-11-12; not yet
    recorded on #1169".
  - In the Standing block (:11–12), cite c.6829898892 for the scope addition.

***

## 5. Other nits

- **Nit 6.** §4.2 (:477–479) incorporates r2's claimed-supply table by reference. Either say "r2 §4.2 is incorporated
  unchanged", or restate it, so that r3 reads on its own.

***

## 6. Bottom line

r3 answers the owner's ladder question within the stated scope.
- **Gap 1 (preparation)** separates knowing from selecting. Under the posited global selection μ-G with "held =
  present `V`", a selected hidden carrier cannot be held together with its choice record, for every bijection. That
  is a blank-memory failure, classical and resolved by MP-0a or MP-0b. Under the derived μ-O, knowing can be native,
  and selecting is open.
- **Gap 2 (classical control)** is a measure-free restriction of the gauge-derived affine class, R-lin included. Its
  repair is classical and is a Layer-0 revision.
- **Gap 3 (quantum operations)** is capped for the configuration identification for every rule [K]. Encoded frames
  are capped by frame-relative paper results, emergent amplitudes are imported, and 5d with M-INACC on growing
  carriers is open, with possible ingredients only.

The owner's key test, that gaps 1–2 can be resolved classically while gap 3 remains, is supported at paper level. The
Fredkin control fails the qubit tier only under the configuration-level interface. Nits 1–6 are wording and citation
fixes and can be applied without a further review round.
