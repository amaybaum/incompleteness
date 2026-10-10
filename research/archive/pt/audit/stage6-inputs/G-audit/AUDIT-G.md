# AUDIT-G — coordinator's audit of G6 (stage 6, step 2: the dependency graph)

Base L = `9f9f8257…`, read-only. Written 2026-10-10, 18:46Z, after G6 reported (`.end_marker` 18:31:23Z).
Inputs read: `pt/G6/RESULT.md` (sha256 `0e0afe04…`), `pt/G6/GRAPH.md` (`83f4619f…`), `pt/G6/graph.tsv`
(`af8d62ee…`), G6's script outputs and its §4 hash list. Nothing under `pt/G6/` was modified. My own baseline
(`parse_inventories.py`, written before G6 reported) and my check (`check_graph.py`) read G6's table as data only.

## 1. Mechanical verification

- **Hashes.** `g6_listed_hashes.txt`: all 59 files G6 lists in RESULT §4 verify (`sha256sum -c`, 59/59 OK);
  RESULT.md itself hashes to `0e0afe04…`.
- **Replays.** `replay/REPLAY-LOG.txt`: the five final scripts (`parse`, `edges`, `classify`, `analyze`, `check`)
  re-run from a copy under `G-audit/replay/` with `python3 -I -B`, stdout and stderr byte-identical to G6's own
  outputs, 5/5 (18:35:37Z–18:35:40Z).
- **Integrity.** G6's start (17:56:31Z) and end (18:31:23Z) markers carry the manifest checks, base HEAD = L,
  clean porcelain, the eleven protocol prefixes and sidecars; sweep clean (the only newer path is `pt` itself,
  whose mtime changed when `pt/R6/` was created); writes only under `pt/G6/`; temporary files removed. No
  bytecode under `pt/base` or `pt/G6`.

## 2. Independent check (`check_graph.py`, run 3: 11/11 CONFIRMED, `CHECK-G-FIXED`, replay byte-identical)

Baseline: `parse_inventories.py` run 3 (`BASELINE-FIXED`, 6/6; replay identical): 633 records (85, 113, 187,
248), 538 `depends_on` id-edges, 391 `yields` id-edges, no dangling id. Decision rule in the check's header
before its first run; own BFS and Tarjan code.

| id | claim checked | result |
|---|---|---|
| G1 | G6's node set = the 633 baseline inventory ids | confirmed |
| G2 | class counts a 109, b 15, c 172, d 36, e 301 | confirmed |
| G3 | edge kinds R 801, RA 31, RN 70, KC 152, Y 495 | confirmed |
| G4 | every baseline `depends_on` id-edge is an R/RA edge of G6, or a `yields` mention my parser absorbed from the same line | confirmed: 62 baseline edges absent from R/RA, all of them Y edges in G6 (verified by reading the I2 records in run 1 → run 2) |
| G5 | Anc(P) from the pair seeds lies at levels P and O only | confirmed: 18 inventory nodes with my seed list (`W d`, `actT`, `actC`, `cnot`, H1–H3, the four (b) forms), levels P/O |
| G6 | Desc(AX) (nodes depending transitively on Axioms 1–2) lies at the manuscript levels H/X, never O or P | confirmed: 31 nodes, the same count as G6's; two nodes' spans also name M (I1.17 `H→M`, I1.34 `H→M/X`), one `H/X` |
| G7 | Anc(P) ∩ Desc(AX) = ∅ with and without the `yields` edges | confirmed (NO-MEET) |
| G7c | countercontrol: a synthetic edge I3.1 → I1.1 makes them meet | confirmed (meet size 7) |
| G8 | the only nontrivial SCCs over dependency edges are {I2.6, I2.10} and {I2.42, I2.56} | confirmed |
| G9 | a1 = {I1.3}; a2 = {I1.7, I1.8, I2.11}; b = C1–C4 (I1.20–I1.24) + {I1.17, I1.25, I1.27, I1.28, I1.29, I1.33, I1.34, I2.53, I2.54, I2.61} | confirmed |
| G10 | no kernel-proved node at a kernel level (O, P, M, G) is in a1, a2 or b | confirmed: no offender; the manuscript records in b whose span names M/X are I1.17, I1.34, I2.61 |

