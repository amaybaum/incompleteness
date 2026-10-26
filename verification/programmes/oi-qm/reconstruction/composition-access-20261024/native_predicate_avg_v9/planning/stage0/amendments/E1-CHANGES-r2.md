# Erratum E1, revision 2: changes

**Revision 1:** `E1-LAYER1-ERRATUM.md` at `21d25752`, SHA-256
`c00b448659d1df4a48c843c3a2eb85ae6e2b35d683896f0780c2cd48de1512ab`.

**Revision 2 applies:**
- the independent review `../../review/E1-REVIEW.md` (`47e16576`): R1–R5 and the owner decisions;
- the follow-up analysis `../../review/E1-ANALYSIS.md` (`5941bc58`): the replacement text of §D;
- the owner's rulings of 2026-10-26 (amaybaum), quoted in the erratum's §1.

Neither revision is in effect. Revision 2 awaits a diff-only re-check (`E1-REVIEW.md`, owner
decision 6). Nothing ran on v8's class, and the frozen files are untouched.

## Review items

| item | edit in revision 2 |
| --- | --- |
| R1, H₁₀₀'s sampling unit | §7 "The samples": both samples are drawn over every record index i ∈ [0, N), with the hash rule stated (§D4) |
| R2, set 2 facts | §7 "The scope", set 2. Under A, T_A ⊆ Surv_A (proved). Under G, the set is (T_G ∩ Surv_G) ∪ F_G, with F_G closure-free, by Lemma G-D (§D4) |
| R3, σ case 3 (c) | §4: "ret_c(R) is the run's computed closure of R (E1-F3)", and "σ reads C9 only on accepted shards. Shard completeness is not an input of σ" (§D2) |
| R4, attribution and certification | §4: σ transcribes Layer 2 r2 (`4a51c675`), including L2-R8's L3-bound checks, which only add non-OK cases; adds "Why σ = OK certifies the bound" (§D2) |
| R5, naming | §0: the tag convention sentence. §8: "equivalence E2" and "equivalence E1". §2 and §7 likewise write "equivalence E4" and "equivalences E1 and E2" (§D0) |

## Owner rulings and decisions

| ruling or decision | edit |
| --- | --- |
| C7 set 2, re-decided: "Preserve the full 595-record G-convention population unless …"; "Retain the approved shared-tip closure scope, including G's 595 records" | §7. Set 2 is kept in full: closure-free F_G under G, computed per record. Orbit reduction is documented as proved for verdicts, multiplicities and set membership, and not for failure detection (`E1-ANALYSIS.md` §A3, fault F2). Under A, set 2's redundancy (T_A ⊆ Surv_A) is documented, not removed (§D4) |
| sampling unit: "Every record index" (decision 2) | §7 "The samples" (§D4) |
| σ diagnostic: "Give S1a its own diagnostic status, not an overriding success label" | §4 "Added definition" and "Precedence" (§D2) |
| L_A and L_G recomputation in σ: "Add it" (decision 3) | §4 case 2 (d); the L3 values are reported, not a σ condition (§D2) |
| rule T's standing: "Approved, with qualification …" (decision 4) | new §6a, item E1-T6, replacing r1's "Not governed by E1" paragraph; `rule_T.statement_scope` (§D1) |
| counts: "Treat 58 as the current baseline …"; "explicit count definitions and a reconciliation table" (decision 5) | §8 "Count convention" and the reconciliation table; 58 kept (§D5) |
| Lemma G-D in C7's reference computation: open | §9: an open owner decision, to be taken with κ once the dry run reports \|F_G\|. The specified default is the full `s0ref` closure; the G-D form is a proved, cost-only alternative needing approval. §7's check bullet states this |
| κ and S7: "Decide later" | §9, unchanged |
| decision 6, effect after a diff-only re-check | status line |

## The §10 table (§D6)

The eight rows of §D6 are added: Lemma G-D, the closure-free set 2, member-only faults, σ never
overriding the label, the L_A and L_G recomputation, rule T's statement scope, record-index
sampling, and coverage reporting. The existing rows for σ and C7 now name case 2 (d), per-record
checking and record-index sampling. Each new row also names the `E1-check` part that covers it on
the toy class.

