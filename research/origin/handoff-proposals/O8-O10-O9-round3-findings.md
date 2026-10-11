# Handoff proposal O8-O10-O9-R3 — round-3 findings of `research/origin` for the coordinator

From: `research/origin` (thread branch, the commit of this file). To: the coordinator, for the bridge, equivalence and
countermodels threads and the overview. Status: proposal only; nothing here is adopted, governed or certified beyond
the kernel declarations cited at their lines at L = `9f9f8257`. Evidence: `NOTES-O8.md`, `NOTES-O10.md`, `NOTES-O9.md`,
RESULTS rows O8-…, O10-…, O9-…, scripts `o8_exclusive`, `o10_pair`, `o9_level2`, `o9_scope` (exact, decision rules fixed
before run 1, replayed byte-identically), design module `lean/OriginExclusive.lean` (`dev-origin/exclusive` @ `5df964af`,
workflow run 38099172719, Build green, 33 declarations on the standard axioms; not certified). Received and used only
at their labels: HO-12 v1, HO-13 v1, HO-3 v1.

## 1. Statements, with labels

1. **The exclusive readout as a premise is OI-N1's factor property, and the stated access refutes it** (O8-T1 … O8-T3,
   O8-V). In every `FiniteOperationalTheory` over a nonempty system the native readout is the kernel's block pinching
   of the ancilla values, a passive repeatable instrument on every algebra whose blocks do not straddle two ancilla
   values; the exclusivity clause relative to such an algebra (`ExclusiveOn`) is false there, and in the substratum
   theory. Holding it on an algebra forces a block straddling two ancilla values (coherence between ancilla values);
   on a factor it holds in every theory. Cost: it contradicts `readout_is_localLuders` with the structure field
   `readout_avail` (OperationalAssembly.lean:658, :642), and in state form `pureSeedPrep_available_of_swap` (:675)
   given the exchanges. Label: CONDITIONAL ([D] `not_exclusiveOn_of_refines`, `exists_straddle_of_exclusiveOn`,
   `exclusiveOn_factor`, `substratumTheory_exclusivity_false`, run 38099172719; kernel facts CERTIFIED at the cited
   lines).
2. **Any nontrivial cell suffices on any finite carrier** (O8-T4): with every permutation available, one passive
   readout of any cell C, ∅ ≠ C ≠ Ω, reaches every point mass from the uniform state — the general form of O5-T1a.
   CONDITIONAL ([D] `reach_pointMass`; [X] closures C(2N−1, N) for N ≤ 5, the construction replicated on 2424 cases).
3. **Disguise test of the premise** (O8-D): passes the owner's letter; fails on the kernel's carrier (it presupposes
   the coherence it was to source); on the knowledge-balance toy it is the observation-side equivalent of the balanced
   mixer, and the witness numbers (1, 1/2) do not detect it (memory erasure reproduces them). CONDITIONAL ([X] + [W]).
4. **HO-13's token pair on one re-preparing token** (O10-T1, O10-T2): on the Kochen–Specker sphere tower, `cyc3` acts
   with the exact witness (1, 1/2) for the body's own frame dephasing, and the tower's stage-crossing datum is HO-13's
   frame-axis rotation R_z(θ₀), cos θ₀ = 3/5; the circle tower carries neither. CONDITIONAL on the cosine
   re-preparation law (outside the stated access; false there by item 1).
5. **The pair half is not supplied by any re-preparing law short of the cone's own** (O10-T3 … O10-T5, O10-D):
   product-law composites have |S_CHSH| ≤ 2 whatever their correlations, while reaching non-separable tables (the
   obstruction is the Bell bound, not separability); a law not taking the first readout's setting cannot realize
   phiW; the law that does is forced to be the table's conditioning rule ψ_B = (s + aCᵀu)/(1 + a r·u), giving the exact
   composite with S(phiW) = 14/5 — CONDITIONAL on that law and on cnot given — and FAILED as a source (it reads the
   correlation block; phiW needs cnot, H2). Read against HO-13 v1 item 1 (CONDITIONAL): the re-preparing premise
   supplies H1 and the token invariances, not H2 or H3.
6. **Level two at the balanced angle** (O9-L2R, O9-L2C): `mixImage 2 (π/4)` with the exchanges generates the real
   Clifford group of two qubits (finite, 2304); with the kernel's single-state quarter phase the closure is
   {U ∈ U(4) : det(U)⁴ = 1} ⊇ SU(4). CONDITIONAL ([X] exact; [W]; [L] Cartan).
