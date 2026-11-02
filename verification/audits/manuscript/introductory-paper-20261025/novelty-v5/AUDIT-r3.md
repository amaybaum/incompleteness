# Novelty and fidelity audit, revision 5 (r3) — introductory paper

Working title of the proposed paper: *Observational Incompleteness: From
Deterministic Dynamics to Quantum Observations*. This revision replaces
revision 4 for drafting purposes.

This is r3 of revision 5.
- r2 applied the independent review of r1 (`revnov5/REVIEW.md`, verdict
  BLOCK, wording only). Its findings are cited as `Rv5:N`.
- r3 applies the nits N1–N8 of the re-check of r2
  (`revnov5/RECHECK-r2.md`, ACCEPT WITH NITS). They are cited as
  `Rc2:Nn`.
- Each item was re-verified against the repository (at `origin/main`
  `ebf98d83` for r3) or against the reviewers' source extractions before
  it was applied (CHANGES.md).
- r1 and r2 are kept unchanged: `AUDIT-r1.md` (sha256 `ef9d475c…787a`)
  and `AUDIT-r2.md` (sha256 `df39e2f9…4b93`).

Revision 5 does three things:

1. restates every candidate contribution against `main` `a411bf46`. That
   commit has landed #920, #921, #922, #910 and #919 since revision 4's
   base `c91bf5dd`;
2. folds in the two accepted full-text literature studies, the
   black-hole study and the stochastic–quantum correspondence study;
3. gives each candidate one of five classes (§0.4) and states what is
   still needed.

Revisions 1–4 are unchanged and remain the record of what each found.
Local work product: nothing was committed, pushed or posted.

## 0. Scope, inputs and standing

### 0.1 Inputs

