# Stage-3 relaunch log (coordinator; kept under pt/audit/ so the running thread X does not see a foreign write)

- Thread U launch 1 (10:22Z) was terminated by a tooling error at 2026-10-10 10:24:51Z + reading phase: the agent's response exceeded the 64000-token output maximum (API error max_output_tokens). It had written only pt/U/.start_marker (sha256 674151c0b333ed5f1daf160c8dbf9d20f13da1dbf503ffd6de1e9d2bacfa1b70), moved here as audit/aborted-launches/U-launch1/.start_marker with its mtime preserved. No script, output or result existed.
- 2026-10-10T11:17:06Z: thread U relaunched (launch 2) with the same frozen protocol PROTOCOL-STAGE3.md (1a649168…) and the same inputs; the relaunch prompt adds only a tooling constraint (write files in parts of at most ~250 lines). Thread X was not affected and keeps running.

- Thread X launch 1 (10:22Z) was terminated by the same tooling error (max_output_tokens) at its first step, having written only pt/X/.start_marker (sha256 6243a89ad15ea8cafb88a7dd3617a22c7b86af14785bb38a6b0e91ec657b8166), moved to audit/aborted-launches/X-launch1/ with its mtime preserved.
- 2026-10-10T11:19:34Z: thread X relaunched (launch 2) with the same frozen protocol and inputs; tooling change only: the agent model is pinned to the one stage 2 ran under (Opus), and files are written in parts. Both failures occurred after the session model was switched to Fable 5.1 (subagents inherit it), which is the probable cause; the mathematics and the protocol are unchanged.

- Thread U launch 2 (11:17Z, still under the inherited Fable 5.1 model) was stopped by the coordinator at 11:20Z, before any script, after X's identical failure showed the cause to be the model switch; it had written only pt/U/.start_marker (sha256 3d061fd35e73f4a627c26113a8014bebc30c15a593cdb2ea91569c3289f83101), moved to audit/aborted-launches/U-launch2/ with its mtime preserved.
- 2026-10-10T11:21:12Z: thread U relaunched (launch 3) with the agent model pinned to Opus, as X launch 2; protocol and inputs unchanged.

