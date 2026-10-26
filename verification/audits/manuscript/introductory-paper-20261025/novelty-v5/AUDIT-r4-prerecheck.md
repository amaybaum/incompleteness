# Novelty and fidelity audit, revision 5 (r4) — introductory paper

Working title of the proposed paper: *Observational Incompleteness: From
Deterministic Dynamics to Quantum Observations*. This revision replaces
revision 4 for drafting purposes.

This is r4 of revision 5.
- r2 applied the independent review of r1 (`revnov5/REVIEW.md`, verdict
  BLOCK, wording only). Its findings are cited as `Rv5:N`.
- r3 applied the nits N1–N8 of the re-check of r2
  (`revnov5/RECHECK-r2.md`, ACCEPT WITH NITS), cited as `Rc2:Nn`.
- r4 does two things (CHANGES.md, "r3 → r4"):
  - it re-bases §0.1, §1 and §4 to `origin/main` `83d1da1b`, after #925,
    #926, #927 and #928 landed, and records for every fidelity note
    whether its site is fixed, changed or open, with the fixing commit;
  - it applies a first-hand full-text reading of the highest-priority
    pending literature (§0.2, §8). That reading changes three classes:
    the XOR example, C3, and the evidence basis of C8.
- r4 has had no separate review.
- r1, r2 and r3 are kept unchanged: `AUDIT-r1.md` (sha256
  `ef9d475c…787a`), `AUDIT-r2.md` (sha256 `df39e2f9…4b93`) and
  `AUDIT-r3.md` (sha256 `6dae22ac…99f9`).

Revision 5 does three things:

1. restates every candidate contribution against `main`. r1–r3 used
   `a411bf46`; r4 uses `83d1da1b` (§0.1);
2. folds in the two accepted full-text literature studies (the
   black-hole study and the stochastic–quantum correspondence study) and,
   from r4, this audit's own full-text reading (§8);
3. gives each candidate one of five classes (§0.4) and states what is
   still needed.

**Correct is not the same as original.** A class in this audit concerns
originality: whether the statement is in the prior literature. Whether
a statement is *correct* is recorded separately, under "Internal" (kernel,
prose or probe). A KNOWN class says nothing against correctness, and a
kernel proof says nothing for originality. C8-R, for example, is proved
in the kernel and its originality is unverified.

Revisions 1–4 are unchanged and remain the record of what each found.
Local work product: nothing was committed, pushed or posted.

## 0. Scope, inputs and standing

### 0.1 Inputs