- **Repository at `main` `a411bf46`** (2026-10-25 20:27 +0200, "Merge
  #919"). It was read with `git show` from a read-only blob-filtered
  clone, `scratchpad/novelty5/repo`. No file in the clone was changed.
  The refs added are a local fetch of PR #919's head, `240e31e8`, and
  updates of `origin/main`.
  - `c91bf5dd` → `8dc36d55` → `a411bf46` is an ancestor chain.
  - `8dc36d55..a411bf46` changes only `papers/Explainer.{md,tex,pdf}`.
    The Explainer.md blob at `a411bf46` is `a6d4cb2b53cc`, identical to
    #919's head `240e31e8`, which r1 read. Its line count is unchanged
    (1064 on both sides), so every `Explainer:NNN` citation resolves at
    `a411bf46`.
  - Every other path in the table below is byte-identical between
    `8dc36d55` and `a411bf46`; blob ids were checked for Main, GR, ch07,
    appendix-b, glossary and Substratum.
  - **After `a411bf46`.** `main` has since moved to `ebf98d83` (#911 and
    #917, both research records). `a411bf46..ebf98d83` changes nothing
    under `papers/`, `book/`, `verification/lean-mathlib/` or the census.
    So every citation here also holds at `ebf98d83`.
    - #917 is the OI-BH-1 black-hole information audit. v4 §0.1 treated
      every black-hole statement attributed to #917 as open.
    - Its landed records under
      `verification/programmes/black-hole-information/` were **not
      read**, and C16-S stays unclassified pending them (§3, C16).

  | Path | Blob at `a411bf46` | Blob at `c91bf5dd` |
  |---|---|---|
  | `papers/Main.md` | `78adc1110e8d` | `01e296e6a1e4` |
  | `papers/GR.md` | `cb7dfbcc9971` | `90268f3b356d` |
  | `papers/Explainer.md` | `a6d4cb2b53cc` | `ce4b28eee244` |
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
- **PR #919**, merged at `a411bf46`. It changes only
  `papers/Explainer.md`, `.tex` and `.pdf`.
  - Its Explainer.md diff was read.
  - Its hunks are at Explainer:98–123, :419 and :1005. They touch
    neither of the F13 sites (:287, :1020) nor :358, :378 or :1026.
  - Its effect is recorded in §3, item (e).
- **Standing of the Explainer (Rc2:N7).**
  - At `ebf98d83`, Explainer:3–8 carries a dated status note: the
    Explainer is "superseded by the book", "frozen at this revision", and
    "where it and the book disagree, the book is authoritative".
  - Draft PR #926 (head `26e365d7`, not merged) replaces it with: "This
    Explainer is retained as a supplementary historical exposition. The
    maintained book and technical papers supersede it as authoritative
    statements of the theory. Where formulations differ, consult those
    sources and their cited verification records."
  - Either way, **the Explainer is superseded, and it is not a drafting
    source for the introductory paper.**
  - The Explainer sites cited below (C12, F13, F22, F26) are recorded for
    the owner. Whether they are correction targets is the owner's
    decision.
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
- **Review of r1**, `revnov5/REVIEW.md` (verdict BLOCK, wording only).
  Cited as `Rv5:N`.

Citation forms:
- `Main:NNN`, `GR:NNN`, `ch07:NNN`, `Explainer:NNN`, `glossary:NNN`,
  `Substratum:NNN`, `appendix-b:NNN` and `File:NNN` are lines at
  `a411bf46` unless marked `@c91`.
- Main.md's line numbering is unchanged between `c91bf5dd` and
  `a411bf46`. #922 replaced the lines at 98–99, 500 and 532 one for one.
- Equivalence.lean is shifted by +3 after line 348: `S_imp_D` is now at
  :422 and `finite_horizon_equivalence` at :462.
- EquivalenceChain.lean is shifted by +1 after line 15:
  `isPermMatrix_of_stochastic_inverse` is now at :110, and `dilation_*`
  at :289–336.

### 0.2 What "read" means in this revision

There are three levels of contact with a source. They are kept apart
throughout.

- **FT (full text).** The cited passage was read in the full-text
  document by one of the two accepted literature studies (Rv5:15).
  - Most FT sources were read in full. Some were read only in the cited
    parts: BI §§1–2; GO's Def. 4, Lemma 6, its proof and footnote 8;
    LPW §1.2 (LC §5.5, §5.7, §5.9).
  - Most cited passages were re-verified by the study's reviewer
    (LC §0.2–§0.3, `revlitcorr` §A; BH §0, `revlitbh` §1). SC Def. 5 and
    EG Example 3 are not in `revlitcorr` §A's list. SC Def. 5 was
    checked on p. 9 by the review of r1 (Rv5:15).
  - The review of r1 re-located more than 30 FT comparisons, page by
    page (Rv5 "What was checked").
  - FT citations give the equation or page from those studies.
  - **This audit did not re-read those sources.** It relies on the two
    accepted studies.
  - It spot-checked the presence of six quotes in the reviewer's
    `pdftotext` extractions (`revlitcorr/txt/`): EG Prop. 9(a), Prop. 12
    and Prop. 13 with its sketch; BD Prop. 1's "only if it is
    information decreasing"; B23 v2's "N ≤ Ñ ≤ N³"; and BB's "a
    stochastic matrix with a stochastic inverse must be a permutation".
    All six are present.
  - That is a presence check, not a reading.
  - For r2 the following were also presence-checked in the same
    extractions:
    - EG Props. 16–18 (Prop. 18 on p. 35);
    - BD's reference to the Blackwell–Sherman–Stein theorem (BD p. 4,
      ref. [3]);
    - PI's citation of Cohen et al. [26] (p. 14);
    - the absence of "XOR" from DO1 and DO2, and its presence in DO3.
- **REC (record or abstract only).** Only a bibliographic record, an
  abstract or a secondary report was read. Any conclusion that rests on
  it is **PROVISIONAL**. **[secondary]** marks a work known only through
  its citation in an FT source.
- **NR (not read).** The source was not obtained, not attempted, or is
  recalled from memory. Any conclusion that rests on it is
  **PROVISIONAL**. **[from memory]** marks a bibliographic detail (venue,
  year) that was not checked against any record in this work.

No external source was read in this session beyond the presence checks
above. Web search was not used.

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

**The PROVISIONAL rule, applied uniformly (Rv5:3).**
- A class, or a part of one, whose decisive comparator is REC or NR is
  marked **PROVISIONAL**.
- This includes "not located" remainders whose decisive search areas
  were not read.
- It also includes REFRAMING classes that rest on unread textbook facts:
  the DPI, Pinsker, subadditivity, König's theorem. There is no textbook
  exemption. For such items PROVISIONAL concerns only the attribution,
  since the mathematical statement is standard and no novelty is claimed.
- Unless a class is so marked, a KNOWN or PARTLY KNOWN class rests on FT
  sources.

**Not classified.** An item gets no class when no literature at all was
examined for it (C15, C16-S), or when it is an interpretation and not a
mathematical claim ((e)).

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
| #919 (merged at `a411bf46`) | Explainer: invariance alone does not select the measure; partition-relativity scoped to the canonical measure | (e): the measure is a third input, consistent with v4 R15; GR:20 and ch07:46 not yet scoped (F23) |
| #911, #917 (after `a411bf46`) | research records only | none for the citations; #917's records not read (C16-S) |
| #925 (draft, head `75a99444`, **not merged**) | Main precision follow-ups | status only; see "Open draft PRs" below |
| #926 (draft, head `26e365d7`, **not merged**) | canonical-measure scope; Explainer status note | status only; see "Open draft PRs" below |

**Open draft PRs (status only, Rc2:N6–N7).** Neither is merged. Every
citation in this audit is to `a411bf46`, which is byte-identical to
`ebf98d83` for these paths. The coverage below comes from a read-only
fetch of each head and a line-by-line diff against `ebf98d83`. It records
what each draft touches; it is not a review of its content.

- **#926** (`26e365d7`) changes these sites:
  - ch01:77–83, ch07:46 and GR:20(ii), with their FULL mirrors, scoped to
    the canonical measure (F23);
  - Explainer:3–8, the status note (N7 above).
  - It also touches Explainer:492 and :1054–1056, and `book/README.md:110`.
  - It does **not** touch GR:20's "necessary as well as sufficient"
    (F24), the glossary (F25), ch01:101 (F21, F22) or `book/README.md:64`
    (F27).
- **#925** (`75a99444`) changes Main:86 and Main:522, pointing them at
  §1.2's "Remark on the measure as a realization datum" (F23).
  - By the same diff, it also changes lines carrying several F-notes:
    - Main:62, Birkhoff–von Neumann removed (F10);
    - Main:167, the "(C1)–(C3)" hypothesis replaced (F12);
    - Main:580(2) and the C10 kernel pointer, the joint-law scope added
      (F6);
    - Main:608 and :690, "Both directions … theorems" and "necessary and
      sufficient" replaced (F5);
    - Main:16, :28, :530, :532, the $Q_{\mathrm{fb}}$ wording (F3, F4).
  - It does **not** change Main:212, Main:680 (C12) or Main:332 and :149
    (F21, F22).
- **Not fixed by either:** GR:20's "necessary as well as sufficient"
  (F24); glossary:39 / FULL:6659 (F25); the F21/F22 sites; the ch01
  numeric-citation mismatch (F21); `book/README.md:64` (F27).

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
  of this paper", and so does Main:680 ("both directions in-house").
  Main:212 says "the equivalence (ii) ⟺ (iii) is proved in-house".
- The same characterization appears at:
  - Explainer:358, :378 and :1026;
  - Substratum:111 and :126;
  - book `appendix-b-derivations.md:22`, :406 and :455 (displayed), and
    their FULL.md mirrors (FULL:5809, :6193).
- In these sites it is the (ii) ⟺ (iii) form, with (C4) on the right.
  It is not the bare form that Main:597–598 displays as false. So it does
  not contradict Main, but C12 below still applies to it.
- **Two sites diverge from Main** (Rv5:6; recorded as F24 and F25):
  - GR:20: "C1–C4 necessary as well as sufficient for accessible
    non-Markovianity". This includes C2, against Main:516's "(C2) is
    deliberately absent from (iii)". The C2 clause carries "conditional
    on the eigenstate thermalization hypothesis", but the sufficiency
    claim is not scoped.
  - glossary:39 and FULL:6659: "The framework's central result … if and
    only if some finite-horizon deterministic realization satisfies the
    four conditions *C1*–*C4*". This contradicts both Main:516 (C2
    absent) and Main:99, which names $S \iff D$ and the universal
    statement as the core.
  - An introductory paper drafted from the glossary or the GR abstract
    would inherit both.

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
- **Claim (restated)**, against `a411bf46`;
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
- **Dating (Rv5:14).** EG v1 (26 Feb 2026) is **prior** for C1 and C1′.
  - The checks bound the first appearance; they do not prove it, since
    no history search was run.
  - `process_dilation_probes.py` is first added at `64c95fee`
    (2026-08-10).
  - Main.md at `6fc02988` (2026-02-25, then at the repository root) and
    at `bbf28c64` (2026-08-01) contains no process-dilation or
    history-ledger text (Rc2:N1).
    - `bbf28c64:papers/Main.md:394` does contain "ledger": the unrelated
      posit ledger ("this ledger counts what is *assumed*").
