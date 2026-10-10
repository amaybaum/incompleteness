# Coordinator's audit of EQ4-SIX (research only)

Thread result: `scratchpad/eq5/SIX/RESULT.md`. Running notes: `NOTES.md`. Protocol: `scratchpad/eq5/PROTOCOL.md`,
section "EQ4-SIX".

## Verdict

The result stands as an **open** result for c = 0 and for c = 1. No proof and no exact countermodel is claimed, and
none is needed to support what is stated.

The evidence:
- The seven exact scripts replay with byte-identical stdout.
- An independent exact audit (own code, 6/6) confirms:
  - the crossing enumeration behind G1;
  - the PN₅ control value −1/64 and its two controls;
  - the memberships of the control's nodes;
  - the theta identity behind (A3);
  - a QM sign control.
- Integrity is clean. The quarantine matches its manifest. The three untracked FourCopy files the thread found are
  the coordinator's own writes, reproduced exactly (§4).

Seven wording items overstate the evidence or need a definition (§3). None changes an exact result.

## 1. Replays

The exact scripts were copied to `eqreview/replaySIX/`. All copied hashes match RESULT §7, as does the copied
`eq4_lib.py` (`cc2c6aca94007ac8`, identical to `eq4/P/eq4_lib.py`). Each was run with the recorded argument
`<base>/verification/lean-mathlib/OIBridge`.

| script | script sha | stdout sha (replay = record) | verdict |
|---|---|---|---|
| `s1_system.py` | `0f633bcb085487e6` | `876d75300459f7ad` | 11/11 `S1-SYSTEM-EXACT` |
| `s2_zcone.py` | `6b12c98ad49e4d29` | `490535e24164594d` | 5/5 `S2-ZCONE-EXACT` |
| `s3_glue_theta.py` | `b08735aaf4516e1d` | `d99d776027c1dd1d` | 5/5 `S3-GLUE-THETA-EXACT` |
| `s4_glue_sector.py` | `8bc18a6314193fb9` | `5176852574064658` | 5/5 `S4-GLUE-SECTOR-EXACT` |
| `s5_xi_sector.py` (run 2) | `c3dbd14fd5cccd3c` | `b446936d9a05b031` | 7/7 `S5-XI-SECTOR-EXACT` |
| `s6_s10_slice.py` | `97ad348af7e89ac7` | `5c79a1a433ed65fc` | 4/4 `S6-S10-SLICE-EXACT` |
| `s7_s10_slice_c1.py` | `c32387af6fe78bf8` | `ac22915ab41d1689` | 3/3 `S7-S10-SLICE-C1-EXACT` |

- **Stdout:** byte-identical for all seven (`cmp`).
- **Stderr:** both runs hold only an exit marker, `exit 0` in the thread's files and `exit=0` in mine. That is a
  difference of harness format, not of output, and no script wrote to stderr.
- **The failed s5 run 1** is kept as recorded: `s5_xi_sector.run1.py` `82943f4a85283078`, `.run1.out`
  `6cc13475043cf5ca`, ending `6/7 … VERDICT NOT RENDERED`. Not replayed, as the thread recorded.

## 2. Independent exact audit

`eqreview/six-audit/audit_six.py`:
- Script sha `64019b1ebe7b0884`; output sha `80678d6e13fe94de`.
- Result: 6/6, `SIX-AUDIT-CHECKS-PASS`, on the first run. The replay is identical. `.err` holds only `exit=0`.
- The decision rule is in the header and was fixed before the first run.
- Independence: the script reads nothing from `eq5/SIX/`, including `eq4_lib.py`. It uses its own exact tensor
  calculus on labelled qubits, with numpy object arrays of `Fraction`s.
- `eq4_lib.py` was read, not imported, for one fact only: its `w3` is the GHZ witness ½·1 − |GHZ⟩⟨GHZ|.

| id | what was checked | result |
|---|---|---|
| C0 | machinery: cond(1, X) is the partial trace; a Bell link gives ½ tr(X Yᵀ); without the transpose the value differs (countercontrol) | pass |
| X1 | crossing enumeration on six tokens: 90 / 360 / 390 ordered pairs of distinct bipartitions with all four intersections nonempty at \|S\| = 4 / 5 / 6, none at \|S\| ≤ 3; classes (2\|4, 2\|4) 120, (2\|4, 3\|3) 90, (3\|3, 2\|4) 90, (3\|3, 3\|3) 90; no part of size 1 or 5 | pass |
| X2 | PN₅ control with the glue network of s3's header: (GHZ, W3) = **−1/64**; (W3, W3) = **1/16**; QM (GHZ, GHZ) = **1/32** | pass |
| X3 | memberships of the X2 nodes: x and y are products across P \| R1R2, so biseparable; GHZ is rank one with trace 1; GHZ's one-token marginal is ½·1 at all three cuts, so W3 ≥ 0 on biseparable states, hence W3 ∈ BS*; ⟨GHZ\|W3\|GHZ⟩ = −½, so W3 is not PSD | pass |
| X4 | theta identity: with product effect nodes ½·1 ⊗ Φ⁺ and Bell links, N = (1/4)(1/8) tr(x T(y′)), T the full transpose, on 3 random rational pairs; without T it differs | pass |
| X5 | QM sign control: N ≥ 0 on 4 random rank-one PSD quadruples | pass |

