# P7-B · Horizon counting step from a finite boundary-mode count

**Status.** Paper-only check, not yet independently reviewed. Outcome: the counting step holds without total finiteness only conditionally on a supplied slope, in a decoupled scope and under a specified hidden law. The unconditional replacement, finite boundary count in place of A1 with nothing else changed, is refuted by an explicit counterexample (node 5). The coupled case is parked at the invariant-law step (node 6.3). No physical recovery is credited; physical source not passed. A1 is neither assumed nor asserted.

**Authority.** Owner `amaybaum`, 2026-11-16, recorded in [#1169 comment 6923725531](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6923725531) (posted 2026-11-16 17:21 UTC): "Proceed as suggested". The comment records this as the answer to the proposal "authorize item 1 now and item 2 alongside it", item 1 reading: "**P7-B (boundary count).** Can the horizon calibration's counting step use the finite boundary-mode count, from Main Lemma 1's finite-area-boundary argument applied to the horizon, in place of total finiteness?" with open links "identifying Lemma 1's ε with the boundary mode-counting unit" and "deriving the entropy slope from that count". The same comment records as not authorized: "manuscript or Lean edits, and merges. A1 stays open and unadopted; A4 is unchanged."

**Source pin.** `main` at `9b2ecf86f3d68b295020250cb3220e57f7796684`. `GR:n`, `Main:n`, `SM:n`, `Substratum:n` are line `n` of `papers/<name>.md`; `ch07:n` is line `n` of `book/ch07-gravity.md`.

**References and their role (§A.42 item 8).**

| Reference | Classification |
|---|---|
| #1169 comment 6923725531 | Provenance: the authority quoted above. No claim uses its content. |
| Draft PR #1319, commit `971ac0366d4077549ef6bc1755d8b0a5a2208662`, `P7-SHELL-CALIBRATION.md` (first P7 check) | Provenance only. Every step taken from it (the four-bit decoupled shell, its cell weights and fluxes, the scalar matching argument) is restated and proved below; no claim here rests on that commit. |
| `verification/audits/foundations/p6-reciprocity-20261116/P6-RECIPROCITY.md` | Support on `main`. The reciprocal-flux step is also re-proved in node 6.1 for the laws used here. |
| `verification/audits/foundations/a1-recovery-matrix-20261116/RECOVERY-MATRIX.md`, P7 row (lines 58–80) | Support on `main` for the decomposition of the P7 obligations; cited for comparison only. |

## Question

GR:58 runs the classical horizon temperature as a counting derivative "under A1", and its hidden-sector condition **H-count** opens with "that the total system is finite (A1)". Can that counting step use instead only a finite boundary-mode count $N(A)=A/\epsilon^2$ (entropy $\sigma A/\epsilon^2$), obtained from Main Lemma 1's argument (Main:46) with the horizon as the bounding surface, without assuming that the whole hidden sector is finite?

## 0. Productivity test (fixed before node 1)

The check counts as productive iff it yields a statement strictly stronger than "the boundary count is finite and A1 is open", and in addition either (i) proves a replacement of A1 at the counting step with every hypothesis listed, or (ii) exhibits an explicit model in which a finite boundary count with an infinite hidden sector leaves the shell weights or the slope undetermined or wrong, or (iii) identifies a load-bearing assumption of the counting step not recorded at GR:58, :74, :86, :98–104 or :665–669. Otherwise the outcome is recorded as a relabelling. Favourable branches (any branch in which the replacement appears to work) are re-examined in node 7 before acceptance.

## Hypotheses

Statuses: **on main** (cited where stated); **proved here**; **posited** (an input this record does not derive); **open**.

| Id | Hypothesis | Status |
|---|---|---|
| H1 | The visible configuration set $\mathcal C_V$ is finite. | On main: Main:42 (finite-capacity clause of the Definition), Main:46 (Lemma 1), Main:60 ("only finite visible resolution is a theorem"). |
| H2 | At each relevant horizon area the hidden boundary configuration set $\mathcal C_B(A)$ is finite (finite alphabet $q$ per mode, finitely many modes). | Posited. Not implied by H1 or by Lemma 1 (node 2.3). GR:132 carries finite alphabets on $V\cup B_n$ as hypothesis (D4). |
| H3 | Mode count $N(A)=A/\epsilon_c^2$ with counting unit $\epsilon_c$; S3: $\epsilon_c$ equals Lemma 1's $\epsilon$. | On main as named condition S3 (GR:665, :669). Not derivable from Lemma 1 (node 4.2). Under H-link on the cubic lattice, false with unit $\epsilon^2$ for a spherical horizon (node 4.4, proved here). |
| H4 | Hidden energy carried by the boundary configurations only; deep coordinate of zero energy; shell law $\#_{\mathcal C_V\times\mathcal C_B}\otimes\nu$ restricted to the shell, with one normalized deep law $\nu$ fixed independently of $b$ and of the energy. | Posited. Law form of H-count's deep clause; a specification of this kind is necessary once the deep sector is infinite (node 5). |
| H5 | The shell law is invariant under $\varphi$ and $\Theta$. | Proved here for decoupled product dynamics (node 6.3). Fails for an explicit deep-coupled energy-conserving bijection (node 6.3); coupled case open. |
| H6 | Density-of-states clause of H-count: $\ln\Omega_B(x)=\sigma A(x)/\epsilon_c^2+C$ for hidden energies $x$ in the shell range, $A(x)$ the area attached to $x$ by the horizon first law. | On main as the second clause of H-count (GR:58), a named condition. Not implied by H2–H3 (node 3.1). Posited. |
| H7 | Horizon first law $dE=c^2\kappa\,dA/(8\pi G)$; on exact de Sitter $E=c^4R/G$, $A=4\pi R^2$, $\kappa=c^2/R$. | On main: GR:56, :58, :98 (Jacobson [1]). Classical input. |
| H8 | Visible cells time-reversal even ($\theta=\mathrm{id}$). | On main as named condition: GR:68, :669. |
| H9 | Positive paired flux $J_{01}>0$ on the compared shell. | Model hypothesis; holds in the models of nodes 5–6; open for the physical shell. |
| H10 | Regularity of the log-rate slope: (a) smooth interpolant $\sigma A(x)/\epsilon_c^2$ in place of the integer count, or (b) H-quant: the hidden energies of the compared cells lie where $A(x)/\epsilon_c^2\in\mathbb Z$. | (a) posited (continuum idealization); (b) posited. Derivative form unavailable from an integer count, proved here (node 3.4); discrete-gap form exact under (b), and bounded by $\sigma/\delta$ without it, proved here. |
| H11 | Detector side: H-slope (GR:74) for the derivative form; H-balance at the finite compared gaps (GR:62–66) for the discrete form. | On main as named conditions; open. |
| H12 | Identification of the classical shell transitions with the frequency-resolved detector transitions, with $E(\omega)=a_*\omega+o(\omega)$. | On main as named requirement (GR:70, :74–86); open. |
| H13 | Exact de Sitter calibration, H-frame, H-Hawking, local boost structure (GR:56, :88, :623, :649). | On main as named conditions; (iv), (v) of H-Hawking discharged there, the rest open. |
| H14 | Entropy per mode $\sigma$. | On main: GR:98–102, not fixed by the count. Under the exact counting form of H6 at all mode numbers $N\ge N_0$, $\sigma=\ln m$ for an integer $m\ge2$ (node 3.5, proved here). |

## 1. Where A1 enters P7, and what the step needs

| Locator | Use of A1 | Need served |
|---|---|---|
| GR:58, first sentence | "Under A1, restrict the finite total system to a conserved energy shell"; uniform counting gives $P(i)=\Omega_H(E-e_i)/\sum_j\Omega_H(E-e_j)$. | (a) |
| GR:58, H-count first clause | "that the total system is finite (A1)". | (a) |
| GR:58, H-count second clause | $s_H=\sigma A/\epsilon^2$ up to an energy-independent constant, $E$ the first-law energy, deep sector contributing no energy-dependent multiplicity and no energy. | (b) |
| GR:68–70 | $N_i=\lvert M_i\rvert$, $N_{ij}=\lvert\{x\in M_i:\varphi(x)\in M_j\}\rvert$: finite counts on the shell of GR:58; $\beta_E=s_H'(E)$ at its H-count value. | (a), (b) |
| GR:74, :78, :86 | $\beta_E$ "under H-count"; H-slope; identification of transitions. | (b), (d) |
| GR:98–104, :156, :665, :669 | One mode per cell of area $\epsilon^2$; S3; "A1 … supplies neither the discreteness scale $\epsilon$ nor its identification with the boundary mode-counting unit". | (c) |
| GR:617 (U1), :623 (b) | Identification of $T_{\rm cl}$ with the shell temperature "under H-count". | (b) |
| ch07:52 | Book mirror of H-count, including "the total system is finite (A1)". | (a), (b) |
| Main:111, :728 (ii) | Total finiteness of the hidden sector as the total-finiteness posit, open, not adopted. | (a) |

**Separation of needs.** (a) finiteness of the counted set; (b) the relative density of states across energies, i.e. the entropy slope $\beta_E=\partial s_H/\partial E$; (c) the identification of $\epsilon$ with the boundary counting unit; (d) the operational match to the detector.

**What A1 does at (a).** Three distinct things: (a1) $\Omega_H(E)$ is finite, so $s_H=\ln\Omega_H$ is defined and $P(i)$ is a ratio of finite numbers; (a2) the uniform law on the finite shell exists and is invariant under every shell-preserving bijection, so no law adapted to $\varphi$ has to be chosen; (a3) the clause "the deep hidden sector contributing no energy-dependent multiplicity" becomes an equation between finite cardinalities, $\lvert\mathcal C_D(x)\rvert$ independent of $x$.

**What A1 does not do.** (b): a finite set admits every energy-resolved profile (node 3.1), so finiteness fixes no slope; the slope is H-count's second clause. (c): GR:669 states that A1 supplies neither $\epsilon$ nor its identification. (d): H-slope and the transition identification (GR:70, :74, :86) are stated independently of any cardinality.

**Verdict, node 1.** A1 enters P7 at GR:58 only (twice), with GR:68–70 inheriting its finite counts and ch07:52 mirroring it. Its role is confined to (a), in the three forms (a1)–(a3). The question reduces to whether (a1)–(a3) can be supplied without total finiteness.

## 2. Does Lemma 1 supply (a) for the boundary modes?

**2.1 What Lemma 1 proves.** The Definition (Main:42) requires the observer $V$ to have "finitely many distinguishable internal states". The first clause of Lemma 1 ($\mathcal C_V$ finite) is that requirement restated; Main:60 records it as the one theorem among the early commitments, "from the finite-capacity clause of the Definition", and Main:728 records that "visible finiteness is stipulated per moment rather than derived". The second clause, "a discreteness scale $\epsilon$ providing a finite minimal cell volume", has no derivation in Main: a finite set of states carries no length scale, and Main:222 refers to "an assumed discreteness scale $\epsilon$". The sentence "Any observer bounded by a finite-area surface can couple to only finitely many modes across that boundary" (Main:46) and GR:565's "classical fact that finite-area boundaries admit finitely many modes" are motivation: a continuum field on a sphere has infinitely many modes (the spherical harmonics of every degree), so the statement holds only once a minimal cell is given, i.e. it presupposes $\epsilon$. Holographic bounds [2] are cited as external support.

Classification: $\mathcal C_V$ finite — proved (immediate from the Definition). $\epsilon$ and "finite area $\Rightarrow$ finitely many coupled modes" — motivated, not proved.

**2.2 Is the horizon an observer?** In Main:42 an observer is a subsystem $V$ with finitely many distinguishable states. In GR:40 the observer is the interior and the horizon is the interface; the counted set of GR:58 and GR:116 is the hidden-side boundary configuration set $\mathcal C_B\subset$ hidden sector. The horizon (a surface) is not a subsystem, and $B$ is not $V$. Declaring $B$ an observer would make finiteness of $\mathcal C_B$ an instance of the Definition's stipulation, i.e. a posit about $B$, not a transfer of a proof. Nothing in Main licenses inferring finiteness of the hidden side from finiteness of the visible side.

**2.3 Counterexample: finite observer, one coupled mode, infinite boundary configuration set.** Let $V=\{0,1\}$, one boundary mode $b\in\mathbb Z$, and
$$
\varphi(v,b)=(v\oplus\mathbf 1_{\{b=0\}},\,b+1),\qquad \varphi^{-1}(v,b)=(v\oplus\mathbf 1_{\{b=1\}},\,b-1).
$$
Check of the inverse: $\varphi(v,b)=(v',b+1)$ with $v'=v\oplus\mathbf 1_{\{b=0\}}$, and $v'\oplus\mathbf 1_{\{b+1=1\}}=v$. So $\varphi$ is a bijection; the visible bit is flipped when $b=0$, so the coupling is nontrivial. The observer has two states and couples through exactly one mode, yet $\mathcal C_B=\mathbb Z$ is infinite. Moreover no normalized law on $\mathbb Z$ is invariant under $b\mapsto b+1$ (invariance forces equal point masses, whose sum is $0$ or $\infty$), so not even a normalized invariant boundary law exists here. A finite number of coupled modes therefore yields neither a finite boundary configuration count nor a finite boundary entropy without a separate finite-alphabet input (H2; GR:98 "a mode with $q$ internal states"; GR:132 (D4)).

**Verdict, node 2.** Lemma 1 does not supply (a) for the boundary modes. It proves finiteness of $\mathcal C_V$ from the Definition and motivates, without proving, a finite mode count across a finite-area surface; that motivation presupposes $\epsilon$ (node 4) and, for a finite configuration count, a finite alphabet per mode. Finiteness of $\mathcal C_B(A)$ is posit H2. This agrees with the P7 row of the recovery matrix on `main` (GR's mode count is "an extra GR condition … rather than an implication of Main:46") and adds the explicit counterexample 2.3. Classification: CONFIRMING, with the counterexample ELABORATING.

## 3. Does a finite boundary count give the entropy slope?

**3.1 Lemma (a count fixes no profile).** Let $\mathcal C$ be a finite set with $\lvert\mathcal C\rvert=M$, let $x_1<\dots<x_k$ be energies and $m_1,\dots,m_k\ge0$ integers with $\sum_r m_r=M$. Then there is $E_B:\mathcal C\to\{x_r\}$ with $\lvert E_B^{-1}(x_r)\rvert=m_r$ for every $r$.

*Proof.* Partition $\mathcal C$ into blocks of sizes $m_1,\dots,m_k$ and assign $x_r$ to the $r$th block. $\square$

So the boundary count $M=q^{N(A)}$ fixes $\sum_x\Omega_B(x)$ and no ratio $\Omega_B(x)/\Omega_B(x')$: the capacity, not the relative density of states. The same holds for any finite total system, which is why A1 does not supply (b) either.

**3.2 Fixed-area example (reproduced from the first P7 check).** Four boundary bits $b\in\{0,1\}^4$ with $E_B(b)=\delta\lvert b\rvert$, $\lvert b\rvert=\sum_\ell b_\ell$, $\delta>0$. Then $\Omega_B(r\delta)=\binom4r$, i.e. $1,4,6,4,1$ for $r=0,\dots,4$. At fixed nominal area $A=4\epsilon^2$ the quantity $\sigma A/\epsilon^2+C$ is one number, while $\ln\Omega_B(\delta)=\ln4\neq\ln6=\ln\Omega_B(2\delta)$; and between $2\delta$ and $3\delta$ the log count decreases, whereas a first law with $\kappa,\sigma>0$ requires it to increase if these energies were identified with first-law energies. The energy-resolved count at fixed area is the boundary's own profile, unrelated to $\sigma A/\epsilon^2$.

**3.3 What supplies the slope.** The slope enters through H6, the second clause of H-count: the multiplicity at hidden energy $x$ is $e^{C}e^{\sigma A(x)/\epsilon_c^2}$ with $A(x)$ the area attached to $x$ by the first law H7. Given H6 and a shell law that weights each boundary configuration equally (node 6.2), the visible weights are
$$
p_i=\frac{e^{\sigma A(E-e_i)/\epsilon_c^2}}{\sum_j e^{\sigma A(E-e_j)/\epsilon_c^2}},
$$
and on exact de Sitter, where $A(x)=4\pi G^2x^2/c^8$,
$$
\ln\frac{p_0}{p_1}=\frac{\sigma}{\epsilon_c^2}\big(A(E)-A(E-\delta)\big)=\frac{4\pi\sigma G^2}{c^8\epsilon_c^2}\,(2E\delta-\delta^2)=\beta_E\!\left(E-\tfrac{\delta}{2}\right)\delta,
\qquad
\beta_E(x)=\frac{8\pi\sigma G^2x}{c^8\epsilon_c^2}=\frac{8\pi G\sigma}{c^2\kappa(x)\epsilon_c^2},
$$
for $e_0=0$, $e_1=\delta$, using $\kappa(x)=c^2/R=c^6/(Gx)$. This is exact: the divided difference over the gap equals $\beta_E$ at the midpoint hidden energy, and $\beta_E(E-\delta/2)=\beta_E(E)(1-\delta/(2E))$ carries the finite-reservoir correction of GR:58.

The count enters only as the numerical form of H6; the slope is supplied by H6, not derived from the count (3.1). Two readings of H6 are possible, and both are posits. (i) On a fixed visible/hidden partition (Main:42; the fixed $B$ of GR:112–126), the boundary site set and its capacity are fixed, and H6 asserts an energy-resolved profile $\ln\Omega_H(x)=\sigma A(x)/\epsilon_c^2+C$ below the capacity energy; by 3.1 this is not a consequence of the capacity. (ii) If instead the counted boundary at hidden energy $x$ is the horizon of area $A(x)$, the partition varies with the hidden energy, which the fixed-$V$ Definition of Main:42 does not provide, and H6 then asserts that every configuration of that boundary has hidden energy $x$ (energy a function of area alone).

**3.4 Regularity of the slope.** A mode count is an integer. With $N(x)=\lfloor A(x)/\epsilon_c^2\rfloor$ and the exact counting form, $s_H(x)=\sigma N(x)+C$ is a step function of $x$.

- *No derivative at zero gap.* If $A(E)/\epsilon_c^2$ is an integer, then for all small $\delta>0$, $N(E)-N(E-\delta)=1$, so $\ln(p_0/p_1)=\sigma$ and the divided difference $\sigma/\delta\to\infty$. If $A(E)/\epsilon_c^2$ is an integer plus $\tfrac12$, then for small $\delta$ the floors agree and the divided difference is $0$. So the classical rate ratio is not a function of the gap below one mode step, and the derivative form $-\partial_{\Delta E}\ln R_E|_0=\beta_E$ used at GR:74 has no counterpart for the integer count. The derivative form requires the smooth interpolant (H10(a)), a posit.
- *Finite gaps.* Since $\lvert\lfloor u\rfloor-\lfloor v\rfloor-(u-v)\rvert<1$, $\big\lvert\ln(p_0/p_1)-\beta_E(E-\delta/2)\,\delta\big\rvert<\sigma$, so the divided difference is within relative error $\sigma/(\beta_E\delta)$ of the midpoint slope. At thermal gaps, $\beta_E\delta=O(1)$, this bound is of order $\sigma$, not small.
- *Exact discrete form.* Under H-quant (H10(b)) the floors are exact and the midpoint formula of 3.3 holds exactly on the compared gaps. One mode step costs hidden energy $\Delta x$ with $\sigma=\beta_E(\bar x)\Delta x$ at the midpoint $\bar x$, i.e. $\Delta x\approx\sigma k_BT_{\rm cl}$: a single mode step is a thermal-scale transition.

Consequence for the matching (H11): with the integer count, the classical side supplies exact finite-gap ratios $\ln(p_0/p_1)=\sigma n$ for $n$ mode steps, to be matched against the detector at the corresponding finite gaps $\omega_n$, which is H-balance at those gaps rather than H-slope at $\omega\to0$. If H-balance holds there, $\tau_K\omega_n=\sigma n=\beta_E(\bar x_n)x_n$, so $x_n/\omega_n=\tau_K/\beta_E(\bar x_n)=\frac{c^3\epsilon_c^2}{4G\sigma}\big(1-\tfrac{x_n}{2E}\big)^{-1}$. The derivative form of GR:74 holds for the smooth interpolant (H10(a)). Neither A1 nor its absence changes this; GR:58, :74, :86 do not record it.

**3.5 Side result: $\sigma$ under the exact counting form.** *If $\Omega(N)=Ke^{\sigma N}$ is a positive integer for every integer $N\ge N_0$, with $K>0$, then $e^\sigma$ is a positive integer.* Proof: $r=e^\sigma=\Omega(N_0+1)/\Omega(N_0)$ is rational; write $r=a/b$ in lowest terms. Then $\Omega(N_0+k)=\Omega(N_0)a^k/b^k\in\mathbb Z$ for all $k\ge1$, so $b^k\mid\Omega(N_0)$ for all $k$ (as $\gcd(a,b)=1$), which forces $b=1$. $\square$ Hence H6 in exact form gives $\sigma=\ln m$, $m\ge2$ an integer, and the value $\sigma=1$ used for the quoted numbers (GR:102, :306) is available only if H6 holds up to energy-dependent corrections: for example a configuration set of size $\lfloor e^N\rfloor\le 3^N$ (any subset of $\{0,1,2\}^N$ of that size, not a product of independent modes) has $\ln\lfloor e^N\rfloor=N+O(e^{-N})$. GR:102 already records $\sigma=1$ as an assumption and as unavailable for $q=2$; this sharpens it for the exact counting form. Classification: ELABORATING.

**Verdict, node 3.** A finite boundary count does not supply (b). The slope is supplied by H6, a posited density of states; given H6 and an equal-weight boundary law, the slope algebra is exact on de Sitter (3.3). The derivative form additionally needs the smooth interpolant; the integer count gives an exact discrete-gap form under H-quant and an $O(\sigma/\delta)$ error otherwise (3.4, proved). Classification: CONFIRMING for 3.1–3.3 (first P7 check, recovery matrix); NEW for 3.4 relative to GR:58, :74, :86.

## 4. Is the identification of $\epsilon$ with the boundary counting unit derivable?

**4.1 The two scales.** Lemma 1's $\epsilon$ is the observer's resolution: the minimal cell volume of $\mathcal C_V$ (Main:46), assumed rather than derived (2.1). The counting unit $\epsilon_c$ is the horizon area per hidden-side boundary mode across which $H_{\rm int}$ couples (GR:98, :104). GR:98 and GR:156 make "one mode per cell of area $\epsilon^2$" definitional given that $\epsilon$ is "the minimal distinguishable scale (Lemma 1)"; but "distinguishable" refers to the observer's distinctions, while the counted modes are hidden-side. GR:665 (S3) names the identification as an additional requirement and GR:669 states that A1 does not supply it.

**4.2 Counter-model to derivability from Lemma 1.** Take visible sites on a cubic lattice of spacing $\epsilon_V$ and a hidden boundary layer with one coupled mode per area $\epsilon_B^2$, $\epsilon_B=2\epsilon_V$ (for instance one hidden mode coupled to each $2\times2$ block of visible boundary cells). Lemma 1's conclusions hold with $\epsilon=\epsilon_V$; the boundary count is $A/\epsilon_B^2$. Nothing in Main:42–46 or in A1 excludes this. With H6 at $\epsilon_c=\epsilon_B$ the calibration gives $a_*=c^3\epsilon_B^2/(4G\sigma)$, not $c^3\epsilon_V^2/(4G\sigma)$. So (c) is independent of Lemma 1.

**4.3 The homogeneity route reintroduces finiteness.** Equality of spacings across the cut would follow from translation invariance of the substratum across it (A4, Main:728 (xi)) with site factorization (viii). A4 as stated (Substratum:98) takes the coupling graph to be "a finite periodic lattice, the quotient of a rank-$d$ lattice by a finite-index sublattice", so this route uses total finiteness of the coupling graph. An A1-free version needs translation invariance on an infinite lattice, which A4 as stated does not provide: a further posit.

**4.4 Orientation dependence of the link count.** GR:104 reads the count through H-link (SM:12; GR:104): each of the $2d=6$ components couples across one link, and "a boundary cell on the horizon has exactly one outward-normal link crossing the partition", giving $\kappa_m=1$. On the simple-cubic coupling graph (Main:728 (x)) with spacing $\epsilon$, the number of crossing links depends on the orientation of the cut.

*Proposition.* Let $V_R=\{x\in\mathbb Z^3:\lvert x\rvert^2\le R^2\}$ (lattice units, $\epsilon=1$) with nearest-neighbour edges. The number of edges with exactly one endpoint in $V_R$ is exactly $6\,N_2(R^2)$, where $N_2(R^2)=\#\{(y,z)\in\mathbb Z^2:y^2+z^2\le R^2\}$. Consequently it equals $6\pi R^2+O(R)=\tfrac32\cdot4\pi R^2+O(R)$.

*Proof.* Fix a direction $e_j$ and a lattice line $\ell$ parallel to it, with transverse coordinates $(y,z)$. The ball is convex, so $\ell\cap V_R$ is a set of consecutive lattice points. If it is nonempty, exactly two edges of $\ell$ cross the boundary (one at each end); if empty, none. It is nonempty iff $y^2+z^2\le R^2$: if so, the point with zero coordinate along $e_j$ lies in $V_R$; conversely any point of $\ell\cap V_R$ has $y^2+z^2\le R^2$. Summing over the three directions gives $3\cdot2\cdot N_2(R^2)$. For the asymptotics, the unit squares centred at the points counted by $N_2$ cover the disk of radius $R-1/\sqrt2$ and lie in the disk of radius $R+1/\sqrt2$, so $N_2(R^2)=\pi R^2+O(R)$. $\square$

More generally, for a large planar patch of area $A$ with unit normal $n$, the links along $e_j$ crossing it are those whose starting site lies in a slab of thickness $\epsilon\lvert n_j\rvert$, so the crossing-link density is $(\lvert n_1\rvert+\lvert n_2\rvert+\lvert n_3\rvert)/\epsilon^2\in[1,\sqrt3]/\epsilon^2$, equal to $1/\epsilon^2$ only for axis-aligned planes; the sphere average of $\lvert n_j\rvert$ is $\tfrac12$, recovering $\tfrac32$. Counting hidden boundary sites instead of crossing links gives a different orientation-dependent density, $\max_j\lvert n_j\rvert/\epsilon^2$ by the same slab argument, again equal to $1/\epsilon^2$ only on axis-aligned planes.

*Check by exact enumeration.* Direct enumeration of cut edges (integer arithmetic, all sites in a bounding box, each of the three positive edge directions once) reproduces the identity and, as a control, the planar count:

| Cut | Cut edges | Comparison |
|---|---|---|
| cube $[0,L)^3$, $L=3,7,12$ | $54,\ 294,\ 864$ | $=6L^2$, surface area: density exactly $1/\epsilon^2$ |
| ball $R^2=100$ | $1902=6\cdot317$ | $1902/(4\pi\cdot100)=1.514$ |
| ball $R^2=400$ | $7542=6\cdot1257$ | $1.500$ |
| ball $R^2=1600$ | $30150=6\cdot5025$ | $1.500$ |
| ball $R^2=3600$ | $67734=6\cdot11289$ | $1.497$ |
| octahedron $\lvert x\rvert_1\le n$ | $6(2n^2+2n+1)$ (same line argument) | area $4\sqrt3\,n^2$, ratio $\to\sqrt3$ |

The proposition, not the table, carries the claim.

*Consequence, under H-link, the nearest-neighbour cubic graph, and a horizon that is a sphere in the lattice frame (H-frame) with the cut taken as the sites inside it.* The crossing-component density on the de Sitter horizon is $\tfrac32\sigma/\epsilon^2$ on average, i.e. $\kappa_m=\tfrac32$ in GR:104's notation $\eta=\kappa_m\sigma/\epsilon^2$. By GR:104's own formulas the Bekenstein–Hawking coefficient is unchanged ($S=\eta A=A/(4l_p^2)$, $\kappa_m$ cancels), while the calibration in terms of the lattice spacing becomes $\hbar=c^3\epsilon^2/(6G\sigma)$ and $\epsilon=2\sqrt{\kappa_m\sigma}\,l_p=\sqrt6\sqrt\sigma\,l_p$. The statement "exactly one outward-normal link" at GR:104 (and its mirror at ch07:59) holds for a planar cut orthogonal to a lattice axis. The relation $\hbar=c^3\epsilon_c^2/(4G\sigma)$ survives with the effective counting unit $\epsilon_c=\epsilon\sqrt{2/3}$ in place of the lattice spacing. Classification: NEW (no treatment of cut orientation was found in `papers/`, `book/` or `verification/` by searching for staircase, axis-aligned, normal link, crossing links, per unit area, spherical horizon). Not propagated here: manuscript edits are outside this authorization.

**Verdict, node 4.** (c) is an independent posit (S3). It is not derivable from Lemma 1 (4.2); the homogeneity route to it uses A4's finite periodic lattice (4.3); and under H-link the counting unit for a spherical horizon on the cubic lattice is $\tfrac23\epsilon^2$, not $\epsilon^2$ (4.4, proved).

## 5. Counterexample: finite boundary count, infinite hidden sector, undetermined slope

**Model.** Carrier $S=\{0,1\}\times\{0,1\}^4\times\mathbb N_0$ with points $(i,b,d)$; energies $e_i=\delta i$, $E_B(b)=\delta\lvert b\rvert$, deep energy $0$, $E_{\rm tot}=e_i+E_B(b)$. Dynamics $\varphi(i,b,d)=(b_1,(i,b_2,b_3,b_4),d)$ (exchange $i$ and $b_1$), time reversal $\Theta=\mathrm{id}$. $\varphi$ is an involution, preserves $E_{\rm tot}$, and satisfies $\Theta\varphi\Theta=\varphi^{-1}$; the visible cells are time-reversal even. The boundary count is finite (16 configurations, four modes) and the hidden sector is infinite.

**Shell $E_{\rm tot}=2\delta$.** Its finite part $P=\{(i,b):i+\lvert b\rvert=2\}$ has 10 points: cell $0$ ($i=0$, $\lvert b\rvert=2$) has 6, cell $1$ ($i=1$, $\lvert b\rvert=1$) has 4. The orbits of $\varphi$ on $P$ are: three fixed points $F_0$ in cell $0$ ($i=b_1=0$, two of $b_2,b_3,b_4$ equal to $1$); one fixed point $F_1$ in cell $1$ ($i=b_1=1$, $b_2=b_3=b_4=0$); three two-point orbits $O_r=\{(0,(1,r)),(1,(0,r))\}$ with $r\in\{100,010,001\}$. Check: $3+3=6$ and $1+3=4$.

**A family of invariant normalized laws.** For $\alpha,\beta,\gamma>0$ let $w=\alpha$ on $F_0$, $\beta$ on $F_1$, $\gamma$ on each point of each $O_r$, let $\nu(\{d\})=2^{-(d+1)}$, and let $\mu_{\alpha\beta\gamma}(\{(i,b,d)\})=w(i,b)\nu(\{d\})/Z$ with $Z=3\alpha+\beta+6\gamma$. Each $\mu_{\alpha\beta\gamma}$ is a probability law on the shell (deep sector infinite), invariant under $\varphi$ ($w$ is constant on $\varphi$-orbits and $d$ is fixed) and under $\Theta$. Its cell masses and fluxes are
$$
p_0=\frac{3\alpha+3\gamma}{Z},\quad p_1=\frac{\beta+3\gamma}{Z},\quad J_{01}=J_{10}=\frac{3\gamma}{Z},\quad
T_{01}=\frac{3\gamma}{3\alpha+3\gamma},\quad T_{10}=\frac{3\gamma}{\beta+3\gamma},
$$
so $T_{01}/T_{10}=p_1/p_0$ and the divided-difference slope is $b_\delta=-\delta^{-1}\ln(T_{01}/T_{10})=\delta^{-1}\ln\frac{3\alpha+3\gamma}{\beta+3\gamma}$. Every $t>0$ is a value of $\frac{3\alpha+3\gamma}{\beta+3\gamma}$: for $t>\tfrac12$ take $\beta=3\gamma$, $\alpha=\gamma(2t-1)$; for $t<2$ take $\alpha=\gamma$, $\beta=\gamma(6/t-3)$. Hence $b_\delta$ takes every real value, with positive rates in both directions throughout. The product law $\alpha=\beta=\gamma$ gives $p_0:p_1=6:4$ and $b_\delta=\delta^{-1}\ln\tfrac32$, the value of the first P7 check at this shell.

**The same family from finite truncations.** For positive integers $a,c,e$, let $g=a$ on $F_0$, $c$ on $F_1$ and $e$ on the points of each $O_r$ (constant on $\varphi$-orbits), and let $S_N=\{(i,b,d):(i,b)\in P,\ d<N\,g(i,b)\}$. Each $S_N$ is finite and $\varphi$-invariant (since $\varphi$ preserves $g$ and fixes $d$), and the uniform law on $S_N$ gives each $(i,b)\in P$ total mass proportional to $g(i,b)$, so its cell masses and fluxes are those of $\mu_{\alpha\beta\gamma}$ with $(\alpha,\beta,\gamma)=(a,c,e)$, independent of $N$. So every positive rational value of $\frac{3\alpha+3\gamma}{\beta+3\gamma}$ arises as the uniform-counting answer on a finite invariant truncation, and the truncations exhaust the infinite shell as $N\to\infty$.

**Where A1 makes the difference.** On a finite truncation, H-count's deep clause in its cardinality form (a3) — deep multiplicity independent of the hidden energy — forces $g$ to be constant on all points of hidden energy $2\delta$ (the points of $F_0$ and the cell-$0$ points of the $O_r$, so $\alpha=\gamma$) and on all points of hidden energy $\delta$ ($F_1$ and the cell-$1$ points of the $O_r$, so $\beta=\gamma$): the unique answer is $6:4$. On the infinite carrier every point of $P$ carries $\aleph_0$ deep states of zero energy for every profile, so the cardinality form of the deep clause holds for all of them and selects none.

**Lemma 5.1.** *No probability law on a countably infinite set $X$ is invariant under all permutations of $X$.* Proof: invariance under transpositions forces equal point masses $c$; countable additivity gives total mass $0$ ($c=0$) or $\infty$ ($c>0$). $\square$ So the A1 property (a2) — one law invariant under every shell-preserving bijection — has no counterpart on an infinite shell: a law has to be specified, and its invariance depends on $\varphi$.

**Verdict, node 5.** Counterexample. A finite boundary count together with an infinite hidden sector of zero deep energy, reversible energy-conserving dynamics, time-even cells, positive rates and normalized invariant laws leaves the visible weights and the log-rate slope undetermined: every real slope occurs. Under A1 with the deep clause the answer is unique. Replacing A1 therefore requires replacing (a2) and (a3) by a specified law (H4), not only (a1) by the boundary count. Classification: NEW (the cardinality form of the deep clause has no content on an infinite carrier).

## 6. Does a normalized invariant hidden law supply the slope?

**6.1 Reciprocity transfers the slope to the cell masses (re-proved).** Let $\mu$ be a probability law on a measurable carrier with a measurable readout $X$ into a finite visible set, cells $A_i=X^{-1}(i)$, a measurable bijection $\varphi$ with measurable inverse, a measurable involution $\Theta$ with $X\circ\Theta=X$ (H8) and $\Theta\varphi\Theta=\varphi^{-1}$, and $\mu$ invariant under $\varphi$ and $\Theta$. Put $R=\Theta\varphi$. Then $R^2=\Theta\varphi\Theta\varphi=\varphi^{-1}\varphi=\mathrm{id}$, and for $E_{ij}=A_i\cap\varphi^{-1}(A_j)$ and $x\in E_{ij}$: $X(Rx)=X(\varphi x)=j$ and $X(\varphi Rx)=X(\Theta x)=i$, so $R(E_{ij})\subseteq E_{ji}$, and by symmetry and $R^2=\mathrm{id}$, $R(E_{ij})=E_{ji}$. Since $\mu(R^{-1}E)=\mu(\varphi^{-1}\Theta^{-1}E)=\mu(E)$, $J_{ij}=\mu(E_{ij})=\mu(E_{ji})=J_{ji}$. With $T_{ij}=J_{ij}/p_i$, $p_iT_{ij}=p_jT_{ji}$, hence $T_{ij}/T_{ji}=p_j/p_i$ whenever $J_{ij}>0$. This is the P6 flux result on `main` specialized to $\theta=\mathrm{id}$, one step. It fixes the log-rate ratio entirely by the cell masses and says nothing about them; node 5 exhibits invariant normalized laws with every mass ratio. Invariance and normalization do not supply a relative density of states across energies.

**6.2 The specified law reproduces the finite answer, and only the boundary's own profile.** Under H4, let $P_E=\{(i,b):e_i+E_B(b)=E\}$ (finite by H1–H2) and $\lambda=\#_{P_E}\otimes\nu$ on $S_E=P_E\times D$, $D$ any measurable space with a probability $\nu$. Then $\lambda(\{i\}\times\{b:E_B(b)=E-e_i\}\times D)=\Omega_B(E-e_i)\,\nu(D)=\Omega_B(E-e_i)$, so with $Z=\sum_j\Omega_B(E-e_j)<\infty$,
$$
p_i=\frac{\Omega_B(E-e_i)}{Z},\qquad \ln\frac{p_i}{p_j}=\ln\Omega_B(E-e_i)-\ln\Omega_B(E-e_j).
$$
This is GR:58's formula with $\Omega_H$ replaced by $\Omega_B$, valid with the deep sector of any cardinality; in this precise sense the boundary count with H4 replaces (a1)–(a3). The slope is the boundary's energy-resolved profile, which equals the first-law value only under H6 (node 3).

**6.3 Invariance needs decoupling.** *Decoupled case (proved).* If $\varphi=\psi\times\chi$ with $\psi$ a permutation of $P_E$ and $\chi$ a $\nu$-preserving measurable bijection of $D$ with measurable inverse, then for rectangles $\lambda(\varphi^{-1}(R_1\times R_2))=\lvert\psi^{-1}R_1\rvert\,\nu(\chi^{-1}R_2)=\lvert R_1\rvert\,\nu(R_2)$. Rectangles form a $\pi$-system generating the product $\sigma$-algebra and containing $S_E$, so $\lambda\circ\varphi^{-1}=\lambda$ by Dynkin's $\pi$–$\lambda$ theorem; likewise for $\Theta=\theta_P\times\theta_D$. *Coupled case (fails in general).* Let the boundary be two bits each of energy $\delta$, $D=\mathbb N_0$ with $\nu(\{d\})=2^{-(d+1)}$ and zero deep energy, and let $\varphi$ exchange $((1,0),0)$ and $((0,1),1)$ and fix every other point. $\varphi$ is a bijection, conserves energy (both points have energy $\delta$) and couples boundary and deep coordinates; but $\lambda(\{((1,0),0)\})=\tfrac12\ne\tfrac14=\lambda(\{((0,1),1)\})$, so $\lambda$ is not invariant. Under A1 the uniform law is invariant for this map and every other shell-preserving bijection. The coupled case is therefore parked at the first missing item: an invariant shell law for a deep-coupled update, with weights fixed independently of the target slope. This is consistent with GR:128 (for linear updates, deep coupling $L\neq0$ excludes H-BD with $\tau_{BD}>2\Delta t$); GR:118, :126 bound transition-probability errors by $2t/\tau_{BD}$ in their finite uniform-prior scope, which gives no invariant law, and a log-rate bound from an $\ell_1$ bound needs rates bounded below ($\lvert\ln\hat T-\ln T\rvert\le\lvert\hat T-T\rvert/\min(\hat T,T)$), which those lines do not supply.

**6.4 A1 and the uniform law.** A1 makes the uniform law on a finite shell available; its selection is GR:58's uniform counting (the measure-selection item Main:728 (iv) for constructed realizations). Without A1 the corresponding specification is H4, whose invariance is specific to the dynamics (6.3) and whose selection is a posit of the same kind.

**Verdict, node 6.** A normalized invariant law does not supply the slope (6.1, node 5). The specified product law H4 supplies (a) in the decoupled scope and reproduces the A1 answer with $\Omega_B$ in place of $\Omega_H$ (6.2, 6.3); the slope still comes from H6. Coupled case parked. Classification: POSITIVE for the decoupled replacement of (a); CONFIRMING for 6.1 (P6).

## 7. Skeptical passes on the favourable branches

1. *Pass on 6.2–6.3 (replacement of (a) works).* Re-examined invariance: holds only for product dynamics (coupled counterexample found, 6.3). Re-examined the deep clause: its cardinality form is empty on infinite carriers (node 5). Both recorded.
2. *Pass on 3.3 (slope algebra exact on de Sitter).* Re-examined regularity: integer count gives a step function; derivative form needs a posit (3.4). Re-examined $\sigma$: exact form forces $\sigma=\ln m$ (3.5). Both recorded.
3. *Pass on node 4 (identification).* Re-examined the link reading of GR:104 against a curved cut: orientation factor $\tfrac32$ (4.4), checked by an exact identity with a planar control.
4. *Pass on GR:68–70, :74–86, :617–629 and ch07:50–57 for further uses of total finiteness.* Only GR:58 (twice) and its inherited finite counts at GR:68–70; GR:70's count $N_{ij}$ is replaced by the mass $J_{ij}$ in 6.1. No further NEW item.
5. *Pass on the conditional theorem below against GR:118, :126, :128.* No use of H-BD or of the boundary-only lemma; the theorem's scope excludes the deep-coupled case these lines constrain. No further NEW item.

Passes 4 and 5 yield no NEW finding.

## Result

**Theorem (conditional; proved here).** Assume H1, H2, H3 with any counting unit $\epsilon_c$, H4, decoupled product dynamics (so H5 holds, 6.3), H6, H7, H8 and H9. Then, with the hidden deep sector of any cardinality and with no assumption of total finiteness:

1. the visible shell weights are $p_i=e^{\sigma A(E-e_i)/\epsilon_c^2}/Z$ with $Z<\infty$ (6.2, 3.3);
2. the paired rates obey $T_{ij}/T_{ji}=p_j/p_i$ (6.1);
3. on exact de Sitter the log-rate ratio over a gap $\delta$ is $\beta_E(E-\delta/2)\,\delta$ with $\beta_E(x)=8\pi G\sigma/(c^2\kappa(x)\epsilon_c^2)$, exactly under H10(b) on the compared gaps, and within $\sigma$ of it without H10(b) (3.3, 3.4);
4. under H10(a), H11 (H-slope), H12 and H13, the matching of GR:74 gives $\beta_E a_*=\tau_K$: if $E(\omega)=a_*\omega+o(\omega)$, $-\ln R_E(x)=\beta_E x+o(x)$, $-\ln R_\omega(\omega)=\tau_K\omega+o(\omega)$ and $\ln R_E(E(\omega))-\ln R_\omega(\omega)=o(\omega)$, then dividing by $\omega$ and letting $\omega\to0$ gives $\beta_Ea_*=\tau_K$, hence $a_*=\tau_K/\beta_E=\frac{2\pi c}{\kappa}\cdot\frac{c^2\kappa\epsilon_c^2}{8\pi G\sigma}=\frac{c^3\epsilon_c^2}{4G\sigma}$; under H10(b) and H-balance at the compared finite gaps, the discrete form of 3.4 gives the same relation up to the relative finite-reservoir factor $(1-x_n/(2E))^{-1}$.

The result fixes a relation among $\hbar$, $\epsilon_c$ and $\sigma$ only. It equals the relation of GR:80 for Lemma 1's $\epsilon$ only under S3 (H3), which is independent of Lemma 1 (4.2) and, under H-link for a spherical horizon on the cubic lattice, holds with $\epsilon_c=\epsilon\sqrt{2/3}$ rather than $\epsilon_c=\epsilon$ (4.4).

**Answer to the question.** Holds only conditionally on a supplied slope. A finite boundary count, from Lemma 1 or otherwise, does not by itself replace A1 at the counting step:

- Lemma 1 proves finiteness of the observer's states and only motivates a finite boundary mode count; the boundary configuration set is finite only by posit H2 (node 2, counterexample 2.3).
- A1 does three things at (a) (node 1). The boundary count can replace the first; the second and third need a specified hidden law H4, without which the slope is undetermined (node 5, counterexample). With H4, the replacement is proved for decoupled dynamics (node 6) and parked for coupled dynamics (6.3).
- The entropy slope is never supplied by counting, whether by A1 or by the boundary count. It is H-count's density-of-states clause H6, a posit (node 3). Its derivative form needs a continuum interpolant of an integer count (3.4).
- The identification (c) is an independent posit, S3 (node 4). Under H-link it carries an orientation factor $\tfrac32$ for a spherical horizon (4.4).

**Classification of findings (§A.31).** NEW: 3.4 (the integer count has no zero-gap derivative; exact discrete-gap form under H-quant); 4.4 (crossing-link density $(\lvert n_1\rvert+\lvert n_2\rvert+\lvert n_3\rvert)/\epsilon^2$, average $\tfrac32$ on a sphere, against GR:104's one link per boundary cell); node 5 (the cardinality form of the deep clause is empty on an infinite carrier; every slope realized). POSITIVE: decoupled replacement of (a) by H2 with H4 (6.2–6.3). ELABORATING: 2.3, 3.5. CONFIRMING: 2.1–2.2, 3.1–3.3, 6.1. The productivity test of node 0 is met under (i), (ii) and (iii).

## Open questions

1. **Coupled shell law.** Is there, for a deep-coupled reversible update of the selected class, a normalized law invariant under $\varphi$ and $\Theta$ whose cell masses are fixed independently of the target slope? This is the first missing item for the coupled case (6.3), the same item at which the first P7 check stopped.
2. **Source of H6.** No traced source derives the hidden density of states $\ln\Omega_H(x)=\sigma A(x)/\epsilon_c^2+C$, on either reading of 3.3. On reading (ii), it also needs a partition that varies with the hidden energy, outside Main:42's fixed $V$.
3. **Regularity.** The detector-side condition at finite gaps under H-quant (H-balance at $\omega_n$), or a justification of the continuum interpolant with an error bound at thermal gaps (3.4).
4. **Orientation factor.** Whether GR:104's $\kappa_m=1$ and the quoted $\epsilon=2\sqrt\sigma\,l_p$ should carry the factor of 4.4 for the de Sitter horizon, or the cut and counting rule should be specified differently. This is an owner decision; manuscript edits are outside this authorization. Assumption-watch marker: the local Jacobson argument (GR:98) applied to local horizon patches of different orientations would use the orientation-dependent density $\sigma(\lvert n_1\rvert+\lvert n_2\rvert+\lvert n_3\rvert)/\epsilon^2$ under H-link; its consistency with isotropy is not examined here.
5. **Identification across the cut without finiteness.** A source for S3 that does not use A4's finite periodic lattice (4.3).