- **Class: PARTLY KNOWN.** The construction is EG Prop. 13's. The
  single-iterated-bijection form was not located as stated. It is an
  elementary strengthening, not a new idea.
  - The "not located" part is **PROVISIONAL**: Bennett 1973, the shift
    realization and HMM realization theory are NR.
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
  - The "not located" part (the reversibility packaging) is
    **PROVISIONAL** (Rc2:N4). It rests on the same unread search areas
    as C1's: Fine 1982, Kallenberg, Bennett 1973 and HMM realization
    theory.
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
  Díaz, PRA 100, 022120 (2019), both with venue **[from memory]**:
  **[NR]** (LC §8, T4; LC §10; Rc2:N8).
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
  - The three-way form is stated at Main:16–18, :526–530 and :580(1).
  - Main:98–99 states the two-way $S \iff D$, with $Q_{\mathrm{fb}}$
    only as the route for ⊇ (`D_imp_Qfb` with `Qfb_imp_S`) (Rv5:10).
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
    weights. It is not stated in GO, and it was not located in any FT
    source.
    - It is likely standard (Rv5:11). A rational doubly stochastic
      $T = A/d$ gives a $d$-regular bipartite multigraph. König's
      theorem (1916) **[NR, from memory]** splits that into $d$ perfect
      matchings, so $T$ is a mixture of permutations with weights in
      $\tfrac1d\mathbb{Z}$.
  - HHO Prop. 1 (p. 3) **[FT]**: the state-conversion version.
  - SCH Thm 1 (p. 5) **[FT]**: adjacent (uniform coarse graining of a
    bistochastic matrix).
- **Class: PARTLY KNOWN.** The closure statement is KNOWN. The exact
  rational clause is an elementary addition that was not located as
  stated. That "not located" part is **PROVISIONAL**, since König 1916
  and the combinatorics texts are NR.
- **Needed.** Cite GO Lemma 6 and footnote 8, plus a source for the
  rational decomposition (König 1916, or a combinatorics text; §5,
  P3.5). Fix F10.

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
  - B26 v1 (5 Aug 2026) predates the lemma's earliest located
    appearance in the repository (branch commit `9c1c157f`, 2026-08-13).
    LC §0.1 notes that its commit checks bound the first appearance and
    do not prove it.
  - SCH (2021) is prior regardless, so the class does not depend on
    that dating.
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
- **Needed.** Cite BB, or B23 footnote 5. Optional: Ding–Rhee's full
  text, or a nonnegative-matrix text (Berman–Plemmons **[NR, from
  memory]**: a nonnegative matrix with nonnegative inverse is monomial).

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
  - **Older classical sources, named in FT sources [secondary]**
    (Rv5:8):
    - BD's semiclassical case rests on the Blackwell–Sherman–Stein
      theorem: BD p. 4, its ref. [3], Blackwell, *Ann. Math. Stat.* 24,
      265 (1953).
    - PI p. 14 credits the classical "divisible iff information
      monotonically decreasing" result to Cohen, Iwasa, Rautu, Ruskai,
      Seneta and Zbăganu, LAA 179, 211 (1993) (PI ref. [26]), "presented
      in Buscemi and Datta".
    - Total-variation contraction under a stochastic matrix is older
      still.
    - So BD is the prior result *in the divisibility form*, not the
      origin of the contraction property.
  - **Main already cites the mechanism (§A.19; Rv5:7).**
    - Main:121 attributes "P-divisibility ⟹ $d(p(t),q(t))$
      non-increasing" to [4, 5]: RHP, PRL 105, 050403 (2010) and RHP,
      Rep. Prog. Phys. 77, 094001 (2014).
    - Main:149 cites [4, 5], Bylicka–Johansson–Acín [9] and Milz et al.
      [10]. Main:194 cites [4, 5, 7, 9].
    - These are quantum sources, and their texts are **[NR]** here.
    - Breuer–Laine–Piilo 2009 is not in Main's bibliography (F21).
- **Class: KNOWN.** It is the data-processing (contraction) property of
  stochastic maps, used once. Its divisibility form is BD Prop. 1's
  data-processing direction (FT). The older classical sources are
  [secondary].
- **Needed.**
  - Cite the contraction property with a classical source: Cohen et al.
    1993, or BD 2016 for the divisibility form. Cite DO3 v3 Prop. 1 as
    concurrent.
  - At Main:121, the citation should name a classical source (BD, or
    Cohen et al.), not only the quantum [4, 5].
  - In Main, cite [22] by version (LC §9 item 3).
  - Read Cohen et al. 1993 and Blackwell 1953 before citing them (§5,
    P1.3).

### C8-R — rooted classification (`finiteRootedRealizable_iff_pper`, `RootedClassificationAllTime:192`) — **novelty unverified**

