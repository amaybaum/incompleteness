# OA-1 (r4): can one fixed deterministic substratum supply preparation, control, measurement and complete records?

**Standing (r4).** Revision r4 applies nits 1–6 of the final re-check `REVIEW-OA-1-r3.md`
(verdict ACCEPT WITH NITS). No verdict changes; the changes are listed in §12. r1–r3 are
unchanged. The scope addition is recorded in #1169 comment 6829898892.

**Standing (r3, retained).** WIP / UNVERIFIED author report for unit OA-1 under #1169, revision r3. It applies
R1–R7 and R5′ of the focused re-check `REVIEW-OA-1-r2.md` (verdict REVISE), which was prompted by
the owner's two points (knowing versus preparing; complete history versus hidden memory). It also
folds in the owner's four additions relayed by the coordinator (A5 as a classical-only modification
candidate; the measure-dependency section; the scope of the Fredkin result; the recommended next
question). OA-1 stays paper-only and unadopted until the r3 re-check. r1
(`OA-1-REPORT.md`) and r2 (`OA-1-REPORT-r2.md`) are unchanged.

- **Authorization.** Owner amaybaum, 2026-11-12: #1169 comment 6829742537 and the approved scope
  addition. Paper-only.
- **What this file does not do.** It adopts no premise, promotes no claim, and edits no manuscript
  or Lean file. It runs no computation on any OI rule.
- **What comes next.** The unit ends with an owner decision checkpoint. TUNE-1 Step 3 stays paused.

**Snapshots and citation forms.**

- `main` is `fb733b4a58558ef64bd7c3585712c76e9f2dfb42`, read with `git show`.
- `Main:n` means `papers/Main.md`. `OB/File:n` means `verification/lean-mathlib/OIBridge/`. Other
  record paths are relative to `verification/programmes/oi-qm/reconstruction/`.
- TUNE-1 is cited from `research/tune-1-20261111` at `d47a6377` (`T1/<file>:n`) as research only
  (§A.46 item 7).

**Support labels.**

| Label | Meaning |
|---|---|
| [K] | Lean statement on `main`. Statement read; nothing built. |
| [P] | Manuscript statement. |
| [R] | Research record that is not independently established. |
| [W] | My own derivation. Reviewed only by a same-family model; not kernel-checked. |
| [O] | Open. |

**Disclosure.**

- **Commands.** As in r1/r2: `git` read commands, `grep`, `sed`, `wc`, `ls`, `mkdir`, `cat -n`;
  one `curl` and one `python3 -I` metadata parse of comment 6829596317; GitHub MCP reads.
