# BORN-SEL (b), QB-3: the μ-form / μ-number classification of O-OBSMU's μ leg, with CE-8 and Lemma B4 (#1059)

## Status

- **Limitation.** OI has not yet been shown to derive the Born rule or select the physical probability measure.
- **What this record is.** The QB-3 obligation classification (§1) and the evidence for the parts of it whose
  support was not on `main`: the swap computation (§3), the counterexample CE-8 (§4) and Lemma B4 (§5).
- **Layer.** Paper derivations [D]. None is kernel-checked. Every other input is a manuscript line or a Lean
  declaration on `main`, classified in §7.
- **Review.** The independent exact-head review of this record is `QB3-EVIDENCE-REVIEW.md`, beside it.
- **Scope.**
  - The classification sources no physical measure and promotes no manuscript claim. No statement in `papers/` or
    `book/` changes.
  - The non-invariance is shown on two non-native finite bijections only. Nothing is inferred for the native wave
    substratum.
  - This record makes no other lemma of the source assessment a premise.
- **Accountable Issue.** #1059. The remaining work is planned there, not here. The QB-4 review ranks B4, with CE-8
  as a decidable witness, first for Lean formalization; that formalization is not authorized (QB-4 ruling, below).
- **Owner decisions this record relies on** (quoted with author and time, §A.42 item 7):
  - #1059 c.6650820790 (amaybaum, 2026-11-05; posted 2026-11-05T05:49:40Z), QB-3: "Record the μ-form / μ-number
    distinction on O-OBSMU after an independent review of the exact proposed wording." "This is an obligation
    classification, not a sourcing of the physical measure." QB-4: "No Lean implementation and no manuscript
    promotion."
  - #1059 c.6651648653 (amaybaum, Claude Code session chat, 2026-11-05; posted 2026-11-05T06:45:16Z): "The owner
    selected **route A** for QB-3: preserve valid mathematical proofs through a reviewed evidence landing on `main`,
    rather than narrowing conclusions purely because their evidence currently exists off-main." "No proof promotion
    before review and evidence retention."
  - #1082 c.6652198391 (amaybaum, Claude Code session chat, 2026-11-05; posted 2026-11-05T07:19:59Z): "The landing
    must explicitly preserve that OI has not yet been shown to derive the Born rule or select the physical
    probability measure."
  - #1082 c.6652561689 (amaybaum, Claude Code session chat, 2026-11-05; posted 2026-11-05T07:42:07Z): "Decision 2:
    Include the QB-3 claim classification in the same landing." "Decision 3: Use a fresh branch from `main`, rather
    than merging the historical research branch." "The landing PR's eventual merge remains subject to my separate
    approval after review and CI."
