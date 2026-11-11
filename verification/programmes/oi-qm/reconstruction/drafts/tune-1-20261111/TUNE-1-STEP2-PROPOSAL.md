# TUNE-1, Step 2 proposal: derived-access coherent qubit operations

**WIP / UNVERIFIED drafting record. A proposal for owner approval; not executed.** Research unit
under Issue #1236 (owner decision: paper-only). This file plans one question and fixes, before any
work, its definitions, decision rule, controls and stopping rule. It runs no Step 2 work, performs
no computation, adopts no premise, advocates and evaluates no candidate mechanism, changes no
manuscript or Lean file and authorizes nothing. Execution needs the owner's recorded approval of
this text (or of an amended text) after the reviews named in section 10.

**Base.** Branch `research/tune-1-20261111`, drafted on head `d3d12426` (TUNE-1-STEP1.md r5a, the
reviewed Step 1 head, unchanged here). The branch descends from the Step 1 pin
`cac5d26441dd33e9348151487e4df7b547195481`, and every line number below is a line number at that
pin; as Step 1 records, each cited line of `papers/Main.md` is two lower at `082c3eaa`.

**Labels.** As in Step 1: **[K]** a Lean statement under `verification/lean-mathlib/OIBridge/`
("OB/" below), statement read, nothing built; **[P]** a manuscript statement on `main`
(**[P-imp]** with an imported half); **[R]** a research record on `main` that states it is not
independently reviewed; **[W]** this writer's own short argument, unreviewed and not
kernel-checked. A [W] step that extends a [K] statement beyond its scope is tagged [W], never [K].
"Step 1" means `TUNE-1-STEP1.md` in this directory, with its section labels (B.12, C, D1–D12,
F.1, F.2).

***

## 0. Plain-language summary

Step 1 found that wherever quantum-like behaviour appears on `main` from a world that only
reshuffles its configurations, someone chose by hand what the observer may prepare and read. This
proposal plans one question: can that hand-choice be removed?

Take the lattice rule OI already uses. Fix once a lattice region as the observer's
apparatus. Let the observer read everything in that region, at every step, and let its only choices
be which settings it writes into its own cells. Does what this observer can do and see then behave
like one quantum bit, to any wanted precision, over experiments of any wanted length? That means
smoothly adjustable reversible operations that compose correctly, two incompatible measurements,
and statistics produced by the dynamics.

