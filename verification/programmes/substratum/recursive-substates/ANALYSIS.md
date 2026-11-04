# SUBSTATE-2: exact arguments, gaps, and falsifiable continuation

**Research-only mathematical analysis** for issue #1010 / draft PR #1011.
No topological statement below is asserted to be Lean certified unless an
explicit kernel build confirms it. The finite Python controls in
`recursive_controls.py` are separate from the infinite-limit proofs.

## The finite-depth theorem: what is proved and what is imported

Let \(X=\varprojlim X_n\) be an inverse limit of finite discrete spaces,
with compact inverse-limit topology and compatible projections
\(p_n:X\to X_n\). Let \(A\) be a finite *discrete* observation alphabet.

**Topological lemma (standard, paper proof here; Lean bridge open).**
If \(f:X\to A\) is continuous, then there exist \(N\) and a function
\(f_N:p_N(X)\to A\) such that \(f=f_N\circ p_N\).

*Proof.* A fiber \(f^{-1}(a)\) is clopen. Every point in the fiber has
a basic open cylinder neighborhood \(p_{n_x}^{-1}(B_x)\) contained
in the fiber. The fiber is compact, so finitely many such cylinders
cover it. Repeat for finitely many \(a\), and let \(N\) be the maximum
of all finitely many cylinder depths. Every level-\(N\) cylinder is
contained in one fiber of \(f\), so \(f\) is constant on each
\(p_N\)-fiber. Define \(f_N\) on the actual projection image.
The same argument applies when bonding maps are not surjective;
one must define \(f_N\) on \(p_N(X)\), not invent values elsewhere. □

This is **not** a universal statement about *measurable* finite
observations; a measurable map may depend on arbitrarily many digits.
Nor does it imply all infinite-state dynamics are continuous.

**Finite-horizon lemma.** If \(T:X\to X\) is continuous and
\(\pi:X\to A\) is continuous, then for every fixed horizon \(K\)
there exists a finite stage \(N(K)\) determining the entire word
\(\pi(x),\pi(Tx),\ldots,\pi(T^Kx)\). The level may grow with K.

*Proof.* Apply the topological lemma to each of these finitely
many continuous compositions and take the largest depth. □

**All-time corollary under a common exact period.**
Suppose a single \(L>0\) satisfies
\(\pi(T^Lx)=\pi(x)\) **for all \(x\)**. For each integer \(t\ge0\),
\(\pi(T^{t+L}x)=\pi(T^t x)\), applying the return assumption
at \(T^t x\). Hence the entire infinite visible word is the
periodic repetition of its first L values. Take the common
finite-stage bound for these L functions, giving one N
that determines *every future visible observation*.
This does not imply \(T^Lx=x\) or that hidden evolution stops.

**Distinctions:** Ordinary Poincaré recurrence is not a common exact
period. A measure-theoretic a.e. common-return statement can be treated
modulo an invariant null set, but that is a separate proof and does
not automatically give the pointwise factor theorem. A chosen
noncontinuous readout is outside these statements.

The new `OIBridge.RecursiveFiniteFactor` Lean candidate is only
the second (finite-family aggregation **assuming** individual
stage factorization) plus a periodic-family wrapper **assuming**
the observation-period identity. It must not be described as a
kernel proof of the topological lemma or of a physical OI recurrence.

## A: compatible odometer, infinite memory storage without visible backflow

At finite stage \(K_n=\mathbb Z/2^n\), put \(T_n(x)=x+1\)
and \(\pi_n(x)=x\bmod2\). Reductions commute with every \(T_n\):
\(p_{n+1,n}(x+1)=p_{n+1,n}(x)+1\).
The infinite map on \(\mathbb Z_2\) is invertible by subtracting 1
and preserves Haar. Yet
\[
X_1=1-X_0,\qquad X_2=X_0
\]
for the least-bit observation, with \(\Gamma_1\) exactly the
two-state permutation swap and \(\Gamma_2=I\).
No root-level P-indivisibility follows. Every low digit depends
only on low digits of its initial state, regardless of carry
from low to high. Inaccessible deeper data alone cannot create
a new visible quantum resource.

The exact source enumerates all \(2^n\) states at each
\(n=1,\ldots,9\), verifies the full three-time law and the
reduction/intertwining identities. The infinite statements
follow algebraically from the compatible reductions.

## B1: specified deep-to-visible feedback does produce *classical* memory

On a fair infinite bit sequence, fix **one level** \(m\ge1\).
Let \(T_m\) flip \(b_0\) conditioned on the static bit \(b_m\)
and keep every other coordinate unchanged. The map is an
involution; it preserves product-fair measure. For
\(X_t=(T_m^t b)_0\),
\[
X_1=X_0\oplus b_m,\qquad X_2=X_0.
\]
Consequently \(\Gamma_1=\frac12J\), \(\Gamma_2=I\) and
\(I(X_0;X_2\mid X_1)=1\) **bit**.
All four allowed triples \(000,010,101,111\) occur with
probability \(1/4\).

The depth really matters: \(b=0\) and the stream with only
\(b_m=1\) are identical at every level below \(m+1\), yet
have different \(X_1\). Thus the next visible observation
cannot factor through a shorter initial prefix.

The exact source checks all 256 configurations of an
8-bit truncation for \(m=1,2,3,5,7\), including all triple
probabilities, involution and depth witness. There is no
single unbounded-depth claim: **each m gives a different
dynamical model**. The result is a controlled *classical*
feedback toy, neither quantum interference nor OI's native C4.

