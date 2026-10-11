# Round 7 — channel protocol and transfer controls

Status: prospective research batch, authorized by the owner's instruction to proceed on 2026-10-11.
This takes up the round-6 deferrals without reopening or spending its one-build budget.
Source heads: main 9f9f8257a980a1819fbbc1dc0019917cf8678626; overview
5d3ccb3e737ded9dfccaabacc3ee901312cf5b20; round-6 record
694219a43bc9af449784c2b4dbc5b38b44df96a2; failed design fd3640202f4b8abdf8d64ff82434eb10d3d18f5c.

## Scope and prior evidence

The preceding review independently rebuilt the RUS circuit and checked depths 0 through 6.
Those exploratory checks are prior evidence, not blind predictions of this batch.
This batch supplies a saved, reproducible checker, the deferred cone controls, a written
all-depth recurrence, and the one-line ComplexOrder repair. It does not derive a transfer
premise or self-duality from OI, construct a full-model counterexample, or certify a Lean
InstAvail witness.

## Decision rule before the first saved run

The checker uses Gaussian rational arithmetic only, no third-party package and no thread
checker. It rebuilds the eight-dimensional circuit, its readout branches, reset and
dictionary directly. Depths are fixed at k = 0,1,2,3,4,5,6. Every positive check below must
pass and every countercontrol must reject the claimed identity; otherwise the verdict is
VOID, with the failed run retained. A replacement checker requires an amendment naming
the defect before the next run.

| check | expected result | checkpoint |
|---|---|---|
| U: raw circuit with four Hadamard normalizations | unitary | U |
| RESET: readout and conditional flips applied to a uniform four-state ancilla | pure 00, trace retained | RESET |
| BRANCH: success and three corrected failures | weights 5/8 and 1/8 each; failures scalar identity | BRANCH |
| TP: sum of branch adjoint products | identity | TP |
| TOKEN: stopped recurrence on all four matrix units, all seven depths | analytic channel formula | TOKEN |
| PAIR: spectator recurrence on all sixteen pair matrix units, all seven depths | analytic channel formula | PAIR |
| DICT: transferred channel on sixteen Pauli table generators | idle first token and contracted target rotation | DICT |
| J: exact mixer and all sixteen dictionary generators | unitary; cyclic target action | J |
| ZF: independently rebuilt defect rays and positive dual tests | minimum drive -1/10; mixer -1/8 | ZF |
| OCT: six octahedral tests and 24 proper signed permutations | input belongs; Phi_1 input fails at -1/4; permutations preserve test set | OCT |
| OPEN: open-disc cone plus one boundary ray | finite images interior, limiting image excluded | OPEN |
| KAPPA: explicit expanded block cone, kappa=3/2 | two members pair to -5/4 and one fails PSD | KAPPA |
| CC-Z: omit correction | claimed depth-one channel identity false | CC-Z |
| CC-OUTCOME: choose a failure as success | claimed success weight false | CC-OUTCOME |
| CC-RESET: replace pure preparation by uniform attachment alone | claimed depth-one channel identity false | CC-RESET |
| CC-ID: identity in the defect-cone witness search | no negative pairing | CC-ID |
| CC-CLIFFORD: target X in the same search | no negative pairing | CC-CLIFFORD |

Finite calculations do not prove invariance over an infinite family. The accompanying
written argument supplies the all-depth recurrence, the open-disc contraction, convexity
and local-channel invariance of the expanded block cone, explicitly at [W].
The octahedral control establishes the stated 24-action comparison; no stronger claim
about every dilation in MixR is inferred from it.

## Lean repair and budget

The new disposable branch starts at fd364020. Its only Lean change is
`open scoped Topology` to `open scoped Topology ComplexOrder`.
One pull-request-triggered design build is permitted for that repair. Expected: Build
succeeds, all seven BridgeChannelTransfer axiom reports omit sorryAx; release gate remains
red at the existing undispositioned design modules. A synthetic merge run is design
evidence, never an exact-head F or E attestation. No rerun or further build is authorized
by this batch's budget; a failure is retained and named.

The subsequent main PR is a native V3 audit round, drafted from main with a frozen scope,
separate from these research branches. F and E require the owner's exact-commit
designations and exact-head all-green workflow attestations under AGENTS.md section A.39.
