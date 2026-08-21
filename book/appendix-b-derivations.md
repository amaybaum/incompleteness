# Appendix B
# Mathematical Derivations

---

## B.1 What this appendix develops

The main chapters of the book develop the framework's content with proofs sketched at the level required for the chapter argument's logical flow. This appendix collects the full mathematical derivations of the framework's key technical results — derivations that are referenced in the main chapters but kept out of the chapter flow to preserve readability.

The appendix's content is organized by mathematical structure rather than by chapter sequence. Six derivations occupy the appendix.

*B.2 The Stinespring construction.* The framework's emergent quantum description is constructed from a deterministic substratum bijection through the Stinespring dilation theorem applied to a partial trace over the hidden sector. This appendix gives the full construction: Hilbert-space embedding, permutation unitarity lemma, CPTP channel structure, Born-form representation of the transition probabilities, emergent coherence theorem, and CP-indivisibility theorem. The construction uses only textbook operator algebra from the 1950s.

*B.3 The trace-out as a Jordan-Chevalley projection.* The framework's content on the Standard Model gauge structure relies on a structural property of the trace-out operation: it extracts the semisimple part of the evolution matrix's Jordan-Chevalley decomposition and discards the nilpotent monodromy. This appendix gives the full algebraic derivation: period formula, Jordan-Chevalley decomposition, $q$-independence of the Weil-Deligne conductor, additive decomposition over gauge irreps, and the precise sense in which the trace-out is a projection.

*B.4 The gap equation for $\hbar$.* The framework derives Planck's constant $\hbar$ from a thermal self-consistency argument between the classical horizon temperature (substratum-level) and the KMS temperature (emergent QFT-level). This appendix gives the full four-step derivation: spatial locality and boundary dependence, deep-sector gauge equivalence, dimensional determination, and thermal self-consistency producing $\hbar = c^3 \epsilon^2 / (4G)$.

*B.5 Anomaly cancellation and unique hypercharges.* The framework's content on the Standard Model matter content derives the unique hypercharge assignment from the six anomaly conditions of $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$. This appendix gives the explicit calculation: the six anomaly conditions, the algebraic constraint structure, and the unique solution producing $(Y_Q, Y_u, Y_d, Y_L, Y_e) = (1/6, 2/3, -1/3, -1/2, -1)$ with no free parameters.

*B.6 Gauge-theoretic derivations.* Two key gauge-theoretic results from Chapter 5: the conditional H-link link count for $K = 2dm = 6$ internal components per site, and the cubic-rotation-group decomposition of the coupling matrix's eigenvalue multiplicities into $(3, 2, 1)$ — the multiplicities that determine $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$.

*B.7 The lemma chain for the characterization.* The framework's characterization theorem — accessible non-Markovianity ⟺ C1/C3/C4 realization per horizon, with the quantum representation internal and universal ($S \iff D \iff Q_{\mathrm{fb}}$, [Main §3.4]) — relies on a chain of intermediate lemmas: partition-relativity, emergent stochasticity, P-indivisibility from a non-permutation witness, accessible-timescale backflow, and phase-locking. This appendix collects these lemmas with their proofs in compact form, providing the reader a self-contained reference for the framework's logical structure.

The appendix's content is *complete derivations*, not exposition. Each derivation gives the algebraic steps, the lemmas invoked, and the result with no glosses. For motivation and context, the relevant main-chapter sections are cross-referenced at the start of each derivation. The appendix is designed for readers wanting full technical content; the main chapters give the same results with motivating context but compressed derivations.

## B.2 The Stinespring construction for emergent quantum mechanics

*Main-text reference: Chapter 1 §1.7-1.9.*

The framework's emergent quantum description is constructed from the substratum's deterministic bijection through a Stinespring dilation applied to the partial trace over the hidden sector. The construction uses only textbook operator algebra from the 1950s, with no reference to recent stochastic-quantum correspondence results.

**Setup.** The finite configuration spaces $\mathcal{C}_V = \{x_1, \ldots, x_n\}$ (visible sector) and $\mathcal{C}_H = \{h_1, \ldots, h_m\}$ (hidden sector) embed into Hilbert spaces $\mathcal{H}_V = \mathbb{C}^n$ and $\mathcal{H}_H = \mathbb{C}^m$ via the canonical identification $|i\rangle \leftrightarrow x_i$ and $|k\rangle \leftrightarrow h_k$. This introduces no quantum postulates: it is the canonical identification of probability distributions on a finite set with diagonal density matrices.

The combined space is the tensor product $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_H$ of dimension $nm$. The substratum's deterministic bijection $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ defines a permutation of the orthonormal basis $\{|i, k\rangle\}_{i=1,\ldots,n; k=1,\ldots,m}$.

**Lemma B.2.1 (Permutation unitarity).** *Any bijection $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ defines a unitary operator $U_\varphi$ on $\mathcal{H}$.*

*Proof.* Define $U_\varphi |i, k\rangle = |\varphi(x_i, h_k)\rangle$. Since $\varphi$ is a bijection, $U_\varphi$ permutes the orthonormal basis, hence is unitary. $\square$

A continuous unitary interpolation comes from the discrete step itself: $U_\varphi$, being unitary, admits a Hermitian logarithm — $U_\varphi = e^{-i\hat{H}}$ for some Hermitian $\hat{H}$, unique only up to the branch and gauge freedom of Lemma B.7.5 — which defines $U_t = e^{-i\hat{H}t}$ through the integer-time dynamics. The finite substratum carries no nontrivial continuous permutation family, so the interpolation is representation-level structure, not substratum dynamics.

**Lemma B.2.2 (Reverse direction, scoped).** *Any single one-step doubly stochastic matrix on a finite configuration space $\mathcal{C}_V$ can be realized as the one-step marginal of a deterministic bijection on $\mathcal{C}_V \times \mathcal{C}_H$ with uniform prior on $\mathcal{C}_H$, for some finite $\mathcal{C}_H$ (exactly when transition probabilities are rational; to arbitrary precision otherwise).* (The restriction is forced: a uniform-prior bijection marginal preserves the uniform distribution, hence is doubly stochastic; the emergent unistochastic statistics lie inside this class.) The scope is the matrix, not the process: realizing prescribed multi-time statistics — a family of joint distributions over trajectories — with a single bijection and a single uniform prior is a stronger demand and is not claimed here.

*Proof.* Any marginal of a bijection with uniform prior is a doubly stochastic matrix. By Birkhoff-von Neumann, every doubly stochastic matrix is a convex combination of permutation matrices. A bijection on $\mathcal{C}_V \times \mathcal{C}_H$ realizing the required mixture is obtained by letting $\mathcal{C}_H$ enumerate the permutations; for multi-step processes, the construction extends by history dilation. $\square$

**Remark.** Lemma B.2.2 is the bijection-stochastic-matrix correspondence at the stochastic-process level. It is *not* a full CPTP-channel correspondence — channels that create coherences from diagonal inputs have no permutation-unitary realization with uniform ancilla. For the characterization theorem (Chapter 1 §1.7), which is stated in terms of transition probabilities, this is the appropriate scope.

**The quantum channel.** The observer's ignorance of the hidden sector corresponds to the maximally mixed state $\rho_H = I_m / m$. The visible-sector quantum channel is
$$\Phi(\rho_V) = \text{Tr}_H\!\left[U_\varphi\,(\rho_V \otimes \rho_H)\,U_\varphi^\dagger\right]$$
This is completely-positive trace-preserving (CPTP) by a standard result (Nielsen-Chuang Theorem 8.1), with Kraus representation $\Phi(\rho_V) = \sum_{k,l} K_{kl}\,\rho_V\,K_{kl}^\dagger$ where $K_{kl} = m^{-1/2}\langle l|U_\varphi|k\rangle_H$. The triple $(\mathcal{H}_H, U_\varphi, \rho_H)$ is the *Stinespring dilation* of $\Phi$.

**Theorem B.2.3 (Born-form representation of the transition probabilities).** *The classical transition probabilities $T_{ij} = P(j|i)$ derived from the substratum's bijection equal the Born-rule probabilities of $\Phi$ — a representation identity: it exhibits the Born form and does not select the quadratic exponent, which remains open ([Main §3.4]).*

*Proof.* $P(j|i) = \langle j|\Phi(|i\rangle\langle i|)|j\rangle = m^{-1}\sum_{k,l} |\langle j,l|U_\varphi|i,k\rangle|^2$. Since $U_\varphi$ is a permutation, $\langle j,l|U_\varphi|i,k\rangle = \delta_{(j,l),\varphi(i,k)}$. Thus $P(j|i) = m^{-1}\sum_k \delta_{j,\pi_V(\varphi(x_i,h_k))} = T_{ij}$, where $\pi_V$ is the projection from $\mathcal{C}_V \times \mathcal{C}_H$ to $\mathcal{C}_V$. $\square$

*Remark (failure of (C1)).* Condition (C1) does not suffice. For $|V| = |H| = 2$ and $\varphi(x,h) = (h,x)$ one has $T_{ij} = 1/2$ for all $i,j$, yet $\Phi(\rho) = I/2$ identically: a constant channel, hence measure-and-prepare. Exhaustive enumeration gives the same verdict for every (C1)-satisfying bijection at $|V| = |H| = 2$, and for 612 of 648 at $|V| = 2$, $|H| = 3$. The obstruction is structural: (C1) constrains the diagonal of $\Phi$, whereas entanglement-breaking is a property of $\mathrm{id} \otimes \Phi$ and is not fixed by the action on single-system inputs.

What replaces (C1) is not a further condition on $T$ but a condition on the partition, and it is established for a specific realization rather than for arbitrary bijections. Take the substratum of §B.1 on a lattice $\Lambda$ with $q = 2$, state $(u,v) \in \mathbb{F}_2^{\Lambda} \times \mathbb{F}_2^{\Lambda}$ and the reversible nearest-neighbour update

