# Audit of thread D5 (stage 5, Q-EX-BRIDGE, derivation side) — coordinator

Base L = `9f9f8257…` (read-only). Governing texts `PROTOCOL-STAGE5.md` (`9e01f098…`) and
`PROTOCOL-STAGE5-AMENDMENT-1.md` (`1f639115…`). Audit inputs: `pt/D5/` as frozen by the thread (its
RESULT.md hash `dba59d33…`, NOTES.md `e6add115…`), the pre-audit `pt/audit/stage5-inputs/preaudit_bridge.py`
(7/7, run 3), the stage-4 audits and integration note, and the kernel at L. Written 2026-10-10, 17:46Z.

## 1. Records and integrity

- **Hashes.** Every hash D5 quotes in RESULT §4 and in its final report verifies on disk (RESULT.md,
  `.start_marker` `6f0e5f4e…`, `.end_marker` `588bb840…`, NOTES.md, `d1_bridge.py` `dc1e885a…` / `.out`
  `c4c10930…`, `d2_levels.py` `5b4aeaca…` / `.out` `8464b5c8…`, `d3_weakest.py` `b21f37f8…` / `.out`
  `2d4360e6…`; all six `.err` files are the single line `exit 0`, `28d3b9e8…`). No `__pycache__`.
- **Replays.** D5's own replays: 3/3 byte-identical (stdout and stderr). Coordinator replays from `pt/D5/`
  into `pt/audit/D5/replay/`: 3/3 IDENTICAL (`REPLAY-LOG.txt`, 17:16:54Z–17:16:58Z).
- **No failed run** in D5; decision rules fixed in each script header before its first run (NOTES N2–N4);
  no rule changed after a run.
- **Start/end checks** (NOTES N0, N7): manifests 6/6, `ns.manifest` OK, base HEAD = L with empty porcelain,
  nine protocol prefixes and sidecars OK at both ends.
- **Deviations D5 disclosed** (all harmless, none touching a result): `.start_marker` assembled from two part
  files inside `pt/D5/`; a transient `pt/D5/.chk` and `pt/D5/d1_time.tmp`, removed; a malformed first sweep
  (`find` precedence) whose oversized listing the tool runner kept outside `pt/`; the correct sweep redone.

## 2. The anomaly D5 reported — attribution

D5's sweep (NOTES N6; `pt/D5/evidence/sweep1/`, 77 files + 4 directories, hashes only, content not opened)
found, newer than its start marker and outside the excluded directories: `pt/PROTOCOL-STAGE6.md`
(16:49:36Z), `pt/PROTOCOL-STAGE6.sha256` (16:49:55Z) and the directories `pt/I1/`–`pt/I4/` (start markers
16:51:44Z–16:53:28Z). **These are the coordinator's stage-6 launch**: the stage-6 protocol and the four
inventory threads, written and launched by the coordinator while D5 and C5 were running (recorded in
`pt/audit/STAGE3-RELAUNCH-LOG.md`, stage-6 launch entry, and in the owner note
`pt/audit/stage6-inputs/OWNER-NOTE8-FULL-CLOSURE.md`). They are not a second uncoordinated writer. D5's
response was correct under §A.26: sweep, quarantine by copy, no deletion, no further measurement; its
decisive runs (17:01:16Z–17:07:02Z) read only two Lean files under `pt/base/`, which the end checks show
unchanged; no anomalous file is an input to any D5 result.

**Coordinator's process breach, recorded.** The amendment-2 rule is that the coordinator writes only under
`pt/audit/` while threads run. Writing `pt/PROTOCOL-STAGE6.md` and launching I1–I4 into `pt/I*/` during
stage 5 broke that rule; it cost both stage-5 threads a sweep, a quarantine copy (77 + 159 files) and a
halt of substantive work after their results were complete. Lesson for the launch checklist: a new stage's
protocol and directories are created only after the running stage's threads have reported, or the running
stage's protocol names the directories in advance so the threads' sweeps exclude them.

## 3. Independent check (`indep_checkD.py`, run 2: 32/32 CONFIRMED, replay identical)

Written from D5's claims, not from its code; different representations throughout (Pauli-string commutators
in `u(4)` instead of 16×16 table maps; the monomial class's permutation group and phase torus enumerated;
the level identity checked on permutation matrices plus a symbolic affine step; defects built from the
stage-3 formula with states as eigenvectors). Run 1 (kept, `indep_checkD.run1.*`, 32/33) carried one line
testing a C5 census row that I mistranscribed; it is removed here and tested with the right transcription in
the C5 check. Results:

| D5 claim | check | verdict |
|---|---|---|
| Lean `sgn/pc/pt` = Ad(CNOT) control-first; `nflip` = R_x(π); `cycEquiv` = rotation of `U_J = (I − i(X+Y+Z))/2`, x→y→z→x; `actC R(U)` = Ad(U⊗I), row 0 fixed | A1, A1c, A2, A3, A4 | CONFIRMED |
| (b_DJ) Lie closure with cnot: dim 6 containing every `ad(σ_k⊗P±)`; drive alone 2; target drive 1 | B1, B1c, B2c | CONFIRMED |
| d3: drive + substratum phase flow on one token: 6 (either token); phase alone 1; both phases 3 | B5, B5c, B6c, B7 | CONFIRMED |
| monomial class: native permutations generate S4 on the basis labels; phase torus full mod global phase; φ₀ = (1,2,3,4)/√30 has min arrangement \|det\| = 1/15 (unreachable); `m = (15+√221)/30` exactly; c = 513/512 in (1, min(2, 1/m)] | C1–C5, C6 (FLOAT sanity, 4000 samples) | CONFIRMED |
| λ countercontrol: family-(i) value −1 for uniform K(E0) at the gate-supplied pair; Q3 control ≥ 0 on all 1296 pairs | D1, D2 | CONFIRMED (replication, same quantity) |
| `actC nflip E0 = E00 + E13 + E22`; a pure state of Q3 ∩ {E0}* pairs < 0 with it | E1, E2, E2c | CONFIRMED |
| K(Z_F): defect set = stage-3 set, D5's ψ(s) rays the same set; `U(w)` fixes every defect; `U(−1)` an involution moving a body state; `actC J` moves a defect out (overlaps 1/4, pairing −1/2); `actC nflip` permutes Z_F | F0–F3, F3c | CONFIRMED |
| level identity: `reindex e_n (1_n ⊗ permMat(levelPerm σ 1)) = permMat(levelPerm σ n)` (|S| = 2, 3, 4; n = 1..4; transposition and 3-cycle); affine step with symbolic `exp(iπt) − 1`; wrong reindexing fails | G1, G1c, G2 | CONFIRMED |

## 4. The kernel and record citations

Every file:line D5 cites was opened at L and says what D5 says it says: ReferenceExtension.lean:182, :447–451;
CompletedOI.lean:129, :131–133, :327, :418–420, :475–484, :506–513; ImplementationLocality.lean:207, :223,
:352–361, :370–371, :820, :943–960 (`[Nonempty A]` required, proof through `instAvail_withSpectator` and
`availExt_zero`); StructuralClosure.lean:180, :183–187, :261, :316, :359, :364–366, :370, :408–411;
PhysicalCharacterization.lean:164; SpectatorBridge.lean:188, :233; LiftAudit.lean:47–52, :112–113,
:183–196 (`hex 1 (1/2)` at :187), :200; SecondOrderCircuit.lean:352–357, :710–711;
ReferenceSufficiency.lean:754; KInfFoundations.lean:264, :284, :416–425, :449; CompositeDimension.lean:112–113,
:201–202, :224–225, :741–758, :793, :797–798; EmbeddedObservation.lean:123; OrbitGeneration.lean:79;
TransitiveBody.lean:301; DerivedQ3.lean:222–226; RouteB.lean:141–143, :149–151;
MicroscopicReversibility.lean:223–225; ExecSource.lean:129; ReadWriteControl.lean:174; GR.md:228, :256, :262;
Main.md:628; ROADMAP.md:68, :1004, :1010–1033 (K∞-Drive :1017); FourCopyDefs.lean:31, 34, 49;
FourCopyPackage.lean:176, 180, 183. The λ records: KT4-PREM-1 `result.md:17–22` (hypothesis list and
conclusion of `kt4_forward_ie1`) and `:186–192` ("kernel-checked in a design run, not certified");
EQ3-AUDIT §2 item 4 (no circularity: every step (s) or (2)) and §4 (relative to uniform pair cones,
KT(4) ⟺ IE₁, one witness per direction); EQ5-SOURCE-RESULT §1 (no three-token structure at L), §3.6
(FCC ⟺ ∃ KT4, one witness per direction), row 9 (`tok` [U] countermodel); PROTOCOL-STAGE2.md:77–78
(renaming test). All resolved as cited.

## 5. Assessment of the verdicts

- **N1 (sourcing map) and N1a/N1b.** Correct at L: the only spectator THEOREM is `ContextStable
  substratumClass` (monomial operators); every other spectator clause (`StructurallyClosed 𝓘` for an
  extension, `ContextStable` inside `DerivedOI`, the ∀-level clause of `LayerFlowExecutable`, OI⁺-1 itself)
  is a hypothesis. CONFIRMED by reading.
- **N1c (every level from level 1 under `HasParallelReferenceExtension`).** The written argument is sound
  as stated: `availExt_zero` at level 0; for n ≥ 1, `hP` with `R = Fin n` and `e_n (r,(s,0)) = (s,r)`,
  `withSpectator_conjChannel`, and the identity checked exactly (G1, G2). Consequence accepted: inside
  `DerivedOI` the ∀-level quantifier of `LayerFlowExecutable` is redundant given level 1, the spectator
  content being carried by `ContextStable` of the generating class (a class that, for any theory executing
  the flow at level 1, must realize it — the monomial class cannot, LiftAudit.lean:183–196). The pressure
  test D5 records is right: this relocates the spectator clause, it does not remove it. Type-3 gem
  (exposed assumption), recorded.
