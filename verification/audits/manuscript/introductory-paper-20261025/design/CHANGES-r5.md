# Introduction r5 (design): changes from r4

The baseline is r4 (`S/paper/draft/Introduction-r4.md`, sha256 `5f9fdcc5…68f6`), which is accepted. These changes
apply the owner's r5 authorization of 2026-10-26, the applications audit (`S/paper/apps/AUDIT.md`), and R11
FINDINGS as amended by REVIEW.md. This is a design: no paper text is written yet.

## 1. Structure

| r4 | r5 | Why |
|---|---|---|
| §1 The central idea | §1, with §1.2 rebuilt around the three questions | Owner's frame (Q1/Q2/Q3) |
| §§2–3 | §§2–3, verbatim, with one sentence added in §2.2 (N-LIT1, 't Hooft) | The novelty-of-viewpoint rule |
| §4 Illustrative examples (§4.1–§4.3) | §4 Two examples (§4.1, §4.2); **§4.3 card table → Appendix B, verbatim** | Owner: technical material to an appendix where practical. This saves about 0.9 pp |
| §5 Black-hole information: a bounded application | §5 **Applications and Potential Resolutions**, with §5.2 black holes condensed | Owner's title. Space goes to the cosmological constant |
| — | §5.1 cosmological constant; §5.3 horizon thermodynamics; §5.4 PE-01 (gated); §5.5 further readings | New Q2 content (`CLAIMS-r5.md`) |
| §6 Limitations and open problems | §6 What remains to be proved: §6.1–§6.3 verbatim; §6.4 Born rule (pointer); §6.5 Bell (r4 §6.4(5) verbatim); §6.6 gravitational coupling (new); §6.7 distinguishing experiments (new); §6.8 r4 §6.4 items (1)–(4) | The owner's Q3 list |
| §6.5 What is not claimed | §7.1, items 1–6 carried and items 7–11 added | New scope |
| §7 Conclusion | §7.2, rewritten around Q1–Q3 | New scope |
| Abstract | rewritten | New scope |

## 2. What is cut or compressed

Every cut removes words or moves text. None removes a hypothesis, a status word or a non-claim.

| Item | r4 | r5 | Qualification kept |
|---|---|---|---|
| Card table | r4:145–166 in the main text | Appendix B, verbatim | All of it, including the BBS24 decomposition and the "not quantum" scope (ERRATUM-r4). Non-claim 6 points to it |
| BH setting | r4:172 | first two sentences only; the verification-layer sentence moves into N-BH1/N-BH3 | "exhaustive at small size", "exact algebra", toy-model scope |
| BH access counts | r4:181 | the 1,376/40,320 count, $P_{\rm succ}\ge1/|\mathcal U|$, "sufficient, not necessary" and [Sha79] kept; "sixty non-injective maps" folded into N-BH1 | all |
| H-scramble paragraphs | r4:185–190 | two sentences (N-BH2) | C1, C6(a), C6(b), C6(c) |
| Page time | r4:195–197 | two sentences (N-BH4) | constant coefficient, S_BH ∝ M², constant β, β not derived, the C7 mass dependence. **Dropped:** Page's β ≈ 1.485 value and "β > 1 in the quasi-stationary regime". Both are information, not qualifications |
| Open steps and decoupling | r4:201, :204 | the open list keeps every item; the decoupling paragraph becomes N-BH3's clause, and the R2-3 non-claims move to §7 item 4 | t_evap/τ_B^D ≥ 10⁵⁷ (item F); no claim that information reaches D, that Thm A.7 fails within its scope, or that no other decoupling argument exists |
| §1.2 | r4:28–34 | lead rebuilt (N-INT1); Contributions keeps r4's reviewed sentences, and its BH sentence is extended to all of §5 (N-INT2, which keeps "whose novelty has not been established"); Conventions verbatim | all |
| Realization paragraph | r4:66 | optional trim of the step mechanics only | injectivity via the record; prior independence proved on paper, with exact probes |

## 3. Status changes forced by R11 REVIEW.md

r4 was at the packages' strength (FINDINGS §B: no INTRO-ERROR). REVIEW.md adds three requirements, and r5 meets
each:
- **Sufficiency-form Page-curve statements must carry D-decoupling** (REVIEW §4 O-1). r5 has no sufficiency form.
  N-BH3 lists H-scramble, decoupling and the pointwise step together as the conditions of a conditional result.
- **A.9 covers time averages** (REVIEW §1 C.4, a SITE-ERROR of proof scope). r5 states that the cycle-typicality
  argument gives a time average at a fixed bipartition and that the pointwise curve is open.
- **The name "H-decouple" is a pending owner default.** r5 states the condition in words. The label is used only if
  adopted.
- **The R11 marker texts** change "contradicts" to "claims more than its support" where REVIEW §1 says so (ch07:110,
  ch18:146 s2). The marker list is extended with REVIEW's missed sites M1–M5, M9 and M10 (`DEPENDENCIES-r5.md` §D).

## 4. Theorems 1–4: confirmation that nothing is lost

Each theorem keeps its statement, hypotheses, reference, verification layer and witnesses **verbatim from r4**.

| | Statement and hypotheses | Reference | Layer and witnesses | r5 location |
|---|---|---|---|---|
| Theorem 1 | r4:58–64: every finite alphabet and horizon K; S_K = D_K = Q_K | [Main §3.4]; attribution r4:70 (EGGH26 Props. 13 and 16, LP17, Bar25/23/26, Bar26 Thm 3.3, Sch21, SGD19, Milz20) | K: `finite_horizon_equivalence`, `S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S` (r4:64); prior independence P plus exact probes (r4:66) | §2.2, verbatim |
| Theorem 2 and Corollary | r4:86–94: every faithful realization; (a)–(c); the Corollary's two directions | [Main §3.4]; [Main §1.5]; [CT06] | K for a joint law; time-t identification not machine-checked (r4:92); Corollary P | §2.4, verbatim |
| Theorem 3 and the readback consequence | r4:110–114: bijection of a finite set; overlapping rows of Γ_s; Γ_n = I | [Main §2.3]; [RHP14; BD16]; [Dou26]; [BB12] | K, rooted form; routed form K [Main §1.3, the realization clause of (C4)]; history-level (C4) P | §3.1, verbatim |
| Theorem 4 and independence | r4:214–220: nonempty finite system; conditions (i)–(v); every positive ancilla level | [GR §3.3, Theorem (operational-completion characterization)] | K: ⇒ `physical_of_exactAll`, ⇐ `exactAll_of_physical_general`, "for every nonempty finite carrier" (§A.34); `five_way_minimality`, `oi_alone_not_qm` | §6.1, verbatim |

**Appendix A** is unchanged (r4:264–277), so the identifier check (`identcheck.py`: 28 identifiers, 0 unresolved, 0
line mismatches) carries over to r5. It is re-run on the r5 draft.

## 5. Owner markers

- **Carried:**
  - R11 at the abstract, the BH paragraphs, §7 item 4 and the conclusion;
  - R12 at the Page time;
  - decision 2 / §A.42 at the Conventions;
  - §A.42 retention at the code section.
- **New:**
  - one gate marker at §5.4, "PE-01 not on `main`; cite only after landing, §A.42";
  - VERIFY on [tH14], [EvEMU11], [KP14] and [Vol06] (abstract only), and on [Haw75] (not read).

## 6. Expected checks for the r5 draft

- **Build:** about 13 pp main text; 0 overfull boxes within the approved raw group; 0 missing glyphs.
- **Repository checks:**
  - `voice_check`, `claims_check` and `duplicate_check`. The r5 §6.4 must not repeat r4:78's paragraph.
  - `claims_check` flags any OI-necessity or withdrawn-result phrase without a qualifier in the same paragraph. §5
    has many conditional statements; each must carry its condition in the same paragraph.
- **Identifiers:** `identcheck.py` adapted to r5.
- **Register:** the §A.32/§A.33 grep. Watch especially for "dissolve", "resolve", "predict", "derive" and
  "explains" in §5.
