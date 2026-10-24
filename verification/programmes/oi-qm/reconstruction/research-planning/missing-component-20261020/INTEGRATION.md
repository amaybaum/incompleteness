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
selector and read-reset checkpoints, and the reviews of this index, are in `integration-reviews/`.

Evidence: *reproducible here* means the code under review, the reviewer's checkers and their outputs are in this
repository. *Author reproduced* means the author bundle with the cited sha256, held outside this repository, replays its
checker byte for byte against its recorded output, and the structured result is in `author-replays/AUTHOR-REPLAYS.json`;
the computation is reproducible from that bundle, not from this repository, and the replay is not an independent
verification. *Reviewer evidence missing* means the independent review's own computations (its checkers, mutants and
sources) are not retained, so its findings are attributed to its report. *On #910* means the material is held on #910's
branch.
`EVIDENCE-RETENTION.md` lists, per checkpoint, what is held and what is not.

| Checkpoint | Identifier | What it establishes, within its scope | Review | Evidence |
| --- | --- | --- | --- | --- |
| Bounded native instrument under the report18 rule | reviewed at commit `455eb092e5bdc37d203945e6689cee5032268dbf`; `mc-node9/design/native-instrument/` | Exact identities, Born values and closure at the register level; native transport of the single read at tick 2; the quantum statistics supplied. The threshold sampler's joint flag has degree 12; any exact sampler needs degree at least 2 | independent: accept with corrections, applied (`review/REVIEW.md`) | reproducible here |
| Selector-record boundary | bundle `3d18fe9cf0306b92ffec69d5e3cd8b77e3b57e36016f6090c49e9a8932d91d33`; session handoff `286d9b1cd345f1b5cb67c7b0e8d70ab27e42effce98116a43e818d2ede177646` | Sharp-read rigidity on the supplied 12-state calibration with deterministic records, under the qubit and independent-apparatus premises of its positivity test; no native selector constructed. The review recommends the factorization P(s,h \| a,ρ) = κ(a,s,h) Tr(P(a,s) ρ), with κ independent of ρ, as the operative acceptance test | independent: holds as stated (`SELECTOR-RECORD-REVIEW.md`) | author reproduced; reviewer evidence missing |
| Native selected-sign readout | bundle `c204e6f6ddd46c160e568e546e4652fcbf6f89988fa5664bb177a293d01b8664`; report `9c2a5dcc50c2d83a48616b9756e7b04bea1812ccafd75d1fff497ee151bed1cc` | A native readout of the selected sign for a setting programmed into the initial apparatus, by opposite-front masking, with exact record laws, under supplied resources and access. The "selection" is a one-time pad: the unselected signs stay in the public record, encrypted under private keys. No outgoing reset | independent: holds, with corrections to claim text (`NATIVE-SELECTOR-REVIEW.md`) | author reproduced; reviewer evidence missing |
| Read-and-reset boundary | bundle `15af0674fd17a0c053a70f5f4949bf2ab0e6585b62b777bc668c3f1dcbb1b7a5`; report `e50b51f0a1e54956065328241654159ce737c37f631026d6bb0f46dcc0b36234` | XOR-mask reset minimax 2/5, and 9/10 if validity is required, for XOR masks; as `READ-RESET-REVIEW.md` reports (E1–E3), input-independent random permutations (XOR masks among them) reach 7/30, also when validity is required, and a non-reversible discard-and-resample reaches 0. An X relay; a shell-collapse condition of one method, binding only if the private payloads must be fair and independent; a joint countercontrol. No read-and-reset instrument | independent: holds, with wording corrections (`READ-RESET-REVIEW.md`) | author reproduced; reviewer evidence missing |
| Native X read-and-reset | bundle `529185bb95a4ab1fb41097be8746418568e9a1a9e892ce5dff8f5fd36ffd2db8`, carried in the combined bundle; external review `2a51fe2a16658c9e3534626b045805a1305acf713eafb2f2e959d06cd32bcd11` | A conditional X instrument candidate: the actual X bit writes fresh outgoing fields under the unchanged rule; a native herald gives the 5:4:1 weights; joint record and carrier law including failures. Success 5/16, or 25/128 with the predecessor's herald. The outgoing carrier uses a private encoding | external: provisional technical acceptance within its scope, pending a proof audit of the inherited transport theorem | author reproduced; external review and spotchecker held outside this repository, spotchecker replayed within its arithmetic scope |
| Combined handoff | bundle `88f805670fe329c1dea9ca48604348a880d3758ea1c4fcf91d5f57eeaf304227`; overview `3e47e54ef0ca50820b95c50a36ce2fedb8f2fce7079d55901cc14e4ef62c4f7b` | The explicit calibrated menu (12 hidden states, 8 preparations); the radius-185 source audit, a concrete application audit and not compiler certification; complete normal and `-O` replays of the native-X suite | radius-185 audit: internal; normal and `-O` replays reported reproduced byte for byte by the coordinating session (Python 3.13.16) | author reproduced (the bundle's own replay driver, default mode; the native-X suite in the native-X row); the coordinating session's replay outputs not retained |
| Native-Y continuation | bundle `977e8e33683e1b06b47e6cfd78071cbccf72d95b03724f2684a77f1242af736e` | The raw Y operand (y, y, 1 ⊕ xy) at the second outward step; the three reachable codes 001, 111, 110 cannot map reversibly onto the two clean codes (0, 0, y) within one cell; an abstract staged-disclosure contract, whose recorder and reset are supplied abstractions; reciprocity does not select the quantum angle | internal; replays reported reproduced by the coordinating session | author reproduced (the bundle's own replay driver); the coordinating session's replay outputs not retained |
| Native-Y junction and readout (#910) | reviewed snapshot `00e85e748cf8e5ada75f4e1a22aef87eb0a823a2`; junction review `1c8c9e5ec501d7cb106d905c3adddf5141eae0cf`; six-source review `bf165400524f2b77f022ceb4e9811d95be3fe1c3`; q7 readout review `5f6786d6f02605f8e8821a536b678495e19015da` | The proposed sidecar junction depends bijectively on a free current triple, so it is not a raw-Y transfer; an initial prescription, restricted to the active no-wrap parity sector, that preserves frontier M1 and the previous input and retains M2. Evaluated exactly at the actual scale, the six-source endpoint of that prescription is not a clean Y transfer: opposite native Y values have overlapping supports at fixed X, so no deterministic decoder of that terminal triple and X alone recovers Y; history-aware decoding, later processing and other preparations are not excluded. Conditionally, with an added seed-only initial source (a supplied initial correlation and readiness resource, not a constructed native initializer) and supplied access (the receiver stays private until its designated read), a depth-seven outward readout gives the native code (0, 0, y) at q7; it is not an arbitrary-input clean socket, a reusable interface, a native reset, or a complete joint-history and access law | internal (#910 calls its reviewers independent; they are review threads within the research effort): accepted within these scopes | on #910 |
| Native post-Y phase (#910) | author `9b334367864c39e969072d9fbd46b0c049584963`; review `8247de450a70d6b48f4049b2ea758ac4f48821da`; reconciled at `71d291297d0a662cbb9377ab48eef7aa4b839e77`; within snapshot `00e85e74` | A two-slice phase-preparation candidate, conditional on #910's retained native family and its supplied initialization and access (including a stipulated six-bit fair seed bank): the selected phase at L = R + 9 has previous q8 = (0, y, 0), current q9 = (0, y ⊕ a, y ⊕ b) and remote Z = (0, 0, z), with conditional mask weights 5:3:2, z jointly fair and success 5/16. The whole-q9 terminal read has the correct restricted X/R raw record laws on that family; its unchanged post-read decoder is nonpositive (determinant −1/4). The phase map is a coordinate comparison, not an observer operation; previous-slice Y access is open. No reusable interface or reset | internal (separate-agent review): accepted within the conditional phase-preparation and restricted terminal-record scope | on #910 |

Author commits behind the #910 reviews above: six-source `8daae9f6c57d30dec13e140155114aa9298097e2`; q7 readout
`6db981c1574ecc6938e9d55388f0ebeea34fab60` and its correction `49a391b9c8c3daf02e603e366cb5489d36677c14`. Earlier
#910 checkpoints: `3fcaa271e689209dd74272c14a924c8f7fe44998`, `5d36a3f64c5992467d28b5fcc153a10c0d5db8b5`,
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
   internal proof audits; it needs an independent proof review. Its historical checkers reproduce byte for byte from
   bundle `4a232a48…`, held outside this repository (`author-replays/`); reproducible checkers do not discharge it.
2. **Native Y read-and-reset.** Starting from the native-X outgoing carrier E(x, y, r, z) = ((x, 1, y) at q_Y,
   (x, 1, r) at q_R, (0, 0, z) at q_Z): a native stage that takes the three reachable codes to a clean Y operand
   while keeping the distinguishing information in initially specified workspace; then a reset with fresh conditional
   resources whose outgoing carrier decodes to (X, Y, R, Z) = (y ⊕ a, y, y ⊕ b, z), with (a, b) = 00, 10, 11 in the
   calibrated post-Y ratio 5:3:2 and z fresh and fair. Then X→Y→X and X→Y→R,
   with every failure branch and the full outgoing carrier. #910 gives a conditional two-slice phase-preparation
   candidate on its retained native family (the post-Y row above); a reusable native Y reset and the complete public-history and
   outgoing-carrier joint law remain open.
3. **A reusable interface.** An outgoing encoding that the next instrument accepts natively, without a decoder that
   reads history.
4. **Selection.** A native relation between a physical direction and the operational observable, or a physically
   justified restriction, that selects the calibration.
5. **Native preparation, clock and settings; access closure.**
6. **Unrestricted depth and menu; composite systems and Bell structure.**

No full OI-to-QM equivalence is established. A failed construction refutes that construction, not OI in general or
its separate finite-precision programme.
