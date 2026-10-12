# OI-CHANNEL-1 audit result

Outcome: OI-CHANNEL-1-READ

Evidence classes: [X] denotes an exact saved computation, [W] a written argument,
and [D] disposable design validation. This package adds no Lean theorem or new
reconstruction premise. Its preregistration remains byte-identical to F.

## Earned reading

The finite stopped circuit realizes the channel formula at depths 0 through 6 by exact arithmetic. The all-depth recurrence and the universal cone arguments are written proofs. Transfer to an arbitrary pair cone and the general-k InstAvail witness remain additional obligations. This audit does not establish unconditional quantum reconstruction or full-model independence.

## Exact execution checkpoint [X]

The native controls passed at S1 2d870fc508cbf2d0f74d7681a8546a694eaef92b:
exit 0, empty stderr, all 17 groups PASS. TOKEN covers 28 matrix-unit cases and
PAIR 112 at depths 0 through 6. DICT separately covers 112 Pauli table cases;
J covers 16. The five countercontrols reject omitted correction, the wrong
success outcome, missing reset, identity and a target Clifford action in the
stated constructions. The controls' positive fixture and all 11 mutations pass.

CHANNEL-CHECK: PASS; 17 checks; 140 matrix-unit cases

The checker stdout SHA256, excluding the native controls' own prefix, is
`ec73839a23e1c2e051140ff9b56d47bbda4f9b55e37963ca1256500b36642da5`.
The original design run and replay were byte-identical. The probe, controls and
workflow have the exact SHA256 values in the preregistration; the unchanged
kernel-source check and all five workflow splices pass the native controls.

ZF's normalized matrix-trace witnesses are -1/10 for the drive and -1/8 for
the mixer. These values are matrix traces. Under the Pauli dictionary the
unscaled table inner product is four times the matrix trace; the trace
normalization is kept explicit.

