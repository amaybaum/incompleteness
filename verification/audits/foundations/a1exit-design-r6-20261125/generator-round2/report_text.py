"""Prose of CORRECTION-REPORT.md.  Static text plus the generator's own log, checks and hashes; imported by
correct.py, so the report is regenerated with the outputs and is never hand-edited."""

ITEMS = [
    ('OC-1', 'OBL-16 / TR5: respecified consistently with AGENTS.md sec. A.39: (a) exact-candidate validation of the candidate F before designation, (b) designation identity verification, (c) durable evidence verification when the round lands; no requirement places F on main before its designation.'),
    ('OC-2', 'OBL-26: r6 specification adoption distinguished from implementation certification; adoption support is the r6 text and its independent exact-head review on main no later than the adoption record (precondition, not authorized); the a3799244 conformance assessment classified as provenance only where the adoption claim does not use it; every remaining off-main support dependency traced and reported as an open governance conflict.'),
    ('OC-3', 'OBL-13, OBL-14, OBL-15, OBL-23 (RT-L2, RT-O9-L2, RT-T, the T1\' figures): ancestry determination per control; structural controls moved to a reproducible representative candidate X_rep; item11-T1p kept as candidate evidence with a named provenance gap.'),
    ('OC-4', 'LC-7: REVIEW_REQUIRED kept pending an explicitly specified and independently reviewed regeneration verification procedure (trusted checker establishes the expected output and compares bytes); open, not resolved.'),
    ('OC-5', 'V4, V27, V27-glossary, V15: kept deferred, unchanged (checked byte for byte).'),
]

