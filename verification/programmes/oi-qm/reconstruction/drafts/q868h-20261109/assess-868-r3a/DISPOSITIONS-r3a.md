# ASSESS-868 r3a: dispositions of REVIEW-868-r3

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Maps each nit of `review/REVIEW-868-r3.md`
(sha256 `2a5014a526399437754ecba4a8d8496ead456c33f10483c1b723acd170f0fd1d`, ACCEPT WITH NITS; hash taken before
reading, re-taken during the work and at the end, unchanged each time) to its change in `ASSESS-868.md` r3a, from r3 =
`r3/ASSESS-868.md` (`4cd2fb04da73060cb0e4ffac0287fd0a1f48ace60f9361fec5e57e3cf50f3228`, byte-identical copy of the
reviewed file). r3a = `ASSESS-868.md` (`d97c4b6b17bea9675d02a697e5164862471dad840dfbe9b54532baacd6788e1b`);
`diff -u r3/ASSESS-868.md ASSESS-868.md` has 6 hunks. Each nit was checked against its source at `fd539e15`
(`git rev-parse fd539e15` → `fd539e150759a6ea51ab279aeeac80fc06050ade`; reads by `git show fd539e15:<path>`; no
`--depth`, `gc` or `prune`; no git or GitHub write) or against the cited draft before it was applied. No nit was
refused. New exact check: `probes/r3a_check.py` (imports nothing from earlier work; no OI mechanism).

