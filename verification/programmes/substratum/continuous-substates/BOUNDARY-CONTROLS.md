# SUBSTATE-1 E-lane: finite boundary observations with infinite hidden stream

**Research-only mathematical control, not a physical OI realization, GR derivation,
Lean theorem, or amendment to a manuscript.** Parent issue #1014; coordination
#1007. This file and its exact enumerator deliberately address only the
distinction between finite *instantaneous* observable alphabet and an
unbounded hidden carrier or cumulative observation record.

## Models and invariant states

Let \(X=(\mathbb Z/2\mathbb Z)^{\mathbb Z}\), the compact product group of
bi-infinite binary sequences, with fair-product (Haar) probability measure.
Let \(B=\mathbb Z/2\mathbb Z\) be the single accessible boundary bit with
independent fair prior; the observer reads \(\pi(x,b)=b\). There is **one**
visible mode, so its instantaneous Shannon entropy is at most one bit
(\(\sigma\le\ln2\) nats), even though \(X\) is uncountable.

Write \(\sigma_X x\) for the left shift
\((\sigma_Xx)_i=x_{i+1}\), an invertible measure-preserving group
automorphism. Compare three independently specified bijections on the
**same** microscopic space and initial measure:

* **D, decoupled:** \(T_D(x,b)=(\sigma_Xx,b)\).
* **R, stream readback:** \(T_R(x,b)=(\sigma_Xx,b\oplus x_0)\).
* **Q, fixed-hidden toggle:** \(T_Q(x,b)=(x,b\oplus x_0)\).

These are continuous invertible automorphisms of the compact product
group and preserve its Haar probability measure. The inverse of R is
\(T_R^{-1}(y,c)=(\sigma_X^{-1}y,c\oplus y_{-1})\);
D and Q have evident inverses.

## Exact results and scope

**D: genuinely decoupled hidden cardinality.** The visible bit never
changes; every length-\((n+1)\) record is either all zero or all one.
The complete visible law is unchanged if a further *independent,
dynamically decoupled* carrier is adjoined. This is a concrete instance
of an exact, interface-relative cardinality equivalence, not a claim
that all hidden cardinalities are physical gauge in every context.

**R: finite instantaneous entropy, unbounded cumulative readable history.**
Under \(T_R\), after \(t\) steps,
\(b_t=b_0\oplus x_0\oplus\cdots\oplus x_{t-1}\).
The map \((b_0,x_0,\ldots,x_{n-1})\mapsto
(b_0,b_1,\ldots,b_n)\) is invertible since
\(x_t=b_t\oplus b_{t+1}\). The \(n+1\) visible bits
are therefore **independent fair bits**. Every word has probability
\(2^{-(n+1)}\), and
\[
H(b_0,\ldots,b_n)=n+1\ \mathrm{bits},\qquad
H(b_t)=1\ \mathrm{bit}.
\]
In particular, the visible process is **exactly Markov/i.i.d.** even
though the hidden carrier is directly coupled to the boundary and
each new public record conveys a fresh hidden bit. Its rooted matrices
are \(\Gamma_t=\frac12\mathbf1_{2\times2}\) for every \(t>0\), so there is
no synchronized identity return and no P-indivisibility from that route.

**Q: the same finite visible resolution with exact visible return.**
Under \(T_Q\), \(b_0,b_0\oplus x_0,b_0,b_0\oplus x_0,\ldots\).
Thus \(\Gamma_1\) has every entry \(1/2\), whereas
\(\Gamma_2=I\). By stochastic-inverse rigidity the rooted family
is P-indivisible on \(\{0,1,2\}\). At time 2, distinct positive
past records with the same current bit have different next-step
conditional laws, so history readback is present. This demonstrates
**possibility**, not automatic recurrence or native OI physics.

**Crucial GR distinction.** These examples **do not refute** a finite
boundary-area entropy bound: the *instantaneous* interface B is always
a single bit. R only shows that a succession of observations can carry
arbitrarily many fresh bits when unlimited observation duration and
external record storage are permitted. A bound on cumulative
distinguishable histories requires an additional finite duration,
capacity, reset, or information-flow condition. Conversely, if the
physical claim is exclusively a simultaneous-boundary entropy bound,
the one-bit readout is consistent with it. A microscopic infinity
alone neither establishes nor violates the GR area law.

**Physical restriction.** The source of the boundary bit, the
dynamical update, and its coupling to X were **chosen** in these
models; they are not derived from actual cubic OI \(d=3\) dynamics.
No claim is made about \(\hbar\), H-slope/KMS, finite \(\epsilon\),
Yang–Mills, Bell correlations, or a physical nonclassical instrument.
The full continuous-product Hilbert or microstate entropy should
not be identified with the measured one-bit Shannon entropy.

## Reproducible finite-prefix countercontrols

Run:

    python3 -I -B verification/programmes/substratum/continuous-substates/boundary_controls_probe.py

For each horizon \(n=1,\ldots,9\), the script uses a cyclic
finite hidden register of length \(q=n+1\), enumerating all
\(2^{q+1}\) total states and checking the exact two-way inverse.
Because \(n<q\), no hidden bit is read twice in the prefix;
the finite enumeration agrees **exactly** with the
infinite-product law through that horizon.

It verifies that R yields all \(2^{n+1}\) visible words equally
often, D yields only the two constant words, and Q at a separate
three-step horizon yields four alternating/constant words together
with the indicated rooted matrices. The independently derived
infinite-product result is algebraic and **not** inferred from
testing only nine horizons.

**Finite-versus-infinite horizon discriminant.** For a finite cyclic register of length
(q), (T_R^q(x,b)=(x,boplus igoplus_{i=0}^{q-1}x_i)), so
(T_R^{2q}=I) and (b_{2q}=b_0) in **every** realization. By contrast,
the unbounded independent stream satisfies
(Pr(b_{2q}=b_0)=1/2) for every (q>0). Thus the finite model
agrees exactly with the infinite observer's full visible law for any
preselected horizon (n<q), but **cannot be equated to it for all
future times**. The script separately tests the finite full return
for (q=2,ldots,8); the infinite probability follows algebraically
from independent fair increments.

This is an exact countercontrol to promoting *finite-horizon surrogate
equivalence* into an *all-horizon gauge equivalence* solely because
the observer has finite instantaneous resolution.

### Discriminant for subsequent GR/SM work

A source model must fix its **same** microscopic update, invariant
state, finite allowed observer/setting interface, finite boundary
mode count, accessible time horizon, and complete public record
before assigning hidden cardinality "gauge" or using a finite
per-mode entropy in a thermal matching calculation. Compare
an exactly decoupled hidden extension, a coupled hidden stream,
and a finite hidden register whose far-horizon recurrence becomes
observable. State whether equivalence is exact on all public
histories, finite-horizon only, or a leading-order estimate.

**Status:** exact paper mathematics + exhaustive finite-prefix
regression; awaits independent review. Research-only draft,
no adoption, manuscript change, merge, F/E, or workflow dispatch.
