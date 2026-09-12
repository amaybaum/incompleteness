# Track B act 8 — layer 1 checkpoint (Track B: the source contract, transcribed)

**The round is IN PROGRESS.** Layer 2 is **not yet executed**, which is a different status from the
*not reached* a stop produces: nothing has stopped the round, and **no outcome label `CE1`–`CE5` is
assigned or may be inferred from this checkpoint.**

Frozen preregistration: `preregistration.md` in this directory, blob
`6517f4dc7b884cb59223a685d5f3a05d4c291e36`, merged by PR #578. Executed from `main` at
`ac2907ae27ce608bbbda489bf23a876e83c606ba`.

**Layer 1 is transcription and audit — evidence level 3. No construction was attempted, and none may
be read into this file.** No Lean was written in this layer, no definition was added, and the
definition budget is unchanged: three of the five remain for layer 2.

## The authoritative surface, verified before reading

Act 1's frozen source table and act 5's authoritative-surface rule govern. **Source A** is *The
Stochastic-Quantum Correspondence*, Jacob A. Barandes, **arXiv:2302.10778v3**. The surface read is
the PDF supplied by the owner, whose p. 1 stamp reads `arXiv:2302.10778v3 [quant-ph] 30 Jul 2025`,
title *The Stochastic-Quantum Correspondence*, 38 pages, dated June 30, 2025. The arXiv HTML
rendering is non-admissible and was not consulted. **Only Source A is read here**; Sources B and C
are not consulted and not compared with it on any axis.

Every coordinate below is a page number and, where one exists, an equation number on that surface.

## E3 — the full admissibility contract for a continuous-time family

The contract is transcribed as the source states it, **including prerequisites inherited from §2 that
§3.4 does not restate locally**, per act 7's clause carried forward verbatim by the freeze. Conditions
the source does **not** state are reported below as findings, separately, and are not silently added
to the contract.

### A — kinematics

| # | Condition | Coordinate | Quoted or stated as |
| --- | --- | --- | --- |
| **A1** | A configuration space `C`, taken finite: `C ≡ {1, …, N}` | §2.1 p. 3 | "the system's configuration space `C ≡ {1, . . . , N}` has a finite number `N` of configurations" |
| **A2** | The finite case is the standing assumption | fn. 3 p. 3 | "the finite, discrete case will be assumed going forward" — continuous `C` is noted as possible but not carried |

### B — the time indices

| # | Condition | Coordinate | Quoted or stated as |
| --- | --- | --- | --- |
| **B1** | **Target times** `t`: "the set of target times `t` will **usually** be assumed to be isomorphic to the real line `ℝ`, up to a choice of measurement units" | §2.1 p. 3 | **hedged on its face by "usually"** |
| **B2** | Target time is real-valued and signed | §2.1 p. 3 | "the target time `t` is treated here as a real-valued variable that can be zero, positive, or negative, so there is no assumption of any fundamental breaking of time-reversal invariance" |
| **B3** | **Conditioning times** `t₀`: "The set of conditioning times `t₀` will be assumed to **contain at least one element**, which can be taken to be the 'initial time' `0` without loss of generality" | §2.1 p. 3 | **unhedged, and the requirement is nonemptiness** |
| **B4** | From §3.1 onward the conditioning time is fixed at `0` | §3.1 p. 6 | "For purposes of notational simplicity, the conditioning time `t₀` will now be taken to be the 'initial time' `0`" |

**B1 and B3 are asymmetric, and the asymmetry is load-bearing for E4.** The target-time set carries a
hedged convention; the conditioning-time set carries an unhedged requirement, and that requirement is
that it be **nonempty**.

### C — stochasticity, at each pair of times

| # | Condition | Coordinate | Quoted or stated as |
| --- | --- | --- | --- |
| **C1** | Non-negativity: `p_j(t₀), p_i(t), Γ_ij(t ← t₀) ≥ 0` | **(2) p. 4** | stated |
| **C2** | Normalization over the **first** index: `∑_{i=1}^{N} Γ_ij(t ← t₀) = 1` | **(3) p. 4** | stated |
| **C3** | The quantifier on C1–C2 | p. 4 | "identify it as a **(column) stochastic matrix** for **each pair of times** `t` and `t₀`" |

