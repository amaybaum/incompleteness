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
(\(H(b)\le\ln2\) nats), even though \(X\) is uncountable.

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
\(\Gamma_2=I\). Since \(\Gamma_1\) has rank 1 and \(\Gamma_2\) rank 2,
no matrix \(\Lambda\) satisfies \(\Gamma_2=\Lambda\Gamma_1\), so the rooted
family is P-indivisible on \(\{0,1,2\}\). At time 2, distinct positive
past records with the same current bit have different next-step
conditional laws, so history readback is present. This demonstrates
**possibility**, not automatic recurrence or native OI physics.

**Instantaneous versus cumulative visible entropy.** In all three
models the instantaneous interface B is a single bit, so
\(H(b_t)\le1\) bit at every \(t\). Under R the cumulative record
entropy \(H(b_0,\ldots,b_n)=n+1\) bits is unbounded in \(n\) when the
observation duration and record storage are unlimited. A bound on
the entropy of cumulative distinguishable histories therefore requires
an additional finite duration, capacity, reset, or information-flow
condition; the one-bit bound on instantaneous visible entropy holds
without one.

**Physical restriction.** The source of the boundary bit, the
dynamical update, and its coupling to X were **chosen** in these
models; they are not derived from actual cubic OI \(d=3\) dynamics.
No claim is made about \(\hbar\), H-slope/KMS, finite \(\epsilon\),
Yang–Mills, Bell correlations, or a physical nonclassical instrument.
The microstate entropy of the continuous product system is infinite;
one bit is the Shannon entropy of the visible marginal.

## Reproducible finite-prefix countercontrols

Run:

    python3 -I -B verification/programmes/substratum/continuous-substates/boundary_controls_probe.py

For each horizon \(n=1,\ldots,9\), the script uses a cyclic
finite hidden register of length \(q=n+1\), enumerating all
\(2^{q+1}\) total states and checking the exact two-way inverses of
R and D. Since \(n\le q\), the increments \(x_0,\ldots,x_{n-1}\)
occupy distinct register cells, so the finite enumeration agrees
**exactly** with the infinite-product law through that horizon.

Each map is iterated directly. The script verifies that R yields all
\(2^{n+1}\) visible words equally often, D yields only the two constant
words, and Q (checked to be an involution) at a separate three-step
horizon yields four alternating/constant words together with the
indicated rooted matrices and their ranks. The independently derived
infinite-product result is algebraic and **not** inferred from
testing only nine horizons.

Expected result: exit status 0, with exactly these lines on standard
output:

    PASS SHIFT-XOR horizon=1, q=2: 4 equiprobable records, H(record)=2 bits; decoupled=2 constant records
    PASS SHIFT-XOR horizon=2, q=3: 8 equiprobable records, H(record)=3 bits; decoupled=2 constant records
    PASS SHIFT-XOR horizon=3, q=4: 16 equiprobable records, H(record)=4 bits; decoupled=2 constant records
    PASS SHIFT-XOR horizon=4, q=5: 32 equiprobable records, H(record)=5 bits; decoupled=2 constant records
    PASS SHIFT-XOR horizon=5, q=6: 64 equiprobable records, H(record)=6 bits; decoupled=2 constant records
    PASS SHIFT-XOR horizon=6, q=7: 128 equiprobable records, H(record)=7 bits; decoupled=2 constant records
    PASS SHIFT-XOR horizon=7, q=8: 256 equiprobable records, H(record)=8 bits; decoupled=2 constant records
    PASS SHIFT-XOR horizon=8, q=9: 512 equiprobable records, H(record)=9 bits; decoupled=2 constant records
    PASS SHIFT-XOR horizon=9, q=10: 1024 equiprobable records, H(record)=10 bits; decoupled=2 constant records
    PASS FINITE-LONG-HORIZON q=2: T^(2q)=identity
    PASS FINITE-LONG-HORIZON q=3: T^(2q)=identity
    PASS FINITE-LONG-HORIZON q=4: T^(2q)=identity
    PASS FINITE-LONG-HORIZON q=5: T^(2q)=identity
    PASS FINITE-LONG-HORIZON q=6: T^(2q)=identity
    PASS FINITE-LONG-HORIZON q=7: T^(2q)=identity
    PASS FINITE-LONG-HORIZON q=8: T^(2q)=identity
    PASS TOGGLE: rooted Gamma_1=[[1/2,1/2],[1/2,1/2]] (rank 1), Gamma_2=I (rank 2) => no Lambda with Gamma_2=Lambda Gamma_1; P-indivisible
    PASS TOTAL: 17758 checks; 9 shift-XOR/decoupled horizons + 7 long-horizon returns + 1 toggle case

A failed check prints a `FAIL` line and exits with status 1.

**Finite-versus-infinite horizon discriminant.** For a finite cyclic register of length
\(q\), \(T_R^q(x,b)=(x,b\oplus \bigoplus_{i=0}^{q-1}x_i)\), so
\(T_R^{2q}=I\) and \(b_{2q}=b_0\) in **every** realization. By contrast,
the unbounded independent stream satisfies
\(\Pr(b_{2q}=b_0)=1/2\) for every \(q>0\). Thus the finite model's
visible law agrees exactly with the infinite observer's for every
horizon \(n\le q\) and first differs at \(n=q+1\), where
\(b_{q+1}\oplus b_q=b_1\oplus b_0\) in every realization; it
**cannot be equated to it for all future times**. The script separately tests the finite full return
for \(q=2,\ldots,8\); the infinite probability follows algebraically
from independent fair increments.

This is an exact countercontrol to promoting *finite-horizon surrogate
equivalence* into an *all-horizon gauge equivalence* solely because
the observer has finite instantaneous resolution.

### Discriminant for later models

A source model must fix its **same** microscopic update, invariant
state, finite allowed observer/setting interface, finite boundary
mode count, accessible time horizon, and complete public record
before assigning hidden cardinality "gauge" or a finite per-mode
entropy. Compare
an exactly decoupled hidden extension, a coupled hidden stream,
and a finite hidden register whose far-horizon recurrence becomes
observable. State whether equivalence is exact on all public
histories, finite-horizon only, or a leading-order estimate.

**Status:** exact derivation on paper (infinite product system);
exhaustive enumeration over cyclic registers \(q=2,\ldots,10\)
(\(q=2,\ldots,8\) for the full-return check); research-only; no
manuscript claim depends on it.
