# TUNE-1, Step 2 proposal: derived-access coherent qubit operations

**WIP / UNVERIFIED drafting record. A proposal for owner approval; not executed.** Research unit
under Issue #1236 (owner decision: paper-only). This file plans one question and fixes, before any
work, its definitions, decision rule, controls and stopping rule. It runs no Step 2 work, performs
no computation, adopts no premise, advocates and evaluates no candidate mechanism, changes no
manuscript or Lean file and authorizes nothing. Execution needs the owner's recorded approval of
this text (or of an amended text) after the reviews named in section 10. This is revision r2,
drafted after the first internal review (verdict REVISE, at `9312b805`); the dispositions of that
review are kept outside this file.

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

Step 1 found that wherever `main` gets quantum-like behaviour from a world that only reshuffles
its configurations, someone chose by hand what the observer may prepare and read. Can that
hand-choice be removed?

Take one lattice rule and fix once a region as the observer's apparatus. The observer reads
everything in the region at every step, nothing outside it, and chooses only the settings it
writes into its own cells. Does what it can do and see behave like one quantum bit, to any wanted
precision, over experiments of any length? That means finely adjustable reversible operations
that compose correctly, two incompatible measurements, every qubit state, and outcome statistics
that come from the dynamics acting on a declared random state of the unobserved world (an
assumption, not derived).

It counts only if one apparatus serves every setting and nothing quantum is put in, not even a
programmed quantum simulator. Controls check that the test has teeth: models with hand-chosen
access or a stored quantum answer must be classed "supplied"; a classical random walk must fail,
for a reason that does not also rule out every hidden-variable model.

For the linear rule, a lemma already on `main` may settle the question quickly, probably
negatively; the nonlinear rule is the open case, and it could be studied only as a named
hypothesis. The owner chooses the rule and the random state.