DETERMINATIONS = [
    ('RT-L2 (OBL-13)',
     'the sequencing safeguard (R6.RECON.21, R6.GATE.16): at a predicted M containing the tool\'s landing paths, every side change is classified and the drift state is none or validly reconciled by a reviewed record bound to the run\'s H, M and C blobs',
     'H..M side changes; the ledgered and corpus path sets (base-drift, R6.TREE.7); class records; for a drifted path, the candidate blob, which RC8 (R6.RECON.13) fixes to the ledger\'s expected_sha256; the only ancestry read is X\'s single parent H (R6.TREE.9)',
     'structure suffices; T1\' ancestry not material',
     'reproducible control at X = C = X_rep, predicted M = pinned main commit M0 plus the candidate\'s landing paths; full because every input the verdict reads is reproduced byte for byte by X_rep (a conforming candidate carries exactly X_rep\'s bytes on every ledgered and corpus path) and the parent relation is met by construction with H on main',
     'kind 1: RT-L2 on the exact tool candidate commit (CI run 45569710442 at a3799244 with X = T1\' and a drafted record stays provenance, R6.EVID.6)',
     'kind 2 once the landing merge and the reviewed reconciliation record (landing after the tool\'s landing commit) are on main; kind 3 re-run on main'),
    ('RT-O9-L2 (OBL-14)',
     'the dependent clause of RT-O9: no base-drift at the predicted M with the plan record directory added, and RT-L2 PASS',
     'base-drift items (decided by path membership in the ledgered and corpus sets) and RT-L2\'s status; a record directory holds no ledgered or corpus path (DIR3), so the content of P\'s record directory does not enter the clause',
     'structure suffices; neither T1\' nor P\'s record directory is material',
     'reproducible control at X_rep with a representative stand-in F holding the pinned ledger, edit list and configuration instance; full for the same reason as RT-L2',
     'kind 1 as RT-L2',
     'as RT-L2'),
    ('RT-T (OBL-15)',
     'with every reviewed record of the review load at F, coverage of the retirement candidate is PASS (R6.HIT.5, R6.HIT.6, R6.PLAN.4)',
     'op B reads only the corpus and the segments E..H and H..X (R6.PUR.5); a ledgered segment is checked against the ledger (no history walk of X); records bind file and line_sha256',
     'structure suffices; T1\' ancestry not material (and T1\' is not even H plus F\'s ledger if the ledger changes at F)',
     'RT-T at X_rep built from the ledger frozen at F; full because every conforming candidate under F\'s ledger has exactly X_rep\'s corpus bytes',
     'kind 1 on the candidate F before its designation, within its exact-candidate validation (OBL-16 (a)); kind 4 at the executed candidate',
     'kind 2 once the round\'s landing is on main (F and the execution reachable)'),
    ('RT-T0 (OBL-23)',
     'coverage at the candidate without records: the HP and RET counts, site states, region lines, merger groups',
     'corpus at X, E..H, H..X with the ledger (R6.PUR.5)',
     'structure suffices',
     'run at X_rep; expected figures carried from T1\' (byte-identical corpus when T1\' conforms); T1\' measurement in reference',
     'kind 1 at X_rep on the exact tool candidate',
     'kind 2 and kind 3'),
    ('RT-D (OBL-23)',
     'item-7 terms at the candidate: no deny match, W1/W2 PASS, GR.md:58 REVIEW, 45 resid REVIEW lines, 17 hit by no other profile',
     'resid hits are corpus lines; "other profile" membership is evaluated on those same lines (a1_controls.py at a3799244, rt_terms)',
     'structure suffices',
     'run at X_rep (scope guard scanned_paths_within)',
     'kind 1 at X_rep',
     'kind 2 and kind 3'),
    ('RT-I7 T1\' case (OBL-23)',
     'item7-literal counts at the candidate',
     'item 7\'s scope is papers/*.md and book/*.md (OBL-4)',
     'structure suffices',
     'case at X_rep; H case unchanged (H on main)',
     'kind 1 at X_rep',
     'kind 2 and kind 3'),
    ('RT-I7A T1\' case (OBL-23)',
     'the proposed item-7 check at the candidate: 0 deny, 12 final-unclassified',
     'corpus lines of the added text H..X under the ledger',
     'structure suffices',
     'case at X_rep',
     'kind 1 at X_rep',
     'kind 2 and kind 3'),
    ('RT-DR3W T1\' case (OBL-23)',
     'DR-3 alone finds no sentence in the candidate\'s AGENTS.md',
     'one text: AGENTS.md, a ledgered path, H\'s bytes plus the ledger\'s splices',
     'structure suffices',
     'control input agents-md-at-Xrep derived from H and the pinned ledger (sha256 59b68984..., the bytes of T1\'s copy)',
     'kind 1 at X_rep',
     'kind 2 and kind 3'),
    ('N10, N11 (OBL-23)',
     'landing composition of AGENTS.md: L with X\'s copy fails landing-conflict-unresolved and record-invalid; L with the composed blob passes',
     'H, M = 8e9b8334 (on main), the ledger\'s splice D296, X\'s AGENTS.md (ledgered: fixed by the ledger)',
     'structure suffices',
     'X = X_rep; L_blob 9f4fc3e8 is X_rep\'s AGENTS.md when T1\' conforms',
     'kind 1 at X_rep',
     'kind 2 and kind 3'),
    ('item11-T1p (OBL-23)',
     'item 11 with --final at the candidate: 176 final-unclassified lines of the repo profile',
     'the repo profile over active files, including T1\'s delegated and record paths; two of the 176 lines lie in generated artifacts (R6.EVID.5)',
     'the exact trial tree is material (delegated and record content that H and the ledger do not determine)',
     'no structural replacement; the requirement\'s behaviour stays covered by S11-11 (synthetic new active file)',
     'kind 1: the run on the exact tool candidate with X = T1\', for the landing decision only',
     'none: named provenance gap (AGENTS.md sec. A.42 item 8, support off main) while T1\'s objects are not on main; whether a kind-1-only figure suffices for the landing gate is an owner question'),
]

