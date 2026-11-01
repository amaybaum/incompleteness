# Separate-author review of the tagged post-Y contract

**Verdict: ACCEPT within the stated algebraic scope; no blocking findings.**

Reviewed author revision: `75619cb724053a68196896181878b5c823f9796c` on #912,
under `verification/programmes/oi-qm/reconstruction/composition-access-20261024/tagged-post-y-v3/`.
This is separate-agent internal review. The reviewer did not author the
candidate report or checker. It is not external validation, a new native
construction, an interface adoption, or owner certification.

## Source and replay

The five published author files were fetched at that immutable revision;
their Git blob identities match the local snapshot. The author's manifest
passes, and normal and optimized Python reproduce result.json byte for byte.
INPUT-HASHES.json records the reviewed inputs.

The direct-Y source REPORT.md and checks.py were read at #910 revision
`f264dff4eacae84959b4a4419be204fb8c31c9e3`. Their blob identities are exactly
`8ad5e46694eb4bd0d20794946f255139f81fa650` and
`4f5f19714bffc78921c8cef5ebf93171525959cd`, as cited by the author.
The source states the mixer, the supplied 5:3:2 acceptance law, public-history
tag, whole-cell terminal record and terminal failure convention. It also
explicitly leaves the actual late-time splice and strict common raw encoding
unsatisfied. The new report preserves those boundaries. This review does
not rerun or reprove the source's large native geometry or compiler.

## Accepted claims

- E_g is a fixed injective embedding of the calibrated carrier with tag g;
  the extraction does not change with public history. The global classical
  record/quantum carrier map has the same extraction on every history block.
  Its positivity claim is restricted to the generated preparation cone,
  not all ontic point masses. Keeping original x,y in the record and retaining
  g=x*y under the abstract resampling extension prevents a silent change of
  decoder after later reads.
- The source's conditional success law is exactly the Y-calibrated six-point
  ensemble with plane ratio 5:3:2 and independent fair z. The probability
  5/16 and terminal failure mass 11/16 agree with the source. The strict
  raw-history TV=1 obstruction survives; fixed global comparison is an
  alternative mathematical interface, not compliance with the unchanged
  strict raw encoding rule.
- Under unchanged-sample reuse, the normalized decoder determinants are
  0 after Y, -1/4 after X or Z, -1/64 after R=y, and -1/4 after R differs
  from y. For R=y the normalized X mean is (-1)^y/4. These are exact
  positive-cone failures for that proposed continuation, not failures of
  the existing terminal-only source claim.
- Independent calibrated resampling supplies a valid abstract reset kernel.
  The complete raw port and retained old history accompany the new output.
  Each of its 28 nonzero history/axis/outcome branches agrees with the
  corresponding projective qubit reset. Zero-probability repeated-Y branches
  are omitted from the count, not renormalized into nonzero branches.
- The minimal future-law equation is explicitly an obligation. It is not
  asserted to hold on arbitrary native boundaries. The report keeps the
  entire two-slice boundary, conditional resources, exposed prefixes and
  failures in scope and does not silently concatenate separately ready
  apparatuses. Neither a native reset nor A1/A2 equivalence follows.

## Independent controls

The accompanying checks.py imports no author module. It enumerates the
source's 256 seed assignments using the mixer, checks all 24 carrier/tag
codes for injectivity, and derives the source law. It reconstructs all
28 raw-record/fresh-carrier branches and verifies their decoded operators
against explicit 2-by-2 projector matrix products using rational real and
imaginary components. This avoids using only the desired Bloch-vector
formula as a positive control. It also verifies all posterior determinants,
the strict raw-history separation and the swapped-calibration discrepancy.

The author's final old-seed assertion is an algebraic identity, rather than
a complete reuse simulation. It is nevertheless a sufficient written
witness when combined with its already-verified fair post-Y X target:
u_old=x XOR y forces X_new=x. The review independently enumerates the
actual herald with this reused u and fresh v,K,z. In each of four histories,
success remains 5/16, the conditional X distribution is deterministic,
its TV distance from the required fair X is 1/2, and the distance including
the shared terminal failure is 5/32. Thus this control is substantive and
does not require an author correction.

Normal and optimized reviewer runs are byte-identical, with structured
verdict PASS. Every required control raises explicitly on failure. No
floating-point approximation or new Lean theorem is used.

## Replay

From this review directory:

```sh
python3 checks.py > replay.json
python3 -O checks.py > replay-O.json
cmp result.json replay.json
cmp result.json replay-O.json
sha256sum -c SHA256SUMS
```

The review requires only Python's standard library. It changes no repository
premise, manuscript claim, frozen record or #885 content. Native preparation,
physical memory/readback, dynamic tag insensitivity, the actual q8 splice,
and the full joint public-history law remain open.
