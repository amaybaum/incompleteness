# Finite protocol design results

This is the successor to #807's completed one-line repair, not a change to that record.
Its draft PR is #810 and its prospective rules are in PROTOCOL.md.

## Exact protocol controls

Gaussian-rational computation: ten of ten required groups pass, including the actual
maximally mixed attachment, its readout/conditional-permutation reset, the circuit
word/table identity, corrected branches, and 36 stopped matrix-unit cases at depths 0–8.
Removing reset, removing failure correction or continuing after success each fails the
intended channel identity on the 0,1 matrix unit. Two saved runs return exit zero,
empty stderr and byte-identical stdout, SHA256
f33e3c97bd1baa7f4b583f798cf0ecdec185860d37f69523f31128e4131d35e1.
This is finite exact evidence [X], not a Lean proof of the general depth statement.

## Design run 1

Head: 5e57fb740496e6e851e1fcc0da13ef392016a9cf.
Run: 38207454267, pull_request, attempt 1.
Mathlib bridge job: 114673991060; Build failed, 05:20:07Z–05:23:01Z.
Release gate skipped, so the forecast thirteen-module census failure was not tested.
The initial head supplies no built design result.

Reported causes: Matrix.diagonal_conjTranspose had been written in the wrong word order;
tensorOf_apply had a wrong namespace; the closed form retained an if-True term; reset and
the finite gate table needed further scalar/star-of-numeral simplification; the branch
calculation exceeded the default 200000 heartbeats; the three-failure sum needed its
linear-map scalar sum normalized before entrywise simplification. The constructor proofs
elaborated, but this failed Build certifies no theorem. Failed source and logs remain at
the immutable first head and job.

## Prospective run-2 correction

Proof corrections only: use the actual library lemma names, normalize numerals under
conjugation, simplify the scalar sums and the pure-reset symmetry, and give the finite
branch calculation 2000000 heartbeats. Statements, primitive availability inputs,
protocol constructors, exact checker and its decision rules are unchanged.
Require the original fourteen standard axiom reports and a successful Build. Only start
this fresh-head run after the first complete workflow finishes. The budget remains three
sequential design runs; none is a native F/E attestation.

## Remaining sources

Primitive memberships of the finite balanced circuit, reset permutations and corrections
remain explicit. Their derivation in MixR {pi/4} is not claimed here. The constructed
finite availability is distinct from an available limiting drive and from preservation
of an arbitrary identified pair cone. A later channel-limit use on such a cone requires
that cone's channel-transfer premise and closedness. The exact full-flow maxCone theorem
does not need closedness; this approximation route has that separate obligation.