## Departures from the §D text

`E1-check` part L confirms that every other block of §D stands verbatim, and that the
G-D permission text is absent.

| §D lines | text | why it is not carried verbatim |
| --- | --- | --- |
| `E1-ANALYSIS.md` 375–378, 388 | "*Shared near tip*: as drafted …", "*Q⁰(R)*: as drafted.", "*Computed closure*: as drafted." | Revision 2 edits the erratum in place, so "as drafted" would refer to deleted text. The drafted definitions are written out instead, unchanged in content. One clause of r1's computed-closure definition is dropped: "Where the two differ, C8 fails and the run is VOID". The per-record check now states that failure directly |
| 416–418 | "Under G, the reference may compute W(Out(R)) ∪ In(R) by Lemma G-D. Layer 2 then checks this form …" | Using the G-D form is an open owner decision with no default that changes results. The bullet states the full `s0ref` closure as the specified default and the G-D form as needing approval, with the same checks if approved |
| 470–471 | "Every list carries rank 3 per degeneracy, so 58 is complete …" | False as stated: the frozen list of 54 carries rank 1 for D = 6 and D = 9, as §D5's own table shows. It now reads "The lists of 58 and of 62 counts both carry rank 3 per degeneracy (the frozen list of 54 carries rank 1 for D = 6 and D = 9), so 58 is complete …" |
| 482–493 (§D6 rows) | the checkpoint cells | Each cell is kept verbatim, followed by a parenthesis naming the `E1-check` part. The Lemma G-D row's "per-record check of sets 3–4" is marked "(when the G-D form is approved, §9)" |

Where §D quotes a ruling inside a sentence, the quotation is kept as §D gives it. Revision 2 also
adds a "What changes" paragraph and a §A.41 checkpoint to E1-T6 (§6a), which §D1 lacks, and
quotes the frozen text E1-T6 governs (L1 lines 1001–1004 and 1033–1035).

## Other edits

- §0 states the review and analysis documents, and adds the toy F_G count to the toy values
  carrying no information about v8.
- §1 gives every ruling, with its source.
- §2 adds the notation ℛ.
- §4 "What changes" states that σ is diagnostic. Its checkpoint adds case 2 (d) and the label
  self-test.
- §11 describes the new check parts H–L and their results.

## `E1-check` (toy only)

The parts added in revision 2:
- **A:** the quotations now cover `E1-REVIEW.md` and `E1-ANALYSIS.md`, and L1 lines 1001–1004 and
  1033–1035. There are 74 quotations, read with blockquote markers stripped.
- **H:** Lemma G-D for L3′ and L3 on the toy class and on the planted records, and its corollaries.
- **I:** the planted faults F1 and F2, the computed-closure mutant, and the direct per-record
  check.
- **J:** record-index sampling and coverage per set. The populations are cross-checked against
  `e1_analysis.out`.
