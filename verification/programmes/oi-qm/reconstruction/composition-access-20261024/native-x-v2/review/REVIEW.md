# Separate-author native-X contract review

Reviewed author checkpoint: `2390b32977151ac3a954f8332a3db5821152b703`,
`verification/programmes/oi-qm/reconstruction/composition-access-20261024/native-x-v2/`.
Verdict: **accept within the stated algebraic and conditional scope**.
No blocking findings remain. This is internal separate-agent review of an
unmerged research draft, not owner acceptance, external review, a physical
realization proof, or Lean certification.

## Independence and recovered provenance

The reviewer did not author the preceding session's calculation or checker.
Before publication, the reviewer recovered its files, replayed the checks,
and corrected a provenance description: the three calibration assignments
had four leading spaces removed. That removal is now explicit in
`SOURCE-EXCERPTS.json`; candidate functions are verbatim. No mathematical
claim or computational result was changed by that correction.

The complete original `candidate.py` and `checks.py` matched the full hashes
retained in the source-excerpt file. Every cited line span matched, allowing
only the recorded four-space removal. The original report's sections 4–6
support the outgoing encoding, failure convention and terminal-read access
contract used here. The review checked the five substantive published file
blobs against the local replay inputs at the exact checkpoint above. Its
`SHA256SUMS` also covers the README. `INPUT-HASHES.json` pins the author inputs
for future replay; the full original geometry is not required to replay this
scoped algebra and is not thereby independently certified.

## Independent checks and reasoning

The author's normal and optimized executions reproduce `RESULT.json`
byte-for-byte. The independent `review/checks.py` imports no author audit
code. It uses the retained original-source fragments, reconstructs the
source acceptance table and evaluates the native collision directly.

For all twelve incoming carrier points and eight ciphertexts, it enumerates
all fresh seed and pad assignments and verifies the entire offered-carrier
law and terminal failure mass: **96 pointwise branches**. This implies the
same finite kernel identity on the eight calibrated preparations by linearity.
The preparation decoder is checked separately: all eight have unit trace,
unit Bloch norm and the stated reference directions, including R=(4/5,3/5,0).
The X-projector probability is checked for both outcomes on each generator.
The success branch therefore has the required decoded projector output,
as well as the stronger calibrated full-carrier distribution. On a zero-mass
branch the identities hold without normalization or division.

All 32 herald assignments agree with the source predicate. The rejected
(u,v) counts are **3,8,4,7**, in order 00,01,10,11. The source stage has success
mass **5/16** and terminal failure mass **11/16**. These are conditional on a
valid incoming history; they do not replace the predecessor's separate herald.

For the expressly proposed unchanged-sample continuation, the independent
seed enumeration gives equal metadata/later-Y bits, whereas independent fresh
post-X samples give independent fair bits. The joint distance is **1/2**
conditional on success, and **5/32** with the common terminal failure branch
retained. Both one-bit marginals agree. Conditioning the unchanged carrier
on each of the four (x,Y_metadata) combinations gives decoder determinant
**-1/4**. Thus the fixed positive comparison cone is not closed under this
proposal. This does not exclude a different cone/decoder with its own proof,
and it does not contradict the source's explicitly terminal-only claim.

Controls reject a herald-weight swap that preserves total success but changes
the carrier law by TV **1/10**, and removal of the constant collision field.
The independent fresh-sample construction supplies the positive joint-law
control. Independent normal and optimized executions are byte-identical to
`review/result.json`. Every condition uses explicit exceptions rather than
optimization-sensitive assertions.

## Remaining limits

The complete physical boundary includes both time slices, old apparatus and
resource correlations. This finite enumeration certifies neither that boundary's
fit to another apparatus nor the long public-noise/frontier theorem. Those
remain explicitly inherited dependencies. The supplied eight preparations
are a calibration cone, not eight newly constructed native inputs.

Failure is correctly represented as the declared terminal no-carrier symbol;
no post-failure qubit state is invented. The unchanged-sample test is an
extension beyond the source access contract, not a simulation of additional
native ticks. No second reset, full native closure, new access policy,
resource derivation, tensor-product construction or full OI–QM equivalence
follows from this checkpoint.

Reproduce from the `native-x-v2` directory:

```sh
python3 checks.py
python3 -O checks.py
python3 review/checks.py
python3 -O review/checks.py
```

The first pair matches `RESULT.json`; the second matches `review/result.json`.
