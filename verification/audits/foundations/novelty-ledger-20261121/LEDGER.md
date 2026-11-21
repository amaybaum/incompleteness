# NOVELTY-LEDGER — OI's exact claims against the prior literature

Issue #1525; owner scope #1169 c.7067233614, start c.7067281228. Drafting snapshot `D` = `main` at
`df6da1c6`. Plan and productivity test: `PLAN.md` (committed first).

**Status: WIP / UNVERIFIED.** No independent review yet. Read-only: no manuscript file is changed and
no computation is run. The ledger compares; it draws no new scientific conclusion. Where it says
"no prior statement located", that reports a bounded search (§6), not an absence in the literature.

**Columns.** *Priority*: who first proved the same or a stronger statement, as far as located.
*Assumptions*: whether OI's hypotheses are weaker, equal or stronger than the nearest source.
*Conclusions*: whether OI's conclusion is weaker, equal or stronger. *Lean*: the kernel status the
manuscript cites at `D`, spot-checked to exist in `verification/lean-mathlib/OIBridge/` (no `sorry`
in the cited files; no build run). *Physical novelty*: whether the claim adds physical content
beyond the mathematics, and on which named hypotheses it does so.

**Line locators** are at `D`. The brief's locators drift slightly: the displayed
$S\iff D\iff Q_{\mathrm{fb}}$ is Main:16 (sentence Main:14–18), and the theorem-statement paragraph
is Main:80. `papers/Explainer.md` does not exist on `main` at `D`; it exists only on non-main
branches (last edited at `f6f7dd13`, 2026-11-05), whose Barandes passages are at its lines 282, 288,
342, 350, 381. On `main` the corresponding explainer text is `papers/Introduction.md` (Introduction:57–97,
references 220–244). The locators Explainer:293/355/386 were not matched to Barandes passages in any
version read.

***

## 1. Unit U1 — the finite-horizon equivalence $S\iff D\iff Q_{\mathrm{fb}}$

### 1.1 What OI states and what the kernel proves

Main:556 (theorem), Main:562 (proof), Main:564 (scope remark). Kernel: `finite_horizon_equivalence`
in `OIBridge/Equivalence.lean:462`, assembled from `S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S`.

The kernel's classes (Equivalence.lean:145–222) fix the exact content:

- (S) `Stochastic P`: $P$ is a probability vector on $V^{K+1}$.
- (D) `RevRealizable P`: one bijection `step : V × Hid ≃ V × Hid`, iterated, with an initial law on
  `V × Hid` that **may correlate** visible and hidden coordinates; the visible trajectory has law $P$.
- ($Q_{\mathrm{fb}}$) `QfbRealizable P`: one fixed matrix $U$ (unitary), an initial weight on a
  finite basis, and a readout `read : Bas → V`; the trajectory weight is
  $\mathrm{init}(\sigma_0)\prod_k |U_{\sigma_{k+1}\sigma_k}|^2$. So $Q_{\mathrm{fb}}$ is, exactly,
  the class of **deterministic functions of a time-homogeneous Markov chain whose kernel is
  unistochastic** ($|U|^2$ with $U$ unitary).

Read at that level the three implications are: (S⇒D) every finite law is the visible marginal of a
finite bijection run from a correlated initial law (a trajectory register plus clock);
(D⇒$Q_{\mathrm{fb}}$) a permutation matrix is unitary and $|0|^2=0$, $|1|^2=1$; ($Q_{\mathrm{fb}}$⇒S)
Born weights of a unitary are row-stochastic. The independent-hidden-prior strengthening (Main:526,
"finite-horizon process dilation" and its response-table extension) is proved on paper and in probes,
and is stated at Main:530 not to be formalized.

### 1.2 Comparison

