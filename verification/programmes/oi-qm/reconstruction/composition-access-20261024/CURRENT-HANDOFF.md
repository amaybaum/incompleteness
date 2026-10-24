# Composition/access: current research handoff

24 October 2026. #912 is a research draft. No changed observer access,
tagged-interface extension, native reset or equivalence verdict is adopted.
The programme source on #885 remains read-only for this effort.

## Current reviewed checkpoint

Author `5b77352f50ddfe750b1cf5cbc72ebdded046df31`,
`native-phase-v4/REPORT.md`; separate-author internal review retained at
`be3840081fb40fe991660fb394b262c8b1a1b89e`. The review accepts the scoped
local controls and conditional contract, with no outstanding blockers.

The actual prepared phase has previous q8=(0,y,0), current q9=(0,X,R),
and a current remote Z field. At the next tick the whole q8 response depends
on the XOR C of its five other current neighbors:

    U_(L+1)(q8)=(C_B XOR X, y XOR C_D XOR R,
                 C_A XOR ((C_B XOR X)(C_D XOR R))).

Selected-coordinate agreement therefore does not determine the next raw
response on an unrestricted local boundary cone. A C_A flip gives next-record
TV 1 on success, or 5/16 including the unchanged terminal failures. More
strongly, a fresh versus correlated C_A can match the entire next public
record while the joint next-record/retained-Z law differs by TV 1/2 on
success, or 5/32 with the same failures.

These are local mathematical controls, not claims that both completions
arise from the retained original-time source family or that the additional
q8 read is already permitted. The native #910 continuation separately audits
actual original-time degrees of freedom. Unequal hidden completions with
equal response-relevant parity give the same one-step output; hidden-state
identity is stronger than this horizon requires.

## Fixed composition contract and next test

Use one operational equivalence relation on full two-slice measures: equality
of all permitted finite adaptive complete future-record laws, retaining
timing, raw fields, initial public history, heralds and terminal failures.
For a decoder-based sufficient contract, specify the admissible boundary
cone, branchwise positivity, closure and complete-record instrument
intertwining. Equality of selected moments is insufficient unless its kernel
is preserved by every actual continuation.

The next native X instrument must accept the actual boundary conditional on
the whole q9 record and old history, restore a valid X post-measurement
carrier, and retain every new record and failure in its joint law. Any fresh
pool must have the required joint law with the incoming response variables;
freshness against public history alone can miss the new countercontrol.
An abstract fresh reset is a positive reference, not a native implementation.

## Validation and retained work

Author and independent review normal/optimized outputs match their retained
structured results. The review reconstructs all four fixed old_x/y contexts,
5,120 native responses, 4,096 equal-parity cases and the complete post-X
reference law. It imports no author engine. Written all-depth conclusions
remain conditional on the specified kernel/access contract.

The earlier conditional composition theorem, native-X audit and strict
raw-tag obstruction at `69540662b234e37c6805ded244962a80f15f63a2` remain
unchanged. They are not relaxed by the new diagnostic. #910 owns native
implementation and full future-history geometry; #911 owns operational-map
and state/operation coverage. Broader inactive gates and activation conditions
are recorded in [#913](https://github.com/amaybaum/incompleteness/issues/913).
No full suite, Lean certificate, exact-head attestation, merge or special
workflow launch is claimed.
