# Retained review comments

The three independent reviews of `../PREMISE-MEMO.md`, kept verbatim. Each `comment-<id>.md` is the comment's `body`
field exactly as the GitHub REST API returned it (UTF-8, no newline added or removed); `SHA256SUMS` carries their
digests. The comments are cited in `../PREMISE-MEMO.md` and `../CORRECTIONS.md` by their ids.

| comment id | file | author | created_at | updated_at | html_url | sha256 of body |
|---|---|---|---|---|---|---|
| 6254408285 | `comment-6254408285.md` | amaybaum | 2026-10-18T19:53:24Z | 2026-10-18T19:53:24Z | https://github.com/amaybaum/incompleteness/pull/864#issuecomment-6254408285 | `5473dd69f2dfedba566f0fcac881856b7eb64fbf155af66c734ad919eb2de30e` |
| 6254747204 | `comment-6254747204.md` | amaybaum | 2026-10-18T20:26:42Z | 2026-10-18T20:26:42Z | https://github.com/amaybaum/incompleteness/pull/864#issuecomment-6254747204 | `d9c42604ac5cfa4273d987969b2bf00a5c114b0efe42acc2b842561e61e58c9a` |
| 6254962113 | `comment-6254962113.md` | amaybaum | 2026-10-18T20:47:48Z | 2026-10-18T20:47:48Z | https://github.com/amaybaum/incompleteness/pull/864#issuecomment-6254962113 | `0d46afb06acb9849b707dc5ae89e122e3c54aca06931bb6cb4370cad981205b2` |

**Provenance.** Each body was fetched read-only with `GET /repos/amaybaum/incompleteness/issues/comments/<id>` at
2026-10-19T11:41:39Z–11:41:40Z. The bodies are byte-identical to an earlier fetch of the same comments that day, and
`updated_at` equals `created_at` for each, so none was edited after posting. The author field is the GitHub account
that posted the comment; each review states in its text that it ran read-only. Before
retention the bodies were scanned for tokens, keys, signed URLs, IP and e-mail addresses; none was found and nothing is
redacted. No body names a CI run.
