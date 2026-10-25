# Novelty and fidelity audit, revision 5 — introductory paper

Working title of the proposed paper: *Observational Incompleteness: From
Deterministic Dynamics to Quantum Observations*. This revision replaces
revision 4 for drafting purposes. It does three things:

1. restates every candidate contribution against `main` `8dc36d55`,
   which has landed #920, #921, #922 and #910 since revision 4's base
   `c91bf5dd`;
2. folds in the two accepted full-text literature studies, the
   black-hole study and the stochastic–quantum correspondence study;
3. gives each candidate one of five classes (§0.4) and states what is
   still needed.

Revisions 1–4 are unchanged and remain the record of what each found.
Local work product: nothing was committed, pushed or posted.

## 0. Scope, inputs and standing

### 0.1 Inputs

- **Repository at `main` `8dc36d55ba1e95fa11029c0700f3e2018543328d`**
  (2026-10-25 19:45 +0200, "Merge #922"). It was read with `git show`
  from a read-only blob-filtered clone,
  `scratchpad/novelty5/repo`. Nothing in the clone was changed. The only
  ref added to the clone is a local fetch of PR #919's head, `240e31e8`,
  for reading. `c91bf5dd` is an ancestor of `8dc36d55`.

  | Path | Blob at `8dc36d55` | Blob at `c91bf5dd` |
  |---|---|---|
  | `papers/Main.md` | `78adc1110e8d` | `01e296e6a1e4` |
  | `papers/GR.md` | `cb7dfbcc9971` | `90268f3b356d` |
  | `papers/Explainer.md` | `ce4b28eee244` | same |
  | `book/ch07-gravity.md` | `323726e06107` | `2876061f1164` |
  | `book/appendix-b-derivations.md` | `7765fb998e03` | `e64b3744c996` |
  | `verification/lean-manuscript-census.json` | `89a44bbc1fff` | `e50b85ffb8df` |
  | `OIBridge/Equivalence.lean` | `9513665b3888` | `08b9c358feb3` |
  | `OIBridge/EquivalenceChain.lean` | `10d3e4bb4286` | `3f06f76b7f3d` |
  | `OIBridge/HiddenMemory.lean` | `b0cb1cb4203c` | same |
  | `OIBridge/RecurrenceHorizon.lean` | `1ee2936d6d16` | same |
  | `OIBridge/RootedClassification.lean` | `ffb7546f72f0` | same |
  | `OIBridge/RootedClassificationAllTime.lean` | `13123378286a` | same |
  | `OIBridge/PhysicalC4Discharge.lean` | `832eeac3ee5f` | same |
  | `OIBridge/CausalReadback.lean` | `d7b71cf56aad` | same |
  | `OIBridge/C3Necessity.lean` | `b6be90e0404e` | same |
  | `OIBridge/FiniteEntropy.lean` | `52fbd89d5e04` | same |
  | `OIBridge/CanonicalMeasure.lean` | `183cc42a69c6` | same |
  | `ARCB/result.md` | `05e9f35b8573` | same |

  `OIBridge/` and `ARCB/` abbreviate the paths in revision 4 §0.1. The
  other modules of revision 4's table are unchanged between the two
  commits (blob ids checked).
- **PR #919** (open, head `240e31e8`; it changes only
  `papers/Explainer.md`, `.tex` and `.pdf`). Its Explainer.md diff was
  read. Its effect is recorded where it matters (§3, item (e); §5). Every
  citation of `Explainer:NNN` below is at `8dc36d55`, where #919 has not
  landed. #919's hunks are at Explainer:98–123, :419 and :1005. They
  touch neither of the F13 sites (:287, :1020) nor :358 or :1026.
- **Revision 4**, `novelty-v4/AUDIT.md`, sha256
  `347643467a62885cf4f7921bffb7b2fbc877cacd84edd363698ede19a829f616`
  (re-checked). Cited as `v4 §N`, `v4 Tn`, `v4 Fn`, `v4 Rn`.
- **Black-hole literature study**, `lit-blackhole/LITERATURE-v2.md`,
  sha256 `c7475d092c2d186f68adad5869ad01dd3bc01b65669a6f890e76db9491eace0d`.
  Its review (`revlitbh/REVIEW.md`) is ACCEPT WITH NITS on revision 1,
  and its addendum is ACCEPT at exactly this sha256. Cited as `BH §N`.
- **Correspondence literature study**, `lit-correspondence/LITERATURE-v2.md`,
  sha256 `005cfe94ef077b93411534d0cc50956682ceee56b42ca039e099ed4172c51c26`.
  Its review (`revlitcorr/REVIEW.md`) is ACCEPT WITH NITS on revision 1,
  and its addendum is ACCEPT at exactly this sha256. Cited as `LC §N`.
  Source keys (B23, B25, B26, BD, EG, …) follow its §1 table.

Citation forms:
- `Main:NNN`, `GR:NNN`, `ch07:NNN`, `Explainer:NNN` and `File:NNN` are
  lines at `8dc36d55` unless marked `@c91`.
- Main.md's line numbering is unchanged between the two commits. #922
  replaced the lines at 98–99, 500 and 532 one for one.
- Equivalence.lean is shifted by +3 after line 348: `S_imp_D` is now at
  :422 and `finite_horizon_equivalence` at :462.
- EquivalenceChain.lean is shifted by +1 after line 15:
  `isPermMatrix_of_stochastic_inverse` is now at :110, and `dilation_*`
  at :289–336.

### 0.2 What "read" means in this revision

There are three levels of contact with a source. They are kept apart
throughout.

- **FT (full text).** The source was read in full by one of the two
  accepted literature studies, and its statements were re-verified by
  that study's independent reviewer (LC §0.2–§0.3, `revlitcorr` §A;
  BH §0, `revlitbh` §1). FT citations give the equation or page from
  those studies.
  - **This audit did not re-read those sources.** It relies on the two
    accepted studies.
  - It spot-checked the presence of six quotes in the reviewer's
    `pdftotext` extractions (`revlitcorr/txt/`): EG Prop. 9(a), Prop. 12
    and Prop. 13 with its sketch; BD Prop. 1's "only if it is
    information decreasing"; B23 v2's "N ≤ Ñ ≤ N³"; and BB's "a
    stochastic matrix with a stochastic inverse must be a permutation".
    All six are present.
  - That is a presence check, not a reading.
- **REC (record or abstract only).** Only a bibliographic record, an
  abstract or a secondary report was read. Any conclusion that rests on
  it is **PROVISIONAL**.
- **NR (not read).** The source was not obtained, not attempted, or is
  recalled from memory. Any conclusion that rests on it is
  **PROVISIONAL**.

No external source was read in this session beyond the six presence
checks above. Web search was not used.

### 0.3 What "kernel" means

As in v4 §0.5:
- the declaration exists with the quoted statement;
- its proof text has no `sorry`, `admit` or `native_decide`;
- no `axiom` declaration appears in the module.

No Lean build was run, and no axiom report was observed. The scan was
re-run on the two modules that changed since `c91bf5dd`
(Equivalence.lean and EquivalenceChain.lean). The only textual hit is
the word `sorryAx` in a docstring (`EquivalenceChain:388`).

### 0.4 Classes

- **NOVEL-CANDIDATE.** No prior art was found in what was read. This is
  always provisional, and it is never a priority claim.
