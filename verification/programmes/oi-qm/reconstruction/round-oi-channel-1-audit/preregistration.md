# OI-CHANNEL-1 — channel protocol and transfer-boundary audit

Status: candidate freeze, native V3 draft. Owner authorization to prepare the research and
PR sequence: 2026-10-11. This file is drafted from D on one PR under AGENTS.md section A.39.
It becomes a freeze only after an exact-head all-green workflow run and the owner's
designation of F. Execution follows F; E and the final receipt require their own checks.
No owner designation is inferred from the instruction to proceed.

```v3-round
round OI-CHANNEL-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-oi-channel-1-audit/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-oi-channel-1-audit/
record AM verification/receipts/OI-CHANNEL-1.json
execution A verification/lean/oi_channel1_check.py
execution M .github/workflows/verify.yml
```

D: 9f9f8257a980a1819fbbc1dc0019917cf8678626.
The delta from D to F is this preregistration alone. F and E are exact objects the owner
designates after their exact-head workflow attestations, not synthetic pull-request merges.

## The bounded package

The audit promotes saved exact evidence for the stopped repeat-until-success circuit and
its cone controls, plus a separately labelled written dependency assessment. It adds no
Lean module and proves no new theorem in the kernel. It neither adopts nor sources H2,
H3, A_miss, arbitrary-cone channel transfer, or a closure of exact availability. No
manuscript, ROADMAP, census registry, kernel source, legacy record or other round's
record changes. The historical research archives are cited, not imported into main.

Research provenance: research/round7-channel-audit at
e7d380fcb9881e3063243aaa149e85be3cd0a914, research/round7-channel/ and
research/AUDITS/2026-10-11-round6/. Round-7 registration preceded the first saved run at
78aa5b25415cf1cd26994cb2280343ab86cd72d9. The prior review's circuit computations and
this batch's successful runs are exploratory evidence, disclosed before this freeze;
their outputs are not presented as blind predictions.

## Frozen files

The files are read from e7d380fcb9881e3063243aaa149e85be3cd0a914 and added byte for byte
during execution under the names below.

| source in research/round7-channel/ | execution destination | SHA256 |
|---|---|---|
| channel_check.py | verification/lean/oi_channel1_check.py | 9937b6ffca6cf570cf7e1c3267ba1525ead48ada4d5f1e92959ec0f603baebff |
| native-controls.py | record directory controls.py | 76b7b76acd6115a7a1bd342859d4d38b4b246a9cab76b0e2e38c3b6bde0b25d7 |
| predicted-verify.yml | .github/workflows/verify.yml | bd71bdc270753be8296c4a5c9723e23673c2f8acdaa9417fb70a6ddd6cbe2443 |

Controls SHA256: 76b7b76acd6115a7a1bd342859d4d38b4b246a9cab76b0e2e38c3b6bde0b25d7

The original workflow at D has SHA256
c31d34ac7f15f2a0f37e7d64592b5ff102381d0fa30fc5bdf5d864ca03e6f185.
The predicted workflow changes only five splices: one OI-channel shard before Act 42,
its addition to the aggregate needs list, and its result environment variable, echo and
required success test. The new shard uses Python 3.11 and no third-party dependency,
runs the exact checker and the controls' mutation tests, and fetches complete Git history.
The frozen controls reconstruct all five splices from D and compare the bytes.

## Questions and decision rules

| question | evidence checkpoint | earned reading when checkpoint passes |
|---|---|---|
| Does the actual circuit realize the stopped channel formula? | U, RESET, BRANCH, TP, TOKEN, PAIR, DICT, J; all exact; depths k=0,...,6 | finite exact identities; general-k recurrence written separately |
| Does the defect-cone countercontrol remain valid? | ZF, CC-ID, CC-CLIFFORD | normalized matrix-trace witnesses -1/10 and -1/8; construction-level obstruction |
| Do the control cones distinguish the assumptions used? | OCT, OPEN, KAPPA; exact examples and separate written arguments | 24 Clifford target actions versus Phi_1; closedness used by the limit; expanded block cone fails self-duality and maxCone |
| Do the protocol countercontrols discriminate wrong constructions? | CC-Z, CC-OUTCOME, CC-RESET | omitted correction, wrong success outcome and missing reset rejected |
| Are the availability, transfer and self-duality boundaries preserved? | unchanged kernel definitions, frozen earned reading and scoped result note | sources remain OPEN; no upgrade from finite evidence to a kernel proof or full-model independence |

