# Full-corpus scientific audit of #918 at `60c976fe`: consolidated report

The full-corpus scientific audit of `papers/Introduction.md` at `60c976fe` (r31, with main `0d917665` merged in) was
done by three independent auditors, each covering one slice:
- `FULL-CORPUS-AUDIT-60c976fe-A.md`: abstract, §1–§2. ACCEPT WITH CHANGES.
- `FULL-CORPUS-AUDIT-60c976fe-B.md`: §3 and Appendix A. BLOCK.
- `FULL-CORPUS-AUDIT-60c976fe-C.md`: §4–§6 and references. BLOCK.

An independent verifier then checked every blocking finding adversarially against its sources
(`FULL-CORPUS-AUDIT-60c976fe-VERIFY.md`). The same verifier mapped every required item (R-01…R-40) and every owner
decision (OD-1…OD-15) of the #942 audit (`audit/intro-corpus-20261026` at `16fc745d`, `FINDINGS.md`) to the
current text. This report consolidates the four documents.

**Verdict: #918 does not meet the scientific-accuracy gate at `60c976fe`.** The blockers are of two kinds:
- the #942 audit's required Introduction-side changes. The owner dispositioned these on 2026-10-27, but they were
  never applied: r16 applied that audit's §D items and Track C's items, not its R-items;
- findings first raised in this audit.

Several corrections also have to land in the corpus before or with #918, under the owner's rule that the Introduction
must not become more accurate than the framework it cites while known errors there stay uncorrected.

## 1. Publication blockers in the Introduction's text (all confirmed by the verifier)

### False or overclaiming as written

| Id | Site | Defect | Source |
|---|---|---|---|
| R-01 / OD-9 | L298, L300, L308 | The Page-curve conditional is stated without saying that GR Theorem A.8 counts configuration initial states with an aligned bipartition, where H-scramble fails, so as stated it has no instance. BHb C2's bound and the fact that the Page value enters only through H-scramble are missing. | GR:817–841; BHb C1, C2, C6 |
| R-03 / OD-7 | L41, L75, L120 | "Exact probe" is defined as exhaustive and exact. The cited Pinsker probe accumulates in floating point, and no cited probe is exhaustive over a class. | `c4_backflow_probes.py` |
| A-B2 | L116 | The memory Corollary's converse omits the common endpoint. The Markov law $X_{t+1}=X_t$ is a counterexample. | Main:99 |
| R-32 / A-B3 | L188 | "No card arrangement violates a Bell inequality" is unrestricted. Setting-dependent reversible dynamics realizes PR-box behaviour. | Main:356, :360 |
| B-B5 | L250 | Bell's bound is stated without measurement independence. | Main §3.3(b), (iv) |
| R-13 / OD-5 / A-B6 | L162, App. A L340 | The routed-readback gloss is the storage-time reading. The cited declaration formalizes the seed-conditioned reading, and the two predicates are incomparable. | PhysicalC4Discharge:27–35; PhysicalC4StorageReadback §CS5, :256, :689 |
| A-B5 | L37 | §2.5 is called discriminating content, which contradicts L158. | Main:141 |
| A-B4 | L186 | Anticorrelated cards: $\Gamma_1$ is used where §2.5's definition requires a root-independent hidden prior. The conclusion holds after re-coordinatizing the hidden card, but the sentence conflicts with L130. | Introduction L130, L136 |
| R-14 | L288 | [Pag93] does not discuss the information problem. The correct source is Page, PRL 71, 3743 (1993). | Pag93, read first-hand |
| R-17 | L244 | [Mon08] is cited for explicit tasks it does not contain. It does report Hardy's result. | Mon08, read first-hand |

### Required content missing under the owner's decisions

| Id | Site | Required |
|---|---|---|
| R-06 / OD-2 | abstract L17, L226, L304, L312 | Report what the kernel establishes for the formalized substratum. Its stated access supplies no quarter phase. With a phase intervention assumed, it supplies no continuously tunable state mixing. Adding that control gives exact finite operational QM. State the converse: Theorem 4 classifies the completions and does not derive QM. Add the declarations to Appendix A. |
| R-07 + R-40 + O-12 / OD-3 | §3.4 heading and body, abstract | Add the ε-realization results with their scope after SC-1: proved on paper, in exact arithmetic, with the finite-$b$ bound open. |
| OD-15 | `papers/introduction_repro/` | Regenerate the retained axiom report with the new declarations: R-06's, and `routedAtStorage_forces_indivisible_somewhere`. |