| Nit | Verified against (fd539e15 unless stated) | Disposition | Change in r3a |
|---|---|---|---|
| **n1** (§0 Q1) "Only with all six is `K = Q3`" reads as the converse | `EqvK2MaxCone.lean:153-161` `pairCone_eq_Q3_of_drive_maxCone` (six hypotheses ⇒ `K = Q3`); `:204-215` `pairCone_eq_Q3_of_sharp_available`; `:165-170` `driveInvariant_of_eq_Q3` (`K = Q3` ⇒ `hH2 ∧ hA` only); `:174-183` the iff holds only with `hH1`, `hadd`, `hsmul`, `hmax` fixed. No named witness derives `hH1`, closure or `hmax` from `K = Q3` | Applied | §0 Q1 *Validity is not quantumness*: "Only with all six is `K = Q3`." → "With all six, `K = Q3` (kernel)." |
| **n2** (§4.4, §11) "`gateFlow_isolation` … states the relation from the other side" imprecise | `LiftAudit.lean:582-587` (`signFun`: −1 only on the lower member of a moved orbit outside `{a, τ a}`; `phaseFun`: `e^{−iπt}` on moved, 1 on fixed), `:655-662` (`gateFlow_isolation`: `diag(phaseFun)·G(t)·(diag(sign)·G(t)·diag(sign)) = flow(transition a (τ a), πt)`), `:47` (`gateFlow = unit (permMat σ)`); `SecondOrderCircuit.lean:356` (`unit g t = 1 + (e^{iπt} − 1)·(1 − g)/2`); `ReachabilitySeam.lean:95` (`flow`); `LieRankSource.lean:199` (`transition`). r3a check: for τ = (01) on three states `signFun ≡ 1` (control: −1 at z = 2 for τ = (01)(23)), `G(t)² = G(2t)`, kernel left side = `e^{−iπtX_01}` = W10's right side at θ = πt; conjugate-phase control fails with an exact nonzero witness at t = 1/3 | Applied | §4.4: "the kernel's isolation identity `gateFlow_isolation`, LiftAudit.lean:660, states the relation from the other side" removed from the parenthesis; new sentence "W10's identity is the kernel's isolation identity `gateFlow_isolation` (LiftAudit.lean:660) specialised to one transposition on three states, where the sign conjugation is trivial and `G(t)² = G(2t)` (reviewer K3; `probes/r3a_check.py`)". §11 W10 entry: adds "(the kernel's `gateFlow_isolation` specialised to one transposition on three states: trivial sign conjugation and `G(t)² = G(2t)`; reviewer K3, r3a check)" |
| **n3** (§4.4; DISPOSITIONS owner-direction table) "added as an empirical controllability resource" attributed to the drive of phase-free richness | Main:590: the substratum supplies "as a stated intervention principle …, the phases — but … not the continuously tunable state-mixing operation; with that one operation added as an empirical controllability resource …" (substratum-source form). GR:260: "Adding that one operation as an empirical controllability resource completes the quantum architecture" (substratum-source form). GR:258: the phase-free-richness equivalence "is not a claim that bare observation incompleteness entails these principles" | Applied | §4.4 driven-transition item: the Main:590 quotation is reattributed to "the state-mixing operation added to the substratum class beside the stated phases" in the substratum-source form (Main:590; also GR:260); for phase-free richness, "the equivalence that consumes it 'is not a claim that bare observation incompleteness entails these principles' (GR:258)". Status "none derived from OI" unchanged. `DISPOSITIONS-r3.md` is the record of r3 and is left unchanged; this entry and the owner-direction row below supersede its attribution |
| **n4** (§8) sources listed as if premises | §4.4 (G7a: monomial Kraus operators keep states diagonal; R6d / r3 W6: operations keeping real states real keep ⟨Y⟩ = 0, under Main:564's interface) | Applied | §8 J3 item: "It follows from Main:564, Main:590, …" → "The necessity rests on G7 and R6d (r3 W6) under Main:564. The label compares it against the sources of a non-real operation, the scope of independence and their context: Main:590, GR:250–260, `obligations_independent` (O1 versus O2 only), `gateFlow_isolation`, BRIDGE r4 §5.1 and the bridge r4 review's R4-B1/R4-B2." Label CONFIRMING unchanged |
| **n5** (§2) "r4, `4e97610d…85e2`, the current working file" stale | `sha256sum`: `bridge/BRIDGE-UNIT1.md` = `78f1098ee4310b0a190e211add27094025f95d3d1fa7d9b0fd77eaf260cf91a4`, header "Revision r5", mtime 13:54:00Z (r3 saved 13:50:16Z); `bridge/r4/BRIDGE-UNIT1.md` = `4e97610df18a8f6a9e8a89486ea3633cc3609bcbd6a2c9686f3ad780af2885e2`. r4 l.455–461 = r5 l.466–472 and r4 l.541–544 = r5 l.574–577 byte-identical (encoded maps without FI-1; "No independence theorem between H-Bell and FI-1 or the phase is stated") | Applied | §2: "the current working file" → "the working file when read (kept at `bridge/r4/`; the working file is now r5, `78f1098e…91a4`, which carries unchanged the two r4 sentences used here, on encoded maps without FI-1 and on H-Bell's independence, at r5 l.469 and l.575)" |
| **n6** (optional; §4.4) the second drive + exchange in W8's `x+ ⊗ z+` preparation is the inverse quarter phase on wing A | Exact check `probes/r3a_check.py` (W8's convention: four states, index 2·first + second; the drive's closed form re-typed and checked against `U′ = −iX_abU`, `U(0) = 1`): `exch(|10⟩,|11⟩)·drive_{(|10⟩,|11⟩)}(π/2) = S† ⊗ I` exactly (S = diag(1, i), `phaseGate`, LieRankSource.lean:209), hence equal channels on a generic Hermitian 4×4 state; controls `S ⊗ I` and the drive alone give different channels (exact nonzero witnesses); first drive at π/4 takes `|10⟩` to `y+ ⊗ z+`, `S† y+ = x+`, full preparation gives `x+ ⊗ z+` | Applied (verified) | §4.4: after the W8 sentence, "in that preparation the second drive at π/2 followed by the exchange on the pair `|10⟩`, `|11⟩` is, as a channel, the inverse quarter phase on wing A, the first factor (`probes/r3a_check.py`; reviewer K4 on that pair)". The review's "wing A's pair" is written as the pair `|10⟩`, `|11⟩` (both with the first wing in state 1), since the transition flips the second factor while the phase lands on the first. §11: r3a probe bullet added (hash, 16 checks, what it checks) |

## Header (task instruction, not a review nit)

- Revision line r3 → r3a; "pending a fresh, independent review" replaced by "independently reviewed: ACCEPT WITH NITS
  (REVIEW-868-r3.md, `2a5014a5…0fd1d` in full); nits applied in r3a"; r3 archive path and hash added; dispositions
  pointer moved to this file. "WIP / UNVERIFIED" kept.

## Probe

- **`probes/r3a_check.py`** (new): sha256 `5121c0f48e7500ecb8b630ce74f081f539e93c8908fed4879d9bf5eeefc3f4b5`; output
  `probes/r3a_check.out` (`6e16d0eaa9be781c9b0042272744bf84d6a38ee20d3a761803955338fe84a01d`); `python3 -I`, sympy
  1.14.0, exit 0, 16 checks, 0 failures, recorded at its first run. Imports only sympy; re-types `unit`, `phaseFun`,
  `signFun`, `flow`/`transition` and `phaseGate` by hand; computes nothing on an OI mechanism.
- Mutation spot-check (not recorded in the probe; mutant deleted): replacing `S† ⊗ I` by `S ⊗ I` in the n6 identity,
  and setting `phaseFun` to `e^{−iπt}` on the fixed state, each makes the targeted checks fail (3 failures), so they
  are not vacuous.

## Not changed

- Everything outside the six hunks: no other line of `ASSESS-868.md` differs from r3. No probe, review or earlier
  dispositions file was edited.
- Left as found, for the coordinator: (a) the header bullet "What this unit did" (l.22) still says "three probes";
  r3a adds a fourth (`r3a_check.py`, recorded in §11). (b) The r3 probe's docstring
  (`probes/r3_scope_checks.py`, line 35) still says `gateFlow_isolation` is "read from the other side"; the probe
  is a hashed record cited by r3 and the review and was not edited. (c) §11's read lists do not add the r3a reads
  (`LiftAudit.lean:575-600`, GR:258/260 re-read, bridge r5 l.466–472 and l.574–577); they are listed in this file.
