# Level 3A — pair-marginal reduction theorem (structural; written 2026-10-03 10:05 UTC, during validation, before any Stage-A output)

This is the structural upper bound PREREG-3A §5 requires for R4-CLOSED: a statement about the true orbit
C(r; G₃) and the full effect space, not about a finite table. The computation is its control (any certified rank
> 4 for the linear rule refutes it); it is not its evidence.

## Setting

Lattice ℤ, site state (u_i, v_i) ∈ {0,1}², leap v^{t+1}_i = F(v^t)_i ⊕ u^t_i, u^{t+1}_i = v^t_i, with
F(v)_i = v_{i−1} ⊕ v_{i+1} (linear; the proof uses only that F has coefficient 1 in one edge variable, see §4).
Initial measure μ₀: uniform product on all (u^0_i, v^0_i). Observer OBS-R: site-0 pair visible; external record.
Interface letters: any permutation π of {0,1}² applied to the site-0 pair (no leap); free leap i; observation o:
read b = v_0, append b to the record, apply κ_b to the pair (any map {0,1}² → {0,1}² depending on b — injectivity
is not needed here), then one leap; m: o with the record discarded. This covers I₂, I₃, every κ ∈ IC and every
action set up to all of Sym({0,1}²).

Write X_{≤t} for the initial data (u^0_j, v^0_j) with |j| ≤ t.

## 1. Cone with disturbances

**Lemma 1.** After t leaps, the site-0 pair (after any actions at time t), every disturbance applied at times ≤ t,
and the record written at times ≤ t are functions of X_{≤t}.

*Proof.* Induction on t. Each leap is radius-1; each action and each disturbance at time s is a function of the
site-0 pair at time s, itself a function of X_{≤s} by induction; the reading at time s is v^s_0, a function of
X_{≤s}. ∎

## 2. The fresh coin

**Lemma 2.** For every t ≥ 0, F_t := v^t_{−1} ⊕ v^t_{1} (the sites adjacent to the observer at time t, after the
actions at time t) satisfies F_t = v^0_{t+1} ⊕ v^0_{−(t+1)} ⊕ g_t(X_{≤t}) for some function g_t. Hence F_t is a
fair bit independent of X_{≤t}, so independent of the record, of the site-0 pair after the actions at time t, and
of every earlier F_s (s < t, a function of X_{≤s+1} ⊆ X_{≤t}).

*Proof.* The leap is affine over GF(2) in the configuration, so the configuration at time t is the free linear
evolution of X plus the linear propagation of the disturbances δ_s (s ≤ t−1), each δ_s a change of the site-0 pair
at time s. Site 1 at time t receives from the free evolution the initial variable at site t+1 with coefficient 1:
the rule carries v_{i+1} with coefficient 1, and the path (t+1, 0) → (t, 1) → … → (1, t) moves one site left per
leap, never passing through site 0, so no disturbance alters it. Every other free contribution to v^t_1 comes from
sites in [1−t, t], i.e. from X_{≤t}; every disturbance contribution is a function of X_{≤t−1} by Lemma 1,
propagated linearly. So v^t_1 = v^0_{t+1} ⊕ g⁺(X_{≤t}), and symmetrically v^t_{−1} = v^0_{−(t+1)} ⊕ g⁻(X_{≤t}).
The variables v^0_{±(t+1)} are uniform and independent of X_{≤t} and of each other under μ₀. ∎

Actions at time t (permutations, κ_b) change only site 0, so they do not affect F_t.

## 3. Reduction to a Markov theory on the pair