The cone for ZF is the historical
`K(Z_F) = (Q3 intersect Z_F*) + cone(Z_F)`, recorded in
[R6 NOTES, N2](https://github.com/amaybaum/incompleteness/blob/e7d380fcb9881e3063243aaa149e85be3cd0a914/research/archive/pt/R6/NOTES.md)
and used by [B4's realization, sections 1 and 2](https://github.com/amaybaum/incompleteness/blob/5f4089a4500a59943c33ba13656b2530824068c5/research/bridge/NOTES-B4.md).
Under the Pauli dictionary this cone is contained in the sum of the PSD cone
and the conic hull of the four defect matrices used by ZF. A PSD test has
nonnegative trace pairing with every PSD matrix; if it also has nonnegative
pairing with each defect, linearity gives nonnegative pairing with every
element of that sum and hence with all of K(Z_F). This sufficiency argument
is [W]; ZF's exact rank-one tests and four generator inequalities are [X].
B4's realization retains its conditional branch-(a) scope; this citation
does not extend it to the unreached inventory rows.

## Provenance and certification boundary

- D: `9f9f8257a980a1819fbbc1dc0019917cf8678626`.
- F: `a5aad0c1c52df963f8d1365479e4c6f1a0305de0`.
- Owner-designation F: recorded in S1's commit message and PR #808's description,
  from the owner's in-session approval on 2026-10-11T19:15:22Z.
- F check-run: [verify #1891](https://github.com/amaybaum/incompleteness/actions/runs/38164920166),
  workflow_dispatch at F, attempt 1, all 33 jobs successful.
- Frozen sources and original exact evidence: `e7d380fcb9881e3063243aaa149e85be3cd0a914`,
  `research/round7-channel/`; prospective registration:
  `78aa5b25415cf1cd26994cb2280343ab86cd72d9`.
- Written-argument source: `research/round7-channel/ARGUMENT.md` at that frozen
  research source. Its mathematical arguments are restated below with their
  evidence classes retained.
- S1: `2d870fc508cbf2d0f74d7681a8546a694eaef92b`, one linear child of F,
  adding the three frozen files. Its PR-triggered CI is a stage checkpoint,
  and is not used as an F or E exact-head attestation.
- S1 stage CI: [verify #1892](https://github.com/amaybaum/incompleteness/actions/runs/38167557092),
  pull_request event at S1, 19 jobs successful and the A42 exclusion matrix
  intentionally skipped. The OI channel job passes its exact 17-group,
  140-case checker and the controls' positive fixture plus 11 mutations.
- E's exact-head check-run and owner designation must be recorded on the host
  and in the later native receipt. This result note precedes those events;
  it does not infer them from a pull-request run.

Separate [D] evidence: the ComplexOrder scope repair at
`13ad14a1ba2973245354aea7790c021d946b1ff0`, PR #807, built successfully in
[run 38162504147](https://github.com/amaybaum/incompleteness/actions/runs/38162504147),
Mathlib job 114538184326. Its seven BridgeChannelTransfer axiom reports use
only propext, Classical.choice and Quot.sound. The 6136-result axiom census
passed with no sorryAx; the release gate failed on 12 missing design-module
manuscript dispositions. No design Lean module is imported by this audit.

The historical inventory's 118 reached rows, 13 FAILS rows and 68 NOT REACHED
rows remain distinct. The 68 unreached rows are unresolved. The expanded
block cone below fails the maxCone product-effect bound and is not a full OI
countermodel. The transfer premise, pair self-duality and general-k formal
availability remain additional obligations; no source of these premises is
adopted by this package.

I4.38 derives the PSD-validity reading from implementation locality. Extending
I4.66 to a pair state space also requires the operational context and label
premises for the spectator step, in addition to validity on the identified
space. Those premises are retained as obligations.

## Written arguments [W] and finite witnesses [X]

Evidence: `channel_check.py`, run 1 and byte-identical replay, 17 checks PASS.
The computations below are [X]; arguments over all depths or all inputs are [W].
None constructs a Lean `InstAvail` witness. The class membership of each primitive
must still be supplied by the operational model when using this circuit as an
availability witness.

### Finite stopped protocols

Use data register a and ancillas b,c, prepared in 00. Hadamard acts on the
ancillas, Toffoli flips a when bc=11, and S=diag(1,i) acts on a. The circuit is
`(I tensor H tensor H) Toffoli (S tensor I tensor I) Toffoli (I tensor H tensor H)`.
The checker uses unnormalized Hadamard matrices and divides the final matrix by
4, so every entry is Gaussian rational; U checks its unitarity independently.

Readout followed by conditional bit flips prepares 00 from the uniformly
attached four-state ancilla: the reset Kraus maps are |00><j|, j=00,01,10,11.
Their action on I/4 sums to |00><00|. RESET checks this step; attachment alone
does not prepare the circuit's input, as CC-RESET verifies.

The successful branch is ((3+i)/4) D, with D=diag(1,(3+4i)/5), and has weight
5/8. Each other branch has weight 1/8 and is proportional to Z; applying Z
after failure restores the data, up to a scalar. BRANCH and TP check all four
matrices and their normalization. CC-Z and CC-OUTCOME reject omitted correction
and mistaking a failure outcome for success.

Let S0=(5/8) Ad(D) and F0=(3/8) id be the success and corrected-failure maps.
The protocol stops at its first success, or returns the corrected data after k
failures. Its recurrence is Phi_0=id and Phi_(k+1)=S0+Phi_k composed with F0.
Induction therefore gives, for every integer k>=0,

`Phi_k=(1-(3/8)^k) Ad(D)+(3/8)^k id`.

The saved computation rebuilds this recurrence from the branch matrices,
independently of the formula, on all matrix units for k=0,...,6: TOKEN has 28
cases and PAIR has 112. DICT checks the Pauli dictionary separately; J checks
the mixer and its cyclic action. This protocol differs from unconditionally
composing Phi_1 with itself: that would apply D again after success.

All finite protocols use only attachment, reset/readout and feed-forward,
available primitive unitaries, composition, coarse-graining and discard. This
is a written construction in the `InstAvail` vocabulary; the general-k Lean
witness remains OPEN. Finite exact checks do not discharge that obligation.

### The limit and its transfer premise

The failure weight tends to zero, so Phi_k tends pointwise to Ad(D). If K is
closed and every transferred Phi_k preserves K, its limit preserves K: for
each omega in K, the convergent images stay in K. Availability of the limit is
not used. Conversely, if K is convex and Ad(D) preserves K, each Phi_k
preserves K by its displayed convex combination with the identity. These two
written implications show that requiring this specific sequence to preserve
a closed convex K has exactly the same invariance content as requiring D to
preserve it. Each direction is a written proof [W]; this audit adds no Lean theorem for the equivalence.

The broader transfer clause for every available channel is a separate premise.
I4.66 at main 9f9f8257 quantifies over PSD matrix states. To apply it to K one
needs the identification of a pair state space C with dict '' K and validity
on C. If C is the PSD state space, the identification is K=Q3, the conclusion.
The limit route therefore does not supply an independent source of transfer.

### Cone controls

OCT uses K_oct={omega: omega b lies in the Lorentz cone for every b=(1,+/-e_i)}.
It is closed and convex, contains every product of Lorentz-cone vectors, and
is invariant under target proper signed permutations, which permute the six
tests. The finite test permutation check exhausts all 24 such rotations.
The table e0 tensor (1,1,1,1) belongs. Phi_1 maps its target spatial vector to
(1/4,5/4,1); pairing with (1,0,-1,0) gives -1/4, outside K_oct. Thus these 24
unitary actions and the transferred Phi_1 have different preservation content.
This control alone does not classify every available unitary with arbitrary
dilations in MixR.

OPEN uses the cone over the open unit disc plus its boundary point (1,0),
embedded in span{e00,e01,e02}, with its apex included. This is a convex cone
and is not closed. For p=(3/8)^k, k>=1, the target-plane map has squared norm
factor 1-(4/5)p(1-p)<1, so it sends the distinguished boundary point and every
interior point into the disc. Phi_0 is the identity. The limiting image of
(1,0) is (3/5,4/5), a different boundary point, excluded from the cone.
The scope is the sequence Phi_k; preservation by every available channel is
not asserted. Closedness cannot be removed from this limit argument.

KAPPA uses block matrices [[A,B],[B*,D0]] with A,D0 PSD and
||B||_1 <= kappa sqrt(tr(A) tr(D0)), kappa>1. The constraint is closed and
convex: the geometric mean is concave on nonnegative arguments, while the
trace norm is convex. Every product PSD matrix obeys it because positivity of
the first token gives |r01|<=sqrt(r00 r11). CNOT controlled on the first token
sends D0 to X D0 X and B to B X, preserving the traces and trace norm.
Every target CPTP channel preserves it. To see the trace-norm contraction,
write B=sum_s b_s |u_s><v_s| by singular-value decomposition and a Kraus
channel Phi(B)=sum_j K_j B K_j*. The triangle inequality and Cauchy-Schwarz
give ||Phi(B)||_1 <= sum_s b_s sqrt(sum_j||K_j u_s||^2 sum_j||K_j v_s||^2)
=sum_s b_s, since sum_j K_j* K_j=I. The diagonal block traces are retained.

For kappa=3/2 the members X_+ and X_- have A=D0=I/2 and B=+/-3I/4.
Their trace pairing is 1-kappa^2=-5/4, so the cone cannot be self-dual.
X_+ has a PSD quadratic test value 1-kappa=-1/2 on |00>-|10>, so it strictly
contains Q3. KAPPA checks both exact witnesses. Thus closedness, products,
CNOT invariance and all target-channel invariance do not by themselves give
self-duality. The universal statements here are [W], not Lean proofs.

This quadratic test is a product vector, so the expanded cone also violates
the maxCone product-effect upper bound. It is a control for the listed H1,
H2 and target-channel hypotheses, not a full OI countermodel. A possible
replacement of H3 by cone structure and maxCone, given H2 and A_miss, requires
a separate argument: the dual cone inherits the inverse unitary actions,
contains the product tests, and the pure-orbit result can then constrain both
cones. That question is proposed for the next conditional-pair proof; no
kernel claim for that replacement is made in this batch.

### Remaining reconstruction work

Source the transfer premise, source pair self-duality, and formalize the
general finite-protocol availability witness. Full-model independence remains
OPEN because the 68 NOT REACHED inventory rows are unresolved. Subsequent
milestones are elementary-token geometry, the conditional pair theorem,
arbitrary finite composites and operation/measurement equivalence. No result
here proves unconditional OI implies quantum mechanics.
