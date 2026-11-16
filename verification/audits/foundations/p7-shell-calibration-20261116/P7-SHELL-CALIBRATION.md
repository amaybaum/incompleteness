# P7 · Horizon-shell calibration without total finiteness

The decoupled reference shell gives exact visible weights and reciprocal probability flux on an infinite total carrier. Its relative boundary weights do not follow from the boundary mode count. The horizon calibration survives as a scalar implication if the boundary first-law slope and the detector match are supplied. The coupled case stops at the missing shell family.

**Authority.** On November 16, 2026, the owner (`amaybaum`) said “Approved” to the paper-only P7 check. [#1169 owner decision](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6913165024)

**Sources.** Manuscript and Lean locators refer to `main` at `ef6a9e1860724691418e0300be96b00d66475ea6`. The P7 row and owner question 3 of the [A1 recovery matrix](https://github.com/amaybaum/incompleteness/blob/06cede15037cfb12475d5459eb7f2f9d8abc861c/verification/audits/foundations/a1-recovery-matrix-20261116/RECOVERY-MATRIX.md#L58-L68) give the order of the check. [P6](https://github.com/amaybaum/incompleteness/pull/1318) is provenance for the mass-matching idea. The proof here uses the specified shell law directly. A1 is open and unadopted (Main:728, item (ii)). A4 retains its stated scope (Substratum:98). This reference model is a test of the shell argument, outside the selected lattice construction.

## 1. Decoupled reference shell

**Choice of model and law.** Take a visible bit $i$, four boundary bits $b=(b_1,b_2,b_3,b_4)$ and a deep coordinate $d\in\mathbb N_0$. Fix a single energy unit $\delta>0$. An occupied bit carries energy $\delta$, the deep coordinate carries zero, and the interaction energy is zero. Set
$$
e_i=\delta i,\qquad E_B(b)=\delta\sum_{\ell=1}^4 b_\ell,\qquad
E_{\rm tot}(i,b,d)=e_i+E_B(b).
$$
These energies are specified before any entropy or temperature comparison. Each retained state $(i,b)$ has one unit of raw mass, with the same normalized deep law $\nu(\{d\})=2^{-(d+1)}$, whose masses sum to one. On the full discrete carrier use raw mass $\lambda=\#_{\{0,1\}^5}\otimes\nu$ and the single fixed probability law $\rho=\lambda/32$. The full carrier is countably infinite and every point in it has positive mass. Let the update $\varphi$ swap $i$ and $b_1$, leaving $b_2,b_3,b_4,d$ fixed, and use time reversal $\Theta=\mathrm{id}$. This allows visible and boundary energy exchange while keeping the total energy constant. The update is an involution and a permutation of the equal-mass retained states at every $d$. Thus $\Theta\varphi\Theta=\varphi^{-1}$, both maps preserve $\rho$, and the visible labels are time-reversal even.

At total energy $k\delta$, where $0\le k\le 5$, use $\mu_k=\rho(\,\cdot\mid E_{\rm tot}=k\delta)$. It is the conditioning of the same law at each energy. The raw shell mass is $Z_k=\binom 5k>0$, so the probability of that shell before conditioning is $Z_k/32$. This fixes all relative shell normalizations independently of the target. Both maps preserve each shell and its conditional law. The normalized depth contributes exactly one to every retained state on every shell. In particular, with $\Omega_B(r\delta)=\binom4r$ on $0\le r\le4$ and zero elsewhere, the visible-cell weights are
$$
p_i^{(k)}=\mu_k\{i\}=\frac{\Omega_B(k\delta-e_i)}{Z_k}.
$$
This is the fibre-mass step of GR:58 for this reference. At a given $k$, conditioning on $i$ restricts the boundary bits to a different excitation layer for each $i$. The common law here is a joint law before conditioning.

**Paired rates.** Fix a shell and write $M_i$ for its visible cells. For a transition set $X_{ij}=\{x\in M_i:\varphi(x)\in M_j\}$, the map $x\mapsto\Theta\varphi(x)$ sends $X_{ij}$ into $X_{ji}$. Applying it a second time returns $x$, by the reversal relation, and both maps in the composition preserve $\mu_k$. Hence $J_{ij}=\mu_k(X_{ij})=J_{ji}$. With $T_{ij}=J_{ij}/p_i^{(k)}$ for $p_i^{(k)}>0$, this gives $p_i^{(k)}T_{ij}=p_j^{(k)}T_{ji}$. This replaces trajectory counts by mass in GR:68–70. The general GR formula compares the reversed labels if reversal permutes the cells. Here $\Theta$ fixes each cell. This argument uses the same mass step as P6 and supplies the shell weights by the explicit $\lambda$ above.

For $1\le k\le4$, an upward transition has $(i,b_1)=(0,1)$ and a downward transition has $(i,b_1)=(1,0)$. In each case the other three bits carry $k-1$ excitations, giving $\binom3{k-1}$ retained states and strict positivity in both directions. Consequently
$$
J_{01}=J_{10}=\frac{\binom3{k-1}}{Z_k},\qquad
T_{01}=\frac{k}{4},\qquad T_{10}=\frac{5-k}{4},\qquad
\frac{T_{01}}{T_{10}}=\frac{p_1^{(k)}}{p_0^{(k)}}=\frac{\Omega_B((k-1)\delta)}{\Omega_B(k\delta)}.
$$
In particular at $k=2$ the cell counts are $6$ and $4$, the two fluxes are $3/10$, and the two rates are $1/2$ and $3/4$. Equal flux here coexists with unequal transition probabilities. At the endpoint energies $k=0,5$ only one cell is occupied, so those shells do not test the paired log ratio.

**Counting and the slope test.** Even if the four modes are assigned nominal area $A=4\epsilon^2$, the count of all boundary configurations $2^4$ is a capacity. Energy-resolved multiplicities at $\delta$ and $2\delta$ are $4$ and $6$ at the same area. Their log difference $\ln(3/2)$ cannot be represented by $\sigma A/\epsilon^2+C$ at both energies for fixed $\sigma$ and $C$. This is a fixed-area reference with no assumed horizon first law. The failure of an inference from the number of modes to the energy-dependent weights can also be seen by comparing signs within the very same law. From $2\delta$ to $3\delta$ the log count decreases from $\ln 6$ to $\ln 4$. A positive-$\kappa$, positive-$\sigma$ boundary first law would require an increasing entropy over that interval if the energies were identified. The example tests what normalized depth and reversibility imply about the count. The identification of the model energies with horizon energies is a separate input.

For the exact gap $\delta$, writing $s_B(r\delta)=\ln\Omega_B(r\delta)$ on the occupied boundary layers gives
$$
-\frac{\ln(T_{01}/T_{10})}{\delta}
=\frac{s_B(k\delta)-s_B((k-1)\delta)}{\delta}
=\frac{1}{\delta}\ln\frac{5-k}{k}.
$$
This divided difference is positive at $k=2$ and negative at $k=3$. Its derivation involves no rate approximation. For perturbed rates of the form $\widehat T_{ij}=T_{ij}(1+\zeta_{ij})$ with $\lvert\zeta_{ij}\rvert\le\eta<1$, the log ratio changes by at most $2\eta/(1-\eta)$, by applying the mean value bound for $\ln$ to the two relative factors. This only gives slope control on shrinking gaps if the corresponding log error divided by the gap tends to zero. The reference has positive rates and an exact discrete gap. It supplies no shrinking-gap family with a controlled derivative and no detector transition. Its finite difference does not test the horizon infrared slope.

## 2. What the supplied scalar slope would give

The exact counting and flux steps above replace finite total counting in this reference. To obtain the classical horizon temperature from shell statistics still requires a separate input: the classical positive-rate slope $\beta_E$ at the boundary first-law value. In the GR counting route this would come from identifying the energy variation of the hidden reservoir's log count $s_H(E)=\ln\Omega_H(E)$ with that of $\sigma A/\epsilon^2$ and identifying the reservoir energy with the first-law energy (GR:58). The corresponding quantity in §1 is $s_B$. The total shell mass $Z_k$ normalizes the visible weights and cancels from their ratio. A direct rate-slope result would also suffice (GR:74, :86). On a horizon with the stated boundary count and $dE=(c^2\kappa/(8\pi G))\,dA$, the boundary calculation with $S$ in nats gives
$$
\beta_E=\frac{8\pi G\sigma}{c^2\kappa\epsilon^2},\qquad
k_BT_{\rm cl}=\frac{1}{\beta_E}=\frac{c^2\kappa\epsilon^2}{8\pi G\sigma}.
$$
GR:98–102 gives the boundary value under its mode-counting conditions, and GR:617 separates that value from its identification with a shell temperature. The identification is not proved by the reference.

For the scalar implication, suppose the same operational excitation and de-excitation are tracked at classical energy gap $x=E(\omega)>0$ and detector frequency gap $\omega>0$. Assume $E(0)=0$, a finite right derivative $a_*=E'(0^+)$, positive rates on the compared gaps approaching zero, and controlled log expansions
$$
-\ln R_E(x)=\beta_E x+o(x),\qquad -\ln R_\omega(\omega)=\tau_K\omega+o(\omega).
$$
Here $R$ means the excitation rate divided by the de-excitation rate in the corresponding description. Each expansion includes any error of the rate description at that gap. Assume $\ln R_E(E(\omega))-\ln R_\omega(\omega)=o(\omega)$, as would hold for an exact match without approximation. Since $E(\omega)=a_*\omega+o(\omega)$, dividing the matched expansions by $\omega$ and taking the limit gives $\beta_E a_*=\tau_K$. A single discrete paired transition like the one in §1 cannot establish these hypotheses. The identification of transitions is essential to this argument. The proof uses the two slopes and does not establish full H-balance or an exact Gibbs spectrum.

With $\tau_K=2\pi c/\kappa$ supplied by the horizon detector condition, the action scale becomes
$$
a_*=\frac{\tau_K}{\beta_E}=\frac{c^3\epsilon^2}{4G\sigma}.
$$
Writing $\hbar$ for the calibrated action scale and $\ell_p^2=G\hbar/c^3$ gives $\epsilon=2\sqrt{\sigma}\,\ell_p$ and $S_{\rm hor}=\sigma A/\epsilon^2=A/(4\ell_p^2)$ under the stated boundary entropy count. At the exact de Sitter calibration $\kappa=cH$, the matched temperature is $k_BT_{\rm cl}=\hbar\kappa/(2\pi c)=\hbar H/(2\pi)$. The $\hbar$ relation is conditional on the supplied slopes and transition match. It fixes a relation among $\hbar$, $\epsilon$ and $\sigma$. Choosing $\sigma=1$ would require its own mode-entropy input (GR:102). The $1/4$ inherits the calibration hypotheses (GR:302–316, :623–629, book/ch07-gravity.md:50–57).

## 3. Hypotheses and existing evidence

| Input or obligation | Status |
|---|---|
| Bit energies with no interaction energy, decoupled depth with zero energy, its geometric probability law and four boundary modes | Specified in §1 for this example. Additivity and zero deep energy are model inputs. The total carrier is infinite, the retained subsystem finite. |
| One raw counting mass on retained states and the same deep factor at every energy | Specified. Normalization, cross-energy shell masses, and cell conditioning are proved in §1. GR:58's route on `main` uses uniform counting on the finite total shell with negligible interaction at the shell scale. Main:728 (iv) concerns a reference measure for constructed realizations. A physical law supplying these shell weights remains open. |
| Shell conservation, invariant law for the update and reversal, time-even visible cells | Proved for the chosen swap and identity reversal. GR:68–70 carries the general reversal relation and the time-even-cell requirement for symmetric flux in the original calculation. No invariance of the shell conditional at fixed visible label is needed. |
| Positive paired rates, relative error and rate limit | Rates and finite differences are exact at each interior shell of the model. The relative-error estimate is proved when the stated relative bound holds. Positive rates on gaps tending to zero, the two controlled log slopes and compatible gap regularity are hypotheses of §2. They are open for the proposed shell-to-detector use of this model. |
| Horizon mode identification, entropy per mode and energy identification | Named GR inputs (GR:58, :98–102, :617, :665). Main:46 gives the observer's finiteness in its own scope. The boundary mode unit, the hidden-reservoir entropy–energy relation and the identification with the energy of the horizon first law remain to be justified for the physical shell. The reference disproves an inference from its structural counting and symmetry inputs alone. |
| Classical rate slope at the first-law value | Named input of the scalar implication (GR:74, :86). The first-law algebra is given in §2. Its realization by the shell rates is open. |
| Detector slope, horizon and frame | H-slope on the same rates is a named hypothesis. GR's exact de Sitter calibration (GR:56, :74–78, :623–627 and §8.5(b)) carries H-frame, H-Hawking and local boost structure. H-spectrum is sufficient for H-balance, which supplies H-slope under those conditions. The freely falling frame and cutoff state are among the open physical inputs. No detector slope or horizon conditions are established here. |
| Matching the same classical and frequency-resolved transitions | Named operational requirement in GR:70, :74–86. Its realization and the corresponding controlled gap map are open. Equal boundary area or equal probability data alone give no such identification. |

`ShellAssignment.lean:69, :90` checks invariance of counting weights on a specified invariant finite shell, without finite-type assumptions for the ambient types in those two lemmas. `:104, :119` uses the finite hidden sum for the actual correlated joint state, and `:119` requires nonzero conditioning mass. The measure in §1 and the GR detector match are separate from those results. In the separate finite-matrix representation question, `CoherentLift.lean:371` constructs a stationary state with the specified readout from the probability mixture. `:392` extracts such a mixture from representation with distinct energies, under its stated matrix hypotheses. Neither direction selects a physical shell or identifies detector transitions.

## 4. Coupled case · first missing item

**Missing: the shell family.** For the coupled extension without total finiteness, the traced sources supply no shell family with the needed cross-energy weights and invariances. The retained shell would have to be shown closed under both the update and reversal, or a defined full shell would have to supply the retained weights and the projected paired flux. The cited finite-shell lemmas start with a specified invariant finite shell. Their invariance checks do not construct the required coupled family.

GR:128 rules out slow H-BD ($\tau_{BD}>2\Delta t$) in its stated finite linear/reference class when a nonzero deep term enters the retained update. GR:118, :126 bound transition-probability error in their finite, uniform-prior scope. That bound alone gives no relative control near vanishing rates and provides no energy-shell family. The coupled investigation stops at the shell-family obligation.

**Disposition.** The decoupled example proves the fibre-weight and reciprocal-flux steps without total finiteness. It does not supply the target counting slope. The temperature and calibration chain survives as a conditional scalar implication under the supplied slopes and operational match. No physical recovery is credited. Physical source remains **NOT PASSED**.