7. **`DenseUnitaryControl (fixedGateTheory (π/4))` is false, through level one** (O9-L1, O9-S): every unitary channel
   available at level one — by ancilla blocks and relabelling of members at every level and by every `InstAvail`
   protocol — is one of the 24 single-qubit Clifford channels. The theory has `DerivedOI` and `FixedGateSourced (π/4)`
   (DiscreteCompletion.lean:1929, :1933), so the hypothesis `Irrational (α / π)` of `denseUnitaryControl_of_fixedGate`
   (:1522) cannot be dropped at π/4: `fixedGateTheory (π/4)` is a natural countermodel to "DerivedOI ∧
   FixedGateSourced α ⇒ DenseUnitaryControl" at that angle. Scope (O9-E): at α = π/8 (also rational) the level-one
   clause holds; the obstruction belongs to angles where rot(α) is Clifford. CONDITIONAL ([W] NOTES-O9 §2, Claims 1–5;
   [X] L1a–L1f and the countercontrols; not kernel-checked).
8. **Correction of reading for HO-9 v1, item 7's may-not-assume clause** (O9-C): its conclusion (the predicate is not
   obtained at π/4) stands by item 7 above; its reason ("level one is finite") does not carry it, since level-one
   availability is not the level-one generated group. Assumption-watch marker: in a generated theory, availability at
   a level includes the blocks of every higher level and the protocols of `InstAvail`.

## 2. What a receiving thread may assume

Items 1–8 at their labels. Bridge: items 1 and 5 as constraints (the exclusive readout is not a source of SRC inside
the kernel's operational structure; no re-preparing pair law short of the cone's own conditioning rule realizes a
candidate cone). Equivalence: item 4 as an exact token model of HO-13 item 2 under the cosine law; item 7 for any use
of `DenseUnitaryControl` at the balanced angle. Countermodels: item 7's theory as a countermodel candidate at α = π/4.

## 3. What it may not assume

- that the exclusive readout, the re-preparing law, SRC or SPEC is sourced — all OPEN;
- kernel status for the [D] declarations of item 1–2 (design-run results) or for item 7 ([W] + [X]);
- that item 5's collapse-law composite sources a candidate cone (FAILED as a source);
- that item 7 says dense control needs α/π irrational (O9-E: false at π/8 for the level-one clause);
- that availability at a level equals the group generated at that level (item 8's marker);
- that the level-two or level-three density gives exactness (countable groups; `fixedGateTheory_not_qm`,
  DiscreteCompletion.lean:1948).

## 4. What would refute this proposal

- an `InstAvail` protocol of `fixedGateTheory (π/4)` realizing a non-Clifford unitary channel at level one (refutes
  item 7; the sanity scans of 80876 isometric blocks found none);
- a `FiniteOperationalTheory` in which `ExclusiveOn` holds on an algebra refining the ancilla value (contradicts item 1);
- a product-law composite with |S_CHSH| > 2, or a setting-free cross-token law reproducing phiW (contradicts item 5).

## 5. Evidence hashes (sha256)

| file | sha256 |
|---|---|
| `RESULTS.md` (rows through O9-E) | `51efa1143ab341f32e5ef79103e9ba4bd02c27a2d30574dac767c764bb74913a` |
| `NOTES-O8.md` | `a525f0fca18a7fbed1831aa272fd28ae0ebc29ba9b569010f22468fdef095474` |
| `NOTES-O10.md` | `fad4750d4f2e7d699360b6bcbb2fa45374fe37ebd30a49b09b16ec175e7c696e` |
| `NOTES-O9.md` | `e23c1a9436a2a06b563dc7c7b1d82b98761955a81a17d88b76d23df94682f5f5` |
| `lean/OriginExclusive.lean` (blob `28776414`) | `a8eb5802c9c6e7bd2164a3f1e0b5b55da4f4925e17930d4b4f848d9ad66869a8` |
| `o8_exclusive.py` / `.out` | `b85db1a7fff5e016197e299ab76b16cf651fa3a894320af00c6a48bfa5778a06` / `b1145dea863bd47f4e9a8cee34461ac1a5bdabc6a7032439561f95be3f0c4a96` |
| `o10_pair.py` / `.out` | `88d3ecc44bbb06cd2edb9b0f850ab48d0c786595a9205d553b59d3afeb60f122` / `48273387e487dcb2098367e539b4b43139243fa93dfdb7a7740a76897256ecbd` |
| `o9_level2.py` / `.out` | `bbb9016dcf492aa726f50586af92b44fb7c9408825acc9bf9852470bcab8ec4f` / `a4a5f47f39782dc1733d57f6fb7678036273dd55abc3bb0efba223331849ce29` |
| `o9_scope.py` / `.out` | `270affd686af1f0abf0bf0c5067d3ce3358dd2f93d46b1a5d9850a9d2663e362` / `0ca39f6ab23635fd5df392411c9d58d55b6b2dcb05a37414fd1511429a424d7b` |

Workflow runs (design evidence only): 38098314988 (dev commit `39fd0e67`, Mathlib bridge job 114348781009, Build
failure in `reach_mergeInto`, kept as the record of the first version) and 38099172719 (dev commit `5df964af`, job
114351335821, Build success, gate red only on `lean-manuscript`, `lean-axioms` PASS).
