# I1 NOTES — running record (thread I1, inventory: foundations, stage 6, Q-EX-FULL)

All clock times are UTC, read from `date -u`.

- 16:50:48 — `pt/I1/` confirmed absent before creation.
- 16:51:54 — `pt/I1/` created; `.start_marker` written as the first file (108 lines). All start
  checks green: six manifests `sha256sum -c --quiet` exit 0 with no complaint; `ns.manifest.sha256`
  `ns/NS-INPUT.md: OK`; `pt/base` HEAD = L = 9f9f8257a980a1819fbbc1dc0019917cf8678626, porcelain
  empty, 0 `__pycache__`/`.pyc`; ten protocol files match the prefixes; ten sidecars verify
  (six from `pt/`, four from SCRATCH). `pt/I2` already existed at 16:51:44 (sibling; not read).
- 16:51:56 — begin reading the governing text `pt/PROTOCOL-STAGE6.md` in full.
- 16:52–16:54 — read in full: `PROTOCOL-STAGE6.md`, `PROTOCOL-STAGE5.md`, its amendment 1,
  `PROTOCOL-STAGE4.md`, `PROTOCOL-STAGE3.md`, `PROTOCOL.md`, `INTEGRATION-NOTE-STAGE4.md`,
  `INTEGRATION-NOTE-STAGE3.md`; `pt/base/AGENTS.md` is byte-identical (diff -q) to the AGENTS.md
  loaded in this session's context (sha256 959c4333…), read there.
- 16:54 — scope decision for the kernel census (a): whole-module census over twelve modules whose
  subject is in I1 (OIRealization, IndependenceCensus, ManuscriptAxioms, RouteB,
  SubstratumInterfaceAudit, BackgroundIndependence, A6Instantiation, C3Necessity, CausalReadback,
  PhysicalC4Discharge, PhysicalC4StorageReadback, InternalObserver), plus the single declaration
  `OICore` of CompletedOI.lean (rest of that module: I4), plus a cross-tree token census (part B)
  of every declaration whose signature mentions the sealed-core / internal-observer predicates.
  `verification/lean/*.lean` (zero-import layer: SM structural chain, gauge certificates, time
  reversal) listed in part C; out of scope (physical layer X, thread I2).
- 16:55 — `kernel_census.py` written with its decision rule in the header, run once
  (exit 0, 562 lines), replayed byte-identical (`.replay.out`/`.replay.err`). Part A: 41 census
  entries, 0 extension entries; part B: 94 declarations in 18 modules; part C: 10 heads.
- 16:55–16:57 — read the decisive kernel objects: OIRealization.lean in full; IndependenceCensus
  §A and the census capstone; ManuscriptAxioms in full; RouteB §A–§F key parts; CompletedOI
  `OICore` and the forward-redundancy theorems; SubstratumInterfaceAudit §A and the sourcing
  section; C3Necessity; CausalReadback; PhysicalC4Discharge and PhysicalC4StorageReadback
  (predicates and theorem list); InternalObserver. ROADMAP queue rows, the A6 / C4 / stochastic
  observer sections, "Settled negatively", "Declared inputs"; README status passages on the core.
- 16:58–17:00 — `bridge_check.py` (decision rule in header: import-graph closure, CORE x PAIR and
  CORE x OPER modules, signature search with a countercontrol) run once, exit 0, replayed
  byte-identical. Controls green (graph: IndependenceCensus in closure(OIRealization); search:
  159 pair-token declarations in CompositeDimension). VERDICT PAIR (level P): NO-MODULE; VERDICT
  OPER (level O): NO-MODULE. No module at L imports both an I1 module and CompositeDimension/K2Guard,
  nor an I1 module and the K-infinity modules.
- 17:00 — `bridge_check2.py` (can H -> M -> P route through one module?): control green
  (OperationalAssembly in closure(OIRealization)); VERDICT NO-MODULE: no module at L imports both
  the M-level carrier `FiniteOperationalTheory` (OperationalAssembly) and a pair-cone module. Run
  once, exit 0, replayed byte-identical. Consequence for the records: every I1 item's `bridge`
  field to level P is `none at L`, with these two outputs as the mechanical evidence.
