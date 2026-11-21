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

## 6. Check results

`python3 -I thm24_checks.py` writes `thm24_checks.json` (sha256 `6754aadd…a1bb460` for script
sha256 `ce81c8ae…6d279579`); a second run reproduces the file byte for byte. Every claim and every
control of §5 came out as preregistered: verdict `pass`.

| Check | Result |
|---|---|
| C1 | 3840 / 3840 cases equal (15 unitaries $W$ in dimensions 1–3, 3 states $\sigma_A$ each in dimensions 2–3, 24 $\varphi$, 4 times); every $W$ passes $W^\dagger W=WW^\dagger=1$ exactly |
| C2a | for every $\varphi$ and each of the 32 maps $w$ ($\lvert A\rvert\le3$), $\varphi\times w$ is a bijection of $S\times A$ iff $w$ is |
| C2b | the Main:336 fibre-injectivity hypothesis holds for $\varphi\times w$ for every $w$, the 23 non-bijective maps included |
| C2c | 6048 / 6048 cases: the Main:336 family of the enlarged carrier (prior uniform $\times\alpha$, two laws $\alpha$ per $\lvert A\rvert\ge2$) equals the original |
| C3 | similar to a permutation matrix: every permutation matrix, $\operatorname{diag}(1,-1)$, $R_3\,C\,R_3^{\mathsf T}$; not similar: the rotation $(3/5,4/5)$, $\operatorname{diag}(1,i)$, $R_3$ |
| K1 | 480 / 480: with $\operatorname{Tr}\sigma_A=2$, $\Phi'_t=2\Phi_t\ne\Phi_t$ |
| K2 | coupled hidden–factor swap: 44 / 96 cases change the channel; visible-dependent classical factor map: 20 / 96 change the family |
| K3 | uniform $\omega_H$: 96 / 96 unchanged under the swap relabelling; $\omega_H=\operatorname{diag}(2/3,1/3)$: 40 / 96 change the channel and 40 / 96 change the rooted populations (supplementary output) |
| K4 | 96 / 96: the Main:336 family with a trivial factor equals the coherent channel (Main:336 part (a)) |

C3's expected classification was fixed from the eigenvalues before the run: $(3\pm4i)/5$ and
$\{1,i\}$ are not unions of complete sets of roots of unity; $R_3$ is a rotation with
$\cos\theta=1/3$; $\{1,-1\}$ and the spectrum of a conjugated 3-cycle are.

Two changes were made to the script after the preregistration commit and before its results were
recorded: a no-op statement was removed, and K3 gained the supplementary population count, which
gates nothing. No case or threshold was changed.

## 7. Branch nodes and verdicts

**N1 — what membership requires.** Every characterization in §2 quantifies over substrata with
bijective dynamics, and Theorem 24 places in $\mathcal G_{\rm sub}$ transformations of such
substrata. Verdict: D-mem is the corpus's implicit condition; the corpus has no formal definition,
and no Lean module defines $\mathcal G_{\rm sub}$ (no identifier for it under
`verification/lean-mathlib/` or `verification/lean/`). Layer: prose reading.

**N2 — classical factor (Q1, decisive branch).**
- *Exact algebra, universal.* For $S\neq\varnothing$ and $\varphi$ a bijection of $S$,
  $\varphi\times w$ is injective iff $w$ is, and surjective iff $w$ is: both properties are
  componentwise. So an enlargement $(S\times A,\varphi\times w)$ satisfies A2 iff $w$ is a bijection.
- *Counterexample.* $\lvert\mathcal C_V\rvert=\lvert\mathcal C_H\rvert=2$, $\varphi=\mathrm{id}$,
  $A=\{0,1\}$, $w\equiv0$, any probability $\alpha$. Then $\varphi\times w$ is not injective, so
  $(S\times A,\varphi\times w)$ violates A2 and is not a substratum; by D-mem the enlargement is not a
  member of $\mathcal G_{\rm sub}$. Its Main:336 family equals the original at every $t\le4$ (C2c);
  the exact proof of Substratum:266 gives every $t$.
- *Where it holds.* The Main:336 family is defined for every measurable $w$, since fibre-injectivity
  comes from $\varphi$ alone (C2b; algebraically, $x\mapsto(\varphi^t(x,h),w^ta)$ is injective because
  $\varphi^t$ is). So the channel identity of D364 for "any measurable map $w$" is supported, and the
  membership restriction of D362/D363 is necessary under D-mem.
- Verdict: **necessary** relative to D-mem; CONFIRMING (it is the obvious restatement, so a non-gem
  under §3). Layers: exact algebra (universal); exhaustive finite computation (the enumerated set).

