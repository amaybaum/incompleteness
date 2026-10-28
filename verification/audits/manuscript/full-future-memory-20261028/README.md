# Whole-future memory companion

Research candidate, not yet independently accepted or compiler verified. Based on
the accepted finite-block trajectory recovery at PR #990, `a958bc54`.

## Exact object and entropy convention

Let the finite initial sample space be Ω = V × H, with arbitrary normalized law μ,
and let φ permute Ω. Define F(s)(j) = πV φ^(j+1)(s), for every natural j. The
codomain FutureTrace is **the image of F**, a finite set of entire sequences. It
is finite because F has finite domain. It can have fewer elements than Ω.

At time t the whole-future random variable is Y_t(q) = F(φ^t(q)). Its j-th decoded
coordinate is exactly X_(t+j+1)(q), not a finite-prefix approximation. Two codes
are equal exactly when their decoded sequences agree at every future time.
Every finite future block is a deterministic truncation of this same variable.

The entropy convention here is ordinary discrete Shannon entropy of Y_t on its
finite image, and similarly for its finite joint laws with X_<t and X_t. This is
the literal entire-future variable for this finite deterministic realization.
No infinite-product measure, sigma-algebra conditional entropy, limit theorem,
or identification with a separate measure-theoretic convention is formalized.

## Written proof

Y_t is a deterministic function of (X_t,H_t), while the time-t joint law is the
pushforward of μ along q ↦ (X_<t(q),φ^t(q)). Therefore the existing finite Shannon
data-processing theorem applies to the actual entire-future variable:

Iμ(X_<t;Y_t | X_t) ≤ Iμ(X_<t;H_t | X_t) ≤ log₂|H|.

The bound holds for every natural t. The range of these conditional information
values is nonempty and uniformly bounded above. Hence its genuine real supremum
I*whole satisfies I*whole ≤ log₂|H|, and exponentiation gives 2^I*whole ≤ |H|.
No replacement of a supremum by a finite maximum is made.

This argument needs neither a period bound nor a claimed N−1 distinguishing
horizon. It does not prove that a chosen finite prefix already determines the
entire future. It does not derive a physical preparation, measurement or retained
record, hidden-state opacity, or information accumulation without hidden reuse.

## Relation to the manuscripts

Main §3.4's C3 proof explicitly treats X_>t as a function of (X_t,H_t), but does
not specify an infinite-product entropy convention. Under the finite-image
discrete convention stated above, the companion matches that whole-future
argument and the supremum over natural times. Any broader stochastic-process or
measure-theoretic reading remains a separate dependency, not a silent promotion.
No manuscript, coverage grade or prior accepted source is changed here.

## Verification path

The new module is imported by OIBridge's normal CI build and has a kernel-only
research entry before the preserved final KTOKEN census family. Eight endpoint
axiom reports are printed. No local Lean/Mathlib build or full suite is run under
AGENTS A.40. The bounded independent controls use complete permutation-period
words to encode entire traces in finite examples, with nonuniform/correlated
initial laws, a short-prefix countercontrol, and sharp cyclic-register examples.
Coordinate and degeneracy checks are exact; the Shannon entropy bounds and
saturation checks are numerical with tolerance 10^-12. Explicit failure guards
execute under normal and optimized Python; a deliberate failing guard must exit
nonzero under both. These examples are controls, not universal proof certificates.

The initial control checkpoint `10c2a5a4` used Python assert statements, which
optimized Python removes. Its matching optimized output was not evidence of
executed optimized checks. That rejected control revision is preserved in branch
history; this correction does not alter the Lean module or written mathematics.
