# FHE-SEL-1 P-MIX: a finite-precision reversible two-mode exchange, preregistered (Stage 1A)

**Standing.** Stage 1A preregistration only, under #1169. Revision r2: it applies the independent review of `eb3802ee`
(REVISE) and the owner's P-MIX requirements recorded by the coordinating session (chat, 2026-11-08). WIP / UNVERIFIED.
Writer: Claude Code session, 2026-11-08.

This file fixes one construction, its motivation, its criteria and its controls before any result is evaluated. It
derives no result, runs no computation, proposes no premise for adoption and changes no manuscript. Stage 1B (the
derivations) is not authorized.

**Authority (quoted).**

- Owner decision, [#1169 c.6720450946](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6720450946)
  (recorded by amaybaum, 2026-11-08T10:38:44Z).
  - P-MIX row: "Can a specified physical carrier produce reversible mixing without importing quantum operations? … Q-B
    remains inactive."
  - Boundary: "A finite-carrier P-MIX candidate cannot claim exact continuous rotations merely by changing its
    representation."
  - "No computation, V3 execution, new physical axiom, manuscript change or Q-B activation is authorized."
- Planning clarification, [#1169 c.6720342295](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6720342295)
  (amaybaum, 2026-11-08T10:26:34Z).
  - P-MIX: "Can an independently motivated physical carrier and dynamics support the relevant reversible mixing?"
  - Safeguard: "Must state whether the carrier is finite or continuum. Must not assume exact rotations or activate Q-B."
  - Anchor: "On finite carriers, encoded unitaries form a finite group: Apparatus-1 excludes `rot`, and MECH-2 Theorem
    U2 applies. The #1173 Gate B1 mixer's controls are unsourced. In Stage 0 this is the relating-evolution/lift rows."
  - Three statuses: proposed / mathematically sufficient / derived from native OI.
- FHE-SEL-1 decisions, [#1169 c.6719386464](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6719386464)
  (amaybaum, 2026-11-08T08:41:15Z).
  - "Every candidate physical restriction must have an independent physical motivation established before evaluating
    whether it selects quantum behaviour."
  - Q-B stays inactive.
- Owner decision, [#1169 c.6720678942](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6720678942)
  (recorded by amaybaum, 2026-11-08T11:03:23Z).
  - Physical selection asks "why should OI or nature select a given extension?" Its success criterion is "independent
    motivation, physical sourcing, explanatory necessity and critical tests."
  - Refinement 2 (NC): "Noncontextuality alone does not rule out every state labelled non-stabilizer under a chosen
    representation."
  - Refinement 2 (U2): "Theorem U2 restricts the available encoded unitaries under its finite-frame and operation-set
    assumptions. It does not exclude every finite-order non-Clifford operation in a different extension."
  - "FHE-SEL-1 Stage 1B is still not authorized."
- **Owner requirements on P-MIX** (chat, 2026-11-08, relayed by the coordinating session to this writer; to be quoted
  with author and time in the portfolio record):
  1. State what P-MIX could establish beyond Main's finite-accuracy realization theorem (Main:566/598) and the
     conditional B1 mixer.
  2. The mechanism-off control and at least one generic reversible-discretization countercontrol must each be able to
     fail the success criterion; meeting a rounding-error bound is not enough on its own.
  3. Separate the oscillator physics from the target-inspired B1 construction; correct Theorem NC's hypotheses; define
     the finite horizon and every outcome category; make every decisive test falsifiable.
  - "A successful rounding approximation must not count automatically as evidence of a hard-to-vary principle."
  - If no new question survives, P-MIX concludes that its construction is already covered by existing mathematical
    results. The owner: "We should not manufacture novelty to keep the three-construction portfolio symmetrical."

**Order of evaluation (fixed).** The steps run in this order:

1. §3: independent physical motivation.
2. §4–§6: mathematical consequences and controls.
3. §7: comparison with the quantum-completion conditions.

§7 is evaluated only after §4–§6 are recorded. Nothing in §7 feeds back.

**Pins.** Every repository citation is to main `9c201475ba6fd8f341591d14dd8e88db2e2aaa90` (`main@9c201475`). Line
citations use these abbreviations, each a file at that commit:

- `Main` = [`papers/Main.md`](https://github.com/amaybaum/incompleteness/blob/9c201475ba6fd8f341591d14dd8e88db2e2aaa90/papers/Main.md);
  `SM` = [`papers/SM.md`](https://github.com/amaybaum/incompleteness/blob/9c201475ba6fd8f341591d14dd8e88db2e2aaa90/papers/SM.md);
  `Sub` = [`papers/Substratum.md`](https://github.com/amaybaum/incompleteness/blob/9c201475ba6fd8f341591d14dd8e88db2e2aaa90/papers/Substratum.md).
- `B1` = [Gate B1, `two-mode-drive.md`](https://github.com/amaybaum/incompleteness/blob/9c201475ba6fd8f341591d14dd8e88db2e2aaa90/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-mode-drive.md);
  `GA` = [Gate A, `endpoints.md`](https://github.com/amaybaum/incompleteness/blob/9c201475ba6fd8f341591d14dd8e88db2e2aaa90/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md).
- `AP1` = [Apparatus-1 `DESIGN.md`](https://github.com/amaybaum/incompleteness/blob/9c201475ba6fd8f341591d14dd8e88db2e2aaa90/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md);
  `M2D` = [MECH-2 `DESIGN.md`](https://github.com/amaybaum/incompleteness/blob/9c201475ba6fd8f341591d14dd8e88db2e2aaa90/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md).
- `HB` = [hydrodynamics round H-B `result.md`](https://github.com/amaybaum/incompleteness/blob/9c201475ba6fd8f341591d14dd8e88db2e2aaa90/verification/programmes/hydrodynamics/round-h-b-reversible-fluid-substratum/result.md);
  `CPP` = [CP-PREP-1 `SELECTION.md`](https://github.com/amaybaum/incompleteness/blob/9c201475ba6fd8f341591d14dd8e88db2e2aaa90/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md).
- Lean identifiers under `verification/lean-mathlib/OIBridge/` at the same commit:
  - `substratumGen_not_control` (StructuralClosure.lean:348);
  - `permTheory_not_control` (SubstratumInterfaceAudit.lean:708);
  - `exists_perm_extending` (Equivalence.lean:60);
  - `nonnegBounded_not_denseUnitaryControl` (FrozenSourcing.lean:173), used in S-NODENSE (§2.5).

  No `readWriteSourced_*` identifier is cited (#1188: `ReadWriteSourced` is vacuous).

**The Stage 0 map.** The map is at
[#1169 c.6719708521](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6719708521). It was reviewed at
[c.6719720616](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6719720616) and confirmed at
c.6719723538, so its standing line "pending" is stale. It was written against `f88c1842`. Between `f88c1842` and
`9c201475` none of the following changed:

- `papers/`;
- `oi-qm-ext-1/`, `apparatus-1-20261107/` and `mechanism-2-20261108/`;
- `StructuralClosure.lean` and `Equivalence.lean`.

Its line numbers therefore carry over unchanged.

## 0. Summary of what is frozen

| Item | Frozen choice |
| --- | --- |
| Carrier | **Finite.** One isolated pair of modes over `Z_q`, `q = 2^m`, with one-step memory, a finite controller and one fresh record cell (§1.1). No continuum carrier is used or assumed, and none is taken as a limit object |
| Rule | SM's second-order form with a center-free symmetric two-site coupling. The coefficient is applied by rounding half away from zero (§1.2). By construction the rule has three exact symmetries of a pair of identical coupled oscillators: exchange, parity and time reversal (§1.3) |
| Families | F-NAT is one coefficient applied for a duration; it is motivated by the oscillator physics. F-B1 is B1's compensated word and setting schedule; it is target-defined and used for comparison only (§2.1) |
| Horizons | H1 is one 24-step program (finite-accuracy tracking). H2 is up to `N_q = q/2^{10}` steps of one primitive (long-horizon invariant), §2.2 |
| Tested object | Classical configuration tracking at H1, and drift of the pair's continuum invariant at H2. Neither is state mixing on an operational carrier (§0.1) |
| Discriminating test | S-LH at H2 (§2.4). The mechanism-off control, a generic reversible-discretization countercontrol (GC) and a first-order generic scheme (MO-3) can each fail the success criterion (§6.2–§6.3) |
| Pre-named outcomes | `NO-OPERATIONAL-QUESTION` (§0.1) and `BLOCKED-QB` (§3.2) |
| Overall verdict categories | `NEW-POSITIVE`, `NEW-NEGATIVE`, `COVERED-BY-EXISTING-RESULTS`, `NEGATIVE-H1`, `INCONCLUSIVE`, `VOID` (§5.2) |
| Stage 0 rows | Row 7 (relating evolution / lift). The mixing part of §5's "(iv) / reversible control (9, 13)" entry, in the comparison only (§1.5) |
| Motivation class | **Mixed.** The rule, its symmetries and F-NAT are the independent component; F-B1 is target-defined (§3.4). A positive is recorded (b) |
| Ceiling | A fixed-horizon success alone is capped at L1. L3 is unreachable as frozen (§8) |

### 0.1 What P-MIX can establish beyond Main:566/598 and the conditional B1 mixer

**What is already established.**
- Main:566 (finite operational realization and gluing, ε-form) and Main:598 (uniform continuum realization) construct,
  for each fixed horizon, finite reversible realizations approximating any finite quantum instrument family to any
  finite accuracy. Any finite set of mixing operations is such a family. Those realizations are built from the target
  family and from the horizon: a density register, preloaded seeds, and one step map per instrument.
- B1 gives an exact continuum mixer, conditional on real modes (E-real) and exact real coefficients (E-control). Both
  are unsourced (B1 §8).
- On a finite carrier, no exact continuously tunable family exists (AP1:955–977 for `rot`; S-FIN here).

**Level 1: operational.** This design supplies no step that turns configuration-level statements into state mixing on
an operational carrier:
- B1's amplitude dictionary `z = x + iy` does not factor through the standard density matrix (B1 §6, lines 124–140);
- a fixed nonnegative-bounded identification excludes dense unitary control (S-NODENSE);
- a derived probability law for reads belongs to Q-B (inactive) or #1059, and none is posited here.

Supplying that step would need three things this design does not supply:
- a physically specified identification of configurations, or of their laws, with operational states and effects;
- read laws derived under that identification;
- validity and composability of the full instrument under it (c.6720678942, refinement 2).

**Preregistered:** at the operational level, P-MIX in this design poses no question beyond Main:566/598. The outcome is
**`NO-OPERATIONAL-QUESTION`**. This is a scope finding about this design. It is not a theorem about every finite design.

**Level 2: configuration, fixed horizon (H1).** At H1, P-MIX asks whether a fixed local rule tracks the exact continuum
exchange family uniformly in the setting. Here the H1 statements may follow from generic error propagation, using only
four facts:
- any second-order form is bijective (SM:106);
- rounding error is "at most 1/3 per site and step" away from alphabet-boundary crossings (SM:298);
- the comparator is a fixed-length product of bounded maps;
- coefficient resolution grows with `q`.

If so, an H1 success is covered by existing mathematics. The frozen genericity clause G-GEN (§8.2) decides this. An H1
success alone never counts as evidence of a hard-to-vary principle (owner requirement).

**Level 3: configuration, long horizon (H2). This is the question that survives.**

> **Q-LH.** Does a fixed finite rule with the exact exchange, parity and time-reversal symmetries of a pair of
> identical, symmetrically coupled oscillators keep the pair's continuum invariant to vanishing relative error over
> horizons growing with the amplitude scale, uniformly in the coupling? And does a generic reversible discretization of
> the same continuum dynamics, lacking those symmetries, fail to do so?

Q-LH is new relative to Main:566/598 and to B1, for three reasons:

- Main's realizations are built for one horizon at a time, from the target. Q-LH asks about one rule whose horizon
  grows with `q`.
- B1 is exact and continuum. Q-LH concerns a finite rule with no real resource.
- At H2, the generic error-propagation argument gives no vanishing bound. Over `N_q ∝ A_q` steps it allows a
  relative drift of order one. A pass at H2 is therefore not a rounding-error bound.

**Relevance limits, stated now.**

- Q-LH is a classical question about configuration dynamics. A positive answer would show that a fixed finite rule can
  supply a repeatable, non-drifting reversible two-mode exchange at the configuration level. It would not touch the
  operational level, which stays `NO-OPERATIONAL-QUESTION`.
- Q-LH is close to an existing open mathematical problem. Q-RED (§4) asks whether the rule's symmetric and
  antisymmetric sectors reduce exactly to single-mode rounded maps. Their long-time boundedness is studied in the
  discretized-rotation literature and is open in general [unverified beyond bibliographic records; K-1 row].
  - If Stage 1B shows the reduction, the sector part of Q-LH is an instance of that problem.
  - Then only configurations outside those sectors, which include the mode-1 initial conditions of a transfer, carry
    anything new.
- Whether Q-LH counts as a P-MIX question at all is for the owner to judge.
  - If the owner rules that it does not, the portfolio entry for P-MIX is `NO-OPERATIONAL-QUESTION`, together with
    `BLOCKED-QB` for the continuum branch and the H1 verdict.
  - The H1 verdict is then `COVERED-BY-EXISTING-RESULTS` if G-GEN applies.
  - The owner has stated that this is a valid outcome.

## 1. Construction

### 1.1 Carrier, stated explicitly as finite

- **Modes.** `x = (x_1, x_2) ∈ Z_q²` (current) and `y = (y_1, y_2) ∈ Z_q²` (previous), with `q = 2^m`, `m ≥ 1`. Each
  member of the family is a finite carrier. Claims are statements about the family, with explicit `q`-dependent bounds.
  No member is identified with a real or complex space.
- **Controller.** B1 §5's controller, with the real coefficient interval replaced by a finite set:
  - a program register of 24 coefficients in `K_q = { j / 2^{r} : j ∈ Z, |j| ≤ 2^{r} }`, where `r = r(m) = ⌊m/2⌋`;
  - a clock `ℓ ∈ Z_64`;
  - a fresh ready bit `ρ_0 = 0`.
- **Centered representatives.** For `t ∈ Z_q`, `t̃` denotes its representative in `(−q/2, q/2]`.

**Choice of `q`.**
- `q = 2` has too few values to carry any approximation. At `m = 1`, `r = 0` and `K_2 = {0, ±1}`, so the rule is the
  linear modular rule of class N.
- MECH-2 Theorem U2 governs that instance only under its own hypotheses: the R1^⊗2 frame identification of laws, Lemma
  F's operation set, and H-LIFT (M2D:315–325, 404–412). This design adopts none of them (P-U2, §6.1).
- As refinement 2 states, U2 does not exclude every finite-order non-Clifford operation in a different extension.
- Odd moduli appear only in robustness item RB-4, and every statement about them is conditional on #1193.
- `q = 2^m` matches SM §4.2's rounded-rule record (`q = 2^16`, SM:294).

### 1.2 Microscopic rule

Rounding half away from zero, on a rational `t`: `ρ(t) = sgn(t)·⌊|t| + 1/2⌋`. For `k = j/2^r ∈ K_q`:

```text
f_k(x) = ( ρ(k·x̃_2) , ρ(k·x̃_1) )  mod q          (integer arithmetic on j·x̃_i and 2^r)
S_k : (x, y) ↦ ( f_k(x) − y ,  x )                (SM's second-order form, SM:106)
```

Each mode reads only the other mode, with one rounded multiplication per slot. The primitive steps of a program are
these maps `S_k`.

The world update at clock `ℓ` follows B1 §5's schedule, unchanged:
- for `ℓ ∈ {0,…,23}`, apply `S_{k_ℓ}`;
- at `ℓ = 24`, apply the copy `ρ_0 ↦ ρ_0 ⊕ 1[x̃_1 > 0]`;
- for `ℓ ∈ {25,…,63}`, apply the identity;
- then advance the clock, `ℓ ↦ ℓ + 1 mod 64`.

**Inherited, not derived here.** Stage 1B re-checks the following as control C-BIJ:
- every `S_k` is a bijection, with inverse `(u, v) ↦ (v, f_k(v) − u)` (SM:106; B1:45);
- the copy is an involution;
- the world update is a bijection (B1 §5's argument).

The rounding convention differs from r1, which used half-up rounding. Half-up rounding is now variation V-P.

### 1.3 The exact symmetries (design properties; checked by control C-SYM)

Let `X` exchange the two slots of `x` and of `y` together, `P(x, y) = (−x, −y)`, and `R(x, y) = (y, x)`. By
construction the design has three properties:

- **exchange covariance:** `S_k ∘ X = X ∘ S_k`, because both slots use the same rounding;
- **parity covariance:** `S_k ∘ P = P ∘ S_k` on every configuration with no coordinate equal to `q/2`, because `ρ`
  is odd. The value `q/2` is its own negative in `Z_q`, and every window of §2.2 excludes it;
- **time reversal:** `R ∘ S_k ∘ R = S_k^{-1}`, because of the second-order form (cf. SM:1227).

Exchange covariance and time reversal hold at every `q` on the whole carrier, exactly. Parity covariance holds exactly
off the single coordinate value `q/2`. They are properties of the construction, not results, and their
presence is not evidence (§8.2). The discriminating content lies in whether they matter for S-LH (§2.4, §8.2).

### 1.4 Observer access, preparations, records, encoded description

- **Read.** The only read is the sign record `1[x̃_1 > 0]`. It is copied at `ℓ = 24` into the fresh cell, and read
  passively for `ℓ ∈ {25,…,63}` (B1 §6). It is a deterministic predicate. No sampling rule, re-preparation law or
  outcome-probability rule is posited.
- **Preparations.** Point preparations (Pp). (Pw): `μ_W`, uniform on a declared window of §2.2, with `ℓ = 0` and
  `ρ_0 = 0`. This is the maximal-entropy default (Main:56, 60; posit (iv)). It is used only to weight record
  disagreements in S-REC.
- **Setting independence.** The prepared law is fixed before `ℓ = 0`, independently of the program. Only the current
  instruction is read (GA:90–92; B1 §5).
- **Encoded description.** The rescaling `(x̃, ỹ) / A_q ∈ R⁴`.
  - It is an injective point map of configurations into `R⁴`.
  - It is not a frame identification of laws into an operator space: it assigns no operator to any law and no
    probability to any event.
  - It is used only to state §2's approximation.
  - Neither the setting intervals nor `R⁴` is a carrier or state space of the model (G-QB5).

### 1.5 Stage 0 rows targeted

- **Row 7** (unitary representation; relating evolution; lift freedom).
  - Column (c): "Relating evolution (Main:646)".
  - Column (d): "None: Main:646 'neither supplies one nor says what form one must take'".
  - P-MIX asks whether a specified finite carrier and rule fix the transformation relating two times of the pair, by
    the program executed between them, rather than by a choice of lift.
- **Stage 0 §5, entry "(iv) / reversible control (9, 13)"**, mixing part only: "a continuously tunable mixing operation
  (Main:590): assumed and target-adjacent … No independent candidate."
  - This entry is addressed only in the §7 comparison, at the level fixed by §0.1.
  - Its access and intervention part belongs to P-CONTROL.
- **Row 15** (hidden dynamics; mixing hypothesis; SM §4.2's rounded rule) is touched by Q-LH and by DC-1. It is not
  targeted for selection.

### 1.6 Source ledger

| Resource | Content | Class | Source / note |
| --- | --- | --- | --- |
| Finite alphabet `Z_q` | Configuration values | native | A1 (Sub:92), a posit. `q = 2^m` is a parameter choice |
| Second-order form | `x(t+1) = f(x(t)) − x(t−1)` | native | SM:106; A2 (Sub:94), a posit |
| Center-free symmetric coupling | Each mode reads only the other mode, with the same coefficient both ways | native (posit) | A4 (Sub:98). The warrant for its no-self-term clause is open (Stage 0 row 9) |
| Odd rounding `ρ` | Half-away-from-zero rounding of a dyadic multiple | supplied | A proposed rule component. SM §4.2 (SM:294, 298) records a rounded rule of the same type, which is not adopted. A5 fails for it |
| Coefficient set `K_q`, `r(m)` | Finite dyadic coefficients | supplied | Replaces B1's E-control. Loading is not sourced (CTL; CPP) |
| Isolated pair | Omitted modes are spectators | supplied | B1's E-pair. RT-3 tests a ring without it |
| Clock and schedule | `Z_64` clock; 24-step program; copy at step 24 | supplied | B1 §5. Stage 0 row 5: no clock source passes CTL's gate |
| Fresh record cell | `ρ_0 = 0` | supplied | Ready-cell supply is open (#1147) |
| Sign read | `1[x̃_1 > 0]`, copied by an involution | supplied (access); native (map form) | B1's E-read |
| Preparations | Point preparations; uniform on a window | supplied (preparation); native posit (law) | Main:56, 60 |
| Representatives, windows, scales | Scope of the claims | representation | They act on no configuration |
| Continuum comparators and invariants | Real-linear maps of §2.1; `E_s` of §2.4 | imported (comparison object only) | B1 §3–§4; SM:296's conserved form |

No supplied entry may be counted as physically generated (owner boundary, c.6720450946).

## 2. Families, horizons, comparators and criteria (fixed in advance)

### 2.1 Comparators and families

- **Continuum primitive.** `T_s(x, y) = (sXx − y, x)` on `R⁴`, for real `s` (B1:36–45). `T[w]` and `Φ_q[w]` are the
  composed continuum and finite maps of a word `w`, applied right to left.
- **Coefficient quantizer.** `κ_q(t)` is the element of `K_q` nearest to the real number `t`, with ties toward 0.
- **F-NAT (oscillator physics).**
  - Setting `s ∈ [−1, 1]`.
  - H1 program: `n_q(s) = (κ_q(s))^{24}`, the same coefficient for all 24 steps.
  - Exact comparator: `E_NAT(s) = T_s^{24}`, with `s` unquantized.
  - The duration 24 matches F-B1 for comparison. It is a representation choice.
- **F-B1 (target-inspired construction; comparison only).**
  - Setting `θ ∈ [−π, π]`.
  - B1 §4's word: `Q_a = T_a T_0³`, `P_b = T_0 T_{−b} T_0²`, `C(a,b) = Q_a P_b Q_a`.
  - Program: `w_q(θ) = C(a_q, κ_q(b(a_q)))²`, where `a(θ) = −tan(θ/4)`, `a_q = κ_q(a(θ))` and `b(a) = −2a/(1+a²)`.
  - Exact comparator: `E_B1(θ) = T[C(a(θ), b(a(θ)))²]`, with unquantized coefficients (B1:89, 108–111).
  - F-B1 enters H1 only. It plays no part in Q-LH, S-LH, the variations or the ladder above L0.

### 2.2 Horizons, windows and the approximation notion

- **H1 (finite-accuracy horizon).** One 24-step program.
  - Window `W_q`: all coordinates satisfy `|t̃| ≤ A_q = q/2^8`.
  - Composition window `W_q^{(2)}`: `A_q / 2`.
- **H2 (long horizon).** Up to `N_q = q/2^{10}` consecutive applications of one primitive `S_k`, with `k ∈ K_q`.
  - Window `W_q^{LH}`: all coordinates satisfy `|t̃| ≤ A′_q = q/2^{10}`.
  - So `N_q = A′_q`: the horizon grows in proportion to the amplitude scale.
- **Error.** `δ_q[Φ, E; W] = max_{z ∈ W} ‖ (Φ z)~ − E z̃ ‖_∞ / A_q`, where `(·)~` takes centered representatives.

These are the only approximation notions. They are uniform (worst-case) statements, not averages. Changing them after
any result is evaluated voids the round.

### 2.3 H1 criteria, for each family F ∈ {NAT, B1}

`P_F(σ)` is the program of setting `σ`; `E_F(σ)` is its exact comparator. "Explicit" means a bound on paper in terms
of `q`, the word length and `r(m)`. A bound valid only for some settings, or only on a window shrinking faster than
`A_q`, does not count.

- **S-BIJ.** Every program is a bijection of the finite world (control C-BIJ).
- **S-TRACK_F (recorded; never sufficient).** An explicit `B_0(q) → 0` with
  `sup_σ δ_q[Φ_q[P_F(σ)], T[P_F(σ)]; W_q] ≤ B_0(q)`. The comparator uses the quantized coefficients, so this measures
  rounding error only.
- **S-TUNE_F.** An explicit `B(q) → 0` with `sup_σ δ_q[Φ_q[P_F(σ)], E_F(σ); W_q] ≤ B(q)`. The comparator is the exact
  family, so this measures rounding and coefficient resolution together.
- **S-INV_F.**
  - F-B1: `sup_θ δ_q[Φ_q[w_q(−θ)] Φ_q[w_q(θ)], id; W_q] → 0`, with an explicit bound.
  - F-NAT: Stage 1B either gives a rule `s ↦ (α, s′, β)`, with `α, β ∈ {0,…,3}` and `s′ ∈ [−1, 1]`, such that
    `sup_s δ_q[Φ_q[(0)^α n_q(s′) (0)^β] Φ_q[n_q(s)], id; W_q^{(2)}] → 0` with an explicit bound; or it shows that no
    such rule exists in that frozen word set. `(0)^α` is `α` zero-coupling steps.
  - The inverse is always a forward program. No time reversal is used.
- **S-COMP_B1 (F-B1 only).** `sup_{θ,φ} δ_q[Φ_q[w_q(θ)] Φ_q[w_q(φ)], E_B1(θ+φ); W_q^{(2)}] → 0`, with an explicit
  bound.
- **S-REC_F.** An explicit `B_4(q) → 0` that bounds, uniformly in `σ`, the `μ_W`-mass of configurations in `W_q` whose
  sign record after `P_F(σ)` differs from the sign of the first coordinate of `E_F(σ) z̃`.
- **CT_F (property of the exact comparator).** Let `τ_F(σ; z)` be the mode-2 share `(u_2² + v_2²)/(|u|² + |v|²)` of
  `(u, v) = E_F(σ) z`, for unit `z` in the mode-1 sector `{x_2 = y_2 = 0}`. CT_F holds iff both of the following hold:
  - for every `t ∈ [0, 1]`, some setting and some such `z` give `τ_F = t`;
  - every `E_F(σ)` is invertible.

  For F-B1, CT holds by B1 §4; this is recorded, not re-derived.

### 2.4 H2 criterion: the discriminating test S-LH

- **Continuum invariant.** For real `s`, define `E_s(x, y) = |x|² + |y|² − s·x·(Xy)`. This is SM:296's conserved form
  `u·u + v·v − u·Av`, with `A = sX`. It is invariant under `T_s`. For `|s| ≤ 1` it satisfies
  `E_s ≥ (1 − |s|/2)(|x|² + |y|²)`.
- **S-LH (for a rule `Ψ_k` with continuum primitive `T_k` and invariant `E_k`).** Stage 1B gives an explicit
  `B_LH(q) → 0` such that

  ```text
  sup_{k ∈ K_q, |k| ≤ 1}  sup_{z ∈ W_q^{LH}}  sup_{0 ≤ n ≤ N_q}  | E_k(Ψ_k^n z̃) − E_k(z̃) | / (A′_q)²  ≤  B_LH(q),
  ```

  with `Ψ_k^n z̃` computed on centered representatives at each step, and no alphabet-boundary crossing on the way.
  Otherwise S-LH fails (a proof that no such bound exists), or is undecided.
- S-LH concerns the invariant, not configuration tracking, at H2. The invariant is the quantity a reversible
  integration scheme is designed to keep (Levesque & Verlet 1993; [unverified] the backward-error literature on
  reversible integrators). Configuration phase at H2 is not required.
- S-LH is evaluated for the design (`Ψ_k = S_k`), for each variant of §8.2, for GC (§6.3), for MO-3 against its own
  invariant (§6.3) and for MO-1 (§6.2).

### 2.5 Standing scope facts (recorded; not controls; outside the VOID rule)

- **S-FIN.** At each `q`, the available programs generate a finite permutation group, and every program has finite
  order. The setting maps take at most `|K_q|` (F-NAT) or `|K_q|²` (F-B1) values, so "uniformly in the setting" ranges
  over finitely many finite maps at each `q`.
- **S-NOEXACT.** No outcome is phrased as exact (iv) (Main:590; `substratumGen_not_control`) or as an exactly induced
  `rot` (AP1:955–977).
- **S-NOTNEW.** H1 approximate realizability is not presented as new (Main:566, 598).
- **S-NODENSE.** No outcome is read as approximate or dense encoded unitary control on any fixed nonnegative
  identification (`nonnegBounded_not_denseUnitaryControl`; AP1:186–192). The design adopts no frame identification of
  laws.
- **S-CLASSICAL.** The finite carrier, with its laws and its deterministic rule, is a classical ontological model of
  every statistic the design produces. The record laws are pushforwards by definition.
- **S-NOINACC.** The design posits no inaccessible functional and no P1/P2 registration. If Stage 1B needs such a
  functional, the design stops as `INCONCLUSIVE` and names the need.

## 3. Independent physical motivation

### 3.1 Candidates considered (owner distinction (b)): search record

**Search scope.** The corpus was searched at `main@9c201475` (papers, book and verification records) for: reversible,
second-order, rounded, floor, lattice gas, billiard, Margolus, Fredkin, Toffoli, symplectic, cat map, beat, discretized
rotation, quantum walk and quantum cellular. The literature searched is listed per row. A reason marked **[unverified]**
is stated from memory or from an abstract. It is not a finding and decides nothing beyond what it states.

| # | Candidate | Carrier | Source (reading status) | Decision | Reason |
| --- | --- | --- | --- | --- | --- |
| K-1 | Finite-precision reversible two-mode exchange (this design) | finite | SM:106, 294–298; B1 §3–§4; Levesque & Verlet, *J. Stat. Phys.* 72, 519 (1993) (bibliographic record and abstract-level descriptions); Lowenstein, Hatjispyros & Vivaldi, *Chaos* 7, 49 (1997); Akiyama, Brunotte, Pethő & Steiner, arXiv:0704.3674; Akiyama & Pethő, arXiv:1206.3868 (bibliographic records and abstracts only) | **selected** | A finite carrier; a fixed local reversible rule carrying the exact symmetries of a coupled pair; a transfer between two distinguishable modes. It replaces B1's unsourced E-real and E-control with finite resources |
| K-2 | Single-mode discretized rotation `(x, y) ↦ (ρ(λx) − y, x)` | finite | Same literature as K-1 | rejected as a candidate; used in Q-RED (§4) | A one-mode family is a phase-type operation, which is already a stated intervention (Main:590), not a two-mode transfer |
| K-3 | Linear modular rule with integer coefficients (class N) | finite | SM:296, 298; AP1; M2D | rejected; **used as control MO-2** | SM:298: "reduction modulo `q` introduces no nonlinearity". Only `k ∈ {0, ±1}` act as real multiplication on rescaled coordinates |
| K-4 | Reversible lattice gases: HPP (*J. Math. Phys.* 14, 1746 (1973), from memory), FHP (PRL 56, 1505 (1986), cited in the corpus), HB's hexagonal gas | finite | HB; hydrodynamics `PROGRAMME.md`:49 | rejected | Collisions permute occupation configurations and have no tunable setting. [unverified] A coarse-grained relaxation is undone by a forward word only at recurrence times |
| K-5 | Billiard-ball and conservative-logic CA (Margolus, *Physica D* 10, 81 (1984); Toffoli & Margolus, *Physica D* 45, 229 (1990); Fredkin & Toffoli 1982, read in CPP) | finite | CPP §1 | rejected | Routing is a permutation of distinguishable states, so it is monomial (`permTheory_not_control`) |
| K-6 | Linear symplectic maps on a finite torus (cat-map type; Arnold & Avez 1968, from memory) | finite | — | rejected | Linear over `Z_N`, so K-3's reason applies. [unverified] Their association with stabilizer-type groups would make a selection target-adjacent |
| K-7 | State-dependent graphs `G_SM` and `G_σ` | finite (`q = 2`) | M2D; #1198 (provisional) | rejected | At `q = 2`, under R1⊗n, Lemma F's operations and H-LIFT, Theorem U2 excludes reversible escape. #1198 reports, provisionally, that `G_σ`'s protection fails within its scope |
| K-8 | Multi-cell finite encoding with a hidden parity (P-8 type) | finite | AP1 §5.2 | rejected | It is Q-A's object, not a tunable family |
| K-9 | B1 as stated | continuum | B1 | rejected; see §3.2 | E-real and E-control are the unsourced controls |
| K-10 | Classical spin on `S²`; the Kochen–Specker model | continuum | AP1 §5.3–§5.4 | rejected | It is Q-B's own first decisive check (AP1:1032, 1082) |
| K-11 | Classical oscillator amplitudes (Briggs & Eisfeld, PRA 85, 052111 (2012), cited by B1) | continuum | B1 §9 | rejected | Same as K-9 |
| K-12 | Quantum walks and quantum cellular automata (Aharonov, Davidovich & Zagury, PRA 48, 1687 (1993); Schumacher & Werner, arXiv:quant-ph/0405174), from memory | — | — | rejected | [unverified] Target-defined |
| K-13 | 't Hooft (Springer 2016); Elze, PRA 89, 012111 (2014), from memory | finite | — | rejected | [unverified] Target-defined: the stated aim is quantum mechanics |
| K-14 | Main's gluing and uniform continuum realizations (Main:566, 598) | finite | Main | rejected; **used as CC-TT** (§6.5) | Built from the target family and horizon (GA:92) |

Selection among candidates occurred. K-1 was chosen because it carries a tunable two-mode transfer on a finite carrier,
and because it can run B1's word. A positive is therefore recorded (b) at best.

### 3.2 The continuum branch and Q-B

A continuum design (K-9 to K-11) would posit real modes or a continuous phase space as physical. The exchange is then
an exact continuous family. Q-B asks "What additional OI principle could produce the continuous rotations" (AP1:1082),
and its first decisive check is a continuum carrier (AP1:1032). No reformulation was found that keeps the mixing and
stays outside Q-B. The continuum branch is therefore not executed, and its outcome is pre-named **`BLOCKED-QB`**.

Five guards keep the finite design clear of Q-B:

- **G-QB1.** No claim concerns a limit object of `{Z_{2^m}}`. A bound "→ 0" is a statement about a sequence of finite
  carriers.
- **G-QB2.** No read re-prepares from a law. The only read is a deterministic predicate.
- **G-QB3.** No cosine-weighted or other outcome-probability law is claimed, used or compared.
- **G-QB4.** No carrier whose representable laws contain a ball, a sphere or any continuum is introduced.
- **G-QB5.** The setting intervals, `R⁴` and the invariant `E_s` are never a carrier or state space of the model.
  They index programs and state the approximation.

### 3.3 Motivation, written without reference to the target

**The physics.** Two identical oscillators with a symmetric coupling exchange energy periodically. With all energy
initially in one oscillator, the energy passes to the other and back, at a rate set by the coupling strength
(small-oscillation theory, e.g. Goldstein, Poole & Safko, *Classical Mechanics*, 3rd ed., ch. 6, from memory). Such a
pair has three exact symmetries:

- relabelling the two identical oscillators;
- reflecting every displacement in a symmetric potential;
- reversing the direction of time in its microscopic dynamics.

It also conserves a quadratic energy.

**Finite precision.** A physical register with finitely many values cannot hold a real coupling coefficient. A
finite-state version must replace multiplication by a real number with an operation on integers. Exactly reversible
integer discretizations of Hamiltonian dynamics were introduced for this purpose (Levesque & Verlet 1993). The
second-order form makes any integer update reversible and keeps the time-reversal symmetry (SM:106). Rounding half
away from zero keeps the reflection symmetry, and using the same rounding in both slots keeps the relabelling
symmetry. SM §4.2 already uses a rounded integer coefficient in the same form, for an unrelated reason: breaking the
integrability of the linear rule (SM:294).

**The family.** The family this motivation offers is a fixed coupling applied for a duration, tuned by its strength
(F-NAT).

**The question.** Does such a pair, given finite precision but keeping its exact symmetries, keep its energy over long
times, and do the symmetries matter for that?

### 3.4 Classification (Q3's standard)

**Source of the classes.** The classes are those of A5-Q3's amendment A1 §3, criterion C2 (PR #1202, off main). They
are restated here, and each assumption is judged on its own.

**The target.** The target `T` is completion condition (iv) in mixing form: an exact, continuously tunable state-mixing
operation on the operational carrier (Main:590). `T` implies the failure of C-ROT (AP1:188). The converse does not hold:
`rot` alone gives density, not exact continuous tunability (AP1:28, 188–192).

**The classes.**

- **independent:** the motivation does not presuppose `T` and is not designed to exclude a particular construction;
- **target-adjacent:** the motivation presupposes `T`, is equivalent to it on the class, or is supported only by a
  consequence of it;
- **target-defined:** the stated reason is to obtain `T`, or to exclude a particular construction;
- **mixed:** each component is identified;
- **none found**.

| Component | Class | Basis |
| --- | --- | --- |
| Energy exchange of two coupled oscillators | independent | Classical mechanics. It motivates the rule `S_k` and F-NAT |
| Exchange, reflection and time-reversal symmetries of the pair | independent | Symmetries of identical oscillators in a symmetric potential, and microscopic reversibility of mechanics |
| F-NAT's form (one coupling, a duration, tuned by strength) | independent | §3.3. The duration 24 is a representation choice |
| Center-free symmetric coupling | independent in its translation clause; open in its no-self-term clause | A4 (Sub:98); Stage 0 row 9 |
| Second-order reversible form | mixed | A2's motivation is mixed (Main:62, 66; Stage 0 row 4). The time-reversal component is independent |
| Finite alphabet | target-adjacent in part | A1 via E3 (Sub:80, 92) |
| Rounding | mixed | Its independent uses are Levesque–Verlet and SM §4.2. Here it is also chosen because it lets a finite rule follow the continuum exchange, which is adjacent to `T` |
| B1's word `C(a,b)²` and the schedule `θ ↦ (a(θ), b(a(θ)))` (F-B1) | **target-defined** | B1:7: to "supply a continuously driven mixing transition". B1:89: the compensation is fixed by "Requiring this endpoint to commute with the fixed quarter-turn J", so that the endpoint is `U(a)` (B1:103–111). The schedule exists to make the word `exp(iθX)` |
| Selection of K-1 | target-defined insofar as it was made to carry F-B1; target-adjacent insofar as it was made to carry a two-mode transfer | §3.1 |

**Overall: mixed.**

- Independent component: the rule `S_k`, its three symmetries, and F-NAT. These carry Q-LH.
- Target-defined component: F-B1, which is retained for H1 comparison only.
- Target-adjacent components: finiteness via E3, the role of rounding, and the selection.

## 4. Mathematical consequences to be derived in Stage 1B (questions only)

If Stage 1B is authorized, it works on paper, in this order:

1. The controls C-BIJ and C-SYM (§6.1).
2. **H1.** The H1 criteria for F-NAT and then F-B1 (§2.3), including the alphabet-boundary question on `W_q` and
   `W_q^{(2)}`. A crossing on the window is a failure of the affected criterion, never a reason to change the window.
   This needs a uniform bound on partial products with margin `2^7`; a crude per-step norm bound does not supply that
   margin. Then G-GEN at H1 (§8.2).
3. **H2.** S-LH for the design, GC, MO-3, MO-1 and each variant of §8.2.
4. **Q-RED.**
   - Q-RED asks whether the symmetric sector `{x_1 = x_2, y_1 = y_2}` and the antisymmetric sector
     `{x_1 = −x_2, y_1 = −y_2}` are invariant under `S_k`, and whether on each sector `S_k` reduces exactly to a
     single-mode rounded map `(x, y) ↦ (ρ(±k x) − y, x)`.
   - If they reduce, Stage 1B lists which published results on such maps (K-1 row) apply at the same coefficient and
     rounding convention, and records the sector part of S-LH as an instance of them, or as an instance of an open
     problem.
5. The controls of §6 and the reach test of §8.3.
6. Only then, the §7 comparison.

**Paper-undecidable items (frozen).** Any criterion, control, variation or reach test that cannot be decided on paper
is recorded as `INCONCLUSIVE`, with its gap named. A later authorization of computation cannot change §2, §5, §6 or §8.
A result obtained under such an authorization is reported against these criteria as written.

**DC-1 (derivation constraint).** No Stage 1B derivation may assume any of the following properties of a rounded rule,
because SM:294–298 records them as unestablished or contrary:

- exact energy conservation;
- integrability;
- cycle ergodicity;
- absence of boundary-crossing jumps outside the window.

A derivation that uses one of these is invalid (control P-SM).

## 5. Outcomes and decision rules (fixed in advance)

### 5.1 Per-horizon outcome categories

**The VOID gate.** A control of §6 is red or vacuous. "Vacuous" means that its pass condition holds for every possible
Stage 1B derivation. The facts of §2.5 are outside this rule. When the gate is met, no other outcome is rendered.

**H1, for each family F.**

| Outcome | Rule |
| --- | --- |
| `H1-POSITIVE_F` | S-BIJ, S-TUNE_F, S-INV_F, S-REC_F and CT_F hold, with explicit bounds tending to 0. For F-B1, S-COMP_B1 also holds |
| `H1-PARTIAL_F` | S-BIJ, S-TUNE_F and CT_F hold, and another H1 criterion fails, holds only with a non-vanishing bound, or holds only on a subset of settings. A rule with a setting-independent finite coefficient alphabet cannot reach it: MO-2 fails S-TUNE when green |
| `H1-NEGATIVE_F` | S-TUNE_F fails, CT_F fails, or S-BIJ fails |
| `H1-INCONCLUSIVE_F` | A criterion is undecided on paper. The gap is named |
| Genericity tag | An `H1-POSITIVE` or `H1-PARTIAL` carries **`generic`** if G-GEN applies (§8.2) |

**H2, for the design.**

| Outcome | Rule |
| --- | --- |
| `LH-NEGATIVE` | S-LH fails for the design |
| `LH-COVERED` | Not `LH-NEGATIVE`. S-LH holds for the design, and the pass is an instance of a published theorem (Q-RED and the K-1 literature, checked per §4 item 4) |
| `LH-GENERIC` | None of the above. S-LH holds for the design, and also for GC or for MO-3 |
| `LH-DISCRIMINATING` | None of the above. S-LH holds for the design, and it fails for both GC and MO-3 |
| `LH-INCONCLUSIVE` | Every other case: S-LH is undecided on paper for the design, for GC or for MO-3. The gap is named, for example reduction to an open problem |

The rows are applied in the order listed; the first row that matches decides.

### 5.2 Overall configuration-level verdict (F-NAT)

| Verdict | Rule |
| --- | --- |
| `VOID` | The VOID gate is met |
| `NEW-POSITIVE` | `H1-POSITIVE_NAT` (or `H1-PARTIAL_NAT`) and `LH-DISCRIMINATING` |
| `NEW-NEGATIVE` | `LH-NEGATIVE`, whatever the H1 outcome. Q-LH is answered no |
| `COVERED-BY-EXISTING-RESULTS` | An H1 positive tagged `generic`, and `LH-GENERIC` or `LH-COVERED` |
| `NEGATIVE-H1` | `H1-NEGATIVE_NAT` and `LH-NEGATIVE` not established |
| `INCONCLUSIVE` | Every other combination, with each undecided item named. This includes an H1 positive with `LH-INCONCLUSIVE`, and an untagged (non-generic) H1 positive with `LH-GENERIC` or `LH-COVERED`; in the latter case the non-generic H1 result is named as the open item |

The rows are applied in the order listed; the first row that matches decides.

The two pre-named outcomes always accompany the verdict:

- `NO-OPERATIONAL-QUESTION` (§0.1);
- `BLOCKED-QB` (§3.2).

F-B1's H1 outcome is reported beside the verdict, marked target-defined. It never changes the verdict.

**Commitment to report.** Every outcome is reported in the portfolio record, whatever it is. Each report carries:

- the pre-named outcomes;
- both horizons' outcomes;
- the overall verdict;
- the three statuses of §5.3;
- the owner label of §5.4;
- the genericity tag, explanatory label and rung of §8.

### 5.3 The three statuses

- **Proposed.** At this freeze, the rule, its symmetries and F-NAT are proposed, subject to independent review, with
  motivation class mixed. F-B1 is not proposed: it is target-defined and retained for comparison.
- **Mathematically sufficient.** This status is recorded only for the criteria that hold, each named. It covers only the
  approximate configuration-level statements of §2.3–§2.4, under §1's hypotheses. It is never recorded at the
  operational level.
- **Derived from native OI.** This status is recorded only if every §1.6 ledger entry used by the positive is native.
  At this freeze the isolated pair, the rounding, the coefficient set, the clock, the record cell and the read access
  are all supplied.

### 5.4 Owner portfolio distinctions

- **(a)** Not available. The motivation is mixed, and selection among candidates occurred.
- **(b)** The label for any positive. It cites §3.1 and the choices in §8.2. An F-B1 positive is also marked
  target-defined.
- **(c)** No outcome statistics are claimed beyond deterministic record laws, which have a classical model
  (S-CLASSICAL). No outcome counts as evidence of nonclassical behaviour. Label (c) is attached if any later reading
  compares the record laws with a quantum law.

## 6. Controls

A verdict is rendered only over green controls. Each control below can be made red by a Stage 1B derivation.

### 6.1 Preserved-result and construction controls

| Id | What it checks | Green iff |
| --- | --- | --- |
| C-BIJ | SM:106; B1 §5 | The world update is shown to be a bijection |
| C-SYM | §1.3 | The design has the three exact symmetries, and each variant of §8.2 and GC breaks exactly the symmetries stated for it. Red if a stated symmetry fails, or if a variant breaks a different set |
| P-U2 | Theorem U2 (M2D:55–64, 404–412) within its hypotheses (M2D:315–325) | Stage 1B states which of U2's hypotheses this design lacks (the R1^⊗n frame identification of laws, Lemma F's operations, H-LIFT), and no §2 statement uses U2's conclusion. Red if a derivation invokes U2, or if the stated reason is false |
| P-B1 | B1's algebra and its density-dictionary obstruction (B1 §4, §6–§7) | The zero-coupling step `J = S_0` has `J⁴ = id`, and `J²` reverses every sign. So the sign-record distinction between `I` and `−I` is carried. Red if either check fails |
| P-SM | SM:294–298 | DC-1 is respected. Red if a derivation uses a DC-1 property |

C1–C4 are not evaluated. Main calls them "diagnostics of a realization rather than hypotheses" (Main:72). They are
defined at Main:74–80, and the theorem statement is at Main:82. Here the visible process (the record cell) is one bit
per clock cycle:

- over one cycle, the diagnostics are near-trivial;
- over many cycles, the configuration leaves `W_q`, which is SM:294–298's open territory and cannot be decided on paper.

No horizon gives them decidable content, so they are removed rather than kept as a control that cannot fail.

### 6.2 Mechanism-off controls

- **MO-1 (coupling off).**
  - Every setting's program is the all-zero program. The comparators remain `E_F(σ)`.
  - Green iff Stage 1B finds that S-TUNE_F fails for MO-1. If S-TUNE_F holds for it, the criterion is miscalibrated
    and the outcome is `VOID`.
  - MO-1's S-LH result is recorded. It concerns `E_0` only, so the success criterion fails for MO-1 through S-TUNE.
- **MO-2 (no fractional coefficients, no rounding).**
  - F-NAT's setting map, with `K_q` replaced by `{−1, 0, 1}` for every `q` (nearest element, ties toward 0). The rule
    is K-3's linear modular rule, and the comparator is `E_NAT(s)`.
  - Green iff Stage 1B finds that S-TUNE_NAT fails for MO-2. If it holds, the outcome is `VOID`.
  - S-TRACK may hold for MO-2. That is recorded.

### 6.3 Generic reversible-discretization countercontrols

These enter the verdict through §5.1. They can fail S-LH, and if they pass it the verdict is not `NEW-POSITIVE`.

- **GC (same continuum dynamics, no exact symmetry).**
  - Slot 1 uses the floor `⌊k·x̃_2⌋`; slot 2 uses the ceiling `⌈k·x̃_1⌉`. The rule is in second-order form, so it is
    bijective, and its continuum primitive `T_k` and invariant `E_k` are those of the design.
  - It breaks exchange covariance and parity covariance, and keeps time reversal.
  - Its per-step rounding error is bounded, so G-GEN's hypotheses (h1)–(h5) cover it at H1.
  - GC passes S-LH iff its own S-LH bound holds.
- **MO-3 (different form, no symmetric coupling).**
  - The first-order rounded shear pair on `x ∈ Z_q²`, with no memory: `x_1 ← x_1 + ρ(k x̃_2)`, then
    `x_2 ← x_2 − ρ(k x̃_1)`, using the updated `x_1`.
  - Its continuum primitive is `L_k = [[1, 0], [−k, 1]] [[1, k], [0, 1]]`.
  - It is judged against its own invariant, `Q_k(x) = x_1² − k x_1 x_2 + x_2²`, and against its own comparator
    `L_s^{24}` at H1.
  - Window: `|x̃_i| ≤ A_q` at H1 and `≤ A′_q` at H2.
  - It enters G-GEN at H1, and `LH-GENERIC` at H2.

### 6.4 Classical model and Theorem NC

- **The classical model.** S-CLASSICAL exhibits the carrier itself as a classical model. It is a standing fact and is
  not a control.
- **Why Theorem NC does not apply here.** NC (M2D:483–498; Lemma F's setting at M2D:315–325) assumes Lemma F's
  operation set, H-LIFT, and a linear identification of laws `μ ↦ Σ_λ μ(λ)A(λ)` by an orthogonal frame of unit-trace
  operators. It also assumes spanning reads, so that encoded and statistical equivalences coincide. Here:
  - the encoded description is an injective point map of configurations into `R⁴`, not a frame identification of laws
    into an operator space, so NC's identification hypothesis is absent;
  - the only read, one sign record, does not span.
- **MECH-2's consequence.** The consequence is "change identification or access, not only dynamics". It is not met in
  NC's sense: the design adopts no operational identification and claims no nonclassicality.
- **Refinement 2.** NC says nothing about states labelled non-stabilizer under other representations. This design
  asserts nothing of that kind.

### 6.5 Target-tuned countercontrols and the structural rule SR

**SR (frozen, decidable).** A construction satisfies SR iff all four clauses hold:

- **SR1.** Its primitives form one parametrized family `{S_k : k ∈ K}`, with `K` a finite set fixed independently of
  the settings.
- **SR2.** Each primitive updates each mode slot from exactly one other slot of the current configuration, by one
  rounded multiplication by `k`, followed by subtraction of that slot's previous value.
- **SR3.** Settings enter only through the choice of a word of fixed length 24 over the primitives.
- **SR4.** Nothing depends on a table indexed by setting, by word or by configuration.

The countercontrols:

- **CC-TT.** For each setting, a nearest-lattice-point permutation of the window toward `E_F(σ)`, completed by
  `exists_perm_extending` and loaded from a table (the K-14 pattern; GA:92). It fails SR1, SR2 and SR4.
- **CC-TT′.** The rounding of each whole 24-word continuum map, applied as one step. It fails SR2 and SR4.
- **The design.** F-NAT and F-B1 satisfy SR as constructions. F-B1's schedule is target-defined and recorded separately
  (§3.4).
- **GC.** GC satisfies SR1, SR3 and SR4. Under SR2, GC's mixed floor/ceiling is one rounded multiplication per slot, so
  GC satisfies SR. SR does not separate GC from the design; only S-LH and C-SYM do.

**Control.** Green iff Stage 1B, applying SR as written, reaches the classification stated above for CC-TT, CC-TT′,
F-NAT, F-B1 and GC. Red if SR admits CC-TT or CC-TT′, or excludes F-NAT; the outcome is then `VOID`.

### 6.6 Target-import check

| Criterion | Refers to | Allowed |
| --- | --- | --- |
| §2.3–§2.4 | Finite rules; real-linear comparators; the invariant `E_s`; window laws | Yes: classical objects only |
| §3.3 | Classical oscillators; symmetries; finite precision | Yes. The reviewer greps §3.3 for: quantum, unitary, Born, completely positive, CP, qubit, Hilbert, density, rotation, Bloch, Pauli. Any hit voids the freeze |
| §0.1, §3.4, §7 | `T`, C-ROT, (iv), `exp(iθX)` | Only to classify, to scope and to record outcomes |

### 6.7 Robustness and replication (required before any positive is promoted)

- **RB-1.** The decisive bounds are re-derived by a reviewer who did not write Stage 1B.
- **RB-2.** Windows `q/2^6` and `q/2^{12}` (H1) and `q/2^8` and `q/2^{12}` (H2), with the horizon `N_q` equal to the H2
  window scale. These are reported only. An item undecided on paper is `INCONCLUSIVE` (§4).
- **RB-3.** The S-LH verdict is repeated with coefficient resolution `r(m) = m`.
- **RB-4.** The S-LH verdict is repeated for `q = 3^m`, with `A′_q = ⌊q/2^{10}⌋` and `r = ⌊m·log₂3 / 2⌋`. This item is
  **conditional on #1193** (odd modulus).

A positive with any RB item not green stays "mathematically sufficient, unreplicated". It is not promoted as evidence
for a physical selection principle.

## 7. Comparison with the quantum-completion conditions (recorded only, after §4–§6)

- **Cmp-1 (F-B1).** Under B1's dictionary `z = x + iy`, `E_B1(θ)` acts as `exp(iθX)` (B1 §4). Record what F-B1's H1
  outcome implies: an approximate family in that representation, at the notion of §2.2 and nothing stronger.
- **Cmp-2 (F-NAT).** Record whether `E_NAT(s)` commutes with B1's `J` for any `s ≠ 0`, that is, whether F-NAT's
  comparator is complex-linear under B1's dictionary. B1:56–63 shows that a single nonzero primitive is not.
- **Cmp-3.** Record that C-ROT holds for every member of every family (S-FIN; AP1:955–977).
- **Cmp-4.** Record that condition (iv) is exact (Main:590), that this design does not supply it, and that the
  operational outcome is `NO-OPERATIONAL-QUESTION`.
- **Cmp-5.** In B1's density dictionary only, record B1 §6's `I` / `−I` sign-record distinction as carried (P-B1).

No §7 entry changes any outcome, status, label or rung.

## 8. Explanatory quality (AGENTS.md §A.29)

### 8.1 Preserved results

These results are preserved:

- the §6.1 controls: C-BIJ, C-SYM, P-U2, P-B1 and P-SM;
- the §2.5 facts: S-FIN, S-NOEXACT, S-NOTNEW, S-NODENSE, S-CLASSICAL and S-NOINACC.

M-INACC (#1198, provisional) is respected through S-NOINACC. No criterion uses M-INACC's content. A derivation that
contradicts a §6.1 result is a red control. If the contradiction is established as a finding against that result, the
finding needs its own review.

### 8.2 Genericity, and the variation analysis

**G-GEN (H1).** For each family, Stage 1B states whether its S-TUNE, S-INV and S-REC bounds follow from one lemma whose
only hypotheses are:

- (h1) a bijective update in second-order or first-order shear form;
- (h2) per-step rounding error bounded independently of `q`;
- (h3) no boundary crossing on the window;
- (h4) coefficient resolution tending to 0;
- (h5) a comparator that is a fixed-length product of real-linear maps, with norms bounded uniformly in the setting.

The success is tagged `generic` iff either of these holds:

- the lemma suffices;
- MO-3 satisfies the same H1 criteria against its own comparator.

A `generic` H1 success never counts toward hard-to-vary. With no discriminating H2 result, it is capped at L1, with the
label "poor explanation".

**What the variations test.** Variations are judged only at H2, never by H1 success. A rounding approximation therefore
never counts automatically toward hard-to-vary.

- **The consequence judged.** `C*` is: S-LH holds for the variant, against its own continuum primitive and its own
  invariant. Rounding variants share the design's `T_k` and `E_k`.
- **Easy and hard to vary.** An assumption is **hard to vary** iff the design satisfies S-LH and at least one listed
  variant of that assumption fails it (a proof that no vanishing bound exists). It is **easy to vary** iff every listed
  variant also satisfies S-LH. An undetermined case counts as neither.
- **Exclusions.** A variant that removes coefficient-resolution growth, or that changes the continuum invariant into
  one that is not conserved by its own continuum primitive, is a change of target. It is excluded from the count.

| Id | Assumption | Exact variant | Symmetries kept / broken | Status |
| --- | --- | --- | --- | --- |
| V-P | Odd rounding (reflection symmetry) | Half-up rounding `⌊t + 1/2⌋` in both slots | keeps exchange and time reversal; breaks parity | counted |
| V-X | Same rounding in both slots (exchange symmetry) | Slot 1 rounds half away from zero; slot 2 rounds half toward zero, `sgn(t)⌈|t| − 1/2⌉` | keeps parity and time reversal; breaks exchange | counted |
| V-PX = GC | Both | Slot 1 floor, slot 2 ceiling (§6.3) | keeps time reversal; breaks parity and exchange | counted (it is also the countercontrol) |
| V-S | No self-term (center-free) | `f(x)_i = ρ(k x̃_{3−i} + x̃_i/2)`, one rounding per slot. Its own primitive is `T′_k(x, y) = ((kX + I/2)x − y, x)`, with invariant `|x|² + |y|² − x·((kX + I/2)y)` | keeps all three; adds a self-term | counted |
| V-T | Second-order form (time reversal) | Replaced by MO-3, which is first-order and has no symmetric coupling | — | used in G-GEN and `LH-GENERIC`; not counted |
| V-A | Symmetric coupling coefficients | Coefficients `(k, 3k/2)`. The coupling matrix is not symmetric, so SM:296's conserved form does not apply | — | change of target; excluded |
| V-R | Resolution growth | `r` fixed at 3 | — | change of target; excluded |

**Explanatory label.** The label is "poor explanation" in any of these cases:

- the verdict is `COVERED-BY-EXISTING-RESULTS`;
- the H2 outcome is `LH-GENERIC`;
- every counted assumption is easy to vary.

Otherwise the label names each hard-to-vary assumption, together with its §3.4 class.

### 8.3 Reach

RT-3 lies beyond row 7 and the §5 (9, 13) entry, and it can fail. It concerns composites (Stage 0 rows 9 and 13):

- **The ring.** Four modes, with the rounded rule on every bond at one coefficient:
  `f(x)_i = ρ(k(x̃_{i−1} + x̃_{i+1}))`, indices mod 4. The ring is addressed by program only, using F-NAT's setting map.
  The isolated pair is not supplied.
- **The test.** For every `t ∈ [0, 1]` and every `ε > 0`, for all large `q`, there must be a setting such that every
  configuration in the H1 window of the mode-1 sector (all other modes and all memory at 0) ends with a mode-2 share
  within `ε` of `t`, and with a mode-3-plus-mode-4 share of at most `ε`.
- **Failure.** RT-3 fails otherwise.

Q-RED's literature comparison (§4 item 4) is a consistency check against independent mathematics, not a novel
prediction. No novel consequence that can be checked independently has been identified. **L3 is unreachable as frozen.**

### 8.4 Assessment ladder (monotone)

Each rung requires everything the rung below it requires.

- **L0:** some construction reaches an H1 positive. Target-built constructions are included: CC-TT and CC-TT′, if
  evaluated, are at most L0, because they fail SR. An F-B1 positive is also L0, because F-B1 is target-defined.
- **L1:** L0; the construction satisfies SR; and the positive family is F-NAT. A `generic` H1 success with no
  `LH-DISCRIMINATING` stops here, with the label "poor explanation". So does `COVERED-BY-EXISTING-RESULTS`.
- **L2:** L1, and all of the following:
  - `NEW-POSITIVE`;
  - at least one counted assumption is hard to vary, and its §3.4 component is independent;
  - RT-3 passes;
  - the SR control is green.
- **L3:** L2, plus a novel consequence that can be checked independently. This is unreachable as frozen.

`NEW-NEGATIVE`, `NEGATIVE-H1`, `INCONCLUSIVE`, `VOID`, `NO-OPERATIONAL-QUESTION` and `BLOCKED-QB` take no rung.
`NEW-NEGATIVE` is still a result: Q-LH is answered no.

### 8.5 Origin disclosure

**How the construction was found.**

1. The construction started from the question's anchors: the B1 mixer, with its unsourced real resources, and the
   finite-group bars on exact families.
2. The search then looked for a reason, independent of those anchors, why a finite reversible system would follow a
   continuous two-mode exchange.
3. The oscillator motivation and SM §4.2's rounded rule were found in that search.

**Influence of the target.**

- F-B1 is taken from B1, which was written to supply the target's mixing transition.
- F-NAT, the three symmetries and Q-LH were added in revision r2, after the review and the owner's requirements showed
  that the r1 criteria could be met by generic error propagation.
- The choice of S-LH as the discriminating test was made so that a generic scheme can fail it. The test was chosen for
  its ability to discriminate, not because of the target's statistics.
- The target informed which candidates were looked for and which was selected.

Disclosing this does not relax the independence requirement. It is why §3.4 classifies the motivation as mixed, why
§5.4 excludes (a), and why §0.1 leaves to the owner whether Q-LH counts as a P-MIX question.

## 9. Invariant → checkpoint table (§A.41)

| Invariant | Checkpoint |
| --- | --- |
| Each revision commit changes exactly this file | `git show --stat` of each commit: one path |
| No computation, simulation, Lean or V3 in Stage 1A | Reviewer: no script, data or Lean file added. §4 lists questions only |
| Carrier finite; no continuum or limit object | Reviewer reads §1.1, §2.5 and G-QB1–G-QB5 |
| Q-B not activated | `BLOCKED-QB` is pre-named. Grep §1–§8 for "limit", "Bloch", "sphere", "S²", "cosine-weighted": hits only in §3.1's rejected rows, the guards and disclaimers |
| No exact continuous-rotation claim | Each "exact" in §2 and §5 is a disclaimer, a finite-carrier fact, an exact symmetry of the finite rule, or the name of an exact *comparator* |
| Tested object stated as configuration-level | "the relevant mixing" appears only in quotations of owner records |
| Motivation free of target vocabulary | §6.6 grep of §3.3 |
| Approximation notions and horizons fixed before any result | §2.2 frozen. The Stage 1B result note quotes §2.2 and §2.4 verbatim |
| Mechanism-off and generic countercontrols can fail the success criterion | MO-1 and MO-2 through S-TUNE (§6.2); GC and MO-3 through S-LH (§6.3, §5.1) |
| H1 success never counts as hard-to-vary evidence | §8.2: variations judged at H2 only |
| Controls green before any verdict; "vacuous" decidable | The result note lists the §6 controls first; the §2.5 facts are listed separately |
| Every odd-modulus statement conditional on #1193 | Grep for `3^m`, "odd modul", "prime": hits only in §1.1, RB-4 and this row, each marked conditional. Other hits of "odd" name the rounding's parity, not a modulus |
| Paper-undecidable items are `INCONCLUSIVE`; criteria immutable | §4's frozen sentence appears unchanged in the result note |
| No `readWriteSourced_*` citation | Grep hits only the disclaimers in the pins, this row and §10 |
| Links pinned to `main@9c201475` | Every `/blob/` link carries `9c201475ba6fd8f341591d14dd8e88db2e2aaa90` |
| Every outcome reported with statuses, label and rung | Result note template: §5.1–§5.4 and §8 fields all filled |

## 10. §A.42 item 8: references off main

| Reference | Used for | Class |
| --- | --- | --- |
| #1169 c.6720450946, c.6720342295, c.6719386464, c.6720678942 | Authority and refinements (quoted) | Provenance (authorization) |
| Owner requirements on P-MIX (chat, 2026-11-08, relayed by the coordinating session) | §0.1, §5.2, §6.2–§6.3, §8.2 | Provenance (authorization). It is not yet a record on GitHub; the portfolio record quotes it with author and time (§A.42 item 7) |
| #1169 c.6719708521, c.6719720616, c.6719723538 (Stage 0) | Row numbering and wording (§1.5) | Provenance for numbering. Row content is cited from Main, AP1 and M2D on main |
| PR #1202, A5-Q3 A1 §3 C2 | Classes of §3.4 | Provenance. They are restated in §3.4 |
| #1198 (M-INACC, provisional) | K-7's reason; the reason S-NOINACC exists | Provenance. No content of M-INACC is used by any criterion, control or outcome |
| Independent review of `eb3802ee` (PR #1204 record) | The changes in r2 | Provenance |
| #1193 | Conditionality of RB-4 | Provenance (Issue) |
| #1188 | Reason not to cite `readWriteSourced_*` | Provenance (Issue) |
| #1147, #866, CTL | Supply obligations in §1.6 | Provenance |
| #1059 | Probability law, out of scope (§0.1) | Provenance (Issue) |
| #1173 reviews of B1 | Review status of B1 | Provenance. B1 is on main |
| Literature in §3.1, §3.3 and §2.4 | Candidate record, motivation and Q-RED | External. Reading status is stated per item, and [unverified] items decide nothing beyond what they state. No literature item is a premise of a criterion |

No commit or blob id is offered as support except `main@9c201475`, which is on main.