| Claim (locator) | Priority | Assumptions vs nearest source | Conclusions vs nearest source | Lean | Physical novelty |
|---|---|---|---|---|---|
| **S⇒D, correlated initial law** (Main:562; `S_imp_D`) | Prior. EGGH26 Prop. 13 (arXiv:2602.23491v1, 26 Feb 2026; p. 31 of the PDF read): every stochastic process family on finite $C$, finite $T$ is realized by a deterministic system–ancilla dynamics $A: T\times C\times\Lambda\to C$ with correlated initial laws; proof by an ancilla labelling a complete trajectory. The idea "draw the whole trajectory at time 0, reveal it" is folklore (canonical coordinate/shift representation); for one Markov step it is the random-mapping representation, Levin–Peres 2017 Prop. 1.5. OI cites both (Main:562 [64]; Introduction:63). | EGGH26's $A$ is time-indexed and need not be injective. OI requires **one fixed bijection, iterated**, with time carried by a hidden clock. EGGH26's target is broader: a whole stochastic process *family* $p_0\mapsto\mu_{p_0}$, one realization serving every initial distribution, whereas OI's `S_imp_D` realizes one supplied law. | Stronger in form: time-homogeneous and reversible. Same in observable content. The strengthening is a standard completion step: a history ledger makes the step injective, the reversible-embedding device of Bennett 1973 (*IBM J. Res. Dev.* 17, 525, "Logical reversibility of computation"; not re-read), and an injection on a subset of a finite set extends to a permutation (`exists_perm_extending`). | Proved (`S_imp_D`, `exists_perm_extending`). | None beyond EGGH26 and folklore at the law level. Reversibility of the realization is what OI's later results use (recurrence, $\Gamma_L=I$). |
| **S⇒D, hidden prior independent of the visible start** (Main:526, response-table extension) | Prior. EGGH26 Prop. 16 (same PDF, p. 34): a fixed ancilla law $\lambda_0$, independent of the system's initial distribution, with time-indexed deterministic $A$, reproduces every stochastic dynamical system on finite $T$; proof by $N$ blocks each encoding a trajectory conditional on the start. OI cites it (Main:562; Introduction:63). Functional-representation lemma (El Gamal–Kim 2011, App. B) is the one-step analogue (locator not re-read). | EGGH26 Prop. 16 covers the whole family of initial distributions with one fixed $\lambda_0$, broader than OI's single supplied law. OI again adds one fixed iterated bijection; OI's response table is indexed by history contexts rather than by start blocks. | Same law-level conclusion, in time-homogeneous reversible form. | Not formalized (Main:530). Probe-certified for rational instances. | None beyond EGGH26. |
| **D⇒$Q_{\mathrm{fb}}$** (Main:562; `D_imp_Qfb`; Main:270 permutation unitarity) | Elementary; already stated by Barandes in 2023: "every permutation matrix is unitary, so deterministic dynamics is a" special case (arXiv:2302.10778v1, 20 Feb 2023, line read in the v1 text), and for a fixed permutation $\Sigma$, "every permutation matrix is unitary, and is also unistochastic" (arXiv:2309.03085v1, 3 Sep 2023, read at that passage). Restated in Bar26 §4 (arXiv:2608.04354v1, 5 Aug 2026, read): a time-homogeneous logically reversible deterministic process has a permutation matrix, which is unitary, with an initially diagonal density matrix $\rho_0=\mathrm{diag}(p)$ and $U(t)=\Sigma^t$. Bar26 treats a single stochastic matrix and its powers, not a hidden-variable multi-time readout. | OI's input is a bijection on $V\times H$ with a correlated initial law and a coarse readout to $V$; Bar26's is a permutation on the full state space with no coarse readout. | OI adds the multi-time record and the visible readout (the fixed-basis projective measurement at every step does not disturb a diagonal state under a permutation). Mathematically immediate in both. | Proved (`D_imp_Qfb`, `permMatrix_mem_unitaryGroup`, `isDiag_Phi`). | None. |
| **$Q_{\mathrm{fb}}$⇒S** (Main:562; `Qfb_imp_S`) | Born rule; textbook. The multi-time law of repeated projective fixed-basis measurement is the object of Strasberg–García Díaz 2019 (PRA 100, 022120; arXiv:1905.03018) and Milz et al. 2020 (PRX 10, 041049), cited in Introduction:65 (SGD19). | — | Same. | Proved (`Qfb_imp_S`, `sum_born`). | None. |
| **The three-class equivalence as a package** (Main:16, Main:80 item (1), Main:556) | No single prior statement located in the read sources that packages S, D (one iterated bijection) and $Q_{\mathrm{fb}}$ as one equivalence. Each arrow is prior or elementary (rows above). | — | The package's content is the union of the arrows. Main itself states that representability is universal and does not discriminate memory-bearing laws (Main:18, Main:564). | Proved as stated (`finite_horizon_equivalence`). | None; Main:564 already scopes it so. The formal verification is the most distinctive contribution of this unit. |
| **One-step ancilla dilation on $n^2$** (Main:212) | Standard Naimark/Stinespring isometry $W\lvert i\rangle=\sum_j\sqrt{T_{ij}}\lvert j\rangle\lvert i\rangle$. Bar26 Thm 3.3 (read) proves the same marginalization of an $N^2\times N^2$ unistochastic matrix for any stochastic matrix, crediting Gopalkrishnan (2026) for tightening Barandes' earlier $N^3$; Bar26 also cites Schmidt 2021 (arXiv:2106.03513, bistochastic dilation by coarse graining; abstract read) as similar, with a noted error. | Same. | Same per-time form. Main:668 lists the $n^2$ per-time form as "internal" and keeps "$\le n^3$" as the source's bound; Bar26 now gives $N^2$ externally. That is a comparison fact, not a correction proposal. | Not cited as formalized. | None. |
| **Barandes correspondence, (Q1)** (Main:210, Main:536, Main:668) | Barandes 2023/2025 (arXiv:2302.10778v3, *Philosophy of Physics* 3(1):8 (2025), DOI 10.31389/pop.186; arXiv:2309.03085v2, 5 Feb 2026). Abstracts read; bodies not re-read here. | Imported under translation hypothesis (T) (Main:538). | OI claims no strengthening of the import; it states the import is load-bearing only for compression and interpretation (Main:668). | Not formalized (imported). | Interpretive only, by OI's own scoping. |

