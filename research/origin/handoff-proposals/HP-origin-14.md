# HP-origin-14 — round-5 findings of `research/origin` (node O14) for the coordinator

From: `research/origin` (thread branch, the commit of this file). To: the coordinator, for the bridge, equivalence and
countermodels threads and the overview. Status: proposal only; nothing here is adopted, governed or certified beyond the
kernel declarations cited at their lines at L = `9f9f8257`. Evidence: `NOTES-O14.md` (S0 at 08:04:30Z and addendum at
11:04Z, before any run or dispatch; addendum 2 at 11:08Z, before the script's run 1; verdict §0–§4), RESULTS rows O14-K …
O14-V, script `o14_opdrive.py` (exact, decision rule fixed before run 1, replayed byte-identically), design module
`lean/OriginDrive.lean` (`dev-origin/drive` @ `86358785`, run 38135099684, green, 110 declarations on the standard axioms
or a subset; not certified), its first version `lean/OriginDrive.run38134267257.lean` (run 38134267257, Build failure at
two proofs, kept as a record). Received and used only at their labels: HO-29 v1, HO-31 v1, HO-32 v1, HO-33 v1 (receipts
at round open, LOG 07:20Z).

Every statement says whether it is about **availability** (an operation obtainable through the kernel's protocols) or
about limits of available channels and the closed sets they leave invariant; none draws availability from a cone.

## 1. Statements, with labels

1. **The existing premises generate neither the drive nor continuous control** (O14-T1, O14-T5, O14-T6, O14-T9). On the
   stated access (`permClass`, `MixR ∅`, FM) every available unitary at every carrier, by every protocol, is a nonzero
   multiple of a matrix with entries in `{0} ∪ μ₄`: the reversible group is finite up to scalar — `(2n)!` and
   `(2n)! · 4^{2n−1}` modulo scalars at level `n` — has scalar powers, and is its own closure; OpDrive(θ₀) fails at every
   level; and the drive is not a limit of available channels (the off-diagonal coefficient stays in the square
   `|Re| + |Im| ≤ 1`). In every submonomial class, the phase intervention at every angle included, the level-one clause
   of `DenseUnitaryControl` fails. Availability (the channel-limit clause: limits of available channels).
   CONDITIONAL ([D] run 38135099684; [X]; the channel-limit step [W] + [X]). Placement (D) at the audited scope.
2. **Every exact source of the drive is the phase intervention or contains it** (O14-T2, O14-T4, O14-T11, O14-D). The
   phase intervention at θ₀ as a class (`driveClass`: structurally closed, `DerivedOI`, inverse accessibility, the drive as
   one step, no mixer, no density, no control, not QM); at every angle (the monomial interface; I4.60); the fractional
   layer flow (`gateFlow σ t = H diag(1, e^{iπt}) H`; with the quarter phase the drive exactly, `G(1/2) S G(θ₀/π) S†
   G(−1/2) = diag(1, w)`); the re-preparing tower (O13). Disguise test FAILED for each. Availability. CONDITIONAL ([D] +
   [X] + [W]). Placement (C).
3. **Scope precision for HO-33 item 2** (O14-T2). I4.60 (`SubstratumAvail`; assumed, level H) implies OpDrive(θ₀)
   (`opDrive_of_substratumAvail`, through `diagonal_avail`), FM fails it (`lattice_not_substratumAvail`), and it is not a
   row of Table A2. Item 2's "no stage-6 item short of composite unitary control or QM" reads as relative to Table A2's
   rows: I4.60 supplies the drive without supplying control or QM. Proposal: add that scope clause. Availability.
   CONDITIONAL ([D]; [A]).
4. **Exact quantum mechanics entails the drive** (O14-T3). `opDrive_of_qm`: so OpDrive(θ₀) is "sufficient, not
   necessary" only as a statement about premises (control and the layer flow with the quarter phase entail it) and, in
   the invariance reading, about closures. Availability. CONDITIONAL ([D]).
5. **No fixed gate at a rational angle makes the drive available** (O14-T8). For `α/π ∈ ℚ`, at every level, by every
   protocol of `MixR {α}`: the valuation at a prime above `2 − i` (O9's norm step in valuation form). `MixR {π/8}`
   (level-one density, O12-T4) is therefore the separating model for "closure-level control without the drive".
   Availability. CONDITIONAL ([W] proof, no kernel check; [X]).
6. **The `InstAvail` closure exceeds the reversible group in the limit** (O14-T9; NEW). In `MixR {π/4}` a
   repeat-until-success protocol of the five constructors — the circuit `(1 ⊗ H ⊗ H) Tof (S ⊗ 1 ⊗ 1) Tof (1 ⊗ H ⊗ H)` on
   the token and two ancilla qubits, Toffoli a permutation and `S` quarter phases of the stated access — makes available
   exactly `(1 − (3/8)^k) conj(zPh) + (3/8)^k id` for every `k`. So the drive is a limit of available channels in a class
   whose level-one reversible group is the 24 Clifford channels and where the drive is never available (items 5 and
   O14-T10); every closed set of states invariant under the available channels of `MixR {π/4}` is invariant under the
   drive. `J` is available there exactly (`uJ = e^{−iπ/4} H S³`). Availability for each `Φ_k`; the limit and the
   invariance consequence are about channels. CONDITIONAL ([W] protocol assembly, no kernel check; [X] exact blocks and
   channel).
7. **Consequence for the bridge, provisional** (O14-P). In the invariance reading — the bridge's cones closed and
   invariant under every available channel — the non-monomial datum J needs, taken as the balanced mixer, already gives
   invariance under the drive (item 6): the phase intervention at θ₀ is then no further premise, and the bridge's premise
   set would reduce to that one finite-order Clifford datum with H1, H3 and whatever (T)_𝓘 requires. In the exact reading
   item 5 stands: no rational fixed gate supplies the drive. Placement (B), provisional twice: the datum's own motivation
   within OI is not decided (I4.239; O2-G3), and the reading depends on how the bridge's cones use invariance and (T)_𝓘.
   Proposal for the bridge's cross-thread check, not a label change.
8. **The transfer clause (T)_𝓘.** No route found by which existing OI premises supply the drive (item 1). O14 did not
   examine (T)_𝓘 itself; nothing here treats (T) as necessary for QM.
9. **Reading note on HO-27 item 3** (this thread's round-4 findings). "The frame-axis rotation is in the stated access
   already" is about the substratum theory (I4.240), which O11 called the stated access; under HO-33's and the owner's
   reading the stated access is `permClass`, `MixR ∅` and FM, where the rotation is unavailable (`lattice_refutes`), and
   the substratum theory is the stated access with the phase intervention at every angle. A correction of reading, not of
   content.

## 2. What a receiving thread may assume

Items 1–6 at their labels. Bridge: items 1, 3 and 5 as the exact-reading boundary of any drive premise; items 6 and 7 as a
candidate reduction of its premise set, to be checked against its own cones. Equivalence: item 4 for any necessity claim
about the drive. Countermodels: FM's exclusion of the drive in the channel limit (item 1); `MixR {π/8}` as dense without
the drive (item 5); `MixR {π/4}` as a model where the drive is a limit of channels but never available (item 6).

## 3. What it may not assume

- kernel status for any [D] declaration (design runs), for item 5's valuation argument, for item 6's protocol, or for
  O9-L1;
- that item 6 gives the drive as an available operation (it does not: item 5), or that it serves the bridge's cones
  without checking that they are closed and invariant under every available channel;
- that the fixed gate at θ₀ supplies or fails to supply the drive exactly through dilations (OPEN);
- that (T)_𝓘 is supplied, or needed for QM, on anything in this proposal;
- availability from cone invariance, anywhere.

## 4. What would refute this proposal

- an available unitary on FM, `MixR ∅` or `permClass` at some carrier that is not a multiple of a `{0} ∪ μ₄` matrix
  (refutes item 1);
- an `InstAvail` protocol of `MixR {α}`, α/π rational, at some level, realizing `conj(zPh ⊗ 1ₙ)` exactly (refutes item 5);
- an error in the block computation of item 6 (the exact values `((3 + i)/4) zPh` and `β_m Z`, weights 5/8 and 3/8);
- a submonomial architecture satisfying the level-one clause of `DenseUnitaryControl` (refutes item 1's last clause).

## 5. Evidence hashes (sha256)

| file | sha256 |
|---|---|
| `RESULTS.md` (rows through O14-V) | `e36a7100175e7aad3172f16bd62b413b924aaa4c7c807c059eb972bacc28bca4` |
| `NOTES-O14.md` (through §4) | `9aa70c72599bcdf915cb065bd03a462de80e8d4ad63d776aa6e9271991d6e799` |
| `lean/OriginDrive.lean` (blob `04444be3`) | `a1d595ea128d7b659c7cbac6441db3afd5cc3f4ef587c89c711a67defbace629` |
| `lean/OriginDrive.run38134267257.lean` (blob `faa9bb59`) | `2639b3ceae9fab543d07c536da594d2c72bad9e570ae8f54d09c05b8dc44a7d8` |
| `o14_opdrive.py` / `.out` | `d5009e41703b21e728f72c259d89f859712981474c9abde554f44e41eeb2703c` / `6ca77df22682c581315cc0d302b889f2d7ee867c83e708944bbad3dc0269d6c2` |

Workflow runs (design evidence only): 38134267257 (dev commit `78baca7c`, Mathlib bridge job 114454805039, Build failure
at `zPh_entries` and `conjAff_iterate_scalar`, kept as the record of the first version); 38135099684 (dev commit
`86358785`, Mathlib bridge job 114457248089, Build success, 110 declarations, 108 on [propext, Classical.choice,
Quot.sound] and two on [propext, Quot.sound], gate red only on `lean-manuscript` (5 problems: the five modules without a
census disposition), `lean-axioms` PASS).
