# A1-07 · P7 energy and state source

**SOURCE GAP at the energy check.** The existing four-site A4 cut has active boundary–deep coupling and a conserved modular quadratic. The traced sources leave open a conserved real energy for that same finite update with an independently justified interpretation as horizon energy. State selection and relative weights across two energy windows therefore remain at the next step. Physical source remains **NOT PASSED**. [Finite and real wave energies][sm-energy] · [GR shell assumption][gr-shell]

**Authority and goal.** On 2026-11-16, the owner (amaybaum) said “Proceed with A1-07.” Codex is the sole writer of the paper-only check under #1325. The unit tests the energy and state input to P7 at P12(b) Stage 3, without adopting total finiteness A1. The drafting snapshot is main at 0283ba315e8c8a8f1465a91eea8613f9aa213ab5. A1-03 supplied the planning basis for the successor. [Owner authorization][owner] · [Rule 0 pin][pin] · [A1-03 planning provenance][a103] · [Substratum Stage 3][stage3]

## Pinned existing cut

The Physical C4 Discharge round's RD6 instance fixes a rank-one periodic lattice with four sites, binary alphabet and coupling coefficient $\alpha=1$. It uses the visible region $V=\{0\}$ and reads that site's previous and current field values. The boundary range in GR then identifies the hidden boundary $B=\{1,3\}$ and the deep set $D=\{2\}$. Both boundary sites read site 2 with coefficient $1$ in the actual finite update. The underlying wave rule has exact translation symmetry and its next-value rule uses neighbours' present values and the site's previous value, as required for the two senses of A4. RD6 is a specified finite test representative. Its source explicitly limits its standing to that model and cut. [RD6 cut and scope][rd6] · [Existing update and readout][toy] · [Wave rule and A4 symmetry][wave] · [A4 statement][a4] · [GR coupling split][gr-cut]

For the previous and current slices $(u,v)$, the fixed update is $U(u,v)=(v,Av-u)$ with $(Av)_i=v_{i-1}+v_{i+1}$ in $\mathbb Z/2\mathbb Z$ and indices in $\mathbb Z/4\mathbb Z$. Reversal swaps the two slices at every site. It preserves the spatial cut and swaps the two components of the visible readout. The second-order circuit source supplies the swap and shear involutions and the inverse in reverse order. [Update][toy] · [Reversal and inverse][circuit]

## Energy evidence at this cut

| Candidate or requirement | Existing evidence | Disposition for RD6 |
| --- | --- | --- |
| Quadratic of the exact finite rule | SM gives conservation of $Q(u,v)=u\cdot u+v\cdot v-u\cdot Av$ for symmetric $A$ over $\mathbb Z/q\mathbb Z$. The equation and arithmetic in the RD6 source give this rule at $q=2$. The later orbit-period bound in SM has its own $p\nmid L$ hypothesis. [SM exact linear rule][sm-energy] · [RD6 update][toy] | The source verifies a modular invariant of the full coupled update. A physical interpretation of the two residue labels as energies, with physical units and the boundary interaction accounted for, would require additional evidence. |
| Real-valued quadratic | SM and the cycle audit give the conserved quadratic for the unrestricted real-valued lift. At this cut's comparator parameters $d=1$, $L=4$, $\alpha=1=1/d$, the real quadratic is positive semidefinite with the constant and staggered null modes. The positive-definite branch requires $\lvert\alpha\rvert<1/d$. [SM real lift][sm-energy] · [Cycle audit, real lift][cycle] | The real-energy statement is sourced for the real lift. A map or independent conservation statement for a physical real energy on the binary update is still needed. |
| Energy in the horizon first law | GR's shell calculation assumes a conserved shell and identifies its energy with the horizon first-law energy. The hidden-fibre count also uses negligible boundary interaction at that scale. GR §8.7 explicitly identifies the shell as an assumption beyond the reversibility and measure result. The earlier W1-1 record flags this same energy identification. [GR H-count][gr-count] · [GR shell assumption][gr-shell] · [W1-1 energy prerequisite][w1] | The traced sources do not identify the finite invariant or the real-lift quadratic with the physical first-law energy on the pinned cut. The treatment of its actual boundary interaction belongs to that missing identification. |

The stop is the link from the sourced finite dynamics to a physically interpreted $E:\operatorname{Conf}_{\rm RD6}\to\mathbb R$ conserved under that dynamics. The evidence needed is a source for that observable and its conservation, including the attribution of interaction and hidden energy relevant to the horizon first law. The verdict is confined to the pinned cut and the sources traced here.

The state step depends on that energy source. Once it is supplied, the unit would need a preparation or selection rule on the same model that yields a normalized law invariant under $U$ and reversal and fixes the relative weights of two energy windows. The readback example's uniform prior belongs to its own stated setup. A1-07 terminates at the energy check. [Issue scope and controls][issue] · [RD6 setup][toy-intro]

**Evidence checked.** The trace uses the maintained manuscript, the RD6 cut and rule, and the existing energy audits. Repository searches for conserved energy, the real lift and the boundary–deep cut found the adjacent source records. The energy check applies the cited results at their stated scope to RD6.

[issue]: https://github.com/amaybaum/incompleteness/issues/1325
[owner]: https://github.com/amaybaum/incompleteness/issues/1325#issuecomment-6915996921
[pin]: https://github.com/amaybaum/incompleteness/issues/1325#issuecomment-6916060015
[a103]: https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6914802462
[stage3]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/papers/Substratum.md#L177-L185
[a4]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/papers/Substratum.md#L98
[rd6]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/verification/programmes/physical-realization/round-c4-1-physical-discharge/result.md#L292-L320
[toy]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/verification/lean/physical_c4_toy_instance_probe.py#L60-L90
[toy-intro]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/verification/lean/physical_c4_toy_instance_probe.py#L15-L21
[circuit]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/verification/lean-mathlib/OIBridge/SecondOrderCircuit.lean#L57-L122
[wave]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L159-L208
[gr-cut]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/papers/GR.md#L116-L128
[gr-count]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/papers/GR.md#L58-L60
[gr-shell]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/papers/GR.md#L695
[sm-energy]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/papers/SM.md#L290-L298
[cycle]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/verification/audits/manuscript/intro-corpus-audit-20261026/tracks/SC34-cycle-ergodicity/README.md#L9-L24
[w1]: https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/verification/programmes/physical-realization/w1-1-20261112/W1-1-REPORT-r4.md#L126-L141