**N3 — Hilbert factor (Q1).**
- *Isometries.* On a finite-dimensional $\mathcal K_A$, an isometry $W:\mathcal K_A\to\mathcal K_A$
  is unitary ($W^\dagger W=1$ makes $W$ injective, hence invertible, so $WW^\dagger=1$). A non-unitary
  isometry exists only for infinite dimension. Among isometries that send basis vectors to basis
  vectors, $|a\rangle\mapsto|w(a)\rangle$, the non-unitary ones are exactly those with $w$ injective
  and not surjective, as the shift $n\mapsto n+1$ on $\mathbb N$; these violate A2's surjectivity.
  Layer: exact algebra.
- *Unitaries: membership is relative to the factor's basis.* If $VWV^\dagger=P_\psi$ for a unitary
  $V:\mathcal K_A\to\ell^2(A)$ and a bijection $\psi$, then $1\otimes V$ carries the datum
  $(U\otimes W,\ \rho_V\otimes\omega_H\otimes\sigma_A)$ to the member datum
  $(P_{\varphi\times\psi},\ \rho_V\otimes\omega_H\otimes V\sigma_AV^\dagger)$, and
  $\operatorname{Tr}_A[(1\otimes V)X(1\otimes V^\dagger)]=\operatorname{Tr}_AX$, so every reduced
  quantity agrees. The factor's basis is traced out and fixed by no observation datum, so such a $W$
  is a member presented in another basis. In finite dimension, normal matrices are unitarily similar
  iff their spectra agree with multiplicity, and a permutation matrix's spectrum is a union of
  complete sets of $m$-th roots of unity, one per cycle. Hence:

  > *A unitary $W$ on $\mathbb C^d$ is carried to the permutation unitary of a bijection by a unitary on the factor alone iff its spectrum, with multiplicity, is a union of complete sets of $m$-th roots of unity.*

  C3 instantiates both directions: $\operatorname{diag}(1,-1)$ and $R_3CR_3^{\mathsf T}$ are members
  in another basis; the rotation $(3/5,4/5)$, $\operatorname{diag}(1,i)$ and $R_3$ are not, in any
  basis, and remain channel-preserving extensions only (C1).
- *Bearing on D364.* D364 reads "such enlargements are channel-preserving extensions, not members of
  $\mathcal{G}_{\text{sub}}$, when their dynamics is not a bijection of configurations". For a
  Hilbert space $\mathcal K_A$ given without configurations, the clause is correct only when read as
  "in no orthonormal basis". Read relative to a given basis, it misclassifies
  $W=\operatorname{diag}(1,-1)$, which is the swap in the Hadamard basis.
- Verdict: **gem** under §3. It is stronger than the obvious restatement and constrains D364's
  wording. Classification: **NEW**, small. The corpus treats "permutation unitary" as given with a
  basis, while for the added factor the basis is unobservable. Pressure test: the favorable reading
  widens membership, so it was checked against D-mem. The rebased datum is a pair
  $(S\times A,\varphi\times\psi)$ with bijective dynamics, and the isomorphism $1\otimes V$ acts on
  the traced factor alone. The finite-dimensional criterion is exact algebra. For an
  infinite-dimensional unitary no spectral criterion is stated here (not established).

**N4 — reached equivalence classes (Q1).** Every channel-preserving extension of §28 (any unitary
or isometry, any measurable $w$) has the fixed-interface family of the original. So does the
trivial member $\psi=\mathrm{id}_A$, and more generally any factor dynamics given by a trace-preserving
map on the factor alone: the reduced state factors as $\Phi_t(\rho_V)\cdot\operatorname{Tr}\mathcal E_t(\sigma_A)$.
For finite $A$ and non-injective $w$, $w$ restricts to a bijection $\psi_\infty$ of its eventual
image $A_\infty$, and $(S\times A_\infty,\varphi\times\psi_\infty)$ with law $(w^N)_*\alpha$ is a
member with the same family, consistent with A2's eventual-image clause (Substratum:94). Verdict:
the restriction to bijective dynamics is necessary for membership and loses no fixed-interface
datum: no equivalence class $[(S,\varphi)]/\mathcal G_{\rm sub}$ is enlarged by admitting the wider
class. Classification: POSITIVE. Layer: exact algebra.

**Lean.** No Lean statement concerns $\mathcal G_{\rm sub}$ or Theorem 24. The nearest is
`padData_rooted` (`OIBridge/OperationalSourcing.lean:476`, census family carried by Main:656). For
a finite ancilla type, every unitary matrix $W$ on it and every real weight $w$ with
$\sum_x w(x)=1$, the padded fixed-basis datum `padData Q Anc W w` (evolution $Q.U\otimes W$, initial
law $Q.\mathrm{init}\cdot w$, readout ignoring the ancilla) has the same rooted family
`rooted t a j` as `Q`, at every root, outcome and time. Here `rooted` is the collapse-chain law
$(\lvert U\rvert^{2})^{t}$ conditioned on the root (`QuantumRepresentation.lean:150–161`). The
theorem is a population-level identity for an arbitrary finite unitary pad. It proves no coherent
channel identity, says nothing about infinite or isometric ancillas, and asserts no
$\mathcal G_{\rm sub}$ membership. It agrees with N4: the kernel admits arbitrary unitary pads as
equivalence-preserving at its level, without a membership claim.

