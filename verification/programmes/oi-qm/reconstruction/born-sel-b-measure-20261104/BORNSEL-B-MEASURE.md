# BORNSEL-B-MEASURE (r2): which branch of the hidden-sector measure fixes the probabilities the representation carries? (#1059, part (b))

## Header

- **Status.** WIP / UNVERIFIED. Paper-only. Part (b) only.
- **Revision.** Revised after independent review of `f6526fb8` (REVISE); not re-reviewed.
- **Authorization.** Owner, chat 2026-11-04, recorded in #1059 c.6622106065. That authorization covers paper analysis of part (b) starting from the BORN-SRC-1 five-branch fork, plus source reading, derivation on paper, a literature examination, documented assumptions and independent review. It does not cover parts (a), (c) or (d), computation, Lean, adopting a premise, promoting a claim, merging or publishing.
- **Base.** `origin/main` `1609dc440f5a12d05b750f6d894bb91d09a099a3`. `papers/Main.md` was last changed at `63b4e32e`. The `Main:N` citations are lines at this base. They match the lines that BORN-SRC-1 cites at `02009693` for the passages used here.
- **Sources read.**
  - #1059 (body and c.6622106065).
  - #914: body, BORN-SRC-1 summary c.6567852459, and the verbatim audit c.6567870091 with its review c.6567879365.
  - #914 master matrix r2, c.6563412926 (rows O-OBSMU, O-BORN, O-RDY; codes H-μ, P-7).
  - #866 body and the planning refresh c.6600176951 (O-OBSMU obligation text).
  - #913 body and its refresh c.6600187630.
  - `papers/Main.md` §1.2–§1.4, §2.3 (:131–:157), §3.1–§3.4 (:208–:656), §4.1, §4.5 (:726), §4.6 (:746).
  - `book/ch01-observation.md:77,:85` and `book/ch18-beyond.md` §18.2.
  - `papers/SM.md:803–:811`.
  - Lean: `OIBridge/CanonicalMeasure.lean`, `OIBridge/StochasticInterface.lean`, `OIBridge/Equivalence.lean`, `OIBridge/FiniteEntropy.lean`.
  - `verification/programmes/oi-qm/PROGRAMME.md` §3.4–§3.6 and `track-b/boundary-audit/result.md`.
- **What this document is.** A paper analysis of how each of the five measure branches bears on the probabilities that OI's fixed-basis representation carries. It states its decision criteria before its derivations. Every derivation is elementary finite combinatorics and was done by hand.
- **What it is not.** It is not evidence under §A.42, a manuscript edit, a status change, an adopted premise or a selection principle proposed for adoption. Nothing here should be cited as established until it has been independently reviewed.
- **Support labels.**
  - **[K]** kernel-checked, with the identifier and the file:line at the base.
  - **[P]** a reviewed paper or record result, with its citation.
  - **[D]** a derivation in this document. These are unreviewed, and in this revision their changes have not been re-reviewed.
  - **[L]** literature cited from memory and not re-read.
  - **[O]** an owner decision.

***

## §1 The question, precisely

### 1.1 The five branches, quoted

