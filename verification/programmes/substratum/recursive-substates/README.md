# SUBSTATE-2 — recursive inverse-limit sub-states, exact controls

**Status: active research-only hypothesis and preregistration, issue #1010.** Based on `main` at `f6989a27815c4d715223eebf2859422c1231e3f8`; **not** a statement that physical OI contains fractal internal states. Separate from SUBSTATE-1 (#1007 / draft PR #1009) and the Yang–Mills/QCD bridge (#1003). No manuscripts, physical premises, Lean certificates or theorem classifications are changed by this note.

## Hypothesis

A finitely observed state might represent a *nested family of finer internal distinctions*, encoded by a compatible inverse limit
\[
K=\varprojlim(K_n,p_{n+1,n}), \qquad
p_{n+1,n}:K_{n+1}\longrightarrow K_n.
\]
The finite stage \(K_n\) represents resolution \(n\); the physical significance of any mathematical level must still be justified. "Fractal" here means *recursive refinement / optional self-similar topology*, not an assertion that ordinary three-dimensional space has noninteger dimension.

Distinguish the inverse limit of finite discrete groups (profinite, compact and totally disconnected) from the inverse limit of *circles* used by a solenoid (a different connected compact group). **No continuous surjective group homomorphism from a profinite group onto connected \(U(1)\) or \(SU(2)\)** follows from this setup. A finite-group tower does not silently supply a continuous Yang–Mills gauge group.

## Frozen competing model choices

These are *mathematically specific controls*, not candidates being fitted after examining an OI or QM result.

| Model | Hidden ontology / update | Visible access | Predicted result and limit |
| --- | --- | --- | --- |
| A: congruence-compatible odometer | \(\mathbb Z_2=\varprojlim\mathbb Z/2^n\), \(T(x)=x+1\), Haar | lowest bit | Deterministic flip; \(\Gamma_2=I\), \(\Gamma_1\) a permutation, so **no** recurrence-based P-indivisibility. Deeper digits cannot affect this readout |
| B1: controlled-depth feedback | Infinite fair binary sequence \((b_0,b_1,\ldots)\); one fixed \(m\ge1\), \(T_m:b_0\mapsto b_0\oplus b_m\), others fixed | \(b_0\) | Reversible involution, \(\Gamma_1\) uniform, \(\Gamma_2=I\), rooted P-indivisible; the full three-time law has one bit of \(I(X_0;X_2\mid X_1)\). **Only the specified finite level m is accessed** |
| B2: scale conveyor negative control | Bernoulli bi-infinite stream \(\{0,1\}^{\mathbb Z}\), invertible coordinate shift | current coordinate 0 | Future observations read successively deeper coordinates and are iid; \(\Gamma_t\) uniform for \(t>0\), **no positive common visible identity return**. Finite cyclic approximations return at their cycle length, which diverges with size |
| C: recursive gauge-link tower | Four oriented links in \((\mathbb Z/2^n)^4\), compatible reductions and local vertex gauge addition; translation \(u_{01}\mapsto u_{01}+1\) | mod-2 plaquette holonomy | Non-flat gauge-invariant closed loop exists; link translation preserves product Haar and is covariant. Lowest-bit readout is a permutation flip with period 2. Neither \(S_W\) nor \(S_W^2\) is selected |

All stated finite probabilities have to be computed from **one pinned initial distribution**. A classical Markov visible law is not evidence of quantum control. A memory-bearing visible law is not evidence of coherent interference. Gauge covariance is not a Yang–Mills action.

## Theorem versus hypothesis: finite-depth obstruction

For a compact inverse limit of finite discrete sets, a **continuous map to a finite discrete alphabet factors through some finite stage**. This is a standard compactness/cylinder argument; proving it in Lean is a *separate target*. Any continuous dynamics \(T\) makes each \(\pi\circ T^t\) a continuous finite-valued map, so each *fixed* time observation has some finite-depth bound \(n_t\).

