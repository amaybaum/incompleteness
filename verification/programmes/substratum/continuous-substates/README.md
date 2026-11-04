# SUBSTATE-1: internal sub-states and visible recurrence

**Status: research-only, work in progress.** Tracking issue #1007. Base: `main` at
`f6989a27815c4d715223eebf2859422c1231e3f8`. This note changes no manuscript claim, status
or premise.

## Question

Main Lemma 1 proves that the visible sector is finite. Finiteness of the whole substratum
is a posit (Main §1.2 Remark, §4.5). This programme asks what happens if each finite
site state carries infinitely many internal sub-states below the resolution ε.

The first question concerns the recurrence route to P-indivisibility (Main §2.3).
It uses `Γ_L = I`: at one common time the visible partition returns for almost
all hidden states under the chosen prior. A finite-state bijection guarantees
this. The separate proof in [observable-recurrence.md](observable-recurrence.md)
gives an exact sufficient criterion on an arbitrary measure-preserving carrier
and treats the free wave map for every ring size `L ≥ 3`.

## Setting of the probe

- **Dynamics:** the 1-D lattice wave map on a ring of `L` sites,
  `u_{t+1}(n) = u_t(n+1) + u_t(n−1) − u_{t−1}(n)`. Its integer matrix `F` reduces
  mod `q` to the substratum wave map (SM Theorem A.1).
- **Two sub-state continua:**
  - **real-type:** each site value in `R/Z`, with `F` acting on the torus `(R/Z)^{2L}`;
  - **`p`-adic-type:** each site value in `Z_p`, whose quotients `Z/p^k` are finite alphabets.
- **Hidden prior:** Haar measure.
- **Visible observable:** an integer linear form `v`, read through a two-cell partition.

`wave_torus_probe.py` uses exact integer and rational arithmetic only and runs in
about two seconds. `expected-result.json` is its byte-exact output; the run is
deterministic. Verdict text is generated from the measurements and printed only when
every control passes.

`observable_recurrence_check.py` provides an additional exact-integer,
finite-range (`L = 3…20`) regression and even-`L` countercontrol for the
all-`L` proof note. Run with `python3 observable_recurrence_check.py`
from this directory. This finite regression is **not** evidence by itself
of a universal theorem. The controls are:

1. `F mod q` has order `qL` for prime `q ∤ L` (SM Theorem A.1).
2. `M = F^L − I` is nonzero with `M² = 0` over `Z` (SM Theorem A.2, over `Z`).
3. Exact counts on the finite subgroup `(Z/8)^6` (`L = 3`). These check facts (H) and
   (R) below independently of their proofs.

Two facts are used:

- **(H)** If `v` and `w` are integer forms of rank 2, then `(v·x, w·x) mod 1` is
  Haar-distributed on `T²` when `x` is Haar-distributed on the torus. So
  `Γ_t = [[½, ½], [½, ½]]` whenever `v F^t` is not proportional to `v`.
- **(R)** If `vM = 0`, then `v F^{mL} = v`, so the visible cell returns exactly at
  every `t = mL`.

## Findings (`L = 3, …, 10`)

1. **Pointwise recurrence does not give `Γ_L = I`.**
   - With real-type sub-states, the single-site observable `u(0)` has `v F^t` never
     proportional to `v` for any `t ≥ 1`. So `Γ_t` is uniform for every `t ≥ 1`.
   - This family is P-divisible: `Γ_t = Γ_s Π` with `Π` uniform.
   - Every trajectory of this *specific* unipotent torus map returns arbitrarily
     close to its start at point-dependent times, by a separate compact-group
     argument (see the proof note). Poincaré recurrence on a finite-measure
     system alone gives recurrence only almost everywhere; neither result
     supplies a common exact return time. The visible space has two cells.
2. **Observables blind to the non-recurring modes recur exactly.**
   - The non-recurring part of `F` is its unipotent part (`M ≠ 0`, `M² = 0`). Its image
     comes from the parabolic modes: the uniform shift of every site, and for even `L`
     the alternating mode.
   - The difference `u(0) − u(1)` (odd `L`) and `u(0) − u(2)` (every `L`) satisfy
     `vM = 0`. They return exactly at every `t = mL`, with `Γ_1` uniform.
   - By the stochastic-inverse lemma (Main §2.3), these rooted families are
     P-indivisible on `{0, …, L}`. The Fourier-mode proof extends this
     *free-map* statement to all `L ≥ 3`, rather than only the sampled sizes.
   - The uniform shift is the amplitude-shift symmetry of SM §2.7.
   - Countercontrol: `u(0) − u(1)` at even `L` has `vM ≠ 0` and does not return.
