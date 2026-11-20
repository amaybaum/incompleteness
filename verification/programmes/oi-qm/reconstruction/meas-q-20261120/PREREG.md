# MEAS-Q preregistration: delivery and preparation on the published rounded rule

**Standing.** Preregistration of a paper-only gem-finding unit (AGENTS.md §A.29, §A.31 depth-first
form, §A.41, §A.44). Committed and pushed before any search, enumeration or simulation on Q is run.
It fixes the tasks, the resource ledger, the search spaces and bounds, the controls, the
invariant→checkpoint table and the decision rule. It states no expected result for Q. It adopts no
premise and edits no manuscript, Lean module or registry.

- **Authorization.** Owner `amaybaum`. Scope:
  [#1169 c.7032429839](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7032429839),
  2026-11-20T06:37:08Z, row MEAS-Q: "Re-run DELIVER-1 and NATPREP-1 on the published rule (q=2¹⁶,
  ℤ³). Support-closure invariance fails there, so ask two questions: can order from outside a
  component reach a ready cell, and does an untuned law produce delivering components with
  positive probability and a stated cost? Use UNIV-2's outcome. Bounds, gadget criteria and controls
  are preregistered. Small exact computations are allowed." Decision rule there: "Counts as a gem
  only if it gives (i) a native delivery or preparation with its cost, or (ii) a scoped obstruction
  on the real rule. A bounded not-found is a recorded negative only." Condition:
  [#1169 c.7033018172](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7033018172),
  2026-11-20T07:12:08Z: "Starts when UNIV-2 (#1444) has an acceptable independent review. Delivery
  and preparation are tested on the published rule; no unaccounted controller or prepared resource
  is imported." "None of these authorizes adopting a new physical assumption." Start:
  [#1169 c.7033513830](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7033513830),
  2026-11-20T07:39:53Z: "MEAS-Q is authorized to begin within its scope in comment 7032429839 once
  the independent re-review of UNIV-2 accepts." That re-review is ACCEPT-WITH-NITS at `8866cf4a`
  ([#1444 c.7033699598](https://github.com/amaybaum/incompleteness/pull/1444#issuecomment-7033699598),
  2026-11-20T07:50:38Z).
- **Goal link (§A.47).** Serves #866 (native preparation source) for #1169: decides, on the
  published rule Q, (Q1) whether content from outside a ready cell's component can reach it and
  leave it ready with a held record, and (Q2) whether an untuned law yields delivering
  configurations with positive probability, and at what accounted cost. It does not decide the
  outcome in advance. Unchanged: A1 OPEN/UNADOPTED; physical measurement sourcing NOT PASSED.
- **Accountable Issues.** #866, #1169. Predecessors (records on `main`, relative to
  `verification/programmes/oi-qm/reconstruction/`): DELIVER-1 `deliver-1-20261119/` (DL1),
  NATPREP-1 `natprep-1-20261119/` (NP1), PREP-REGRESS-1 `prep-regress-1-20261119/` (PR1), UNIV-1
  `univ-1-20261119/` (U1). UNIV-2 (U2R) is cited at commit `8866cf4a` on
  `research/univ-2-20261120`: accepted on review, not on `main` at `D`; nothing here is proved from
  it. U2R's verdict (no controlled turn within its bounds; first failure R3, radiation; hypothesis
  AW-UNIV-3) is used only to choose what is not searched again.
- **Not overlapped.** G3-W1 (conserved energy of the d = 3 rule) and POSIT-MIN (posit audit, #1451)
  are separate units; this unit computes no conserved quantity and audits no posit.
- **Snapshot `D`.** `main` at `bce3ab0b6f28b2129505a84ad4756c0b11ea67b9` (branch base).

***

## 1. Object

**Q.** The rounded rule of SM §4.2 at `q = 2^16` on `ℤ³` (U1 §1):
`x_{t+1}(i) = ⌊(Σ_{j∼i} x_t(j) + 1)/3⌋ − x_{t−1}(i) mod q`, sum over representatives `0,…,q−1`.
State: the two-slice pair `(x_{t−1}, x_t)`. All computations are exact integer arithmetic, either in
Q itself (mod `q`) or in RZ `y_{t+1} = ⌊(Σ y_t + 1)/3⌋ − y_{t−1}` on a uniform background `c` with the
window `0 ≤ c + y < q` checked at every tick (U1 Lemma 2.1, one direction). Any reported candidate
is re-run in Q itself.

**Backgrounds.** A uniform background `c` (both slices equal to `c` at every site) is a fixed point
of Q for every `c`. The unit treats `c` as a parameter and records which values of `c` a statement
holds for. Every background is a prepared resource and is entered in the ledger (§3).

**U₂.** The `q = 2` member (DL1 §2), used only for positive controls and countercontrols.

***

## 2. Tasks

Carriers, blocks and laws are as in DL1's DT and NP1 §1.4. Fixed here:

- **Carrier.** A fair bit `c_k` placed at `t = 0` on declared slots: `c_k = 0` leaves the
  configuration as declared; `c_k = 1` adds `+1` (Q, RZ) or flips the bit (U₂) on each declared slot.
- **DT_s** (NP1 §1.4, unchanged). Single-site block `H`, `ε = 0`: times `τ₁ < τ₂` at which `W_τ(H)`
  equals the same known value `w*` in every carrier branch; a use of `c_k` in `(τ₁, τ₂)` (the law of
  `W_s(H)` depends on `c_k`); at `τ₂` a log block `L` disjoint from `H` and from the carrier's
  initial slots determines `c_k`, and meets (R): `W_t(L)` does not depend on `c_k` for `t` before the
  first use of `c_k` at `H`. One carrier, one delivery (`N = 1`) in the searches.
- **DT_A** (stricter; defined here because carriers can move on Q, see AW below). DT_s plus:
  (A1) `H` and `L` lie in a declared bounded apparatus region `A`, and the carrier's initial slots lie
  outside `A`; (A2) persistence: `W_t(L)` determines `c_k` at every `t ∈ [τ₂, τ₂ + 60]`, the same
  `L` throughout. A record that leaves `A` with the carrier, or is erased within 60 ticks, fails.
- **Cross-class delivery (Q1).** A DT_s or DT_A delivery in which the carrier's initial slots and
  `H` lie in different classes of `Comp(A_0)` (NP1 §3: classes of `cl₂` of the initial perturbation
  support, at mutual ℓ1-distance `≥ 3`; perturbation relative to the background `c`).
- **Untuned law (Q2).** NP1's U1–U4, with the single-site law on the pair alphabet `{0,…,q−1}²`. The
  family used for statements: `ν_{c,ρ,κ}` = product over sites of `(1−ρ)δ_{(c,c)} + ρκ`, with `κ` a
  full-support law on the pair alphabet. U4 (open set) requires every positive statement to hold for
  all `κ` of full support and all `ρ` in an open interval. Positive probability plus selection of one
  pattern is not counted as preparation (NP1 §2.6); its selection cost is stated.

***

## 3. Resource ledger (the owner's accounting condition)

Every run is generated from a ledger: a list of items, each with its sites and slots, its values,
and its cost. Nothing else may enter the initial state, and nothing may act during the run.

| Item | Cost stated as |
|---|---|
| background `c` on a region `V` | `D(δ ‖ u) = 32|V|` bits (two 16-bit slices per site); for an untuned law, `|V| · D(single-site law ‖ u)` |
| designed pattern (line, gadget, environment, signal) on slots `S` | `16|S|` bits for a pinned pattern; under `ν_{c,ρ,κ}`, its probability and selection cost `log₂(1/ν(E))` |
| carrier | a fair bit: `0` bits of budget; it is the measured system |
| controller (any write not produced by the declared rule) | must be declared with its schedule; a run whose trajectory differs from the rule's own iterate is **unaccounted** |

**Ledger audit** (`ledger_audit`): rebuilds the initial state from the ledger and requires equality
with the run's initial state; then recomputes every tick with the declared rule and requires
equality with the run's trajectory. Any difference is reported as an unaccounted prepared resource
or an unaccounted controller. The audit runs on every reported candidate and on every control.

Cost accounting for any reported delivery also states: the budget DL1 (2.4) and PR1 2.5 require,
`(N+1)(1 − h₂(ε))`; the budget supplied on the delivering region; the PR1 2.3 transfer identity
`K_t(H) + D(p_{Rest,t} ‖ u) = D(p₀ ‖ u)` evaluated exactly on the run's two-branch law; and the
probability and selection cost under `ν_{c,ρ,κ}`.

***

## 4. Depth-first walk (nodes, searches, bounds)

**Node 1 — analytic (Q1, obstruction branch).** Is there a confinement property of Q in place of
DL1 Theorem 2.2, which fails on Q (DL1 E8, NP1 §3.4)? The question is answered by a written proof
or not at all; the checks K1–K3 below test any stated lemma exactly. No result is assumed here.

**Node 2 — Q1 on Q, searches.**

- **S-A (box enumeration, DT_s and DT_A, NP1 §2.3 re-run).** Q at background `c = 2^15`, run in RZ.
  Boxes: line 3, line 4, line 5, `2×2`. One carrier at one site, mode current / previous / both
  slice. Environment: every other slot in `{−1, 0, 1}`. Every `H` in the box other than the carrier
  site; every single-site log (sufficient for one carrier at `ε = 0`, since two branches differ on a
  block iff they differ on one of its sites). Evolution in the box with zero outside; the box run
  is exact in `ℤ³` up to and including the tick after the first tick on which any box site leaves
  `{−1,0,1}` (a *breach*; every site of these boxes has a neighbour outside the box). Window: if
  the orbit returns to its initial state with period `P ≤ 40`, the window is `3P` (as NP1); otherwise
  the window is 120 ticks, cut at breach + 1. DT_A in S-A: `A` = the box minus the carrier site.
- **S-B (breach and cross-class contact).** For every S-A configuration on line 3, line 4 and `2×2`
  that breaches: re-run in Q itself (mod `q`) on the torus `(ℤ/42)³`, background `2^15`, both carrier
  branches, horizon 28. The torus orbit is the `ℤ³` orbit of the periodically repeated pattern;
  every site at torus distance at most 8 from the box has an exact `ℤ³` value up to `t = 28`. For
  every such site outside the box: first contact (value ≠ background in some branch), use, return
  to `(c, c)` in both branches, and DT_s with any single-site log in that exact region. Bound: if
  there are more than 4 000 breaching configurations, every `m`-th in enumeration order with
  `m = ⌈count / 4000⌉`. Recorded per configuration: breach time, two-slice support radius at 28.
- **S-C (moving carrier on a W2 line).** U1's W2 line on `ℤe₁` at `c = 2^15`, W2 signal as carrier
  (`c_k = 1`: signal present; `c_k = 0`: absent), launched 8 sites from `H`, `H` every line site
  within 2 of the origin, horizon 120. DT_s and DT_A, with `A` = sites within ℓ∞ distance 2 of the
  origin.
- **S-D (latch beside a straight W2 line; DT_A).** Not a turn and not U2R's junction families: one
  straight W2 line along `e₁` (U2R J-geometry with no B), gadget in `R_L` = the 24 non-line sites
  within ℓ∞ distance 1 of the origin, signal component only (U2R A1, reproved by check K4 here), at
  most 2 gadget sites, values in `{±1, ±2}`; 4 line phases; signal launched 8 sites away from either
  side (2 directions). Size `(1 + 4·24 + 16·C(24,2)) · 4 · 2 = 36 104`. `A` = line sites with
  `|x| ≤ 2` ∪ `R_L⁺` (non-line sites within ℓ∞ distance 2 of the origin). Requirements, in order:
  - L1 quiescence: no-signal orbit `N` with `N(4) = N(0)` and nothing outside line ∪ `R_L⁺` for `t ≤ 8`;
  - L2 no radiation: in the signal orbit `S`, no value outside line ∪ `R_L⁺` is ever nonzero, to
    `T₁ + 60` (`T₁ = 120`), and the box margin stays zero (the box orbit is then the `ℤ³` orbit);
  - L3 line restoration: at `T₁` and `T₁ + 60`, every line site outside `A` and outside the window of
    the outgoing signal (if any) equals `N`;
  - L4 DT_A: some `H ∈ A` and some fixed `L ⊆ A ∖ {H}` meet DT_A with `τ₁ = 0`, `τ₂ ∈ [T₁ − 3, T₁]`,
    persistence to `τ₂ + 60`;
  - L5 exactness: `max |y| < 2^15` along both orbits, and the candidate re-run in Q agrees;
  - L6 (informative only, not a requirement): a second signal 12 sites behind gives a second
    persistent record.
- **Not searched** (U2R covered or bounded them): junction turns, transfer onto a second line,
  gadgets of more than 2 sites, other signal types, other launch phases.

**Node 3 — Q2, untuned law.**

- **Probability and cost.** For every delivery found in S-A, S-B, S-C or S-D: its pattern weight,
  the isolation cone, `ν_{c,ρ,κ}` lower bound and selection cost as NP1 §2.4 and Lemma N4.1, with the
  exact formula and values at `κ` uniform on the pair alphabet and at `ρ ∈ {10⁻², 10⁻³}`.
- **Dilution.** Whether NP1 Lemma N2.3 holds on Q (proof or not; check by exact enumeration on the
  S-A boxes under `ν` restricted to a ternary `κ`).
- **S-E (noise on Q, evidence).** Q itself on `(ℤ/32)³`, background `2^15`, initial law
  `ν_{c,ρ,κ}` with `ρ ∈ {10⁻³, 10⁻², 5·10⁻²}` and `κ ∈ {uniform on all pairs, uniform on the 8
  non-background ternary pairs}`, 3 seeds each, horizon 40: fraction of sites equal to `(c, c)`,
  fraction ever outside `{c−1, c, c+1}`, per tick. Evidence only; no statement about `ℤ³` beyond
  the light cone is drawn from it.

Compute bound (§A.40): each command below 30 minutes on one core; a run that would exceed it is
stopped and reported.

***

## 5. Controls (computed before any verdict; a failed control voids the verdict)

| Id | Control | Required outcome |
|---|---|---|
| PC1 | the S-A enumerator, unchanged, run on U₂ (rule-parametrized) for line 3, line 4, line 5, `2×2`, one carrier, `N = 1` | NP1 S2 counts reproduced: 0, 184, 1904, 736 |
| PC2 | DL1 2.3(f) in the PC1 run (line 5, carrier site 0 current slice, `H` = 1, `w* = (0,0)`, environment `(·,0,1,0,1)`) | found as DT_s, `τ₂ = 5`, log site 3 |
| PC3 | latch calibration oracle: S-D's line run by the 1D rule, plus one gadget site whose two slices update `(g_p, g_c) ↦ (g_c, g_p + [y_ℓ(t) ≠ y_ℓ(t−4)])` at the line site `ℓ` beside it | passes L1–L4 through the S-D classifier, fails L5 (not Q) |
| PC3b | the same oracle with the increment set to 0 | fails at L4 (no record) |
| CC1 | U₂, two classes at distance ≥ 3 (carrier class and `H` class), random designs on a torus | `H` never depends on the carrier (cross-class use impossible, DL1 2.3(c)) |
| CC2 | an imported controller: a Q run in which `H` is rewritten to `w*` by a write not produced by Q | DT arithmetic met; ledger audit reports an unaccounted controller |
| CC3 | an imported prepared resource: an initial state with a pattern not in the ledger | ledger audit reports an unaccounted prepared resource |
| CC4 | S-C, the plain W2 line with a passing signal | DT_s met; DT_A fails (persistence) |
| CC5 | breach: a configuration whose boundary layer leaves `{c−1,c,c+1}`, and the background `c = 0` with a value `−1` | support leaves the closed set |
| K1 | one-site test in Q: background site with one non-background neighbour of value `v`, all `v ∈ {0,…,q−1}`, `c ∈ {0, 1, 2^15, q−2, q−1}` | the site stays at `c` exactly for the `v` stated by any Node 1 lemma |
| K2 | windowed confinement on random configurations in Q (any lemma of Node 1, tested on its stated hypothesis) | holds on every instance where its hypothesis holds |
| K3 | U1 Lemma 2.1 at `c ∈ {1, 2^15, q−2}`: ternary RZ orbit = Q orbit; countercontrol `c = 0` | equality; countercontrol differs |
| K4 | component independence (U2R A1) on S-D's box | other component perturbed, signal component unchanged |

***

## 6. Decision rule and productivity test (fixed here)

Verdict text is generated by the check script from its structured output (§8), and only if every
control of §5 holds.

1. **Gem (i), native delivery or preparation with its cost.** A delivery meeting **DT_A** on Q
   (re-run in Q itself), whose ledger audit passes, with its cost stated as in §3. It is labelled
   (i-nat) if its supply meets U1–U4 and it holds in law without selection, and (i-cond) if it rests
   on a designed supply; (i-cond) is a native mechanism conditional on that accounted supply, and
   the record states that NSC-3 and NSC-5 (PR1 §2) are not met by it. A delivery meeting only DT_s
   is not (i).
2. **Gem (ii), scoped obstruction on Q.** A written proof, with exact checks green, that excludes on
   Q a stated class of deliveries (cross-class, DT_s or DT_A) or of in-law preparations, for a
   stated class of configurations or laws. It counts only if the class covers configurations of Q
   that DL1 and NP1 do not cover, and if its boundary is shown to matter: outside the class, the
   searches exhibit the excluded behaviour (for example, contact across classes) or the proof states
   why it cannot.
3. **Otherwise: recorded negative.** Bounded not-found results are record-only.

Both (i) and (ii) may be reported. A favourable branch gets the strictest check (§A.31): any
candidate for (i) is re-run in Q, ledger-audited, and checked against CC2–CC4 before it is reported.

***

## 7. Invariant → checkpoint table (§A.41)

| Invariant asserted | Checkpoint |
|---|---|
| arithmetic is exact | integer dtypes asserted; RZ window `|y| < 2^15` checked per tick (assertion) |
| box runs equal `ℤ³` runs | S-A: breach test per tick, window cut at breach + 1; S-D: box margin zero per tick (L2) |
| torus runs equal `ℤ³` runs where used | S-B: only sites at distance ≤ 8 from the box, `t ≤ 28` on `n = 42` (distance argument in RESULT; check that the box plus 8 plus 28 is below `n − 5`) |
| enumerator semantics equal NP1's | PC1, PC2 |
| S-D classifier can pass and can fail | PC3, PC3b, CC4 |
| no unaccounted resource or controller | ledger audit on every reported candidate and control; CC2, CC3 |
| search counts complete | asserted equal to the formulas of §4 |
| Q re-run of every candidate | L5 / reported field `q_rerun` |
| controls green before verdict | the verdict function refuses to print a verdict if any control is false |
| preregistration before search | commit order on the branch: this file, then amendments, then the checks |

***

## 8. Structured outputs (§A.44)

`checks/measq_checks.py` writes `results.json` (schema: `{"checks": {id: {"ok": bool, "data": …}},
"searches": {id: {counts…, "hits": […]}}, "controls_green": bool, "verdict": {"gem_i": …,
"gem_ii": …, "class": …}}`) and exits 0 iff every check holds. The verdict is computed from that file.
Gem (ii) also needs the written proof in RESULT; the script records only whether its exact checks
hold.

***

## 9. Not done

No Lean; no manuscript edit; no premise adoption; no merge; no workflow dispatch. No conserved-
quantity search (G3-W1), no posit audit (POSIT-MIN), no junction or turn search (U2R). No
unrestricted universality search.