If, additionally, a **single exact visible period** \(L>0\) holds pointwise (or with the appropriate separately specified almost-everywhere interpretation), finitely many observation functions \(\pi\circ T^0,\ldots,\pi\circ T^{L-1}\) suffice. Their finite-depth bounds have one finite maximum \(N\). Therefore every future visible word is insensitive to initial coordinates beyond \(N\). This is the tension: **unbounded initial-depth sensitivity at unbounded times and a uniform common exact visible period do not coexist under these continuity/factorization premises.**

Do not oversell: finite-horizon bounded-depth dependence is true even **without** periodicity. The additional periodicity is used to obtain **one bound uniform across all time**. "Every trajectory eventually returns close" or "returns a.e." does **not** imply the strong pointwise common period. For almost-everywhere assertions, prove the required null-set versions separately.

A minimal new Lean module may certify (i) finite-family maximum-depth aggregation given finite-stage factorization and (ii) a common bound under an *explicitly supplied* periodic observation law. It must **not** be called a Lean proof of compactness or of the OI physical model unless those bridges are proved too.

## Required hard-to-vary checks and guards

1. **Exact per-model controls:** invertibility, tower projection consistency, common prior, complete finite joint trajectories, and whether visible recurrence is pointwise, a.e., or merely asymptotic.
2. **Depth sensitivity control:** a fixed passive finite factor may never read arbitrarily deep initial digits under common exact visible period. B1 proves a depth-m witness per choice of m; B2 deliberately drops common return in the infinite model. Never confuse a *family* of couplings with a *single* fixed physical law.
3. **OI/QM:** preserve finite-horizon \(S\Leftrightarrow D\Leftrightarrow Q_{\rm fb}\) as an independently established representation theorem. Neither recurrence/P-indivisibility nor exact inverse-limit structure produces native selectable noncommuting quantum instruments, purification, independent spectators, composite consistency, C4, or the F2 sourcing gate.
4. **OI/YM:** C is a **profinite abelian** gauge model; it is not connected U(1), SU(2), or SU(3) and does not imply H-link/H-cust or A6 for the current OI substratum. Test nonflat plaquette holonomy and both \(\sum w\) and \(\sum w^2\), preserving #1003's gauge-covariant action non-uniqueness. No Wilson Gibbs weight arises from Haar-preserving translation alone.
5. **Geometry/entropy:** the ultrametric/Cantor-like internal structure does **not** show fractal physical space. A finite visible alphabet has finite stagewise entropy, but full Haar entropy of infinitely many hidden digits diverges; any physical boundary entropy density or finite \(\sigma\) needs its own sourced accounting.
6. **Possible independent payoff:** discrete-scale invariance might produce log-periodic correlations **if** a specific self-similar dynamics selects a nonzero amplitude, scale and exponent. Such a signature is **not** a consequence of the mere inverse limit. Keep this as an explicit falsifiable future target, not a prediction or fit.

## Native sourcing and scope

