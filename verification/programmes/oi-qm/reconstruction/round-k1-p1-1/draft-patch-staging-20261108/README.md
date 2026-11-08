# K1-P1-1 mutation patches and exact X5 proposal before freeze

**Reviewed source candidates; not frozen.** This staging package pins concrete
MU-C1/C2/C3 patches against independently reviewed A/B source that passed its
prescribed author fixtures. It supersedes the old unrevised-draft patch bytes
in this branch's preserved history. The new patch bytes still need independent
review and the combined synthetic gate. No instance kill has run, no freeze
table is filled and no F is designated.

Authority: [owner continuation scope](https://github.com/amaybaum/incompleteness/issues/1031#issuecomment-6721619842),
following the original [draft-staging authorization](https://github.com/amaybaum/incompleteness/issues/1031#issuecomment-6719802814).
Guiding PR #1135; accountable Issue #1031; patch-package writer Codex root.
Independent source/safe-path reviews: [c.6721877817](https://github.com/amaybaum/incompleteness/pull/1135#issuecomment-6721877817).
The fixture expectations were independently re-derived by hand at unchanged
round d92e0882e7609e91e3458193391e89610fffa777. This branch is separate from the
round and eventual code integration staging branch. No control plane changes.

## Actual source bytes

| Unit | Delivery commit | Source blob | Source SHA-256 |
|---|---|---|---|
| A | d5cec548669088bea9be35e65b7242bdecd2c643 | 2252965843430155fedfbc8855a5d23d13c2c920 | 0e8721e5fe1c8fc8540d36ce2eed84d812a5630867ec4af56d920169466b3fdd |
| B | f9a051c5ee11f97d73195dab39607d9691828b44 | 63eadd818e59f86c48969552ef144f56b4154b95 | c5bfb8d198ed464c093ebf38ddc6f0d0e160f3e5e91395b1f98014c33928c7e5 |

These blobs equal the independently accepted ce6f0f2c and 79ff3a7a sources;
later delivery commits change logs only. Under Python 3.11.17, A passed eight
admitted fixtures and all seven negatives, B fourteen fixtures and its six
negatives. NF-1 used its prescribed B-positive then A-refusal pair across the
independent contexts. These are author checks, not the combined gate.

manifest.json pins source commits/blobs/hashes, patches and patched-byte hashes.
No candidate source or patched program is copied into this tree.

## Intended mutations

- MU-C1 changes only A's instance T from 1 to 2. PR-E's instance kill is unrun.
- MU-C2 flips exactly inverse-matrix row 0 column 0 inside B's instance builder.
  CC-BIJ's instance kill is unrun; the fixture bad-inverse control is separate.
- MU-C3 changes only A's single ratio helper from Fraction to floating division.
  Its required before-F test is exit 3 on the fixed SF-3 input through the bound
  and independently reviewed controls harness; it has not run in this package.

Only the newly reviewed patch hashes may be bound in controls. Old prototype
hashes must not be reused. These are proposed inputs, not freeze authorization.

## Exact X5 workflow proposal

X5-verify.patch is data only, against verify.yml at round d92 (also byte-equal
at main merge 38fec475). It adds the named K1-P1-1 job, Python 3.11 and:

    python3 -I controls.py check --stage final

It wires that job into aggregate needs, result environment, diagnostics and
mandatory success check. No workflow file is changed or dispatched. Independent
review is still required before proposing this as the future X5 edit.

## Static reproduction

From this checkout's root, with both delivery commits and round d92 in Git:

    python3 -I -B verification/programmes/oi-qm/reconstruction/round-k1-p1-1/draft-patch-staging-20261108/check_static.py > /tmp/k1p1-draft-static.json
    cmp /tmp/k1p1-draft-static.json verification/programmes/oi-qm/reconstruction/round-k1-p1-1/draft-patch-staging-20261108/static-validation.json

The checker reads pinned blobs and patch bytes, splices ordered hunks at exact
positions without offset/fuzz, verifies hashes and intended edits, and parses
original/patched Python without executing it. Eight malformed controls per MU-C
patch must reject. The X5 proposal is checked against its five declared edits;
its YAML/job semantics additionally need independent review. This staging audit
is neither controls.py nor a freeze gate; it evaluates no candidate/map.

## Remaining gates

Independent review of these patch bytes/X5 proposal, controls corrections,
review and exact binding, reviewed integration copies of the three code blobs,
fixture JSON and patches, and the bounded full synthetic gate remain necessary.
Section-14 equality to round-branch patch bytes cannot hold while the owner
keeps that round at d92, where the patches are absent. Staging success does not
fill that gap: a separately approved freeze revision must record actual pins.
No approval (b), F/E, instance run, dispatch, receipt, merge or scientific-status
promotion follows. No implementation, round or workflow branch is changed here.
