# Handoff proposal O5-O7-R2 — round-2 findings of `research/origin` for the coordinator

From: `research/origin` (thread branch, the commit of this file). To: the coordinator, for the bridge and
equivalence threads and the overview. Status: proposal only; nothing here is adopted, governed or certified beyond
the kernel declarations cited at their lines. Evidence: `NOTES-O5.md`, `NOTES-O6.md`, `NOTES-O7.md`, RESULTS rows
O5-…, O5-SRC…, O6-…, O7-…, scripts `o5_kbd`, `o5_src`, `o6_tower`, `o7_density` (exact, replayed byte-identically),
design module `lean/OriginPassive.lean` (dev-origin/passive @ c2484cca, workflow run 38091462366, Build green, standard
axioms; not certified).

## 1. Statements, with labels

1. **KB-D splits; the native readout excludes its exclusivity** (O5-T1, O5-T1a, O5-KB1). The KB-D instrument is the
   native Lüders readout composed with a forgetful map; the toy bit's octahedron needs in addition that no passive
   readout of any partition be available, and one passive readout of any of the 14 nontrivial partitions restores
   the simplex. Sharpened Lemma P: passive repeatable readouts make every extreme state outcome-deterministic, and
   point masses under separation. CONDITIONAL ([W] + [X]; [D] `extreme_cellMass_det`, `extreme_pointMass_of_passive`;
   kernel facts CERTIFIED: OperationalAssembly.lean:658 `readout_is_localLuders`, :675 `pureSeedPrep_available_of_swap`).
2. **Candidate sources of KB-D closed** (O5-a, O5-b; O5-d CONDITIONAL). A memory bound gives knowledge-balanced
   posteriors under linear dynamics but not the disturbance (frequencies V = 0); the kernel recorder is passive on
   the system or erases to a known value; symplectic couplings force KB-D's form only with unknown pointer
   conjugates, which is the exclusivity relocated.
3. **Passive towers: finite rank and an infinite-order datum exclude each other** (O6-T1). Every reversible datum,
   stage-crossing or not, has finite order on the completed chart body of a passive repeatable finite-rank tower.
   CONDITIONAL ([W] tower step; [D] `finiteOrderOn_chartBody_of_binary`, composed with landed TransitiveBody and
   CompletionAction lemmas). Relevant to HO-8's K∞-Drive and K∞-Trans targets: neither is reachable on a passive
   finite-rank tower.
4. **The three requirements of O3-T5 hold together on an invasive re-preparing tower** (O6-I): circle and sphere
   substrata with the cosine (Kochen–Specker) re-preparation law; rank 3 / 4, an infinite-order stage-crossing datum,
   OFF on the sphere, repeatable readout, exact witness for a closure member. CONDITIONAL on the re-preparing law
   (outside the stated access).
5. **One premise for both targets** (O6-V): the field-neutral Continuous Origin and the source of KB-D are the same
   open premise — an exclusive measure-and-re-prepare readout. Assumption-watch marker.
6. **SRC via KB-D is token-only** (O5-SRC1, O5-SRC2): it makes J = cyc3 available on one token as a configuration
   permutation with the exact witness, while every product-register composite of such tokens is Bell-local
   (|S| ≤ 2 exactly), so it realizes no candidate pair cone (HO-3). For HO-5 item 6: SRC from KB-D cannot serve
   SPEC's target.
7. **Density at the balanced angle** (O7-D1 … O7-D4, O7-C): on three states the kernel's `rot(π/4)` on overlapping
   pairs is dense in SO(3); the Hadamard pair (the audit's X5) is infinite dihedral, closure a copy of O(2); with the
   exchanges both close to O(3); with the quarter phase the closure contains SU(3). Reading note for X5: its
   infinite-order value is correct; density does not follow from it for reflections.

## 2. What a receiving thread may assume

Items 1–7 at their labels. In particular: the bridge may use item 6 as a constraint (a KB-D-type token source does not
reach any candidate cone through product registers); the equivalence thread may use item 3 as a constraint on
sourcing K∞-Drive / K∞-Trans through classical conditioning towers.

## 3. What it may not assume

- that KB-D, the re-preparing law, or SRC is sourced — all OPEN;
- kernel status for any item beyond the cited landed declarations; the [D] declarations are design-run results.

## 4. What would refute this proposal

- a passive repeatable finite-rank tower with an infinite-order datum (contradicts item 3);
- a premise at L that removes the native readout's availability on the classical carrier (would re-open item 1);
- a product-register composite of KB-D tokens with |S| > 2 (contradicts item 6's exact check).
