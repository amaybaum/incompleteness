# Prior-art comparison for the finite native-gate ball no-go (read-only)

Baseline `fdebc6e3`. Full texts are blocked in this environment (`arxiv.org`, `nature.com`, `iopscience`, `springer`).

Each entry is tagged with its verification status:
- **[owner]** — confirmed from the primary source by the owner;
- **[abstract]** — from the abstract or search snippet only;
- **[UNVERIFIED]** — details not checked.

## The result being compared

See `THEOREM.md`. For two locally tomographic d-ball systems (min ⊆ ⋯ ⊆ max), suppose an invertible `G` has:
- the classical CNOT frame action;
- both native NOT/CNOT relations, with **one** NOT involution `N` acting on both factors;
- `G` and `G⁻¹` both mapping product states into the max cone.

Then `d ∈ {1, 3}`.

Not required:
- connectedness;
- a continuous local group;
- `G² = I`;
- swap symmetry;
- normalization;
- an invariant intermediate cone.

## Comparison

| work | local dynamics | global dynamics | CNOT | conclusion | relation to this result |
| --- | --- | --- | --- | --- | --- |
| **Krumm & Müller 2019**, npj QI 5, 7 (arXiv:1804.05736) | full local `SO(d)` [owner] | closed **connected** matrix group; disconnected components explicitly disregarded [owner] | not assumed [owner] | d ≠ 3 ⇒ only local transformations (their Thm 1) [owner] | Different hypothesis profile. Here: weaker local assumption (one finite NOT), no connectedness, but a specific native gate algebra. Covers the discrete-component regime their framework sets aside. Not "stronger than", not contained in. |
| **Masanes, Müller, Augusiak, Pérez-García 2014**, J. Math. Phys. 55, 122203 | continuous reversible local and global dynamics | continuous reversible interaction | not assumed | for ball systems, interaction ⇒ d = 3 [abstract; premises UNVERIFIED in full] | Continuity is essential there. Here no continuity is used anywhere. |
| **Al-Safi & Richens 2015**, NJP 17, 123001 (arXiv:1508.03491) | general, incl. d-dimensional hyperballs | reversible dynamics on **maximally nonlocal** composites (the max tensor product) | — | reversible dynamics trivial (local ops + permutations of subsystems) for local spaces meeting a dichotomy criterion, including hyperballs [abstract] | Their composite is fixed to be max. Here the composite is unspecified between min and max. Their snippet notes a classical-CNOT analogue exists for **reducible** local spaces; balls are irreducible. Different setting; no overlap in hypotheses. |
| **Barnum & Wilce 2014**, Found. Phys. 44, 192 (arXiv:1202.4513) | Jordan-algebraic systems (spin factors included) | natural composites (non-signalling) | — | locally tomographic + Jordan + at least one qubit ⇒ complex QM with superselection [abstract] | Assumes Jordan structure and a qubit system outright. Here: only ball kinematics and a finite gate algebra; no Jordan product assumed, no qubit assumed. |
| **Barnum, Graydon & Wilce**, composites of EJAs (arXiv:1606.09331) | Euclidean Jordan algebras | categories of composites | — | constraints on composites of EJAs [abstract; details UNVERIFIED] | Jordan-structural route, a different assumption base. |
| **Gross, Müller, Colbeck & Dahlsten 2010**, PRL (boxworld) | gbits (square state spaces) | maximally nonlocal composites | — | all reversible dynamics trivial [known; UNVERIFIED here] | Polytope analogue of the Al-Safi–Richens line; not ball-based. |

## Provisional novelty statement

> The result is not contained in the connected-reversibility ball theorems (Krumm–Müller; Masanes et al.). It
> addresses the discrete-component regime those frameworks explicitly set aside, using only a finite native gate
> algebra (one NOT involution and a CNOT) and two-sided positivity on products. No exact prior theorem of this form
> was found in this search. That is not a global novelty claim.

**Before any external use:**
- read the full texts (Krumm–Müller §§ on assumptions and any remark on discrete gates; MMAP's premises; Al-Safi–Richens'
  CNOT construction for reducible spaces);
- search once more for "discrete gates on ball GPTs" and "stabilizer-like ball theories". This needs owner access or a
  network policy allowing arXiv.

Search sources used here:
- [Krumm–Müller, npj QI](https://www.nature.com/articles/s41534-018-0123-x), [arXiv:1804.05736](https://arxiv.org/abs/1804.05736);
- [Al-Safi–Richens, IOP](https://iopscience.iop.org/article/10.1088/1367-2630/17/12/123001), [arXiv:1508.03491](https://arxiv.org/abs/1508.03491);
- [Barnum–Wilce, Springer](https://link.springer.com/article/10.1007/s10701-014-9777-1), [arXiv:1606.09331](https://arxiv.org/pdf/1606.09331).
