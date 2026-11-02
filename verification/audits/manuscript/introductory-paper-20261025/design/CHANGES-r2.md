# Changes in revision 2 of the paper design

**Inputs and outputs**
- **Applies:** `paper/review/REVIEW.md` (ACCEPT WITH CHANGES).
- **Unchanged as the reviewed objects:** `OUTLINE.md`, `CONTRIBUTION.md`, `SOURCES.md` and
  `probe/examples.py`.
- **New:** `OUTLINE-r2.md`, `CONTRIBUTION-r2.md`, `SOURCES-r2.md` and this file.
- **Repository:** no file changed. The git commands used `-c gc.auto=0 -c maintenance.auto=false`.

**Verified independently before applying**, at `687e885b`:
- `gl2_strong_gauge_moves_relative_candidate` (CoherentLiftGauge:537) and
  `gl3_constant_gauge_preserves_relative` (:451);
- `compositeCompleteness_unconditional` (IsometryExtension:179), called at GeneralCarrier:84;
- `finiteIsometryExtensionSF_discharged` (IsometryExtension:116);
- `sh1_necessity` (TwoSidedGauge:168) and `gramPhaseEquiv_of_twoSided` (:263);
- `RealizesSealedOICore` on `Fin 2` (OIRealization:234);
- the `Fin 2` typing of `oi_compatible_classification` (GeneralCarrier:168–172), and `main_result`
  (:188);
- the census families "act 11" and "act 12", with their Main anchors, and the families with
  `manuscript: []` (RecurrenceHorizon, PhysicalC4Discharge);
- the FULL mirrors at :1987 and :2036–2038;
- GR:721;
- the parent of `ce7937d2` is `ee2d4e68`;
- the Explainer reference counts: `verification/README.md` 15, `FULL.md` 1,
  `book/bibliography.md` 1;