**Reconciliation of the Anc(P) count.** G6 reports 25 nodes; my G5 rule counted inventory nodes from my own seed
list and found 18. With G6's seed list (NOTES N3 adds `CandidateCone` I3.43) my BFS over G6's dependency edges
gives exactly 25: 21 inventory nodes (the 18 plus I3.43, `maxCone` I3.3, `IsEffectOn` I3.58) and 4 kernel
declarations reached by RN edges (`prodEffVal`, `cnot_prodEffVal_nonneg`, `hom`, `homMap`), all at levels P and O.
G6's count stands. (Run 1 of my check, 7/11, is kept: a level regex that caught letters inside parentheticals,
G4 before the `yields` reading, and G10 applied to manuscript records; run 2, 11/11, is kept because its G5/G6
detail strings printed tallies in set-iteration order and did not replay byte-identically — the same class of
defect G6 found in its own `check.py` runs 1–2; run 3 prints them sorted.)

## 3. G6's own check (item 4) and what it found

- **C2 FAIL: two 2-cycles** between assumed records that cite each other, I2.6 ⇄ I2.10 and I2.42 ⇄ I2.56 — my G8
  reproduces exactly these two SCCs and no other. Neither cycle meets Anc(P) or Desc(AX) (GRAPH.md §5).
- **C3 FAIL: 4 DISAGREE** (I2.25, I2.36, I2.96, I3.105): the record's `depends_on` names a dependency absent from
  the cited declaration's arguments. On reading, these are proof-level or definition dependencies (what the proof
  uses, or what a definition unfolds to) written into a field whose schema asks for declared hypotheses. 21
  INCOMPLETE-RECORDED fields omit a declared argument that G6's kernel completion supplies (mostly the carrier).
- **Classification:** record-hygiene findings about the step-1 inventories, reported and not repaired (G6 changed
  no record, per the amendment). They bear on no status and on no bridge: the four DISAGREE items are not in
  Anc(P), and the kernel-completed edges (KC) supply the declared arguments wherever a record omits them. They go
  to the integration note as record items for the inventories (ids kept, no renumbering; AUDIT-I §4).

## 4. G6's disclosed deviations (RESULT §5), assessed

1. Amendment header times first stamped ahead of the clock, corrected in the final scripts; the kept copies
   `classify.run3.py`, `check.run2.py` keep the uncorrected stamps. Cosmetic; outputs re-verified byte-identical.
2. `edges.py` runs 2–3 amended in place, scripts not kept (outputs kept). A departure from "failed runs kept as
   `.runN.*`" for the scripts; the final `edges.py` replays identically and its edge set is what every later
   result reads, so no claim rests on the lost versions. Process deviation, recorded.
3. `analyze.py` run 1's output and intermediate outputs of `analyze.py`/`check.py` overwritten by re-runs of
   unchanged scripts on later graphs. Same assessment as 2.
4. **Post-hoc re-scoping of the classification rules** (NOTES N2) after `classify.py` run 1: d 63 → 36; (a1),
   (a2), (b) changed only by I2.53 and I2.61 entering (b). This is the one substantive deviation: the partition's
   rules were adjusted after an output was seen. G6 disclosed it with the sensitivity (GRAPH.md §1–§2, §7 item 6).
   Audit position: the partition (item 1) is a classification convention over fixed edges, not a verdict; item 3
   (NO-MEET) reads only the edge table, which my own BFS reproduces, and every baseline edge parsed from the
   inventories before G6 reported is among G6's R/RA/Y edges (G4). The re-scoped partition is accepted as a
   disclosed convention; the integration note cites its class counts as G6's convention and NO-MEET as the result.
5. `check.py` run 1 stricter than NOTES N1's DISAGREE definition, amended to it; runs 1–2 printed a
   hash-seed-dependent first cycle, fixed in run 3. Fine; the final check replays identically.

