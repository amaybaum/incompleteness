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