EVIDENCE = [
    'T1\' (14ac71b4) has exactly one parent, H (53c6601a): `git log -1 --format=%P` on the full clone.',
    'E (e837e3db), H (53c6601a), W (413b0bb8) and the N10/N11 M (8e9b8334) are ancestors of main e2e2a623; T1\' (14ac71b4), P (4c79be64) and the tool commit a3799244 are not (`git merge-base --is-ancestor`).',
    'P\'s and T1\'s `ledger.json` are the same blob ba37c1cd... (sha256 2055e68f...), and their `edits.json` the same blob ec384fdf... (sha256 528f146d...); T1\'s AGENTS.md is blob 9f4fc3e8... (sha256 59b68984...), H\'s is 12a9281f... (`git rev-parse`, `sha256sum`).',
    'The record directory verification/audits/foundations/a1exit-deletion-20261121/ (P\'s plan files) is on no commit reachable from main (`git rev-list` on main for that path is empty); P\'s edits_check.py is blob 1153e039... with sha256 2856e58c...d98c.',
    'H..T1\' and H..main (e2e2a623) share exactly one path, AGENTS.md; T1\' changes nine PDF/TeX pairs, the coverage ledger, the census, sc42-integration-result.json, Lean modules and the plan record directory in addition to manuscript files (`git diff --name-only`).',
    'At a3799244: tools/ledger_coverage/adapters/a1_controls.py tree_controls (around lines 917-990) builds the predicted M by `derive(M, tool_files)` and runs RT-L2 with `--candidate T` (T1\'), the ledger and edits at P, and a drafted reconciliation record placed at a derived commit, not in M; rt_o9 (around line 997) builds the stand-in F from P\'s record directory; rt_terms (around lines 280-400) shows the item-7, resid and item-11 scans; RT-L2\'s recorded predicate does not read the in-memory landing\'s MAIN items.',
    'At a3799244: engine/cli.py segments (around line 800): a segment with a ledger is checked by `check_ledger` against its base, with no first-parent walk of the candidate; engine/gitobj.py derive (lines 236-251): an in-memory commit id is the sha1 of the subject, base, changes and parents, so X_rep and the predicted M are reproducible from their inputs.',
    'R6.PUR.5: op B coverage is defined over the corpus (papers/*.md, book/*.md); R6.TREE.9 fixes every ledgered path of a conforming candidate to H plus its splices and every other path to H except delegated and record paths; R6.RECON.13 (RC8) fixes the candidate blob of a reconciled path to the ledger\'s expected_sha256.',
    'R6.REC.18 point 6 and R6.REC.19: chain admission requires head_branch main and GITHUB_REF refs/heads/main; the workflow fetches F by its full id. Hence TR5\'s chain run is dispatched on main naming F and cannot itself be the sec. A.39 check-run, whose head_sha is the candidate.',
]

STAGES = [
    ('1. Pre-merge candidate validation (tool PR)',
     'the gate on the exact candidate commit of the tool\'s pull request: every row it runs, including RT-L2 and RT-O9-L2 at X_rep with the predicted M = M0 plus the candidate\'s landing paths and the reviewed reconciliation record named from outside those paths; REP-BUILD; RT-T0, RT-D, RT-I7, RT-I7A, RT-DR3W, N10, N11 at X_rep; item11-T1p at T1\'; the obligations OBL-19 to OBL-22, OBL-24, OBL-25, OBL-28 with their controls; LC-1 to LC-7 (LC-7 REVIEW_REQUIRED)',
     'kind 1',
     'qualifies as evidence for the landing decision; provenance (sec. A.42 item 2) for any enduring claim until the candidate is reachable from main'),
    ('2. Tool landing decision',
     'stage 1 evidence; r6 adopted by a recorded owner decision whose support (r6 text and its independent exact-head review) is on main (R6.STAT.10); OBL-22\'s advance approval and independent review of the identifier migration; the owner\'s approval of the merge (sec. A.50 item 1)',
     'kind 1 plus governance records',
     'qualifies for the decision; the reviewed reconciliation record is supplied from outside the landing paths; open: item11-T1p rests on kind 1 only (owner question), RT-O9\'s own checks read P\'s record directory, and the other T1\'/P-input controls listed in the adoption trace'),
    ('3. Post-merge confirmation',
     'the stage 1 runs once the landing merge is on main (candidate reachable; inputs H, E, M0, the tool revision with the pinned ledger, edit list, configuration template and records) and the same recipes re-run on main; RT-L2 re-run with M the main that holds the tool and a reconciliation record bound to it, landed in a later commit; OBL-26 conformance certification against the landed revision',
     'kinds 2 and 3',
     'qualifies for every X_rep control once the reviewed reconciliation record (RT-L2, RT-O9-L2) is on main; not for item11-T1p (named provenance gap) nor for controls still reading T1\' or P'),
    ('4. A1 plan freeze F',
     'TR5 (a): the sec. A.39 exact-head check-run on the candidate F (head_sha F, every job green) and TR5\'s chain run on main at T naming the same F; RT-T at X_rep built from F\'s ledger with F\'s records; the records and comparisons of OBL-1 to OBL-11 and OBL-27 at F; TR5 (b): the owner\'s designation quoted with author and time and compared with the check-run\'s head_sha and TR5\'s snapshot F by the record\'s reviewer',
     'kind 1 for the designation decision (R6.EVID.7 item 1, freeze clause); records frozen at F (kind 4); designation comparison (governance)',
     'qualifies for the designation decision without F on main (no cycle); qualifies as kind 2 when the round lands (TR5 (c)); dispatches need owner approval (sec. A.40, sec. A.50 item 5)'),
    ('5. A1 trials',
     'runs of the pinned workflow on main naming F, under the frozen plan, for trials the owner approves (sec. A.50 item 2); OBL-1 and OBL-5 where a trial claims items 5, 6 or 7',
     'kind 4',
     'qualifies as A1 execution evidence gated at F; enduring once the round lands (F and the trial records reachable, sec. A.42 item 7)'),
    ('6. A1 retirement execution',
     'G-A1 (native delegated runs at X and C, after TR5 released), TR45-opC, EI14-dispatch (after the tool lands, owner-approved launch), RT-T at the executed candidate, OBL-12, OBL-17, OBL-18; the landing check (sec. 20, sec. 23) with the re-resolved M; the round\'s receipt with --verify-round printing VERDICT HOLDS',
     'kind 4; receipt and host attestations (sec. A.39)',
     'qualifies when the round lands (sec. A.42 item 7: the certified head on main re-establishes the computational claims); LC-7 keeps derived artifacts REVIEW_REQUIRED until the regeneration verification procedure exists'),
]

