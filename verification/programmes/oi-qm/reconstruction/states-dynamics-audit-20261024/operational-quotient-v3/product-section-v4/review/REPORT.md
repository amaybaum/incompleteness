# Separate-author review: canonical product preparation section

Verdict: **accept within scope**, with no blocking findings.

Reviewed #911 author `d6966ce055f6f1d872080328023fc37d68d17533`, under
`operational-quotient-v3/product-section-v4/`. All six remote source blobs
match the local reviewed files. Their hashes and the immutable revision are
in `INPUT-HASHES.json`. This is an internal separate-author review, not a
native construction, owner premise adoption, external validation or formal
certificate.

## Product preparations and the exact operator obstruction

For every Bloch vector r, the stated product prior is positive, normalized
and has first moments r. The preparation rule therefore supplies full Bloch
state representability under the fixed eight-sign moment decoder. It does
not establish native availability of those preparations or operations.

The finite span claim is correct without using full preparation fibres or
physical mixture closure. On the eight valid vectors r=(1/3)s, s a sign
triple, the matrix of product priors is invertible. An independent Walsh
diagonalization gives eigenvalues (1/3)^degree for each of the eight Fourier
characters, all nonzero. Their product is (1/3)^12=1/531441. The priors have
minimum atom 1/27 and squared Bloch norm 1/3. Thus all are allowed inputs.

If one stochastic continuation implements the target rotation on these
inputs, multiplication by the inverse preparation matrix extends the linear
intertwining identity to the hidden point-vector basis. The inverse has
negative entries; they are algebraic interpolation coefficients, not an
assertion that point priors or negative mixtures are physically preparable.
Consequently the cube-preservation argument of the predecessor applies.
For proper unitary rotations only the 24 signed-coordinate Clifford actions
can satisfy this fixed-map contract.

An additional independent binary-effect calculation gives the same exact
obstruction without imposing any output-state geometry. Solving for the
common final-X response probabilities required by the eight spanning inputs
gives values ranging from -1/5 to 6/5. A classical binary response must lie
in [0,1]. This is the final-record version of the same linear-span witness;
it does not add an assumption about output hidden states.

The rational rotation and its unitary control have the correct sign. The
off-diagonal conjugation multiplier from diag(2-i,2+i)/sqrt(5) is (3-4i)/5,
which yields r'_x=(3r_x-4r_y)/5 and r'_y=(4r_x+3r_y)/5. A sign-cube vertex
(1,-1,1) has target first coordinate 7/5. The fixed map, carrier, input
section and common-kernel assumptions are essential to these conclusions.

## New approximation pair and its exact scope

For the two new Bloch vectors plus/minus (2/3,-2/3,0), the product priors in
the report are correct. They have squared Bloch norm 8/9 and positive atoms
at least 1/72. Their l1 Bloch norm is 4/3, so this pair lies outside the
predecessor's octahedral input region.

The source pair TV is 2/3. Rotation followed by X produces probabilities
(29/30,1/30) and its reverse, with TV 14/15. Data processing for a common
classical continuation, followed by triangle inequality for the two errors,
gives worst-pair record error at least 2/15. The ordinary X sign read
attains this value. All 256 deterministic binary responses independently
confirm the bound and its attainability; six attain the optimum in this
reviewer's outcome convention. Stochastic responses cannot beat it because
the data-processing lower bound already covers them.

This proves a sharp two-preparation binary-record bound. It does not claim
the full-channel minimax error or exclude a different input encoding. The
bound remains valid with arbitrary extra classical output memory and a
different output-state region, since only contraction of distinguishability
in the common complete-input kernel is used.

The earlier 1/15 pair bound, the earlier 1/10 octahedral state-coverage bound
and this 2/15 pair bound use different questions and domains. The report
keeps them separate. The present span result needs only eight product inputs;
the larger new pair gives the stated quantitative control. No universal OI
or A2 error floor is inferred.

## Mixtures, resources and positive controls

The equal forgotten mixture of the new product pair has zero first moments
but xy correlation -4/9. The canonical product prior at zero moments is
uniform with zero xy correlation. Thus the product section is nonconvex.
Physical mixture closure contains more hidden fibres for the same decoded
state; replacing them by the canonical product prior would need an actual
future-kernel congruence proof. The predecessor's Pauli/Clifford/fresh-reset
contract does provide that restricted congruence. Adding mixtures cannot
remove inputs already used by the span and pair arguments.

The preparation-dependent controller is an appropriate positive control.
A supplied input label and uniform 30-valued seed produce the two requested
binary laws exactly, but the complete labeled input distributions have TV
one. They no longer satisfy the common unknown-carrier channel premise.
The report explicitly supplies the seed and makes no claim that it is an
always-success finite-fair-bit or native source. Additional preparation-
dependent private memory would likewise have to be counted in the complete
input law if it can affect the record. Its omission cannot be used to apply
the smaller carrier-only TV bound to a different physical architecture.

The signed-permutation Clifford product controls remain positive, and Pauli
eigenstate resets return product priors. Thus the negative result is not an
artifact of forbidding every operation or losing the supplied full state
representation. No extra herald, discarded failures or completion-time
postselection enters this binary-record test.

## Verification

The author normal and optimized runs match the retained `result.json`
byte for byte. The independent standard-library checker here imports no
author or predecessor engine. It verifies the 64-entry spectral certificate,
an explicit inverse and affine reconstruction, the forbidden binary response,
the exact pair, all 256 binary responses, 20 Clifford product closures,
mixture correlation and the label-dependent positive control. Rational
Gaussian-integer off-diagonal calculations check the target rotation on ten
input vectors. Normal and optimized review outputs are byte-identical.

The written general arguments were reviewed separately from these bounded
controls. No Lean build, full repository gate, native simulation, premise
adoption, new observer access, dispatch, merge or #885 edit is supplied.
The next architecture must explicitly change its encoding, preparation or
resource/continuation contract and re-establish full-record congruence and
availability. The current native #910 encoding is outside this audit's
fixed eight-sign representation.
