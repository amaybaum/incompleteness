# Independent mathematical review: hidden-state identifiability

Baseline: `efa84ad90e3663fa2f5fdb036437f52a6b95fc54`. This note is an independently derived repair criterion and dependency audit, not a publication acceptance or a new physical reconstruction mechanism.

## Fixed model, preparation support and retained records

Let Omega be a nonempty finite set of N microscopic states, P a known permutation, r a known passive deterministic readout, and A the support of the stipulated initial law. For a retained word w of length k >= 1 define

F(w) = {s in A : r(P^j s) = w_j for every 0 <= j < k}.

A positive-probability retained word has nonempty F(w). Every state in F(w) has positive posterior probability. The initial microscopic state is identified by this word precisely when F(w) has one element. More generally, a specified quantity q(s) is identified precisely when q is constant on F(w). The proofs are separate directions: a constant value gives the decoder on this record; two compatible states with differing q values make every decoder from this record wrong on at least one positive-probability state.

For Omega = V x H and r = pi_V, the current microscopic candidates after the last readout are P^(k-1) F(w). Since P is bijective, this set has the same size as F(w). Its visible coordinate is fixed by the last retained record. Consequently its hidden coordinate is unique precisely when the entire set has one element. The same holds for the initial hidden coordinate because w includes the initial visible value. This current/initial equivalence requires invertibility; it fails for merging dynamics.

The information used here is the retained record sigma-algebra, not one instantaneous readout. The result does not establish that an actual embedded observer can store the necessary word, knows P/support, or has the required interventions. Those are specifications of the observational carrier, not automatic consequences of proper subsystem membership.

## Future-trace classes and a finite bound

Write s ~ s' when their passive readouts agree at every future time. Let C_l be the partition of the whole carrier by its first l readouts, C_0 the indiscrete partition. C_(l+1) refines C_l. If two consecutive partitions agree, equality of the readout and successor classes makes the partition forward invariant; no later split occurs. Every strict refinement increases the number of classes. Thus C_(N-1) already equals the full future partition for N >= 2. For N=1, the unique state is known without records, and a one-record convention is harmless.

Intersecting these full classes with A gives the final record classes on the selected support. Non-invariant support must not be substituted for the whole carrier in the bound: a two-state support inside a long deterministic cycle can require many observations before its two trajectories separate.

For a particular actual state, passive permanent ambiguity means that its full-trace class intersects A in at least two states. The much stronger statement that every possible record remains ambiguous requires *every* nonempty such intersection to have at least two elements. A proper instantaneous readout alone implies neither statement.

Interventions or altered readouts can split passive future classes. For a general permitted protocol family, use equivalence under that entire family; do not identify it with passive-readout equivalence. No N-1 active-protocol bound is asserted here for an arbitrary restricted grammar.

This is known-model state inference. Substratum Proposition 24.4 instead reconstructs an unknown predictive quotient from word probabilities under full-support and state-bound hypotheses. Even if the quotient is uniquely reconstructed, microscopic hidden fibres or a preferred factorization need not be identified across different models. One model can have singleton passive classes while a nonminimal spectator extension has the same visible law and non-singleton microscopic classes.

## Memory does not imply residual opacity

The conditional entropy chain rule gives

H(H_t | X_t) = I(X_<t ; H_t | X_t) + H(H_t | X_<=t).

Main's unavoidable-hidden-predictive-memory theorem bounds the first term from below by the observed conditional memory, not the last term. Each history-conditioned hidden posterior may be a point mass. Distinct histories ending at the same visible present can induce different point masses, giving a positive readback gap while the hidden state is fully inferred from the complete retained history.

The exact family P(b_0,...,b_m) = (b_1,...,b_m,b_0), m >= 1, read b_0, makes this explicit with arbitrarily large hidden capacity. Under the uniform initial law the first m+1 records are exactly the initial bits. At t=m the current state is (b_m,b_0,...,b_(m-1)), so the complete hidden vector is known. Nevertheless X_(m+1)=X_0 and the present X_m is an independent bit, giving I(X_<m ; X_(m+1) | X_m)=1 bit. The hidden capacity and full past/future conditional information are m bits, while H(H_m | X_<=m)=0. The m=1 member is the user's swap witness.

A permanently unread passive spectator is a different case. P(v,h,b)=(h,v,b), read v, leaves b unidentifiable from every passive history while v,h become identifiable after two records. Enlarging the readout to (v,b), or permitting a reversible swap of b into the visible slot, removes that ambiguity. This validates the interface dependence rather than restoring a universal opacity claim.

## Algorithmic and physical boundaries

For a known explicit finite model, compatibility and the full future partition are decidable by finite enumeration/refinement. Information-theoretic non-identifiability is therefore not Turing undecidability. The halting theorem is a statement about the absence of a uniform algorithm for all program/input pairs; it is not a theorem that each machine cannot know its own finite configuration or halting behavior.

Physical causal horizons may restrict accessible data, and no additional mathematical readout operation is supplied by the finite criterion. Their permanence and relevant preparation/control assumptions must be stated physically. Operational closure of a computational model excludes extra oracle operations; it does not forbid inference from histories produced by the operations already allowed.

## Independent bounded controls

`independent_controls.py` imports none of the author's implementations. It compares explicit full-period trajectories with the N-1 bound for all 442 permutation/binary-readout models of sizes 1 through 4 and all 6,122 nonempty support cases. It separately checks nonuniform posterior supports, all four swap states and the C4 gap, cyclic registers with one through six hidden bits, spectator law equivalence, interface/intervention refinement, delayed separation of a non-invariant support, and the noninvertible merging counterexample.

All 39,546 explicit predicates pass. Normal Python and `-O` produce identical structured output. These are finite controls supporting the written proofs; they are not a kernel proof or empirical validation of a physical OI observer mechanism.