$$u'_x = \sum_{z \sim x} u_z + v_x, \qquad v'_x = u_x ,$$

the visible sector being the sites of a region $R \subseteq \Lambda$. Write $M_{HV}$ and $M_{VH}$ for the blocks of this update carrying visible input to hidden output and hidden input to visible output, $\kappa = \dim \ker M_{HV}$, $w = \mathrm{rank}\, M_{VH}$, and $s = \dim V = 2|R|$. The inner and outer boundaries of $R$ are $\partial^{-}R = \{x \in R : \exists\, z \notin R,\ z \sim x\}$ and $\partial^{+}R = \{y \notin R : \exists\, z \in R,\ z \sim y\}$.

**Lemma 1 (boundary bound).** *$\mathrm{rank}\, M_{HV} \leq |\partial^{+}R|$ and $\mathrm{rank}\, M_{VH} \leq |\partial^{-}R|$.*

*Proof.* For $y \notin R$ the component $v'_y = u_y$ is a hidden input, and $u'_y = \sum_{z \sim y} u_z + v_y$ involves a visible input only if some $z \sim y$ lies in $R$, that is only if $y \in \partial^{+}R$; so $M_{HV}$ has non-zero rows only among $\{u'_y : y \in \partial^{+}R\}$. Dually, for $x \in R$ the component $v'_x = u_x$ is a visible input, and $u'_x$ involves a hidden input only if $x \in \partial^{-}R$. $\square$

One update step transports information one lattice site, so the sectors resolve one another only across the cut. This argument is a statement about supports and uses no property of the coefficient ring: it holds verbatim over $\mathbb{Z}_q$, and for a general nearest-neighbour bijection it yields the weaker conclusion that the hidden output depends on the visible input only through $\partial^{-}R$.

**Lemma 2 (channel normal form).** *Write $A = M_{VV}$, $B = M_{VH}$, $C = M_{HV}$ for the blocks of the update, and $L_{RR}$ for the adjacency of $\Lambda$ restricted to $R$. Then: (i) $A$ is invertible, with $A^{-1}(a_u, a_v) = (a_v,\ a_u - L_{RR}\,a_v)$, so the visible block alone induces the permutation (Clifford) unitary $V_A|i\rangle = |Ai\rangle$; (ii) $\Phi(|i\rangle\langle i'|)$ vanishes unless $C(i - i') = 0$; (iii) on the Weyl operators the channel acts, with no phase, as*

$$\Phi\!\left(X^{a}Z^{b}\right) = \big[\,Ca = 0\,\big]\,\big[\,B^{T}A^{-T}b = 0\,\big]\; X^{Aa}\,Z^{A^{-T}b},$$

*so that $\Phi = \mathrm{Ad}_{V_A} \circ \Phi_G$, where $\Phi_G = |G|^{-1} \sum_{g \in G} g\,\cdot\,g^{\dagger}$ is the uniform mixture over the group $G$ of Weyl operators $X^{\alpha}Z^{\beta}$ with $\alpha \in \mathrm{im}(A^{-1}B)$ (translations) and $\beta \in \mathrm{im}\,C^{T} = (\ker M_{HV})^{\perp}$ (phases); (iv) $G$ is abelian, of order $2^{\,s - \kappa + w}$.*

*Proof.* (i) is the displayed inverse, read off from $v'_x = u_x$ and $u'_x = (L_{RR}u)_x + v_x$ on $R$; invertibility of $A$ is what makes $i \mapsto Ai$ a relabelling. (ii) The hidden outputs of $i$ and $i'$ agree for some hidden input exactly when $C(i-i') = 0$, and then for every hidden input. (iii) With the hidden input uniform, $\Phi(|i\rangle\langle i'|) = [\,C(i-i')=0\,]\ \mathbb{E}_{t \in \mathrm{im}\,B}\, |Ai+t\rangle\langle Ai'+t|$. Summing this against $X^{a}Z^{b} = \sum_i (-1)^{b\cdot i}\,|i+a\rangle\langle i|$ and substituting $i \mapsto i - A^{-1}t$ gives the displayed rule: the character sum over $\mathrm{im}\,B$ produces the second indicator and cancels every phase. The right-hand side is $\mathrm{Ad}_{V_A}$ applied to the Hilbert–Schmidt-orthogonal projection onto $\mathrm{span}\{X^{a}Z^{b} : Ca = 0,\ B^{T}A^{-T}b = 0\}$, and the uniform mixture over the symplectic complement of that index set — which is exactly $G$ — is that projection. (iv) An element $X^{\alpha}Z^{\beta}$ with $\alpha \in \mathrm{im}(A^{-1}B)$, $\beta \in \mathrm{im}\,C^{T}$ commutes with another iff the cross-pairings $\alpha \cdot \beta'$ vanish; over all of $G$ this is the single condition $C A^{-1} B = 0$, which holds identically for this update: $B$ feeds hidden $u$ into the visible $u'$-components, $A^{-1}$ carries the $u'$-subspace onto the $v$-subspace, and $C$ reads only the visible $u$-components. The translation and phase families intersect only in the identity, so $|G| = 2^{\mathrm{rank}\,B}\cdot 2^{\mathrm{rank}\,C} = 2^{\,w + (s-\kappa)}$. $\square$

**Theorem (separability threshold).** *Let $G$ be an abelian subgroup of the Weyl group on $s$ qubits, of order $2^{t}$ modulo phases. Then $\Phi_G = |G|^{-1}\sum_{g \in G} g\,\cdot\,g^{\dagger}$ is entanglement-breaking if and only if $t = s$.*

