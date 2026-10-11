# Round-7 channel results

Preregistration committed before the first saved run at 78aa5b25415cf1cd26994cb2280343ab86cd72d9.
Run 1: channel_check.py, exit 0, all 17 checks PASS; stdout byte-identical on replay and both stderr files empty.
The 140 matrix-unit cases comprise 28 token cases and 112 pair cases at depths 0 through 6.
DICT separately checks 112 Pauli cases; J checks 16. Five countercontrols discriminate
omitted correction, wrong success outcome, missing reset, identity, and a target Clifford action.

| result | evidence | remaining scope |
|---|---|---|
| stopped RUS channel formula | [X] finite depths; [W] all-depth induction in ARGUMENT.md | general-k InstAvail Lean witness OPEN |
| transfer of the limit | [W], [D] conditional bridge module after repair | arbitrary-cone transfer is introduced; exact availability of D is not inferred |
| 24 Clifford actions versus Phi_1 | [X] OCT and [W] cone construction | arbitrary dilation-generated unitary classification not established |
| closedness in the limit step | [X] OPEN and [W] contraction argument | the example covers the sequence, not every available channel |
| closedness, H1, H2 and target-channel invariance versus H3 | [X] KAPPA, [W] block-cone argument | this cone fails maxCone product positivity; not a full OI countermodel |
| full-class defect-cone control | [X] ZF: trace pairings -1/10 and -1/8 | normalized trace witnesses, not a claim of full-model independence |
| ComplexOrder repair | [D] Build successful, seven standard axiom reports | design module; no census disposition or main certification |

Design source 13ad14a1ba2973245354aea7790c021d946b1ff0 changes one line from fd364020.
PR 807 targets dev-bridge/r6-channel-transfer. Run 38162504147, Mathlib job 114538184326:
Build successful 18:08:14Z–18:11:08Z; Release gate failed 18:11:08Z–18:11:55Z.
All seven BridgeChannelTransfer reports list only propext, Classical.choice and Quot.sound.
lean-axioms passed with 6136 named results and no sorryAx; lean-manuscript failed with
12 missing design-module dispositions, every other reported release-gate step passed.
The run is pull_request-triggered and tests a synthetic merge; it is not an exact-head
F/E check-run attestation. CI-REPAIR.log saves the relevant diagnostic excerpt.
No rerun or additional repair build was dispatched.

Sources of H2, H3 and A_miss remain open at their existing status. The sequence-specific
transfer condition on closed convex K has the same invariance content as preservation by D
(ARGUMENT.md gives the two written directions); broader channel transfer needs its own source.
The next bounded step is a native audit PR promoting the exact evidence and its scoped
written reading. The conditional pair theorem is a subsequent proof package.