- **Claim, scoped to the two-sided characterization (Rv5:4).** For
  finite $V$, `PPer` is *exactly* the realizable class.
  - A family $(\Gamma_t)_{t \in \mathbb{N}}$ is the family of rooted
    visible maps of one finite permutation, with one hidden prior shared
    by every visible root, **iff** $\Gamma_0 = 1$, every $\Gamma_t$ is
    row-stochastic, and the family has a positive period (`PPer`).
  - The candidate is the biconditional as a whole. Neither half, taken
    alone, is a candidate:
    - necessity is folklore;
    - sufficiency is a located construction, packaged (below).
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
    `book/*.md` at `a411bf46` finds no statement of it (no
    `finiteRootedRealizable`, `rootedMap`, `RootedClassification` or
    "rooted classification" hit).
  - So if it enters the introductory paper, it enters as **new
    manuscript content**, not as a restatement of Main.
- **Literature.**
  - **EG Props. 16–18 (pp. 34–35) [FT] give C8-R's sufficiency
    construction**, once restricted to one period (Rv5:4).
    - Prop. 18 (p. 35), via Props. 16 and 17, realizes every linear
      probability dynamics over a finite $T = \{0, \dots, \tau\}$. That
      is every rooted family on $\{0, \dots, \tau\}$, realized by a
      time-indexed deterministic map
      $A : T \times C \times \Lambda \to C$ with an independent fixed
      ancilla law.
    - Apply it to one visible period $\{0, \dots, M-1\}$. Add a clock
      mod $M$, and record the root on zero-prior padding states, so
      that the time-indexed readout becomes one iterated bijection. The
      result is C8-R's sufficiency half.
    - Why the family returns: at clock value 0 the readout is
      $A(0, a, \lambda) = a$, so $\Gamma_M = 1$, and the static ancilla
      makes $\Gamma_{t+M} = \Gamma_t$.
    - This argument is Rv5:4's. It was re-checked here in prose only,
      not computed. The kernel's own sufficiency proof
      (`RootedClassificationAllTime:162`, response tables per residue on
      embedded cycles) is of the same kind.
    - That is the same ledger-and-clock packaging this audit counts as
      elementary for C1 and C1′. On the C1/C1′ standard, the sufficiency
      half is PARTLY KNOWN.
    - EG Props. 16–18 do **not** give necessity. Over a finite horizon,
      time-indexed maps impose no periodicity. Necessity is the finite
      order of a permutation.
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
  direction), for the two-sided characterization only. Within it:
  - sufficiency is PARTLY KNOWN (EG Props. 16–18 plus elementary
    packaging, FT);
  - necessity is folklore.
  - What was not located is the statement that `PPer` is exactly the
    realizable class of one finite permutation with a shared prior.
- **Skeptical reading (§A.31).** The favorable reading is that this is a
  new characterization. Pressure-tested:
  1. Necessity is the finite order of a permutation, which is folklore.
  2. Sufficiency is an elementary embedding of a random-mapping
     representation, one response table per residue mod the period,
     into the cycles of one permutation.
  3. The search that found nothing was keyword-based, and it skipped
     the three areas where an equivalent statement would most likely
     appear: realization theory, automata and symbolic dynamics.
  4. The sufficiency construction itself is located (Rv5:4). EG
     Props. 16–18 restricted to one period, plus a clock and zero-prior
     root padding, give it [FT].
     - So the only unlocated content is the conjunction of a located
       construction with a folklore necessity.
     - That is a remark-sized combination, and the least likely kind of
       statement to be new.
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
- **Class: REFRAMING, PROVISIONAL** (a direct Pinsker application;
  attribution only, §0.4).
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
- **Class: REFRAMING, PROVISIONAL.** It is the DPI applied to
  $Y = f(X, H)$. The decisive comparator, the conditional DPI, is NR, and
  SC Thm 5 is FT but a different statement. PROVISIONAL concerns the
  attribution only (§0.4; Rv5:3).
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
- **Class: REFRAMING, PROVISIONAL** (attribution only, as C10).
- **Needed.** As for C10.

### C12 — the "characterization theorem" (ii) ⟺ (iii) (Main:212, :516–522, :608, :680; Explainer:358, :378, :1026; Substratum:111, :126; appendix-b:22, :406, :455; FULL:5809, :6193)

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
  - Main:99 names $S \iff D$ and the universal statement as the
    paper's core.
    - What #922 removed was the bare form (C4-old).
    - (ii) ⟺ (iii) was not the displayed core at `c91bf5dd` either
      (Rv5:13).
  - glossary:39 (and FULL:6659) still calls the characterization
    theorem "the framework's central result", in a four-condition form
    that diverges from Main (F25).
  - It must not be offered as a "characterization of non-Markovianity"
    in the introductory paper.
