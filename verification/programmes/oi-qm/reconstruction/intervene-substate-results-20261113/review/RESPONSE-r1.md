# Response to the exact-head review r1 of the option-(c) landing package

The review is `REVIEW-r1.md` in this directory, of head `1ef60d92`. The four package files at the
response's base `3f56d543` are identical to those at `1ef60d92`, so the review's line numbers apply
to the base. Line numbers below are those of the edited files. "NR" is `NEW-RESULTS.md`, "DEP"
`DEPENDENCIES.md`, "CH" `CHANGES.md` and "PROV" `PROVENANCE.md`.

Sources were read at their pins (`ea12fde1`, `86a413c8`, `703ae20e`, `e1534b08`, `e41cf613`,
`9f7d2612`), and `main` anchors at `c3b5f37a` (= `origin/main`). No mathematics is changed by any
disposition below; `CHANGES.md`'s closing claim stands.

## Blocking

| # | Disposition | Where it landed | Notes |
|---|---|---|---|
| 1 | applied, with one clause added | NR:215–224 (hand check); NR:254–255 (support layer); DEP:36 (row L(i), classification and closure); DEP:68–75 (gap 3 deleted; "No reference other than those of gaps 1–2 is a gap.") | Every step was checked. The proposed text defines 𝒟 through κ(s, E_s) without showing that the section E_s lies in ℛ, so the integrand is not yet defined for a general E. The added clause puts "every section E_s lies in ℛ" into the definition of 𝒟. The same three closure steps then carry it: a rectangle's section is B or ∅, (E ∖ F)_s = E_s ∖ F_s and (⋃E_n)_s = ⋃(E_n)_s. The check also states that Ω_S × R ∈ 𝒟 (a rectangle), which a λ-system needs, and that rectangles are closed under intersection. With these the π–λ argument goes through, and no gap remains. The only external input left is Dynkin's π–λ theorem [L], which row L(i) records. Nothing in the package is "owed before landing". |

## Should-fix

| # | Disposition | Where it landed | Notes |
|---|---|---|---|
| 2 | applied | NR:441–444; CH:30 (Δ10 package-text and reason cells corrected in place) | Main:724's (vii) text was checked at `c3b5f37a`. |
| 3 | applied | NR:502–505; CH:35 (Δ15 package-text and reason cells corrected in place) | S:303 and S:309 were checked. |
| 4 | applied differently (heading); applied (label); optional move not applied | NR:129 (heading); NR:131–132 (label) | The heading reads "part (c), given (T5a) and (T5b): `InstAvail CM ↔ InstAvail substratumClass` and `genTheory CM = substratumTheory`". The proposed order, "↔, and `genTheory CM = substratumTheory` given (T5a), (T5b)", can be read as making the ↔ unconditional, but the ↔ needs (T5b). The optional move of "Carried form" under the heading is not made: that paragraph names (T5a), (T5b) and (T5d), which are defined in the paragraph above it, and the new label already says that the copied block is the draft's statement and the record carries only the conditional form. |
| 5 | applied | NR:541–543 (§5 *Hypotheses carried*); DEP:36 (row L(iii): reference, claim and classification cells); DEP:58 (Main row) | Main:366–381 (theorem) and Main:401–404 ("gives up at least one of two remaining hypotheses") were checked at `c3b5f37a`. Row L's reference and claim columns for (iii) also name §5's opening statement, so that the row agrees with its classification cell. |
| 6 | applied differently | NR:309–313 | The proposed middle expression "p_k(Rr) = 1/4 + r_k·R(4 Σ_j p_j r_j)" lacks a factor 1/4. Since p_k(Rr) = (1 + r_k·Rr)/4, the correct form is 1/4 + (1/4) r_k·R(4 Σ_j p_j r_j). That is the probe's own line 141, and it equals Σ_j p_j (1/4 + r_k·(R r_j)) because Σ_j p_j = 1, which is also stated. The record carries the corrected expression. Uniqueness is stated as "the vectors p(r) span ℝ⁴", which is the spanning hypothesis of I:143, in place of "the four frame points span". Σ_k r_k r_kᵀ = I, Σ_k r_k = 0 and the minimum −2/5 were re-derived. |
| 7 | applied, with one wording change | NR:119–122 | Bell-scope (Gen) and (Rec) at `e1534b08`:142–149 were checked. T_A is glossed as the end of wing A's record window ("at time `t` of its record window `[t_s, T_A]`"), so that every symbol of (Sep) is defined. Main:362 is the re-pinned Main:364 that Bell-scope cites. |
| 8 | applied | NR:100–101 (NX-1 bullet, Δ28); NR:319–320; CH:48 (Δ28); DEP:19 (row A2 closure names NX-1) | The NX-1 bullet copies I:123's defining clause. Its E_f clause is replaced by the spanning class of §0.3, as INC-1 requires, and its route-C clause is not carried. Δ28 records both. |
| 9 | applied | NR:247; CH:28 (Δ8 package-text and reason cells corrected in place) | |
| 10 | applied, first option (deletion) | NR:382–383; CH:29 (Δ9 package-text and reason cells corrected in place) | The row option is not taken. The proposed row names QP/U′ "(on `main`)", and the review locates it in the `bsel-2-*` records. On `origin/main` no record defines the label "QP/U′", and the `bsel-2-*` records do not use it as a name. Adding the row would therefore have placed an unverified anchor in the record. The scope sentence does not use the examples, as the review notes, so deleting them changes no claim. |
| 11 | applied, with a consequence | NR:6–11; NR:424–425 and NR:463 (RV:70–71 cited at L1 and L4) | #1169 is an open Issue, and I:294 and S:347 name the four kernel targets. The new sentence says that the hand-checked steps "are cited at each result". RV:70–71 hand-checks L1 and L4 against Main:362, but L1 and L4 did not cite it. The citation is added to both *Support layer* paragraphs so that the sentence holds. |
| 12 | applied, with a convention sentence | NR:529–535 (SLL brackets); NR:476, NR:490 (table headers); NR:44–45 (convention); CH:36 (Δ16 package-text cell shows the brackets) | The convention sentence says that words inserted or replaced inside a quotation are bracketed, apart from Δ1's re-pinned Main lines and Δ2's SM anchor. The conventions paragraph already covers those two. |