X4 is checked on real pairs. Both sides are complex-bilinear, so this covers the complex case. That reduction is
written, not computed.

## 3. Wording and scope

1. **G1 "Exact"** (§0, Gems).
   - The crossing enumeration is exact, and is confirmed independently (X1).
   - The reduction P6 ⟺ (A1) ∧ (A2) ∧ (A4) is a written case list with exact ingredients [X s1 B–G, s3 + W]. Its "⇐"
     direction rests on that case list.
   - Correct label: [X enumeration + W case list].
2. **"Reduction (proved, both directions witnessed)"** (§2).
   - Each direction has its own witness, as §A.34 requires: "⇒" from EQ4-P (audited) and from the glue construction;
     "⇐" from the case list.
   - But the status is a written argument with exact ingredients, not kernel-checked. Replace "proved" with
     "written, both directions witnessed".
3. **"Two further searches (y19, and y26 with structured starts) confirm the separating dual element Y ∈
   Lift(K_A)*"** (§0).
   - Both searches are float. "Confirm" should be "agree with", and the sentence should carry [F].
   - §1 already says, correctly, that Y "survives three independent searches".
4. **"Lift(K_A)* also contains the boundary point X_t of C_A (y29), with ⟨X_t, Y⟩ = −0.223"** (§0). This is stated
   as a fact, but it rests on the float search y29.
   - Only X_t ∈ BS* is exact (s5 A).
   - Needs [F], as §3 ML-SIX-lift already has it.
5. **"(A4) is the genuinely six-token constraint"** (§0).
   - The content is an independence statement: (A4) is not implied by the constraints up to five tokens, because PN₅
     satisfies those and violates (A4) at −1/64. Confirmed exactly here (X2, X3).
   - State it that way.
6. **Define W3 at first use.**
   - In this thread and in `eq4_lib`, W3 is the GHZ-fidelity witness ½·1 − |GHZ⟩⟨GHZ|, an element of BS* that is not
     PSD (X3). It is not the W-state projector.
   - RESULT uses it without a definition (§0, §1 N5, §7), next to separate "W witness" explorations (y12, y14, y15).
   - Without the definition, the PN₅ control reads as a QM violation.
7. **G2's demonstration is float.**
   - The y23 quadruple's −2.2e-3 is a float evaluation at identity filters. The hidden assumption it exposes is a
     method assumption, so float evidence is adequate for a record-only methodological finding, which is how §0 uses
     it.
   - If its nodes are rational, an exact evaluation of that value would be cheap. It is recommended before G2 is cited
     outside this thread.

The P/A/C ledger (§2) is otherwise correct:
- P ⇒ C is not proved.
- No exact model of P ∧ ¬C is constructed.
- PN₅, K_A and K_tw are models of weaker premise sets only.
- A_hom is recorded as unused, conditional on [L] and on an unverified step, with necessity disclaimed.
- No result uses purification, transitivity, Choi-state availability, IE₂ or an (o)-type step.

## 4. Integrity

- **Quarantine** (`eqreview/quarantine-SIX-stray/`): both files match the manifest.
  - `.Z3.err` `ddc51debb9d097f0`, 121 bytes. `.Z3.out` `e3b0c44298fc1c14`, empty. Both have mtime
    10:10:19 UTC.
  - The `.err` content is the interpreter's "can't open file …/y13_sector_gap_float.py" line and "exit 2".
  - Neither file is in the working tree, and `git status --porcelain` is empty.
  - The thread's own account (RESULT §6) agrees: a `cd SIX && A & B &` harness error. The files are not data.
- **The three untracked FourCopy files** (RESULT §6, found 11:00 UTC) are the coordinator's EQ4-F drafts, reproduced
  exactly from the coordinator's own write history:
  - `FourCopyLocal.lean`, `a9e9434d10b3c5e8`, 13629 bytes: the coordinator's Write at 10:58:51 UTC, byte for byte.
    Applying the coordinator's next edit (11:04:03) gives `12c1cd6cc79a651b`, the hash EQ5-PREM recorded later.
  - `FourCopyCore.lean` `9fce26e66fdec1e9` and `FourCopyBridge.lean` `febb3d1fc9658275`: the same hashes EQ5-PREM
    recorded. They are reconstructed exactly in `EQ5-PREM-AUDIT.md` §4.
  - The thread's attribution to "the concurrent EQ4-F thread" is correct. Its handling (sweep, files left in place,
    no measurement after) follows §A.26.
- **Head movement:** the move the thread recorded, from `f0d37906` to `1310e629`, is the coordinator's design-run-1
  commit (11:42:46 UTC).
- **Manifests:** the base manifest and the inputs manifest verify silently, with exit 0, checked from their roots.

## 5. Not checked by this audit

- **Replayed only:** s2 (Z^GD has 28 extreme rays), s4 (the exhaustive 92⁴ and 36⁴ sector minima of (A4)) and s5–s7
  (the Ξ and S10 slices). They replay byte for byte but were not re-derived independently.
- **Written only:** the "⇐" case list of N1, beyond the exact identities it cites.
- **Not re-run:** the float explorations y1–y29. They certify nothing, and RESULT lists them as such.
- **Literature:** row N6 is [L, unverified] and was not checked.

Consistency-axis work only; bands unchanged.