**C3 is the orientation clause act 7's `D2` settled and act 2's `RT1` licenses the move for.** Source
A's external orientation is column-stochastic; the OI family is row-stochastic; the transpose converts
between them. Nothing here revises `RT1`.

### D — root and continuity, stated in one sentence after (5)

Verbatim, p. 4, immediately following (5):

> The non-negativity and normalization conditions on the time-dependent transition matrix
> `Γ(t ← t₀)` identify it as a (column) stochastic matrix for each pair of times `t` and `t₀`. On
> physical grounds, `Γ(t ← t₀)` will be assumed to satisfy the **continuity condition** that in the
> limit `t → t₀`, it approaches its value `Γ(t₀ ← t₀)`, which will be taken to be the `N × N`
> identity matrix `𝟙 ≡ diag(1, …, 1)`.

| # | Condition | Coordinate | Content |
| --- | --- | --- | --- |
| **D1** | **Root**: `Γ(t₀ ← t₀) = 𝟙` | p. 4 | stated as what `Γ(t₀ ← t₀)` "will be taken to be" |
| **D2** | **Continuity**: `Γ(t ← t₀) → Γ(t₀ ← t₀)` as `t → t₀` | p. 4 | stated as an assumption made "on physical grounds" |

**D2's quantifier structure, read off the text rather than assumed** — the freeze requires this
explicitly, "over which `t₀`, and in which variable the limit is taken":

- **The limit is taken in the TARGET variable `t`.** `t₀` is held fixed while `t → t₀`.
- **The condition is indexed by `t₀`, ranging over the conditioning-time set of B3.** Under B4's
  reduction that set is `{0}`, so on the surface the correspondence actually runs on, **D2 binds at
  `t₀ = 0` alone**: `Γ̂(t ← 0) → 𝟙` as `t → 0`.
- **D2 is a one-point limit condition at the conditioning time. It is NOT a requirement that
  `t ↦ Γ(t ← t₀)` be continuous at every `t`.** The source states no such requirement anywhere; see
  finding **F-1** below.

### E — divisibility is declined, not required in either direction

| # | Condition | Coordinate | Content |
| --- | --- | --- | --- |
| **E1** | Divisibility (6) is **not assumed** | (6) p. 4 | "`Γ(t ← t₀)` will **not** be assumed to be 'divisible'" |

**E1 removes a condition; it does not add one.** Nothing in the contract requires an admissible family
to be indivisible or non-Markovian. Act 1's `BD3` governs the reading and is unrevised: "indivisible
stochastic process" is a **tuple/class definition**, and class membership neither entails nor is
entailed by failure of divisibility — Markov chains are members, and (57)–(58) p. 19 exhibits one.
**This round therefore does not treat indivisibility as an admissibility burden on an extension, and
does not argue from it.**

### F — the Θ / Kraus layer: entailed by C, adding no hypothesis

| # | Item | Coordinate | Status in the contract |
| --- | --- | --- | --- |
| **F1** | `Γ_ij(t ← 0) = \|Θ_ij(t ← 0)\|²` | **(12) p. 6** | **not a hypothesis** — "this equation is **not a postulate**—it is a mathematical identity"; `Θ` "is guaranteed to exist, although it is not unique" (p. 7) |
| **F2** | `∑_{i=1}^{N} \|Θ_ij(t ← 0)\|² = 1` | **(13) p. 7** | **entailed** — "**Due to the normalization condition** on the transition matrix `Γ(t ← 0)`" |
| **F3** | No unitarity on `Θ` at this stage | p. 7 | "For now, **no further conditions, such as unitarity, will be imposed** on `Θ(t ← 0)`" |
| **F4** | `K_β(t ← 0) ≡ Θ(t ← 0)P_β` | **(25) p. 10** | a definition |
| **F5** | Kraus identity `∑_β K_β†(t ← 0)K_β(t ← 0) = 𝟙` | **(26) p. 10** | **entailed** — "The summation condition on `Θ(t ← 0)` **then becomes** the statement that…" |
| **F6** | Number system for `Θ`: complex "at most" | p. 7 | a **choice**, act 5's `F1`/`F2` territory, not adjudicated here |

