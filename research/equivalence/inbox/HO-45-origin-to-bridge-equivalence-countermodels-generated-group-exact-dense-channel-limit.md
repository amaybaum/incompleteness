# HO-45 (v1) — origin → bridge, equivalence, countermodels: the generated group of the stated access, exact against dense; every exact source of the drive is the phase intervention; at the balanced angle the drive is a limit of available channels and never available

**From** `research/origin` (round 5, node O14; proposal HP-origin-14). **To** `research/bridge`, `research/equivalence`
and `research/countermodels`. Written by the coordinator from the source thread's committed record and the round-5
audit (`AUDIT-ORIGIN-R5.md`), which adds two qualifications (findings F-O5-2, F-O5-3, in items 1 and 7); version 1,
2026-10-11. Each item says whether it is about **availability** or about limits of available channels and the closed
sets they leave invariant; none draws availability from a cone.

## Statements and labels

1. **The existing premises generate neither the drive nor continuous control** (O14-T1, T5, T6, T9; availability, with
   a channel-limit clause). On the stated access (`permClass`, `MixR ∅`, FM's `latticeClass`) every available unitary at
   every carrier, by every protocol, is a nonzero multiple of a matrix with entries in `{0} ∪ μ₄`
   (`lattice_avail_finite_upToScalar`, `mixEmpty_avail_finite_upToScalar` [D]; for a unitary-ray-saturated architecture
   the `InstAvail` closure adds no unitary conjugation, `avail_unitary_iff` [D]): the reversible group is finite up to
   scalar at every carrier, every element has a scalar power, and the group is its own closure. Its orders modulo
   scalars are `(2n)!` (`permClass`) and `(2n)! · 4^{2n−1}` (`MixR ∅`, FM) **computed at levels one and two** ([X], and
   independently by the coordinator), and the monomial count at general `n` [W] (F-O5-2). OpDrive(θ₀) fails at every
   level, and the drive is not a limit of available channels: the coefficient `⟨0|Φ(|0⟩⟨1|)|1⟩` of every available
   channel stays in the square `|Re| + |Im| ≤ 1` (every Kraus operator is a positive multiple of a partial monomial with
   `μ₄` entries [W]; spot-checked on 400 random protocols by the coordinator [X]), while the drive's is `w̄`, with `7/5`.
   In every submonomial class the level-one clause of `DenseUnitaryControl` fails (`not_levelOneClause_of_submonomial`
   [D]). Label: CONDITIONAL ([D] run 38135099684; [X]; the channel-limit step [W] + [X]). Placement (D) at the audited
   scope.
2. **Every exact source of the drive is the phase intervention or contains it** (O14-T2, T4, T11, O14-D; availability).
   The phase intervention at θ₀ as a class (`driveClass`: structurally closed, `DerivedOI`, inverse accessibility, the
   drive as one step, no mixer, no density, no control, not QM); at every angle (the monomial interface; I4.60); the
   fractional layer flow (`gateFlow σ t = H diag(1, e^{iπt}) H`; with the quarter phase the drive exactly,
   `G(1/2) S G(θ₀/π) S† G(−1/2) = diag(1, w)`); the re-preparing tower (O13). Disguise test FAILED for each.
   CONDITIONAL ([D] + [X] + [W]). Placement (C).
3. **I4.60 implies the drive and lies outside Table A2** (O14-T2): issued as the scope correction HO-33 v2.
4. **Exact quantum mechanics entails the drive** (O14-T3, `opDrive_of_qm` [D]; availability). "Sufficient, not
   necessary" therefore has content only as a statement about premises (control and the layer flow with the quarter
   phase entail it) and, in the invariance reading, about closures (`MixR {π/8}` is dense at level one and never makes
   the drive available). CONDITIONAL ([D]).
5. **No fixed gate at a rational angle makes the drive available** (O14-T8; availability). For `α/π ∈ ℚ`, at every
   level, by every protocol of `MixR {α}`: the valuation at a prime above `2 − i` (`w = (2 + i)/(2 − i)`, valuation −1),
   O9's norm step in valuation form. CONDITIONAL ([W] proof, no kernel check; [X] inputs, checked independently).
6. **The `InstAvail` closure exceeds the reversible group in the limit** (O14-T9; NEW). In `MixR {π/4}` the circuit
   `(1 ⊗ H ⊗ H) Tof (S ⊗ 1 ⊗ 1) Tof (1 ⊗ H ⊗ H)` on the token and two ancilla qubits has readout blocks
   `((3 + i)/4) zPh` (weight 5/8) and three multiples of `Z` (weight 3/8); the protocol "attach, read out and reset the
   ancillas, apply the circuit, read out, correct a failure by `Z`, repeat `k` times, coarse-grain, discard" uses only
   `op`, `readout`, `bind`, `coarse` and `discard` and makes available exactly `Φ_k = (1 − (3/8)^k) conj(zPh) + (3/8)^k id`
   (with a spectator, at every level). So the drive is a limit of available channels in a class whose level-one
   reversible group is the 24 Clifford channels and where the drive is never available (item 5; O14-T10 under O9-L1);
   every closed set of states invariant under the available channels of `MixR {π/4}` is invariant under the drive.
   `J` is available there exactly (`uJ = e^{−iπ/4} H S³`). Verified independently by the coordinator with the thread's
   circuit and with a second circuit (doubly controlled `iZ`, failures `∝ S`, success `∝ diag(1, (4 − 3i)/5)`, `S·V = D`).
   Availability for each `Φ_k`; the limit and its consequence concern channels and closed invariant sets. CONDITIONAL
   ([W] protocol assembly, no kernel check; [X]).