It counts only if one apparatus serves every setting and nothing quantum is put in. Controls check
that the test has teeth: models with hand-chosen access, or with the quantum answer stored inside
(as in Main's approximation theorems), must be classed "supplied"; a classical wave or diffusion
that looks rotationally symmetric at large scales must fail; a known one-qubit model must pass the
"acts like a qubit" part and fail the "derived access" part.

Outcomes: pass; fail, for a stated class only; inconclusive, with a named gap; or void, if a
control fails. A pass would not establish the Born rule's selection, contextuality, Bell
correlations, composite systems or quantum mechanics. Paper work only; nothing adopted. Fresh
internal and ChatGPT reviews come before the owner decides.

***

## 1. The question

### 1.1 Rule and carrier: what "a single fixed OI dynamics" means

**Alphabet and phase space.** Fix an integer `q ≥ 2` and `V = ℤ/qℤ`. For a set of sites `Λ` the
phase space is `X_Λ = (V × V)^Λ`, a pair (previous value, current value) at each site.

**Rule class 𝓡.** One step is the second-order update

> `Φ_F : (y, x) ↦ (x, F(x) − y)`,

the form of Main:726 item (xiii), "a posit of the selected lattice model, not derived and not an
axiom of OI", already in the posit ledger [P]; its kernel form is `ruleDynamics`
(OB/SecondOrderDrive.lean:339) [K]. Using it adds no premise. Two members are named; the owner
chooses which enter (section 9, choice 1).

- **R-lin** (reference). `F` is the nearest-neighbour sum on the simple cubic lattice, the
  instance of Main §3.2 at `q = 2` (Main:726 item (xiii)) and the exact rule of SM:296 with
  `α = 1` at general `q`. It is linear (item (vii)), translation-invariant, of range one (item (ix)), on a
  site-factorized configuration space (item (viii)). One fixed `F`; no class of couplings is
  quantified over, so no coupling can be fitted.
- **R-nl** (owner option only). The rounded bijection of SM:294,
  `x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q` on the representatives `0, …, q−1`. It has the
  second-order form, so it is a bijection [W: `(x, z) ↦ (g(x) − z, x)` inverts it], but it is not
  linear and so is not covered by ledger item (vii); SM:298 and SM:1416 call it a separate
  realization.

**Excluded from 𝓡**, because Step 1 shows each is unsourced (Step 1 B.12, row
`two-mode-drive.md`; section C, B1 row): real-valued sites (E-real), an isolated pair (E-pair),
an externally loaded or switched coefficient (E-control), and any carrier added to the lattice
(per-site continua, `p`-adic or recursive substates, a continuum sphere). Recursive structure
enters only as structure of the fixed rule acting on the lattice, for example nested or
multi-scale apparatus regions (section 1.2); it does not enter as an added carrier.

**Carrier class 𝓛.**

- `𝓛_fin`: the tori `Λ_L = (ℤ/Lℤ)^3`, `L ≥ 1`. The world is finite for each `L`; `L` is a
  resource and may grow with the requested precision and horizon. This stays inside the
  manuscripts' finite construction (Main:726 item (ii)).
- `𝓛_∞`: the lattice `ℤ^3` with the finite alphabet `V`, the setting of the kernel's quasilocal
  interface (Step 1 B.12). It enters only under a named hypothesis **H-∞** ("the world is the
  infinite lattice"), carried into every conclusion that uses it. H-∞ is not adopted (Issue #1236:
  no new physical premise; Step 1 B.0).

**The alphabet is fixed.** `q` is fixed for each verdict; statements are made for each fixed `q`.
A family in growing `q` needs a correspondence between alphabets that SM §2.7 states "is not
constructed here" (SM:94) and is not part of this question.

### 1.2 The embedded apparatus

An **interface** is `I = (Λ, O, C, τ, r_O, μ)`:

- `Λ ∈ 𝓛`, the world;
- `O ⊂ Λ`, a finite **observer region**, and `C ⊆ O`, its **control cells**;
- `τ ≥ 1`, the duration of one **round**, in ticks, the same for every label;
- `r_O ∈ (V × V)^O`, a fixed **ready configuration** of `O`;
- `μ`, the law of the configuration of `Λ ∖ O` at time zero, independent of everything the
  observer does (hypothesis **H-μ**, section 1.3, D3).

**Labels.** A label is a configuration `c ∈ (V × V)^C`. The menu is every configuration of `C`;
no label is selected or excluded.

**Rounds and protocols.** At the start of round `j` the observer exchanges the content of `C` with
the label `c_j`, held in its own register. Exchanges of configurations are access the stated
architecture already supplies (`obs_exchangesAvailable`, Step 1 A.3) [K]. Then `Φ_F` runs `τ`
ticks on the whole world, unchanged. The record of the round is the **complete history of `O`**:
its configuration at each of the `τ` ticks, `h_j ∈ ((V × V)^O)^τ`. A **protocol of horizon `K`**
is a policy that chooses `c_1, …, c_K`, each `c_j` a function of `h_1, …, h_{j−1}` (adaptive), and
may declare a **herald**, an event on the records on which the run is accepted, with its raw
acceptance probability reported and no renormalization of rejected runs
(`observation-context-protocol.md`:45 [R]). `Π_K(I)` is the set of such protocols. The **record
law** `P^I_π` is the law of `(h_1, …, h_K)` under `μ`, the ready configuration and the dynamics.

**Initial-condition mode** (owner option, section 9, choice 5): all labels of a non-adaptive
protocol are written at time zero into disjoint control blocks of `O`, laid out by a fixed rule,
and no exchange occurs afterwards. Every observer choice is then an initial condition, as in Main's
program register (Main:582).

**Family.** A family is `{I_n}_{n ∈ ℕ}` produced by one generating rule `n ↦ I_n` (for example the
`n`-fold scaling of a fixed pattern of `O` and `C`), stated before any statistics are examined.
The resource of `I_n` is `N(I_n) = |Λ_n|` on `𝓛_fin`, and on `𝓛_∞` the number of sites of `O_n`
plus those of its light cone over the protocol's duration, finite by the range bound.

### 1.3 Derived versus supplied: the criterion

A family is **derived** iff it satisfies D1–D7. It is **supplied** iff it fails at least one.
Each clause is stated so that a reader can check it from the specification of the family alone.

- **D1 (one interface for all targets).** The generating rule `n ↦ I_n` is fixed before the
  comparator is consulted and does not depend on the target operation, on the requested angle,
  on the protocol or on the outcome. For each `n` one `I_n` serves every label, every protocol of
  `Π_K` and every target. Only `n` may depend on the requested `(ε, K)`, through the stated
  function `n(ε, K)`.
- **D2 (embedding).** The only dynamics is `Φ_F` with `F` from 𝓡 on the whole world. The observer
  acts only by the label exchanges of section 1.2 (or by initial conditions, in
  initial-condition mode). No coefficient is loaded, no step is switched off or replaced, no
  region is isolated, and the round duration `τ` is the same for every label and every
  configuration.
- **D3 (ensemble).** `μ` is one declared law for the whole family, chosen without reference to
  the comparator: the reference law is the uniform law on `(V × V)^{Λ∖O}` (on `ℤ^3`, the uniform
  product law). The stated architecture fixes no ensemble (stochastic observer-interface audit,
  `verification/audits/operational/stochastic-observer-interface-audit.md`:369–381; Step 1 B.12
  (ix)), so H-μ is a named hypothesis and every conclusion carries it. Robustness requirement: a
  result counts as derived only if it is also stated under one second declared law `μ′` with the
  same symmetries (section 9, choice 6); if it holds under `μ` and fails under `μ′`, the verdict
  records the measure as supplied (Step 1 F.1, control 2).
- **D4 (readout).** The observer's record is the complete history of `O`. No pointer function,
  response function, threshold or decoder is chosen. Outcome probabilities are the pushforward of
  `μ` through the dynamics; this is the **derived readout rule** the owner requires, and nothing
  else is called a readout rule.
- **D5 (no access by declaration).** Every protocol of `Π_K(I)` is admitted. No read, label or
  herald is declared unavailable. Information is inaccessible only if it lies outside `O` when it
  would be read. A restriction that is not a consequence of D1–D4 makes the family supplied.
- **D6 (no quantum input; vocabulary boundary).** The specification of the family uses no quantum
  object or target quantity: no amplitude, density matrix, unitary, Kraus operator, Born weight,
  rotation, cosine or sine, orthogonal-matrix dynamics, or operational-control predicate (the
  boundary frozen in the pair-flow equivalence audit, quoted in Step 1 F.1, control 12). These
  words occur only in the comparator (section 1.4).
- **D7 (rule class).** `F ∈ 𝓡` as fixed by the owner; `Λ ∈ 𝓛`; none of E-real, E-pair,
  E-control or an added carrier.

The criterion is aimed at the two ways the answer has been supplied on `main`: a per-target choice
of access, measure or decoder (D1, D3, D4, D5), and the quantum rule placed in the hidden state
(D6), as in Main's realization theorems, where "Quantum mechanics enters as the instrument data
and as the state held in the hidden register" (Main:582) [P].

### 1.4 The operational target: what "approximately coherent two-state operations" means

**Comparator.** A **qubit model** `𝔔 = (ρ₀, {𝓘_c})` is a density operator `ρ₀` on `ℂ²` and, for
each label `c`, an instrument `𝓘_c = {𝓘_{c,h}}_h` on `ℂ²` with outcome set the round records `h`.
For a protocol `π`, `P^𝔔_π(h_1, …, h_K) = Tr(𝓘_{c_K,h_K} ∘ ⋯ ∘ 𝓘_{c_1,h_1}(ρ₀))`, with the
labels chosen by the same policy and the same herald. The model is fixed for all protocols at a
given `n`: it is chosen once, not per protocol, setting or outcome (`endpoints.md`:67 [R]).

**Distance.** `d_K(I, 𝔔) = sup_{π ∈ Π_K(I)} TV(P^I_π, P^𝔔_π)`: total variation on complete
multi-time records, over every adaptive protocol of horizon at most `K`. Later reads in the same
protocol test every outgoing state, so no separate state distance is needed. A diamond-norm
bound on the comparator side converts to this distance by Main's telescoping Lemma (Main:596)
[P].

**Operational conditions** at error `ε` and horizon `K`, for one interface `I`:

- **Q0 (resources).** `N(I) ≤ N(ε, K)` for an explicit function `N`, finite at every `(ε, K)`.
- **Q1 (two-state capacity; model-free).** Some two preparations (protocol prefixes, heralded or
  not) are distinguished with error at most `ε` by some continuation, and no three are pairwise
  so distinguished.
- **Q2 (one fixed qubit model).** There is a qubit model `𝔔` with `d_K(I, 𝔔) ≤ ε`.
- **Q3 (a dense coherent family).** For a fixed axis `n̂`, every `θ ∈ [0, 4π)` has a label `c(θ)`
  with `Σ_h ‖𝓘_{c(θ),h} − p_h(θ) · Ad(e^{−iθ n̂·σ/2})‖_⋄ ≤ ε` for some probability vector
  `p(θ)`: the round acts on the qubit as the unitary channel, and its record carries at most `ε`
  information about the qubit.
- **Q4 (composition; model-free).** For all `θ₁, θ₂`, replacing two consecutive rounds
  `c(θ₁), c(θ₂)` by `c(θ₁ + θ₂), c(0)` in any protocol of horizon `K` changes the law of all later
  records, and of the records of those two rounds after marginalization, by at most `ε`.
- **Q5 (incompatible sharp reads).** Two labels, with two-class coarse-grainings of their records,
  are represented in `𝔔` within `ε` of rank-one projective measurements `{P_a, 1 − P_a}` and
  `{P_b, 1 − P_b}` with `Tr(P_a P_b) ∈ [1/4, 3/4]`.
- **Q6 (the whole Bloch ball).** The states `𝔔` assigns to preparation prefixes are `ε`-dense in
  the pure states of `ℂ²`, not only in one great circle.

**One direction each, to be proved in method step M2** (§A.34). Q2 implies the upper half of Q1
for `ε` below an explicit constant (approximate form of Lemma 2 of `whole-model-bridge.md`:167–178
[R]). Q2 and Q3 imply Q4 with error a fixed multiple of `ε`. Neither converse is claimed. Q1 and
Q4 are kept as separate conditions because they can be checked without any model.

**Uniformity.** "Uniform finite-precision error bound" means: one `ε` holds for every target `θ`
and every protocol of `Π_K`, at the one interface `I_{n(ε,K)}`.

**Relation to the kernel's two obligations.** The C5 discovery audit separates a relative-phase
resource (O1) from a continuous coherent transition (O2), each with a countermodel lacking the
other (`verification/audits/foundations/c5-discovery-audit.md`:25–37, :59–62) [K for the modules the audit cites, as it reports].
On the operational quotient Q3 plays the part of O2, and Q6 carries the complex structure that a
one-axis family with real reads lacks: rotations about one axis acting on reads in one plane give
real quantum theory of one system, a disk (a rebit) [W]. Q3 without Q6 is therefore reported
separately (token `PARTIAL-REBIT`, section 2).

### 1.5 The question, stated once

> **TUNE-1/Q2.** For the rule class 𝓡 and carrier class 𝓛 fixed by the owner, does there exist a
> derived family of interfaces `{I_n}` (D1–D7) and an explicit function `N(ε, K)` such that, for
> every `ε > 0` and every horizon `K`, the interface `I_{n(ε,K)}` satisfies Q0–Q6 at error `ε` and
> horizon `K`?

In words: can one fixed OI dynamics, observed through an apparatus region chosen once and read
completely, produce operations that agree, to any requested precision over complete multi-time
records of any requested length, with one qubit carrying a dense one-parameter family of
coherent reversible operations that compose, two incompatible sharp measurements and every pure
state, with no gate, preparation law or decoder chosen for the target?

This is the question proposed in the external assessment of Step 1, with each word made
operational: "single fixed OI dynamics" is section 1.1; "observational access derived from an
embedded apparatus" is section 1.2 with D1–D7; "approximately coherent two-state operations" is
Q2 and Q3; "uniform finite-precision error bounds" is Q0 and the uniformity clause; "preserving
composition" is Q4; "complete observable histories" is the distance `d_K`; "one reusable physical
interface" is D1.

### 1.6 Owner decisions this question implements

| Owner decision (Issue #1236, 2026-11-11, and the original authorization) | Where it enters |
|---|---|
| Target reading (B): what an embedded observer can prepare and measure; agreement in experiments, not a quantum description of configurations | Q2 compares record laws only; no clause reads a representation of the configurations (control C-REP) |
| Approximate first | Q0–Q6 at error `ε`; exact rotations are not asked |
| One quantum bit | The comparator is `ℂ²`; Q6 asks for the whole Bloch ball |
| Amplitude rotations count only together with a derived readout rule | Q3 is never sufficient alone; D4 fixes the readout as the pushforward of `μ` |
| "without introducing an independently postulated quantum rule" | D6 |
| "I do not want us to assume that finite observational access necessarily means finite underlying dynamics" | Both carrier classes are admitted; neither is inferred from the other; control C-CARD |
| Born probabilities, Kochen–Specker contextuality and Bell are separate obligations (Step 3) | Section 2.3: none is decided or claimed here; H-μ stays a named hypothesis |

***

## 2. Decision rule

### 2.1 Tokens and conditions

Let `𝕀_D` be the set of derived families for the owner's 𝓡 and 𝓛. The tokens:

- **`PASS-DERIVED`**: a family in `𝕀_D` and an explicit `N(ε, K)` are exhibited, and Q0–Q6
  are proved for every `ε > 0` and every `K`, under H-μ and, if used, H-∞, with the robustness
  clause of D3 met.
- **`FAIL-CLASS(𝓢)`**: for a stated subclass `𝓢 ⊆ 𝕀_D` it is proved that there are `ε₀ > 0` and
  `K₀` such that no member of any family in `𝓢`, at any resource, satisfies Q1–Q6 at `(ε₀, K₀)`.
  `𝓢` is named by its rule, carrier, ensemble, mode and any further restriction; the token never
  states more than `𝓢`.
- **`PARTIAL-x`** (reported only if the owner says so; section 9, choice 8): a family in `𝕀_D`
  for which a stated proper subset holds. `x` is one of: `REBIT` (Q0–Q5 without Q6); `NOCOMP`
  (Q3 without Q4 at the uniform bound); `FIXEDK` (Q0–Q6 for one stated `K` only);
  `NONADAPTIVE` (Q0–Q6 for non-adaptive protocols only).
- **`OPERATIONAL-ONLY`**: Q0–Q6 hold and some D-clause fails. This is the classification of a
  supplied construction. It is not a verdict on the question and never counts towards a pass.
- **`INCONCLUSIVE(gap)`**: none of the above is reached within the effort bound (section 7). The
  gap names the lemma that was not proved, with its exact statement.
- **`VOID(control)`**: some control of section 3 is not green when the verdict would be rendered,
  or a link of the verdict rests on a premise that section 5 shows unsupported.

### 2.2 How the token is generated

The result note carries two tables in a stated schema (§A.44): a **condition table** with one row
per condition used (identifier, exact statement, status `proved` / `refuted` / `open`, layer
[K]/[P]/[P-imp]/[R]/[W], source file:line), and a **control table** (section 3; identifier,
expected classification, obtained classification, status `green` / `red`). The token is computed
from the two tables in this order, and from nothing else:

1. If any control is red, or any row the verdict uses is `open` while presented as `proved`:
   `VOID(that row)`.
2. Else, if Q0–Q6 and D1–D7 are `proved` for one family over every `(ε, K)`: `PASS-DERIVED`.
3. Else, if a `FAIL-CLASS` theorem is `proved` for `𝓢 = 𝕀_D`: `FAIL-CLASS(𝕀_D)`. If it is proved
   for a proper subclass only: `FAIL-CLASS(𝓢)` together with `INCONCLUSIVE(gap)` for
   `𝕀_D ∖ 𝓢`.
4. Else, if a `PARTIAL-x` row set is `proved` and the owner has asked for partials: `PARTIAL-x`
   together with `INCONCLUSIVE(gap)` for the rest.
5. Else: `INCONCLUSIVE(gap)`.

A candidate family encountered during the work that is classified `OPERATIONAL-ONLY`, or that
fails a Q-condition, is recorded with its classification and does not change the token.

### 2.3 What each outcome would and would not establish

**`PASS-DERIVED` would establish**, at the layer of its weakest link (most likely [W], a paper
derivation awaiting review): for the stated rule, carrier class and ensemble, an observer region
chosen once and read completely has a record theory within `ε`, over complete records of horizon
`K`, of one qubit with a dense coherent one-parameter family, two incompatible sharp reads and
every pure state, with explicit resources `N(ε, K)`. It would be the first construction on `main`
of quantum operational behaviour in which neither the access nor the quantum rule is supplied
(Step 1 B.12 (ii)).

**It would not establish:** the selection of the Born rule (H-μ remains a hypothesis: why the
world's unprepared part has law `μ` is the measure question, and agreement for one qubit with
`d = 2` is not the general rule); Kochen–Specker contextuality or any nonclassicality (the
Kochen–Specker sphere model reproduces one qubit with a classical hidden variable, so one-qubit
agreement is compatible with a noncontextual model); Bell correlations or any composite system;
exact rotations (reading B-exact); quantum mechanics or the five completion conditions
(`exactAll_iff_physical_general`, Step 1 A.1); a quantum description of the configurations
(reading A); that a physical apparatus of this kind exists in nature; any change in correctness
(it would be a consistency-axis result, §A.23); any manuscript statement.

**`FAIL-CLASS(𝓢)` would establish** that the stated subclass does not reach the target at
`(ε₀, K₀)`. **It would not establish** a no-go for other rules, other ensembles, other access
modes, other carriers, exact forms, other observer-level extensions or OI generally (Code Review
Rules, "Bridge and no-go scope"). A result proved on `𝓛_fin` is not transferred to `𝓛_∞` or
conversely without its own proof.

**`INCONCLUSIVE(gap)`** establishes nothing about the question and records the gap.
**`VOID`** establishes nothing.

***

## 3. Controls

Each control is a paper derivation, carried out first (method step M1), and is a checkpoint: its
expected classification is stated now, its obtained classification is entered in the control
table, and the verdict is generated only when every row is green (§A.29, §A.41). A control turns
red if its obtained classification differs from the expected one; that means the criterion is
wrong, and the step returns to the owner with the definitions, not with a verdict.

| ID | Construction | Why it is a control | Expected classification | Source |
|---|---|---|---|---|
| C-SUP-1 | Main's uniform continuum realization: one finite reversible realization per `(d, m, K, ε)`, built from a net of quantum instruments | Supplied access with the quantum rule inside; shows D6 has teeth | Q0–Q6 at the stated `(ε, K)` [P]; D6 fails ("Quantum mechanics enters as the instrument data and as the state held in the hidden register", Main:582); D1 fails (the realization is built from the target net). `OPERATIONAL-ONLY` | Main:566, :582, :596, :598 [P] |
| C-SUP-2 | Per-target access: for each `θ`, a world, region or law chosen so that the record law of that one target is reproduced | Shows D1 and Q4 have teeth: per-target worlds cannot be composed in one world | D1 fails; Q4 not even definable across targets. Supplied | Gate A, `endpoints.md`:67 [R]; `whole-model-bridge.md`:283–287 ("It cannot simply identify states that an available sensor distinguishes") [R] |
| C-POS-1 | The Kochen–Specker sphere model with its supplied contract | Known positive: exercises the two halves of the criterion separately | Q0–Q6 with `ε = 0` for every finite adaptive rank-one projective protocol (the record states this; general instruments not covered, so Q2 is checked on that protocol class); D3 fails (cosine-hemisphere law supplied), D5 fails (preparation cone, private workspace and seeds by declaration), D6 fails (rotation primitives), D7 fails (continuum carrier). `OPERATIONAL-ONLY` | `history-architecture-v5/REPORT.md`:305–312 [R]; Kochen–Specker 1967 (imported there) |
| C-POS-2 | Its finite discretization `finite-a2-v5` | Positive control for the approximate form and for Q0 | Q0–Q6 at a fixed finite menu and horizon `h`, with the explicit bound of :36–37; D fails as for C-POS-1. `OPERATIONAL-ONLY` (with the menu restriction recorded) | `finite-a2-v5/REPORT.md`:14, :36–37 [R] |
| C-ISO-1 | A classical wave on the cubic lattice with real amplitudes (the real lift of R-lin), read completely in a region; its large-scale propagation is isotropic | The external assessment's countercontrol: isotropy and interference without a qubit | Q1 fails: complete reads of real amplitudes distinguish arbitrarily many preparations (the mechanism of the bridge's Lemma 1) [W]; D7 fails (E-real). Interference statistics alone are not a failure of the control (`observation-context-protocol.md`:37–38, "interference alone is insufficient") [R]. Not `PASS-DERIVED` | SM:258–268, Corollary 1a (`ohInvariant_iff`, OB/CubicIsotropy.lean:116) [K]; `whole-model-bridge.md`:132–197 [R] |
| C-ISO-2 | A classical diffusion (an `O_h`-symmetric random walk) observed through a region | Isotropic classical propagation with a classical state space | A classical theory whose largest set of perfectly distinguishable states has two members has a segment as state space [W]; the segment admits no drive (`not_drivable_Icc`, OB/KInfFoundations.lean:529) [K]; so Q3 fails, and Q5 fails (a segment has two pure states, so two sharp reads have overlap 0 or 1) [W]. Not `PASS-DERIVED` | SM:258–268 [P]; OB/KInfFoundations.lean:529 [K] |
| C-FIN | The eight-point model with the first-moment decoder | A supplied finite access quotient with a known error floor; checks Q3's detection of a finite group | Q3 fails below `ε = 1/15` (24 Clifford actions; error at least 1/15 for one non-Clifford rotation); D fails (supplied contract). Not `PASS-DERIVED` | `operational-quotient-v3/REPORT.md`:20–23, :218–227 [R] |
| C-REBIT | Real quantum theory of one system (state space a disk); the kernel's `realClass`, which has `rot` and lacks the phases, is its configuration-level analogue | Exercises the separation of Q3 from Q6 | Q0–Q5 hold, Q6 fails. `PARTIAL-REBIT`, never `PASS-DERIVED` | `realTheory_rot`, `realTheory_not_phases` (OB/F2CoherenceControls.lean:306, :317) [K]; the disk is [W] |
| C-TAB | The finite-menu table representation: any `N` listed preparations represented on `ℂ^N` | Shows Q2's fixed dimension has teeth | Q2 holds only with `d = N`; with three pairwise distinguishable preparations, Q1 and Q2 at `d = 2` fail | `whole-model-bridge.md`:204–211 [R] |
| C-B1 | B1 with the bridge's access: one isolated real pair, a loaded coefficient, point preparations, a sign read | The one record on `main` with continuous mixing in the substratum | Q1 fails (the bridge's Proposition, `d + 1` perfectly distinguishable preparations for every `d`) [R]; D2 fails (E-control), D7 fails (E-pair, E-real) | `two-mode-drive.md`:22–32, :124–147; `whole-model-bridge.md`:132–197 [R] |
| C-REP | A "construction" whose only evidence is a Hilbert-space representation of the records containing a mixing unitary | The Arc D result that representation is a disqualified ground | No Q-condition reads a representation; padding by an ancilla unitary (`padData_rooted`, OB/OperationalSourcing.lean:476) changes no record law and so cannot move `d_K`; not `PASS-DERIVED` | `PROGRAMME.md`:216 [K for the module, as the map reports] |
| C-CARD | (a) A fixed finite world (`L` fixed). (b) The infinite lattice under H-∞. (c) A finite cyclic surrogate of an infinite carrier | Checks that the criterion assumes neither a finite nor an infinite world | (a) For fixed `L` there is `ε₀(L) > 0` below which Q3 and Q6 fail together: a fixed finite realization cannot reproduce a qubit's full theory (Main:560 [P, P-imp]), and for a fixed finite experiment family its behaviours form a compact set (Step 1 C, B.7 row, column (2)) [W]. The criterion must not certify a fixed `L`; Q0 lets `L` grow. (b) Every definition of sections 1.2–1.4 is well-defined on `ℤ^3` (product law; finite `O`; finite records; finite light cone by range one) [W], and no clause uses finiteness of `Λ` except the resource count. (c) Verdicts are indexed by `K`: a finite surrogate agrees with an infinite carrier up to a horizon and differs after it (finiteness audit, control (1), Step 1 B.12) [R] | Main:560 [P, P-imp]; Step 1 B.0, C |
| C-MEAS | The robustness clause of D3 | Supplied-measure control | A construction whose record law matches only under one law tuned to the target, and not under `μ′`, is classified supplied | Step 1 F.1, control 2; B2 (`measurement-source.md`) [R] |
| C-EXACT | The definitions applied to the exact cases C-POS-1 (`ε = 0`) and C-ISO-2 (a segment) | §A.21: the operation modelled must preserve what it provably must; a definition that misclassifies an exact case is wrong | Both exact cases classified as stated above, with no slack | as above |

