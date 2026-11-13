# SQ4 — accessible-effect dependency in OA-2 E(b) and OA-3 N4.3

**Standing:** AUTHOR-SIDE / UNVERIFIED paper-only proof-dependency audit (ChatGPT, 2026-11-13). This is **not** an independent review, a counterexample to either theorem, a proof of a native quantum mechanism, or an instruction to revise the manuscripts. Requires a separate non-author review and then an owner decision before any integration. No computation, Lean, experiment, frozen-record change, physical premise, board change, or merge.

**Question (SQ4, #1169 SYNTHESIS-r3 `7):** Do OA-2 E(b) step 4 and OA-3 N4.3 step 4 use a label-free-retention or effect-separation hypothesis that is not stated in their conditional classicality claims? If so, what is the weakest proof obligation, and what does not follow?

**Pinned references.**
- `OA2: `verification/programmes/oi-qm/reconstruction/oa-2-20261112/OA-2-REPORT-r4.md` on `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`. Relevant lines OA2:95–118 (C-PM), 128–157 (E3, G3), 224–227 (closure), 242–278 (Proposition B), 483–504 (H1, H4, SP), 519–546 (E(b)), 577–605 (E1).
- `OA3: `verification/programmes/oi-qm/reconstruction/oa-3-20261112/OA-3-REPORT-r4.md` at the same main snapshot. Relevant OA3:99–126 (C-PM and V-ii effect classes), 405–416 (held-at-use vs ensemble heralds), 460–495 (N4.3, N4.4).
- `P0: `verification/programmes/oi-qm/reconstruction/drafts/rec-1-20261113/REC-1-P0-r3.md` on draft PR #1268 at `2a9f10bab2b7047f8bcc7b03bf8744f22efb066e`. Relevant N5/N6 (C3/C4), N8.2(b), `6 and AW-P0-2 (off main; accepted as O-U by ChatGPT review 5892912758, not established under `A.46 item 7).
- `Synthesis: `#1276 SYNTHESIS-r3.md` at `9eeee392fcfe7489fab3e007d95488ecf4a3eb13`, `6 T5 and `7 SQ4 (off main; model-reviewed ACCEPT 5896999231).
- This audit does not assume the ongoing Claude C3 test's result and does not change its preregistration.

## 1. Exact proof interface

Take the fixed `(S, φ, V, H, μ, A)` and the operational prepare–measure fragment from OA2. Its admissible preparation laws `P` on the de-setting record `Z₀` have support-union `U`; put `W = span(P)`. Let `E_CPM` be the *actual available measurement effects under C-PM*, for all permitted measurement settings, with the preparation's own setting, coin, herald and other label cells excluded as measurement effects.

For the particular ontic model used in E(b), `ι(p) = law_p(Z₀)`. Preparation noncontextuality of that model requires the following implication for **admissible preparations p,q**:

    for all e ∈ E_CPM, e(p) = e(q)  ==>  ι(p) = ι(q).

Call this **SEP(P,E_CPM)**. This is an operational separation requirement, **not** an assertion that every individual singleton indicator of `Z₀` must be a permitted effect. It is sufficient, for example, that an admitted set of effects be informationally complete on the differences of the reachable laws. An even stronger sufficient condition is an effect-evaluation map injective on `W`. Under convex mixture closure, a full-rank effect matrix on `U` suffices.

By contrast **(SP)** in OA2 E(b) says `W = ℝ^U`, a state-span condition. It does not assert that `E_CPM` separates these laws. For a mathematical control, let `U={0,1}`, `P={δ₀,δ₁}` (and mixtures), but give the operational fragment only the null and unit effects. Then `W=ℝ²` satisfies SP, while `δ₀` and `δ₁` are operationally indistinguishable and `ι(δ₀) ≠ ι(δ₁)`. Thus SP alone does **not** validate the preparation-NC step for this chosen `ι`. This abstract control is **not** claimed to satisfy OA2's native physical hypotheses, and the trivial operational fragment has a one-point classical model. It diagnoses a logical nonimplication, **not** a counterexample to the theorem's conclusion.

The stronger hypothesis **(LF)** from P0 N5 ensures that the relevant measurement-stage records are jointly held in cells that do not hold preparation-stage labels. It supplies individual C-PM indicators and therefore SEP for the appropriate label-free ontic variable `Z_e`. LF is a **sufficient repair route**, not yet shown necessary for OA2 E(b) or OA3 N4.3. A different set of label-free effects could be separating without including joint singleton indicators.

## 2. OA-2: theorem E(b), proof steps

- **Step 1 / (H4):** One formally joint held history is assumed. This is a retention hypothesis; it does not itself decide which held cells are forbidden preparation labels under C-PM.
- **Steps 2–3:** The affine translation `Z = Z₀ + h(c)` and the formula `ι(s)=law(Z₀)` reproduce statistics for each *admitted* effect. The source argument remains usable as a conditional construction.
- **Step 4, preparation NC:** “because singleton indicators are available” (OA2:534) requires proof that these indicators are available **as measurement effects under C-PM**, rather than just as mathematical post-processings of a joint held history that includes excluded label cells. OA2:103–111 excludes preparation labels; OA2:486/502's H4 does not explicitly establish label-free access. One can instead prove SEP for `ι` and the actual allowed effects, perhaps without all indicators. **Status here: unestablished dependency**, not a demonstrated failure of E(b).
- **Step 5, measurement NC:** Once the ontic law `ι` is fixed and effects on `U` are well defined, SP makes operationally equivalent effects equal on `U` (Proposition B(ii) ⇐). That step is distinct from and does **not** repair step 4. The state-span and effect-separation directions must not be confused.
- **Conclusions affected:** the claim of a simplex embedding of the *C-PM prepare–measure fragment* in E(b), the corresponding N2.4 “NO” verdict, and any use of Corollary E1's contrapositive are conditional on closing the step-4 dependency by a valid source argument or an explicit scope condition. The affine translation statement E(a), the restricted result of step 5, and other independent classicality arguments are not challenged by this audit.

## 3. OA-3: N4.3 and N4.4

OA3 N4.3 replaces (H4) with an effect class (V-ii-H), adding heralded composites `e ∘ π`. The proof says that singleton indicators of the entire formal multi-tick `Z` are available as “heralds at every tick followed by a final read” (OA3:468–469).

The **missing typed step to examine** is whether each such composite is an effect *of the prepared system* under C-PM, with all preparation-label reads removed, rather than an admitted **preparation herald** or an ensemble-conditioned statistic. OA3:410–416 itself separates held-at-use herald typing from ensemble conditioning. With held-at-use typing, OA3:474–475 says V-ii-H is retention-type, but does not on its own prove that all retained history values used for indicators are label-free C-PM effects.

- If a reviewer exhibits a fully specified C-PM measurement-side realization of the needed separating effects for **every admitted preparation**, with no label leakage, N4.3 step 4 is discharged on its stated scope.
- If not, N4.3's proof needs SEP (or a narrower physically justified access class) before its simplex conclusion can be invoked. The proof's step 5 still uses SP on the state side.
- N4.4's assertion that the V-ii-H effect cone is generated by joint indicators requires the same check of which joint indicators are **operationally permitted under C-PM**. “In the mathematical cone of all history functions” and “in the physically allowed effect cone” must not be identified without proof.

This is a **candidate dependency gap**, not a claim that all heralded composites are forbidden or that N4.3/N4.4 are false. Some measurement-side heralds may remain available; the reviewer must classify them by exact preparation/measurement boundary and use time.

## 4. Controls and limits

1. **Do not infer theorem falsity from an unstated step.** A different simplex model may exist even when the particular `ι(s)=law(Z₀)` model is not preparation noncontextual. The two-state toy above illustrates this.
2. **Do not import a counterexample.** P0 N8.2(b)'s additive ring-conveyor gbit violates the R-lin/(xiii) class, and raw (SP) fails. It cannot refute OA2 E(b) or prove that native R-lin admits a gbit. It illustrates why full history and label-free measurement access must be distinguished.
3. **Do not impose LF globally as an axiom.** P0 proves a conditional LF subclass result and returns O-U for the full class. The minimal theorem repair, if needed, may be SEP, a concrete construction, or a more precise reading of C-PM/V-ii-H.
4. **Keep independent results:** OA2 E(a) translation, state-span ⇒ measurement-NC conditional step, and the model's reproduction of allowed effect statistics remain on their prior scope. No statement about all OI observers follows from this audit.
5. **One-way logic only:** a sufficient separation condition yields NC for the candidate model, not its necessity in all simplex embeddings and not a native QM derivation.

## 5. Decision-oriented disposition (AUTHOR-SIDE, unreviewed)

**Tentative verdict: SCOPE / PROOF-DEPENDENCY CHECK REQUIRED**, not REVISE of already merged files and not a new physical theorem.

The narrowest next paper question: **Does the original C-PM/H4 or C-PM/V-ii-H definition itself ensure SEP for the E(b)/N4.3 candidate ontic space for every admitted preparation, including adaptive settings, earlier heralds, their failure records and retained labels?** A reviewer must either:

(A) exhibit a complete allowed-effect separation proof, with preparation/measurement timing and label exclusion; or

(B) identify a missing independent access condition, specifying whether it is already derived, an explicit conditional theorem hypothesis, or an added physical premise under `A.29; or

(C) give a precise unresolved proof gap.

No new OI computation is necessary for this audit. Claude's separate R-lin/(xiii) C3 investigation concerns actual rule reachability and cannot be assumed to answer the abstract OA2/OA3 proof-typing question.

**Independent non-author review checklist:** verify C-PM label typing at OA2:103–118 and OA3:101–126; independently rederive the implication SEP ⇒ prep NC for the **specific** `ι` model; check that SP does not imply SEP; inspect whether (V-ii-H) already entails the required indicators without label leakage; separate within-horizon composition from postselection over disallowed labels; inspect the exact downstream use of N4.4/E1 and the finite-ring scope of OA3; check all source pins, and return ACCEPT / ACCEPT-WITH-CHANGES / REVISE. The author of this draft cannot count as its independent reviewer.

## 6. Off-main support and source status (`A.42)

| Source | Use | Classification |
|---|---|---|
| OA2 r4 and OA3 r4 on `main` at `c3b5f37a` | primary source text and proof claims | research records [R] on main, **not** established theorems (`A.46 item 7) |
| P0 r3 at PR #1268 `2a9f10ba`, ChatGPT review 5892912758 | nearest prior evidence for C3/LF and AW-P0-2 | **support off main**, review-scoped; this audit's abstract separation lemma is independently argued and does not promote P0 |
| SYNTHESIS-r3 on #1276 `9eeee392` | provenance of SQ4 and T5 | **provenance off main**; not a premise for the argument |
| Claude's running C3 unit | none used | **not used**; results unavailable here |

**Next gates:** non-author independent scientific/scope review, a follow-up ChatGPT review by a reviewer separate from the writer only when policy-compliant, and an explicit owner decision before any manuscript/established-claim change or integration.