- **Sites and their wording** (Rv5:6, verified at `a411bf46`):
  - "both directions are theorems" or "in-house":
    - Main:608, :680 and :212;
    - Explainer:378 ("Both directions are the foundational paper's own
      theorems"). The same line carries the self-narration "The old
      three-way biconditional is retired" (§A.30, §A.33; F26).
  - Characterization as stated: Main:516; Explainer:358, :1026;
    Substratum:111; appendix-b:22, :406, :455 (displayed); FULL:5809,
    :6193.
  - Substratum:126 attaches "accessible non-Markovianity ⟺ C1/C3/C4
    realization per horizon" to "the universal hidden-memory theorem".
    That conflates C12 with C10-B.
  - **Divergent from Main:** GR:20 (F24) and glossary:39 / FULL:6659
    (F25); see §1.
- **Needed.**
  - The paper should either omit C12, or state it with Main:596's
    reduction beside it.
  - Main:608's "Both directions … are theorems" (F5) is unchanged and
    stays a correction target, with Main:212, :680 and Explainer:378.
  - The paper must not be drafted from GR:20 or glossary:39.

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
    - 0.646 is Page's half-area time $t_{1/2}$ (pdf p. 12).
    - Paraphrase (Rv5:15): Page notes there that describing the Page
      time as the time "when the black hole has emitted half of its
      initial Bekenstein-Hawking entropy" would be correct only if β
      were unity.
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
  - Propagation was checked by a grep at `8dc36d55`. Those files are
    byte-identical at `a411bf46`. All of the following carry the
    conditional form:
    - ch07:12;
    - ch09:127, ch18:148, ch19:72, glossary:113;
    - FULL.md:1887, :2013–2036, :2605, :4966, :5246, :6733;
    - GR:611.
  - **Summary site without the condition** (Rv5:16; F27).
    `book/README.md:64` lists "the Page curve from nested trace-out"
    without H-scramble. It is not one of the withdrawn claims, but the
    omission is noted.
- **C16e — subadditivity bound** (GR Thm A.6): from a product state under
  a global unitary, the sum of the sectors' von Neumann entropies does
  not decrease.
  - **Class: REFRAMING, PROVISIONAL** of subadditivity. Textbook
    **[NR]**; PROVISIONAL concerns the attribution only (§0.4).
- **C16-S — the three-way separation** for an access class (v4 §7.3):
  preserved, recoverable by 𝒜, and typical.
  - Hayden–Preskill, PSW and decoupling: **[NR]**.
  - #917's landed records (`verification/programmes/black-hole-information/`,
    at `ebf98d83`) were not read.
  - **Class: not classified** (Rv5:12). No literature was examined, which
    is the same basis on which C15 is left unclassified. The pedagogical
    use stays open.
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
  - **#919, merged at `a411bf46`, brought the Explainer into line with
    this.** Partition-relativity is scoped to "the canonical measure" at
    Explainer:101, :422 and :1008, matching Main:86.
  - So the measure is a third input whenever a general prior is
    allowed, which reinforces R15.
- **Mirrors not yet scoped** (Rv5:9; F23). These state partition-relativity
  without the canonical-measure scope:
  - GR:20 item (ii): "the emergent description is uniquely determined by
    the partition";
  - ch07:46: "the emergent description is uniquely determined by the
    partition geometry".
  - Under bidirectional §A.25 propagation, Main and the Explainer now
    lead GR and ch07.
  - #919's description names GR.md:20 and ch07:46 (with ch01:79, :83 and
    their FULL.md mirrors) as "Not in this PR … Separate correction".
  - Per the coordinator, they are within the scope of the
    manuscript-consistency PR. This audit did not read that PR.
- **Literature.**
  - Barandes B23, B25, B26 **[FT]**.
  - Calvo v1/v2 **[FT]** and the journal record **[REC]**. Calvo's claim
    to derive the textbook axioms is **stronger** than OI's equivalence
    (LC §3.4). The paper must not present OI as such a derivation, and
    must not describe Calvo as a dimension extension (F14 below).
  - Doukas **[FT]**; Pimenta **[FT]**.
  - 't Hooft 2016 **[NR]**. Main cites it as [1] (Main:30, :688, :776).
  - Spekkens 2007 **[NR]**. Main:550 names "Spekkens noncontextuality",
    which is not a citation of Spekkens 2007.
- **Class: not classified** (interpretation; §0.4; Rv5:3). No novelty
  class applies to an interpretation.
  - Its relation to the FT comparators is as stated above. Its relation
    to 't Hooft and Spekkens is open.
- **Needed.** 't Hooft (2016) and Spekkens 2007 before the paper
  positions the reading against them (§5, item P2.3).

### Other items the literature studies touched

- **The XOR example** (Main:606: $X_1$ uniform, $X_2 = X_0 \oplus X_1$,
  non-Markov but with a P-divisible matrix family).
  - **Concurrent: DO3 v3 App. A** (pp. 36–37) **[FT]**. It is the same
    process, with all two-time kernels $\tfrac12 J$.
    - App. A is in v3 only: "XOR" occurs in neither DO1 nor DO2.
    - v3 was posted 19 Oct 2026.
  - **The repository's example is earlier** (Rv5:1). It is in
    `papers/oi_lattice_code/foundations/review4_probes.py` from that
    file's first commit, `e6c21398` (2026-08-11), lines 6–8: "X2 = X0 XOR
    X1 … T^(1) = T^(2) = J/2 and the family factors with Lambda = I".
  - So by the dating standard used for C8, DO3 is concurrent, not prior.
  - **Class: KNOWN, PROVISIONAL.** A non-Markov process with
    Chapman–Kolmogorov-consistent kernels is a classical type of
    example, but no prior source has been read. Prior-source candidates,
    both **[NR]**:
    - Feller 1959, *Ann. Math. Stat.* 30 **[from memory]**: a non-Markov
      process with the semigroup property;
    - the quantum analogue Milz, Kim, Pollock and Modi, "Completely
      positive divisibility does not mean Markovianity", PRL 123, 040401
      (2019), which is Main [10] (Main:149, :794).
  - **Needed.** Read one prior source (§5, P3.6) before the example is
    attributed. Until then, cite DO3 v3 App. A as concurrent.
- **v4 §4.5's branch-(B) witness** ($\Gamma_1 = \tfrac12 J$) is the same
  matrix, used for a different point.

***

## 4. Fidelity notes: status at `a411bf46`

The F-identifiers are kept. Nothing is renumbered, and no retired number
is reused (§A.30).

