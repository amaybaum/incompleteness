# DESIGN-v5.3: changes against DESIGN-v5.2

## Inputs

I verified the sha256 of each input before use:

- `DESIGN-v5.2.md`: 195d1e288b1d6750c333b4707332868d351926793ad2b2a555d64e3bd78f4aeb.
- `review-v5.2/review-v5.2.md`: 15260f0957ba81bb555c413a7e73db201a828f059a073a601fbe471da2c34fd0.
  Its verdict is REVISE, with two blocking points: V1 (pass condition 2) and V2 (pass condition 4).

I read the review's scripts. I re-derived its parity cases with my own script against P's verified
code.

## Limits

- Paper-only: no repository, git or GitHub write, and no workflow run.
- The Stage 1 worktree was not touched. I read one engine file, `engine/rules.py` at 8c1e628a, from
  the object store, to state the context-hash definition.
- New scripts are in `work-v53/`. They read git objects only.
- No safeguard was weakened. Every change adds a check or narrows an allowance.

In this file, V1-V8 and O1 are the v5.2 review's items. The design's adversarial controls V1-V27
are named "control Vn".

## 1. Required corrections

| Item | DESIGN-v5.3 sections | What changed | How verified; figures re-derived |
|---|---|---|---|
| V1 (blocking): register and infinity parity with P | 6.1 (semantics rewritten); 11 rows 5 and 6; 10.4 (S11-56 restated, S11-57a-d added); 16.2 (extractor `python-ast-call-arg`) | See "V1 in detail" below the table | `work-v53/units.py`, with P's blob imported under `-I` after a hash check. 401 edits and 399 splices; all 399 splices are byte-identical to their edits; D032 and D039 are the only edits without a splice; no edit has a second step. P's `static_new` gives 0 / 0 / 0. Cases (a)-(c) give register 1 under P's per-edit check and 0 under the per-splice rule, which reproduces the review. All re-derived |
| V2 (blocking): `F`'s designation from outside the caller and outside `F` | 6.3 (admission rewritten, points 1-7); 5 (acceptance requires a host CI run's own artifact); 16.7; 10.4 (TR1-TR13); 15 item 0a | See "V2 in detail" below the table | Textual, against review points (i)-(iii) and the refusal cases the owner listed: missing designation (TR6), designation in `F`'s tree only (TR6), wrong author (TR7), a different commit (TR8), caller-supplied identity (TR9), a caller-built `F` (TR10). TR5 (positive) and the host reads run only in CI; the rest can run on API fixtures |
| V3: tool-landing class bound to exact blobs | 13.1 (`M`, side changes) | A prefix only locates paths. The class lists every landed path with its exact blob, and only listed paths with matching blobs are classified. The class record itself is pinned by the configuration | Control R19 (an unlisted path, a changed blob) |
| V4: controls for R3, R5, R6, R8, R10, R11, R12 | 13.2 (N12-N18); 13.3 (control map R1-R13) | One control per reconciliation condition; the inaccurate "N4-N9" sentence is replaced by the full map | Textual: every one of R1-R13 has exactly one named control |
| V5: context hash, location, deterministic grant | 6.2 (new paragraphs "The fingerprint's context and location" and "One grant, deterministically"); 10.4 WB9, WB13, WB14 | See "V5 in detail" below the table | Definition taken from the Stage 1 engine (`engine/rules.py`, `sentence_context_sha`), which computes exactly this. WB13 and WB14 added |
| V6: SW2 reference | 10.3 SW2 | 14 sites carry HP items at the unmutated H: the 7 meaning-context FAILs and the 7 structure REVIEWs, named. The review's 584/584 run with the Stage 1 engine under the tuple predicate is recorded | The 7 + 7 sites are the IR and S1 figures of sec. 0.3 and 4.4; not re-run |
| V7: native execution at `C` | 7.2; 10.4 G9 | A second disposable full clone at exact `C` when `C ≠ X`, with the same recording and re-derivation. A class PASSes only if it PASSes at both `X` and `C` | Textual; control G9 |
| V8: N10 pinned to the S6 probe | 13.2 N10, N11 | Exact inputs: `M` 8e9b8334, `X` T1', landing `AGENTS.md` 9f4fc3e8, record `l` 9f4fc3e8, reference composition 86d79863. N10 expects `landing-conflict-unresolved` and `record-invalid`; N11 is the positive direction at the same inputs | `work-v53/ci.py`: `AGENTS.md` at `M` is 6b1280fa, at T1' 9f4fc3e8; D296's `old` bytes are unique at `M` at offset 2332; the composition is 86d79863821f3f8cdad86771008b2df89fd1961a. Re-derived |
| O1: case-insensitive negative literals | 6.2 ("Case") | Literal negatives of every allow rule (W1, W2 and later rules) are matched case-insensitively, and allowances count case-insensitive matches. Applying it beyond W1 is stricter, and it changes no real-tree outcome | `ci.py`: on all 7 W1 and 4 W2 sentences at T1', case-insensitive counts equal case-sensitive counts (W1-c: one `finit`). Control WB15 added |