- **N1e (carrier exposure).** Every matrix-level spectator clause lives on `Matrix (A × Fin n)` with the
  PSD cone: the composite is the tensor product by construction, and conjugations are reference-positive
  for every spectator (ReferenceExtension.lean:182). Transcribed to the pair setting each becomes (b) for
  its class. CONFIRMED; it is corroborated independently by the stage-6 inventory threads I3 and I4, which
  find no theorem at L connecting the matrix carrier to `W 3` and no kernel definition of `pauliW`/`Q3`.
- **α, β, δ: CONDITIONAL** on the spectator clause (OI⁺-1; `ContextStable` of a class containing the
  flow and J; the ∀-level clause) plus L1 — CONFIRMED. Each fails the disguise test exactly where D5 says.
  β minus `ContextStable` is INDEPENDENT by Stab(K(Z_F)) — CONFIRMED by the stage-4 Z record (K(Z_F) is
  invariant under ⟨G16, SWAP⟩; my C5 check K1).
- **γ: INDEPENDENT for the substratum class** (exact seed c = 513/512 at φ₀ = (1,2,3,4)/√30, EXOTIC-E
  through the audited stage-4 dichotomy; Ĝ is the closure of the monomial group, compact and containing
  cnot) — CONFIRMED (C1–C6). CONDITIONAL for an extension — CONFIRMED.
- **ε: INDEPENDENT** (no-signalling is an identity of the carrier, true for every K) — CONFIRMED (A4 row-0
  identity; the stage-3 cones satisfy H1–H3).
- **ζ, drivability form: INDEPENDENT** (K(Z_F) carries a pair-level drive; fails (b_DJ)) — CONFIRMED (F1–F3;
  B3b). Transitivity forms: literal form not retained (Q3 fails it, TransitiveBody.lean:301), extreme-ray
  form UNRESOLVED — consistent with stage 4 (node T).
- **λ: "DERIVED(λ)" in the protocol's sense at [D + W + X].** The derivation chain is as D5 states: λ (with
  the pair premises) ⇒ IE₁ at every pair (`kt4_forward_ie1`, a design-run theorem, not certified) ⇒ (b_S4)
  ⇒ Q3. The disguise test passes as written (EQ3-AUDIT §2 item 4). Two qualifications the integration note
  must carry: (i) the kernel step is [D], so the verdict is DERIVED at [D + W + X], not at [K]; (ii) λ is
  not an existing OI premise — EQ5-SOURCE finds no three-token structure and no source for `tok` at L — so
  the derivation relocates the open bridge to λ's own sourcing rather than closing it from the certified
  base. D5 says both; the verdict table should say them in the cell, not only in the text.
- **"Below the OI⁺ layer no principle at L yields L2."** The argument (single-token principles quantify
  over one body and its operation data; every K with H1–H3 carries Q3's single-token structure; the
  stage-3 cones satisfy them and fail (b_DJ)) is a valid exact obstruction for the stated class [W + X],
  and C5's countermodels (η, θ, ι, ζ-1, the NOT-only forms on K(Z_F)) exhibit it candidate by candidate.
  CONFIRMED.
- **Weakest sufficient added content.** Field-neutral: (b) for two non-commuting one-parameter rotation
  groups on one token (drive + J-conjugate, or drive + phase flow about z), each family alone
  insufficient — CONFIRMED (B1, B1c, B2c, B5–B7) and matching C5's census for {flow, J}. Matrix: the
  drive's spectator stability given level 1 — CONFIRMED (G1, G2). Minimality not claimed — correct.

## 6. Wording items (no result changes)

1. In section F, D5 writes "J = Ad(X ⊗ I)". Elsewhere J = `cyc3`. The F3 witness is the control NOT's
   conjugate of the flow, not `cyc3`'s; the conclusion (an off-axis automorphism of the pair body exists)
   stands, and C5's ζ-1 reaches it with a different witness (a permutation unitary in the defect basis).
   Use a different letter.
2. The E-line prints `⟨φ|pW(E0)|φ⟩ = 1` and `−1` for an unnormalized φ (norm² 4); the normalized values
   are 1/4 and −1/4. Say "unnormalized".
3. The verdict table's λ cell should read "DERIVED at [D + W + X]; λ unsourced at L" rather than "DERIVED".
4. D5 cites CompositeDimension.lean:224–225 for `relT`/`relC` as structure fields; the kernel theorems for
   cnot are `cnot_relT` (:854) and `cnot_relC` (:860). Both are right; cite both.

## 7. Verdict

D5's results stand as stated, with the λ qualification above. Bands unchanged (consistency-axis work;
no certified label changes). Coordinator's process breach recorded in §2.

**Files (sha256).** `indep_checkD.py` `969652b0…`, `indep_checkD.out` `52bc08e2…`, `indep_checkD.err`
`28d3b9e8…` (replay identical); run 1 kept (`indep_checkD.run1.py` `d641498d…`, `.run1.out` `ce54c1da…`);
`replay/REPLAY-LOG.txt` and the three replay pairs.