7. **Consequence for the bridge, provisional** (O14-P; scoped by the coordinator, F-O5-3). Item 6 cannot supply B20's
   availability premise OpDrive(θ₀) (item 5: the drive is never available in `MixR {π/4}`). In the invariance reading it
   gives invariance under the drive of every **closed** pair cone that is invariant under every **available channel** of
   the class. The bridge's transfer clause (T)_𝓘, as built, transfers admissible one-token **unitaries** only; the
   repeat-until-success channels act through ancillas, readout, feed-forward and discard, so the route needs the
   transfer in **channel form**, (T^ch)_𝓘 (every available one-token channel `Φ` maps `K` into itself through
   `coordOf ∘ (1 ⊗ Φ) ∘ dict`), together with closedness of `K` (`hcl`). The J datum must be available on every qubit
   factor, which follows from the token by I4.30 and kernel transport. The candidate premise set {J-datum taken as the
   balanced mixer, (T^ch)_𝓘, `K` closed} trades the phase intervention at θ₀ for the channel form of the transfer
   clause; the J datum stays introduced (I4.239; O2-G3). Placement **(B), provisional twice**: the datum's motivation
   within OI is not decided, and the route serves the bridge only if its cones are required to be invariant under every
   available channel. Not assembled against `bridge_derived_half`.
8. **The transfer clause.** No route found by which existing OI premises supply the drive (item 1). O14 did not examine
   (T)_𝓘 itself; nothing here treats (T) or (T^ch) as necessary for quantum mechanics.
9. **Reading note on HO-27 item 3.** "The frame-axis rotation is in the stated access already" is about the substratum
   theory (I4.240), which O11 called the stated access; under HO-33's and the owner's reading the stated access is
   `permClass`, `MixR ∅` and FM, where the rotation is unavailable (`lattice_refutes`), and the substratum theory is the
   stated access with the phase intervention at every angle. A correction of reading, not of content.

## The alternative generating sets (O14 §2, confirmed by the coordinator)

| set | what it generates | the drive |
|---|---|---|
| `T = diag(1, ζ₈)` with the stated access | a finite group (16 elements modulo scalars) | no |
| `T` with the balanced mixer (Hadamard–T) | dense [L] | not available (item 5's argument over `ℤ[ζ₈][1/2]`); a limit |
| `rot(π/8)`, `S`, `X` | dense at level one | never available (item 5) |
| the balanced mixer with Toffoli and `S` | level one: 24 Clifford channels | a limit of available channels (item 6), never available |
| `rot θ₀` | dense at every level ([K] composed in [D]) | exact OPEN (excluded at level one without dilations given [L]) |
| the layer flow with the quarter phase | every token unitary | exactly; the phase intervention in another basis (disguise test FAILED) |

## Evidence

| item | pointer |
|---|---|
| source | `research/origin` @ `44c06d46` (O14 closed at `f0128275`) |
| proposal | `research/origin/handoff-proposals/HP-origin-14.md` (sha256 `0eeb4e33…`) |
| module | `lean/OriginDrive.lean` (sha256 `a1d595ea…`; dev `dev-origin/drive` @ `86358785`; run 38135099684, job 114457248089: Build success, 110 prints, 108 standard and 2 on `[propext, Quot.sound]`, `lean-axioms` 6178, gate red only on `lean-manuscript`); the first version `lean/OriginDrive.run38134267257.lean` (`2639b3ce…`, run 38134267257, Build failure at two sites) |
| script | `experiments/o14_opdrive.py` (`d5009e41…`) / `.out` (`6ca77df2…`): run 1 both verdicts, replay byte-identical |
| notes, results | `NOTES-O14.md` (`9aa70c72…`: S0 08:04:30Z, addenda 11:04Z and 11:08Z before run 1, verdict §0–§4); `RESULTS.md` (`e36a7100…`) rows O14-K … O14-V |
| audit | `research/AUDITS/2026-10-11-round5/AUDIT-ORIGIN-R5.md`; `origin/indep_checkO5.py` (Z1–Z6 PASS, CC1–CC6 False) and `origin/indep_checkO5b.py` (Y1–Y4 PASS, DD1–DD3 False), replays identical |

## What the receiving threads may assume

Items 1–9 at their labels, item 1 with its qualification on the orders and item 7 with its scope. **Bridge:** items 1, 3
(HO-33 v2) and 5 as the exact-reading boundary of any drive premise; items 6 and 7 as a candidate alternative premise
set, to be checked against its own cones in the channel form of the transfer. **Equivalence:** item 4 for any necessity
claim about the drive. **Countermodels:** FM's exclusion of the drive in the channel limit (item 1); `MixR {π/8}` as
dense without the drive (item 5); `MixR {π/4}` as a model where the drive is a limit of channels but never available
(item 6).

## What they may not assume

- kernel status for any [D] declaration, for item 5's valuation argument, for item 6's protocol, or for O9-L1;
- that item 6 gives the drive as an available operation (it does not: item 5), or that it serves the bridge's cones
  without the channel form of the transfer and closedness;
- the exact orders at every level as computed (they are computed at levels one and two);
- that the fixed gate at θ₀ supplies or fails to supply the drive exactly through dilations (OPEN);
- that (T)_𝓘 or (T^ch)_𝓘 is supplied, or needed for QM, on anything here;
- availability from cone invariance, anywhere.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-45 v1` and records in its `LOG.md`
whether and how it relies on it.
