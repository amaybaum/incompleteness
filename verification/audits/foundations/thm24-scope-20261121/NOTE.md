# THM24-SCOPE: membership scope of Substratum Theorem 24(iii)

Stream 1 of the research streams authorized at
[#1169 c.7063843557](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7063843557).
Issue #1485. Research and design only: nothing here edits a manuscript, and nothing here is under
the #1477 retirement ledger.

Line numbers are those of `main` at `df6da1c6` unless marked otherwise. "Predicted" text is the
#1477 plan's text, read from `edits.json` at `55544cc3` (branch `research/a1exit-deletion-20261121`,
read-only).

## 1. Questions

- **Q1.** Is the restriction of Theorem 24(iii) to bijective factor dynamics (A2), made by #1477
  §28 (D362–D364, D368, D370–D373), necessary? Either an explicit enlargement with non-bijective
  dynamics whose image is not in $\mathcal G_{\rm sub}$ as the corpus uses it, or membership for a
  stated wider class.
- **Q2.** Does the text on `main` overstate anything about Theorem 24 beyond what §28 fixes, at any
  mirror or summary?
- **Q3.** N3: is $\operatorname{Tr}\sigma_A=1$ needed for the identity D364 extends, and is it
  missing from D364? N4: the book summaries of Theorem 24(i) without "(finite $\mathcal C_H$)".

## 2. Definitions used

The corpus gives $\mathcal G_{\rm sub}$ no set-theoretic definition. Every characterization of it
quantifies over substrata $(S,\varphi)$ with $\varphi$ a bijection:

| Site | Text |
|---|---|
| Substratum:94 (A2) | "$\varphi: S \to S$ is a bijection (deterministic, reversible dynamics)" |
| Substratum:249 | "Write $\sim$ for equality of the specified coherent-channel data at that fixed interface … The representative freedoms denoted by $\mathcal{G}_{\text{sub}}$ below are compared on their stated data" |
| Substratum:251 | Theorem 24: "$\mathcal{G}_{\text{sub}}$ contains the independent families of transformations (i) and (iii) below" |
| Substratum:292 | "$\mathcal{G}_{\text{sub}}$ acts on $(S, \varphi)$ before the trace-out" |
| ch02:136 | "the substratum is a set … with a bijection on it. $\mathcal{G}_{\text{sub}}$ is a symmetry of the *equivalence class of substrata*" |
| Computation:254 | "$\mathcal{G}_{\text{sub}}$ partitions the space of bijections into equivalence classes" |
| Structure:646 | Proposition 9.5: "$(S_1,\varphi_1)$ and $(S_2,\varphi_2)$ … OI-class substrata (satisfying A1-A6) related by … a deep-sector enlargement" |

**Working definition (D-mem).** A transformation is a member of $\mathcal G_{\rm sub}$ only if it
sends a substratum $(S,\varphi)$ with $\varphi$ bijective to a pair $(S',\varphi')$ with $\varphi'$
a bijection of $S'$, and preserves $\sim$ at the fixed interface. D-mem states a necessary condition
read off the table; it is not a definition the corpus states, and Q1's verdicts hold relative to it.

Other definitions used:

- The coherent channel, Substratum:253: $\Phi_t(\rho_V)=\operatorname{Tr}_H[\hat\varphi^{t}(\rho_V\otimes\omega_H)\hat\varphi^{-t}]$, $\hat\varphi$ the permutation unitary.
- The enlarged channel, Substratum:258–261: $\Phi'_t(\rho_V)=\operatorname{Tr}_{HA}[(U^t\otimes W^t)(\rho_V\otimes\omega_H\otimes\sigma_A)(U^{\dagger t}\otimes W^{\dagger t})]$.
- The hidden-prior channel family on a measurable hidden carrier, Main:336 (Corollary, measurable hidden carrier): $\Phi_t(\sigma)=\int_H\Psi_{t,h}(\sigma)\,\rho(dh)$, $\Psi_{t,h}(|x\rangle\langle y|)=[K_t(x,h)=K_t(y,h)]\,|A_t(x,h)\rangle\langle A_t(y,h)|$, defined when $x\mapsto F^t(x,h)$ is injective for every $t,h$.
- The kernel's padding theorem, `padData_rooted` (`verification/lean-mathlib/OIBridge/OperationalSourcing.lean:476`), cited at Main:656.

## 3. Productivity test (fixed before any check)

