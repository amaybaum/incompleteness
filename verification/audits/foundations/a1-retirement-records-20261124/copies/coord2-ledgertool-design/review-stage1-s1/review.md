# Independent review of the S1 corrective delta, head 443e871f

Subject: 443e871f225a414f69bef3f1e3cab45cb30d6594 (nine single-parent commits on 9da5dd5f, branch
tools/ledger-coverage-20261123, unpushed). Design: DESIGN-v5.5.9.md, sha256 cdfbe08c...79df9 (verified). Scope:
OWNER-DECISIONS-Q.md and PLAN.md sec. 1 P1-P6. Reviewer wrote none of the subject. Writer evidence MANIFEST
66f7df32... verified (`sha256sum -c` OK). Read-only: no commit, push, PR, GitHub write or dispatch; GitHub GET only.
`S/coord2-impl-wt` untouched (HEAD 443e871f, clean). My detached worktree was removed with `git worktree remove`.

**Verdict: ACCEPT-WITH-NITS.** No demonstrated defect or counterexample against v5.5.9 or an agreed pass condition.
One owner finding (REST cost) blocks TR5 and acceptance in CI as the reader stands, but not this delta.

Labels: [real git] local git objects; [real host] GitHub GET; [simulated] fake host; [NOT RUN].

## 1. P1: A and the freeze ledger leave the landing

- [real git] `git diff --name-status 9da5dd5f 443e871f`: D authority.json, D freeze/freeze-ledger.json, D evidence/
  stage1-controls.json, D workflow-draft/ledger-coverage.yml; M host.py, a1_controls.py, conformance_controls.py,
  purity.py (comment only, 1 line), README, class record; A rest_fixture.py.
- Nothing in the tree reads the removed files: the only remaining mentions are the engine's fixed path constant
  (`authority.py`, `checker.py`, `purity.tool_paths`), fixtures (`syn/...`), and the README. No JSON record names them.
- No check weakened: the removed lines of `conformance_controls.py` are only the three list lines extended to add
  S1-P2 (group list, must-be-reported list, group-name list). Z9h's function is byte-identical (AST) at 9da5dd5f and
  443e871f; `purity.py` changes one comment line only.
- Class record `tool-landing`: 54 pins; equal as a set to `git ls-files -s` of the landing paths less the record;
  every git_blob and blob_sha256 recomputed equal; all mode 100644. Record blob 6ef7c891..., sha256 416f4685...0fbf.
  Staged config 75558ee3... differs from r8's 83c81a65... only at `records[1].blob_sha256` and
  `roles.side_change_classes.blob_sha256` (534e96bd -> 416f4685).

## 2. Q2: stale evidence and workflow draft

- [real git] Archive `S/coord2-stage1-evidence-archive/`: `git hash-object` gives 544f8bc9... and 597fd397..., equal
  to `9da5dd5f:<dir>/evidence/stage1-controls.json` and `.../workflow-draft/ledger-coverage.yml`; its MANIFEST checks.
- My reading of AGENTS.md at origin/main (§A.50 item 3; §A.42 items 5-6; §A.46 item 6): not a deletion of evidence.
  §A.42/§A.46 govern removal from `main`; neither file was ever on `main` or pushed. The removal is a new commit, so
  the blobs remain in 9da5dd5f, an ancestor of the head; if the branch lands through `U` and `L`, both blobs become
  reachable from `main` through `L`'s second parent. §A.50 item 3 is about destroying evidence (branches, Issues, PRs,
  evidence); nothing is destroyed here, and the owner's Q2 explicitly directs the removal from the landing with
  preservation. I agree with the writer. Nit N4: the scratch archive is disposable (§A.40); the durable copy is the git
  history, which exists only on this unpushed local branch until it is pushed.

## 3. P2 (decisive): RestHost.file_history and on_first_parent_chain

Code read in full. `first_parent_chain` pages the unfiltered `commits?sha=<head>` listing (pinned to a commit id),
accumulates every entry, follows first parents to a parentless commit; a short page or `max_pages` before the root
raises. `file_history` walks the chain root-first, reads each commit's entry for the path through cached
non-recursive trees, compares blob ids with the previous chain commit (= first parent), raises on a non-regular entry,
checks fetched bytes against the blob id (sha1 of `blob <n>\0...`), reads the merge record per version. This matches
v5.5.9 sec. 6.3 ("every change to `A` on `main`" on the first-parent chain; deletion refuses downstream in
`authority.py`).

Independent fake host (`scripts/gitrest.py`): REST answers served from REAL local git repositories (real object ids,
real `git rev-list -- path` simplification), not derived from the writer's fixture. `scripts/attack_reader.py`,
results `results/attack-reader.json`. All [simulated, real git objects]:

| Attack | Result |
|---|---|
| add on a branch merged `--no-ff` (first parent lacks the file), modify by merge, delete by merge, re-add the first blob by merge (revert), squash commit, `-s ours` merge (no version), evil merge | new reader == git first-parent truth: 6 versions m1,m2,m3(deleted),m4(blob = m1),s5,m7; `-s ours` not a version; same in date, topo and random listing order |
| path listing | omits m1-m4 (merges); old reader (`rest_fixture.old_file_history`) returns only s5, m7: old failure reproduced |
| committer clock skew, 150 commits | equal to truth |
| pagination: linear chains of 99/100/101/199/200/201 | equal; pages read 1/1/2/2/2/3 |
| root holds the path | root is the first version |
| force-pushed main: head re-read after rewrite; old head still served; later pages served from the other head | exact for the head read; old->new mixed pages exact; new->old mixed pages HostUnavailable (never a wrong answer) |
| symlink / directory / submodule at the path | HostUnavailable "not a regular file" |
| intermediate component is a symlink | absent (equals git truth) |
| mode 100644 -> 100755, same blob | not a version (equals blob-id truth) |
| 403 rate limit mid-walk, 429 on pulls, 500 on tree, 403 on contents, root dropped from listing, corrupt bytes, max_calls one short | HostUnavailable in every case |

Default transport (`scripts/real_transport.py`, real urllib code, local HTTP server) [simulated host]: 403, 429, 500
-> HostUnavailable. A 200 non-JSON body and a tree entry without `sha` raise JSONDecodeError / KeyError instead (nit N1).

Writer's fake [simulated]: S1-P2-LISTING, -OLD, -NEW, -ADMIT (old reader: exit 65 CONFIG_UNREVIEWED; new: exit 0),
-SQUASH, -REVERT, -CHAIN, -FAILCLOSED all PASS in my run.

Real host [real host, GET only via `gh api --method GET`, `scripts/probe_real.py`, `results/real-host-probe.json`],
main pinned 8e9b8334, path AGENTS.md, 2026-11-24T07:04Z:
- commits-by-path listing: 133 commits; contains 8e9b8334 false, 4fb2c1ee false; one listed commit (47365b03) on the
  chain.
- subject reader: 60 versions, contains 8e9b8334 and 4fb2c1ee true; newest bytes equal local `8e9b8334:AGENTS.md`;
  newest merge record: merged_by 7273571, merge_commit = commit, parent 4fb2c1ee. 1415 REST reads.
- independent check (my own chain from the listing, blob ids from the contents API, not the trees API): chain 1181 to
  root a3e1f097, 60 versions, equal to the subject's list; 59 of the 60 are merge commits. 1240 reads.

## 4. REST cost (owner finding, not fixed)

- Measured [real host]: 1415 reads for one depth-1 path (59 listing pages, ~1176 root trees, 60 contents, 120 pull
  reads). For `A` (depth 3) and the ledger (depth 6) the root trees are shared, but each changed subtree on the way is
  one more read. Local estimate over the 146 local first-parent commits: 146 root trees + 252 distinct subtrees on the
  two paths (verification 121, audits 80, foundations 47, tools 4), i.e. ~2.7 tree reads per commit. Scaled to 1181:
  of the order of 3,000-3,500 REST reads per admission (estimate, not measured), plus 2 contents per version in
  `_provenance_problem`, plus run/K7 reads. `comments()` adds one GraphQL query per comment (605 in #1169).
- GitHub documents the GITHUB_TOKEN limit as 1,000 REST requests per hour per repository (15,000 for
  enterprise-owned resources). The gh token here shows core 15,000, which is a user token and says nothing about the
  job token. Under 1,000/h an admission exceeds the limit; GitHub returns 403/429, which the transport maps to
  HostUnavailable -> ERROR CONFIG_UNREVIEWED. So it fails closed (no false acceptance, shown above), but TR5-positive
  and every acceptance admission in CI would refuse. This blocks TR5/acceptance as the reader stands, and should be
  settled before `A` pins the engine (an engine change afterwards needs an authority change). It does not violate
  v5.5.9 and is not a defect of S1. The step 7 host-api job should measure `GET /rate_limit` under the job token.
- GraphQL alternative (paper only, no POST): `object(oid:<main>){... on Commit{history(first:100){nodes{oid
  parents(first:2){nodes{oid}} a:file(path:A){oid mode type} g:file(path:G){oid mode type}}}}}` pages the unfiltered
  history (no `path` argument, so no simplification). That is ~59 pages at about 2 points each, ~120 points for both
  paths together. The chain and the per-commit comparison are computed locally exactly as now, with the same
  fail-closed rule (root not reached -> refuse). Version bytes come from REST contents with the same sha1 check, and
  merge records come from REST pulls or `associatedPullRequests` (aliases batched), for about 2 x versions. Comments
  batch through `nodes(ids:[...100])`, ~7 queries for #1169 instead of 605. Caveats: GraphQL's job-token budget
  (documented as of the order of 1,000 points/h) and secondary limits; `file(path:)` semantics for symlink and
  submodule entries; the result must be cross-checked against the REST reader on the real host before adoption.

## 5. P5, P6, Q8, Q10

- P5/Q11: README "Comments in governed threads" documents the guard; no admission code changed (host.py, authority.py
  untouched except the reader).
- P6 [real git]: no `--main` -> exit 2 "--main is required"; `--main deadbeef` -> exit 2 "does not resolve"
  (`^{commit}` required); `--main 8e9b8334` -> RT-L2 PASS, finding text names 8e9b8334. `a1_conformance.py` keeps
  its fixed M for N10/N11 (fixture, acceptable).
- Q8: every ledger the fixtures build is `{schema, events}`; S1-Q8 PASS; README states it.
- Q10, completeness [real git + real host compare GET against 8e9b8334]: full-length commit ids in the 55 landed
  files: 14ac71b4 (T1') diverged; 4c79be64 (P) diverged; 413b0bb8, 53c6601a, ca3a5bb2, e837e3db, 4fb2c1ee: ancestors
  (status "ahead"); 8e9b8334 identical. Abbreviated ids that resolve to commits: only 4fb2c1ee and 8e9b8334. Of the 56
  cited blobs, only 9f4fc3e8 (T1''s AGENTS.md) lies outside main/H/E/W/the landing. 86d79863 exists nowhere (404 on
  the host), as the writer reported. The writer's list (T1', P; plus 9f4fc3e8 and 86d79863 noted) is complete and
  correct.
- Q10 is not resolved: the owner decision says "resolve the two off-main citations before landing". The README
  narrows the control results to provenance, but the writer's own table leaves six load-bearing records (`rules/*`
  `recorded_at` T1'/P, `repo-scope` at P, `gr58` at T1') "for the owner". Nit N3: the README labels the whole group
  "provenance only", and §A.42 item 8 says that label is "a finding about each reference, never a label applied to a
  group". The per-file classification exists in EXACT-DELTA, not in the landed text. This is a precondition for
  landing, correctly flagged and not a defect of S1.

