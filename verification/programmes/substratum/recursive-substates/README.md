# SUBSTATE-2 — recursive inverse-limit sub-states, exact controls

**Status: active research-only hypothesis and preregistration, issue #1010.** Based on \`main\` at \`f6989a27815c4d715223eebf2859422c1231e3f8\`; **not** a statement that physical OI contains fractal internal states. Separate from SUBSTATE-1 (#1007 / draft PR #1009) and the Yang–Mills/QCD bridge (#1003). No manuscripts, physical premises, Lean certificates or theorem classifications are changed by this note.

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

The real OI cubic wave carrier and observer-access constraints are not modified here. SUBSTATE-1 rejected one pure site-gradient link candidate and showed a separately invented gauge-pointer toy can be reversible and covariant without supplying quantum mechanics. SUBSTATE-2 tests a different *structure hypothesis*. It does not import those unreviewed constructions as axioms or copy their physics claims.

**Verdicts to record:** A is a negative control, B1 a positive finite-depth memory control, B2 a positive all-depth-over-time/no-common-return control, C a gauge-kinematic but action/operational negative control. All require independent review before moving from research to manuscripts. No merge or special CI launch is authorized.
