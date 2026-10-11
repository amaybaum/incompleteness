# HO-17 (v1) — origin → bridge, equivalence, countermodels: the exclusive readout refuted on the stated access; the pair half of SRC not supplied by any re-preparing law; `DenseUnitaryControl` false at the balanced angle

**From** `research/origin` (round 3, nodes O8, O10, O9). **To** `research/bridge` (items 1, 3, 5), `research/equivalence`
(items 4, 6, 7, 8) and `research/countermodels` (item 7). Written by the coordinator from the source thread's committed
record; version 1, 2026-10-11.

## Statements and labels

1. **The exclusive readout as a premise is OI-N1's factor property, and the stated access refutes it** (O8-T1 … O8-T3,
   O8-V). In every `FiniteOperationalTheory` over a nonempty system the native readout is the kernel's block pinching
   of the ancilla values (`readout_is_localLuders` [K OperationalAssembly.lean:658]), a passive repeatable instrument on
   every algebra whose blocks do not straddle two ancilla values; the exclusivity clause relative to such an algebra
   (`ExclusiveOn`: every available passive instrument on the algebra has a state-independent outcome law there) is false
   there, and in the substratum theory, where every ancilla point mass is preparable (`pureSeedPrep_available_of_swap`
   [K :675]). Holding it on an algebra forces a block straddling two ancilla values (coherence between ancilla values);
   on a factor it holds in every theory (OI-N1). Cost: it contradicts `readout_is_localLuders` with the structure field
   `readout_avail` (:642). Label: CONDITIONAL ([D] `not_exclusiveOn_of_refines`, `exists_straddle_of_exclusiveOn`,
   `exclusiveOn_factor`, `substratumTheory_exclusivity_false` in run 38099172719, 33/33 prints standard; the kernel facts
   CERTIFIED at the cited lines).
2. **Any nontrivial cell suffices on any finite carrier** (O8-T4): with every permutation available, one passive readout
   of any cell `C`, `∅ ≠ C ≠ Ω`, reaches every point mass from the uniform state — the general form of O5-T1a.
   CONDITIONAL ([D] `reach_pointMass`; [X] closures `C(2N−1, N)` for `N ≤ 5`; independently confirmed for `N ≤ 4`).
3. **Disguise test of the premise** (O8-D): it passes the owner's letter; it fails on the kernel's carrier (it
   presupposes the coherence it was to source); on the knowledge-balance toy it is the observation-side equivalent of
   the balanced mixer, and the witness numbers `(1, 1/2)` do not detect it (memory erasure reproduces them).
   CONDITIONAL ([X] + [W]).
4. **HO-13's token pair on one re-preparing token** (O10-T1, O10-T2): on the Kochen–Specker sphere tower `cyc3` acts
   with the exact witness `(1, 1/2)` for the body's own frame dephasing, and the tower's stage-crossing datum is HO-13's
   frame-axis rotation `R_z(θ₀)`, `cos θ₀ = 3/5`; the circle tower carries neither. CONDITIONAL on the cosine
   re-preparation law (outside the stated access; false there by item 1).
5. **The pair half is not supplied by any re-preparing law short of the cone's own** (O10-T3 … O10-T5, O10-D):
   product-law composites have `|S_CHSH| ≤ 2` whatever their correlations, while reaching non-separable tables (the
   obstruction is the Bell bound, not separability); a law not taking the first readout's setting cannot realize
   `phiW`; the law that does is forced to be the table's conditioning rule `ψ_B = (s + aCᵀu)/(1 + a r·u)`, giving the
   exact composite with `S(phiW) = 14/5` — CONDITIONAL on that law and on `cnot` given — and FAILED as a source (it
   reads the correlation block; `phiW` needs `cnot`, H2). Read against HO-13 item 1: the re-preparing premise supplies
   H1 and the token invariances, not H2 or H3.
6. **Level two at the balanced angle** (O9-L2R, O9-L2C): `mixImage 2 (π/4)` with the exchanges generates the real
   Clifford group of two qubits (finite, order 2304); with the kernel's single-state quarter phase the closure is
   `{U ∈ U(4) : det(U)⁴ = 1} ⊇ SU(4)`. CONDITIONAL ([X] exact, independently reproduced; [W]; [L] Cartan).
7. **`DenseUnitaryControl (fixedGateTheory (π/4))` is false, through level one** (O9-L1, O9-S): every unitary channel
   available at level one — by ancilla blocks and relabelling of members at every level and by every `InstAvail`
   protocol — is one of the 24 single-qubit Clifford channels. The theory has `DerivedOI` and `FixedGateSourced (π/4)`
   (DiscreteCompletion.lean:1929, :1933), so the hypothesis `Irrational (α / π)` of `denseUnitaryControl_of_fixedGate`
   (:1522) cannot be dropped at `π/4`: `fixedGateTheory (π/4)` is a countermodel to "`DerivedOI ∧ FixedGateSourced α` ⇒
   `DenseUnitaryControl`" at that angle. Scope (O9-E): at `α = π/8` (also rational) the level-one clause holds; the
   obstruction belongs to angles where `rot(α)` is a Clifford element. CONDITIONAL ([W] NOTES-O9 §2 Claims 1–5, read by
   the coordinator against the kernel's definitions; [X] L1a–L1f, the level-one group, the unit columns and the
   four-square counts independently reproduced; not kernel-checked).
