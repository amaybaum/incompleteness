# Separate-author review of the operational-quotient checkpoint

Verdict: **accept within its stated scope**, with no blocking findings.

Reviewed author commit: `fb0f799d94b621cdb82a8e06183f07afc070f14c` on #911,
under `operational-quotient-v3/`. All six source files were fetched at that
immutable revision. Their Git blob identities match the local files reviewed;
`INPUT-HASHES.json` pins both Git and SHA-256 identities. This is a separate
agent's internal review, not external validation, kernel certification or
owner adoption of a new operational map.

## Main mathematical claims

The candidate admits every nonnegative eight-sign prior whose first-moment
vector lies in the Bloch octahedron. Its fixed decoder preserves mass and is
positive on that cone. The six uniform Pauli-eigenstate priors map to the
vertices, and their convex mixtures cover the octahedron. This establishes
the stated image in both directions, without implying native preparation.

Under the explicitly supplied kernel/access contract, equality of first
moments is exactly equality of all finite adaptive future-record laws.
For the forward implication, signed-coordinate permutations transform equal
moments equally; a Pauli outcome probability depends only on the appropriate
first moment, and the fresh reset makes the entire outgoing carrier law the
same eigenstate prior on that branch. Induction includes all outcome labels,
gate choices, settings, fixed ticks and the certain-success flag. Zero-mass
branches stay zero without normalization. For the reverse implication, any
unequal first moment is separated by the corresponding permitted Pauli read.

That proof requires the stated full contract: fresh seeds for each use,
initially blank workspace, and no permitted return coupling from spent private
workspace or seeds into later carrier operations. Merely declaring those
registers unreadable would not suffice. The author states this explicitly.
The all-finite-depth result is a written induction for the abstract kernel
family, not a claim that one finite seed bank supports unbounded reuse.

The reversible dilation is globally bijective for every setting, including
nonblank output and record registers. The retained old label, retained seed
and modular subtraction recover the input uniquely. On the stipulated ready
registers it produces exactly the fresh-reset law. This is an abstract
reversible implementation; it is not an implementation under native H.

The positive Hadamard control is valid. A positive permutation of eight
hidden states takes the negative-Z prior to the negative-X prior. Its decoded
off-diagonal entry is -1/2 and its density matrix has determinant zero. Thus
the old fixed pointwise/G3 entrywise invariant cannot automatically be used
after changing the correspondence. The old theorem at its original map is
unchanged. The cited primary paper does describe the eight-sign model and
Hadamard action on PDF pages 2-3; no novelty for this stabilizer model or
universal noncontextuality is claimed.

## Fixed-map operation obstruction

The full preparation-fibre assumption is essential and printed prominently.
The eight allowed priors nu_lambda=(2/3)u+(1/3)delta_lambda average to u and
satisfy delta_lambda=3nu_lambda-2u. Exact linear moment intertwining on these
allowed priors therefore extends to the point vectors as a linear identity;
the proof does not assume the point priors themselves are physically allowed.

A stochastic output kernel on the same eight signs has each output moment
in [-1,1] on every point vector. A unitary Bloch rotation must consequently
send the sign cube into itself. Each row then has l1 norm at most one while
orthogonality gives l2 norm one. Equality in the elementary norm inequality
forces one signed unit entry per row and distinct columns. The proper
rotations are exactly the 24 signed-coordinate Clifford actions. Both the
cube constraint and the norm argument are valid under the stated map, carrier
and full-fibre domain. They are not a classification of arbitrary encodings.

The rational non-Clifford rotation has first row (3/5,-4/5,0). Applied to
(1,-1,1), it gives 7/5 in the first coordinate. Conjugation by the stated
diagonal unitary has exactly this rotation: its off-diagonal multiplier is
(3-4i)/5. The sign and normalization are correct.

The two-preparation record bound is also sound and stronger than merely a
state-coverage observation. The allowed antipodal nu pair has ontic TV 1/3,
while the target rotated-X outcome laws have TV 7/15. Every fixed classical
continuation with the same independent apparatus is a stochastic map on the
complete input and obeys data processing. If both record errors are bounded
by epsilon, triangle inequality gives epsilon at least 1/15. The ordinary
X read attains that pair bound. This proves tightness for this pair/test,
not a minimax theorem for the full channel.

The separate 1/10 bound concerns representing the state (3/5,4/5,0) inside
the octahedron under two Pauli tests. The supporting inequality r_x+r_y<=1
and the attainable point (2/5,3/5,0) give that bound. Enlarging the supplied
domain to all valid-Bloch priors permits a product prior for the missing
state, but retains the problematic nu pair and hence the 1/15 operation/test
bound. The two numbers address different questions and are not combined.

The pair bound remains scoped to the fixed preparations and a common
classical continuation with the specified resource law. Preparation-dependent
hidden apparatus, a changed decoder or a different admissible preparation
section changes the premises. No general OI A1/A2 impossibility follows.

## Independent verification

The author's normal and optimized executions reproduce the retained
`result.json` byte for byte. The separate `checks.py` here imports no author
code and reconstructs exact distributions and kernels with rational arithmetic.
It independently checks:

- 17 admissible priors and 102 Pauli projector branches;
- all 24 proper signed permutations and 120 Fourier-kernel congruence cases;
- all 27 depth-two adaptive axis policies per prior, with conditional H/S
  gates, 1,836 complete leaf records and 396 retained zero-mass leaves;
- all 1,536 global dilation inputs across the three settings;
- no-reset correlation leakage, negative posteriors after altered access,
  and the positive Hadamard/negative-off-diagonal control;
- the eight-prior affine reconstruction, proper rational rotation,
  all 256 deterministic binary response functions, the exact 1/15 pair
  floor and its attainability, and the separate 1/10 state-coverage bound.

The finite branch checks validate these explicit implementations; the full
finite-depth and general orthogonal-rotation conclusions rest on the reviewed
written proofs. All controls pass in normal and optimized review execution,
with byte-identical structured output. No floating arithmetic, external LP
solver, native construction or full repository gate is used.

Primary background checked: Lillystone, Wallman and Emerson,
<https://arxiv.org/pdf/1802.06121v2>, pages 2-3. The new scoped affine-span and
TV claims were re-derived directly rather than imported from that paper.
No manuscript or #885 change is requested by this review. The actionable
next step remains an explicitly changed architecture/preparation contract
with a new full-record congruence and availability proof.
