# P0 locality sources, correction 1 (2026-10-16): what the tick cone rests on

Append-only correction, raised in owner review of the locality assessment (decision 4). `RULES.md`, the amendment,
`RESULT.md`, `p0_ls_exact.py` and its output are unchanged.

## The defect

`RESULT.md` L1 says: "The tick cone rests on the rule's dependency structure (`Rule.dep`), together with A3 and the
nearest-neighbour stipulation". §5 attributes locality of the dynamics to "the spatial constitution (A3,
nearest-neighbour range, site factorization)".

The kernel theorem does not use A3 or the nearest-neighbour range. `iterate_dependsOnlyOn_ball`
(RegionTower.lean:283) has two hypotheses:

- a configuration type `ι → Q`, which is a site factorization with one local alphabet;
- a `CouplingGraph φ` (RegionTower.lean:254): any assignment `nbhd : ι → Finset ι` such that each site's next value
  depends only on its neighbourhood (`local_dep`).

Neither hypothesis bounds a degree or fixes a graph. On a finite site set, `nbhd i = univ` is a coupling graph for every
rule, so the theorem holds for every update of a product configuration space.

## The corrected statement

The light-cone theorem is a theorem relative to a coupling graph. Given a site factorization and a coupling graph of the
rule, after `k` ticks a function of the sites of `A` depends only on the `k`-ball of `A` in that graph, and an
intervention outside that ball leaves the readout unchanged (`readout_unaffected_outside_ball`, :304).

A3 and the nearest-neighbour range are not needed for this graph-theoretic dependency result. They give it content of
two further kinds:

- A3, in family form, gives the balls bounded growth across the family of finite representatives. At a single finite
  lattice it is automatic (`a3_of_fintype`, SubstratumInterfaceAudit.lean:115).
- Identifying the balls with lattice neighbourhoods, one tick to one lattice spacing on the simple-cubic graph, needs
  further spatial structure: the nearest-neighbour range, with the site factorization it is stated in.

This strengthens the conditional mathematical result: its hypotheses are weaker than L1 stated.

## What it bears on

- **L1's classification stands.** Locality of the dynamics is adopted, not derived. What changes is which adopted
  inputs the cone itself consumes: site factorization and a coupling graph read from the rule.
- **§5's parenthetical** reads, corrected: site factorization and a coupling graph for the cone; A3, in family form, for
  bounded growth; the nearest-neighbour range for lattice neighbourhoods.
- **L2–L4 and every recorded token are unchanged.** The cuts they use are cuts of the rule's coupling graph.
- **The ledger observation under L1** is taken up in the manuscript corrections of #851. These add site factorization,
  A3 in family form, the nearest-neighbour range, A4 and A6 to the posit ledger as items (viii)–(xii), and withdraw
  SM §2.4's factorization-uniqueness theorem. That theorem's LEDGER **GAP**, cited under L1, is retired there.

**Classification:** ELABORATING. This is a sharper attribution of the cone's premises, not a new gap.
