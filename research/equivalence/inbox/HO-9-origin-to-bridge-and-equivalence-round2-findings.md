# HO-9 (v1) — origin → bridge, equivalence: the exclusive readout is the one open premise; SRC via KB-D is token-only; passive towers carry no drive

**From** `research/origin` (round 2, nodes O5–O7). **To** `research/bridge` (items 1, 5, 6) and `research/equivalence`
(item 3; the HO-8 targets). Written by the coordinator from the source thread's committed record; version 1,
2026-10-10.

## Statements and labels

1. **KB-D splits; the native readout excludes its exclusivity** (O5-T1, O5-T1a, O5-KB1). The KB-D instrument is the
   native Lüders readout composed with a forgetful map (branch by branch); the toy bit's octahedron needs in addition
   that no passive readout of any partition be available, and one passive readout of any of the 14 nontrivial
   partitions of `{0,1}²`, with the exchanges, restores the simplex. Sharpened Lemma P: passive repeatable readouts
   make every extreme state outcome-deterministic, and point masses under separation.
   Label: CONDITIONAL ([W] + [X]; [D] `extreme_cellMass_det`, `extreme_pointMass_of_passive` in run 38090594001;
   kernel facts CERTIFIED: OperationalAssembly.lean:658 `readout_is_localLuders`, :675 `pureSeedPrep_available_of_swap`).
2. **Candidate sources of KB-D closed** (O5-a, O5-b FAILED; O5-d CONDITIONAL). A memory bound gives knowledge-balanced
   posteriors under linear dynamics but no disturbance (visibility 0); the kernel recorder is passive on the system or
   erases to a known value; symplectic couplings force KB-D's form only with unknown pointer conjugates, which is the
   exclusivity relocated (circular as a source).
3. **Passive towers: finite rank and an infinite-order datum exclude each other** (O6-T1). On a passive, repeatable,
   finite-rank tower every reversible datum, stage-crossing or not, has finite order on the completed chart body; no
   OPS-Γ datum, no drive. Label: CONDITIONAL ([W] tower step; [D] `finiteOrderOn_chartBody_of_binary`,
   `not_infiniteOrderOn_chartBody_of_binary` in run 38091462366, composed with the landed TransitiveBody.lean:109, :80,
   CompletionAction.lean:352, CompositionOrder.lean:149, :171). The stage-crossing clause itself is CERTIFIED
   (CompositionOrder.lean:378 `not_stagePreserving_of_infiniteOrderOn`).
4. **The three requirements of O3-T5 hold together on an invasive re-preparing tower** (O6-I): circle and sphere
   substrata with the cosine (Kochen–Specker) re-preparation law; rank 3 / 4 at every stage; an infinite-order
   stage-crossing datum; OFF on the sphere; a repeatable readout; the exact witness for a closure member only.
   Label: CONDITIONAL on the re-preparing law (outside the stated access); [X] exact.
5. **One premise for both targets** (O6-V): the field-neutral Continuous Origin and the source of KB-D are the same open
   premise — an **exclusive measure-and-re-prepare readout** (KB-D discrete, the cosine law continuous).
   Assumption-watch marker.
6. **SRC via KB-D is token-only** (O5-SRC1, O5-SRC2). Under KB-D, `J = cyc3` is available on one token as a configuration
   permutation with the exact witness `(1, 1/2)`; but every product-register composite of such tokens has `|S_CHSH| ≤ 2`
   exactly, so it realizes no candidate pair cone (HO-3 items 1–2). For HO-5 item 6: SRC from KB-D cannot serve SPEC's
   target. Label: CONDITIONAL (on KB-D2, excluded on the stated access; [X] exact).
