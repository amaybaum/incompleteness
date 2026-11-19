# Equal weights on the energy-two shell

**Goal link (§A.47).** For E27 (equal finite-shell weights), determine whether active exchangeability of the four boundary bits forces the weights on this cut and whether an independently specified preparation supplies that symmetry. [Accountable issue #1373](https://github.com/amaybaum/incompleteness/issues/1373)

**Scope.** Keep the update, visible cut, identity reversal and independent deep law of P7-B §5. At total energy two in units of the bit gap, compare normalized swap-invariant laws on the ten finite configurations. The checks are the two visible masses, both crossing fluxes and one-step conditional probabilities, their oriented ratio, and the existing stationary reweighting with the same physical data. The physical question concerns the source of the preparation and of the measurement. [P7-B §5](../../../../audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md#L154)

**Provenance.** The owner authorized this paper-only unit. The ranking nominated the question. The on-main model and counterexample at `5704fc484a3a3e187185dbf9ea16c7797bbd571c` supply the scientific starting point. [Owner decision](https://github.com/amaybaum/incompleteness/issues/1367#issuecomment-6972185820) · [Nomination in #1368](https://github.com/amaybaum/incompleteness/pull/1368)

## Which law is forced?

Let $i$ be the visible bit and $b=(b_1,b_2,b_3,b_4)$ the boundary bits. Each occupied bit has energy $\delta>0$. The finite shell is $P=\{(i,b):i+|b|=2\}$. The update $s$ interchanges $i$ and $b_1$. On the full shell $P\times\mathbb N_0$ it fixes the zero-energy coordinate $d$, and time reversal is the identity. Write the preparation as $w\otimes\nu$, where $w$ is a probability on $P$ and the fixed independent deep law has $\nu(d)=2^{-(d+1)}$.

**Proposition.** Among preparations with $w(sx)=w(x)$, active exchangeability of the boundary bits is equivalent to $w(x)=1/10$ on $P$. Active exchangeability means $w(i,b)=w(i,\pi b)$ for every permutation $\pi$ of the four boundary positions, with the preparation and the labels held fixed.

**Proof.** Boundary permutations act transitively on the six two-element supports of $b$ at $i=0$, and on the four one-element supports at $i=1$. Each point in the first cell therefore has the same mass $a$, and each point in the second has the same mass $c$. The swap takes $(0,1100)$ to $(1,0100)$, so stationarity gives $a=c$. Then $6a+4c=1$ gives $a=c=1/10$. Conversely the uniform law is invariant under every boundary permutation and the swap. Strict positivity follows from normalization and these symmetries. The equal weights belong to the finite factor. Each full atom has mass $\nu(d)/10$. $\square$

## One-step law and stationary counterexample

Write $p_i$ for the visible mass, $J_{ij}$ for the joint probability of seeing $i$ and then $j$ one step later, and $T_{ij}=J_{ij}/p_i$. In the finite factor, three configurations cross in each direction. They have $(i,b_1)=(0,1)$ or $(1,0)$ and exactly one occupied bit among $b_2,b_3,b_4$. The swap pairs them. The other configurations are fixed, three in cell 0 and one in cell 1.

Give the three fixed states in cell 0 weight $\alpha$ each, the fixed state in cell 1 weight $\beta$, and each of the six crossing states weight $\gamma$, all positive. The normalization is $Z=3\alpha+\beta+6\gamma$. The weights are constant on swap orbits, so this whole P7-B family is stationary for the same update, energy, cut, reversal and deep law. Summing the weights gives $p_0=(3\alpha+3\gamma)/Z$, $p_1=(\beta+3\gamma)/Z$ and $J_{01}=J_{10}=3\gamma/Z$. Thus $T_{01}/T_{10}=p_1/p_0$. [P7-B §5, invariant laws](../../../../audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md#L160)

| Weights $(\alpha,\beta,\gamma)$ | $p_0$ | $p_1$ | $J_{01}$ | $J_{10}$ | $T_{01}$ | $T_{10}$ | $T_{01}/T_{10}$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $(1,1,1)$ | $3/5$ | $2/5$ | $3/10$ | $3/10$ | $1/2$ | $3/4$ | $2/3$ |
| $(2,1,1)$ | $9/13$ | $4/13$ | $3/13$ | $3/13$ | $1/3$ | $3/4$ | $4/9$ |

In the second row $(0,0110)$ has weight $2/13$ and $(0,1010)$ has weight $1/13$. Interchanging $b_1,b_2$ relates these configurations of equal energy. Even agreement with the entire first row would leave exchangeability undecided. Starting at the uniform law, transfer any mass $0<\varepsilon<1/10$ between two fixed states in cell 0. This preserves stationarity and every visible quantity in the table while breaking exchangeability.

## Source of the symmetry

A passive renaming carries the update and the law along with the labels. An active permutation compares occupations assigned by the same law. Interchanging $b_1,b_2$ before the update makes the old $b_2$ visible. Interchanging them afterwards leaves the old $b_1$ visible. Repeating the update preserves each orbit's initial mass. P7-B posits the counting-product preparation in H4 and §6.4. Main distinguishes stationarity on an orbit from maximum-entropy selection among orbits and calls the latter an epistemic postulate. Neither source gives a preparation history that produces active exchangeability on this cut. [P7-B H4](../../../../audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md#L35) · [P7-B §6.4](../../../../audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md#L191) · [Main, Lemma 3](../../../../../papers/Main.md#L54) · [Main, item (iv)](../../../../../papers/Main.md#L728)

At $2\delta$ the proposition replaces E27 by an equivalent symmetry within the stationary class. The finite weights still require one unsourced preparation premise, and the independent deep law is a separate input. E27 on the other shells requires a law there. The reference calculation fixes both the conditional laws and the relative shell populations by choosing one full-carrier law before conditioning. The ratio $2/3$ concerns one finite gap. Infrared detector calibration further requires identifying the detector channels and their gap dependence. [P7 reference shell §1](../../../../audits/foundations/p7-shell-calibration-20261116/P7-SHELL-CALIBRATION.md#L16) · [GR on the detector comparison](../../../../../papers/GR.md#L74)

Physical use requires an independently justified preparation or heralding history on this cut that entails exchangeability without using the target weights. An observer-controlled operation requires a physical implementation. Turning the specified readout $i$ into a measured result also requires a detector coupling, a retained outcome and resources to repeat the measurement. This conditional paper derivation is submitted for independent review under #1373. Physical measurement sourcing remains **NOT PASSED**. [Operational requirements](../o-acc-native-record-20261117/O-ACC.md#L104)