**The finding that matters for layer 2: F1–F5 impose NOTHING beyond C1 and C2 at the given `t`.** The
entire potential-and-Kraus layer the freeze asked about — (12) p. 6, (13) p. 7, (25)–(26) p. 10 — is
stated as identities and consequences of pointwise column-stochasticity. It requires no regularity in
`t`, no divisibility, and no relation between different times. Act 7's `D2` recorded these as
"follows ✓" for its discrete witness; this layer records **why**, with the source's own words, since
layer 2's admissibility predicate is transcribed from here.

### G — the §3.4 dilation: what it consumes and what it supplies

| # | Item | Coordinate | Content |
| --- | --- | --- | --- |
| **G1** | The **trigger** | §3.4 p. 10 | "if `Θ(t ← 0)` is **not already a unitary matrix**, then one can turn it into a unitary matrix by enlarging or **dilating** the original `N`-element configuration space" |
| **G2** | Ancilla bound | §3.4 p. 10 | `N′ ≤ N²`, dilated size `Ñ ≤ N³`; the ancilla "need not be regarded as physical" |
| **G3** | What Stinespring supplies | §3.4 p. 10 | **existence**, at each `t`: "implies the existence of an `Ñ × Ñ` unitary time-evolution operator", recovering `Γ` by marginalization "for **at least some** choices of the ancilla's configuration `j′`" |
| **G4** | The post-dilation reduction | **(28)–(29) p. 11** | "**Without any real loss of generality**… one can focus on the case in which the time-evolution operator is unitary" — a reduction, not a condition on `Γ̂` |
| **G5** | Unistochasticity named | **(30)–(31) p. 11** | `Γ_ij(t ← 0) = \|U_ij(t ← 0)\|²`; "a unistochastic matrix is a square matrix whose individual entries are the modulus-squares of the corresponding entries of a unitary matrix" |

**G1 is `O-C`'s coordinate and act 7's `D1`, cited and unrevised.** G3 is act 7's `D3` gap —
pointwise existence with no coherent time-indexed family derived or selected — **recorded here as
inherited, and not reopened.**

### H — regularity, and exactly where it binds

| # | Item | Coordinate | What it binds |
| --- | --- | --- | --- |
| **H1** | Differentiability | **(33) p. 12** | "Assuming a unistochastic process based on a unitary time-evolution operator `U(t ← 0)` that is a **differentiable function of the time `t`**, one can define a corresponding self-adjoint generator `H(t)`…" |

**H1 binds `U(t ← 0)` — the post-(28) unitary family — and nothing else.** It does not bind `Γ̂`, it
does not bind `Θ` in general, and it is stated as a hypothesis **of the Hamiltonian derivation** ((33)
p. 12 and its consequences (34)–(36) pp. 12–13), not as an admissibility condition on an indivisible
stochastic process. This is act 7's `D3` reading, confirmed against the surface and unrevised.

**The freeze asked whether an analogue of (33) binds `Γ̂` itself, the `Θ` built from it, both, or
neither. The answer is: NEITHER.** No differentiability or smoothness is required of `Γ̂` anywhere in
Source A, and none is required of `Θ`. "Smooth" appears twice more and descriptively only — of the
p. 4 examples (7), and in fn. 11 p. 12 — never as a condition imposed on an admissible family.

### I — a consequence available as a test, recorded but not relied on

| # | Item | Coordinate | Content |
| --- | --- | --- | --- |
| **I1** | Every unistochastic transition matrix is doubly stochastic | **(32) p. 12** | `∑_i Γ_ij = ∑_j Γ_ij = 1` |

