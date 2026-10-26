# Scientific review: Introduction paper draft

- **Object:** `S/paper/draft/Introduction.md`, sha256 `03c1154bc560…4b25`. It is byte-identical to
  `pintro/repo/…/introductory-paper-20261025/draft/Introduction.md` at `8fcc6443`. Also read:
  `DRAFT-NOTES.md` and `probe/swap_memory.py`.
- **Sources:** Main tree at `687e885b` (`S/paper/mainwt`), covering `papers/Main.md`, `GR.md`, book
  ch01/ch07/ch18/ch19/FULL, the `OIBridge` kernel, and the BH-01 and BH-02 packages and their
  reviews. Also OUTLINE/CONTRIBUTION/SOURCES r4, the RECHECK files, AUDIT r4
  (`novelty-v5/AUDIT.md`) and AGENTS.md.
- **Read-only.** No repository file was changed and nothing was committed or posted. Git ran with
  `-c gc.auto=0 -c maintenance.auto=false`.
- **Own checks** (all in `S/paper/sci-review/`):
  - `probe/card_exact.py` and `probe/card_exact.out`: an exact sympy/Fraction computation, written
    independently of `swap_memory.py`;
  - `probe/crossref.py` and `dl/arxiv.xml`: bibliographic records from Crossref and the arXiv API,
    treated as data.

## Verdict: ACCEPT WITH CHANGES

The mathematics is sound and kernel citations are accurate. All 30 cited identifiers exist at the
stated `module:line` and state what the paper says. The finite-law and operational layers are
kept within the scope the kernel proves. No overclaim was found in Theorems 1–4.

The card-table correction is **right**, and I confirmed it exactly (§1 below). It needs one
supporting citation and a precise statement of the decomposition.

There are seven required changes:
1. **One false statement:** §4.3, line 213.
2. **The card-table sentence:** it needs a definition, a citation and a rewording.
3. **§5.2 is stronger than the BH-02 package**, and it rests on PSW, which nobody has read.
4. **The R11 OWNER markers are incomplete.** There are uncovered restatements in §6.5 and §8, and
   live book sites in ch18 and ch19 are missed.
5. **§6.2 drops scope**, and its equivalence has no directional witnesses (§A.34).
6. **The abstract and §1 do not attribute the known components**, against the owner's requirement
   that known results not be presented as novel.
7. **The non-claims list is incomplete** per CONTRIBUTION-r4 (c).

None of these is structural. The paper cannot land in any case until the owner resolves R11 and
the §A.42 retention.

***

## 1. Priority check: the card-table correction (draft:217)

### 1.1 What Main:702 states

Main:702 (§4.5, "Falsifiability") gives the definition of Bäcker, Beyer and Strunz [28]:
- the memory of a two-step process is classical when "the second step can be written as a quantum
  instrument realizing the first step, followed by channels conditioned on the instrument's
  classical outcome";
- the classification is a property of the maps on all density matrices.

It then states the no-decomposition result for **"a swap realization, $\varphi(x,h)=(h,x)$ with an
initialized hidden slot (§1.2), whose two-step maps are $\rho\mapsto|0\rangle\langle0|$ and
$\rho\mapsto\rho$"**. The argument given is that every Kraus operator of the first map has
one-dimensional range, so every outcome-conditioned processing is entanglement-breaking, and the
identity is not.

Main:702 says nothing about the swap with a uniform hidden card.

So r4's citation "(Main:702)" for the card game, which has a uniform burn card, cites a different
realization. The draft's diagnosis in DRAFT-NOTES item 2 is correct.

### 1.2 Exact computation (`probe/card_exact.py`, section 3 onward)

Setup:
- the swap is embedded as a permutation unitary on $\mathbb C^2\otimes\mathbb C^2$;
- the input is an arbitrary symbolic $2\times2$ matrix $\rho=\begin{pmatrix}a&b\\c&d\end{pmatrix}$,
  so the maps are checked on all of $M_2$.

Results:

