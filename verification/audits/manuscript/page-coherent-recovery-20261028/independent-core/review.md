# Independent mathematical review: coherent-subspace cut profiles

**ACCEPT — scoped written mathematical result and bounded controls.** No defect found in the three propositions as stated. This is not acceptance of a physical Page curve, evaporation, OI-native preparation/scrambling, a repeated-permutation time law, or a Lean certificate. No manuscript, coverage, merge or release approval is given.

## Immutable candidate and review independence

Reviewed candidate: `bdcbd32bb55a5464d72b61682721f0b4bfaf446c`, tree `700fa72b23aaa37245d136804d0ad62bb5337a21`, PR #989. The worktree observed at the start and end of review instead names local HEAD `b0affb210e9f0a856ef9a55dd3e9a2e6e8eea2c7`; its entire tree is identical. Parent commit identities differ. This report pins the assigned immutable candidate, not its history or a moving branch. Both identities were reported to the coordinator. No candidate source was changed.

All reviewed inputs were extracted with `git show <candidate>:<path>` into `input/`. Their blob IDs, exact bytes, SHA256 digests and sizes are in `manifest.json`. The applicable `AGENTS.md` blob is `ca0d37ad1b4aa95b266bac3d4b27acab207eefe6` (the previously read guide). Relative to base `20ca05fe9e7e460de29e08f7a21029042fa45b12`, the candidate adds exactly the four research files; no manuscript or coverage file changes.

I derived the proof steps directly and implemented a separate exact enumerator using binary reduced-row-echelon bases, not the candidate's extension-by-one-vector enumeration. The independent checker does not import or execute the candidate checker. After those controls passed, I separately replayed the candidate checker; its complete structured output equals the retained result. Neither run establishes the universal proof by enumeration.

## Mathematical assessment

### Ensemble, entropy, and schedule

The inputs are explicit and nonempty: n≥2, 0≤k≤n, a coherent product seed |+>^k|0>^(n−k), and one uniformly sampled L in GL(n,2). The map x↦Lx is a reversible permutation of configurations. Transitivity with equal stabilizer size makes V=L(F₂^k×0) uniform among k-subspaces. No Haar distribution, physical preparation or time mixing follows from this construction. A single V supplies every nested coordinate cut R_r, r=0,…,n. Entropy is the von Neumann entropy in bits of a reduced globally pure coherent state; the cuts are an abstract partition schedule.

### Flat spectrum and exact entropy: accepted

Let I=V∩R, J=V∩B, and W=V/(I⊕J). For distinct W cosets, equality of their R-coordinate cosets modulo I would imply that after subtracting an element of I their difference lies in J, contradicting distinctness. The same argument holds on B. Thus both sets of normalized coordinate-coset vectors are orthonormal. There are 2^s terms, s=k−dim I−dim J, all with coefficient 2^(−s/2). This is a valid Schmidt decomposition, so all nonzero reduced eigenvalues are 2^(−s), entropy is s, and purity is 2^(−s).

The bounds s≤k,r,n−r are immediate. The dimension inequalities dim I≥k−(n−r) and dim J≥k−r give s≤n−k. Consequently h_r=min(k,n−k,r,n−r) is a valid upper bound even at k=0,n or endpoint cuts.

### Gaussian-binomial distribution: accepted; no missing lift factor

Fix I⊂R of dimension i and J⊂B of dimension j. In the quotient (R/I)⊕(B/J), the image W has dimension s=k−i−j and trivial intersection with either coordinate summand. Each projection of W is therefore injective. Its images are two s-subspaces, and W is the graph of their uniquely determined linear isomorphism. Conversely any such graph has a full inverse image under the quotient map of dimension i+j+s=k. That inverse image is exactly one V, and its intersections are exactly I and J. There is no additional lift choice: the inverse image already contains the full kernel I⊕J.

Thus the number is exactly

N(i,j)=[r choose i]₂[n−r choose j]₂[r−i choose s]₂[n−r−j choose s]₂|GL(s,2)|.

Zero Gaussian coefficients handle infeasible dimensions; s<0 is excluded. Summing counts each V once. Dividing by [n choose k]₂ gives the stated joint distribution and exact rational mean entropy.

An independent hand check at n=4,k=r=2 gives entropy-zero counts 1+9+1=11 for (i,j)=(0,2),(1,1),(2,0); entropy-one counts 9+9=18; and entropy-two count |GL(2,2)|=6. Total 35. Their mean purity is (11+18/2+6/4)/35=43/70.

### Mean purity by incidence: accepted independently of the distribution

