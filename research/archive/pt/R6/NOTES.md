# R6 — NOTES (stage 6, step 3: reassessment of the stage-4/5 countermodels; running record)

Thread R6. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`, read-only). Governing texts
`pt/PROTOCOL-STAGE6.md` (`b277b7c1…`) and `pt/PROTOCOL-STAGE6-AMENDMENT-1.md` (`59019538…`, A1.5 the assignment,
A1.2–A1.3 and A1.7 binding), with the protocols they name. Times are UTC from `date -u`.

## N0 — start (17:57:30Z)

- `pt/R6/` checked absent at 17:56:57Z, created, `.start_marker` written first (17:57:30Z): six manifests exit 0;
  `ns.manifest.sha256` OK; base HEAD = L, porcelain empty, no `__pycache__`/`.pyc` under `pt/base`; eleven protocol
  files match their prefixes and every sidecar verifies (six from `pt/`, five from SCRATCH); `ls -la` of `pt/` recorded.
- Read in the prescribed order (17:58Z–18:00Z): PROTOCOL-STAGE6, its amendment 1, AUDIT-I (§4, §5 binding),
  PROTOCOL-STAGE5 and its amendment 1, PROTOCOL-STAGE4, PROTOCOL-STAGE3, PROTOCOL, amendments 1–2; the integration notes
  of stages 5, 4, 3; AUDIT-Y, AUDIT-Z, AUDIT-D, AUDIT-C, AUDIT-X; the thread records Y, Z, D5, C5 (RESULT.md);
  `pt/base/AGENTS.md` lines 41–94, §A.21, §A.26, §A.31; I3 RESULT (full) and INVENTORY (to I3.39 so far); I4 RESULT
  §0–§3; I1 RESULT §0–§1; I2 RESULT §0. Not read: `pt/G6/`, `pt/T6/`, any `OWNER-*`, `pt/audit/stage5-inputs/`,
  `pt/audit/reviews/`, `pt/audit/aborted-launches/`, the `evidence/` copies in `pt/D5/`, `pt/C5/`.

## N1 — productivity test and decision vocabulary (fixed 18:01Z, before the first node)

**Productivity test (§A.31, fixed now).** A finding of this thread is a gem iff it is (1) an exact certificate at a
stated instance (an item checked SATISFIED or FAILED on an alternative by an exact script with green controls, where
the outcome is not a restatement of the stage-3/4/5 records), or (2) an exact obstruction (an item at L that excludes
an alternative, or a proof that no item at L can), or (3) an exposed hidden assumption (a level transfer, a
dictionary, or an identification the earlier records used without a bridge at L). Otherwise record-only. Fixed point:
3–4 passes with no NEW finding, or the assignment answered.

**Decision vocabulary (per item × alternative).**
- **SATISFIES** — the item applies to the alternative (at level P, or at level O through the single-token structure
  the pair inherits) and the alternative meets it. Sub-tags: `[K-indep]` the item is a proved kernel statement or a
  definition about objects the alternative shares with every pair cone on `W 3` (the carrier, `cnot`, `nflip`,
  `eball 3`, product data) and does not mention the pair cone `K`, so it holds for the alternative because it holds
  at L; `[cone]` the item's clause on `K` is checked on the alternative itself (exact script [X], or a written
  argument [W] over audited stage-3/4/5 certificates); `[inherit]` a single-token premise, met by the alternative's
  single-token structure exactly as by `Q3`'s (by construction, the same `eball 3`, `nflip`, `cnot`).
- **FAILS** — the alternative violates the item's clause on `K`. Every FAILS is pressure-tested: the item's status,
  its level, its bridge, and whether it is a do-not-assume item. A FAILS of a do-not-assume item, of an assumed
  hypothesis, or of a [D]/PT-record premise is recorded as the failure of a hypothesis, not of a theorem, and is
  never an exclusion by L.
- **NOT REACHED** — the item is at a level other than P/O (H, M, G, X) or is a pair statement routed through an
  absent bridge (I3's A1–A13; AUDIT-I §5 items 2–3), so at L it says nothing about a cone in `W 3`. Never recorded as
  SATISFIES or FAILS.
- **Excluded by L** — an item at status *proved [K]* (or a definition at L) that the alternative FAILS. Only such an
  item excludes; a FAILS of anything else does not.

**Evidence levels** (amendment 2): [K] certified at L (file:line); [D] design module; [W] written argument;
[X] exact computation in this directory (check id); [A] audited stage record cited (stage, check id). No [N].

**Realization question (ii), vocabulary.** For each alternative: what L provides at level H for a pair whose
operational cone is the alternative — "realization exhibited (file:line)", "obstruction proved (file:line)", or
"nothing at L (missing bridge named)". The answer is read from the inventories' bridge fields and checked by grep at L.

## N2 — the alternatives (as assigned, A1.5 and the launch message)

- A1 `K(E0) = (Q3 ∩ E0*) + R+E0`, `E0 = E00 + E13 − E22`, level (i) (stage 3, X `K1` / U `K★`).
- A2 `K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F`, `z_s = (E00 + s1 E13 + s2 E22 − s1 s2 E31)/4`, level (ii) (stage 3, X `K4`).
- A3 stage-4 EXOTIC-E seeds: A3a Y4 `c = 4609/4608` at `φ0 = (1,2,3i,−1+i)`, control flow about x (S3 and the
  drive); A3b Y5 `d_min = 5/256`, `c = 517/512` (S1, S2 reachable set, every listed finite extension); A3c Z
  `α = 7/8` at `ψ_a = (15,−1,7,7)/18` (S3), with its `G_H` (9/10) and `G_Cl` (99/100) variants.
- A4 stage-5 seeds: A4a C5 census `d_low = 1/2304` (`α = 499783/500000`), `5/256` (`α = 122509/125000`), `1/8704`
  (`ball3Drive` flow on the target); A4b the κ Bell seed `F = e_(−1,−1)` on the invariant circles; A4c D5's
  monomial-class seed `c = 513/512` at `(1,2,3,4)/√30`.
- A5 the torus and finite-group nodes of stage 4: S2 (`actC Rz ∘ actT Rx` with G16; Bell seeds on `C1 ∪ C2`), the
  stabilizer subgroups of `Stab_Cl(Z_F)` (explicit, `K(Z_F)`), `G_S`, `G_H`, `G_Cl`, every finite group (EXOTIC-E).
- Not assigned by A1.5 (named in PROTOCOL-STAGE6 step 3): `K({F, cnot F})`, `K(e_c)`; recorded as such, not decided.

## N3 — plan and the verdict rules (fixed 18:09Z by `date -u`, before any script runs)

Read by 18:09Z: I3 INVENTORY in full (I3.1–I3.187); I4 records.txt head and I4.236; I1.17's place; I2.12, I2.18, I2.63;
Main.md:352, :544, :552, :562, :628 at L; CompositeDimension.lean:97–205, :736–800 and K2Guard.lean:40–140 at L
(transcription of `hom`, `homMap`, `prodState`, `pairVal`, `maxCone`, `actT`, `actC`, `sgn`, `pc`, `pt`, `cnot`, `z3`,
`nflip`, `reflY`, `idW`, `chainW`); `pt/inputs/fourcopy/FourCopyDefs.lean:25–49` and `FourCopyPackage.lean:172–189` [D]
(`tabMul`, `tabT`, `ipW`, `dualW`, `transposeW`, `pauli1`, `pauliW`, `Q3`, `twin`).

Nodes (depth-first, decisive first): R1 the applicable-item list (parser with count controls); R2 the explicit cones
(exact certificates, every cone-level item, witnesses for the do-not-assume failures, `no_candidateCone_cnot_reflY`
consistency, FCC uniform); R3 the EXOTIC-E seeds (seed certificates, recomputed minima where cheap); R4 the verdict
tables generated from R1 and the R2/R3 outputs; R5 the realization question (grep at L); R6 the single-token premises.

**Item classes and verdict rules (R4 applies them mechanically; a check id names the evidence).**
1. `def-P` — a definition at level P (carrier, maps, data): SATISFIES [K-indep] (the alternative lives on `W 3`).
2. `thm-indep` — a proved [K] statement at P or O whose statement does not quantify over the pair cone: SATISFIES
   [K-indep]; where it is a property of the shared gate/NOT (`relT`, `relC`, frame, involution, `IsNot`, `Entangling`),
   also re-checked exactly (R2 D-checks).
3. `gate-hyp` — an assumed hypothesis-structure on the gate/NOT (NativeGate, GateRel, CtrlGate, NativeGateOf,
   Entangling, EntanglingOf, IsNot): SATISFIES [K] by the certified instance for (`eball 3`, `z3`, `nflip`, `cnot`),
   which every alternative shares; K-independent.
4. `cone` — a clause on `K` itself (H1, H2, H3, `CandidateCone`, `PairAdm`, `hcl`, `hgate`, `maxCone` bound,
   `PreComposite`/`Composite`/`JointReversible` of the slice under `cnot`, S2 Pair, INV2's cone transcription, LT of
   the coordinate model): SATISFIES or FAILS by the R2/R3 check named; [X] for explicit cones, [W] over audited [A]
   records and exact seed checks for EXOTIC-E.
5. `kthm-K` — a proved [K] theorem quantifying over `K` (`no_candidateCone_cnot_reflY`): SATISFIES [K] (its conclusion
   holds for the alternative; R2 checks the predicted non-invariance on explicit cones). If an alternative met all
   hypotheses and violated the conclusion it would be EXCLUDED BY L.
6. `dna-P` — a do-not-assume item at P ((b) forms, IE1, IE1Drive, FC, `Q3`-reachability, K2's local-actions clause,
   idle-extended `JointReversible`, P-ACT2's idle-extension reading, the IE1-using classification step): FAILS where an
   exact witness or the audited stage-4 theorem (every (b_min) form with H1–H3 forces `Q3`) applies; recorded as the
   failure of a hypothesis. Never an exclusion.
7. `4tok` — four-token items ([D] or PT-record): FCC/`H` for the uniform assignment FAIL as [D]-level hypotheses where
   checked; items whose content is not a function of the pair cone (token clauses, `KT4Cone`, SDC, N0–N2, IE2) are
   NOT REACHED (no structure with three or more tokens at L); [D] theorems (`kt4_forward_ie1`, Lemma B1) SATISFIES
   vacuously [D] (hypothesis `H` fails); `EvenCycle` SATISFIES for `cnot` with identity locals.
8. `O-inherit` — single-token items (bearing "inherits", "not read", or "through B1/B2"): SATISFIES [inherit]: the
   alternative's tokens are `eball 3 = ball3` with `nflip`, `z3`, `cnot`, the same as `Q3`'s; [K] instance cited where
   L has one on the ball; "open for Q3 likewise" where L has none. Through B1/B2 the item reaches only the upper bound
   `maxCone (eball 3)`, which every alternative respects (cone rule, `maxCone` bound).
9. `HMG` — items at H, M, G or X (I1.17; the 44 do-not-assume items of I4; the 11 of I2): NOT REACHED (no H→P, M→P,
   G→P bridge at L; AUDIT-I §2, §5 items 2–3).
10. `PT-cand` — PT-record candidates H, T: H FAILS (exotic cones are not homogeneous: [W + L] stage 3) recorded as a
   hypothesis failure; T FAILS for the explicit cones (invariant c = 15 vs 9, [A] stage 4 Y6) and is undecided for
   EXOTIC-E (NOT DECIDED is not a verdict of this vocabulary: recorded as FAILS-NOT-SHOWN → listed as "not decided"
   in a note, verdict column "—"). This is the one place the three-word vocabulary does not close; stated so.
Controls of R4: every applicable item gets one verdict per alternative; the `Q3` comparison column is SATISFIES on
every item of classes 1–8 (or NOT REACHED for class 7's not-reached items); any FAILS outside classes 6, 7, 10 is
printed as EXCLUDED-BY-L and stops the verdict line.

## N4 — node R1, the applicable-item list (18:10Z–18:11Z)

`r1_inventory.py`: run 1 (18:10Z) failed its own controls C2 and C3 and is kept (`r1_inventory.run1.*`): my prefix
rule put I3.96 and I3.99 under "single-token, not read" where I3's own `r0lists.out` puts them under "through bridge"
(their bearing reads "constrains the single-token structure; at the pair level only through P-STAGE2/P-ACT2"), and
`records.txt` writes I4's bearing as `none` and the flag as `DNA ;; …`. Rule amended in the header (an "only through"
clause is class bridge unless the text begins with the inherits phrase; I4 field values as written). Run 2 (kept,
`.run2.*`) placed the new test after the "not read" test, so it never fired; run 3 fixed the order (no rule or control
change); run 4 differs from run 3 only in two header timestamps I had written from an estimate instead of `date -u`
(corrected; outputs byte-identical, `cmp`). Result (run 4, controls C1–C6 green): **199 applicable items** — I3's 142
(80 direct, 25 inherits, 20 not read, 17 through a bridge; the class sets equal I3's own lists), I4.236, I1.17, the 44
do-not-assume records of I4 and the 11 of I2. Process lesson recorded: every time written into a file is taken from
`date -u` at the moment of writing.

## N5 — node R2, the explicit cones (18:13Z–18:17:47Z)

`r2_cones.py`, final run 5 (code identical to run 3, outputs byte-identical): 57/57 checks, VERDICT R2-CONES-EXACT.
Run 1 (kept) failed three of its own checks, each a harness error: the C1 identity assumed an orthogonal bilinear
part (E0's has rank 2: the residual form `I − MᵀM` is PSD and was added), the C7/C8 witness pool missed the joint
eigenvector inside a degenerate eigenspace (the eigenvectors of the moved table were added, and slides
`ψ' − (k/8)c_tψ_t` for the defects), and C9's pool for E, F lacked the defects. Run 2 (kept) still gave min 0 for
K(Z_F)'s FCC: Y was confined to Z; stage-3 thread X's `x8_fcc_crossnote.out` (read at 18:16Z) puts the violation at
Y = cnot prodState(e2, e2), so run 3 takes Y, E, F over the 72 tables and Z (integer arithmetic, scale 4). Runs 4–5
corrected header timestamps only. Findings:
- Both cones: H1 (symbolic SOS over the whole ball), H2 (level (i); level (ii) and SWAP for K(Z_F)), the H3
  certificates (one negative eigenvalue −a, the rest ≥ a, pairwise orthogonal), K ≠ Q3, the `maxCone` bound, the
  slice conditions — all exact. Countercontrols fail as required (e_{3/2}; the non-orthogonal pair, −1; the twin's
  H2 failure through `chainW`, −1/2; E00 has no defect).