OPEN_ITEMS = [
    'Off-main support of adoption (R6.STAT.10, sec. 32 adoption trace), each an open governance conflict, none resolved by exception: (i) the r6 documents and their independent exact-head review must be on main before the adoption record (precondition: an ordinary owner-approved merge, not authorized here); (ii) statements of fact about the tool commit, CI run 45569710442 and T1\' (R6.PUR.12, R6.PIPE.3, R6.ANCH.10, R6.ANCH.12, R6.HP.7, R6.OUT.18, R6.OUT.24, R6.SPLIT.3, R6.RULE.11, R6.RULE.12, R6.REC.20, R6.HIT.2, R6.CLASS.1, R6.CLASS.11, R6.GATE.7, R6.CTRL.19, R6.CTRL.25, R6.CTRL.29, R6.TREE.13, R6.RDIR.7, R6.RECON.11, OBL-21, OBL-28, R6.EVID.6, R6.NOTE.3); (iii) semantics defined by reference to P\'s edits_check.py (R6.SPLIT.3, R6.PROF.3, R6.PROF.4, R6.PROF.5, R6.PROF.7, R6.PROF.8, R6.PROF.9, R6.PROF.10, R6.PROF.12, R6.DENY.5, R6.A1CFG.2, OBL-1): P\'s record directory is on no commit reachable from main; (iv) owner decisions held only in paraphrase or relayed in session (PARAPHRASED-DECISIONS.md, R6.STAT.8, and the owner corrections OC-1 to OC-5 themselves, which were relayed in session without a comment id; PARAPHRASED-DECISIONS.md is copied unchanged as instructed, so OC-1 to OC-5 are listed only in the design\'s adoption trace and here).',
    'item11-T1p (OBL-23): exact trial tree material; candidate evidence only; enduring claim a named provenance gap; whether a kind-1-only figure suffices for the landing gate is an owner question.',
    'Controls outside OC-3\'s list that still read T1\' or P (not re-specified, reported only): RT-C, the T1\' case of RT-DR, RT-M, RT-D-gr58, RT-L, S11-56, RT-O9\'s own record-directory checks (stand-in F from P\'s record directory), and every execution control whose ledger and edit list are read at P (exec_args at a3799244). R6.EVID.8 defines the pinned ledger and edit list and X_rep they could use; extending it to them needs its own authorization.',
    'LC-7 / R6.TREE.12 (OC-4): REVIEW_REQUIRED for every candidate L until a regeneration verification procedure is specified explicitly and reviewed independently (trusted checker establishes the expected output itself and compares bytes; the evaluated tree\'s claim never suffices). Open, not resolved.',
    'Deferred expectations V4, V27, V27-glossary, V15 (RE-1): unchanged, decided at r6 adoption.',
    'Pending owner confirmation: the requirements of PARAPHRASED-DECISIONS.md (unchanged).',
    'Implementation obligations added by OC-3 (OBL-28 row OC-3): the X_rep builder, the pinned ledger and edit list and the configuration template land with the tool revision; the runners record the paths each verdict read (scanned_paths_within); the gate supports the two new invariant keys. Until implemented, REP-BUILD is missing-id.',
    'The TR5 chain run and the sec. A.39 check-run are two host runs bound by the candidate\'s full id (R6.REC.18 point 6 forbids chain admission off main); both dispatches need owner approval. This is not a cycle.',
]