These are quoted verbatim from BORN-SRC-1 §3 (#914 c.6567870091), with the "Results that depend on it" column abridged:

| Branch | Statement (quoted) | Sources (quoted) | Results that depend on it (abridged) |
|---|---|---|---|
| α | "uniform on the actual orbit" | "Main:56 clause 1; Main:62 clause 1" | "Short orbits excluded as observer-lacking (Main:62). `ensembleDetermined_of_transitive` … Support is one cycle, not full support unless φ is transitive, and the wave substratum is not" |
| β | "unconditioned counting (H-μ)" | "Main:56 clause 2; KC :227" | "One-step doubly-stochastic lemma … ρ_H = I/m and the Born-form theorem's weights (Main:282–290) …" |
| γ | "maximal entropy compatible with records" | "Main:62 clause 2; Main:726; ch01:85" | "No result in the corpus computes with a record-constrained measure. … It reduces to β only when the records constrain nothing" |
| δ | "a stated prior (realization datum)" | "Main:518, 524, 532; ch01:85" | "Finite-horizon process dilation … the gluing theorem's rational uniform seed … O-RDY positives [C: prior] …" |
| ε | "dynamical non-equilibrium" | "ch18 §18.2; RM:1232" | "F7 and H-NEQ only" |

The same audit records the following as branch-free: "S ⇔ D ⇔ Q_fb and the Born *form* …; `invariance_does_not_select`; the finite-carrier obstruction (Main:560)". It also states that "the fork decides **which numbers the Born-form theorem outputs**".

### 1.2 Notation

- $S=\mathcal C_V\times\mathcal C_H$ is finite, $\varphi$ is a bijection of $S$, and $\pi_V$ projects onto the visible factor. $L$ is the order of $\varphi$. $\mathcal O$ is the set of orbits (cycles), $O^*$ is the orbit of the actual microstate $s^*$, and $n=|\mathcal C_V|$, $m=|\mathcal C_H|$.
- A **measure** $\mu$ is a probability law on $S$ at the reference time. It factors as a visible prior $\nu(a)=\mu(\{a\}\times\mathcal C_H)$ and a **hidden conditional** $\kappa_a(h)=\mu(a,h)/\nu(a)$ on the roots with $\nu(a)>0$. The measure is a **product** measure when $\kappa_a$ does not depend on $a$, i.e. $\mu=\nu\otimes\mu_H$.
- A **record** $r$ is a visible history $x_{-k..0}$, which has $k+1$ values. Its compatible set is $A_r=\{s:\pi_V\varphi^{-i}s=x_{-i},\ 0\le i\le k\}$.
- A record is **time-varying** if the predicate $s\in A_r$ is not constant on $O^*$.

### 1.3 "Fixes the probabilities the representation carries"

**The representation.** For a realization $(\varphi,\mu)$, the representation $R_\mu$ is the fixed-basis datum that `D_imp_Qfb` builds [K: `Equivalence.lean:294`]: `U := permMatrix (step.symm)`, `init := R.init` $=\mu$, `read := Prod.fst`. Its diagonal `init` carries any law on $S$, product or not.

Two other forms carry the same data only for **product** μ:
- the channel form $\Phi(\rho_V)=\mathrm{Tr}_H[U_\varphi(\rho_V\otimes\rho_H)U_\varphi^\dagger]$ (Main:282–290), with input $\rho_V\otimes\rho_H$;
- the fixed-$\hat H$ form with input $|i\rangle\langle i|\otimes\rho_{\rm anc}$, $\rho_{\rm anc}=\sum_h\mu_H(h)|h\rangle\langle h|$ (Main:532).

Neither form carries a root-dependent κ, such as general α or γ-c with records longer than the present state.

**The probabilities it carries.** Five objects, kept separate:
- (P1) the finite-horizon trajectory law $P_\mu=\mathrm{traj}_*\mu$ (`RevReal.law`, `Equivalence.lean:180`);
- (P2) the rooted family $\Gamma^\kappa_t(a,j)=\kappa_a\{h:\pi_V\varphi^t(a,h)=j\}$ (Main:137, Main:640; PROGRAMME §3.4);
- (P3) the one-step matrix $T_{ij}$ of the Born-form theorem (Main:288–290);
- (P4) the Born weights $|U_\varphi|^2$ of the native step unitary (`QfbReal.born`, `Equivalence.lean:205`);
- (P5) the conditional predictions $P_\mu(\text{future}\mid r)$ that an embedded observer holding record $r$ uses.

**The interface.** The D → Q_fb interface: finite horizon, fixed basis, law level. The interfaces of part (c) (preparation and instrument families across settings) and part (d) (context assignment over effects) are excluded.

**"Branch X fixes them."** This means two things together:
1. the probabilities (P1)–(P3) and (P5) that the theory asserts are those computed from $\mu_X$;
2. an OI premise, or a named hypothesis, entails $\mu\in\mathrm{Inv}_F(\mu_X)$, where $\mathrm{Inv}_F(\mu_X)=\{\mu: F(P_\mu)=F(P_{\mu_X})\}$ is the invariance class of the consuming functional $F$.

Two questions are kept apart throughout:
- **(Q-inv)** Are the representation's probabilities invariant across branches?
- **(Q-sel)** Does a premise physically select a branch?

***

## §2 Decision criteria (fixed before the §3 derivations)

These criteria are fixed in this document's order, before §3. They are not frozen and not externally preregistered. For a branch X and a consuming functional F, the outcomes are:

| Outcome | Criterion |
|---|---|
| **Selected** (under named hypotheses H) | A proof that H entails $\mu\in\mathrm{Inv}_F(\mu_X)$ for every realization in a stated scope. H is drawn from Axioms 1–2, the posit ledger (Main:726), C1–C4, or is named explicitly. H must not restate X's defining property, since a posit "μ = μ_X" counts as a stipulation, not a selection. A countercontrol must show that some other branch is consistent once H is dropped. Under §A.29, a proposed new H additionally needs preserved controls and an independent consequence. |
| **Reduces to Y** | A proof that $\mathrm{Inv}_F(\mu_X)=\mathrm{Inv}_F(\mu_Y)$ under stated hypotheses. X then adds nothing for F beyond Y. |
| **Compatible, not selected** | Some realization in scope has $\mu_X$ consistent with every stated premise. Another branch is also consistent there. A counterexample shows their F-values differ. |
| **Excluded** (for a stated class) | A proof that $\mu_X$ contradicts a premise, or the defining requirement of the role X is proposed for, on every member of the class. Scope: that class only. |
| **Undecidable from current premises** | X's definition leaves F undetermined (several readings with different F), or no premise stated in the corpus decides it (§A.19 search). |

Two further rules apply:
- **Q-inv.** It holds for F exactly when F is constant over all branches in scope. It is checked separately for the form-level functionals (P4, class membership) and the numerical ones (P1–P3, P5).
- **Productivity test (§A.31).** A node counts as a gem only if it yields a fact strictly stronger than restating the audit, and that fact either constrains a branch or exposes a hidden assumption. Otherwise the node is recorded only.

***

## §3 Work, depth-first

### N0. What carries the numbers (recheck of BORN-SRC-1 F0)

`D_imp_Qfb` proves two things [K: `Equivalence.lean:294` ff.]:
- `hborn`: `Q.born b b' = if b' = R.step b then 1 else 0`;
- `hchain`: `Q.chain = marg R.init R.states`.

So every fractional weight of (P1) is a pushforward of $\mu$.

The same construction is used for every `init` satisfying `IsLaw`, and `U` and `read` do not depend on `init`. That independence is read off the proof term. It is not stated as a theorem.

**Verdict.** CONFIRMING. F0 holds at the base.

### N1. Q-inv: what is invariant across branches

**Lemma B1 (form invariance)** [K + D]. For every law $\mu$ on $S$, $P_\mu\in Q_{\rm fb}$ through the same $U_\varphi$, basis and readout. Only `init` changes.
- Existence for every $\mu$ is [K] (`D_imp_Qfb`, universally quantified over `RevReal`).
- The Born weights (P4) lie in $\{0,1\}$ for every branch [K, `hborn`].
- For every $p>0$ the chain is unchanged if $|U|^2$ is replaced by $|U|^p$ [D: $0^p=0$, $1^p=1$]. This agrees with Main:556's "check 6" (`equivalence_recovery_probes.py`) [P].

So the representation's form and its exponent-insensitivity are branch-free.

**Lemma B2 (what each numerical object depends on)** [D].
1. (P2) $\Gamma^\kappa_t$ depends on $\mu$ only through the hidden conditional $\kappa$ on supported roots. It does not depend on the visible prior $\nu$. This follows from the definition.
2. (P3) The Born-form $T_{ij}$ of Main:290 equals $\Gamma^\kappa_1$ with $\kappa_a$ uniform on $\mathcal C_H$. So every $\mu$ whose hidden conditional is uniform on each supported root gives exactly Main:290's numbers, whatever $\nu$ is. Only this direction is claimed. The converse fails: $T$ depends on $\kappa_a$ only through its pushforward under $h\mapsto\pi_V\varphi(a,h)$.
3. (P1) $P_\mu=\sum_a\nu(a)\,P^{\kappa_a}_{a}$ depends on both $\nu$ and $\kappa$.

**Lemma B3 (numbers are not branch-invariant, on a generic finite bijection)** [D]. Counterexample CE-8:
- $\mathcal C_V=\{0,1\}$, $\mathcal C_H=\{0,1,2,3\}$, with $\varphi$ having two orbits of length 4:
  - $O_A:(0,0)\to(1,0)\to(0,1)\to(1,1)\to(0,0)$, with visible sequence $0101\ldots$;
  - $O_B:(0,2)\to(0,3)\to(1,2)\to(1,3)\to(0,2)$, with visible sequence $0011\ldots$.
- **Under β** (uniform $\kappa$): from root 0 the next visible values are $(1,1,0,1)$ over $h=0..3$, and from root 1 they are $(0,0,1,0)$. So $T^\beta=\begin{pmatrix}1/4&3/4\\3/4&1/4\end{pmatrix}$, a non-permutation matrix (C1 witness).
- **Under α:**
  - $T^{\alpha,A}=\begin{pmatrix}0&1\\1&0\end{pmatrix}$;
  - $T^{\alpha,B}=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix}$.