- the sha256 of the bridge log, `e20abaee…5251`, and its gate lines (:38887 "PASS lean-axioms …
  6082 named result(s)", :38895 "release gate: PASS");
- the axiom reports of five cited declarations;
- the AUDIT sha256s `eacbdd56…22ad` (applied) and `b8967887…a781` (pre-recheck).

## Required changes

| Finding | Change | Where |
|---|---|---|
| F1 / R-1 | "each independent of embedded observation, none supplied by it" replaced by the review's wording verbatim: "each independent of the other four and of one finite C1–C4 observation process, by qubit countermodels, and none implied by bare finite OI; which of them a physical substratum supplies is open". Also applied to (a)4, the (b) row for §6-d and non-claim 2. Added risk R22 | CONTRIBUTION-r2 paragraph; SOURCES-r2 R22 |
| F2 / R-2 | §6-d now gives independence "on the qubit … (`five_way_minimality`, `Fin 2`)", calls `oi_alone_not_qm` a qubit countermodel, and states that E2 is carrier-general. GR:228 is added for the open question | OUTLINE-r2 §6-d and the E2 table; SOURCES-r2 §6-d |
| F3 / R-3 | §6-b now cites `gl2_strong_gauge_moves_relative_candidate` (two lifts, different relative candidates) and `gl3_constant_gauge_preserves_relative` (a constant deformation cancels), with their census anchoring. The clause is restated at kernel scope. UNTRACED-1(a) now points to `TwoSidedGauge.lean` and the act 12 family, as "not yet checked direction by direction"; the first pass's "not located" is recorded as a search gap | OUTLINE-r2 §6-b; SOURCES-r2 §6-b, UNTRACED-1 |
| F4 / R-4 | In the E2 sufficiency chain, `compositeCompleteness` is replaced by `compositeCompleteness_unconditional` (IsometryExtension:179), which is the conditional `compositeCompleteness` (AncillaClosure:373) with its premise discharged by `finiteIsometryExtensionSF_discharged` | OUTLINE-r2 E2 row; SOURCES-r2 §6-d |
| F5 / R-5 | §7-c becomes "not classified (C16-S; AUDIT r4 did not read the #917 records, AUDIT:1397–1398)". §7-d becomes "covered in kind, per the package's own description of C2 and C4; not literature-mapped". §7-g and §7-h become "not classified (no literature examined)". The design's own "known in kind (elementary)" is removed everywhere. SOURCES-r2 now states that no originality entry is the design's own judgment | CONTRIBUTION-r2 (b); OUTLINE-r2 §7; SOURCES-r2 §7, "Originality" |
| F6 / R-6 | R11 adds FULL:1987 and FULL:2036–2038. Its safe form is the review's wording: correct first, or drop §7-c and §7-f; Alt-L still carries §7-c. Decision 1(a) is mirrored. OUTLINE-r2 states the conflict under §7 and adds a **conflict-free §7 variant** (§7-a, §7-b, §7-g, §7-h, §7-i, §7-j) as a concrete form of the "drop" option. That variant is this revision's addition, not the review's | SOURCES-r2 R11, decision 1(a); OUTLINE-r2 §7, "Alternative scopes" |
| F7 / R-7 | §7-i states three conditions (constant coefficient, β, $S_{\mathrm{BH}}\propto M^2$) and the M-dependent counterexample values (0.7027 and 0.8707). Non-claim 6 states the three conditions. §7-f writes "$t_P/\tau_B^D \ge 1.153\times10^{57}$ ($t_P$ at β = 1)" and gives the 1.785×10^57 bound (REPORT:228). R12 is extended | OUTLINE-r2 §7-f, §7-i; CONTRIBUTION-r2 (c)6; SOURCES-r2 R12 |
| F8 / R-8 | Non-claims 9, 10 and 11 added verbatim. §3-d excludes Main:532's "fixed autonomous generator" remark | CONTRIBUTION-r2 (c); OUTLINE-r2 §3-d |

## Findings F9–F14

| Finding | Change |
|---|---|
| F9 | The risk "no Lean build or axiom report observed" is replaced by the observed result. At `687e885b`, the push run `40291389159`, job `121467032075` ("Mathlib bridge"), succeeded. Its release gate passed, and `lean-axioms` reported 6082 results within the three standard axioms; the cited declarations were spot-checked. This is cited as provenance only. SOURCES-r2 ("Kernel"), UNTRACED-4, R6 and decision 2 state that an expected result retained on `main` (§A.42 item 1) is needed before the paper says "machine-checked". The contribution paragraph now reads "checked in Lean 4/Mathlib at a stated commit" |
| F10 | R17 is extended. It now says that the literature studies' reviews are scratch only. It says that the AUDIT text relied on (`eacbdd56…22ad`) is r4 with Rc4's nits applied and was not itself re-checked, since Rc4 reviewed `b8967887…a781`. It says that the governed design decisions rest on scratch until the records are retained. OUTLINE-r2's input line now reads "r4 with the nits of its re-check (Rc4) applied". Added as decision 3. **Path correction:** the reviews are at `S/revlitcorr/` and `S/revlitbh/`, not under `S/introaudit/` as REVIEW.md:238 has it (verified by `ls`) |
| F11 | GR:226's box is added to "Not to be displayed", with its typing evidence. Added risk R21, and the box is listed as a separate owner check of GR (decision 5). Non-claim 2 says the paper does not cite the box |
| F12 | The census question becomes decision 4. It covers paper registration in `manuscripts`; anchors for the RecurrenceHorizon (§5-c), PhysicalC4Discharge (§5-e) and, in Alt-X, RootedClassification families; and the paper's anchors in families already carried. §5-c and §5-e note `manuscript: []` |
| F13 | Page format stated: single column, about 550 words per page (proposed; decision 6). Appendix A is restricted by default to about 15 kernel-backed rows at 0.5 pp, with the full map at about 1.5 pp as an alternative that needs a cut elsewhere. Alt-L now keeps §7-g as one sentence, because §7-h depends on it. Alt-L is defined identically in OUTLINE-r2 and SOURCES-r2, with Alt-L's non-resolution of R11 stated. §6 is marked as the tightest section |
| F14 | Probe caveats recorded in SOURCES-r2 §5-b and §5-f, and in OUTLINE-r2 §5-b. The CMI is computed in floating point; only the matrices are exact. $P(x_2{=}0\mid x_1{=}1)=1/3$ assumes $x_0$ uniform ($a/(2-a)$ in general), and the paper must state the $x_0$ law |

## Nits

Every nit is adopted:

| Nit | Applied |
|---|---|
| N1 | `main_result` (GeneralCarrier:188) and `oi_compatible_classification` (GeneralCarrier:168) are now attributed to their module |
| N2 | §7-a cites GR:721, the partition, not the :719 heading |
| N3 | E2 reads "on the system and at every positive ancilla level" |
| N4 | "carries **at least** the visible predictive information" |
| N5 | "in finite toy access models" |
| N6 | XOR: "up to flipping the final bit, RHP 2014 Eq. (15)", in CONTRIBUTION-r2 (b), (c)7 and OUTLINE-r2 §5-f |
| N7 | §7-c reads "in a bijective instance", with the 32 non-injective violators noted (REPORT:21) |
| N8 | §7-f discloses the post-plan Γ and $\tau_B^D$ intervals and their insensitivity (REPORT:234–235) |
| N9 | The Explainer dependent list now includes `verification/README.md` (15), `book/bibliography.md` and FULL (1 each), the census anchors in the act 11 and act 12 families, and frozen records (errata.json, A12P.json) marked as not correction targets |
| N10 | The parent of `ce7937d2` is `ee2d4e68`, now stated |

## Not adopted

- **Rewriting `probe/examples.py` to compute the CMI exactly (F14's option).**
  - Not done, because the probe is part of the reviewed object and is kept unchanged.
  - The paper does not cite the probe; it cites Main:178–196 and the repository probe
    `review4_probes.py`.
  - Every mass in the XOR law is a power of 2, so the float value is exact in substance.
  - The review's alternative, "the record should say float", is adopted.

## Owner decisions, final list (all in SOURCES-r2)

1. **Scope:** recommended (≈ 14.25 pp), Alt-L (≈ 12.25) or Alt-X (≈ 15.0). Within it:
   - (a) resolve the R11 conflict: correct ch07:110, ch07:159–161, GR:811 and their FULL mirrors
     first, or drop §7-c and §7-f (the conflict-free §7 variant). Alt-L does not resolve it;
   - (b) choose a single worked example if pages force it.
2. **"Machine-checked":** retain an expected result on `main` (§A.42), or use "checked in Lean
   4/Mathlib at commit X by recipe Y".
3. **Provenance:** land or retain AUDIT r4 as applied, the two literature studies and their reviews
   on `main`, or state that the classes are design inputs only.
4. **Census registration:** register the paper and add anchors for RecurrenceHorizon,
   PhysicalC4Discharge and (Alt-X) RootedClassification, or cite those results as prose plus
   probe.
5. **GR:226's box:** a separate §A.34/§A.25 check of GR; the paper does not cite the box.
6. **Page format and Appendix A scope.**
7. **The Explainer:** the outline needs nothing from it; retirement is a separate change with the
   listed dependents.

**Flagged, not required:** the title (R1).