## Nits

| # | Disposition | Where it landed | Notes |
|---|---|---|---|
| 1 | status labels applied; owner question not resolved | NR:144–153 | (T5a) cites I:159–166, the range the package already gives for part (a), in place of the proposed I:159–168. Part (b) is I:168. The owner question is left open (below). |
| 2 | applied | NR:164; CH:49 (Δ29) | |
| 3 | applied | NR:150 | The witness uses ⟨1|, so it needs a second point of S. (T5d) is a hypothesis written for this record, so stating this changes no mathematics. |
| 4 | applied | NR:460 | |
| 5 | applied | NR:427 | |
| 6 | applied | CH:40 (Δ20 reason cell corrected in place) | S:26 was checked; it carries the gloss verbatim. |
| 7 | applied | NR:497–498 | Probe lines 213–214 (h_A = d ⊕ ab, h_B = d) were checked. |
| 8 | applied | NR:67 | DESIGN.md:319–321 was checked at `c3b5f37a`. |
| 9 | applied | NR:68 | |
| 10 | applied, bracket option | NR:494; CH:34 (Δ14 package-text and reason cells corrected in place) | |
| 11 | applied | PROV:9 | `703ae20e`'s single parent is `1d3c4599`, whose parent is `b36bba60`. |
| 12 | applied | PROV:78–83 | #1169 was read through the REST API. Between c.6854728636 and c.6855167580 the only other comment is c.6854774010, the safeguards for the running units, which does not address step 5. |
| 13 | applied, with a consequence | DEP:31 (row H); PROV:17 | `REC-1-r7.md` has an empty diff from `9f7d2612` to the live head `cd38655c` (three later commits). Row H and PROV:17 named `7f465d56` as the head, so both now name `cd38655c`. |

## Other changes made with these

- CH:6–8: the header adds "review r1" with a finding or nit number as a cited reason source.
- DEP:21 (row C): "(row M)" referred to a row that does not exist. It is replaced by "the MECH-2 row of the `main` content table below", which is the content it names. This defect was not among the review's findings and was found while applying finding 10.

## Open owner question

- **Nit 1, second part (gap A1).** Should the package's scope be widened to carry the short proofs
  of T5(a), (b) and (d) (I:159–168 and I:179), so that row A1 closes and the headline "FI-1 is not
  theory-invariant" can be stated unconditionally? Owner decision c.6855167580 fixes the scope at
  "T5 part (c) only". The package is left unchanged on this point: (T5a), (T5b) and (T5d) stay named
  hypotheses, and gap A1 stays open.

## Checks

These were run from the worktree root at the edited state: `tools/claims_check.py`,
`tools/staleness_check.py`, `tools/voice_check.py`, `tools/artifact_placement_check.py`,
`tools/legacy_records_check.py` at HEAD, and the SC-42 integration comparison after staging the
package directory. No other computation was run.