- The two orbits have equal length and equal hidden capacity, so no period-based or C3-based exclusion (Main:62) separates them.
- Under β the visible process has memory: $P_\beta(x_1=1\mid x_0=0)=3/4$, but $P_\beta(x_1=1\mid x_{-1}x_0=10)=2/3$ and $P_\beta(x_1=1\mid x_{-1}x_0=00)=1$. So under β the example lies in the C4 sector. Under α on $O_A$ the visible process is the deterministic alternation $0101\ldots$, which has no memory. Membership of the C4 sector therefore depends on μ.

**Verdict on Q-inv.**
- Invariant: the form (B1) and the exponent-insensitivity.
- Not invariant, as a class-wide claim over finite bijections: the numbers (B3). Whether the numbers differ across branches on the manuscripts' wave substratum has not been checked (C-1).
- The numbers of (P2) and (P3) are κ-functionals (B2).

This sharpens the audit's "the fork decides which numbers": the fork for (P2) and (P3) is a fork over κ alone. The visible prior belongs to preparations (§4, interface (c)). ELABORATING.

**Lemma B4 (Main:137 as an implication, and its μ-dependent hypothesis)** [D]. Main:137 (gap + finite recurrence ⇒ rooted indivisibility) is stated for "a hidden prior shared by every root", roots of visible probability zero included. As an **implication**, its proof goes through for a root-dependent $\kappa_a$, with $\kappa_a$ chosen arbitrarily on roots of visible probability zero:
- $\varphi^L=\mathrm{id}$ gives $\Gamma^\kappa_L=I$ for every $\kappa$.
- If every $\Gamma^\kappa_s$ with $1\le s\le k$ were a permutation matrix, the visible trajectory from each root would be deterministic. Then two distinct positive-probability trajectories with the same endpoint at $k$ would need distinct roots with $\sigma_k(a)=\sigma_k(a')$, which contradicts $\sigma_k$ being a permutation.
- The no-stochastic-divisor step does not involve κ.

The theorem holds under every branch. Whether its **hypothesis** holds, and so whether its **conclusion** holds, depends on μ. CE-8 shows this:
- Under α on $O_A$, $\kappa_0$ and $\kappa_1$ are both uniform on $\{0,1\}$. Then $\Gamma_1$ is the swap and $\Gamma_2=I$, and every $\Gamma_t$ is a permutation. The rooted family is P-divisible ($\Gamma_2=\Gamma_1\cdot$swap), and there is no gap.
- Under β, or under α on $O_B$, $\Gamma_1$ is not a permutation and $\Gamma_4=I$. So no stochastic $\Lambda$ satisfies $\Gamma_4=\Gamma_1\Lambda$, and the family is not P-divisible on $\{0,\ldots,4\}$.

**Verdict.**
- ELABORATING: the implication is branch-free.
- The consuming conclusion (indivisibility of the rooted family) is **not** branch-invariant on this class.
- This needs independent review.

### N2. Q-sel: does any current premise select?

The premises were searched across `papers/`, `book/` and the kernel (§A.19):
- **Invariance (Lemma 3, clause 1).** An invariant law is constant on orbits [K: `invariant_pow`, `CanonicalMeasure.lean:96`].
  - It fixes $\mu$ only when $\varphi$ is transitive [K: `ensembleDetermined_of_transitive`, `StochasticInterface.lean:38`].
  - It does not fix $\mu$ for two disjoint invariant sets [K: `invariance_does_not_select`, `CanonicalMeasure.lean:242`].
  - The manuscripts' wave substratum is not transitive [K: `waveSubstratum_stochastic_interface_gap`, `StochasticInterface.lean:191`].
- **Maximal entropy (Lemma 3, clause 2, Main:56; posit (iv), Main:726).** Posit (iv) is "a standard but substantive epistemic postulate, not derived" [P]. It is a stipulation, not a selection (§2).
- **Bijectivity, recurrence, finiteness and C1–C4** constrain $\varphi$ and the partition, not $\mu$.
- **C3** excludes short orbits as observer-lacking (Main:62) [P]. That narrows the candidates for $O^*$ but chooses nothing among long orbits (CE-8).
- **Mixing and relaxation.** These are stated only as hypotheses about the coarse-grained channel:
  - the effective-mixing hypothesis (EM), Main:746, which is "an explicit physical hypothesis — motivated by local thermalization phenomenology, not derived from φ";
  - posit (v), Main:726, "the hidden-sector mixing hypothesis (ETH-motivated) conditioning the slow-bath form of the C2-necessity direction" [P].

  Neither is shown to fix μ on $S$ or to deliver orbit-frequency typicality (N4, N5).
- **Frequency reading.** No premise in the corpus names a frequency reading of probability.
- **ch18.** The §18.2 ledger states: "No entry in this section is a theorem of the foundational paper" [P].

**Verdict.** No branch is selected by a current premise beyond the stipulation of posit (iv). This confirms BORN-SRC-1 §4(b) at the base. CONFIRMING.

**Lemma N2.1 (the invariant fork is a law on orbits)** [D].
- Every invariant law has the form $\mu_w=\sum_{O\in\mathcal O}w_O\,\mathrm{unif}(O)$ with $w\in\Delta(\mathcal O)$. This follows from `invariant_pow` and the fact that the orbits partition $S$.
- Its entropy is $H(\mu_w)=H(w)+\sum_Ow_O\log|O|$.
- So on any invariant set $U$, the maximal-entropy invariant law is the one with $w_O\propto|O|$ for $O\subseteq U$, which is $\mathrm{unif}(U)$. This is the Gibbs variational identity [L: Jaynes 1957; Gibbs inequality], and it agrees with `counting_maximal_entropy` [K] for $U=S$.
- So among invariant laws, $\alpha=\delta_{O^*}$-weights and $\beta=$ weights $\propto|O|$.

### N3 (decisive). γ: what "maximal entropy compatible with the observer's records" can mean

This node is decisive because posit (iv) is the only premise in the corpus that names a choice of measure, though as a stipulation (N2), and owner question O3 asks about it. Main:62 composes two parts: "on the orbit of the actual microstate, the uniform measure is the unique φ-invariant measure; the selection among orbits is fixed by maximal entropy compatible with the observer's records". The posit ledger wording is "the maximal-entropy invariant measure compatible with the observer's records". There are four readings.

**Lemma G (hard-constraint maximal entropy)** [D; standard, L]. For $\emptyset\ne A\subseteq S$:
- among laws with support in $A$, the unique entropy maximizer is $\mathrm{unif}(A)$ (`entropy_le_log_card` [K, `FiniteEntropy.lean:98`] on the subtype $A$, with equality only at uniform [L]);
- for every $B\supseteq A$, $\mathrm{unif}(B)(\cdot\mid A)=\mathrm{unif}(A)$.

**Lemma G2 (no invariant law holds a time-varying record with probability 1)** [D].
- If $\mu$ is invariant and $\mu(A_r)=1$, then $\mu(\varphi^tA_r)=1$ for all $t$. So $\mathrm{supp}\,\mu\subseteq I(A_r):=\bigcap_t\varphi^tA_r$, the largest invariant subset of $A_r$.
- If also $s^*\in\mathrm{supp}\,\mu$, then $O^*\subseteq I(A_r)\subseteq A_r$, so the record is constant (true) on $O^*$.
- So for a time-varying record, no invariant law gives the record probability 1 while keeping $s^*$ in its support.
- Consequently the observer's assignment (P5), which gives its own record probability 1, is non-invariant.

**The four readings:**
- **γ-c (condition on records):** maximal entropy subject to $\mathrm{supp}\subseteq A_r$. By Lemma G it is $\mathrm{unif}(A_r)=\beta(\cdot\mid A_r)$.
  - **Verdict: reduces to β-conditioning, for (P5).** γ-c adds no reference measure beyond β. What it adds is the conditioning event $A_r$.
  - Special case: with record $r=\{x_0=i\}$ (present visible configuration only), $\mathrm{unif}(\{i\}\times\mathcal C_H)$ is exactly $|i\rangle\langle i|\otimes I/m$, the input of Main:282–290. So the Born-form theorem's weights are γ-c with present-visible records.
- **γ-i (invariant prior over record-compatible orbits).** Take maximal entropy among invariant laws supported on $U_r=\bigcup\{O:O\cap A_r\neq\emptyset\}$. By N2.1 the result is $\mathrm{unif}(U_r)$. There are two ways to read it:
  - *As a final assignment.*
    - $U_r\supseteq O^*$, because $s^*\in A_r\cap O^*$.
    - If $\mathrm{unif}(U_r)(A_r)=1$, then $U_r\subseteq A_r$. Since $U_r$ is invariant, $U_r\subseteq I(A_r)$, so $s^*\in I(A_r)$, and the record is not time-varying (G2).
    - So for every time-varying record, $\mathrm{unif}(U_r)(A_r)<1$. In CE-8, with $r=\{x_0=0\}$, the value is $1/2$.
    - **Verdict: excluded** as the observer's assignment for time-varying records.
  - *As a prior followed by Bayesian conditioning on $r$.* This is the reading of Main:62's "selection among orbits". Both clauses are then literal: the prior is invariant, and the records enter by conditioning. By Lemma G, $\mathrm{unif}(U_r)(\cdot\mid A_r)=\mathrm{unif}(A_r)$, which is γ-c.
    - **Verdict: reduces to γ-c.**
- **γ-strict (a single invariant law that gives the records probability 1):** by G2 it is supported on $I(A_r)$, and its maximal-entropy member is $\mathrm{unif}(I(A_r))$.
  - $s^*\in I(A_r)$ requires that the record hold at every point of $O^*$, i.e. that $r$ be the value of a conserved function on $O^*$. Conversely, a conserved-function record puts $O^*$ inside $I(A_r)$. The two directions are checked separately.
  - In CE-8, every visible record has $I(A_r)=\emptyset$.
  - **Verdict: excluded for time-varying records**, and undefined or excluding $s^*$ there.
  - For records that are values of conserved quantities, the law is microcanonical on the level set. That has the form of SM:803–811's "on-shell measure" candidate [P, there a conjecture, with the stationary-law hypothesis open].
  - On the linear rule this law is not α: posit (v) records that the exact linear rule "conserves a quadratic invariant" and "splits its largest energy shell into exponentially many cycles" (Main:726) [P].
- **γ-soft (records as expectation constraints):** the maximal-entropy law under $E_\mu[f_i]=c_i$ is an exponential family [L: Jaynes]. It is invariant when the $f_i$ are conserved.
  - **Verdict: undecidable.** The corpus names no constraint functions.

**Skepticism toward the favorable reading.** The collapse γ-c = β|r could be read as making posit (iv) coherent. It does not derive β: Lemma G shows that a hard constraint returns the uniform law on the constraint set, which is β restricted by definition. So γ-c contains β as its reference measure and contributes only the event. Whether the physical record event is a visible history is the open record-formation question (O-REC, O-RET).

**Verdicts.**
- γ is undecidable as worded.
- Read as an invariant prior followed by conditioning (Main:62), the wording is literal and gives γ-c, which reduces to β-conditioning.
- Read as a single invariant law that gives the records probability 1, the wording fails for every time-varying record (G2).
- NEW finding of this node (a hidden assumption in the posit ledger wording): no invariant law gives a time-varying record probability 1 with $s^*$ in its support, so the observer's assignment (P5) is non-invariant. The ledger's "invariant" applies coherently to the prior over orbits, not to the assignment. This bears directly on O3 (§6).

### N4. α and the frequency reading

**Lemma A (single-run frequencies over a whole cycle)** [D].
- For every $f:S\to\mathbb R$ and every positive multiple $N$ of $|O^*|$ (in particular $N=|O^*|$ and $N=L$), $\frac1N\sum_{t<N}f(\varphi^ts^*)=E_{\mathrm{unif}(O^*)}f$. This holds because $t\mapsto\varphi^ts^*$ covers $O^*$ exactly $N/|O^*|$ times.
- With $f$ the indicator of $\{\pi_Vs=i,\pi_V\varphi s=j\}$, the empirical transition frequencies over such a horizon are exactly $T^{\alpha,O^*}$ on every row that $O^*$ visits.

Under the named hypothesis **H-freq** (probability is the relative frequency along the actual trajectory over a whole cycle of the actual orbit), α is **stipulated**: Lemma A shows that H-freq and α are equivalent statements of the same law. By §2's rule this is not a selection, because H-freq restates α, and it adds nothing under §A.29 (see item 4 below). The countercontrol is CE-8: β's $3/4$ is the cycle frequency of neither orbit.

**Lemma A2 (α versus β)** [K + D].
- α = β whenever $\varphi$ is transitive [K: `ensembleDetermined_of_transitive`, since the only invariant law is then $\mathrm{unif}(S)=\mathrm{unif}(O^*)$].
- Conversely, $\mathrm{unif}(O^*)=\mathrm{unif}(S)$ forces $O^*=S$ [D].
- The wave substratum is not transitive [K]. So β's numbers are cycle frequencies only when the orbit statistics happen to coincide. CE-8 shows that on a generic finite bijection they need not. The wave substratum is unchecked (C-1).

**Lemma A3 (records converge the branches)** [D].
- Conditioning the invariant law $\mu_w$ on $r$ gives weights $\propto w_O|O\cap A_r|/|O|$ on $\mathrm{unif}(O\cap A_r)$.
- If $A_r\subseteq O^*$, every $w$ with $w_{O^*}>0$ gives the same (P5), namely α's.
- For a record with at least $L$ values ($k+1\ge L$), every μ with $s^*$ in its support predicts the visible future with certainty. Every visible sequence is $L$-periodic, so $L$ consecutive agreeing values force agreement everywhere.
- CE-8: after $r=10$, the branches give $P(x_1=1)$ equal to $2/3$ (β), $1$ (α, $O_A$) and $0$ (α, $O_B$). After $r=010$, $A_r\subseteq O_A$ and β|r = α|r, both equal to 1.

So the branches differ exactly in the regime where the probabilities are nontrivial.

**Skepticism toward the favorable reading.** H-freq stipulates α, but:
1. The horizon is the orbit's cycle, of order up to the recurrence time, which no accessible window reaches (Main:141). On accessible windows, empirical frequencies equal α's only under a typicality hypothesis. (EM) (Main:746) and posit (v) (Main:726) are mixing hypotheses for the coarse-grained channel, and neither is shown to supply orbit-frequency typicality.
2. α is ontic and the observer does not know $O^*$, so α cannot serve as the observer's assignment (P5) unless records pin the orbit down (A3).
3. In general α supplies no hidden prior shared by every root, whereas the P2/H-μ results assume a product form (matrix code H-μ, "on a declared product partition"). CE-8 does not show this, because there α is product on each orbit. A minimal instance: $\mathcal C_V=\mathcal C_H=\{0,1\}$ with $\varphi$ swapping $(0,0)\leftrightarrow(1,1)$ and $(0,1)\leftrightarrow(1,0)$. On $O^*=\{(0,0),(1,1)\}$, $\kappa_0=\delta_0$ and $\kappa_1=\delta_1$, which depend on the root.
4. H-freq is a reading of "probability", not a physical premise. Under §A.29 it delivers no independent prediction at accessible horizons.

**Verdict.**
- α is compatible with every non-posited premise. For non-transitive φ it conflicts with Lemma 3 clause 2 and posit (iv), which select counting globally (Main:56, :726).
- The manuscript holds clause 1 (α on the actual orbit, Main:62) and clause 2 together. They are consistent only if clause 2 is read as the epistemic prior over orbits (N3, γ-i as a prior) and clause 1 as the ontic statement.
- α is stipulated by (equivalent to) H-freq at the cycle horizon. It is selected by no premise.
- ELABORATING. As a guard, the result is NEW in the narrow sense that the Born-form theorem's β weights are not single-run frequencies on generic non-transitive bijections (CE-8).

### N5. ε: dynamical non-equilibrium

The reading ch18 proposes is coarse-grained: Born statistics as "the stationary statistics of the cycle for the equilibrated hidden prior", approached on a timescale $\tau_{\rm eq}\sim\tau_B$ [P: ch18 §18.2]. ch18 itself disclaims fine-grained relaxation: "Neither asymptotic convergence to zero nor a universal decay rate follows from the finite reversible substratum dynamics, which is recurrent (§18.7)" [P].

**Coarse-grained ε (the proposed reading).**
- It would need a closed relaxation law and a mixing hypothesis (ch18 §18.2 ledger; H-NEQ).
- The mixing hypotheses the corpus states are (EM) (Main:746) and posit (v) (Main:726) [P]. Neither, as stated, selects the relaxation target:
  - Posit (v) conditions an analysis whose mixing class is "hidden dynamics that relax toward the reference prior between couplings" (Main:453). There the target is an input.
  - (EM) asserts a dissipative gap of a compression, "the coarse-grained effective channel", and does not identify the compression's stationary state with a measure on $S$.

  This reading of the two hypotheses is [D].
- **Verdict: undecidable from current premises.** Conditional on (EM) or (v), coarse-grained ε reduces to whichever reference prior those hypotheses take as input, and selects none.

**Lemma E (fine-grained: no relaxation; time average)** [K + D].
- $\varphi_*$ permutes the values of $\mu$. So:
  - $H(\varphi^t_*\mu)=H(\mu)$ [K: `entropy_marg_of_injective`, `FiniteEntropy.lean:158`];
  - $\|\varphi^t_*\mu-\pi\|_1=\|\mu-\pi\|_1$ for every invariant $\pi$ [D];
  - $\varphi^L_*\mu=\mu$ [D; Main:640].
- So at the fine-grained level no law approaches an invariant law. This agrees with Main:746: "The exact Koopman operator of φ … is a permutation operator: unitary, with modulus-one spectrum and exact recurrence. It has no dissipative gap" [P].
- The Cesàro mean is $\frac1L\sum_{t<L}\varphi^t_*\mu=\Pi(\mu):=\sum_O\mu(O)\,\mathrm{unif}(O)$ [D, the same counting as Lemma A].
- For the ontic initial condition $\mu=\delta_{s^*}$, $\Pi(\delta_{s^*})=\mathrm{unif}(O^*)=\alpha$.
- For an epistemic $\mu_0$ (δ), $\Pi(\mu_0)$ has orbit weights $\mu_0(O)$. It equals β exactly when $\mu_0(O)=|O|/|S|$ for every orbit.

**Verdicts (fine-grained).**
- As a mechanism that selects a law on $S$ by fine-grained relaxation, ε is excluded, for every finite bijection. ch18 does not propose this mechanism.
- The time-averaged stationary law reduces to α (ontic start) or to $\Pi(\delta)$ (epistemic start). It never independently yields β.
- CONFIRMING (it agrees with ch18's and Main:746's recurrence remarks), plus the reduction, which is ELABORATING.

### N6. δ, and what "β is selected" would have to contain

**Lemma U (every rational prior is conditioned counting)** [D].
- Let $\mu(s)=n_s/D$ be rational. Take $S'=S\times[D]$, $\varphi'=\varphi\times\mathrm{id}$ (an inert register), and $A=\{(s,c):c<n_s\}$.
- Then $\mathrm{unif}(A)$ projects to $\mu$, and the visible law is $P_\mu$.
- So every rational δ-law is β′ conditioned on an event in an inert enlargement.
- Counting conditioned on a finite event yields only rational laws. Irrational priors are outside Lemma U's scope.

**Lemma U2 (β is stable under the posit-(ii) enlargements)** [D]. With an independently prepared, decoupled factor and counting on it, $\mathrm{unif}(S\times D)$ projects to $\mathrm{unif}(S)$, so β-laws are unchanged. This is consistent with Main:726 (ii) [P].

**Consequence.** "β is selected" has numerical content only together with:
1. a conditioning event, and
2. the condition that any added register is prepared independently.

Without them, β plus conditioning reproduces every rational δ-law (U). The content that the Born-form theorem uses is the conditional uniformity of $\kappa$ given the visible root (B2.2), i.e. γ-c with present-visible records (N3). It is not global counting as such.

**Verdict.**
- δ is compatible by construction, as a datum, and is not selected.
- On rational priors, δ and "β plus an event" are law-equivalent.
- The residual choice is therefore the event, which is the preparation (interface (c), O-RDY) and the record (O-REC).
- NEW, as a hidden assumption: on rational priors, the measure fork is a fork over a pair (reference measure, conditioning event), and the second component carries the numbers.

### Passes and fixed point

There was one depth-first pass per branch, N0–N6, and one cross-pass checking every lemma against CE-8. NEW findings came from N3 and N6, plus N4 in the narrow guard sense. The §A.31 fixed point of 3–4 consecutive passes with no NEW finding was not reached within this paper budget. That is a limitation.

***

## §4 Results

| Branch | Verdict | Hypotheses | Support | Does NOT establish |
|---|---|---|---|---|
| α | Compatible with every non-posited premise. For non-transitive φ it conflicts with Lemma 3 clause 2 and posit (iv). Selected by no premise. Stipulated by (equivalent to) H-freq at the cycle horizon. Equals β if and only if φ is transitive, one direction at a time. | H-freq; finite S; bijection | Lemma A, A2, A3 [D]; `ensembleDetermined_of_transitive` [K]; non-transitivity of the wave substratum [K]; CE-8 [D] | A selection at any horizon; agreement with α at accessible windows; that α is the observer's assignment; a shared hidden prior; a property of the wave substratum's orbit statistics (§7) |
| β | Compatible, stipulated by Lemma 3 clause 2 and posit (iv), not derived. Its Born-form numbers hold on the whole class "κ uniform on each supported root" (one direction). | Main:56 clause 2 and posit (iv) [P]; product/independence clause (H-μ) | B2 [D]; `counting_maximal_entropy` [K]; Main:56, :726 [P] | That invariance or any non-posited premise selects it; that its numbers are single-run frequencies (CE-8, generic bijections); content without a stated conditioning event (U) |
| γ | Undecidable as worded. As an invariant prior followed by conditioning (Main:62), the wording is literal and reduces to γ-c, i.e. β-conditioning (P5). As a single invariant law giving the records probability 1 (γ-i final, γ-strict), it is excluded for every time-varying record (G2). For conserved records, γ-strict is microcanonical. γ-soft is undecidable. | Reading of "compatible"; record event $A_r$ | Lemma G, G2, N2.1, N3 [D]; `entropy_le_log_card` [K]; CE-8 | Which reading the posit intends [O]; that the physical record is a visible history (O-REC); any γ-soft result |
| δ | Compatible as a datum, not selected. On rational priors, law-equivalent to β plus an event. | Rational weights | Lemma U [D]; Main:518–532 [P] | Any statement about irrational priors; which preparation is physical (c, O-RDY) |
| ε | The proposed reading (coarse-grained relaxation) is undecidable. (EM) and posit (v) are stated but select no target. Fine-grained relaxation, which ch18 does not propose, is excluded for every finite bijection. Its time-average reduces to α (ontic) or Π(δ) (epistemic). | For coarse-grained relaxation: (EM) or posit (v), H-NEQ, a closed relaxation law. Otherwise: a finite bijection | Main:746, :726 (v), :453 [P]; Lemma E [D]; `entropy_marg_of_injective` [K]; Main:640 [P]; ch18 §18.2 [P] | Anything about coarse-grained relaxation beyond its undecidability; ch18's CMB prospect |

**Q-inv, summarized.**
- The form is branch-invariant: class membership, $U_\varphi$, $|U_\varphi|^2\in\{0,1\}$, and exponent-insensitivity (B1 [K+D]).
- The implication of Main:137 holds under every branch (B4 [D]). Its hypothesis and conclusion (rooted indivisibility) do not (B4, CE-8).
- The numbers (P1–P3, P5) are not invariant as a class-wide claim over finite bijections (B3 [D], CE-8). On the manuscripts' wave substratum this is unchecked (C-1).
- (P2) and (P3) are κ-functionals; (P1) also depends on ν.

**Q-sel, summarized.** No branch is physically selected by a current OI premise. The fork reduces to two components:
1. the reading of probability: ontic and frequency (stipulating α) versus observer credence (giving β-conditioning);
2. the conditioning event, i.e. the preparation or record (for rational priors, Lemma U).

**Interfaces.**
- **(a) the exponent.** On native data the exponent is invisible under every branch (B1). No measure choice bears on (a). (a) needs non-monomial sourced operations, which no branch supplies.
- **(c) preparations across settings.** The visible prior ν and the conditioning event from N6 are the preparation. Part (b)'s residual therefore passes into (c) and O-RDY: (b) can fix the reference measure only, and (c) has to supply the event.
- **(d) context independence.** (d2) takes (b)'s μ as its input state. No branch supplies (d1)'s contexts, since complete passive observation reads one commutative algebra (`complete_passive_iff_commutative`, `CentralObservation.lean:620`, as cited by BORN-SRC-1 §4(d) and confirmed by the review of `f6526fb8`). Fixing μ cannot address (d3).

***

## §5 Consequences for #914 (proposals only)

None of these is a status change. Each needs review and an owner decision.

1. **O-BORN.** Record that part (b) has a paper analysis:
   - no branch is selected;
   - the Born form is branch-invariant and the numbers are κ-functionals;
   - the residual choice is (reading, event).

   Row 1e and 17c status: unchanged (O).
2. **O-OBSMU, the μ leg.** The obligation (#866 c.6600176951, item 7) reads "supply independently motivated structure selecting the physical observation map and ensemble, or prove that the claims consuming an induced stochastic law are invariant under that residual choice". Proposal: split the μ leg into
   - **μ-form**, where the invariance option is proved for S ⇔ D ⇔ Q_fb, the Born form and exponent-insensitivity (B1), once reviewed; and
   - **μ-number**, where the invariance option fails as a class-wide claim over finite bijections, for the numbers (B3) and for Main:137's indivisibility conclusion (B4; CE-8), and the selection option remains open.

   The second clause is scoped to the class tested. Whether it holds for the wave substratum's own orbits is computation item C-1. Main:137's implication holds under every branch (B4). That is not a μ-invariance of the consuming conclusion, and it is not proposed for μ-form.
3. **P-7** (`ensemble_underdetermined`) is unchanged. Its consequence is sharpened by N2.1: the undetermined invariant law is exactly a law on orbits.
4. **O-RDY ← O-OBSMU (μ leg).** By N6, the μ-number residual coincides with the readiness/preparation event, for rational priors. The matrix edge "O-OBSMU (μ leg) or a named prior [C]" may be two names for one obligation. This is a proposal for D-12.

***

## §6 Open items and owner questions

- **QB-1 [O] (reading of probability).** Are the representation's numbers single-run frequencies or the embedded observer's credences?
  - Frequencies are equivalent to α at the cycle horizon by Lemma A, and silent at accessible windows.
  - Credences give β-conditioning by γ-c.

  This is a decision about interpretation, not a theorem.
- **QB-2 [O], O3 refined.** O3 asks whether to name β where the "compatible with records" wording appears, or to formalize γ. N3 shows:
  - naming β alone is not enough, because Main:62 and :726 include records, and the Born-form theorem's input is β conditioned on the present visible configuration;
  - "formalizing γ" means choosing a reading. γ-c is short (Lemma G plus conditioning). Its substantive part is the record event, which belongs to O-REC;
  - read as an invariant prior over orbits followed by conditioning (Main:62's "selection among orbits"), the ledger wording is literal and coherent, and gives γ-c;
  - read as a single invariant law that gives the records probability 1, it fails for every time-varying record (G2).

  Which reading is intended? Should G2 be recorded as a finding on Main:62, :726 and ch01:85 (propagation is not authorized here)?
- **QB-3 [O].** Should the μ-form / μ-number split of §5.2, with indivisibility on the μ-number side, be recorded on O-OBSMU after review?
- **QB-4 [O].** Should B4 (Main:137's implication under root-dependent κ) and Lemmas G, G2, U, E and N2.1 go to independent review, and later to Lean (§7)?
- **Open items.**
  - γ-soft needs named constraint functions.
  - Agreement with α at accessible windows (N4) needs a typicality hypothesis. Coarse-grained ε (N5) needs a closed relaxation law and a relaxation target. (EM) (Main:746) and posit (v) (Main:726) are stated mixing hypotheses for the coarse-grained channel, but neither is shown to fix μ on $S$, to fix a target, or to deliver orbit-frequency typicality.
  - The wave substratum's orbit statistics have not been checked (C-1).
- **Out of scope, observed.** At the base, Main:20 and Main:556 still point to "§3.1" for the exponent frontier, so BORN-SRC-1's F2 is unapplied. That item belongs to O2.

***

## §7 Proposed computation (for separate authorization only; nothing run)

- **C-1 (exact enumeration, small wave substrata).**
  - **Instances:** the wave substratum at d = 1, small L, q ∈ {2, 3}, with a declared region R, and the orbit decomposition of φ.
  - **Rule:** state the decision rule, not the expected numbers. The verdict on instance I is "β's one-step numbers are single-orbit frequencies on I" if and only if $T^{\alpha,O}=T^\beta$ exactly over ℚ for every orbit with $|O|\ge\ell_{\min}$, with $\ell_{\min}$ fixed in advance.
    - The comparison is made on the rows each orbit visits.
    - A row that an orbit does not visit is recorded as unvisited and excluded from that orbit's comparison.
    - Any other outcome gives the verdict "not".
  - The verdict is void if no orbit reaches $\ell_{\min}$.
  - The same instances also record, per orbit, whether the α-rooted family is P-divisible on $\{0,\ldots,|O|\}$ (B4).
  - **Controls:**
    - a transitive toy, which must return equality (control for A2);
    - CE-8, which must return $3/4$ against $\{1,1/2\}$, and α on $O_A$ P-divisible against β indivisible;
    - an exact-arithmetic check, with no floating point.
  - The verdict is void if a control fails (§A.29, §A.44).
- **C-2 (Lean, small).**
  - the invariant simplex and the Cesàro identity (N2.1, E);
  - the hard-constraint maximal-entropy lemma, the conditioning identity and G2 (G, G2);
  - Lemma U;
  - B4 as an implication.

  Kernel anchors would be needed for any manuscript use, together with registry entries (§A.35).
- **C-3 (deferred).** Accessible-window frequency distributions against α and β on C-1's instances. This is numerical only and not decisive. It should not run before QB-1 is decided.