## 5. Verdict

The graph stands. Node set, class counts, edge kinds, inclusion of every baseline edge, the levels of Anc(P) and
Desc(AX), their disjointness with and without the `yields` edges (NO-MEET) with its countercontrol, the two
cycles, the sublabel memberships and the no-kernel-node-in-(a)/(b) claim are all reproduced by independent code
that reads G6's table as data. G6's checks C2 and C3 are findings about the step-1 records, not about the graph.

Carried to T6 and the integration note:

- **NO-MEET at L** (G6 item 3, confirmed): no dependency path at L joins the descendants of Axioms 1–2 (levels
  H/X, with two manuscript spans reaching toward M) to the ancestors of the pair-level objects (levels P/O). The
  "complete applicable premise set" T6 tests is therefore the set of items that reach the pair cone at L — R6's
  199-item list, of which 68 are NOT REACHED — and no H-, M- or G-level item enters a derivation of (b) at L
  except through an obligation G6 names (K2, P-STAGE2, P-ACT2, K∞-Act, K∞-Drive, K1).
- **Do-not-assume items** (item 2): no flagged item is a hypothesis of a derived node in Anc(P); discharges for
  particular objects exist at the matrix or substratum-class level only; (b), IE1, IE2, frame covariance and
  `Q3` have no kernel discharge at L.
- **Record items** for the inventories: the two co-presupposition cycles; the four DISAGREE fields; the 21
  fields that omit a declared argument.
- **Wording:** G6 §0's "all at level H" for Desc(AX) should read "all manuscript H/X records, two of whose spans
  also name M (I1.17, I1.34)"; the same two appear in (b) (G10).

Gem classification (§A.31): CONFIRMING (AUDIT-I §5.2–§5.3 at the level of the whole graph), NEW as record findings
(the cycles and the DISAGREE fields), BORDERLINE (the root convention, which moves items between (c) and (d) only).

## 6. Files (sha256)

```
471978428dceb4f7ab554227d7f96fea9c7c2ee88c60c173efc1d8c3c2e2848d  check_graph.py          (run 3)
1101926ccb9bca6fe9115b97123c0586013efc07b8557e4fd7e6b650f04e8956  check_graph.out         (11/11, CHECK-G-FIXED; replay identical)
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  check_graph.err         (exit 0)
2b5f6b73c32ba2a61ffe2ad27251889373406893607f90cc84db222950e9eaba  check_graph.run1.py     (kept, 7/11)
d34910a0122144dddc81f6288048ccd7f02c3f48855119812c0831d998acc6f1  check_graph.run1.out
5c6547acb0f1ff203d7220996eb9622d8f19d5204c49c721a0579b3ff10230ec  check_graph.run2.py     (kept, 11/11, replay differed in detail order)
c4c3b031ed7d0ea83df7278b6e5b1c1caa1ac4a276c462e2e86b59f86e3afe4e  check_graph.run2.out
7f8a0d00a30a60e9634098dd8abfa917b5fde9756da4fc54f52bc23bdef0cf19  parse_inventories.py    (run 3; runs 1–2 kept)
411bcd15c1ba91851478e409f4498c762e57eb8e7d72128c5f90166f510c8622  parse_inventories.out   (6/6, BASELINE-FIXED; replay identical)
3d360a7b8c552e5b228f0515b17695a26f1184c80677848a09b1ac854ba4ded7  nodes.tsv
2dc904015c4fdac76d5f01481a6137f6ad596c1184e9b1b3afc94095ee32ed48  edges_by_id.tsv
31012b57c94b3eb64c24e27a6c59de8dbed30cc6d6de87c7a3ec96b012505b29  g6_listed_hashes.txt    (59/59 OK)
dac89f0fd6b27196f9b0a82168b65f32a916351c25b7fdc447a9081cdf2b3fd3  replay/REPLAY-LOG.txt   (5/5 IDENTICAL)
```