| Hidden state | $\Phi_1(\rho)$ | $\Phi_2(\rho)$ |
|---|---|---|
| uniform $I/2$ (the card game) | $\tfrac{a+d}{2}I=\operatorname{tr}(\rho)\,I/2$ | $\rho$ |
| initialized $\lvert0\rangle\langle0\rvert$ (Main:702) | $(a+d)\lvert0\rangle\langle0\rvert$ | $\rho$ |

**Classical-memory decomposition, uniform case.** Take $I_o(\rho)=\tfrac14\sigma_o\rho\sigma_o$ for
$o\in\{0,x,y,z\}$ and $\Psi_o=\mathrm{Ad}_{\sigma_o}$. Exactly:
- each $I_o$ is CP, with Kraus operator $\sigma_o/2$ and a positive semidefinite Choi matrix;
- $\sum_o(\sigma_o/2)^\dagger(\sigma_o/2)=I$, so the instrument is trace-preserving in sum;
- $\sum_o I_o(\rho)-\Phi_1(\rho)=0$;
- $\sum_o\Psi_o(I_o(\rho))-\Phi_2(\rho)=0$;
- the Choi matrix of the decomposition equals the Choi matrix of $\mathrm{id}$.

This is a decomposition in exactly the sense of Main:702, so **one exists for the uniform-burn
realization.**

**No decomposition, initialized case.** Main's argument is confirmed in Choi form:
- $J(\Phi_1)=\mathrm{diag}(1,1,0,0)$ has rank 2, with range $\{|0\rangle_{\rm out}\otimes|v\rangle_{\rm in}\}$;
- so every CP $I_o\le_{\rm CP}\Phi_1$ has the form $|0\rangle\langle0|\operatorname{tr}(E_o\,\cdot)$, and
  every $\sum_o\Psi_o\circ I_o$ is measure-and-prepare;
- $J(\mathrm{id})$ has partial-transpose spectrum $\{1,1,1,-1\}$, so it is not PPT and $\mathrm{id}$ is
  not entanglement-breaking.

In the uniform case $J(\Phi_1)=\tfrac12 I_4$ has full rank, so this obstruction is absent.

**CP-indivisibility.**
- The rooted matrices are $\Gamma_1=\tfrac12J$ and $\Gamma_2=I$, which is P-indivisible.
- The card game is a member of Main:326's permutation-dilation family: Main:322 uses a general
  diagonal $\mu_H$, and the burn card is $I/2$. Main:326 therefore gives CP-indivisibility.
- Directly: $\Lambda\circ\Phi_1(\rho)=\operatorname{tr}(\rho)\Lambda(I/2)$ is a rank-1 linear map and
  $\mathrm{id}$ has rank 4, so no linear divisor exists at all, let alone a CPTP one.

**Classical card odds** (section 1 of the probe): one shuffle 1/2; two shuffles 1; chained
through the middle street 1/2. The peek gives:
- overwrite the burn card: 1/2;
- replace the hole card only: 1;
- reveal only: 1.

With anticorrelated cards, $\Gamma_1$ is the swap permutation. All of this matches draft:204–215.

### 1.3 Assessment of the draft's wording

The draft's corrected wording is **mathematically right**:
- no classical-memory decomposition for the initialized slot, with Main:702 cited;
- for the uniform burn, the one-step map equals the Pauli twirl as a channel, and the identity
  decomposes through it.

As written it is **not yet exact**, for four reasons:
- (a) The paper uses "classical-memory decomposition" without defining it, and it does not cite
  Bäcker–Beyer–Strunz, the source of the definition. The bibliography has no BBS entry.
- (b) "Record which Pauli was applied, then undo it" reads as a description of the card mechanism.
  In the swap realization no Pauli is applied, and the hidden register stores the quantum state.
  The decomposition is a property of the map pair, which is exactly how Main:702 frames the
  classification.
- (c) "Under the permutation-unitary embedding of §2.2" is imprecise: §2.2's construction
  measures diagonal states. Coherent hole-card inputs are the permutation-dilation family of
  Main §3.2 (Main:276–286, :322–328).
- (d) It is worth one clause that the family is CP-indivisible *and* classical-memory. That is
  exactly the distinction between CP-indivisibility and quantum memory that the paper is careful
  about elsewhere. This is an owner choice; see RC-2.