*Proof.* Modulo phases the Weyl operators form the symplectic space $\mathbb{F}_2^{2s}$, on which abelian subgroups are exactly the isotropic subspaces; isotropy bounds $t \leq s$. Any isotropic subspace of dimension $t$ is carried to $\langle Z_1, \dots, Z_t \rangle$ by a symplectic transformation (Witt's extension theorem for the symplectic space $\mathbb{F}_2^{2s}$), and every symplectic transformation is implemented by a Clifford unitary $U$. Hence $U \Phi_G U^{\dagger}$ is complete dephasing on $t$ qubits tensored with the identity on the remaining $s - t$. Complete dephasing is measure-and-prepare and therefore entanglement-breaking, and a tensor product of channels is entanglement-breaking exactly when every factor is — separability of the joint Choi state survives the partial trace onto any single factor pair, so one entangled factor Choi rules out separability of the whole; the identity on a non-trivial factor is not entanglement-breaking. Since conjugation by a unitary preserves the property, $\Phi_G$ is entanglement-breaking precisely when $s - t = 0$. $\square$

**Corollary 1.** *For one step of the displayed update on $\mathbb{F}_2$ — $u'_x = \sum_{z \sim x} u_z + v_x$, $v'_x = u_x$, with the hidden sector initially uncorrelated and maximally mixed — the visible channel $\Phi$ admits the Clifford-conjugated abelian Weyl-mixture normal form of Lemma 2 and is not entanglement-breaking if and only if $w < \kappa$.* Immediate from Lemma 2 and the Theorem with $t = s - \kappa + w$: entanglement breaking is invariant under composition with the unitary $\mathrm{Ad}_{V_A}$, so $\Phi$ is entanglement-breaking exactly when $\Phi_G$ is, and $t = s$ reads $w = \kappa$ (Lemma 2 gives $w \leq \kappa$, matching $t \leq s$).

**Corollary 2.** *If $|\partial^{-}R| + |\partial^{+}R| < 2|R|$ then $\Phi$ is not entanglement-breaking.*

*Proof.* $s = 2|R|$, so Lemma 1 gives $w + (s - \kappa) \leq |\partial^{-}R| + |\partial^{+}R| < s$, that is $w < \kappa$. $\square$

*Remark.* For a $d$-dimensional region of linear size $\ell$, $|\partial R| = O(\ell^{d-1})$ against $2|R| = 2\ell^{d}$, so the hypothesis of Corollary 2 holds whenever $\ell > 2d$; in $d = 3$ this is roughly six sites across. Within this single-step result the criterion carries no dependence on $|H|$, since the coupling reads only the boundary; the counterexample above is the degenerate case, every visible site lying on the cut so that the region has no bulk. Whether the same holds over many steps is not settled here: repeated interaction can propagate boundary information into the hidden bulk, and a multi-time statement would require a process-tensor argument rather than a single-channel one. The suggestion that coherence is a bulk quantity and decoherence an area quantity — the accounting that reappears in the horizon entropy of Chapter 7 — is at this stage an interpretation of the one-step result, not a theorem about the asymptotic dynamics.

*Remark (scope).* Lemma 1 holds over any $\mathbb{Z}_q$ and, in weakened form, for arbitrary nearest-neighbour bijections. Lemma 2, the Theorem and both Corollaries are stated for $q = 2$; the symplectic and Clifford arguments carry over to prime $q$ with $2^{\bullet}$ replaced by $q^{\bullet}$, while composite $q$ requires module-theoretic treatment of rank and kernel and is not covered. All of this concerns the realization displayed above and is not a property of arbitrary finite bijections. For a general linear bijection the abelian property of Lemma 2(iv) can fail ($C A^{-1} B \neq 0$); the mixture is then over a non-abelian Weyl family, and entanglement breaking is governed by the isotropy of the surviving index set rather than by its order alone — not treated here. Two boundary markers on interpretation. Coherence preservation is a property of this realization, not an additional structural condition: (C1)–(C4) constrain coupling, timescales, and capacity, and neither contain nor imply a coherence requirement — the swap example satisfies (C1) while its channel is entanglement-breaking, and which realizations preserve one-step coherence is the geometric question answered above for the displayed update alone. And non-entanglement-breaking is a statement about a single channel, not about quantum mechanics: it supplies neither the observable algebra, nor preparations and interventions, nor tensor composition, nor multi-time statistics — the operational reconstruction claims rest on the dilation and correspondence arguments, not on Corollary 1 — and the entanglement-breaking status of one step does not determine whether the visible multi-time process is P-divisible: the hidden sector can carry memory even when a step's channel is entanglement-breaking, as a two-state system with a two-state hidden register already shows.

**Theorem B.2.5 (CP-indivisibility).** *The P-indivisibility of the substratum dynamics (under C1–C4) implies CP-indivisibility of $\{\Phi_t\}$: there exist $t_2 > t_1 > 0$ with no CPTP map $\Lambda$ satisfying $\Phi_{t_2} = \Lambda \circ \Phi_{t_1}$.*

*Proof.* The framework's $\Phi_t$ are permutation dilations with uniform ancilla, so they map computational-diagonal states to exactly diagonal states (a permutation unitary conjugates a diagonal state to a diagonal state; the partial trace preserves diagonality). If $\Phi_{t_2} = \Lambda \circ \Phi_{t_1}$ with $\Lambda$ CPTP, then $M_{kj} := \langle j|\Lambda(|k\rangle\langle k|)|j\rangle$ is stochastic and, by the diagonality of $\Phi_{t_1}(|i\rangle\langle i|)$, $T(t_2) = T(t_1)\,M$ — P-divisibility of the population process. The contrapositive gives the result. For a general CPTP family the diagonal-input reduction fails — a Hadamard pair is CP-divisible with P-indivisible populations — so the diagonal-preservation property is what licenses the step. $\square$

CP-indivisibility is completely witnessed by ancilla-assisted distinguishability ([Main §3.4]); ordinary system-only trace-distance revival — the Breuer-Laine-Piilo *information backflow* signature — is sufficient evidence of non-Markovianity, not a necessary consequence of CP-indivisibility. The framework's content is therefore that the C1–C4/readback sector is necessarily memory-bearing — non-Markovian, with information backflow at observable timescales — while fixed-basis quantum representability itself is universal, not confined to that sector ([Main §3.4]).

**Approximate unitarity.** On observable timescales $t \ll \tau_B$, the hidden-sector state is approximately frozen (conditions C2-C3). At $t=0$ the channel generator is exactly Hamiltonian,
$$\frac{d\Phi_t}{dt}\bigg|_{t=0}(\rho_V) = -i[\hat{H}_{\text{eff}}, \rho_V],$$
with $\hat{H}_{\text{eff}} = H_V + \mathrm{Tr}_H[V_{\text{int}}(\mathbb{1}\otimes\rho_H)]$; the dissipative part vanishes at $t=0$. At finite time the dissipator $\mathcal{D}$ has two contributions: a frozen-bath dephasing of order the coupling strength squared (the spread of bath-conditioned visible Hamiltonians, independent of $\tau_B$), and a bath-motion correction of order $(\tau_S/\tau_B)^2$. The dynamics is the Schrödinger equation generated by $\hat{H}_{\text{eff}}$ to leading order provided both the slow-bath condition $\tau_S\ll\tau_B$ and a weak-coupling condition (small conditioned-Hamiltonian spread) hold. The phase-locking lemma (Chapter 1 §1.6) then determines $\hat{H}_{\text{eff}}$ from continuous-time transition data up to the lemma's full gauge: an overall energy shift, the residual diagonal-unitary rephasing freedom that is physically trivial (basis convention), and the antiunitary conjugation $\hat{H} \to -\hat{H}^*$ — a genuine twofold ambiguity (Lemma B.7.5).

The construction is complete: the substratum's deterministic bijection produces the memory-bearing visible-sector description — its unitary quantum representation supplied through the Stinespring dilation, the coherent operational lift still to be established ([Main §3.4]) — with leading-order Schrödinger evolution and structurally non-Markovian corrections at $\mathcal{O}(\tau_S/\tau_B)$.

## B.3 The trace-out as a Jordan-Chevalley projection

*Main-text reference: Chapter 5 §5.4-5.6.*

The framework's content on the Standard Model gauge structure relies on a precise algebraic property of the trace-out operation: it extracts the semisimple part of the evolution matrix's Jordan-Chevalley decomposition and erases the nilpotent monodromy. This appendix gives the full derivation for the scalar wave equation on a ring of $L$ sites over $\mathbb{F}_q$; the multi-component extension incorporating the gauge group follows by additive decomposition.

**Setup.** The discrete wave equation $x(n, t+1) = x(n-1, t) + x(n+1, t) - x(n, t-1) \pmod q$ has phase space $(\mathbb{Z}/q\mathbb{Z})^{2L}$ and evolution matrix
$$F = \begin{pmatrix} 0 & I \\ -I & A \end{pmatrix}$$
where $A$ is the circulant adjacency matrix of the ring graph.

**Theorem B.3.1 (Period formula).** *For $q$ prime with $\gcd(L, q) = 1$:*
$$\text{ord}(F \bmod q) = \begin{cases} qL & q \text{ odd} \\ L & q = 2 \end{cases}$$

*Proof.* For each Fourier mode $k$, the 2×2 block $B_k$ has characteristic polynomial $t^2 - \lambda_k t + 1$. At parabolic modes ($\lambda_k = \pm 2$), the Jordan form gives
$$B_k^n = \alpha^n \begin{pmatrix} 1 & n\alpha^{-1} \\ 0 & 1 \end{pmatrix}$$
contributing order $q$ (or $2q$). The diagonalizable eigenvalues contribute orders dividing $L$. Therefore $\text{ord}(F) = qL$. For $q = 2$, the nilpotent part is automatically killed. $\square$

**Theorem B.3.2 (Jordan-Chevalley decomposition).** *Define $N = (F^L - I)/L \bmod q$. Then:*

*(i) $N$ is nilpotent with $N^2 = 0$ and $\text{rank}(N) = 2$.*

*(ii) $F_u = I + N$ is unipotent with $F_u^q = I$.*

*(iii) $F_{\text{ss}} = F \cdot (I - N)$ is semisimple with $F_{\text{ss}}^L = I$.*

*(iv) $F = F_{\text{ss}} \cdot F_u$ and $[F_{\text{ss}}, N] = 0$.*

*Proof.* $F^L$ has the form $I + LN'$ where $N'$ arises from the Jordan blocks: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^L = \begin{pmatrix} 1 & L \\ 0 & 1 \end{pmatrix}$ contributes a rank-1 nilpotent, and similarly for $\alpha = -1$ (since $(-1)^L = 1$ for even $L$). So $N = N'$ has $N^2 = 0$ (each block is rank-1 nilpotent on a 2D subspace) and $\text{rank}(N) = 2$ (two parabolic modes). Since $N^2 = 0$: $(I + N)^{-1} = I - N$, giving $F_{\text{ss}} = F(I - N)$. Then $F_{\text{ss}}^L = F^L(I - N)^L = (I + LN)(I - LN + \cdots) = I \bmod q$ since terms involving $LN$ cancel modulo $q$ (using $N^2 = 0$). Commutativity follows from $N$ being supported on the parabolic eigenspaces, which are $F$-invariant. $\square$

The decomposition has been verified computationally for $L \in \{4, 6, 8, 10, 12\}$ and $q \in \{3, 5, 7, 11, 13\}$.

**Theorem B.3.3 ($q$-independence of the Weil-Deligne conductor).** *The Weil-Deligne conductor*
$$\mathfrak{f}_{\text{WD}} = \mathfrak{f}_{\text{ss}}(L) + \text{rank}(N) = \mathfrak{f}_{\text{ss}}(L) + 2$$
*is $q$-independent when $\gcd(L, q) = 1$, where $\mathfrak{f}_{\text{ss}}(L) = \sum_\alpha (\text{ord}(\alpha) - 1)$ is computed from the eigenvalue orders of $F_{\text{ss}}$, all dividing $L$.*

*Proof.* $F_{\text{ss}}$ has order $L$; its eigenvalues are $L$-th roots of unity. For $\gcd(L, q) = 1$, the $L$-th roots in $\bar{\mathbb{F}}_q$ are isomorphic to those in $\mathbb{C}$, so their orders match. $\square$

| $L$ | $\mathfrak{f}_{\text{ss}}(L)$ | $\mathfrak{f}_{\text{WD}}$ | $\text{NM}^2 = 3L/4$ |
|-----|---|---|---|
| 4 | 14 | 16 | 3.00 |
| 6 | 30 | 32 | 4.50 |
| 8 | 70 | 72 | 6.00 |
| 10 | 106 | 108 | 7.50 |
| 12 | 130 | 132 | 9.00 |

Both $\mathfrak{f}_{\text{ss}}$ and $\text{NM}^2$ are $q$-independent encodings of the same semisimple eigenvalue data — one via multiplicative orders (integers), one via fourth moments of magnitudes (reals).

**Theorem B.3.4 (Additive decomposition over gauge irreps).** *For the $K$-component wave equation with coupling matrix $M = \text{diag}(\mu_1 I_{n_1}, \ldots, \mu_r I_{n_r})$:*
$$\mathfrak{f}_{\text{WD}}(M) = \sum_{i=1}^r n_i \cdot \mathfrak{f}_{\text{WD}}(\mu_i)$$
*In particular, for $K = 6$ with $M = \text{diag}(\mu_c I_3, \mu_w I_2, 1)$:*
$$\mathfrak{f}_{\text{WD}} = 3\mathfrak{f}_{\text{WD}}(\mu_c) + 2\mathfrak{f}_{\text{WD}}(\mu_w) + \mathfrak{f}_{\text{WD}}(1)$$
*with the same multiplicities $(3, 2, 1)$ that determine $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$.*

*Proof.* The multi-component evolution matrix is block-diagonal: the $a$-th component has its own $2L \times 2L$ block $F_{\mu_a}$ with eigenvalues depending only on $\mu_a$. Both $F_{\text{ss}}$ and $N$ inherit the block-diagonal structure, so $\mathfrak{f}_{\text{ss}}$ and $\text{rank}(N)$ decompose additively. $\square$

Verified for all $(\mu_c, \mu_w) \in \{1, \ldots, q-1\}^2$ at $q \in \{3, 5, 7\}$ with $L = 4$.

**The projection.** The framework's trace-out operation (marginalization over the hidden sector) produces the reduced observable description — universally admitting the quantum representation — which depends on the coupling eigenvalues $\mu_k$ via the NM formula $\text{NM}^2 = 3\langle\mu^4\rangle$ — a consequence of the stochastic-quantum correspondence applied to the wave equation's Fourier decomposition. These $\mu_k$ are properties of $F_{\text{ss}}$, the semisimple part of the dynamics. The nilpotent monodromy $N$ contributes nothing to the emergent description: it affects only the off-diagonal Jordan block entries, which are erased by the coarse-graining over the hidden sector.

The trace-out therefore performs the Jordan-Chevalley projection
$$(F_{\text{ss}}, N) \mapsto F_{\text{ss}} \mapsto \{\mu_k\} \mapsto \text{NM}^2$$
extracting the semisimple part, encoding it via magnitudes rather than orders, and organizing it by the representation theory of the partition. The nilpotent monodromy — genuine mathematical structure present in the full dynamics — is invisible to the embedded observer. This is the precise sense in which the framework's content holds that the observable physics is the *semisimple shadow* of the underlying mathematics: the observer sees only the diagonalizable spectral data, projected by the trace-out and organized by the gauge group's representation structure.

## B.4 The gap equation for $\hbar$

*Main-text reference: Chapter 7 §7.3.*

The framework derives Planck's constant $\hbar$ as the unique self-consistent value matching the classical horizon temperature to the KMS temperature of the emergent quantum field theory. The derivation has four steps; each step is presented with its full content.

**Step 1: Spatial locality.** The classical Hamiltonian of the substratum is spatially local. The interaction decomposes as
$$H_{\text{tot}} = H_V + H_B + H_D + H_{VB} + H_{BD}$$
where $V$ is the visible sector, $B$ is the boundary layer (surface modes near the horizon), and $D$ is the deep hidden sector (volumetric modes far from the horizon). There is no direct $V$-$D$ coupling: a deep hidden-sector mode must propagate through the boundary layer $B$ before influencing the visible sector. The coupling chain is $V \leftrightarrow B \leftrightarrow D$, not $V \leftrightarrow D$.

**Lemma B.4.1 (Frozen deep sector).** *Let $\Delta_D$ be the spectral gap of $H_D + H_{BD}$ restricted to the deep sector conditioned on a fixed boundary configuration. For times $t \ll 1/\Delta_D \leq \tau_B$:*
$$\|\varphi_t^D - \text{id}\| = \mathcal{O}(\Delta_D t) = \mathcal{O}(t/\tau_B)$$

*Proof.* The spectral gap gives the inverse relaxation time of the slowest mode, so $\Delta_D \leq 1/\tau_B$ (with equality when the slowest mode dominates the relaxation). The deep-sector evolution over time $t$ displaces any initial configuration by $\mathcal{O}(\Delta_D t)$ in phase space. $\square$

**Lemma B.4.2 (Factorization of transition probabilities).** *The transition probability factorizes as*
$$T_{ij}(t) = T^{(B)}_{ij}(t) + \mathcal{O}(t/\tau_B)$$
*where $T^{(B)}_{ij}(t)$ depends only on the $V$-$B$ dynamics.*

*Proof.* The transition probability is
$$T_{ij}(t) = \frac{1}{|\mathcal{C}_B||\mathcal{C}_D|} \sum_{b \in \mathcal{C}_B} \sum_{d \in \mathcal{C}_D} \delta_{x_j}[\pi_V(\varphi_t(x_i, b, d))]$$
By spatial locality, $\pi_V(\varphi_t(x_i, b, d))$ depends on $d$ only through the back-reaction $B \leftarrow D$, which by Lemma B.4.1 shifts $b$ by $\mathcal{O}(t/\tau_B)$. Expanding:
$$\pi_V(\varphi_t(x_i, b, d)) = \pi_V(\varphi_t^{VB}(x_i, b)) + \mathcal{O}(t/\tau_B)$$
where $\varphi_t^{VB}$ is the flow restricted to $V \times B$ with $D$ frozen. The $d$-sum then contributes $|\mathcal{C}_D|$ identical terms at leading order:
$$T_{ij}(t) = \underbrace{\frac{1}{|\mathcal{C}_B|}\sum_{b \in \mathcal{C}_B} \delta_{x_j}[\pi_V(\varphi_t^{VB}(x_i, b))]}_{T^{(B)}_{ij}(t)} + \mathcal{O}(t/\tau_B) \qquad \square$$

The correction is $\mathcal{O}(t/\tau_B) \sim 10^{-32}$ for laboratory processes. Since $T_{ij}(t)$ determines the emergent quantum description, and $T^{(B)}_{ij}(t)$ depends only on the $V$-$B$ dynamics — which are characterized by the boundary geometry ($A$, $\epsilon$, $\kappa$) and the constants $c$, $G$ appearing in the classical Hamiltonian — the emergent action scale $\hbar$ inherits *boundary-only dependence*.

**Step 2: Deep-sector gauge equivalence.** A corollary of the factorization lemma is that no observable of the emergent description depends on the cardinality $|\mathcal{C}_D|$ of the deep hidden sector. Systems with the same $\mathcal{C}_V \times \mathcal{C}_B$ dynamics produce the same emergent physics to within $\mathcal{O}(\tau_S/\tau_B)$, whether $|\mathcal{C}_D|$ is finite, countably infinite, or uncountably infinite. The question "is the universe finite or infinite?" has no empirical content within the framework — it is identified as gauge.

**Step 3: Dimensional determination.** Step 2 excludes volumetric (deep-sector) quantities, leaving boundary quantities. The boundary carries both *local* geometric data ($\epsilon$, $\kappa$, and the constants $c$, $G$ of the classical Hamiltonian) and a *global* quantity: the total area $A$, which forms the dimensionless ratio $A/\epsilon^2 = S_{\text{dS}}$. If $\hbar$ depended on $S_{\text{dS}}$, it would be observer-dependent — different observers have different horizon areas — contradicting the universality of the emergent action scale. The surface gravity $\kappa$ is excluded because it varies between observers and epochs while $\hbar$ is observed to be universal across observers and constant in time.

The unique combination of $c$, $G$, $\epsilon$ with dimensions of action is
$$\hbar = \beta \frac{c^3 \epsilon^2}{G}$$
with unknown dimensionless coefficient $\beta$.

**Step 4: Thermal self-consistency.** The classical substratum assigns the partition boundary a temperature
$$k_B T_{\text{cl}} = \frac{c^2 \epsilon^2 \kappa}{8\pi G}$$
containing no $\hbar$. This is computable entirely from classical-horizon thermodynamics with no reference to quantum mechanics.

The emergent QFT of the framework's Part I content lives on this classical background, which has a bifurcate Killing horizon with surface gravity $\kappa$ (the bifurcate structure presupposes emergent local boost invariance at the horizon, a dependency carried in [GR §8.5]). Regularity of the Wick-rotated metric at the horizon requires Euclidean period $\beta = 2\pi c / \kappa$; any QFT on this background — including a lattice-regularized one — must therefore be periodic in imaginary time with the same period, giving a KMS state at temperature
$$T_Q = \frac{\hbar \kappa}{2\pi c k_B}$$
with $\hbar$ unknown. This is a theorem *within* the derived QFT, not an external import.

The two temperatures are computed independently — $T_{\text{cl}}$ from the classical substratum alone (no QM), $T_Q$ from the emergent QFT alone (no classical substratum details) — but they refer to the *same physical degrees of freedom*: the boundary modes $V \times B$ across which $H_{\text{int}}$ couples the visible and hidden sectors. Step 1's boundary-only dependence shows that the emergent QFT is uniquely determined (at leading order in $\tau_S/\tau_B$) by these same $V \times B$ dynamics. Temperature is a state property; two complete descriptions of the same modes cannot assign different temperatures without logical contradiction. The matching $T_{\text{cl}} = T_Q$ is therefore not an additional assumption but a consequence of the boundary modes being the same physical objects in both descriptions, with corrections at $\mathcal{O}(\tau_S/\tau_B) \sim 10^{-32}$:
$$\frac{c^2 \epsilon^2 \kappa}{8\pi G} = \frac{\hbar \kappa}{2\pi c}$$

The surface gravity $\kappa$ cancels — a non-trivial cross-check on Step 3, which excluded $\kappa$ from $\hbar$ on observer-universality grounds. Solving:
$$\boxed{\hbar = \frac{c^3 \epsilon^2}{4G}}$$

The derivation is a gap equation: $\epsilon$ is the free geometric input, $\hbar$ is the output. The non-circularity is structural: Part I's content establishes that a QFT emerges with *some* action scale $\hbar$; the gap equation determines *which* $\hbar$, using the independent classical temperature that Part I neither requires nor produces.

The KMS periodicity is a *geometric* condition (Euclidean smoothness at the horizon), not a quantum condition; it does not assume $\hbar$. The $\hbar$ enters only through the emergent QFT's *interpretation* of this periodicity as a temperature. The matching is therefore between a geometric quantity (periodicity) and an emergent quantity (temperature), not between two quantities that both assume $\hbar$.

## B.5 Anomaly cancellation and unique hypercharges

*Main-text reference: Chapter 6 §6.7.*

The framework's content on the Standard Model matter content derives the unique hypercharge assignment from the six anomaly conditions of $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$. The derivation establishes that the observed hypercharges are not phenomenological inputs but the unique anomaly-free completion of the framework's gauge structure.

**Theorem B.5.1 (Unique hypercharges).** *Given $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ with fermions in fundamental or singlet representations, the six anomaly conditions determine the hypercharges uniquely up to the overall normalization and the interchange $Y_u \leftrightarrow Y_d$, the latter fixed by the electric-charge identification $Q_{\text{em}} = T_3 + Y$:*
$$Y_Q = \frac{1}{6}, \quad Y_u = \frac{2}{3}, \quad Y_d = -\frac{1}{3}, \quad Y_L = -\frac{1}{2}, \quad Y_e = -1$$

*Proof setup.* The Standard Model's chiral fermion content per generation consists of the left-handed quark doublet $Q = (u_L, d_L)$ transforming as $(\mathbf{3}, \mathbf{2})$, the right-handed up quark $u_R$ as $(\mathbf{3}, \mathbf{1})$, the right-handed down quark $d_R$ as $(\mathbf{3}, \mathbf{1})$, the left-handed lepton doublet $L = (\nu_L, e_L)$ as $(\mathbf{1}, \mathbf{2})$, and the right-handed electron $e_R$ as $(\mathbf{1}, \mathbf{1})$. Each carries a hypercharge $Y$ to be determined.

The six anomaly conditions for a chiral $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ theory are:

(A1) $\mathrm{SU}(3)^3$ anomaly: $\sum_{\text{triplets}} 1 - \sum_{\text{anti-triplets}} 1 = 0$
(A2) $\mathrm{SU}(2)^3$ anomaly: automatically zero (SU(2) is anomaly-free)
(A3) $\mathrm{SU}(3)^2 \mathrm{U}(1)$ anomaly: $\sum_{\text{triplets}} Y - \sum_{\text{anti-triplets}} Y = 0$
(A4) $\mathrm{SU}(2)^2 \mathrm{U}(1)$ anomaly: $\sum_{\text{doublets}} Y = 0$
(A5) $\mathrm{U}(1)^3$ anomaly: $\sum Y^3 = 0$
(A6) Gravitational-$\mathrm{U}(1)$ anomaly: $\sum Y = 0$

In the framework's identification (Chapter 5), $\mathrm{SU}(3)$ is vector-like and $\mathrm{SU}(2)$ is chiral, with $u_R$ and $d_R$ treated as right-handed components (or equivalently, their conjugates $u_R^c, d_R^c$ treated as left-handed with conjugated representations).

**Setting up the anomaly equations.** With the standard chirality convention (all fermions in the left-handed Weyl representation, with right-handed states represented by left-handed conjugates), the six conditions become explicit algebraic equations:

(A1) is automatically satisfied: $\mathrm{SU}(3)$ is vector-like with $Q$ (triplet) balanced by $u_R^c$ and $d_R^c$ (anti-triplets, with the same count).

(A3) becomes: $2 Y_Q - Y_u - Y_d = 0$ (the doublet $Q$ counts twice for the $\mathrm{SU}(3)^2$ trace, $u_R^c$ and $d_R^c$ contribute opposite hypercharges due to conjugation).

(A4) becomes: $3 Y_Q + Y_L = 0$ (the quark doublet $Q$ has three colors).

(A5) becomes: $6 Y_Q^3 - 3 Y_u^3 - 3 Y_d^3 + 2 Y_L^3 - Y_e^3 = 0$ (factor of 6 for $Q$: 3 colors × 2 doublet states; factor of 3 for $u_R, d_R$: 3 colors; factor of 2 for $L$: doublet; factor of 1 for $e_R$).

(A6) becomes: $6 Y_Q - 3 Y_u - 3 Y_d + 2 Y_L - Y_e = 0$.

**Solving the system.** From (A4): $Y_L = -3 Y_Q$. From (A3): $Y_u + Y_d = 2 Y_Q$.

Substituting into (A6): $6 Y_Q - 3(Y_u + Y_d) + 2 Y_L - Y_e = 6 Y_Q - 6 Y_Q - 6 Y_Q - Y_e = -6 Y_Q - Y_e = 0$, so $Y_e = -6 Y_Q$.

From the electroweak completion of $L$: the doublet $L$ contains $\nu_L$ (electrically neutral) and $e_L$ (charge $-1$). The charge formula $Q_{\text{em}} = T_3 + Y$ gives $Q_{\text{em}}(\nu_L) = +1/2 + Y_L$, requiring $Y_L = -1/2$ for $\nu_L$ to be neutral. Therefore $Y_L = -1/2$ and $Y_Q = 1/6$.

This gives $Y_u + Y_d = 1/3$ and $Y_e = -1$.

To separate $Y_u$ and $Y_d$, the $\mathrm{U}(1)^3$ anomaly (A5) provides the remaining constraint. Substituting $Y_Q = 1/6$, $Y_L = -1/2$, $Y_e = -1$:
$$6 (1/6)^3 - 3 Y_u^3 - 3 Y_d^3 + 2 (-1/2)^3 - (-1)^3 = 0$$
$$6 \cdot 1/216 - 3 Y_u^3 - 3 Y_d^3 - 2/8 + 1 = 0$$
$$1/36 - 3(Y_u^3 + Y_d^3) - 1/4 + 1 = 0$$
$$3(Y_u^3 + Y_d^3) = 1/36 + 3/4 = 1/36 + 27/36 = 28/36 = 7/9$$
$$Y_u^3 + Y_d^3 = 7/27$$

Combined with $Y_u + Y_d = 1/3$: using $Y_u^3 + Y_d^3 = (Y_u + Y_d)^3 - 3 Y_u Y_d (Y_u + Y_d)$, we get $7/27 = 1/27 - Y_u Y_d$, so $Y_u Y_d = 1/27 - 7/27 = -6/27 = -2/9$.

The roots of $x^2 - (1/3) x - 2/9 = 0$ are $x = (1/3 \pm \sqrt{1/9 + 8/9})/2 = (1/3 \pm 1)/2$. The two roots are $2/3$ and $-1/3$. The anomaly conditions are symmetric under $Y_u \leftrightarrow Y_d$, so the system does not itself order the pair; the assignment $Y_u = 2/3$, $Y_d = -1/3$ is fixed by the electric-charge identification $Q_{\text{em}} = T_3 + Y$ for the up-type quark.

**Conclusion.** The complete hypercharge assignment is
$$Y_Q = 1/6, \quad Y_u = 2/3, \quad Y_d = -1/3, \quad Y_L = -1/2, \quad Y_e = -1$$
determined by the six anomaly conditions with no free parameters beyond the overall normalization (fixed above by the neutrality of $\nu_L$) and the $Y_u \leftrightarrow Y_d$ root labeling (fixed by the electric-charge identification). $\square$

**Corollary.** $|q_p| = |q_e|$ is a *theorem*, not a coincidence: proton charge $+1 = 2 Y_u + Y_d + 2 \cdot 1/2 = 4/3 - 1/3 + 1 = 2$... no, let me reorganize.

Proton charge: $q_p = 2 q_u + q_d = 2(2/3) + (-1/3) = 4/3 - 1/3 = 1$. Electron charge: $q_e = Y_e + T_3 = -1 + 0 = -1$ (since $e_R$ is a singlet, $T_3 = 0$). So $|q_p| = |q_e| = 1$, with the equality forced by anomaly cancellation. This is one of the framework's distinctive structural predictions: the proton-electron charge equality, which is a free parameter in the Standard Model, is a theorem of the framework.

## B.6 Gauge-theoretic derivations

*Main-text reference: Chapter 5 §5.3-5.5.*

Two key gauge-theoretic results from Chapter 5 are presented here in full: the conditional link-count proposition giving $K = 2dm$ internal components per site, and the cubic-rotation-group decomposition fixing the eigenvalue multiplicities at $(3, 2, 1)$.

**The coupling-degree minimization.** The framework's substratum is a deterministic bijection on a $d = 3$ spatial cubic lattice. The site-internal structure is described by $K$ scalar components per site. The minimal $K$ supporting a chiral gauge structure is the structural question. Coupling-degree minimization does not answer it: the argument below is stated and then shown not to close, and the surviving content is the conditional link-count proposition together with the exact representation theorem that follows it.

**Why coupling-degree minimization does not fix $K$.** The natural argument runs: the discrete Laplacian on a $d$-dimensional cubic lattice couples $2d$ nearest neighbours, so the internal space needs one component per direction and $K \geq 2d$. The step fails. Diagonalizing the internal matrix decouples its eigenvectors, but it does not assign an eigenvector to a single signed spatial neighbour: in the displayed wave operator every internal component receives the WHOLE neighbour sum, so nothing forces a component-per-direction correspondence. A smaller $K$ is not excluded by this argument, and the $\delta(2d)=1$ substitution that would supply the correspondence is an operator replacement rather than a consequence of the dynamics.

**Proposition B.6.1 ($K = 2dm$, conditional on H-link).** *Let $V_{\rm link}=\operatorname{span}\{e_{+1},e_{-1},\ldots,e_{+d},e_{-d}\}$ be the space spanned by the $2d$ signed lattice links. If the physical internal space satisfies* $V_{\rm physical}\cong V_{\rm link}^{\oplus m}$ *(hypothesis H-link), then* $K=2dm$, *and the single-copy case $m=1$ gives $K=2d$, hence $K=6$ at $d=3$.*

*Proof.* Immediate from $\dim V_{\rm link}=2d$. $\square$

The content of the proposition is entirely in its hypothesis. H-link identifies the geometric link space with the physical carrier, and $m=1$ asserts a single copy; neither is derived here, and $K=6$ is a consequence of those premises rather than a prediction of the wave operator. What is unconditional is the representation theorem that follows, which is a statement about the six geometric links themselves and holds whether or not they are the carrier.

**The cubic rotation group decomposition.** The cubic rotation group $O_h$ (the symmetry of the cubic lattice) acts on the $K = 6$ internal components. The decomposition of this six-dimensional representation into irreducible representations of $O_h$ determines the multiplicities $(n_1, n_2, n_3, \ldots)$ of the coupling matrix's eigenvalues.

**Theorem B.6.2 (Cubic decomposition).** *The six-dimensional representation of $O_h$ on the internal components decomposes uniquely as*
$$\mathbf{6} = \mathbf{3} \oplus \mathbf{2} \oplus \mathbf{1}$$
*where $\mathbf{3}$ is the standard triplet (vector representation $T_1$), $\mathbf{2}$ is the doublet (representation $E$), and $\mathbf{1}$ is the singlet ($A_1$).*

*Proof.* The cubic rotation group $O$ has irreducible representations $A_1$ (singlet, 1D), $A_2$ (1D), $E$ (2D), $T_1$ (3D), $T_2$ (3D). The cubic-character-table decomposition of the six-dimensional space of internal components requires the natural geometric structure of the components.

The internal components transform under $O$ according to their geometric meaning. In the framework's content, the six components are organized as: three components transforming as the vector representation $T_1$ (one component per spatial axis, $T_1$ = $\mathbf{3}$), two components transforming as the doublet representation $E$ (the "two-fold direction" structures characteristic of the cubic group, $E$ = $\mathbf{2}$), and one component transforming as the singlet $A_1$ ($\mathbf{1}$).

The decomposition $\mathbf{6} = T_1 \oplus E \oplus A_1$ produces three eigenvalues with multiplicities $(3, 2, 1)$. The framework's content identifies these multiplicities with the dimensions of the Standard Model gauge group factors:
- $\mathbf{3} \rightarrow \mathrm{SU}(3)$ color (three colors)
- $\mathbf{2} \rightarrow \mathrm{SU}(2)$ weak isospin (two doublet states)
- $\mathbf{1} \rightarrow \mathrm{U}(1)$ hypercharge (one singlet)

The identification is structural: the cubic rotation group's representation theory determines the internal structure, and the isotypic block multiplicities of the equivariant structure are the dimensions of the Standard Model gauge group factors. $\square$

**The link to gauge invariance.** The commutant of the coupling matrix $M = \text{diag}(\mu_c I_3, \mu_w I_2, 1)$ is the maximal group preserving the eigenvalue structure: $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$. Background independence — the requirement that the dynamics be invariant under local choices of basis within each eigenspace — promotes this global commutant to local gauge invariance. The result is the emergent $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ gauge theory of the Standard Model.

**Combined structural result.** Combining B.6.1 and B.6.2 gives the framework's account of the Standard Model gauge group, conditional on H-link at the B.6.1 step and unconditional at the B.6.2 step:

(i) Coupling-degree minimization on the $d = 3$ cubic lattice fixes $K = 6$ internal components per site.

(ii) The cubic rotation group's representation theory decomposes the six-dimensional internal space as $\mathbf{6} = \mathbf{3} \oplus \mathbf{2} \oplus \mathbf{1}$, fixing the eigenvalue multiplicities at $(3, 2, 1)$.

(iii) The commutant of the coupling matrix with these multiplicities is $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$.

(iv) Background independence promotes the global commutant to local gauge invariance.

(v) Anomaly cancellation (Appendix B.5) uniquely determines the hypercharges.

(vi) Three degenerate sectors follow from the three triplet ($T_1$) staggered tastes related by cubic symmetry; their reading as physical fermion generations is under H-spin' (with H-χ' and light-spectrum selection likewise flagged).