**N5 — corpus sites (Q2).** See §8.

**N6 — normalization and N4 (Q3).** See §9.

## 8. Q2: Theorem 24 sites on `main` beyond §28

Sites read: every hit of "Theorem 24", "enlargement", "ancilla", "uniform hidden" and "relabel" in
`papers/*.md` and `book/*.md` (FULL mirrors located by exact-line match). The appendix tables carry
no Theorem 24 row. "Ledger" names a #1477 edit on the line; those lines are frozen, and a finding
there routes only through #1477 or after it lands.

| # | Site | Ledger | Finding | Class |
|---|---|---|---|---|
| F1 | Methodology:353 | none | "*State relabeling* — conjugating the bijection by a permutation of the hidden states applied uniformly in every visible fibre, which preserves every channel". The uniform (or $\sigma$-invariant) hidden prior is omitted. Under $\omega_H=\operatorname{diag}(2/3,1/3)$ the swap changes channels and populations (K3; the R6 pass's K4 countermodel, `a1exit-r6-20261120/RESULT.md:49`, is the diffuse-carrier analogue) | overstatement: omitted hypothesis |
| F2 | ch02:140 = FULL:770 | none | The statement of (i) gives no prior. "produces the same emergent physics" is stronger than the fixed-interface coherent data of Substratum:249/253. "The transition probabilities depend on … not on which labels are attached to which hidden states" fails under a non-uniform prior (K3). The prior appears only in the proof (ch02:148) | overstatement: omitted hypothesis, unscoped "emergent physics" |
| F3 | ch02:134 = FULL:764; Structure:154 | Str:154 D369 | "uniform hidden-coordinate relabelling … preserve[s] the coherent family" with no prior. "uniform" here means fibre-uniform (the next sentence contrasts fibre-dependent relabelling), so the prior is unstated | omitted hypothesis, milder (summary of a scoped theorem) |
| F4 | Substratum:300 | none | $\mathcal G_{\rm sub}$ "is a symmetry of the *equivalence class of substrata*, defined by the condition that all observables are preserved". Theorem 24's own scope (Substratum:249, and the proof's "It preserves the fixed observed data, not measurements that access $A$", :266) is the specified fixed-interface data | definitional overstatement relative to §4's own definition |
| F5 | ch02:148 = FULL:778 | none | The proof of (iii) uses $\sigma_A$ and $W$, which the book's statement (ch02:144, and D370's text) never introduces | cosmetic notation |
| F6 | Structure:683 | none | "where the earlier formulation named only the first and third": revision-history voice in paper prose (§A.33). Outside Theorem 24's scope, recorded in passing | editorial |

No other site overstates Theorem 24. Checked and found consistent, as special cases, as
channel-identity statements without a membership claim, or as already scoped:
- Substratum:16, 50, 60, 139, 191, 235, 268, 292, 395, 429, 437, 538, 548;
- Structure:49, 64 (a proposal §6 rejects), 196, 206, 646–654, 693;
- Introduction:36; Complexity:206, 214; Computation:254; Methodology:355, 467; GR:138;
- ch02:28, 44, 146, 172; ch03:80, 136, 142, 220; ch04:172; ch14:234.

The sites §28 edits (Substratum:54, 201, 249, 253, 257, 262; Structure:53, 154; ch02:144 =
FULL:774) carry the class-D cases. After §28 their only residue is N3's wording point (§7, N3).

## 9. Q3: N3 and N4

