# Batch A: accepted sources and review record

This record identifies the sources reconciled for Batch A under #914 comment 6881174757,
with LC-5 scoped by comment 6880700869 and MC-1 by #1028 comment 6880012900.
Codex is the writer and ChatGPT the independent reviewer. The source baseline is
`dfeec843bec08443b25cffe34d33dc8401c3b604`.

## Accepted individual checkpoints

`REVIEW-RECORDS.json` retains the complete public review texts, exact commits, reviewer
attribution, submission times, verdicts and GitHub review states. The individual scientific
verdicts are seven ACCEPT and two ACCEPT WITH NITS; the recorded GitHub state is COMMENTED.
These verdicts apply to their stated scopes and preserve their evidence layers.

| Unit | PR | Reviewed commit | Individual verdict | Review |
|---|---|---|---|---|
| LC-5 / ledger r9 | #1292 | `4470bd02453f45327776689ed9fa46bec0c5edc7` | ACCEPT | 5906575489 |
| D7 | #1295 | `b3314afb820eb29e23518e5bd9fedb1cc5982f61` | ACCEPT | 5906575654 |
| D8 | #1296 | `124f5cd6f5387be6dc2bd1d795a3643fe05c14f9` | ACCEPT | 5906575962 |
| F-32 | #1297 | `e4ef5a70b32f4ea103b6dd15f8e3b47a2b00c5e6` | ACCEPT WITH NITS | 5906578782 |
| F-31 | #1298 | `be5de6eb1cd15d8709e4fed39bccbba6d236a23b` | ACCEPT | 5906579045 |
| F-33 | #1299 | `70c22b4910f59fcdb0c8b54e9242e5512170252d` | ACCEPT | 5906579298 |
| D1 | #1300 | `b34c82cc7f0d62a034e821858a1af72df264c144` | ACCEPT | 5906581448 |
| F-34 | #1301 | `218dcb2540466887e8de68f349fdcad253b2615c` | ACCEPT WITH NITS | 5906581566 |
| F-36 C1 | #1302 | `740f17d53fed804a8767e62eb8bd48ce596d0438` | ACCEPT | 5906785538 |

F-36's earlier review 5906581660 at `04c1239db5582f98bbe6352012c3d56f0b0313f0`
is retained in its review-history field. Focused review 5906785538 accepts C1 at the child
shown above. Original reviews and reviewed commits remain unchanged.

## Reconciliation and preservation

The integration retains all nine reviewed commits in its ancestry. Its six changed
manuscript Markdown files contain the union of the accepted source edits. Shared TeX/PDF
artifacts and the SC-42 result are regenerated for the combined source. Individual green
PRs do not certify a combined publication artifact.

The 49 files under
`verification/programmes/oi-qm/reconstruction/drafts/unified-ledger-20261114/`
are retained byte-for-byte from the LC-5 checkpoint. They preserve the ledger's reading,
coverage, review and disposition trail, including earlier revisions. The review records
and older index statements describe their historical checkpoints; r9's current individual
review is retained here. They are historical research snapshots rather than a replacement
for the corrected manuscripts. The original r8 files, 12 QCD-related rows and ten
unresolved-finding rows are unchanged. No new coverage audit or QCD investigation is
performed by this integration.

This preservation keeps the evidence needed to interpret LC-5 and its predecessor
assessments under §A.46. Underlying mathematical and scientific claims retain their
primary manuscript/proof support, named assumptions and existing limitations. Retaining
an assessment or review supplies no new physical derivation or empirical confirmation.
A future landing still requires the applicable dependency tracing, integration review,
verification and separate owner merge decision.

## Retained corrections and open obligations

| Unit | Accepted correction retained | Remaining scope |
|---|---|---|
| LC-5 | r9's additional proof-body and chapter 13–17 reading/classification | New D19–D21 candidates and prior unresolved rows retain their own disposition gates under #914. |
| D7 | H-link/H-cust, H-spin' and open H-χ' conditions in Chapter 18 | Native chirality and physical sourcing remain open under #1190/#1028. |
| D8 | Standard-QCD account distinguished from the open native confinement/nuclear-binding derivation | Strong dynamics and binding-energy derivations remain open under #1028; both FULL passages and Complexity propagation are retained. |
| F-32 | The Higgs doublet is an input; existence and hypercharge are not derived | The separate automatic-inflation clause remains a nonblocking finding under #1028/#1058. Its correction or justification needs a separately scoped decision accounting for coupling, potential, dynamics and initial conditions. |
| F-31 | Candidate-sector counting distinguished from anomaly cancellation given the observed family pattern | Physical-generation and light-spectrum identification remain conditional. |
| F-33 | The total dark fraction is the identity 1−Ω_B | No first-principles dark-sector split is supplied. |
| D1 | Mixed-status section heading | Individual problem verdicts are unchanged. |
| F-34 | Eleven biology entries and the count retain conjectural status | The local marker's taxonomy clarification remains a nonblocking issue under #1028, requiring a separate legend/wording disposition. B3/D16 remains unresolved and outside the eleven-entry correction. |
| F-36 | N5 remains a branch-dependent heuristic, outside the seven prediction classes | C1 is resolved; no ordering theorem or measurement confirmation is added. |

## Publication checks

Canonical regeneration uses Pandoc 3.1.3 and the repository's unchanged build entry point:

```sh
sh ./build.sh --book
sh ./build.sh Complexity
```

The build's dropped-glyph hard gate applies without an override. Chapter/FULL mirrors,
source stamps, pagination, all-page PDF decoding/rendering and the changed passages need
combined validation. Source-scope verification uses the unchanged checker:

```sh
python3 -I -B verification/audits/manuscript/bell-operational-reconciliation-20261029/check_sc42_integration.py
```

Its structured result is regenerated in the existing audit directory. Full-history,
SC-42 must-fail controls, release and other required checks run in ordinary CI on the
actual integration head. Independent integration review checks preservation of the
accepted corrections and absence of additional scientific changes.

## Scientific and authorization limits

Physical source remains **NOT PASSED**. No OI-derived information-causality principle,
quantum-equivalence result, new premise or scientific-status promotion is established by
reconciliation. This is draft integration preparation; scientific execution, dispatch,
F/E designation and merges retain their separate authorization gates. RO-1 is unchanged.
