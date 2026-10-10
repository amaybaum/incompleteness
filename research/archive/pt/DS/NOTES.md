# DS — running notes (thread DS, research-only)

Governing: PROTOCOL-STAGE2-DS.md (086a4cb8…) over PROTOCOL-STAGE2.md, PROTOCOL.md, amendments 1–2.
Input under review: inputs3/DS-INPUT.md (ffb6eb75…), treated as verbatim data.
Base L = 9f9f8257 at pt/base/ (read-only). Not read: pt/S2/, pt/S3/, pt/audit/S2/, pt/audit/S3/, pt/audit*-replay/.

## Log

- 08:49Z start checks all pass; `.start_marker` written first into a freshly created DS/ (see marker).
- Noted at start: DS-LAUNCH-LOG.md (coordinator, 08:48:46Z) and auditS3-replay/ (coordinator, excluded, not opened)
  appeared between my first listing and the checks; both predate the marker. Recorded in the marker.
- Reading order done: PROTOCOL-STAGE2-DS, PROTOCOL-STAGE2, PROTOCOL, amendments 1–2, DS-INPUT, INTEGRATION-REVIEW,
  base/AGENTS.md (824 lines at L; note it differs in length from the working-copy AGENTS.md shown in the session
  context, which is not L — I use pt/base/AGENTS.md only).

## Productivity test (fixed before the investigation, PROTOCOL.md §Investigation mode)

A finding is a gem iff it is (1) an exact certificate at a stated instance (a derivation with every step checked, or
an exact countermodel), (2) an exact obstruction for a stated class of routes, or (3) an exposed hidden assumption.
Otherwise record-only.

## Node log (depth-first; each node closed by a check)

N1 (DS.2a, Main L660–664). Read at L. L660 heading "### 4.1 Interpretive Consequences"; L662 "photons, electrons,
slits, detectors — are all visible-sector objects"; L664 single-slit assertion, "boundary conditions of the transition
matrix", detector "couples the trajectory to additional visible-sector degrees of freedom", and "What remains open is
the common coherent operational extension of that dictionary to all interventions and composites". Verdict at node:
input paraphrase partly unfaithful (hidden sector vs L662; "complete dynamics" vs boundary conditions with φ fixed).
Other corpus double-slit sites found by grep (book: none): Substratum.md:412, Explainer.md:564–568,
Methodology.md:401 (cites "Main §3.4" for the treatment, which is at §4.1 — corpus pointer error, record-only),
Structure.md:1312 (three-path interference bound, empirical anchor).

N2 (DS.2b, AncillaInterference.lean). Read in full (406 lines). Theorems and hypotheses listed for RESULT §1.
Build route at L: root import OIBridge.lean:114 `import OIBridge.AncillaInterference`; lakefile.toml defaultTargets
["OIBridge"]; CI verify.yml job "Mathlib bridge" runs `lake --rehash build` (L118–127) then the release gate
(L149–150) whose step `lean-axioms` reads `#print axioms` (tools/release_gate.py:137–138); 0 files with `sorry` in
OIBridge/; census lean-manuscript-census.json:213 family "instruments, dilation and assembly", status
"verification-only", manuscript []. => [K] for its theorems (route stated; no local rebuild: no Lean toolchain here).
Gem candidate (3, hidden assumption): its interference premise (balanced mixer 1⊗hMat) moves the all-ones ray, so by
[K] instAvail_unitary_fixes_ones (InstrumentRealization.lean:398) + permClass_onesFixing (PhaseSource.lean:79) the
theory the stated access generates (permTheory = genTheory permClass, PhaseSource.lean:104–106) cannot make it
available. To be checked exactly in ds7_structure (S6).

N3 (DS.2c, ROADMAP L1442–1447). Quoted at L. Classification there: "publication-facing validation target rather than a
dependency gap", under "Deliberately not prioritized" (L1422). Same file L1392–1414: "The source of phases |
INDEPENDENT", "Dense/nonclassical operational control ... INDEPENDENT", fixed nonclassical gate an "independent
empirical datum relative to the present architecture". Phase-source audit read in full (headline L266–273).

N4 (DS.3). Main L526–534 theorem + kernel names; Equivalence.lean:459–465 `finite_horizon_equivalence` (∀P, three
iffs; hypotheses: Fintype V, DecidableEq V, K:ℕ), S_imp_D :419, D_imp_Qfb :294 (permutation unitary, diagonal init),
QfbReal.law :207–214 = projective fixed-basis measurement WITH COLLAPSE AT EVERY STEP. Root import OIBridge.lean:58;
census family "current", anchors in Main. Scope limits already stated: Main L20, L534, L622, L750; Equivalence.lean
L18–23; ROADMAP L36–49; phase-source audit P6 (L77, L261). Observation: the representation the theorem constructs
(D_imp_Qfb) has no coherence at all (permutation unitary, diagonal prior); to be illustrated exactly in ds7_models.