3. **The finite alphabet as a grid, and the direction of carries.** `(Z/N)^{2L}` is a
   finite `F`-invariant subgroup of the torus, and its uniform measure is the finite
   substratum with alphabet `Z/NZ`.
   - **Most significant digit:** for `L = 3` the *full finite matrix*
     has order `ord(F mod N) = 3N` (6, 12, 24, 48 for `N = 2, 4, 8, 16`).
     This supplies a common return **by** that time and shows the carrier's
     order grows. The probe has not established the *least* return time
     for the single-site two-cell observable for every listed `N`.
   - **Least significant digit:** the same observable returns exactly at
     `ord(F mod 2) = 6` on `(Z/8)^6`, with `Γ_1` uniform.
   - The reason is the direction of carries:
     - In `R/Z` the coarse digit is the most significant, and carries from finer digits
       reach it. The sub-states influence the visible cell.
     - In `Z_p` the coarse digit is the least significant, and carries only move upward.
       Under congruence-compatible `Z_p`-linear dynamics, higher digits cannot influence
       a readout depending only on the lowest digit. For this readout
       `Γ_{ord(F mod p)} = I` holds for every sub-state.

## Reading

A rigorous **sufficient** replacement for total finiteness in this one
recurrence step is `π ∘ T^L = π` almost everywhere, where `π` is the finite
visible partition. Equivalently, `Γ_L = I`. The proof note shows that
any non-permutation `Γ_s`, `0 < s < L`, then forces rooted-family
P-indivisibility. This is not claimed necessary for all OI memory results.
In the free wave example, cancellation of non-returning parabolic modes
is one mechanism satisfying the condition. Total finiteness is another.

The two continua sit at opposite ends of this condition:

- **`p`-adic sub-states** preserve finite recurrence for readouts factoring
  through `Z_p → Z/p^kZ` and the tested congruence-compatible linear map.
  Higher digits do not affect those readouts under that class of maps.
  This is **not** a general no-go for p-adic observables or interactions,
  nor does `Z_p` itself supply the requested connected Lie gauge group
  or resolve full QM equivalence.
- **Real-type sub-states** influence the single-site readout in the free map.
  The tested difference observables nevertheless return exactly because they
  annihilate its parabolic modes. Whether an **interacting** map retains any
  such observable is open; no interacting map is tested here.

Influence and synchronized visible return need to be tested together, rather
than inferred from the cardinality of the internal state space.

## Scope and limits

- Exact computational probe: free linear dynamics in `d = 1` for `L = 3, …, 10`.
  A separate paper-level Fourier proof in [observable-recurrence.md](observable-recurrence.md)
  covers the stated difference readouts for every `L ≥ 3`; it is **not Lean-checked**
  or independently reviewed.
- **The `d = 3` coefficient has two levels.** SM §4.1 treats `α=1/3`
  as the normalized *observer-level* wave-operator coefficient; it is
  not established as the microscopic update coefficient. Division by
  three is not a well-defined circle-group endomorphism on `R/Z`,
  but the actual observer-level operator may act on real vectors.
  A compact 3-solenoid supplies a mathematical carrier supporting
  multiplication by `1/3`, and `Z_p` does so for `p≠3`; neither
  construction derives the missing map `φ → L_obs → Δ_g`.
  See [equivalence-and-d3-scope.md](equivalence-and-d3-scope.md).
- **What is established:** P-indivisibility of the rooted family `Γ_t` only. Multi-time
  memory and the readback route are not examined.
- **The prior:** the hidden prior is Haar measure; other invariant measures are not
  examined.

## Next steps

1. Obtain independent mathematical review of the all-`L` Fourier proof and
   observable-factor criterion; keep this as an unverified paper-level proof.
2. Separate the actual microscopic `d=3` bijection from the observer-level
   `α=1/3` harmonic operator; pin a carrier, observation and invariant
   prior for each model **before** comparing their visible statistics.
