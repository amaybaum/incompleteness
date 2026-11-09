# ASSESS-868 r2: dispositions of REVIEW-868

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Maps each finding of
`review/REVIEW-868.md` (sha256 `c8da0967e83ca872214dc850d67970b84bab9aae7506bca81c36c8674e9fd763`, REVISE) to its
change in `ASSESS-868.md` r2, from r1 = `r1/ASSESS-868.md`
(`3499d405ca75c9b83bef58508cf1a413689fdff5d69b114f342f8c0d732013c3`). Every finding was checked against its source at
`fd539e15`, the cited draft or the Issue (REST read) before it was applied. The reviewer's `rv_868_checks.py` was re-run
with `python3 -I`: exit 0, byte-identical output. Independent r2 checks: `probes/r2_validity_scope.py`. No finding was
refused.

| Finding | Verified against | Disposition | Change in r2 |
|---|---|---|---|
| B1 (Lemma H's native form: body closure sufficient, not necessary) | QP `DESIGN.md:558` (C-EAR, "Encoded laws lie in the octahedron"); dual of Pauli sharp effects = cube (r2 V1); witness w3 (reviewer R3; r2 V2) | Accepted | §4.1 "Available-family form" and new "Native form" with w3; §0 Q1 second bullet; J5 row; §5 J5 item; §6 M3 row; §7 Q-868-H split into (V) validity on native tests and (C) closure, with (C) ⇒ (V), (V) ⇏ (C), and separate outcomes; §0 Q3 |
| B2 ("single-system property" overstates; decomposition not an equivalence) | Lemma H's quantifier over composite preparations; `hsharp` separate in `EqvK2MaxCone.lean:208-209` | Accepted | §0 Q1: r1's "not an independent composite principle", "Its content is a single-system property" and "Its OI status is the status of the single-token body" removed; §4.1 "Reading, one direction at a time" (availability separate; NS step one-directional prose); J5 row; §6 verdict; §9 Q2 (D-02) reworded as a sufficient route |
| B3 (Lemma H (⇒) is kernel `lor_toOp_of_maxCone`) | `CompositeDimension.lean:1049` ("A maximal-cone vector, read as an operator, carries the cone into itself"); DIM-1 `result.md:32, :101`; `preregistration.md:71-72, :147`; `lor_pair_bound` :877, `lor_of_forall_pair` :1015 | Accepted | §4.1 (⇒) layer K, (⇐) [A] from `lor_pair_bound`; §3 table row added; §0 Q1 first bullet; §5 Established; §8 relabelled (⇒) CONFIRMING, (⇐) ELABORATING, "not found stated" for both directions dropped; §11 read list |
| B4 (PR-box witness wrong for M20 ⇏ J9; SHARED §9 "omission" is not a column-(ii) route) | PR box S = 4 (r2 V4; reviewer R5a); law (1, 1, 1, 1/2) NS with max CHSH 5/2 and not quantum (reviewer R5b–c; r2 V4); `composition-source-map.md:166` ("conditional on the common representation, not a derivation of it from OI") | Accepted | J9 row: new witness and the non-quantumness argument; J11 row recast (J9's premise is quantum structure, column (iii); SHARED's "none identified" stands); §6 M20 row; §5 column-discipline sentence; §8 "J9 ⇒ M20 omitted from SHARED §9" finding removed |
| B5 (identity claims where support is containment) | SHARED r5 M17 row (`SHARED-MECHANISM.md:51`); QX-6 r5 R6.9, R6.11, R6.12 rows (`QX6-BELL-CHSH.md:227-230`) | Accepted | §6 table: M17 "shared part"; R6.11 "part of"; R6.9 ↔ J12 "containment, one direction"; M18 = J13 and R6.12 = J2 kept as identities (same clause, same anchor); verdict and §0 Q2 restated; J12 row |
| B6 (FI-1 "earliest"/"downstream" framing; J3 also needs the phase) | REVIEW-UNIT1-r2 RB1; BRIDGE r3 §0 item 8 and §5.1 *Position*; `obligations_independent` (C5Discovery.lean:59, as cited by BRIDGE r3 and the review); Main:590 ("as a stated intervention principle"); reviewer R6d; r2 V5 | Accepted | "earliest" and "downstream" removed throughout; FI-1 cited as a necessary condition, one direction only, for exact finite endomorphic operational QM on the configuration carrier, with the phase and H-Bell as independent gaps (§0 Q2, §6 first row); J3 row and §4.4 state both necessary inputs (non-monomial operation and phase); §2 BRIDGE status updated to r3 with r2's REVISE |
| N1 (planning-finding wording) | `gh api repos/amaybaum/incompleteness/issues/868` body: two rows read "#1173 draft/unmerged"; links `blob/e306143d…` and `pull/1173`; names only `research/oi-qm-composition-source-20261107`, which `git ls-remote` shows at `2de820fb` | Accepted | §2 planning-record bullet rewritten |
| N2 (run-1 disclosure incomplete) | `diff` of `g868_generic_checks.run1-misspecified.out` and `g868_generic_checks.out` (16 → 18 checks; G7a/b added; run-1 label "(probability −1/8)") | Accepted | §11 run-1 bullet |
| N3 (G3 control; cite kernel reproduction) | reviewer R2a–e, R2g | Accepted | §4.3 item 2: kernel `cnot` = quantum CNOT table on 16 Pauli inputs, `phiW`/`idW`/`chainW` entrywise, kernel control `nflip` gives 0; the writer's Z-conjugation control described |
| N4 (non-quantumness independent of completion; validity not) | reviewer R4a–d | Accepted | §4.3 item 1 split into "Not quantum, whatever the other cross terms" and "Full-ball validity depends on the completion"; §0 Q1 native-evidence bullet; §5 Conditional; §8 |
| N5 (C-CP link is standard; fifth premise) | `mechanism-1-20261107/DESIGN.md:199` ("determinant −1 … which is not CP") | Accepted | §4.3 item 2: fifth premise (sequential composability); literature (Peres 1996, Horodecki 1996; L) and MECH-1:199 cited; §8 label CONFIRMING; assumption-watch marker adds composability |
| N6 (`hA` is invariance, not availability) | `EqvK2MaxCone.lean:159-160`, `:212-213` | Accepted | §3 table `hA` wording; J8 row scoped to the availability route; §0 Q2; §6 FI-1 row |
| N7 ("not upstream of J13" needs scope) | reviewer R6a (G7 on the 4-state carrier) | Accepted | §4.4 last bullet of the first group; §6 FI-1 row: necessary for J13 only when the pair source is coherent |
| N8 ("in order" → partial order) | dependency of J1/J2/J9–J12 on J13; J3, J6, J7, J8 independent of it | Accepted | §10 Q1; §5 "Missing, with dependencies"; J13 row status |
| N9 (cite the "FI-1 not sufficient" witness) | G5; reviewer R6c; r2 V6 | Accepted | §0 Q2; §4.4 "Mixing does not give the composition rules"; §6 FI-1 row |
| N10 (A6.1 label; one-step case; hypotheses held) | Main §3.3 (one-step Bell ceiling, Main:366–416) | Accepted | §0 Q2 Bell bullet; J14 row (iii); §5 Conditional; §6 A6.1 row (adds (D)) |

## Owner-direction and cross-unit changes

| Source | Change in r2 |
|---|---|
| Owner direction 2026-11-09 (#868): keep product-test validity distinct from genuinely quantum joint-state behaviour | §0 Q1 new bullet "Validity is not quantumness"; §1 distinctions; §4.1 closing paragraph "Validity is not quantumness" (swap, node-10 table; r2 V3); §4.3 item 1 ("validity holds and the table is not a quantum state"); §7 "None of the outcomes makes the composite a quantum state"; §10 Q1 |
| Owner direction (all units): carriers; availability versus derivation; mixing versus full rules | §1 distinctions; node 10 named as an encoded carrier (§0, §4.3); J3 and §4.4 scoped to the configuration carrier, with the encoded-carrier stabilizer case; J7 row (the kernel `cnot` is a mathematically available map, its native availability not derived); §4.4 "Mixing does not give the composition rules"; §0 Q2 mixing bullet; §4.4 J2 bullet (J as mathematically available, not derived) |
| Cross-unit: FI-1 cited as a necessary condition for exact finite endomorphic operational QM on the configuration carrier; never earliest or only; drop "downstream" framing (#868 B6) | as B6 above |
| Cross-unit: correct hashes | BRIDGE r3 `a5d7aad1…78c1`, REVIEW-UNIT1-r2 `3cdf7dc2…4eb3` (§2) |

## Untraced changes (not from a review finding)

- **U1.** §4.4 bullet "On the encoded carrier, stabilizer-scope coherent preparations arise without FI-1 (BRIDGE r3 §5.1
  [D], citing QP)" — from the owner's carrier distinction and BRIDGE r3.
- **U2.** §8's r2 search extension records what the extended `git grep` (run here) found: the DIM-1 lemma; "herald" as
  bookkeeping; "self-dual" in unrelated cones; no statement of Lemma H's native form.
- **U3.** J13 status reworded from "earliest #868-specific input" to its dependency list (follows N8).
- **U4.** §1 layers: D now also covers model-reviewed derivations off `main` (A6.1), and X covers reviewer checks re-run
  here; §1 directionality adds that a non-implication carries a witness (follows B4).
- **U5.** Header and §11 updated for r2 (revision line, owner-direction note, new probe, re-runs, reads).

## Probe added

`probes/r2_validity_scope.py` (sha256 `60095dc01a21c62735f81f29ac85f11986a58ff535cc72f6112a3350fa5e0ea2`), output
`probes/r2_validity_scope.out` (`d86e03c1979355d7bee206e9e68e3712576ec035fe0683df2f8e0a48558ef020`), exit 0, 6 checks.
Run 1 (`probes/r2_validity_scope.run1-float.out`, `a101caf5b74c140db9175fd7a7711ebe53a821208618d9bd0977d1d7a36708f2`)
failed V4 only, because the check used Python integer division (floats) and sympy 1.14 compares Rational and float
strictly; the coefficients were made exact sympy integers. No expectation changed. Exact generic checks only; imports
no earlier probe; computes nothing on an OI mechanism. The reviewer-script re-run output is in `reassess/rerun-868/`.