- 2026-10-10T12:34:09Z: review thread NS launched (one agent, model pinned to Opus, research-only) under PROTOCOL-NS.md sha256 4f61891f82a4bfe13a9d0ed74fd064c903c94d57ed8d29bf039633f72b2494e0; working directory pt/audit/reviews/NS/ (inside the coordinator's area because U and X are running); input ns/NS-INPUT.md sha256 d8c5a1b3da937217f207cad416c6d0d1a59f69ac177cb704274f3956449d98fb.

## Stage 4 launch (Q-EX), 2026-10-10T14:22:11Z
- Stage-3 archive delivered first (evidence/pt-stage3-evidence.tar.gz bc275ae3…, manifest e3d58960…), per owner note 4.
- Protocol: pt/PROTOCOL-STAGE4.md, sha256 d3da28116a5bcdd3…; threads Y (exclusion) and Z (countermodels),
  Opus model, write-in-parts constraint (as the stage-3 relaunches); working directories pt/Y/, pt/Z/; coordinator writes only
  under pt/audit/ while they run.

## Stage 4 close (2026-10-10T16:16Z)
Y reported 15:23Z, audited (AUDIT-Y.md a4d12a39…); Z reported 16:00Z, audited (AUDIT-Z.md 4be00ec5…). Integration note pt/INTEGRATION-NOTE-STAGE4.md written; archive built by drafts/build_stage4_evidence.sh. Holds unchanged.

## Stage 5 launch (Q-EX-BRIDGE), 2026-10-10T16:40:27Z
- Owner note 7 recorded (pt/audit/stage5-inputs/OWNER-NOTE7-STAGE4-CLOSE.md 1436874a…); manuscript obligation M1 recorded, not applied (MANUSCRIPT-OBLIGATIONS.md 3b362615…).
- Protocol: pt/PROTOCOL-STAGE5.md, sha256 9e01f098cbe0a279…, sidecar verifies from the scratchpad directory; coordinator pre-audit PRE-AUDIT-BRIDGE.md with preaudit_bridge.py 7/7 (run 3; runs 1-2 kept), replay identical.
- Threads D (BRIDGE-DERIVE) and C (BRIDGE-COUNTER), Opus model, write-in-parts constraint; working directories pt/D/, pt/C/; coordinator writes only under pt/audit/ while they run. Holds unchanged.
- 16:41Z first launch ABORTED by the threads' own guard: pt/D/ and pt/C/ are the stage-1 records (coordinator error); nothing written; manifests verify (16:42:34Z). Amendment 1 (pt/PROTOCOL-STAGE5-AMENDMENT-1.md 1f639115d369de13…) renames the working directories to pt/D5/ and pt/C5/; record pt/audit/aborted-launches/stage5-launch1.md. Relaunch follows.
- Relaunch: thread D into pt/D5/ at 16:43:4xZ and thread C into pt/C5/ at 2026-10-10T16:44:55Z, both under PROTOCOL-STAGE5.md 9e01f098… + AMENDMENT-1 1f639115… (nine protocol hashes in the brief). First instances D and C both stopped at their guard without writing; C reported at 16:44Z (28 stage-1 files verified by its own check).

## Stage 6 launch (Q-EX-FULL), 2026-10-10T16:49:55Z
- Owner note 8 recorded (pt/audit/stage6-inputs/OWNER-NOTE8-FULL-CLOSURE.md). Protocol pt/PROTOCOL-STAGE6.md sha256 b277b7c1a7020c4e…; step 1 (complete premise inventory) threads I1–I4 launched in parallel in pt/I1..I4 (Opus, write-in-parts, read-only); steps 2–4 by append-only amendment after stage 5 is audited. Records snapshot evidence/pt-records-snapshot-20261010T164943Z.tar.gz delivered to the owner for preservation. Holds unchanged.

## Stage-5 close and stage-6 steps 2–3 launch (2026-10-10, 17:46Z–17:57Z)

- Stage 5 (Q-EX-BRIDGE) closed: D5 audited (`pt/audit/D5/AUDIT-D.md`, independent check 32/32, replays 3/3),
  C5 audited (`pt/audit/C5/AUDIT-C.md`, independent check 41/44 with the three mismatches reconciled as the level
  of C5's orbit counts; replays 2/2), integration note `pt/INTEGRATION-NOTE-STAGE5.md` (sha256 `50246e07…`);
  archive `evidence/pt-stage5-evidence.tar.gz` (`3fe5e2eb…`, 332 entries), manifest `evidence/stage5.manifest.sha256`
  (`b346a3c9…`), verified by extraction. Verdict: no principle at L derives (b); CONDITIONAL on a spectator clause
  (α, β, γ-extension, δ), INDEPENDENT for every other candidate, DERIVED only relative to the unsourced λ.
- Anomaly attribution recorded in both audits: the files D5 and C5 flagged are the coordinator's stage-6 launch
  (`pt/PROTOCOL-STAGE6.md`, its sidecar, `pt/I1/`–`pt/I4/`), written while stage 5 ran — a coordinator process
  breach of the "write only under `pt/audit/` while threads run" rule; lesson recorded in AUDIT-D §2.
- Stage 6 step 1 audited: `pt/audit/stage6-inputs/I-audit/AUDIT-I.md` (hashes 76/77/53/73 verified, replays 31/31
  identical, coordinator import-graph check confirms "no bridge M/H/G → P at L").
- Amendment 1 to the stage-6 protocol issued: `pt/PROTOCOL-STAGE6-AMENDMENT-1.md` (`59019538…`, sidecar verifies
  from SCRATCH); working directories `pt/G6/` (step 2), `pt/R6/` (step 3), `pt/T6/` (step 4), checked absent and
  absent from every manifest before issue.
- Launched 17:57Z: G6 (dependency graph) and R6 (countermodel reassessment), in parallel, both told the other's
  directory is never read; T6 (test of (b)) is launched after both report and are audited. The coordinator writes
  only under `pt/audit/` until then.

## Stage 6 steps 2–3 audited, step 4 launch (2026-10-10T18:48:35Z)

- G6 reported 18:31Z and was audited: `pt/audit/stage6-inputs/G-audit/AUDIT-G.md` (sha256 `3fd6763d…`; hashes 59/59,
  replays 5/5 identical, independent check `check_graph.py` run 3 11/11 with replay identical; NO-MEET reproduced
  with countercontrol; G6's post-hoc rule re-scoping recorded as a disclosed convention; C2/C3 findings carried as
  record items).
- R6 reported 18:34Z and was audited: `pt/audit/stage6-inputs/R-audit/AUDIT-R.md` (sha256 `04308355…`; hashes 59/59,
  replays 6/6 identical; every prediction of PRE-AUDIT-R6T6 §2 matched; FAILS rows hypotheses only; A1.5 gap
  (`K({F, cnot F})`, `K(e_c)` not reassessed) recorded with the covering argument).
- Amendment 2 issued: `pt/PROTOCOL-STAGE6-AMENDMENT-2.md` (sha256 `748f1764…`, sidecar verifies from SCRATCH): T6 reads the
  frozen G6/R6 records and the audits AUDIT-I/G/R only from `pt/audit/stage6-inputs/`; the applicable premise set as
  audited; outcome statement (DERIVATION / CONDITIONAL on a named item / INDEPENDENCE / UNRESOLVED).
- `pt/T6/` checked absent and absent from every manifest at 2026-10-10T18:48:35Z. T6 (test of (b)) launched next; the coordinator
  writes only under `pt/audit/` while it runs.
- T6 launched at 2026-10-10T18:50:30Z (Opus, background, write-in-parts, read-only; brief carries twelve protocol prefixes incl. amendment 2 748f1764 and the three audit hashes 845bd662 / 3fd6763d / 04308355; budget ~90 min).

## Stage 6 step 4 reported (2026-10-10T19:29:05Z)

- T6 reported 19:24Z (RESULT.md sha256 `8de7fabe…`): INDEPENDENCE — the complete applicable premise set at L does
  not force (b) in its weakest sufficient form; countermodel K(Z_F) checked row by row against R6's Table A2 (118
  SATISFIES incl. 3 vacuous, 68 NOT REACHED, 13 FAILS all hypotheses); exact witness family: for every unit axis n,
  either token and every s, `ipW(R_n(t) z_s, R_n(π/2) p_s) = −sin(t)/8` with the witness in Q3 ∩ Z_F*; missing
  assumption = (b) for {R_x, R_z} on one token (fails the disguise test: restates I3.153 / I3.165 and is the drive
  instance of OI⁺-1); λ and pair homogeneity H pass the disguise test but are not items at L.
- Coordinator's mechanical verification (`pt/audit/stage6-inputs/T-audit/`): listed hashes 35/35 OK; replays 5/5
  byte-identical (`verify_thread.sh`); row-by-row check `check_t6_rows.py` 4/4 against the coordinator's own
  recount of R6's Table A2, replay identical; independent exact check `indep_checkT.py` 5/5 (flow law and witness
  membership proved symbolically for every unit axis, cyc3^±1, mixed placement, controls).

## Stage 6 close (2026-10-10T19:32:43Z)

- T6 audited and accepted as INDEPENDENCE under the pre-registered rule: `pt/audit/stage6-inputs/T-audit/AUDIT-T.md`
  (sha256 `98c61669…`). Integration note `pt/INTEGRATION-NOTE-STAGE6.md` (sha256 `1130a8c5…`): verdict INDEPENDENCE in the
  owner's two-way form; CONDITIONAL readings named at their status (α, β, γ, δ at level M without a bridge; λ [D];
  H, T PT-record); the missing assumption isolated as (b) for ball3Drive's flow and its J-conjugate on one token.
  Archive built by `drafts/build_stage6_evidence.sh`. Holds unchanged.