FINDINGS = [
    'Hash binding of the RT-L2 reconciliation record: a reconciliation record names the M of its run (R6.RECON.1), so it cannot be a path of that M. The out-final release check ("a reconciliation record referenced at the commit under check") could not be met by a record among the tool\'s landing paths, which the predicted M contains. OC-3 specifies the placement: named from a commit outside the landing paths, landed on main after the tool\'s landing commit. RT-L2\'s and RT-O9-L2\'s release condition and release check are restated accordingly.',
    'Table 17.1\'s RT-L2 case in out-final put the plan record directory of the stand-in F into RT-L2\'s predicted M; R6.RECON.21 and the runner at a3799244 put only the tool\'s landing paths there, and the record directory into RT-O9\'s M. The case cell now follows R6.RECON.21; the record directory belongs to RT-O9 and RT-O9-L2.',
    'The out-final OBL-16 cycle came from the condition "F on main" in TR5\'s text and release condition. The tool\'s execution identity never needed it: chain admission needs T on main and F fetchable by id (R6.REC.18, R6.REC.19). With OC-1 the cycle is gone.',
    'The staged configuration cannot land with the tool as a byte copy without a reference cycle with the class record (K1-GRAPH countercontrol 1). R6.EVID.8 therefore uses a configuration template whose class-record pin the runner fills, which names no blob the class record pins.',
    'The mechanical index rule of final.py (non-testable verification = the OBL ids the text names) is reused unchanged; it gives R6.STAT.10 the verification OBL-26. R6.EVID.7 names TR5 rather than OBL-16 so that its verification stays "review".',
]