- **K:** σ case 2 (d) with a perturbed-count countercontrol, and σ = OK never overriding a failing
  label (Layer 2 r2's `label` and `rule_T`).
- **L:** §D applied verbatim, with its departures.

There are 55 checks in all. All pass, the run exits 0, and the output is byte-identical under
`-O`.

## Layer 2 follow-ups the revision implies (not done here)

- Replace the C7 scope placeholder with:
  - sets 1–4 of E1-F3, with F_G computed per record and closure-free;
  - direct production and reference closures per record of the scope;
  - per-set raw and orbit coverage;
  - record-index samples with the `C7_H100` and `C7_H1000` streams, or the names Layer 2 freezes.
- Add σ case 2 (d), and record rule T's outcome beside a non-passing run label.
- Add `rule_T.statement_scope`.
- Have the dry run report |F_G| and the C7 cost term.
- Add the self-tests and the computed-closure mutant named in §10.
- Align `LAYER2-PLAN.md` §4.3 with E1-T2.
- Extend the count keys to 58.

## Revision 3: the re-check's nits (E1 in effect)

**Revision 2:** `E1-LAYER1-ERRATUM.md` at `d2d5e92f`, SHA-256
`4db591adda83cd19eb2cfff13fd1bc1aef67f5ad0548781012cd26d7312fce8b`.

Its diff-only re-check is `../../review/E1-RECHECK-r2.md`, SHA-256
`98f092f3a722d12a3fc43ece2a85daa189362ceb6f5d7b3ae92e0ba132120e5e`. Its verdict was ACCEPT WITH
NITS, and it accepts all four departures listed above (its §1). Revision 3 applies N1–N6 and the
owner's rulings of 2026-10-26 that were given during the re-check. No definition, population,
count or label changes.

| nit or ruling | edit |
| --- | --- |
| N1, the owner's decisions | §1. Five rows quote the rulings, with author and date: C7 per-record evaluation ("Approved. Retain per-record evaluation …"); the revised check set ("Approved in principle …"), whose condition `E1-RECHECK-r2.md` §4 meets; Lemma G-D ("Conditionally approved …"); counts and S1a ("Approved. Retain 58 counts …"); the four departures ("Independent review required …"), accepted in the re-check's §1. §7's ruling line also quotes the per-record ruling |
| N1, §9's G-D bullet | The re-check's text is used verbatim up to "guards them." The bullet then reads that the full form remains the default, and that the G-D form stays a non-executing optimization proposal until the owner confirms that the proof meets the bar, a confirmation taken together with κ. §7's check bullet and the §10 row ("when the G-D form is enabled") agree |
| N2 | §7 "What changes": "(with the closure code's retained/logged partition of Q⁰, a code invariant)" |
| N3 | §7 "Orbit reduction": "sets 1 and 2, and I_c, are unions of orbits; the record-index samples H₁₀₀ and H₁₀₀₀ are not, which is one reason C7 is computed per record" |
| N4 | §7, after Lemma G-D's ∎: the pointer to `E1-ANALYSIS.md` §E, verbatim |
| N5 | §7 "What changes": the residual over-elimination escape, verbatim. §9 adds owner decision O1 (E_G as set 5), optional and not adopted |
| N6 | Status line: "in effect", under `LAYER1-FREEZE.md`, citing the review, the re-check and N1–N6. The title drops "(revision 2)" |
| standalone note | §0 cites `E1-NOTE-symmetry-and-G-D.md`, which holds the orbit-reduction result and Lemma G-D outside the specification, as the re-check recommends |

**One departure from the re-check's text.** N1's proposed §9 bullet ends: "The full form remains
the default; the G-D form executes only when Layer 2 enables it with that cross-check." That would
let the shortcut run once Layer 2 enables it. The owner's ruling allows the shortcut "only after
proving its equivalence … including failure behavior", and otherwise keeps it "as a non-executing
optimization proposal". The re-check's proof covers production faults, but not faults in the
reference code itself; those fail safe. Whether that meets the bar is the owner's confirmation, to
be taken with κ. So the closing sentence is replaced, and `E1-check` part M checks that the
erratum does not contain it.

**Other edits.**
- §0 cites the re-check with its SHA-256.
- §9 is retitled "Owner decisions: conditional and open".
- §11 describes the check's revision-3 parts.

**`E1-check`.**
- **Part H** adds E_G, with Surv_G ⊆ E_G (P_G) and Surv_A ⊆ I_A (P_A), on the toy class and on the
  planted records. Toy: E_G has 12 records, all in F_G, equal to the reviewer's `eg_probe`.
- **Part L** checks §D after N2's and N3's substitutions. Block 421–459 is split around N5's
  insertion, giving ten blocks.
- **Part M** is new. It checks that the erratum carries N1's §9 text (up to "guards them."), N4,
  N5, N6, O1 and the five rulings, and that the G-D form is not stated as executing.
- **Not checkable against the repository.** The re-check and the relayed rulings are not in the
  repository. The new owner quotations, and the nit texts, are therefore checked against the
  script's own transcription, not against a repository source. Once `E1-RECHECK-r2.md` is
  committed at `../../review/E1-RECHECK-r2.md` with the pinned SHA-256, part M's transcriptions
  can be re-pointed to it.

All 62 checks pass, the run exits 0, and the output is byte-identical under `-O`.
