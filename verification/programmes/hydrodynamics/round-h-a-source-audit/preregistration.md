# Hydrodynamics round H-A — the source audit of the concrete wave representative: CONTROL PLANE

Owner-called, under `../PROGRAMME.md` §6 ("Round H-A — hydrodynamic source audit"). This file is
the whole of round H-A's control plane and is merged **alone**, before any execution object exists.
The round inventories the concrete OI substratum — the manuscripts' discrete wave rule as the
kernel already carries it — against the exact ingredients of deterministic lattice hydrodynamics,
one item at a time, and reports each as **HD**, **HC**, **HI** or **HO** in the programme's taxonomy.

**Blob identity is authoritative.** The execution guard pins this file by content.

**Parallel-track separation.** This round runs on its own branch from `main` at
`b821d69ae86f7d76020383735b3161e77c064ccc`. It neither consumes nor produces evidence for the
OI → QM chain (Track B, Track I), for Bell, or for gravity; the programme's control 1 applies in
full.

## Start state

| | |
| --- | --- |
| Merged `main` | `b821d69ae86f7d76020383735b3161e77c064ccc` (PR #591) |
| The programme roadmap | `../PROGRAMME.md`, blob `bda6a01e41c046b07536e06d2f81b4085b89cd0b` — its status line names an earlier base; the roadmap is consumed as the taxonomy and round list, and its §8 one-line state is not edited by this PR |
| The concrete substratum in the kernel | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` — `waveF`, `waveRule`, `waveSubstratum`, and `waveSubstratum_A1` … `waveSubstratum_A5` |
| The phase-space update | `verification/lean-mathlib/OIBridge/SecondOrderCircuit.lean`, blob `4eacbb0910dd7b9002640847a7bb4929ca7b92b9` — `leap F x i = ((x i).2, F (curOf x) i − (x i).1)`, `leapEquiv` |
| The rule interface | `verification/lean-mathlib/OIBridge/SecondOrderLayer.lean`, blob `fb7e172024597ba3e217a993169447753fa052ec` — `Rule` |
| The isotropy layer | `verification/lean-mathlib/OIBridge/CubicIsotropy.lean`, blob `c1918dc0c4ffaf1547f1918e6665f7c086233796` — `OhInvariant`, `ohInvariant_iff`, `quadratic_isotropic`, `quartic_ohInvariant`, `quartic_not_isotropic` |
| The manuscript's rule and gauge principle | `papers/SM.md`, blob `bad76808e6ab708732edcb3c6294236aa052cf34` — §2.7 "The alphabet as gauge freedom"; §4.1's rule `f = Σ_nn x − x(t−1)`; Corollary 1a; "The two roles of the dynamics, stated explicitly" |
| The substratum gauge group | `papers/Substratum.md`, blob `0ada99357ffd6f475beb1fab4adaa597dc4eae9d` — Theorem 24 (ii), alphabet change, "parametrized by all integers `q ≥ 2`" |

## The object, FROZEN

The concrete substratum is exactly the kernel's `waveSubstratum d L q α`: sites `Fin d → ZMod L`
(a cubic torus of side `L`), alphabet `ZMod q`, and the second-order update in phase-space form

```
x_{t+1}(i) = F(x_t)(i) − x_{t−1}(i),      F(x)(i) = α · Σ_{p : Fin d × Bool} x(i + dir p),
```

so that `F` is `α` times the sum over the `2d` axis neighbours. The manuscript's rule is `α = 1`;
`q` is **free**, and by [SM §2.7] and [Substratum, Theorem 24 (ii)] it is a **gauge parameter**:
"every prediction of the OI framework is independent of the alphabet size `q`", and alphabet change
to any `q' ≥ 2` "leaves all observables unchanged", conditional on the stated `q`-gauge principle.
**There is no manuscript-fixed `q` to discover**, and the round does not go looking for one.

The kernel already proves, at evidence level 2: `waveSubstratum_A1` (finiteness),
`waveSubstratum_A2` (bijectivity), `waveSubstratum_A3` (degree `2d`), `waveSubstratum_A4Exact`
(translation covariance), and **`waveSubstratum_A5` (additivity of `F`)**. These are consumed
unmodified; none is re-proved.

Two facts about the object fix the round's framing and are recorded here so the execution cannot
drift from them.

1. **The exact dynamics is additive over `ZMod q`.** [SM] "The two roles of the dynamics" says so in
   terms — the linear rule is exact modular-linear algebra, and the mod-`q` wraparound is "a bounded
   nonlinearity that is present in any faithful finite realization". `waveSubstratum_A5` is that
   statement in the kernel. The round consumes it; it does not test it.
2. **The lattice stencil is the `2d` axis directions `±e_k`.** Nothing else enters `F`. Isotropy
   questions are questions about this stencil and no other.

## Why this round exists, and what it can and cannot decide

The programme's H1–H7 ladder starts from conservation laws and isotropy because a Navier–Stokes
limit needs, at least, a locally conserved density, a locally conserved momentum, an isotropic
fourth-rank velocity moment for the stress expansion, a closure, and a scaling map. The source audit
asks, for the **present wave representative** and for nothing broader, which of those it already
supplies. Two of the answers turn out to be sharp enough to freeze as predictions with reasons:

- **Linearity.** An additive microscopic rule composed with an additive coarse-graining yields an
  additive coarse recurrence. The advection term `(u·∇)u` of Euler/Navier–Stokes is quadratic. So
  under `ZMod q`-linear coarse variables the advective nonlinearity **cannot arise** — not as a
  matter of approximation but of algebra. This is a conditional no-go, conditional on the class of
  coarse variables, and the round says exactly that.
- **`q`-dependence of the total-sum conservation law.** The only candidate conserved "momentum-like"
  quantity built from the total field sum is the first difference `ΔS_t = S_t − S_{t−1}`, and it is
  conserved for every configuration **iff** `2dα ≡ 2 (mod q)`. At `d = 3`, `α = 1` that is `q ∣ 4`,
  i.e. `q ∈ {2, 4}`. A physical conservation law would have to be `q`-gauge invariant. **This one is
  not.** The round freezes that as the finding — about **this candidate field under the present
  rule** — and **not** as a universal no-go for every possible hydrodynamic variable.

What the round cannot decide, and does not claim to: whether a *different* OI-compatible reversible
local substratum (round H-B's question) supplies what this one does not; whether nonlinear or
real-valued coarse variables of the present rule carry an advective term; whether a statistical
closure exists at any scale. Those are recorded **HO**, and H-B stays alive whatever H-A returns.

## Targets, FROZEN

Every target is stated for `waveSubstratum d L q α` with `[NeZero L]` (a nonempty torus), the
manuscript instance `α = 1` recorded separately where it changes the arithmetic, and `q ≥ 2`
throughout (`ZMod q` with `q = 0` is `ℤ`, outside the manuscript's alphabet class and outside this
round).

### `H0` — the linearity gate

**`H0-a` (kernel).** For every `ZMod q`-linear coarse map `C : (sites → ZMod q) →+ (blocks → ZMod q)`,
the coarse two-time evolution `(x_{t−1}, x_t) ↦ (C x_t, C x_{t+1})` is `ZMod q`-linear. Immediate
from `waveSubstratum_A5` and additivity of `C`; stated so that `H0-b` has a hypothesis to consume.

**`H0-b` (kernel).** If a coarse rule `Φ : (blocks → ZMod q) × (blocks → ZMod q) → (blocks → ZMod q)`
**closes** — `C x_{t+1} = Φ(C x_t, C x_{t−1})` for every microscopic pair — then `Φ` agrees with an
additive map on the range of `(C, C)`. Consequently no closed `ZMod q`-linear coarse description of
the present rule carries a quadratic (advective) term on the coarse states it is defined on.

**Prediction: positive, full strength.** The proof is the composition of two additive maps.

**Reported status for the advection obligation: HI, conditional on the coarse-variable class.** The
class is `ZMod q`-linear coarse-graining, named in the statement. **Real-valued or nonlinear coarse
variables are HO**: the round does **not** freeze "the mod-`q` wraparound is the only nonlinearity
available", because a real lift `ZMod q → ℤ → ℝ` followed by products is *a* nonlinear
coarse-graining, and whether it carries an advective term is a separate question this round neither
asks nor answers.

### `H1` — the total-sum conservation law and its `q`-gauge invariance

Let `S_t = Σ_i x_t(i) ∈ ZMod q`. On the torus every translate of a configuration has the same total,
so `Σ_i F(x)(i) = 2dα · S`, hence `S_{t+1} = 2dα S_t − S_{t−1}` for every trajectory.

**`H1-a` (kernel).** The first difference `ΔS_t = S_t − S_{t−1}` is conserved along **every**
trajectory iff `(2dα − 2 : ZMod q) = 0`. Both directions: if `2dα = 2` then
`ΔS_{t+1} = (2dα − 2) S_t + ΔS_t = ΔS_t`; conversely conservation on the trajectory with
`x_{t−1} = 0` and `x_t = δ_{i₀}` (one site, needing `L ≥ 1`) gives `S_t = 1`, `ΔS_t = 1`,
`ΔS_{t+1} = 2dα − 2`, forcing `2dα − 2 = 0`.

**`H1-b` (kernel).** More generally, a combination `a S_t + b S_{t−1}` is conserved on every
trajectory iff `b = −a` and `a · (2dα − 2) = 0` in `ZMod q`. So the first difference is the only
shape a universally conserved total-sum combination can take, and it is available exactly when the
coefficient `2dα − 2` annihilates `a`.

**`H1-c` (kernel, the manuscript instance).** At `d = 3`, `α = 1`: `ΔS` is conserved for every
trajectory iff `q ∣ 4`, i.e. iff `q ∈ {2, 4}`.

**Prediction: positive, full strength**, for all three; the arithmetic was checked by hand before
this file was written and is recorded here so no execution-specific artifact precedes the freeze.

**The `q`-gauge test, FROZEN.** [SM §2.7] and [Substratum, Theorem 24 (ii)] make `q` a gauge
parameter whose choice leaves all observables unchanged. A conservation law of a physical
hydrodynamic field is an observable statement. `H1-c` shows the candidate law holds for two alphabet
sizes and fails for every other `q ≥ 2`. **Therefore the candidate conserved field `ΔS` is not
`q`-gauge invariant**, and under the stated gauge principle it cannot be the universal conserved
hydrodynamic momentum of the present wave rule. **The execution does not choose `q = 2` or `q = 4`
to rescue the field**, and the round does not report "the substratum has a conserved momentum at
`q = 4`" as a hydrodynamic finding.

**Bounded reading, FROZEN in terms.** The finding is that **this candidate field**, under **this
rule**, fails `q`-gauge invariance. It is **not** a universal no-go for all possible hydrodynamic
variables: block variables, real-lifted variables, currents built from differences, and any variable
of a different substratum are outside `H1` and are **HO** until a round asks about them.

**A recorded reading of the coefficient, analysis only.** Writing the update as
`x_{t+1} − 2x_t + x_{t−1} = α Σ_nn x − 2 x_t`, the zero-mode recurrence
`S_{t+1} − 2S_t + S_{t−1} = (2dα − 2) S_t` carries the on-site coefficient `2dα − 2` that a discrete
Laplacian would cancel and this rule does not; `H1-a` is the statement that the zero mode is
conserved exactly when that coefficient vanishes mod `q`. This is recorded as an interpretation of
the same identity, not as a separate target, and it licenses no claim about a mass, a metric, or a
continuum operator.

**Reported status for H1: HI for the total-sum candidate under the `q`-gauge principle; HO for every
other candidate conserved field.**

### `H2a`, `H2b` — the fourth-rank tensor Navier–Stokes needs, and the axis stencil against it

The stress expansion of a lattice-gas hydrodynamic derivation needs the fully symmetric fourth
velocity moment of the stencil to be isotropic. Under the rotation group the fully symmetric
isotropic rank-4 tensors on `ℝ³` form a one-dimensional space (spanned by
`δ_{(ab}δ_{cd)}`); under the cubic group `O_h` they form a two-dimensional space (the two
independent quartic invariants `Σ_i k_i⁴` and `(Σ_i k_i²)²`, which [SM] Corollary 1a already names
and the kernel's `quartic_ohInvariant`/`quartic_not_isotropic` already separate).

**`H2a` (kernel, targeted at level 2).** The space of `O_h`-invariant fully symmetric rank-4 tensors
on `ℝ³`, identified with `O_h`-invariant homogeneous quartic forms, is spanned by `Σ_i k_i⁴` and
`(Σ_i k_i²)²` and is two-dimensional; the rotation-invariant ones are the multiples of `(Σ_i k_i²)²`,
one-dimensional. **Prediction: positive.** Strength high for the spanning set (the two invariants
exist and are independent — `quartic_not_isotropic` already exhibits the independence), **medium**
for the exact dimension count at kernel level, since the "no other invariant" direction is a
finite averaging argument over the 15 quartic monomials that may exceed the round formally.
**Fallback, frozen now:** if the count is not reached at level 2, it is reported at evidence level 3
(an exact enumeration in a probe) with the label stated, and the spanning statement at level 2.
**The counts are the fully symmetric ones — 2 versus 1.** The general (non-symmetric) rank-4
invariant counts are different objects and are not this round's.

**`H2b` (kernel).** The fourth moment of the present stencil, `T_{abcd} = Σ_{p} (dir p)_a (dir p)_b
(dir p)_c (dir p)_d` over the `2d` axis directions `±e_k`, equals `2 · [a = b = c = d]` — nonzero
only on the diagonal. Its quartic form is `2 Σ_i k_i⁴`, which by `quartic_not_isotropic` is **not** a
function of `|k|²`; so `T` is `O_h`-invariant but **not** rotation-invariant, and the present stencil
**fails** the isotropy the stress expansion requires. **Prediction: positive (the failure), full
strength.** The computation consumes the existing quartic-anisotropy result and adds only the
stencil moment.

**Reported status for H2: exact stencil anisotropy proved; conditional HI if H5's stress closure
consumes this tensor; otherwise H2 remains HO.** Whether the bare fourth moment of the stencil is
the effective rank-4 tensor the H5 stress closure consumes is a bridge this round does **not**
build; until it lands, the anisotropy is a proved fact about the stencil and a *conditional* finding
about hydrodynamics, and the round does not label the isotropy obligation HI outright. This is the
cubic-lattice fourth-order anisotropy that deterministic lattice-gas hydrodynamics historically had
to escape by changing the stencil; it says nothing about stencils the round does not examine, and
it is precisely the kind of finding H-B is designed to act on. Corollary 1a's quadratic isotropy is consumed unchanged and is
**not** contradicted: quadratic order is isotropic, quartic order is not, and Navier–Stokes needs
the quartic order.

### `H3a` — a block-observable diagnostic for closure

Freeze one coarse observable before testing it: for a block partition of the torus into cubes of
side `b ∣ L`, the block sums `B_β(x) = Σ_{i ∈ β} x(i) ∈ ZMod q`, and the two-time block state
`(B(x_t), B(x_{t−1}))`.

**`H3a` (kernel).** The block state does **not** close: there exist two microscopic pairs with equal
block states at `(t, t−1)` whose block states at `t + 1` differ. The witness, valid for **every**
`q ≥ 2`, is at `d = 1`, `L = 6`, `b = 3`, `α = 1`, pinned by equation in the statement: both pairs
have `x_{t−1} = 0`; one has `x_t = 0`, the other `x_t = y = (−1, 1, 0, 0, 0, 0)`. Both block states
are `(0, 0)` at `t` and at `t − 1`. At `t + 1` the zero trajectory stays zero, while on block
`{0, 1, 2}`
`Σ_{i∈{0,1,2}} F(y)_i = (y_5 + y_1) + (y_0 + y_2) + (y_1 + y_3) = 1 ≠ 0`.
**The smaller candidate `d = 1`, `L = 4`, `b = 2` is NOT a witness and is recorded as a control**:
there the block sum of `F` over `{0, 1}` is `(x_3 + x_1) + (x_0 + x_2)`, the total sum, which the two
block sums determine, so that block variable closes. **Prediction: positive (non-closure), full
strength.**

**Reported status for H3: HO.** Non-closure of one exact coarse observable is not an impossibility
of a statistical closure at some other scale or in some other variable, and no local-equilibrium
or mixing statement is made in either direction. **No relation `τ_B ≪ τ_S` is preregistered**, no
timescale is asserted, and the memory diagnostic is exactly what its statement says: this block
variable needs more than its own two-time state to predict its next value.

### `H4a` — the scaling skeleton

Not a theorem. The execution records, in the result note, the list of choices a continuum map for
this substratum must fix before any PDE statement is meaningful — lattice spacing as a function of
`L`, time step, field normalization (including how `ZMod q` values are lifted and rescaled), carrier
growth, and the topology in which convergence would be claimed — and records that **none is fixed
by the manuscripts or by A1–A6**. **Status: HO**, with the skeleton as the deliverable. No limit is
taken and no PDE is written.

### `H-C` separation, frozen for the later round

Two evidence tracks are kept apart from now on: a **formal Chapman–Enskog expansion** (an
uncontrolled asymptotic derivation, which can be recorded as prose analysis or a probe) and a
**rigorous hydrodynamic-limit theorem** (convergence in a stated topology). Round H-C must say which
it delivers for each of H5, H6, H7. The rigorous-limit literature is consumed as **calibration for
H5–H7 only** — what a proof has to contain — and never as evidence that the OI representative
satisfies its hypotheses. This paragraph binds H-C; it is not a target of H-A.

## The preregistered predictions, and their strengths

| target | prediction | strength | status reported | what would falsify it |
| --- | --- | --- | --- | --- |
| `H0-a`, `H0-b` | positive | full | HI for advection, conditional on `ZMod q`-linear coarse variables; HO otherwise | nothing plausible; composition of additive maps |
| `H1-a`, `H1-b` | positive | full | — | an error in the torus sum identity `Σ_i F(x)(i) = 2dα S` |
| `H1-c` | positive: conserved iff `q ∣ 4` | full | HI for the total-sum candidate under the `q`-gauge principle; HO for other candidates | a `ZMod` arithmetic slip; would change the set, not the shape of the finding |
| `H2a` spanning | positive | high | — | — |
| `H2a` dimension count | positive: `2` vs `1` | **medium at kernel level** | — | the averaging argument exceeding the round; frozen level-3 fallback |
| `H2b` | positive: the axis stencil is not rotation-isotropic at fourth order | full | exact anisotropy proved; conditional HI if H5 consumes this tensor; otherwise HO | — |
| `H3a` | positive: non-closure witness at `d = 1`, `L = 6`, `b = 3` | full | HO for H3 | an error in the witness arithmetic recorded above — then a larger witness is sought, and if none is found the diagnostic is UNDECIDED |
| `H4a` | skeleton recorded | — | HO | — |

**UNDECIDED remains a permitted label for every target**, reported with the obstruction.

**The programme-level reading the round is allowed to give, if all of the above land:** the present
wave representative is pushed toward **HI for a direct Navier–Stokes limit** by the linearity gate
on `ZMod q`-linear coarse variables, together with the `q`-dependence of the only total-sum
conservation law, and — **conditionally on H5's closure consuming the stencil's fourth moment** — by
the fourth-order anisotropy of the axis stencil; while the broader construction programme (H-B:
other OI-compatible reversible local substrata) is **entirely alive** and is where the next round
belongs. **This reading is conditional on every
qualifier above**, and the execution may not shorten it.

## What none of these outcomes licenses

- **Nothing here says OI cannot support fluid hydrodynamics.** The findings are about one
  representative rule, one stencil, one class of coarse variables, and one candidate conserved
  field. H-B's construction question is untouched and unprejudiced.
- **Nothing here is a continuum statement.** No limit is taken, no PDE is asserted or denied, and
  the continuum-breakdown branch (S1–S5) stays closed until H4–H7 exist, per the programme's
  control 5.
- **Nothing here changes A1–A6 or their status.** A6 remains a GAP on its own branch; A5 is consumed
  as proved.
- **Nothing here bears on the OI → QM chain**, on Track B's `P0`, on Bell, or on gravity — control 1.
- **The `q`-gauge principle is consumed as the manuscript states it, not tested.** If the principle
  were weakened elsewhere, `H1`'s status claim would need re-reading; `H1-a`–`H1-c` themselves would
  not change.
- **No manuscript is edited by this round.** Publication-facing claims wait, per the programme's
  control 10.

## Immutable inputs

Cited and consumed **unmodified**: `waveF`, `waveRule`, `waveSubstratum`, `waveSubstratum_A1`–`A5`,
`dir`, `nbrs`; `leap`, `leapEquiv`, `curOf`; `Rule`; `OhInvariant`, `ohInvariant_iff`,
`quadratic_isotropic`, `quartic_ohInvariant`, `quartic_not_isotropic`, `IsSign`; [SM §2.7],
[SM §4.1] Corollary 1a and "The two roles of the dynamics"; [Substratum] Theorem 24 (ii).

## The chronology control — act 10's STRENGTHENED mechanism, carried forward by name

1. **This preregistration blob is merged into `main` before any execution-specific H-A object
   enters the repository tree** — any Lean definition or proof about total sums, block sums, coarse
   linearity, stencil moments or rank-4 invariants, any probe, any result artifact. **The single
   permitted exception is the analysis recorded inside this control-plane blob itself**, merged
   *as* the freeze, including the `H1` arithmetic and the `H2b` moment.
2. **The execution PR's base must be exactly the merge commit of this control-plane PR.**
3. **The execution guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails
   closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B` this control plane's merge commit and
   `H` the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B`
   itself a descendant of `B`**, fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for
   `B`, for `H`, and for every enumerated commit alike.

**The claim is scoped to the repository record.**

## Definition budget

The execution introduces **at most seven** top-level definitions, and these are the seven:

1. **`totalSum`** — `S(x) = Σ_i x(i)`, as a `ZMod q`-linear functional. *Needed.*
2. **`blockSum`** — the block-partition coarse map `B` of `H3a`. *Needed.*
3. **`CoarseCloses`** — the closure predicate of `H0-b`/`H3a` on a coarse map and a coarse rule.
   *Needed.*
4. **`axisMoment4`** — the fourth moment tensor of the axis stencil, `H2b`. *Needed.*
5. **`SymInvariantQuartic`** or an equivalent predicate for fully symmetric `O_h`-invariant rank-4
   data, if `H2a` is attempted at kernel level. *Conditional.*
6. **`IsotropicQuartic`** — rotation invariance of a quartic form, if `H2a`'s "1" side is stated
   rather than consumed from `quartic_not_isotropic`. *Conditional.*
7. **A `ΔS` abbreviation**, if `H1` cannot be stated readably without one. *Conditional.*

**An eighth definition requires its own append-only amendment.** **No witness configuration, block
partition instance, or trajectory is a top-level definition** — each is a bound variable pinned by
an equation in the statement that needs it. `CubicIsotropy`'s and `SubstratumInterfaceAudit`'s
definitions are **reused, not redefined**.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide` — for `H0`,
`H1`, `H2b`, `H3a`, and for `H2a` with the single preregistered exception of its dimension count
under the frozen fallback. `H4a` is a recorded specification, evidence type "prose/source audit"
(programme control 9), and is labelled as such.

## Named hazards

1. **Reading `H1-c` as a universal no-go.** It is a statement about one candidate field under one
   rule. "No hydrodynamic variable can be conserved" is forbidden in terms.
2. **Rescuing the field by choosing `q`.** Fixing `q = 2` or `q = 4` and reporting a conserved
   momentum is exactly the move the `q`-gauge principle forbids; the round names it and does not
   make it.
3. **Freezing "wrap is the only nonlinearity".** It is *a* nonlinearity of a faithful finite
   realization; nonlinear and real-valued coarse-grainings are HO, not excluded.
4. **Sliding from HI-conditional to HI.** `H0`'s status carries its coarse-variable class in the
   statement; dropping the class over-reads it.
5. **Reading `H2b` against Corollary 1a.** Quadratic isotropy holds and is consumed; quartic
   anisotropy is what Navier–Stokes trips on. The two orders are different statements.
   **And reading `H2b` as HI outright**: the bare stencil moment is not yet shown to be the tensor
   H5's closure consumes; the status is conditional until that bridge lands.
6. **Counting the wrong tensor space.** `2` versus `1` is the fully symmetric count; general rank-4
   invariant counts are other numbers and belong to other physics.
7. **Reading `H3a`'s non-closure as absence of local equilibrium.** It is a diagnostic about one
   exact coarse variable; the statistical question is HO.
8. **Preregistering a timescale separation.** None is; `τ_B ≪ τ_S` does not appear as a hypothesis
   or a finding.
9. **Attaching the rigorous-limit calibration to H4.** It calibrates H5–H7; H4 is a map
   specification.
10. **Importing OI → QM results or Track B labels** as evidence here, or exporting these findings
    there — control 1.
11. **Speaking about singularities.** S1–S5 remain closed until a continuum map exists.
12. **Using the word that the repository's style rule bans for constructions.** Elementary,
    smallest, least.

## Non-doings

The round does not: construct a different substratum or stencil (H-B); take any continuum limit or
assert any PDE (H-C); test or weaken the `q`-gauge principle; edit A1–A6 or their kernel status;
edit `PROGRAMME.md`'s status line in this PR; touch any manuscript; say anything about Track B,
Track I, Bell, gravity or singularities.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.**
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the Lean
  module, the result note, the probe guard (pinning this blob and certifying clause 5's ancestry),
  the `PROGRAMME.md` §8 refresh and `ROADMAP` propagation, and the census entry. **No manuscript
  changes.**
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. **`H0`** — the linearity gate, with the coarse-variable class stated in the status and the HO
   remainder named;
2. **`H1`** — the classification `H1-a`/`H1-b`, the manuscript instance `H1-c` with the exact set of
   `q`, and the `q`-gauge test in this file's bounded words: the candidate field fails `q`-gauge
   invariance; no universal no-go;
3. **`H2a`/`H2b`** — the fully symmetric counts at the strength reached, with the fallback label if
   used; the axis-stencil moment as a proved anisotropy; the conditional status in this file's
   words — HI only if H5 consumes this tensor, otherwise HO — and nothing about other stencils;
4. **`H3a`** — the witness with coordinates; HO for H3; no timescale;
5. **`H4a`** — the skeleton, as a list of unfixed choices;
6. the programme-level reading, verbatim from this file and conditional on every qualifier;
7. what the outcomes do **not** license, in this file's wording, with H-B named as alive;
8. the definition count against the seven-slot budget, conditional slots marked fired or unused;
9. the chronology certification, and the axiom table with one line per named result.