N5 (corpus facts for DS.4/DS.7/DS.8). Main L20/L282/L534 Born exponent not selected (frontier). Main L562 gluing
theorem "can realize non-quantum finite instrument families". Main L564–568 OI⁺ ⟺ exact finite endomorphic QM
(carrier_general_oiPlus, OIBridge.lean:139) and L568 "finite reversible read-write dynamics, even with genuine
hidden-memory and readback behavior, does not itself generate quantum state mixing"; phases "a stated intervention
principle rather than a consequence" (readWriteSourced_not_qm ReadWriteControl.lean:174, root :146). ROADMAP K row L68,
K2 L1001–1006 (two-copy d=3 composite; Kₙ L1058–1069 for arbitrary carriers), H-Bell L953–966, stochastic observer
interface L918–931 (ensemble_underdetermined StochasticInterface.lean:118). P0 OPEN (L63; Main L622).

N6 (landed pair objects for DS.7(c)). CompositeDimension.lean: W :97 (docstring L95–96 "Local tomography is the
premise this carrier encodes"), hom :100, prodState :161, pairVal :164, prodEffVal :182, maxCone :186, actT :198,
actC :201, sgn/pc/pt :741–755, cnotFun :758, cnot :775, z3 :793, cnot_prodState_mem_maxCone :1152, xplus :1213,
phiW :1220, cnot_prodState_xplus_z3 :1222, phiW_not_product :1232, phiW_mem_jointStates :1246. Landed probe
kt4_prem1_probe.py:119 R_H, :560–562 T_psi = actT R_H phiW (exact probe, not kernel). Stage-1: INTEGRATION-REVIEW
L119 "L defines no pair system at all"; K_gen = SEP + cnot SEP (A, DERIVED for constructed systems).

Decision (labels). The input's target names generic premises ("one observer embedded in a deterministic system").
Countermodels to those premises are reported as "route refuted" (amendment 2), not INDEPENDENT; the framework-
specific target is UNRESOLVED because L defines no double-slit arrangement, detector, (Obs, μ) or OI-native pair
system in the physical substratum. Fixed before writing the scripts.

## Scripts — pre-run edits and runs

- ds5_physics.py written with its decision rules in the header. Two pre-run edits before the first run, neither
  touching a rule: (1) the `cplx` helper rewritten to the plain `re + I*im` form (the first draft computed the same
  value through a dead conditional); (2) `sp.nsimplify` removed around exact values in F2-unitary (unnecessary on
  exact inputs; removed so that no approximation routine is ever on a decisive path).
- ds5_physics run 1 (kept: ds5_physics.run1.{py,out,err}): 26/27 PASS; CC-F7 FAIL. Cause: harness error of mine.
  The frozen rule compares the e_+ CONDITIONAL pattern with the unconditioned record pattern at x=0; the code used the
  joint P(0,+) = 1/4, which equals the fringe-free value 1/4 because P(+) = 1/2. Fix (only this): divide by
  P(+) = sum_x P(x,+). No rule changed; no other line changed. The claim under test (conditioned fringes) was never in
  question: F7-plus/minus/sum/record all passed in run 1.
- ds7_structure.py written with its decision rules in the header. One pre-run edit before the first run: the three
  S0 matrix comparisons switched from sp.expand(Matrix) to Matrix.applyfunc(sp.expand) (explicit elementwise
  expansion). No rule changed.
- ds7_models.py written with its decision rules in the header. Pre-run edits before the first run: `frac` now uses
  simplify and raises unless the result is an exact Rational, and `bound_ok` compares against the exactly expanded
  bound; both previously called sp.nsimplify. No rule changed.
- ds5_physics run 2: 27/27 PASS, 7/7 blocks; replay byte-identical (out 2de948fb…, err 19eaf438…).
- ds7_structure run 1: 24/24 PASS, 7/7 blocks; replay byte-identical (out 9c582278…).
- ds7_models run 1: 19/19 PASS, 10/10 blocks; replay byte-identical (out 3005de67…).

## Gem passes (maximum skepticism on framework-favourable readings)

Pass 1 — favourable reading "the cnot-record double slit, with eraser readouts, fits inside stage-1's native K_gen".
  Pressure test: K_gen (A-i) is DERIVED only for the constructed systems, with the single-system ball taken as given
  (K∞ seams unsourced, ROADMAP L1007–1033), local tomography by product labels (K2 premise), and cnot available (K1
  gate premises, unsourced). The eraser needs detector effects off the record axis; at the level of the stated
  substratum access a complementary readout needs a non-ones-fixing unitary, which the stated access does not supply
  (S6 + instAvail_unitary_fixes_ones + permClass_onesFixing). Verdict: holds only inside the K-programme's coordinate
  model with given single-system data; NEW (as a constraint on the input's "more accessible").
Pass 2 — favourable reading "Main L664: the detector eliminates the interference terms". Check: in the certified
  representation (D_imp_Qfb: permutation unitary, diagonal prior, collapse at every step) there are no interference
  terms to eliminate (ds7_models B9); "interference terms" in L664 refer to a representation the equivalence does not
  select. Record-only corpus marker.
Pass 3 — favourable reading "ROADMAP L1442–1447: only packaging is missing". Check: an "OI conditions X ⟹ formula"
  theorem is packaging only if X already contains what L1392–1414 records as INDEPENDENT of the stated architecture
  (relative phase; fixed nonclassical control) or OI⁺'s added principles; with X = the stated architecture the
  formula is not implied (ds7_models B6/B8 + S_imp_D + Main L568). Record-only corpus marker.
Pass 4 — favourable reading "Explainer L568: a derivation". Check: no derivation at L (ROADMAP L1442–1447); Main
  L568 has the phases entering "as a stated intervention principle rather than a consequence". Record-only marker.
Pass 5 — my own unfavourable reading "S5: general detectors leave K_gen" pressure-tested: for ONE fixed coupling one
  may take that coupling as the native gate (K_gen built on CZ contains the CZ record). The finding is about a detector
  FAMILY containing two couplings related by a local rotation of the detector (cnot and the phase kick): their records
  cannot both lie in one K_gen; a common state space needs IE1 at R_H or frame covariance (flagged). Scope narrowed
  accordingly in RESULT.
Pass 6 — C4 as OI content: CL1 meets R1–R3 with no visible memory (C4 fails trivially: all histories before the
  landing step coincide); CL0m has a C4 witness and a non-quantum pattern. On these instances C4 is neither necessary
  nor sufficient for R1–R3 [X]. NEW.
Fixed point: passes 5–6 refined scope; a further pass over C1–C55 found no new structural finding. Stop.

## Final claim numbering (used in RESULT)

"Worked for 1m 58s" (UI artifact) and the three image links are not assertions: recorded, not numbered, images not
fetched. Claims C1–C55 in input order, C45 split into C45a (scope vs K2) and C45b (accessibility). The script header
of ds7_models.py refers to the input's closing route as "C53"; this is the same claim C53 in RESULT.

## Labels decided

T-DS framework-specific reading: UNRESOLVED (objects undefined at L; gap listed in RESULT §3). Generic route (C53 and
the target's own premises): route refuted. R1–R3: non-discriminating (CL1). INDEPENDENT not claimed anywhere.

## End

- 09:32:31Z end checks: manifests rc 0 (41/209/3/1); HEAD 9f9f8257…; status empty; no bytecode under base/; five
  protocol hashes unchanged; no __pycache__ in DS/.
- Sweep (mtime and ctime) outside DS/, audit/, audit*-replay/: no file newer than the marker; only pt/ itself has a
  newer mtime/ctime (09:14:01Z). New top-level entry: auditS2-replay/ (birth 09:01:24Z; coordinator; excluded; not
  opened). No surviving unexplained entry; nothing quarantined.
- All §6 hashes recomputed and confirmed; replays identical; RESULT.md §7 written; RESULT sha256 reported in the
  final reply (computed after this note, RESULT.md not edited afterwards).
- Post-check read-through of RESULT.md (after the end checks; edits inside DS/ only): six wording corrections, no
  verdict or label changed — C53 verdict written in the protocol vocabulary ("INACCURATE", qualifier moved to the
  anchor); [K] moved off a ROADMAP citation onto StochasticInterface.lean:118 in the T-DS row; §2 assumption (e)
  marked as covered by F3 rather than by a countercontrol; "two sections above" corrected to "the section immediately
  above (L1392–1414)"; FourCopyLocal.lean path written as pt/inputs/fourcopy/ (design run) twice. §6 and §7 untouched.
  Final RESULT.md sha256 26c33475983c5d389d0e14b803a01980b8659a9bf8eb192c9172490de03989c8; RESULT.md not edited after
  this line. A final integrity re-check follows and is reported in the reply.