**Invariant → checkpoint table** (§A.41). Every property this proposal asserts of its own
execution, with the checkpoint that measures it.

| Invariant | Checkpoint |
|---|---|
| No computation is run in Step 2 | The result note's disclosure lists every command run; the reviewer checks it contains no interpreter, probe, checker or Lean build |
| Definitions and decision rule fixed before work | The owner-approved text of this file is identified by its sha256 in the result note; every definition used is quoted from it; any change is an amendment approved by the owner before work resumes |
| Controls green before the verdict | The control table; step 1 of section 2.2 |
| Verdict computed from the tables | Section 2.2; the reviewer recomputes the token from the two tables |
| No premise adopted | A hypothesis ledger in the result note lists H-μ, H-∞ if used, and every [R] statement used, each with its status, and each appears in every conclusion that uses it |
| Rule class respected | A D7 row for every family considered |
| Vocabulary boundary | The specification text of every family is searched for the D6 word list; a hit makes the family supplied |
| Layer tags kept distinct | Every link of every proof carries one tag; no [W] extension is tagged [K] (in particular no extension of `nonnegBounded_not_denseUnitaryControl` beyond its statement) |
| Negatives scoped | Every `FAIL-CLASS` row names `𝓢` |
| No manuscript or Lean change | `git diff --stat` of the unit touches only this directory |
| Paper register | The added text is searched for the §A.32/§A.33 phrase families before review |