The design files carry the uncorrected clause and need a correction record (r5 or a note):
OUTLINE-r4 §5-h:226, CONTRIBUTION-r4 non-claim 13 (:182–185) and SOURCES-r4 §5-h:135. The
drafter flagged this. I agree, and add RECHECK-r4's RC-A row to the list. That row accepted the
clause without checking which realization Main:702 concerns. No Main or book site needs a change:
Main:702 is correct for what it states.

***

## 2. Required changes

Each change is given as exact replacement text. Line numbers refer to the draft.

### RC-1 — False statement in §4.3 (line 213) [error]

"Since $\Gamma_1\Lambda=\tfrac12J$ for every stochastic $\Lambda$" is false. $\tfrac12J\Lambda$ has
both rows equal to the average of $\Lambda$'s rows. For $\Lambda=\begin{pmatrix}1&0\\1&0\end{pmatrix}$
it gives $\begin{pmatrix}1&0\\1&0\end{pmatrix}\neq\tfrac12J$ (probe section 2). The claim holds
only for doubly stochastic $\Lambda$. The conclusion is still true.

Replace:
> Here $\Gamma_1=\tfrac12J$ and $\Gamma_2=I$. Since $\Gamma_1\Lambda=\tfrac12J$ for every stochastic $\Lambda$, the family is P-indivisible.

with:
> Here $\Gamma_1=\tfrac12J$ and $\Gamma_2=I$. The two rows of $\Gamma_1$ are equal, so for every $\Lambda$ the two rows of $\Gamma_1\Lambda$ are equal and $\Gamma_1\Lambda\neq I$: the family is P-indivisible.

### RC-2 — The card-table quantum sentence (line 217)

Replace from "Under the permutation-unitary embedding of §2.2, …" through "… then undo it." with:
> Embedded as a permutation unitary acting on an arbitrary hole-card state $\rho$, with the burn card in the uniform diagonal state [Main §3.2], the one-step channel is the constant channel $\rho\mapsto\operatorname{tr}(\rho)\,I/2$, which is entanglement-breaking [Main §3.2, Remark on the failure of (C1)], and the two-step map is the identity channel; the family is therefore CP-indivisible [Main §3.2, Theorem on CP-indivisibility]. Following Bäcker, Beyer and Strunz [BBS], a two-step process has classical memory when the second map can be written as an instrument realizing the first map, followed by channels conditioned on its outcome. With the hidden slot initialized to a fixed card instead, the swap has the maps $\rho\mapsto|0\rangle\langle0|$ and $\rho\mapsto\rho$ and admits no such decomposition [Main §4.5]. With the uniform burn card it does: the instrument $\rho\mapsto\tfrac14\sigma_o\rho\sigma_o$, $o\in\{0,x,y,z\}$, sums to the one-step map, and the channels $\rho\mapsto\sigma_o\rho\sigma_o$ conditioned on $o$ return $\rho$.

Keep the closing sentence, "A card arrangement violates no Bell inequality [Book §1.11; Main §3.3]."

Optionally (owner decision D1), append:
> CP-indivisibility of this family therefore does not by itself witness quantum memory.

Add the reference. Its bibliographic data are verified on Crossref, doi 10.1103/PhysRevLett.132.060402. Its content was not read in the audits: the definition is taken from Main:702's statement of it.
> [BBS] C. Bäcker, K. Beyer, and W. T. Strunz, "Local disclosure of quantum memory in non-Markovian dynamics," *Phys. Rev. Lett.* **132**, 060402 (2024).

Also correct the design record: OUTLINE-r4 §5-h, CONTRIBUTION-r4 non-claim 13, SOURCES-r4 §5-h
and RECHECK-r4 RC-A row.

### RC-3 — §5.2 is stronger than BH-02 and rests on unread PSW (line 256)