- **Source of the extract.** §1 is verbatim from `QB3-QB4.md` lines 48–75, and §2, §4 and §5 are verbatim from
  `BORNSEL-B-MEASURE.md` (BSB) r4 at the stated lines. Both files are at commit
  `e50917cab03a1c8db6fd668ecad2a04c880399db` on branch `research/born-sel-b-measure-20261104` (#1082). That commit
  is not on `main`; this record carries the content it uses (§7). Every change from the source text is listed in §6.

***

## 1. The classification (QB-3)

The obligation it classifies is the O-OBSMU μ leg: "supply independently motivated structure selecting the physical
observation map and ensemble, or prove that the claims consuming an induced stochastic law are invariant under that
residual choice" (`verification/ROADMAP.md`:80).

> **O-OBSMU, μ leg: μ-form / μ-number.** This is an obligation classification. It does not source the physical
> measure, and it discharges nothing for a consumer that uses numerical probabilities.
> - **μ-form (invariant within its proved scope).** For every probability law μ on a finite `S = C_V × C_H` and every
>   horizon, the induced finite-horizon law lies in `Q_fb` (`D_imp_Qfb`, `Equivalence.lean:294`). `S ⇔ D ⇔ Q_fb`
>   holds for every finite-horizon law, with each direction kernel-checked (`finite_horizon_equivalence`,
>   `Equivalence.lean:462`). For every μ, the construction in that proof uses the permutation unitary of φ, the
>   product basis and the visible readout, and only the initial weights change. This is a reading of the proof, not a
>   stated theorem. The unitary's entries are 0 or 1, so the recovered table is the same for `|U|^p` at every `p > 0`
>   (Main:556).
> - **μ-number (invariance fails on the tested class; selection open).** On finite bijections, the numerical
>   probabilities change with μ: the finite-horizon law, the rooted family, the one-step rooted matrix (which equals
>   the Born-form theorem's `T_ij` when the hidden law given each root is uniform), and the conditional predictions
>   given a record. Main:60 records this for the two-state swap `φ(x,h) = (h,x)` under uniform versus point-mass hidden
>   priors. On the eight-state bijection CE-8 (§4 of this record), the uniform law on `O_A`, the uniform law on `O_B` and
>   the counting law give one-step matrices `[[0,1],[1,0]]`, `J/2` and `[[1/4,3/4],[3/4,1/4]]`. Main selects the
>   counting measure by a posited maximal-entropy principle (Lemma 3, Main:56; posit (iv), Main:726, "not derived").
>   No derivation of a selection is established, and the physical selection is open.
> - **Indivisibility (Main:137) is on the μ-number side.** The implication holds for every law μ, with the hidden law
>   given each root taken as any probability law on `C_H` (fixed arbitrarily at roots of visible probability zero).
>   The implication: two distinct positive-probability visible histories with a common endpoint at order `k` make some
>   `Γ_s`, `1 ≤ s ≤ min(k, L−1)`, a non-permutation, and then the rooted family is not P-divisible on `{0,…,n}` for
>   every `n > s` with `Γ_n = I`. Support: Main:137 for a hidden prior shared by every root; Lemma B4 (§5 of this record) for
>   root-dependent hidden laws. Whether its hypothesis and its conclusion hold depends on μ. On CE-8, the product law
>   uniform on `O_A` gives a P-divisible rooted family and no such pair of histories, and the counting law gives an
>   indivisible one.
> - **Scope.** The non-invariance is shown on non-native finite bijections: the two-state swap, and CE-8. These are not
>   claimed to satisfy (C2)–(C3) or to be instances of the native wave substratum. Nothing is inferred for the wave
>   substratum, where the question is unchecked.

Where each clause is supported is in §7.

## 2. Notation (BSB:49–50, :66, :126)

- $S=\mathcal C_V\times\mathcal C_H$ is finite, $\varphi$ is a bijection of $S$, and $\pi_V$ projects onto the visible factor. $L$ is the order of $\varphi$. $\mathcal O$ is the set of orbits (cycles), $O^*$ is the orbit of the actual microstate $s^*$, and $n=|\mathcal C_V|$, $m=|\mathcal C_H|$.
- A **measure** $\mu$ is a probability law on $S$ at the reference time. It factors as a visible prior $\nu(a)=\mu(\{a\}\times\mathcal C_H)$ and a **hidden conditional** $\kappa_a(h)=\mu(a,h)/\nu(a)$ on the roots with $\nu(a)>0$. The measure is a **product** measure when $\kappa_a$ does not depend on $a$, i.e. $\mu=\nu\otimes\mu_H$.
- the rooted family $\Gamma^\kappa_t(a,j)=\kappa_a\{h:\pi_V\varphi^t(a,h)=j\}$ (Main:137, Main:640; PROGRAMME §3.4);
- The Born-form $T_{ij}$ of Main:290 equals $\Gamma^\kappa_1$ with $\kappa_a$ uniform on $\mathcal C_H$. So every $\mu$ whose hidden conditional is uniform on each supported root gives exactly Main:290's numbers, whatever $\nu$ is.
- α on `O` means `unif(O)`; β means the counting law.
- `J` is the all-ones matrix.

A *branch* is a choice of the measure μ. P-divisibility of the rooted family on `{0,…,n}` is as defined at Main:137.

## 3. The two-state swap [D]

- **The map.** Main:78 gives the swap `φ(v,h) = (h,v)` on `C_V = C_H = {0,1}`. Reading Main:60's "two-state swap" as
  this map is itself [D], since Main:60 gives no formula.
- **The rooted matrix.** `π_V φ(a,h) = h`, so `Γ_1(a,j) = μ_H{h : h = j}` for every root `a`.
  - Under the uniform hidden prior, `Γ_1 = J/2`.
  - Under the point mass `δ_0`, `Γ_1 = [[1,0],[1,0]]`.
- **The conditional prediction.** For a product law and a root `a` with `ν(a) > 0`, `x_1 = π_V φ(x_0, h) = h` with
  `h` drawn from `μ_H`. So `P(x_1 = j | x_0 = a) = μ_H(j)`, which is row `a` of `Γ_1`.
- **Hence** the rooted family, the one-step rooted matrix, the conditional prediction `P(x_1 | x_0)`, and with it the
  finite-horizon law, differ between the two priors. These are the μ-number objects of §1.

## 4. CE-8 (BSB:129–136)

**Lemma B3 (numbers are not branch-invariant, on a generic finite bijection)** [D]. Counterexample CE-8:
- $\mathcal C_V=\{0,1\}$, $\mathcal C_H=\{0,1,2,3\}$, with $\varphi$ having two orbits of length 4:
  - $O_A:(0,0)\to(1,0)\to(0,1)\to(1,1)\to(0,0)$, with visible sequence $0101\ldots$;
  - $O_B:(0,2)\to(0,3)\to(1,2)\to(1,3)\to(0,2)$, with visible sequence $0011\ldots$.
- **Under β** (uniform $\kappa$): from root 0 the next visible values are $(1,1,0,1)$ over $h=0..3$, and from root 1 they are $(0,0,1,0)$. So $T^\beta=\begin{pmatrix}1/4&3/4\\3/4&1/4\end{pmatrix}$, a non-permutation matrix.
- **Under α:**
  - $T^{\alpha,A}=\begin{pmatrix}0&1\\1&0\end{pmatrix}$;
  - $T^{\alpha,B}=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix}$.

## 5. Lemma B4 (BSB:147–162)

**Lemma B4 (Main:137 as an implication, and its μ-dependent hypothesis)** [D]. Main:137 (gap + finite recurrence ⇒ rooted indivisibility) is stated for "a hidden prior shared by every root", roots of visible probability zero included. As an **implication**, its proof goes through for a root-dependent hidden law.

*Hypotheses.* For **every** $a\in\mathcal C_V$, $\kappa_a$ is a probability law on $\mathcal C_H$; at roots of visible probability zero it is fixed arbitrarily, but it is a probability law there too. Put $\Gamma^\kappa_t(a,j)=\kappa_a\{h:\pi_V\varphi^t(a,h)=j\}$, so every row of every $\Gamma^\kappa_t$ sums to 1. Positivity of a visible history is relative to the joint law $\nu\otimes\kappa$ (root from $\nu$, hidden state from $\kappa_a$).

*Statement.* If two distinct positive-probability visible histories $(x_0,\ldots,x_k)\neq(x'_0,\ldots,x'_k)$ have $x_k=x'_k$, then some $\Gamma^\kappa_s$ with $1\le s\le\min(k,L-1)$ is not a permutation matrix. For every $n>s$ with $\Gamma^\kappa_n=I$ ($n=L$ among them), no row-stochastic $\Lambda$ satisfies $\Gamma^\kappa_n=\Gamma^\kappa_s\Lambda$, so the rooted family is not P-divisible on $\{0,\ldots,n\}$.

*Proof.*
- (i) $\varphi^L=\mathrm{id}$ gives $\Gamma^\kappa_L=I$ for every $\kappa$, and $\varphi^{t+L}=\varphi^t$ gives $\Gamma^\kappa_{t+L}=\Gamma^\kappa_t$.
- (ii) Suppose every $\Gamma^\kappa_s$ with $1\le s\le\min(k,L-1)$ is a permutation matrix, with permutation $\sigma_s$. By (i), every $\Gamma^\kappa_t$ with $t\le k$ is then a permutation matrix ($I$ when $L\mid t$, otherwise $\Gamma^\kappa_{t\bmod L}$ with $1\le t\bmod L\le\min(k,L-1)$). So for every root $a$ and $\kappa_a$-almost every $h$, $\pi_V\varphi^t(a,h)=\sigma_t(a)$, and every positive-probability history is $(\sigma_t(x_0))_{t\le k}$. Two distinct such histories therefore have distinct roots $x_0\neq x'_0$, and $\sigma_k(x_0)=x_k=x'_k=\sigma_k(x'_0)$ contradicts $\sigma_k$ being a bijection.
- (iii) If $\Gamma^\kappa_n=I=\Gamma^\kappa_s\Lambda$ with $\Lambda$ row-stochastic, then $\Gamma^\kappa_s$, which is row-stochastic because every $\kappa_a$ is a probability law, has a stochastic right inverse, so it is a permutation matrix (`isPermMatrix_of_stochastic_inverse`, via Main:133). This contradicts the choice of $s$.

The implication does not depend on the choice of $\kappa_a$ at roots of visible probability zero. What the conclusion says about those roots' rows does depend on it.

The theorem holds under every branch. Whether its **hypothesis** holds, and so whether its **conclusion** holds, depends on μ. CE-8 shows this. Its three laws are **product** laws: $\mathrm{unif}(O_A)=\mathrm{unif}\{0,1\}\otimes\mathrm{unif}\{0,1\}$, $\mathrm{unif}(O_B)=\mathrm{unif}\{0,1\}\otimes\mathrm{unif}\{2,3\}$, and counting $=\mathrm{unif}\{0,1\}\otimes\mathrm{unif}(\mathcal C_H)$. So the μ-dependence of hypothesis and conclusion already lies inside Main:137's shared-prior scope; the root-dependent extension above is needed only for hidden laws that depend on the root.
- Under α on $O_A$, $\kappa_0$ and $\kappa_1$ are both uniform on $\{0,1\}$. Then $\Gamma_1$ is the swap and $\Gamma_2=I$, and every $\Gamma_t$ is a permutation. The rooted family is P-divisible ($\Gamma_2=\Gamma_1\cdot$swap), and there is no gap.
- Under β, or under α on $O_B$, $\Gamma_1$ is not a permutation and $\Gamma_4=I$. So no stochastic $\Lambda$ satisfies $\Gamma_4=\Gamma_1\Lambda$, and the family is not P-divisible on $\{0,\ldots,4\}$.

## 6. Changes from the source text

Every passage of §1, §2, §4 and §5 is the source text at `e50917ca`, except for these changes:
1. **Headings.** The section headings and their line references are this record's own.
2. **BSB:147.** Its bracket `[D; corrected after review #1082 c.6651169194, the r4 wording not re-reviewed]` becomes
   `[D]`: the source's revision and reviewer note is removed. BSB:167, the source's review note on B4, is outside the
   extract.
3. **BSB:133.** "(C1 witness)" is removed, since the classification makes no (C1) claim.
4. **Citations of passages not carried.**
   - BSB:66 drops its list label "(P2) ".
   - BSB:126 drops its item number and list label "2. (P3) ", and keeps only its first two sentences.
5. **Markers in §1.** In `QB3-QB4.md` lines 61 and 69, "[landed record]" becomes "(§4 of this record)" and
   "[landed B4]" becomes "Lemma B4 (§5 of this record)".
6. **Added definitions** (§2). "α on `O` means `unif(O)`; β means the counting law", which gives the meanings the
   source assigns at BSB:39–40. "`J` is the all-ones matrix."

Everything else in this record is this record's own text: the status header, the framing sentences of §1 and §2,
§3, this section and §7.

## 7. Support and references (§A.42 item 8)

**Support on `main`.** Each item is checked at this record's base, `main` `4f016afd943f5a3939493eab752664949e90dbbb`.

| Reference | Used for | Classification |
|---|---|---|
| `D_imp_Qfb` (`Equivalence.lean:294`), its proof term (`Equivalence.lean:297–299`), `finite_horizon_equivalence` (`Equivalence.lean:462`), all in `verification/lean-mathlib/OIBridge/` | μ-form | support on `main` [K]; "the same unitary, basis and readout" is a paper reading of the proof term |
| `isPermMatrix_of_stochastic_inverse` (`verification/lean-mathlib/OIBridge/EquivalenceChain.lean:110`); Main:133 | B4 (iii) | support on `main` [K] |
| Main:556 | μ-form, the exponent | support on `main` |
| Main:56 (Lemma 3); Main:726 (posit (iv), "not derived") | μ-number, the selection | support on `main` |
| Main:60; Main:78 (the map `φ(v,h)=(h,v)`) | μ-number, the swap | support on `main` for the phenomenon and the map; the computation is §3 [D] |
| Main:137 | indivisibility for a shared prior; the definitions of `Γ_t` and of P-divisibility; B4 | support on `main` |
| Main:290 | the Born-form `T_ij` (§2) | support on `main` |
| Main:640 | cited at BSB:66 beside the definition: a bijection of finite order `L` gives an `L`-periodic law | support on `main` |
| `verification/programmes/oi-qm/PROGRAMME.md` §3.4 (line 96) | `Γ^κ_t`'s definition, as cited at BSB:66 | support on `main` |
| `verification/ROADMAP.md`:80 | the O-OBSMU obligation text | support on `main` (a frozen historical record) |
| `QB3-EVIDENCE-REVIEW.md` | the review entry of the status header | support on `main` |

**References off `main`.** Each is classified by the claim it is attached to.

| Reference | Attached to | Classification |
|---|---|---|
| Commit `e50917ca`; `BORNSEL-B-MEASURE.md` r4 and `QB3-QB4.md` on branch `research/born-sel-b-measure-20261104`; PR #1082 | the source of §1, §2, §4 and §5 | provenance: this record carries the text it uses |
| #1059 c.6650820790, c.6651648653; #1082 c.6652198391, c.6652561689 (owner records) | the status header | provenance (§A.42 item 7): owner decisions on what is recorded and how it lands, quoted with author and time; no mathematical claim rests on them |
| #1082 c.6651169194 (model-authored review of the QB-3 wording and of Lemma B4) | the corrected wording; B4's hypothesis correction | provenance: the wording and B4 stand on §1–§5 and the support above |
| #1082 c.6651181144 (model-authored review; it recomputed CE-8 as a toy control) | CE-8's numbers | provenance: the numbers stand on the hand derivation in §4 |
| #1082 c.6651778560 and c.6651925573 (model-authored rechecks of the source branch) | B4's corrected hypothesis | provenance |
| #866, #914 (where the O-OBSMU obligation is tracked) | §1 | provenance: no status lives in an Issue (§A.45 rule 1) |
| #1059 | the accountable Issue | provenance |