**V1 in detail.**

- Items 5 and 6 are now defined on P's unit. For every frozen edit, the tool evaluates `(old, new)`
  and `(old_step2, new_step2)` exactly as `static_new` does:
  - REG: set difference per pair;
  - CAPS: per pair, restricted by the edit's own `kind`;
  - INF less NEUTRAL: split with **P's splitter**, `re.split(r'(?<=[.;:?])\s+', t)` (stated
    explicitly; not splitter v2), with P's rewrite and P's `inf_key` normalization, as a multiset
    difference.
- In addition, the per-splice unit runs, and a FAIL from either unit is a FAIL.
- A fail-closed edit/splice correspondence check runs in the integrity stage. Any relation other
  than one splice per edit, with byte-identical old and new text, or the result of both steps for a
  two-step edit, gives ERROR `SOURCE_CHANGED`.
- P's split regex is extracted from P's `sentences` function. The edit kinds, key rule and rewrite
  are kept in a reviewed rule file, linted against P's source.
- Controls added: S11-57a (re-added "now", two-step), S11-57b ("no longer" added then removed),
  S11-57c (one splice over two edits) and S11-57d (P's splitter).

**V2 in detail.** `F` is designated only by the owner's host comment that quotes `F`'s full id, in
the thread the plan amendment names. The tool reads it from the host API inside the CI job, along
with the whole thread. The owner's identity is the repository owner as the host reports it for the
job's own repository; it never comes from an argument, the environment, the configuration or `F`'s
tree. The comment must meet all of these:

- it is by that owner;
- it quotes exactly `F`;
- it has not been edited since creation;
- no later owner comment in the thread supersedes it.

Further changes:

- The pin table is authenticated only by that designation of exactly `F`.
- A record of the designation inside `F`'s tree is never read for admission.
- Local runs can never reach `"chain"`.
- The acceptance predicate also requires that the result is the uploaded artifact of a host CI run
  on the evaluated commit, read from the host API by the consumer.

**V5 in detail.** The context hash is
`sha256(utf8(prev) || 0x00 || utf8(next))` over the file's sentence list under splitter v2.
Neighbours may cross paragraph boundaries, and `BOF` and `EOF` are the sentinels. "Location" means
this pair of neighbours. It is not a position. So a shift (WB8) keeps the allowance, and so does a
move of the sentence together with both neighbours (WB13, expected PASS). A move of the sentence
alone loses it (WB5). When several sentences qualify, the grant goes to the smallest byte offset
(WB14; WB9 restated).

## 2. Unchanged on purpose

These are unchanged from v5.2:

- every deny rule;
- `resid`;
- the W1 allowance values;
- the item-7 check;
- D2-D8 apart from SW2's reference;
- B1 and B3-B6 apart from admission (V2);
- S2-S7 apart from V3, V4 and V8.

Optional points O2 (keep O6 and O8 deferred) and the earlier deferred points stay deferred.

`diff DESIGN-v5.2.md DESIGN-v5.3.md` has 25 hunks. The document grows from 2414 to 2533 lines.

## 3. What I could not follow or verify

- **V2 needs the plan amendment.** It must name the designation thread and the designation form.
  Until it does, the host checks cannot run, and TR5 (positive) is possible only in CI.
- **V2's owner rule may need the owner's confirmation.** I chose the repository owner as the host
  reports it for the job's repository. If the owner wants a different host source of identity, the
  rule's point 2 must change; any replacement must still be one the caller cannot choose.
- **Two V2 checks are new behaviour I introduced.** "Unedited since creation" and "no later
  superseding comment" are my strengthening, so that the caller cannot select an old or edited
  comment. The owner may wish to confirm them.
- **The correspondence check of V1 assumes a two-step splice.** For a two-step edit, it requires the
  splice's image to equal the result of both steps. A1 has no two-step edit, so this is untested on
  real data.
- **S11-57d is a splitter-level control.** I did not construct an infinity case whose verdict
  differs between the two splitters, so the control checks that the tool splits as P does and that
  its result equals P's.
- **Not re-run:** SW2, the S6 probe in the tool, and the Stage 1 engine. N10's inputs were
  re-derived from git objects only.
- **Comment ids.** None is held for any owner decision.