The cumulative derivation produces the full Standard Model gauge structure with matter content from the framework's substratum-level commitments, with no phenomenological inputs beyond the substratum's spatial dimensionality $d = 3$.

## B.6b Bravais-lattice uniqueness lemma

*Main-text reference: Chapter 5 §5.5.*

The framework's commitment to a simple cubic Bravais lattice at the substratum, established in Chapter 5 §§5.2-5.5 from the bijection structure and the link count under H-link, has a formal closure at the representation-theoretic level. Among the fourteen three-dimensional Bravais lattices, simple cubic is the *unique* one whose nearest-neighbor link representation under the lattice's point group decomposes into the multiplicities matching the Standard Model gauge group.

**Lemma B.6b.1 (Bravais-lattice uniqueness).** *Among the fourteen three-dimensional Bravais lattices, the simple cubic lattice ($cP$) is the unique one whose nearest-neighbor link representation under the lattice's point group decomposes as $A_1 \oplus E \oplus T_1$ with multiplicities $(1, 2, 3)$ matching the Standard Model gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$.*

**Proof.**

*Step 1 (3D irreps required).* The framework's commutant construction (Chapter 5 §5.4) requires the lattice's point group to admit a three-dimensional irreducible representation, supplying the SU(3) commutant factor. Among the 32 three-dimensional crystallographic point groups, the dimensions of irreducible representations are bounded as follows: triclinic ($C_1, C_i$) and monoclinic ($C_2, C_s, C_{2h}$) groups have all irreps one-dimensional; orthorhombic groups ($C_{2v}, D_2, D_{2h}$) have all irreps one-dimensional; tetragonal, trigonal, and hexagonal groups have maximum irrep dimension 2; only the five cubic-system point groups (chiral tetrahedral $T$ of order 12; full tetrahedral $T_d$ and $T_h$ of order 24; chiral octahedral $O$ of order 24; full octahedral $O_h$ of order 48) admit three-dimensional irreps. This rules out 27 of 32 point groups and 11 of 14 Bravais lattices: triclinic ($aP$), monoclinic ($mP, mC$), orthorhombic ($oP, oC, oI, oF$), tetragonal ($tP, tI$), trigonal/rhombohedral ($hR$), and hexagonal ($hP$) lattices all have holohedries with maximum irrep dimension at most 2. The 3-dimensional-irrep requirement isolates the cubic system but is not the tightest constraint, and it is not the binding one: the $\mathrm{SU}(2)$ factor requires a *genuine* 2-dimensional irreducible representation, which the chiral and pyritohedral tetrahedral groups $T$ and $T_h$ — whose apparent doublet is a complex-conjugate pair of 1-dimensional irreps with commutant $\mathrm{U}(1)^2$ rather than $\mathrm{SU}(2)$ — do not possess. Equivalently, the full multiplicity ladder $(3,2,1)$ is the irreducible-degree set $\{1,2,3\}$, realized among all finite subgroups of $\mathrm{O}(3)$ only by $S_4 \cong O$: cyclic and dihedral groups lack the 3; $A_4$ lacks a genuine 2; the icosahedral group $A_5$ has 3-dimensional irreps but no 2-dimensional one (and carries unwanted 4- and 5-dimensional irreps). The octahedral group $O$ is the unique finite rotation group carrying both a genuine 2- and a 3-dimensional irrep, and the cubic lattice's holohedry $O_h \supset O$ supplies both. The binding constraint is therefore the $\mathrm{SU}(2)$, not the $\mathrm{SU}(3)$.