***

## 4. Method (paper derivation only)

Depth-first (§A.12, §A.31): each step is a numbered node closed by an explicit check, with its
verdict recorded at the node; the decisive branch is chosen at each level. A favourable branch is
pressure-tested before it is accepted.

**M0. Freeze.** The owner approves this file or an amended one; its sha256 is recorded. Owner
choices of section 9 are fixed then and are not reopened after a verdict to obtain a different one
(Gate A, `endpoints.md`:119–123: an approximation target may not retrospectively replace a failed
one; here, equally, a failed verdict may not be replaced by changing a choice). A later different choice is a new question with its own
proposal.

**M1. Controls.** Derive each row of section 3 on paper from the cited records, and enter the
obtained classification. Rests on: Main:560, :566, :582, :596, :598 [P]; the records cited in the
control table [R]; OB/KInfFoundations.lean:529, OB/CubicIsotropy.lean:116,
OB/OperationalSourcing.lean:476, OB/F2CoherenceControls.lean:306, :317 [K]. If any control is
red, stop and return to the owner (section 7).

**M2. Lemmas about the criterion** (route-independent; each proved as [W] for review).

- L1 (well-posedness on both carrier classes): the record law, `d_K` and Q0–Q6 are defined on
  `𝓛_fin` and on `ℤ^3`; on `ℤ^3` with the uniform product law the record law exists (product
  measure) and depends on finitely many sites for each `K` (finite range).