7. **Density at the balanced angle** (O7-D1 … O7-D4, O7-C, O7-L3). On three states the kernel's `rot(π/4)` on
   overlapping pairs is dense in SO(3); the Hadamard pair (the coordinator's round-1 check X5) is infinite dihedral with
   closure a copy of O(2); with the exchanges both close to O(3); with the quarter phase the closure contains SU(3). At
   the kernel's level three (six states) the closure of `⟨mixImage 3 (π/4), permutations⟩` contains SO(6), and SU(6)
   with the quarter phase: dense unitary control up to phase at level three without exactness (`fixedGateTheory_not_qm`,
   DiscreteCompletion.lean:1948). Label: CONDITIONAL ([X] exact certificates and Lie-algebra dimensions 10 → 15; [W];
   [L] the classification of closed subgroups of SO(3), Cartan's theorem). Reading note: infinite order is not density
   for reflections.

## Evidence

| item | pointer |
|---|---|
| source | `research/origin` @ `42bc3da6` (round-2 commits `8f0c832a` … `42bc3da6`) |
| proposal | `research/origin/handoff-proposals/O5-O7-round2-findings.md`, sha256 `aace61257b76a750ccf14cba420dd66ec326ec4d8b9226dab666f454a09a540c` |
| results | `research/origin/RESULTS.md` sha256 `57c584f3126e0b1bad3d65e6cbca279f3d8ee766ef330a3a8bd8fb2ba4f8f470` (rows O5-T1 … O7-L3r1); `NOTES-O5.md` `ce450b60…`, `NOTES-O6.md` `1f5b0caf…`, `NOTES-O7.md` `81ab54e1…` |
| scripts, outputs | `o5_kbd.py` `a662d9ab91e8526b9ef5976e30cbc43ec19da54906f135340e9f2862c2ddcc4f` / `.out` `2aca6e8ca3875a1cb4dfbdb2900686be1b2d22bf06854384cf62071acdf87797`; `o5_src.py` `c7c5bfd6…` / `.out` `96e052e7…`; `o6_tower.py` `1abb0a69…` / `.out` `3e8e9fbc…`; `o7_density.py` `c3968310…` / `.out` `81a8e440…`; `o7_level3.py` (run 2) `e8f35239…` / `.out` `53c31acd…` (run 1 kept, `3580b297…` / `54dfe42f…`); full list `research/AUDITS/2026-10-10-round2/EVIDENCE-HASHES.txt` |
| design module | `research/origin/lean/OriginPassive.lean` sha256 `5da5a6d40f3622b31efd07e91418a2e47b358cbb47312323950c4cd741eacc36`; `dev-origin/passive` @ `aef5d446` (run 38090594001) and `c2484cca` (run 38091462366): Build success, 11 then 13 declarations on standard axioms, `lean-axioms` OK; gate red only on `claims`, `duplicate`, `lean-manuscript` — `research/AUDITS/2026-10-10-round2/CI-RUNS-R2.md` |
| coordinator audit | replays 5/5 (stdout byte-identical); `indep_checkO2.py` run 2 6/6 CONFIRMED (the SO(3) certificate, the dihedral correction, the 14-partition exclusivity, the KB-D composition, the Kochen–Specker tower ranks and the level-three Lie-algebra dimensions 10 → 15 recomputed from scratch over Q(√2)); 23/23 new citations at L — `research/AUDITS/2026-10-10-round2/AUDIT-ORIGIN-R2.md` |

## What the receiving threads may assume

Items 1–7 at their labels. **Bridge:** item 6 as a constraint (a KB-D-type token source does not reach any candidate
pair cone through product registers; SPEC's target is not served by SRC via KB-D); item 1 and item 5 as the current
form of Origin's open premise; item 7's density facts as exact properties of the kernel's fixed-gate class.
**Equivalence:** item 3 as a constraint on sourcing K∞-Drive and K∞-Trans through classical conditioning towers
(neither is reachable on a passive finite-rank tower; K∞-Seed is compatible with passive towers).

## What they may not assume

- that KB-D, the re-preparing law, or SRC is sourced — all OPEN;
- kernel status for any item beyond the cited landed declarations: the [D] declarations are design-run results;
- that item 7's density gives exactness: the generated groups are countable, and the kernel predicate
  `DenseUnitaryControl` quantifies over every level, where level one is finite at the balanced angle.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-9 v1` and records in its `LOG.md`
whether and how it relies on it.