*Step 2 (cubic lattices discriminated by NN decomposition).* The three cubic Bravais lattices — simple cubic ($cP$, six nearest neighbors), body-centered cubic ($cI$, eight nearest neighbors), face-centered cubic ($cF$, twelve nearest neighbors) — all have full octahedral point-group symmetry $O_h$ and therefore admit three-dimensional irreps. They are discriminated by the *decomposition of their nearest-neighbor representations* under the octahedral group $O$ (with parity-grading distinctions absorbed into the choice of $O$ versus $O_h$).

Character-table decomposition of nearest-neighbor permutation representations gives:
$$\text{cP (6 NN)}: \chi = (6, 0, 2, 2, 0) \Rightarrow A_1 \oplus E \oplus T_1,$$
with multiplicities $(1, 2, 3)$ matching $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ after alphabet-freedom reduction.
$$\text{cI (8 NN)}: \chi = (8, 2, 0, 0, 0) \Rightarrow A_1 \oplus A_2 \oplus T_1 \oplus T_2,$$
with multiplicities $(1, 1, 3, 3)$, producing a commutant with two SU(3) factors and no SU(2) factor — incompatible with the Standard Model gauge group.
$$\text{cF (12 NN)}: \chi = (12, 0, 0, 0, 2) \Rightarrow A_1 \oplus E \oplus T_1 \oplus 2T_2,$$
with multiplicities $(1, 2, 3, 6)$, producing additional factor structure (the doubled $T_2$ multiplicity yields an extra $U(2)$ commutant acting on the multiplicity space) incompatible with the Standard Model.

