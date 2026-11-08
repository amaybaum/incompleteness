# FHE-SEL-1 P-MIX: a finite-precision reversible two-mode exchange, preregistered (Stage 1A)

**Standing.** Stage 1A preregistration only, under #1169. WIP / UNVERIFIED; independent review pending.
Writer: Claude Code session, 2026-11-08. This file fixes one construction, its motivation, its criteria
and its controls before any result is evaluated. It derives no result, runs no computation, proposes no
premise for adoption, and changes no manuscript. Stage 1B (the derivations) is not authorized.

**Authority (quoted).**

- Owner decision, [#1169 c.6720450946](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6720450946)
  (recorded by amaybaum, 2026-11-08T10:38:44Z). P-MIX row: "Can a specified physical carrier produce
  reversible mixing without importing quantum operations? … Q-B remains inactive." Research boundary: "A
  finite-carrier P-MIX candidate cannot claim exact continuous rotations merely by changing its
  representation." And: "No computation, V3 execution, new physical axiom, manuscript change or Q-B
  activation is authorized." Stage 1B "is not yet authorized by this decision."
- Planning clarification, [#1169 c.6720342295](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6720342295)
  (amaybaum, 2026-11-08T10:26:34Z). P-MIX: "Can an independently motivated physical carrier and dynamics
  support the relevant reversible mixing?" Safeguard: "Must state whether the carrier is finite or
  continuum. Must not assume exact rotations or activate Q-B." Anchor: "On finite carriers, encoded
  unitaries form a finite group: Apparatus-1 excludes `rot`, and MECH-2 Theorem U2 applies. The #1173
  Gate B1 mixer's controls are unsourced. In Stage 0 this is the relating-evolution/lift rows." Three
  statuses per entry: proposed / mathematically sufficient / derived from native OI.
- FHE-SEL-1 decisions, [#1169 c.6719386464](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6719386464)
  (amaybaum, 2026-11-08T08:41:15Z): "Every candidate physical restriction must have an independent
  physical motivation established before evaluating whether it selects quantum behaviour. A restriction
  that eliminates an unwanted classical model is not automatically evidence that nature obeys that
  restriction." Unchanged: "Q-B stays inactive."

**Order of evaluation (fixed).** §3 independent physical motivation → §4–§5 mathematical consequences →
§7 comparison with the quantum-completion conditions. §7 is evaluated only after §4–§5 are recorded,
and nothing in §7 feeds back into §3–§5.

**Pins.** Every repository citation is to main `9c201475ba6fd8f341591d14dd8e88db2e2aaa90`
(`main@9c201475`). Line-number citations use these abbreviations, each a file at that commit:

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
  `substratumGen_not_control` (StructuralClosure.lean:348), `permTheory_not_control`
  (SubstratumInterfaceAudit.lean:708), `exists_perm_extending` (Equivalence.lean:60),
  `nonnegBounded_not_denseUnitaryControl` (FrozenSourcing.lean:173). No `readWriteSourced_*` identifier
  is cited (#1188: `ReadWriteSourced` is vacuous).

The Stage 0 map ([#1169 c.6719708521](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6719708521),
reviewed at [c.6719720616](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6719720616),
confirmed at c.6719723538; its standing line "pending" is stale) was written against `f88c1842`. Between
`f88c1842` and `9c201475` none of `papers/`, `oi-qm-ext-1/`, `apparatus-1-20261107/`,
`mechanism-2-20261108/`, `StructuralClosure.lean` or `Equivalence.lean` changed, so its line numbers
carry over unchanged.

## 0. Summary of what is frozen

| Item | Frozen choice |
| --- | --- |
| Carrier | **Finite.** One isolated pair of modes over `Z_q`, `q = 2^m`, with one-step memory, plus a finite controller and one fresh record cell (§1.1). No continuum carrier is used, assumed or taken as a limit object |
| Rule | SM's second-order form with a center-free symmetric two-site coupling, the coupling coefficient applied by finite-precision rounding (§1.2) |
| Relevant mixing | Approximate, uniformly in a tuning setting, of the continuum two-mode exchange family of B1 §4, under a fixed rescaled-sup-norm notion on a fixed window (§2). No exact claim of any kind about continuous families |
| Stage 0 rows | Row 7 (relating evolution / lift); the mixing part of §5's "(iv) / reversible control (9, 13)" entry, as comparison only (§1.4) |
| Motivation class | **Mixed** (§3.3); selection among candidates occurred (§3.1), so a positive is recorded (b) |
| Continuum branch | Not executed. Its outcome is pre-named `BLOCKED-QB` (§3.2, §5.6) |
| Ceiling | L3 unreachable as frozen (no novel independently checkable consequence identified, §8.3) |

## 1. Construction

### 1.1 Carrier, stated explicitly as finite

- **Modes.** `x = (x_1, x_2) ∈ Z_q²` (current) and `y = (y_1, y_2) ∈ Z_q²` (previous), `q = 2^m`,
  `m ≥ 1`. Claims are statements about the family `{q = 2^m}` with explicit `q`-dependent bounds (§2);
  each member is a finite carrier. No member is replaced by, or identified with, a real or complex space.
- **Controller.** A program register holding 24 coefficients in the finite set
  `K_q = { j / 2^{r} : j ∈ Z, |j| ≤ 2^{r} }`, `r = r(m) = ⌊m/2⌋`; a clock `ℓ ∈ Z_64`; a fresh ready bit
  `ρ_0 ∈ {0,1}` initialised to `0`. This is B1 §5's controller with the real coefficient interval
  `[-1, 1]` replaced by the finite set `K_q`.
- **Centered representatives.** For `t ∈ Z_q`, `t̃` denotes its representative in `(−q/2, q/2]`. This is
  a representation choice used only to define the rule's rounding and the read (§1.2–§1.3).

**Choice of `q`.** `q = 2` alone has too few values to carry any approximation; at `q = 2` the instance is
the domain of MECH-2 Theorem U2 and is used only as a preserved-result control (§6.1, P-U2). Odd `q` is
excluded, because statements at odd `q` are conditional on #1193 (memory sign). `q = 2^m` keeps the family
even and matches the alphabet size of SM §4.2's rounded-rule record (`q = 2^16`, SM:294).

### 1.2 Microscopic rule

For a coefficient `k = j / 2^r ∈ K_q`, define the rounded coupling map on `Z_q²`

```text
f_k(x) = ( ⌊(j·x̃_2 + 2^{r−1}) / 2^r⌋ ,  ⌊(j·x̃_1 + 2^{r−1}) / 2^r⌋ )   mod q        (r ≥ 1)
f_k(x) = ( j·x̃_2 , j·x̃_1 )  mod q                                                      (r = 0)
```

that is, `k·x̃` rounded half-up to an integer in each slot, and each mode reads only the other mode. The
primitive step is SM's second-order form (SM:106) on the pair:

```text
S_k : (x, y) ↦ ( f_k(x) − y ,  x ).
```

World update at clock `ℓ` (B1 §5's schedule, unchanged): for `ℓ ∈ {0,…,23}` apply `S_{k_ℓ}`, `k_ℓ` the
`ℓ`-th program coefficient; at `ℓ = 24` apply the copy `ρ_0 ↦ ρ_0 ⊕ 1[x̃_1 > 0]`; for `ℓ ∈ {25,…,63}`
leave modes and record unchanged; then `ℓ ↦ ℓ + 1 mod 64`. The program register is never written.

**Inherited, not derived here.** Every `S_k` is a bijection of `Z_q⁴` with inverse
`(u, v) ↦ (v, f_k(v) − u)`, for any map `f_k` (SM:106; B1:45). The copy is an involution. Given the new
clock value the previous opcode is known, so the world update is a bijection of the finite world
(B1 §5's argument, which uses only these facts). Stage 1B re-checks this; it is a control (C-BIJ), not a
result.

**Mechanism.** The mechanism under test is the conjunction of (i) the symmetric center-free two-mode
coupling, (ii) the second-order form, and (iii) finite-precision rounding of a dyadic coefficient. "Mixing
on" means programs with nonzero coefficients; "mixing off" is defined in §6.2.

### 1.3 Observer access, preparation, records

- **Read.** The only read is the sign record `1[x̃_1 > 0]`, copied at `ℓ = 24` into the fresh record cell
  and read passively for `ℓ ∈ {25,…,63}` (B1 §6). It is a deterministic configuration predicate; no
  sampling rule, re-preparation law or outcome-probability rule is posited.
- **Preparations.** (Pp) Point preparations of `(x, y)`. (Pw) The law `μ_W` uniform on the window `W_q`
  of §2.1, with `ℓ = 0`, `ρ_0 = 0`. Uniformity on a declared set is Main's maximal-entropy default
  (Main:56, 60; posit (iv)); it is used only to weight record disagreements in S-REC (§2.2).
- **Setting independence.** The prepared law of modes and record cell is fixed before `ℓ = 0`
  independently of the loaded program, and only the current instruction is read (GA:90–92; B1 §5).
- **Encoded description.** The encoded state of the pair is the rescaled configuration
  `(x̃, ỹ) / A_q ∈ R⁴`, `A_q` as in §2.1. This is a coarse, non-injective representation used to state
  §2's approximation; it is not an identification of any configuration with a vector of a continuum
  carrier, and it is never used to assign probabilities.

### 1.4 Stage 0 rows targeted

- **Row 7** (unitary representation; relating evolution; lift freedom). Column (c): "Relating evolution
  (Main:646)". Column (d): "None: Main:646 'neither supplies one nor says what form one must take'".
  P-MIX asks whether a specified finite carrier and rule fix the transformation relating two times of the
  pair, by the program executed between them, rather than by a choice of lift.
- **Stage 0 §5, entry "(iv) / reversible control (9, 13)"**, mixing part only: "a continuously tunable
  mixing operation (Main:590): assumed and target-adjacent … No independent candidate." This entry is
  addressed only in the §7 comparison. Its access and intervention part belongs to P-CONTROL and is not
  addressed here.

### 1.5 Source ledger

| Resource | Content | Class | Source / note |
| --- | --- | --- | --- |
| Finite alphabet `Z_q` | Configuration values | native | A1 (Sub:92), a posit; `q = 2^m` is a parameter choice (§1.1) |
| Second-order form | `x(t+1) = f(x(t)) − x(t−1)` | native | SM:106; A2 (Sub:94), a posit |
| Center-free symmetric coupling | Each mode reads only the other; same coefficient both ways | native (posit) | A4 (Sub:98); its no-self-term clause has open warrant (Stage 0 row 9) |
| Rounding of `k·x̃` | Half-up rounding of a dyadic multiple | supplied | Proposed rule component. SM §4.2 (SM:294, 298) records a rounded rule of the same type as a candidate realization, not adopted. A5 fails for it |
| Coefficient set `K_q`, resolution `r(m)` | Finite dyadic coefficients | supplied | Replaces B1's E-control by a finite controller alphabet; loading is not sourced (CTL; CPP) |
| Isolated pair | Omitted modes are spectators | supplied | B1's E-pair, unchanged |
| Controller clock and schedule | `Z_64` clock, 24-step program, copy at 24 | supplied | B1 §5; Stage 0 row 5: no clock source passes CTL's gate |
| Fresh record cell | Ready bit `ρ_0 = 0` | supplied | Ready-cell supply is open (#1147 per #1173 record) |
| Sign read | `1[x̃_1 > 0]` copied by an involution | supplied (access); native (map form) | B1's E-read |
| Preparations (Pp), (Pw) | Points; uniform on `W_q` | supplied (preparation); native posit (law) | Max-entropy posit (iv), Main:56, 60 |
| Centered representatives; window `W_q`; rescaling `A_q` | Scope of claims | representation | Restrict what is claimed; they act on no configuration |
| Continuum comparator `T[w]` | B1's real-linear words | imported (comparison object only) | B1 §3–§4, on main. Not a resource of the model |

No resource is classified native that the corpus states only as a posit without saying so. No supplied
entry may be counted as physically generated (owner boundary, c.6720450946).

## 2. The relevant mixing and the approximation notion (fixed in advance)

### 2.1 Comparator, programs, window

- **Comparator.** For a real `k`, `T_k(x, y) = (kXx − y, x)` on `R⁴`, `X` the exchange of the two slots
  (B1:36–45). For a program `w = (k_0, …, k_23)`, `T[w]` and `Φ_q[w]` denote the composed continuum and
  finite maps, applied right to left in clock order.
- **Tunable programs.** B1 §4's word: `Q_a = T_a T_0³`, `P_b = T_0 T_{−b} T_0²`, `C(a,b) = Q_a P_b Q_a`,
  program `w(a,b) = C(a,b)²` (24 primitives). For a setting `θ ∈ [−π, π]`:
  - `a_q(θ)` is the element of `K_q` nearest to `−tan(θ/4)`, ties toward 0;
  - `b_q(θ)` is the element of `K_q` nearest to `−2 a_q(θ) / (1 + a_q(θ)²)`, ties toward 0;
  - `w_q(θ) = w(a_q(θ), b_q(θ))`.
  Every setting uses the same 24-step duration (B1:114).
- **Window and scale.** `A_q = q / 2^8`. `W_q = { (x, y) : |x̃_i|, |ỹ_i| ≤ A_q, i = 1, 2 }`. For
  composition, `W_q^{(2)}` uses `A_q / 2` in place of `A_q`.
- **Error.** For a program `w` and a set `W`,
  `ε_q[w; W] = max_{(x,y) ∈ W} ‖ (Φ_q[w](x,y))~ − T[w](x̃, ỹ) ‖_∞ / A_q`,
  where `(·)~` takes centered representatives coordinatewise.

This is the only approximation notion. It is a uniform (worst-case) statement on the window, not an
average, and it compares the finite rule with the same coupled-mode dynamics over the reals. Changing the
notion after any result is evaluated voids the round.

### 2.2 Success criteria (each a statement about the finite family; no exact continuous claim)

- **S-BIJ.** For every `q` and every program, `Φ_q[w]` is a bijection of the finite world (control C-BIJ).
- **S-TUNE.** Stage 1B derives an explicit bound `B(q)` with
  `sup_{θ ∈ [−π, π]} ε_q[w_q(θ); W_q] ≤ B(q)` and `B(q) → 0` as `m → ∞`.
- **S-COMP.** An explicit `B_2(q) → 0` with, for all `θ, φ`,
  `max_{W_q^{(2)}} ‖ (Φ_q[w_q(θ)] Φ_q[w_q(φ)])~ − T[w_q(θ+φ)] ‖_∞ / A_q ≤ B_2(q)`, `θ+φ` reduced to
  `[−π, π]`.
- **S-INV.** An explicit `B_3(q) → 0` with `max_{W_q} ‖ (Φ_q[w_q(−θ)] Φ_q[w_q(θ)])~ − id ‖_∞ / A_q ≤ B_3(q)`
  for all `θ`. The inverse is a forward program of the same controller and duration; no time reversal is
  used.
- **S-REC.** An explicit `B_4(q) → 0` bounding, uniformly in `θ`, the `μ_W`-mass of window configurations
  whose finite sign record after `w_q(θ)` differs from the sign of the first coordinate of
  `T[w_q(θ)](x̃, ỹ)`.
- **S-FIN (standing fact, recorded, not a success).** At each `q` the available programs generate a
  finite permutation group of the finite world, and every program has finite order. Nothing in
  S-TUNE–S-REC is read as an exact property of any continuous family.

"Explicit" means a bound written in terms of `q`, the word length and `r(m)`, derived on paper. A bound
that holds only for a subset of `θ`, or only on a window shrinking faster than `A_q`, does not satisfy the
criterion as stated.

## 3. Independent physical motivation

### 3.1 Candidates considered (owner distinction (b)): search record

Corpus search terms at `main@9c201475` (papers, book, verification records): reversible, second-order,
rounded, floor, lattice gas, billiard, Margolus, Fredkin, Toffoli, symplectic, cat map, beat, discretized
rotation, quantum walk, quantum cellular. Literature: as listed per row. "Read" states what was inspected.

| # | Candidate | Carrier | Source | Decision | Reason |
| --- | --- | --- | --- | --- | --- |
| K-1 | Finite-precision reversible two-mode exchange (this design) | finite | SM:106, SM:294–298 (rounded rule); B1 §3–§4 (continuum template); Levesque & Verlet, *J. Stat. Phys.* 72, 519 (1993), bit-reversible integer integration (bibliographic record and abstract-level descriptions checked); discretized-rotation literature: Lowenstein, Hatjispyros & Vivaldi, *Chaos* 7, 49 (1997); Akiyama, Brunotte, Pethő & Steiner, arXiv:0704.3674; Akiyama & Pethő, arXiv:1206.3868 (bibliographic records checked; not read in full) | **selected** | Specifies a finite carrier, a fixed local reversible rule and a transfer between two distinguishable modes; replaces B1's unsourced real modes (E-real) and real coefficients (E-control) by a finite alphabet and a finite controller, which is the question the anchor poses |
| K-2 | Single-mode discretized rotation `(x, y) ↦ (⌊λx⌉ − y, x)` | finite (on `Z_q`) | Same literature as K-1 | rejected | Acts on one mode; a one-mode quarter-turn family is a phase-type operation, already a stated intervention (Main:590), not a transfer between two distinguishable states |
| K-3 | Linear modular rule with integer coefficients (class N; SM's exact rule) | finite | SM:296, 298; AP1; M2D | rejected as candidate; **used as mechanism-off control** | Modular multiplication does not approximate real multiplication on rescaled coordinates (SM:298: "reduction modulo `q` introduces no nonlinearity"), so only `k ∈ {0, ±1}` transfers exist; at `q = 2` the ceilings of AP1 and Theorem U2 already decide it |
| K-4 | Reversible lattice gases: HPP (Hardy, Pomeau & de Pazzis, *J. Math. Phys.* 14, 1746 (1973), from memory), FHP (PRL 56, 1505 (1986), cited in the hydrodynamics programme), the corpus hexagonal gas (HB) | finite | HB; hydrodynamics `PROGRAMME.md`:49 | rejected | Conservation-law-driven mixing here is ergodic relaxation, a different property: collisions permute occupation configurations (monomial at configuration level), there is no tunable setting, and the inverse of a coarse-grained relaxation is available as a forward word only at recurrence times |
| K-5 | Billiard-ball / conservative-logic CA (Margolus, *Physica D* 10, 81 (1984); Toffoli & Margolus, *Physica D* 45, 229 (1990); Fredkin & Toffoli 1982, read in CPP) | finite | CPP §1; O-RET records | rejected | Routing of discrete signals: a permutation of distinguishable states, which is monomial and falls under `permTheory_not_control` |
| K-6 | Linear symplectic maps on a finite torus (cat-map type; Arnold & Avez 1968, from memory) | finite | — | rejected | Linear over `Z_N`: covered by K-3's reasoning; their known association with stabilizer-type groups would make a selection target-adjacent |
| K-7 | State-dependent graphs `G_SM`, `G_σ` | finite (`q = 2`) | M2D; #1198 (provisional) | rejected | At `q = 2` under R1⊗n, Theorem U2 excludes reversible escape for every fixed bijection; `G_σ`'s protection fails within scope (provisional) |
| K-8 | Multi-cell finite encoding with a hidden parity (P-8 type) | finite | AP1 §5.2 | rejected | Q-A's object (quarter phase), not a tunable family; a finite tunable family needs carriers growing with resolution in any case |
| K-9 | B1 as stated (real modes, real coefficients) | continuum | B1 | rejected for the finite design; see §3.2 | Its E-real and E-control are the unsourced controls the anchor names |
| K-10 | Classical spin on `S²` with precession; Kochen–Specker model | continuum | AP1 §5.3–§5.4 (MP-2 row) | rejected | Is Q-B's own first decisive check (AP1:1032, 1082) |
| K-11 | Classical coupled oscillators with continuum amplitudes (Briggs & Eisfeld, PRA 85, 052111 (2012), cited by B1) | continuum | B1 §9 | rejected | Same as K-9 |
| K-12 | Quantum walks / quantum cellular automata (Aharonov, Davidovich & Zagury, PRA 48, 1687 (1993); Schumacher & Werner, arXiv:quant-ph/0405174), from memory | — | — | rejected | Target-defined: their dynamics is posited as quantum |
| K-13 | Cellular-automaton routes aimed at quantum mechanics ('t Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics*, Springer 2016; Elze, PRA 89, 012111 (2014)), from memory | finite | — | rejected | Target-defined: the stated aim is to obtain quantum mechanics |
| K-14 | Main's finite operational gluing / uniform continuum realization (Main:566, 598) | finite | Main | rejected as candidate; **used as target-tuned countercontrol** (§6.4) | The step map is built from the target instrument family (density register, preloaded seeds); GA:92 |

Selection among candidates occurred: K-1 was chosen over K-2–K-8 because it carries a tunable transfer
between two distinguishable modes on a finite carrier. That property is the object of the P-MIX question.
A positive is therefore recorded as owner distinction (b) at best (§5.3).

### 3.2 The continuum branch and Q-B

A continuum design (K-9–K-11) would posit real modes or a continuous phase space as physical. On such a
carrier the two-mode exchange is an exact continuous family. Q-B asks "What additional OI principle could
produce the continuous rotations" (AP1:1082); a continuum P-MIX design would be a proposal of exactly such
a principle, and its first decisive check is listed as Q-B's (AP1:1032). No reformulation was found that
keeps the relevant mixing and stays outside Q-B's scope. This design therefore does not execute a
continuum branch. Its outcome is pre-named **`BLOCKED-QB`**: the continuum version of the P-MIX question
is blocked by the inactive Q-B, and is reported as such in the portfolio record.

The finite design stays clear of Q-B by four frozen guards:

- **G-QB1.** No claim concerns any limit object of the family `{Z_{2^m}}`. "`B(q) → 0`" is a statement
  about a sequence of finite carriers.
- **G-QB2.** No read re-prepares a configuration from a law; the only read is a deterministic predicate.
- **G-QB3.** No cosine-weighted or other outcome-probability law is claimed, used or compared.
- **G-QB4.** No carrier whose representable laws contain a ball, sphere or any continuum is introduced.

### 3.3 Motivation, written without reference to the target

Two coupled oscillators exchange energy periodically: with all energy initially in one mode, the energy
passes to the other and back at a rate set by the coupling strength (small-oscillation theory, e.g.
Goldstein, Poole & Safko, *Classical Mechanics*, 3rd ed., ch. 6; from memory). The exchange is reversible
and conserves a quadratic energy. A physical register with finitely many values cannot hold a real
coupling coefficient or real amplitudes, so a finite-state version must replace multiplication by a real
coefficient with an operation on integers. Exactly reversible integer discretizations of Hamiltonian
dynamics exist for this purpose (Levesque & Verlet 1993), and the second-order form makes any such
integer update reversible (SM:106). SM §4.2 already uses a rounded integer coefficient in the same form to
realize the real coefficient `1/3` on a finite alphabet, for a reason unrelated to this question
(breaking the integrability of the linear rule, SM:294). The construction asks what remains of the
exchange when the oscillator pair is given finite precision.

### 3.4 Classification (Q3's standard)

The classes are those of the A5-Q3 record's amendment A1 §3, criterion C2 (PR #1202; off main), restated
here so that this file is self-contained. The target `T` is, for this construction, completion condition
(iv) in its mixing form: an exact continuously tunable state-mixing operation on the operational carrier
(Main:590), equivalently the failure of C-ROT (AP1 §1.2).

- **independent**: the motivation and its support do not presuppose `T` and are not designed to exclude
  a particular construction;
- **target-adjacent**: the motivation, taken alone, presupposes `T`, is equivalent to it on the class at
  issue, or is supported only by a consequence of it;
- **target-defined**: the stated reason is to obtain `T` or to exclude a particular construction;
- **mixed**: an independent component and a target-adjacent component, each identified;
- **none found**: after the search of §3.1.

| Component | Class | Basis |
| --- | --- | --- |
| Energy exchange of two coupled oscillators | independent | Classical mechanics; no reference to `T` |
| Center-free symmetric coupling | independent in its translation clause; open in its no-self-term clause | A4 (Sub:98); Stage 0 row 9 |
| Second-order reversible form | mixed | A2's motivation is mixed (Main:62, 66; Stage 0 row 4) |
| Finite alphabet | target-adjacent in part | A1 via E3 (Sub:80, 92; Stage 0 §3) |
| Rounding of the coefficient | mixed | Independent use in SM §4.2; here it is chosen because it lets a finite rule follow the continuum exchange, which is the P-MIX object and is adjacent to `T` |
| Choice of B1's word as the program family | target-adjacent | B1 was built to supply "a continuously driven mixing transition" (B1:7), the content of `T` |
| Selection of K-1 among K-1–K-14 | target-adjacent | Selected for carrying the P-MIX object (§3.1) |

**Overall: mixed.** Independent component: the coupled-oscillator exchange and the translation clause of
center-free coupling. Target-adjacent components: the program family taken from B1, the role assigned to
rounding, finiteness via E3, and the selection among candidates.

## 4. Mathematical consequences to be derived in Stage 1B (questions only)

Stage 1B, if authorized, derives on paper, in this order:

1. C-BIJ (§1.2) for the world update.
2. The bounds `B, B_2, B_3, B_4` of §2.2, or a proof that no bound tending to 0 exists for one of them,
   or a named gap.
3. Whether any configuration in `W_q` or `W_q^{(2)}` meets an alphabet-boundary crossing during a
   program. A crossing on the window is a failure of the affected criterion on that window, never a reason
   to change the window.
4. The variation analysis of §8.2 and the reach tests of §8.3.
5. Only then, the §7 comparison.

No exhaustive enumeration, simulation or numerical evaluation is part of Stage 1B under this design.
Any computation needs its own authorization; a computation would be evidence for the executor only, with
an exactness control.

## 5. Outcomes and decision rules (fixed in advance)

### 5.1 Outcome classes

| Outcome | Rule |
| --- | --- |
| `VOID` | Any control of §6 fails or is vacuous. No other outcome is rendered |
| `POSITIVE-APPROX` | All controls green; S-BIJ, S-TUNE, S-COMP, S-INV and S-REC hold with explicit bounds tending to 0 |
| `PARTIAL` | All controls green; S-BIJ and S-TUNE hold, and at least one of S-COMP, S-INV, S-REC fails or holds only with a non-vanishing bound or on a subset of settings |
| `NEGATIVE` | All controls green; S-TUNE fails (a proof that the uniform error does not tend to 0), or S-BIJ fails |
| `INCONCLUSIVE` | All controls green; a criterion is neither proved nor refuted on paper. The precise gap is named |
| `BLOCKED-QB` | The continuum branch (§3.2). Pre-named; not executed |

Every outcome is reported, whatever it is, in the portfolio record, with the three statuses of §5.2, the
owner label of §5.3, the ladder rung and explanatory-quality label of §8.

### 5.2 The three statuses

- **Proposed.** At this freeze: proposed, with motivation class mixed (§3.4), subject to independent
  review. Review may lower it to "not proposed" if it finds the independent component does not carry the
  construction.
- **Mathematically sufficient.** Recorded only for `POSITIVE-APPROX`, and only for the approximate
  statements of §2.2 under the hypotheses of §1 (isolated pair, finite controller, window). `PARTIAL`
  records sufficiency for the criteria that hold, each named.
- **Derived from native OI.** Recorded only if every ledger entry in §1.5 used by the positive is native.
  At this freeze the isolated pair, the rounding, the coefficient set, the clock, the record cell and the
  read access are supplied; this status can change only by sourcing those entries, which is outside
  Stage 1B.

### 5.3 Owner portfolio distinctions

- **(a) independently predicted positive**: requires motivation class independent and no selection among
  candidates. Neither holds at this freeze, so (a) is not available to this design.
- **(b) positive only after selecting among candidates**: the label for any `POSITIVE-APPROX` or
  `PARTIAL` outcome, citing §3.1 (selection across candidates) and §8.2 (selections inside the design:
  rounding convention, coefficient resolution, program word).
- **(c) reproduces quantum statistics but admits an equivalent classical imitation**: this design claims
  no outcome statistics beyond the deterministic record laws of S-REC. The carrier is a finite
  deterministic system, so every statistic it produces has a classical model, the carrier itself (§6.3).
  No outcome of this design counts as evidence of nonclassical behaviour. If any later reading of the
  outcome compares its record laws with a quantum law, label (c) is attached.

## 6. Controls

A verdict is rendered only over green controls.

### 6.1 Preserved results (also listed in §8.1)

| Id | Result preserved | Pass condition |
| --- | --- | --- |
| P-U2 | MECH-2 Theorem U2 (M2D:55–64, 404–412) | At `m = 1` the design asserts nothing inconsistent with U2's group `A_4 ≀ S_n` under R1⊗n. Since this design's encoded description is not Lemma F's frame identification (M2D:319–325), Stage 1B states that U2 does not apply to the rescaled description at `m ≥ 2`, and why |
| P-ROT | AP1 §5.3: no finite carrier induces `rot` with exact statistics (AP1:955–977) | No exact claim is made; S-FIN is recorded |
| P-CTRL | `substratumGen_not_control`; Main:590: finite bijective read-write dynamics does not supply the continuously tunable mixing operation | No outcome is phrased as exact (iv); §7 records approximation only |
| P-B1 | B1's algebra and its density-dictionary obstruction (B1 §4, §6–§7) | The continuum comparator is B1's. Stage 1B checks that the finite zero-coupling step `J = S_0` has `J⁴ = id` and that `J²` reverses all signs, so that the sign-record distinction of `I` and `−I` is carried, not removed; a failure of either check is a red control |
| P-GLUE | Main's uniform continuum and gluing theorems (Main:566, 598) | The design does not present approximate realizability as new; its question is whether a fixed, independently motivated rule supplies it |
| P-MINACC | M-INACC (#1198; provisional) | The design posits no inaccessible functional and no P1/P2 registration; no outcome claims protection of hidden information. If Stage 1B needs such a functional, MI's watch markers apply and the design halts as `INCONCLUSIVE` |
| P-C1–C4 | Main's C1–C4 theorems (Main:76, 82) | Evaluated as diagnostics for the partition visible = record cell, hidden = modes and controller. Each must agree with Main's theorems (C2-structural by reversibility, C3 capacity bound). They are never success criteria |
| P-SM | SM §4.2's records on the rounded rule (SM:294–298) | Nothing in Stage 1B assumes exact energy conservation, integrability or cycle ergodicity of a rounded rule, which SM states are not shown |

### 6.2 Mechanism-off controls

- **MO-1 (coupling off).** Every setting's program is replaced by the all-zero program, while S-TUNE's
  comparator stays `T[w_q(θ)]`. Stage 1B checks that the finite map is then the same for every setting
  and that the S-TUNE error does not tend to 0 for settings whose comparator differs from the zero-coupling
  map. A pass of S-TUNE with coupling off voids the criteria.
- **MO-2 (rounding off).** The modular linear rule with `K = {0, ±1}` and no rounding (K-3). The set of
  transfers reachable at fixed duration is finite and independent of `q`; S-TUNE must fail for it. A pass
  voids the criteria.

### 6.3 Classical-imitation countercontrol

The finite carrier with the law `μ_W` and its deterministic rule is an explicit classical ontological
model of every statistic this design produces. Theorem NC (M2D:483–498) assumes an injective
identification by an orthogonal frame with spanning reads; this design's encoded description is a
non-injective rescaling and its only read is one sign record, so NC's hypotheses fail here, and the
design states this rather than invoking NC. The countercontrol is the exhibited model itself. It passes
when Stage 1B confirms that the S-REC record laws are pushforwards of `μ_W` under the rule. MECH-2's
consequence (change identification or access, not only dynamics) is met by a change of identification,
and the design claims no nonclassicality from it.

### 6.4 Target-tuned countercontrol (must be rejected)

**CC-TT.** For each setting in a finite grid, take a permutation of `Z_q⁴` that sends each window
configuration to a nearest lattice point of the continuum image `T[w(θ)]`, completed to a bijection by
`exists_perm_extending`, and load the setting's permutation from a table (the K-14 pattern; GA:92). It
satisfies S-BIJ and S-TUNE-type bounds by construction. Rejection rule: a construction whose rule is
defined from the comparator family, or which loads a per-setting permutation table, is classified
target-defined and assigned L0 with explanatory label "poor explanation" (§8). If the decision rules of
§5 and §8 do not reject CC-TT when applied to it on paper, they are miscalibrated and no outcome is
rendered.

### 6.5 Target-import check

| Criterion | Refers to | Allowed |
| --- | --- | --- |
| S-BIJ–S-REC | Finite rule; B1's real-linear comparator; window law | Yes: classical objects only |
| §3.3 motivation | Classical oscillators; finite precision | Yes; the reviewer greps §3.3 for: quantum, unitary, Born, completely positive, CP, qubit, Hilbert, density, rotation, Bloch, Pauli. Any hit voids the freeze |
| §3.4 table, §7 | `T`, C-ROT, (iv), `exp(iθX)` | Only to classify and to record outcomes |

### 6.6 Robustness and replication (required before any positive is promoted)

- **RB-1.** The bounds are re-derived independently by a reviewer who did not write Stage 1B.
- **RB-2.** Scope variations reported alongside the result: window `A_q = q/2^6` and `q/2^{10}`;
  representatives `0, …, q−1` (SM's convention) in place of centered ones. These are representation
  choices: their variation is reported and does not enter §8.2's count.
- **RB-3.** One replication on the second program family named in §8.2 (V8).

A positive with any RB item not green stays at "mathematically sufficient, unreplicated" and is not
promoted as evidence for a physical selection principle.

## 7. Comparison with the quantum-completion conditions (recorded only, after §4–§6)

- **Cmp-1.** Under B1's fixed amplitude dictionary `z = x + iy`, B1 shows `T[w(a(θ), b(a(θ)))]` acts as
  `exp(iθX)` (B1 §4). Record what S-TUNE's outcome implies for an approximate tunable family in that
  representation, with the approximation notion of §2.1 and nothing stronger.
- **Cmp-2.** Record C-ROT as holding for every member of the family (P-ROT).
- **Cmp-3.** Record that condition (iv) in Main:590 is exact, and that no outcome of this design supplies
  it; record whether the approximate family is distinct, as a fixed local rule, from Main's
  target-constructed approximations (P-GLUE).
- **Cmp-4.** Record that B1's density-dictionary obstruction is inherited (P-B1): the sign record
  distinguishes programs whose standard density-channel actions agree.

No §7 entry alters §5's outcome class, §5.2's statuses or §8's rung.

## 8. Explanatory quality (AGENTS.md §A.29)

### 8.1 Preserved results

The results of §6.1 (P-U2, P-ROT, P-CTRL, P-B1, P-GLUE, P-MINACC, P-C1–C4, P-SM) are the construction's
preserved results. Each is a control: a Stage 1B derivation that contradicts one of them voids the
outcome unless the contradiction is itself established as a finding against that result, which then
needs its own review.

### 8.2 Variation analysis (decision rules; no prediction)

For each load-bearing assumption, Stage 1B applies the stated variation and asks whether the claimed
consequence, S-TUNE together with S-COMP, still holds under §2's notion. **Rule:** the assumption is
**easy to vary** if the consequence survives every listed variation, and **hard to vary** if at least one
listed variation destroys it (a proof that the uniform bound does not tend to 0). An undetermined case is
recorded as undetermined and counts as neither. Representation choices (window, representatives, scale)
are excluded (§6.6).

| Id | Assumption | Variations applied |
| --- | --- | --- |
| V1 | Finite alphabet `Z_{2^m}` | `Z_{3^m}` (conditional on #1193, stated as such); `Z_p` for primes `p` |
| V2 | Second-order form | A first-order bijective rule realizing the same continuum coupling to first order (e.g. a split shear `(x_1, x_2) ↦ (x_1 + ⌊k x_2⌉, x_2)` followed by its mirror) |
| V3 | Half-up rounding | Floor without offset; round half to even; rounding on representatives `0, …, q−1` |
| V4 | Symmetric center-free coupling | Asymmetric coefficients `(k, k(1+δ))` with fixed `δ ≠ 0`; adding a self-term `k'·x̃_i` with fixed `k' ≠ 0` |
| V5 | Isolated pair | The pair embedded in a ring of `n ≥ 3` modes with the same rule on every bond and the spectator bonds at coefficient 0 |
| V6 | Coefficient resolution `r(m) = ⌊m/2⌋` | `r(m) = m`; `r` fixed independent of `m` |
| V7 | Rounding of both `a` and `b` to `K_q` | Exact compensation dropped: `b_q` set to the nearest element to `−a_q` |
| V8 | B1's symmetric twelve-step word | The asymmetric word `Q_a P_b` followed by a phase correction by `J`-powers, same duration |

**Explanatory-quality outcome.** If every assumption V1–V8 is easy to vary, the outcome is labelled
**"poor explanation"**, whatever S-TUNE's result. If a hard-to-vary assumption is found, the label records
which, and whether its motivation component in §3.4 is independent.

### 8.3 Reach

Consequences beyond row 7 and the §5 (9, 13) entry that the mechanism would also have to fix, each a test
it can fail:

- **RT-1 (Stage 0 row 15; SM §4.2).** The same type of rounded second-order rule is SM's candidate for
  breaking integrability on the lattice. Decision rule: RT-1 passes if S-TUNE's derivation uses no
  property of rounded rules that SM:294–298 records as unestablished or contrary (exact energy
  conservation, integrability, cycle ergodicity, absence of boundary-crossing jumps off the window); it
  fails if it needs one.
- **RT-2 (Stage 0 row 7, lift classification; Main:646).** If the program fixes the relating evolution,
  two programs whose encoded actions agree must agree on every native record. Decision rule: RT-2 fails if
  two settings with `ε`-equal encoded actions under §2.1 give different sign-record laws on a
  `μ_W`-mass not tending to 0.
- **RT-3 (composites; Stage 0 rows 9, 13).** Under V5's embedding, the exchange on the addressed pair
  must leave the spectator modes within the same `ε`-notion of their initial configurations. Fails if
  not.

No consequence identified here is a novel prediction checkable against independent data or independent
mathematics: RT-1–RT-3 are internal consistency tests. The discretized-rotation literature (K-1 row) bears
only on single-mode maps, and the two-mode rounded rule does not reduce to them unless Stage 1B shows an
exact reduction. **L3 is therefore unreachable as frozen.**

### 8.4 Assessment ladder

Each outcome is recorded at one rung, alongside (a)/(b)/(c):

- **L0**: `POSITIVE-APPROX` or `PARTIAL` holds.
- **L1**: L0, and §8.2 labels it "poor explanation", or the positive depends on a choice among V3, V6,
  V7 or V8 with no motivation beyond reaching the criteria.
- **L2**: L0, at least one hard-to-vary assumption whose §3.4 component is independent, RT-1–RT-3 pass,
  and the design's independently motivated constraints reject CC-TT and the V7 family (non-target
  alternatives) without reference to the comparator.
- **L3**: L2 plus a novel independently checkable consequence. Unreachable as frozen (§8.3).

`NEGATIVE`, `INCONCLUSIVE`, `VOID` and `BLOCKED-QB` take no rung.

### 8.5 Origin disclosure

The construction was found by starting from the question's anchors: the B1 mixer, whose real modes and
real coefficients are unsourced, and the finite-group results that bar exact families on finite
carriers. The search then looked for a reason, independent of those anchors, why a finite reversible
system would follow a continuous two-mode exchange approximately. The coupled-oscillator motivation and
SM §4.2's rounded rule were identified in that search; the program family is taken from B1, which was
written to supply the target's mixing transition. The target informed which candidates were looked for
and which was selected. Disclosing this does not relax the independence requirement; it is the reason
§3.4 classifies the motivation as mixed and §5.3 excludes (a).

## 9. Invariant → checkpoint table (§A.41)

| Invariant | Checkpoint |
| --- | --- |
| One commit adds exactly this file | `git show --stat` of the commit: one path, `fhesel1-p-mix-20261108/DESIGN.md` |
| No computation, simulation, Lean or V3 in Stage 1A | Reviewer: the commit adds no script, data or Lean file; §4 lists derivations as questions only |
| Carrier finite; no continuum carrier or limit object claimed | Reviewer reads §1.1, §2.2, G-QB1–G-QB4 |
| Q-B not activated | Continuum branch pre-named `BLOCKED-QB` (§3.2); grep of §1–§8 for "limit", "Bloch", "sphere", "S²", "cosine-weighted": hits only in §3.1's rejected-candidate rows, §3.2's guards and disclaimers |
| No exact continuous-rotation claim | Grep for "exact" in §2 and §5: each hit is a disclaimer or a finite-carrier fact |
| Motivation free of target vocabulary | §6.5 grep of §3.3 |
| Approximation notion fixed before any result | §2.1 frozen; Stage 1B's result note quotes §2.1 verbatim and diffs it |
| Controls green before any verdict | Stage 1B result note lists §6 controls with status before §5's outcome |
| Odd `q` only as conditional on #1193 | Grep for odd-`q` statements: only §1.1 and V1, each conditional |
| No `readWriteSourced_*` citation | Grep hits only the disclaimers in the pins, this row and §10 |
| Links pinned to `main@9c201475` | Grep for `/blob/`: every hit carries `9c201475ba6fd8f341591d14dd8e88db2e2aaa90` |
| Every outcome reported with statuses, label, rung | Stage 1B result note template: §5.1–§5.3, §8.2, §8.4 fields all filled |

## 10. §A.42 item 8: references off main

| Reference | Used for | Class |
| --- | --- | --- |
| #1169 c.6720450946, c.6720342295, c.6719386464 | Authority, questions, safeguards (quoted) | Provenance (authorization) |
| #1169 c.6719708521 (Stage 0 map), c.6719720616 (review), c.6719723538 | Row numbering and row wording of §1.4 | Provenance for numbering. The rows' content is cited here from Main:590, Main:646, AP1, M2D, all on main |
| PR #1202, A5-Q3 amendment A1 §3 C2 | Classification classes of §3.4 | Provenance. The classes are restated in §3.4, so no claim rests on the off-main text |
| #1198 (M-INACC, provisional) | P-MINACC control | **Support off main: a gap.** Used only as a preserved-result control; no claim of this design rests on it, and P-MINACC is satisfied by positing no inaccessible functional |
| #1193 (odd `q`) | Reason to exclude odd `q` | Provenance (Issue) |
| #1188 | Reason not to cite `readWriteSourced_*` | Provenance (Issue) |
| #1147, #866, CTL | Ready-cell and controller sourcing obligations in §1.5 | Provenance; they name open obligations, not support |
| #1173 reviews of B1 | Review status of B1 | Provenance. B1's content is on main |
| Literature in §3.1 | Candidate record | External; reading status stated per row; none is a premise of a criterion |

No full commit or blob id is offered here as support except `main@9c201475`, which is on main.
