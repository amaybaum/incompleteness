# rev910b: separate-engine review of native_decode_v14 (#910, local 36213be6/7f843073/cd9390a0)

**Overall: BLOCK. The computation is accepted; the text needs edits.** The preregistered computation reproduces exactly from the native dynamics. No recomputation is needed. Findings 1–3 are false or overstated statements on status surfaces; fixing them is a text-only change. Per question: **Q1 derived, narrower than worded. Q2 insufficiently supported** (no permitted read). **Q3 insufficiently supported.**

## What I regenerated and what I only read
- **Regenerated with my own engine** (`native_table.py`, which imports no author or review code). Field values are stored as A/B/D bit-planes. The upper cluster is computed by backward dependency closure plus a forward time sweep (383,207 nodes, 3,608 requests). The lower first front is a (y,z) dynamic programme. Upper and lower cones are checked to be disjoint on all 3,608 R-1/R-2 cells, and E enters only (0,-11,10) at R-1. The 11-tick diamond is run with all six neighbours and the old-local term. The table regenerates in 12 s.
  - Digest **b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc**. This equals the retained v13 hex, and the E=000 rows equal Native B's 512-row table.
  - q9 at L is independent of E and N.
  - Exact minimal lower-front period: **1152**, which divides 384·840³ and P. The Lucas forcing formula is checked up to j=600.
- **Inherited, not re-derived:**
  - the upper source positions and payloads (Q/C/G/J/K±/N) and the four pure-B selector sources;
  - the 12·840²⁰ upper-strip period proof (I checked only that it divides P);
  - the torus/no-wrap envelope and the bank/ready-region geometry.
- **Conventions confirmed:**
  - rows are x,u,mY,mR,a,b,E,N; code = 4A+2B+D;
  - s = x⊕u⊕a;
  - the 24 contexts are those with (a,b)≠(0,1);
  - v = 8E+N, with fields EA..ND as bits 5..0;
  - a field coefficient has bit j for feature (1,u,mY,mR,a,b)[j];
  - bit c of a readout D is its value on code c.
- **Read, not regenerated:** the post-hoc fresh-bit pad pairs (512; 0/4 hidden contexts) and the 16/680/6768 raw-code multiplicities.