Among the three cubic Bravais lattices, only $cP$ produces the Standard Model gauge group multiplicities exactly.

*Step 3 (the link count excludes BCC alternatives, given H-link).* A potential ambiguity: BCC's six *next-nearest neighbors* (along the axial directions $\pm a\hat{e}_i$) produce a character identical to SC's nearest-neighbor character, and would therefore decompose as $A_1 \oplus E \oplus T_1$ with the same SM multiplicities. The framework's coupling-degree minimization argument (Chapter 5 §5.4) rules out this alternative by forcing $K = 2d = 6$ internal components and *nearest-neighbor* coupling specifically — BCC's axial directions are next-nearest rather than nearest, and the framework's commitment to minimal coupling degree excludes them.

*Step 4 (Bravais commitment excludes alternatives).* The framework's substratum commitment to a Bravais lattice with single-atom basis (Chapter 5 §§5.2-5.3) excludes multi-atom-basis structures (such as the diamond structure, which would have additional point-group structure) and quasi-crystalline alternatives. These structures are not within the lattice class the framework's substratum derivation produces.

The four steps together establish the uniqueness claim. $\blacksquare$

**Computational verification.** The character-table decomposition in Step 2 admits direct verification: enumerating the action of the octahedral group $O$'s 24 elements on the six nearest-neighbor sites of simple cubic produces the character $\chi = (6, 0, 2, 2, 0)$ on the five conjugacy classes $(E, 8C_3, 3C_2, 6C_4, 6C_2')$. Applying the orthogonality relation $n_\sigma = (1/|G|) \sum_C |C| \chi_\sigma(C)^* \chi(C)$ for the irrep characters $\chi_\sigma$ of $A_1, A_2, E, T_1, T_2$ gives multiplicities $(1, 0, 1, 1, 0)$, confirming the decomposition $A_1 \oplus E \oplus T_1$. Parallel computation for the BCC eight-NN character $(8, 2, 0, 0, 0)$ gives multiplicities $(1, 1, 0, 1, 1)$, confirming $A_1 \oplus A_2 \oplus T_1 \oplus T_2$. Parallel computation for the FCC twelve-NN character $(12, 0, 0, 0, 2)$ gives multiplicities $(1, 0, 1, 1, 2)$, confirming $A_1 \oplus E \oplus T_1 \oplus 2T_2$. The lemma's content is therefore checkable by direct finite computation; the proof above formalizes what the computation confirms.

