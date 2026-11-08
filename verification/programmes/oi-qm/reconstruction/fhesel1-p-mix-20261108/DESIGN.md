# FHE-SEL-1 P-MIX: a finite-precision reversible two-mode exchange, preregistered (Stage 1A)

**Standing.** Stage 1A preregistration only, under #1169. Revision r4: it applies the independent re-review of `1975c649`
(REVISE). Earlier revisions applied the reviews of `eb3802ee` (r2, with the owner's P-MIX decision) and `3f12b442` (r3). WIP / UNVERIFIED. Writer: Claude Code
session, 2026-11-08.

This file fixes one construction, its motivation, its criteria and its controls before any result is evaluated. It
derives no result, runs no computation, proposes no premise for adoption and changes no manuscript. Stage 1B (the
derivations) is not authorized.

**Authority (quoted).**

- Owner decision, [#1169 c.6720450946](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6720450946)
  (recorded by amaybaum, 2026-11-08T10:38:44Z).
  - P-MIX row: "Can a specified physical carrier produce reversible mixing without importing quantum operations? … Q-B
    remains inactive."
  - "A finite-carrier P-MIX candidate cannot claim exact continuous rotations merely by changing its representation."
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
- Owner decision on P-MIX, [#1204 c.6720827308](https://github.com/amaybaum/incompleteness/pull/1204#issuecomment-6720827308)
  (recorded by amaybaum, 2026-11-08T11:19:07Z).
  - "The revised design must show three things."
    1. "A new research question."
    2. "A discriminating test. The mechanism-off control, and at least one generic reversible-discretization
       countercontrol, must each be able to fail the success criterion. Meeting a rounding-error bound is not enough."
    3. "Honest motivation and scope", including "Every decisive test can fail."
  - "A successful rounding approximation must not automatically count as evidence of a hard-to-vary physical
    principle."
  - "Then P-MIX should conclude that its proposed construction is already covered by existing mathematical results.
    That would be a valid outcome. We should not manufacture novelty to keep the three-construction portfolio
    symmetrical."
  - "The portfolio should report all three outcomes even if P-MIX is ultimately rejected as redundant."
  - "No new scientific execution is authorized."

**Order of evaluation (fixed).**
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
- Lean identifiers are under `verification/lean-mathlib/OIBridge/` at the same commit:
  - `substratumGen_not_control` (StructuralClosure.lean:348);
  - `permTheory_not_control` (SubstratumInterfaceAudit.lean:708);
  - `exists_perm_extending` (Equivalence.lean:60);
  - `nonnegBounded_not_denseUnitaryControl` (FrozenSourcing.lean:173), used in S-NODENSE.

  No `readWriteSourced_*` identifier is cited (#1188: `ReadWriteSourced` is vacuous).

**The Stage 0 map.** The Stage 0 map is
[#1169 c.6719708521](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6719708521). It was reviewed at
[c.6719720616](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6719720616) and confirmed at
c.6719723538. Its standing line "pending" is stale. It was written against `f88c1842`. Between `f88c1842` and
`9c201475`, none of the following changed:
- `papers/`;
- `oi-qm-ext-1/`;
- `apparatus-1-20261107/`;
- `mechanism-2-20261108/`;
- `StructuralClosure.lean` or `Equivalence.lean`.

## 0. Summary of what is frozen

| Item | Frozen choice |
| --- | --- |
| Carrier | **Finite.** One isolated pair of modes over `Z_q`, `q = 2^m`, with one-step memory, plus a finite controller and one fresh record cell. No continuum carrier is used or assumed, and none is taken as a limit object |
| Rule | SM's second-order form with a center-free symmetric two-site coupling, applied by rounding half away from zero. It has exact exchange, parity and time-reversal symmetries by construction (§1.3) |
| Families | F-NAT: one coefficient applied for a duration (oscillator physics). F-B1: B1's compensated word and schedule (target-defined; comparison only) |
| Horizons | H1: one 24-step program (finite-accuracy tracking). H2: up to `N_q = q/2^{10}` iterations of one primitive `S_k` (long horizon) |
| Discriminating test | S-LH at H2: drift of **both** normal-mode invariants of the pair (SM:296's `Q_I` and `Q_X`). Generic countercontrols are GC (floor/ceiling rounding), V-P and V-X (one tie rule changed each) and MO-3 (first-order lifting). If GC or MO-3 passes, the H2 outcome is `LH-GENERIC`. A failure counts only against a matched control that differs in the varied property alone (§5.1). Reversal by `R` is not discriminated as frozen: no admissible non-reversed countercontrol was found (§6.3) |
| Pre-named outcomes | `NO-OPERATIONAL-QUESTION` (§0.1); `BLOCKED-QB` (§3.2) |
| Overall verdicts | `NEW-POSITIVE`, `NEW-NEGATIVE`, `COVERED-BY-EXISTING-RESULTS`, `GENERIC`, `NEGATIVE-H1`, `INCONCLUSIVE`, `VOID`. If the owner rules Q-LH outside P-MIX, the alternative is `COVERED-BY-EXISTING-RESULTS (H1)` (§5.2) |
| Expected Stage 1B outcome | The honest expected H2 outcomes are `LH-GENERIC`, `LH-INCONCLUSIVE` with the open discretized-rotation problem named, or `LH-NEGATIVE`. No generic countercontrol has an identified failure route, so `LH-DISCRIMINATING` is not expected (§0.1). This is a scope statement, not a criterion |
| Stage 0 rows | Row 7 (relating evolution / lift). The mixing part of §5's "(iv) / reversible control (9, 13)" entry, in comparison only |
| Motivation class | Mixed. The rule, its symmetries and F-NAT are the independent component; F-B1 is target-defined. A positive is recorded (b) |
| Ceiling | A fixed-horizon success alone is capped at L1. L2 is reachable in principle (RT-3′, §8.3), but is unlikely to be decided in Stage 1B. L3 is unreachable as frozen |

### 0.1 What P-MIX can establish beyond Main:566/598 and the conditional B1 mixer

**Already established.**
- Main:566 (finite operational realization and gluing, ε-form) and Main:598 (uniform continuum realization) construct
  finite reversible realizations, for each fixed horizon, that approximate any finite quantum instrument family to any
  finite accuracy. Each realization is built from the target family and the horizon.
- B1 gives an exact continuum mixer, conditional on unsourced real modes (E-real) and exact real coefficients
  (E-control).
- On a finite carrier no exact continuously tunable family exists (AP1:955–977; S-FIN).

**Operational level.** This design supplies no step from configuration statements to state mixing on an operational
carrier:
- B1's amplitude dictionary does not factor through the standard density matrix (B1 §6, lines 124–140);
- dense unitary control is excluded on a fixed nonnegative-bounded identification (S-NODENSE);
- a derived read probability law belongs to Q-B (inactive) or #1059.

**Preregistered: `NO-OPERATIONAL-QUESTION`.** This is a scope finding about this design, not a theorem about every
finite design.

**Configuration level, fixed horizon (H1).** Whether a fixed local rule tracks the exact continuum exchange family
uniformly in the setting is likely to follow from generic error propagation. The relevant facts are:
- every second-order form is bijective (SM:106);
- the rounding error is "at most 1/3 per site and step" away from alphabet-boundary crossings (SM:298);
- the comparator is a fixed-length product of bounded maps;
- the coefficient resolution grows with `q`.

The genericity clause G-GEN decides whether H1 tracking does follow from generic error propagation (§8.2). An H1
success never counts as evidence of a hard-to-vary principle.

**Configuration level, long horizon (H2): the question that survives.**

> **Q-LH.**
>
> - Does the design keep **both** normal-mode invariants of the pair to vanishing relative error over `N_q ∝ A′_q`
>   steps, uniformly in `k ∈ K_q`? The invariants are SM:296's `Q_I` and `Q_X`, equivalently the energies of the
>   symmetric and antisymmetric sectors.
> - Do generic reversible discretizations of the same continuum primitive, which round differently, fail to keep
>   them? These are GC, V-P and V-X; MO-3 is a first-order lifting scheme judged on its own invariant.
> - Does the property depend on the design's exchange and parity symmetries? These are probed by V-X and V-P, each
>   against the design as matched control. Reversal by `R` is shared by every admissible scheme found, so Q-LH does
>   not discriminate reversal as frozen (§6.3).

**What a positive would show, and no more.**
- It would show that a fixed finite rule keeps the *depth* of the two-mode exchange over horizons growing with
  resolution: the energies of both normal modes do not drift, and hence neither does the largest share attainable for
  the kept sector energies. Whether that share is reached, and when, is timing.
- It would not show that the *timing* of the exchange (the beat phase) is kept. That is recorded separately (S-LH-TR)
  and enters no verdict.
- It stays at the configuration level. The operational level remains `NO-OPERATIONAL-QUESTION`.

**Why Q-LH is new relative to Main and B1, and how far.**
- Main's realizations are built per horizon. Q-LH concerns one rule whose horizon grows with `q`. B1 is continuum and
  exact.
- At H2 the crude worst-case error bound does not exclude a relative drift of order one. Over `N_q = A′_q` steps it
  sums per-step changes of order `A′_q` to order `(A′_q)²`. A pass therefore needs an argument beyond that bound.
  Whether that argument is generic is decided by G-GEN-H2 (§8.2).

**Scope statement (frozen as a statement, not a criterion).** S-LH may not be decidable on paper.
- On the symmetric and antisymmetric sectors it contains a horizon-limited form of the long-time boundedness of
  discretized rotations `x_{n+1} + x_{n−1} = ρ(λ x_n)` (Q-RED, §4). Their general case is open [unverified beyond
  bibliographic records; K-1 row].
- The supremum over `k ∈ K_q` includes coefficients within `2^{−r}` of `0` and `±1`.
- Showing on paper that a countercontrol fails requires an explicit drifting orbit, and no route to one is identified
  for GC, V-P, V-X or MO-3 (§6.3).
- RT-3′, which L2 requires, is as likely as S-LH to be undecidable on paper. L2 is reachable in principle and unlikely
  to be decided in Stage 1B.

The honest expected outcomes are therefore three:
- `LH-GENERIC`: a generic scheme passes too;
- `LH-INCONCLUSIVE`, with the open problem named, giving an overall `INCONCLUSIVE`;
- `LH-NEGATIVE`, giving `NEW-NEGATIVE`.

`LH-DISCRIMINATING` would need a generic scheme to be shown to fail where the design passes, and no route to such a
failure is known. Nothing in this design is tuned toward a positive. The owner can weigh Stage 1B with that in
view.

**Owner's call, and the preregistered alternative.** Whether Q-LH counts as a P-MIX question is for the owner to judge.
If it does not, the portfolio entry for P-MIX is:
- `NO-OPERATIONAL-QUESTION`;
- `BLOCKED-QB`;
- `COVERED-BY-EXISTING-RESULTS (H1)`, if the H1 positive is tagged generic, or the H1 outcome otherwise (§5.2).

The owner has stated that this is a valid outcome.

## 1. Construction

### 1.1 Carrier, stated explicitly as finite

- **Modes.** `x = (x_1, x_2) ∈ Z_q²` (current) and `y = (y_1, y_2) ∈ Z_q²` (previous), with `q = 2^m`, `m ≥ 1`.
  - Each member of the family is a finite carrier.
  - Claims are statements about the family, with explicit `q`-dependent bounds.
  - No member is identified with a real or complex space.
- **Controller.** B1 §5's controller, with the real interval replaced by `K_q = { j/2^r : j ∈ Z, |j| ≤ 2^r }`,
  `r = r(m) = ⌊m/2⌋`. It holds a program register of 24 coefficients, a clock `ℓ ∈ Z_64` and a fresh bit `ρ_0 = 0`.
- **Centered representatives.** `t̃` is the representative of `t ∈ Z_q` in `(−q/2, q/2]`.

**Choice of `q`.**
- At `m = 1`, `r = 0` and `K_2 = {0, ±1}`, so the rule is the linear modular rule of class N.
- MECH-2 Theorem U2 governs that instance only under its own hypotheses: the R1^⊗2 frame identification of laws, Lemma
  F's operation set and H-LIFT (M2D:315–325, 404–412). This design adopts none of them (P-U2).
- As refinement 2 states, U2 does not exclude every finite-order non-Clifford operation in a different extension.
- Odd moduli appear only in RB-4, where they are conditional on #1193.
- `q = 2^m` matches SM §4.2's alphabet size (`q = 2^16`, SM:294).

### 1.2 Microscopic rule

`ρ(t) = sgn(t)·⌊|t| + 1/2⌋` for rational `t` (rounding half away from zero). For `k = j/2^r ∈ K_q`:

```text
f_k(x) = ( ρ(k·x̃_2) , ρ(k·x̃_1) )  mod q
S_k : (x, y) ↦ ( f_k(x) − y ,  x )                (SM's second-order form, SM:106)
```

**World update** (B1 §5's schedule):
- at `ℓ ∈ {0,…,23}`, apply `S_{k_ℓ}`;
- at `ℓ = 24`, apply the copy `ρ_0 ↦ ρ_0 ⊕ 1[x̃_1 > 0]`;
- for `ℓ ∈ {25,…,63}`, apply the identity;
- then advance the clock: `ℓ ↦ ℓ + 1 mod 64`.

**Inherited, not derived here** (re-checked by control C-BIJ):
- every `S_k` is a bijection with inverse `(u, v) ↦ (v, f_k(v) − u)` (SM:106; B1:45);
- the copy is an involution;
- the world update is a bijection (B1 §5's argument).

**Departure from SM's rule.**
- SM §4.2's rounded rule `⌊(Σ_nn x + 1)/3⌋` acts on representatives `0, …, q−1` and is not odd. This rule rounds
  centered representatives and is odd.
- The two rules share only the second-order form.
- The r1 convention (half-up rounding) is kept as variation V-P (§8.2).

### 1.3 Symmetry sets (design properties; checked by control C-SYM)

Write:
- `X` for the exchange of the two slots of `x` and of `y` together;
- `P(x, y) = (−x, −y)` for parity;
- `R(x, y) = (y, x)` for time reversal, under which a map `S` is reversed when `R S R = S⁻¹`.

"Off `q/2`" means on configurations with no coordinate equal to `q/2`, the one value that is its own negative in
`Z_q`. Every window of §2.2 excludes it.

| Rule | Stated as kept | Stated as broken |
| --- | --- | --- |
| Design `S_k` | `X` (everywhere); `P` (off `q/2`); reversed by `R` (everywhere) | — |
| V-P (half-up rounding) | `X`; reversed by `R` | `P` |
| V-X (slot 1 half away from zero, slot 2 half toward zero) | `P`; reversed by `R` | `X` |
| GC (slot 1 floor, slot 2 ceiling) | reversed by `R`; the product `XP: (x, y) ↦ (−Xx, −Xy)` (off `q/2`) | `X` and `P` separately |
| GC-NR (recorded pair, §6.3) | `P` (off `q/2`) | `X`; not reversed by `R` (`R S R ≠ S⁻¹`) |
| GC-R (recorded pair, §6.3) | `P` (off `q/2`); reversed by `R` | `X` |
| MO-3 (first-order lifting, §6.3) | `P`; reversed by the involution `RA`, where `R: (x_1, x_2) ↦ (x_1, −x_2)` and `A: x_1 += ρ(k x̃_2)` | `X` not claimed |
| V-S (self-term) | `X`; `P`; reversed by `R` | — (adds a self-term) |

GC-NR is the only listed rule for which reversal by `R` is not claimed. Whether some other involution reverses it is
not claimed either way. GC-NR and GC-R are a recorded pair only; they enter no category, attribution or label
(§6.3). These symmetries are properties of the constructions, not results, and their presence is not
evidence (§8.2).

### 1.4 Observer access, preparations, records, encoded description

- **Read.** The only read is `1[x̃_1 > 0]`. It is copied at `ℓ = 24` and read passively afterwards (B1 §6). It is
  deterministic. No sampling, re-preparation or outcome-probability rule is posited.
- **Preparations.**
  - Point preparations.
  - The law `μ_W`, uniform on a declared window (Main:56, 60; posit (iv)). It is used only to weight disagreements in
    S-REC.
- **Setting independence.** The prepared law is fixed before `ℓ = 0`, independently of the program. Only the current
  instruction is read (GA:90–92; B1 §5).
- **Encoded description.** `(x̃, ỹ)/A_q ∈ R⁴`.
  - It is an injective point map of configurations into `R⁴`.
  - It is not a frame identification of laws into an operator space: it assigns no operator to any law and no
    probability to any event.
  - Neither the setting intervals, nor `R⁴`, nor any invariant is a carrier or state space of the model (G-QB5).

### 1.5 Stage 0 rows targeted

- **Row 7** (relating evolution / lift). Column (c): "Relating evolution (Main:646)". Column (d): "None: Main:646
  'neither supplies one nor says what form one must take'". P-MIX asks whether a specified finite rule fixes the
  transformation relating two times of the pair, by the program executed between them, rather than by a choice of lift.
- **Stage 0 §5 "(iv) / reversible control (9, 13)"**, mixing part only.
  - The entry reads: "a continuously tunable mixing operation (Main:590): assumed and target-adjacent … No independent
    candidate."
  - It is addressed in §7 only, at the level fixed by §0.1.
  - The access part belongs to P-CONTROL.
- **Rows 15 and 13** are touched by Q-LH and RT-3′ respectively. They are not targeted for selection.

### 1.6 Source ledger

| Resource | Content | Class | Source / note |
| --- | --- | --- | --- |
| Finite alphabet `Z_q` | Configuration values | native | A1 (Sub:92), a posit. `q = 2^m` is a parameter choice |
| Second-order form | `x(t+1) = f(x(t)) − x(t−1)` | native | SM:106; A2 (Sub:94), a posit |
| Center-free symmetric coupling | Each mode reads only the other, with the same coefficient | native (posit) | A4 (Sub:98). The warrant for its no-self-term clause is open (Stage 0 row 9) |
| Odd rounding `ρ` on centered representatives | Half-away-from-zero rounding of a dyadic multiple | supplied | Proposed rule component. It differs from SM §4.2's convention (§1.2). A5 fails for it |
| `K_q`, `r(m)` | Finite dyadic coefficients | supplied | Replaces B1's E-control. Loading is not sourced (CTL; CPP) |
| Isolated pair | Omitted modes are spectators | supplied | B1's E-pair |
| Clock and schedule | `Z_64`; 24-step program; copy at step 24 | supplied | B1 §5. Stage 0 row 5 |
| Fresh record cell | `ρ_0 = 0` | supplied | #1147 |
| Sign read | `1[x̃_1 > 0]` copied by an involution | supplied (access); native (map form) | B1's E-read |
| Preparations | Points; uniform on a window | supplied (preparation); native posit (law) | Main:56, 60 |
| Representatives, windows, scales | Scope of the claims | representation | They act on no configuration |
| Continuum comparators and invariants | §2.1, §2.4 | imported (comparison only) | B1 §3–§4; SM:296 |

No supplied entry may be counted as physically generated (owner boundary, c.6720450946).

## 2. Families, horizons, comparators and criteria (fixed in advance)

### 2.1 Comparators and families

- **Continuum primitive.** `T_s(x, y) = (sXx − y, x)` on `R⁴` (B1:36–45). `T[w]` and `Φ_q[w]` are the composed
  continuum and finite maps, applied right to left.
- **Quantization.** `κ_q(t)` is the nearest element of `K_q`, with ties toward 0.
- **F-NAT** (oscillator physics).
  - Setting: `s ∈ [−1, 1]`.
  - H1 program: `n_q(s) = (κ_q(s))^{24}`.
  - Exact comparator: `E_NAT(s) = T_s^{24}`, with `s` unquantized. The duration 24 is a representation choice, made so
    that F-NAT and F-B1 can be compared.
- **F-B1** (target-inspired; comparison only).
  - Setting: `θ ∈ [−π, π]`.
  - Building blocks: `Q_a = T_a T_0³`, `P_b = T_0 T_{−b} T_0²`, `C(a,b) = Q_a P_b Q_a`.
  - Program: `w_q(θ) = C(a_q, κ_q(b(a_q)))²`, where `a(θ) = −tan(θ/4)`, `a_q = κ_q(a(θ))` and `b(a) = −2a/(1+a²)`.
  - Exact comparator: `E_B1(θ) = T[C(a(θ), b(a(θ)))²]` (B1:89, 108–111).
  - F-B1 enters H1 only. It plays no part in Q-LH, S-LH, the variations, or the ladder above L0.

### 2.2 Horizons, windows, error

- **H1.** One 24-step program.
  - Window `W_q`: `|t̃| ≤ A_q = q/2^8` for every coordinate.
  - Composition window `W_q^{(2)}`: `A_q / 2`.
- **H2.** Up to `N_q = q/2^{10}` iterations of a single primitive `S_k`, `k ∈ K_q`.
  - Window `W_q^{LH}`: `|t̃| ≤ A′_q = q/2^{10}`.
  - H2 is a property of the map `S_k`, not of the world update. The world update reaches `S_k^n` only for `n ∈ 24ℕ`,
    with record copies in between. The supremum over all `n ≤ N_q` is the stronger statement.
- **Error.** `δ_q[Φ, E; W] = max_{z ∈ W} ‖ (Φ z)~ − E z̃ ‖_∞ / A_q`.

These are the only approximation notions. They are uniform (worst-case) notions. Changing them after any result is
evaluated voids the round.

### 2.3 H1 criteria, for each family F ∈ {NAT, B1}

"Explicit" means a bound written on paper in terms of `q`, the word length and `r(m)`. A bound that holds only for some
settings, or only on a window shrinking faster than `A_q`, does not count.

- **S-BIJ.** Every program is a bijection (C-BIJ).
- **S-TRACK_F (recorded; never sufficient).** `sup_σ δ_q[Φ_q[P_F(σ)], T[P_F(σ)]; W_q] → 0`, with an explicit bound.
  This measures rounding error only.
- **S-TUNE_F.** `sup_σ δ_q[Φ_q[P_F(σ)], E_F(σ); W_q] → 0`, with an explicit bound. The comparator is the exact,
  unquantized family.
- **S-INV_F.** Inverse by forward programs only; no time reversal is used.
  - F-B1: `sup_θ δ_q[Φ_q[w_q(−θ)] Φ_q[w_q(θ)], id; W_q] → 0`.
  - F-NAT: either a rule `s ↦ (α, s′, β)`, with `α, β ∈ {0,…,3}` and `s′ ∈ [−1, 1]`, such that
    `sup_s δ_q[Φ_q[(0)^α n_q(s′) (0)^β] Φ_q[n_q(s)], id; W_q^{(2)}] → 0`; or a proof that none exists in that frozen
    word set.
- **S-COMP_B1.** `sup_{θ,φ} δ_q[Φ_q[w_q(θ)] Φ_q[w_q(φ)], E_B1(θ+φ); W_q^{(2)}] → 0`.
- **S-REC_F.** The `μ_W`-mass of window configurations whose sign record after `P_F(σ)` differs from the sign of the
  first coordinate of `E_F(σ) z̃` tends to 0, uniformly in `σ`.
- **CT_F.** Let `τ_F(σ; z)` be the mode-2 share `(u_2² + v_2²)/(|u|² + |v|²)` of `(u, v) = E_F(σ) z`, for unit `z` in
  `{x_2 = y_2 = 0}`. CT_F holds iff both of the following hold:
  - for every `t ∈ [0, 1]`, some `σ` and `z` give `τ_F = t`;
  - every `E_F(σ)` is invertible.

  For F-B1, CT holds by B1 §4; this is recorded.

### 2.4 H2 criterion S-LH (both normal-mode invariants)

For a symmetric translation-invariant coupling `A` on the pair (translation group `{I, X}`), SM:296's conserved forms
are:

```text
Q_B(u, v) = u·Bu + v·Bv − u·BAv,     B ∈ {I, X},
```

with `(u, v)` the two configuration slots. For the design, and for every rule sharing its continuum primitive, the
coupling is `A = kX`. Then:
- `Q_I = |u|² + |v|² − k u·Xv`, the total energy;
- `Q_X = u·Xu + v·Xv − k u·v`.

**Sector-energy identity (stated for quotation; Stage 1B quotes it rather than re-deriving it).** With sector
coordinates `u_± = (x_1 ± x_2)/√2` and `v_± = (y_1 ± y_2)/√2`:

```text
Q_I + Q_X = 2 (u_+² + v_+² − k u_+ v_+),        Q_I − Q_X = 2 (u_−² + v_−² + k u_− v_−).
```

These are twice the invariants of the symmetric sector (`x_1 = x_2`, coupling `+k`) and the antisymmetric sector
(`x_1 = −x_2`, coupling `−k`), each for the map `(u, v) ↦ (λu − v, u)` with `λ = ±k`.

**S-LH (for a rule `Ψ_k` with continuum coupling `A_k` and its two forms `Q_I`, `Q_X`).** Stage 1B gives an explicit
`B_LH(q) → 0` such that:

```text
max_{B ∈ {I, X}}  sup_{k ∈ K_q, |k| ≤ 1}  sup_{z ∈ W_q^{LH}}  sup_{0 ≤ n ≤ N_q}
      | Q_B(Ψ_k^n z̃) − Q_B(z̃) | / (A′_q)²   ≤   B_LH(q),
```

with no alphabet-boundary crossing along the way. Otherwise S-LH fails (a proof that no such bound exists) or is
undecided.

Bounding `Q_I` alone would not see energy flowing between the two sectors, which is the exchange (re-review R1).

**S-LH-TR (recorded only; enters no verdict).** Whether the mode-2 share of `S_k^n z` stays within a vanishing distance
of the continuum beat `T_k^n z̃`, for all `n ≤ N_q`. This records the timing of the exchange at H2.

S-LH is evaluated for:
- the design;
- MO-1 (§6.2);
- GC and MO-3 (§6.3);
- the recorded pair GC-NR and GC-R (§6.3), which enters no category;
- each variant of §8.2.

### 2.5 Standing scope facts (recorded; not controls; outside the VOID rule)

- **S-FIN.** At each `q`, the programs generate a finite permutation group, and every program has finite order. The
  setting maps take at most `|K_q|` values (F-NAT) or `|K_q|²` values (F-B1).
- **S-NOEXACT.** No outcome is phrased as exact (iv) (Main:590; `substratumGen_not_control`) or as an exactly induced
  `rot` (AP1:955–977).
- **S-NOTNEW.** H1 approximate realizability is not presented as new (Main:566, 598).
- **S-NODENSE.** No outcome is read as approximate or dense encoded unitary control on a fixed nonnegative
  identification (`nonnegBounded_not_denseUnitaryControl`; AP1:186–192). No frame identification of laws is adopted.
- **S-CLASSICAL.** The carrier, with its laws and deterministic rule, is a classical model of every statistic the
  design produces.
- **S-NOINACC.** No inaccessible functional and no P1/P2 registration are posited. If one is needed, the outcome is
  `INCONCLUSIVE` and the need is named.

## 3. Independent physical motivation

### 3.1 Candidates considered (owner distinction (b)): search record

**Search scope.**
- Corpus terms, searched at `main@9c201475`: reversible, second-order, rounded, floor, lattice gas, billiard,
  Margolus, Fredkin, Toffoli, symplectic, cat map, beat, discretized rotation, quantum walk, quantum cellular.
- **[unverified]** marks a reason stated from memory or from an abstract. Such a reason decides nothing beyond what it
  states.

| # | Candidate | Carrier | Source (reading status) | Decision | Reason |
| --- | --- | --- | --- | --- | --- |
| K-1 | Finite-precision reversible two-mode exchange (this design) | finite | SM:106, 294–298; B1 §3–§4; Levesque & Verlet, *J. Stat. Phys.* 72, 519 (1993) (bibliographic record and abstract-level descriptions); Lowenstein, Hatjispyros & Vivaldi, *Chaos* 7, 49 (1997); Akiyama, Brunotte, Pethő & Steiner, arXiv:0704.3674; Akiyama & Pethő, arXiv:1206.3868 (bibliographic records and abstracts only) | **selected** | Finite carrier; fixed local reversible rule with the exact symmetries of a coupled pair; two-mode transfer. It replaces B1's E-real and E-control with finite resources |
| K-2 | Single-mode discretized rotation `(x, y) ↦ (ρ(λx) − y, x)` | finite | Same literature as K-1 | rejected as a candidate; used in Q-RED | A phase-type operation, which is already a stated intervention (Main:590) |
| K-3 | Linear modular rule with integer coefficients (class N) | finite | SM:296, 298; AP1; M2D | rejected; **control MO-2** | SM:298: "reduction modulo `q` introduces no nonlinearity" |
| K-4 | Reversible lattice gases: HPP (*J. Math. Phys.* 14, 1746 (1973), from memory), FHP (PRL 56, 1505 (1986), cited in the corpus), HB's gas | finite | HB; hydrodynamics `PROGRAMME.md`:49 | rejected | Collisions permute occupation configurations; no tunable setting. [unverified] Relaxation is undone by a forward word only at recurrence times |
| K-5 | Billiard-ball and conservative-logic CA (Margolus, *Physica D* 10, 81 (1984); Toffoli & Margolus, *Physica D* 45, 229 (1990); Fredkin & Toffoli 1982, read in CPP) | finite | CPP §1 | rejected | Monomial routing (`permTheory_not_control`) |
| K-6 | Cat-map-type linear maps (Arnold & Avez 1968, from memory) | finite | — | rejected | K-3's reason. [unverified] A target-adjacent association with stabilizer-type groups |
| K-7 | `G_SM`, `G_σ` | finite (`q = 2`) | M2D; #1198 (provisional) | rejected | U2 within its hypotheses. #1198 reports, provisionally, that `G_σ`'s protection fails |
| K-8 | P-8-type hidden parity | finite | AP1 §5.2 | rejected | Q-A's object |
| K-9 | B1 as stated | continuum | B1 | rejected; §3.2 | Unsourced E-real and E-control |
| K-10 | Classical spin on `S²`; the Kochen–Specker model | continuum | AP1 §5.3–§5.4 | rejected | Q-B's first decisive check (AP1:1032, 1082) |
| K-11 | Briggs & Eisfeld, PRA 85, 052111 (2012) | continuum | B1 §9 | rejected | Same as K-9 |
| K-12 | Quantum walks and quantum cellular automata (Aharonov, Davidovich & Zagury, PRA 48, 1687 (1993); Schumacher & Werner, arXiv:quant-ph/0405174), from memory | — | — | rejected | [unverified] Target-defined |
| K-13 | 't Hooft (Springer 2016); Elze, PRA 89, 012111 (2014), from memory | finite | — | rejected | [unverified] Target-defined |
| K-14 | Main:566, 598 realizations | finite | Main | rejected; **CC-TT** | Built from the target family and horizon (GA:92) |

Selection among candidates occurred, so a positive is recorded (b) at best.

### 3.2 The continuum branch and Q-B

A continuum design (K-9 to K-11) would posit real modes as physical. The exchange is then an exact continuous family.
Q-B asks "What additional OI principle could produce the continuous rotations" (AP1:1082), and its first decisive check
uses a continuum carrier (AP1:1032). No reformulation was found that stays outside Q-B. The continuum branch is not
executed. Its outcome is **`BLOCKED-QB`**.

The following guards keep the finite design outside Q-B:
- **G-QB1.** No claim concerns a limit object of `{Z_{2^m}}`.
- **G-QB2.** No read re-prepares from a law.
- **G-QB3.** No outcome-probability law is claimed, used or compared, cosine-weighted or otherwise.
- **G-QB4.** No carrier whose laws contain a ball, a sphere or any continuum is introduced.
- **G-QB5.** Setting intervals, `R⁴` and the invariants `Q_B` are never a carrier or state space of the model.

### 3.3 Motivation, written without reference to the target

**Coupled oscillators.** Two identical oscillators with a symmetric coupling exchange energy periodically. With all
energy initially in one oscillator, the energy passes to the other and back, at a rate set by the coupling strength
(small-oscillation theory, e.g. Goldstein, Poole & Safko, *Classical Mechanics*, 3rd ed., ch. 6, from memory).

**Normal modes and the beat.** The pair has two normal modes, the in-phase motion and the opposite-phase motion. Each
keeps its own energy. The exchange is the beat between them.

**Exact symmetries.** The pair has three exact symmetries:
- relabelling the two identical oscillators;
- reflecting every displacement in a symmetric potential;
- reversing the direction of time.

**Finite precision.** A physical register with finitely many values cannot hold a real coupling coefficient. A
finite-state version must therefore replace multiplication by a real number with an operation on integers.
- Exactly reversible integer discretizations of Hamiltonian dynamics were introduced for this purpose (Levesque &
  Verlet 1993).
- The second-order form makes any integer update reversible and keeps time reversal (SM:106).
- Rounding half away from zero keeps the reflection symmetry.
- The same rounding in both slots keeps the relabelling symmetry.
- SM §4.2 uses a rounded integer coefficient in the same second-order form, with a different rounding convention and
  different representatives, and for an unrelated reason: breaking the integrability of the linear rule (SM:294).

**The family.** The family this motivation offers is a fixed coupling applied for a duration, tuned by its strength
(F-NAT).

**The question.** Does such a pair, given finite precision but keeping its exact symmetries, keep the energy of each
normal mode over long times? And does that depend on its exchange and reflection symmetries? Time reversal is shared
by every admissible scheme found, so the frozen design does not ask whether it matters (§6.3).

### 3.4 Classification (Q3's standard)

**Classes.** The classes are those of A5-Q3's amendment A1 §3, criterion C2 (PR #1202, off main). They are restated
here, and each assumption is judged on its own:
- **independent:** the motivation neither presupposes `T` nor is designed to exclude a particular construction;
- **target-adjacent:** the motivation presupposes `T`, is equivalent to it on the class, or is supported only by a
  consequence of it;
- **target-defined:** the stated reason is to obtain `T` or to exclude a particular construction;
- **mixed:** an independent component together with another component, each identified;
- **none found**.

**Target.** `T` is completion condition (iv) in mixing form: an exact, continuously tunable state-mixing operation on
the operational carrier (Main:590).
- `T` implies the failure of C-ROT (AP1:188).
- The converse fails: `rot` alone gives density, not exact continuous tunability (AP1:28, 188–192).

| Component | Class | Basis |
| --- | --- | --- |
| Energy exchange of two coupled oscillators; normal modes | independent | Classical mechanics. It motivates `S_k`, F-NAT and S-LH's two invariants |
| Exchange, reflection and time-reversal symmetries | independent | Identical oscillators; a symmetric potential; microscopic reversibility |
| F-NAT's form | independent | §3.3. The duration 24 is a representation choice |
| Center-free symmetric coupling | independent (translation clause); open (no-self-term clause) | A4 (Sub:98); Stage 0 row 9 |
| Second-order reversible form | mixed | A2's motivation is mixed (Main:62, 66; Stage 0 row 4). Its time-reversal component is independent |
| Finite alphabet | target-adjacent in part | A1 via E3 (Sub:80, 92) |
| Rounding | mixed | Independent uses (Levesque–Verlet; SM §4.2). Its role here, letting a finite rule follow the continuum exchange, is adjacent to `T` |
| F-B1's word and schedule | **target-defined** | B1:7; B1:89 (compensation fixed by "Requiring this endpoint to commute with the fixed quarter-turn J"); B1:103–111 |
| Selection of K-1 | target-defined insofar as it was made to carry F-B1; target-adjacent insofar as it was made to carry a two-mode transfer | §3.1 |
| Choice of S-LH and of the countercontrols | Not a motivation component; disclosed in §8.5 | It was chosen after review, for its power to discriminate |

**Overall: mixed.**
- Independent component: the rule, its symmetries, F-NAT and S-LH's invariants.
- Target-defined component: F-B1, used for H1 comparison only.
- Target-adjacent components: finiteness via E3, the role of rounding, and the selection.

## 4. Mathematical consequences to be derived in Stage 1B (questions only)

If authorized, Stage 1B works on paper, in this order:

1. **Controls.** C-BIJ and C-SYM, for the design and every rule of §1.3.
2. **H1.** The H1 criteria for F-NAT, then for F-B1, including the boundary-crossing question.
   - A crossing on a window counts as a failure. It is never a reason to change the window.
   - A margin of `2^7` needs a uniform bound on partial products.
   - Then G-GEN (§8.2).
3. **H2.** S-LH for the design, MO-1, GC, MO-3, each variant, and the recorded pair GC-NR and GC-R. S-LH-TR where decidable. Then G-GEN-H2 (§8.2).
4. **Q-RED.** Are the symmetric and antisymmetric sectors invariant under `S_k`? Does `S_k` reduce on each to
   `(x, y) ↦ (ρ(±k x) − y, x)`? If so, list which published results on such maps (K-1 row) apply at the same coefficient
   and rounding convention, and record the sector part of S-LH as an instance of them or of an open problem. Do the
   same for the reversible-integration literature cited in K-1.
5. **Reach.** RT-3′ (§8.3), with its continuum invariance recorded as a preserved comparator.
6. **Comparison.** Only then, §7.

**Paper-undecidable items (frozen).** Any criterion, control, variation or reach test that cannot be decided on paper
is recorded `INCONCLUSIVE`, with its gap named. A later authorization of computation cannot change §2, §5, §6 or §8.

**DC-1 (derivation constraint).** No derivation may assume any of the following properties of a rounded rule, which
SM:294–298 records as unestablished or contrary:
- exact energy conservation;
- integrability;
- cycle ergodicity;
- absence of boundary-crossing jumps outside the window.

## 5. Outcomes and decision rules (fixed in advance)

### 5.1 Per-horizon outcome categories

**VOID gate.** The outcome is `VOID` when any §6 control is red or vacuous.
- A control is **vacuous** iff its pass condition is fixed by the text of this design without deriving any property of
  a finite rule, or iff no property of the rules it names could make it red.
- Under this definition MO-1, MO-2, P-B1, C-SYM and the SR control are legitimate sanity controls.
- The §2.5 facts are outside the VOID rule.

**H1, for each family F.**

| Outcome | Rule |
| --- | --- |
| `H1-POSITIVE_F` | S-BIJ, S-TUNE_F, S-INV_F, S-REC_F and CT_F hold, with explicit bounds. For F-B1, S-COMP_B1 also holds |
| `H1-PARTIAL_F` | S-BIJ, S-TUNE_F and CT_F hold, and another H1 criterion fails, holds only with a non-vanishing bound, or holds only on a subset of settings |
| `H1-NEGATIVE_F` | S-TUNE_F fails, CT_F fails, or S-BIJ fails |
| `H1-INCONCLUSIVE_F` | A criterion is undecided on paper. The gap is named |
| Tag `generic` | An H1 positive or partial result carries the tag if G-GEN applies (§8.2) |

**H2, for the design.** The rows are applied in order, and the first match decides.

| Outcome | Rule |
| --- | --- |
| `LH-NEGATIVE` | S-LH fails for the design |
| `LH-COVERED` | The design passes, and its pass is an instance of a published theorem (§4 item 4) |
| `LH-GENERIC` | The design passes, and GC or MO-3 passes S-LH (MO-3 against its own `Q_k`), directly or because G-GEN-H2 finds that the design's bound follows from a lemma whose hypotheses GC or MO-3 also satisfies |
| `LH-DISCRIMINATING` | The design passes, neither GC nor MO-3 is shown to pass, and at least one admissible countercontrol (GC, V-P or V-X) is shown to fail S-LH under the matched-control rule |
| `LH-INCONCLUSIVE` | Every other case, with the gap named |

**Admissible countercontrol.** A countercontrol is admissible iff it meets all of the following:
- it has the design's continuum primitive `T_k` and forms `Q_I`, `Q_X`;
- it is in second-order form;
- it differs from the design only in the rounding rule applied to the products `k·x̃_i`.

GC, V-P and V-X are admissible. GC-NR and GC-R are not, because each adds a bounded kick that is not a rounding of
`k·x̃_i`.

**Matched-control rule (frozen).** A countercontrol's failure counts toward `LH-DISCRIMINATING` only if a matched
control that differs from it only in the varied property passes. For GC, V-P and V-X the matched control is the design:
- V-P differs from the design only in the parity of the tie rule;
- V-X differs only in the exchange of the tie rule;
- GC differs only in the rounding convention, using floor and ceiling in place of symmetric odd rounding.

The design must pass for any of these failures to count. The same rule governs every hard-to-vary attribution in §8.2.

The results for V-S and the recorded pair are reported beside the category, and V-S enters §8.2.

### 5.2 Overall configuration-level verdict (F-NAT)

The rows are applied in order, and the first match decides.

| Verdict | Rule |
| --- | --- |
| `VOID` | The VOID gate is met |
| `NEW-NEGATIVE` | `LH-NEGATIVE`. Q-LH is answered no |
| `NEW-POSITIVE` | An H1 positive or partial result for F-NAT, together with `LH-DISCRIMINATING` |
| `COVERED-BY-EXISTING-RESULTS` | An H1 positive tagged `generic`, together with `LH-COVERED` |
| `GENERIC` | An H1 positive tagged `generic`, together with `LH-GENERIC`. The property is generic and established in Stage 1B; it is not found in the existing literature |
| `NEGATIVE-H1` | `H1-NEGATIVE_NAT` |
| `INCONCLUSIVE` | Every other combination, with each undecided item named. This includes `LH-INCONCLUSIVE`, and an untagged H1 positive together with `LH-COVERED` or `LH-GENERIC` |

**Alternative, if the owner rules that Q-LH is outside P-MIX.** The verdict is `COVERED-BY-EXISTING-RESULTS (H1)` if
the H1 positive for F-NAT is tagged `generic`. Otherwise it is the H1 outcome itself.

**Reported in every case.**
- `NO-OPERATIONAL-QUESTION` and `BLOCKED-QB`.
- F-B1's H1 outcome, marked target-defined. It never changes the verdict.

**Commitment to report.** Every outcome is reported in the portfolio record, whatever it is: the pre-named outcomes,
both horizons, the verdict and its alternative, the three statuses, the owner label, the genericity tags, the
explanatory label and the rung. The portfolio reports all three constructions' outcomes even if P-MIX is ultimately
rejected as redundant (c.6720827308).

### 5.3 The three statuses

- **Proposed.** The rule, its symmetries and F-NAT are proposed (mixed; subject to review). F-B1 is not proposed.
- **Mathematically sufficient.** Recorded only for the criteria that hold, each named. It is limited to the
  configuration-level statements under §1's hypotheses, and is never recorded at the operational level.
- **Derived from native OI.** Recorded only if every ledger entry used is native. At this freeze, six entries are
  supplied:
  - the isolated pair;
  - the rounding;
  - `K_q`;
  - the clock;
  - the record cell;
  - the read access.

### 5.4 Owner portfolio distinctions

- **(a)** Not available. The motivation is mixed and candidates were selected.
- **(b)** Applies to any positive. It cites §3.1 and §8.2. An F-B1 positive is additionally marked target-defined.
- **(c)** No outcome statistics are claimed beyond deterministic record laws, which have a classical model
  (S-CLASSICAL). No outcome counts as evidence of nonclassical behaviour. (c) is attached if a later reading compares
  the record laws with a quantum law.

## 6. Controls

A verdict is rendered only over green controls. Each control's route to red is named.

### 6.1 Preserved-result and construction controls

| Id | What it checks | Green iff | Route to red |
| --- | --- | --- | --- |
| C-BIJ | SM:106; B1 §5; every rule of §1.3 | Each rule's step is a bijection | A non-injective step |
| C-SYM | §1.3 table | Every "kept" entry holds as stated, and every "broken" entry is broken on some window configuration | A kept symmetry fails, or a broken one holds on the whole window |
| P-U2 | U2 (M2D:55–64, 404–412) within its hypotheses (M2D:315–325) | Stage 1B names the hypotheses this design lacks, and no §2 statement uses U2's conclusion | A derivation invokes U2, or the stated reason is false |
| P-B1 | B1 §4, §6–§7 | `J = S_0` has `J⁴ = id`, and `J²` reverses every sign | Either check fails |
| P-SM | SM:294–298 | DC-1 is respected | A derivation uses a DC-1 property |

C1–C4 are not evaluated. Main calls them "diagnostics of a realization rather than hypotheses" (Main:72); they are
defined at Main:74–80, and the theorem is at Main:82. The visible process here is one bit per cycle. Over one cycle the
diagnostics are near-trivial. Over many cycles they fall in SM:294–298's open territory. No horizon gives them
decidable content.

### 6.2 Mechanism-off controls

- **MO-1 (coupling off).**
  - At H1, every setting's program is the all-zero program, and the comparators remain `E_F(σ)`.
    - Green iff S-TUNE_F fails for MO-1.
    - Route to red: S-TUNE_F holds for a setting-independent map against a non-constant family.
  - At H2, `Ψ_k = S_0` for every `k`, judged against the design's `Q_I` and `Q_X` at coupling `k`.
    - **This is a calibration check of S-LH, not evidence about the mechanism.** `S_0 = J` changes the sign of the
      `k u·v` terms, so it does not keep the forms at `k ≠ 0`. At `k = 0` it keeps both forms exactly and cannot fail.
    - Green iff S-LH fails for MO-1.
    - Route to red: S-LH holds, which would mean the criterion does not register a coupling-dependent invariant.
- **MO-2 (no fractional coefficients, no rounding).**
  - F-NAT's setting map, with `K_q` replaced by `{−1, 0, 1}` (nearest element, ties toward 0). This is K-3's linear
    modular rule, with comparator `E_NAT(s)`.
  - Green iff S-TUNE_NAT fails for MO-2.
  - Route to red: S-TUNE holds with a finite, setting-independent coefficient alphabet.
  - This is also the reason no such rule can reach `H1-PARTIAL`.
  - S-TRACK may hold for MO-2, and that is recorded.

In either case, a red result means the criterion is miscalibrated, and the outcome is `VOID`.

### 6.3 Countercontrols (enter §5.1; not VOID controls)

Each countercontrol below is stated with its symmetry set (§1.3), its invariants, and its route to failing S-LH.

- **GC.**
  - Rule: slot 1 uses `⌊k x̃_2⌋`, slot 2 uses `⌈k x̃_1⌉`, in second-order form.
  - It shares the design's `T_k`, `Q_I` and `Q_X`. It keeps `R` and `XP`, and breaks `X` and `P` separately.
  - Route to failure: **none identified**. Its floor/ceiling bias acts like a nearly constant force. For `|k| ≤ 1` that
    force is not resonant with the primitive, which suggests bounded displacement rather than drift.
  - GC therefore tests `X` and `P` separately, through the variation rule. It does not test `R`.
- **V-P and V-X** (§8.2) are admissible countercontrols with the design as matched control. Route to failure:
  **none identified**.
- **Recorded pair GC-NR and GC-R (not admissible; enters no category, attribution or label).**
  - GC-NR, with `κ(x, y_2) = sgn(x̃_2 − ỹ_2)`:

    ```text
    x′_1 = ρ(k x̃_2) − y_1 + κ(x, y_2),     x′_2 = ρ(k x̃_1) − y_2,     y′ = x.
    ```

    It is bijective by a triangular inverse. It keeps `P`, breaks `X`, and is not reversed by `R`.
  - GC-R: `x′_1 = ρ(k x̃_2) + sgn(x̃_2) − y_1`, `x′_2 = ρ(k x̃_1) − y_2`. It is bijective (SM:106), reversed by `R`,
    keeps `P` and breaks `X`. It is GC-NR's symmetry set with reversal restored.
  - **What is known.** The re-review of `1975c649` reasons, by hand-checkable recurrences at `k = 0` from
    `z = ((0, a), (0, 0))`, that both fail S-LH. Their added kicks are resonant at mode 1's own frequency, so mode 1
    grows linearly. This is reviewer reasoning; Stage 1B re-checks it.
  - **Reading.** The failures come from an added bounded forcing correlated with the oscillation, not from the presence
    or absence of reversal. The pair is recorded as: "an added velocity- or position-correlated forcing drifts". It
    bears on forcing, not on reversal.
- **Reversal is not discriminated as frozen.**
  - One candidate was considered: `x′ = f_k(x) − σ(y)`, with `σ` the bounded bijection that flips the lowest bit. It
    is not reversed by `R`.
  - It was not adopted. Its per-step deviation, `σ(y) − y = ±1`, reads the memory slot, which the design's rounding
    never does. So a failure could not be attributed to reversal without a further matched control, and no matched
    control differing only in reversal was found.
  - No admissible non-reversed countercontrol is available. Q-LH therefore does not test whether reversal matters, and
    no reversal credit is available in §8.2.
- **MO-3 (first-order lifting, no memory, no symmetric coupling).**
  - Rule: `A: x_1 += ρ(k x̃_2)`, then `B: x_2 −= ρ(k x̃_1)`.
  - Continuum primitive: `L_k = [[1, 0], [−k, 1]] [[1, k], [0, 1]]`.
  - Invariant: the single form `Q_k(x) = x_1² − k x_1 x_2 + x_2²`. A first-order map on `R²` has one quadratic
    invariant, so MO-3 is judged on that one.
  - It keeps `P` and is reversed by `RA` (§1.3). It is the integer lifting scheme of the bit-reversible literature.
  - Route to failure: **none identified**. MO-3 enters G-GEN at H1, and the variation report at H2.

**Owner requirement 2, stated honestly.**
- The mechanism-off controls MO-1 and MO-2 can each fail the success criterion, by a named route. MO-1's route at H2 is
  a calibration check.
- The generic countercontrols GC, V-P, V-X and MO-3 can fail S-LH in the logical sense only: no route to failure is
  identified. They are kept because, if any of them passes, the design's pass is generic (`LH-GENERIC`). That is the
  case the owner excluded from counting as evidence.
- The only schemes with a known failure route, GC-NR and GC-R, fail through added forcing. They are therefore not
  admissible.
- `LH-DISCRIMINATING` is therefore not expected. If Stage 1B finds no admissible countercontrol that fails, Q-LH is not
  discriminating as frozen, and Stage 1B records that in those words.

### 6.4 Classical model and Theorem NC

- **Classical model.** S-CLASSICAL exhibits the carrier as a classical model. It is a standing fact, not a control.
- **NC's hypotheses.** NC (M2D:483–498; Lemma F at M2D:315–325) assumes Lemma F's operation set, H-LIFT, a linear
  identification of laws `μ ↦ Σ_λ μ(λ)A(λ)` by an orthogonal frame of unit-trace operators, and spanning reads.
- **Why it does not apply here.** The encoded description is an injective point map of configurations into `R⁴`, not
  a frame identification of laws, so the identification hypothesis is absent. In addition, the single sign read does
  not span.
- **MECH-2's consequence**, "change identification or access, not only dynamics", is not met in NC's sense. No
  operational identification is adopted, and no nonclassicality is claimed.
- **Refinement 2.** NC says nothing about states labelled non-stabilizer under other representations. This design
  asserts nothing of that kind.

### 6.5 Target-tuned countercontrols and the structural rule SR

**SR (frozen).** A construction satisfies SR iff all four conditions hold:
- **SR1.** It uses one parametrized primitive family `{S_k : k ∈ K}`, with `K` finite and independent of the settings.
- **SR2.** Each primitive updates each slot from one other slot by one rounded multiplication, followed by subtraction
  of that slot's previous value, and by nothing else.
- **SR3.** Settings enter only as words of fixed length 24.
- **SR4.** No table is indexed by setting, word or configuration.

| Construction | SR clauses failed |
| --- | --- |
| CC-TT (per-setting nearest-lattice-point permutation, completed by `exists_perm_extending`, loaded from a table; GA:92) | SR1, SR2, SR4 |
| CC-TT′ (rounding of each whole 24-word map) | SR2, SR4 |
| GC-NR, GC-R | SR2 (the kick) |
| MO-3 | SR2 (first-order, no memory) |
| F-NAT, F-B1, GC | none. F-B1's schedule is target-defined, recorded in §3.4 |

**The control.** Green iff Stage 1B, applying SR as written, reaches this table.
- Route to red: SR admits CC-TT or CC-TT′, or excludes F-NAT.
- The countercontrols MO-3 and the recorded pair GC-NR and GC-R need not satisfy SR. SR classifies constructions; it does not gate countercontrols.

### 6.6 Target-import check

| Criterion | Refers to | Allowed |
| --- | --- | --- |
| §2.3–§2.4 | Finite rules; real-linear comparators; `Q_B`; window laws | Yes |
| §3.3 | Classical oscillators; symmetries; finite precision | Yes, subject to a grep of §3.3 for: quantum, unitary, Born, completely positive, CP, qubit, Hilbert, density, rotation, Bloch, Pauli. Any hit voids the freeze |
| §0.1, §3.4, §7 | `T`, C-ROT, (iv), `exp(iθX)` | Only to classify, to scope and to record |

### 6.7 Robustness and replication (required before any positive is promoted)

- **RB-1.** The decisive bounds are re-derived by a reviewer who did not write Stage 1B.
- **RB-2.** The windows are varied: `q/2^6` and `q/2^{12}` at H1; `q/2^8` and `q/2^{12}` at H2, with `N_q` equal to
  the H2 window scale. These are reported only. A case undecided on paper is `INCONCLUSIVE`.
- **RB-3.** S-LH is repeated with `r(m) = m`.
- **RB-4.** S-LH is repeated for `q = 3^m`, with `A′_q = ⌊q/2^{10}⌋` and `r = ⌊m·log₂3/2⌋`. **Conditional on #1193**
  (odd modulus).

A positive with any RB item not green stays "mathematically sufficient, unreplicated".

## 7. Comparison with the quantum-completion conditions (recorded only, after §4–§6)

- **Cmp-1 (F-B1).** Under `z = x + iy`, `E_B1(θ)` acts as `exp(iθX)` (B1 §4). Record F-B1's H1 outcome at the notion
  of §2.2 and nothing stronger.
- **Cmp-2 (F-NAT).** Record whether `E_NAT(s)` commutes with B1's `J` for any `s ≠ 0`. B1:56–63 shows that a single
  nonzero primitive does not.
- **Cmp-3.** Record that C-ROT holds for every member of every family (S-FIN; AP1:955–977).
- **Cmp-4.** Record that (iv) is exact (Main:590), that it is not supplied here, and that the operational outcome is
  `NO-OPERATIONAL-QUESTION`.
- **Cmp-5.** In B1's density dictionary only, record that B1 §6's distinction between `I` and `−I` is carried (P-B1).

No entry here changes any outcome, status, label or rung.

## 8. Explanatory quality (AGENTS.md §A.29)

### 8.1 Preserved results

The preserved results are the §6.1 controls (C-BIJ, C-SYM, P-U2, P-B1, P-SM) and the §2.5 facts. M-INACC (#1198,
provisional) is respected through S-NOINACC, and none of its content is used.

### 8.2 Genericity clauses and the variation analysis

**G-GEN (H1).** For each family, Stage 1B states whether S-TUNE, S-INV and S-REC follow from one lemma whose only
hypotheses are:
- (h1) bijective second-order or first-order shear form;
- (h2) bounded per-step rounding error;
- (h3) no boundary crossing on the window;
- (h4) coefficient resolution tending to 0;
- (h5) a fixed-length comparator with bounded norms.

The H1 success is tagged `generic` iff the lemma suffices or MO-3 meets the same criteria against its own comparator.
A `generic` H1 success never counts toward hard-to-vary.

**G-GEN-H2.** For each of GC, MO-3, V-P, V-X and V-S, Stage 1B states whether the design's S-LH bound follows
from a lemma whose hypotheses that rule also satisfies. If it does, that rule counts as passing S-LH, both for §5.1 and
for the variation rule below.

**Variation rule.** Variations are judged at H2 only. A rounding approximation never counts toward hard-to-vary.
- Each variant is judged against its own primitive and its own two forms `Q_I` and `Q_X`.
- An assumption is **hard to vary** iff the design passes S-LH and at least one listed variant of that assumption
  fails it. A failure means a proof that no vanishing bound exists, and G-GEN-H2 may not count the variant as passing.
  The attribution also requires the matched-control rule of §5.1: the matched control, which differs from the variant
  only in that assumption, must pass. For V-P, V-X and GC the matched control is the design.
- An assumption is **easy to vary** iff every listed variant passes, directly or by G-GEN-H2.
- An undetermined case counts as neither.
- Excluded as a change of target: variants that remove resolution growth, and variants whose own continuum primitive
  conserves no pair of forms `Q_I`, `Q_X`.

| Id | Assumption | Exact variant | Symmetry set (§1.3) | Status |
| --- | --- | --- | --- | --- |
| V-P | Odd rounding (reflection) | Half-up `⌊t + 1/2⌋` in both slots | keeps `X`, reversed by `R`; breaks `P` | counted |
| V-X | Same rounding in both slots (relabelling) | Slot 1 rounds half away from zero, slot 2 half toward zero | keeps `P`, reversed by `R`; breaks `X` | counted |
| GC | Both separately | Slot 1 floor, slot 2 ceiling | reversed by `R`; keeps `XP`; breaks `X` and `P` | counted |
| — | Reversal by `R` | No admissible variant (§6.3) | — | not testable as frozen; no reversal credit |
| GC-NR, GC-R | (recorded pair) | §6.3 | GC-NR: keeps `P`, breaks `X`, not reversed by `R`. GC-R: the same with reversal restored | recorded only; not counted. Both add a bounded forcing, and the re-review of `1975c649` reasons that both fail at `k = 0` |
| V-S | No self-term (center-free) | `f(x)_i = ρ(k x̃_{3−i} + x̃_i/2)`. Own coupling `A = kX + I/2`, which is symmetric and translation-invariant, so SM:296's `Q_I` and `Q_X` apply with this `A` | keeps `X`, `P`, reversed by `R` | counted |
| MO-3 | Second-order form | §6.3; single invariant `Q_k` | keeps `P`; reversed by `RA` | reported; used in G-GEN; not counted |
| V-A | Symmetric coefficients | Coefficients `(k, 3k/2)`; non-symmetric `A`, so SM:296's forms do not apply | — | change of target; excluded |
| V-R | Resolution growth | `r` fixed at 3 | — | change of target; excluded |

**Explanatory label.** The label is **"poor explanation"** in each of these cases:
- the verdict is `COVERED-BY-EXISTING-RESULTS` or `GENERIC`;
- the H2 outcome is `LH-GENERIC`;
- every counted assumption is easy to vary.

Otherwise the label names each hard-to-vary assumption and its §3.4 class.

### 8.3 Reach

**RT-3′ (composites; Stage 0 row 13).** RT-3′ tests whether the mechanism also keeps the normal-mode structure of a
composite carrier.
- **Ring.** Four modes. The rounded rule acts on every site, with one rounding per site:
  `f(x)_i = ρ(k(x̃_{i−1} + x̃_{i+1}))`, indices mod 4. Its continuum coupling is `A = k(T + T⁻¹)`, where `T` is the ring
  translation.
- **Invariants.** By SM:296, the continuum keeps `Q_B` for `B ∈ {I, T + T⁻¹, T²}` and `P_C` for `C = T − T⁻¹`.
- **Pass condition.** RT-3′ passes iff the S-LH bound holds for all four forms over `n ≤ N_q` on the window
  `|t̃| ≤ A′_q`.
- **Failure.** RT-3′ fails if no vanishing bound exists for one of the four forms.
- **Preserved comparator.** Continuum invariance of the four forms is SM:296's statement. Stage 1B records it as the
  preserved comparator, so that a finite failure cannot be confused with a continuum impossibility.

RT-3′ can both pass and fail in principle. Like S-LH, it may be undecidable on paper.

**The r2 transfer-share test is withdrawn.** The reflection that fixes mode 1 and swaps modes 2 and 4 commutes with the
rule, so `x_2 = x_4` holds exactly. The test could never pass. Composite tests stated as transfer shares are decided by
the continuum comparator's linear algebra, and in the finite part they reduce to H1 tracking. They do not test the
mechanism.

**L3.** RT-3′ and Q-RED's literature comparison are consistency tests, not novel predictions. No novel, independently
checkable consequence has been identified, so **L3 is unreachable as frozen**.

### 8.4 Assessment ladder (monotone)

Each rung requires everything the rung below it requires.

- **L0:** some construction reaches an H1 positive.
  - CC-TT and CC-TT′, if evaluated, are at most L0, because they fail SR.
  - An F-B1 positive is L0, because F-B1 is target-defined.
- **L1:** L0, the construction satisfies SR, and the positive family is F-NAT.
  - A `generic` H1 success without `LH-DISCRIMINATING` stops here, labelled "poor explanation".
  - So do `COVERED-BY-EXISTING-RESULTS` and `GENERIC`.
- **L2:** L1 and all of the following. L2 is reachable in principle but is unlikely to be decided in Stage 1B (§0.1):
  - `NEW-POSITIVE`;
  - at least one counted assumption is hard to vary, with an independent §3.4 component;
  - RT-3′ passes;
  - the SR control is green.
- **L3:** L2 plus a novel, independently checkable consequence. Unreachable as frozen.

The following outcomes take no rung: `NEW-NEGATIVE`, `NEGATIVE-H1`, `INCONCLUSIVE`, `VOID`, `NO-OPERATIONAL-QUESTION`,
`BLOCKED-QB`.

### 8.5 Origin disclosure

**How the construction was found.**
1. The construction started from the anchors: the B1 mixer's unsourced real resources, and the finite-group bars.
2. The search then looked for an independent reason why a finite reversible system would follow a continuous two-mode
   exchange.
3. The oscillator motivation and SM §4.2's rounded rule came out of that search.

**What changed after review.**
- **r2 (after the first review and the owner's decision):** F-NAT, the three symmetries, Q-LH, GC and MO-3 were added.
- **r3 (after the re-review):** three further changes.
  - The second invariant `Q_X` was added. r2 bounded only total energy, which the mechanism-off map keeps exactly and
    which does not see the exchange.
  - GC-NR was constructed with a named failure route, because GC and MO-3 share reversal by an involution with the
    design.
  - RT-3′ replaced a reach test that could not pass.
- **r4 (after the re-review of `1975c649`):**
  - GC-NR was found by the reviewer to fail at `k = 0` through a resonant period-4 kick. The matched reversed control
    GC-R fails the same way, so the failure comes from the added forcing, not from the loss of reversal. GC-NR was
    removed from the discrimination and from the reversal attribution, and kept with GC-R as a recorded pair.
  - GC and MO-3 were restored to `LH-GENERIC`.
  - The matched-control rule and the admissibility condition were added.
  - The finding that reversal is not discriminated as frozen was recorded.

**How the discriminating test was chosen.**
- S-LH and its countercontrols were chosen so that a generic scheme can fail them. They were not chosen from the
  target's statistics.
- GC-NR was designed to have a failure route. That design choice made its failure certain, and its failure is due to
  forcing. It therefore counts toward nothing. No countercontrol in the frozen design has been tuned to fail.

**The rounding switch.** The rounding convention was changed in r2 from half-up rounding to rounding half away from
zero. The r1 convention is kept as V-P. If V-P passes S-LH, the switch made no difference to the outcome, and the
report says so.

**Disclosure and independence.** The target informed which candidates were looked for and which one was selected.
Disclosing this does not relax the independence requirement. It is why:
- §3.4 classifies the motivation as mixed;
- §5.4 excludes (a);
- §0.1 leaves to the owner whether Q-LH is a P-MIX question.

## 9. Invariant → checkpoint table (§A.41)

| Invariant | Checkpoint |
| --- | --- |
| Each revision commit changes exactly this file | `git show --stat` of each commit: one path |
| No computation, simulation, Lean or V3 in Stage 1A | Reviewer: no script, data or Lean file is added; §4 lists questions only |
| Carrier finite; no continuum or limit object | Reviewer reads §1.1, §2.5 and G-QB1–G-QB5 |
| Q-B not activated | `BLOCKED-QB` is pre-named. Grep §1–§8 for "limit", "Bloch", "sphere", "S²", "cosine-weighted": hits only in §3.1's rejected rows, the guards and disclaimers |
| No exact continuous-rotation claim | Each "exact" in §2 and §5 is a disclaimer, a finite-carrier fact, an exact symmetry of a finite rule, or the name of an exact comparator |
| S-LH sees the exchange | §2.4 bounds both `Q_I` and `Q_X` |
| Mechanism-off controls can fail, with named routes; countercontrols' routes stated honestly | §6.2 (MO-1 at H1; MO-1 at H2 as a calibration check; MO-2). §6.3 (GC, V-P, V-X and MO-3 marked "none identified"; GC-NR and GC-R recorded as failing through forcing and not admissible) |
| Generic passes force `LH-GENERIC`; failures count only against matched controls | §5.1 `LH-GENERIC` row; matched-control rule; §8.2 |
| No reversal credit as frozen | §6.3; §8.2 reversal row |
| H1 success never counts as hard-to-vary evidence | §8.2: variations judged at H2 only |
| Symmetry sets are correct and checked | §1.3 table; C-SYM |
| L2 reachable in principle | RT-3′ can pass and fail (§8.3) |
| "Vacuous" decidable | §5.1 definition |
| Approximation notions and horizons fixed before any result | §2.2 and §2.4 are quoted verbatim in the result note |
| Every odd-modulus statement conditional on #1193 | Grep for `3^m`, "odd modul" and "prime": hits only in §1.1, RB-4 and this row. Other hits of "odd" name a rounding's parity |
| Paper-undecidable items are `INCONCLUSIVE`; criteria immutable | §4's frozen sentence appears unchanged in the result note |
| No `readWriteSourced_*` citation | Grep hits only the disclaimers in the pins, this row and §10 |
| Links pinned to `main@9c201475` | Every `/blob/` link carries `9c201475ba6fd8f341591d14dd8e88db2e2aaa90` |
| Every outcome reported | Result note template: §5.1–§5.4 and §8 fields are all filled |

## 10. §A.42 item 8: references off main

| Reference | Used for | Class |
| --- | --- | --- |
| #1169 c.6720450946, c.6720342295, c.6719386464, c.6720678942; #1204 c.6720827308 | Authority, refinements, owner requirements (quoted with author and time) | Provenance (authorization) |
| #1169 c.6719708521, c.6719720616, c.6719723538 (Stage 0) | Row numbering and wording | Provenance. Row content is cited from Main, AP1 and M2D on main |
| PR #1202, A5-Q3 A1 §3 C2 | The classes in §3.4 | Provenance. The classes are restated here |
| #1198 (M-INACC, provisional) | K-7's reason; why S-NOINACC exists | Provenance. Its content is unused |
| Independent reviews of `eb3802ee`, `3f12b442` (#1204 c.6720796018, c.6720991687) and `1975c649` (PR #1204 record) | Changes in r2–r4; the recorded-pair reasoning in §6.3, which is attributed to the reviewer and re-checked in Stage 1B | Provenance. No criterion, category or attribution rests on the reviewer's reasoning |
| #1193 | Conditionality of RB-4 | Provenance (Issue) |
| #1188 | Reason not to cite `readWriteSourced_*` | Provenance (Issue) |
| #1147, #866, CTL | Supply obligations in §1.6 | Provenance |
| #1059 | Probability law, out of scope | Provenance (Issue) |
| #1173 reviews of B1 | Review status of B1 | Provenance. B1 is on main |
| Literature in §3.1, §3.3 and §4 | Candidates, motivation, Q-RED | External. Reading status is stated per item; [unverified] items decide nothing. No literature item is a premise of a criterion |

No commit or blob id is offered as support except `main@9c201475`, which is on main.