- L2 (Q2 ⇒ upper half of Q1, for `ε` below an explicit constant): from Lemma 2 of
  `whole-model-bridge.md`:167–178 [R], re-derived here in approximate form (three qubit states
  cannot be pairwise distinguished with small error).
- L3 (Q2 ∧ Q3 ⇒ Q4 with error `c·ε`, explicit `c`): from Main:596 [P].
- L4 (escape audit, necessary conditions on any `PASS-DERIVED`): (a) the map from preparation
  prefixes to qubit states in `𝔔` is not injective on laws over configurations, and is not a
  fixed orthogonal linear frame with H-LIFT; otherwise MECH-2 Lemma F and Theorem U2(ii)
  (`mechanism-2-20261108/DESIGN.md`:307–345, :404–416) [R] would give a finite group of encoded
  unitaries, contradicting Q3; (b) the resource `N(ε, K)` is unbounded as `ε → 0` (C-CARD (a)).
  The parts of Lemma F and U2(ii) used are re-derived in the unit, since an [R] statement cannot
  serve as an established premise (§A.46 item 7), or the conclusion is stated as conditional on
  them (section 9, choice 9).

**M3. The decisive branch for R-lin.** Before any constructive attempt, decide the following
question, stated here and not answered (no work on it was done in drafting).