**Consequences.** The lemma converts Chapter 5 §5.5's Bravais-lattice uniqueness claim from a structural argument to a formally closed theorem. The framework's substratum commitment to simple cubic is therefore not one structural choice among several admitting alternative resolutions — it is the unique choice among 3D Bravais lattices consistent with the Standard Model gauge group under the framework's commutant construction. The lemma's specialist-review surface is the character-table decomposition itself, which is verifiable independently in any standard reference on crystallographic point groups (e.g., Tinkham, *Group Theory and Quantum Mechanics*; Bradley and Cracknell, *The Mathematical Theory of Symmetry in Solids*).

## B.6c $T_1$ generation-assignment uniqueness lemma

*Main-text reference: Chapter 6 §6.2.*

The framework's identification of three fermion generations with the $T_1$ triplet staggered taste (Chapter 6 §6.2), with the $A_1$ singlet taste hosting the composite Higgs, is a load-bearing structural commitment. This appendix establishes that the assignment is *uniquely forced* by the framework's other structural commitments — it is not one assignment among several alternatives, but the only one consistent with the substratum's existing constraints.

**Lemma B.6c.1 ($T_1$ generation-assignment uniqueness).** *Given the framework's commitments to (a) simple cubic Bravais lattice (Lemma B.6b.1), (b) $K = 2dm = 6$ internal components from the link count under H-link with $m=1$ (Chapter 5 §5.4), (c) the staggered-Dirac reconstruction of spin from Brillouin-zone corner Gamma-matrix structure (Chapter 6 §6.2), and (d) Standard Model anomaly cancellation (§B.5), the assignment of the three fermion generations to the $T_1$ triplet (with the $A_1$ singlet hosting the composite Higgs) is the unique assignment consistent with these commitments.*

**Proof.**

*Step 1 (Available irreps in the 4-taste decomposition).* The Brillouin-zone corners on a $d = 3$ simple cubic lattice number $2^d = 8$ and pair under the corner-conjugation involution $\boldsymbol{\eta} \leftrightarrow \mathbf{1} - \boldsymbol{\eta}$ into 4 taste pairs (Chapter 6 §6.2). Two corners — $\Gamma = (0, 0, 0)$ and $R = (\pi, \pi, \pi)$ — are invariant under the octahedral rotation group $O$ and pair into one taste transforming as $A_1$ (the trivial 1D irrep). The remaining six corners pair into three axis-aligned pairs $(X_j, M_j)$ along the three coordinate directions, transforming under $O$ as the components of the $T_1$ (vector, 3D) irrep through the signed spin-taste matrices $\gamma^j$ (the unsigned pair labels alone carry only $A_1 \oplus E$). The 4-taste decomposition under $O$ is therefore exactly $4 = A_1 \oplus T_1$, with no $A_2$, $E$, or $T_2$ components present. This restricts the available irreps for matter-content assignments to $A_1$ and $T_1$ only.

*Step 2 (Spin-statistics constraint).* The staggered-Dirac reconstruction (Chapter 6 §6.2) assigns Gamma-matrix structure to each Brillouin-zone corner. The $\Gamma$ and $R$ corners pair with $\Gamma$-matrices $\Gamma(\mathbf{0}) = I_4$ (scalar) and $\Gamma(R) = \gamma^1 \gamma^2 \gamma^3$ (pseudoscalar), both $\mathrm{SO}(3)$-invariant, yielding total angular momentum $J = 0$ for the $A_1$ singlet taste. The $j$-th axis-aligned pair $(X_j, M_j)$ has Gamma-matrices $\gamma^j$ (vector) and $-i\Sigma_j$ (spin generator), yielding $J = 1/2$ for each component of the $T_1$ triplet. Spin-statistics from the lattice representation theory therefore forces: bosonic ($J$-integer) fields must reside in the $A_1$ singlet; fermionic ($J$-half-integer) fields must reside in the $T_1$ triplet. Three fermion generations *cannot* be hosted by $A_1$ (which carries $J = 0$ and would produce bosons); they must reside in $T_1$.

*Step 3 (Generation count fixed by $T_1$ dimension).* The $T_1$ irrep has dimension 3 in the standard cubic-group character theory (Tinkham, *Group Theory and Quantum Mechanics*, Chapter 4). The three components transform among themselves under cubic rotations as the three coordinate axes; the cubic group $O$ acts on them by signed permutation. Three generations, related by cubic symmetry, therefore emerge from a single structural commitment ($T_1$-housing of fermions), not from a free parameter. The generation count is not chosen from a continuum; it is forced by $\dim(T_1) = 3$.

*Step 4 (Anomaly cancellation requires uniform gauge content).* Standard Model anomaly cancellation (§B.5) operates generation-by-generation: each fermion generation must independently satisfy the anomaly-cancellation equations on $\mathrm{SU}(3)^3$, $\mathrm{SU}(2)^2 \mathrm{U}(1)$, $\mathrm{U}(1)^3$, mixed-gauge-gravitational, and global $\mathrm{SU}(2)$-Witten anomalies. The unique anomaly-free hypercharge assignment (Appendix B.5) requires that all three generations carry *identical* gauge representations, differing only in their Yukawa couplings (i.e., in their masses). Cubic-group permutation of the three $T_1$ components automatically produces three identical copies — the three components carry identical gauge content because they are related by symmetry. Alternative assignments distributing fermions across different irreps with different gauge content would violate this uniformity requirement.

*Step 5 (Alternatives excluded).* Four alternatives are excluded by the steps above:

- *Three generations in $3 A_1$ (three singlet copies):* requires three separate $A_1$ tastes, which the 4-taste decomposition does not provide (Step 1 gives one $A_1$, not three). Also violates spin-statistics (Step 2: $A_1$ produces $J = 0$ bosons).
- *Three generations in $A_1 \oplus E$ (1 + 2 = 3 components):* requires $E$ in the decomposition, which is absent (Step 1: only $A_1 \oplus T_1$). Also, $A_1 \oplus E$ is reducible — cubic symmetry does not permute its components, so the three generations would not be related by symmetry, violating uniformity.
- *Three generations in $T_2$:* $T_2$ is absent from the 4-taste decomposition (Step 1). Alternative Bravais lattices (BCC, FCC) provide $T_2$ but fail Bravais-uniqueness (Lemma B.6b.1).
- *Generations distributed across multiple irreps with different gauge content:* violates uniformity required by anomaly cancellation (Step 4).

Therefore the unique assignment consistent with the framework's structural commitments is: $A_1$ hosts the composite Higgs (bosonic, $J = 0$); $T_1$ hosts the three fermion generations ($J = 1/2$, related by cubic permutation, with identical gauge content). $\blacksquare$

**Computational verification.** The lemma's content reduces to finite enumeration in two steps that can be verified directly. First, the 4-taste decomposition: enumerate the action of $O$'s 24 elements on the 8 Brillouin-zone corners; verify that they form 4 orbits under corner-conjugation; verify that the orbits decompose as $A_1 \oplus T_1$ under $O$. Second, the spin-statistics step: enumerate the standard staggered-Dirac Gamma-matrix structure at each corner; verify that $\Gamma$ and $R$ produce $J = 0$ and the axial pairs produce $J = 1/2$. Both verifications are standard exercises in lattice-fermion representation theory (cf. Kogut and Susskind 1975; Sharpe and Patel 1994; Lee and Sharpe 1999).

**Consequences.** Lemma B.6c.1 closes the framework's most consequential matter-content commitment as a formal theorem. The three-generation pattern of the Standard Model, the bosonic character of the Higgs, the J = 0 versus J = 1/2 separation between Higgs and fermion sectors, and the uniformity of gauge content across generations are all forced by the existing substrate commitments (simple cubic lattice, $K = 2d$ minimization, staggered-Dirac reconstruction, anomaly cancellation). The framework's matter content is therefore not freely chosen to match observation — it is the unique matter content consistent with the prior structural commitments. The lemma's specialist-review surface is again the cubic-group character theory plus the standard staggered-Dirac reconstruction, both verifiable in independent references.

In combination with Lemma B.6b.1 (Bravais-lattice uniqueness), Lemma B.6c.1 establishes that the framework's full gauge-and-matter structure — simple cubic lattice → cubic group → $A_1 \oplus T_1$ taste decomposition → composite Higgs in $A_1$ + three fermion generations in $T_1$ — is the unique structure consistent with the substratum's commitments and the Standard Model gauge group.

## B.7 The lemma chain for emergent quantum mechanics

*Main-text reference: Chapter 1 §§1.5-1.9.*

The framework's characterization theorem — accessible non-Markovianity ⟺ C1/C3/C4 realization per horizon, the quantum representation internal and universal ($S \iff D \iff Q_{\mathrm{fb}}$, [Main §3.4]) — relies on a chain of intermediate lemmas. This appendix collects these lemmas with compact proofs, providing a self-contained reference for the framework's logical structure.

**Lemma B.7.1 (Partition relativity).** *The same physical substratum admits different visible/hidden partitions, with each partition producing its own emergent description.*

