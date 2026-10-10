# R6 RESULT — reassessment of the stage-4/5 countermodels against every applicable item at L (stage 6, step 3)

Thread R6, research only, read-only on the corpus. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`. Governing
texts `pt/PROTOCOL-STAGE6.md` (`b277b7c1…`) and `pt/PROTOCOL-STAGE6-AMENDMENT-1.md` (`59019538…`, A1.5 the assignment;
A1.2–A1.3, A1.7 binding), AUDIT-I §4–§5 binding. Deliverables in `pt/R6/`: `REASSESSMENT.md` (the tables and the
statements), `NOTES.md`, this file, six scripts with outputs, replays and kept runs.

## §0 — Answer

**Scope.** The alternatives of A1.5: the stage-3 cones K(E0) (level (i)) and K(Z_F) (level (ii)); the EXOTIC-E seeds
of stage 4 (Y4 `c = 4609/4608` at `φ0 = (1,2,3i,−1+i)`; Y5 `d_min = 5/256`, `c = 517/512`; Z `α = 7/8` at
`ψa = (15,−1,7,7)/18`) and of stage 5 (C5 census `d_low = 1/2304, 5/256, 1/8704`; the κ Bell seed on the invariant
circles; D5's monomial seed `c = 513/512` at `(1,2,3,4)/√30`); the torus node S2 and the finite-group nodes. They were
decided against the 199 applicable items fixed by `r1_inventory.py` from the frozen inventories: I3's 142 records with
bearing other than "none at L" (80 direct, 25 inherited single-token, 20 single-token not read by a pair statement,
17 through a named bridge; equal to I3's own lists), I4.236, I1.17, and the 44 + 11 do-not-assume records of I4 and
I2. The hidden-history level and the cone level are kept apart: no item at H, M, G or X reaches a cone in `W 3`,
because L has no H→P, M→P or G→P bridge; those items are NOT REACHED, never satisfied or failed.

**(i) Exclusion by L: none, for every alternative.** Per alternative: 118 SATISFIES, 13 FAILS (EXOTIC-E: 12 FAILS
and node T UNDECIDED), 68 NOT REACHED; the comparison object Q3 fails nothing. Every item at status *proved [K]* or a
definition at L is satisfied; every clause on `K` that L or the PT records carry is met (H1 by a symbolic
sum-of-squares identity over the whole ball, H2 at level (i) for K(E0) and level (ii) for K(Z_F), the H3
certificates, `CandidateCone`, `hadm`, `hcl`, `hgate`, `K ⊆ maxCone`, the slice conditions of `PreComposite`,
`Composite`, `JointReversible` for `cnot`, S2 Pair, INV2's cone transcription); the one kernel theorem that ties a pair
cone to a one-copy map, `no_candidateCone_cnot_reflY` (K2Guard.lean:143), holds for each (`actT reflY` moves K(E0) and
K(Z_F), pairings −1 and −1/8). The FAILS rows are all hypotheses: the do-not-assume items IE1, IE1Drive, Q3/pure-state
reachability, (b_S4), (b_n), (b_R1), (b_DJ), frame covariance and K2's clause "local actions compatible with the
composite cone"; the [D] four-token hypotheses `H` (KT4Core) and FCC for the uniform assignment (exact minima −1 and
−1/2 for the explicit cones); the PT-record candidates homogeneity H and extreme-ray transitivity T. Exact witnesses
for the explicit cones: K(E0) leaves itself under every listed one-token map, the NOT on either token included
(pairing −1); K(Z_F) is invariant under G16, SWAP, both NOTs and `rot3 π`, and leaves itself under `cyc3` (−1/2), the
quarter-turns about x and about (3,0,4)/5 (−1/2) and the order-3 rotation R1 (−2383/5316). For the EXOTIC-E
alternatives the failures follow from the audited theorem "(b_min) with H1–H3 forces Q3" and the exact seed
certificate `K ∋ e ∉ Q3`.

**(ii) Embedded-observer realization: nothing at L, either way.** No statement at L attaches an embedded-observer
realization, or an obstruction to one, to any cone in `W 3` (`r5_realization.py`: the only module whose imports reach
both a pair module and an H-level realization module is the root aggregator; the one module carrying both
vocabularies, CompositeInterface.lean:53, says "realizes a tensor product" in the algebraic sense; no manuscript,
roadmap or round-note line carries both). L provides at level H, not about `W 3`: Main.md:544–558 (finite operational
realization and gluing, ε-form, for a fixed quantum experiment; proved [M], no kernel anchor), Main.md:562 ("the same
reversible machinery can realize non-quantum finite instrument families"), Main.md:352 ("Bare finite OI therefore does
not select quantum mechanics"), and the kernel's H→M realizations of the sealed core (I1.41–I1.60) on the matrix
carrier, where composites are tensor products by construction. Missing bridge: an H→P or M→P theorem (the dictionary
`pauliW` is a design-module object; K2 OPEN, ROADMAP.md:1001–1006). Exposed assumption: the only H-level composition
clause at L, Main.md:552, takes the local instruments' action `I_a ⊗ I_b` as input — the composite action every
alternative lacks — so L's realization statements cannot be read as realizing an exotic pair with local
interventions. Realization: open; obstruction: none proved.

**(iii) Single-token premises: inherited from Q3's single-token structure by construction** (every alternative lives
on two copies of `eball 3 = ball3` with `nflip`, `z3`, `cnot`), and verified exactly where checkable: the DIM-1
`NativeGate` hypotheses (`relT`, `relC` on all 16 basis tables; frame; the positivity identity behind `posFwd`/`posInv`;
countercontrol `reflY`), `IsNot` (π-rotation about e1), `Entangling`, `HasTwoSharpTests`, K∞-Seed, K∞-Drive (`J_off_axis`
for `ball3Drive` and for the drive about x), K∞-Trans (instance), K∞-Copy (one NOT; exchange identity), K∞-Geom on the
token; K∞-Stage and K∞-Act are pair-blind and open for Q3 likewise. K∞-Geom's pair reading fails for Q3 and the
explicit cones alike (I4.236's scope), so it cannot discriminate.

**Evidence.** Exact scripts: `r1` 12/12 controls, `r2` 57/57, `r3` 30/30, `r4` 7/7, `r5` 4/4, `r6` 12/12, each with its
decision rule fixed in the header before its first run and its VERDICT printed over green controls; recomputed
independently of the stage-4/5 code: the X⊗X forms (1/9, 121/42), the orbit minima 5/256 (16, 48, 768, 384 rays), the
Z⊗Z bound 1/8704, the monomial bound 1/15, ψa's f-bound, `G_H`'s m = 4160/6561, the invariant circles, `G_S`'s orbit,
the FCC minima, the R1 witness. Replays 6/6 byte-identical. Kept runs: five failed runs (harness errors caught by the
scripts' own controls) and three header-only reruns. Integrity green at start and end; the sweep found nothing.

## §1 — Node by node (details in REASSESSMENT.md §1–§9 and NOTES.md N1–N9)

| node | content | result |
|---|---|---|
| R1 | applicable-item list from I1–I4 | 199 items; I3 classes reproduce `r0lists.out`; I4: one non-none bearing (I4.236), 44 do-not-assume; I2: 11 do-not-assume; I1.17 |
| R2 | explicit cones K(E0), K(Z_F) | H1–H3 certificates, maxCone bound, slice, I3.44 consistency, (b)-family witnesses, FCC −1 / −1/2, SF pair reading fails for Q3 too |
| R3 | ten EXOTIC-E seeds | each: one negative eigenvalue, excludes its own pure state, in its window, ≥ 0 on its group's reachable instances; minima recomputed |
| R4 | verdict tables | Tables A1, A2, A3 (+ A3-seeds); excluded by L: none |
| R5 | realization scan at L | no attachment, no obstruction; root aggregator only |
| R6 | single-token premises | 12 exact checks with countercontrols |

Gem classification (§A.31): CONFIRMING — the stage-3/4/5 certificates re-derived agree with the audited records
(including AUDIT-Y R7's R1 witness value and C5's corrected orbit counts 768/384); NEW (assumption-watch marker) — the
gluing theorem's composition clause presupposes `I_a ⊗ I_b`, the composite action the alternatives lack; POSITIVE —
the single-token premises are exactly pair-blind.

## §2 — Ledger of sources read

- Governing texts in full, in the prescribed order: PROTOCOL-STAGE6, its amendment 1, AUDIT-I, PROTOCOL-STAGE5 and its
  amendment 1, PROTOCOL-STAGE4, PROTOCOL-STAGE3, PROTOCOL, amendments 1–2; INTEGRATION-NOTE-STAGE5/4/3; AUDIT-Y, AUDIT-Z,
  AUDIT-D, AUDIT-C, AUDIT-X; `pt/Y/RESULT.md`, `pt/Z/RESULT.md`, `pt/D5/RESULT.md`, `pt/C5/RESULT.md`;
  `pt/base/AGENTS.md` lines 41–94, §A.21, §A.26, §A.31.
- Inventories: I3 RESULT and INVENTORY in full; I4 RESULT §0–§3, `records.txt` (parsed), I4.236; I1 RESULT §0–§1 and
  its INVENTORY (parsed; I1.41's heading); I2 RESULT §0 and its INVENTORY (parsed; I2.12, I2.18, I2.63 read);
  `pt/I3/r0lists.out` (parsed, as R1's control).
- Kernel at L (read-only): CompositeDimension.lean:97–205, :736–800; K2Guard.lean:40–140; CompositeInterface.lean:15–60;
  the whole `OIBridge/` tree, the root, 64 text files scanned by `r5`. Manuscripts at L: Main.md:352, :544, :552, :562,
  :628. Design modules [D]: FourCopyDefs.lean:25–49, FourCopyPackage.lean:172–189. Stage-3 record:
  `pt/X/x8_fcc_crossnote.out` and the matching lines of its script (the FCC witness arguments).
- Not read: `pt/G6/`, `pt/T6/` (absent), `pt/audit/stage3-inputs/OWNER-*`, `pt/audit/stage4-inputs/OWNER-*`,
  `pt/audit/stage5-inputs/`, `pt/audit/stage6-inputs/OWNER-*` (the directory `pt/audit/stage6-inputs/` was listed by
  name once; its OWNER file was not opened), `pt/audit/reviews/`, `pt/audit/aborted-launches/`, the `evidence/` copies
  in `pt/D5/` and `pt/C5/`.

## §3 — What is not claimed

- No verdict on (b), no outcome label of step 4, no status upgrade; a FAILS of a do-not-assume item, a [D] item or a
  PT-record candidate is the failure of a hypothesis.
- EXOTIC-E alternatives exist by EBF (non-constructive); not recomputed here and cited [A]: the Clifford census, the
  torus reductions to {φ0, CNOT φ0}, Z's reachable-set formula, EBF and SD1/SD2.
- Every check using `Q3` or PSD passes through the design-module dictionary `pauliW` (I4 marker 1). Instance checks
  (reachable states at rational points) are instance-scoped.
- "SATISFIES [inherit]" for an open single-token item means pair-blind and open for Q3 alike.
- `K({F, cnot F})` and `K(e_c)` are not reassessed (named in PROTOCOL-STAGE6 step 3, not in A1.5).
- No realization of any alternative is claimed, and no obstruction.

## §4 — Evidence log

Every script ran as `python3 -I -B <name>.py` from `pt/R6/`, stdout to `<name>.out`, stderr plus an appended `exit N`
line to `<name>.err`; decision rules in each header before its first run (amendments after a failed run recorded in
the header and NOTES); every final script replayed into `<name>.replay.{out,err}` and compared with `cmp`: 6/6
byte-identical on stdout and stderr. Every `.err` is the single line `exit 0` (`28d3b9e8…`), kept runs included (they
failed on their own controls, not by crashing).

| script | node | checks | verdict line | runs | replay |
|---|---|---|---|---|---|
| `r1_inventory.py` | R1 | 12/12 | `VERDICT R1-ITEMS-EXACT: 199 applicable items …` | 4 (runs 1–2 failed controls C2/C3, kept; run 3 = run 4 but for header times, kept) | identical |
| `r2_cones.py` | R2 | 57/57 | `VERDICT R2-CONES-EXACT: …` | 5 (runs 1–2 failed C1/C7/C9, kept; runs 3–4 = run 5 but for header times, kept) | identical |
| `r3_seeds.py` | R3 | 30/30 | `VERDICT R3-SEEDS-EXACT: …` | 2 (run 1 failed one per-seed check, kept) | identical |
| `r4_tables.py` | R4 | 7/7 | `VERDICT R4-TABLES-EXACT: 199 items … excluded by L: none …` | 1 | identical |
| `r5_realization.py` | R5 | 4/4 | `VERDICT R5-SCAN-EXACT: …` | 1 | identical |
| `r6_single.py` | R6 | 12/12 | `VERDICT R6-SINGLE-EXACT: …` | 1 | identical |

sha256 of every file in `pt/R6/` other than this one (the hash of RESULT.md is given in the final report):
```
5c7a1e9e2259386a90ff4b0b7d3be05335c9414d5616cf23b22ac811099ff4fa  .start_marker
593cdbd16c9bc9b181dbcec70d61961a58df18ae82926d3c0654ce794d7bc0d5  .end_marker
7dc400d228bb11a6cda4bfe6510ba6c871c10c22167639d66e6140b25af06acc  NOTES.md
1ff62ad633fbd752f247d49b605e6cc8d984e23d8b7151b6497cdd60fa884ffe  REASSESSMENT.md
7235178c5cb48fbce5046b13835dbc022c480c046714f4d10b2022e0302715c9  r1_inventory.py
e75682bac82c825e493765de885450da8d4f36c244625d92fa722d949601d0a8  r1_inventory.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r1_inventory.err
e75682bac82c825e493765de885450da8d4f36c244625d92fa722d949601d0a8  r1_inventory.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r1_inventory.replay.err
6b50bfe12b0c8a42121b86035fc4442facfdd6f1cf4d6390b27cf7d59f5c3df4  r1_inventory.run1.py
07e4b4b65d7449913ff496409e2b03e20fde62054442b6fba7f1797a59815a76  r1_inventory.run1.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r1_inventory.run1.err
4ecf38636c6a743f1e0da95cd5f44b34370af181d459c95d522e224a3fa6db15  r1_inventory.run2.py
154130cc42c6c838850cf05ba239d7b60829bc64cfba8af2dd742dc949c6a153  r1_inventory.run2.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r1_inventory.run2.err
2db5b0485b9991ea73a5f1a3dfa0920431facd53886f96864e9fc0cdff98e89e  r1_inventory.run3.py
e75682bac82c825e493765de885450da8d4f36c244625d92fa722d949601d0a8  r1_inventory.run3.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r1_inventory.run3.err
c3de61f7577e6e5338b60eeb408308695c394b6a28fd994d677a564cb10495fd  r2_cones.py
cf04091ba8af10b9fe326e1c45232acbee5f753ea8312723ed8cd4d90c521032  r2_cones.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r2_cones.err
cf04091ba8af10b9fe326e1c45232acbee5f753ea8312723ed8cd4d90c521032  r2_cones.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r2_cones.replay.err
948a7f901f869ed7a250fcb9af2f3f7fbc005347d7a653b6cd006c406bd20464  r2_cones.run1.py
b6f2478cb3fd8f943c35f97a09762fad35ca15e6c781ad20192b2769ee11c1fa  r2_cones.run1.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r2_cones.run1.err
afeecd7c5b901c21d45499aef35b7cba3c04f4625187a0a34764354c5820e71d  r2_cones.run2.py
d45ae26b2c858a34813d67a8d773fbd08b57347db9d8975b132f6589722b7f9d  r2_cones.run2.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r2_cones.run2.err
55d891d67bade2b87e9640e7e2ec817389215b33a74121e464e69a9d2c812c19  r2_cones.run3.py
cf04091ba8af10b9fe326e1c45232acbee5f753ea8312723ed8cd4d90c521032  r2_cones.run3.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r2_cones.run3.err
4e899938337ca622ae2b149cd244dbbb932f49c765b4cf78fea566b9abc0b027  r2_cones.run4.py
cf04091ba8af10b9fe326e1c45232acbee5f753ea8312723ed8cd4d90c521032  r2_cones.run4.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r2_cones.run4.err
8eab5ed48a4c25ed072efb654d6d08e22834f6995ed3a6b66d44975f0b7dd954  r3_seeds.py
6e657bf6cc347adba1ff8560fb4eb4f72b24d486347f5a59bdcb3942cdf8cba7  r3_seeds.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r3_seeds.err
6e657bf6cc347adba1ff8560fb4eb4f72b24d486347f5a59bdcb3942cdf8cba7  r3_seeds.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r3_seeds.replay.err
d4289e9f1a69c4174b0c1d15f544e4c5d54d1e1412cdd0b35bccd67a33b09f0e  r3_seeds.run1.py
f00d75b0da8b299c53eef2fd3174281137c2e82bea4f5137d2c741fb57238720  r3_seeds.run1.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r3_seeds.run1.err
06563bd9d69a38fee97bc12e35aa102342477990214af403dae755d0806cc2f4  r4_tables.py
08d38e1cab735d25245a1335bddb1a95305977f68ee5b542e4351efac0438219  r4_tables.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r4_tables.err
08d38e1cab735d25245a1335bddb1a95305977f68ee5b542e4351efac0438219  r4_tables.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r4_tables.replay.err
133df831ad54642e0f194bcb6cbbd52dd1ef6a60676e63afd69425aa59d7d080  r5_realization.py
8ba3e6083263b6bd01604390ce54047257e04ede2e3fdb484b19ec1edc30402f  r5_realization.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r5_realization.err
8ba3e6083263b6bd01604390ce54047257e04ede2e3fdb484b19ec1edc30402f  r5_realization.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r5_realization.replay.err
0c6e743b257d6c12762d73f022327bb3a03d159dab0cead88709360430572377  r6_single.py
f76e6a8537a39d6d4b15ff348842ba2d1369a12c8be783b17e130281b99ca579  r6_single.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r6_single.err
f76e6a8537a39d6d4b15ff348842ba2d1369a12c8be783b17e130281b99ca579  r6_single.replay.out
28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320  r6_single.replay.err
```

## §5 — Integrity

- **Start** (`.start_marker`, written first into the newly created `pt/R6/`, absent at 17:56:57Z; 17:57:30Z): the six
  manifests `inputs`, `stage1`, `inputs2`, `inputs3`, `stage2`, `inputs4` exit 0 (`sha256sum -c --quiet`);
  `audit/stage3-inputs/ns.manifest.sha256` OK from its own directory; base HEAD = L, `status --porcelain` empty
  (`GIT_OPTIONAL_LOCKS=0`), no `__pycache__`/`.pyc` under `pt/base`; the eleven protocol files match their prefixes
  (239dc123, b41aa0e7, 2a2f78f3, 38603692, 086a4cb8, 1a649168 from `pt/`; d3da2811, 9e01f098, 1f639115, b277b7c1,
  59019538 from SCRATCH) and every sidecar verifies; `ls -la` of `pt/` recorded.
- **End** (`.end_marker`, 18:34:13Z): the same checks, all green; no bytecode under `pt/base` or `pt/R6`. **Sweep:** no
  entry under `pt/` newer than `.start_marker` outside `G6/`, `R6/`, `T6/`, `I1/`–`I4/`, `D5/`, `C5/`, `audit/`,
  `audit*-replay/`; top-level names unchanged. No anomaly; nothing quarantined.
- **Writes.** Only inside `pt/R6/`. One transient file of my own, `pt/R6/.hashlist.tmp` (the 58 hash lines above,
  checked with `sha256sum -c` before use), removed after this section was written. Edits to my own files were exact
  string replacements printed with their match counts, or appends of at most 250 lines.
- **Git and holds.** Git used only for `rev-parse HEAD` and `status --porcelain` (`GIT_OPTIONAL_LOCKS=0`). No branch,
  commit, PR, CI, network, URL fetch, publication or sub-agent.
- **Deviations, disclosed.** Several times written into script headers and NOTES were first entered from an estimate
  rather than from `date -u`; each was corrected to the `date -u` value, which forced the header-only reruns listed in
  §4 (outputs byte-identical). One version check ran `python3 -I -B -c` (no file written).
