# Separate-author review of the finite branching-control reduction

**Verdict: accept within the stated finite-table scope; no blocking findings.**

Reviewed author revision: `a523daede14f1f92bb364f572f77e4724b6b2a36`,
`branch_v10/` on #910. The reviewer did not author its checker or report.
This is internal separate-agent review, not a native realization, owner
adoption, external validation or Lean certificate.

## Provenance and replay

The six author files were fetched at the immutable revision above and their
Git blob identities matched the reviewed local bytes. The published
reset_v9/result.json blob is `89c9de73f2d43fcec6c348e33329c4a1c86fb8de`;
its SHA-256 is `4bddbbeec267c831f31d8d578e9768e18f64c1319388bf9512563cae35aa6ac4`.
This is the actual native table used by both author and reviewer.
INPUT-HASHES.json pins the input identities. The author manifest and normal
and optimized replays pass with byte-identical result.json.

The independent checker imports no author module. It uses the native table
as already-reviewed physical input; it does not claim a new simulation of
that table's lattice dynamics. Its enumeration represents each affine source
component by its own four coefficient bits for 1,u,a,b, independently of
the author's three-bit-vector enumeration.

## Findings

1. All 4,096 affine maps are covered. Exactly 32 make every mask's raw q9
   pair common across the old u values. The accepted-only requirement
   on 00,10,11 also admits 32 common maps, but none has three distinct codes
   for either y. The maximum accepted-mask capacity is two. Every fixed
   x,u map J to q9 is bijective. The eight common J pairs fall into four
   u-coefficient groups with two pairs each, confirming the structural
   capacity proof.
2. The unique J table for q9=(0,y XOR a,y XOR b) is reproduced for every
   u,a,b. The three displayed algebraic-normal-form expressions agree on
   all eight inputs. Independent parity-over-subcubes reconstruction gives
   exactly the reported monomials and degree three. On the six inputs with
   (a,b) in 00,10,11, the displayed quadratic extension agrees exactly.
   This is a required truth table, not an available nonlinear initial
   preparation or a native seed processor. The extension does assign
   mathematical values on mask01, but no physical failure law is inferred
   from those values or adopted.
3. The existing one-mask J=(u XOR a,a,u XOR a) is an effective positive
   control and works on every x,u,a. The source's previously reviewed
   selector-mask independence, together with J-to-output injectivity,
   supports the statement that adding old-mask affine coefficients cannot
   help a raw output required to be independent of those masks. This
   conclusion inherits that physical table property; it is not a claim
   about a larger multi-source circuit.
4. The q8 value at R+8 belongs to the previous slice of the R+9 physical
   phase. Its availability in that mathematical boundary is distinct from
   a same-current-slice Y port or permitted observer readout. The report
   states this distinction and does not declare previous-field access.
5. The shallow A/B/C control-source distances are N to the owned target
   and N+2 to the others. The positive-x alternative violates the named
   old ready ball by 401. At A, the R selector source and its first two
   frontier coordinates arrive at N-2,N-1,N. At B, both origin and W
   arrive at N-2. These exact distances independently confirm that the
   existing first-front initializer cannot be reused. Source separation
   alone does not authorize blanking new ready cones, pinning existing
   frontier variables, or discarding coupled histories. The report leaves
   those spatial branches unconstructed, as required.

The negative result is restricted to the stated single affine J-source
family and full raw-code condition. Native nonlinear processing of initially
affine sources, a larger controller and a separately justified interface
remain open. No simultaneous calibrated X/Y/R/z carrier, success selector,
failure law, joint public-record proof or full reset follows from this audit.

## Review evidence and replay

The independent exact checker verifies the affine census, common-group
bound, one-mask positive control, unique truth table, full ANF, quadratic
success extension and critical fork geometry. Normal and optimized outputs
are byte-identical to result.json. All controls use explicit exceptions.

From `branch_v10/review/` in the published layout:

```sh
python3 checks.py > replay.json
python3 -O checks.py > replay-O.json
cmp result.json replay.json
cmp result.json replay-O.json
sha256sum -c SHA256SUMS
```

`--source-root PATH` optionally names the containing checkpoint directory;
the sole physical input remains the pinned sibling reset_v9/result.json.
The checker needs only Python's standard library. #885, frozen records,
physical premises and acceptance criteria are unchanged.
