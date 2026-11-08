# K1-P1-1 provisional mutation-patch staging

**PROVISIONAL AGAINST UNREVISED DRAFTS. Not final freeze pins.**

This package supplies concrete draft MU-C1, MU-C2 and MU-C3 patch bytes for
inspection under the owner's [draft-staging authorization](https://github.com/amaybaum/incompleteness/issues/1031#issuecomment-6719802814).
The guiding PR is #1135 and the accountable Issue is #1031. Codex root is the
package writer; an independent non-author reviewer reviews the pushed head.
The original independent A/B/controls writers and branches are preserved.

The package branch is staging/k1-p1-1-draft-patches-20261108, from main at
9c201475ba6fd8f341591d14dd8e88db2e2aaa90. It is separate from the pre-F round
branch and from the eventual integration staging branch of A1 section 14.
The round's control plane remains d92e0882e7609e91e3458193391e89610fffa777.
No round-branch amendment, candidate implementation, controls constant or
workflow is changed here. No main merge, rebase or freeze is proposed.

## Actual source bytes

The source drafts are still unrevised and lack A1's adopted fixture interface:

| Target | Source commit | Source SHA-256 |
|---|---|---|
| A | caea695c875179fb9b310739c4aa2a9196332fe4 | 9d4eb0a778333a6606ab507bacd026e56e054ec03cfe38288cf2d22c5c080825 |
| B | e32fe4eea312b1a468ea19ed1f1559d768c5dbda | 1adc93d872cc7a788555c6226fa8644dc7f132a2fab56aa54a391065f09f2440 |

manifest.json pins each source commit/blob/hash, patch hash and patched-byte
hash. Those are provisional draft inputs, not entries in the round's final
freeze table. No candidate source or patched program is copied into this tree.
The source commits remain on their existing separate staging branches.

## Intended edits, read statically

- MU-C1 changes A's instance T from 1 to 2. Its eventual required killer is PR-E.
- MU-C2 adds one bit flip in B's already-built inverse matrix, row 0 column 0,
  inside build_instance. The row-bit representation makes this one matrix-entry
  change; its eventual required killer is CC-BIJ.
- MU-C3 replaces A's single ratio helper's Fraction return by floating division.
  Its eventual required result is A's exactness exit 3, including MU-C3-prime
  through SF-3 before F once the adopted fixture route exists.

No kill outcome above has been tested or certified. These patches must be
regenerated and independently reviewed against the final revised source bytes.
Copying the current hashes into controls.py or the freeze table would be wrong.

## Static verification recipe

With this staging checkout and the two source commits available in its Git
object store, from the repository root:

    python3 -I -B verification/programmes/oi-qm/reconstruction/round-k1-p1-1/draft-patch-staging-20261108/check_static.py > /tmp/k1p1-draft-static.json
    cmp /tmp/k1p1-draft-static.json verification/programmes/oi-qm/reconstruction/round-k1-p1-1/draft-patch-staging-20261108/static-validation.json

If necessary, fetch the source commit IDs above from this same repository
before using the recipe. The checker reads Git blobs only. It verifies hashes,
exact one-file/single-hunk splicing at the stated line numbers without offset
or fuzz, the intended byte edit alone, and Python syntax via ast.parse. Eight
malformed-patch controls per patch must be rejected: wrong target, old offset,
new offset, count mismatch, truncation, extra file header, shifted context and
missing final LF. They test patch mechanics, not physical or mathematical
mutation killers. The checker is a staging audit, not the future controls.py
patch applier or a substitute for independent code review.

No A, B or controls module is imported or executed; no map is evaluated, fixture
answer derived, fixture run performed, or K1 instance/state generated. A1's
fixture JSON, its constants and the full synthetic gate are not staged here.
There is no workflow edit, dispatch, V3 execution or special launch.

## Gates that remain

Revised independent A/B/controls deliveries, independent static and fixture
answer reviews, qualifying approved-interface tests, actual final code and
patch pins, the byte-identical integration fixture copy/head, exact X5 edit,
and applicable CI remain outstanding. The full patch-dependent self-test is
not qualified by this package. Approval (b), F, K1-instance computation, E,
receipt, merge and scientific-status promotion retain their separate gates.

Only this dedicated branch receives the draft patches. The pre-F round branch
receives no patch or final pin under this authorization. Ordinary CI on the
unchanged round head does not validate these staging bytes. Before publication,
the writer checks push triggers; these paths do not start a push workflow.