- **New r3 source checks.** For r3 I re-read Main:54 ("a selection principle, not uniqueness from
  invariance alone"), Main:88, Main:129 ("under the uniform hidden prior that defines `T`") and
  MECH-2 :104–108 ("At the native read level (`Z` and `X` only) A6 is undecided"). All hold at
  `fb733b4a`.
- **Reviewer derivations.** The reviewer's [W-rev] derivations were re-derived by hand before use
  (§2, D8, N1-S). One was refined (N1-S under R-lin).
- **Nothing published.** Nothing was committed, pushed or posted.

***

## 0. Plain-language summary

1. S⇔D⇔Q_fb never fails, because it chooses the world after the target.
2. With the corpus's affine lattice rule fixed first, I followed four operations: prepare,
   control, measure, record.
3. **Preparation splits in two:**
   - *knowing* the hidden carrier;
   - *selecting* which state it is in.

   Writing a chosen value into a hidden cell is something an affine rule can do. Under the global
   maximum-entropy selection, the observer cannot keep a record of its choice next to the carrier
   it chose. This is the blank-memory cost that classical computers also pay. A ready-cell supply
   (MP-0a) or the history-record convention (MP-0b) resolves it classically. Under Main's per-orbit
   measure, knowing can be native, and selecting is open.
4. **Control:** under any affine rule, a stored setting can only shift values. It cannot choose
   which operation runs or which quantity is read. This is a property of the map, and it is the
   earliest failure that holds under every measure. A classical computer has this ability.
5. **Quantum operations:** the kernel caps the configuration-level observer interface, and no rule
   change lifts the cap. It holds for every rule, including the native branch read in the same
   identification.
6. **The owner's key test is supported at paper level.** Gaps 1 and 2 can be resolved by purely
   classical means. Gap 3 remains open. It is not shown impossible.
   - Gap 2 points at A5 linearity, together with the affine form it strengthens. That is a candidate
     for modification **only** to recover classical control. Dropping it does not by itself explain
     quantum behaviour.
   - The classical computer used as a control fails the quantum tier only under the
     configuration-level interface. That has not been shown for every observer-relative
     representation of it.
   - The results depend on which measure is used; §2A lists the dependence for each.
7. **One candidate result (unreviewed).** Under the global selection, an observer whose records
   are inert never sees two held histories with the same present predict different futures.
   Hidden readback shows only beyond what it holds.

***

## 1. Definitions in OI's own terms

**One physical setup.** `𝔖 = (S, φ, (V, H), μ, A)`:

- `S` is finite (Main:60; ledger item (ii), Main:724).
- `φ` is a bijection, fixed **before** any target is named.
- `V ⊊ S` is the registered configuration and `H` the hidden sector (Main:42, :48).
- `A` is the apparatus layout, fixed once for all settings.
- **Measures, typed (R2).**
  - **μ-O**, uniform on the orbit of the actual microstate. **Derived:** it is the unique
    invariant measure there (Main:54, :60).
  - **μ-G**, the global counting measure, uniform on `C_V × C_H` (Main:58). **Posited:** a
    selection principle, "not uniqueness from invariance alone" (Main:54). It is the case of
    ledger item (iv) in which the records exclude no orbit.
  - **μ-R**, maximal entropy "compatible with the observer's records". **Posited:** ledger item
    (iv), Main:724.
  - μ-G and μ-R rest on the same posit, (iv). A structured prior declared as a realization datum
    (Main:58, :97, :602) is a further named premise.

There is no write access outside `φ`. A setting is a configuration of designated cells. It is
either an initial condition or written by `φ` from the observer's own records. **Held** means a
function of the present configuration `V_t`. That convention carries D2's no-go (R1); MP-0b
replaces it.

**Native, premise, not supplied.**

- *Native:* supplied by `(φ, partition, μ, A)` with a stated `μ`. Under μ-G and μ-R, "native" is
  therefore relative to posit (iv).
- *Supplied under a named premise:* one extra statement, carrying no target data.
- *Not supplied:* otherwise.

**Non-import test (§A.29).** A construction imports its target if its supplied elements could be
re-tuned, with `φ` and the partition unchanged, to realize a non-quantum target just as easily.

**Operations.** Each operation has an infrastructure tier (target-neutral) and a qubit tier
(§4.2).

| | Operation | Infrastructure tier |
|---|---|---|
| N1-K | Knowing a carrier | A held record event `E` (with `P(E) > 0`, failures recorded) such that the carrier's law conditional on `E` at use time differs from its unconditional law. `E` is still held at use time. |
| N1-S | Selectable preparation | A setting `s`, whose law is independent of the carrier (ledger (xiv)), is chosen and recorded. For at least two values of `s`, the carrier's law at use time, conditional on everything held then (`s` included), differs. Heralds are allowed and failures are recorded. |
| N2 | Controllable interaction | The non-translational part of `φ^τ` acting on `Σ` depends on the content of setting cells `s`, for at least two operationally distinct values. `s` is independent of `Σ` (xiv). |
| N3 | Measurement | A meter whose later record is correlated with a functional of `Σ`. *Selectable* if a setting (N2) fixes the functional. The residual `Σ` is handed on. |
| N4 | Complete records | Every outcome, herald and failure, plus knowledge of the residual carrier, is held in `V` at the end. |

***

## 2. Facts derived here ([W] unless cited)

**D1 (stationarity: any bijection, any invariant μ).** The unconditional law is the same at every
time. Every time-specific preparation, and every new same-time correlation between record and
carrier, is conditional on a record event. ∎

**D2 (equal-time blindness, under μ-G only).**

- *Statement.* The law at every `t` is uniform on `C_V × C_H` (Main:58, invariance Main:54). So
  `H_t` is uniform and independent of every function of `V_t`.
- *What the no-go needs.* It needs **both** μ-G and "held = a function of present `V`" (R1).
  Uniformity alone does not give it.
- *Novelty.* Q-b1 (`observer-interface-obsmu-20261104/ANALYSIS.md:907–912`) already states this.
  D2 adds one consequence (ELABORATING): under μ-G it closes obsmu's in-`V` retention route
  (:913–917).
- *Scope.* Not established under μ-O or μ-R. Those laws are invariant but not products. ∎

**D3 (herald bound).**

- `P(Σ_t = σ | E) ≤ μ(Σ_t = σ) / P(E)`, which under μ-G is at most `1/(|Σ| P(E))`.
- Point-preparing `M` distinct `q`-ary cells costs `P(E) ≤ q^{−M}`, with equality for a visible
  herald on visible cells. Ready cells under μ-G cost exactly this. ∎

**D4 (complete in-`V` records; ELABORATING; scoped in r3, R5).** Premise: the physical visible
configuration determines its predecessor, `V_{t−1} = g(V_t)`.

- **(a) Any stationary law ν.** `g` maps ν to itself, so `g` is a bijection on the support. The
  visible process is deterministic on the support, and (C1) and (C4) fail *for that law*. `φ`
  itself need not be visibly autonomous.
- **(b) Under μ-G only.** The one-step matrix is then the uniform-prior kernel `T` (Main:88, :129).
  It is a permutation. By Main:147, `φ(x, h) = (φ_V(x), σ_x(h))`, so the hidden sector has no
  influence on `V` at any step (Main:72).
- **(c) Reading.** In an equilibrium state, complete in-`V` records and hidden influence on `V`
  exclude each other. This is a physical constraint, the blank-memory cost of D3 (MP-0a). It is
  not a claim that hidden memory disappears.
- **(d) Scope.** Full-history records only. D4 dissolves under MP-0a. Partial records are D8. ∎

**D5 (Lemma A: any affine rule; a property of the map).** Let `Φ` be affine, with state
`(c, x, u)` = (setting, carrier, rest). Then
`Φ^τ(c, x, u) = L_c c + L_x x + L_u u + k`, and `L_•` and `k` do not depend on `c`.

- **(i)** The non-translational part of the carrier's map does not depend on `c`.
- **(ii)** Every record is `H_O r_O + H_P c + H_U u + const`, and the functionals read do not
  depend on `c`.
- An affine exchange that writes `c` changes neither.
- **Measure (R4).** (i) and (ii) hold for every state, so no measure and no independence
  assumption enters. Ledger (xiv) matters only for the *operational* reading. Under μ-O and μ-R,
  cells on the actual orbit can be correlated, so (xiv) may fail for the actual setting cells. Any
  remaining effect of `c` on the record law then comes through the `c`–`u` correlation. That is
  preparation correlation (D7), not control.
- **Scope.** Ledger (vii) derives the affine form from amplitude-scale gauge invariance
  (Main:724), so D5 covers the gauge-derived affine class.
- **Status.** One paper proof, re-derived twice at the same layer: MECH-1 Lemma A
  (`mechanism-1-20261107/DESIGN.md:404–430`) [R]; TUNE-1 Lemma A-T
  (`T1/TUNE-1-STEP2-SESSION3.md:32–98`) [W], ChatGPT-reviewed per `T1/TUNE-1-STEP2-SESSION4.md:13–16`;
  and this file. ∎

**D6 (point 3; [W] on [K]).** A theory generated from φ's configuration bijections by the closure
rules of `FiniteOperationalTheory` (`OB/OperationalAssembly.lean:594`ff.) is, in availability, a
sub-theory of `permTheory 𝒮.Conf`. That theory contains every permutation conjugation (:406) and is
closed under the same rules. `NonnegBounded` (`OB/FrozenSourcing.lean:65`) is monotone under
inclusion, so the ceiling follows from `obsTheory_nonnegBounded` (:84). ∎

**D7 (post-hoc and timing selection do not supply N2).**

- If the setting does not change `φ`'s action, every "selectable" read is a coarse-graining of one
  joint record.
- Selecting by timing turns the setting into a different preparation procedure. "The setting is
  the parity of the armed tick, which is available only through P3 and E-iso"
  (`apparatus-1-20261107/DESIGN.md:510–511`). ∎

**D8 (partial-window records and the owner's test; candidate, unreviewed; ELABORATING of Main:97;
R5′).** Write `V = (Y, R)`: readout `Y`, record cells `R`, where `R_t` determines
`Y_{t−k..t−1}`. Let `μ` be μ-G.

- **(a) Inert records.** If `Y_{t+1} = f(Y_t, H_t)`, then `P(Y_{t+1} | Y_t, R_t) = P(Y_{t+1} | Y_t)`,
  because `H_t ⊥ (Y_t, R_t)` (D2). By data processing,
  `I(Y_{t−k..t−1}; Y_{t+1} | Y_t) ≤ I(R_t; Y_{t+1} | Y_t) = 0`.
- **(b) Non-inert records.** If `Y_{t+1} = f(Y_t, R_t, H_t)`, then `P(Y_{t+1} | Y_t, R_t)` is the
  uniform-`h` pushforward of `f(Y_t, R_t, ·)`. Any history dependence the observer sees is
  therefore mediated by the visible cells `R`, not by `H`.
- **(c) Hand check of the reviewer's example.**
  - Take `(y, r, h) ↦ (h, y, r)`, a cyclic permutation of coordinates and hence a bijection.
  - From `(y₀, r₀, h₀)` the sequence is `(h₀, y₀, r₀)`, then `(r₀, h₀, y₀)`, then `(y₀, r₀, h₀)`.
    So `r_t = y_{t−1}` (faithful window-1 records), `y_{t+1} = h_t = y_{t−2}`, and the update of
    `y` is inert in `r`.
  - The three initial bits are independent, so `y_{t+1}` is independent of `(y_t, y_{t−1})`.
    Memory is zero at order 1 and one bit at order 2.
  - Adding a second record cell, `(y, r₁, r₂, h) ↦ (h, y, r₁, r₂)`, moves the memory to order 3.
- **(d) The owner's test.** Do two histories with the same present predict different futures?
  - Run it on histories the observer **holds**: under μ-G with inert records the answer is **no**
    at every order the window covers.
  - With non-inert records the answer can be yes, but the dependence runs through visible cells.
  - A yes from hidden readback appears only for histories that differ beyond the window, i.e.
    history the observer does not hold (Main:97).
- **(e) Scope.** μ-G only. It dissolves under MP-0a (the law is not stationary) and under μ-O or
  μ-R (D2 fails). It does not say hidden memory is absent; it says where an embedded observer can
  and cannot see it. ∎

***

## 2A. Measure dependency (owner addition 2)

The three measures are not interchangeable.

- **Typing:**
  - μ-O (per-orbit) is **derived**: the unique invariant measure on the actual orbit (Main:54, :60).
  - μ-G (global counting) is a **posited selection principle** (Main:54) and rests on ledger item
    (iv).
  - μ-R (record-compatible, conditioned) is likewise **posited** and rests on (iv) (Main:724).
- **A result that succeeds under one measure does not establish that OI physically selects that
  measure.** For example, N1-K being native under μ-O shows what holds *if* the actual
  microstate's orbit is the relevant law. It does not show that the observer's description uses
  μ-O rather than μ-G or μ-R. Main's own selection, (iv), is a posit.

| Result | μ-G (posited, (iv)) | μ-R (posited, (iv)) | μ-O (derived) |
|---|---|---|---|
| R0–R2 (representation and realizations) | hold (stated for any law / supplied priors) | hold | hold |
| D1 stationarity | holds | holds (invariant) | holds |
| D2 equal-time blindness | **holds** | not established | not established (fails on the swap's 2-cycle) |
| D3 herald bound, general form | holds | holds | holds |
| D3, `q^{−M}` form | holds | not established | not established |
| D4(a): full-history in-`V` records ⇒ deterministic on the support | holds | holds | holds |
| D4(b): ⇒ no hidden influence (Main:147) | **holds** | not established | not established |
| D5 / N2 as a property of the map | holds | holds | holds (measure-free) |
| N2, operational reading via (xiv) | (xiv) holds for disjoint cells | (xiv) may fail on the record-compatible support | (xiv) may fail on the orbit |
| D6, R4 kernel ceiling | measure-free | measure-free | measure-free |
| D7 | holds | holds | holds |
| D8 (inert partial records show no held-order memory) | **holds** | not established | not established |
| N1-K, hidden carrier | **fails** | can be native once records exclude the fixed points (swap) | can be native (swap) |
| N1-S, hidden carrier | **fails** (retention) | open | open |
| Coset-uniform record laws under R-lin (Lemma A-T (c); obsmu Proposition C) | hold (uniform law) | not established | not established |
| N3 fixed read | native | native | native |
| N3 backaction | only given half-known meters, a posit (apparatus-1 SA-1(c), :298–303) that costs D3 under μ-G | only given half-known meters (posit) | only given half-known meters (posit) |
| N4 | not native; under μ-G also D2, D4(b), D8 | not native | not native |
| R5 rows | measure-free for the kernel rows; paper rows as cited | — | — |

***

## 3. The debugging ladder

- **Target held fixed:** one physical `𝔖` across settings, with source-derived preparation,
  control, readout, failures and residual state.
- **Shape:** below R2 the ladder forks into two parallel branches. R3 is the native fixed-rule
  branch; R4 is the kernel interface branch.

### R0. `finite_horizon_equivalence`

- **Holds [K].** `OB/Equivalence.lean:462–469`: :422, :294, :245. See also Main:546–552.
- `S_imp_D` builds its carrier and initial law from the target.
- **Target.** Not addressed. This rung cannot fail.

### R1. + C1–C4

- **Holds [P/K].** Main:68–80 and :602–612; the kernel identities are cited at Main:97.
- **Target.** Unchanged.
- **Records against readback.**
  - D4(b): under μ-G, complete in-`V` records exclude hidden influence.
  - D8: under μ-G, an observer with inert partial records sees no memory at the orders it holds.
  - AW-OA1-1, CONFIRMING, scoped to Main's convention `X = V`.

### R2. + one common realization for a fixed finite experiment

- **Holds [P; checked by probes].**
  - Main:480–482: `u_c ~ P(·|c)`.
  - Main:564–578.
  - Main:580: "Quantum mechanics enters as the instrument data and as the state held in the
    hidden register".
  - Main:596.
- **Target.** Met only with supplied data. The non-import test fails by Main:582: "the same
  reversible machinery can realize non-quantum finite instrument families".

### R3 (branch A). Sourcing from the actual rule

The fixed rule is R-lin (ledger items (vii) and (xiii), Main:724). Where a result holds for the
whole gauge-derived affine class, that is stated.

**Node N1-K: knowing a hidden carrier (R1).**

- **Under μ-G (posited, via (iv)).** No held record is correlated with the present hidden state
  (D2). The no-go needs μ-G **and** "held = function of present `V`". It holds for every
  bijection.
- **Under μ-O (derived).** Knowing can be native. In the swap `(v, h) ↦ (h, v)` the orbits are
  `{00}`, `{11}` and `{01, 10}`. On the 2-cycle, `h_t = 1 − v_t`, so the present configuration
  determines the hidden bit with no memory at all (re-derived by hand).
- **Under μ-R.** The same holds once the records exclude the fixed points.
- **Owner's swap example, under μ-G.** The remembered `V_t` *is* `H_{t+1}`. A copy into another
  visible cell needs a blank; a CNOT into a uniform cell gives a one-time pad. The memory therefore
  sits in `H`, or outside the configuration (MP-0b). This is consistent with D2.
- **Visible carriers.** Native, by a visible herald, at the D3 cost.

**Node N1-S: selectable preparation (R1).**

- **Selecting dynamically.** Writing a chosen setting into a carrier is in the affine class. A
  cell exchange `(s, Σ) ↦ (Σ, s)` is linear and writes `s` into `Σ` exactly. A translation
  `Σ ↦ Σ + s` also selects, but only if `Σ` starts known.
- **Refinement for R-lin itself (r4, nit 1).** R-lin's update is
  `(y_i, x_i) ↦ (x_i, Σ_{j∈N(i)} x_j − y_i)` (ledger (xiii), Main:724), checked by hand. A value
  written from `s` reaches `Σ`'s new slot with two kinds of terms added:
  - the other neighbours' current values;
  - the carrier's **own previous slot**, `−y_i`. Isolation does not remove it: an isolated, armed
    cell gives `s − y_i`.

  R-lin therefore selects only if the carrier's previous slot is known **and** the other
  neighbours are known or isolated. The first condition always needs a blank cell (MP-0a).
  Isolation (E-iso, a posit) can replace only the second. The obstacle is blanks, with isolation
  as an alternative only for the neighbours. It is not affinity.
- **Keeping the choice, under μ-G (posited).** If `s` (or any record of it) is held in `V_{t′}` at
  use time, then by D2 `Σ_{t′}` is independent of everything held. The held conditional law of the
  carrier does not depend on the choice, for every bijection.
- **Verdict under μ-G.** Not supplied for hidden carriers. This is a **retention** failure, the
  blank-memory cost (D3, D4(c)). It is not a missing selection mechanism. MP-0a resolves it
  classically (blank copy cells), and so does MP-0b.
- **Under μ-O and μ-R.** Open [O]. N1-S also needs (xiv) to hold on the actual orbit or orbit
  union, where cells are correlated.
- **Visible carriers.** Native: a setting written into a visible cell is held.
- **Under premises.** **MP-0a** (H-LOW, a resource): fixed known values on designated cells,
  independent of settings and carrier, uniform elsewhere, declared as the joint initial law
  (Main:58, :97, :602). It passes the non-import test; general structured priors do not
  (Main:482, :522, :580). **MP-0b** (H-MEM, an interface convention): the visible history counts
  as held, outside `V`. R4 grants it (`OB/OperationalAssembly.lean:594–643`). H-PREP stays open
  (obsmu :892–900).
- **Qubit tier under R-lin.** Coset-uniform laws only (`T1/TUNE-1-STEP2-SESSION3.md:48–79`; obsmu
  :546–575): stabilizer-type states. At odd `q` there is nothing beyond them (MECH-1 Proposition
  C). At `q = 2` with heralds it is open (L5.4).

**Node N2: controllable interaction (R4).**

- **Property of the map.** By D5, under any affine rule, a setting held in the world acts only
  by translation, for every state. This is **measure-free**.
- **Operational reading.** It uses ledger (xiv). Under μ-O and μ-R that is a posit that may fail on
  the actual orbit. A residual setting effect there is correlation (D7), not control.
- **Verdict.** Not supplied natively for the gauge-derived affine class, R-lin included.
- **Scope.**
  - A classical controlled permutation is supplied by Fredkin-type bijections (§4.1).
  - Apparatus-1 obtains it only through P3 and E-iso (:510–511).
  - MECH-1's M1/CTRL-MON keeps supplied elements (a)–(e).
  - R-nl is open.
  - G_SM switches natively but breaks A5. It is non-reciprocal for `L ≥ 5`. Its "not CP" verdict
    is relative to R1, under which joint-CP failure holds for every rule
    (`mechanism-2-20261108/DESIGN.md:44–61`, :95–96).
  - CP-PREP-1: the Fredkin switch is not identified with the selected ring (:105–121).
- **This is the earliest failure that holds under every measure.**

**Node N3: measurement.**

- Fixed read: native.
- Backaction: native, given half-known meters.
- Selectable read: not supplied (D5(ii), D7).
- Repeatability: needs P1 and E-iso.
- A passive internal observer reads existing records only (`OB/InternalObserver.lean:92`, :272,
  :290 [K]).

**Node N4: complete records.**

- Under R-lin no cell is inert. Retention needs P1 and E-iso, or blanks (D3, MP-0a).
- Under μ-G:
  - in-`V` retention is closed (D2);
  - full-history in-`V` records exclude hidden influence (D4(b));
  - inert partial records show no held-order memory (D8).
- Under any other stationary law, full-history in-`V` records make the visible process
  deterministic on the support (D4(a)).
- **Verdict.** Not supplied natively. Supplied under P1, E-iso and MP-0a.

### R4 (branch B). Kernel interface `obsTheory 𝒮 := permTheory 𝒮.Conf`

- **Holds [K].**
  - `OB/SubstratumInterfaceAudit.lean`: :770, :775, :780, :790, :816, :708.
  - `OB/FrozenSourcing.lean`: :84; :99 (no phases on any carrier); :111 (not `DerivedOI` on any
    carrier); :295, :302, :318, :327.
  - `OB/StructuralClosure.lean:348`.
  - Dense unitary control is defined only for `Fin 2` (`OB/DiscreteCompletion.lean:45`).
- **Parallel to R3.** R4 grants H-write and MP-0b, and fixes the configuration identification.
  **R3 read in the same configuration identification is a sub-theory (D6), so it inherits R4's
  ceiling.** R3's encoded-frame tier (5c) lies outside that identification.
- **Point 3, confirmed.** Rule-independence holds by `rfl`, and its substance is maximality.
  Rule-derived, bijection-generated configuration interfaces stay inside the ceiling (D6). An
  escape must change what an observer operation acts on.

### R5. Candidate replacement interfaces

| Candidate | Escapes R4? | Source | No-go results | Classical control | Single-qubit target |
|---|---|---|---|---|---|
| **5a** rule-derived configuration availability | No (D6) | — | [K] | classical | fails T-C |
| **5b** nonlinear or state-dependent rule, configuration level | No (D6); G_SM addresses N2 as a proposal | rule change; G_SM is an SM hypothesis | as 5a; MECH-2 Lemma F, U2, NC [R] | Fredkin switching is classical | G_SM: non-CP relative to R1; no non-Clifford (U2) |
| **5c** encoded carrier via a fixed linear frame | Partly: an encoded Hadamard from a hidden permutation (op-quotient v3 :11–23) | the identification, a representation choice; frame chosen for covariance (MECH-1 SC-1) | U2(ii) (R1); Lemma F; NC **only with spanning reads** (MECH-2 :66–71); no exact `rot` on finite carriers (apparatus-1 :955–1023; Main:558) | with spanning reads: classical epistricted model | **reachable by CP operations, relative to the frame: stabilizer/Clifford only** (U2 under R1, `A_4 ≀ S_n`; Proposition C at odd `q`; 24 Clifford under eight-sign; P★ only in a non-CP instrument) |
| **5d** record level, operations on record laws | Not shown | target-neutral by M-INACC's definition, if achieved | see R7 below; M-INACC not supplied by G_SM or `G_σ`; ARP-1-MARC | full access is commutative ([K] `OB/CentralObservation.lean:620`); supplied restrictions (KS sphere, Apparatus-1 P1–P3, op-quotient v3 private access) caught by the non-import test | [O] |
| **5e** emergent amplitude space | Only with E-real, E-pair and E-control supplied (two-mode-drive :25–40) | **imported**: those resources, plus Main:552, `OB/LiftSource.lean:164` [K], `OB/ExecSource.lean:129` [K], Main:644, :588 | the native sign read does not factor through a density matrix (whole-model-bridge :14, :242) | Koopman–von Neumann [W], for a real continuous oscillator lattice (not R-lin over `ℤ/q`): passing T-C does not discriminate | T-C only with those resources |
| **5f** infinite quasilocal lattice | No by itself (`OB/QuasilocalCharacterization.lean:792` [K]) | — | needed for exactness (Main:558), not sufficient | — | combine with 5d |

**MP-2: the open escape (CONFIRMING; R6, R7).**

- **The structure to replace.** The configuration-basis identification. No rule change lifts it
  (D6).
- **The escape left open.** Within their hypotheses, U2 (R1), Lemma F, Theorem NC, Main:558 and
  TUNE-1's bounded-`|C_n|` FAIL-CLASS leave open 5d with **M-INACC on growing carriers**.
  - Credit: MECH-2 §6.2 (:108–117); mathcon1 Shape 1 (:585); ARP-1-MARC (`result.md:36–38`).
    ARP-1-MARC is a finite-model protection result. It survives decoupling, and it is conditional
    on registration, P2 and H-PREP.
- **R7: possible ingredients, not established requirements.**
  - M-INACC is necessary only within NC's hypotheses (injectivity, H-LIFT, spanning reads).
  - Carrier growth is necessary for exact reproduction by Main:558 [P, half imported], and, at
    fixed ε, for TUNE-1's bounded-`|C_n|` family classes [W].
  - Sufficiency is open.
- **Other ground (R6).**
  - Native `Z`/`X` reads without a `Y` read: NC's hypotheses are not met, and contextuality there
    is **undecided** (MECH-2 :107–108). This is not an escape route.
  - mathcon1 Shape 2, a changed identification under which P★-type conditioning is CP: it overlaps
    rows 5b and 5c.
  - mathcon1 Shape 3, B1's mixing template with a phase-congruent readout quotient: it overlaps
    row 5e, and mathcon1 counts E-real, E-pair and isolation against it. It is open only on the
    terms of 5e.
- **"Non-importing" holds by definition.** Whether any `φ` realizes M-INACC is open.
- **Scope of "not constructed".** The sources read, plus `git grep M-INACC` over
  `main@fb733b4a`. Hits: mathcon1, MECH-2, minacc-1, ARP-1-MARC and q3-a6-offsets. None constructs
  5d.

***

## 4. Controls

### 4.1 Classical control

`𝔖_F` is a classical reversible computer: Fredkin exchanges
`(s, a, b) ↦ (s, s ? b : a, s ? a : b)` plus a clock.

| Criterion | Result | Too weak? |
|---|---|---|
| N1-K / N1-S, hidden carrier, μ-G | fail. Selection is dynamical (a routed write) but the choice cannot be held next to the carrier (D2), exactly as for OI | no; the failure is target-neutral and shared |
| N1–N4 under MP-0a | pass | infrastructure is target-neutral by design |
| Qubit tier, configuration-level operational interface | fail: no phases (any carrier), no dense control (`Fin 2`) [K]; compatible reads [K]. Not established for other observer-relative representations | no |
| Qubit tier, restricted-access classical models (KS, Spekkens, Main gluing) | pass T-P to T-R | caught by the non-import test |

- R-lin is weaker than `𝔖_F` at N2.
- One qubit has classical hidden-variable models, so the qubit tier tests sourcing, not
  quantumness.
- **Scope of `𝔖_F`'s qubit-tier failure (owner addition 3).** The failure is established under
  the configuration-level operational interface: `permClass`, `NonnegBounded`
  (`OB/FrozenSourcing.lean:79`, :84, :99, :327 [K]). It is **not** established for every observer-relative
  representation of `𝔖_F`. Under an encoded identification (5c) or a record-level quotient (5d),
  `𝔖_F` is not covered by that ceiling, and its standing there is open. The non-import test
  catches the restricted-access classical models known to pass, but it is not a theorem about
  every representation.

### 4.2 Single-qubit target, at (ε, K)

| Requirement | Content |
|---|---|
| T-P | **Selectable** heralded preparations reproducing `(1 + r·n)/2` within ε on an ε-net of the Bloch ball. The net includes a non-stabilizer pure state, e.g. `r = (3/5, 4/5, 0)`, and an equal-Z, different-X pair. |
| T-C | Setting-selected reversible family about two axes at `cos θ = 3/5`, consistent over `j ≤ K` applications. |
| T-M | Selectable sharp Z and X reads (Y for spanning), chosen after and independently of the preparation, with Lüders repeatability and disturbance. |
| T-R | Complete records, no renormalization; the residual carrier matches the Lüders post-state. |
| D | One fixed `𝔖`; no write outside `φ`; non-import test passed. |

The claimed supplies, restated from r2 §4.2 so that this report stands on its own (r4, nit 6),
with the r3 qualifiers added:

| Claimed supply | T-P | T-C | T-M | T-R | D |
|---|---|---|---|---|---|
| Main gluing and single dynamics (Main:564–582) | ε | ε | ε | pass | **fails** (data in the hidden register; realizes non-quantum families, Main:582) |
| Comb theorem (Main:480) | per menu | no continuum (Main:486) | per menu | pass | **fails** (`u_c` holds the target) |
| Apparatus-1 (R-lin, `q = 2`, P1–P3, E-iso, H-PREP) | stabilizer | no encoded S, no `rot` | Z/X Lüders exact | heralded pass | **fails** (P3, P1, P2, E-iso) |
| MECH-1 (odd `q`) | stabilizer | Clifford via NNB | stabilizer instruments | under posits | **fails** (Theorem T) |
| MECH-2 (G_SM, `q = 2`) | P★ only in a non-CP instrument (relative to R1) | no non-Clifford (U2, R1) | Z/X | — | hypothesis; C-CP fails relative to R1 |
| B1 two-mode drive | points | every angle | the sign read is not quantum | — | **fails** (E-real, E-pair, E-control) |
| KS sphere model | exact | exact | exact | exact | **fails** (everything supplied) |
| Operational quotient v3 | stabilizer region | 24 Clifford; error ≥ 1/15 non-Clifford | — | — | supplied region and access |
| TUNE-1 R-lin, R-nl | FAIL-CLASS on subclasses, else INCONCLUSIVE | same | same | same | H-μ, H-write carried |
| `obsTheory` (R4) | readout only | no dense control on `Fin 2` [K]; no phases (any carrier) [K] | passive record reads | external labels (MP-0b) | grants write access |

Every row fails D, or fails a T-condition, or is INCONCLUSIVE.

***

## 5. The three gaps, the earliest failure, and the owner's key test

| Gap | Target | Supported finding | Layer | Verdict |
|---|---|---|---|---|
| **1. Preparation** (N1-K, N1-S) | a real inability to make selectable preparations, not merely a lack of correlation | Under μ-G (posited via (iv)), for hidden carriers and every bijection, the choice cannot be held alongside the selected carrier (D2 applied to N1-S). Writing the chosen value is in the affine class; R-lin itself needs the carrier's previous slot known (a blank, MP-0a) and the neighbours known or isolated. The cost is blank memory, resolved classically by MP-0a or MP-0b. Under μ-O (derived) and μ-R: N1-K can be native (swap); N1-S is open | paper [W] on [P] Main:54, :58 | **Classical gap, measure-relative.** The no-go needs μ-G **and** "held = function of present `V`" |
| **2. Classical control** (N2) | a restriction of the actual affine rule and its apparatus, not of all deterministic systems | D5/D7: under one affine `φ` acting on every cell, a setting acts only by translation, as a measure-free property of the map. Fredkin bijections supply control, so the restriction is specific to the gauge-derived affine class. **Classical repair only:** the candidate for modification is A5 linearity together with the affine form it strengthens (ledger (vii)). Dropping A5 alone, keeping the affine form, does not restore control (D5). Lifting both is a Layer-0 revision (MP-1). It recovers classical setting-selective control and does not by itself bear on gap 3 | paper [R] + [W]; one proof, re-derived twice | **Classical gap of the actual rule; the earliest failure that holds under every measure** |
| **3. Quantum operations** | a sourced operation beyond the configuration-level ceiling, without assumed quantum structure | Configuration identification capped for every rule [K]: no phases and not `DerivedOI` on any carrier; no dense control on `Fin 2`. Rule-derived interfaces stay inside (D6), and so does R3 read in that identification. **Nonlinear or non-affine rules at configuration level also stay inside (D6, row 5b),** so the gap-2 repair does not close gap 3. Encoded frames are capped by frame-relative paper results. Emergent amplitudes are imported. 5d with M-INACC on growing carriers is not constructed | [K] configuration level; [R] encoded; [O] 5d | **Remains open; not shown impossible. Independent of the gap-2 repair** |

**Earliest failure, qualified.**

1. **N1 (as N1-S) comes first in operation order,** but only under the posited global selection
   μ-G and the held-equals-present-`V` convention. It is classical.
2. **N2 is the earliest failure that holds under every measure.** It is classical and paper-level.
3. **The configuration-identification ceiling is the first kernel-proved failure,** on branch R4.
   R3 read in that identification inherits it (D6).

**The owner's key test is supported at paper level.** Can gaps 1–2 be resolved entirely
classically while gap 3 remains?

- **Gap 1** is resolved by a classical resource (MP-0a) or a classical convention (MP-0b), which a
  reversible computer shares.
- **Gap 2** is resolved by a classical non-affine switch. For OI this means modifying A5 linearity
  and the affine form it strengthens, a Layer-0 revision under §A.29.
  - This is a **classical repair only**. By D6 and row 5b, a nonlinear or non-affine rule at the
    configuration level stays inside the kernel ceiling.
  - Removing A5 therefore does not by itself explain quantum behaviour. The repair and the
    quantum question are kept separate.
- **Gap 3 then remains.**
  - `𝔖_F` with MP-0a passes N1–N4 [W]. It still fails the qubit tier **under the
    configuration-level operational interface** [K].
  - That failure is not established for every observer-relative representation of `𝔖_F`
    (§4.1). Under such representations it passes the qubit tier only in the known cases where an
    access restriction is supplied, which the non-import test catches.
- **"Remains" means no route on `main` closes gap 3,** not that closing it is impossible. M-INACC
  and growing carriers are possible ingredients only (R7).

**Missing premises.**

- **MP-0a (H-LOW; resource; gap 1).**
  - *Statement:* fixed known values on designated cells, independent of setting and carrier,
    uniform elsewhere, declared as the joint initial law (Main:58, :97, :602).
  - *Physical content:* a past-hypothesis-type supply of ready cells.
  - *Why it is not supplied:* μ-G is not that law, and ready cells under μ-G cost D3 (R3 nit). Main
    §4.6 supplies only selection (Main:742).
  - *Hard to vary?* No. It carries no quantum content.
- **MP-0b (H-MEM; interface convention; gap 1).** The visible history counts as held, outside
  `V`. It is the same type as MP-2. R4 grants it.
- **MP-1 (M-CTRL; gap 2).**
  - *Statement:* the non-translational part of `φ^τ|_Σ` depends on `s`; `s` is recorded and
    independent of `Σ` (xiv); the timing is sourced.
  - *Physical content:* non-affine conditional couplings.
  - *Why it is not supplied:* D5. The affine form is **derived** (ledger (vii)).
  - *Hard to vary?* No in bare form. Adopting it is a **Layer-0 revision under §A.29**. Nothing here
    proposes it.
  - *Modification candidate (owner addition 1).* A5 linearity, together with the affine form it
    strengthens. The candidate exists **only** to recover classical setting-selective control. It
    is **not by itself** a route to gap 3 (r4, nit 2).
    - At the configuration level, D6 excludes it.
    - Under NC's hypotheses no dynamics escapes (MECH-2 §6.2).
    - In a changed identification (5c, 5d), the rule's form stays a possible ingredient: MECH-2's
      nonlinear conditioning gives the non-stabilizer state P★, and M-INACC (a functional the
      fixed rule uses) was tested on the nonlinear `G_σ` (`minacc-1-20261108/RESULT.md:37–60`).
    - Dropping the affine form also means modifying the amplitude-scale gauge-invariance step from
      which ledger (vii) derives it.
- **MP-2 (gap 3).** Replace the configuration identification. The open escape is 5d with M-INACC on
  growing carriers. These are possible ingredients only, and sufficiency is open.

***

## 6. Status table

| Item | Status | Support |
|---|---|---|
| S⇔D⇔Q_fb | proved | [K] |
| Comb, gluing, continuum realizations with supplied data | proved on paper | [P] |
| No fixed finite carrier gives the full qubit | proved, half imported | [P] Main:558 |
| `obsTheory` ceiling: no phases, not `DerivedOI` (any carrier); no dense control (`Fin 2`); rule-independent | proved | [K] |
| D1, D3, D6, D7 | derived here | [W] (D6 on [K]) |
| D2 | Main:58 plus invariance; Q-b1; closes the in-`V` route under μ-G | [P] + [R], ELABORATING |
| N1-K under μ-G: fails for hidden carriers | derived | [W] |
| N1-K under μ-O, μ-R: can be native (swap) | derived by hand | [W] |
| N1-S under μ-G: retention failure, hidden carriers, every bijection | derived | [W] |
| N1-S under μ-O, μ-R | open | [O] |
| Selection writable in the affine class; R-lin needs the carrier's own previous slot known (blank) and the neighbours known or isolated | derived | [W] |
| D4(a) (any stationary law); D4(b) (μ-G) | ELABORATING | [W] |
| D8 (partial-window form; owner's test) | candidate, unreviewed, ELABORATING of Main:97 | [W] |
| D5 / N2 (affine class; measure-free map property) | one paper proof re-derived twice | [R] + [W] |
| N3 fixed read; N4 under P1, E-iso, MP-0a | conditional | [R] / [W] |
| R-nl at N2; L5.4; 5d with M-INACC; sufficiency of MP-0 to MP-2 | open | [O] |
| Owner's key test (gaps 1–2 classical, gap 3 remains) | supported at paper level; `𝔖_F`'s qubit-tier failure holds under the configuration-level interface only | [W] on [K]/[P]/[R] |
| Measure dependence of each result | tabulated (§2A); success under one measure does not establish that OI selects it | [W] |

***

## 7. §A.31 classification and markers

- **D2: ELABORATING.** **D4: ELABORATING.** **D5: CONFIRMING.** **D6: ELABORATING.** **MP-2:
  CONFIRMING.** **5e Koopman–von Neumann: ELABORATING.**
- **D8:** ELABORATING candidate, unreviewed. It is restated from the reviewer's check and verified
  by hand here.
- **N1-K/N1-S split: ELABORATING.** It separates knowing from preparing, as the owner raised.
- **AW-OA1-1 (CONFIRMING; scoped).** Under Main's convention `X = V`, conditioning on `X_{<t}`
  uses history that `V_t` does not hold (Main:97; obsmu :913–917). With a coarser readout `Y` and
  records in `R ⊂ V`, the observer does hold its history, and D8 applies instead.
- **AW-OA1-2:** Main §4.6 replaces the past hypothesis's selection role, not its supply role.
- **AW-OA1-3:** under the affine class, the first native gap that holds under every measure is
  classical.
- **Pressure test on a favourable branch.** "Selection is native under affine rules" was checked
  against R-lin's actual coupling and narrowed: the fixed wave coupling masks the written value
  with the carrier's own previous slot (always a blank requirement) and with the neighbours (known
  or isolated).
- **Tally:** no NEW findings in this pass.

***

## 8. FH→SOURCE-1 trace check

Unchanged from r2 §8. The §D3 row reads: "settled by D6 for configuration-level,
bijection-generated source maps". The final row reads: "first kernel-proved loss, on a parallel
branch; the measure-robust paper loss at R3/N2 is classical."

## 9. Reading inventory

As in r2 §9, plus:

- Main:54, :88, :129 (re-read for r3);
- MECH-2 :104–108;
- `REVIEW-OA-1-r2.md`.

Not read: as in r2. Negative claims are limited to these sources and the stated grep.

## 10. Limits

- [W] items are reviewed only by a same-family model. D8 is unreviewed.
- R3 verdicts are for R-lin; N2 covers the gauge-derived affine class. R-nl is open.
- The N1 no-go is scoped to μ-G with held-equals-present-`V`. Under μ-O and μ-R, N1-S is open;
  neither measure is H-LOW.
- D4(b) and D8 are μ-G only. §2A gives each result's measure dependence.
- The classical control's qubit-tier failure is established under the configuration-level
  interface only, not for every observer-relative representation of it.
- A5 is named as a candidate for classical repair only. Modifying it is not claimed to bear on
  gap 3.
- The qubit tier tests sourcing, not quantumness. Composite systems, Bell and the Born exponent are
  untouched.
- 5d with M-INACC is named, not constructed. Its necessity holds only within stated hypotheses, and
  its sufficiency is open.
- No manuscript claim is affected.

## 10A. Recommended next question (owner's words as relayed by the coordinator; not authorized; not part of OA-1)

> "Can deterministic physical dynamics induce operations on emergent observer states that are
> genuinely richer than permutations of configurations, while still providing a common physical
> preparation and readout process?"

*Provenance (r4, nit 5).* These are the owner's words, given in the coordinating session chat on
2026-11-12 and relayed by the coordinator. They are not yet recorded on #1169; the coordinator will
record them there.

It is recorded as the recommended next question. It is not authorized and is not part of OA-1. It
sits at the open ground this report identifies: gap 3, rows 5c and 5d, and MP-2. Any unit on it
would need its own owner scope.

## 11. Changes from r2 (finding → change; verdicts moved)

| Item | Change | Verdict moved? |
|---|---|---|
| R1 | N1 split into N1-K and N1-S. The μ-G no-go now needs "held = function of present `V`". Selection is in the affine class (refined for R-lin: known or isolated neighbours). N1-S under μ-G is a retention/blank-memory failure, resolved by MP-0a or MP-0b. Under μ-O, N1-K is native (swap); N1-S is open. Propagated to §0.3, N3 and N4, §4.1, §5, §6 | **Gap 1 recast:** from "no hidden carrier can be prepared" to "a selected hidden carrier cannot be held with its choice record under μ-G". Still classical |
| R2 | μ-G and μ-R typed as posited via (iv) (Main:54 "a selection principle"); μ-O as derived; §1 reconciled with N1 | the N1 failure now holds "under the posited global selection" |
| R3 | MP-0a's "why not supplied" corrected; §5 item 3 notes that R3 in the configuration identification inherits R4's ceiling | wording |
| R4 | N2 measure-free as a map property; (xiv) only for the operational reading; "earliest failure that holds under every measure" | wording; N2 verdict unchanged |
| R5 | D4 split: (a) any stationary law, deterministic on the support; (b) μ-G only, by Main:147 with `T` the uniform-prior kernel (Main:88, :129). R1, N4 and §10 edited | D4(b) narrowed |
| R5′ | D8 added (partial window; owner's test run: no observed memory at held orders under μ-G with inert records); example hand-checked; AW-OA1-1 scoped to `X = V` | new candidate (ELABORATING, unreviewed) |
| R6 | native `Z`/`X` marked "undecided"; mathcon1 Shape 2 ↔ 5b/5c, Shape 3 ↔ 5e | route list corrected |
| R7 | M-INACC and growing carriers are possible ingredients, necessary only within NC, Main:558 and TUNE-1 FAIL-CLASS; sufficiency open; "growing carriers" used | necessity claim narrowed |
| Added | three-gap table; owner's key test stated as supported at paper level | — |
| Owner 1 | A5 linearity, with the affine form it strengthens, named as a modification candidate for classical control only (gap-2 row, §5 key test, MP-1, §0). Gap-3 row notes that nonlinear configuration rules stay inside the ceiling (D6, 5b) | gap 2 and gap 3 explicitly decoupled |
| Owner 2 | §2A measure-dependency table; measures typed (μ-O derived; μ-G and μ-R posited via (iv)); success under a measure ≠ OI selecting it | — |
| Owner 3 | `𝔖_F`'s qubit-tier failure scoped to the configuration-level interface (§0, §4.1, §5, §6) | key-test qualifier added |
| Owner 4 | recommended next question recorded verbatim (§10A), not authorized | — |

## 12. Changes from r3 (nits of `REVIEW-OA-1-r3.md`; no verdict moved)

| Nit | Change |
|---|---|
| 1 | N1-S under R-lin: the carrier's own previous slot `−y_i` also masks the write, and isolation does not remove it. Selection needs that slot known (a blank, MP-0a) **and** the neighbours known or isolated. Applied in N1-S, the gap-1 row, §6 and §7 |
| 2 | MP-1: "not a route to gap 3" → "not by itself a route". Cites D6, MECH-2 §6.2, P★ and `G_σ` as ingredients under a changed identification, and the gauge step behind ledger (vii) |
| 3 | §2A: N3 split into fixed read (native) and backaction (only given half-known meters, a posit, SA-1(c); D3 cost under μ-G) |
| 4 | §4.1 citation `FrozenSourcing.lean:74` → :79, :84, :99, :327 |
| 5 | §10A provenance: owner's words from the coordinating session chat, 2026-11-12, relayed by the coordinator, not yet on #1169. Standing cites c.6829898892 for the scope addition |
| 6 | §4.2: r2's claimed-supply table restated with r3 qualifiers |