## Values my engine computed
These come from a cube-splitting solver plus literal brute force, written independently of solvers A and B.
- **Readouts:** 78 of 254 have a solution, 7464 solutions in total; by ANF degree, 8 / 29 / 41.
- **Per-readout counts:** all 254 equal the author's `readout_solution_counts`. Every solution was checked directly on all 48 rows.
- **q10.A = s: 1456 laws.** The law [1,5,1,4,1,5] (E=(1,1⊕mY,1), N=(mY,1,1⊕mY)) is present. It is one of exactly two laws that use mY alone; the other is [1,5,5,4,5,1].
- **Degree one:** A 1456, ¬A 912, A⊕B 384, ¬ 424, A⊕D 24, ¬ 16, B⊕D 8, ¬ 4. B, ¬B, D, ¬D, A⊕B⊕D and ¬(A⊕B⊕D) have 0.
- **E terms:** E≡000 0; E constant 40; N constant 0. With E forced to 000, every readout gives 0.
- **Controls, all matching the author where comparable:**
  - planted full-rank law: 1489, law recovered (under both my coefficient convention and the author's);
  - brute force (1,u): 0 / diagnostic 2560; (1,u,a): 0 / 143360; (1,mY,mR): 4 / 45568; (1,a,b): 0 / 150528;
  - author's planted (1,u,a) table: 818 over 64 readouts, diagnostic 149568, reproduced exactly;
  - raw pairs: 32 common pairs, 16 affine E maps, 0 joint laws;
  - the constant witness E=001, N=000 separates s on all 24 contexts, using 6 distinct pairs.

## The owner's three questions
**Q1, nontriviality: derived, but narrower than worded.**
- s is not available before the dynamics act. At every context the solution laws give identical sources for s=0 and s=1.
- Controls:
  - constant sources: 0 laws for any readout;
  - sign-erased table: 0 for every readout and for the diagnostic, which is the same as erasing x at fixed k;
  - E,N affine in s alone: 0 laws;
  - E,N affine in (seeds, s): 25,160 q10.A laws out of 2⁴², against 1456 without s. The s-free class is a much narrower contract.
- q10.A depends on x in 768 of the 1536 (k,E,N) cells.
- **However, s is not singled out.** For every one of the 64 affine seed functions f, some law makes q10.A = x⊕f(k); counts range from 512 to 2016.
  - With f=0, q10.A = **x itself under 992 laws**, for example [1,4,1,4,0,16]: E=(1,mY,1), N=(mY,0,a), checked directly.
  - So the table shows the unknown input x carried into q10.A, with an offset in the seeds that the source law selects. s is the case f=u⊕a. Nothing here distinguishes "reconstructs the earlier sign" from "exposes x relabelled by the source law".
- The sign-erased control is zero by construction for any solver that keeps the two signs apart. It is a sanity check, not a decisive countercontrol.

**Q2, accessibility: insufficiently supported. No permitted read exists.**
- q10 first carries s at **L+1**. At L-1 and L my engine finds 0 rows depending on E or N, and 0 solutions over all 254 readouts. At L+1 the counts are 3584 rows and 7464 solutions.
- No rule on the branch permits reading q10 at any tick:
  - CURRENT-HANDOFF.md:6-7 says no access rule is adopted.
  - INTERFACE-CONTRACT.md:93-96 requires each proposal to list its public access; v13 and v14 list none.
  - native_seed_v12/review/REPORT.md:105-106 says no new q10 public-prefix or flag law.
- The Native A contract permits a single whole-V (q9) read at L+2 (CURRENT-HANDOFF.md:30-32). The L+2 inverse also uses q9's previous neighbours, q10 at L+1 among them; that inverse is "a coordinate map, not an available observer read" (INTERFACE-CONTRACT.md:63-72).
- Under Native A, q10 at L+1 is the private Q10 pool cell. v13 replaces F10 by a pin and does not inherit that pool (EQUIVALENCE-OBLIGATIONS.md:57-58).
- The readout touches no register other than q10. But the result needs a new q10 access rule, plus v13's unadopted affine known-seed preparation contract.

**Q3, reusability: insufficiently supported.**
- The checkpoint models no read interaction, no post-read evolution and no carrier or public-record law. Nothing about outgoing-carrier preservation follows.
- Across the 1456 q10.A laws:
  - D depends on s on 4–16 contexts in every law;
  - (B,D) depends on s on 12–24 contexts, and reveals s on all 24 contexts in 24 laws;
  - **B is sign-free on every context in 8 laws.** Example [1,3,3,2,5,1]: E=(1,1⊕u,1⊕u), N=(u,1⊕mY,1).
- So reading A leaves an s-correlated residual given the seeds; this is a leak or disturbance hazard that was not tested.
- No surface claims a reusable interface or a quantum instrument; REPORT:122-126, PLAN:52-54 and HANDOFF:102-104 disclaim them.

## Findings (file:line — issue — safe fix)
1. **REPORT.md:25 and CURRENT-HANDOFF.md:94: "All eight degree-one readouts succeed" is false.** There are 14 nonconstant degree-one readouts and 8 succeed. A⊕B⊕D and its complement fail, and REPORT:29-30 does not list them. checks.py `affine_readouts` lists only readouts that have solutions. Fix: "8 of the 14 degree-one readouts succeed", and list all six failures.
2. **CURRENT-HANDOFF.md:100-101 "the B and D fields depend on s in every q10.A law", and CHECKPOINT-CHECKS.json `native_decode_v14_scope` "B/D fields carry s in every q10.A law", overstate the result.** They are false for B: there are 8 counterexample laws. REPORT:61-62 is correct, because it reads the pair jointly. Fix: "(B,D) jointly, and D alone, depend on s on some context in every q10.A law; B alone is sign-free in 8 laws".
3. **The title and REPORT.md:32-34 ("carries s … into the outward port q10"), EQUIVALENCE-OBLIGATIONS.md:59-61 ("A fixed redundant readout succeeds") and HANDOFF:98-99 frame the result as delivery of the old sign through a port.**
   - The winning readout is a single field, not a redundant one.
   - Every target x⊕f(k) is equally decodable.
   - q10 has no access rule.
   - Fix: say "q10.A = x⊕f(k) for every affine seed function f under some law (s is f=u⊕a); q10 is a cell, not a permitted read". Add "review pending" at EQUIVALENCE:59.
4. **REPORT.md:52 "The second front is required", and the post-hoc E≡000 item placed inside result.json `verdict.second_front_required`.** Fix: restrict the wording to "no affine law with E≡000". Keep post-hoc items outside the verdict object in future groups. The result.json is not to be rewritten.
5. **EQUIVALENCE-OBLIGATIONS.md:4 ("Each has … a separate-agent internal review") and :33-34 (the plans are listed at 9e92ff42 only) are stale.** The v14 group is unreviewed, and its plan is at 36213be6. Fix: correct both lines forward.
6. **PLAN/REPORT control 5:** state that the sign-erased zero is guaranteed by construction. Add the constant-source and x⊕f relabelling countercontrols if a v14 revision is made.

## Replay, integrity, mutation, voice
- **Author group replay:** the normal run and the `-O` run (68 s each) are both byte-identical to result.json, which is unchanged since 7f843073.
- **Manifests:** the top-level SHA256SUMS passes on 349 of 349 files; the v14 SHA256SUMS passes on 5 of 5.
- **PLAN.md** is unchanged after 36213be6, and its sha256 equals the provenance pin ac1f55b9….
- **`94a4e6cc..cd9390a0`** changes, outside native_decode_v14/, only CHECKPOINT-CHECKS.json, CURRENT-HANDOFF.md, EQUIVALENCE-OBLIGATIONS.md, README.md, SHA256SUMS and replay.py. No earlier reviewed result file changed.
- **`replay.py --latest`:** run on a fresh export, it passes all five groups normally and with `-O`, plus the manifest (194 s).
- **Mutants of the author's checker, all caught:**
  - contexts (1,0) excluded instead of (0,1): caught by control 4;
  - kernel reads x=s⊕a: caught by control 2;
  - solver B misses the current basis value: caught by control 2;
  - table bits corrupted after the pin check: caught by control 4;
  - readout ignores the s=0 condition: caught by control 3.
- **Post-hoc labelling:** REPORT:48-50 and PROVENANCE `post_plan_additions` are correct, apart from finding 4.
- **Voice:** no caps emphasis, revision-history phrasing or reader-instruction phrasing in the added lines. These files are verification records, so §A.32/§A.33 are applied as a style check.

Files, all in rev910b/: `native_table.py`, `review_checks.py`, `q2_ticks.py`, `q_extra.py`, `q_plant2.py`, `make_mutants.py`, `out/`. The checker's normal and `-O` outputs are identical, sha256 f2164968….
