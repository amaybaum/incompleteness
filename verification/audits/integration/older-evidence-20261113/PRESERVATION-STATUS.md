# Selected evidence preservation status

**Writer checkpoint / WIP. This package preserves historical content; it does not establish its scientific claims or authorize a landing.** Accountable Issue: [#1169](https://github.com/amaybaum/incompleteness/issues/1169). Guiding draft: [#1280](https://github.com/amaybaum/incompleteness/pull/1280).

## Scope and custody

The owner requested preparation of the four-artifact scope below after the read-only identity check. This child adds the actual content in [evidence/preserved-artifacts.zip](evidence/preserved-artifacts.zip), the machine-readable [manifest](PRESERVED-ARTIFACTS.json), and this status/trace record. The eight audit files at parent `116d6e9092d9c2c802959c33d68a5b71c37f47a6` are unchanged. No other proposed payload in [PRESERVATION-MANIFEST.tsv](PRESERVATION-MANIFEST.tsv) is included by implication.

The archive has four ordinary UTF-8 text members. It is uncompressed, unencrypted ZIP data, with fixed member order, container date and regular-file permissions. Container dates are not source dates. All **147,390 member bytes** are unchanged: no redaction, identifier cleanup, normalization or scientific edit was applied.

| ID | Archive member | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| R1 | `review/REVIEW-APPROX-UNIT1.r4a-diff.md` | 7,367 | `ceeab15fedcfd40e373b4c270df8af3d2d78a0960093727f2fc9878be0f72c49` |
| R2 | `review/REVIEW-APPROX-UNIT1.r4a-final.md` | 6,160 | `f17ccc0e2f74f44ce03f41884668478823ce869c3df36623c9b595dfe28df32d` |
| M1 | `evidence/MATRIX-PAGE-SNAPSHOT.json` | 76,923 | `41f1198fbf6d4b2412a2555b1ac7af77eef9b71f2f49c2344bb0adc49c188f9f` |
| M2 | `evidence/MATRIX-PAGE-PROJECTION.md` | 56,940 | `c68b93555905b543b3c80c6029eb5d6678e0948c7033640d1035de121ce6b9ab` |

The complete archive is **148,006 bytes**, SHA-256 `604013567c9087f97a112ec140f64de91ec33c7d8ecd004c0bd4e9028f385be9`. Its member paths realize the four logical selections in the parent manifest *inside the archive*; they are not loose repository files. Member hashes and the container hash identify different objects.

Verbatim historical task identifiers and wording remain inside the evidence data. The ordinary prose scan does not inspect ZIP members; its passing result cannot certify them. The byte-verification recipe below and a separate non-author preservation review cover this boundary. No checker, whitelist or workflow is changed. The original files remain available for full inspection after extraction.

## Provenance and review identity

**R1 and R2 are recovered original model-review reports**, compared byte-for-byte with the pre-existing deliverable originals. Their earlier identities and recovery are recorded in [PROVENANCE-RECEIPTS.md](PROVENANCE-RECEIPTS.md). They are not newly authored reviews or historical GitHub review submissions.

R1 records the non-author Codex task `review_approx_r4`'s 2026-11-09 focused ACCEPT of the N1–N3 cleanup at `b1a17e01160f7dffde7ba63f7b7f69e8b95c1997`, from baseline `4e526de57b0a4fedf7821d63722a1733c0f49298`. R2 records the same reviewer's final publication-metadata supplement at `e41cf6137be165add39c7e557e97d3dddf110239`, carrying the focused acceptance forward. Their original attribution, source identifiers, verdicts, comparison limits and integration qualifications are retained verbatim. They document model review; they are not independent mathematical or kernel verification.

**M1 is a complete historical Page capture; M2 is its derived Markdown projection.** M1 identifies the [dependency-matrix Page](https://chatgpt.com/space/page_9580d355639c81919a21ae4d8af34201), its 84 canonical blocks, block identities/hashes, source sequence 1, source update time `2026-11-10T13:23:20.179160Z` and read date 2026-11-13. M2 is exactly the block Markdown strings joined with two LF characters, followed by one LF. It is not an original historical Markdown file or a second independent source.

Historical WIP, pending-review and planning statements remain historical. In particular, the matrix's pending PREP-MIN wording and transfer-era status must not be treated as current authorization. The parent [DECISION-PACKET.md](DECISION-PACKET.md) identifies this stale-status boundary. Neither the capture nor a retained review starts an experiment or reopens #1216.

## Claim-specific dependency trace

| Statement or use | Content actually needed | Status in this proposal |
| --- | --- | --- |
| Four selected originals exist with the recorded bytes | All four archive members, this manifest and the parent's selection manifest | Content is included in this research-branch package. This is not a claim of retention on main. |
| R1/R2 contain the quoted focused review verdicts and subjects | The full original reports R1/R2 | Included. Recording what a report says does not independently validate the reviewed assessment. |
| Correctness of the reviewed #1221 assessment or its original commit ancestry | The actual assessment/proof/support records and the relevant Git history | Still support off main where not already retained. Copying reports does not make the subject commits reachable from main or re-establish their ancestry. |
| M1's recorded block count and M2's exact projection relation | The complete captured JSON and derived Markdown | Both included; reproducible from these members. No new assertion about a later live Page state is made. |
| Origin of the historical capture | Its recorded Page identity, source times and capture metadata | Retained as capture provenance. A source URL does not replace the captured content. |
| Scientific claims and inherited review assertions inside the matrix | Each claim's actual supporting proof/check/review content | The existing [source](SOURCE-MANIFEST.tsv) and [support inventory](SUPPORT-INVENTORY.tsv) remain applicable. Their limits and gaps are not closed by retaining the matrix. Citations used as support are not relabelled as provenance. |
| Proposed future preservation basis | A separately adopted policy and a valid claim-specific landing decision | Not supplied by this package; see the current-policy boundary below. |

This is a custody increment, not retention of all 116 locally audited copies, all 101 proposed preservation rows, or the complete external proof corpus. The source versions, ancestry and other support each surviving claim needs still require the applicable §A.42 trace before landing. The parent's calculated member blob identifiers are content identities; an archived member is not thereby a standalone Git object or a commit reachable from main.

## Open discrepancies and remediation obligations

| Gap | Current evidence and limit | Missing verification or decision | Accountable Issue |
| --- | --- | --- | --- |
| Frozen dispositions review identity | The existing audit records CHECK-r7c's reviewed `856fa01d…` digest and the actual frozen `d3adc823…` digest. They are different. Neither ledger is added here. | Recover/retain the exact reviewed bytes and establish their relationship, or obtain a separately authorized check/disposition of the actual frozen bytes. The owner freeze is not an independent review of a different digest. Keep this gap open; do not edit a frozen record. | #1210 |
| OICORE version bridge | Historical `9b82…`/`ec796…` and published `a30d8d79…` are not equated. The existing landing receipt requires an exact version reconstruction/bridge. | Recover the originals or establish and check the exact bridge. Acceptance of a historical version is not transferred to different published bytes. Actual consumed OICORE content remains support, with its existing gates. | #1169 |
| Other consumed off-main science/history | The matrix and review originals retain their own scope and limitations; the parent inventories distinguish fetched, identity-only and manifest-only sources. | Retain or independently validate each needed proof/history at landing, narrow a mutable claim where applicable, or obtain the exact claim-specific owner exception permitted by the current rules. No exception is granted here. | #1169 and each source's named Issue |
| Main retention and landing basis | Actual selected content is prepared in a research branch, not adopted on main. | Complete the applicable review, tracing and landing-basis assessment and obtain a separate owner integration/merge decision. This remediation plan authorizes no additional work. | #1169 |

The [existing provenance record](PROVENANCE-RECEIPTS.md) gives the full source/review identities and limits for both version discrepancies. This package preserves those distinctions; it resolves neither discrepancy and introduces no new scientific obstruction.

## Current policy and next gates

The preparation snapshot is main `c3b5f37a354bb26437e2e0165c576a347a63c153`, with the [published AGENTS.md](https://github.com/amaybaum/incompleteness/blob/c3b5f37a354bb26437e2e0165c576a347a63c153/AGENTS.md). This is a WIP research-branch publication under §A.43. No main-landing basis under current §A.46(2), or claim-specific §A.42(8) exception, is selected or certified here.

At preparation, [#1283](https://github.com/amaybaum/incompleteness/pull/1283) remains draft and unadopted. Its proposed new preservation basis is **not used**. Reliance on that basis requires adoption first; adoption alone would not authorize this package's integration or waive support gaps. Until then, the existing rules and exception requirements govern.

The new preservation delta requires a separate non-author byte/provenance review, ordinary exact-head CI and ChatGPT exact-head confirmation. Parent audit acceptance does not certify this added payload. Their exact checkpoint and receipts belong on guiding PR #1280. No full scientific re-review or scientific computation is part of this preparation unit.

Physical source remains **NOT PASSED**; IC₂ remains conditional and OI–QM equivalence remains open. #1278/#1281 retain their separate integration gates. No premise, manuscript, frozen record, board, workflow, F/E designation or merge is changed or authorized by this custody package.

## Re-establish byte identity

From this directory, using Python's standard library, the following checks the archive, exactly four members, the prior selection manifest, and the complete projection. It writes nothing and executes no archived content. Expected output: `4 artifacts; 147390 bytes; hashes and projection match`.

```sh
python3 -I - <<'PY'
import csv, hashlib, json, zipfile
from pathlib import Path, PurePosixPath
m = json.loads(Path('PRESERVED-ARTIFACTS.json').read_text())
a = Path(m['archive']['path']).read_bytes()
assert len(a) == m['archive']['bytes']
assert hashlib.sha256(a).hexdigest() == m['archive']['sha256']
old = {r['path']: r for r in csv.DictReader(
    Path('PRESERVATION-MANIFEST.tsv').open(), delimiter='\t')}
with zipfile.ZipFile(Path(m['archive']['path'])) as z:
    names = [x['member'] for x in m['artifacts']]
    assert len(names) == len(set(names)) == 4 and z.namelist() == names
    assert all(not PurePosixPath(n).is_absolute()
               and '..' not in PurePosixPath(n).parts for n in names)
    assert z.testzip() is None
    data = {}
    for x in m['artifacts']:
        b = z.read(x['member'])
        assert len(b) == x['bytes']
        assert hashlib.sha256(b).hexdigest() == x['sha256']
        assert old[x['member']]['sha256'] == x['sha256']
        data[x['id']] = b
    assert sum(map(len, data.values())) == 147390
    blocks = json.loads(data['M1'])['content']['blocks']
    assert len(blocks) == 84
    assert ('\n\n'.join(x['markdown'] for x in blocks) + '\n').encode() == data['M2']
print('4 artifacts; 147390 bytes; hashes and projection match')
PY
```
