# Owner decisions, 2026-10-17 (off-repo record)

## Thread A, hvalid
- **Label:** HVALID-INDEPENDENCE-SUPPORTED.
- **What the countermodel establishes:** valid subsystem states do not, on their own, guarantee valid joint
  measurements. The witness is H = diag(-1,1,1,1). It lies in K2 = {H : λ1 + λ2 ≥ 0}, both of its partial traces
  equal diag(0,2), and ⟨00|H|00⟩ = -1. Marginal validity in general follows from the Ky Fan bound.
- **Scope:** the independence verdict stays tied to Thread A's stated compatibility assumptions.
- **Still open:**
  - observer-level sourcing, until the Origin_K/Origin_M decision;
  - neither K2 nor Kₙ is marked resolved on this basis.
- **Candidate route:** the pair is itself an observed stage. This is a candidate, not an adopted principle.
- **Next step:** the result can become a separately reviewed research result, but not yet an adopted physical
  principle.

## Archiver
- The design is approved in principle.
- One four-run pilot push to an isolated `tmp/log-archive-*` branch is authorized. It is subject to:
  1. an independent source review;
  2. fail-closed completeness;
  3. bounded execution;
  4. no publication;
  5. completion of #854's remaining reproduction (run 38997947966).
- Full 388-run processing and durable publication are separate decisions.

## Unchanged
No merge, F designation or durable-log publication is authorized. #854, #855, LOC-1 and the research threads stay
on their established paths.

## Scratch cleanup (Tier 1)
- **Verdict: CLEANUP-ACCEPTED.** 17 of 19 paths deleted, 8.97 GB recovered, 13.47 GB free. The ledger is in
  `decisions/cleanup-20261017/` with SHA256SUMS.
- **Kept, with conditions:**
  - `agent-r2b/u4.git`: until its borrowers are self-contained and verified;
  - `agent-accept/host.git`: its 25 unique synthetic-merge commits are to be kept; a verified bundle may be considered
    later.
- Tiers 2 and 3 are kept. No further deletion, `git gc` or restructuring.

## Archiver pilot
- **Execution behaviour accepted,** including the attempt-2 job-log semantics.
- **Archival integrity not yet accepted:** that waits for the independent artifact validation, Route B.
  - **Route B:** a parentless branch `tmp/artifact-validate-20261017` with a read-only, SHA-pinned workflow. It
    hashes the original zip bytes taken from the REST endpoint, and the API request's endpoint is checked.
  - **Verdicts:** HOLDS, FAILS or UNVERIFIED; FAILS and UNVERIFIED never count as HOLDS.
  - A pass establishes validation within GitHub's infrastructure, not off-GitHub preservation.

## #855 and #854
- **#855:** one exact-head run at `8021c1fc` is authorized, then an independent acceptance review. It stays a draft
  and is not merged.
- **#854:** pushing the independently reviewed SHA is authorized. Then exact-head CI, and the positive and negative
  reproductions the fix affects. It stays a draft and is not merged.