- **KNOWN.** Prior art was found, with an exact citation.
- **PARTLY KNOWN.** Some components or a weaker or stronger form are in
  the literature with exact citations, and the remainder was not located.
- **REFRAMING.** A restatement of known results, or a direct application
  of a standard tool, in OI language.
- **WITHDRAWN.** The claim lost its support in the manuscript
  corrections, and the manuscript no longer makes it.

A class is reported with its **evidence basis**: FT, REC or NR (§0.2).
Unless it says otherwise, a KNOWN or PARTLY KNOWN class rests on FT
sources. Any class whose decisive comparator is REC or NR is marked
**PROVISIONAL**.

Every NOVEL-CANDIDATE is provisional by definition. "No counterpart
found" reports the searches of LC §6. It is not a claim that no
counterpart exists.

***

## 1. What changed on `main` since revision 4, and what it does to the audit

| PR | Change | Bearing |
|---|---|---|
| #922 | Main §1.5 core now $S \iff D$ (Main:98–99); `S_imp_D` scope stated at Main:500, :532; Equivalence:346–351 comment; EquivalenceChain:14–20 header; census note | C4 restated; v4 F1, F2, F2b, F11 (header) resolved; F6 narrowed |
| #920 | ch07 §7.6 and GR App. A: Page time conditional on β = 1; island correspondence conjectural; GSL open; Page 2013/2005 and Penington cited | C16 split; v4 F9 resolved, with mirrors |
| #921 | Book B.7 D-gauge classification from GR §3.3; GR §3.3 aligned | none (not an intro-paper candidate; §6) |
| #910 | research record (second-front source audit) | none (no manuscript change) |
| #919 (open) | Explainer: invariance alone does not select the measure | (e): the measure is a third input; consistent with v4 R15 |

**#922 in detail** (Main:97–99):

- The display now reads {finite-horizon visible laws} = {visible marginals
  of finite reversible hidden-state systems}, "that is $S \iff D$,
  Markov laws included, so the existence of a realization does not
  distinguish non-Markovian laws".
- Directional kernel pointers: `S_imp_D` for ⊆; `D_imp_Qfb` with
  `Qfb_imp_S` for ⊇; assembled in `finite_horizon_equivalence`.
- A faithful realization is class (D): an initial law on
  $\mathcal{C}_V \times \mathcal{C}_H$ "which may correlate the hidden
  and visible coordinates".
- "Non-Markovianity is instead recorded in every realization (§3.4,
  unavoidable hidden predictive memory)."
- §1.5 then states the universal biconditional: a memory witness at $t$
  ⟺ every faithful realization carries readout-relevant hidden memory at
  $t$. Each direction is assigned, and the following are stated as
  unformalized:
  - reading a realization's time-$t$ law as `HiddenMemory`'s joint law
    of history, present and hidden state;
  - the vanishing criterion for conditional mutual information.
- "The equivalence $S \iff D$ and this universal statement are the
  paper's core."

**What #922 does not change.**

- Main §3.4 is still headed "The Characterization Theorem: Necessity of
  the Conditions" (Main:409). Its theorem (Main:516–522) is still
  (ii) non-Markovianity ⟺ (iii) a per-horizon realization with
  (C1), (C3) and (C4).
- Main:608 still says "Both directions of the equivalence are theorems
  of this paper".
- The same characterization appears at Explainer:358 and :1026, and at
  book `appendix-b-derivations.md:22`, :406 and their FULL.md mirrors
  (FULL:5809, :6193).
- This is the (ii) ⟺ (iii) form, with (C4) on the right. It is not the
  bare form that Main:597–598 displays as false. So there is no
  contradiction, but C12 below still applies to it.

***

## 2. The foundational statement, restated

For the introductory paper, the foundational result is:

> **Representation equivalence** (`finite_horizon_equivalence`,
> `Equivalence:462`). For a finite visible alphabet $V$ and finite
> horizon $K$, the following three classes of laws coincide, and each is
> the set of all probability laws on $V^{K+1}$:
> - finite stochastic laws (S);
> - visible marginals of a permutation of $V \times H$, for some finite
>   $H$, under an initial law on $V \times H$ that need not factor (D);
> - fixed-basis Born records of a finite unitary, with projective
>   measurement of the whole basis at every step ($Q_{\mathrm{fb}}$).

It is a **representation-equivalence theorem**. It is **not a
characterization of non-Markovianity**:
- Markov laws are in all three classes;
- the existence of a realization discriminates nothing (Main:99, :534,
  :592).

The discriminating content is separate, and it is universal over
realizations rather than existential:

- **C10 / C10-B.** Every faithful realization carries the visible memory
  in its hidden posterior (Main:99, :582–592). This is a data-processing
  statement (§3).
- **C8 / C8-D.** For one fixed finite reversible representative with a
  hidden prior shared by all visible roots, the rooted maps are either
  permutations at every time or indivisible within every visible period
  (v4 §4, unchanged).
  - The step from history-level (C4) to a non-permutation rooted map is
    still prose (Main:20, :139; v4 R4).

The near-definitional "characterization theorem" (ii) ⟺ (iii) of Main §3.4
is classified separately (C12) and should not be presented as the
foundation.

***

## 3. Per-candidate classification

Each entry gives:
- **Claim (restated)**, against `8dc36d55`;
- **Internal status**: kernel, prose or probe;
- **Literature**: each comparator, tagged FT, REC or NR, with its
  location;
- **Class**;
- **Needed**: what remains before the item can be stated in the paper.

### C1 — S ⇒ D (`S_imp_D`, `Equivalence:422`)

- **Claim.** Every finite-horizon law is the visible-trajectory
  pushforward of a single permutation of $V \times \mathrm{Hid}$ under
  some initial law.
  - The carrier is a clock plus the complete trajectory record,
    `Fin (K+1) × Traj V K`.
  - The initial law may correlate the hidden and visible coordinates
    (`Equivalence:150–156`, and the corrected comment at :346–351).