## B2: reveal deeper coordinates at later times without common return

Take \(X=\{0,1\}^{\mathbb Z}\) with product-fair measure
and invertible left shift \((Tx)_i=x_{i+1}\).
Let \(\pi(x)=x_0\). Then \(X_t=x_t\) for all \(t\ge0\), so
all finite visible words are iid fair coin tosses. In
particular, for every **positive** L,
\[
\Pr[\pi(T^L x)=\pi(x)]=\tfrac12\ne1.
\]
There is no common a.e. identity return, despite the
continuous invertible measure-preserving dynamics on
a compact Cantor space. At each finite time t, only one
coordinate is required, but the necessary initial depth
grows without bound over time.

Finite controls use n-bit cyclic shifts, with n from 3 to 9,
and verify exact uniform cylinder probabilities through the
specified accessible horizon, as well as return after n steps.
**Finite cyclic return at n is not a uniform period
surviving n→∞.** This separates unbounded-depth
sensitivity from a common periodic observed factor.

## C: profinite links can carry curvature, not an action selector

Let four oriented links around a single plaquette take values
in \((\mathbb Z/2^n)^4\). The compatible system defines
\(K=(\mathbb Z_2)^4\), a compact totally disconnected **abelian**
group. For vertex variables \(g_v\), gauge re-description is
\(u_{vw}\mapsto u_{vw}+g_v-g_w\), so the oriented plaquette
sum \(k=\sum_e u_e\) is gauge invariant. The link configuration
\((1,0,0,0)\) gives \(k=1\), so this system is *not*
restricted to pure gradients. Conversely, if links are obtained
from site differences they all have k=0.

The toy's dynamics \(T(u_0,u_1,u_2,u_3)
=(u_0+1,u_1,u_2,u_3)\) is invertible, compatible
under reduction, gauge covariant and Haar preserving.
The readout \(k\bmod2\) toggles every step and has
period 2; its rooted transitions are permutation matrices,
not an instrument for QM.

An exact **ambient** lattice-action control at n=2
uses \(q=4\) and \(c_k=\cos(2\pi k/4)\).
For \(w_k=1-c_k\), the values
\[
(w_1,w_1^2)=(1,1),\qquad
(w_2,w_2^2)=(2,4)
\]
are not proportional. Counting Haar yields
\(\mathbb E[w]=1\),
\(\mathbb E[w^2]=3/2\), but these are **observables**,
not a dynamically chosen Gibbs weight.
The exact probe checks gauge covariance, projection
compatibility, inversion, non-flatness and uniform
holonomy distribution on all \(2^{4n}\) link states at
\(n=1,2,3,4\), with largest enumeration 65,536.

This profinite group is **not** a connected \(U(1)\)/
\(SU(2)\) gauge group. A continuous group homomorphism
from a compact profinite group into a finite-dimensional
Lie group has finite image; hence no such homomorphism
can surject onto connected \(U(1)\) or \(SU(2)\).
One must source a different connected carrier, non-group
representation, or suitable physical continuum limit.
A solenoid, as an inverse limit of circles, is a different
topological choice; SUBSTATE-1 already shows its
continuous structure alone does not force memory.

## "Fractal" / logarithmic scale corrections are not yet predictions

An infinite binary hierarchy can be assigned an ultrametric
\(d_b(x,y)=b^{-k(x,y)}\) for \(b>1\), with k the first
disagreeing digit. Its n-th cylinders have diameter
of order \(b^{-n}\) and count \(2^n\); the resulting
mathematical dimension is \(\log 2/\log b\).
The free choice of **metric scale b** shows that a
"fractal dimension" is not an OI-derived physical
spatial dimension or a prediction of d=3.

Under an independently derived discrete *dynamical*
scale covariance, certain observables could show
log-periodic corrections. Merely positing a Cantor-like
space gives neither the scale law nor a nonzero correction.
The independently varying b, coupling and readout
are precisely the fit freedom that the next hypothesis
must prevent.

## Literature and independent controls

The finite-factor proof is a standard result for
profinite spaces; see the compactness/entourage argument
at https://mathoverflow.net/questions/27461/profinite-spaces-are-the-pro-completion-of-finite-sets
and notes on profinite finite quotients at
https://www.dpmms.cam.ac.uk/~grw46/LectureNotes2021.pdf .
The finite-image obstruction for continuous homomorphisms
from profinite to Lie groups is discussed in
https://www.math.purdue.edu/~tongliu/teaching/598/p-adicrep.pdf .
For scale invariance versus log-periodic physical
corrections, see D. Sornette,
https://arxiv.org/abs/cond-mat/9707012 .
These references are **background/literature controls**,
not new OI physical evidence. No full first-hand audit
of their proofs is claimed.

**Required before any physical candidate:** fix one
coupling T across all levels, show its microscopic
realization and invariant measure, specify which
measurements are accessible and repeatable,
test a new independent observable against both
classical feedback and gauge-covariant action ambiguity,
and retain the area-law, C4, Bell and operational F2
requirements separately. Anything chosen to fit QM
or Wilson action after looking at the target fails
the hard-to-vary rule.

**Disposition:** finite models A/B/C have exact
regression controls; B1 has an all-depth family of
finite-m-sourced classical memory, not one universal
dynamics; B2 has all-depth-over-time sensitivity but
no common visible period; C is a non-flat profinite
gauge kinetic setup with action selection open.
Quantum, Yang–Mills and physical fractal claims **OPEN**.
