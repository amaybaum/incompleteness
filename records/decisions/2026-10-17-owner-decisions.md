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

## Preservation and archiving (later on 2026-10-17)
The owner approved the recommendations, reconsidered against AGENTS §A.42 and §A.28: "Approve the recommendations,
proceed with the off-main design refresh."

- **Archiver pilot: accepted** under the pre-set rule (`VALIDATE HOLDS`, run 39008888084). The acceptance covers
  integrity within GitHub's infrastructure only.
- **388-run raw-log archive: not published.** Raw logs are not evidence under §A.42 item 1. Cited CI runs are
  retained as expected results with recipes, like tranche 1, or recorded as gaps. This is to be done before the
  earliest log expiry on 2026-12-17, as a separate reviewed change. No release assets or log refs.
- **Off-main objects, Q1–Q8:**
  - Q1: inside `verification/audits/evidence-retention/` (§A.42 item 3).
  - Q2: small raw outputs withheld (item 1).
    - Clarified by the owner later on 2026-10-17: "The withholding policy covers non-empty captured raw run
      outputs, including .out and .err, plus the three identified .txt outputs approved later. Empty, zero-byte
      outputs may remain stored; documenting all four paths is appropriate." Also: "extensions alone must not
      authorize withholding"; the reviewer verifies that the exact withheld paths match the approved scope,
      including against coordinated manifest/list edits.
    - The three .txt outputs (Rall_39.txt, Rle13_39_a.txt, Rle13_39_b.txt under 1f19a347) were approved for
      withholding on 2026-10-17, after the first review of the tranche.
  - Q3: PDFs withheld. CONSC-2's preregistration :516–517 says their bytes are not frozen.
  - Q4: uncited parents named, not retained.
  - Q5: hybrid layout, as prototyped.
  - Q6: the R3 pair and BG-3's heads join the first tranche.
  - Q7: id discrepancies cross-reference the landed provenance errata PE-1..PE-5 (#855); no native round.
  - Q8: identity exemption only for addresses present in main's history, verified by the checker; no hiding by
    compression.
- **First tranche:** host-unreferenced objects plus R3 and BG-3. Branch-held objects follow later; the no-delete rule
  protects them meanwhile.
- **Recovery bundles:** stay on the handoff branch. The off-GitHub copy is the owner cloning that branch locally.
- **The refresh** is rebased on main `49ba3297`, kept on a `wip/*` branch until independently reviewed, with no PR.

## Branches (owner, later on 2026-10-17)

- Keep the evidence branches for now: `research/wip-checkpoints`, this handoff branch, and the R1 and preservation
  recovery branches.
- Merged working branches can go; the repository's automatic head-branch deletion on merge is acceptable. No other
  branch cleanup is needed.
- The F2 text corrections at `804843f1` are authorized to land on `research/f2-extension-candidates-20261014` only.

## #829 checker review (owner, later on 2026-10-17)

**Decisions**
- The checker review passes at `9a37144796f93bddba695472e72b2ae6c5975552`, and both reported defects are resolved.
  This clears the checker blocker for run 2.
- This does not designate F or authorize merging.
- Evidence retention and the evidence pins remain required before F.

**Recommendations (owner), not decisions**
- Keep `if: ${{ !cancelled() }}` on the A3 step.
- Push exactly `6959ced4c327ebb800cf6d463a049e4066e37288`, verify its remote files against the reviewed package, then
  launch the single remaining design run.

The owner's verification scope and the reviewed objects are in `records/k829/REVIEW-9a371447.md`.

## #859, F2 decision memo (owner review, earlier on 2026-10-17)

**Recommendations (owner), not decisions.** The memo records each as "recommended (owner), open".
- Target: exact operational QM on qubit-power registers first.
- The eight revised admissibility gates.
- The monitored law is preserved on retained original protocols only, with an explicit embedding and a compatibility
  check. A failure there is an obstruction to report.
- Necessity: holds-in-target plus drop-one countermodels. Global minimality and full-framework independence stay open.

**Qualifications (owner)**
- Conditional mathematics may proceed: the #829 checker repair, #831 control preparation, and #822 relative-form
  drafting.
- Candidate-dependent decisive testing needs these choices fixed first.
- #829 → #831 → #822 is the preferred order, not a required one.
- #853 and #838 need their pre-F evidence and controls reviewed before any F.
- A round is re-cut only before F. Once frozen, it follows its lifecycle and reconciles after E.

Memo: `plan/f2-target-extension-scope-20261017` at `362131e0` (draft PR #859). The previous commit, `28e9c06f`, carried
DEC-ADOPTED labels for recommendations, which `362131e0` corrected.
