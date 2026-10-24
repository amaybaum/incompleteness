# OI-to-QM reconstruction programme: integration record

Research only, consistency axis (§A.23). No premise is adopted, no status changes, no round, F or E. This file is
the programme's index: it names each checkpoint by an exact commit or, for material held only in handoff bundles, by
the bundle's sha256. It does not reproduce their evidence.

## Responsibility

| Thread | Owns | Record |
| --- | --- | --- |
| #885 (`research/missing-component-20261020`) | the programme: its questions, assumptions, acceptance criteria and synthesis | this directory |
| #910 (`draft/native-y-research-checkpoints-20261024`) | the native-Y continuation: its constructions, counterexamples, evidence and reviews | `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/` on that branch |

Each thread has its own writer. A stable #910 conclusion enters this record as a reviewed synthesis with exact commit
references. Governance rounds such as KTRANS-SEP-2 (#905) are separate and are not part of this programme.

## The question

Can OI's fixed native reversible dynamics, with every resource and every access restriction stated explicitly,
realize a reusable measurement instrument? That requires its complete public record and its outgoing carrier to obey,
jointly and including every failure branch, the law of a quantum instrument on the qubit menu. And which ingredients
remain supplied rather than derived: the calibration, readiness, the clock, settings, and access?

## Acceptance rule for instrument candidates

- The whole public history and the outgoing carrier are checked jointly, on every branch, including failures.
- Fresh resources are independent conditional on every earlier outcome and herald. A new pin may not overwrite a
  reserved fair source.
- Correct reported outcomes, or correct pooled outgoing marginals, are not sufficient. X→Y→X statistics alone do not
  separate a wrong Y calibration (5:2:3 against 5:3:2); a terminal R read does, and serves as a diagnostic beside
  the joint rule, not in place of it.
- Per-port freshness is not sufficient. Two ports that are each uniform can be identical (TV 7/8 from the product
  law); a joint proof is needed.

## Checkpoints

Review status: *independent* means a reviewer outside the work's author, commissioned by the coordinator; *internal*
means a separate review thread within the research effort that produced it, with its own checkers; *external* means
the owner's outside reviewer. None is formal certification. The independent review reports for the selector, native
selector and read-reset checkpoints, and the review of this index, are in `integration-reviews/`.

| Checkpoint | Identifier | What it establishes, within its scope | Review |
| --- | --- | --- | --- |
| Bounded native instrument under the report18 rule | reviewed at commit `455eb092e5bdc37d203945e6689cee5032268dbf`; `mc-node9/design/native-instrument/` | Exact identities, Born values and closure at the register level; native transport of the single read at tick 2; the quantum statistics supplied. The threshold sampler's joint flag has degree 12; any exact sampler needs degree at least 2 | independent: accept with corrections, applied (`review/REVIEW.md`) |
| Selector-record boundary | bundle `3d18fe9cf0306b92ffec69d5e3cd8b77e3b57e36016f6090c49e9a8932d91d33`; session handoff `286d9b1cd345f1b5cb67c7b0e8d70ab27e42effce98116a43e818d2ede177646` | Sharp-read rigidity on the supplied 12-state calibration with deterministic records, under the qubit and independent-apparatus premises of its positivity test; no native selector constructed. The review recommends the factorization P(s,h \| a,ρ) = κ(a,s,h) Tr(P(a,s) ρ), with κ independent of ρ, as the operative acceptance test | independent: holds as stated |
| Native selected-sign readout | bundle `c204e6f6ddd46c160e568e546e4652fcbf6f89988fa5664bb177a293d01b8664`; report `9c2a5dcc50c2d83a48616b9756e7b04bea1812ccafd75d1fff497ee151bed1cc` | A native readout of the selected sign for a setting programmed into the initial apparatus, by opposite-front masking, with exact record laws, under supplied resources and access. The "selection" is a one-time pad: the unselected signs stay in the public record, encrypted under private keys. No outgoing reset | independent: holds, with corrections to claim text |
| Read-and-reset boundary | bundle `15af0674fd17a0c053a70f5f4949bf2ab0e6585b62b777bc668c3f1dcbb1b7a5`; report `e50b51f0a1e54956065328241654159ce737c37f631026d6bb0f46dcc0b36234` | XOR-mask reset minimax 2/5, and 9/10 if validity is required, for XOR masks; input-independent random permutations (XOR masks among them) reach 7/30, also when validity is required, and a non-reversible discard-and-resample reaches 0. An X relay; a shell-collapse condition of one method, binding only if the private payloads must be fair and independent; a joint countercontrol. No read-and-reset instrument | independent: holds, with wording corrections |
| Native X read-and-reset | bundle `529185bb95a4ab1fb41097be8746418568e9a1a9e892ce5dff8f5fd36ffd2db8`, carried in the combined bundle; external review `2a51fe2a16658c9e3534626b045805a1305acf713eafb2f2e959d06cd32bcd11` | A conditional X instrument candidate: the actual X bit writes fresh outgoing fields under the unchanged rule; a native herald gives the 5:4:1 weights; joint record and carrier law including failures. Success 5/16, or 25/128 with the predecessor's herald. The outgoing carrier uses a private encoding | external: provisional technical acceptance within its scope, pending a proof audit of the inherited transport theorem |
| Combined handoff | bundle `88f805670fe329c1dea9ca48604348a880d3758ea1c4fcf91d5f57eeaf304227`; overview `3e47e54ef0ca50820b95c50a36ce2fedb8f2fce7079d55901cc14e4ef62c4f7b` | The explicit calibrated menu (12 hidden states, 8 preparations); the radius-185 source audit, a concrete application audit and not compiler certification; complete normal and `-O` replays of the native-X suite | radius-185 audit: internal; replays reproduced byte for byte outside the research session (Python 3.13.16) |
| Native-Y continuation | bundle `977e8e33683e1b06b47e6cfd78071cbccf72d95b03724f2684a77f1242af736e` | The raw Y operand (y, y, 1 ⊕ xy) at the second outward step; the three reachable codes 001, 111, 110 cannot map reversibly onto the two clean codes (0, 0, y) within one cell; an abstract staged-disclosure contract, whose recorder and reset are supplied abstractions; reciprocity does not select the quantum angle | internal; replays reproduced outside the research session |
| Native-Y junction (#910) | commit `1c8c9e5ec501d7cb106d905c3adddf5141eae0cf` | The proposed sidecar junction depends bijectively on a free current triple, so it is not a raw-Y transfer; an initial prescription, restricted to the active no-wrap parity sector, that preserves frontier M1 and the previous input and retains M2; reduction of the target calculation to six current sources | internal (#910 calls its reviewer independent; it is a review thread within the research effort): obstruction and initial geometry only |

Earlier #910 checkpoints: `3fcaa271e689209dd74272c14a924c8f7fe44998`, `5d36a3f64c5992467d28b5fcc153a10c0d5db8b5`,
`4f2407732611f9d6c0838a64de8f2226d65eb8e5`. The earlier checkpoints of this branch are listed in `PLAN.md`
(*Status*) and recorded on #885.

## Supplied, not derived

- the calibrated menu: the Born probabilities of the 12-state model, which reciprocity does not select (both
  (4/5, 3/5) and (3/5, 4/5) meet the sharp-qubit condition);
- readiness, initial fair resources and their independence;
- the clock, the settings and their local selection;
- access: which registers are public, private or never read, and when.

## Open obligations

1. **Transport theorem.** The general transport and frontier theorem that the native constructions inherit has
   internal proof audits; it needs an independent proof review. Reproducible checkers do not discharge it.
2. **Native Y read-and-reset.** Starting from the native-X outgoing carrier E(x, y, r, z) = ((x, 1, y) at q_Y,
   (x, 1, r) at q_R, (0, 0, z) at q_Z): a native stage that takes the three reachable codes to a clean Y operand
   while keeping the distinguishing information in initially specified workspace; then a reset with fresh conditional
   resources whose outgoing carrier decodes to (X, Y, R, Z) = (y ⊕ a, y, y ⊕ b, z), with (a, b) = 00, 10, 11 in the
   calibrated post-Y ratio 5:3:2 and z fresh and fair. Then X→Y→X and X→Y→R,
   with every failure branch and the full outgoing carrier.
3. **A reusable interface.** An outgoing encoding that the next instrument accepts natively, without a decoder that
   reads history.
4. **Selection.** A native relation between a physical direction and the operational observable, or a physically
   justified restriction, that selects the calibration.
5. **Native preparation, clock and settings; access closure.**
6. **Unrestricted depth and menu; composite systems and Bell structure.**

No full OI-to-QM equivalence is established. A failed construction refutes that construction, not OI in general or
its separate finite-precision programme.
