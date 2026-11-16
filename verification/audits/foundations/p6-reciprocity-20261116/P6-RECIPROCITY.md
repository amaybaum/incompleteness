# P6 · Reciprocity under a specified invariant law

**Credit.** Conditional paper proof. The outcome is reciprocal probability flux under one invariant reference law, with equality of conditional transitions under the stated equal-weight condition. The conditional transition result supplies the mathematical reciprocity input to Stage 2(f) of Substratum Theorem 23 (P12(b)). Physical source **NOT PASSED**.

**Authority.** On 2026-11-16, owner `amaybaum` said “Sounds good, proceed as suggested” in the coordinating session. [Owner decision on #1169](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6912298340). The adopted recommendation is the ChatGPT review [relayed by `amaybaum` on 2026-11-16](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6912223025).

**Goal link (§A.47).** #1169, priority 2. Determine whether the reciprocity input to P12(b) has a conditional proof without total finiteness.

**Source pin.** `main` at `32322301e4b8c54f000560db73201260c63bf7f8`. SM, Main and Substratum are `papers/<name>.md`. Short Lean paths are relative to `verification/lean-mathlib/OIBridge/`. The [P6 row in the A1 recovery matrix](https://github.com/amaybaum/incompleteness/blob/06cede15037cfb12475d5459eb7f2f9d8abc861c/verification/audits/foundations/a1-recovery-matrix-20261116/RECOVERY-MATRIX.md#p6--reciprocity-on-a-measurable-carrier) supplies the proposed test. That reference and the decision records are provenance (§A.42 item 8). The proof is given here and needs no off-main mathematical result.

## 1. Small cases checked first

Use visible cells $A_i=\{X=i\}$ and compare $i\to j$ to $\theta j\to\theta i$. The check is whether a positive pair can have different masses under the complete invariant-law contract, and what fails when a condition is removed. Each example uses a single law fixed before the comparison. These are hand checks on specified mathematical models.

1. **Unequal starting weights.** Take $V=\{0,1\}$ and $H=\{a,b\}$. Give $(0,a),(0,b),(1,a),(1,b)$ masses $1/6,1/6,1/6,1/2$. Let $\varphi$ exchange $(0,a)$ and $(1,a)$ and fix the other states. With $\Theta=\mathrm{id}$, reversibility and both measure invariances hold. The flux in each direction is $1/6$. The starting masses are $1/3$ and $2/3$, so $P(X_1=1\mid X_0=0)=1/2$ and $P(X_1=0\mid X_0=1)=1/4$. This is a counterexample to unweighted reciprocity from invariant flux alone.
2. **Invariance under time reversal.** Take $V=\mathbb Z/3\mathbb Z$, $H=\{+1,-1\}$, $\varphi(i,s)=(i+s,s)$ and $\Theta(i,s)=(i,-s)$. They obey $\Theta\varphi\Theta=\varphi^{-1}$. A uniform visible law times hidden weights $3/4,1/4$ is $\varphi$-invariant because $\varphi$ permutes the visible labels at each fixed sign. It is not $\Theta$-invariant. The fluxes $0\to1$ and $1\to0$ are $1/4$ and $1/12$. For a control model on the same maps, take the single fixed hidden law with weights $1/2,1/2$. The reversal now preserves the law, and both fluxes are $1/6$. This check gives no counterexample under the complete product contract.
3. **Invariance under the dynamics.** Take $V=\{0,1\}$ and $H=\{a,b\}$ with uniform visible weights and hidden weights $3/4,1/4$. Let $\varphi$ transpose $(0,a)$ and $(1,b)$ and fix both other points. With $\Theta=\mathrm{id}$ the maps satisfy the reversal relation and the law is $\Theta$-invariant. $\varphi$ exchanges masses $3/8$ and $1/8$, so it does not preserve the law. These are the unequal paired fluxes. A fixed product law with equal visible weights and an invertible reversal are insufficient by themselves.
4. **Reversed labels.** On $V=\mathbb Z/3\mathbb Z$ with a singleton $H$, take $\varphi(i)=i+1$, $\Theta(i)=-i$ and the uniform law. All invariances hold. The $0\to1$ and $2\to0$ transitions both have probability $1$. The $1\to0$ transition has probability $0$. This checks why the result keeps the reversed labels when $\theta\ne\mathrm{id}$.

## 2. Fixed reference law and hypotheses

Let $(S,\mathcal S)$ be a measurable state space, $V$ a nonempty finite set of visible labels with the discrete sigma algebra, and $X:S\to V$ a measurable readout. Write $A_i=X^{-1}(\{i\})$. Supply one normalized probability law $\mu$ on $(S,\mathcal S)$ before choosing a starting cell, lag or run. Supply the following maps and conditions:

| Hypothesis | Mathematical and source status |
|---|---|
| A measurable carrier, the finite visible label set and measurable readout. | Inputs to the paper theorem. Main:46 supplies finite visible resolution for the framework. The measurable structure on a general carrier and the readout on that structure are specified model data. There is no condition on the total cardinality. |
| $\varphi$ is a bijection, and $\varphi$ and $\varphi^{-1}$ are measurable. | Hypothesis for the declared dynamics. SM:643 uses a bijection. `SecondOrderDrive.ruleDynamics` (SecondOrderDrive.lean:336–342) supplies a reversible second-order rule in the stated model interface, rather than general measurable or physical reversibility. |
| $\Theta$ is a measurable involution, $\theta$ is an involution of $V$, and $X\circ\Theta=\theta\circ X$. | Hypotheses on the chosen observation and reversal. The product form $T_m=\theta\times\theta_H$ with involutive components is the existing version (`Reciprocity.Tm`, `Tm_involutive`, Reciprocity.lean:42–61). Measurability and the cut must hold on the model to which the proof is applied. |
| $\Theta\varphi\Theta=\varphi^{-1}$. | Hypothesis in the general setting. SM:625–629 supports time reversal for the stated wave rule and spatial cut, and `Reciprocity.key` carries the conjugacy as an input. The identity for powers follows in the proof below. |
| $\mu(S)=1$ and, for every $E\in\mathcal S$, $\mu(\varphi^{-1}(E))=\mu(E)$ and $\mu(\Theta^{-1}(E))=\mu(E)$. | Hypotheses about the supplied law. A finite uniform law is preserved by permutations, as used in the counting case. For instance, `CanonicalMeasure.counting_invariant` (CanonicalMeasure.lean:205) is the finite reference-law result. Normalization and the two invariances are separate conditions for a general law. Physical selection of such a law is open under Q6. |
| The two conditioning masses $p_i=\mu(A_i)$ and $p_{\theta j}=\mu(A_{\theta j})$ are positive for the conditional comparison. To infer unweighted equality from positive flux, require $p_i=p_{\theta j}$. | This condition belongs to the unweighted conclusion. It is automatic in the specified product specialization below. The flux result holds with arbitrary cell masses. |

**Law for the Theorem 19 specialization.** Take $S=V\times H$ with the product sigma algebra, $X=\pi_V$ and $\Theta(i,h)=(\theta i,\theta_Hh)$ with $\theta_H$ a measurable involution on $H$. Supply one fixed normalized probability $\nu$ on $H$ with $\nu(\theta_H^{-1}(D))=\nu(D)$ for all measurable $D\subset H$. If $m=|V|$, the reference law is exactly $\mu=u_V\otimes\nu$, with
$$
\mu(E)=\frac{1}{m}\sum_{i\in V}\nu(E_i),\qquad E_i=\{h:(i,h)\in E\}.
$$
Thus $\mu(S)=1$ and $p_i=1/m$ for every $i$. The law is assumed $\varphi$-invariant on this product. The $\Theta$-invariance follows because the $i$-section of $\Theta^{-1}(E)$ is $\theta_H^{-1}(E_{\theta i})$. Its $\nu$-mass is $\nu(E_{\theta i})$, and summing over the permutation $\theta$ leaves the sum unchanged. This verifies the stated $\Theta$-invariance from the product assumptions. The law $\nu$ is the same in every visible cell and at every lag tested. Root conditioning means selecting an event of this one law, with no new draw of a reference law. Section 5 gives a concrete normalized $\nu$ and dynamics satisfying both invariances on an infinite carrier.

The product construction and $\nu$-invariance under $\theta_H$ are conditional model inputs. The natural finite reference in Main:54–60 and SM:641 is the uniform law on the chosen finite model. Main:728(iv) concerns measure selection for constructed realizations. Under [the Q6 decision](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6899511671), the specification here supplies mathematical hypotheses and leaves their realization in nature open.

## 3. Proof

For any integer $n\geq0$ define the measurable sets and masses
$$
E_{ij}^{(n)}=A_i\cap(\varphi^n)^{-1}(A_j),\qquad
J_{ij}(n)=\mu(E_{ij}^{(n)}).
$$
Here $J_{ij}(n)$ is the probability flux over $n$ steps, namely the joint mass of the starting cell $i$ and the ending cell $j$. Write
$$
T_{ij}(n)=P_\mu(X\circ\varphi^n=j\mid X=i)=J_{ij}(n)/p_i
\quad\text{when }p_i>0.
$$
These are lagged endpoint statistics of one law. No Markov condition or matrix-power rule for $T(n)$ is used.

**Trajectory reversal.** The identity $\Theta\varphi^n\Theta=\varphi^{-n}$ follows by conjugating each factor of the $n$th power and using $\Theta^2=\mathrm{id}$, including $n=0$. Set $R_n=\Theta\circ\varphi^n$. Then $R_n^2=\mathrm{id}$ and $\varphi^n R_n=\Theta$. For $x\in E_{ij}^{(n)}$, $X(R_nx)=\theta j$ and $X(\varphi^nR_nx)=\theta i$. The same rule applied to $\theta j\to\theta i$ sends it to $i\to j$, since $\theta^2=\mathrm{id}$. The involution therefore gives
$$
R_n(E_{ij}^{(n)})=E_{\theta j,\theta i}^{(n)}.
$$

**Probability mass.** Iterating invariance under $\varphi$ gives $\mu((\varphi^n)^{-1}(D))=\mu(D)$ for every measurable $D$. For every measurable $E$,
$$
\mu(R_n^{-1}(E))
=\mu((\varphi^n)^{-1}(\Theta^{-1}(E)))
=\mu(\Theta^{-1}(E))
=\mu(E).
$$
Taking $E=E_{\theta j,\theta i}^{(n)}$ gives
$$
J_{ij}(n)=J_{\theta j,\theta i}(n).
$$
This is reciprocal flux, with no restriction on the conditioning masses. Reversal invariance also gives $p_{\theta j}=p_j$, since $\Theta^{-1}(A_{\theta j})=A_j$. It does not equate the masses of arbitrary distinct visible cells. Invariance makes the set bijection preserve probability mass, the property that must replace finite cardinality.

**Conditional transitions.** With both roots positive, let $J$ denote the common paired flux. Then
$$
p_iT_{ij}(n)=p_{\theta j}T_{\theta j,\theta i}(n)=J.
$$
Equal root weights give equal transition probabilities by division by the common positive mass. In the other direction, for $J>0$, equality of the transitions implies $J/p_i=J/p_{\theta j}$ and hence equality of the weights. If $J=0$ and both roots are positive, both transitions are zero even with unequal weights. A zero-mass root supplies no conditional transition by this formula.

**Theorem 19 conclusion on the specified product law.** All roots have the same positive mass $1/m$, so $T_{ij}(n)=T_{\theta j,\theta i}(n)$ for every pair and every $n\ge 0$. For time-even visible cells ($\theta=\mathrm{id}$) this gives $T_{ij}(n)=T_{ji}(n)$. In the general case it gives the reversed-label equality proved above. The proof uses neither recurrence nor a limit over finite models.

## 4. Correspondence with the finite counting proof

In the product specialization, let $H_{ij}^{(n)}=\{h:X(\varphi^n(i,h))=j\}$. This is measurable by composition with the section $h\mapsto(i,h)$, and $E_{ij}^{(n)}=\{i\}\times H_{ij}^{(n)}$. The hidden component $F_{ij}^{(n)}(h)=\pi_H(R_n(i,h))$ is precisely SM:643's fibre map with the power $\varphi^n$. Its inverse on the target fibre is the corresponding reversed-pair map. For measurable $D\subset H_{ij}^{(n)}$, $R_n(\{i\}\times D)=\{\theta j\}\times F_{ij}^{(n)}(D)$ is measurable because $R_n$ is a measurable involution. Taking the $\theta j$-section makes $F_{ij}^{(n)}(D)$ measurable. Invariance on this image gives
$$
\frac{1}{m}\nu(F_{ij}^{(n)}(D))
=\mu(R_n(\{i\}\times D))
=\mu(\{i\}\times D)
=\frac{1}{m}\nu(D).
$$
The fibre map therefore preserves $\nu$-mass on the entire transition fibre and every measurable part of it. The common hidden law is used on **both** fibres.

| SM:643 proof step | Counting dependence and replacement |
|---|---|
| Reverse the trajectory and construct the inverse fibre map. | No counting is used. Reciprocity.lean:67–74 (`key`) and :79–103 (`count_reciprocity`) use the algebra above. The measurable proof checks the same map and both directions. |
| Count each hidden fibre and use its bijection to equate cardinalities. | `N` at Reciprocity.lean:50–53 counts a subset of `Finset.univ` using `Fintype H` (:40), and `count_reciprocity` uses `Finset.card_bij` (:82). The replacement is the measurable event mass comparison and the restricted-fibre equality above. |
| Divide by $\lvert\mathcal C_H\rvert$ to obtain transition probabilities. | `theorem_19` at Reciprocity.lean:129–137 divides the counts by the common finite cardinality. Here the flux is normalized by the root mass in the one law. For the specified product, this gives $T_{ij}(n)=\nu(H_{ij}^{(n)})$. With a nonempty finite $H$ and uniform $\nu$, this is exactly $\lvert H_{ij}^{(n)}\rvert/\lvert H\rvert$. The uniform product on finite $V\times H$ is invariant under both permutations. Multiplying the equality by $\lvert H\rvert$ recovers count equality in this finite case. The Lean count theorem does not require a finite visible type. Its denominator has a probability interpretation for nonempty $H$. |
| Apply the argument to every power and specialize to time-even cells. | `hT_pow` (Reciprocity.lean:105–124) needs no finite hidden type. Powers also preserve the same $\mu$. `detailed_balance` (:142–145) states the finite count equality when $\theta=\mathrm{id}$. The paper proof gives the corresponding probability equality under the stated root condition. |

## 5. One infinite model with an explicit law

Take $V=\{0,1\}$ and $H=\{(m,k):m\ge2,\ k\in\mathbb Z/m\mathbb Z\}$, both discrete. Define $\nu(\{(m,k)\})=2^{1-m}/m$, so the total mass of the $m$th layer is $2^{1-m}$ and the sum of these masses for $m\ge2$ is $1$. Use the uniform visible law times this fixed $\nu$. Let
$$
\varphi(i,m,k)=(i\oplus\mathbf 1_{\{k=0\}},m,k+1),
\qquad
\Theta(i,m,k)=(i,m,1-k),
$$
with $\oplus$ addition modulo two. The inverse is $\varphi^{-1}(i,m,k)=(i\oplus\mathbf 1_{\{k=1\}},m,k-1)$. Applying $\Theta\varphi\Theta$ gives the same formula, since $1-k=0$ in the layer at $k=1$. Both maps permute the states of each layer, where all point masses of $\mu$ are equal. Thus both preserve the specified law on the whole space. A common period would be divisible by every $m$ because $k$ advances by one in each layer. The compared transitions are nontrivial: at one step, the positive-mass sites with $k=0$ switch visible labels. This example verifies consistency of the hypotheses for an infinite mathematical carrier.

## 6. Standing for the reconstruction

P6 replaces the count-based reciprocity in SM:641–643 with a conditional probability result on the specified model. This addresses the reciprocity input at Substratum:167. The dynamics, partition-preserving reversal and invariant law must still be supplied on the *same* carrier used in P12(b). A law with unequal root weights can support the weighted flux statement and needs an additional justification for unweighted reciprocity. SM:647–649 gives a separate obstruction to inferring a time-reversal-invariant visible Hamiltonian from that reciprocity. The product-reference proof supplies neither a correlated energy-shell law for P7 nor a physical state selection under Q6. Physical application waits for a justification of the law and its invariances on the declared physical carrier. A1 is open and unadopted (Main:728(ii)). A4's finite periodic class remains the condition stated at Substratum:98. Physical source remains **NOT PASSED**.