A branch is a **gem** iff it yields a fact strictly stronger than the obvious restatement
"a non-bijective map is not a bijection, so its product is not A2", and that fact either constrains
the wording of a Theorem 24 site or exposes a hidden assumption. Otherwise it is recorded as a
non-gem (CONFIRMING or ELABORATING). Output classes as §A.31.

## 4. Branch plan

- **N1** What does membership require (D-mem)? Verdict by reading.
- **N2** Q1, classical factor: does a non-injective $w$ give an enlargement outside D-mem while the
  Main:336 family is unchanged? Exhaustive finite check (C2).
- **N3** Q1, Hilbert factor: which unitaries $W$ make the enlargement a member up to the choice of
  basis of the factor, and which isometries can occur? Exact algebra and exhaustive finite check (C3).
- **N4** Q1, the reached equivalence classes: does the restriction lose any observational datum?
- **N5** Q2: corpus-wide reading of every Theorem 24 site.
- **N6** Q3: normalization (C1 countercontrol) and the N4 sites.

## 5. Preregistered checks and decision rules

Script `thm24_checks.py`, exact arithmetic only (Python `fractions`, complex numbers as pairs of
rationals). Output `thm24_checks.json`. Carrier: $|\mathcal C_V|=2$, $|\mathcal C_H|=2$, all 24
bijections $\varphi$ of $S=\mathcal C_V\times\mathcal C_H$, times $t=1,\dots,4$, every matrix unit
$|x\rangle\langle y|$ as input (linearity covers every $\rho_V$).

- **C1 (iii), Hilbert factor.** Factor dimensions 1–3; $W$ ranging over every permutation matrix of
  that dimension and, in dimension 2, the rational rotation $\begin{psmallmatrix}3/5&-4/5\\4/5&3/5\end{psmallmatrix}$,
  $\operatorname{diag}(1,i)$ and $\operatorname{diag}(1,-1)$; $\sigma_A$ ranging over a diagonal, a real
  non-diagonal and a complex non-diagonal density matrix. Claim: $\Phi'_t=\Phi_t$ in every case.
- **C2 (iii), classical factor.** $|A|\in\{1,2,3\}$, every map $w:A\to A$ (1+4+27), two laws
  $\alpha$. Claims: (a) $\varphi\times w$ is a bijection of $S\times A$ iff $w$ is a bijection, for
  every $\varphi$; (b) the Main:336 hypothesis (fibre-injectivity) holds for $\varphi\times w$ for
  every $w$; (c) the Main:336 family of the enlarged carrier, prior uniform times $\alpha$, equals the
  original family for every $w$.
- **C3 spectral criterion.** A unitary on $\mathbb C^d$ is unitarily similar to a permutation matrix
  iff its characteristic polynomial equals that of some permutation matrix (normal matrices are
  unitarily similar iff they have the same spectrum with multiplicity). Claim to be decided, for
  $d\le3$ and the C1 unitaries: which are similar to a permutation matrix.
- **Controls (each must come out as stated, or every verdict above is void):**
  - **K1 normalization.** $\sigma_A$ with trace 2: $\Phi'_t=2\Phi_t\neq\Phi_t$ for every case.
  - **K2 coupling.** A coupled permutation of $S\times A$ (a hidden–factor controlled swap) changes
    the channel for at least one $\varphi$ and $t$; in C2, a factor map that depends on the visible
    coordinate changes the Main:336 family for at least one case.
  - **K3 relabelling prior.** Theorem 24(i) with uniform $\omega_H$ leaves $\Phi_t$ unchanged for
    every $\varphi$ and $t$; with $\omega_H=\operatorname{diag}(2/3,1/3)$ and $\sigma$ the swap it
    changes $\Phi_t$ for at least one $\varphi$ (cf. the countermodel K4 of the R6 pass,
    `verification/audits/foundations/a1exit-r6-20261120/RESULT.md:49`).
  - **K4 implementation.** The script's coherent channel for $\varphi$ and its Main:336 family
    (factor trivial) agree for every $\varphi$, $t$ and input (Main:336 part (a)), so the two
    computations are independent and consistent.
- **Decision rule.** A claim holds iff the script reports it for every case enumerated, with every
  control as stated. A failing control voids the verdicts; nothing is re-run with changed cases.
  Each verdict is evidence about the enumerated set only; universal statements rest on the exact
  algebra given beside them, not on the enumeration.