- `no_candidateCone_cnot_reflY` [K] is consistent with both cones: `actT reflY` moves K(E0) (pairing −1) and K(Z_F)
  (−1/8); Q3 likewise (`actT reflY phiW = idW` is not PSD). The only kernel theorem at L that asks a pair cone to be
  invariant under a one-copy map other than the gate is satisfied by the exotic cones in the only way it allows.
- One-token maps (the (b) family): K(E0) leaves itself under every listed map, the NOT on either token included
  (pairing −1), so it fails even the NOT-only form; K(Z_F) is invariant under `rot3 π`, both NOTs (in G16), and
  leaves itself under `cyc3` on either token (−1/2), the quarter-turn about x (a member of the drive's flow, −1/2),
  the quarter-turn about (3,0,4)/5 (−1/2) and R1 (−2383/5316, the value AUDIT-Y's R7 found with its own witness).
- FCC (famI) for the uniform assignment fails: min −1 (K(E0)), −1/2 (K(Z_F)), as recorded at stage 3; Q3 control
  min 0 over 3·72³ values.
- K∞-Geom's singleton faces fail on the pair slice of Q3, K(E0) and K(Z_F) alike (the effect of `|0⟩⟨0|⊗I`): the
  pair transfer of the geometric premise does not discriminate (consistent with I4.236; record).

## N6 — nodes R3 (seeds), R5 (realization scan), R6 (single-token premises) (18:19Z–18:26Z)

**R3, `r3_seeds.py`** (run 2 final, 30/30, VERDICT R3-SEEDS-EXACT). Run 1 (18:21:03Z, kept) failed one check: it used
the S3 group's reachable sample for every seed, against its own rule ("listed per seed"); the Bell seed F (κ, S2) is
not bounded on the X⊗X torus, which is not in its group. Run 2 lists the instances per seed group (no rule change).
Recomputed exactly, independent of the stage-4/5 code: the X⊗X torus forms (det Q/tr Q = 1/9, 121/42 ⇒ d_low =
1/2304, c = 4609/4608, C5's α = 499783/500000 admissible); the φ0-orbit minima 5/256 under G16 (16 rays), ⟨G16,
SWAP⟩ (48), and the level-(ii) J and NOT+J groups (768 rays control, 384 target: C5's corrected counts); the Z⊗Z bound
1/8704 (sharp: fails at 1/8600); D5's monomial bound 1/15 (countercontrol (1,2,2,4): 0); ψ_a's V-coefficients and
f = 1/2 + 5√137/162 ≤ 7/8; G_H's m = 4160/6561 (32 rays); the κ/S2 circles invariant under U(w), CNOT, Z⊗I, I⊗Z,
conj and the S2 torus (symbolic), maximally entangled, F = z_(−1,−1); G_S's orbit of 8 with overlaps {0, 1/2}. Each
of the ten seeds: one negative eigenvalue, excludes its own pure state (so K ≠ Q3), inside its window, pairs ≥ 0
with its group's listed reachable instances. Cited, not recomputed: the full Clifford census (Y5, Z z4: 6272/6561),
the torus reductions to {φ0, CNOT φ0} (Y4, C5), Z's reachable-set formula, EBF.

**R5, `r5_realization.py`** (run 1, VERDICT R5-SCAN-EXACT). Over 214 kernel modules + root and 64 text files
(papers, book chapters, ROADMAP, README, the K-programme round notes): (a) the only module whose import closure reaches both a pair module
and an H-level realization module is the root aggregator (as AUDIT-I §2); (b) one module carries both kinds of token:
`CompositeInterface.lean:53` — read: "The coordinate model of §E is a function space on index pairs and realizes a
tensor product" — "realizes" in the algebraic sense; not an embedded-observer realization; (c) no manuscript, roadmap
or round-note line carries both kinds. So no statement at L attaches an embedded-observer realization (or an
obstruction to one) to a pair-cone object. What L does provide at level H (read at L, 18:06Z): Main.md:544–558 (finite
operational realization and gluing, ε-form, for a fixed quantum experiment; clause (4) takes `I_a ⊗ I_b` as input),
Main.md:562 ("an operational realization theorem, not a uniqueness theorem: the same reversible machinery can realize
non-quantum finite instrument families"), Main.md:352 ("Bare finite OI therefore does not select quantum mechanics";
each completion condition fails on a qubit theory realizing the same C1–C4 process); the kernel H→M realizations I1.41–
I1.60 (matrix carrier, composites tensor products by construction). None is stated for a cone in `W 3`.

**R6, `r6_single.py`** (run 1, 12/12, VERDICT R6-SINGLE-EXACT): HasTwoSharpTests and SharpSeed witnesses on the ball
(countercontrol: e with 1 − e fails the separation clause); nflip is the π-rotation about e1 (det 1), and
`ball3Drive`'s NOT `rot3 π` fixes z3 (the two NOTs differ: I3 fact 3); `J_off_axis` for `ball3Drive` (flow about z) and
for the stage-4/5 drive about x (J = cyc3), countercontrol J = id; CopyNatural under identity and exchange; a rational
boundary transport; the singleton-face identity on the ball.

## N7 — node R4, the verdict tables; pressure test of every FAILS (18:27Z–18:30Z)

`r4_tables.py` (run 1, 18:29:08Z, 7/7 controls, VERDICT R4-TABLES-EXACT): 199 items × {K(E0), K(Z_F), EXOTIC-E} + Q3.
Tally per alternative: 118 SATISFIES, 13 FAILS (EXOTIC-E: 12 FAILS + T UNDECIDED), 68 NOT REACHED (the 56 H/M/G
items and 12 items needing a ≥3-token structure or an absent bridge); Q3: 131 SATISFIES, 68 NOT REACHED, no FAILS.
EXCLUDED-BY-L: none.

**Pressure test of the 13 FAILS rows** (status, level, bridge, flag; PROTOCOL-STAGE6 step 3):
- I3.137 IE1, I3.142 IE1Drive, I3.144 Q3/pure-state reachability, I3.150–I3.153 the (b) forms, I3.155 FC: do-not-assume
  (stage-6 list); statuses [D] or PT-record open/flagged; level P; no bridge needed (P). Failure of a hypothesis.
- I3.165 K2: an OPEN obligation (ROADMAP.md:1001); the clause that fails is "local actions compatible with the composite
  cone", flagged do-not-assume; its other clauses (LT encoded, a composite cone) are met. Not a theorem.
- I3.133 `H` (KT4Core), I3.135 FCC: [D] design-module hypotheses ("not at L"), four tokens, for the uniform
  assignment; the failure is exact for the explicit cones (−1, −1/2) and follows for the EXOTIC-E cones from the [D]
  theorems with stage 4. Not certified, not at L: not an exclusion.
- I3.160 homogeneity H, I3.161 T: PT-record candidates of stage 4 (H "absent at L for the pair", Y O; T "EXCLUDES-KNOWN";
  OI⁺'s reversible richness, the do-not-assume counterpart, is matrix-level). Not items the corpus asserts.
Result: no FAILS row is a theorem or definition at L; (i) holds as "no item at L excludes" for every alternative.
Skepticism applied to the favourable branch (an exclusion would favour the framework's QM target): the one
kernel theorem at L that quantifies over pair cones with a one-copy map (`no_candidateCone_cnot_reflY`) was checked to
be met (C7), and the B1/B2 bridges reach only the upper bound `maxCone`, which every alternative respects (C5).

**Gem classification (§A.31).** (1) CONFIRMING: every stage-3/4/5 certificate re-derived here (H1–H3, the seeds, the
minima, FCC values, the R1 witness −2383/5316) agrees with the audited records. (2) NEW, exposed assumption (type 3,
assumption-watch marker): the only H-level composition statement at L, the gluing theorem's clause (4) (Main.md:552),
takes the local instruments' action on the joint register, `I_a ⊗ I_b`, as input; for a pair cone that fails (b) this
input does not exist beyond product effects (r2 C8: K(E0) is not preserved even by the NOT), so L's realization
machinery cannot be read as realizing an exotic pair with local interventions; Main.md:562's "non-quantum finite
instrument families" is not stated for cones in `W 3`. (3) POSITIVE: the single-token premises are pair-blind exactly:
the alternatives meet every one of them as Q3 does (r6, r2 D-checks), and K∞-Geom's pair reading fails for Q3 itself
(r2 C10), so it cannot discriminate. Pass 2 over the classes (gate, cone, inherit, bridge) found no further item; pass 3
over the HMG items found none with a bridge; fixed point reached with the assignment answered.

## N8 — replays, REASSESSMENT, closing (18:30Z–18:34Z)

- Replays (18:30:16Z–18:31:06Z): all six final scripts re-run into `<name>.replay.{out,err}`; `cmp`: 6/6 byte-identical
  on stdout and stderr. Every `.err` (finals, replays, kept runs) is the single line `exit 0`; no bytecode under `pt/R6`.
- Kept runs: failed on their own controls — `r1_inventory.run1.*`, `.run2.*`, `r2_cones.run1.*`, `.run2.*`,
  `r3_seeds.run1.*`; successful, superseded only by header-timestamp corrections (outputs byte-identical to the final
  runs) — `r1_inventory.run3.*`, `r2_cones.run3.*`, `.run4.*`.
- `REASSESSMENT.md` written 18:31Z–18:33Z: §0–§2 by one write (70 lines), the four generated tables appended from
  `r4_tables.out` lines 3–631 in four appends (204, 204, 204, 17 lines), §4–§9 in one append (130 lines); three
  sentences then narrowed to their evidence (hcl is [A], not exact; the EXOTIC-E FAILS rows named by their separate
  grounds; K∞-Geom on the ball cited to ROADMAP.md:1045–1047 instead of `kinf2_kernel_core`).
- Register check of REASSESSMENT.md and NOTES.md (grep for revision-history and reader-instruction phrases): no hit.

## N9 — end (18:34Z)

`.end_marker` written 18:34:13Z: six manifests exit 0; `ns.manifest.sha256` OK; base HEAD = L, porcelain empty, no
bytecode under `pt/base` or `pt/R6`; the eleven protocol prefixes and sidecars OK; `ls -la` of `pt/` recorded; sweep
(`find` with `-newer R6/.start_marker`, excluding `G6/`, `R6/`, `T6/`, `I1/`–`I4/`, `D5/`, `C5/`, `audit/`,
`audit*-replay/`): no entry — no anomaly, nothing quarantined, no `evidence/` directory. Top-level names unchanged
since the start (`T6/` not present). This NOTES file is final; RESULT.md is written next and lists the sha256 of every
other file in `pt/R6/` (58 files).