The checker reads no file, imports no thread code, uses Gaussian rational arithmetic
from the standard library, and prints the 17 named check groups. The exact stdout
SHA256 is ec73839a23e1c2e051140ff9b56d47bbda4f9b55e37963ca1256500b36642da5,
stderr empty, exit 0. Its final line is:
CHANNEL-CHECK: PASS; 17 checks; 140 matrix-unit cases
Any changed stdout, nonempty stderr, failing check or nonzero status voids the reading.

## Written reading and non-inferences

The result note contains this exact earned reading, once:

The finite stopped circuit realizes the channel formula at depths 0 through 6 by exact arithmetic. The all-depth recurrence and the universal cone arguments are written proofs. Transfer to an arbitrary pair cone and the general-k InstAvail witness remain additional obligations. This audit does not establish unconditional quantum reconstruction or full-model independence.

The note states Phi_0=id and Phi_(k+1)=S0+Phi_k composed with F0, with S0=(5/8)Ad(D0)
and F0=(3/8)id, where D0=diag(1,(3+4i)/5). The all-depth formula follows by written
induction. Limits use closedness of the invariant cone, not exact availability of D0.
On closed convex K, the sequence-preservation and D0-preservation directions are written
separately; neither is labelled kernel-certified.

The broader channel-transfer clause remains an additional hypothesis. I4.66 preserves
PSD matrix states and I4.38 derives that validity from implementation locality. Extending
it to an arbitrary pair cone requires validity on an identified pair state space C and
C=dict '' K, plus the context and label premises for the spectator step. At C=PSD,
this identification is K=Q3, so it is excluded as an independent source.

KAPPA has a negative test on a product vector and fails the maxCone upper bound. It is a
control for the stated H1, H2 and target-channel hypotheses, not a full OI countermodel.
The 118 reached inventory rows and the 68 NOT REACHED rows are kept distinct. The latter
remain unresolved. H3's possible replacement by cone structure and maxCone, given H2 and
A_miss, is a separate proof question, not a result certified by this audit.

## Invariants and checkpoints

| invariant | measurement |
|---|---|
| probe and controls unchanged from the frozen sources | P and C SHA256 checks |
| exactly the five frozen workflow splices | W byte comparison with reconstructed D workflow |
| I4.66, I4.38 and their source modules unchanged | L object-byte checks of OperationalValidity and ImplementationLocality at D and the checked execution |
| preregistration unchanged after F | F object-byte check; V3 control-plane immutability |
| exact record population and bounded changed paths | R and G controls; V3 governed-path verification |
| expected exact output and no hidden errors | V checksum, stderr and return code |
| scoped earned reading, outcome and summary line | S control; review of the separate written statements |
| controls reject mutations | positive fixture plus 11 mutations in controls --self-test |

The mutations change the probe, workflow, landed source, preregistration, record population,
earned reading, controls, appended overclaim, stdout, stderr and exit status. All must be
rejected by their named control. No success verdict is printed over a failed control.

## Design evidence and stages

Saved checker run 1 and its replay are byte-identical: 17/17 PASS, 140 matrix-unit cases,
five negative controls discriminating the stated faults. The frozen controls pass their
positive fixture and 11 mutations. Python parsing passes for both scripts.

Separately, disposable design 13ad14a1ba2973245354aea7790c021d946b1ff0 repairs the
missing ComplexOrder scope in BridgeChannelTransfer. Run 38162504147, Mathlib job
114538184326: Build successful, seven standard axiom reports, lean-axioms 6136 with no
sorryAx; release gate failed at lean-manuscript with 12 undispositioned design modules.
This is design evidence only. This round adds none of those Lean modules.

1. Before F: hold the control-plane branch at the proposed F, dispatch verify.yml on
   that exact head, and record an all-green run before requesting the owner's designation.
2. S1 after the owner's F designation: add the three frozen files and controls.py in
   one linear commit. Run controls HEAD --freeze F and the mutation tests; CI must pass.
3. S2: add result.md with Outcome: OI-CHANNEL-1-READ, the frozen earned reading, the
   checker's final line, written arguments at their labels and exact evidence pointers.
   Run controls HEAD --freeze F; obtain an all-green exact-head run and the owner's E
   designation. No unrelated main history enters before E.
4. Reconcile if needed, build the native receipt, and require v3_verifier --verify-round Q
   to print VERDICT HOLDS before ordinary review and merge.

A failed frozen checker or control halts this round under V3 S12 rather than changing the
decision rule after F. A valid read is a consistency-axis audit; it sources no premise and
does not complete the OI-to-QM research programme. Later proof packages follow their own
scopes, freezes, exact-head attestations and owner approval.