The real OI cubic wave carrier and observer-access constraints are not modified here. SUBSTATE-1 rejected one pure site-gradient link candidate and showed a separately invented gauge-pointer toy can be reversible and covariant without supplying quantum mechanics. SUBSTATE-2 tests a different *structure hypothesis*. SUBSTATE-1 Track A has been independently accepted; SUBSTATE-2 still does not import those constructions as axioms or copy their physics claims (see also #1007 comment 6529586144 for a parallel consistency note).

**Verdicts to record:** A is a negative control, B1 a positive finite-depth memory control, B2 a positive all-depth-over-time/no-common-return control, C a gauge-kinematic but action/operational negative control. All require independent review before moving from research to manuscripts. No merge or special CI launch is authorized.


## Executed exact controls and replay

The preregistered finite controls were executed locally on the **same
source bytes** as committed in `recursive_controls.py`, and both
ordinary Python and `-O` runs reproduced the committed
`RESULTS.json` byte-for-byte. The separate `replay.py` enforces
these checks, validates the structured result labels, checks that
no quantum/Yang–Mills/physical-fractal claim is being asserted, and
fails if stderr, exit status, expected bytes or the pinned
source/result SHA-256 differ.

From the repository root:

    python3 -I -B verification/programmes/substratum/recursive-substates/replay.py

Source SHA-256: `6beb25044fc6966a954adc186d1a136f42fedd78c938c2683983316b886af666`.
Results SHA-256: `8b949aa7cbd688f7c41fa079f761424afea98700e387db42c2b15320174e2b64`.

**Finite checks completed:**
- A: all quotient states at depths 1–9.
- B1: 256 8-bit states per feedback depth in {1,2,3,5,7}, with exact three-time laws and minimal-prefix witness.
- B2: complete cyclic-shift state spaces for cycle lengths 3–9 and uniform finite words before return.
- C: exact complete four-link configurations at levels 1–4, including 65,536 states at level 4, with four local gauge-generator checks, inverse, reduction and uniform holonomy; separate rational quarter-turn Wilson-vs-squared controls.

**Formal status:** `OIBridge.RecursiveFiniteFactor` is an explicitly
*conditional* Lean theorem candidate, imported into the pinned
Mathlib bridge and classified `kernel-only` in the manuscript
census. It proves finite-horizon/max-depth assembly and periodic
extension given finite-stage hypotheses, plus a reversible
hidden-controlled Boolean flip. The module builds and its axiom
report passes in CI. The separate compactness
lemma that continuous finite readouts factor through a finite
stage is a paper-level argument only (see `ANALYSIS.md`).

These controls neither select a unique physical recursive coupling
nor derive quantum instruments, a continuous nonabelian gauge
group, Wilson/Yang–Mills dynamics, a physical boundary entropy law,
or a log-periodic prediction. Independent mathematical and
scientific review are required.


## FIXED-SCALE-1: one continuous reversible rule across all depths

After the predeclared A/B/C controls, the active **single-law**
candidate is specified in
[FIXED-SCALE-1 preregistration](fixed-scale-skew/PREREGISTRATION.md).
[Proof and finite result](fixed-scale-skew/REPORT.md) and
[exact source](fixed-scale-skew/fixed_scale_probe.py) are separate.

The entire infinite hidden state is \((a,r,c)\), with a current
visible bit \(a\), one persistent hidden bit \(r\), and a
bi-infinite fair bit hierarchy \(c_i\). One fixed update
\[
T(a,r,c)=(a\oplus r\oplus c_0,\ r,\ Sc)
\]
works at **every** depth, rather than choosing one coupling
index m for each target. The observer sees \((a,c_0)\).

**Mathematical prediction:** For each positive time, the
four-by-four rooted two-time matrix has every entry \(1/4\)
(and is P-divisible), yet the full three-time visible law
has **one bit** of conditional predictive memory. The
three-record identity
\(a_{t-1}\oplus a_{t+1}=c_{t-1}\oplus c_t\) holds with
probability one. The infinite shift has no exact shared
positive-time visible return. The finite cyclic
approximations instead return after no more than \(2n\)
updates, a **boundary effect that disappears in the
infinite model**.

A **matched two-time negative control** now uses an independent
reversible four-symbol iid shift: it has exactly the same
four-by-four rooted matrices as this model for all positive
times, but all 64 three-time words occur at probability
\(1/64\), unlike the skew model's 32 words at \(1/32\).
Their exact three-record total-variation distance is
**1/2**, with conditional memory 0 versus 1 bit.
The [matched-control program](fixed-scale-skew/matched_control.py)
checked all four-symbol cyclic tapes of lengths 3–7
(up to 16,384 states) and retained exact
[MATCHED.json](fixed-scale-skew/MATCHED.json).
The [joint replay](fixed-scale-skew/replay.py) verifies both
results against pinned hashes, normally and optimized.
This follow-up was not included in the original
FIXED-SCALE-1 preregistration and remains classical.

Exact finite controls exhaust all states for tape lengths
\(n=3,\ldots,9\) (up to **2,048** full states), including
inverse, complete three-time words, rooted matrices before
wraparound, hidden-bit ablation, growing-depth witnesses
and finite-size return. This experiment was run locally
both normally and with optimized Python on byte-identical
source, with result matching the committed
[RESULTS.json](fixed-scale-skew/RESULTS.json). The
[fixed-law replay](fixed-scale-skew/replay.py) pins both
source and results by SHA-256 and rejects missing checks
or output mismatches. This is **written infinite proof
plus finite executable controls**, not Lean certification
of the infinite probability law.

**Status:** one parameter-free (after specifying the
model) **classical** construction with hidden memory and
indefinitely deeper state access. It does not source an
OI-native gate, a nonclassical operational repertoire, a
physical fractal dimension, Yang–Mills link dynamics, a
Wilson action, or finite boundary entropy. Its fair
Bernoulli hierarchy is an explicit physical *candidate
prior*, not one OI has selected. The next gate is native
sourcing and an independent falsifiable quantum/YM
observable. No manuscript or main-branch upgrade is allowed.


## NATIVE-PADIC-1: unchanged cubic wave cannot access deeper low digits

[Source test and exact proof](native-padic-bridge/REPORT.md) compares
the α=1 reference rule (the 3-D integer-coefficient two-slice
wave rule of `wave_eqn.c`; SM §4.1 leaves the substratum
coefficient open) to its **hypothetical** compatible \(\mathbb Z/2^n\) alphabet
lifts. [Preregistration](native-padic-bridge/PREREGISTRATION.md)
was committed before computation.

For every \(m<n\), coordinatewise reduction modulo \(2^m\)
**commutes with the reference step and inverse**. Hence
arbitrarily fine digits never influence the lower-m passive
readout through this same equation. The congruence argument holds for any
integer \(\alpha\) and any compatible 2-adic \(\alpha\)
(including \(\alpha=3^{-1}\) in \(\mathbb Z/2^n\)); the
Lean module covers coefficient 1 only. The resulting infinite
\(\mathbb Z_2\)-valued lift has exact **visible**
common returns for each fixed low-m factor (a finite
permutation), even though the whole infinite carrier
need not have a common return at all scales.

The [exact regression](native-padic-bridge/native_padic_probe.py)
covers the 27-site L=3 cubic torus, q=2,4,8,16,32,64,
twelve deterministic initial pairs per q, 16 forward
and inverse ticks for every relevant quotient, and
higher-digit perturbations at every tested depth:
**9,344 exact arithmetic controls**. The
[structured result](native-padic-bridge/RESULTS.json)
and [pinned replay](native-padic-bridge/replay.py)
are retained. A deliberately **non-native but reversible**
bit1-to-low-bit kick breaks the reduction property,
showing the test does not reject all deeper-to-visible
couplings by construction.

A new research Lean candidate,
`OIBridge.NativePadicReduction`, formalizes
commutation of a finite neighbor-sum stencil, the
two-slice step and its intended inverse (the inverse
property is not proved there) with an arbitrary additive
alphabet homomorphism. It is imported into
the Mathlib bridge and entered in the maintained
census as `kernel-only`; it builds and its axiom report
passes in CI. The separately written topological \(\mathbb Z_2\) inverse-limit
identification is not formalized. The result does not cover nonlinear
observer-access mechanisms, the native-Y triple
interaction, genuine gauge fields or quantum
operational structure.

**Disposition:** narrow passive low-digit NO-BACKFLOW,
pending independent review. This rules out a simple
fractal-alphabet shortcut without prohibiting a
sourced cross-scale physical mechanism. Do not
promote it to any OI manuscript claim.
