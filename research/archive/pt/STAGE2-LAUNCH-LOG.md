# Stage 2 launch log (coordinator; scratchpad record)

- Protocol `PROTOCOL-STAGE2.md` was written and frozen before launch 1: mode 444, sha256
  `386036921cd55ed976884aa97c548b0440024d5d1a7be493395784dce2da18da` (in `PROTOCOL-STAGE2.sha256`). It is unchanged
  since then.
- **Launch 1, 2026-10-10 ~07:12 UTC.** Threads S3 and S2 were launched with the prompts recorded in the coordinator's
  session. Both were terminated by the account's weekly usage limit (HTTP 429) during their first step, before any
  substantive work.
  - S2 wrote nothing.
  - S3 wrote only `S3/.start_marker`, at 2026-10-10T07:12:54Z. It records all start checks as OK.
- **Disposition.** S3's marker was moved, unchanged, to `aborted-launch1/S3/.start_marker`:
  - sha256 `77c4f57a97d23a227eef1cf6e3cbacd8f16cdff6964f6127a269e2233f0bc01f`;
  - 970 bytes;
  - mtime 2026-10-10 07:12:54.752503928 +0000.

  Nothing else was written after the protocol was frozen. `S2/` and `S3/` are empty again.
- **Pre-relaunch verification, 2026-10-10T07:25Z.** All passed:
  - the archive `evidence/pt-stage1-evidence.tar.gz` has sha256 `128ae0dd…4dd28`, as delivered;
  - the `inputs`, `stage1` and `inputs2` manifests are OK;
  - the four protocol hashes are OK;
  - base HEAD is `9f9f8257…`, with empty status;
  - the repository working tree is clean.
- **Launch 2:** the same prompts; see the coordinator's session for the time.
