# Retained review records

The review records of `../PREMISE-MEMO.md`, kept verbatim. `SHA256SUMS` carries the digest of every file here. They
are provenance for the memo's [W, rev] and [NR, rev] citations and for the review status stated in `../CORRECTIONS.md`.
They are not replayable evidence for the memo's computations, which rest on `../dc_premise.py`, `../witness_check.py`
and `../compression_check.py` and their outputs.

## PR #864 comments

Each `comment-<id>.md` is the comment's `body` field exactly as the GitHub REST API returned it (UTF-8, no newline
added or removed).

| comment id | kind | file | author | created_at | updated_at | html_url | sha256 of body |
|---|---|---|---|---|---|---|---|
| 6254408285 | independent review of the original memo | `comment-6254408285.md` | amaybaum | 2026-10-18T19:53:24Z | 2026-10-18T19:53:24Z | https://github.com/amaybaum/incompleteness/pull/864#issuecomment-6254408285 | `5473dd69f2dfedba566f0fcac881856b7eb64fbf155af66c734ad919eb2de30e` |
| 6254747204 | independent review of the first-pass correction | `comment-6254747204.md` | amaybaum | 2026-10-18T20:26:42Z | 2026-10-18T20:26:42Z | https://github.com/amaybaum/incompleteness/pull/864#issuecomment-6254747204 | `d9c42604ac5cfa4273d987969b2bf00a5c114b0efe42acc2b842561e61e58c9a` |
| 6254962113 | independent review of the second-pass correction | `comment-6254962113.md` | amaybaum | 2026-10-18T20:47:48Z | 2026-10-18T20:47:48Z | https://github.com/amaybaum/incompleteness/pull/864#issuecomment-6254962113 | `0d46afb06acb9849b707dc5ae89e122e3c54aca06931bb6cb4370cad981205b2` |
| 6257588156 | the corrector's checkpoint for the third pass, not a review; it reports the third-pass review's verdict at second hand | `comment-6257588156.md` | amaybaum | 2026-10-19T01:16:31Z | 2026-10-19T01:16:31Z | https://github.com/amaybaum/incompleteness/pull/864#issuecomment-6257588156 | `9213042898a99d4a18adc287394833e78e7daa8b9504bbfb9f582293f44726c6` |

**Provenance.** Each body was fetched read-only with `GET /repos/amaybaum/incompleteness/issues/comments/<id>`: the
first three at 2026-10-19T11:41:39Z–11:41:40Z, 6257588156 at 2026-10-19T12:11:10Z. Each body is byte-identical to an
earlier fetch of the same comment that day, and `updated_at` equals `created_at` for each, so none was edited after
posting. The author field is the GitHub account that posted the comment; each review states in its text that it ran
read-only. Comment 6257588156 calls itself a "WIP checkpoint; not a merge request", and its text matches the
corrector's draft of it in the corrector's working directory, apart from the blank line before its footer; the review
it reports is `third-pass/REVIEW.md`. Before retention the bodies were scanned for tokens, keys, signed URLs, IP and
e-mail addresses; none was found and nothing is redacted. No body names a CI run.

## Third-pass independent review (`third-pass/`)

The complete independent review of the third-pass correction (commit `a147aa3a`), kept verbatim. These are local files
from the reviewer's working directory; they were never posted.

| file | sha256 | bytes | written (mtime, UTC) |
|---|---|---|---|
| `third-pass/REVIEW.md` | `e5d3c8c7e40d20a5eeb00074b4385b934ff284155a9c6804f78869320fef29ea` | 10507 | 2026-10-19T01:15:13Z |
| `third-pass/rv_mev.py` | `d264de654943745294371661184da0ef05b913ff385635e3be9bf5cd4df3261c` | 4195 | 2026-10-19T01:11:58Z |
| `third-pass/rv_mev.out` | `1bfd506fa57c040d602e3579a8833b63e04535c8d29fae8167c1f65029142913` | 959 | 2026-10-19T01:11:59Z |

**Provenance.** Written on 2026-10-19 by the independent third-pass reviewer, and copied byte-exact from the local
working directory where they were written. `REVIEW.md` states the verdict ACCEPT-WITH-NITS and the findings N1, N2, O1
and O2. Its text names local working paths and the commit-author address `noreply@anthropic.com`, which also appears in
the commit objects already retained on `main`. It contains no token, key, signed URL, IP address or CI run number, and
it is kept unredacted.

**What `rv_mev.py` checks.** Exact SymPy checks of the MEV/OV-LU counterexample X_c = I/2 − (53/100)P_v, with
v ∝ 4|00⟩ + |11⟩:
- X_c is not PSD (minimum eigenvalue −3/100);
- its minimum over maximally entangled projectors is 15/136, attained at Φ+, and its minimum over product vectors is
  1/850;
- CN(e_v⊗P_0)CN = P_v, and the product test after the coupling has value −3/100;
- X_c's even block has eigenvalue −3/100;
- B = CN(|+⟩⟨+|⊗P_0)CN = |Φ+⟩⟨Φ+|;
- Tr(P_ψX) equals the product test |+⟩⟨+|⊗P_0 after I⊗W and the coupling, for symbolic X and unitary W.

It includes a countercontrol (a PSD state passes the product test), a mutation (c = 1/2 gives 0), and one
floating-point sampling line that its own text labels evidence only. Recorded output: 17 PASS, 0 FAIL. Replayed under
`python3 -I -B` on 2026-10-19: rc 0, byte-identical to `rv_mev.out`, twice.
