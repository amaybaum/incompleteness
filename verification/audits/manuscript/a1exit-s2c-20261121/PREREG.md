# A1-EXIT Step 2, unit S2-C — R1/R2 scoping and criterion-3 qualifications: preregistered edit list

**Status.** Writer's preregistration, WIP / UNVERIFIED. Written and pushed before any manuscript edit.
Independent non-author review is required; merge is a separate owner decision. Manuscript corrections
only; no physical premise is added, no conditional mechanism is promoted or dropped, A1 and Main
ledger item (ii) stay in place, and no §A.23 correctness band moves (bands unchanged: consistency work).

**Authorization.** Owner `amaybaum`, #1169 comment 7056875845, 2026-11-21T03:51:25Z: "Units S2-A
through S2-E (manuscript corrections per the Step 2 package) | **authorized**", and "S2-C includes the
observability qualifications for all eight relabelled conditions whose wording is not yet fully
printed. Whole-carrier law assumptions (X-15, X-17, X-41, X-60, X-61) are kept distinct from all-time
return conditions (X-20, X-23, X-50), as established in review round 6."

**Goal link (§A.47).** The A1-exit objective (#1169). This unit decides whether its sites can be made
true without A1: each relabelled condition printed as a conditional hypothesis with its observability
qualification, each finite-only statement with an explicit finite scope, and R1 and C1 visibly open.

**Base.** `main` at `1c7eedc4`. Line numbers are at that base. No edit adds or removes a line.

**Source record.** The A1-EXIT ledger, `verification/audits/foundations/a1exit-ledger-20261120/`
(LEDGER.md §3.1, §6, §12 N1/N11, §16; rows.json; sitemap.json). The qualification texts are the
ledger's queued wordings, adapted only in grammar.

## 1. Canonical wordings

Two kinds, kept distinct (owner record above; LEDGER §3.1, §16 2a).

- **Law form** (whole-carrier law conditions: (IP) X-15, H-μ(sp) X-17, H-μ(φ,Θ) X-41, (IL) X-60/X-61):
  "a condition on a law on the whole carrier; finite-window data can test some of its consequences but
  cannot establish it, and do not distinguish it from a finite carrier's counting law". For (IP) this
  stays true: a rooted map that is not doubly stochastic refutes (IP) on a finite window, which is a
  consequence being tested, not the condition being established.
- **Return form** (all-time return conditions: (NR) X-20/X-23): "(NR) concerns a time that need not be
  accessible and then has no finite-window test; for the selected update of §3.2 on $\mathbb{Z}^d$ the
  only laws known to satisfy it are supported on periodic configurations". At restatements the subject
  "(NR)" becomes "it" or "the condition (NR)" where grammar requires.

Grammar adaptations, fixed in advance:

- "of §3.2" (Main), "of [Main §3.2]" (companions), "of Main §3.2" (book) is added after "the selected
  update", because no Main text defines "the selected update"; §3.2 displays the update. The ledger's
  "(X-21)" tag is internal and is not printed.
- SM:252 adds "on $\mathbb{Z}^d$," before the law clause: the counting measure of Main Lemma 3 lives on a
  finite carrier, and O-A4 row 10 places the invariant law on ℤ^d (Lemma U).
- H-μ(φ,Θ) is typeset H-$\mu(\varphi,\Theta)$, since Θ has no `unicode-fix.tex` mapping.

## 2. Decisions recorded before editing

- **X-25 (M:147): option (a), F as printed. No edit.** LEDGER §12 N1 records "X-25 is F as printed. A J
  form would need a printed correction". The finite scope is visible at the site: both readings are
  stated to be "instances of the overlap-and-return theorem", which M:145 states for finite
  $\mathcal{C}_V$, $\mathcal{C}_H$ and a bijection, and the conclusion rests on "$(\Gamma_t)$ is periodic"
  with kernel citations on finite carriers (`rootedMap_periodic`). Option (b) would add a new printed
  result (the revival under (NR) from RIGID) and is not the minimum change.
- **X-12 (M:732 (iv)): edit.** Item (iv) names no carrier, and its quoted principle, "the
  maximal-entropy invariant measure compatible with the observer's records", is the record-compatible
  selection μ-R, which the owner made finite-only (#1169 c.7041456852 item 3). With item (ii) an open
  hypothesis, the posit ledger is read without a carrier size, so (iv) reads as possibly a law on an
  infinite carrier. "on a finite representative" is added after the quotation (the ledger's anchor
  "maximal entropy compatible with the observer's records" is M:60's phrase; (iv)'s quotation differs,
  so the phrase follows the closing quotation). The postulate status, "a standard but substantive
  epistemic postulate, not derived", is kept, so R1 (X-11) stays named as open. Only clause (iv) is
  touched; S2-B edits item (ii) of the same line.
- **X-50: skipped**, handled by S2-B inside its M:328–334 edit (brief). To be confirmed against S2-B's
  PR before RESULT; if S2-B reports it did not handle it, this unit reports that and does not edit M:328.
- **X-13: no site** (criterion 3 met; LEDGER §3.1).
- **Sitemap X-20 lines owned by this unit** (LEDGER §12 N11; sitemap.json):
  - M:159: edit C8 (finite representative).
  - M:356: no edit. The sentence states the role of P-indivisibility ("its role is confined to
    nontriviality at the recurrence scale"), not that it holds, and the role is the same on a finite
    representative and under (NR).
  - Cx:474 and ch15:113 = FULL:3990: no edit. Each sentence opens "On a fixed finite reversible
    representative", which scopes the recurrence-cycle statement.
  - Str:1224 and ch01:161 = FULL:494: edits C17, C19 (finite representative). The finite-only scope is
    used rather than naming (NR), which would bring the return qualification into a table cell.
- **R1 (X-11) and C1 (X-71): check only.** Search Main, SM, GR, Sub and the book for an unconditional
  statement of a selected law on an infinite carrier (R1) or of a normalized invariant shell law for
  coupled bijections (C1). Add a minimal qualification only if a site states either unconditionally;
  otherwise record that the check found nothing.
- **Not edited (other units):** Meth, ch18, glossary:105 and their FULL mirrors (Q3, S2-E, which copies
  this unit's wording); M:328–336, M:60, M:732 item (ii), Sub:253–268, appB:92 (S2-B); SM:202/222/539
  (S2-A); Main §4.6 other than M:766's (IL) sentence, Comp (S2-D). M:224's mention of (IP) is a pointer
  to §3.2's remark and is not a site LEDGER §3.1 lists for X-15; it is left as is.

## 3. Overlaps with parallel units (line-level)

- **M:732** (S2-B: items #4 and #11 inside (ii)); this unit: clause (iv) only (C9).
- **Sub:92** (S2-B); this unit: the (NR) sentence end only (C16).
- **M:766** is the §4.6 Scope paragraph (S2-D edits Main §4.6); this unit: one sentence appended after
  the statement of (IL) (C7).
- **appB** (S2-B edits appB:92 = FULL:5769); this unit edits appB:46 = FULL:5723 (C22).

Each is a disjoint substring of a shared line; at landing the merge keeps both changes.

## 4. Mirrors (§A.14, §A.25)

M:131 → ch01:121 = FULL:454 (C18). M:280 → appB:46 = FULL:5723 (C22). Book restatements ch01:179 =
FULL:512 (C20), appC:104 = FULL:6259 (C21), ch01:161 = FULL:494 (C19). Companion restatements SM:44,
GR:138, GR:589, Sub:92 (Phase 2 S1, G1, G2, B1; C13–C16). M:141, M:180, M:224, M:724, M:766, M:159,
M:732 (iv), SM:122, SM:252, SM:334 and Str:1224 have no book mirror (distinctive-phrase grep at base).

## 5. Edit list

| ID | Site (base `1c7eedc4`) | Row | Finding | Old string (unique in file) | New string |
|---|---|---|---|---|---|
| C1 | `papers/Main.md:131` | X-20 | criterion 3: (NR) introduced without the observability qualification | $n$ is any time after $s$ at which its inequality holds. | $n$ is any time after $s$ at which its inequality holds. (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations. |
| C2 | `papers/Main.md:141` | X-23 (X-20) | criterion 3: index-free form, (NR) without the qualification | both assumed as hypotheses of this form and not adopted, one direction at a time. | both assumed as hypotheses of this form and not adopted, one direction at a time. (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations. |
| C3 | `papers/Main.md:180` | X-20 | criterion 3: restatement without the qualification | the near-return condition (NR) of §2.3, assumed in its place and not adopted, without finiteness | the near-return condition (NR) of §2.3, assumed in its place and not adopted (it concerns a time that need not be accessible and then has no finite-window test; for the selected update of §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations), without finiteness |
| C4 | `papers/Main.md:224` | X-20, X-23 | criterion 3: restatement prints neither part | the index-free form of §2.3 under (FS) and (NR), and the remark | the index-free form of §2.3 under (FS) and (NR), assumed as hypotheses and not adopted (the condition (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations), and the remark |
| C5 | `papers/Main.md:724` | X-20 | criterion 3: restatement without the qualification | or the near-return condition (NR) assumed in its place and not adopted, and a non-permutation | or the near-return condition (NR) assumed in its place and not adopted (it concerns a time that need not be accessible and then has no finite-window test; for the selected update of §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations), and a non-permutation |
| C6 | `papers/Main.md:280` | X-15 | criterion 3: (IP) without the law qualification | with $\nu$ uniform. For the rooted maps $\Gamma_t$ of the prior $\rho$, as in §2.3 | with $\nu$ uniform. (IP) is a condition on a law on the whole carrier; finite-window data can test some of its consequences but cannot establish it, and do not distinguish it from a finite carrier's counting law. For the rooted maps $\Gamma_t$ of the prior $\rho$, as in §2.3 |
| C7 | `papers/Main.md:766` | X-60, X-61 | criterion 3: (IL) without the law qualification | and (EM) stated for the $\mu$-centred observables of $L^2(\mu)$. | and (EM) stated for the $\mu$-centred observables of $L^2(\mu)$. (IL) is a condition on a law on the whole carrier; finite-window data can test some of its consequences but cannot establish it, and do not distinguish it from a finite carrier's counting law. |
| C8 | `papers/Main.md:159` | X-20 (sitemap, extended scan) | recurrence-cycle indivisibility stated without a finite-representative or (NR) qualifier | The recurrence argument establishes P-indivisibility across the recurrence cycle. | The recurrence argument establishes P-indivisibility across the recurrence cycle of a finite representative. |
| C9 | `papers/Main.md:732` | X-12 | (iv) names no carrier and quotes the record-compatible (mu-R) selection, finite-only by owner decision | compatible with the observer's records") — a standard but substantive epistemic postulate | compatible with the observer's records") on a finite representative — a standard but substantive epistemic postulate |
| C10 | `papers/SM.md:122` | X-41 | criterion 3: area-law lemma uses H-mu(phi,Theta), neither part printed | in the uniform state class, the mutual information | in the uniform state class, for a law invariant under the update and the reversal (H-$\mu(\varphi,\Theta)$), assumed as a hypothesis and not adopted (a condition on a law on the whole carrier; finite-window data can test some of its consequences but cannot establish it, and do not distinguish it from a finite carrier's counting law), the mutual information |
| C11 | `papers/SM.md:252` | X-41 | criterion 3: application of Lemma 1c with the selected invariant measure, law condition not printed | the counting measure of [Main] Lemma 3, or a stated structured prior — and | the counting measure of [Main] Lemma 3, or a stated structured prior, or, on $\mathbb{Z}^d$, a law invariant under the update and the reversal (H-$\mu(\varphi,\Theta)$), assumed as a hypothesis and not adopted (a condition on a law on the whole carrier; finite-window data can test some of its consequences but cannot establish it, and do not distinguish it from a finite carrier's counting law) — and |
| C12 | `papers/SM.md:334` | X-17 | criterion 3: H-mu(sp) extension printed without either part | equivariant under signed permutations of the six components (H-blind).* | equivariant under signed permutations of the six components (H-blind), assumed as a hypothesis of this extension and not adopted; the measure clause is a condition on a law on the whole carrier; finite-window data can test some of its consequences but cannot establish it, and do not distinguish it from a finite carrier's counting law.* |
| C13 | `papers/SM.md:44` | X-20 (Phase 2 S1) | criterion 3: companion restatement without the qualification | assumed in place of finiteness as a hypothesis and not adopted, is a weaker sufficient condition. | assumed in place of finiteness as a hypothesis and not adopted, is a weaker sufficient condition. (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of [Main §3.2] on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations. |
| C14 | `papers/GR.md:138` | X-20 (Phase 2 G1) | criterion 3: companion restatement without the qualification | under its near-return condition (NR), assumed in place of finiteness as a hypothesis and not adopted. | under its near-return condition (NR), assumed in place of finiteness as a hypothesis and not adopted. (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of [Main §3.2] on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations. |
| C15 | `papers/GR.md:589` | X-20 (Phase 2 G2) | criterion 3: companion restatement without the qualification | or the near-return condition (NR) of [Main §2.3], assumed in its place as a hypothesis and not adopted. | or the near-return condition (NR) of [Main §2.3], assumed in its place as a hypothesis and not adopted. (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of [Main §3.2] on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations. |
| C16 | `papers/Substratum.md:92` | X-20 (Phase 2 B1) | criterion 3: companion restatement without the qualification | the near-return condition (NR) of [Main §2.3], assumed in its place and not adopted, is a weaker sufficient condition. | the near-return condition (NR) of [Main §2.3], assumed in its place and not adopted, is a weaker sufficient condition. (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of [Main §3.2] on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations. |
| C17 | `papers/Structure.md:1224` | X-20 (review B1) | recurrence-scale indivisibility in a table cell without qualifier | C4 memory; indivisible at recurrence scale \| | C4 memory; indivisible at recurrence scale on a finite representative \| |
| C18 | `book/ch01-observation.md:121` | X-20 (mirror of M:131) | criterion 3: book mirror of the introduction site | $n$ is any time after $s$ at which its inequality holds. | $n$ is any time after $s$ at which its inequality holds. (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of Main §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations. |
| C19 | `book/ch01-observation.md:161` | X-20 (review B1) | recurrence-cycle indivisibility stated unqualified | present wherever a rooted visible map is not a permutation. | present on a finite representative wherever a rooted visible map is not a permutation. |
| C20 | `book/ch01-observation.md:179` | X-20 (book restatement) | criterion 3: book restatement prints neither part | Without A1, the near-return condition of the corollary in §1.5 is the stated sufficient condition for the indivisibility conclusion. | Without A1, the near-return condition of the corollary in §1.5, assumed as a hypothesis and not adopted, is the stated sufficient condition for the indivisibility conclusion; it concerns a time that need not be accessible and then has no finite-window test; for the selected update of Main §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations. |
| C18-FULL | `book/The-Incompleteness-of-Observation-FULL.md:454` | X-20 (mirror of M:131) | criterion 3: book mirror of the introduction site | $n$ is any time after $s$ at which its inequality holds. | $n$ is any time after $s$ at which its inequality holds. (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of Main §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations. |
| C19-FULL | `book/The-Incompleteness-of-Observation-FULL.md:494` | X-20 (review B1) | recurrence-cycle indivisibility stated unqualified | present wherever a rooted visible map is not a permutation. | present on a finite representative wherever a rooted visible map is not a permutation. |
| C20-FULL | `book/The-Incompleteness-of-Observation-FULL.md:512` | X-20 (book restatement) | criterion 3: book restatement prints neither part | Without A1, the near-return condition of the corollary in §1.5 is the stated sufficient condition for the indivisibility conclusion. | Without A1, the near-return condition of the corollary in §1.5, assumed as a hypothesis and not adopted, is the stated sufficient condition for the indivisibility conclusion; it concerns a time that need not be accessible and then has no finite-window test; for the selected update of Main §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations. |
| C21 | `book/appendix-c-objections.md:104` | X-20 (book restatement) | criterion 3: book restatement without the qualification | also follows from the near-return condition of Chapter 1 §1.5, assumed in its place and not adopted; | also follows from the near-return condition of Chapter 1 §1.5, assumed in its place and not adopted (it concerns a time that need not be accessible and then has no finite-window test; for the selected update of Main §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations); |
| C21-FULL | `book/The-Incompleteness-of-Observation-FULL.md:6259` | X-20 (book restatement) | criterion 3: book restatement without the qualification | also follows from the near-return condition of Chapter 1 §1.5, assumed in its place and not adopted; | also follows from the near-return condition of Chapter 1 §1.5, assumed in its place and not adopted (it concerns a time that need not be accessible and then has no finite-window test; for the selected update of Main §3.2 on $\mathbb{Z}^d$ the only laws known to satisfy it are supported on periodic configurations); |
| C22 | `book/appendix-b-derivations.md:46` | X-15 (mirror of M:280) | criterion 3: book mirror of (IP) | with $\nu$ uniform. For the rooted maps $\Gamma_t$ of the prior $\rho$, as in Chapter 1 §1.5 | with $\nu$ uniform. (IP) is a condition on a law on the whole carrier; finite-window data can test some of its consequences but cannot establish it, and do not distinguish it from a finite carrier's counting law. For the rooted maps $\Gamma_t$ of the prior $\rho$, as in Chapter 1 §1.5 |
| C22-FULL | `book/The-Incompleteness-of-Observation-FULL.md:5723` | X-15 (mirror of M:280) | criterion 3: book mirror of (IP) | with $\nu$ uniform. For the rooted maps $\Gamma_t$ of the prior $\rho$, as in Chapter 1 §1.5 | with $\nu$ uniform. (IP) is a condition on a law on the whole carrier; finite-window data can test some of its consequences but cannot establish it, and do not distinguish it from a finite carrier's counting law. For the rooted maps $\Gamma_t$ of the prior $\rho$, as in Chapter 1 §1.5 |

27 splices in 12 files (17 paper sites, 5 book sites with 5 FULL mirrors). Each old string occurs once
in its file at the base and lies on the stated line.

## 6. Checks after editing

1. Each new string occurs exactly once in its file; each old string is gone where it was replaced.
2. Re-grep: every occurrence of "(NR)" or "near-return" in `papers/` and `book/` outside the S2-E
   sites (Meth, ch18, glossary and their FULL mirrors) and the S2-B sites carries "assumed … not
   adopted" and the return form in its sentence or paragraph, or is a pointer, a definition-internal
   use or the NR-1 citation; every introduction of (IP), (IL), H-μ(φ,Θ) and H-μ(sp) carries the law form.
3. Register scan of added lines (§A.32, §A.33): no "now", "no longer", "corrected", reader
   instructions or capitals for emphasis.
4. `sh ./build.sh Main SM GR Substratum Structure` and `sh ./build.sh --book`: no dropped glyphs; page
   count and median characters per page compared with the base.
5. `python3 tools/coverage_check.py`; `verification/coverage/LEDGER.json` updated if a fingerprint moves.
6. `python3 verification/audits/foundations/a1exit-ledger-20261120/ledger_check.py` is run for
   information only (the ledger is reconciled after Step 2; a pin mismatch is expected).