**I1 is the source's own statement of the route act 6 proved in-round** through
`collapsed_slice_not_unistochastic`, which computes a **row** sum on `Aᵀ`. It is recorded as a
coordinate, not adopted as a lemma: act 6's proof stands on its own and nothing here imports I1 as
evidence.

### The contract, assembled

**An admissible continuous-time family, on Source A's stated terms, is exactly this:** a family
`Γ̂(t ← t₀)` of `N × N` matrices over a finite `C` (A1–A2), indexed by target times and by a
**nonempty** set of conditioning times (B1–B4), non-negative and normalized over the first index at
**each pair of times** (C1–C3), equal to `𝟙` at `t = t₀` (D1), and approaching `𝟙` in the limit
`t → t₀` for each conditioning time `t₀` (D2). Divisibility is not required (E1). The potential and
Kraus layer follows with no further hypothesis (F1–F5). The §3.4 dilation consumes `Θ(t ← 0)` at each
`t` where it is invoked (G1–G3). Differentiability enters only at (33) p. 12 and only on `U` (H1).

**That is the whole of it.** The contract is fixed here and is not narrowed or widened afterwards, in
either direction, whatever layer 2 finds.

### Source-implicit conditions, named as findings

Control 5 requires that any condition the source leaves implicit be reported as a finding rather than
folded into the contract. Four are recorded.

**`F-1` — no global continuity of `t ↦ Γ̂(t ← 0)` is stated.** D2 is a limit at the conditioning time
only. A family continuous at `0` and discontinuous elsewhere meets D2 as written. The source assumes
regularity in `t` exactly once, at (33) p. 12, and there on `U`, not on `Γ̂`.

**`F-2` — no link is stated from `Γ̂`'s regularity to `Θ`'s or `U`'s.** (33) p. 12 assumes
differentiability of `U` directly. `Θ` is non-unique (p. 7) and carries a **time-dependent phase
gauge** `Θ_ij(t ← 0) ↦ exp(θ_ij(t))Θ_ij(t ← 0)` (fn. 6 p. 7), so regularity of `Γ̂` does not by itself
select a regular `Θ`, and the source does not claim it does. This is the **regularity face** of act
7's `D3` derivation-and-selection gap; it is recorded as inherited and open, and `D3` is not revised.

**`F-3` — the target-time domain is hedged and the conditioning-time domain is not.** B1 says
"usually"; B3 does not. Act 7's `D2` already drew this distinction, treating the real-line convention
as a domain mismatch rather than an independent hard failure, and resting `DC2a` on D2 alone. **That
reading is inherited here unchanged and is not re-adjudicated.**

**`F-4` — admissibility does not require indivisibility.** Per E1 and `BD3`. Recorded so that no
later step reads an extension's divisibility as an admissibility failure, or its indivisibility as
evidence of anything.

### The domain gap this layer opens, stated rather than deferred silently

Layer 0 fixed the extension relation's ambient domain as `ℝ≥0`, before the source was read, for a
Track I reason recorded there. **B1 asks for `ℝ`.** These do not agree, and layer 1 records the
disagreement now rather than discovering it convenient later:

- The layer-0 relation is a **Track I** object and is not revised by a Track B finding; the freeze's
  two-predicate design exists precisely so that source admissibility is a **second** predicate applied
  to an extension, never fused into the first.
- **Layer 2 therefore carries an explicit obligation**: either extend to all of `ℝ` and satisfy B1 as
  stated, or satisfy the contract on `t ≥ 0` and **say so**, citing B1's own hedge and act 7's
  `F-3` reading. **Which of these the round does is a layer-2 report item, not a layer-1
  determination, and it may not be settled by whichever turns out to be easier to build.**

## E4 — ROOTED. The contract is satisfied by a family with conditioning-time set `{0}`

**The finding: Source A's admissibility contract does NOT require a full two-time family
`Γ̂(t ← t₀)` over all pairs. A rooted family `Γ̂(t ← 0)` satisfies it.**

