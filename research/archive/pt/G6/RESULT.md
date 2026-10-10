# G6 RESULT — stage 6 (Q-EX-FULL), step 2: the dependency graph

Thread G6. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`, read-only). Assignment
`PROTOCOL-STAGE6-AMENDMENT-1.md` §A1.4 (`59019538…`) under `PROTOCOL-STAGE6.md` (`b277b7c1…`), AUDIT-I §4–§5
binding. Started 17:56:31Z (`.start_marker`), end marker 18:31:23Z. Deliverables: `GRAPH.md`, `graph.tsv`,
`NOTES.md`, this file, the scripts with their outputs. The graph records dependencies; it derives nothing and
changes no status.

## §0 Answer

- **Graph.** 633 nodes (the inventory ids, unchanged); 1054 dependency edges — 801 recorded, 31 inherited from
  "as Ix.n", 70 to kernel or design declarations without a record, 152 completed from kernel signatures at L
  (122 nodes; file:line cited per edge) — and 495 `yields` edges kept as a control. `graph.tsv` (node table and
  edge table) is a byte copy of `classify.out`.
- **Item 1, partition.** (a) 109: Axioms 1–2; I1.3 (the non-derivability of Axiom 2) as the only consequence of
  the axioms alone; I1.7, I1.8, I2.11 with an observation-base posit (the Definition I1.6, the perspectival
  reading I1.4, the counting measure); 103 premise-free statements about defined objects. (b) 15: C1–C4
  (I1.20–I1.24) and ten derived manuscript H items (I1.17, I1.25, I1.27, I1.28, I1.29, I1.33, I1.34, I2.53,
  I2.54, I2.61), each with the conditions it needs. (c) 172 need an operational hypothesis (most often the
  matrix carrier `FiniteOperationalTheory`, `W d`, the implementation-locality clauses, the K∞ premises,
  `IsNot`/`NativeGate`). (d) 36 need a physical hypothesis (Lemma 3, total finiteness, Substratum A1–A6, the
  mixing hypothesis, E1–E7, M1-T, the Bell branch, H-local-lift, H-scramble, lattice hypotheses). (e) 301 have
  no derivation at L. No kernel declaration at level O, P, M or G is in (a1), (a2) or (b).
- **Item 2, do-not-assume.** 75 flagged rows (I2 11, I3 20, I4 44), each listed with its status at L and the
  kernel relations its status cites. Discharges for particular objects exist at the matrix or substratum-class
  level only (`ContextStable` and `StructurallyClosed` for the substratum class, `HasParallelReferenceExtension`
  for the full theory, `LayerFlowExecutable` under composite unitary control, implementation locality and
  embedded observation for exact QM, `DerivedOI` for the substratum theory), by closed theorems or theorems
  whose premises are the matrix carrier and the flagged QM endpoint. (b), IE1, IE2, frame covariance and `Q3`
  have no kernel discharge at L. No flagged item is a hypothesis of a derived node among the pair premises.
- **Item 3, meeting: NO-MEET.** The ancestor set of `W 3`, `K`, `cnot`, `actC`/`actT`, H1–H3 and (b) has 25
  nodes, all at levels P and O; the descendant set of Axioms 1–2 has 31 nodes, all at level H (manuscript
  records, plus two kernel theorems on passive observability reached through recorded links to Lemmas 2–3).
  They share no node, with or without the `yields` edges and over all edges; a synthetic edge I3.1 → I1.1
  makes them meet (countercontrol). Missing links: manuscript H → kernel H (images only; nearest row the
  stochastic observer interface, OPEN); H/M → O: K∞ and its seams (I3.166–I3.173); H/M/G → P: K2 (I3.165);
  O → P beyond products and involutions: K2's local actions with K∞-Act and K∞-Drive for (b), P-STAGE2 for
  closedness, P-ACT2 for gate preservation, K1 for the selector; H3: no obligation at L.
- **Item 4, check.** `check.py` (independent of the build scripts; rule, sampling rule and sample of 44 in its
  header before run 1): C0 PASS, C1 PASS (every edge target exists), **C2 FAIL** (two cycles between assumed
  records that cite each other: I2.6 ⇄ I2.10, I2.42 ⇄ I2.56), **C3 FAIL** (19 recorded fields agree with the
  signature, 21 omit a declared argument that the graph completes, 4 carry a dependency absent from the cited
  declarations: I2.25, I2.36, I2.96, I3.105); countercontrols behave; no VERDICT line. Both failures concern
  the step-1 records and are reported, not repaired.
- **Item 5.** Statuses are the records' own strings; proved lemmas are traversed to their premises; each
  cross-level edge is marked kernel-supplied or manuscript-asserted, and the meeting result holds under either.
- **Gems (§A.31).** NEW: the descendants of Axioms 1–2 stay at level H; in the records, Lemmas 1–3 do not follow
  from Axiom 1 alone (they pass through I1.4, I1.6 or are themselves assumed / empirically motivated); the two
  co-presupposition cycles and four recorded dependencies absent from their declarations. CONFIRMING: AUDIT-I
  §5.2–§5.3 at the level of the whole graph. BORDERLINE: the physical / operational convention for roots moves
  items only between (c) and (d).

## §1 The graph by section (`GRAPH.md`)

§0 summary · §1 construction (nodes, edges, levels, derived and roots, runs and amendments) · §2 item 1, the
partition with every member listed · §3 item 2, the 75 flagged rows and the discharges for particular objects ·
§4 item 3, Anc(P), Desc(AX), the roots with their missing sources, the five missing links · §5 item 4, the check
· §6 item 5 · §7 findings · §8 what is not claimed.

## §2 Ledger of sources read (read-only)

- Governing texts in the instructed order: `pt/PROTOCOL-STAGE6.md`, `pt/PROTOCOL-STAGE6-AMENDMENT-1.md`,
  `pt/audit/stage6-inputs/I-audit/AUDIT-I.md`, `pt/PROTOCOL-STAGE5.md` with amendment 1, `pt/PROTOCOL-STAGE4.md`,
  `pt/PROTOCOL.md`, amendments 1–2, `pt/INTEGRATION-NOTE-STAGE5.md`, `pt/INTEGRATION-NOTE-STAGE4.md` — in full;
  `pt/base/AGENTS.md` 41–94, §A.21, §A.26, §A.31.
- Step-1 records: `pt/I1/RESULT.md`, `pt/I2/RESULT.md`, `pt/I3/RESULT.md`, `pt/I4/RESULT.md` in full; the four
  inventories (`INVENTORY.md` of I1–I3, `records.txt` and `INVENTORY-HEADER.md` of I4) by script and by targeted
  reads. CENSUS.md and NOTES.md of I1–I4, the stage-4/5 thread records and audits: not needed, not read.
- Kernel at L (`pt/base/verification/lean-mathlib/OIBridge/*.lean`, `OIBridge.lean`): every file by script
  (declaration index, imports, namespaces, signatures); targeted reads of `CompositeDimension.lean`,
  `K2Guard.lean`, `EmbeddedObservation.lean`, `CarrierGeneralOIPlus.lean`, `KInfFoundations.lean` (imports,
  `qubit_certain_face`). Design modules `pt/inputs/fourcopy/*.lean`: declaration index only (for [D] names).
- Not read: `pt/R6/`, `pt/T6/` (R6 seen as a name in the end listing only), `pt/audit/stage3-inputs/OWNER-*`
  (hashed through `ns.manifest.sha256` only), `pt/audit/stage4-inputs/OWNER-*`, `pt/audit/stage5-inputs/`,
  `pt/audit/stage6-inputs/OWNER-*`, `pt/audit/reviews/`, `pt/audit/aborted-launches/`, the `evidence/`
  quarantine copies of `pt/D5/` and `pt/C5/`, `pt/audit/stage6-inputs/I-audit/` other than AUDIT-I.md.

## §3 What is not claimed

- No derivation and no verdict on (b), (b_min), `K = Q3` or Q-EX-FULL; no status upgraded or changed.
- "Consequence" means reachable by recorded or kernel-completed dependency edges, not proved; (a0) members need
  no premise and say nothing about the axioms.
- NO-MEET is a statement about the record graph at L under the stated edge rules, not that no bridge can exist.
- Kernel completion covers 122 of the 252 derived kernel-proved nodes (those whose header names a theorem at
  L); `variable` binders are taken without section scoping; hypotheses written after the colon are not
  declared arguments. The check's agreement verdicts hold for the 44 sampled theorems only.
- The root categories (physical, operational, observation-base) are a convention fixed in NOTES N2 and
  disclosed with its sensitivity; every root is listed by id.

## §4 Evidence log

Every script runs from `pt/G6/` as `python3 -I -B <name>.py`, stdout to `<name>.out`, stderr plus an appended
`exit N` line to `<name>.err`; decision rule in the header before the first run, amendments written into the
header before the run they govern; superseded runs kept as `<name>.runN.*`; every final script replayed into
`<name>.replay.{out,err}` and compared with `cmp`: 5/5 byte-identical.

| script | role | runs (kept) | final result | replay |
|---|---|---|---|---|
| `parse.py` | node table of the four inventories | 1 | P1–P3, C1 PASS; `VERDICT PARSE VALID` | identical |
| `edges.py` | edges R, RA, RN, KC, Y | 4 (run 1 `.run1.{py,out,err}`; runs 2–3 `.run2/.run3.{out,err}`, scripts amended in place) | E1–E3 PASS; `VERDICT EDGES VALID` | identical |
| `classify.py` | classes, `graph.tsv` | 5 (runs 1–4 `.runN.{py,out,err}`) | G1–G3 PASS; `#VERDICT GRAPH VALID` | identical |
| `analyze.py` | items 1–3 | 3 (run 2 `.run2.{py,out,err}`; run 1's output overwritten, NOTES N4) | A2, A3 PASS; NO-MEET; `VERDICT ANALYSIS COMPLETE` | identical |
| `check.py` | item 4 | 3 (runs 1–2 `.runN.{py,out,err}`) | C0, C1 PASS; C2, C3 FAIL; CC1–CC3 behave; no VERDICT | identical |

sha256 of every file in `pt/G6/` other than this one (58 files, computed 18:31:39Z after the last write to
each; `graph.tsv` = `classify.out`):

```
9b8870114d65aeca027e5cf6d7b2372bb45c6ad826ba9730750f2aff8f1d1b8b  .end_marker
a5c623c34f43670461935365852a1a34d7563f833a8d95b9664d5282b88b4a61  .start_marker
83f4619f48982f881e43b0a19c14b7c6cc182179ea2a3c69dcf5992c4aab342c  GRAPH.md
7fa860fae018baaab710eb6b8de462c5171595d0601fef094a652a49e88ff501  NOTES.md
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  analyze.err
d9b5c5cce2664f15e5a77402bb3a069e3696d86cd8bfd53daa764c75a075526f  analyze.out
e005abfadb612889f4df61c1cf1c3f4421759a457706879e3a13e4b5643915a0  analyze.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  analyze.replay.err
d9b5c5cce2664f15e5a77402bb3a069e3696d86cd8bfd53daa764c75a075526f  analyze.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  analyze.run2.err
940cb210cb624c2ba4bcef5ec41131f1d912de87689d9b625f6f926c268260fa  analyze.run2.out
ec667aee2cd03248c9c28a1914eb52158be40b14bd85a1010aabcf44ed592675  analyze.run2.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  check.err
35f4acbc3fc93a813e4c58597846c6fa299c3264eb244830ce79629430bc1b6d  check.out
dbe5a102a389d5d2005303ab89d4a8d0789ba06955c92662fef12b2316c88b4b  check.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  check.replay.err
35f4acbc3fc93a813e4c58597846c6fa299c3264eb244830ce79629430bc1b6d  check.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  check.run1.err
cafcef9299ef3aed7977a1e83fcfbbdd5a33163f62ea595c13e874f4eca6668c  check.run1.out
2011ac03b5ef9f42d790c15ca85888a6945009cdb12187d86b090f5c31cd2a9b  check.run1.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  check.run2.err
c0d42ac5179ffc1704b4c8142f1d5e2244c1ffad41bb3fc8ef0822e5e698e017  check.run2.out
d751cbc21faec00043d58d068ede6494c10922606064bf25efc853f5bb7a0b34  check.run2.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  classify.err
af8d62ee7a0e7d8eedcc589628536b5334a3f4cc9a4b5bd4945fb369bb13c0ad  classify.out
6909d71b04c66ba2c1a8c47ffbac9978de10d16b3f924dbff59944ef83b4180b  classify.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  classify.replay.err
af8d62ee7a0e7d8eedcc589628536b5334a3f4cc9a4b5bd4945fb369bb13c0ad  classify.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  classify.run1.err
1922e0539366486498bbdb21424cf81c9fb0ede0299858ba799c8827d15e27f2  classify.run1.out
f90a8da07e19c5c82b244a31157ebadf4ac583b0b114ed08465ef548945b067b  classify.run1.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  classify.run2.err
50dcf16e184e9d3854ea7599ee122c2fdcc6faf7a6a1d74f7bf471f35fabe3c9  classify.run2.out
7b52aafb0ff4e0b47e1afe577cfbe02a0e36d2934e3a0d21ddf71b2b78f09dd7  classify.run2.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  classify.run3.err
4f849e65a5a22369fcd0c2982a387a7cb5180418a088141fa8e12d37556d2763  classify.run3.out
473251bd62cef03562f8dd778b0c40c712f54168e503627d9bce001750fdb6b4  classify.run3.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  classify.run4.err
63cc2f1c26d9a7a2887437573654510c90a2cbf5b56e0dbf1b5cb1a7e33b40ca  classify.run4.out
8f6a2aa3c63829812f7c4e8c55e0f69488b0bbeda8773dc7620329b16dd456a1  classify.run4.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  edges.err
e33e73340a917b8303bce4813928e276bee6a38513acf0dad65f8136762f906b  edges.out
accbc7a8cac6fbf19dc80aaed203ff64caa66c921d9779db9c9c55d36c684eed  edges.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  edges.replay.err
e33e73340a917b8303bce4813928e276bee6a38513acf0dad65f8136762f906b  edges.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  edges.run1.err
89aa9d8bdcf8c452c723c8f955ac7a3b74e47894a2f0a0b7faea4fd4db4bb192  edges.run1.out
d42c0a6bfe48ca7c706c2e17300fe23a0d98dedfa2260a684205f04b908b9add  edges.run1.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  edges.run2.err
6437ad6ba1385b679a745bf45f348dfc08b4ae3383664e0fa0826610f9c6de83  edges.run2.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  edges.run3.err
b122a8efc1f4371be2b61c7b25084588add9c6022c8d4ed007bc59b5a64e94a1  edges.run3.out
af8d62ee7a0e7d8eedcc589628536b5334a3f4cc9a4b5bd4945fb369bb13c0ad  graph.tsv
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  parse.err
d75be47d0a59c887f3a89ed9b11e500c08b8b55a074b96d0e5c543582f4694e5  parse.out
749e2f88a0845ba4faba3b414b9dfb160655f8ad2625002ca98de4c533c133e7  parse.py
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  parse.replay.err
d75be47d0a59c887f3a89ed9b11e500c08b8b55a074b96d0e5c543582f4694e5  parse.replay.out
```

## §5 Integrity

- **Start** (`.start_marker`, 17:56:31Z, written first into `pt/G6/`, which was absent at 17:56:15Z): six
  manifests `sha256sum -c --quiet` exit 0; `audit/stage3-inputs/ns.manifest.sha256` OK from its own directory;
  base HEAD = L, `status --porcelain` empty, no `__pycache__`/`.pyc`; the eleven protocol files at their
  prefixes (239dc123, b41aa0e7, 2a2f78f3, 38603692, 086a4cb8, 1a649168, d3da2811, 9e01f098, 1f639115,
  b277b7c1, 59019538) and every sidecar OK (six from `pt/`, five from SCRATCH); `pt/` listing recorded. No
  `pt/R6/` or `pt/T6/` existed.
- **End** (`.end_marker`, 18:31:23Z): the same checks, all green; no bytecode under `pt/base` or `pt/G6`. New
  top-level name since the start: `R6` (18:31:06Z; names only, never read). **Sweep:** no file under `pt/` newer
  than `.start_marker` outside `pt/G6/`, `pt/R6/`, `pt/T6/`, `pt/I1/`–`pt/I4/`, `pt/D5/`, `pt/C5/`, `pt/audit/`,
  `pt/audit*-replay/`; the only path printed is the directory `pt` (mtime changed when `R6` was created). No
  anomaly; nothing quarantined; no `evidence/` directory was needed.
- **Writes.** Only inside `pt/G6/`. Authored files written in parts of at most 250 lines per write call;
  `graph.tsv` is a byte copy of a script output; the table of GRAPH.md §3 was formatted from `analyze.out` with
  `awk` into `s3.tmp` and appended. Temporary files (`s3.tmp`, `c.tmp`, `a.tmp`, `*.final.tmp`) were created in
  `pt/G6/` and removed. Script edits between runs used inline Python editing helpers reading stdin and `sed -i`
  on this thread's own scripts (not evidence runs).
- **Deviations, recorded.** (1) Amendment headers were first stamped with times ahead of the clock; the stamps
  were corrected in the final scripts (comment-only; outputs re-verified byte-identical); the kept copies
  `classify.run3.py` (18:20Z for 18:18Z) and `check.run2.py` (18:24Z for 18:22Z) keep the uncorrected stamps.
  (2) The run-2 and run-3 versions of `edges.py` are not kept as separate files (amended in place; their outputs
  are kept). (3) `analyze.py` run 1's output and the outputs of `analyze.py` / `check.py` on intermediate graphs
  were overwritten by re-runs of unchanged scripts on later graphs (NOTES N4, 18:25Z, 18:27Z). (4) The
  classification rules of NOTES N2 were re-scoped after `classify.py` run 1 (post hoc, disclosed with the
  sensitivity in GRAPH.md §1–§2). (5) `check.py` run 1 was stricter than NOTES N1's definition of DISAGREE and
  was amended to it; runs 1–2 printed a hash-seed-dependent first cycle, fixed in run 3.
- **Holds.** Git used only for `rev-parse HEAD` and `status --porcelain` with `GIT_OPTIONAL_LOCKS=0`. No branch,
  commit, PR, CI, network, publication or sub-agent. No manuscript, kernel or record file was edited.