Outcomes: pass; fail, for a stated class only; inconclusive; or void, if a control fails. Even a
pass would show only that this follows from OI's rules; it would not be evidence that OI is
correct, nor establish the Born rule. Paper work only; nothing adopted.

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
  realization. What `main` states about it [P]: SM §4.2 introduces it to test numerically whether
  rounding breaks the linear rule's integrability, as full-shell sampling needs (SM:294); it
  "behaves chaotically at the sizes measured" on three numerical diagnostics, and no nonconstant
  polynomial invariant of degree at most two was found in the computed instances (SM:292, :294);
  away from alphabet-boundary crossings its floor differs from the real linear update by at most
  1/3 per site and step, and a crossing can change that by order `q/3` (SM:298); "numerical chaos
  of the rounded rule supplies neither that sampling nor its identification with the normalized
  observer-level operator" (SM:298); it "does not inherit A5 or exact amplitude-scale invariance"
  (SM:1416). In Main it appears only in ledger item (v), as the source of numerical motivation for
  the hidden-sector mixing hypothesis: "numerical motivation comes from the rounded candidate of
  [SM §4.2]" (Main:726). It is therefore a candidate realization, not a ledger posit: it meets the
  second-order form of item (xiii) and items (viii), (x) and (xi) [W], and it does not meet item
  (vii). It enters only under the named hypothesis **H-nl** ("the world's rule is R-nl"), which
  replaces item (vii) for that subclass, is carried into every conclusion that uses it, and is not
  adopted (Issue #1236). SM's chaos diagnostics are numerical evidence and are not premises of
  any Step 2 derivation (§A.46 item 7; Code Review Rules, "Exactness and controls"). No record
  read for this proposal states anything about R-nl's record laws through a region or about its
  computational capacity (section 10 lists the reading).

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
acceptance probability `p_acc` reported and no renormalization of rejected runs
(`observation-context-protocol.md`:45 [R]). The distance `d_K` of section 1.4 compares joint
laws, so it controls a law conditional on a herald only to within `2 d_K / p_acc` [W]. Every
condition stated on heralded preparations (Q1, Q5, Q6) is therefore required at *conditional*
error `ε`, which holds when `2 d_K / p_acc ≤ ε`, and the `p_acc` of each heralded preparation used
is reported. `Π_K(I)` is the set of such protocols. The **record
law** `P^I_π` is the law of `(h_1, …, h_K)` under `μ`, the ready configuration and the dynamics.

**Initial-condition mode** (owner option, section 9, choice 5): all labels of a non-adaptive
protocol are written at time zero into disjoint control blocks of `O`, laid out by a fixed rule,
and no exchange occurs afterwards. Every observer choice is then an initial condition, as in Main's
program register (Main:582).

**Family.** A family is `{I_n}_{n ∈ ℕ}` produced by one generating rule `n ↦ I_n` (for example the
`n`-fold scaling of a fixed pattern of `O` and `C`), stated in full as part of the family's
specification and a function of `n` alone (D1).
The resource of `I_n` is `N(I_n) = |Λ_n|` on `𝓛_fin`, and on `𝓛_∞` the number of sites of `O_n`
plus those of its light cone over the protocol's duration, finite by the range bound.

### 1.3 Derived versus supplied: the criterion

A family is **derived** iff it satisfies D1–D7. It is **supplied** iff it fails at least one.
Each clause is stated so that a reader can check it from the construction as submitted: the
specification of the family and, for D6(b), the proofs of the Q-conditions submitted with it.

- **D1 (one interface for all targets).** The generating rule `n ↦ I_n` is part of the family's
  specification and is a function of `n` alone: its statement takes no target operation,
  requested angle, protocol, outcome, record statistic or comparator model as an argument. For
  each `n` one `I_n` serves every label, every protocol of `Π_K` and every target. Only `n` may
  depend on the requested `(ε, K)`, through the stated function `n(ε, K)`.
- **D2 (embedding).** The only dynamics is `Φ_F` with `F` from 𝓡 on the whole world. The observer
  acts only by the label exchanges of section 1.2 (or by initial conditions, in
  initial-condition mode). No coefficient is loaded, no step is switched off or replaced, no
  region is isolated, and the round duration `τ` is the same for every label and every
  configuration.
- **D3 (ensemble).** `μ` is one law for the whole family, stated in its specification, the same
  for every `n`, and taken from the list the owner fixes at M0 (section 9, choice 6). The list
  as drafted: the uniform law on `(V × V)^{Λ∖O}` (on `ℤ^3`, the uniform product law); the uniform
  law on one level set of the conserved quantity `E(u, v)` of SM:296; a translation- and
  `O_h`-invariant product law with a non-uniform site marginal. Which of them a pass must hold
  under is choice 6. Requiring the uniform law is not part of the owner's question, and by the
  expectation recorded in M3 that requirement alone decides R-lin. The stated
  architecture fixes no ensemble (stochastic observer-interface audit,
  `verification/audits/operational/stochastic-observer-interface-audit.md`:369–381; Step 1 B.12
  (ix)), so H-μ is a named hypothesis and every conclusion carries it. Main's posit ledger item
  (iv) posits a maximal-entropy measure selection ("the maximal-entropy invariant measure
  compatible with the observer's records", Main:726) [P]; reading it as selecting the uniform law
  on the unprepared part is [W] and is not used as a premise (`measurement-source.md`:148 [R]
  reads Main's selection premise as selecting the global counting measure). Robustness
  requirement: a result counts as derived only if it is also stated under one second law `μ′` of
  the list with the same symmetries (choice 6); if it holds under `μ` and fails under `μ′`, the
  verdict records the measure as supplied (Step 1 F.1, control 2).
- **D4 (readout).** The observer's record is the complete history of `O`. No pointer function,
  response function, threshold or decoder is chosen. Outcome probabilities are the pushforward of
  `μ` through the dynamics; this is the **derived readout rule** the owner requires, and nothing
  else is called a readout rule. The two-class coarse-grainings of Q5 test a property of the
  comparator `𝔔`; they are not a readout rule and do not change `d_K`, which compares complete
  records.
- **D5 (no access by declaration).** Every protocol of `Π_K(I)` is admitted. No read, label or
  herald is declared unavailable. Information is inaccessible only if it lies outside `O` when it
  would be read. A restriction that is not a consequence of D1–D4 makes the family supplied.
- **D6 (no quantum input).** Two tests; failing either makes the family supplied, classified as
  choice 11 fixes.
  - *(a) Vocabulary.* The specification of the family uses no quantum object or target quantity:
    no amplitude, density matrix, unitary, Kraus operator, Born weight, rotation, cosine or sine,
    orthogonal-matrix dynamics, or operational-control predicate (the boundary frozen in the
    pair-flow equivalence audit, quoted in Step 1 F.1, control 12). These words occur only in the
    comparator (section 1.4).
  - *(b) Compilation.* None of `r_O`, the shapes of `O` and `C`, `τ`, `μ` or the generating rule
    is defined as the encoding into configurations of a program, table or data stream that
    computes a **D6 quantity** (an amplitude, a rotation angle's cosine or sine, a Born weight, or
    a matrix entry of a density operator, unitary or instrument), or that samples from a law
    defined by one (a Born law, a cosine law, the sphere model's hemisphere law). The test is
    applied to how each item is defined and to the submitted proofs of Q2 and Q3: if a proof
    identifies the configurations of some set of cells with numerals or tables of a D6 quantity,
    and the dynamics with an algorithm acting on them, the family fails (b), whatever its bit
    pattern contains. The test is not failed because the rule could compute, nor by a proof that
    obtains the record law from the structure of the dynamics without such an identification.
    It is aimed at Main's single controlled dynamics, whose "read-only program register — the
    protocol table" holds the quantum data (Main:582) [P], moved into the apparatus region, and
    is exercised by control C-PROG.
- **D7 (rule class).** `F ∈ 𝓡` as fixed by the owner; `Λ ∈ 𝓛`; none of E-real, E-pair,
  E-control or an added carrier.

The criterion is aimed at the two ways the answer has been supplied on `main`: a per-target choice
of access, measure or decoder (D1, D3, D4, D5), and the quantum rule placed in the hidden state,
by declaration or by compilation (D6), as in Main's realization theorems, where "Quantum mechanics enters as the instrument data
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
  so distinguished; for heralded preparations the errors are conditional (section 1.2).
- **Q2 (one fixed qubit model).** There is a qubit model `𝔔` with `d_K(I, 𝔔) ≤ ε`.
- **Q3 (a dense coherent family).** For a fixed axis `n̂`, every `θ ∈ [0, 2π)` (the channel
  `Ad(e^{−iθ n̂·σ/2})` has period `2π` in `θ`) has a label `c(θ)`
  with `Σ_h ‖𝓘_{c(θ),h} − p_h(θ) · Ad(e^{−iθ n̂·σ/2})‖_⋄ ≤ ε` for some probability vector
  `p(θ)`: the round acts on the qubit as the unitary channel, and its record carries at most `ε`
  information about the qubit.
- **Q4 (composition; model-free).** For all `θ₁, θ₂`, replacing two consecutive rounds
  `c(θ₁), c(θ₂)` by `c(θ₁ + θ₂), c(0)` in any protocol of horizon `K` changes the law of all later
  records, and of the records of those two rounds after marginalization, by at most `ε`.
- **Q5 (incompatible sharp reads).** Two labels, with two-class coarse-grainings of their records,
  are represented in `𝔔` within `ε` of rank-one projective measurements `{P_a, 1 − P_a}` and
  `{P_b, 1 − P_b}` with `Tr(P_a P_b) ∈ [1/4, 3/4]`. The coarse-grainings test a property of `𝔔`;
  they are not a readout rule and leave `d_K` unchanged (D4).
- **Q6 (the whole Bloch ball).** The states `𝔔` assigns to preparation prefixes are `ε`-dense in
  the pure states of `ℂ²`, not only in one great circle; for heralded prefixes, at conditional
  error `ε` (section 1.2).

**One direction each, to be proved in method step M2** (§A.34). Q2 implies the upper half of Q1
for `ε` below an explicit constant (approximate form of Lemma 2 of `whole-model-bridge.md`:167–178
[R]). Q2 and Q3 imply Q4 with error a fixed multiple of `ε`. Neither converse is claimed. Q1 and
Q4 are kept as separate conditions because they can be checked without any model. Q5 is close to
implied by Q1, Q2, Q3 and Q6 (not proved); it is kept because it names the two reads, and the
overlap does no harm.

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

### 1.7 Why D1–D7 leave room for a pass, and where restricted access enters (rationale; [W])

This is the first internal review's answer to whether a pass is possible at all under D1–D7 with
full access inside the region. It is recorded as an unreviewed rationale, not a result.

- Full access inside `O` does not reduce the question to the configuration-level reading.
  `Λ ∖ O` is never read, and the record theory is a quotient of laws, so Step 1's
  configuration-indexed obstructions (section 5, rows 1–3) do not apply to it.
- C-POS-1 and C-POS-2 show that classical hidden state with restricted access can meet Q1–Q6, and
  C-POS-2 meets Q0 as well at a fixed menu.
- A pass therefore needs a rule that carries information out of `O`, keeps it unread, and returns
  it only through randomly sampled outcomes. The reviewer's example is one-time-pad masking at the
  region boundary, which the second-order form allows (not examined here).

This is where the owner's third class, "Restricted observational access" (Step 1 B), does the
work in this question: through the boundary of `O` and the unread law `μ`, not through a declared
restriction (D5 forbids those). For R-lin, the expectation recorded in M3 is that it does no work.

***

## 2. Decision rule

### 2.1 Tokens and conditions

Let `𝕀_D` be the set of derived families for the owner's 𝓡 and 𝓛. The tokens:

- **`PASS-DERIVED[R, 𝓛, λ | H]`**: a family in `𝕀_D` and an explicit `N(ε, K)` are exhibited,
  and Q0–Q6 are proved for every `ε > 0` and every `K`, under the hypotheses `H`, with the
  robustness clause of D3 met. The token names the rule `R`, the carrier class `𝓛` (`𝓛_fin`, or
  `𝓛_∞`), the law `λ` and every hypothesis used: H-μ always, H-∞ with `𝓛_∞`, H-nl with R-nl. For
  example `PASS-DERIVED[R-lin, 𝓛_fin, uniform | H-μ]` and
  `PASS-DERIVED[R-lin, 𝓛_∞, uniform | H-μ, H-∞]` are distinct tokens.
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
- **`PASS-COMPILED`** (exists only if the owner picks choice 11(b)): Q0–Q6 hold, and D6(b) is
  the only D-clause that fails. It is reported apart and never counts towards a pass.
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

1. If any control is red, or any row the verdict relies on as established has status ≠ `proved`:
   `VOID(that row)`. A refuted condition enters the verdict as the `proved` row that states its
   negation for the named subclass.
2. Else, if Q0–Q6 and D1–D7 are `proved` for one family over every `(ε, K)`:
   `PASS-DERIVED[R, 𝓛, λ | H]` for that family. Every `FAIL-CLASS(𝓢)` proved for another
   subclass is reported with it, row for row.
3. Else, if a `FAIL-CLASS` theorem is `proved` for `𝓢 = 𝕀_D`: `FAIL-CLASS(𝕀_D)`. If it is proved
   for a proper subclass only: `FAIL-CLASS(𝓢)` together with `INCONCLUSIVE(gap)` for
   `𝕀_D ∖ 𝓢`.
4. Else, if a `PARTIAL-x` row set is `proved` and the owner has asked for partials: `PARTIAL-x`
   together with `INCONCLUSIVE(gap)` for the rest.
5. Else: `INCONCLUSIVE(gap)`.

A candidate family encountered during the work that is classified `OPERATIONAL-ONLY` (or
`PASS-COMPILED`), or that fails a Q-condition, is recorded with its classification and does not
change the token.

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
| C-POS-1 | The Kochen–Specker sphere model with its supplied contract | Known positive: exercises the two halves of the criterion separately | Not a lattice interface, so Q1–Q6 (Q0 does not apply): `ε = 0` for every finite adaptive rank-one projective protocol (the record states this; general instruments not covered, so Q2 is checked on that protocol class); D3 fails (cosine-hemisphere law supplied), D5 fails (preparation cone, private workspace and seeds by declaration), D6 fails (rotation primitives), D7 fails (continuum carrier). `OPERATIONAL-ONLY` | `history-architecture-v5/REPORT.md`:305–312 [R]; Kochen–Specker 1967 (imported there) |
| C-POS-2 | Its finite discretization `finite-a2-v5` | Positive control for the approximate form and for Q0 | Q0–Q6 at a fixed finite menu and horizon `h = K`, at every `ε ≥ b + δ`: `b` is the record bound of :36–37 at that `h`, and `δ` is the largest gap between a requested angle and the nearest menu angle, the diamond distance between the two rotations being at most `δ` [W]. Q3 therefore holds only to the menu's resolution. D fails as for C-POS-1. `OPERATIONAL-ONLY` (with the menu restriction recorded) | `finite-a2-v5/REPORT.md`:14, :36–37 [R] |
| C-ISO-1 | A classical wave on the cubic lattice with real amplitudes (the real lift of R-lin), read completely in a region; its large-scale propagation is isotropic | The external assessment's countercontrol: isotropy and interference without a qubit. Out of class: it fails D7 trivially and has no `μ` specified. Its value is that operations which vary continuously and compose (Q4) are still rejected by Q1 [W]. The external countercontrol's in-class wave is R-lin itself, which L5 tests | Q1 fails: complete reads of real amplitudes distinguish arbitrarily many preparations (the mechanism of the bridge's Lemma 1) [W]; D7 fails (E-real). Interference statistics alone are not a failure of the control (`observation-context-protocol.md`:37–38, "interference alone is insufficient") [R]. Not `PASS-DERIVED` | SM:258–268, Corollary 1a (`ohInvariant_iff`, OB/CubicIsotropy.lean:116) [K]; `whole-model-bridge.md`:132–197 [R] |
| C-ISO-2 | **A classical diffusion: one lazy random walker.** *World:* `Λ ∈ 𝓛` and one walker, whose position `X_t ∈ Λ` is the whole state. *Dynamics:* each tick moves the walker by the `O_h`-symmetric lazy kernel `K(x, x) = 1/2`, `K(x, x ± e_j) = 1/12` (`j = 1, 2, 3`), with fresh randomness each tick; the walker's law obeys the lattice heat equation and spreads isotropically at large scales. *Interface:* `O` a box, `C ⊆ O`. A label is a permutation `g_c` of `C`. At the start of a round the walker is moved to `g_c(X)` if it is in `C`, and nothing happens otherwise; then `τ` ticks of `K` run. The record at each tick is the walker's position if it is in `O`, and a blank symbol otherwise. At time zero the walker is outside `O`, with `μ` uniform on `Λ ∖ O` | Isotropic classical propagation in which the labels do act on the walker. The negative must not come from a property that every classical hidden-variable model has (proves-too-much check below) | Q1, Q3 and Q6 cannot hold together at `ε < ε_D`, an explicit constant stated at M1 with the conditional-error factor of section 1.2; D7 fails (a stochastic rule outside 𝓡). Not `PASS-DERIVED`. Argument [W]. (i) The whole state is the walker's position, so a label can act only when the walker is in `C ⊆ O`, where the preceding tick has read it. Conditional on a prefix's complete records, either the walker is at a recorded `x ∈ O`, and the effective state is fixed by `x` alone (Markov property), or it is outside `O`, and every label acts exactly as `c(0)` does. (ii) A state of the second kind satisfies `Ad(U_θ)ρ ≈ ρ` for every `θ` under Q3, read out through Q5's reads, so it lies within `O(ε)` of the `n̂` axis. (iii) By laziness, from `x ∈ O` the round's first-tick record shows the walker at `g_c(x)` with probability at least 1/2, while any other starting point puts mass at most 1/12 there. Round record laws from distinct starting points therefore differ in total variation by at least 5/12, whereas Q3 makes the round's record law independent of the input within `ε`. So below `ε_D` all effective states are of one kind: either all lie near the axis (Q6 fails), or there is a single state (Q1 fails). The argument uses two properties: the whole state is read whenever a label acts, and the walk is lazy. It does not use that the walk is classical. Strict contraction of `K^τ` is not used, because it is not uniform in `L` and a contraction can act isometrically on a quotient [W] | SM:258–268 (isotropy of `O_h`-equivariant kernels) [P]; the argument is [W] |
| C-FIN | The eight-point model with the first-moment decoder | A supplied finite access quotient with a known error floor; checks Q3's detection of a finite group | Q2 with Q3 fails below `ε = 1/15`: the model has 24 Clifford actions, and 1/15 is a record-level error floor for one non-Clifford rotation, reached through the comparator (Q2), not a direct diamond bound on Q3; D fails (supplied contract). Not `PASS-DERIVED` | `operational-quotient-v3/REPORT.md`:20–23, :218–227 [R] |
| C-REBIT | Real quantum theory of one system (state space a disk); the kernel's `realClass`, which has `rot` and lacks the phases, is its configuration-level analogue | Exercises the separation of Q3 from Q6 | Not a lattice interface: Q1–Q5 hold and Q6 fails, the pattern that `PARTIAL-REBIT` reports for a family in `𝕀_D`. Never `PASS-DERIVED` | `realTheory_rot`, `realTheory_not_phases` (OB/F2CoherenceControls.lean:306, :317) [K]; the disk is [W] |
| C-TAB | The finite-menu table representation: any `N` listed preparations represented on `ℂ^N` | Shows Q2's fixed dimension has teeth | Q2 holds only with `d = N`; with three pairwise distinguishable preparations, Q1 and Q2 at `d = 2` fail | `whole-model-bridge.md`:204–211 [R] |
| C-B1 | B1 with the bridge's access: one isolated real pair, a loaded coefficient, point preparations, a sign read | The one record on `main` with continuous mixing in the substratum | Q1 fails (the bridge's Proposition, `d + 1` perfectly distinguishable preparations for every `d`) [R]; D2 fails (E-control), D7 fails (E-pair, E-real) | `two-mode-drive.md`:22–32, :124–147; `whole-model-bridge.md`:132–197 [R] |
| C-REP | A "construction" whose only evidence is a Hilbert-space representation of the records containing a mixing unitary | The Arc D result that representation is a disqualified ground | No Q-condition reads a representation; padding by an ancilla unitary (`padData_rooted`, OB/OperationalSourcing.lean:476) changes no record law and so cannot move `d_K`; not `PASS-DERIVED` | `PROGRAMME.md`:216 [K for the module, as the map reports] |
| C-CARD | (a) A fixed finite world (`L` fixed). (b) The infinite lattice under H-∞. (c) A finite cyclic surrogate of an infinite carrier | Checks that the criterion assumes neither a finite nor an infinite world | (a) For fixed `L` there is `ε₀(L) > 0` below which Q3 and Q6 fail together: a fixed finite realization cannot reproduce a qubit's full theory (Main:560 [P, P-imp]), and for a fixed finite experiment family its behaviours form a compact set (Step 1 C, B.7 row, column (2)) [W]. The criterion must not certify a fixed `L`; Q0 lets `L` grow. (b) Every definition of sections 1.2–1.4 is well-defined on `ℤ^3` (product law; finite `O`; finite records; finite light cone by range one) [W], and no clause uses finiteness of `Λ` except the resource count. (c) Verdicts are indexed by `K`: a finite surrogate agrees with an infinite carrier up to a horizon and differs after it (finiteness audit, control (1), Step 1 B.12) [R] | Main:560 [P, P-imp]; Step 1 B.0, C |
| C-MEAS | B2: B1's carrier with the posited quadratic sensor `t(z)`, seeds with an atomless law `μ`, and the one-read law `p_1(θ) = F(cos²θ)`, with `F(t) = μ((0, t))`. The law matches the quantum value for every `θ` exactly when `μ` is uniform in the detector coordinate. It is run here under that uniform law and under one of the record's predeclared symmetric seed laws as `μ′` | Supplied-measure control on a concrete construction: shows that the robustness clause of D3 has teeth | The one-read match holds under the tuned law and fails under `μ′`, so D3's robustness clause classifies the measure as supplied. Independently, D4 fails (a posited response function), D7 fails (B1's carrier), and Q2 fails on the two-read law (no fixed `ℂ²` instrument matches it). Not `PASS-DERIVED` | `measurement-source.md`:29, :57–63, :87, :118, :141 [R]; Step 1 F.1, control 2 |
| C-NULL | The interface of section 1.2 with the labels decoupled: the exchange writes into cells that no `F_i` reads, so `μ` alone drives the records | The cheapest check that Q3 is not met vacuously. Out of class: under a rule of 𝓡 every cell is read by its neighbours' `F_i` | Every label acts as `c(0)` does, so under Q3 every state the data constrain lies within `O(ε)` of the `n̂` axis, and Q3 and Q6 cannot hold together below an explicit constant [W]. Q3 alone is a diamond-norm statement about `𝔔`, constrained by data only through the states reached, so the expected failure is of Q3 together with Q6, not of Q3 alone. Not `PASS-DERIVED` | this proposal, section 1.4 [W] |
| C-PROG | finite-a2-v5's controller (REPORT:11–19), or Main's single controlled dynamics with its read-only program register (Main:582), compiled into `r_O` under a hypothetical rule `F_U` in second-order form that can simulate any finite controller. `F_U` is assumed for this control only, and neither R-lin nor R-nl is claimed to be such a rule. The fair bits are drawn from the uniform environment `Λ ∖ O`, and the private workspace is kept outside `O` | A simulator moved into the apparatus meets D3, D5 and D6(a). Shows that D6(b) has teeth, and fixes the classification of compiled simulators before any result | As fixed by choice 11, which is fixed at M0. Under 11(a): `r_O` is defined as the compilation of a controller whose specification uses sphere rotations and a hemisphere-law sampler (finite-a2-v5) or the instrument data of quantum mechanics (Main:582), so D6(b) fails; D7 fails as well, since `F_U ∉ 𝓡`; `OPERATIONAL-ONLY`. Under 11(b): `PASS-COMPILED`, apart from the D7 failure. Under 11(c): D7 is the only D-clause that fails, and the control then checks D7 alone | `finite-a2-v5/REPORT.md`:11–19 [R]; Main:582 [P] |
| C-EXACT | The definitions applied to the exact cases: C-POS-1 at `ε = 0` on its protocol class, and C-ISO-2, which must fail at every `ε` below its stated constant | §A.21: the operation modelled must preserve what it provably must; a definition that misclassifies an exact case is wrong | Both exact cases classified as stated above, with no slack | as above |

**Proves-too-much check** (every negative control). Each negative control's argument names the
properties of its construction that it uses (C-ISO-2 lists them in its row). At M1 each such
property is checked against three cases:

- C-POS-1;
- C-POS-2, as its menu and `M` grow;
- the class of reversible deterministic rules acting on `O` and on an environment that is never
  read, under a uniform law.

The argument must not apply to any of them. Applied to C-POS-1 or C-POS-2, it would contradict
their stated classification. Applied to the third case, it would exclude the route that section
1.7 leaves open, and no control may decide that route. If an argument applies to any of the three,
the control is red: the argument proves too much, and the criterion goes back to the owner
(section 7).

What the check is expected to find, as [W]:

- *C-ISO-2.* Its first property, that the whole state is read whenever a label acts, fails in
  all three cases, and the argument needs both properties. In C-POS-1 the hidden sphere point that
  the rotations act on is never read. In C-POS-2 the controller acts on a private workspace that
  is never read. In a reversible rule with an unread environment, the environment's state stays
  unread when `O` is read.
- *C-ISO-1, C-B1 and C-TAB.* Their arguments use more distinguishable preparations than two, and
  that property fails in each positive case.
- *C-FIN and C-CARD (a).* Their arguments are fixed-size arguments. C-POS-2 at a fixed size obeys
  them too, which is consistent with Q0's growing resources and is not a contradiction.
- *C-NULL.* Its argument uses labels that act on nothing, and that property fails in each
  positive case.

**Invariant → checkpoint table** (§A.41). Every property this proposal asserts of its own
execution, with the checkpoint that measures it.

| Invariant | Checkpoint |
|---|---|
| No computation is run in Step 2 | The result note's disclosure lists every command run; the reviewer checks it contains no interpreter, probe, checker or Lean build |
| Definitions and decision rule fixed before work | The owner-approved text of this file is identified by its sha256 in the result note; every definition used is quoted from it; any change is an amendment approved by the owner before work resumes |
| Controls green before the verdict | The control table; step 1 of section 2.2 |
| No negative control proves too much | A proves-too-much row for each negative control in the control table: the properties its argument uses, and, for each of C-POS-1, C-POS-2 and the reversible rule with an unread uniform environment, whether the property holds there; an argument whose properties all hold in one of the three cases turns the control red |
| Compiled simulators classified as fixed in advance | Choice 11 is recorded at M0; C-PROG's obtained classification is compared with the one choice 11 fixes |
| Verdict computed from the tables | Section 2.2; the reviewer recomputes the token from the two tables |
| No premise adopted | A hypothesis ledger in the result note lists H-μ, H-∞ and H-nl if used, and every [R] statement used, each with its status, and each appears in every conclusion that uses it |
| Rule class respected | A D7 row for every family considered |
| No quantum input (D6) | A D6 row for every family considered, with two entries. (a) The search of its specification for the D6 word list. (b) For each of `r_O`, `O`, `C`, `τ`, `μ` and the generating rule, how it is defined, and whether that definition, or any submitted proof of Q2 or Q3, identifies configurations of cells with numerals, tables or a sampler of a D6 quantity. A hit on either entry makes the family supplied, classified as choice 11 fixes |
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
proposal. The owner's approval record states: "A `PASS-DERIVED` would be a consistency-axis
result (§A.23); it would move no correctness assessment."

**M1. Controls.** Derive each row of section 3 on paper from the cited records, and enter the
obtained classification. Then apply the proves-too-much check to every negative control. Rests
on: Main:560, :566, :582, :596, :598 [P]; the records cited in the control table [R];
OB/CubicIsotropy.lean:116, OB/OperationalSourcing.lean:476, OB/F2CoherenceControls.lean:306,
:317 [K]. If any control is red, stop and return to the owner (section 7).

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

**M3. The decisive branch for R-lin** (if choice 1 admits R-lin). Before any constructive
attempt, decide the following question. It is stated here and not answered: no work on it was done
in drafting beyond recording the first internal review's sketch below.

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

**Expected outcome of L5.** This is an unreviewed expectation, not a result. It is the first
internal review's sketch [W], not evaluated in drafting:

1. By Lemma A(i)–(iii) [R], labels only translate the state. A label exchange is affine with a
   fixed linear part, so exchange mode is covered as well.
2. Under a law uniform on a coset, every record law is uniform on a coset of a subgroup that does
   not depend on the labels. The uniform law with a fixed `r_O` is such a law, on both carriers.
3. Take two preparations whose prefixes have equal length. Their continuation laws are equal for
   every continuation, or disjoint for every non-adaptive one, so their distinguishability is 0
   or 1. Heralds and adaptivity only form mixtures and change nothing.
4. Pad the prefixes to equal length with `c(0)`, and take states near the `|a+⟩`, `|b+⟩` of Q5
   and Q6. The comparator then needs a distinguishability bounded away from 0 and 1: two pure
   states with `Tr(P_a P_b) ∈ [1/4, 3/4]` have trace distance in `[1/2, √3/2]` [W]. That is a
   contradiction for `ε` below a small explicit constant, at `K₀ ≈ 3`.

MECH-1 records the same direction: "Any in-world source of setting selection must make the rule
non-affine in the joint state" (`mechanism-1-20261107/DESIGN.md`:434–435) [R].

If L5 confirms the sketch, after Lemma A has been re-derived under choice 9(a), the node yields
`FAIL-CLASS(R-lin, coset-uniform law, all modes)` for every `q` on both carriers. The R-lin child
nodes left open are then those under a law that is not uniform on a coset (choice 6): a level set
of the quadratic `E` (SM:296), or a non-uniform product law. Whether the sketch extends to them is
not settled. This is why choices 1 and 6 bear directly on the outcome.

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
| MECH-1 Theorem W, Proposition C, Lemma A and its consequence (`mechanism-1-20261107/DESIGN.md`:404–435, :751–766) | R | Non-Clifford encoded unitaries for class N at odd prime `q` under P1–P3 in Gross's frame; non-translational setting dependence under one fixed affine rule | Posited access and a fixed frame; Lemma A is the input to L5 and bears on R-lin only | A pass on R-lin must be consistent with Lemma A, or show where its hypotheses fail |
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
one law from the list fixed at M0, with a robustness check; the label menu is every configuration of `C`; the read
is the complete history of `O`. What remains existential is the shape of `O` and `C`, `τ`, the
generating rule `n ↦ I_n` and the comparator `𝔔`. These are fixed once for all targets and all
protocols (D1), and the comparator is a single `ℂ²` model, so they cannot be adjusted per outcome.
Q4, Q5 and Q6 are not tuned by any of them: they are checks the family either passes or fails.

**Independent prediction or postdiction a pass would have to deliver.** None can be stated with
confidence in advance. Two candidates are named so that a pass can be held to them:

1. the error law `ε(N, K)` of the passing family, fixed by `F`, `q` and `μ` with no free
   parameter: a statement about how a finite apparatus departs from a qubit. A comparison with
   precision tests of single-qubit rotations would further need a bridge from the apparatus
   region to a laboratory apparatus, which this question does not supply;
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

Each choice has options, and every choice but the first has a recommendation. The choices are
fixed at M0 and are not reopened afterwards. Choices 1 and 6 very probably decide much of the
outcome by themselves, as follows. These are unreviewed expectations, not results.

1. **Which rule.** No recommendation: this choice decides what Step 2 can find.
   - (a) **R-lin only.** This is cheap, and it is probably negative. By the expectation recorded
     in M3, MECH-1 Lemma A with a law uniform on a coset gives record laws uniform on cosets of a
     label-independent subgroup. Then two equal-length preparations are distinguishable with
     probability exactly 0 or 1, while Q5 and Q6 need intermediate values. MECH-1 already
     concludes that in-world setting selection "must make the rule non-affine in the joint state"
     (:434–435) [R]. If L5 confirms this, (a) yields `FAIL-CLASS(R-lin, coset-uniform law, all
     modes)` in essentially one node. That closes the subclass and leaves TUNE-1/Q2 open for every
     other rule. Inside R-lin, only a law not uniform on a coset escapes the sketch (choice 6).
     No new premise is involved: R-lin is the rule of ledger items (vii) and (xiii).
   - (b) **R-lin first (L5), then R-nl as a separate verdict.**
   - (c) **R-nl only.** Here the question is actually open. R-nl is non-affine, so Lemma A and the
     sketch do not apply to it. Section 1.1 gives what `main` states about R-nl: a candidate
     realization used for numerical motivation of ledger item (v) (Main:726; SM:294, :298,
     :1416), with chaos diagnostics that are numerical evidence only; nothing about its record
     laws through a region or its computational capacity. Because it is a candidate and not a
     ledger posit (it does not meet item (vii)), it enters only under the named hypothesis H-nl,
     not adopted, and carried into every conclusion. A verdict on R-nl is then a statement about
     a rule `main` does not posit. It says nothing about the ledger's linear rule, and the R-lin
     verdict says nothing about R-nl. Within "no new physical premise" (Issue #1236) this is
     admissible only as a conditional study, in the way H-∞ is. It is the owner's decision whether
     that is wanted. Cost: open-ended within the effort bound (choice 10). Because R-nl's
     computational capacity is unknown, choice 11 bears on it.
   - (d) **Both together**, each with its own token.
2. **Alphabet.** (a) Statements for each fixed `q ≥ 2`; (b) `q = 2` only (Main §3.2's instance);
   (c) a family in growing `q`. *Recommendation: (a)*, with `q = 2` first. (c) needs the
   correspondence between alphabets SM §2.7 leaves unbuilt.
3. **World.** (a) Finite tori only; (b) finite tori, and the infinite lattice under the named
   hypothesis H-∞ as a separately labelled conditional result, with its own token
   (`PASS-DERIVED[…, 𝓛_∞, … | H-μ, H-∞]`, or a `FAIL-CLASS` naming `𝓛_∞`).
   *Recommendation: (b).* It honours "finite observational access" not implying "finite
   underlying dynamics" without adopting an infinite world.
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
6. **Ensemble.** For R-lin, this choice probably decides the outcome. By the expectation recorded
   in M3, a law uniform on a coset gives `FAIL-CLASS` for R-lin, and the uniform law is such a
   law, so requiring it is the premise that decides R-lin. Requiring it is not part of the
   owner's question. The list of section 1.3 (D3): the uniform law; the uniform law on one level
   set of `E(u, v)` (SM:296); a translation- and `O_h`-invariant product law with a non-uniform
   site marginal.
   - (i) *Which law a pass must hold under.* (a) The uniform law, as the mandatory reference,
     and `μ′`. (b) One law of the list, declared at M0, and `μ′ ≠` that law. (c) Every law of the
     list, each reported with its own token; under D3's robustness clause, a pass under one law
     then counts as derived only if it also holds under a second law of the list.
     *Recommendation: (c).* No law is then picked after the results are known, and the
     uniform-law row is reported whatever the others give. Main's ledger item (iv) bears on (a)
     only through the [W] reading recorded in D3. Under (a) with choice 1(a), the expected outcome
     is `FAIL-CLASS`.
   - (ii) *The second law `μ′`, if (a) or (b).* (a) The level-set law, which is invariant under
     R-lin and has the same symmetries; (b) the non-uniform product law; (c) the uniform law,
     under (i)(b) only. *Recommendation: (a)*, for the reason given. Whenever the uniform law is
     one of the two laws a pass must hold under, R-lin is decided as above whatever the other law
     is.
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
11. **Compiled simulators.** The question is how a family is classified when it meets Q0–Q6 and
    fails only D6(b), because its ready configuration or generating rule implements a qubit
    simulator or a Born- or cosine-law sampler. Control C-PROG is classified by this choice.
    (a) Supplied (`OPERATIONAL-ONLY`). The quantum rule is in the hidden state, as in Main's
    program register (Main:582), whether it is placed there by declaration or compiled into
    `r_O`. (b) A separate token `PASS-COMPILED`, reported apart and never a pass of TUNE-1/Q2. It
    records that the rule can host such a simulator in a region chosen once, which is a statement
    about the rule's computational capacity. (c) Derived. *Recommendation: (a)*: a compiled
    simulator is the hand-choice of Step 1 made through the ready configuration. Under (a), any
    such family found is still recorded with its classification (section 2.2), so the
    information (b) would carry is kept.

***

## 10. Disclosure and review status

- **No computation was run.** Commands used in drafting r1: `git` (rev-parse, status, log,
  merge-base, branch, add, commit, push), `grep`, `sed`, `awk`, `cut`, `tr`, `wc`, `ls`, `find`,
  `head`, `tail`, `df`, `sha256sum`. `python3` was invoked once by mistake, with the one-line
  script `print(1)`, output discarded; it computed nothing about any OI rule. Commands used in
  drafting r2: `git` (status, log, show, ls-tree, diff, add, commit, push), `grep`, `sed`, `cut`,
  `fold`, `diff`, `wc`, `ls`, `sha256sum`. No interpreter was run in r2. No probe, checker or Lean
  build. No GitHub comment.
- **Read for r2**, at the pin: the first internal review of `9312b805` (in full);
  `papers/SM.md`:290–298 and the sentences of :811, :1225, :1227 and :1416 that name the rounded
  rule; `papers/Main.md`:582 and :726 (the posit ledger, in full) and the opening of :564;
  `mechanism-1-20261107/DESIGN.md`:92–100, :404–440, :990–1004;
  `finite-a2-v5/REPORT.md`:1–45; `oi-qm-ext-1/measurement-source.md`, only the lines located by
  search and cited in C-MEAS and D3 (:29, :32, :57–63, :73, :87, :118, :141, :148, :160); Step 1
  B (the owner's three classes) and its summary item 3.
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
- **Not done:** Step 2 itself; any evaluation of L5 or of any family (the M3 sketch is the
  first internal review's, recorded and not checked); any check that the controls behave as
  expected (that is M1).
- **Review status.** r1 (`9312b805`) received one fresh internal review (same model family,
  verdict REVISE, three blocking findings and twelve nits). This revision r2 is not reviewed. It
  needs a further internal review and the ChatGPT review before it goes to the owner for approval.