### 1.3 Bar26 verification

arXiv:2608.04354 exists: J. A. Barandes, "The Born Representation Theorem and the Unistochastic
Theorem", v1 submitted 5 August 2026, 13 pp., quant-ph (cross-lists math-ph, math.PR, math.RA),
CC BY 4.0. Read in full text. It states:

- **Thm 3.1 (Born Representation Theorem).** For an $M\times N$ stochastic $\Gamma$ there are an
  $M$-member POVM $E_1,\dots,E_M$ and an $N$-member PVM $P_1,\dots,P_N$ of $N\times N$ matrices with
  $\Gamma_{ij}=\mathrm{tr}(E_iP_j)$. Corollary 3.2: if the POVM is itself a PVM, $\Gamma$ is
  unistochastic.
- **Thm 3.3 (Unistochastic Theorem).** With $N=\max(M,L)$, there is an $N^2\times N^2$ unitary $U$
  whose unistochastic matrix $|U|^2$ marginalizes to $\Gamma$:
  $\Gamma_{ij}=\sum_k(\Gamma\Gamma)_{(ik),(j1)}$.
- §4: applications to time-homogeneous Markov chains and deterministic processes, as summarized in
  the D⇒$Q_{\mathrm{fb}}$ row; for an irreversible deterministic map, projections at integer times
  are needed.

Bar26 concerns single stochastic matrices. It states no multi-time joint-law representation and no
hidden-memory result. Introduction:65 cites it ([Bar26]) only for the unistochastic definition;
that citation matches the paper.

### 1.4 Citation error noted (not repaired; manuscripts are read-only here)

SM:1735 cites arXiv:2302.10778 as *Foundations of Physics* **53**, 82 (2023), and the generated
SM.tex:8969 repeats it. This is an error, not an unlocated reference. Crossref assigns
*Foundations of Physics* 53, article 82 (2023) to a different paper: Gurwich, "The Non-vanishing
Imprint of Gravitational Waves as the Result of Its Nonlinear Evolution in Space", DOI
10.1007/s10701-023-00714-w. The arXiv record of 2302.10778 gives *Philosophy of Physics* 3(1):8
(2025), DOI 10.31389/pop.186, as Main:827 and GR:998 do.

**Proposed post-retirement correction item** (not applied): replace the SM:1735 journal reference
with *Philosophy of Physics* **3**(1), 8 (2025), DOI 10.31389/pop.186; regenerate SM.tex/SM.pdf;
re-grep the corpus for "Foundations of Physics" beside 2302.10778 (§A.25). The ledger does not
edit SM.

***

## 2. Unit U2 — hidden memory, the capacity bound and P-indivisibility