**N3: needed, and carried; cosmetic.**
- *Exact algebra.* For any positive trace-class $\sigma_A$ and any isometry $W$,
  $\Phi'_t=(\operatorname{Tr}\sigma_A)\,\Phi_t$: the factor contributes
  $\operatorname{Tr}(W^t\sigma_AW^{\dagger t})=\operatorname{Tr}\sigma_A$. So the identity holds iff
  $\operatorname{Tr}\sigma_A=1$, and K1 instantiates the failure ($\Phi'_t=2\Phi_t$). The
  normalization is necessary.
- *Text.* In the predicted Substratum:262, D364's sentence follows, in the same paragraph, "it uses
  the normalization $\operatorname{Tr}\sigma_A=1$ (respectively $\alpha(A)=1$)", and it says the
  identity and its proof "hold unchanged". The normalization is therefore stated. The residue is
  that D363 introduces $\sigma_A$ as a density matrix on $\ell^2(A)$, while D364 passes to a Hilbert
  space $\mathcal K_A$ without reintroducing $\sigma_A$ there. "Density matrix" is also what excludes
  the singular states the R6 pass flagged (P1).
- *Contrast.* The kernel's conditioned rooted law is a ratio, `jointMass / rootMass`, and both
  scale by $\sum_x w(x)$. By the definitions, that law needs only a nonzero total weight. The
  unconditioned channel of Theorem 24(iii) needs the normalization. This is exact algebra from the
  Lean definitions; no kernel theorem states it.
- Verdict: cosmetic. Optional precision for D364: "for any density matrix $\sigma_A$ on $\mathcal K_A$ and any unitary or isometry $W$".

**N4: cosmetic where a uniform prior is named; substantive where no prior is named.**
- *Where a uniform prior is named* (ch02:172 = FULL:802, ch03:80 = FULL:941, ch03:136 = FULL:997):
  a uniform probability on $\mathcal C_H$ exists only for finite $\mathcal C_H$. A countably
  infinite set has none, and an uncountable one needs a reference measure. So "uniform hidden prior"
  carries finiteness, and adding "(finite $\mathcal C_H$)" is cosmetic.
- *Where no prior is named* (F1–F3: Methodology:353, ch02:140 = FULL:770, ch02:134 = FULL:764,
  Structure:154), the missing hypothesis is the prior itself, not finiteness. That gap is real (K3).
- The precise hypothesis of (i) is $\sigma$-invariance of the hidden prior: uniform on a finite
  $\mathcal C_H$, or any prior $\sigma$ preserves. For a diagonal prior this follows directly from
  the conjugation identity in the proof at Substratum:266, and the R6 pass proves the
  measurable-carrier form. The uniform prior is the framework's baseline (Main:268). The minimal
  correction names it.

## 10. Proposed corrections (record only; routing is an owner decision)

None is applied. Lines under the #1477 ledger (Structure:154, and D364's text) can change only
through #1477 or after it lands.

- **P1 (F1, Methodology:353).** "… applied uniformly in every visible fibre, which preserves every
  channel under the uniform hidden prior (a fibre-dependent …".
- **P2 (F2, ch02:140 = FULL:770).** "For a finite hidden configuration set $\mathcal{C}_H$ with the
  uniform hidden prior and any bijection $\sigma$ …, the substratum $(S, \pi \circ \varphi \circ
  \pi^{-1})$ has the same coherent visible channels as $(S, \varphi)$ at the fixed interface. Under
  that prior the transition probabilities depend on …". Mirror both files (§A.14).
- **P3 (F3, ch02:134 = FULL:764; Structure:154 after #1477).** "uniform hidden-coordinate
  relabelling with the uniform hidden prior". This also settles N4 at these sites.
- **P4 (F4, Substratum:300).** "defined by the condition that the specified fixed-interface
  observation data are preserved (§4)".
- **P5 (N3 node, D364; for #1477's final scientific review).** Either "…not members of
  $\mathcal{G}_{\text{sub}}$ unless a unitary on the factor carries $W$ to the permutation unitary of
  a bijection", or leave D364 as is and read "bijection of configurations" basis-free. Add "for any
  density matrix $\sigma_A$ on $\mathcal K_A$" (N3, optional).
- **P6 (F5).** Introduce $\sigma_A$ and $W$ in the book's statement of (iii) when ch02:144's D370
  text lands.

Each correction narrows or scopes a statement; none strengthens one (§A.22). Bands unchanged:
consistency work only (§A.23).

## 11. Assumption-watch markers (cross-propagation, §A.31)

- **AW1 (basis-relative membership).** Wherever the corpus says "permutation unitary" of a factor
  that is traced out, membership is fixed only up to a unitary on that factor. In finite dimension
  the invariant criterion is the cycle-type spectrum (§7, N3).
- **AW2 (prior as a hidden hypothesis of relabelling).** Statements that a relabelling "preserves
  every channel" depend on the hidden prior's invariance. A non-uniform (structured) prior, as in
  Main §3.4, breaks them (K3).

## 12. Fixed point

Passes over the branches: N2 (CONFIRMING), N3 (NEW), N4 (POSITIVE), the N5 site sweep (F1–F4 new
site findings, ELABORATING the R6 pass's relabelling scope to the summaries), N6 (CONFIRMING for N3,
ELABORATING for N4). A further pass over the Lean census families mentioning ancillas and
relabelling (`OperationalSourcing`, `DiagonalTheory.preservesDiag_relabel`,
`DilationChoice.readback_relabel`) found no $\mathcal G_{\rm sub}$ statement: the first is diagonal preservation of a relabelled correlation extension, the second the name-independence of a dilation readback. The §A.31 fixed point
of 3–4 passes without a NEW finding is not claimed: one pass after the NEW finding came back empty.
Independent review is pending.
