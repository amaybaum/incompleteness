# SUMMARY of NLCAND-r4: one non-linear candidate, the SM ring rule

**The candidate.** The ring rule of `papers/SM.md`:112, as written: each cell adds its left and right
neighbours and subtracts its own previous value, mod `q`; if the right neighbour holds `0`, it reads the
cell two to the right instead. It is a complete, reversible update.
**The manuscript's, and what was chosen.** The manuscript gives the update, the ring, the special value `0`
and the jump of two. It gives no `d = 3` version of this rule, no edge longer than two cells, and no list of
the configurations in its reference class. Chosen here: the uniform law, a three-cell observer, one declared
ready cell, labels in two cells, one-cell setting generators, and the zero-free configurations (`K_nz`) as
the reference class.
**Preserved results.** Survive: reversibility, the second-order kernel layer, `S ⇔ D ⇔ Q_fb`, the cone lemma
and Bell ceiling (on this rule's own graph), centre independence, time reversal. Only on `K_nz`: the
nearest-neighbour graph, wave-rule form and dispersion. Break: shift covariance, reflection covariance, the
linear rule's quadratic invariant. Undetermined: every `d = 3` result. The list is not a complete inventory.

**Control.** Two record conventions are kept apart: H, a wing keeps the complete history of its cells; S, it
reads their state at one time (`papers/Main.md`:369–372). A label can switch a read on and off, which is not
a translation: supplied, under H and S. The kernel no-go on mixing does not take the rule as input, so it
does not test this candidate. The single-qubit target is undecided.

**Bell.** For the member: not supplied at lattice scale. For the rule: not established.
- H and S: no dependence outside the rule's own cone (two cells per tick one way, one the other), and
  Bell-local there under measurement independence (ledger item (xiv)). With adjacent blocks, the ready cell
  and label `0`, the member reads the remote setting two cells away after one tick; this is the same gated
  read counted as control.
- H only: with one unread cell between the blocks the member's record law shifts with the remote setting
  (total variation `1/q`; CHSH at most `2 + 2/q`), and one-cell records give a no-signalling PR-type table.
  Under S both effects are absent at one tick.
- Whatever speed is taken as physical, the member has no dependence outside the cone or it signals outside
  it. Wings many cells apart are undecided.

**Cell supply.** Under the uniform law no bijective rule supplies known cells unconditionally; a herald that
fixes `M` slots is accepted with probability at most `q^{−M}`. Orbit and record-compatible laws: undecided.

**Joint.** The member is not shown to meet the three requirements, and for Bell it has a derived defect at
lattice scale. It is not shown that no completion of the ring rule can meet them.

**About the non-linear class.** Shown only for this member. Not shown: anything about the rounded rule of
`papers/SM.md`:294, a longer switched edge, a `d = 3` version, H-Bell, other observers or laws,
long-wavelength behaviour, or non-linear rules as a class.

**Status.** Paper-only, hand derivations; a non-author model review of r1, its confirmation of r2, and an
exact-head confirmation of r3; r4 itself is unreviewed; not independently verified. H-nl (TUNE-1's hypothesis
that the world's rule is the rounded rule of `papers/SM.md`:294) and H-ring (that it is this ring rule) are
different hypotheses, both named and unadopted. No computation is proposed.