| Claim (locator) | Priority | Assumptions vs nearest source | Conclusions vs nearest source | Lean | Physical novelty |
|---|---|---|---|---|---|
| **(a) Pushforward identity** $P(X_{t+1}\mid p,x)=(f_x)_\#\mu_p$ (Main:614) | Standard: the predictive law of a deterministic function of a hidden state is the pushforward of the filter (hidden-Markov filtering; folklore). | Same. | Same. Reformulation. | Proved (`pushforward_identity`), for a joint law of history, present and hidden state; reading a realization's time-$t$ law as that joint law is not formalized (Main:620). | None. |
| **(b) Distinguishability floor** (Main:614) | Data processing for total variation (contraction coefficient $\le1$; Dobrushin). | Same. | Same. | Proved (`distinguishability_floor`), same caveat. | None. |
| **(c) Capacity floor** $M_t\le I(X_{<t};H_t\mid X_t)\le\log_2\lvert\mathcal C_H\rvert$ (Main:614) and **C3 necessity** $I(X_{<t};X_{>t}\mid X_t)\le\log_2 m$ (Main:514) | Data processing. The unconditioned analogue $\mathbf E\le C_\mu\le\log_2\lvert\text{states}\rvert$ for predictive presentations is in computational mechanics (Shalizi–Crutchfield 2001, *J. Stat. Phys.* 104, 817; bounds section located in the table of contents, body not re-read). | OI conditions on the present visible state, works per time on a finite non-stationary horizon, and quantifies over every faithful deterministic realization. Computational mechanics treats stationary processes and their causal-state presentations. | Equal in strength as an inequality; the conditional, per-time form is a direct specialization of data processing. Reformulation. | Proved (`capacity_floor`, `c3_necessity`, `card_hidden_ge_two_pow_Istar`). | Physical content enters only through the identification of the hidden sector (C3's horizon count, Main:76), not through the inequality. |
| **Biconditional**: $M_t>0$ iff every faithful realization carries readout-relevant hidden memory (Main:624; Main:95 Layer 1) | Follows from (a) plus existence of one realization. No prior statement of this exact biconditional located; its content is (a). | — | Reformulation of (a) with existence. The CMI vanishing criterion used is standard and, per Main:95, not formalized. | Partly: (a), (b), `S_imp_D`; the CMI criterion is not formalized. | None beyond (a). |
| **Variational remark**: $\inf$ over deterministic completions of $I(X_{<t};H_t\mid X_t)$ equals $I(X_{<t};X_{>t}\mid X_t)$; over bijective ones it is $H(X_{<t}\mid X_t)$ (Main:626) | The lower bound is data processing. The gap between stored and predictive information is the crypticity of Crutchfield–Ellison–Mahoney 2009 (*PRL* 103, 094101; arXiv:0902.1209; abstract read): excess entropy is in general not the information stored in the present. | OI: conditional on $X_t$, finite horizon; the minimizer is the future-tail object, not the causal-state partition. | Different minimand: OI minimizes the mutual information, computational mechanics minimizes the state entropy $C_\mu$ over prescient rivals. Neither subsumes the other. | Bijective-case inequality proved (`c3_necessity_via_hidden`); the non-injective step is on paper (Main:626). | None. |
| **Canonical predictive quotient** (Main:632) | Structurally the finite-horizon, stage-indexed instance of final-coalgebra semantics for stream systems: every system maps uniquely to its behaviour, the stream it emits (Rutten 2000, *Theor. Comput. Sci.* 249, 3; not re-read). Causal states are the minimal-entropy sufficient statistic, a different quotient (Shalizi–Crutchfield 2001). | Same as the coalgebraic setting, specialized to a probability law. | OI adds the probability pushforward and the ledger closure to a bijection. No prior statement of that combination located. Main:634 already scopes it as "an ingredient" toward CDP purification, not the axiom. | Not formalized; probe-certified (`purification_probes.py`). | None. |
| **Stochastic-inverse lemma** (Main:133) | Classical: a nonnegative matrix with nonnegative inverse is monomial. Remarked for stochastic matrices by Barandes in 2023: the inverse of a stochastic matrix has negative entries unless it is a permutation (arXiv:2302.10778v1 and 2309.03085v1, read at those passages) (attributed to Berman–Plemmons, *Nonnegative Matrices in the Mathematical Sciences*, SIAM 1994; exact theorem number not verified). Rectangular form: Plemmons 1973, *Proc. AMS* 39 (not read). | Same. | Same (stochastic case of the monomial statement). | Proved (`isPermMatrix_of_stochastic_inverse`). | None. |
| **Overlap and return** (Main:143): $\Gamma_n=I$ plus two overlapping rows at $s<n$ ⇒ not P-divisible | Contrapositive of TV contraction under stochastic maps; the revival-of-distinguishability witness of Breuer–Laine–Piilo 2009 and Rivas–Huelga–Plenio 2010/2014 (Main [4,5,63]); classical form in Buscemi–Datta 2016 (PRA 93, 012101; abstract read). Concurrently Doukas 2026, Prop. 1 "No distinguishability revival" (arXiv:2602.22095v3, read at its statement), cited at Introduction:91. | Same. | Same. Main:119 correctly notes that monotonicity is necessary, not sufficient, for P-divisibility; Buscemi–Datta's converse uses a Blackwell-type ordering over all ensembles, not total variation alone. | Proved (`pIndivisible_of_rooted_identity_return_of_overlap`). | None. |
| **History readback + finite recurrence ⇒ indivisibility** (Main:137; Main:113 first theorem) | No prior statement in this exact form located. Ingredients are prior: finite-order permutation gives $\Gamma_L=I$; the inverse lemma; the revival witness. That finite (non-continuum) environments produce non-Markovian revivals is general open-systems knowledge (e.g. the continuum-bath assumption behind the Markovian limits cited at Main:182). | Finite bijection, shared hidden prior, rooted maps including zero-probability roots. | The conclusion is P-indivisibility over the recurrence cycle, which Main:141 scopes explicitly: it does not give indivisibility on accessible windows. With full support it is equivalent to memory at some order below $L$. | Final clause proved via the overlap theorem; three intermediate steps on paper (Main:139). | Bears on physics only through A1 (finite carrier) or the near-return condition (NR), both not adopted (Main:133; Substratum §3.1 A1). |
| **Readback lemma** $I(X_{<k};X_{k+1}\mid X_k)\ge p_0\delta^2/\ln2$ (Main:173) | Pinsker's inequality plus the mixture-divergence form of CMI; standard. | Same. | Same. Reformulation. | Not formalized; checked in exact rationals for laws, floating point for information (Main:176). | None. |
| **Genericity count** $P_{\mathrm{perm}}=n_V!\,(n_H!)^{n_V}/(n_Vn_H)!$ (Main:149) | Elementary counting; no prior statement sought. | — | — | Not cited as formalized. | None. |
| **CP-indivisibility, framework scope** (Main:332) | Diagonal-preserving permutation dilations embed the classical process; P- and CP-divisibility then coincide on the diagonal. Related classical-embedding analyses: Smirne et al. 2019 (NCGD dynamics; not re-read), Milz et al. 2020 (PRX 10, 041049; abstract read), Milz–Kim–Pollock–Modi 2019 (PRL 123, 040401). | Restricted to permutation dilations with diagonal hidden prior. | Main:340 scopes it: for general CPTP families the reduction fails. | `isDiag_Phi` (diagonal preservation) proved; the CP clause not separately cited. | None. |
| **Divisibility ≠ Markovianity** (Main:155, Main:638; Introduction:97 parity example) | Prior: Rivas–Huelga–Plenio 2014 Eq. (15) (cited, Introduction:97), Milz et al. 2019; concurrent Doukas 2026 App. A (XOR process, read). | — | Same. | — | None. |

**U2 summary.** Every inequality in U2 is a direct specialization of data processing, Pinsker or
TV contraction, stated in conditional, per-time, finite-horizon form for deterministic
completions. The two statements with no located prior in their exact form are the
recurrence-cycle indivisibility theorem (Main:137) and the canonical predictive quotient
(Main:632); both are assembled from standard ingredients, and the manuscript already scopes the
first to the recurrence cycle and the second to "an ingredient". The ledger finds no U2 statement
the manuscript presents as strengthening a cited divisibility result beyond what its proof gives.

***

## 3. Unit U3 — the Theorem 23 reconstruction

Substratum:193 (Theorem 23), Substratum:121–171 (Stages 1–2), Substratum:189 (Lemma 23.0),
Substratum:203 (Refinement: forced / selected), SM:1420–1430 (three tiers).

### 3.1 Three-way classification

The manuscript already supplies this split (Substratum:203; SM:1420–1430). The ledger checks it
against the stated proofs and the literature.

**(F) Forced, given the $\mathbb Z^3$ simple-cubic lattice, its cubic group $O$, the nearest-neighbour premise, A4 (center independence), A5 (linearity), the second-order reversible form, and, for hypercharges, the supplied family representation pattern** — exact mathematics, independent of E1–E7 once those premises are given:

- $6=T_1\oplus E\oplus A_1$ for the signed links of $\mathbb Z^3$ under $O$ (SM Theorem 7, SM:374);
  Schur block-scalarity of equivariant operators.
- $8$ BZ corners $\to4$ taste pairs $=\mathbf1\oplus\mathbf3$ under $O$ (SM Theorem 8, SM:434).
- The stabilizer of a generic $\mathrm{diag}(aI_3,bI_2,c)$ in $\mathrm U(6)$ is
  $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$ (the algebraic core of SM Theorem 5).
- Uniqueness of $f=\alpha\sum_{\rm nbrs}x$ among center-independent, isotropic, linear
  nearest-neighbour second-order rules (SM §4.1, SM:228).
- Anomaly-fixed hypercharges given the family pattern (SM Theorem 15, SM:589).
- $\theta\in\{0,\pi\}$ and reciprocal counts from T-invariance (SM Theorems 17–21).
- Gauge-coupling dimension $[g]=(3-d)/2$ (SM Theorem 16).

**(E) Empirically selected** — the inference runs from observation back to the commitment
(Substratum:203 says so):

- $d=3$: E5 ($d\ge3$) and E6 ($d\le3$); E7 a consistency comparison conditional on the GR §7.2
  boundary-energy identification.
- Simple cubic: selected by the observed $\mathrm{SU}(3)$ factor in the nearest-neighbour
  condensate comparison (SM Theorem 7b, SM:390).
- The supplied Higgs doublet $(\mathbf1,\mathbf2,+\tfrac12)$.
- E1 and E2 enter Stage 1 through M1-T and M1-B (Substratum:123).

**(H) Hypothesis-dependent** — physical identifications:

- $K=6$: H-link single copy (SM:360; SM Theorem 6).
- The physical stabilizer reading: H-link and H-cust (SM Theorem 5).
- The local SM gauge algebra: A6 plus the specified charged action.
- Three generations: H-spin′ plus light-spectrum selection (SM:452; its free-kernel form H-spin is
  refuted there).
- Weak chirality: H-χ′ (SM:513, SM:553).
- $\hbar=c^3\epsilon^2/(4G\sigma)$: H-slope, H-count and GR §8.5(b).
- Bell-inclusive existence: H-Bell; its uniqueness is open (Substratum:193).

Tier 3 definitional stipulations (SM:1428) — the site and internal factorizations, the
nearest-neighbour restriction, the C1–C4 architecture — sit beneath all three.

**Check against the proofs.** The ledger found no conclusion of Theorem 23 placed in (F) whose
stated proof uses an (E) or (H) input, except as the theorem itself states: SM Theorem 5's
physical reading uses H-link and H-cust, and only its algebraic core is in (F).

### 3.2 Comparison

| Claim | Priority | Assumptions | Conclusions | Lean | Physical novelty |
|---|---|---|---|---|---|
| $6=T_1\oplus E\oplus A_1$ (SM:374) | Textbook character theory of $O$ on the six $\pm\hat e_j$ (any point-group text; not re-read). | Same. | Same. | Proved (`theorem_7`, `sum_proj`, `finrank_PT`, `char_c4_odd`). | Only under H-link (SM:360). |
| $4=\mathbf1\oplus\mathbf3$ taste pairs (SM:434) | Elementary. Staggered-fermion symmetry groups and taste representations: Kogut–Susskind 1975 (PRD 11, 395; cited SM [17]); Golterman–Smit 1984 and Golterman 1986 (Nucl. Phys. B) — not re-read, cited from standard knowledge. | Same. | Same. | Proved (`theorem_8`). | Reading tastes as physical generations needs H-spin′. The standard lattice view treats tastes as discretization artifacts removed in the continuum (search, §6). Tastes or Kähler–Dirac species as physical generations were proposed in 1982: Banks–Dothan–Horn, "Geometric fermions" (*Phys. Lett. B* 117, 413; DOI 10.1016/0370-2693(82)90571-8) and Benn–Tucker, "A generation model based on Kähler fermions" (*Phys. Lett. B* 119, 348; DOI 10.1016/0370-2693(82)90686-4); bibliographic records confirmed, texts not read. Later doublers-as-physical-species proposals: Schmelzer 2001 (arXiv:hep-lat/0111057; abstract read), a doubler pair read as a physical doublet with a suggested account of three families; Schmelzer 2009 (*Found. Phys.*, DOI 10.1007/s10701-008-9262-9; arXiv:0908.0591; abstract only). The generic idea that staggered/Kähler species are generations is therefore prior (1982). No prior source located for OI's narrower 1+3 claim: the cubic-group split with the singlet as Higgs host and the triplet as the three generations. |
| Stabilizer $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$ (SM:340) | Standard linear algebra. Structurally parallel to $\mathrm{SU}(5)$ breaking by an adjoint with eigenvalue multiplicities $(3,2)$, Georgi–Glashow 1974 (PRL 32, 438), whose stabilizer is $\mathrm S(\mathrm U(3)\times\mathrm U(2))$. | OI's $(3,2,1)$ multiplicities come from the cubic link decomposition; Georgi–Glashow's from the chosen Higgs vacuum. | Different origin of the multiplicities; same group-theoretic step. | Not cited as formalized. | The multiplicity origin is OI's; its physical reading needs H-link and H-cust. |
| Wave-equation uniqueness (SM:228) | The second-order reversible form $x(t+1)=F(x(t))-x(t-1)$ is the standard construction of invertible cellular automata (Fredkin; Toffoli–Margolus 1990, *Physica D* 45, 229; not re-read). Uniqueness of the isotropic linear nearest-neighbour stencil is elementary. | Linearity (A5), nearest-neighbour premise, no self-term (A4). | Same. | Not cited as formalized. | None beyond the premises. |
| Anomaly-fixed hypercharges (SM:589) | Prior: hypercharge uniqueness from gauge and mixed gauge–gravitational anomaly cancellation for one SM family is known (Geng–Marshak 1989, PRD 39, 693; Minahan–Ramond–Warner 1990, PRD 41, 715 — not re-read). SM cites Alvarez-Gaumé–Witten 1984 and Mohapatra §6.3. | Same given the representation pattern. | Same, including the exceptional $Y_Q=0$ branch. | Not cited as formalized. | None beyond the pattern, which is input. |
| $d=3$ selection (Substratum:157) | Prior arguments: Ehrenfest 1917 (stability), Tangherlini 1963 (orbits), both cited; Tegmark 1997 (*Class. Quantum Grav.* 14, L69) reviews them and is cited only in Structure.md. | Same filters; E7 is OI-specific and conditional on GR §7.2. | Same as the cited sources for E5/E6. Substratum:203 states it is uniqueness relative to observed inputs. | Not formalized. | E7's ratio $2/(d-1)$ is OI-specific, conditional. |
| Simple-cubic selection by $\mathrm{SU}(3)$ (SM:390) | Crystallographic point-group irreducible-representation dimensions are textbook. No prior source located for this nearest-neighbour Bravais comparison. | Generic condensate, nearest-neighbour link representation, specified charged action. | Selection relative to the observed gauge group (Substratum:203). | Not cited as formalized. | Empirically selected, per the manuscript. |
| Emergent local gauge invariance from A6 (Substratum:163) | Emergent gauge structure from lattice or condensed-matter models is an established programme (Wilson 1974; Volovik, *The Universe in a Helium Droplet*, 2003; Levin–Wen 2005, PRB 71, 045110 — not re-read). A6 is the standard gauge-covariance interface (Substratum §3.1 A6). | A6 is covariance with the link coupling transformed (SM §3.1). | Promotion of a global commutant to local invariance is the standard lattice-gauge construction. | `a6cov_all` and its instantiation exist in the census (programme records), and by those records' own caveat hold identically for every link-coupled rule. | Not new as a programme; OI's specific carrier route is new as far as located. |
| Continuum curvature / gravity (Substratum:171; H-Bell) | Jacobson 1995 (PRL 75, 1260; cited); Ollivier 2009 Ricci curvature on graphs (cited in SM/GR); graph-based emergent geometry, e.g. Konopka–Markopoulou–Severini 2008 (PRD 77, 104029; not cited; not re-read). | — | Substratum:171 states that the hop-metric curvature route fails on the reference graph and that H-Bell is open. | Not formalized. | Open by the manuscript's own statement. |
| **Theorem 23 as a whole** (Substratum:193) | No prior statement located that combines these steps. | Its hypotheses are E1–E7, M1-T, M1-B, A1–A6, the nearest-neighbour and continuum premises, and H-link, H-cust, H-spin′, H-χ′, H-slope, H-count, H-Bell. | A layered conditional statement. Uniqueness is of the local residue and is relative to the (E) inputs (Substratum:203). | Not formalized as a theorem. Only the (F) components listed carry kernel names. | Physical content lives in (H), where every item is a named open hypothesis. |

***

## 4. Productivity test outcome

- **U1 — productive.** (a) holds: EGGH26 Props 13 and 16 prove S⇒D in both initial-law forms;
  Barandes 2023 (2302.10778v1, 2309.03085v1) states D⇒$Q_{\mathrm{fb}}$'s permutation-unitary step, restated in Bar26 §4; Bar26 Thm 3.3 gives the $N^2$
  per-time marginalization. (b) holds: OI's D-class realization is a single iterated bijection,
  strictly stronger in form than EGGH26's time-indexed, non-injective $A$. Its observable content
  is the same. The kernel formalization is the unit's most distinctive item.
- **U2 — productive.** (a) holds for every inequality (data processing, Pinsker, TV contraction,
  the monomial-inverse lemma, the revival witness, crypticity). (b) is limited to forms with no
  located exact prior: the recurrence-cycle theorem and the stage-indexed quotient. Both are built
  from standard ingredients.
- **U3 — productive.** (a) holds for the (F) components (character theory, Georgi–Glashow-type
  stabilizer, anomaly-fixed hypercharges, the second-order reversible CA form, dimension-stability
  arguments). The (E)/(H) split in Substratum:203 and SM:1420 matches the stated proofs. No item in
  (b) was found: nothing in Theorem 23 is shown to be strictly stronger than a located source under
  weaker hypotheses. INCONCLUSIVE on physical novelty of the combination, because the located
  sources for the doublers-as-generations idea were read only at abstract level.

## 5. What is established, assumed, missing (owner standard)

1. **Established** (comparison layer only): the priority attributions above, each with the read
   or unread mark of §6. Bar26 exists, and its theorems are as stated in §1.3. Explainer:293/355/386
   do not resolve on `main`. SM:1735's journal reference is an error (another paper holds *Found. Phys.* 53, 82), repeated at SM.tex:8969.
2. **Assumed**: that the standard references marked "not re-read" state what is attributed to
   them; the manuscript's kernel citations as spot-checked (identifiers exist; no build run).
3. **Missing**: a full read of Barandes 2309.03085v2 and Golterman–Smit 1984 / Golterman 1986;
   a dated priority comparison for OI's own results, which the shallow checkout here cannot
   supply (its history begins 2026-11-11); and independent review of this ledger.

No (N)/(I) classification is introduced: every OI result in this ledger is a mathematical
statement whose (N)/(I) status, where recorded, is the manuscripts' own.

## 6. Sources

Read here, at full text or the stated part:

- **Bar26** — arXiv:2608.04354v1. Full text.
- **EGGH26** — arXiv:2602.23491v1. Props 13 and 16 with their sketches.
- **Dou26** — arXiv:2602.22095v3. Abstract, Prop. 1 and App. A heading.
- **Calvo** — arXiv:2601.18720v2. Abstract.
- **Barandes 2023/2025** — arXiv:2302.10778v3 and 2309.03085v2: abstract pages and version
  histories; 2302.10778v1 and 2309.03085v1: the permutation-unitary and stochastic-inverse
  passages.
- **Schmidt** — arXiv:2106.03513. Abstract.
- **BD16** — arXiv:1408.7062. Abstract.
- **Milz et al.** — PRX 10, 041049 (2020). Bibliographic record and abstract.
- **Schmelzer** — arXiv:hep-lat/0111057 and hep-lat/0311009. Abstracts.
- **Further arXiv records** — 2507.21192, 2505.08785, 2512.18105 and 1905.03018. Existence,
  titles and authors.

Searched, with only the bibliographic record confirmed:

- Shalizi–Crutchfield 2001.
- Crutchfield–Ellison–Mahoney 2009.
- Schmelzer 2009.
- The non-negative-inverse ⇒ monomial theorem (Berman–Plemmons).
- The *Foundations of Physics* 53, 82 record: Crossref, a different paper (§1.4).
- Banks–Dothan–Horn 1982 and Benn–Tucker 1982: Crossref records.

Not re-read, cited from standard knowledge:

- Bennett 1973.

- Levin–Peres 2017 Prop. 1.5.
- El Gamal–Kim 2011 App. B.
- Rutten 2000.
- Golterman–Smit 1984 and Golterman 1986.
- Georgi–Glashow 1974.
- Geng–Marshak 1989 and Minahan–Ramond–Warner 1990.
- Toffoli–Margolus 1990.
- Smirne et al. 2019.
- Levin–Wen 2005.
- Volovik 2003.
- Konopka–Markopoulou–Severini 2008.
- Tegmark 1997.
