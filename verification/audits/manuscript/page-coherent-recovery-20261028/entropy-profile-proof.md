# Finite coherent-subspace entropy profiles

Research candidate; written proof, not Lean-certified. Base `20ca05f`.
Related correction: SC-36 #978. No claim here restores GR A.8–A.9.

## Model and ensemble

Let n≥2 and 0≤k≤n. Computational configurations are F₂ⁿ. Prepare the pure
coherent product state |+>^⊗k |0>^⊗(n−k), then choose **one** uniformly random
L∈GL(n,2) and apply U_L|x>=|Lx>. This is a reversible configuration permutation,
not a general unitary. Gaussian elimination realizes each L by reversible XOR
row additions and coordinate swaps. Its image state is

|V> = 2^(−k/2) Σ_{v∈V}|v>,

where V is a uniformly random k-dimensional subspace. Uniformity follows because
GL(n,2) acts transitively on these subspaces, with equal stabilizer sizes.
The coherent seed and this precise ensemble are inputs, not derived OI physics.

For every r=0,...,n use the nested coordinate cut R_r={1,...,r}, B_r its
complement **on the same sampled state**. Define S_r=−Tr(ρ_R log₂ρ_R) in bits.
There is no resampling at different cuts. These cuts are an abstract partition
schedule, not an evaporation dynamics or a mechanism transporting radiation.

## Proposition 1: exact entropy and spectrum

Write i=dim(V∩R), j=dim(V∩B), s=k−i−j. The nonzero Schmidt coefficients of |V>
are all 2^(−s/2), with multiplicity 2^s. Thus S_R=s and Tr(ρ_R²)=2^(−s).

Proof. Put I=V∩R and J=V∩B. Choose representatives v_a=(x_a,y_a) of V/(I⊕J).
The coordinate cosets x_a+I are distinct: equality would make the difference of
the representatives lie in I⊕J; the same holds for y_a+J. The normalized uniform
coset states |x_a+I> and |y_a+J> therefore form orthonormal families. Expanding
V into its 2^s disjoint cosets gives

|V> = 2^(−s/2) Σ_a |x_a+I>⊗|y_a+J>,

which is a Schmidt decomposition. In particular the entropy is an integer here.
It satisfies 0≤s≤h_r:=min(k,n−k,r,n−r). The r and n−r bounds are Schmidt-rank
bounds; i≥k−(n−r) and j≥k−r imply s≤n−k, and s≤k is immediate.

## Proposition 2: exact distribution

Let [a choose b]_2 denote the number of b-dimensional subspaces of F₂^a,
zero outside 0≤b≤a. Let g_s=|GL(s,2)|=∏_{t=0}^{s−1}(2^s−2^t), with g_0=1.
For i,j≥0 and s=k−i−j≥0, the number of V having those intersection dimensions is

N(i,j) = [r choose i]_2 [n−r choose j]_2
         [r−i choose s]_2 [n−r−j choose s]_2 g_s.

Divide by [n choose k]_2 for its probability. Consequently the mean entropy is
the exact rational number Σ_{i,j}(k−i−j)N(i,j)/[n choose k]_2.

Proof. Choose I⊂R and J⊂B. The image of V in (R/I)⊕(B/J) has trivial
intersection with either summand. It is exactly the graph of an isomorphism
between an s-dimensional subspace of R/I and an s-dimensional subspace of B/J.
Conversely the inverse image of every such graph is a unique V with precisely
I,J as its intersections. The factors count these independent choices. Summing
therefore counts every k-dimensional subspace once. This is elementary finite
subspace/stabilizer-state mathematics; no novelty is claimed.

## Proposition 3: exact mean purity and a finite tent bound

Put b=n−r,
p=(2^k−1)/(2^n−1),
p₂=(2^k−1)(2^k−2)/((2^n−1)(2^n−2)). Then

E Tr(ρ_R²) = 2^(−k)[1+(2^r+2^b−2)p+(2^r−1)(2^b−1)p₂].

Proof independent of Proposition 2. If I=V∩R,J=V∩B then purity is |I||J|/|V|.
Expand |I||J| as a sum over pairs (a,c)∈R×B. The zero pair contributes 1.
A pair with exactly one nonzero vector has membership probability p, by counting
nonzero vectors in V. Two nonzero vectors on disjoint coordinate supports are
linearly independent and have joint membership probability p₂, by counting
ordered independent pairs. This gives the formula, including k=0 and k=1.

Since p≤2^(k−n) and p₂≤2^(2k−2n),

E purity ≤ 2^(−k)+2^(−r)+2^(−b)+2^(k−n) ≤ 4·2^(−h_r).

Convexity of −log₂ and Proposition 1 give

max(0,−log₂ E purity) ≤ E S_r ≤ h_r,
so in particular E S_r≥h_r−2 bits.

For n=2m,k=m this bounds the mean nested-cut profile within two bits below
min(r,2m−r), with exact zero endpoints. It is an ensemble expectation for the
stated positive-amplitude subspace states, not Page's Haar mean or its 1/2-nat
correction. For example n=2,k=r=1 gives mean entropy 1/3 bit and mean purity5/6.

For d≥0, Markov's inequality gives
Pr(S_r≤h_r−d)≤min(1,4·2^(−d)). For one common sampled V, a union bound gives
Pr(there exists r with S_r≤h_r−d)≤min(1,4(n+1)·2^(−d)).
No independence between cuts is assumed. The bound is useful only when its
right-hand side is small; it is not an exponentially-in-Hilbert-dimension Haar
concentration theorem. It controls a simultaneous **cut profile**, not the orbit
of repeated powers of one fixed matrix or the time series of an evaporation.

## Explicit examples and countercontrols

1. CNOT on |+>|0> gives Bell and a second CNOT returns |+>|0>. For a fixed cut,
   the entropies are 0,1,0 bits; a cycle average is 1/2 bit. It is not the uniform
   GL(2,2) ensemble average of 1/3 bit. An ensemble cannot silently replace time.
2. For n=2m apply the m disjoint CNOTs i→2m+1−i to the coherent seed. The resulting
   mirror Bell-pair state has S_r=min(r,2m−r) at every nested cut. A static,
   structured Bell-pair state therefore exhibits an exact tent without being a
   scrambling ensemble or an evaporation model.
3. k=0 gives a configuration state and S_r=0 under every permutation, preserving
   SC-36's vacuity obstruction. Identity L on the coherent seed gives zero at
   every coordinate cut too: coherence alone does not ensure entanglement.
4. The incoherent mixture on {00,11} has reduced entropy one bit but global
   purity1/2, unlike the pure Bell state. Reduced entropy is an entanglement
   measure here because global purity is assumed; a classical mixture is not a
   substitute coherent preparation.

## Relation to the actual Page problem

This finite ensemble is nonempty, explicit and implementable by permutation
unitaries acting on a stipulated coherent seed. It supplies a rigorous possible
mathematical replacement route, not the physical preparation or ensemble measure,
local scrambling, energy-shell dynamics, decoupling or evaporation law. It is not
a pure-state design on the full Hilbert sphere and it is not the whole stabilizer
ensemble. The existing configuration-orbit theorem remains vacuous; SC-36 and its
Introduction qualifications must survive independently of this research result.

Context: Page (1993), https://arxiv.org/abs/gr-qc/9305007, studies Haar-random pure
states. Smith–Leung (2006), https://arxiv.org/abs/quant-ph/0510232, study typical
entanglement in the larger stabilizer ensemble. Our restricted subspace counting
and finite bounds do not replace either result or claim a new Page theorem.