**Theorem.** Let a preparation (protocol P, record string ρ of positive weight) be given, and let ν be the
conditional distribution of the site-0 pair given ρ (after P's last letter). For every effect protocol E and
record event B, P(B | P, ρ) = Σ_p ν(p) · K_E(p, B), where K_E does not depend on P or ρ. Consequently every effect
is a linear functional of ν ∈ ℝ^{4}: the system-effect space, as functionals on all preparations, has dimension
≤ 4, and so has its subspace C(r; G) for every generator set G built from the letters above.

*Proof.* Follow E letter by letter, tracking the conditional law of (pair, record) given the past record.
- A permutation π maps the pair by π; the hidden lattice is untouched.
- A reading (the first step of o or m) reads v_0 of the current pair; the branch κ_b maps the pair by κ_b.
- A leap at time t maps the pair (u′, v′) (after the actions) to (v′, F_t ⊕ u′). By Lemma 2, F_t is a fair bit
  independent of (record so far, (u′, v′)) jointly, hence conditionally independent of (u′, v′) given the record:
  the new pair is (v′, N) with N uniform and independent of everything so far.
So the pair-and-record process is a Markov chain on {0,1}² × records whose transition kernels (π, read-and-κ_b,
leap ↦ (v′, uniform)) are fixed functions of the letter alone; the hidden lattice enters only through the F_t,
each of which is fresh. Hence the law of E's record given the start is Σ_p ν(p) K_E(p, ·), with K_E the product of
the kernels. Linearity in ν gives the dimension bound; the orbit span is a subspace of the effect space. ∎

**Corollary (what the computation can add).** If for some κ a finite table certifies rank 4 (effects of length
≤ L_e on preparations of length ≤ L_p), then the full effect space has dimension exactly 4 (≥ 4 from the table, ≤ 4
from the theorem). If moreover dim C_k(r; G₃)|_X = 4 is certified, then dim C(r; G₃) = 4 exactly;
C(r; G₃) contains 1 and r and is G₃-invariant by construction (g(1) = 1 for non-selective g; g(w(r)) = (gw)(r)),
so **R4(r; G₃) holds with E = C(r; G₃)** — R4-CLOSED for that κ. The WELLDEF guard is not needed for this
conclusion: the theorem supplies the invariant object directly.

## 4. Scope of the proof (what it uses and what it does not)

- Used: (a) the product initial measure (independence of v^0_{±(t+1)} from X_{≤t}); (b) coefficient 1 of F in an
  edge variable along a cone-edge path that avoids site 0 — **edge-permutivity**. Both edges were used above for
  symmetry; one suffices: with F = v_{i−1} ⊕ h(v_i, v_{i+1}), v^t_{−1} = v^0_{−(t+1)} ⊕ g(X_{≤t}) still holds
  along the left edge (the h-terms and u-terms on the path are functions of X_{≤t}), and F_t ⊕ u′ is again
  uniform and independent of X_{≤t} ∪ {the right-edge data it may involve}, which suffices for the Markov step
  because the record and pair at time t are functions of X_{≤t}. The affine-superposition form of Lemma 2's proof
  is then replaced by this direct edge argument. This is the prediction for 3B's cells R_LS and R_5.
- Not used: linearity beyond edge-permutivity; injectivity of κ_b; the record being one bit; the specific action
  set; the horizon. The bound is for the infinite-horizon objects.
- Not covered: correlated initial measures (3B's H₁: v^0_{t+1} dependent on v^0_t breaks (a)); rules without an
  edge variable of coefficient 1 (R_NL, R_NS-n, R_NS-m); observers other than OBS-R; any Q-layer property. The
  reachable state set is a subset of the simplex on four pair configurations; nothing here says it is or is not
  a polytope with six vertices — that is a finite computation on the reachable set, separate from this bound.

## 5. Status

Proof written before Stage-A output; to be re-read against the tables once they exist (any certified rank > 4 for
the linear rule refutes Lemma 2 or the Theorem as stated). Independent review of the two lemmas is the remaining
verification step; they are short enough to be checked by hand.

***

## Amendment 1 (owner review, 2026-10-03, after Stage-A output; the text above is unchanged, hash `272bee1b`)

**Fresh-coordinate lemma (the single place edge-permutivity enters).** Let F have coefficient 1 in the edge
variable v_{i−1} (left-edge-permutive; the right edge is symmetric and only one edge is needed). Then after every
leap at time t, the v-coordinate of the site-0 pair is
v^{t+1}_0 = v^0_{−(t+1)} ⊕ R_t, where R_t is a function of X_{≤t} together with data of sites ≥ 1 at time t,
and v^0_{−(t+1)} is uniform and independent of all of it under the product measure. *Proof.* Along the left
cone edge the path (−(t+1), 0) → (−t, 1) → … → (−1, t) → (0, t+1) moves one site right per leap and never meets
site 0 before the last step, so no action or disturbance touches it; at each step the rule carries the edge
variable with coefficient 1, so it survives with coefficient 1 to v^t_{−1} and then to v^{t+1}_0 =
v^t_{−1} ⊕ (rest); the rest is built from sites ≥ −t at time t and from u′_0, all functions of X_{≤t} and the
right-hand data. ∎ Linearity is not used; the product measure is used once, for the independence of
v^0_{−(t+1)} from the rest.

Therefore, after every leap, one pair coordinate is a fresh fair bit independent of everything observable, and
every protocol's record law depends only on the four-state pair marginal at its start (Theorem, §3): the true
effect space of OBS-R under any interface in the class has dimension ≤ 4, as functionals on all preparations.

**The sandwich, explicitly.** For a κ with a certified finite table at horizon k on preparation set X:

    4 = dim(C_k(r; G₃)|_X)  ≤  dim C_k(r; G₃)  ≤  dim C(r; G₃)  ≤  4,

the first inequality because restriction to X cannot raise rank, the second because C_k ⊆ C, the third by the
Theorem (C(r; G₃) is a subspace of the effect space). Hence dim C(r; G₃) = 4. C(r; G₃) = span({1} ∪ {w(r) :
w ∈ G₃*}) contains 1 and r and is invariant under every g ∈ G₃ by construction (g(1) = 1; g(w(r)) = (gw)(r)).
So E := C(r; G₃) witnesses R4(r; G₃): **R4-CLOSED** for that κ. Finite equality C_k = C_{k−1} (AT-RANK) plays no
role in this conclusion; it is finite-horizon evidence only. Stage C is a depth probe and is not needed for it.

**What this does and does not say.** The ceiling is "edge-permutivity + product measure ⇒ effect space ≤ 4", not
"linearity ⇒ rank ≤ 4". Level 3A establishes interface capacity: I₃ can expose R4(r; G₃) for the linear rule. It
does not say that linearity caused R4 (3B's question) and does not say anything Q-layer.