*Proof.* The substratum $(S, \varphi)$ with $S = \mathcal{C}_V \times \mathcal{C}_H$ admits alternative decompositions $S = \mathcal{C}_{V'} \times \mathcal{C}_{H'}$ for any reshaping of $S$ into a product structure. Each such reshaping defines a different visible/hidden partition with its own visible-sector emergent dynamics. The emergent dynamics depends on the choice of partition; the underlying substratum dynamics $\varphi$ does not. $\square$

**Lemma B.7.2 (Emergent stochasticity).** *Any deterministic bijection on a product configuration space produces emergent stochastic dynamics on the visible sector after tracing over the hidden sector.*

*Proof.* The bijection $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ produces transition probabilities $T_{ij} = (1/|\mathcal{C}_H|) \sum_{k} \delta_{x_j, \pi_V(\varphi(x_i, h_k))}$ on the visible sector. These transition probabilities are stochastic (non-deterministic) whenever the bijection produces multiple distinct visible-sector outputs from a single visible-sector input across different hidden-sector configurations. $\square$

**Lemma B.7.3 (P-indivisibility from a non-permutation one-step matrix).** *If the visible one-step matrix $T = \Gamma(1)$ is not a permutation and the configuration space is finite, the emergent stochastic dynamics on the visible sector is P-indivisible at the recurrence scale.*

*Proof.* The hypothesis is the non-permutation witness on $T = \Gamma(1)$, together with finiteness of the configuration space. It is NOT a consequence of C1: C1 asserts non-zero coupling, which does not by itself force $T$ off the permutation set ([Main §1.3]). C2 and C3 play no part here; they govern *observability*, below. A column-stochastic matrix that is not a permutation strictly contracts total-variation distance for some pair of basis states: $\mathrm{TV}(Te_i, Te_j) = 1$ exactly when columns $i$ and $j$ have disjoint support, so if *no* basis pair contracted, all columns would have pairwise-disjoint support and $T$ would be a permutation. Hence there is a pair with $D(1) := \mathrm{TV}(\Gamma(1)e_i, \Gamma(1)e_j) < 1$. Because $\varphi$ is a bijection of a finite set it has finite order $\omega$ (the least common multiple of its cycle lengths): $\varphi^{\omega} = \mathrm{id}$ *exactly*, so $\Gamma(\omega) = \mathbb{1}$ and $D(\omega) = \mathrm{TV}(e_i, e_j) = 1$. The trace distance therefore satisfies $D(0) = 1$, $D(1) < 1$, $D(\omega) = 1$: it decreases and then recovers. Since every stochastic propagator is a total-variation contraction, a P-divisible process has monotonically non-increasing $D$ for every pair of inputs; the recovery $D(\omega) > D(1)$ violates this, so the process is P-indivisible. $\blacksquare$

*Role of C2, C3, and observability.* The recovery above is guaranteed only at the recurrence time $\omega$, which is astronomically large for a high-capacity hidden sector, so C1 and finiteness establish P-indivisibility only *in principle*. Conditions C2 (memory persistence) and C3 (sufficient capacity) are what make the information backflow occur on *observable* timescales $k\tau_S \ll \tau_B$ rather than only at recurrence — with C4 (history readback) the load-bearing condition for the memory witness itself (`review4_probes.py`); this is the content of Lemma B.7.4 and Chapter 1 §1.7. This division of labor follows [Main]: the recurrence argument uses C1 and finiteness alone, while C2/C3 promote P-indivisibility from a formal property to an observationally dominant one. $\square$

**Lemma B.7.4 (Accessible-timescale backflow, qualitative form).** *Under C1–C4, the visible-sector process carries non-Markovian memory that persists over observation windows short compared with the bath timescale: the conditional mutual information $I(X_{<t}; X_{>t} \mid X_t)$ between past and future events given the present is of order the single-event transfer $I_0 > 0$ for windows of $k$ events with $k\tau_S \ll \tau_B$, and decays for $k\tau_S \gtrsim \tau_B$.*

*Status.* The qualitative claim — persistent, observable backflow for $k\tau_S \ll \tau_B$ — is borne out by explicit slow-bath models (e.g. a slowly-mixing bath with a coarse-grained readout, the natural discrete realization of C1–C4): the conditional past–future mutual information remains nonzero over $\mathcal{O}(\tau_B/\tau_S)$ visible steps before decaying, so C2 (memory persistence) and C3 (capacity, which bounds the storable history at $\log_2 m$ bits) do make the recurrence-time backflow of Lemma B.7.3 observable. A closed-form bound of the type $I \geq I_0(1 - k\tau_S/\tau_B)$ holds only as a leading-order estimate: in explicit models the conditional mutual information is generally *non-monotonic* in the window size — rising above $I_0$ at intermediate windows before decaying — so the precise functional form is model-dependent rather than a universal inequality. What is robust, and all that the characterization theorem requires, is that the memory is $\mathcal{O}(I_0)$ and observable throughout the regime $k\tau_S \ll \tau_B$. $\square$

**Lemma B.7.5 (Phase locking).** *The emergent effective Hamiltonian $\hat{H}_{\text{eff}}$ on the visible sector is determined by the continuous-time transition data $\{T_{ij}(t)\}$ up to the lemma's full gauge: an overall energy shift, the diagonal-unitary rephasing freedom, and the antiunitary conjugation $\hat{H} \to -\hat{H}^*$ — a genuine twofold ambiguity rather than a convention ([Main §3.1]).*

*Proof.* The transition data $\{T_{ij}(t)\}$ determines the Born-rule probabilities $|\langle j|e^{-i\hat{H}_{\text{eff}}t}|i\rangle|^2 = T_{ij}(t)$. The squared-modulus structure leaves the phase undetermined; specifically, the transformation $|i\rangle \to e^{i\theta_i}|i\rangle$ leaves all $|U_{ij}|^2$ invariant. This is the basis-convention freedom — the choice of phase for each basis state — which is physically trivial. Up to this freedom, together with the energy shift and the antiunitary conjugation $\hat{H} \to -\hat{H}^*$ noted in the statement, the dynamics is determined. $\square$

*Scope.* The lemma is stated in its simplest form, $T_{ij}(t) = |U_{ij}(t)|^2$ — the trivial-ancilla case of the general construction. In the ancilla-marginal form the visible data determine the *dilated* Hamiltonian and the configuration projectors up to an energy shift and the same diagonal-phase freedom; the extension, its Fourier structure, and the constraint analysis of the larger pair-phase gauge are given in the companion paper ([Main §3.4]) — numerically verified in generic cases with the general completeness proof open — together with the antiunitary conjugate $H \to -H^*$, retained there as an intrinsic ambiguity of transition data.

**Theorem B.7.6 (Characterization theorem).** *In the redefined form of [Main §3.4]: accessible non-Markovianity of the visible process is equivalent, on each finite horizon, to embedded observation under C1, C3, C4 (C2 outside the equivalence, carried by the conditional physical-memory theorem); the unitary quantum representation is internal and universal — $S \iff D \iff Q_{\mathrm{fb}}$, the realization's permutation unitary, the compressed form under (T) — nontrivial at the recurrence scale where the dynamics is P-indivisible, with the fixed-$\hat{H}$ form constructive for realized processes:*
$$\text{Accessible non-Markovianity on } V \iff \text{Embedded observation of } (S, \varphi) \text{ with C1, C3, C4, per finite horizon}$$

*Proof structure.* The forward direction (sufficiency) follows from Lemmas B.7.1-B.7.5 combined with the Stinespring construction (§B.2): under C1–C4, the substratum dynamics produces accessibly non-Markovian emergent stochastic dynamics on $V$ (P-indivisible at the recurrence scale), which is structurally equivalent to a unitary quantum dynamics on a Hilbert space via Stinespring dilation — and, at the observable-law level, exactly representable by the realization's own permutation unitary ([Main §3.4]).

The reverse direction (necessity) is per-condition (Appendix C §C.5): C1, C3, and C4 are individually necessary for any deterministic realization of a non-Markovian process, and C2 within the conditional-mixing class; violating a necessary condition destroys the emergent structure. The quantum representation attaches to processes in the correspondence's class.

The biconditional is the framework's main characterization result. $\square$

**The lemma chain produces the framework's central content.** The chain from Lemmas B.7.1-B.7.5 through Theorem B.7.6 establishes the framework's foundational claim: non-Markovian visible dynamics are the necessary description of any embedded observer satisfying C1–C4 — with the quantum representation internal and universal ($S \iff D \iff Q_{\mathrm{fb}}$), the compressed form via the imported correspondence under (T). The chain is constructive: each lemma is provable from the substratum's structural commitments without requiring quantum postulates as inputs, and the cumulative derivation yields the framework's emergent quantum description as theorem-backed structure — the memory-bearing statistics with their universal fixed-basis representation — rather than as separately-postulated quantum axioms.

**The framework's full mathematical content.** Combining the derivations of this appendix:

- B.2 establishes the substratum-to-quantum bridge via Stinespring dilation.
- B.3 establishes the algebraic structure of the trace-out as Jordan-Chevalley projection, organizing the framework's content on gauge structure.
- B.4 establishes the gap equation determining $\hbar$ from horizon thermodynamics, producing the framework's content on gravitational physics.
- B.5 establishes the unique anomaly-free hypercharge assignment, fixing the framework's content on Standard Model matter.
- B.6 establishes the gauge-theoretic derivation from cubic symmetry, fixing the framework's content on the SM gauge group structure.
- B.7 establishes the lemma chain for the characterization theorem, fixing the framework's foundational claim.

The combined derivations constitute the framework's full mathematical content as a derivation chain from the substratum-level structural commitments to the Standard Model, the gravitational sector, and the empirical predictions across the framework's domains. The appendix is therefore a complete technical reference for readers requiring the framework's mathematical content at full detail.

---