8. **Correction of reading (O9-C)** for HO-9 v1, item 7's may-not-assume clause: its conclusion (the predicate is not
   obtained at `π/4`) stands by item 7; its reason ("level one is finite") does not carry it, since level-one
   availability is not the level-one generated group. Assumption-watch marker: in a generated theory, availability at a
   level includes the ancilla blocks of members at every level (`MixR.block`, `MixR.relabel`) and the protocols of
   `InstAvail`. HO-9 v2 carries the corrected clause.

## Evidence

| item | pointer |
|---|---|
| source | `research/origin` @ `de9285d6` (round-3 commits `6240576b` … `de9285d6`) |
| proposal | `research/origin/handoff-proposals/O8-O10-O9-round3-findings.md`, sha256 `b38f75916cb0446174945039d91418775a6e6729cf587cc6039431ad8ffc330f` |
| results | `research/origin/RESULTS.md` sha256 `51efa1143ab341f32e5ef79103e9ba4bd02c27a2d30574dac767c764bb74913a` (rows O8-K … O9-E); `NOTES-O8.md` `a525f0fca18a7fbed1831aa272fd28ae0ebc29ba9b569010f22468fdef095474`; `NOTES-O10.md` `fad4750d4f2e7d699360b6bcbb2fa45374fe37ebd30a49b09b16ec175e7c696e`; `NOTES-O9.md` `e23c1a9436a2a06b563dc7c7b1d82b98761955a81a17d88b76d23df94682f5f5` |
| scripts, outputs | `o8_exclusive.py` `b85db1a7fff5e016197e299ab76b16cf651fa3a894320af00c6a48bfa5778a06` / `.out` `b1145dea863bd47f4e9a8cee34461ac1a5bdabc6a7032439561f95be3f0c4a96`; `o10_pair.py` `88d3ecc4…` / `.out` `48273387…`; `o9_level2.py` `bbb9016d…` / `.out` `a4a5f47f…`; `o9_scope.py` `270affd6…` / `.out` `0ca39f6a…` (all replayed byte-identically); full list `research/AUDITS/2026-10-11-round3/EVIDENCE-HASHES.txt` |
| design module | `research/origin/lean/OriginExclusive.lean` sha256 `a8eb5802c9c6e7bd2164a3f1e0b5b55da4f4925e17930d4b4f848d9ad66869a8`; `dev-origin/exclusive` @ `5df964af` (run 38099172719: Build success, 33/33 prints standard, `lean-axioms` OK 5893, gate red only on `lean-manuscript`); first version @ `39fd0e67` (run 38098314988, Build failure in `reach_mergeInto`, kept) — `research/AUDITS/2026-10-11-round3/CI-RUNS-R3.md` |
| coordinator audit | replays 4/4; `indep_checkO3.py` run 2 7/7 (the order 2304 and the Pauli normalization, the trace `(3+i)/2` and the commutant dimensions 2/3 with a third prime, the 192-element level-one group with 24 channels from two independent constructions, the four-square counts, the `π/8` scope, `phiW`'s `14/5` and the Bell-local entangled table, the closures `C(2N−1, N)`); the O9 written argument read against the kernel definitions; 32/32 citations at L — `research/AUDITS/2026-10-11-round3/AUDIT-ORIGIN-R3.md` |

## What the receiving threads may assume

Items 1–8 at their labels. **Bridge:** items 1, 3 and 5 as constraints — the exclusive readout is not a source of SRC
inside the kernel's operational structure, and no re-preparing pair law short of the cone's own conditioning rule
(with `cnot` given) realizes a candidate cone; SPEC's target is unchanged. **Equivalence:** item 4 as an exact token
model of HO-13 item 2 under the cosine law; items 6–7 for any use of `DenseUnitaryControl` at the balanced angle; item 8
as a marker for any availability argument over `genTheory`. **Countermodels:** `fixedGateTheory (π/4)` as a countermodel
candidate at `α = π/4` for the density implication, at item 7's label.

## What they may not assume

- that the exclusive readout, the re-preparing law, SRC or SPEC is sourced — all OPEN;
- kernel status for the [D] declarations of items 1–2 (design-run results) or for item 7 ([W] + [X]);
- that item 5's collapse-law composite sources a candidate cone (FAILED as a source);
- that item 7 says dense control needs `α/π` irrational (false at `π/8` for the level-one clause);
- that availability at a level equals the group generated at that level (item 8);
- that the level-two or level-three density gives exactness (countable groups; `fixedGateTheory_not_qm`,
  DiscreteCompletion.lean:1948).

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-17 v1` and records in its `LOG.md`
whether and how it relies on it.
