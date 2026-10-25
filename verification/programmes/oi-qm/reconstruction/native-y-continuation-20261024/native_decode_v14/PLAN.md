# Native operand decoding v14: redundant q10 readouts of the two-front table

Research only, 24 October 2026. Base #910 is
`94a4e6ccf18845af6c2d37cd797da1082f575d65`. Input is the retained
second-front q10 table of `native_route_v13/`, author
`753fe4f69392ca940754489468e8c8235f6aa583`, whose 4096-row digest
`b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc` was
reproduced by the separate-engine review retained under
`native_route_v13/review/`. No native evolution is recomputed here; the
large-time reduction and geometry are inherited from that reviewed pair.

## Question

`native_route_v13` decided one encoding: a common two-symbol raw q10 code
for the old sign s=x XOR u XOR a, selected by jointly affine known-seed
payloads E(k),N(k), k=(u,mY,mR,a,b), on the 24 accepted contexts
((a,b) other than (0,1)). It found none, and both author and review list an
arbitrary redundant q10 decoder as untested. This plan tests that class.

**Primary question (fixed readout).** Is there a nonconstant Boolean readout
D of the q10 raw triple (any of the 254 nonconstant maps from the eight
codes to {0,1}), common to all 24 accepted contexts, and a jointly affine
source law (E,N)(k)=C(1,u,mY,mR,a,b) with C one of the 2^36 binary 6x6
coefficient matrices, such that

    D(q10(s,k,E(k),N(k))) = s   for s=0,1 and every accepted k?

A raw pair (o0,o1) is the special case of singleton readout classes, so the
primary class strictly contains the one already excluded.

**Diagnostic (known-seed readout).** Is there a jointly affine C with
q10(0,k,E(k),N(k)) different from q10(1,k,E(k),N(k)) for every accepted k?
This allows the readout to depend on the known seeds, which is itself a
nonlinear known-seed computation placed after q10. It is reported, never
counted as a fixed-readout delivery.

## Decision rule

For every nonconstant D, compute the exact number of jointly affine C
satisfying the primary condition by two independently written exact
solvers (A: per-coefficient-field bit-set elimination over 64-element
coefficient sets; B: backtracking over an affine basis of the context
feature vectors with linear determination of the remaining contexts).
The counts must agree for all 254 readouts.

- If every count is zero, the verdict is: no fixed q10 readout, redundant
  or not, decodes s under jointly affine E,N in this geometry.
- If some count is positive, the verdict is: a fixed redundant q10 readout
  with jointly affine E,N exists; the checker retains every readout with a
  positive count, its count and one explicit (D,C), and verifies that
  witness directly against all 48 (s,k) table rows. A positive verdict is
  operand-delivery evidence at one cell only. It is not the acceptance
  predicate, a reusable interface, or a native downstream gate that acts on
  the readout classes.

The diagnostic reports existence and one verified witness, or exhaustion.
No numerical expectation is stated in advance. No float enters any count.

## Controls (all must pass before any verdict text is emitted)

1. **Input pins.** SHA-256 of `native_route_v13/result.json`, its
   `table_sha256` field, a recomputed digest of its table string, and the
   review's independent table digest must all agree with the values above.
2. **Planted positive control.** A synthetic table with a prescribed
   readout D* and full-rank affine C*: both solvers must report C* among
   the solutions of D* (solver A by enumeration, solver B by count and
   membership), and an equal count.
3. **Brute-force control on the real table.** With the affine features
   restricted to (1,u) and to (1,u,a), all 2^12 and 2^18 maps are
   enumerated directly; the per-readout counts must equal both solvers'
   counts under the same restriction.
4. **Reproduction countercontrol.** Using singleton classes ({o0},{o1}) as
   partial readouts for all 56 ordered injective pairs, solver A's number
   of surviving affine E prefixes and of joint maps must equal the
   per-pair counts retained in `native_route_v13/result.json` (16 E maps
   in total over 8 pairs, no joint map).
5. **Sign-erased countercontrol.** The table with the s=1 row replaced by
   the s=0 row must give zero for every readout and for the diagnostic.
6. **Solver agreement.** Solvers A and B agree for all 254 readouts on the
   real table, and on the diagnostic decision.

If any control fails, emit no verdict and record the failure.

## Execution

Standard library only, exact integers. Run `python3 checks.py` and
`python3 -O checks.py`; both outputs must equal result.json byte for byte.
The group joins `replay.py --latest`. Scope remains this geometry and
contract; other layouts, fresh-seed mixers, multi-cell or multi-time
readouts, distribution-level instruments and OI generally are untested by
this plan. No dispatch, push, merge, F/E designation or #885 write.