Purity=|I||J|/2^k. Expand |I||J| over ordered a∈R,c∈B. The zero pair contributes one. There are 2^r+2^(n−r)−2 pairs with exactly one nonzero vector; each vector belongs to a uniform k-subspace with probability p=(2^k−1)/(2^n−1). There are (2^r−1)(2^(n−r)−1) pairs with both entries nonzero. Disjoint supports make them independent; counting ordered independent pairs in each k-subspace gives p₂=(2^k−1)(2^k−2)/((2^n−1)(2^n−2)). This proves exactly the candidate formula without the graph count.

For k=0, p=p₂=0 and the formula gives purity one. For k=1, p₂=0. For k=n, p=p₂=1 and the bracket is 2^n, again giving purity one. Denominators are nonzero because n≥2. The bounds p≤2^(k−n), p₂≤2^(2k−2n) hold, including k=0 separately; they yield the four-term purity bound and then E purity≤4·2^(−h_r).

### Jensen, entropy deficit and common-state tails: accepted

Because each state has S=−log₂(purity), convexity of −log₂ gives E S≥−log₂ E purity≥h_r−2. Entropy is nonnegative and at most h_r. The argument claims a two-bit additive bound for this particular ensemble, not the Haar/Page correction.

For any real d≥0, S_r≤h_r−d implies purity≥2^(d−h_r). Markov then gives probability at most 4·2^(−d), capped by one. Applying the union bound to the n+1 events on the very same random V gives min(1,4(n+1)2^(−d)). It uses no independence and no resampling. Weakness of this bound for small d is disclosed; it is not a false concentration claim.

The theorem is nonvacuous: for balanced n=2m,k=m, the midpoint expectation is at least m−2, positive for m≥3. As one example of a nontrivial simultaneous bound, n=32,k=16,d=8 gives probability at least 31/64 that every cut satisfies S_r>h_r−8. None of this makes the profile the orbit of repeated powers of a single permutation.

## Controls and limitations

Independent `independent_controls.py` passed **14,924 predicates**, with **2,658 direct state/cut cases** for every binary subspace at n=2,…,5 and every k. It checked the full joint (i,j) distribution, not only the entropy marginal. Reduced-amplitude matrices were directly contracted, independently ranked by exact integer elimination, and checked for the flat-spectrum polynomial identity. Exact distribution/purity/entropy/tail comparisons passed for **104** larger moment cases (all cuts at n=6,8,12,16,24,32 with k=n/2). The independent checker used the Gaussian Pascal recurrence, not the candidate's product implementation. See `independent-results.json`.

The separately replayed candidate produced exactly its retained structured output: **18,837 predicates**, **2,658 state/cut cases**, **35 larger exact moment cases**. See `candidate-replay.json`. Predicate counts are implementation-specific and are not mathematical evidence weights.

The countercontrols are correct and their interpretations appropriately narrow:

- CNOT on |+0> gives the fixed-cut entropy 0→1→0; its two-state cycle average is 1/2 bit. The three uniform one-dimensional subspaces of F₂² instead give entropies 0,0,1, with mean 1/3 and mean purity 5/6. Ensemble and temporal averages differ.
- Every definite configuration remains a product configuration under any configuration permutation. The configuration-state obstruction therefore survives; k=0 does not become an example of positive entanglement.
- The unmixed coherent seed remains product at every coordinate cut, so coherence alone is insufficient.
- Disjoint mirror Bell pairs have the exact nested-cut tent. That static profile alone does not demonstrate scrambling or evaporation.
- A diagonal mixture supported on 00,11 and a Bell state can have the same reduced purity but different global purity. Here reduced entropy measures entanglement because a pure coherent global state is assumed.

The graph counting, uniform-subspace incidence, Schmidt arguments, Jensen, Markov and union bound are established mathematics. The candidate properly declines novelty and distinguishes its restricted positive-amplitude subspace ensemble from both Haar-random pure states and the entire stabilizer ensemble, citing Page and Smith–Leung as context. I did not audit those papers for a novelty or priority claim; none is made or accepted.

## Disposition and forward boundary

No mandatory mathematical revision is identified. Accept this scoped exploratory checkpoint and its written theorem. Keep the coherent preparation, GL ensemble, global purity, entropy definition and same-state nested schedule explicit in every future use. Preserve SC-36 and the Introduction's configuration-state qualifications independently. A physical Page/evaporation theorem, OI-derived measure, local scrambling mechanism or native physical premise would require new evidence and new review. This report supplies no such bridge and does not authorize any manuscript/status promotion.