- 17:01–17:03 — `statements.py` (exact-quote appendix; decision rule in header) run once: exit 0,
  104 declarations found, 0 missing, 89 manuscript lines. Some manuscript line picks in its MLINES
  list were imprecise (e.g. Methodology.md:225 is blank; :243 is the lead-in line); INVENTORY cites
  the verified lines directly. Plan: correct MLINES and re-run as run 2, keeping run 1.
- 17:03–17:11 — INVENTORY.md written in ten parts (each ≤ 250 lines): 83 records I1.1–I1.83 in
  sections A (observation base), B (C1–C4 manuscript forms and theorems), C (sealed core and its
  realization), D (Route B), E (A1–A6), F (C4 kernel forms and physical discharge), G (observer
  structure, ROADMAP status records), H (core-carrying realization theorems), I (out-of-scope names).
  Every cited kernel line re-verified with grep after writing; eighteen line references and
  fourteen cross-reference ids corrected (records were numbered before the numbering was final).
  Corrections applied with a stdin helper (`python3 -I -B -`) that asserts each replaced string
  occurs exactly once; no evidence script was involved.
- Observations recorded in the inventory (not adjudicated): (i) status variance on bijectivity —
  Methodology.md:251 lists it among lemmas, Main.md:38/:62 call the bijective representative a
  reconstruction/representation choice (I1.10); (ii) C2 stated in its slow form as the definition
  in book ch01:55 and Explainer.md:67, while Main.md:76 defines unqualified C2 as persistence
  (I1.21/I1.22); (iii) ch01:71 calls the four conditions "logically independent", Main.md:602 says
  only C4 is (I1.25/I1.26); (iv) the book's Definition says "a deterministic dynamics" (ch01:26),
  Main.md:44 "a dynamics" (I1.6).
- 17:12–17:14 — `census_ms.py` (manuscript census (b)): run 1 exit 0, 946 sentences, 18 UNMAPPED;
  kept as `census_ms.run1.{py,out,err}`. Pre-run edit for run 2: a MANUAL table for exactly those
  18 sentences (each read; mappings in the script). Run 2: 946 sentences, 0 unmapped; replayed
  byte-identical; diff against run 1 is exactly the 18 formerly unmapped lines. All 231 counted
  book sentences have an identical sentence in FULL.md; FULL-only restatements 0.
- 17:14 — `census_rm.py` (roadmap census (c)): run 1 exit 0, 92 items, 0 unmapped, but rule (a)
  missed the four "Settled negatively" finding rows (plain first cell). Kept as
  `census_rm.run1.*`; pre-run edit adds rule (f); run 2: 96 items, 0 unmapped, 10 in scope;
  replayed byte-identical.
- 17:14:58 — `statements.py` run 2 (pre-run edit: MLINES replaced by the lines INVENTORY cites;
  run 1 kept as `statements.run1.*`): 104 declarations, 0 missing, 153 manuscript lines; replayed
  byte-identical.
- 17:15–17:19 — `quote_check.py` (are INVENTORY's quotations exact?; countercontrol: an altered
  fragment must fail). Run 1: 122 fragments, 5 FAIL — four quotes carried a markdown asterisk the
  source does not have at that point (Lemma 3 and the ch01 variant, the measure clause, the C2
  process-form theorem), one cited the wrong line (the coreIdx header box); INVENTORY corrected,
  run 2: 122/122 exact. Run 3 (pre-run edit: also check relative `:<n> "…"` citations, resolved to
  the last quoted citation in the record): 124/124. Run 4 (pre-run edit: resolve to the last file
  NAMED in the record): 158 checks, 8 FAIL — three docstrings cited at the def line instead of the
  docstring line, one cited a line late, and four relative citations resolved to ROADMAP instead of
  PhysicalC4Discharge.lean because the record named ROADMAP in between; INVENTORY citations made
  explicit/corrected; run 5 (no script change): 160/160 exact, countercontrol green. Runs 1–4 kept
  as `quote_check.run{1,2,3,4}.*` (script copies for the edited versions: `quote_check.run2.py`,
  `quote_check.run3.py`; run 1 used the run-2 script text before any edit — identical file).
