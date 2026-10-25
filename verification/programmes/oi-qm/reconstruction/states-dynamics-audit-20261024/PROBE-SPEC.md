# Finite-resource diagnostic: decision rule

Fixed before computation. This is a bounded exploratory check, not a governed
round or a native lattice implementation. Exact Python integer and Fraction
arithmetic only; no floating-point verdicts.

For each fixed input y and earlier public history h, assume the entire remaining
random input to the proposed sampler is a uniform space of 2^b atoms conditional
on y,h. It can arise from b initially independent fair bits whose conditional
independence survives that history. The apparatus is deterministic thereafter;
readiness bits are fixed, not counted as random entropy. The condition is about
the complete relevant randomness: correlated or additional uncontrolled inputs
are outside this diagnostic.

The target on successful branches is independent fair z and
(a,b)=00,10,11 with respective probabilities 5/10, 3/10, 2/10. The six joint
probabilities, ordered00z0, 00z1, 10z0, 10z1, 11z0, 11z1, are
(5,5,3,3,2,2)/20. The illustrative success probability 5/16 is a proposed
sampler benchmark, not an inherited requirement or a proved second-stage rate.

## Written derivation

If M>0 atoms succeed, the count of any outcome with probability 3/20 is 3M/20,
an integer. Coprimality of 3 and 20 forces 20 to divide M. Conversely if 20 divides
M, assigning these six integer counts realizes the law on successful atoms;
the remaining atoms are failures. This is abstract sampling feasibility only.
Thus a deterministic always-success sampler from finitely many fair bits
cannot give this exact law, since 20 never divides a power of two. For a
success rate 5/16, M=5*2^(b-4), which is integral only for b>=4 and divisible
by 20 only for b>=6. Six bits suffice at this abstract level: M=20 out of 64,
with the six counts 5,5,3,3,2,2 and 44 failures.

Retain the seed s and use an initially blank three-bit label register r.
The map (s,r)->(s,r XOR label(s)) is an involution on 64*8 states. This makes
the abstract sampler reversible, without erasing any distinctions among
seeds. The three blank bits are additional preparation resources. It does
not assert that the native lattice implements the map or prepares the bank.
The four interpreted carrier values are(y XOR a,y,y XOR b,z); a label
decoder here is only a mathematical test of their target law.

For the separate one-bit target p=(2+sqrt(2))/4, one has 8p^2-8p+1=0 and
p is irrational. Any successful event on M uniform atoms has probability n/M.
The integer 8n^2-8nM+M^2 is nonzero, so |8(n/M)^2-8(n/M)+1|>=1/M^2.
Factoring by p and using |8(n/M+p)-8|<8 for 0<=n/M<=1 gives
|n/M-p|>1/(8M^2). If M<=2^b this implies error>1/(8*4^b).
This is a finite-budget bound. It vanishes as b grows and does not refute A2.

For b>=1 and N=2^b, k=N/2+floor(sqrt(2N^2))/4 floored to an integer
(implemented as N//2+isqrt(2*N*N)//4) is floor(Np). The rational interval
[k/N,(k+1)/N] contains p and has width 1/N. Thus these fair-bit Bernoulli
samplers approach p arbitrarily closely, even though each misses it exactly.
A two-state model with initial probabilities(p,1-p) and identity evolution
reproduces p exactly; this countercontrol shows why the fair/rational-prior
assumption matters. It does not source that prior or a continuum of operations.

## Computational decision rule and scope

The checker reports pass only if all required checks and countercontrols pass:

1. Direct integer-count feasibility for b=0..16 agrees with the divisibility
   argument, including the success5/16 benchmark and always-success cases.
2. Enumerating every state of the64*8 sampler confirms bijection, involution,
   the full successful six-cell law, 44 failures, and both y carrier laws.
3. A wrong 5:2:3 calibration and a shared/fixed z construction are rejected;
   the latter preserves the (a,b) marginal, so the joint check is decisive.
4. Exact arithmetic in Q(sqrt(2)) verifies the polynomial identity and the
   strict error bound for all 0<=n<=M, 1<=M<=64. These finite cases test the
   implementation; the preceding integer/factorization argument establishes
   the general statement.
5. Dyadic brackets for b=1..16 contain p, have width2^-b, and shrink; the
   irrational-prior countercontrol remains exact.

The checker writes structured JSON and exits nonzero on any failed condition.
Normal and optimized Python executions must produce identical JSON. No verdict
is a kernel certificate, and no countability claim is inferred from the finite
enumeration. No approximation to an entire quantum instrument is inferred from
the Bernoulli example.