- L5 (structure of R-lin record laws). For R-lin under the uniform law, in initial-condition mode
  and without heralds, what is the form of the record law of a label sequence? For R-lin each
  `Φ_F^t` is an endomorphism of the group `X_Λ` [W], and MECH-1 Lemma A states that under one
  fixed affine rule a setting held in the state "can only translate values"
  (`mechanism-1-20261107/DESIGN.md`:96–97, :404–430) [R]. If L5 determines the record laws as a
  family of translates, it bounds which operational distances can occur, and so bears directly on
  Q1, Q2 and Q5 for that subclass. The node then records which of the following leave L5's hypotheses:
  heralded preparations, adaptive label choice (exchange mode), the second law `μ′`, R-nl. Each
  such departure is a separate child node, taken in the owner's order (section 9).

L5 is first because it is the cheapest node whose answer can close or open a whole subclass, and
because MECH-1 Lemma A already bears on it. Its outcome may yield `FAIL-CLASS(𝓢)` for a subclass
only; by section 2.3 that is not a statement about the other subclasses.

**M4. The remaining branches**, depth-first, in the order the owner fixes.

- *Route N (obstruction) for a subclass `𝓢`.* State an invariant of the record theory that every
  member of `𝓢` preserves and that the qubit target violates at a fixed `(ε₀, K₀)`. Candidate
  sources of such invariants on `main`: MECH-1 Theorem W and Proposition C (stabilizer closure at
  odd prime `q` under the access posits P1–P3, `mechanism-1-20261107/DESIGN.md`:751–766) [R],
  whose hypotheses (Gross's frame, posited access) differ from D1–D7 and must be re-established
  or replaced, not assumed; apparatus-1 §5.3, the finite-carrier argument against exact `rot`
  (`apparatus-1-20261107/DESIGN.md`:955–1023) [R], which is about exactness and bears here only
  on the growth of `N` with `K`.
- *Route P (construction) for a subclass `𝓢`.* Exhibit a family in `𝓢`, prove D1–D7 from its
  specification, and prove Q0–Q6 with explicit `N(ε, K)`. Every link is tagged; the C-SUP and
  C-MEAS checks are applied to the exhibited family before Q is attempted.

No mechanism is named here as a candidate. The proposal fixes what a construction must satisfy,
not what it is.

**M5. Verdict.** Fill in the two tables and compute the token by section 2.2.

**If the question cannot be decided on paper.** A later step, separately authorized, would need
exact computation: for R-lin (and R-nl if chosen) on small tori (for example `L ≤ 4`,
`q ∈ {2, 3}`) and small observer regions, the exact record laws of every label sequence up to a
small horizon under the reference law and `μ′`; from them the operational distance spectrum, the
capacity (Q1), the best fixed `d = 2` model (Q2) as an exact or certified optimization, and the
group induced on the operational quotient; with the controls C-POS-2, C-ISO-2 and C-FIN replayed in
the same harness as positive and negative controls; in exact integer or rational arithmetic, with a
frozen decision rule, as a native V3 round under §A.39. Nothing of this is planned to run in
Step 2.

***

## 5. Prior results that constrain the answer

Each row states what any `PASS-DERIVED` must be consistent with, and why the result does not decide
the question as posed. Layer tags are Step 1's.

| Result | Layer | What it excludes | Why it does not decide TUNE-1/Q2 | What a pass must respect |
|---|---|---|---|---|
| Configuration-basis obstructions: `substratumGen_not_control`, `obs_not_control`, `configurationLevel_not_qm` (Step 1 B.1, B.5) | K | Mixing in a matrix indexed by the configurations, for the monomial and sourced classes | Reading A; Q2 compares record laws, and the qubit is an image of an operational quotient, not a matrix over configurations. `operational-quotient-v3`: "not a map-independent no-go for all operational quotients" [R] | The OI-side operations stay nonnegativity-preserving at the configuration level; a pass must not imply configuration-indexed availability of `rot` or the quarter phase |
| `nonnegBounded_not_denseUnitaryControl` (OB/FrozenSourcing.lean:173–174) | K | Dense unitary control for a nonnegativity-bounded theory on the two-state carrier, where availability is conjugation by configuration-indexed matrices | The kernel statement is on `FiniteOperationalTheory (Fin 2)` with configuration-indexed availability; it is not an observer-level quotient no-go. Its extension to other carriers or interfaces is [W] (Step 1 C) and is not cited as kernel-checked | As above |
| `phaseQ_ne_heisQ` (OB/QuasilocalCharacterization.lean:792) | K | The one-site quarter phase as the automorphism of a reversible finite-range dynamics, on a lattice with any site set | Exactness, one dynamics, configuration algebra; no statement about approximation or a quotient | Same as row 1 |
| Counting: `countable_not_layerFlowExecutable` (OB/PolarizationClosure.lean:87–92) and the polarization closure audit (:54–85) | K | Exact flows in a class countable up to scalar | Exactness only. The same audit records non-Clifford operations of infinite order at finite level ("What it cannot contain is a continuum", :84–85; the infinite order of the hexagon product is from a numerical check, not proved, :233) | Q3 is approximate: a countable dense family is admissible |
| `flow_endpoint_refuted` (OB/FlowEndpoint.lean:149) | K | Sufficiency of a tunable flow for quantum mechanics | Not an obstruction; a necessity-only warning | Q1, Q5 and Q6 are required beside Q3 (controls C-ISO-1, C-ISO-2) |
| C5 discovery audit, O1 and O2 with countermodels (:25–37, :59–62) | K (as the audit reports) | — | Separation of two obligations at configuration level | `PARTIAL-REBIT` is reported apart; a pass needs Q3 and Q6 |
| Main:560, finite-substratum obstruction | P, P-imp | Exact reproduction of one qubit by one fixed finite realization | Exactness and fixed `N`; approximation by growing `N` is not excluded (Main:598) | `N(ε, K) → ∞` as `ε → 0` (C-CARD (a), L4 (b)) |
| Main:566, :582, :598, ε-realization and gluing | P | — | Positive, with the quantum rule supplied | Is control C-SUP-1; a pass may not resemble it in the respect D6 forbids |
| MECH-2 Lemma F, Theorem U2(ii), §6.4 (`mechanism-2-20261108/DESIGN.md`:307–345, :404–416, :901–911) | R | Encoded unitaries of infinite order under a fixed orthogonal injective frame with H-LIFT, for every dynamics on a finite set | Hypothesis on the identification (Step 1 B.12 (v)); D2 of Step 1 is the opening of non-injective encodings | L4 (a): the qubit image must be non-injective |
| MECH-1 Theorem W, Proposition C, Lemma A (`mechanism-1-20261107/DESIGN.md`:404–430, :751–766) | R | Non-Clifford encoded unitaries for class N at odd prime `q` under P1–P3 in Gross's frame; non-translational setting dependence under one fixed affine rule | Posited access and a fixed frame; Lemma A is the input to L5 and bears on R-lin only | A pass on R-lin must be consistent with Lemma A, or show where its hypotheses fail |
| apparatus-1 Lemma 5, C-ROT and dense control (`apparatus-1-20261107/DESIGN.md`:731–784); §5.3 (:955–1023) | R | The encoded quarter phase and dense control in the one-cell frame R1 at `q = 2`; exact `rot` on any finite carrier | R1 and posits P1–P3; §5.3 is about exactness | The resource must grow with the horizon for an irrational angle [W, from §5.3's periodicity argument] |
| `whole-model-bridge.md` Proposition (:132–197) | R | Any fixed finite-dimensional quantum carrier for point preparations with a sign read | Out-of-class carrier and access (E-real, E-control) | The derived access must leave no read that separates more than two preparations (Q1) |
| `a2_depth_v7`, `a2_memory_v8` (`a2_memory_v8/REPORT.md`:26) | R | Depth-uniform agreement by one controller with finite persistent state and dyadic fresh bits on one protocol | One protocol and one controller class | `N(ε, K)` is stated as a function of `K`; a `K`-independent claim must show why the class does not apply |
| Arc D round 1, `padData_rooted` (OB/OperationalSourcing.lean:476; `PROGRAMME.md`:216) | K | Representation as evidence of a resource | — | Control C-REP |
| Stochastic observer-interface audit (:369–381) | K (ensemble leg) | — | The architecture fixes neither an observation map nor an ensemble | D4 removes the first choice (complete reads); H-μ names the second |
| Observer-level isotropy, SM Corollary 1a (SM:258–268; OB/CubicIsotropy.lean:116) | K | Quadratic anisotropy of a projected `O_h`-equivariant kernel | Classical and positive; isotropy is not the target | Controls C-ISO-1, C-ISO-2 |

**Openings this question uses** (Step 1 D). D2 (non-injective encodings): the qubit is a quotient
image. D7 (access as coarser operational equivalence), here derived from a region chosen once
rather than posited. D11 (an access quotient on a carrier with continuous mixing) in its finite
and approximate form, which Step 1 records as "not posed in any record read". D12 (approximation
by finite systems of growing size from ingredients other than the quantum rule). D1 (an infinite
underlying space) only under H-∞.

**Openings it does not use.** D10 (Q-B), which asks for an "additional OI principle"; D3
(input-correlated memory outside a carrier), except as it arises inside the fixed world; exact
forms.

***

## 6. Hard-to-vary statement (§A.29)

The question adopts no premise and is not a Layer-0 revision; the statement is made because the
owner asked for it.

**What the investigation preserves.** Every row of section 5 stays true whatever the verdict, and
each is a control or a necessary condition of a pass (sections 3, 4 L4). In particular a pass
leaves every kernel obstruction on the configuration-basis interface intact, because it is stated
on the operational quotient.

**Where it could be varied, and how that is closed.** The rule is one fixed `F`; the ensemble is
one declared law with a robustness check; the label menu is every configuration of `C`; the read
is the complete history of `O`. What remains existential is the shape of `O` and `C`, `τ`, the
generating rule `n ↦ I_n` and the comparator `𝔔`. These are fixed once for all targets and all
protocols (D1), and the comparator is a single `ℂ²` model, so they cannot be adjusted per outcome.
Q4, Q5 and Q6 are not tuned by any of them: they are checks the family either passes or fails.

**Independent prediction or postdiction a pass would have to deliver.** None can be stated with
confidence in advance. Two candidates are named so that a pass can be held to them:

1. the error law `ε(N, K)` of the passing family, fixed by `F`, `q` and `μ` with no free
   parameter: a statement about how a finite apparatus departs from a qubit, in principle
   comparable with precision tests of single-qubit rotations;
2. what the same generating rule gives, unchanged, for two disjoint apparatus regions: whether
   the joint record theory composes as `ℂ² ⊗ ℂ²` or as a classical or other composite. This was
   not designed in and could fail. Its evaluation belongs to the separately gated Step 3.

If neither is stated and checked, a pass stands as a conditional consistency-axis result and moves
no correctness assessment (§A.23).

***

## 7. Scope, cost and stopping rule

**Scope.** Paper derivation only. No computation, no Lean build, no manuscript or Lean change, no
premise adopted, no GitHub comment by the writer. Records cited are read at the pin. A premise
taken from an [R] record is either re-derived in the unit or carried as a named condition (section
9, choice 9).

**Cost.** Bounded effort: by default at most three writer sessions for M1–M5 (section 9,
choice 10), each followed by a review, inside §A.40's resource limits.

**The step ends** at the first of:

- a token of section 2.1 computed by section 2.2;
- a red control (then `VOID`; the definitions go back to the owner before any further work);
- the effort bound (then `INCONCLUSIVE(gap)`, the gap stated as the exact lemma not proved).

**What happens next.** In every case the result goes to independent review and then to the owner.
No next step starts without the owner's recorded decision.

- `PASS-DERIVED`: the owner decides whether to open Step 3 (the measure question for H-μ,
  contextuality, composites and Bell, and the independent consequences of section 6), and whether
  a verification round is wanted.
- `FAIL-CLASS(𝓢)`: the owner decides whether to stop TUNE-1 or to pose a different question
  (another rule, ensemble or mode) under a new proposal.
- `PARTIAL-x` or `INCONCLUSIVE(gap)`: the owner decides whether to pursue the named gap, on paper
  or by a separately authorized computation (section 4, last paragraph).
- `VOID`: the owner decides on amended definitions.

***

## 8. Not part of this question

Exact rotations (B-exact); the Born rule's selection, including the justification of `μ`;
contextuality; Bell correlations; composite systems beyond the postdiction named in section 6;
reading A; real-valued sites, an isolated pair, a loaded coefficient or any added carrier;
growing alphabet size; any statement about OI's correctness; any manuscript change.

***

## 9. Open choices for the owner

Each choice has options and a recommendation. The choices are fixed at M0. Some may decide part of
the question by themselves (for example, if L5 settles the strictest subclass), and that is why
they are fixed before work and not afterwards.

1. **Which rule.** (a) R-lin only; (b) R-lin, then R-nl as a separate verdict; (c) both together.
   *Recommendation: (a).* R-lin is the rule Main's ledger posits; R-nl is not covered by ledger
   item (vii), and adding it is the owner's decision. If R-lin gives `FAIL-CLASS`, R-nl can be a
   new question.
2. **Alphabet.** (a) Statements for each fixed `q ≥ 2`; (b) `q = 2` only (Main §3.2's instance);
   (c) a family in growing `q`. *Recommendation: (a)*, with `q = 2` first. (c) needs the
   correspondence between alphabets SM §2.7 leaves unbuilt.
3. **World.** (a) Finite tori only; (b) finite tori, and the infinite lattice under the named
   hypothesis H-∞ as a separately labelled conditional result. *Recommendation: (b).* It honours
   "finite observational access" not implying "finite underlying dynamics" without adopting an
   infinite world.
4. **Error measure and horizon.** (a) Total variation on complete records over all protocols of
   horizon `K`, for every `K`, with `N(ε, K)` explicit; (b) the same for one fixed `K` (for
   example `K = 3`, as in `finite-a2-v5`) as the target. *Recommendation: (a)* as the pass
   condition, a fixed-`K` result reported as `PARTIAL-FIXEDK`. The owner's Q-B record asks that
   errors under repetition, adaptive measurement and recombination be controlled (Step 1 F.2).
5. **How the observer chooses.** (a) Exchange mode with adaptive protocols (label choice may
   depend on earlier records), heralded preparations allowed with raw rates; (b) initial-condition
   mode only (every choice an initial condition; no adaptivity); (c) both, reported separately.
   *Recommendation: (c)*, with a pass requiring (a). (b) is the strictest embedding; (a) is the
   form Main §3.4 and Gate A use.
6. **Ensemble.** The reference is the uniform law on the unprepared part. The second law `μ′` for
   the robustness check: (a) the uniform law on one level set of the conserved quantity
   `E(u, v)` of SM:296; (b) a translation- and `O_h`-invariant product law with a non-uniform
   site marginal. *Recommendation: (a)*, since it is invariant under R-lin and has the same
   symmetries.
7. **Rebit or qubit.** (a) A pass requires the whole Bloch ball (Q6); (b) a disk suffices.
   *Recommendation: (a)*, with a disk reported as `PARTIAL-REBIT`. The owner asked for one
   quantum bit, and a disk is real quantum theory.
8. **Partial results.** (a) Report the `PARTIAL-x` tokens, each labelled as not answering the
   question; (b) report only the final token. *Recommendation: (a).*
9. **Premises from unreviewed records in a negative.** (a) Re-derive in the unit every [R]
   statement a `FAIL-CLASS` uses (MECH-1 Lemma A, MECH-2 Lemma F); (b) cite them and state the
   negative as conditional on them. *Recommendation: (a)*, so that a negative does not rest on an
   unverified premise (§A.46 item 7).
10. **Effort bound.** (a) Three writer sessions with reviews; (b) another bound.
    *Recommendation: (a).*

***

## 10. Disclosure and review status

- **No computation was run.** Commands used in drafting: `git` (rev-parse, status, log,
  merge-base, branch, add, commit, push), `grep`, `sed`, `awk`, `cut`, `tr`, `wc`, `ls`, `find`,
  `head`, `tail`, `df`, `sha256sum`. `python3` was invoked once by mistake, with the one-line
  script `print(1)`, output discarded; it computed nothing about any OI rule. No probe, checker or
  Lean build. No GitHub comment.
- **Read for this proposal**, at the pin: Step 1 (its summary, A.1–A.4, B.0–B.12, C, D, F.1,
  F.2); `apparatus-1-20261107/DESIGN.md`:725–790, :955–1025, :1072–1090; `mechanism-1-20261107/
  DESIGN.md`:92–100, :211–243, :404–440, :751–770, :1060–1080; `mechanism-2-20261108/DESIGN.md`:
  305–345, :400–420, :737–756, :810–830, :901–912; `oi-qm-ext-1/two-mode-drive.md` (whole);
  `oi-qm-ext-1/whole-model-bridge.md`:1–48, :132–307; `oi-qm-ext-1/endpoints.md` (the lines
  cited); `c5-discovery-audit.md`:25–65; `polarization-closure-audit.md`:50–90;
  `observation-context-protocol.md` (whole); `PROGRAMME.md`:216; the statements cited in
  OB/FrozenSourcing.lean, OB/DiscreteCompletion.lean:40–62, OB/SecondOrderDrive.lean:339; Main:4,
  :268, :554, :564, :566, :582, :584, :590, :596, :598, :602, :726; SM:88–90, :256–270, :294–298;
  the lines of the `states-dynamics-audit-20261024` reports cited. Statements whose line numbers
  were located by search and not read in full are the Lean names listed in sections 3 and 5 other
  than those above, and the record lines cited from Step 1's tables.
- **Not done:** Step 2 itself; any evaluation of L5 or of any family; any check that the
  controls behave as expected (that is M1).
- **Same-family drafting.** This proposal was drafted by a model of the same family as the writer
  and the reviewers of Step 1. It is not reviewed. It needs a fresh internal review and the
  ChatGPT review before it goes to the owner for approval.