## 6. Regression and mutation

[real git] My detached worktree at 443e871f, the writer's staged config 75558ee3..., `--main 8e9b8334`
(`scripts/repro.sh`, `results/full/`):
steps 1-5 exit 0; 6a exit 2; 6b (bad main) exit 2; step 6 exit 1 (RT-T NOT RUN, as at r8), 1263 s; step 7 exit 1 with
the same failing rows as the writer and r8 (lean-axioms, legacy-records, v3-corpus, v3-receipts, citation-roles:
shallow clone / no Lean). `results/controls-table.md`: 394 PASS, 3 NOT RUN (TR5, G-A1, RT-T), 0 FAIL. Identical
row-for-row to the writer's table. Against r8 (388): no regression, no status change, 9 added (S1-P2-*, S1-Q8). RT-L2:
landed 55 paths (tool-landing 54 + class record), AGENTS.md base-drift reconciled, no unclassified side change. Worktree
clean after the run.

Mutation (export of 443e871f via `git archive`, r8 harness + S1 mutants + 6 of mine, `results/mutation-*`), 12 m 21 s:
91 mutants, 82 killed. Base 256 PASS, 2 NOT RUN, 1 FAIL (synthetic/M10: export not a git repo, as at r8). The
writer's 85 reproduce exactly (78 killed; survivors M07, M13, M24, M38, M53, M58 as at r8; S1-10 equivalent). Mine:
RV-01 (symlink mode accepted), RV-03 (parent dropped), RV-05 (pulls of parent), RV-06 (bytes from parent) killed.
RV-02 (non-directory intermediate yields an entry) and RV-04 (chain cache keyed by repo only) survive the harness.
My supplementary controls (`scripts/kill_rv.py`, `results/kill-rv.txt`) kill both. RV-04 returns a stale history after
main moves within one instance (fail-open in the mutant). RV-02 only turns a correct "absent" into HostUnavailable
(fail-closed). Nit N2.

## 7. Scope

[real git] Diff from 9da5dd5f touches only `tools/ledger_coverage*` and the audit directory. From 4fb2c1ee: 55 files,
all status A, all under those paths. Added lines: no `<tmp>/`, `/home/`, "workspace", model ids, emails. Z9h
unchanged. origin/research/a1exit-deletion-20261121 = 4c79be642ca631573f06b444903be75ec4f5e2b6 (local ref and GitHub
GET).

## Findings

BLOCKING: none.

Owner finding OF-1 (REST cost, sec. 4): an admission with the new reader needs an estimated 3,000-3,500 REST reads
plus 605+ GraphQL queries. That is above the documented 1,000/h GITHUB_TOKEN limit: it fails closed and so blocks TR5
and acceptance in CI. Decide before `A` pins the engine: measure the job-token limit, or adopt a batched GraphQL
reader, with re-review.

Nits:
- N1: `_tree` and `_json` let a malformed host answer (non-JSON 200, entry missing `sha`/`path`) escape as
  JSONDecodeError/KeyError instead of HostUnavailable. Non-acceptance still results (crash), but it is not a recorded
  ERROR. Smallest fix: catch ValueError/KeyError/TypeError in `_json`/`_tree` and raise HostUnavailable, as
  `first_parent_chain` already does for listing entries.
- N2: add controls for RV-02 (a file as an intermediate component) and RV-04 (main moves between two reads of one
  instance) to S1-P2.
- N3: the README group "provenance only" label (sec. 5); give the per-reference classification in the landed text when
  Q10 is resolved.
- N4: the archive lives in disposable scratch; the durable copy is 9da5dd5f, an ancestor of the head.