### Lesser required items

These are not false as written, but are required by the #942 audit or confirmed here.
- **R-items not applied:** R-11 (L37/L39, where the proofs are), R-16 (RHP14 only-if half), R-27 (L316, §3's
  paper-only results), R-28 (L230 heading), R-10 stage 1 (infinite-dimensional extension).
- **R-items partly applied:** R-02 (L200, the proved direction), R-04 (the "minimal model" label), R-05 (L308), R-15
  (Doukas), R-18 (Bar26/Sch21), R-21 (arbitrary bijections in the toy model), R-30 (L29), R-36 (L116, which is A-B2).
- **New findings confirmed in part:**
  - B-B4: L256 omits the one-step own-wing hypothesis, though L252's definition mitigates the omission.
  - B-B8: L214 leaves Theorem 4's complex-matrix kinematics implicit.
  - B-O6: L214's closure rule admits only a deterministic follow-on operation.

## 2. Corpus corrections that must land before or with #918

None of these has a PR. #961 (SC-29) and #968 (SC-33) exist and should land with #918.

| Unit | Sites | Why it is a dependency |
|---|---|---|
| PR-G | Main §2.3 (:137–:139): the rooted overlap-plus-return theorem and routed readback in both readings, with kernel anchors. The census families for recurrence horizon, physical C4 discharge and physical C4 round 2 move from `kernel-only` to `current`. The Introduction's Appendix A identifiers become resolvable by the census tool. | Main understates the kernel that the Introduction cites. The census resolves none of the Introduction's 29 identifiers. |
| PR-E | GR App. A.8–A.9 (:817–:841); book ch07 §7.6, ch19:72 and :334, appendix-a G11 (:111) and :102, with their FULL mirrors | The corrected Introduction would otherwise be more accurate than GR (R-01). |
| PR-A (part) | GR:344, GR:573; ch07:177 and FULL:2056; Explainer:543, :551, :579 | These state the open coupling step G3 unconditionally, against GR:356 and the Introduction's §4. |
| PR-F (part) | Main:170 ("Certified exactly" for a floating-point probe); Main:178 and ch01:273 ("minimal") | R-03 and R-04. |
| Card-Bell | book ch01:286 and FULL:630 | R-32. |
| Main:465 | The contrapositive is stated with $I^*$ where only $M_k$ is bounded. | The Introduction's L122 is correct; Main is not. |
| Main §4.5 | The Pauli-twirl classical-memory decomposition is cited to it at L204, but it is not there. | Add it to Main, or stop citing Main for it. The mathematics checks. |
| PR-B CON-15 | A kinematics clause in GR §3.3 and Main §3.4 | Pairs with B-B8. |

Lower priority: SC-19 (Main:72/78, GR:52, "(C3) follows from (C4)"). It is not false, but its reason is
misattributed.

## 3. Already corrected, or explicitly qualified in the text

- **Applied or superseded:** R-08 (SC-2 form), R-12, R-19, R-20, R-22, R-23, R-24, R-26, R-29, R-31, R-35, R-37
  (except for A-B5), R-38, R-39 (except for B-B4 and B-B5), OD-1, OD-6, OD-12.
- **Obsolete:** R-25 and R-33, whose text no longer exists, and R-34's phrase.
- **Recorded as numerically correct** by auditors A and C, and by the verifier where checked: the card and four-bit
  examples, the different-deck instance, the 1,376 of 40,320 count and the related counts, the secret-sharing floor,
  and the 122-digit dimensional identity.

## 4. Findings not about the Introduction

These are recorded for the gate (#946) and the research backlog (#970), and do not block #918:
- GR:366 and ch07:193: the convention-factor range;
- GR Theorem A.5/A.7: the coupling chain and the product step;
- book ch07:110 and ch19:72: "resolves";
- the assumption-watch marker from A-B4: whether a hidden prior is "shared and independent" depends on how the hidden
  sector is coordinatized.

## 5. What the corrections do not change

None of the required changes alters the framework's scientific status. They do four things:
- add hypotheses the sources already carry;
- report kernel results that exist, with their scope;
- correct citations;
- bring evidence classes into line with what was run.

Theorem 1, Theorem 2, Theorem 3, Theorem 4 and the recurrence Corollary keep their statements and proof strengths.