def table(head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    for r in rows:
        out.append('| ' + ' | '.join(x.replace('|', '/') for x in r) + ' |')
    return out


def build(c):
    R = ['# r6 correction report (owner corrections of 2026-11-25)', '',
         'Deterministic correction of the consolidated design r6 by `build/correct.py`, which reads `out-final/` '
         '(read only) and applies the explicit, logged edits below. Every edit carries the number of the owner '
         'correction it applies (OC-1 to OC-5) or `meta` for a mechanical consequence (two-way links, the Requirements '
         'column of Table 17.1, the invariant annex, the requirement index, record ids). No governance rule is amended '
         'and no exception is created. r6 stays a draft until the owner adopts it. No git or GitHub write was made and '
         'the tool was not run; the facts in sec. 4 were obtained by read-only inspection.', '',
         'The corrections, as authorized:', '']
    for k, v in ITEMS:
        R.append('- %s: %s' % (k, v))
    R += ['', '***', '', '## 1. Inputs and outputs (sha256)', '']
    R += table(['Input (read only)', 'sha256'], [(p, h) for p, h in c['INPUT_SHA']])
    R += ['']
    R += table(['Output', 'sha256'], [(n, h) for n, h in c['OUT_SHA']] +
               [('CORRECTION-REPORT.md', 'this file (its own digest is reported by the generator run)')])
    R += ['', 'Counts: %d expectation rows (one added: REP-BUILD), %d requirements (two added: R6.STAT.10, R6.EVID.8), '
          '%d invariant keys (two added: representative_candidate, scanned_paths_within). PARAPHRASED-DECISIONS.md is '
          'copied unchanged.' % (c['N_ROWS'], c['N_REQ'], c['N_INV']), '', '***', '', '## 2. Edits applied', '']
    R += table(['#', 'Item', 'Target', 'Edit'], [(str(i + 1), a, b, d) for i, (a, b, d) in enumerate(c['LOG'])])
    R += ['', '***', '', '## 3. What each correction changed', '',
          '### OC-1 (OBL-16, TR5)', '',
          '- OBL-16 restated: TR5 is the exact-candidate validation of the plan freeze in three parts: (a) before the '
          'owner designates F, with the round\'s branch held at exactly the candidate, the sec. A.39 exact-head check-run '
          'on the candidate and TR5\'s chain-admitted run (pinned workflow dispatched on main at T, --freeze the same full '
          'id); (b) designation identity verification: the quoted owner designation names a full id equal to the '
          'check-run\'s head_sha and TR5\'s snapshot F, compared by the record\'s reviewer (not by the tool, R6.STAT.4, '
          'R6.REC.23); (c) once the round lands, F is an ancestor of the certified head on main and TR5\'s recipe and '
          'expected result qualify under sec. A.42 items 1 and 7, with the receipt recording the attestation.',
          '- TR5\'s expectation row: reason, release condition and release check restated; "F on main" removed; F need '
          'only be fetchable by full id. Release condition and release check of G-A1 unchanged ("TR5 released").',
          '- R6.EVID.7 item 1: the exact-candidate validation of a native round\'s candidate F before designation is kind 1 '
          'for the designation decision and kind 2 when the round lands.',
          '- Sec. 32 trace row of OBL-16 restated; the OPEN marker "circular evidence dependency" removed from OBL-16 '
          '(resolved: no evidence needs F on main before its designation). What remains is not a cycle: the two '
          'dispatches of (a) need the owner\'s approval, and the host attestations stay residual trust (R6.REC.25).', '',
          '### OC-2 (OBL-26, adoption)', '',
          '- New R6.STAT.10: adoption support = the r6 documents and their independent exact-head review, both on main '
          'no later than the adoption record (precondition: an ordinary owner-approved merge, sec. A.50 item 1; not '
          'authorized); adoption certifies no implementation; implementation certification after the tool lands '
          '(OBL-26, kinds 2 and 3); OPEN "off-main support of adoption".',
          '- OBL-26 restated: conformance certification of the landed tool revision; gate changed from r6\'s adoption to '
          'the implementation certification of the landed revision (OC-2 replaces the gate RE-37 confirmed). The a3799244 '
          'assessment is provenance for the requirements and obligations, which hold or fail by their own controls; it is '
          'not provenance for r6\'s statements that describe the tool commit, which use its content (adoption trace). '
          'OPEN "circular evidence dependency" removed from OBL-26.',
          '- Sec. 32: gated steps extended; the trace row of OBL-26 restated; an adoption trace table added that lists '
          'every place where adoption or an enduring claim uses off-main content, with its classification.', '',
          '### OC-3 (OBL-13, OBL-14, OBL-15, OBL-23)', '',
          '- New R6.EVID.8 (testable; controls REP-BUILD, RT-L2, RT-O9-L2, RT-T, RT-T0, RT-D, RT-I7, RT-I7A, RT-DR3W, N10, '
          'N11): construction of X_rep, its pinned inputs (byte copies of the ledger and edit list landed with the tool '
          'revision; a configuration template; H, E and a pinned main commit M0), why the safeguard is full, the scope '
          'guard (scanned_paths_within), the carrying of expected values (byte comparison as candidate evidence only, '
          'never as support), the reconciliation-record placement, and a per-control evidence table.',
          '- OBL-13, OBL-14, OBL-15, OBL-23 restated; OPEN "T1\'-bound evidence cannot qualify" removed from OBL-13, OBL-14 '
          'and OBL-15 and kept on OBL-23 for item11-T1p only. Sec. 32 trace rows of OBL-7, OBL-13, OBL-14, OBL-15 and '
          'OBL-23 restated. R6.NOTE.3, R6.CTRL.7, R6.CTRL.19, R6.PLAN.8, R6.RECON.21 and R6.EVID.4 (text and Input column) '
          'follow; OBL-28 gains row OC-3; Table 17.1 case cells of the affected rows and a REP-BUILD row.',
          '- Expectation rows: X_rep cases and invariants for RT-L2, RT-O9-L2, RT-T, RT-T0, RT-D, RT-I7, RT-I7A, RT-DR3W, '
          'N10, N11; their T1\' measurements recorded in `reference` as provenance; release conditions of RT-L2 and '
          'RT-O9-L2 (record outside the landing paths) and RT-T (X_rep from F\'s ledger); REP-BUILD added; item11-T1p '
          'flagged exact-tree material.', '',
          '### OC-4 (LC-7)', '',
          '- R6.TREE.12\'s generated-artifact case, OBL-28 row RE-18, the LC-7 row flag and its Table 17.1 case state that '
          'the path stays REVIEW_REQUIRED for every candidate L until a regeneration verification procedure is specified '
          'explicitly and reviewed independently, in which the trusted checker establishes the expected output itself '
          'and compares bytes; the evaluated tree\'s claim of regeneration is never sufficient. The OPEN markers '
          '("derived-artifact landing blob" on R6.TREE.12 and on the LC-7 row) are kept: not resolved.', '',
          '### OC-5', '', '- V4, V27, V27-glossary and V15 are unchanged (byte-identical rows, expect DEFERRED).', '',
          '***', '', '## 4. Ancestry determinations (OC-3)', '',
          'Decision rule, fixed before the per-control reading: a control may take a representative candidate only if '
          'every input its verdict reads is a function of H, the ledger and inputs on main, and the only ancestry it '
          'reads is a relation that a commit built on H satisfies by construction; otherwise the exact trial tree or '
          'its ancestry is material, and the T1\' run stays candidate evidence with the enduring claim a named provenance '
          'gap. Byte equality with T1\' is never offered as a substitute for ancestry; it is used only to carry expected '
          'values, as candidate evidence.', '']
    R += table(['Control', 'What it asserts', 'What its verdict reads', 'Determination', 'Replacement and why full',
                'Candidate evidence (landing decision)', 'Reproducible evidence (enduring claim)'], DETERMINATIONS)
    R += ['', 'Evidence for the determinations (read-only inspection):', '']
    R += ['- ' + e for e in EVIDENCE]
    R += ['', '***', '', '## 5. Stage-by-stage evidence', '',
          'Evidence kinds as R6.EVID.7: 1 pre-merge candidate validation (including, for a native round\'s freeze, the '
          'exact-candidate validation of the candidate F before designation); 2 qualifying landing evidence; 3 post-merge '
          'confirmation on main; 4 A1 execution evidence gated at F.', '']
    R += table(['Stage', 'Required evidence', 'Kind', 'Qualifies at that point'], STAGES)
    R += ['', 'Circular dependencies remaining: none. The two cycles of out-final (OBL-16, OBL-26) are removed by OC-1 '
          'and OC-2. The reconciliation-record self-reference found while specifying RT-L2 is avoided by placement '
          '(sec. 7), not by an exception.', '',
          'Off-main support dependencies remaining: see sec. 6, first three items.', '', '***', '',
          '## 6. Remaining open items and governance conflicts', '']
    R += ['- ' + o for o in OPEN_ITEMS]
    R += ['', 'OPEN markers in the requirement index after the correction:', '']
    for k, v in c['OPEN_LEFT'].items():
        R.append('- `%s`: %s' % (k, ', '.join(v)))
    R += ['', 'OPEN flags on expectation rows:', '']
    for rid, f in c['OPEN_ROWS']:
        R.append('- %s: %s' % (rid, f))
    R += ['', '***', '', '## 7. Findings made while correcting', '']
    R += ['- ' + f for f in FINDINGS]
    R += ['', '***', '', '## 8. Self-checks', '',
          'The checks of out-final/build/final.py, re-run on the corrected outputs, and the correction\'s own checks:', '']
    for k, v in c['CHECKS'].items():
        R.append('- %s: %s' % (k, len(v) if not v else '%d (%s)' % (len(v), ', '.join(str(x) for x in v[:10]))))
    R += ['- coverage: testable requirements without a control: %d (%s)' % (len(c['TESTABLE_NO_CTRL']), ', '.join(c['TESTABLE_NO_CTRL'])),
          '- hygiene: no at sign, no temporary-directory path, no github URL, no carriage return, no non-ASCII space and no '
          'non-ASCII character not already in the corresponding input, in any output: checked',
          '- reproducibility: the generator re-ran itself in a separate process (`python3 -I -B`) and compared the sha256 '
          'of every output before writing; identical',
          '- generator problems: %d' % len(c['PROBLEMS']), '']
    return '\n'.join(R)
