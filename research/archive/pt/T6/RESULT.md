# T6 RESULT — the test of (b) against the complete applicable premise set at L (stage 6, Q-EX-FULL, step 4)

Thread T6, research only, read-only on the corpus. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`).
Governing texts `PROTOCOL-STAGE6.md` (`b277b7c1…`), `-AMENDMENT-1.md` (`59019538…`, A1.6–A1.7), `-AMENDMENT-2.md`
(`748f1764…`, A2.1–A2.4), with AUDIT-I (`845bd662…`), AUDIT-G (`3fd6763d…`), AUDIT-R (`04308355…`) binding.
Deliverables in `pt/T6/`: `TEST.md`, `NOTES.md`, this file, five scripts with outputs, replays and two kept runs,
`.start_marker`, `.end_marker`. Order of the last writes: this file's §0–§3, then `.end_marker`, then §4–§5.

## §0 Answer

**INDEPENDENCE** (two-way form of `PROTOCOL-STAGE6.md` step 4, as stated by A2.4).
- **Derivation: failed, wall located.** No chain from inventory items at their actual status reaches (b) in its
  weakest sufficient form. At L there is no H→P, M→P or G→P bridge even at the level of declarations (t1: the only
  module whose import closure reaches both the pair vocabulary and the H/M/G vocabulary is the root, whose 65
  declarations carry neither); the only kernel theorems that quantify over a pair cone are the reflY no-go
  (K2Guard.lean:143) and its restatement, and none of the 39 theorems mentioning `actC`/`actT` concludes the invariance
  of a pair cone (t2); the kernel-completed edges add no H/M/G premise to Anc(P) (t2); the ten object-specific
  discharges are closed statements about objects off the pair carrier (t2). The chain stops at the step "`actτ R(t)`
  preserves `K` for the flow and `J`", for which L has no premise; every route that supplies it uses a do-not-assume
  item, a design-run [D] item, a PT-record candidate, or a level-M clause without a bridge.
- **Countermodel: K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F**, rebuilt from the kernel's definitions with my own exact code
  (t3, 17/17; self-duality by a complete written proof, TEST §3.3). Row by row against R6's audited Table A2 with my
  own re-checks (t4): 115 SATISFIES, 3 SATISFIES vacuously, 68 NOT REACHED, 13 FAILS — every non-hypothesis row
  SATISFIES or NOT REACHED, every FAILS row a hypothesis (do-not-assume, [D] not at L, PT-record). Exact witness of
  the violation: for every unit axis `n`, either token and every `s`, `ipW(R_n(t)_τ z_s, R_n(π/2)_τ p_s) = −sin(t)/8`
  with `R_n(π/2)_τ p_s ∈ Q3 ∩ Z_F* ⊆ K(Z_F)` (t3, t5); `cyc3^{±1}` likewise (−1/8). So every member with `sin t ≠ 0`
  of the drive through the NOT (`R_x`), of ball3Drive's flow (`R_z`), of their J-conjugates, and `J` itself, moves
  K(Z_F) out on the control, on the target and in the mixed placement: every weakest sufficient form of (b) fails.
- **Missing assumption:** A_miss — for one token τ, `K` is invariant under `actτ R_x(t)` and `actτ R_z(t)` for all `t`
  (ball3Drive's flow and its `J`-conjugate; equally the drive through the NOT with the phase flow about z). With
  H1–H3 it forces `Q3` (stage 4 [A]) and hence (b). **Disguise test: fails** — it restates I3.153 (b_DJ) and the clause
  "local actions compatible with the composite cone" of I3.165 (K2), both do-not-assume, and is the drive instance of
  observational independence (I4.3 / I4.82 / I4.96, level M, do-not-assume). The candidates that pass the disguise
  test and would close the gap are not items at L: λ (KT4Core with `tok`, [D], no ≥3-token structure at L) and pair
  homogeneity H (PT-record, [W + L]).
- **Scope:** independent of the items that reach the pair cone at L, as stated; the 68 H/M/G items are NOT REACHED
  (no bridge), never satisfied or failed; no embedded-observer realization of K(Z_F) is claimed and none is obstructed
  at L. Gem classes: ELABORATING (the wall located exactly; a self-contained H3 proof; the closed-form flow law for
  every axis — K(Z_F) has no one-parameter local rotation symmetry), CONFIRMING (declaration-level NO-MEET; discharges
  off P), POSITIVE (R6's 199-row classification survives an independent re-check), BORDERLINE (with the certified
  ball3Drive the two weakest forms of the stage-5 note are the same pair of flows). No NEW finding; fixed point.

## §1 Node by node (details: TEST.md §2–§5, NOTES N3–N8)

| node | question | evidence | verdict |
|---|---|---|---|
| D1 | does any H/M/G item reach `W 3` through a bridge at L? (per route: α, β, γ, δ, ζ, DerivedOI, CompletedOI, sealed core) | [X t1 run 2, 2 countercontrols; W Lean scoping; K the M-level carriers read] | no bridge; each route ends at an obligation (K2; P1 ROADMAP.md:68) |
| D2 | do the P/O kernel content, B1–B7, the reflY no-go or the KC edges force (b)? | [X t2: 9 cone-binders, 39 act-theorems classified; Anc(P) 25 nodes P/O; K K2Guard:143] | no: no theorem concludes a cone invariance; KC adds nothing |
| D3 | does a discharge for a particular object reach the composite cone? | [X t2 (d): 10 discharges, carriers, closure] | no: all closed statements off P (substratum class, MixC, exact QM, genTheory, substratum theory) |
| D4 | the direct chain from the reached items | [W] step table TEST §2.4 | fails at "flow and J preserve K": no premise at L |
| C1 | K(Z_F): H1, H2 (level (ii)), H3, K ≠ Q3, slice, I3.44 consistency, witnesses | [X t3 17/17; W TEST §3.3–§3.4] | countermodel valid; (b) violated for every tested map on each token |
| C2 | row by row against R6's Table A2 | [X t4 VERDICT ROWS-OK] | 118 SATISFIES (3 vacuous), 68 NOT REACHED, 13 FAILS — all hypotheses |
| C3 | every axis | [X t5 VERDICT C3-ALL-AXES] | no one-parameter rotation subgroup of either token preserves K(Z_F) |
| M1 | missing assumption, disguise test | [W] TEST §5 | A_miss = (b) for {R_x, R_z} on one token; fails the disguise test; λ, H pass but are not at L |

## §2 Ledger of sources read and not read

- **Read, in the prescribed order and in full:** `pt/PROTOCOL-STAGE6.md`, `-AMENDMENT-1.md`, `-AMENDMENT-2.md`,
  `pt/audit/stage6-inputs/I-audit/AUDIT-I.md`, `G-audit/AUDIT-G.md`, `R-audit/AUDIT-R.md`, `pt/PROTOCOL-STAGE5.md` with
  its amendment 1, `pt/PROTOCOL-STAGE4.md`, `pt/PROTOCOL.md`, `pt/PROTOCOL-AMENDMENT-1.md`, `-AMENDMENT-2.md`,
  `pt/INTEGRATION-NOTE-STAGE5.md`, `pt/INTEGRATION-NOTE-STAGE4.md`; `pt/base/AGENTS.md` lines 41–94, §A.21 (:436),
  §A.26 (:223–246), §A.31 (:306–342). The stage-2/2-DS/3 protocols were verified in the start marker;
  `PROTOCOL-STAGE3.md:30–69` read (levels (i)/(ii)).
- **Step-2/3 records (A2.1):** `pt/R6/RESULT.md`, `REASSESSMENT.md` (all tables), `r1_inventory.out` (199 APPL lines,
  parsed by t4), `r2_cones.py` lines 1–170 (conventions); `pt/G6/RESULT.md`, `GRAPH.md` §3–§4, `graph.tsv` (parsed by
  t2 as data).
- **Step-1 records:** `pt/I3/RESULT.md` in full; `pt/I4/records.txt` (six records by line).
- **Stage-3 record:** `pt/X/RESULT.md:170–209` (the K4 instance, G16, SD2 sketch).
- **Kernel at L (read-only):** K2Guard.lean (whole); CompositeDimension.lean:80–254, :730–869; KInfFoundations.lean
  :250–309, :395–504; CompositeInterface.lean:200–274, :436–450; ReferenceExtension.lean:440–456;
  ImplementationLocality.lean:355–376; LiftAudit.lean:105–116; OperationalAssembly.lean:585–610; the root
  `OIBridge.lean` head; the whole tree and the root by script (t1, t2, t4). Roadmap: ROADMAP.md:68, :1001–1006.
  Manuscripts and book: scanned by t1 (B5) only.
- **Not read:** `pt/audit/stage3-inputs/OWNER-*` (the directory was entered only to run `sha256sum -c` on
  `ns.manifest.sha256`), `pt/audit/stage4-inputs/OWNER-*`, `pt/audit/stage5-inputs/`, every file of
  `pt/audit/stage6-inputs/` other than the three audits named above, `pt/audit/reviews/`,
  `pt/audit/aborted-launches/`, the `evidence/` copies under `pt/D5/` and `pt/C5/`; the D5/C5/Y/Z thread records and
  the stage-4/5 audits were not opened beyond what the integration notes and R6 cite (their results enter as [A]).

## §3 What is not claimed

- No status of any inventory item changes; no item is upgraded; a FAILS is the failure of a hypothesis.
- INDEPENDENCE is relative to the items that reach the pair cone at L as stated — not to every extension of the
  framework, not to a future H→P or M→P bridge, not to the hypotheses λ, H, T.
- No embedded-observer realization of K(Z_F) and no obstruction to one (open at L).
- Cited, not re-proved [A]: stage 4's "(b_S4) with H1–H3 forces `Q3`" (Y2), the C5 census (minimality of {flow, J}
  in the native repertoire), the [D] theorem `kt4_forward_ie1`, R6's FCC values, stage 4 Y6 (H, T), stage 2's
  FC ⟺ IE1 given hgate. G16 ⊆ Gbig is read from its definition (PROTOCOL-STAGE3.md:51–52).
- Instance checks (t3 Z4) are instance-scoped; the universal statements rest on the written proofs (TEST §3.3) and on
  the symbolic identities (t3 Z3, flow law; t5).
- The dictionary `M(ω) = Σ ω σ⊗σ` (the [D] `pauliW` up to normalization) is used only to construct and verify the
  model, never as a premise.

## §4 Evidence log

Every script ran from `pt/T6/` as `python3 -I -B <name>.py`, stdout to `<name>.out`, stderr plus an appended `exit N`
line to `<name>.err`; the decision rule is in each header before its first run; amendments after a run are recorded
in the header and in NOTES, with the earlier run kept as `<name>.run1.{py,out,err}`; every final script was replayed
into `<name>.replay.{out,err}` and compared with `cmp`: 5/5 byte-identical on stdout and stderr (19:20Z). Every
`.err` is the single line `exit 0`. Exact arithmetic only (fractions; sympy rationals with I and square roots).

| script | node | result | runs | replay |
|---|---|---|---|---|
| `t1_bridges.py` | D1 | `VERDICT NO-BRIDGE-AT-L` (MEET = root only; root declarations carry neither vocabulary; 1 roadmap line, P1) | 2 (run 1 kept: false P-anchor `W` in WeylTwirl, verdict unchanged) | identical |
| `t2_pairthms.py` | D2, D3 | `VERDICT D2-D3-SCAN` (9 cone-binders, 39 act-theorems, 3 ACT-MEM read; Anc(P) 25 P/O; DISCHARGE-OFF-P) | 2 (run 1 kept: level-string parse) | identical |
| `t3_countermodel.py` | C1 | `VERDICT C1-KZF-EXACT`, 17/17 | 1 (pre-run edits in the header) | identical |
| `t4_rows.py` | C2 | `VERDICT ROWS-OK` (199 rows; 115 + 3 SATISFIES, 68 NOT REACHED, 13 FAILS hypotheses) | 1 (pre-run edit in the header) | identical |
| `t5_axes.py` | C3 | `VERDICT C3-ALL-AXES` | 1 | identical |

sha256 of every file written in `pt/T6/` other than this one (the hash of RESULT.md is given in the final report):
```
ffc804677737039a2e08a13585adbdf423a0aa15e1177120a0b79402944831d7  .start_marker
5eaf61d2bfd3c64a67aea49473dbd3af6e154c546383acb59b055fea50dc3c98  .end_marker
bf1bc7c6d88ff697ef3c1fd5ae7cb36091e8e5aabe2f6df3e5eae4de9d2b633e  NOTES.md
e007939c78da0fa1f9990b05f47971c0297acfe609c050de1090ba596f20d287  TEST.md
da62dcca5b7b00a35da2999ff889fd7227898491c479294c01f80e8b6ff23a42  t1_bridges.py
180799a9e558a8201e9d007450a4e07288c9d480218d1393e6d94de3dcff7a8d  t1_bridges.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t1_bridges.err
180799a9e558a8201e9d007450a4e07288c9d480218d1393e6d94de3dcff7a8d  t1_bridges.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t1_bridges.replay.err
862fdc353fd72cc010c43669dc2d456f413725e83adf26244a6eabc83616d0af  t1_bridges.run1.py
71b3280c30f325d4a6f03cbdb7b8e91a3030bb69e38b394c1b1e4952eb5a0e0f  t1_bridges.run1.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t1_bridges.run1.err
91f171daa23b2ab46d60785a2b436df9389dd9f04d94b3657d2f492b4e0bddeb  t2_pairthms.py
a0aaef771e876e343edee2da2f0ad8050f86d95d03990db57ac1e6afa549572f  t2_pairthms.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t2_pairthms.err
a0aaef771e876e343edee2da2f0ad8050f86d95d03990db57ac1e6afa549572f  t2_pairthms.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t2_pairthms.replay.err
82702784267c7a95787c633a2174fdd6bd5d2ca47c062f657b6d836079c0a0c0  t2_pairthms.run1.py
674f19835cfd86d8522715b13f32698917fa33ef2c6b102140a443ffeb9b4a88  t2_pairthms.run1.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t2_pairthms.run1.err
ba9f5a84f4e5d550f1a42d4965229871274d025d2400c5a2da4e3a2e4e2fdcfb  t3_countermodel.py
3dd1658287b764a3d23aa100c5c3cd8c0f05e48e767882844343bf4e36a21314  t3_countermodel.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t3_countermodel.err
3dd1658287b764a3d23aa100c5c3cd8c0f05e48e767882844343bf4e36a21314  t3_countermodel.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t3_countermodel.replay.err
9a815c9ed50ea64981bfcd8c54a8ed4f92259335e7cfba2e940f857cc0511c61  t4_rows.py
b457aa4061f9d69e20c54c6efc669c24acc9f13b4a63049a17c0f2e6c698ed1d  t4_rows.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t4_rows.err
b457aa4061f9d69e20c54c6efc669c24acc9f13b4a63049a17c0f2e6c698ed1d  t4_rows.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t4_rows.replay.err
2389e639dd34ca5d506901b4793e6343389f33a6fee11223fa366dbf7cb52bdc  t5_axes.py
5bb4f1b84efb48f175cb81d82398c2503d1df6702c9e854bdf843f784a6638b8  t5_axes.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t5_axes.err
5bb4f1b84efb48f175cb81d82398c2503d1df6702c9e854bdf843f784a6638b8  t5_axes.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  t5_axes.replay.err
```

## §5 Integrity

- **Start** (`.start_marker`, the first file written into the newly created `pt/T6/`, which did not exist; 18:50:48Z):
  the six manifests `inputs`, `stage1`, `inputs2`, `inputs3`, `stage2`, `inputs4` exit 0 (`sha256sum -c --quiet`
  from `pt/`); `ns.manifest.sha256` exit 0 from `pt/audit/stage3-inputs/`; base HEAD = L, `status --porcelain`
  empty (`GIT_OPTIONAL_LOCKS=0`), no `__pycache__`/`.pyc` under `pt/base`; the twelve protocol files at their prefixes
  (239dc123, b41aa0e7, 2a2f78f3, 38603692, 086a4cb8, 1a649168 with their sidecars from `pt/`; d3da2811, 9e01f098,
  1f639115, b277b7c1, 59019538, 748f1764 with their sidecars from SCRATCH); `ls -la pt/` recorded. The three audits
  verified at their prefixes 845bd662, 3fd6763d, 04308355 (18:50:54Z).
- **End** (`.end_marker`, 19:23:21Z): the same checks, all green; no bytecode under `pt/base` or `pt/T6`; the audits at
  their prefixes. **Anomaly sweep:** no entry under `pt/` newer than `.start_marker` outside `pt/T6/`, `pt/G6/`,
  `pt/R6/`, `pt/I1/`–`pt/I4/`, `pt/D5/`, `pt/C5/`, `pt/audit/`, `pt/audit*-replay/`; the top-level listing is unchanged
  (36 entries, `pt/` mtime 18:50). Nothing quarantined; no `evidence/` directory was needed. The end marker was
  written once at 19:22:18Z (same results) and regenerated at 19:23:21Z after the NOTES stamp correction below.
- **Order of the last writes:** RESULT.md §0–§3 (19:21Z) → `.end_marker` → NOTES stamp correction → `.end_marker`
  regenerated → hashes (19:23:26Z) → RESULT.md §4–§5.
- **Writes.** Only inside `pt/T6/`. Authored files were written in parts of at most 250 lines per write call (TEST.md
  in three parts; t3 in three parts); edits were exact replacements. No temporary files.
- **Git and holds.** Git used only for `rev-parse HEAD` and `status --porcelain` with `GIT_OPTIONAL_LOCKS=0`. No branch,
  commit, push, PR, CI, network or URL fetch, publication, sub-agent, or edit to any manuscript, kernel file or record.
- **Deviations, disclosed.**
  1. One version check `python3 -c "import sympy; print(sympy.__version__)"` (19:08Z) ran without `-I -B`. It wrote
     nothing under `pt/` (no bytecode in `pt/base` or `pt/T6` at the end); whether it touched sympy's own cache in
     site-packages, outside `pt/`, was not checked.
  2. One inline `python3 -` stdin helper (standard library only, without `-I -B`) applied two exact replacements to
     `t3_countermodel.py` before its first run (19:11Z: the Z4 weights in header and code); recorded in the header.
  3. NOTES N2 and N3 first carried interval stamps with one estimated end each ("18:52Z", "19:03Z"); corrected in place
     at 19:22:56Z to the bounding `date -u` readings, the correction written into the two headers.
  4. The pre-run edit stamp "19:14Z" in `t4_rows.py`'s header is an estimate (no `date -u` was taken at that edit; the
     file's mtime is 19:13); the edit preceded the first run, and the stamp is a comment that affects no output.
  5. NOTES entries were appended in batches (19:06:54Z, 19:16:23Z, 19:21:10Z), each carrying the `date -u` readings
     taken during the work it records.
  6. Directory listings (names only) of `pt/I1/`–`pt/I4/`, `pt/D5/`, `pt/C5/` were made to locate records; no file of
     `pt/D5/` or `pt/C5/` was opened.