- **Internal.** Kernel.
- **Literature.**
  - EG Prop. 13 (p. 31) **[FT]** is the same trajectory-labelling
    construction ("A large enough ancilla can label a complete system
    trajectory"). It realizes a family $\vec p_0 \mapsto \mu$ by a
    time-indexed readout $A : T \times C \times \Lambda \to C$, in which
    the ancilla does not evolve.
  - OI strengthens this to one iterated bijection for a single law
    (LC §5.3). The strengthening is elementary.
  - DO3 §4.1 (p. 19) **[FT]** is different: an endpoint realizer on the
    same configuration space.
  - Path-space shift realization, Bennett 1973 and HMM realization
    theory: **[NR]**.
- **Class: PARTLY KNOWN.** The construction is EG Prop. 13's. The
  single-iterated-bijection form was not located as stated. It is an
  elementary strengthening, not a new idea.
- **Needed.**
  - Cite EG Prop. 13.
  - Read Bennett 1973 and HMM realization theory before saying anything
    about who first used a history tape for reversibility (§5, item P2.4).

### C1′ — S ⇒ D with a hidden prior independent of the visible initial state (Main:496–500)

- **Claim.** The same, with $\mu_H$ independent of $x_0$ (uniform tape
  for rational laws; product prior over response tables for real laws,
  Main:498).
- **Internal.** Prose and probes only. Main:500 now says so in place
  ("the independence of $\mu_H$ from the visible initial state rests on
  the construction above and the cited probes and is not formalized"),
  and so does the census note. v4 F2 and F2b are resolved.
- **Literature.**
  - EG Prop. 16 (p. 34) **[FT]**: the same statement, with an
    independent fixed ancilla law, but without reversibility or
    homogeneity. It is more general on the input side: arbitrary real
    λ₀, every $\vec p_0$, and no rationality condition.
  - LPW Prop. 1.5 (book p. 6) **[FT]**: the Markov, one-step case of the
    quantile-tape idea.
  - Fine 1982 (response functions), Kallenberg (transfer / noise
    outsourcing): **[NR]**.
- **Class: PARTLY KNOWN.** Known up to the reversibility packaging. The
  packaging is ledger plus clock, and it is elementary.
- **Needed.** Cite EG Prop. 16 and LPW Prop. 1.5. Fine 1982 must be read
  before Main's bibliography entry [25] is described.

### C2 — D ⇒ $Q_{\mathrm{fb}}$ (`D_imp_Qfb`, `Equivalence:294`)

- **Claim.** $U = $ the permutation matrix of $\mathrm{step}^{-1}$ on
  $V \times \mathrm{Hid}$. Born weights are indicators, so collapse at
  every step costs nothing.
- **Internal.** Kernel.
- **Literature.**
  - B25 v3 p. 12 **[FT]**: "a discrete, deterministic system whose
    dynamics is defined by a permutation matrix Σ is a special case of a
    unistochastic process".
  - B23 v2 §4.3 (pp. 19–20) and B26 §4 (pp. 10–12) **[FT]**.
  - BI Thm 2.1 (p. 5) **[FT]**: Born kernels compose exactly for
    unitary monomials, which is why the every-step collapse is harmless.
  - Koopman 1931 and 't Hooft: **[NR]**.
- **Class: KNOWN.** It is a special case, applied on the joint space and
  then lumped.
- **Sub-item, "the Born form is internal" (Main:514).** **KNOWN** and
  non-discriminating. B26 Thm 3.1 (p. 5) **[FT]** gives every
  stochastic matrix the trace form $\mathrm{tr}(E_i P_j)$, by a
  one-line diagonal choice. The paper must not present the internal
  Born form as a derivation (LC §2.4).
- **Needed.** Read 't Hooft and Koopman 1931 only if the paper attributes
  the permutation unitary historically. The FT citations suffice for the
  mathematics.

### C3 — $Q_{\mathrm{fb}}$ ⇒ S (`Qfb_imp_S`, `Equivalence:245`)

- **Claim.** The record of a finite quantum experiment, with collapse in
  a fixed basis, is a probability law.
- **Internal.** Kernel (normalization by `sum_chain`).
- **Literature.** Milz et al., PRX 10, 041049 (2020) and Strasberg–García
  Díaz, PRA 100, 022120 (2019): **[NR]** (LC §8, T4; LC §10).
- **Class: REFRAMING.** Born-rule normalization in OI class language.
  No comparator was read, so the attribution is **PROVISIONAL**. No
  novelty is claimed in any case.
- **Needed.** Milz et al. and Strasberg–García Díaz bear more on C4's
  multi-time packaging than on C3 (§5, item P2.1).

### C4 — the three-way equivalence (`finite_horizon_equivalence`, `Equivalence:462`)

- **Claim (restated, §2).** A representation-equivalence theorem: all
  three classes equal all laws on $V^{K+1}$.
  - Each of the six directions has a kernel witness (the compositions at
    `Equivalence:466–468`), so §A.34 is met for these definitions.
  - Main:98–99 now states it this way, with directional pointers.
- **Internal.** Kernel.
- **Literature.**
  - The components are in EG (C1, C1′), in B25, B23 and B26 (C2), and in
    the Born rule (C3).
  - B23 Thm (69) (p. 18) **[FT]** is a **different object**. It concerns
    one-time transition maps Γ(t ← 0), and its dilated process has
    T̃₀ = {0} (§5.8). It is not a multi-time trajectory law with a record
    at every step (LC §2.4).
  - Calvo, arXiv:2601.18720 v1 and v2 **[FT]** (LC §3). He re-exposits
    the correspondence and claims to derive the six textbook axioms from
    one stochastic axiom (Thm 1, p. 4). He gives no finite-dimensional
    result beyond B23. His countable case is one sentence (§3, p. 6),
    and he argues that continuous bases fail.
    - The journal article (*Quantum Stud. Math. Found.* 14, 2 (2026),
      doi:10.1007/s40509-026-00415-9) is the published version on its
      Crossref record **[REC]**: same abstract as v2, same 37
      references.
    - Its body was **not read**.
  - Milz et al. 2020 and Strasberg–García Díaz 2019: **[NR]**. These are
    the most likely places for a multi-time "quantum records are
    classical processes" statement.
- **Class: PARTLY KNOWN.**
  - Every direction is known, or an elementary strengthening of a known
    construction.
  - The multi-time, fixed-basis-collapse three-way identification was
    not located as a packaged statement (LC §8, T5 (c)).
  - "Not located" rests on FT for Barandes, Calvo, EG and Doukas, and on
    NR for Milz and Strasberg. **The packaging-novelty part is
    PROVISIONAL.**
- **Withdrawn sub-claim, C4-old.** "Finite-horizon non-Markovianity ⟺ ∃
  finite reversible hidden-state realization" as the paper's core
  (Main:97–99 @c91, v4 F1).
  - **WITHDRAWN**: removed by #922, and Main:597–598 shows it false.
  - It must not appear in the introductory paper, in either the display
  or the prose.
- **Needed.**
  - Read Milz et al. 2020 and Strasberg–García Díaz 2019 (§5, item P2.1).
  - The paper's novelty statement should claim only a self-contained,
    machine-checked packaging of elementary facts (§7).

### C5 — one-step uniform-prior marginal (Main:270–272)

- **Claim.** A one-step doubly stochastic matrix is a uniform-prior
  marginal of a bijection: exactly when its entries are rational, and
  approximately otherwise.
- **Internal.** Probes only; there is no OIBridge declaration.
  - Main:62 still attributes the forward direction (marginal ⇒ doubly
    stochastic) to Birkhoff–von Neumann (v4 F10, unchanged). Main:272
    uses Birkhoff–von Neumann correctly, for the converse.
  - GO's own proof confirms that this direction is marginalization
    **[FT]**.
- **Literature.**
  - GO Lemma 6 (p. 6) with its proof (App. A, p. 43) **[FT]**: noisy
    classical operations, defined as the closure, are exactly the doubly
    stochastic matrices in equal dimension. This is the closure
    statement.
  - GO footnote 8 (p. 6) **[FT]**: maps of the exact form send rational
    vectors to rational vectors. That gives the necessity half of the
    exact clause.
  - The sufficiency half needs a Birkhoff decomposition with rational
    weights. It is not stated in GO, and it was not located elsewhere.
  - HHO Prop. 1 (p. 3) **[FT]**: the state-conversion version.
  - SCH Thm 1 (p. 5) **[FT]**: adjacent (uniform coarse graining of a
    bistochastic matrix).
- **Class: PARTLY KNOWN.** The closure statement is KNOWN. The exact
  rational clause is an elementary addition that was not located as
  stated.
- **Needed.** Cite GO Lemma 6 and footnote 8. Fix F10.

### C6 — one-step dilation (`dilation_isometry`, `dilation_marginal`, `dilation_extends`, `EquivalenceChain:293–336`)

- **Claim.** For an $n \times n$ row-stochastic $T$,
  $W|i\rangle = \sum_j \sqrt{T_{ij}}\,|j\rangle \otimes |i\rangle$ is an
  isometry with ancilla-marginal $T$, and it extends to a unitary on
  $n^2$ dimensions.
- **Internal.** Kernel. `dilation_extends` asserts an injective column
  embedding, which is equivalent to a fixed ancilla state after
  reordering (LC §2.4).
- **Literature.**
  - B26 Thm 3.3 (p. 7) and Eq. (50) (p. 9) **[FT]**: **identical
    construction**, in the column convention.
  - SCH Thm 2 / Def. 2 (pp. 9–10) **[FT]**: the same $N^2$ unistochastic
    dilation.
  - OI is strictly less general: square $T$ and real $\Theta = \sqrt{T}$
    only.
  - B26 v1 (5 Aug 2026) predates the lemma's first appearance in the
    repository (branch commit `9c1c157f`, 2026-08-13). SCH (2021) is
    earlier still. Both are **prior**.
- **Class: KNOWN.**
- **Needed.** Cite B26 and SCH. B26's footnote-1 claim of an error in
  SCH's proof was not adjudicated (LC §10). Cite SCH for the statement
  only.

### C7 — stochastic-inverse lemma (`isPermMatrix_of_stochastic_inverse`, `EquivalenceChain:110`)

- **Claim.** If $A$ and $B$ are row-stochastic and $AB = 1$ or $BA = 1$,
  then $A$ is a permutation matrix.
- **Internal.** Kernel.
  - The header (`EquivalenceChain:14–20`) now says correctly that the
    manuscript's argument rests on this lemma, and that
    `RecurrenceHorizon` reaches the no-go by TV contraction instead.
    v4 F11's header item is resolved.
- **Literature.**
  - BB Problem 23, answer on PDF p. 167 **[FT]**: "a stochastic matrix
    with a stochastic inverse must be a permutation".
  - B23 v2 footnote 5 (p. 11) **[FT]**.
  - B25 v3 §3.5 (p. 13) **[FT]**.
  - PI p. 13 **[FT]**.
  - Ding–Rhee 2014: Crossref abstract **[REC]**.
- **Class: KNOWN.**
- **Needed.** Cite BB, or B23 footnote 5. Ding–Rhee's full text is
  optional.

### C8 — identity return plus overlap ⇒ P-indivisible (`pIndivisible_of_rooted_identity_return_of_overlap`, `RecurrenceHorizon:148`)

- **Claim.** For a rooted realization with $s < n$,
  $\Gamma_n = 1$, and rows $a \neq b$ overlapping at a column at time
  $s$, the rooted family is P-indivisible within $n$.
  - The argument is TV contraction, applied once.
  - From a routed-readback witness the same conclusion is kernel
    (`routed_forces_indivisible_somewhere`, `PhysicalC4Discharge:122`;
    storage-time analogue `PhysicalC4StorageReadback:256`).
  - From Main:80's history-level (C4) it is prose (Main:20, :139; v4 R4,
    unchanged).
- **Internal.** Kernel, at the matrix and routed levels. Kernel-only:
  census `manuscript: []`, and still uncited in Main.
- **Literature.**
  - BD Prop. 1 (p. 5) **[FT]**, its data-processing direction ("only
    if"; Lemma 2's "if" part, called "trivial"). For the ensemble
    $\{\tfrac12\delta_a, \tfrac12\delta_b\}$ the guessing probability is
    $(1+\mathrm{TV})/2$. It is below 1 at $s$ by the overlap and equal
    to 1 at $n$ by identity return, so the mapping is not divisible.
    BD is 2016 and **prior**.
  - DO3 Prop. 1 (p. 20) **[FT]**: the same one-line argument, stated for
    Markov compatibility.
    - It was posted 19 Oct 2026, after `RecurrenceHorizon.lean` (commit
      `70b39d57`, 2026-09-08).
    - It is **concurrent, not prior**. It is still to be cited.
  - Breuer–Laine–Piilo 2009 and Rivas–Huelga–Plenio: **[NR]**. They are
    not needed for the class, because BD suffices.
- **Class: KNOWN.** It is a special case of BD Prop. 1's data-processing
  direction.
- **Needed.**
  - Cite BD Prop. 1 as prior and DO3 v3 Prop. 1 as concurrent.
  - In Main, cite [22] by version (LC §9 item 3).

### C8-R — rooted classification (`finiteRootedRealizable_iff_pper`, `RootedClassificationAllTime:192`) — **novelty unverified**

- **Claim.** For finite $V$, a family $(\Gamma_t)_{t \in \mathbb{N}}$ is
  the family of rooted visible maps of one finite permutation, with one
  hidden prior shared by every visible root, iff $\Gamma_0 = 1$, every
  $\Gamma_t$ is row-stochastic, and the family has a positive period
  (`PPer`).
- **Scope** (v4 R5, unchanged):
  - the result is finite-visible only;
  - sufficiency uses zero-prior padding states;
  - with a full-support prior the realizable class is strictly smaller.
    This is a prose theorem with a probe witness (`ARCB/result.md:113–127`),
    not a kernel declaration.
- **Internal.** Kernel.
  - Necessity: `RootedClassification:339`, the finite order of a
    permutation.
  - Sufficiency: `RootedClassificationAllTime:162`, a product prior over
    response tables carried on embedded cycles.
  - Kernel-only: census `manuscript: []`. A grep of `papers/*.md` and
    `book/*.md` at `8dc36d55` finds no statement of it (no
    `finiteRootedRealizable`, `rootedMap`, `RootedClassification` or
    "rooted classification" hit).
  - So if it enters the introductory paper, it enters as **new
    manuscript content**, not as a restatement of Main.
- **Literature.**
  - EG Props. 16–18 (pp. 34–35) **[FT]**: every rooted linear dynamics
    over a *finite* horizon is realizable by *time-indexed*
    deterministic system–ancilla maps. This is **different**, because
    time-indexed maps impose no periodicity.
  - EG Props. 11–12 (p. 29) **[FT]**: no ancilla.
  - DO3 §4.1 (p. 19) **[FT]**: the endpoint realizer on the same space.
  - LC §6's arXiv, INSPIRE and Crossref searches, and the reviewer's
    API and forward-citation scan (LC §6.3), found no counterpart.
  - **Not searched** (LC §6.3, §10):
    - HMM / stochastic realization theory (Heller, Anderson, Vidyasagar,
      Picci);
    - ergodic-theory and automata literature on factors and codings of
      finite permutations;
    - probabilistic-automata realization by deterministic machines with
      random state (Rabin 1963; Paz 1971) [NR, from memory as a search
      direction only];
    - forward citations of BD.
- **Class: NOVEL-CANDIDATE — novelty unverified** (owner's standing
  direction).
- **Skeptical reading (§A.31).** The favorable reading is that this is a
  new characterization. Pressure-tested:
  1. Necessity is the finite order of a permutation, which is folklore.
  2. Sufficiency is an elementary embedding of a random-mapping
     representation, one response table per residue mod the period,
     into the cycles of one permutation.
  3. The search that found nothing was keyword-based, and it skipped
     the three areas where an equivalent statement would most likely
     appear: realization theory, automata and symbolic dynamics.
  - The likelier risk is a textbook remark or a lemma in realization
    theory, not a paper (LC §6.3).
  - The only safe wording is "we have not located a statement of …",
    and only after items P1.1–P1.3 of §5 are read.
- **Needed.** §5 items P1.1–P1.3, before any sentence that presents it
  as new. Optionally, kernelize the full-support separation (v4 K1).

### C8-D — the rooted recurrence dichotomy (v4 §4)

- **Claim.** For one finite reversible system with a shared hidden
  prior, either every $\Gamma_t$ is a permutation, and then the family
  is P-divisible at every horizon, or the family is P-indivisible within
  every visible period.
  - It is assembled from kernel theorems and the prose steps B3, B4 and
    A1. The display of v4 §4.4 is not kernel-certified as an
    equivalence.
  - Unchanged by #920–#922.
- **Literature.**
  - (A) is a special case of EG Props. 11–12 (p. 29) **[FT]**: for a
    deterministic $D$ with every $D_t$ bijective, $P_D$ is decomposable,
    hence divisible.
  - (B)'s mechanism is BD Prop. 1 **[FT]**, prior. DO3 v3 Prop. 1 is
    concurrent.
  - Stochastic-inverse rigidity is C7's sources **[FT]**.
  - Analogues: BCN Ex. 2 (p. 7) **[FT]**, the qubit-unitary analogue;
    BI Thm 2.1 and Eq. (5) **[FT]**, unitary semigroups; PI Fig. 4
    (p. 6) **[FT]**, two configurations and continuous paths.
  - Not located: the support lemma B4 as a stated result, and the
    combined statement.
- **Class: PARTLY KNOWN.** Every ingredient is published (FT). The
  combination was not located, and it is elementary.
  - It is not NOVEL-CANDIDATE: the class reflects that its content is
    the conjunction of three FT-located facts and finite recurrence.
  - The combined-statement search inherits C8-R's uncovered areas.
    **PROVISIONAL** for the "not located" part.
- **Needed.**
  - v4 §4.6's hedged wording, now citing BD Prop. 1 (with DO3 v3 as
    concurrent) for (B) and EG Prop. 12 for (A).
  - v4 K2 (B3, B4, A1 in the kernel) if the display is to be cited as
    an equivalence.

### C9 — readback ⇒ CMI ≥ p₀δ²/ln 2 (Main:167–170)

- **Claim.** A next-step TV gap δ between two histories, each of
  probability at least $p_0$, gives
  $I(X_{<k}; X_{k+1} \mid X_k) \ge p_0\delta^2/\ln 2$.
- **Internal.** Probes only. The "(C1)–(C3)" hypothesis is unused
  (v4 F12, unchanged at Main:167).
- **Literature.** Pinsker's inequality **[NR]**: no textbook was read in
  either study (LC §10).
- **Class: REFRAMING** (a direct Pinsker application). The attribution
  is **PROVISIONAL**, but trivially so.
- **Needed.** A textbook citation (Cover–Thomas). Fix F12.

### C10 — unavoidable hidden predictive memory (`unavoidable_hidden_predictive_memory`, `HiddenMemory:185`; Main:99, :582–590)

- **Claim (restated).** "Non-Markovianity is recorded in every
  realization" (Main:99). In every faithful deterministic realization:
  - (a) the next-step law is the pushforward of the hidden posterior;
  - (b) the next-step TV gap is at most the posterior TV gap;
  - (c) $M_t \le I(X_{<t}; H_t \mid X_t) \le \log_2|H|$.
- **Internal.** Kernel, with v4 R6's scope.
  - The kernel's law `w` on `Hist × V × H` is arbitrary, and bijectivity
    is unused (`HiddenMemory:54–63`).
  - Main:99 now states that reading a realization's time-$t$ law as that
    joint law is not formalized.
- **Literature.**
  - The conditional data-processing inequality and $I \le \log|H|$
    **[NR]** (textbook).
  - SC Thm 5 (p. 16, $E \le C_\mu$) **[FT]**: **same type, different
    statement**. It is asymptotic, stationary and about minimal
    prescient states. OI's is finite-horizon, conditional on the
    present, and about any deterministic realization.
- **Class: REFRAMING.** It is the DPI applied to $Y = f(X, H)$.
- **Needed.** Cite the DPI (Cover–Thomas). Optionally contrast with SC
  Thm 5. The paper may present it as the precise sense in which
  realizations must carry memory, but not as a new inequality.

### C10-B — the universal biconditional (Main:99; Main:580(2), :592)

- **Claim (restated).** A memory witness at $t$ ⟺ every faithful
  realization carries readout-relevant hidden memory at $t$.
  - Main:99 now names the directions:
    - forward, the pushforward identity in each realization;
    - converse, the same identity in one realization, which exists by
      `S_imp_D`.
  - It also flags two unformalized links:
    - the time-$t$ joint-law reading;
    - the CMI vanishing criterion.
- **Internal.** Directional witnesses are now stated (§A.34). Neither
  direction is a single kernel declaration.
  - Main:580(2) still says "proved, every faithful completion" without
    the two caveats.
  - v4 F6 is **narrowed, not closed** (§4).
- **Literature.** None needed. The statement is clause (a) read in both
  directions.
- **Class: REFRAMING.**
- **Needed.** In the paper, carry Main:99's directional form and its
  caveats, not Main:580(2)'s "proved".

### C11 — C3 necessity (`c3_necessity`, `card_hidden_ge_two_pow_Istar`, `C3Necessity:80, 117`)

- **Internal.** Kernel. It is the same DPI at the whole-future readout,
  then exponentiated.
- **Literature.** SC Thm 5 **[FT]**: same type, different statement. DPI
  text **[NR]**.
- **Class: REFRAMING.**
- **Needed.** As for C10.

### C12 — the "characterization theorem" (ii) ⟺ (iii) (Main:516–522, :608; Explainer:358, :1026; appendix-b:22, :406)

- **Claim (restated).** (ii) non-Markovian at an accessible order ⟺
  (iii) a per-witness-horizon realization exists with (C1), (C3) and
  (C4).
  - (ii) ⇒ (iii) is C1′/C1 plus inheritance.
  - (iii) ⇒ (ii) is C9.
  - Main:596 says (C4) coincides with (ii) in any faithful realization,
    which `primitive_probes.py` confirms exhaustively at three small
    sizes. So the equivalence reduces to "(ii) ⟺ (ii) holds and a
    realization exists".
- **Internal.** Prose and probes. Neither direction is kernel-checked
  as stated (v4 F5).
- **Literature.** None needed.
- **Class: REFRAMING.** It is near-definitional.
  - Since #922, it is no longer the paper's core.
  - It must not be offered as a "characterization of non-Markovianity"
    in the introductory paper.
- **Needed.** The paper should either omit it, or state it with Main:596's
  reduction beside it. Main:608's "Both directions … are theorems" (F5)
  is unchanged and stays a correction target.

### C13 — canonical predictive quotient (Main:600)

- **Claim.** $q_R : (x, h) \mapsto (x, \text{visible future-tail})$ is
  the unique morphism to the tail object $T(P)$. Fibres above it need not
  be unique.
- **Internal.** Prose and probes. `fiber_freedom` was not audited.
- **Literature.**
  - SC Def. 5 (p. 9) **[FT]**: causal states partition *pasts* by the
    conditional law of the future, a **different** object. v4 R13 is
    confirmed from the full text.
  - Rutten 2000 (final coalgebras): **[NR]**, not obtained.
  - Kalman observability and Myhill–Nerode: **[NR]**.
- **Class: REFRAMING** (final-coalgebra / observability quotient).
  **PROVISIONAL**: the decisive comparator, Rutten, was not read.
- **Needed.** Rutten 2000 (§5, item P3.1). The ε-machine distinction may
  be stated now (FT).

### C14 — no fixed finite carrier for a qubit (Main:538, :580(3))

- **Internal.** Elementary factorization $B = \Xi M$, plus the imported
  unbounded nonnegative rank [55].
- **Literature.**
  - Hardy 2004 (SHPMP 35, 267): **[NR]**, not obtained.
  - MO p. 2 **[FT]** reports **[secondary]** that Hardy proved "the
    number of ontic states can not be finite".
  - MO Theorem (p. 8) **[FT]**.
  - GH (abstract; pp. 4–5, $L \ge 2N - 1$) **[FT]**: an explicit qubit
    task needing unbounded classical memory.
  - Heinosaari et al. [55]: **[NR]**.
- **Class: REFRAMING** of the Hardy-type no-go. **PROVISIONAL**: Hardy
  2004 and [55] were not read.
- **Needed.** Hardy 2004 and [55] (§5, item P3.2). Cite GH and MO now.

### C15 — finite reversible ε-realization of quantum experiments ("ε-gluing", Main:544–578, :580(4))

- **Internal.** Prose and probes. It was not audited against a kernel
  (v4 F7: "proved unconditionally" has no traced kernel anchor).
- **Literature.** Neither study examined it (LC §10). No comparator was
  read.
- **Class: not classified.** No literature was examined, so none of the
  five classes can be assigned on evidence.
  - It is not NOVEL-CANDIDATE: that class requires that literature was
    read and found empty.
  - Any statement about it in the introductory paper is **PROVISIONAL**
    in both its internal and its literature standing.
- **Needed.**
  - An internal audit first.
  - Then a literature map. The candidates are the finite-precision
    nullification literature (Meyer 1999; Kent 1999; Clifton–Kent
    2000), ontological-model resource bounds (Harrigan–Spekkens 2010;
    Montina, MO above) and classical-simulation-cost results. All are
    **[NR]**, named from memory as search directions only.

### C16 — the black-hole application (GR App. A; ch07 §7.6)

Restated against #920. The sub-items are classed separately.

- **C16a — the Page-time formula.**
  - Claim: $t_P/t_{\mathrm{evap}} = 1 - (\beta/(1+\beta))^{3/2}$, with
    0.646 at β = 1 (GR:855–863, ch07:137–143).
  - Literature: Page 2013, Eq. (8), pdf p. 11 **[FT]**, under the same
    inputs: constant α, $S \propto M^2$, constant β, turnover at
    $\tilde S_{\mathrm{rad}} = \tilde S_{\mathrm{BH}}$.
    - 0.646 is Page's half-area time $t_{1/2}$ (pdf p. 12). Page notes
      there that the "half its initial entropy" description is correct
      only at β = 1.
    - GR now cites it as [60, Eq. (8)].
  - **Class: KNOWN.**
- **C16b — β > 1 for every greybody profile** in the quasi-stationary
  semiclassical regime (GR:863, ch07:143).
  - Literature: Page 2005, Eqs. (5)–(10), pdf pp. 10–11 **[FT]**;
    species values in Eqs. (19)–(21), p. 13 **[FT]**.
  - The manuscript's alternative lower bound $g(N)/N \ge g(n)/n$ reaches
    the same per-mode inequality by a different bound (BH §2). It is an
    exposition, not a new result.
  - **Class: KNOWN.**
- **C16c — the Page curve from cycle typicality** (GR Thms A.8–A.9;
  GR:611).
  - The curve's formula is Page 1993, Eq. (10) **[FT]**, the
    large-dimension mean $\ln m - m/(2n)$, substituted with the mode
    counts $d = q^{n}$ (GR:847, "direct substitution").
  - The cycle-averaging step (A.8) is a counting argument on top of
    Popescu–Short–Winter, and it is conditional on H-scramble, which is
    "not established" (GR:611).
  - PSW 2006, Hayden–Preskill 2007 and decoupling: **[NR]** in both
    studies.
  - **Class: PARTLY KNOWN.** The formula is known. The deterministic
    cycle-typicality route is not compared with any read source, so the
    class is **PROVISIONAL**. Internally, the result is conditional on
    H-scramble.
- **C16d — "quantitatively matches the QES prediction", "a microscopic
  realization of the entanglement-island construction" (asserted), "the
  framework proves the generalized second law".**
  - **WITHDRAWN.** #920 removed all three.
    - The QES agreement on the Page time is stated as not established
      (GR:869, ch07:147).
    - The island correspondence is "conjectured"; GR:871 and ch07:151
      keep "microscopic realization" only after "If the conjectured
      correspondence holds".
    - The GSL is "open" (GR:605, :609, :805; ch07:157; ch19:72).
  - Literature confirms the withdrawal. The only 4D island fraction
    located is HIM's 0.43 (fn 16, pdf p. 15) **[FT]**, with s-wave,
    no greybody factor and eternal formulas. Penington 2019 (pdf p. 12)
    **[FT]** gives $A_{\mathrm{hor}} > A^0_{\mathrm{hor}}/2$ at the
    Page time (BH §4).
  - Propagation was checked by a grep at `8dc36d55`, and all of the
    following carry the conditional form:
    - ch09:127, ch18:148, ch19:72, glossary:113;
    - FULL.md:1887, :2013–2036, :2605, :4966, :5246, :6733;
    - GR:611.
- **C16e — subadditivity bound** (GR Thm A.6): from a product state under
  a global unitary, the sum of the sectors' von Neumann entropies does
  not decrease.
  - **Class: REFRAMING** of subadditivity. Textbook **[NR]**.
- **C16-S — the three-way separation** for an access class (v4 §7.3):
  preserved, recoverable by 𝒜, and typical.
  - Hayden–Preskill, PSW and decoupling: **[NR]**.
  - **Class: REFRAMING, PROVISIONAL.** Pedagogical value only.
- **Needed.** If the introductory paper mentions black holes:
  - cite Page 2013 Eq. (8) and Page 2005 Eqs. (5)–(10);
  - say 0.646 is conditional on β = 1;
  - read PSW and Hayden–Preskill before describing the typicality step's
    relation to prior work (§5, item P4.1).

### (e) — the physical reading: quantum structure as the form of embedded observation

- **Claim.** An interpretation laid over a universal representation
  (Main:534, :542, :624). It is not a theorem.
  - The interface $(\varphi, \mathrm{Obs}, \mu)$ is underdetermined by
    the stated architecture (v4 R15).
  - Main:56–60 and `invariance_does_not_select` (`CanonicalMeasure:242`)
    agree that invariance alone does not select the measure. The
    counting measure is *selected* as maximal-entropy, and a realization
    carries its own hidden prior as a datum.
  - #919 brings the Explainer into line with this.
  - So the measure is a third input whenever a general prior is
    allowed, which reinforces R15.
- **Literature.**
  - Barandes B23, B25, B26 **[FT]**.
  - Calvo v1/v2 **[FT]** and the journal record **[REC]**. Calvo's claim
    to derive the textbook axioms is **stronger** than OI's equivalence
    (LC §3.4). The paper must not present OI as such a derivation, and
    must not describe Calvo as a dimension extension (F14 below).
  - Doukas **[FT]**; Pimenta **[FT]**.
  - 't Hooft and Spekkens 2007: **[NR]**.
- **Class: REFRAMING** (interpretive). No novelty class applies to an
  interpretation. Its relation to 't Hooft and Spekkens is
  **PROVISIONAL**.
- **Needed.** 't Hooft (2016) and Spekkens 2007 before the paper
  positions the reading against them (§5, item P2.3).

### Other items the literature studies touched

- **The XOR example** (Main:606: $X_1$ uniform, $X_2 = X_0 \oplus X_1$,
  non-Markov but with a P-divisible matrix family). The same process,
  with all two-time kernels $\tfrac12 J$, is DO3 App. A (pp. 36–37)
  **[FT]**. **KNOWN** as an example.
- **v4 §4.5's branch-(B) witness** ($\Gamma_1 = \tfrac12 J$) is the same
  matrix, used for a different point.

***

## 4. Fidelity notes: status at `8dc36d55`

The F-identifiers are kept. Nothing is renumbered, and no retired number
is reused (§A.30).

| ID | v4 finding | Status at `8dc36d55` |
|---|---|---|
| F1 | Main:97–99 displayed the bare false form as the core | **resolved** (#922) |
| F2 | Main:500 pointed at `S_imp_D` for the independent-prior form | **resolved** (#922: scope stated in place; census note) |
| F2b | `Equivalence:346–348` and Main:532 called the carrier "response-table" | **resolved** (#922: comment at :346–351; Main:532 "by a different carrier") |
| F3 | $Q_{\mathrm{fb}}$ wording; `e^{-iĤ}` remark contentless | unchanged (Main:16, :530, :532) |
| F4 | title (Main:2) and Main:28 beyond Main:22, :534, :542 | unchanged; Calvo FT (LC §3.4) sharpens it |
| F5 | Main:608 "Both directions … are theorems", Main:690 "necessary and sufficient" | unchanged |
| F6 | Main:580(2) "proved" for the biconditional | **narrowed**: Main:99 states the directions and two unformalized links; Main:580(2) does not carry them |
| F7 | Main:580(4) "proved unconditionally", no kernel anchor | unchanged |
| F8 | missing citations | unchanged, now with an exact list (below) |
| F9 | ch07 §7.6 overclaims and mirrors | **resolved** (#920, mirrors checked; C16d) |
| F10 | Main:62 credits Birkhoff–von Neumann with double stochasticity | unchanged; GO's proof confirms it **[FT]** |
| F11 | kernel route vs Main:20 and :139; EquivalenceChain header | header **resolved** (#922); the citation guidance for C8 stands (C8 above) |
| F12 | Main:167's (C1)–(C3) unused | unchanged |
| F13 | the `≤ n³` import | **kept separate** (§6) |

**F8, refreshed.** A grep of `papers/*.md` and `book/*.md` at `8dc36d55`
for each name found no citation of:
- Buscemi–Datta;
- Egri et al. (the "Egri" hits in ch12 and Bioinformatics.md are a
  different author);
- B26 (arXiv:2608.04354);
- Schmidt (the "Schmidt" hits are Gram–Schmidt or Hilbert–Schmidt);
- Gour et al. in Main (the only hit is in Methodology.md);
- Ding–Rhee (the "Ding" hits are other authors);
- Levin–Peres–Wilmer (the "Levin" hits are other authors);
- Shalizi–Crutchfield, Rutten, Galvão–Hardy, Montina, Biamonte, Benatti,
  Kallenberg;
- Hardy 2004.

Main names "the exact Koopman operator" (Main:728, :742) as an object
but cites no Koopman source for the permutation unitary. These
name-greps are §A.19 evidence for "Main does not cite X"; they are not
evidence that the corpus is silent on the underlying mathematics.

**New fidelity findings carried from LC §9** (verified there in full
text; their Main lines are unchanged at `8dc36d55`). None is applied
here; each is for the owner under §A.25.

- **F14.** Main:210, :212, :218 describe Calvo [13] as a dimension
  extension. He asserts the countable case is "trivial" in one sentence,
  and argues that continuous bases fail (LC §3.4).
- **F15.** Main:210's "non-trivial only in the P-indivisible regime" is
  not in PI. The nearest statement is PI p. 17, which is weaker.
  Main:212 needs PI's two-configuration scope.
- **F16.** Main:212's Doukas scope condition (iii) and its
  "finite-environment bound" cite v1/v2 §3.1 content that is absent
  from v3. [22] needs version-specific citations.
- **F17.** Main:212 swaps [11] and [12].
- **F18.** Main:220's "The Born rule is the equilibrium distribution of
  the indivisible process [11, 12]" has no source. "equilibri" occurs in
  no version of B23, B25 or B25b, except in a reference title.
- **F19.** Main [24] (Main:822) is stale. It is *Phys. Rev. A* 114,
  022208 (2026) **[REC, Crossref]**.
- **F20.** Main:636's reader-instruction phrase (§A.32) must not be
  carried into any F13 edit.

***

## 5. Literature that must be read before any novelty claim enters the paper

The list is prioritized by what each item gates. P1 items gate the only
two candidates that could carry a novelty sentence (C8-R, C8-D). Nothing
in P2–P4 can raise any class to NOVEL-CANDIDATE. Those items gate
attributions and the correct description of related work.

**P1 — gates C8-R and C8-D**

1. **HMM and stochastic realization theory.**
   - Sources: Heller 1965 (Ann. Math. Stat.); Anderson 1999 (MCSS, "The
     realization problem for hidden Markov models"); Vidyasagar's HMM
     realization work; Picci's stochastic realization.
   - Why: this is the field whose subject is which processes are
     functions of finite (deterministic or Markov) systems. A
     characterization of rooted families of *deterministic* periodic
     systems with a random initial state is most likely to sit here as a
     lemma. The searches did not cover it (LC §6.3).
2. **Automata and symbolic dynamics.**
   - Sources: realization of stochastic sequential machines by
     deterministic machines with random state (Rabin 1963; Paz 1971;
     Carlyle 1963); factors and codings of finite permutations and
     periodic processes in ergodic theory.
   - Why: C8-R's sufficiency is "a product prior over response tables on
     the cycles of one permutation". That is a deterministic-machine,
     random-state realization, a standard construction in that
     literature.
3. **Divisibility and revival literature beyond BD.**
   - Sources: forward citations of BD 2016 (not indexed by INSPIRE;
     Semantic Scholar and OpenAlex returned 429); Wißmann–Vacchini–Breuer
     (full text; abstract only so far, LC §5.11); Breuer–Laine–Piilo
     2009; Rivas–Huelga–Plenio (Rep. Prog. Phys. 2014); the Milz–Modi
     PRX Quantum 2021 review; Breuer–Petruccione on finite-environment
     revivals; Pleasance, arXiv:2607.07332 (located, not read).
   - Why: a recurrence-forced indivisibility statement for finite
     systems (C8-D) would most likely be stated there, as would a
     permutation-or-indivisible dichotomy.

**P2 — gates C4's packaging and the related-work section**

1. **Milz et al., PRX 10, 041049 (2020)** and **Strasberg–García Díaz,
   PRA 100, 022120 (2019).** These are the nearest likely statements
   that multi-time projective records of quantum systems form
   (Kolmogorov-consistent) classical processes, and when. They bear
   directly on the $Q_{\mathrm{fb}}$ ⇒ S direction and on whether the
   three-way multi-time packaging (C4) was already stated.
2. **The Calvo journal full text** (*Quantum Stud. Math. Found.* 14, 2
   (2026), CC BY). Its body identity with arXiv v2 is unverified. It is
   needed before Main [13] is re-described (F14) or its version cited.
3. **'t Hooft (2016, *The Cellular Automaton Interpretation*)** and
   **Spekkens 2007.** These are the positioning comparators for (e).
   't Hooft is also the comparator for C2's historical attribution.
4. **Bennett 1973, Fine 1982 (PRL 48, 291), Kallenberg (transfer
   lemma), Koopman 1931.** These settle the attributions of C1, C1′
   and C2 (history tape; response functions; noise outsourcing; the
   permutation operator). They cannot change those classes, because EG
   and LPW already make them PARTLY KNOWN.
5. **Barandes, *Philosophy of Physics* 3(1):8 (2025)**, the published
   version of [12]. It is needed for [12]'s exact claims, including "at
   least some choices" of j′ (relevant to §6).

**P3 — gates REFRAMING attributions**

1. **Rutten 2000** (TCS 249), plus Kalman observability, for C13.
2. **Hardy 2004** (SHPMP 35, 267) and **Heinosaari et al. [55]**, for C14.
3. **Cover–Thomas** (DPI, conditional DPI, Pinsker), for C9, C10 and C11
   citations.
4. **Ding–Rhee 2014** full text, for C7 (optional; BB and B23 suffice).

**P4 — gates the black-hole paragraph, if there is one**

1. **Popescu–Short–Winter 2006, Hayden–Preskill 2007**, and a decoupling
   reference, for C16c and C16-S.
2. Zurek 1982, Page 1976 (PRD 13, 198; PRD 14, 3260), Page 1983.
   Optional: Page 2005 and 2013 already supply every citation the
   manuscripts make.
3. Alishahiha et al., arXiv:2005.08715 (abstract only so far), for the
   statement that no 4D evaporating island Page-time fraction is
   established.

**Outside the literature check:** C15 needs an internal audit before it
needs a literature map (C15 above). Kernel items v4 K1–K4 are unchanged.

***

## 6. F13 — the `≤ n³` bound, kept separate and not resolved here

**This audit does not resolve F13.** Its author did not read B23, B25
or B26. The sources were checked for presence only (§0.2), which does
not meet the full-text bar the owner set for F13.

What the accepted correspondence study reports (LC §7), recorded here as
input to the separate F13 check:

- **The bound is in the sources.**
  - B23 v2: Eq. (94) (p. 24), footnote 13 (p. 25), §5.9 (p. 28).
  - B23 v1: Eq. (89).
  - B25 v3: §3.4 (p. 10).
  - The reviewer re-verified these (`revlitcorr` §A). This audit
    confirmed only that the string "N ≤ Ñ ≤ N³" occurs in the
    reviewer's B23 v2 extraction.
- **Its form.**
  - One dilated space for the whole family.
  - One unitary per target time, with no composition law and no
    time-independent generator.
  - Conditioning time 0 only.
  - B23's construction works for every initial ancilla configuration
    j′, while B25 claims only "some choices".
- **B26 Thm 3.3 gives N²** for a fixed j′, and so does OI's C6. Hence:
  - Main:210's contrast ("$n^2$ at a single step, within the source's
    $\le n^3$ bound for the full process family") compares objects of
    the same kind;
  - Main:504's definition ($\le n^3$ *and* $e^{-i\hat H t}$) exceeds
    both sources.
- **Sites, unchanged at `8dc36d55`:**
  - Main:204, 210, 350, 504, 506, 514, 636, 690, 716;
  - Explainer:287 (which also restricts the class to P-indivisible
    processes) and Explainer:1020. #919 does not touch either.
  - Code carrying the wording: `architecture_check.py:202, 218, 255` and
    `tdilate_probes.py:73`.

**Decision for the owner.** Either:
- accept LC §7, which a reviewer accepted at sha256 `005cfe94…1c26`, as
  F13's full-text check; or
- commission a separate reading.

Until then, the introductory paper does not repeat the bound, the
Main:210 contrast, or Main:504's definition.

***

## 7. Positioning and the surviving novelty statement

Unchanged in substance from v4 §8. Now every class in it rests on FT
sources, except those marked PROVISIONAL.

- **A technical perspective / pedagogical review, not a research
  article.** After both studies:
  - KNOWN: C2, C6, C7, C8, C16a, C16b;
  - PARTLY KNOWN: C1, C1′, C4, C5, C8-D, C16c;
  - REFRAMING: C3, C9–C14, C16e, C16-S, (e);
  - WITHDRAWN: C4-old, C16d;
  - not classified: C15;
  - NOVEL-CANDIDATE: only C8-R, novelty unverified.
- **The literature check lowered the estimate**, as v4 §8 predicted it
  could. C6 moved from "pending" to KNOWN (B26, SCH), C8 to KNOWN (BD),
  and C5 to PARTLY KNOWN (GO). Nothing moved up.

**Novelty statement that should survive scrutiny** (v4's text,
corrected):

> We give a self-contained, machine-checked (Lean 4/Mathlib) account of
> the elementary fact that, at any finite horizon, finite stochastic
> laws, visible marginals of finite reversible dynamics, and
> fixed-basis Born records of finite unitary systems (projective
> measurement in one basis at every step) are the same class of laws —
> every law on the finite trajectory space. This is a representation
> equivalence: Markov laws are included, so representability carries no
> discriminating content by itself. Its components are known (Egri et al.
> 2026 for the trajectory-labelling realization; Barandes for
> permutation dynamics as unistochastic processes). Two elementary
> consequences do discriminate. By the data-processing inequality, every
> deterministic completion carries at least the visible predictive
> information in its hidden state (machine-checked). And for one finite
> reversible system with a hidden prior shared by all visible roots, the
> rooted visible maps are either permutations at every time or
> stochastically indivisible within every visible recurrence period —
> an elementary combination of finite recurrence with the
> data-processing direction of Buscemi and Datta, assembled from
> machine-checked theorems and elementary steps that are not formalized.
> For a finite visible alphabet, and with hidden states of zero prior
> weight permitted, we also give the machine-checked characterization of
> exactly which rooted families such systems realize. We state where the
> finite correspondence stops short of operational quantum theory, and
> we offer the reading of quantum structure as the form of embedded
> observation as an interpretation, not a derivation.

- **No priority sentence** may be attached to the rooted classification
  until §5 P1.1–P1.3 are read.
- "Machine-checked" presupposes a Lean build (v4 K4). It covers only the
  kernel declarations: never B3, B4 or A1, the time-$t$ joint-law
  reading, or C1′'s prior independence.

**Related work the paper needs** (FT unless marked):
- B26; B23 and B25 (correctly labelled, F17); EG; BD; DO3 v3 Prop. 1 as
  concurrent work, with [22] by version; GO Lemma 6 and footnote 8; SCH;
  BB or B23 footnote 5; LPW Prop. 1.5; SC (the ε-machine contrast);
  GH and MO;
- Calvo, correctly described (F14);
- Pimenta, with its two-configuration scope (F15);
- pending: Hardy 2004, Rutten, Milz et al., Strasberg–García Díaz,
  't Hooft, Spekkens, and the P1 areas.

If black holes appear: Page 2013 Eq. (8), Page 2005 Eqs. (5)–(10),
Penington 2019 §2, and Page 1993 Eq. (10).