| ID | v4 finding | Status at `a411bf46` |
|---|---|---|
| F1 | Main:97–99 displayed the bare false form as the core | **resolved** (#922) |
| F2 | Main:500 pointed at `S_imp_D` for the independent-prior form | **resolved** (#922: scope stated in place; census note) |
| F2b | `Equivalence:346–348` and Main:532 called the carrier "response-table" | **resolved** (#922: comment at :346–351; Main:532 "by a different carrier") |
| F3 | $Q_{\mathrm{fb}}$ wording; `e^{-iĤ}` remark contentless | unchanged (Main:16, :530, :532) |
| F4 | title (Main:2) and Main:28 beyond Main:22, :534, :542 | unchanged; Calvo FT (LC §3.4) sharpens it |
| F5 | Main:608 "Both directions … are theorems", Main:690 "necessary and sufficient" | unchanged; also Main:212, :680 and Explainer:378 (C12) |
| F6 | Main:580(2) "proved" for the biconditional | **narrowed**: Main:99 states the directions and two unformalized links; Main:580(2) does not carry them |
| F7 | Main:580(4) "proved unconditionally", no kernel anchor | unchanged |
| F8 | missing citations | unchanged; both halves listed below |
| F9 | ch07 §7.6 overclaims and mirrors | **resolved** (#920, mirrors checked; C16d) |
| F10 | Main:62 credits Birkhoff–von Neumann with double stochasticity | unchanged; GO's proof confirms it **[FT]** |
| F11 | kernel route vs Main:20 and :139; EquivalenceChain header | header **resolved** (#922); the citation guidance for C8 stands (C8 above) |
| F12 | Main:167's (C1)–(C3) unused | unchanged |
| F13 | the `≤ n³` import | **kept separate** (§6) |

**F8, refreshed. What Main does not cite.** A grep of `papers/*.md` and
`book/*.md` at `8dc36d55` (byte-identical at `a411bf46` except
Explainer) found no citation of:
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
- Hardy 2004;
- Breuer–Laine–Piilo 2009, in Main: "Laine" occurs in Main only at
  :332 (F21).
  - Elsewhere in the corpus BLP is *named*: Explainer:148; ch01:101 and
    its mirror FULL:445, as "Breuer, Laine, and Piilo [9]"; ch18:78 and
    FULL:4896.
  - `book/bibliography.md` has no BLP entry. Its only Breuer is T.
    Breuer 1995 (F21).

Main names "the exact Koopman operator" (Main:728, :742) as an object but
cites no Koopman source for the permutation unitary.

**F8. What Main does cite** (§A.19; Rv5:7). The paper's task for these
is to describe them correctly, not to add them.
- **For the C8 mechanism:**
  - Main:121 cites Rivas–Huelga–Plenio [4] (PRL 105, 050403, 2010) and
    [5] (Rep. Prog. Phys. 77, 094001, 2014) for "P-divisibility ⟹
    $d(p(t),q(t))$ non-increasing".
  - Main:149 cites [4, 5], Bylicka–Johansson–Acín [9] (PRL 118, 120501,
    2017) and Milz et al. [10] (PRL 123, 040401, 2019).
  - Main:194 cites [4, 5, 7, 9].
- **For (e) and positioning:**
  - 't Hooft's cellular-automaton interpretation [1] (Main:30, :688).
  - Spekkens noncontextuality is named at Main:550; Spekkens 2007 is not
    cited.
  - Hardy 2001 [51] (Main:352, :876).
- **Already in v4's list:** the Calvo preprint [13]; Fine 1982 [25],
  with no in-text citation found; Pimenta [14]; Doukas [22].
- **Caveat.** These name-greps are evidence for "Main does or does not
  cite X". They are not evidence that the corpus is silent on the
  underlying mathematics.

**Fidelity findings carried from LC §9** (verified there in full text;
their Main lines are unchanged at `a411bf46`). None is applied here; each
is for the owner under §A.25.

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

**New fidelity findings in r2** (verified at `a411bf46`; for the owner,
none applied):

- **F21.** Main:332 attributes "the Breuer-Laine-Piilo criterion" to
  [3, 4], which are Breuer–Petruccione 2002 and RHP 2010. BLP 2009 has no
  bibliography entry (Rv5:7a).
  - **Beyond the review:** the book has the same gap. ch01:101 and
    FULL:445 cite "Breuer, Laine, and Piilo [9]", but `book/bibliography.md`
    has no BLP entry.
  - **Further BLP sites (Rc2:N5):**
    - appendix-b:96 / FULL:5883 name the "Breuer-Laine-Piilo
      *information backflow* signature" as sufficient evidence, which is
      consistent with Main:332;
    - Explainer:624 names "the Breuer–Laine–Piilo indivisibility
      criterion" in passing.
  - **ch01 numeric citations (Rc2:N5).** ch01 uses numeric citations
    ([2] at :32, [8] at :85, [9] at :101) against the author-year
    `book/bibliography.md`.
    - Under Main's numbering, [9] is Bylicka–Johansson–Acín (Main:792),
      not BLP.
    - So ch01:101's "[9]" dangles.
  - Status: neither #925 nor #926 fixes these sites.
- **F22.** Main:149's "divisibility failure is equivalent to information
  backflow [4, 5]" contradicts two other Main statements (Rv5:7b):
  - Main:121: "The converse is *false*";
  - Main:332: system backflow is "sufficient evidence of
    indivisibility, never necessary".
  - BD Prop. 1's equivalence (FT) holds for the guessing probability
    over general ensembles, not for a single distinguishability
    pair-norm. The paper must state which notion it uses.
  - **Beyond the review — the same equivalence is asserted, attributed
    to BLP, at:**
    - Explainer:148 ("Breuer, Laine, and Piilo proved that
      P-indivisibility is equivalent to 'information backflow'");
    - ch01:101 and FULL:445 ("showed that P-indivisibility is equivalent
      to … information backflow").
  - Under §A.25 these are sites of the same correction. BLP 2009 itself
    is NR here, so what it states is not adjudicated.
- **F23.** These state partition-relativity without the canonical-measure
  scope of Main:86 and Explainer:101, :422, :1008 (Rv5:9; Rc2:N6;
  (e) above):
  - GR:20 item (ii);
  - ch07:46;
  - ch01:79 (the Lemma: "*The emergent description is uniquely
    determined by the partition*") and ch01:83;
  - their FULL.md mirrors.
  - Separately, Main:86's pointer "(§1.3 Remark)" should name §1.2.
  - #919's description lists all of these as "Not in this PR … Separate
    correction".
  - **Status:** draft #926 (`26e365d7`, not merged) scopes ch01:77–83,
    ch07:46 and GR:20(ii), with their FULL mirrors. Draft #925
    (`75a99444`, not merged) changes Main:86 and Main:522 to point at
    §1.2's Remark. Until they merge, the sites stand as listed.
- **F24.** GR:20: "C1–C4 necessary as well as sufficient for accessible
  non-Markovianity". It includes C2, against Main:516's "(C2) is
  deliberately absent from (iii)" (Rv5:6; §1, C12).
- **F25.** glossary:39 and FULL:6659: "The framework's central result …
  if and only if some finite-horizon deterministic realization satisfies
  the four conditions *C1*–*C4*". It contradicts Main:516 (C2 absent)
  and Main:99, which names $S \iff D$ and the universal statement as the
  core (Rv5:6).
- **F26.** Explainer:378 carries the self-narration "The old three-way
  biconditional is retired" (§A.30, §A.33), beside "Both directions are
  the foundational paper's own theorems" (F5).
- **F27.** `book/README.md:64` summarizes "the Page curve from nested
  trace-out" without the H-scramble condition that every other book
  summary carries (Rv5:16; C16d).

***

## 5. Literature that must be read before any novelty claim enters the paper

The list is prioritized by what each item gates. P1 items gate the only
two candidates that could carry a novelty sentence (C8-R, C8-D). Nothing
in P2–P4 can raise any class to NOVEL-CANDIDATE. Those items gate
attributions and the correct description of related work.

Bibliographic details marked **[from memory]** (venue, year, title) were
not checked against any record in this work (Rv5:16). Items marked
**[secondary]** are named in an FT source, and their details are taken
from that source.

**P1 — gates C8-R and C8-D**

1. **HMM and stochastic realization theory.**
   - Sources: Heller 1965 (Ann. Math. Stat.) **[from memory]**; Anderson
     1999 (MCSS, "The realization problem for hidden Markov models")
     **[from memory]**; Vidyasagar's HMM realization work; Picci's
     stochastic realization.
   - Why: this is the field whose subject is which processes are
     functions of finite (deterministic or Markov) systems. A
     characterization of rooted families of *deterministic* periodic
     systems with a random initial state is most likely to sit here as a
     lemma. The searches did not cover it (LC §6.3).
2. **Automata and symbolic dynamics.**
   - Sources: realization of stochastic sequential machines by
     deterministic machines with random state (Rabin 1963; Paz 1971;
     Carlyle 1963; all **[from memory]**); factors and codings of finite
     permutations and periodic processes in ergodic theory.
   - Why: C8-R's sufficiency is a deterministic-machine, random-state
     realization. EG Props. 16–18 already give it over one period, and
     the construction may be older still.
3. **Divisibility, contraction and revival literature.**
   - **Classical contraction sources** (Rv5:8):
     - Cohen, Iwasa, Rautu, Ruskai, Seneta and Zbăganu, LAA 179, 211
       (1993) **[secondary, via PI p. 14]**;
     - Blackwell, *Ann. Math. Stat.* 24, 265 (1953) **[secondary, via BD
       p. 4]**.
   - **Quantum sources Main already cites for the mechanism** (Rv5:7):
     RHP 2010 [4] and RHP 2014 [5]; Bylicka–Johansson–Acín 2017 [9].
   - **Others:**
     - forward citations of BD 2016 (not indexed by INSPIRE; Semantic
       Scholar and OpenAlex returned 429);
     - Wißmann–Vacchini–Breuer (abstract only so far, LC §5.11);
     - Breuer–Laine–Piilo 2009;
     - the Milz–Modi PRX Quantum 2021 review **[from memory]**;
     - Breuer–Petruccione on finite-environment revivals;
     - Pleasance, arXiv:2607.07332 (located, not read).
   - **Optional:** the embedding and divisibility of stochastic matrices,
     Elfving 1937 and Kingman 1962 **[from memory]**.
   - Why: a recurrence-forced indivisibility statement for finite
     systems (C8-D) would most likely be stated there, as would a
     permutation-or-indivisible dichotomy. Cohen et al. or Blackwell is
     also needed before the paper credits the contraction property
     (C8, §7).

**P2 — gates C4's packaging and the related-work section**

1. **Milz et al., PRX 10, 041049 (2020)** and **Strasberg–García Díaz,
   PRA 100, 022120 (2019)**, both **[from memory]** as to venue (cited
   so by v4 and LC from search summaries).
   - These are the nearest likely statements that multi-time projective
     records of quantum systems form (Kolmogorov-consistent) classical
     processes, and when.
   - They bear directly on the $Q_{\mathrm{fb}}$ ⇒ S direction and on
     whether the three-way multi-time packaging (C4) was already stated.
2. **The Calvo journal full text** (*Quantum Stud. Math. Found.* 14, 2
   (2026), CC BY; from the Crossref record). Its body identity with arXiv
   v2 is unverified. It is needed before Main [13] is re-described (F14)
   or its version cited.
3. **'t Hooft (2016, *The Cellular Automaton Interpretation*; Main [1])**
   and **Spekkens 2007** **[from memory]**. These are the positioning
   comparators for (e). 't Hooft is also the comparator for C2's
   historical attribution.
4. **Bennett 1973, Fine 1982 (PRL 48, 291; Main [25]), Kallenberg
   (transfer lemma), Koopman 1931 (PNAS 17, 315; from LC §1's retrieval
   attempt).**
   - These settle the attributions of C1, C1′ and C2: history tape;
     response functions; noise outsourcing; the permutation operator.
   - They cannot change those classes, because EG and LPW already make
     them PARTLY KNOWN. They gate the PROVISIONAL "not located" part of
     C1.
5. **Barandes, *Philosophy of Physics* 3(1):8 (2025)**, the published
   version of [12]. It is needed for [12]'s exact claims, including "at
   least some choices" of j′ (relevant to §6).

**P3 — gates REFRAMING attributions and the example**

1. **Rutten 2000** (TCS 249, 3–80), plus Kalman observability, for C13.
2. **Hardy 2004** (SHPMP 35, 267) and **Heinosaari et al. [55]**, for C14.
3. **Cover–Thomas** (DPI, conditional DPI, Pinsker), for C9, C10, C11
   and C16e citations.
4. **Ding–Rhee 2014** full text, or **Berman–Plemmons** **[from memory]**,
   for C7. Optional; BB and B23 suffice.
5. **König 1916** **[from memory]**, or a combinatorics text, for C5's
   rational Birkhoff decomposition (Rv5:11).
6. **A prior source for the XOR example** (Rv5:1): Feller 1959, *Ann.
   Math. Stat.* 30 **[from memory]**, and Milz et al., PRL 123, 040401
   (2019), Main [10].

**P4 — gates the black-hole paragraph, if there is one**

1. **Popescu–Short–Winter 2006, Hayden–Preskill 2007** **[from memory]**,
   and a decoupling reference, for C16c and C16-S. Also #917's landed
   records, `verification/programmes/black-hole-information/` at
   `ebf98d83`, for C16-S.
2. Zurek 1982, Page 1976 (PRD 13, 198; PRD 14, 3260), Page 1983.
   Optional: Page 2005 and 2013 already supply every citation the
   manuscripts make.
3. Alishahiha et al., arXiv:2005.08715 (abstract only so far), for the
   statement that no 4D evaporating island Page-time fraction is
   established.

**Outside the literature check:**
- C15 needs an internal audit before it needs a literature map (C15
  above). Its search directions are **[from memory]**.
- Kernel items v4 K1–K4 are unchanged.

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
- **Sites at `a411bf46`, unchanged since `c91bf5dd`:**
  - Main:204, 210, 350, 504, 506, 514, 636, 690, 716;
  - Explainer:287 (which also restricts the class to P-indivisible
    processes) and Explainer:1020. #919 merged without touching either
    line, and the review of r1 confirmed both.
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

Unchanged in substance from v4 §8.

**Evidence basis (Rv5:3).**
- Every KNOWN or PARTLY KNOWN class rests on FT sources, except the parts
  marked PROVISIONAL.
- The PROVISIONAL marks follow the uniform rule of §0.4. They cover the
  "not located" remainders of C1, C1′, C4, C5 and C8-D; the REFRAMING classes
  resting on unread textbook facts (C3, C9, C10, C11, C16e); C13 and C14;
  C16c; and the XOR example.

**Classes after both studies:**
- KNOWN: C2, C6, C7, C8, C16a, C16b; the XOR example, PROVISIONAL;
- PARTLY KNOWN: C1, C1′, C4, C5, C8-D, C16c;
- REFRAMING: C3, C9, C10, C10-B, C11, C12, C13, C14, C16e;
- WITHDRAWN: C4-old, C16d;
- not classified: C15, C16-S, (e);
- NOVEL-CANDIDATE: only C8-R, as the two-sided characterization, with
  novelty unverified. Its sufficiency half is a located construction
  (EG Props. 16–18) and its necessity half is folklore.

**A technical perspective / pedagogical review, not a research
article.** The literature check lowered the estimate, as v4 §8 predicted
it could:
- C6 moved from "pending" to KNOWN (B26, SCH), C8 to KNOWN (BD), and C5
  to PARTLY KNOWN (GO);
- r2 narrowed C8-R to the biconditional.
- Nothing moved up.

**Novelty statement that should survive scrutiny** (v4's text, corrected
in r1 and r2):

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
> information in its hidden state; the inequality is machine-checked for
> the joint law of history, present visible state and hidden state, and
> the identification of a realization's time-$t$ law with that joint law
> is not formalized. And for one finite reversible system with a hidden
> prior shared by all visible roots, the rooted visible maps are either
> permutations at every time or stochastically indivisible within every
> visible recurrence period — an elementary combination of finite
> recurrence with the contraction (data-processing) property of
> stochastic maps, in the divisibility form of Buscemi and Datta 2016,
> assembled from machine-checked theorems and elementary steps that are
> not formalized. For a finite visible alphabet, and with hidden states
> of zero prior weight permitted, we also give a machine-checked proof
> that the rooted families realizable by one finite permutation with a
> hidden prior shared by all roots are exactly the periodic stochastic
> families rooted at the identity. The realization half is an instance
> of the time-indexed construction of Egri et al. (Props. 16–18),
> packaged as one bijection, and the necessity half is the finite order
> of a permutation. We state where the finite correspondence stops short
> of operational quantum theory, and we offer the reading of quantum
> structure as the form of embedded observation as an interpretation,
> not a derivation.

- **No priority sentence** may be attached to the rooted classification
  until §5 P1.1–P1.3 are read.
- **Cohen et al. 1993 and Blackwell 1953 are [secondary]** and stay in
  the pending list (§5, P1.3). The sentence cites Buscemi–Datta alone
  until one of them is read (Rc2:N2).
- **"Is an instance of … packaged as one bijection"** describes a
  relation of constructions. It does not assert provenance: the kernel
  proof (`RootedClassificationAllTime:162`) was not shown to derive from
  EG (Rc2:N3).
- **"Machine-checked"** presupposes a Lean build (v4 K4). It covers only
  the kernel declarations. It never covers:
  - B3, B4 or A1;
  - the time-$t$ joint-law reading;
  - C1′'s prior independence;
  - the full-support separation (v4 K1).

**Related work the paper needs** (FT unless marked):
- B26; B23 and B25 (correctly labelled, F17); EG; BD; DO3 v3 Prop. 1
  and App. A as concurrent work, with [22] by version; GO Lemma 6 and
  footnote 8; SCH; BB or B23 footnote 5; LPW Prop. 1.5; SC (the
  ε-machine contrast); GH and MO;
- Calvo, correctly described (F14);
- Pimenta, with its two-configuration scope (F15);
- Main's existing [4, 5, 9, 10], described consistently with Main:121
  (F22);
- pending:
  - Hardy 2004, Rutten, Milz et al. 2020, Strasberg–García Díaz,
    't Hooft, Spekkens;
  - Cohen et al. and Blackwell;
  - a prior source for the XOR example;
  - König 1916;
  - the P1 areas.

If black holes appear: Page 2013 Eq. (8), Page 2005 Eqs. (5)–(10),
Penington 2019 §2, and Page 1993 Eq. (10). Note the README omission
(F27).