3. Test the *actual* gauge-coupled update, not a surrogate, for any exact or
   near-total common-time return.
4. Complete the literature controls in #1007 and test whether an induced
   measure selects Wilson/Yang–Mills over covariant countercontrols.

## Initial literature control

The ordinary Poincaré recurrence theorem guarantees almost-everywhere return,
not a single common period and not every point; see Hochman's
[ergodic-theory notes](https://math.huji.ac.il/~mhochman/courses/ergodic-theory-2017/notes.pdf), §2.2.
Wilson lattice gauge theory uses compact **link** variables, invariant measure,
and a specified plaquette action; these are separate choices, as in these
[QCD foundations lectures](https://www.phenix.bnl.gov/WWW/publish/elke/EIC/BOOKs/Lectures-on-QCD.Foundations.pdf).
A full literature and novelty audit is still pending.

## Three-solenoid countercontrol (exactly Markov)

[solenoid-countercontrol.md](solenoid-countercontrol.md) proves that the
reversible automorphism `x → 3x` on the compact 3-solenoid, under Haar,
with the first circle coordinate read as a binary half-interval, has a
**stationary Markov** visible law with one-step matrix
`[[2/3,1/3],[1/3,2/3]]`. Its rooted law obeys `Γ_t=P^t`, is
P-divisible and has no positive-time common visible identity return.
[solenoid_markov_probe.py](solenoid_markov_probe.py) independently
enumerates the exact finite-word cylinders through horizon 7.
The countercontrol refutes the naive assumption that continuous
sub-states and division by 3 automatically produce useful recurrence,
readback or nonclassical control. It is **not** the actual OI
gauge-coupled 3-D wave map and does not rule out other partitions.

## Formal and operational dependency status

The existing Lean module `OIBridge.RecurrenceHorizon` already proves the
**carrier-independent** rooted identity-return/overlap obstruction;
`OIBridge.EquivalenceChain` already proves stochastic-inverse rigidity.
At independently reviewed head `a02e197d`, both research modules
`OIBridge.ObservableFactorRecurrence` and `OIBridge.ObservableMeasureReturn`
compiled in Lean/Mathlib; the whole automatic CI run `41094894776`
passed (25 jobs passed, 1 skipped). They establish the carrier-independent
change-event identity, stochastic inverse obstruction, and a conditional
**ENNReal-valued** measured ratio identity `measuredGamma = I ↔
μ(visible-change event) = 0` for positive finite initial-cell masses.
**Still missing in Lean:** measurability assumptions for the observation
and update, an ℝ-valued row-stochastic rooted physical transition law,
and a composition of the measured criterion with the P-indivisibility
obstruction. The all-L free-wave Fourier argument remains a paper proof,
not a Lean theorem; no gauge-coupled law or full QM is derived.

[Equivalence and 3-D scope audit](equivalence-and-d3-scope.md) explains why
removing fixed finite-carrier restrictions does **not** by itself discharge
the five independently characterized operational quantum conditions.

## Observation-context experimental controls (double-slit analogue)

[Observation-context protocol](observation-context-protocol.md) records a
**preregistered three-way comparison**: (C0) a restricted fixed-path
classical stochastic baseline, (C1) a **classical coherent-wave positive
control**, and (C2) an as-yet-unbuilt native OI dynamical construction.
The [exact benchmark](observation_context_probe.py) verifies the
subnormalized two-slit, one-slit, which-way and eraser-style *reference*
probabilities with rational arithmetic. It does **not** implement the
underlying OI dynamics, show that observations alone create coherence,
or prove uniquely quantum behavior: ordinary classical waves also
interfere. The controlled process must generate independently selectable,
noncommuting operations and demonstrate a composite/spectator test
without importing a quantum instrument menu. The source, losses and
full joint setting/marker records must remain comparable. A Markov
passive readout and a memory-bearing controlled readout may coexist, but
that is an open hypothesis, not a theorem.


## Yang–Mills/QCD bridge: action selection versus observational selection

[Yang–Mills sub-state bridge](yangmills-substate-bridge.md) relates this
research programme to draft [#1003](https://github.com/amaybaum/incompleteness/pull/1003).
A continuous internal carrier could support gauge **link** variables,
but the link identification, local gauge covariance, invariant measure,
and Wilson/Yang–Mills *action selection* are separate physical obligations.
A gauge redundancy is not an observer-controlled quantum measurement.

The self-contained [exact U(1) probe](yangmills_context_probe.py)
uses four independent Haar-distributed links on one closed plaquette.
Two nonnegative gauge-invariant heralding contexts have the **same**
overall acceptance rate 13/16, but different conditional loop means:
1/14 versus 2/13. The unconditional mean is zero in both cases.
This proves, **for that ambient countercontrol only**, that a difference
in selected Wilson-loop statistics is not enough to infer different
native gauge dynamics or an action. Full attempted/rejected records and
a physically sourced intervention are required. The probe does NOT
implement Yang–Mills, SU(3), an OI native link dynamics or a quantum
gate; it does not select #1003's Wilson action or its squared alternative.
The [bridge note](yangmills-substate-bridge.md) also records a
**restricted Haar-stationarity obstruction**: if the microscopic
state is exactly the full link configuration with product Haar prior
and the evolution preserves that measure, its one-time full-link law
cannot become a nonconstant Wilson Gibbs weight without an actual
change in prior, readout or physical coupling. This does not exclude
nontrivial time-correlations, constrained ensembles or genuinely
interacting alternatives.


The native observation-context sourcing gate remains **BLOCKED** for
the current retained interface: no paired same-preparation selectable
which-path/complementary interventions have been established. This is
not an OI-wide no-go. The next candidate must be derived from one
microscopic update and observer contract rather than post-hoc decoder
freedom. No manuscript or physics-status upgrade follows.

## Shared link and pointer source gate (bounded native/no-go pair)

The [native sourcing analysis](native-link-sourcing-gate.md) compares the
**actual** finite two-slice cubic OI wave update with an explicitly
**added** gauge/link-pointer model. The new research Lean module
`OIBridge.GradientLinkFlatness` attempts to certify the square-gradient
telescope and generic two-slice inverse, with its source imported into
the Mathlib bridge and categorized **kernel-only** in the maintained
Lean manuscript census. Its Lean build and release-gate checks passed on automatic exact-head run `41094894776`; the independent review still requires revisions. It separates a rigorous negative
result from a usable mathematical consistency control:

- **Native pure-gradient negative:** assigning links by site
  differences `U_xy=exp[2πi(f_y−f_x)/q]` makes every closed
  plaquette holonomy exactly 1 by telescoping, for **every**
  microstate and every time. Not every local site-dependent shift commutes
  with the cubic wave update: a delta-site shift fails (q=5, L=3,
  origin values 4 versus 1), while commuting shifts satisfy
  `ker(A−2I)`, including `g=h⊗h⊗h`, `h=(2,4,4)`. The
  [native-wave exact check](native_wave_gradient_check.py) provides
  positive inverse controls, nonconstant open links, evolved
  plaquette checks and the shift witness. This rejects only the
  **naive site-gradient link assignment**, not H-link or other
  physical carriers.
- **Reversible gauge-pointer toy:** an independently specified
  [U(1) link/pointer construction](shared-gauge-pointer-candidate.md)
  has two selectable reversible gauge-covariant read/kick updates,
  one physical pointer bit, genuine link back-action, and
  complete raw input/loop/pointer records. The
  [exact Z/8 control](gauge_pointer_toy_probe.py) tested 8192
  states and 32 controls, including the explicitly enumerated outgoing
  plaquette distributions; normal/optimized replay still needs fresh confirmation.
  Removing the kick makes its two classical control settings
  commute. With the kick they do not commute, **as classical
  permutations**; this is not quantum operational noncommutation,
  interference, or a YM action. The toy adds its own links and
  apparatus as **new premises** and must not be called native OI.

**Unified physical sourcing remains BLOCKED** on verifying SM §6.5's
conditional non-Abelian exponential link as a covariant dynamical link
with nontrivial loop holonomy, and a public reusable measurement interface.
The next proposed candidate must supply both from one actual OI
microscopic state/update and invariant prior, with the
independent Wilson/squared-action, contextual observation,
full attempted-record, decoupled, and composite-controls retained.
Neither result authorizes a manuscript claim change or merge.