**The coordinates that establish it, both quoted above:**

1. **§2.1 p. 3, B3** — "The set of conditioning times `t₀` will be assumed to **contain at least one
   element**, which can be taken to be the 'initial time' `0` without loss of generality." The
   requirement placed on the conditioning-time set is **nonemptiness**. A singleton meets it.
2. **§3.1 p. 6, B4** — "For purposes of notational simplicity, the conditioning time `t₀` will now be
   taken to be the 'initial time' `0`." Every object of the correspondence from (12) p. 6 onward is
   written `(t ← 0)`: `Θ(t ← 0)`, `ρ(t)`, `Ψ(t)`, the Kraus operators (25) p. 10, the dilation §3.4
   p. 10, `U(t ← 0)` at (28) p. 11, and the Hamiltonian (33) p. 12.

**And the confirmation that decides it — the source's own two-time objects are DERIVED from the rooted
family, not posited alongside it:**

3. **(37) p. 13** — `Γ̃(t ← t′) ≡ Γ(t ← 0)Γ⁻¹(t′ ← 0)`, defined from the rooted family where the
   inverse exists.
4. **(39) p. 13** — the relative time-evolution operator `U(t ← t′) ≡ U(t ← 0)U†(t′ ← 0)`, likewise
   defined from the rooted family.

So where Source A uses two times, it **constructs** the two-time object out of the rooted one. It does
not require a two-time family as an input datum.

### The evidence pointing the other way, recorded rather than suppressed

The freeze warned that "the temptation to read it as rooted — E0's own shape — is strong" and called
the two-time reading roughly even money. Everything cutting against the finding is therefore recorded
here, with coordinates, and answered:

| Points toward two-time | Coordinate | Why it does not change the finding |
| --- | --- | --- |
| The general definition uses **two index sets**, "possibly distinct", and writes `Γ_{t←t₀}` generically | §2.1 p. 3 | It **permits** many conditioning times; B3 **requires** only one. Permission is not a requirement. |
| D2's continuity is stated for `Γ(t ← t₀)` generically | p. 4 | Its quantifier is over the conditioning-time set. If that set is `{0}`, D2 binds at `0`. The quantifier was read off the text, per the freeze's instruction, not assumed. |
| "the initial time `0` will typically be only one of **many** conditioning times" | §2.1 p. 3, forward-referencing §3.7 | A **derived** claim about systems "in sufficiently strong contact with a repeatedly eavesdropping environment", under added physical hypotheses — and hedged by "typically". Not an admissibility condition. |
| **Division events**: `t′` "has become a valid conditioning time"; `Γ^S(t ← 0) = Γ^S(t ← t′)Γ^S(t′ ← 0)` | §3.7 **(56) p. 19** | Derived from an environment interaction, and it produces **divisibility** at `t′` — the opposite of the generic case. It describes what happens to some systems, not what a family must satisfy to be admissible. |
| fn. 11 p. 12 writes `Γ_ij(n δt + t ← n δt)`, a **non-zero** conditioning time | fn. 11 p. 12 | An illustrative interpolation formula, not a statement of the contract. It is layer 2's control (E6) and is **not run here**. |

**The distinction the finding rests on is between what the contract REQUIRES and what the source
elsewhere DERIVES or PERMITS.** Only B3 is a requirement on the conditioning-time set, and it is
satisfied by `{0}`.

### Consequences — and what does NOT fire

**The freeze's two-time branch does not fire.** Its three consequences — that the obligation includes
constructing the two-time family, that the two-time family is a further selection, and that continuity
binds at every `t₀` — are **not triggered**, because the contract does not require the two-time
family. This is recorded explicitly so that silence is not later read as a skipped step.

**In particular, the freeze's `BD3` prohibition is carried forward unused and unweakened.** Had the
answer been two-time, the round would have been required to say that the rooted family alone does not
supply a two-time family **absent an established composition or selection theorem**, and forbidden
from arguing it from indivisibility or class membership. That prohibition stands; this round has no
occasion to invoke it, and **invokes nothing in its place**.

