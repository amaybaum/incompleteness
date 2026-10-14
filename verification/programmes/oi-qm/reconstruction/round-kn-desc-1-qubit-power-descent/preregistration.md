# Reconstruction round KN-DESC-1 — drivability descends from qubit-power carriers inside the K3 architecture: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** Drafted on a pull
request from `D`. The text was written by the research thread `research/equivalence` (node E8) at
L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` and is carried here from that branch (head `424aa33b`,
`research/equivalence/preregistration-drafts/S3-kn-descent.md`) with the drift from L to `D` applied (below). Its design
evidence was measured at L and is re-taken at `D` before `F`: `controls.py` is generated, the predicted execution
tree is built from `D` and dispatched, and this file may change in any of those steps (`G9`). Nothing is executed.
Only the owner designates `F` under AGENTS §A.39; an instruction to proceed is not a designation.

```v3-round
round KN-DESC-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-kn-desc-1-qubit-power-descent/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-kn-desc-1-qubit-power-descent/
record AM verification/receipts/KN-DESC-1.json
execution A verification/lean-mathlib/OIBridge/KnDescent.lean
execution A verification/lean/kn_desc1_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

D: 5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5.
This is `main` after #844. Delta(D, F) is this preregistration and any amendments in the round's `amendments/`
directory. Drift from L to `D`, measured: 64 commits; under `verification/lean-mathlib/` they add eight modules
(`BridgeConverge`, `BridgeDictionary`, `BridgeFiniteProtocol`, `EqvK2Block`, `EqvK2Converse`, `EqvK2Generation`,
`EqvK2MaxCone`, `EqvK2Schema`) and two import lines and change no landed module cited here, so every kernel line
reference below holds at `D`; the K block of `verification/ROADMAP.md` moved twelve lines with its text unchanged
(references below are at `D`); the last import line of `OIBridge.lean` at `D` is `import OIBridge.EqvK2MaxCone`;
the workflow and the census registry changed, so any workflow edit and the census family are re-derived at `D`.
The research rebuild below ran on `dee3b5ae` (`main` after #818). From `dee3b5ae` to `D`, measured: 19 commits;
`verification/lean-mathlib/` is the same tree (`0289118d4b5ff7074ae5ff88d0a4bf2692eb450b`) at both, and so are
`.github/workflows/verify.yml` (blob `159936eb`), `verification/receipts/` (46 receipts),
`verification/infrastructure/legacy-records.json` (303 records), `tools/` apart from `tools/unicode-fix.tex`,
`verification/audits/foundations/kn-elementary-carrier-census.md` and KT4-PREM-1's record;
`verification/ROADMAP.md` changed only outside the K block, and the census registry (blob `c8e0e184` at `D`) changed
only in the status and note of the GR 3.3 family, with 106 families and none naming `KnDescent`. Every reference
below is measured at `D`. KINF-COPY-1, whose controls P, W, V, I, C, R, G are adopted below by reference, has no
record at `D`: its control plane is the draft on #822 (head `90c72640`, from `dee3b5ae`).

**No manuscript, no built artifact, `verification/ROADMAP.md`, no landed kernel module and no other round's record
change under any outcome.**

## The objects

- **`D`** — `5bfdaba6`, the base of this pull request. Drafting measurements: L, re-taken at `D` before `F`. **`F`**, **`E`**, **`Λ`**, **`Q`** as §A.39.

## What the round is

Kₙ (ROADMAP :1070–1081) is the lift from DIM-1's elementary `d = 3` system to the complex matrix carriers of every
finite size, with the implementation repertoire `DrivesElementary` (SubstratumSource.lean:77) assumes at **every**
carrier. The census (`verification/audits/foundations/kn-elementary-carrier-census.md`) records that no subspace or
face principle relating higher-level systems to elementary ones exists. The round asks:

- **Q-DESC (kernel).** In an implementation class with `Architecture` (ImplementationLocality.lean:506),
  `ContextStable` (:359) and `LabelInvariant` (:364), does every admissible operator on `T` compress to an admissible
  operator on any nonempty `S` along any injection `S ↪ T`; do the three elementary generator families compress to
  themselves; and does drivability at the carriers `Fin (2 ^ k)`, all `k`, give `DrivesElementary`?
- **Q-IFF (kernel).** Is `QuantumArchitecture 𝓘` (SubstratumSource.lean:86) equivalent to `Architecture 𝓘 ∧
  ContextStable 𝓘 ∧ LabelInvariant 𝓘 ∧ DaggerStable 𝓘 ∧ ∀ k, DrivesElementaryAt 𝓘 (Fin (2 ^ k))`, with one kernel
  witness per direction (§A.34)?
- **Q-EXACT (exact layer).** Do the exact instances behave as the theorems state, and is `ContextStable` load-bearing
  on the exact failure instances of the class "every matrix at sizes `2^k`, unit-disk diagonal matrices elsewhere"?

## The kernel declarations the round would add (frozen surface, module `OIBridge/KnDescent.lean`)

Imports `OIBridge.SubstratumSource` and `OIBridge.LiftAudit`; namespace `OIBridge.KnDescent`. The statement surface
is the design module `EqvKnDesc` built green in run 38090116254 (copy: `research/equivalence/lean/EqvKnDesc.lean`,
blob `8157f8ea`), with thirteen declarations (one definition and twelve theorems) and twelve `#print axioms` lines:

```lean
def DrivesElementaryAt (𝓘 : ImplementationClass) (T : Type) [Fintype T] [DecidableEq T] : Prop :=
  (∀ (a b : T) (t : ℝ), 𝓘 T (ReachabilitySeam.flow (transition a b) t))
    ∧ (∀ a b : T, 𝓘 T (permMatrix (Equiv.swap a b))) ∧ ∀ a : T, 𝓘 T (phaseGate a)
theorem drivesElementaryAt_of_drives (h : DrivesElementary 𝓘) (T : Type) [Fintype T] [DecidableEq T] :
    DrivesElementaryAt 𝓘 T
theorem compress_mem (arch : Architecture 𝓘) (hC : ContextStable 𝓘) (hL : LabelInvariant 𝓘)
    {S T : Type} [Fintype S] [DecidableEq S] [Nonempty S] [Fintype T] [DecidableEq T]
    (ι : S ↪ T) {K : Matrix T T ℂ} (hK : 𝓘 T K) : 𝓘 S (K.submatrix ι ι)
theorem transition_submatrix (ι : S ↪ T) (a b : S) :
    (transition (ι a) (ι b)).submatrix ι ι = transition a b
theorem flow_transition_self (a : S) (t : ℝ) : ReachabilitySeam.flow (transition a a) t
    = 1 + (Complex.exp ((-(t : ℂ) * Complex.I) * 2) - 1) • Matrix.single a a (1 : ℂ)
theorem flow_transition_submatrix (ι : S ↪ T) (a b : S) (t : ℝ) :
    (ReachabilitySeam.flow (transition (ι a) (ι b)) t).submatrix ι ι = ReachabilitySeam.flow (transition a b) t
theorem permMatrix_swap_submatrix (ι : S ↪ T) (a b : S) :
    (permMatrix (Equiv.swap (ι a) (ι b))).submatrix ι ι = permMatrix (Equiv.swap a b)
theorem phaseGate_submatrix (ι : S ↪ T) (a : S) : (phaseGate (ι a)).submatrix ι ι = phaseGate a
theorem drivesElementaryAt_of_embedding (arch) (hC) (hL) (ι : S ↪ T) (hT : DrivesElementaryAt 𝓘 T) :
    DrivesElementaryAt 𝓘 S                                   -- [Nonempty S]
theorem le_two_pow (n : ℕ) : n ≤ 2 ^ n
theorem drivesElementary_of_pow (arch : Architecture 𝓘) (hC : ContextStable 𝓘) (hL : LabelInvariant 𝓘)
    (hpow : ∀ k : ℕ, DrivesElementaryAt 𝓘 (Fin (2 ^ k))) : DrivesElementary 𝓘
theorem quantumArchitecture_iff_pow (𝓘 : ImplementationClass) :
    QuantumArchitecture 𝓘 ↔ Architecture 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘
      ∧ DaggerStable 𝓘 ∧ ∀ k : ℕ, DrivesElementaryAt 𝓘 (Fin (2 ^ k))
theorem drivesElementaryAt_fullClass (T : Type) [Fintype T] [DecidableEq T] : DrivesElementaryAt fullClass T
```

The directional witnesses of the displayed equivalence (§A.34): (→) `drivesElementaryAt_of_drives` applied to the
`drives` field; (←) `drivesElementary_of_pow`. The compression proof uses `Equiv.Perm.exists_extending_pair` (Mathlib)
to relabel `S × T` onto `S × Fin |T|` with `(s₀, ι s) ↦ (s, k)`, then `Architecture.block` at `(k, k)`; the flow
compressions use LiftAudit's closed form `flow_transition_closedForm` (`a ≠ b`) and its idempotent lemma
`exp_smul_idempotent` (`a = b`).

**Pre-`F` revision item (owner's choice).** Run 38090116254 reported, as warnings only, unused `[Fintype S]
[Fintype T]` section binders in `transition_submatrix`, `permMatrix_swap_submatrix`, `phaseGate_submatrix`, and a
`haveI` style hint. Omitting the unused binders changes those three effective statements; if the owner wants a
warning-free module, the revision is made before `F` and the predicted tree is rebuilt.

**Census family:** "inside the K3 interfaces drivability descends from qubit-power carriers: in an implementation class
with Architecture, ContextStable and LabelInvariant every admissible operator compresses along any injection of
carriers, the elementary generators compress to themselves, and drivability at the carriers Fin (2^k) gives
DrivesElementary (round KN-DESC-1, reconstruction)", `modules: ["KnDescent"]`, `status: "kernel-only"`,
`manuscript: []`. **Import line** after `import OIBridge.EqvK2MaxCone`.

## The exact layer (frozen probe `verification/lean/kn_desc1_probe.py`)

The probe is `research/equivalence/experiments/e3_compress.py` (sha256 `18c3aa1b…`; 7 checks), using Python and
SymPy 1.14.0 with exact symbolic arithmetic: F0 (the closed form of `flow (transition a b) t` solves `M' = −iHM`, `M(0) = 1`), G1–G3 (the
literal construction — tensor, an explicit bijection, reindex, block — returns the three generator families for
`(|S|, |T|) = (3, 4), (3, 8), (5, 8)`, 32 ordered distinct-index pairs), B1 (every bijection used sends `(s₀, ι s)` to `(s, 0)`), K1
(compressing a flow that leaves `ι(S)` is not unitary: `B Bᴴ − 1` has entry `−sin² t` — the invariance of the
coordinate subspace is load-bearing for the generators), K2 (no bijection `Fin 4 ≃ Fin 3 × Fin m`; `1_3 ⊗ X` is not
diagonal; the `Fin 3` transition flow at `t = 1` is not diagonal — the exact failure instances showing `ContextStable`
load-bearing). The frozen probe does not sample self-index transition flows (`a = b`); the universal kernel theorem
covers that case separately through `flow_transition_self`. Its shard `probes_kndesc1` and the aggregate edit follow
KT4-PREM-1, with the Python/SymPy dependency installed explicitly.

## The decision rules (frozen; implemented by `controls.py verdict`)

| Cell | Outcome | Rule |
|---|---|---|
| Q-DESC | `KN-DESC-DESCENT-PROVED` | the module's statements are exactly the frozen ones (S1), resolve to the landed objects (S2), and the exact-head run at `E` builds the module with every frozen `#print axioms` line within `[propext, Classical.choice, Quot.sound]` |
| Q-DESC | `KN-DESC-DESCENT-NOT-ESTABLISHED` | otherwise |
| Q-IFF | `KN-DESC-IFF-PROVED` | Q-DESC's conditions for `quantumArchitecture_iff_pow`, `drivesElementaryAt_of_drives` and `drivesElementary_of_pow`, and the proof of the iff names exactly those two witnesses, one per direction (S3) |
| Q-IFF | `KN-DESC-IFF-NOT-ESTABLISHED` | otherwise |
| Q-EXACT | `KN-DESC-INSTANCES-EXACT` | the probe blob at `E`, run by `controls.py` with `python3 -I`, prints `PASS` for F0, G1, G2, G3, B1, K1, K2, no `FAIL`, `checks: 7, failures: 0` and `VERDICT COMPRESSION-DESCENT-EXACT` |
| Q-EXACT | `KN-DESC-INSTANCES-NOT-ESTABLISHED` | otherwise |

No rule reads another cell's outcome. `KN-DESC-1-READ` when the three cells are assigned; tokens printed by
`controls.py verdict E` from the measurements at `E`.

## The earned reading and the non-inference rule (frozen)

> Earned reading (only when all three cells are positive): inside the K3 interfaces, an implementation class with
> Architecture, ContextStable and LabelInvariant that drives the elementary transitions on every carrier Fin (2^k)
> drives them on every finite carrier, and QuantumArchitecture is equivalent to its four closure clauses with
> drivability at the qubit-power carriers.

> Non-inference rule: this round does not show that OI, K2 or any composite supplies drivability on any carrier, a
> dictionary from a field-neutral k-token composite to the carriers Fin (2^k), or any of the closure clauses
> Architecture, ContextStable, LabelInvariant, DaggerStable. The descent fixes the repertoire at carriers the formalism
> already has as types and uses ContextStable with spectators of odd size; it does not produce a three-level system
> from qubits. ContextStable is the matrix form of the spectator clause the composite action (b) needs; the reduction
> moves the carrier generality of Kn into it and does not discharge it. The load-bearing status of block and
> LabelInvariant rests on written arguments and is not part of this round. The probe is an exact computation, not a
> Lean kernel proof.

**Premise this round does NOT source:** drivability at the qubit-power carriers (`hpow`), and every closure clause
(`arch`, `hC`, `hL`, `DaggerStable`); the substratum class has the closure clauses as theorems and lacks drivability
(`substratum_residual`, StructuralClosure.lean:383).

## What a positive outcome strengthens (frozen)

A positive outcome strengthens a conditional assembly and nothing else. The K3 assembly
`genTheory_qm_of_quantumArchitecture` (SubstratumSource.lean:136) takes `QuantumArchitecture 𝓘` as a premise;
with all three cells positive, the drivability clause of that premise may be stated at the carriers `Fin (2 ^ k)`
alone (`quantumArchitecture_iff_pow`), every other clause unchanged, and the assembly stays conditional on every
hypothesis in the table below. Certifying this round alone does not close Kₙ and does not establish F1, the full
conditional equivalence of `verification/programmes/oi-qm/PROGRAMME.md` (Arc F); no cell, and no combination of
cells, is read as either.

**The matrix framework the design assumes: carrier-general architecture and spectator closure.** Every hypothesis
of the twelve theorems, with its kernel object (landed at `D`) or design object (defined in the module):

| hypothesis | object | taken by |
|---|---|---|
| carrier-general matrix framework | `ImplementationClass` (ImplementationLocality.lean:244): admissibility is a predicate on the complex matrices of every finite carrier type, so `Fin (2 ^ k)`, `S × T` and `S × Fin m` are carriers before any drivability is asked | every theorem, through the type of `𝓘` |
| carrier-general architecture | `Architecture 𝓘` (ImplementationLocality.lean:506), every field quantified over every carrier; the proofs use the field `block` (:514) with `ancBlock` (AncillaClosure.lean:457) and no other field | `arch` of `compress_mem`, `drivesElementaryAt_of_embedding`, `drivesElementary_of_pow`; a conjunct of both sides of `quantumArchitecture_iff_pow` |
| spectator closure | `ContextStable 𝓘` (ImplementationLocality.lean:359), `𝓘 S K → 𝓘 (R × S) (tensorOf 1 K)` for every finite spectator `R`; `compress_mem` instantiates `R := S`, the target carrier, so the descent to an odd `S` uses a spectator of odd size | `hC` of the same three; a conjunct of both sides of the iff |
| relabelling | `LabelInvariant 𝓘` (ImplementationLocality.lean:364), applied to the bijection `S × T ≃ S × Fin (Fintype.card T)` obtained from `Equiv.Perm.exists_extending_pair` (Mathlib) | `hL` of the same three; a conjunct of both sides of the iff |
| dagger stability | `DaggerStable 𝓘` (MicroscopicReversibility.lean:216) | a conjunct of both sides of the iff only; no descent theorem takes it |
| drivability at every carrier | `DrivesElementary 𝓘` (SubstratumSource.lean:77) | `h` of `drivesElementaryAt_of_drives` |
| drivability at one carrier | `DrivesElementaryAt 𝓘 T` (design object) | `hT` of `drivesElementaryAt_of_embedding` |
| drivability at the qubit-power carriers | `∀ k, DrivesElementaryAt 𝓘 (Fin (2 ^ k))` (design object) | `hpow` of `drivesElementary_of_pow`; the last conjunct of the iff's right side |
| injection of carriers | `ι : S ↪ T` | `compress_mem`, the four generator compressions, `drivesElementaryAt_of_embedding` |
| nonempty target | `[Nonempty S]`; `drivesElementary_of_pow` treats the empty carrier by vacuity | `compress_mem`, `drivesElementaryAt_of_embedding` |
| admissible operator | `𝓘 T K` | `hK` of `compress_mem` |

The remaining theorems take no hypothesis on `𝓘`: `transition_submatrix`, `flow_transition_self`,
`flow_transition_submatrix`, `permMatrix_swap_submatrix` and `phaseGate_submatrix` are matrix identities for the
landed `transition` (LieRankSource.lean:199), `phaseGate` (:209), `permMatrix` (CoherentLift.lean:92) and
`ReachabilitySeam.flow` (ReachabilitySeam.lean:95), through LiftAudit's `flow_transition_closedForm` (:276) and
`exp_smul_idempotent` (:219); `le_two_pow` is arithmetic; `drivesElementaryAt_fullClass` is about `fullClass`
(ImplementationLocality.lean:374). No hypothesis in the table is sourced by the round.

## The ROADMAP wording the round would license (HP-1, row Kₙ; not applied by the round)

At `D`, ROADMAP :1070–1081 ends "… or by another carrier-general construction. The classification is recorded in
[`audits/foundations/kn-elementary-carrier-census.md`](…)." and states "No current theorem supplies the lift." Under
`KN-DESC-1-READ` with all three cells positive, the row may gain: "Inside the K3 interfaces the carrier-general
quantifier of drivability reduces to qubit-power carriers: an implementation class with `Architecture`,
`ContextStable` and `LabelInvariant` that drives the elementary transitions on every `Fin (2^k)` drives them on every
finite carrier (`drivesElementary_of_pow`); what remains is drivability on qubit registers from the elementary system
and those closure clauses." The caution travels with it: the reduction moves the carrier generality into
`ContextStable`, the matrix form of the spectator clause (b) needs. "No current theorem supplies the lift" stays true
and stays. Kₙ remains OPEN under every outcome.

## The controls (in `controls.py`)

- **S1 surface**: preamble, thirteen declarations (one definition and twelve theorems) in order with frozen signatures, twelve prints. Mutations, each
  failing with its code: `hC` dropped from `compress_mem`; `[Nonempty S]` dropped from `compress_mem`; `hpow` weakened
  to `∀ k, 1 ≤ k → …`; `DaggerStable` dropped from the iff's right side; the conclusion of `drivesElementary_of_pow`
  replaced by `DrivesElementaryAt 𝓘 (Fin 3)`; a thirteenth print.
- **S2 resolution**: `ImplementationClass`, `Architecture`, `ContextStable`, `LabelInvariant`, `DaggerStable`,
  `DrivesElementary`, `QuantumArchitecture`, `fullClass`, `ancBlock`, `tensorOf`, `transition`, `phaseGate`,
  `permMatrix`, `ReachabilitySeam.flow`, `LiftAudit.pairProj` resolve to the landed declarations at `D`.
- **S3 directional witnesses**: the proof term of `quantumArchitecture_iff_pow` names `drivesElementaryAt_of_drives`
  in the forward and `drivesElementary_of_pow` in the backward component. Mutation: a forward component given by a
  term that does not name `drivesElementaryAt_of_drives` fails S3 and nothing else.
- **S4 phrases** (header, result note): "OI supplies", "K2 supplies", "drivability is sourced", "Kn is discharged",
  "Kn is closed", "Kₙ is closed", "F1 is established", "establishes F1", "the lift is supplied",
  "produces a three-level system", "kernel proof of" (for the probe), "design module", "not for merge".
- **P, W, V, I, C, R, G** as KINF-COPY-1 (probe and workflow frozen; three tokens; the earned reading exactly when all
  three are positive; one import line; one family; the governed paths).

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls and the probe are the frozen ones | `C2`: blobs at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms | `C3`: the dispatch run at exactly `E`, every job `success`; the Mathlib bridge build and the twelve prints |
| each direction of the displayed iff has its own witness | `C5`: S3 in `controls.py check E --freeze F` |
| the result note reads no outcome as closing Kₙ or establishing F1 | `C5`: S4 in `controls.py check E --freeze F` |
| the exact layer replays and renders | `C3`: shard `probes_kndesc1` green with `VERDICT COMPRESSION-DESCENT-EXACT`; the aggregate job green |
| the module is registered; no manuscript changes | `C4`: the release gate at `E` passing every step |
| the change stays inside the governed paths | `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Design evidence and the predicted outputs

| run | commit | workflow run | measured |
|---|---|---|---|
| 1 | `05b5756c` (`dev-equivalence/kn-desc`, based on L; module `EqvKnDesc` and its import line) | 38090116254 | Mathlib bridge job 114324651733: `Build completed successfully (3644 jobs)`; all twelve `EqvKnDesc` prints `[propext, Classical.choice, Quot.sound]`; release gate: every step PASS except `lean-manuscript` (1 problem: no family) — `lean-axioms` 5872 named results, no `sorryAx`; `legacy-records` 303 intact; `v3-receipts` 43 hold; `claims`, `duplicate` PASS |
| exact | `research/equivalence` | `e3_compress` (local; replayed by the coordinator, 3/3 identical) | 7 checks, 0 failures, `VERDICT COMPRESSION-DESCENT-EXACT` |

**Research rebuild at `dee3b5ae`.** Exact source commit
`d3a95be6a0049ee1450f438803ebcf2896f69744` (`research/finite-reconstruction-design-20261013`), workflow
`.github/workflows/finite-reconstruction-design.yml` ("finite reconstruction research design"),
[run 38457070337, job 115502431432](https://github.com/amaybaum/incompleteness/actions/runs/38457070337/job/115502431432),
compiled the research-only module
`verification/programmes/oi-qm/reconstruction/carrier-descent-design/KnDescentDesign.lean`
in namespace `OIBridge.KnDescentDesign`, with all twelve theorem prints
`[propext, Classical.choice, Quot.sound]`. Its SHA256 is
`fa9c3b084ddfa01a5fcb2ec3023f004d7614f16943b021c1d2f1ebfe67f0b70f`.
The proof body is the original `EqvKnDesc` source at
`424aa33bf16c5160c00e6f6aea974d00c0d745dd`, Git blob
`8157f8eaf77a080391c54e518f4c6f3bb4de8f56`, with only the research header
and namespace changed. The landed Lean sources in the build are D's: `verification/lean-mathlib/` is the tree
`0289118d` at `dee3b5ae`, at `d3a95be6` and at `D`.
The job verified the source probe's seven checks and byte-identical output,
the separately written standard-library checker's 2410 controls (including
self-index flows), 303 legacy records, 46 receipts and artifact placement.
The retained unused-section-binder warnings and `haveI` style hint match the
historical source. This is confirming research design evidence. It does not
execute the native round, designate F or E, adopt a module, or certify the
predicted execution tree with its new census family, import line and shard.

**Re-measurement at `D`.** Disposable commit `22e0d002c2f1439adca8ca5c99cccc9a0debfaa1`, single parent `D`, whose
tree is `D` with the design files and the workflow of `d3a95be6` byte for byte and the workflow's push trigger
extended to that commit's branch,
[run 38597304093, job 115967222595](https://github.com/amaybaum/incompleteness/actions/runs/38597304093/job/115967222595),
measured: every step `success`; the landed imports `OIBridge.EqvK2Schema`, `OIBridge.SubstratumSource` and
`OIBridge.LiftAudit` built (`Build completed successfully (3172 jobs)`); `KnDescentDesign.lean` (SHA256
`fa9c3b08…`) elaborated with all twelve theorem prints `[propext, Classical.choice, Quot.sound]` and the same four
linter warnings; the source probe and the standard-library checker replayed byte-identical to their saved outputs;
303 legacy records intact, 46 receipts hold, artifact placement OK. This re-measures the design at `D`; the design's
provenance is the build of `d3a95be6` above. Neither run is a `check-run` attestation of a round object.

**Predicted outputs, generated from those measurements by the rules:** Q-DESC `KN-DESC-DESCENT-PROVED`, Q-IFF
`KN-DESC-IFF-PROVED` (run 1's statements and prints; the iff's two components are the named witnesses in the built
proof), Q-EXACT `KN-DESC-INSTANCES-EXACT` (`checks: 7, failures: 0`). Of the release gate at the predicted tree, every
step is predicted PASS: run 1 failed only at `lean-manuscript`, which the census family discharges. **Not yet
measured:** the predicted execution tree at `D` (module renamed `KnDescent`, the family, the probe and
its shard), to be built and dispatched before `F`.

## Stages and outcomes

Stages as KT4-PREM-1 (C1 `controls.py`; S1 module, probe, workflow edit, import line and family; proof repairs only; S2
the result note = candidate `E`). **`KN-DESC-1-READ`**: `controls.py check E --freeze F` OK, three tokens printed, the
exact-head run at `E` green on every job. **`KN-DESC-1-HALTED`**: anything else (`S12`). No outcome sources drivability
or a closure clause, or edits the ROADMAP or a manuscript; correctness bands unchanged (consistency axis).