"A dynamics satisfying H-scramble would produce the Page value through Popescu–Short–Winter
typicality [PSW; Page93]" has two problems:
- **It omits BH-02 C6(c)**, which the reviewed package states beside C6(b) (REPORT "C6(c) shell
  factorization", CONDITIONAL; H-scramble finding item 4). On an energy shell the Haar-typical
  entropy differs from $S_{\rm Page}(d_B,d_R)$, in a shell-dependent direction. The package's "would
  produce it" holds only with the full product space as the shell.
- **It describes the typicality step's relation to PSW**, which no audit has read. AUDIT C16c and
  C16 "Needed" require reading PSW and Hayden–Preskill first (P4.1).

Replace those two sentences ("A dynamics satisfying … Whether the substratum supplies such a
condition is open.") with:
> A dynamics satisfying H-scramble with the full product space as its shell would produce the Page value [BH-02, C6(b)]; on an energy shell the Haar-typical value differs from $S_{\mathrm{Page}}(d_B,d_R)$, in a direction that depends on the shell [BH-02, C6(c)]. Whether the substratum supplies H-scramble, or any substitute, is open.

Then delete the [PSW] reference, which is cited nowhere else. Alternatively, keep it only after
PSW is read.

### RC-4 — R11 OWNER markers: uncovered restatements and missed live sites

**(a) Restatements without markers.** The draft notes say the paper must not land until the
owner corrects the R11 sites *or drops these paragraphs*. Dropping the three marked paragraphs
would still leave the same findings asserted here:
- **§6.5 item 5** (lines 363 and 367): "The Page curve follows only under H-scramble" and "The
  stated support for decoupling the trans-cosmological sector is reversed".
- **§8** (line 399): "Bijectivity conserves the global state but does not determine what an access
  class recovers. In the framework's Page-curve argument, the Page entropy enters through a
  scrambling hypothesis and not through bijectivity."
- **The abstract's last sentence** (line 16) depends on the access paragraph.

Add before §6.5 item 5 and before §8's second paragraph:
> `<!-- OWNER: R11. Restates §5.1 claim A, §5.1 item F and §5.2's H-scramble finding; it stands or falls with those paragraphs. -->`

**(b) Live sites missed by the markers**, checked by corpus grep at `687e885b`. The BH packages'
own manuscript audits flag them (BH01 MANUSCRIPT-AUDIT:182–198; BH02 MANUSCRIPT-AUDIT:271–278),
but neither SOURCES-r4 R11 nor the draft markers include them.

Contradicts claim A, as ch07:110:
- `ch18:146` / `FULL:4966`: "Information is never lost … because $\varphi$ is bijective" within "the
  framework's resolution of the information paradox".
- `ch18:158` / `FULL:4978`: the parenthetical "(which it does, through the nested partition)",
  which BH01 marks **contradicts** (claims A and E).

Unconditional against §5.2 and §6.5 item 5:
- `ch18:146` / `FULL:4966`: "reproducing the Page curve at the emergent level", with no H-scramble.
- `ch19:334` / `FULL:5510`: "Resolved (Page curve from typicality)". It also meets the paper's
  "No resolution of the black-hole information problem".

Conditions level, non-blocking:
- `ch18:130` / `FULL:4950`;
- R12, `ch18:148` / `FULL:4968`: "mass-independent fraction", against §5.3's "A mass-dependent
  coefficient moves the fraction".

Extend the §5.1 access marker (line 233) to:
> `<!-- OWNER: R11. Claim A below contradicts live text at ch07:110 / FULL:1987, ch18:146 / FULL:4966 and ch18:158 / FULL:4978; the falsification framing at ch07:159–161 / FULL:2036–2038 is unfalsifiable as stated; ch18:130 / FULL:4950 inherits ch07:110. The paper must not land until the owner corrects those sites or drops this paragraph and its restatements (§6.5 item 5, §8, abstract). -->`

Extend the §5.2 marker (line 255) to:
> `<!-- OWNER: R11. The following paragraph contradicts live text at ch07:126 sentence 1 / FULL:2003 and GR:869, and the unconditional Page-curve statements at ch18:146 / FULL:4966 and ch19:334 / FULL:5510. -->`

Update DRAFT-NOTES "Every OWNER marker" to match. Also record R12 (ch18:148 / FULL:4968) as a
conditions-level book correction.

### RC-5 — §6.2 "The quotient" drops scope and lacks directional witnesses (line 324)

Main:624 scopes the statement to "a lift with trivial ancilla at one time … the fixed-basis datum
whose evolution is the lift's unitary, with uniform initial law and identity readout". The draft
drops this and writes "fixed-basis data built from a lift". It also states an "exactly when"
without naming directions (§A.34).

The kernel shows the two directions separately:
- `bridge_traj` (`TrackBQfbBridge:276`): same one-step slice $G$ implies equal root-conditioned
  trajectory laws at every horizon.
- `rooted_eq_iff_slice_eq` (`:180`): equal **rooted families** iff $G=G'$, for trivial-ancilla
  admissible dilations (`pad U`, `Fin 1` ancilla). Its forward direction is `slice_eq_of_rooted_eq`;
  its backward direction is `visible_congr`.

Neither declaration states "equal trajectory laws ⇒ equal visible laws" in that form. The
trajectory-law ⇒ rooted-family step is elementary, but it is not stated.

Replace the bullet with:
> - **The quotient.** Take a lift with trivial ancilla at one time, and form the fixed-basis datum whose evolution is the lift's unitary, with uniform initial law and identity readout. If two such data have the same one-step visible matrix, their root-conditioned trajectory laws agree at every horizon (`bridge_traj`, `TrackBQfbBridge.lean:276`); conversely, if their rooted families agree, their one-step visible matrices are equal (`rooted_eq_iff_slice_eq`, forward direction, `:180`). Each such trajectory law is fixed-basis realizable and stochastic (`realData_traj_stochastic`, `:286`). The fixed-basis correspondence therefore acts on the quotient by visible equality [Main §3.4, Remark on representability].

### RC-6 — Attribute the known components up front (abstract or §1.2)

The abstract states "At any finite horizon, three classes of observable law coincide …" with no
attribution, and §1.2 item 1 does the same. Attribution appears only in §2.2.

Per AUDIT r4 (C4: PARTLY KNOWN, components known; packaging PROVISIONAL) and CONTRIBUTION-r4's
contribution paragraph, the entry document should say up front that the components are known. The
owner's requirement is that known results not be presented as novel.

After the abstract's sentence "…fixed-basis Born records of finite unitary systems.", insert:
> The components of this correspondence are known, from the trajectory-labelling realization of Egri et al. and Barandes's treatment of permutation dynamics as unistochastic processes; it is stated here as one theorem, each direction checked in Lean 4/Mathlib at a stated commit.

The final clause depends on owner decision 2 and the §A.42 retention. Until that is met, end the
sentence at "as one theorem".

### RC-7 — Complete the non-claims (§6.5) per CONTRIBUTION-r4 (c)

**Add item 7:**
> 7. **No claim that the card game of §4.3 produces quantum rather than classical statistics.** On card inputs its statistics are classical stochastic ones; under the unitary embedding its one-step channel is entanglement-breaking and its two-step family admits a classical-memory decomposition; it violates no Bell inequality.

This is CONTRIBUTION-r4 non-claim 13, corrected per §1.

**In item 2, add a bullet:**
> - Which of conditions (iii)–(v) a physical substratum supplies is open.

**In item 5, replace the last bullet with:**
> - The black-hole computations are finite toy models; their reviews are internal, not external validation.

This is CONTRIBUTION-r4 non-claim 6, last bullet. It also matches the package READMEs: "not
external validation or owner adoption".

***

## 3. Minor findings (should fix)

### M1 — §2.2, line 83: wrong lemma cited for the non-disturbance step

`isDiag_Phi` concerns the reduced channels for a product state $\rho\otimes\mu_H$. Class D allows
a correlated initial law, and `D_imp_Qfb` gets non-disturbance from the Born weights of a
permutation matrix being indicators (`Equivalence.lean:253–258` and the proof comment at `:300`). Replace:
> A permutation unitary preserves diagonal states (`isDiag_Phi`, `:253`). So projective measurement in the configuration basis at every step does not disturb the state, and the measured record reproduces the law.

with:
> Its Born weights are the indicators of the deterministic step, so projective measurement in the configuration basis at every step does not disturb the state, and the measured record reproduces the law (`D_imp_Qfb`). For a product initial state the reduced channels also preserve diagonal states (`isDiag_Phi`, `:253`).

### M2 — §1.2, line 37: imprecise and interpretive

"the would-be intermediate transition maps acquire negative entries" holds only when $\Gamma_s$ is
invertible. In the card game $\Gamma_1$ is singular and no divisor of any sign exists.

Separately, "usually associated with quantum theory" applied to stochastic laws and memory is an
interpretive framing. Replace with:
> - the failure of stochastic divisibility, in which no stochastic intermediate transition map exists (where the would-be map $\Gamma_s^{-1}\Gamma_t$ exists, it has negative entries).

Also change "three features that are usually associated with quantum theory" to "three features
that the stochastic–quantum correspondence relates to quantum theory [B23; B25]".

### M3 — §6.3, line 330: stated facts rest on unread sources

The unbounded-nonnegative-rank statement rests only on [HKLP], whose content is unread. "Hardy's
finite-ontic-state no-go" rests on [Hardy04], also unread; MO reports it secondhand. See AUDIT C14
(PROVISIONAL) and P3.2.

Either read HKLP and Hardy04 before landing, or rest the sentence on the full-text sources:
> … no fixed finite realization reproduces the full prepare-and-measure theory of a qubit exactly [Main §3.4, Proposition on the finite-substratum obstruction]; qubit tasks requiring unbounded classical memory are given by Galvão and Hardy [GH] and Montina [MO], and Montina reports Hardy's result that the number of ontic states cannot be finite [MO; Hardy04].

### M4 — §7, line 375: one-step dilation

AUDIT C6 requires both B26 and SCH. "Is B26's construction" reads as provenance, which C6's
dating does not establish. Replace with:
> … the one-step $n^2$-dimensional ancilla dilation used in [Main §3.1] coincides with B26's construction (Thm 3.3) and with Schmidt's [SCH, Thm 2].

Add the reference (arXiv record verified):
> [SCH] H.-J. Schmidt, "Dilation of stochastic matrices by coarse graining," arXiv:2106.03513v1.

### M5 — §5, line 225: scope of the checking

Item F is exact interval arithmetic and the Page-time fraction is exact algebra; neither is an
exhaustive check. "Independent internal review" can be misread as external. Replace with:
> The combinatorial results were checked exhaustively at small size, item F by exact interval arithmetic, and the Page-time fraction by exact algebra; each package passed a separate internal review, which is not external validation [BH-01; BH-02].

### M6 — §2.4, line 131: the characterization's hypotheses

Main:516 states the characterization for a time-homogeneous process on accessible timescales
$t\ll t_R$. Main:620 shows homogeneity is load-bearing only for (i), so the draft's statement is
not wrong. To stay at Main's scope, add after "[Main §3.4]": "(stated there for time-homogeneous
processes on accessible timescales)".

***

## 4. Owner decisions

- **D1.** Include RC-2's optional sentence: CP-indivisibility does not by itself witness quantum
  memory.
- **D2.** Calvo. AUDIT §7 lists "Calvo, correctly described (F14)" among related work the paper
  needs: his claim to derive the textbook axioms is stronger than OI's equivalence. OUTLINE-r4 §9
  omits it, and the draft follows the outline. For an entry document positioned as "not a
  derivation of QM", one correctly scoped sentence on Calvo would sharpen the positioning.
- **D3.** Whether the HKLP/Hardy04 reading (M3) and the PSW reading (RC-3) happen before landing,
  or the text rests only on read sources.
- **D4.** The existing markers stand: R1 (title), R11 (now extended, RC-4) and §A.42 retention.
  The retention marker is correctly placed and correctly worded.
- **D5.** The design-record correction for the card clause: r5 or a note (§1.3).

## 5. Other items checked, with no change needed

- **Kernel identifiers.** All 30 exist at the cited lines (`finiteIsometryExtensionSF_discharged` is cited without a line; it is at `IsometryExtension:116`) at `687e885b` and state what the draft
  says.
  - `finite_horizon_equivalence`: six directions, with the compositions at 466–468.
  - `RevReal`: a correlated initial law.
  - `QfbReal`: diagonal initial weights, every-step collapse, readout a function.
  - HiddenMemory (a)–(c): for a joint law, with bijectivity unused.
  - C3 bounds; `pIndivisible_of_rooted_identity_return_of_overlap`;
    `routed_forces_indivisible_somewhere`; `isPermMatrix_of_stochastic_inverse`.
  - Theorem 4: both directions, with `[Nonempty A]`. The chain is `krausSoundExt_of_validity_inert`,
    then `compositeCompleteness_unconditional` (its extension premise discharged), then
    `exactAll_of_levelOne`.
  - `five_way_minimality`: five cells on `Fin 2`, each realizing the sealed core.
  - `oi_alone_not_qm` (`diagTheory`), `gl2`/`gl3`, `invariance_does_not_select`.
- **§A.34 equivalences.** Theorem 1 and Theorem 4 have witnesses for both directions. The §2.4
  biconditional states its directions and its two unformalized links, as Main:99 does. The
  per-horizon characterization (l.131) states both prose directions. The BJA equivalence is
  external and cited. The only defect is §6.2 (RC-5).
- **Exact numbers recomputed.**
  - §4.1: $\Gamma_1$, $\Gamma_2=I$, $\Gamma_1^{-1}\Gamma_2$ entries $(2,-1;-1,2)$, $\Gamma_1^2$
    entries 5/9 and 4/9; $P=1$ and $1/3$; $a/(2-a)$.
  - §4.2: XOR $I(X_0;X_2\mid X_1)=1$ bit.
  - §5.3: 0.6464 at β = 1; 0.538 at β = 1.4847; 0.7027 and 0.8707 (BH-02 C7).
  - BH-01 counts: 40,320; 1,376; 60; 32; $1.785\times10^{57}$; $1.153\times10^{57}$.
  - The readback bound $p_0\delta^2/\ln2$ is checked against Main:170's proof.
  - Main:708's posit ledger has twelve items (i)–(xii).
- **Novelty and originality.**
  - Every attribution matches AUDIT r4: EG Props. 13 and 16; LPW Prop. 1.5; B25 p. 12, B23 §4.3,
    B26 §4 and Thm 3.1; SGD Eq. (3); RHP14 Thm 2.4 and Eq. (15); BD Prop. 1; DO Prop. 1 and App. A
    as concurrent; BB Problem 23; BLP one-way; BJA.
  - The B26 Thm 3.3 attribution is AUDIT C6 KNOWN; M4 adds SCH.
  - There is no "first", "novel" or priority sentence.
  - The packaging sentence (l.90) is within AUDIT C4's admissible form and names the unread comb
    literature.
  - C8-R is absent. Line 98 states only the folklore necessity half (finite order), from Main:618.
- **Hypothesis, mathematics and open questions.**
  - The OI hypothesis (§1.1), H-scramble, H-Bell, the mixing hypothesis behind C2 necessity, and the
    island correspondence are each labelled as hypotheses or conjecture.
  - The operational layer is stated as a characterization under named conditions, with bare OI
    ⇏ QM.
  - The relating evolution is open.
  - No hypothesis is presented as a result, apart from M2's framing sentence.
- **Explainer stale list.** None of items 1–11 is carried. The characterization uses Main:522's
  binding.
- **The other OWNER markers.**
  - The ch07:110, ch07:126 s1, ch07:159–161, GR:811 and GR:869 citations and their FULL mirrors
    are accurate at `687e885b`.
  - ch07:161's "sharp prediction once β is derived" is not contradicted: BH-02 says the fraction
    carries no OI-specific quantity *given* β.

## 6. Bibliography (the 17 VERIFY entries, plus a spot check of the others)

Records come from Crossref (`probe/crossref.py`) and the arXiv API (`dl/arxiv.xml`). "Content
unread" items stay flagged as in AUDIT r4.

| Key | Finding | Action |
|---|---|---|
| BB | arXiv: John C. Baez, Jacob Biamonte; journal-ref "World Scientific Press, Singapore, 2018" | Remove VERIFY. Optionally add "(World Scientific, 2018)". The book's exact title was not checked here |
| Bell64 | Crossref: *Physics Physique Fizika* 1, 195–200 (1964) ✓ | Remove VERIFY; optionally add doi 10.1103/PhysicsPhysiqueFizika.1.195 |
| CHSH69 | Crossref ✓ | Remove VERIFY |
| CT | Crossref 10.1002/047174882X: Cover, Thomas; Wiley; online 2005 (2nd ed., print 2006) ✓ | Bibliographic data fine. Content is unread (P3.3), so keep the content flag |
| EG | arXiv: Győző Egri, Márton Gömöri, Balázs Gyenis, Gábor Hofer-Szabó | **Fix:** "G. Egri, M. Gömöri, B. Gyenis, and G. Hofer-Szabó" |
| GH | arXiv: Ernesto F. Galvão, Lucien Hardy; PRL 90, 087902 (2003) | Remove VERIFY; add the journal reference |
| Hardy04 | Crossref: L. Hardy, "Quantum ontological excess baggage," SHPMP 35, 267–276 (2004), doi 10.1016/j.shpsb.2003.12.001 | **Fix:** add the title and page range. Content is still unread (M3) |
| Hawking76 | Crossref ✓ | Remove VERIFY |
| HKLP | arXiv v4 and Crossref ✓ (PRA 109, 032627) | Bibliographic data fine; content unread (M3) |
| Lean4 | Crossref: de Moura, Ullrich, LNCS, pp. 625–635 (2021) ✓ | Add the pages. The LNCS volume (12699) is from memory and not in the record |
| LPW | Crossref 10.1090/mbk/107 lists authors David Levin and Yuval Peres (AMS, 2017) | **Fix:** the 2nd edition is "D. A. Levin and Y. Peres, with contributions by E. L. Wilmer". Check against the edition AUDIT read for Prop. 1.5 |
| Mathlib | Crossref: CPP 2020, pp. 367–381 ✓ | Add the pages; remove VERIFY |
| Milz20 | arXiv and Crossref ✓, all seven authors | Remove VERIFY |
| MO | arXiv: Alberto Montina; PRA 77, 022104 (2008) | Remove VERIFY; add the journal reference |
| Pen19 | arXiv title "Entanglement Wedge Reconstruction and the Information Paradox" ✓; JHEP 09 (2020) 002 | Remove VERIFY; add the journal reference |
| PSW | Crossref ✓ (Nature Phys. 2, 754–758) | Delete the entry with RC-3, or keep it only once read |
| SGD | arXiv and Crossref: Philipp Strasberg, María García Díaz ✓ | Remove VERIFY |

Unmarked entries spot-checked, all consistent:
- B23: v2 updated 2026-02-05.
- B25: *Philosophy of Physics* 3(1):8, doi 10.31389/pop.186.
- B26: v1 2026-08-05.
- DO: v3 2026-10-19.
- BD, BJA, BLP, RHP10, RHP14.
- Page93 (pp. 1291–1294), Page05, Page13.

**New entries required:** [BBS] (RC-2) and [SCH] (M4).

## 7. Nits

- Abstract l.16: change "characterized only under five completion conditions" to "characterized
  exactly by five completion conditions". Change "does not distinguish any law" to "does not
  distinguish a law with memory from one without".
- Abstract l.16: "Three statuses are kept apart" is self-description close to §A.32's
  meta-commentary. Use "Three statuses are distinguished".
- l.44: "Its gravitational and lattice applications are in [GR] and the book." The lattice
  substratum is [Substratum], which is not cited. Add it, or drop "lattice".
- l.129: "(C4) coincides with $M_t>0$" is an equivalence in prose. Point to the l.113
  biconditional as its proof.
- l.204: "by exact enumeration" could read "by exact enumeration of the equally likely cases
  (checkable by hand)". No repository probe exists for the card protocol (OUTLINE-r4 §5-h).
- DRAFT-NOTES says Appendix A has 16 rows. The table has 17 (lines 420–436).
- §6.5 item 4 and §3.2 both cite "§3.2". That is fine, but §3.2's first sentence, "The result is
  global", could name the result: "The indivisibility of §3.1 is global".