**What E4 does establish for layer 2, and only this:** the continuity condition D2 binds at `t₀ = 0`,
in the limit `t → 0`, and the object the correspondence consumes throughout is the rooted family. The
obligation acts 6 and 7 identified is at the rooted family, and Source A puts its correspondence
there too.

**E4 is not a finding about how much of Source A a rooted family exercises.** It says the contract is
met, not that the two-time structures of §3.5 and §3.7 are dispensable or that anything follows about
them.

## E5 — `O-A`, `O-B`, `O-C` located, separately

| Label | The object it is about | Where it must hold | Coordinate fixing it |
| --- | --- | --- | --- |
| **`O-A`** | the continuous family `Γ̂` | **somewhere** in the ambient domain: `∃ t` with `¬ IsUnistochastic ((Γ̂ t)ᵀ)` | unistochasticity as Source A defines it, (30)–(31) and the naming sentence, p. 11 |
| **`O-B`** | the **discrete restriction** `restrict Γ̂` | **at an embedded time**: `∃ n : ℕ` with `¬ IsUnistochastic ((Γ̂ (ι n))ᵀ)` | act 6's `UB2`, via `collapsed_slice_not_unistochastic`; the source's own (32) p. 12 is the same route and is cited, not imported |
| **`O-C`** | the **potential** `Θ(t ← 0)` — a different object from the transition matrix | at the time index where §3.4's dilation is invoked | **§3.4 p. 10**: "if `Θ(t ← 0)` is **not already a unitary matrix**" — act 7's `D1` |

**The required conjunction, as frozen: `CE1` requires `O-B ∧ O-C`.** `O-A` alone is never sufficient,
and a result stating only `O-A` is reported as `O-A`.

### Two locations E5 fixes now, before any construction

The freeze leaves E5 to fix where off-directness must hold. Two determinations are made here, in
layer 1, so that layer 2 cannot make them after seeing what is convenient.

**`L1` — `O-B`'s index, on act 6's merged witness.** Act 6's witness is `Γ 0 = 𝟙` with period `2` and
`A = [[1,0],[1,0]]` at odd times. Its transpose `Aᵀ = [[1,1],[0,0]]` is column-stochastic with row
sums `2` and `0`, which is what `collapsed_slice_not_unistochastic` computes. So `O-B` is available at
**every odd `n`**, and the index this round uses is **`n = 1`**. Layer 0's
`screening_extension_nonunistochastic_slice` already proves non-unistochasticity of that slice at
`t = 1` for the screening extension; that theorem answers E0's own wording and **is not `O-B` for a
layer-2 construction**, which must prove it of whatever extension layer 2 exhibits.

**`L2` — `O-C`'s index and its quantifier over the non-unique `Θ`.** Two readings of G1 are possible,
because `Θ` is not unique (p. 7) and carries the time-dependent phase gauge of fn. 6 p. 7:

- **de re** — *some particular chosen* `Θ(t ← 0)` fails to be unitary;
- **de dicto** — *no* admissible `Θ(t ← 0)` at that time is unitary.

**This round uses the de dicto reading, and that choice is made here and fixed.** The de re reading
would let an extension satisfy `O-C` while a gauge change produced a unitary `Θ` at the same time — so
§3.4's dilation would be avoidable, and "the source's construction never enters its dilated branch" is
exactly the failure the freeze's `O-C` clause exists to block. The de dicto reading is a
**strengthening** of the requirement, adopted before construction, and it is not a narrowing of the
contract. **`O-C`'s time index is fixed to coincide with `L1`'s**: the embedded time `n = 1` at which
`O-B` holds, since §3.4's dilation is invoked per-`t` (act 7's `D3`).

### Entailments: what is available, what is required, and what is NOT yet proved

Control 7 requires that **every entailment among `O-A`, `O-B` and `O-C` that the round uses be proved
in-round**. None is proved in layer 1, and none is assumed. The status of each is recorded:

| Entailment | Status |
| --- | --- |
| `O-B ⟹ O-A` | **available and unproved.** An embedded time is a time. If layer 2 uses it, layer 2 proves it. |
| `O-A ⟹ O-B` | **false in general** and not used. A family may leave the unistochastic set strictly between embedded times and sit inside it at every embedded time. |
| `¬ IsUnistochastic ((Γ̂ (ι n))ᵀ) ⟹ O-C` at `n`, under `L2` | **required for `CE1`, and NOT proved.** The route runs through (12) p. 6 together with act 6's structural lemma: under the de dicto reading, `O-C` at a time says no `Θ` there is unitary, and by F1 a unitary `Θ` at that time would exhibit the slice as unistochastic. **The transpose orientation must be handled explicitly in that proof.** Layer 2 proves this in-round or the round does not use it. |

**Nothing in the informal reading above is evidence.** The three propositions remain distinct until a
kernel-checked proof relates them.

## The preservation burden — its status entering layer 2

The freeze's four clauses are **layer 2's to discharge**, and none is discharged here. One is settled
in advance and is recorded now:

**Clause 3 is settled: the witness is act 6's merged one.** It is already frozen, `UB2` is merged, and
**no append-only amendment is anticipated or required.** The freeze anticipated one by name in case a
different witness were needed; none is. Substituting a witness at execution time is foreclosed.

Clauses 1, 2 and 4 — `PPer` membership of the restriction, `O-B`, and `O-C` — are **unproved** and are
layer 2's, each to be proved rather than asserted.

## What layer 1 does NOT establish

- **No outcome label.** `CE1`, `CE2`, `CE3`, `CE4` and `CE5` are all unassigned.
- **No construction, and no witness search.** Layer 2 is unexecuted.
- **No `O-A`, `O-B` or `O-C` for any layer-2 object**, and no entailment among them proved.
- **`E6` is not run.** The fn. 11 control (fn. 11 p. 12) is layer 2's, and its non-applicability is a
  live answer there. Nothing in this file prejudges it. The observation that fn. 11's formula uses a
  non-zero conditioning time is recorded above **only** as evidence bearing on E4, not as a finding
  about the control.
- **Nothing about act 7.** `D4a`/`D4b` remain *not reached*; only `CE1` reopens act 7, at the
  adjudication with the signs unset. `DC2a` is cited and unrevised, and act 7's `D3` gap is recorded
  as inherited, not reopened.
- **No adjudication of act 5's freedoms.** `F1` versus `F2` is untouched; F6 above is a transcription,
  not a decision.
- **No candidate-selection principle** is adopted or proposed.
- **`BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1`, `UB2` and `DC2a` are cited and unrevised.**
- **No claim that Source A is applicable or inapplicable**, and no claim that the correspondence
  succeeds or fails. E3 transcribes a contract; it adjudicates nothing.
- **No sourcing inference in either track direction**, and no manuscript edit.

## The prediction, and whether it held

The freeze predicted: "**The live uncertainty is E3 and E4** … Call the two-time reading roughly even
money; it is asked with a coordinate precisely because the temptation to read it as rooted — E0's own
shape — is strong."

**That prediction did not hold in the direction the freeze leaned toward.** E4 returns **rooted**, on
B3's nonemptiness requirement and B4's reduction, confirmed by (37) and (39) p. 13 deriving the
source's two-time objects from the rooted family. The freeze's hardest anticipated cost — a second
construction with no composition theorem to determine it — **does not arrive.**

**That is reported as the finding it is, and at no more than its strength.** It removes an
anticipated obligation; it supplies no construction, and it makes nothing about layer 2 easier except
by not adding to it. The round's difficulty now sits where E3's findings put it: `F-1` and `F-2` —
that the source states no regularity on `Γ̂` and no link from `Γ̂`'s regularity to `Θ`'s — together
with the `ℝ` versus `ℝ≥0` domain gap, and the unproved `O-C` entailment that `CE1` requires.