- **Repository at `main` `83d1da1b`** (2026-10-26 06:44 +0200, "Merge
  #928"). This is r4's base. It was read with `git show` and `git diff`
  from a read-only blob-filtered clone, `scratchpad/novelty6/repo`, in
  which no tracked file was changed.
  - r1–r3 were based on `a411bf46` ("Merge #919"), and r3 checked that
    every citation also held at `ebf98d83` ("Merge #917").
  - `a411bf46` → `ebf98d83` → `83d1da1b` is an ancestor chain. The
    first-parent merges after `ebf98d83` are #925 (`8b5e8681`), #926
    (`c1cade86`), #927 (`03eb1395`) and #928 (`83d1da1b`).
  - #928 adds only `.github/workflows/pe01-bounded-tests.yml`.
  - #925, #926 and #927 change manuscript files only:
    - Main, GR, Explainer, Substratum and Methodology;
    - book ch01, ch04, ch07, appendices b and c, glossary, bibliography,
      README and FULL;
    - their `.tex`/`.pdf`;
    - `verification/coverage/LEDGER.json`.
    What each one fixed is recorded in §1 and §4.
  - `a411bf46..83d1da1b` changes no file under
    `verification/lean-mathlib/`, nor the census, nor
    `arc-b-rooted-classification/result.md`, nor
    `papers/oi_lattice_code/`. Every kernel citation in r3 therefore holds
    unchanged.
  - #917 is the OI-BH-1 black-hole information audit. v4 §0.1 treated
    every black-hole statement attributed to #917 as open. Its landed
    records under `verification/programmes/black-hole-information/` were
    **not read**, and C16-S stays unclassified pending them (§3, C16).

  | Path | Blob at `83d1da1b` | Blob at `a411bf46` | Blob at `c91bf5dd` |
  |---|---|---|---|
  | `papers/Main.md` | `dff86915265a` | `78adc1110e8d` | `01e296e6a1e4` |
  | `papers/GR.md` | `f662d1e0730b` | `cb7dfbcc9971` | `90268f3b356d` |
  | `papers/Explainer.md` | `1e40cb80bd23` | `a6d4cb2b53cc` | `ce4b28eee244` |
  | `papers/Substratum.md` | `3e429344065e` | `e745c55a9047` | — |
  | `book/ch01-observation.md` | `b5c006fa2430` | `f650b66dd3d9` | — |
  | `book/ch07-gravity.md` | `3ad3c8ce71ef` | `323726e06107` | `2876061f1164` |
  | `book/appendix-b-derivations.md` | `8c7c6cd917e5` | `7765fb998e03` | `e64b3744c996` |
  | `book/glossary.md` | `b9af820fdb1e` | `9f9d63d5ed92` | — |
  | `book/README.md` | `bc896fba2792` | `ee357d0e7c11` | — |
  | `book/…-FULL.md` | `c46f2d40a111` | `1e3801e0c534` | — |
  | `verification/lean-manuscript-census.json` | `89a44bbc1fff` | same | `e50b85ffb8df` |
  | `OIBridge/Equivalence.lean` | `9513665b3888` | same | `08b9c358feb3` |
  | `OIBridge/EquivalenceChain.lean` | `10d3e4bb4286` | same | `3f06f76b7f3d` |
  | `OIBridge/HiddenMemory.lean` | `b0cb1cb4203c` | same | same |
  | `OIBridge/RecurrenceHorizon.lean` | `1ee2936d6d16` | same | same |
  | `OIBridge/RootedClassification.lean` | `ffb7546f72f0` | same | same |
  | `OIBridge/RootedClassificationAllTime.lean` | `13123378286a` | same | same |
  | `OIBridge/PhysicalC4Discharge.lean` | `832eeac3ee5f` | same | same |
  | `OIBridge/CausalReadback.lean` | `d7b71cf56aad` | same | same |
  | `OIBridge/C3Necessity.lean` | `b6be90e0404e` | same | same |
  | `OIBridge/FiniteEntropy.lean` | `52fbd89d5e04` | same | same |
  | `OIBridge/CanonicalMeasure.lean` | `183cc42a69c6` | same | same |
  | `ARCB/result.md` | `05e9f35b8573` | same | same |

  `OIBridge/` and `ARCB/` abbreviate the paths in revision 4 §0.1
  (`ARCB/` = `verification/programmes/oi-qm/track-i/arc-b-rooted-classification/`).
  "—" marks a blob that r1–r3 did not record at `c91bf5dd`.
- **PR #919**, merged at `a411bf46`. It changes only
  `papers/Explainer.md`, `.tex` and `.pdf`. Its effect is recorded in §3,
  item (e).
- **Standing of the Explainer (Rc2:N7).** #926 (`50203701`) replaced the
  dated status note at Explainer:3–8 with one line, Explainer:3: "This
  Explainer is retained as a supplementary historical exposition. The
  maintained book and technical papers supersede it as authoritative
  statements of the theory. Where formulations differ, consult those
  sources and their cited verification records."
  - **The Explainer is superseded, and it is not a drafting source for
    the introductory paper.**
  - The Explainer sites cited below (C12, F5, F13, F26) are recorded for
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
- `Main:NNN`, `GR:NNN`, `ch01:NNN`, `ch07:NNN`, `Explainer:NNN`,
  `glossary:NNN`, `Substratum:NNN`, `appendix-b:NNN`, `FULL:NNN` and
  `File:NNN` are lines at `83d1da1b`. A line at the old base is marked
  `@a411`, and one at revision 4's base `@c91`.
- **Line maps** (computed from the hunks of `git diff -U0 a411bf46 83d1da1b`;
  spot-checked by comparing line text at both commits):
  - Main, GR, ch07, appendix-b, glossary, Substratum and `book/README.md`:
    numbering unchanged. Every changed line was replaced one for one;
    Main gains [63] at :899–900.
  - Explainer: lines 3–8 became line 3 (#926). So Explainer:N@a411 is
    Explainer:N−5 for N > 8, e.g. :148 → :143, :378 → :373, :1026 → :1021.
  - ch01: line 83 became three lines (#926). So ch01:N@a411 is ch01:N+2
    for N > 83, e.g. :101 → :103.
  - FULL: +2 for lines 428–6798@a411, +4 for 6799–6896 and +6 from 6897
    (bibliography insertions), e.g. :445 → :447, :5809 → :5811,
    :6659 → :6661.
- Main.md's line numbering is also unchanged between `c91bf5dd` and
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
  document, either by one of the two accepted literature studies (Rv5:15)
  or, from r4, by this audit itself. The latter is marked **FT-r4**, and
  §8 gives each such document's URL, sha256, and the page and quoted
  passage relied on. The rest of this bullet concerns the studies' FT
  sources.
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

**r1–r3** read no external source beyond the presence checks above, and
used no web search.

**r4** read 19 open full-text documents (§8).
- **Where they came from.** arXiv, plus two free-access Cambridge Core
  publisher PDFs.
- **How they were handled.**
  - Each PDF was downloaded into its own empty directory and treated as
    untrusted data.
  - Text was extracted with `pdftotext` 24.02.0.
  - Page numbers are PDF page indices, located by extracting each page
    alone and searching it for the quoted string.
- **How they were found.** By the arXiv API, Crossref records and a few
  web searches (one targeted search per open item).
- **Not retained.** The PDFs and extractions are not kept in the
  repository. Each one is identified by URL and sha256.

**Primary texts that could not be read** (r4). Each one stays NR, and every
conclusion resting on it stays PROVISIONAL.

| Work | Reason |
|---|---|
| Blackwell 1953, Feller 1959, Heller 1965 (*Ann. Math. Stat.*, Project Euclid) | Bot challenge (Incapsula): the request for Blackwell 1953 returned a challenge page, not the PDF; the other two are on the same host and were not attempted |
| Cohen, Iwasa, Rautu, Ruskai, Seneta, Zbăganu 1993 (*LAA*) | Crossref lists an Elsevier open-archive licence, but ScienceDirect returned HTTP 403. A request through the Elsevier API was refused by the session's permission policy, and no other route was tried |
| Rabin 1963, Carlyle 1963 (Elsevier) | ScienceDirect, HTTP 403 |
| van Kampen, *Braz. J. Phys.* 28, 90 (1998) | Bot challenge (SciELO) |
| Anderson 1999 (*MCSS*), Vidyasagar 2011 (*MCSS*), Picci 1978 | Paywall or book chapter; no arXiv version located |
| Paz 1971; Kallenberg; Breuer–Petruccione; Parzen; van Kampen (book); Cover–Thomas | Books |
| Davis 1961 (*Amer. Math. Monthly*) | Paywall (JSTOR) |
| Bennett 1973 (*IBM J. Res. Dev.*) | Paywall; Crossref lists no licence |
| Fine 1982 (*PRL*) | Paywall (APS default licence) |
| König 1916 (*Math. Ann.*) | Paywall (Springer) |

Nothing was done to get around a block.

**Bibliographic details checked against Crossref records (r4, REC).** The
following move from [from memory] or [secondary] to **[REC, Crossref]**:
- Blackwell, *Ann. Math. Stat.* 24 (1953), doi:10.1214/aoms/1177729032;
- Cohen et al., *LAA* 179, 211–235 (1993), doi:10.1016/0024-3795(93)90331-H;
- Feller, *Ann. Math. Stat.* 30, 1252–1253 (1959),
  doi:10.1214/aoms/1177706110;
- Heller, *Ann. Math. Stat.* 36, 1286–1291 (1965),
  doi:10.1214/aoms/1177700000;
- König, *Math. Ann.* 77, 453–465 (1916), doi:10.1007/bf01456961.

Their content is still unread.

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

**Correctness and originality are separate axes.** The five classes are
about originality only. A kernel or prose proof establishes correctness for
the stated definitions; it is not evidence of originality. A KNOWN or
REFRAMING class is not evidence against correctness.

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
| #925 (merged `8b5e8681`) | Main precision follow-ups (and Methodology's mirror of F10) | F3 changed (remark open); F4 changed (title open); F5 fixed at Main:608, :690; F6, F10, F12 fixed; F23's Main pointers fixed (§4) |
| #926 (merged `c1cade86`) | canonical-measure scope at GR:20(ii), ch07:46, ch01:77–85 and FULL; Explainer status note; Explainer C₄ and two-branch status | F23 fixed; Explainer standing (§0.1) |
| #927 (merged `03eb1395`) | characterization scope (GR, glossary, appendix-b, Substratum, Explainer, ch04, Main:680); BLP cited and backflow one-way; ch01 author-year citations; README H-scramble | F21, F22, F24, F25, F27 fixed; C12 sites changed; **F28 introduced** (§4) |
| #928 (merged `83d1da1b`) | a CI workflow only | none |

**What #925–#927 changed, by commit** (read from each merge's
second-parent history; every changed line was read at both ends):

- **#925**
  - `607c23e7` and `4c5012ab`: the $Q_{\mathrm{fb}}$ class stated as the
    kernel defines it, at Main:16 and :530 (F3).
  - `d2a7c4ff`: Main:28 states the identification at its proved scope
    (F4).
  - `6909c672`: Main:608 and :690, the characterization's status at its
    proved strength (F5).
  - `510df1d1` and `ec6beb61`: Main:580(2) and :588 carry the joint-law
    scope and the proof route (F6).
  - `0a172590`, with `eb3e5fc5` for Methodology: double stochasticity
    attributed to counting (F10).
  - `22625cd2`: Main:167's unused hypothesis removed (F12).
  - `a04443bf`: Main:86 and :522 point at §1.2's Remark (F23).
- **#926**
  - `231ca420` and `ebfc12ad`: canonical-measure scope at GR:20(ii),
    ch07:46, ch01:77–85 and their FULL mirrors (F23).
  - `50203701`: Explainer:3 status line.
  - `4af081c0`: Explainer §5.3.
- **#927**
  - `01f343aa`, with `6250782a` for GR:567: GR in Main's proved scope
    (F24).
  - `01159740`: glossary:39 and FULL:6661 (F25).
  - `58dd3448`: BLP cited at Main:332 [63], and backflow stated one-way at
    Main:149, Explainer:143, ch01:103 and FULL:447 (F21, F22).
  - `1d4a1bad`: ch01's author-year citations (F21).
  - `5d58e753`: `book/README.md:64` carries H-scramble (F27).
  - `6250782a`: C2 placed outside the equivalence at Main:680, GR:567 and
    ch04:180. The same commit adds "[4]" to Main:332's ancilla clause
    (**F28**).
  - `ddbcd800` and `04aeef14`: appendix-b B.7.6 on accessible horizons.
    The same pair gives the characterization shorthand at Substratum:111,
    :126 and Explainer:353, :373, :1021.

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

**The characterization theorem at `83d1da1b`** (it was not changed by
#922; #925 and #927 changed its status wording).

- Main §3.4 is still headed "The Characterization Theorem: Necessity of
  the Conditions" (Main:409). Its theorem (Main:516–522) is still
  (ii) non-Markovianity ⟺ (iii) a per-horizon realization with
  (C1), (C3) and (C4).
- **Main:608** (#925, `6909c672`) now reads: "Both directions are proved
  here in prose and neither is formalized in the kernel". It continues:
  "since (C4) coincides with (ii) in every faithful realization …, what
  (ii) ⟹ (iii) adds to (ii) is the existence of a realization, and
  (iii) ⟹ (ii) is the readback lemma". This is C12's reduction, stated in
  place.
- **Main:680** (#927, `6250782a`): "(ii) ⟺ (iii), with (iii) carrying (C1),
  (C3) and (C4) and (C2) outside it, both directions in-house".
- **Main:212** is unchanged: "the equivalence (ii) ⟺ (iii) is proved
  in-house". "In-house" now agrees with Main:608's "proved here in prose".
- **The same characterization appears at:**
  - Explainer:353, :373 and :1021;
  - Substratum:111 and :126;
  - appendix-b:22, :406 and :454–455 (B.7.6, displayed at :455), with
    their FULL mirrors (FULL:5811, :6195, :6243–6244).
  - #927 restated all of these on accessible horizons, with C2 outside
    the equivalence.
- In these sites it is the (ii) ⟺ (iii) form, with (C4) on the right.
  It is not the bare form that Main:597 displays as false. So it does not
  contradict Main, but C12 below still applies to it.
- **The two sites that diverged from Main are fixed by #927:**
  - **GR:20 (F24; `01f343aa`).** It now reads "obtaining exactly when every
    finite accessible horizon containing a memory witness admits a
    deterministic realization with C1, C3 and C4 … both directions proved
    in prose, C2 lying outside that equivalence". The same change is at
    GR:567 (`6250782a`).
  - **glossary:39 / FULL:6661 (F25; `01159740`).** It now reads "The
    per-horizon characterization of the memory-bearing sector … *C2* lies
    outside the equivalence".
- **Still open at Explainer:373** (F5, F26): "Both directions are the
  foundational paper's own theorems" and "The old three-way biconditional
  is retired". #927 (`04aeef14`) added only "accessible" there.

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
- **Claim (restated)**, against `83d1da1b` (r1–r3: `a411bf46`);
- **Internal status**: kernel, prose or probe. This is the correctness
  axis, and it is independent of the class;
- **Literature**: each comparator, tagged FT, FT-r4, REC or NR, with its
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
    - r4: Bennett 1973 is paywalled, and the primary HMM texts could not
      be obtained (§0.2).
    - The open surveys of realization theory were read **[FT-r4]**:
      Monràs–Winter §2 and Ohta §1 (§8). They concern stationary process
      laws and their positive (Markov) realizations, and say nothing on
      history tapes or reversibility.
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
    outsourcing): **[NR]**. r4: Fine 1982 is paywalled and Kallenberg is
    a book (§0.2).
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
- **Literature.**
  - **Strasberg–García Díaz, arXiv:1905.03018v2 [FT-r4]** (§8), p. 2.
    - Eq. (3) writes the every-step projectively measured record of a
      system coupled to an environment as
      $p(\mathbf r_n \mid \mathcal A_0) = \mathrm{tr}_{SE}\{\mathcal P_{r_n}\mathcal U_{n,n-1}\cdots\mathcal P_{r_1}\mathcal U_{1,0}\mathcal A_0\rho_{SE}(t_0)\}$.
    - It says of it: "Albeit condition (2) is in general not fulfilled for
      quantum dynamics, the joint probability distribution (1) is
      nevertheless a well-defined object in quantum mechanics."
    - Condition (2) is Kolmogorov consistency under omitting a
      measurement (Def. II.1).
    - That is C3's statement, with general system observables and
      preparations: the every-step record is a probability law, whether or
      not it is consistent.
  - Milz et al., arXiv:1907.05807v3 **[FT-r4]**, uses the same object
    (Eq. (9) and Def. 1, p. 5). Its question, like Strasberg's, is
    consistency across subsets of measured times (C4 below).
  - The published venues (PRX 10, 041049 (2020); PRA 100, 022120 (2019))
    are still **[from memory]**; the arXiv versions were read.
- **Class: REFRAMING (FT-r4).** It is Born-rule normalization in OI class
  language. The attribution now has a full-text comparator, and the
  PROVISIONAL mark is removed. No novelty is claimed.
- **Correctness:** kernel. **Originality:** none claimed.
- **Needed.** Cite Strasberg–García Díaz Eq. (3), or any textbook
  statement of the Born rule for sequential measurements.

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
  - **Milz, Egloff, Taranto, Theurer, Plenio, Smirne and Huelga,
    arXiv:1907.05807v3 [FT-r4]** (§8).
    - Def. 1 (p. 5): a "K-classical process" is one whose every-step
      projective records satisfy the Kolmogorov consistency conditions,
      Eq. (9), across subsets of times.
    - Thm 4 (p. 21): the statistics of an underlying system–environment
      evolution are K-classical iff there exists a NDGD evolution
      reproducing them. Its proof inserts dephasing maps into the given
      dilation ("for every K-classical process there is an NDGD dilation
      that reproduces it correctly").
  - **Strasberg–García Díaz, arXiv:1905.03018v2 [FT-r4].**
    - Def. II.1 (p. 2): "classical" is the same consistency condition.
    - Thms III.1–III.2: classicality and incoherence, for Markovian
      invertible dynamics.
  - **Comparison with C4.** Both papers ask when every-step projective
    records are consistent with *omitting* intermediate measurements. OI's
    $Q_{\mathrm{fb}}$ measures at every step and never meets that
    question. Neither paper states, or implies, that every law on
    $V^{K+1}$ is the every-step fixed-basis record of a *finite unitary*
    (S ⊆ $Q_{\mathrm{fb}}$):
    - Milz Thm 4 takes a quantum dilation as given;
    - Strasberg's Eq. (3) is the C3 direction.
  - **Not read: the realization theorem for quantum combs**
    (Chiribella, D'Ariano and Perinotti 2008, **[from memory]**). It would
    give every comb a realization by isometries with finite memory. With
    diagonal combs, it may give S ⊆ Q in a form close to $Q_{\mathrm{fb}}$.
- **Class: PARTLY KNOWN.**
  - Every direction is known, or an elementary strengthening of a known
    construction.
  - The multi-time, fixed-basis-collapse three-way identification was
    not located as a packaged statement (LC §8, T5 (c)).
  - "Not located" now rests on FT for Barandes, Calvo, EG, Doukas, Milz
    2020 and Strasberg 2019.
  - **The packaging-novelty part stays PROVISIONAL**, now on one named
    unread area, the comb-realization literature. It remains partly
    verified.
- **Correctness:** kernel, all six directions. **Originality:** packaging
  only, unverified.
- **Withdrawn sub-claim, C4-old.** "Finite-horizon non-Markovianity ⟺ ∃
  finite reversible hidden-state realization" as the paper's core
  (Main:97–99 @c91, v4 F1).
  - **WITHDRAWN**: removed by #922, and Main:597–598 shows it false.
  - It must not appear in the introductory paper, in either the display
  or the prose.
- **Needed.**
  - Read the comb-realization theorem (§5, item P2.1).
  - Describe Milz 2020 and Strasberg 2019 in related work as studying the
    Kolmogorov consistency of projective records, which is a different
    question.
  - The paper's novelty statement should claim only a self-contained,
    machine-checked packaging of elementary facts (§7).

### C5 — one-step uniform-prior marginal (Main:270–272)

- **Claim.** A one-step doubly stochastic matrix is a uniform-prior
  marginal of a bijection: exactly when its entries are rational, and
  approximately otherwise.
- **Internal.** Probes only; there is no OIBridge declaration.
  - Main:62 now attributes the forward direction (marginal ⇒ doubly
    stochastic) to counting: "since each set $\{x_j\} \times
    \mathcal{C}_H$ has exactly $|\mathcal{C}_H|$ preimages" (#925,
    `0a172590`; v4 F10 fixed).
  - Main:272 still reads "Any marginal of a bijection with uniform prior
    is a doubly stochastic matrix, and by Birkhoff–von Neumann is a convex
    combination of permutation matrices". That uses Birkhoff–von Neumann
    correctly, for the converse.
  - GO's own proof confirms that the forward direction is marginalization
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
      theorem (1916) **[NR; record REC, Crossref]** splits that into $d$
      perfect matchings, so $T$ is a mixture of permutations with weights
      in $\tfrac1d\mathbb{Z}$.
    - **The construction is FT-r4.** Johnson, Dulmage and Mendelsohn,
      *Canad. Math. Bull.* 3, 237 (1960), p. 4 of the PDF (journal
      p. 240) (§8), give Birkhoff's algorithm: "Let c1 be the smallest
      (possibly unique) non-zero element of A. There exists a diagonal of
      non-zeros of which c1 is the least. Let A1 be the permutation matrix
      with ones on this diagonal, and let A⁽¹⁾ = A − c1A1. Repeating this
      process …".
      - Each weight $c_i$ is an entry of a matrix obtained from $A$ by
        subtracting multiples of 0/1 matrices. So a rational $A$ gives
        rational weights.
      - **That inference is this audit's.** JDM does not state it.
    - Isbell, *Canad. Math. Bull.* 5, 1 (1962), p. 3 **[FT-r4]**, is about
      rational *entries*: "Peck and Rattray added the restriction that
      a_ij takes only rational values [3]; then it does follow
      trivially". But that concerns the *existence* of a decomposition
      for infinite matrices, not rational weights.
  - HHO Prop. 1 (p. 3) **[FT]**: the state-conversion version.
  - SCH Thm 1 (p. 5) **[FT]**: adjacent (uniform coarse graining of a
    bistochastic matrix).
- **Class: PARTLY KNOWN.** The closure statement is KNOWN.
  - The exact rational clause is an elementary addition.
  - Its construction is located in full text (JDM 1960).
  - An explicit statement that the weights are rational was not located.
  - That part stays **PROVISIONAL**, since König 1916 and the
    combinatorics texts are NR. It remains partly verified.
- **Needed.** Cite GO Lemma 6 and footnote 8, and JDM 1960 for the
  algorithm, adding the one-line rationality observation as the paper's
  own. If a statement is wanted, read König 1916 or a combinatorics text
  (§5, P3.5). F10 is fixed.

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
  - **RHP 2014, Main's [5], arXiv:1405.0303v2 [FT-r4]** (§8): the
    classical divisibility form, in a source Main already cites.
    - Def. 2.2 (p. 7): "A stochastic process … for which the associates
      transition matrices satisfy Eqs. (11), (12) and (13) is called
      divisible". These are stochastic intermediate maps that compose.
    - Theorem 2.4 (p. 8): "Let T(x2,t2|x1,t1) be the transition matrices
      of some stochastic process. Then such a process is divisible if and
      only if the L1-norm does not increase when T(x2,t2|x1,t1) is applied
      to every vector v(x)". The "only if" proof uses only (11) and (12),
      that is, nonnegativity and normalization.
    - p. 9: "Pmin(fail) increases monotonically with time for a
      divisible process".
    - C8's step is this "only if" direction, applied to
      $v = \delta_a - \delta_b$ pushed to time $s$. If
      $\Gamma_n = T\,\Gamma_s$ with $T$ stochastic, then
      $\lVert\Gamma_n(a)-\Gamma_n(b)\rVert_1 \le \lVert\Gamma_s(a)-\Gamma_s(b)\rVert_1 < 2$,
      against identity return.
    - Dating: v1 May 2014; v2, read here, dated 24 Aug 2014. Prior.
  - **Other FT-r4 sources for the same direction** (§8). None is needed
    beyond RHP 2014 and BD:
    - Wißmann–Vacchini–Breuer 2015 Thm 2 (p. 4), Helstrom-matrix form for
      bijective maps;
    - Bylicka–Johansson–Acín (Main [9]), abstract (p. 1), CP-divisibility
      with an ancilla, bijective maps;
    - Pleasance 2026 Prop. 2 (p. 8), later than BD and RHP.
  - **Older classical sources, named in FT sources [secondary]**
    (Rv5:8). r4 could not read either (§0.2); their bibliographic details
    are now [REC, Crossref].
    - BD's semiclassical case rests on the Blackwell–Sherman–Stein
      theorem: BD p. 4, its ref. [3], Blackwell, "Equivalent Comparisons
      of Experiments", *Ann. Math. Stat.* 24 (1953). The text is behind
      Project Euclid's bot challenge.
    - PI p. 14 credits the classical "divisible iff information
      monotonically decreasing" result to Cohen, Iwasa, Rautu, Ruskai,
      Seneta and Zbăganu, "Relative entropy under mappings by stochastic
      matrices", *LAA* 179, 211–235 (1993) (PI ref. [26]), "presented in
      Buscemi and Datta". ScienceDirect returned 403.
    - BD does not cite Cohen et al. (BD v3 reference list, read FT-r4).
    - Total-variation contraction under a stochastic matrix is older
      still.
    - So RHP 2014 and BD are prior results *in the divisibility form*,
      not the origin of the contraction property.
  - **Main already cites the mechanism (§A.19; Rv5:7).**
    - Main:121 attributes "P-divisibility ⟹ $d(p(t),q(t))$
      non-increasing" to [4, 5]: RHP, PRL 105, 050403 (2010) and RHP,
      Rep. Prog. Phys. 77, 094001 (2014).
    - [5] carries the classical statement (Thm 2.4 above). [4] is quantum:
      an ancilla-entanglement witness and a Choi-norm criterion, read
      FT-r4.
    - Main:121's "The converse is *false*" concerns pair distances
      $d(p, q)$. RHP's iff is over *all* vectors $v$, so the two are
      consistent.
    - Main:149 cites [4, 5], Bylicka–Johansson–Acín [9] and Milz et al.
      [10]. Main:194 cites [4, 5, 7, 9].
    - Breuer–Laine–Piilo 2009 is Main [63] from #927 (F21 fixed).
- **Class: KNOWN (FT).** It is the data-processing (contraction) property
  of stochastic maps, used once. Its classical divisibility form is RHP
  2014 Thm 2.4 ("only if") and BD Prop. 1's data-processing direction.
  The older classical sources are [secondary].
- **Correctness:** kernel. **Originality:** none.
- **Needed.**
  - Cite RHP 2014 Thm 2.4 and BD Prop. 1 for the divisibility form, and
    DO3 v3 Prop. 1 as concurrent.
  - Main:121 needs no new classical source, since [5] is one. Adding BD
    there is optional.
  - In Main, cite [22] by version (LC §9 item 3).
  - Cohen et al. 1993 and Blackwell 1953 are optional. If cited, they
    must first be read (§5, P1.3).

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
    `book/*.md` at `83d1da1b` finds no statement of it (no
    `finiteRootedRealizable`, `rootedMap`, `RootedClassification` or
    "rooted classification" hit; the same at `a411bf46`).
  - **Correct, not thereby original.** The kernel establishes that the
    theorem is correct, for the stated definitions. Whether it is original
    is the separate, unverified question below.
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
  - **§5 P1 reading in r4** (§8). Each P1 item is reported as read,
    unread with reason, or read only in secondary form.
    - **P1.1, HMM and stochastic realization theory.**
      - The primary texts are **unread**: Heller 1965 (bot challenge),
        Anderson 1999, Vidyasagar 2011 and Picci 1978 (paywall or book;
        §0.2).
      - The open surveys were read **[FT-r4]**: Monràs–Winter,
        arXiv:1412.3634v1, §2, and Ohta, arXiv:2008.11487v1, §1.
      - *Object.* Monràs–Winter p. 2: "We will be concerned with
        stochastic processes defined on sequences of random variables over
        M, i.e., stationary probability measures over M∗."
      - *Realizations.* $p(u) = \pi^\top D^{(u)}\tau$ (Def. 1, p. 2). A
        positive realization has nonnegative $M^{(u)}$ with
        $\sum_u M^{(u)}$ stochastic and π stationary (Def. 5, p. 5).
      - *Central theorem.* Dharmadhikari's cone criterion (Thm 6, p. 5):
        "an equivalent positive realization exists if and only if there
        is a convex pointed polyhedral cone C …".
      - *Comparison.* C8-R's object is a root-conditioned, non-stationary
        family of one-time maps. Its generator is a single bijection with
        a hidden prior independent of the root, and its condition is
        periodicity. The surveyed theory concerns stationary word laws,
        Markov generators and the cone condition. Neither survey states a
        deterministic, reversible or periodic special case, or a
        shared-prior rooted class.
    - **P1.2, automata and symbolic dynamics.**
      - The primary texts are **unread**: Rabin 1963 and Carlyle 1963
        (HTTP 403), Paz 1971 (book), Davis 1961 (paywall).
      - Antonelli, Dal Lago and Pistone, arXiv:2409.11999v1, §2.1, p. 3
        **[FT-r4]**, quotes Davis 1961 **[secondary]**: "Consider a box
        whose consecutive input values are selected randomly and
        independently by a sampling device of some kind. … Its behavior is
        exactly that of a Markov chain. More remarkably, however, is that
        the converse is also true."
      - *Comparison.* Davis's converse is the random-mapping
        representation of a homogeneous *Markov* chain, with fresh
        randomness at every step. C8-R draws its randomness once and has
        no input.
      - The two classes are different. $(\tfrac12 J)^t$ is Markov and not
        periodic. A periodic family rooted at 1 with $\Gamma_1$ not a
        permutation is realizable, hence P-indivisible by C8-D, hence not
        Markov.
      - Symbolic-dynamics codings of finite permutations: no open source
        was located in one targeted search.
    - **P1.3, divisibility, contraction and revivals.** Read
      **[FT-r4]**: RHP 2010, RHP 2014, BJA, BLP 2009,
      Wißmann–Vacchini–Breuer, Milz–Modi 2021, Pleasance 2026, Vacchini
      et al. 2011, and Figueroa-Romero et al. 2019 (cited parts).
      - None of them considers the realizability of rooted families by
        finite deterministic systems.
      - "Recurren…" and "Poincar…" occur in none of RHP 2014,
        Milz–Modi, Pleasance, WVB, BD, Milz 2019 or Milz 2020.
      - Still unread: BD's forward citations; Breuer–Petruccione (book).
  - **Still unread, the decisive areas:** P1.1 and P1.2 in primary text,
    and BD's forward citations.
- **Class: NOVEL-CANDIDATE — novelty unverified** (owner's standing
  direction), for the two-sided characterization only. It is a candidate,
  not an established novelty claim, and it carries **no priority
  sentence**. Within it:
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
  3. The search that found nothing was keyword-based. r4 reached the
     three areas where an equivalent statement would most likely appear
     (realization theory, automata and symbolic dynamics) only through
     open surveys. Their primary texts are unread, and a remark or
     exercise in Heller, Picci or Paz is not excluded.
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
    and only after the remaining P1 items of §5 are read.
  - The P1.3 reading favours the candidate in that nothing was found. By
    §A.31 that favourable branch gets the most skepticism. P1.3 is not
    where a realization statement would sit, so its silence carries
    little weight.
- **Needed.** Before any sentence that presents it as new:
  - P1.1 and P1.2 in primary text;
  - BD's forward citations (§5).
  - Optionally, kernelize the full-support separation (v4 K1).

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
  - (B)'s mechanism is BD Prop. 1 **[FT]** and RHP 2014 Thm 2.4 "only
    if" **[FT-r4]** (C8), both prior. DO3 v3 Prop. 1 is concurrent.
  - Stochastic-inverse rigidity is C7's sources **[FT]**.
  - Analogues: BCN Ex. 2 (p. 7) **[FT]**, the qubit-unitary analogue;
    BI Thm 2.1 and Eq. (5) **[FT]**, unitary semigroups; PI Fig. 4
    (p. 6) **[FT]**, two configurations and continuous paths.
  - **r4, one targeted search** (the P1.3 sources above):
    - Figueroa-Romero, Modi and Pollock 2019, p. 5 **[FT-r4]**, has only a
      qualitative expectation, for the quantum case: a typical process
      "could be highly non-Markovian. Indeed, we expect this to be the
      case, since the finite-dimensional ES space will have a finite
      recurrence time."
    - No recurrence-forced divisibility dichotomy was found, classical or
      quantum.
  - Not located: the support lemma B4 as a stated result, and the
    combined statement.
- **Class: PARTLY KNOWN.** Every ingredient is published (FT). The
  combination was not located, and it is elementary.
  - It is not NOVEL-CANDIDATE: the class reflects that its content is
    the conjunction of three FT-located facts and finite recurrence.
  - The combined-statement search inherits C8-R's uncovered areas: P1.1
    and P1.2 in primary text. **PROVISIONAL** for the "not located" part.
- **Needed.**
  - v4 §4.6's hedged wording, now citing RHP 2014 Thm 2.4 and BD Prop. 1
    (with DO3 v3 as concurrent) for (B) and EG Prop. 12 for (A).
  - v4 K2 (B3, B4, A1 in the kernel) if the display is to be cited as
    an equivalence.

### C9 — readback ⇒ CMI ≥ p₀δ²/ln 2 (Main:167–170)

- **Claim.** A next-step TV gap δ between two histories, each of
  probability at least $p_0$, gives
  $I(X_{<k}; X_{k+1} \mid X_k) \ge p_0\delta^2/\ln 2$.
- **Internal.** Probes only. Main:167 now states only the hypothesis it
  uses: "Suppose the visible process has a gap at order $k$ …, as (C4)
  asserts" (#925, `22625cd2`; v4 F12 fixed).
- **Literature.** Pinsker's inequality **[NR]**: no textbook was read in
  either study (LC §10), nor in r4 (Cover–Thomas is a book).
- **Class: REFRAMING, PROVISIONAL** (a direct Pinsker application;
  attribution only, §0.4).
- **Needed.** A textbook citation (Cover–Thomas).

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
  - Main:580(2) now carries both caveats (#925, `510df1d1`, `ec6beb61`):
    "proved: clauses (a)–(c) of the theorem below proved in the kernel for
    a joint law of history, present and hidden state, with the reading of
    a realization's time-$t$ law as that joint law not formalized; …
    both directions using the vanishing criterion for conditional mutual
    information, which is not formalized".
  - Main:588 carries the joint-law scope beside the kernel pointer.
  - v4 F6 is **fixed** (§4).
- **Literature.** None needed. The statement is clause (a) read in both
  directions.
- **Class: REFRAMING.**
- **Needed.** In the paper, carry Main:99's (or Main:580(2)'s) directional
  form with its two caveats.

### C11 — C3 necessity (`c3_necessity`, `card_hidden_ge_two_pow_Istar`, `C3Necessity:80, 117`)

- **Internal.** Kernel. It is the same DPI at the whole-future readout,
  then exponentiated.
- **Literature.** SC Thm 5 **[FT]**: same type, different statement. DPI
  text **[NR]**.
- **Class: REFRAMING, PROVISIONAL** (attribution only, as C10).
- **Needed.** As for C10.

### C12 — the "characterization theorem" (ii) ⟺ (iii) (Main:212, :516–522, :608, :680; Explainer:353, :373, :1021; Substratum:111, :126; appendix-b:22, :406, :454–455; FULL:5811, :6195, :6243–6244)

- **Claim (restated).** (ii) non-Markovian at an accessible order ⟺
  (iii) a per-witness-horizon realization exists with (C1), (C3) and
  (C4).
  - (ii) ⇒ (iii) is C1′/C1 plus inheritance.
  - (iii) ⇒ (ii) is C9.
  - Main:596 says (C4) coincides with (ii) in any faithful realization,
    which `primitive_probes.py` confirms exhaustively at three small
    sizes. So the equivalence reduces to "(ii) ⟺ (ii) holds and a
    realization exists".
  - Main:608 now states this reduction in place (#925, `6909c672`; §1).
- **Internal.** Prose and probes. Neither direction is kernel-checked
  as stated. Main:608 now says so: "Both directions are proved here in
  prose and neither is formalized in the kernel" (v4 F5, fixed there).
- **Literature.** None needed.
- **Class: REFRAMING.** It is near-definitional.
  - Main:99 names $S \iff D$ and the universal statement as the
    paper's core.
    - What #922 removed was the bare form (C4-old).
    - (ii) ⟺ (iii) was not the displayed core at `c91bf5dd` either
      (Rv5:13).
  - glossary:39 / FULL:6661 now states the per-horizon characterization
    with C2 outside the equivalence, and no longer calls it the central
    result (#927, `01159740`; F25 fixed).
  - It must not be offered as a "characterization of non-Markovianity"
    in the introductory paper.
- **Sites and their wording** (verified at `83d1da1b`):
  - Status wording:
    - Main:608, "proved here in prose and neither is formalized in the
      kernel" (fixed);
    - Main:680, "both directions in-house", now with C2 outside (changed,
      #927 `6250782a`);
    - Main:212, "proved in-house" (unchanged).
    - "In-house" at :212 and :680 agrees with :608.
    - **Explainer:373** still reads "Both directions are the
      foundational paper's own theorems", next to the self-narration "The
      old three-way biconditional is retired" (§A.30, §A.33). This is
      open: F5 at that site, and F26.
  - **Characterization as stated** (all on accessible horizons, C2
    outside):
    - Main:516;
    - Explainer:353, :1021;
    - Substratum:111;
    - appendix-b:22, :406, :454–455 (displayed at :455);
    - FULL:5811, :6195, :6243–6244.
    - #927 (`ddbcd800`, `04aeef14`) changed all of the book and
      Substratum sites, and the Explainer ones.
  - **Substratum:126** still attaches "accessible non-Markovianity ⟺
    C1/C3/C4 realization per accessible horizon" to "the universal
    hidden-memory theorem". That conflates C12 with C10-B and is open.
  - **No longer divergent from Main:** GR:20 and GR:567 (F24 fixed), and
    glossary:39 / FULL:6661 (F25 fixed); see §1.
- **Correctness:** prose proof, both directions; neither kernel-checked.
  **Originality:** none claimed.
- **Needed.**
  - The paper should either omit C12, or state it with the reduction of
    Main:596/:608 beside it.
  - Still correction targets for the owner: Explainer:373 (F5, F26) and
    Substratum:126 (the conflation).

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
    byte-identical at `a411bf46`. At `83d1da1b`, the sites below have the
    same text: ch07, ch09, ch18, ch19 and GR are unchanged at these lines,
    and the FULL lines are renumbered (§0.1). All of them carry the
    conditional form:
    - ch07:12;
    - ch09:127, ch18:148, ch19:72, glossary:113;
    - FULL:1889, :2015–2038, :2607, :4968, :5248, :6735;
    - GR:611.
  - **The summary site without the condition is fixed** (Rv5:16; F27).
    `book/README.md:64` now reads "the Page curve from nested trace-out,
    conditional on the scrambling condition H-scramble" (#927,
    `5d58e753`).
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
    Explainer:96, :417 and :1003, matching Main:86.
  - So the measure is a third input whenever a general prior is
    allowed, which reinforces R15.
- **Mirrors now scoped** (Rv5:9; F23 fixed by #926, `231ca420`, with
  `ebfc12ad`):
  - GR:20 item (ii): "under the canonical measure of [Main] Lemma 3 — the
    invariant measure selected by maximal entropy, which the physical
    realization uses — the emergent description is uniquely determined by
    the partition";
  - ch07:46: "under the canonical measure of Lemma 3 of Chapter 1, the
    emergent description is uniquely determined by the partition
    geometry";
  - ch01:77–85, with the Lemma at ch01:79 "*Under the canonical measure
    of Lemma 3, …*" and the three statements about the measure at
    ch01:85;
  - their FULL mirrors (FULL:421–429, :1923).
  - Main:86's pointer now names "§1.2, Remark on the measure as a
    realization datum" (#925, `a04443bf`), and so does Main:522.
- **Still at the title level** (F4, open): Main:2 reads "The Equivalence
  of Quantum Mechanics and Embedded Observation". Main:28 is now scoped:
  the observable laws "are identified exactly with fixed-basis unitary
  Born representations (§3.4); whether the full operational theory of
  quantum mechanics follows is the separate completion question stated
  there".
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
  - **Prior source, the same process: RHP 2014, Main's own [5],
    arXiv:1405.0303v2, §2.2, Eq. (15), p. 7 [FT-r4]** (§8).
    - It gives three binary times with
      $P(x_3,x_2,x_1) = \tfrac14(\delta_{x_3,0}\delta_{x_2,0}\delta_{x_1,1} + \delta_{x_3,0}\delta_{x_2,1}\delta_{x_1,0} + \delta_{x_3,1}\delta_{x_2,0}\delta_{x_1,0} + \delta_{x_3,1}\delta_{x_2,1}\delta_{x_1,1})$.
      That is, $x_1, x_2$ are independent and uniform, and
      $x_3 = 1 \oplus x_1 \oplus x_2$.
    - It states: "the transition matrices can be written as
      T(x3,t3|x2,t2) = 1/2 … and similarly T(x2,t2|x1,t1) = T(x3,t3|x1,t1)
      = 1/2. Hence the conditions (11), (12) and (13) are clearly
      fulfilled". It notes P(1,t3|0,t2;0,t1) = 1 and P(1,t3|0,t2;1,t1) =
      0, so the process is non-Markovian.
    - Relabelling $x_3 \mapsto 1 - x_3$, and setting
      $(X_0, X_1, X_2) = (x_1, x_2, x_3)$, gives Main:606's process with
      $X_0$ uniform. All two-time kernels are $\tfrac12 J$, and
      $I(X_0; X_2 \mid X_1) = 1$ bit.
    - RHP introduces it "As an example (see [4, 6])", that is, Parzen,
      *Stochastic Processes*, and van Kampen, *Stochastic Processes in
      Physics and Chemistry* **[secondary]**. It lists further examples
      in [9–13], among them Lévy, *C. R. Acad. Sci. Paris* 228, 2004
      (1949), and Feller, *Ann. Math. Statist.* 30, 1252 (1959), ref. [10]
      on p. 46 **[secondary]**.
  - **The four-time parity version, prior [FT-r4]:**
    - Capela, Céleri, Modi and Chaves, arXiv:1910.04236v1 (9 Oct 2019),
      §IV.A, p. 6: "x1 = 0, 1 with probability 1/2. Let x_j = y_j for
      j = 2, 3, where y_j are random bits. Finally, we let x4 = x1 + y2 +
      y3 (here we have modular addition). … the process is divisible".
      PRR 2, 013350 (2020) **[secondary, via Milz–Modi ref. 37]**.
    - Milz and Modi, PRX Quantum review, arXiv:2012.01894v2, p. 14,
      repeat it, "which comes from Ref. [37]".
  - **Not a source for it:** Milz, Kim, Pollock and Modi 2019 (Main [10]),
    read in full **[FT-r4]**.
    - p. 1: "In the classical domain, it is well-known that divisibility
      does not imply that a stochastic process is Markovian". No classical
      example or citation is given for that sentence.
    - p. 3: its own example is a quantum swap collision model with a
      correlated environment.
  - **Class: KNOWN (FT-r4).** The PROVISIONAL mark is removed. The prior
    source is RHP 2014 Eq. (15), the same process up to relabelling the
    final bit, in a work Main already cites.
    - DO3 v3 App. A remains concurrent.
    - The repository's 2026-08-11 example is later than RHP 2014 and
      Capela et al.
    - **Unverified:** who stated it first (RHP points to the Parzen and
      van Kampen books, both unread), and what Feller 1959 contains
      (Project Euclid, bot challenge; §0.2).
  - **Needed.** Cite [5] Eq. (15) at Main:606 and in the paper, with DO3
    v3 App. A as concurrent. Make no claim about who stated it first.
- **v4 §4.5's branch-(B) witness** ($\Gamma_1 = \tfrac12 J$) is the same
  matrix, used for a different point.

***

## 4. Fidelity notes: status at `83d1da1b`

The F-identifiers are kept. Nothing is renumbered, and no retired number
is reused (§A.30).

**Status words:**
- **fixed**: every listed site now reads correctly;
- **changed**: a site was edited, but part of the finding remains;
- **open**: no listed site was changed.

Every site was read at both `a411bf46` and `83d1da1b`. The fixing commits
are on the second-parent history of the merges in §1.

| ID | Finding | Status at `83d1da1b` | Commit(s) |
|---|---|---|---|
| F1 | Main:97–99 displayed the bare false form as the core | fixed (r2) | #922 |
| F2 | Main:500 pointed at `S_imp_D` for the independent-prior form | fixed (r2) | #922 |
| F2b | `Equivalence:346–348` and Main:532 called the carrier "response-table" | fixed (r2) | #922 |
| F3 | $Q_{\mathrm{fb}}$ wording; `e^{-iĤ}` remark contentless | **changed.** Main:16 and :530 now state projective measurement in one fixed basis at every step, from a diagonal initial state. The remark "$U_\varphi = e^{-i\hat H}$ for a Hermitian $\hat H$, giving a fixed autonomous generator at integer times" is still at Main:532: **open** | `607c23e7`, `4c5012ab`, `ec6beb61` (#925) |
| F4 | title (Main:2) and Main:28 beyond Main:22, :534, :542 | **changed.** Main:28 now stops at "fixed-basis unitary Born representations", with the completion question separate. The title "The Equivalence of Quantum Mechanics and Embedded Observation" (Main:2) is unchanged: **open** | `d2a7c4ff` (#925) |
| F5 | Main:608 "Both directions … are theorems", Main:690 "necessary and sufficient"; also Main:212, :680, Explainer:373@83d1 | **changed.** Main:608 now says "proved here in prose and neither is formalized in the kernel". Main:690 now says "a characterization (ii) ⟺ (iii) whose conditions are diagnostics of a realization". Main:212 and :680 keep "in-house", which agrees with :608 (Main:680 also gained the C2 scope, `6250782a`). Explainer:373 "Both directions are the foundational paper's own theorems" is **open** | `6909c672` (#925); `6250782a` (#927) |
| F6 | Main:580(2) "proved" for the biconditional | **fixed.** Main:580(2) and :588 carry the joint-law scope and the CMI-criterion caveat | `510df1d1`, `ec6beb61` (#925) |
| F7 | Main:580(4) "proved unconditionally", no kernel anchor | **open** (Main:580(4) unchanged) | — |
| F8 | missing citations | **changed.** BLP 2009 is now Main [63] (Main:332, :900). Every other item below is still not cited | `58dd3448` (#927) |
| F9 | ch07 §7.6 overclaims and mirrors | fixed (r2) | #920 |
| F10 | Main:62 credits Birkhoff–von Neumann with double stochasticity | **fixed.** Main:62 now credits counting ("each set $\{x_j\}\times\mathcal{C}_H$ has exactly $|\mathcal{C}_H|$ preimages"), mirrored in Methodology | `0a172590`, `eb3e5fc5` (#925) |
| F11 | kernel route vs Main:20 and :139; EquivalenceChain header | header fixed (r2); Main:20 and :139 unchanged, and the C8 citation guidance stands | #922 |
| F12 | Main:167's (C1)–(C3) unused | **fixed.** "Suppose the visible process has a gap at order $k$ …, as (C4) asserts" | `22625cd2` (#925) |
| F13 | the `≤ n³` import | **kept separate** (§6). Sites unchanged; the Explainer ones are renumbered :282, :1015 | — |
| F14 | Main:210, :212, :218, Calvo as a dimension extension | **open** | — |
| F15 | Main:210 "non-trivial only in the P-indivisible regime"; Main:212 PI scope | **open** | — |
| F16 | Main:212's Doukas scope (iii), "finite-environment bound"; [22] by version | **open** | — |
| F17 | Main:212 swaps [11] and [12] | **open** | — |
| F18 | Main:220 "The Born rule is the equilibrium distribution …" unsourced | **open** | — |
| F19 | Main [24] (Main:822) stale | **open** | — |
| F20 | Main:636 reader-instruction phrase | **open** | — |
| F21 | BLP misattributed or uncited (Main:332; book) | **fixed.** Main:332 cites "[63]"; `book/bibliography.md:17` has the entry. ch01 now uses author-year citations (:32 "Bao, Carroll, and Singh 2017"; :103 "Breuer, Laine, and Piilo (2009)"), mirrored at FULL:447 | `58dd3448`, `1d4a1bad` (#927) |
| F22 | "P-indivisibility equivalent to backflow" (Main:149; Explainer:148@a411; ch01:101@a411; FULL:445@a411) | **fixed.** Main:149: "information backflow witnesses divisibility failure [4, 5], and divisibility can fail without it". Explainer:143: "backflow certifies P-indivisibility, though a P-indivisible process need not show it". ch01:103 / FULL:447: "The signature runs one way". Adjudicated against BLP 2009 in r4 (below) | `58dd3448` (#927) |
| F23 | partition-relativity without the canonical-measure scope (GR:20(ii), ch07:46, ch01:79, :83, FULL; Main:86 pointer) | **fixed** ((e) above) | `231ca420`, `ebfc12ad` (#926); `a04443bf` (#925) |
| F24 | GR:20 "C1–C4 necessary as well as sufficient" | **fixed.** GR:20 and :567 state C1, C3, C4 per accessible horizon, both directions proved in prose, C2 outside | `01f343aa`, `6250782a` (#927) |
| F25 | glossary:39 / FULL:6659@a411 "central result … C1–C4" | **fixed.** glossary:39 / FULL:6661: "The per-horizon characterization of the memory-bearing sector … *C2* lies outside the equivalence" | `01159740` (#927) |
| F26 | Explainer:378@a411 (now :373) "The old three-way biconditional is retired" | **open.** #927 (`04aeef14`) added only "accessible" | — |
| F27 | `book/README.md:64` Page curve without H-scramble | **fixed** ("conditional on the scrambling condition H-scramble") | `5d58e753` (#927) |
| F28 | Main:332 cites [4] for the ancilla-assisted distinguishability characterization | **open; new in r4.** Introduced by #927; a correction PR is being prepared (below) | introduced `6250782a` (#927) |

**F8. What Main does not cite** (grep of `papers/*.md` and `book/*.md`
at `83d1da1b`; the same result as at `8dc36d55` apart from BLP):
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
- Capela et al.; Strasberg–García Díaz; Milz et al. 2020; Johnson–Dulmage–
  Mendelsohn (the FT-r4 sources of §3);
- **Cited since r3:** Breuer–Laine–Piilo 2009, as Main [63]. The book
  bibliography has it at `book/bibliography.md:17` and FULL:6801.
  Elsewhere BLP is named at Explainer:143, :619, ch01:103 / FULL:447,
  ch18:78 / FULL:4898 and appendix-b:96 / FULL:5885.

Main names "the exact Koopman operator" (Main:728, :742) as an object but
cites no Koopman source for the permutation unitary.

**F8. What Main does cite** (§A.19; Rv5:7). The paper's task for these
is to describe them correctly, not to add them.
- **For the C8 mechanism:**
  - Main:121 cites Rivas–Huelga–Plenio [4] (PRL 105, 050403, 2010) and
    [5] (Rep. Prog. Phys. 77, 094001, 2014) for "P-divisibility ⟹
    $d(p(t),q(t))$ non-increasing".
    - r4 read both **[FT-r4]**. [5] §2.3 Thm 2.4 is the classical
      statement with proof (C8).
  - Main:149 cites [4, 5], Bylicka–Johansson–Acín [9] (PRL 118, 120501,
    2017) and Milz et al. [10] (PRL 123, 040401, 2019). Both were read
    **[FT-r4]**.
  - Main:194 cites [4, 5, 7, 9].
  - Main:332 cites BLP [63] and RHP 2010 [4]; see F28.
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

**F14–F20, carried from LC §9** (verified there in full text). Their Main
lines are unchanged at `83d1da1b`. None is applied here; each is for the
owner under §A.25.

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

**F21–F27, the r2 findings, as fixed.** The wording at `a411bf46` is in
`AUDIT-r3.md` §4. Two points are kept here:
- **F22 adjudicated (r4).** BLP 2009 (arXiv:0908.0238v2) **[FT-r4]**
  states only one direction:
  - p. 2: "we have σ ≤ 0 for all quantum processes for which the
    divisibility property (9) holds";
  - p. 1: backflow implies "the dynamical map of non-Markovian processes
    must necessarily be non-divisible".
  - It claims no equivalence. So the sites F22 listed at `a411bf46`
    misattributed an equivalence to BLP.
  - The #927 wording agrees with BLP's text (Main:149, Explainer:143,
    ch01:103, FULL:447).
  - BD Prop. 1's equivalence (FT) holds for the guessing probability over
    general ensembles, not for a single distinguishability pair-norm. The
    paper must still state which notion it uses.
- **appendix-b:96 / FULL:5885** name the BLP "*information backflow*
  signature" as sufficient evidence, consistent with Main:332. Unchanged.

**New fidelity finding in r4** (verified at `83d1da1b`; for the owner,
not applied):

- **F28.** Main:332 reads: "By the Breuer-Laine-Piilo criterion [63],
  CP-indivisibility is witnessed by non-monotonic distinguishability, but
  the correct witness is the *ancilla-assisted* one [4]: monotonicity of
  system-plus-ancilla distinguishability characterizes CP-divisibility".
  - The "[4]" was added by `6250782a` (#927). At `a411bf46` the clause was
    uncited ("the ANCILLA-ASSISTED one:").
  - **What [4] gives instead.** RHP 2010 (arXiv:0911.4270v2) **[FT-r4]**
    gives two things:
    - an ancilla *entanglement* witness, p. 2, Fig. 1: "the entanglement
      between system and ancilla is no longer constrained to decrease
      monotonically";
    - a Choi-norm criterion, p. 4: "E(t+ε,t) is CP if and only if
      f_NCP(t+ε,t) = 1".
    It does not give a distinguishability characterization.
  - **Where that characterization is.** Bylicka, Johansson and Acín
    (Main [9]; arXiv:1603.04288v2, abstract, p. 1) **[FT-r4]**: "a
    bijective dynamical map is completely-positive-divisible if and only
    if a monotonic non-increase of distinguishability is observed for two
    equiprobable states of the evolving system and an ancilla". For
    general (non-bijective) maps it is Buscemi–Datta.
  - **Correction.** Cite [9] (and BD) for the distinguishability clause,
    keeping [4] only for the entanglement or Choi-norm witness if wanted.
    A correction PR is being prepared, per the coordinator. Until it lands
    the site stands as quoted.
  - **Mirrors.** appendix-b:96 / FULL:5885 cite only "[Main §3.4]" for
    "completely witnessed by ancilla-assisted distinguishability", so they
    carry no misattribution of their own. They follow Main's.

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

Status after r4. Each item is read FT-r4, read only in secondary form, or
unread with the reason given in §0.2.

1. **HMM and stochastic realization theory. Primary texts: unread.**
   - Heller, "On Stochastic Processes Derived From Markov Chains",
     *Ann. Math. Stat.* 36, 1286–1291 (1965) **[REC, Crossref]**:
     Project Euclid, bot challenge.
   - Anderson 1999 (MCSS, "The realization problem for hidden Markov
     models") **[from memory]**: paywall.
   - Vidyasagar 2011 (MCSS): paywall; no arXiv version located.
   - Picci 1978: book chapter.
   - Read in secondary form **[FT-r4]**: Monràs–Winter 2014 §2 and Ohta
     2020 §1 (C8-R).
   - Why it still matters: this is the field whose subject is which
     processes are functions of finite (deterministic or Markov) systems.
     A characterization of rooted families of *deterministic* periodic
     systems with a random initial state is most likely to sit here as a
     lemma or remark. The surveys show the field's central problems are
     posed for other objects, but cannot exclude such a remark.
2. **Automata and symbolic dynamics. Primary texts: unread.**
   - Rabin 1963 and Carlyle 1963 (Elsevier): HTTP 403.
   - Paz 1971: book.
   - Davis 1961, "Markov chains as random input automata", *Amer. Math.
     Monthly* 68, 264–267 **[secondary, via Antonelli et al. 2024]**:
     paywall.
   - Factors and codings of finite permutations and periodic processes in
     ergodic theory: no open source was located in one targeted search.
   - Read in secondary form **[FT-r4]**: Antonelli, Dal Lago and Pistone
     2024, §2.1 (C8-R).
   - Why it still matters: C8-R's sufficiency is a deterministic-machine,
     random-state realization. EG Props. 16–18 already give it over one
     period, and the construction may be older still.
3. **Divisibility, contraction and revival literature. Read FT-r4,
   except as listed.**
   - **Read:** RHP 2010 [4], RHP 2014 [5], Bylicka–Johansson–Acín [9],
     Breuer–Laine–Piilo 2009 [63], Wißmann–Vacchini–Breuer 2015, the
     Milz–Modi PRX Quantum review (arXiv:2012.01894v2), Pleasance 2026
     (arXiv:2607.07332v2), Vacchini et al. 2011, and Figueroa-Romero et
     al. 2019 (cited parts).
   - **Unread:**
     - forward citations of BD (not indexed by INSPIRE; Semantic Scholar
       and OpenAlex returned 429 in LC; no open citation index was used in
       r4);
     - Breuer–Petruccione on finite-environment revivals (book);
     - **classical contraction sources, now optional** (C8; Rv5:8):
       - Cohen, Iwasa, Rautu, Ruskai, Seneta and Zbăganu, *LAA* 179,
         211–235 (1993) **[secondary, via PI p. 14; REC, Crossref]**:
         ScienceDirect 403.
       - Blackwell, *Ann. Math. Stat.* 24 (1953) **[secondary, via BD
         p. 4; REC, Crossref]**: Project Euclid, bot challenge.
   - **Optional:** the embedding and divisibility of stochastic matrices,
     Elfving 1937 and Kingman 1962 **[from memory]**.
   - Why: a recurrence-forced indivisibility statement for finite
     systems (C8-D) would most likely be stated here, as would a
     permutation-or-indivisible dichotomy. None was found in what was
     read (C8-D).

**P2 — gates C4's packaging and the related-work section**

1. **The quantum-comb realization theorem** (Chiribella, D'Ariano and
   Perinotti, PRL 2008 **[from memory]**). It is the one named unread
   area for C4's packaging (C4).
   - Read in r4 and now FT-r4: Milz et al. (arXiv:1907.05807v3) and
     Strasberg–García Díaz (arXiv:1905.03018v2). Their published venues
     are still [from memory].
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
   attempt).** r4: Bennett is paywalled (Crossref lists no licence), Fine
   is paywalled (APS), Kallenberg is a book; Koopman was not attempted.
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
5. **König 1916** (*Math. Ann.* 77, 453–465; **[REC, Crossref]**;
   paywall), or a combinatorics text, for an explicit statement of C5's
   rational Birkhoff decomposition (Rv5:11). The construction is now FT-r4
   (JDM 1960; C5).
6. **The XOR example: satisfied for attribution** (Rv5:1). The prior
   source is RHP 2014 Eq. (15) **[FT-r4]**. Milz et al. 2019 (Main [10])
   was read and is not a source for it. Optional, for who stated it first:
   - Feller 1959 (*Ann. Math. Stat.* 30, 1252–1253, **[REC, Crossref]**;
     Project Euclid, bot challenge);
   - Lévy 1949 **[secondary, via RHP 2014]**;
   - the Parzen and van Kampen books **[secondary, via RHP 2014]**;
   - van Kampen, *Braz. J. Phys.* 28, 90 (1998), and Hänggi–Thomas
     1977/1982 **[secondary, via Vacchini et al. 2011, refs. 25, 27,
     28]** (SciELO bot challenge for van Kampen 1998).

**P4 — gates the black-hole paragraph, if there is one**

1. **Popescu–Short–Winter 2006, Hayden–Preskill 2007** **[from memory]**,
   and a decoupling reference, for C16c and C16-S. Also #917's landed
   records, `verification/programmes/black-hole-information/` (landed at
   `ebf98d83`, unchanged in r4's reading), for C16-S.
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
- **Sites at `83d1da1b`.** The `n^3` occurrences are at the same lines as
  at `a411bf46` and `c91bf5dd`. #925 and #927 changed Main:690 elsewhere in
  the line and left its "≤ n³" in place.
  - Main:204, 210, 350, 504, 506, 514, 636, 690, 716;
  - Explainer:282 (which also restricts the class to P-indivisible
    processes) and Explainer:1015 (@a411 :287, :1020). #919 and #926
    merged without touching either line, and the review of r1 confirmed
    both.
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
- The PROVISIONAL marks follow the uniform rule of §0.4. They cover:
  - the "not located" remainders of C1, C1′, C4, C5 and C8-D;
  - the REFRAMING classes resting on unread textbook facts (C9, C10,
    C11, C16e);
  - C13 and C14;
  - C16c.
- **r4 removed two PROVISIONAL marks** on first-hand full text (§8):
  - the XOR example (RHP 2014 Eq. (15));
  - C3 (Strasberg–García Díaz Eq. (3)).
- **r4 narrowed two** that remain partly verified:
  - C4: the comb-realization literature is now the one unread area;
  - C5: the construction is in JDM 1960, and an explicit statement is
    still unlocated.

**Classes after both studies and r4:**
- KNOWN: C2, C6, C7, C8, C16a, C16b; the XOR example (FT-r4);
- PARTLY KNOWN: C1, C1′, C4, C5, C8-D, C16c;
- REFRAMING: C3 (FT-r4), C9, C10, C10-B, C11, C12, C13, C14, C16e;
- WITHDRAWN: C4-old, C16d;
- not classified: C15, C16-S, (e);
- NOVEL-CANDIDATE: only C8-R, as the two-sided characterization, with
  novelty unverified. Its sufficiency half is a located construction
  (EG Props. 16–18) and its necessity half is folklore. It is a
  candidate, not an established novelty claim.

**Correct versus original, for the items the paper would state.** The
first column is what is established about correctness (§0.3, "Internal").
The second is the originality class.

| Item | Correctness (this repository) | Originality (this audit) |
|---|---|---|
| C4, $S \iff D \iff Q_{\mathrm{fb}}$ | kernel, all six directions | PARTLY KNOWN; packaging part PROVISIONAL |
| C1′, independent prior | prose and probes; not formalized | PARTLY KNOWN; packaging part PROVISIONAL |
| C5, rational one-step clause | probes only | PARTLY KNOWN; explicit statement PROVISIONAL |
| C8, identity return ⇒ indivisible | kernel | KNOWN |
| C8-D, the dichotomy | kernel theorems plus prose steps B3, B4, A1 | PARTLY KNOWN; combination PROVISIONAL |
| C8-R, `PPer` = realizable class | kernel (finite visible) | NOVEL-CANDIDATE, unverified; no priority sentence |
| C10, hidden-memory floor | kernel, for the joint law; time-$t$ reading not formalized | REFRAMING (DPI), attribution PROVISIONAL |
| C12, (ii) ⟺ (iii) | prose, both directions; not formalized | REFRAMING (near-definitional) |
| XOR example | probe | KNOWN (FT-r4) |

**A technical perspective / pedagogical review, not a research
article.** The literature check lowered the estimate, as v4 §8 predicted
it could:
- C6 moved from "pending" to KNOWN (B26, SCH), C8 to KNOWN (BD), and C5
  to PARTLY KNOWN (GO);
- r2 narrowed C8-R to the biconditional;
- r4 found the XOR example in RHP 2014 (Main's own [5]) and a second
  classical source for C8 (RHP 2014 Thm 2.4).
- Nothing moved up.

**Novelty statement that should survive scrutiny** (v4's text, corrected
in r1, r2 and r4):

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
> stochastic maps in its divisibility form (Rivas, Huelga and Plenio 2014,
> Thm 2.4; Buscemi and Datta 2016), assembled from machine-checked
> theorems and elementary steps that are
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

- **The rooted classification is a novelty candidate, not an established
  novelty claim.**
  - The sentence above says what is proved, and that is a correctness
    claim. It makes no originality claim.
  - **No priority sentence** may be attached to it until §5 P1.1 and P1.2
    are read in primary text and BD's forward citations are checked. P1.3
    is read (r4).
  - No "we have not located" clause is needed. If one is wanted, it is
    admissible only in the form "we have not located a statement of this
    characterization in the divisibility, process-tensor or
    stochastic–quantum literature". That is the scope actually read. It
    must not name realization theory or automata.
- **The divisibility credit** rests on two FT sources:
  - RHP 2014 Thm 2.4, its "only if" direction (FT-r4; Main's [5]);
  - BD Prop. 1 (FT).
  Cohen et al. 1993 and Blackwell 1953 stay [secondary] (their
  bibliographic details are REC) and are not needed for the sentence
  (Rc2:N2, superseded).
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
- added in r4 (FT-r4):
  - RHP 2014 (Eq. (15) for the XOR example; Thm 2.4 for the divisibility
    form);
  - Capela et al. 2019/2020 (the four-time parity example);
  - Strasberg–García Díaz 2019 (C3; described as studying the Kolmogorov
    consistency of projective records) and Milz et al. 2020 (likewise);
  - Johnson–Dulmage–Mendelsohn 1960 (C5's algorithm);
  - BLP 2009, described as a one-way witness (F22), and BJA [9] for the
    ancilla distinguishability characterization (F28);
- Calvo, correctly described (F14);
- Pimenta, with its two-configuration scope (F15);
- Main's existing [4, 5, 9, 10], described consistently with Main:121
  (F22);
- pending:
  - Hardy 2004, Rutten, 't Hooft, Spekkens;
  - the comb-realization theorem (C4);
  - König 1916 (C5, an explicit statement only);
  - the P1.1 and P1.2 primary texts and BD's forward citations (C8-R,
    C8-D);
  - optional: Cohen et al. and Blackwell; Feller 1959 and the textbook
    sources of the XOR example.

If black holes appear: Page 2013 Eq. (8), Page 2005 Eqs. (5)–(10),
Penington 2019 §2, and Page 1993 Eq. (10). The README omission (F27) is
fixed.

***

## 8. Full-text sources read in r4

Each document was downloaded once, into its own empty directory, and
treated as untrusted data. The PDFs are not retained in the repository.

Columns:
- **Key**: the label used in this audit.
- **URL**: what was fetched.
- **sha256**: the downloaded file.
- **Passages relied on**: PDF page index, then the passage.

| Key | URL | sha256 | Passages relied on |
|---|---|---|---|
| RHP 2014 (Main [5]) | https://arxiv.org/pdf/1405.0303v2 | `51befd88fd235f9f6fdb1ff7b3f3da5b3c2d3f0d464a35ccc70606ac2c7f59e2` | p. 7: Def. 2.2; Eq. (15) and "Hence the conditions (11), (12) and (13) are clearly fulfilled"; refs. [4, 6] cited there. p. 8: Thm 2.4 and its "only if" proof. p. 9: "Pmin(fail) increases monotonically with time for a divisible process". p. 46: refs. [9, 10] (Lévy 1949, Feller 1959) |
| Capela et al. 2019 | https://arxiv.org/pdf/1910.04236v1 | `3f20ea0ce9cca8aa25dc3d6c5befafb60285cf2cfbc91e22db92fa23242f49a2` | p. 6, §IV.A: "x4 = x1 + y2 + y3 (here we have modular addition) … the process is divisible" |
| Milz–Modi 2021 | https://arxiv.org/pdf/2012.01894v2 | `d070eb1b8cc2e4e8d39614a530bf69c1adb998ff756ddb7a6f9d3facbba2520a` | p. 14: the four-time parity process, "which comes from Ref. [37]"; p. 64: ref. [37] |
| Milz et al. 2019 (Main [10]) | https://arxiv.org/pdf/1901.05223v2 | `1f48d0d8adba5003a585d91506a16df8a300d1a1ec2a34ef66146c1347658f6e` | p. 1: "In the classical domain, it is well-known that divisibility does not imply …". p. 3: the swap collision example. Whole text checked for "XOR", "⊕" and "Feller" (none) |
| BLP 2009 (Main [63]) | https://arxiv.org/pdf/0908.0238v2 | `9e05b98a5b6a902be4fa8d4d2662b7e9b7592d150ddef6bf74a8d6e9f9bf4553` | p. 1: "must necessarily be non-divisible". p. 2: "σ ≤ 0 for all quantum processes for which the divisibility property (9) holds" |
| RHP 2010 (Main [4]) | https://arxiv.org/pdf/0911.4270v2 | `3eb009a0537ba42ac174b87070f4e49e97461c52562a1b02b1e73335d731a0a0` | p. 2, Fig. 1: the ancilla entanglement witness. p. 4: "E(t+ε,t) is CP if and only if f_NCP(t+ε,t) = 1" |
| BJA (Main [9]) | https://arxiv.org/pdf/1603.04288v2 | `50bafba8c193f2fc91cd88bc4c803b24a700cfc5c6d0b0d61404249dcd3218f0` | p. 1, abstract: the bijective CP-divisibility ⟺ ancilla-distinguishability equivalence |
| Wißmann–Vacchini–Breuer 2015 | https://arxiv.org/pdf/1507.08867v1 | `717aa51b6f64a32b3f0a13626769d479242b90c6b323438f7e488636c052c793` | p. 4, Thm 2: "If the dynamical maps defining a process Φ are bijective, then Φ is Markovian if and only if it is P-divisible" |
| Pleasance 2026 | https://arxiv.org/pdf/2607.07332v2 | `b85ff7cf58efe60a440b9f6fd6c16dcb95b69650e1ecbb164f51d7c4ccfd85b7` | p. 8, Prop. 2 (P-divisible ⇒ Kolmogorov distance non-increasing) |
| Vacchini et al. 2011 | https://arxiv.org/pdf/1106.0138v1 | `7b671d559d40f0d64fc565fbb003bfd946dc27051a6519701dfa8ed1e8b690ff` | pp. 3–4, §III; refs. [25–29] |
| Figueroa-Romero et al. 2019 | https://arxiv.org/pdf/1802.10344v5 | `a0d576651fcfdeefd7ced4a4131147554758458c3cc7df7e0585a6b9c10a62f2` | p. 5, §4.2: "we expect this to be the case, since the finite-dimensional ES space will have a finite recurrence time" |
| BD v3 | https://arxiv.org/pdf/1408.7062v3 | `14666c8ca8797aad2664f01bf64e61b8eb4247f8448335a49a46cfa2b9e85c3a` | reference list only: [3] = Blackwell 1953; no Cohen et al. |
| Milz et al. 2020 | https://arxiv.org/pdf/1907.05807v3 | `54308a84227b781bd77ed6a702072c976a2a053a0f8afe950b5c0bf759f594be` | p. 5: Eq. (9) and Def. 1. p. 21: Thm 4 and its proof |
| Strasberg–García Díaz 2019 | https://arxiv.org/pdf/1905.03018v2 | `9afb61e472e16efb95c7e7a1c0fbafa8674b7b21a08beb556f146a02cfb4484d` | p. 2: Def. II.1; Eq. (3) and "is nevertheless a well-defined object in quantum mechanics" |
| Monràs–Winter 2014 | https://arxiv.org/pdf/1412.3634v1 | `91f89afbcd332bc3563ffb95ed5d64df2576740a412be1a13e36778b3c2510ff` | p. 2: Def. 1 and "stationary probability measures over M∗". p. 5: Def. 5, Thm 6 |
| Ohta 2020 | https://arxiv.org/pdf/2008.11487v1 | `0b9f6979f847a02424db0e5cb825cd2f797721b92c3c1521b7c9e01531f08c12` | p. 1, §1 (the field's lineage) |
| Antonelli, Dal Lago, Pistone 2024 | https://arxiv.org/pdf/2409.11999 (v1) | `55e1feab1f7afa28d97e8f02f9b05b508a3b0ebbf678dad4017557a4f5ec197c` | p. 3, §2.1: Davis 1961 quoted; Carlyle and Rabin |
| Johnson–Dulmage–Mendelsohn 1960 | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/92A57E6F8FF8838AF9806D4A3D6C1BA4/S0008439500050578a.pdf/on-an-algorithm-of-g-birkhoff-concerning-doubly-stochastic-matrices.pdf | `1b3a7ee0794a80834737a58c781f42785c29780ba5559d14b1e3719e76c6b9c3` | p. 4 (journal p. 240): the Birkhoff construction in the Theorem's proof |
| Isbell 1962 | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/25F8DC72F465C77891D64ECED7ED99C0/S0008439500050992a.pdf/infinite-doubly-stochastic-matrices.pdf | `3000a8d5ec3a1dbbff49f4ce469307000bdb5b6efa13ff22d283dc23f899bcbc` | p. 3: Prop. 2 and the Peck–Rattray remark |

**Failed retrievals.** These are challenge pages, not sources, recorded
only as evidence of the attempt:
- Blackwell 1953 via `projecteuclid.org/journalArticle/Download?urlId=10.1214%2Faoms%2F1177729032`
  returned an Incapsula page (sha256 `c17f8405…8059`);
- van Kampen 1998 via `scielo.br` returned a bot-shield page (sha256
  `aae8f165…45ac`);
- Cohen et al. 1993 via ScienceDirect returned HTTP 403.
