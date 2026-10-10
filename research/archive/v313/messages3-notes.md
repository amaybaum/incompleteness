# messages3 — per-tag deletions and judgement calls

Method: every retained predicate was read in `verification/lean/edge_rigidity_probe.py`, together with its helper functions and mutation definitions. A clause stays only if a retained predicate or a retained mutation tests it.

## R7-A6I
Deleted:
- "Every kernel target was predicted positive -- one of them a preregistered NEGATIVE -- so". Predictions are preregistration content, and the outcome check (`_a6i_outcome`) is removed.
- "and the note is checked to say so at the caveat, at PK2 and at the non-licences, with the write-back mutation-tested three times". `_a6i_caveat`, `_a6i_pk2_bounded` and `_a6i_not_licensed` are removed. `_a6i_non_licences` only checks that the over-readings are absent. The "three times" count no longer holds: the retained write-backs are m1 and m18.
- The blob pin and drift control, the execution ancestry (act 10 form), ARCHIVE MODE, and the round-1 and propagation blob pins with the status rule clause 9 drift controls.
- In pk5: the words "SEPARATE STRONGER". `_a6i_pk5_kernel` checks `¬ A6Inv` and `A6Glob`, not that A6Inv is stronger. That wording came from the removed `_a6i_pk5_forbidden`. **Uncertain.**
- In cx2: "and one-way". `_a6i_cx_kernel` does not test that the containment is one-way; `_a6i_cx_bounded` did. **Uncertain.**
- The whole "load-bearing distinction ... in the freeze's words" sentence (`_a6i_cx_bounded`; mutations m3 and m12). The carrier-outside and A1-not-weakened phrases are still checked in the ROADMAP section and README paragraph, which the message covers generically.
- The PK0/CX0 type-P sentence, the PK3-d and PK4 clauses (with their mutations), and the two-slot budget clause (`_a6i_budget`, m13).
- The discrepancy, unsettled-points and chronology clauses, and the count sentence (31 / 21 / 3).

Kept "the four readings are checked never identified": `_a6i_lean_defs` checks the module docstring for "no two of them are ever identified".

Kept the descriptor "in the TWO HALVES the freeze keeps apart": `_a6i_roadmap_section` checks the separate packaging and lift halves.

"mu a unit" was kept. The check strings pin `(μ : ZMod q) • v` (a coercion), not `(μ : (ZMod q)ˣ)` itself.

## R7-TUPLE
Deleted:
- "so the pairing itself is what is guarded first" and the headline ordered-pair sentence (`_tu_pair`, m1).
- The direct-unistochasticity/dilatability sentence (`_tu_branch_not_dilation`, m6).
- The UB2 EXISTENTIAL / full-class sentence (`_tu_existential_scope`, m15).
- "then" in "is then checked".
- From the count sentence: "Fifteen named contracts, each mutation-tested ..., plus the freeze-pin controls". `_tu_registered` has no mutation, so "each mutation-tested" is false.
- "and the standing hygiene checks" was re-joined as "; plus the standing hygiene checks".

`_tu_priors_unrevised` (m11) was never in the old message, so nothing to delete for it.

Historical rationale that justifies a retained check was kept, e.g. "the check this execution actually failed once" and "corrected under review".

## R7-A12P
Deleted:
- The blob pin (1d471edd), the execution ancestry, and ARCHIVE MODE.
- "R7-A11P's contracts E4, E5 and E18 are re-pinned ... in the same commit, and no other." This is a commit-history statement about another guard, and no A12P predicate tests it.
- From the count sentence: "Twelve named contracts," and "plus one freeze-pin drift control".

Kept "Thirteen mutation controls": m1–m13 are all retained. Also kept the framing sentence "Nothing new is proved, so the only failure mode ...", which is rationale for all the retained checks. **Judgement call.**

## R7-WTS
Deleted:
- The boxed-outcome clause and its WT2-promotion mutations (`_wts_outcome`, `_wts_wt2`, m1, m11). The WT3-in-the-note part is also gone (`_wts_wt3`, m13).
- The three-boundaries sentence (`_wts_boundaries`, m3–m7).
- WT0 "necessity cited and not re-proved" (`_wts_wt0`).
- WT1 "the trace form as the kernel step" (`_wts_wt1`).
- WT2-gen:
  - "as the matrix-unit construction and no other";
  - "as the label and the one-sided form reported as the strengthening";
  - "and the one-sided form substituted for the label" (m12);
  - "spanning is checked never HiddenCommutantTrivial" (all from `_wts_wt2gen`).
- "WT2 is checked UNDECIDED with the obstruction named among (a)-(f) and not promoted" (`_wts_wt2`). WT2 UNDECIDED is still covered by the README/census clause and the descriptor. **Judgement call.**
- WT4 "a bound mutation-tested" (m14).
- From the non-licences sentence: the six forbidden sentences, 24.1B not begun, selection principle, "in the note", "both moves", and no manuscript touched (`_wts_not_licensed`, `_wts_no_manuscript`, m8–m10, m28). Only the ROADMAP-row part survives, reworded to "The P1 label is checked OPEN in the ROADMAP row (the move mutation-tested)" (m29).
- The slot-budget clause (`_wts_budget`, m24, m25).
- The chronology control sentence and the count sentence.

"those five" became "five".

Kept the post-round spanning-class sentence clause. `_wts_roadmap` checks the frozen spanning-class sentence in the ROADMAP, and m30 generalises it to all pairs. The old clause was attributed to the note (`_wts_post_round`, m2, removed); it is now true only of the ROADMAP copy. **Uncertain.**

Kept "the seven properties as conjuncts of ONE existential". `_wts_lean_wt1` pins the single existential and several conjuncts (range, injective, unital, trace), not all seven explicitly. **Flagged.**

Kept "WT4 is checked with NO length bound": `_wts_lean_controls` pins the bound-free Finset statement.

## R7-CLG
The only retained predicate is `_clg_gi2_conjunct_kernel` (kernel conjunct plus module docstring), with m29 and m30.

Deleted:
- "and the one whose control plane took THREE review rounds" (process history).
- Everything on strong/weak classes, GL1s, GL1w, |V| = 1, GL2, GL3, act 5, act 7, GI2 earned, the struck inferences in the note, the stronger target OPEN, GL1w evidence scope, P0, D3, slots, no manuscript edit, D5, and the counts.
- "so the forced element is constant and GL3 applies to it" (untested).
- "GI2 is therefore a statement about the LIFT SPACE" (untested in the kernel check).
- "and not only in the note".

Kept "the GI2 witness uses two lifts CONSTANT IN TIME ... IDENTICAL relative objects": the docstring says "both lifts are constant, so each relative object is identically 1", and the conjunct pins it. Kept "NOT evidence of non-gauge ambiguity" and "GL2 ... ONLY relative-evolution no-go": both are in the module docstring checked by the predicate. Those two clauses were attributed to the note in the old message, and the note is no longer read. **Judgement call.**

The phrase "each mutation-tested against deletion" is kept verbatim. m30 negates the disclaimer rather than deleting it, so this imprecision is inherited from the old message.

## R7-CAND
Deleted:
- "and -- the point of this round -- to claim only what the outcome it reached licenses". This mostly describes `_cs_licence` and `_cs_cu3_grounding`, both removed; `_cs_no_external` covers only part of it. **Judgement call.**
- The blob-pin sentence.
- The absences sentence (`_cs_cu3_grounding`, m3c).
- From the note sentence: "name CU1a", the bridge sentence at interface scope, and "claiming nothing about the external framework" (`_cs_licence`, m5).
- "Nine" from the count sentence. All seven retained contracts have mutations (m1, m1b/m1c, m1d, m3/m3b, m4, m6, m7), so "each mutation-tested" still holds.

Rephrased "The note is checked ... identifying candidateOf with no external object" to "The note is checked to identify candidateOf with no external object" (grammar).

## R7-SOURCE
Deleted:
- "nine".
- The deferred-list clause (F3, m3).
- "no Reducible verdict is recorded" (F6, m6).
- The S2 VERBATIM summary clause (F8, m8).
- "of the nine" in "Each of the nine is mutation-tested".

With "nine" deleted, "the frozen failure modes ... are enforced" is an unqualified plural, although only six of the nine are still enforced. No number was added, because that would be a new claim. **Flagged.**

## R7-OGS
Retained predicates: `_ogs_lean` (head module), `_ogs_wired`, `_ogs_p0`, and mutations m11–m14.

Deleted:
- "a SEALING round under A.37 through the MANIFEST PROTOCOL".
- "each with its own route, verdict rule and failure interpretation" (preregistration content, untested).
- "executed in the order GEO1..GEO4 with one verdict commit per target and the gate read between targets".
- "act 12's equivalence and act 21's ladder consumed UNCHANGED".
- The control-plane blob pin and the chronology verdict.
- All commit-ordering content: the stage-A commit, the module commit, the fourteen shared lemmas, the verdict commits, "at any commit from the module commit to the certified object", "at every such commit", the fabricated SHA, the out-of-order chain, and the verdict theorem in the module commit.
- "an altered geometry" (no retained geometry mutation) and "on synthetic data".
- All note-distinction items except the P0 sentence.
- "twenty-five mutation controls", the locating controls, and the seal-state reading.

The head-level module clauses were re-joined as "the module carrying ...". The mutations kept in "each checked to FAIL" are the ones that exist as retained `_ogs_lean` mutations: m12 (second definition), m12b (altered body), m13 (substituted family) and m13b (family named in another subsection).

Kept the descriptor "the first GATED round -- four targets frozen together (...)" as the leading phrase. **Judgement call:** it is untested descriptor text.

## R7-SCF
Deleted only "and its finite-table rule and bounded-horizon S2 form are intact". The two `_sfn1` checks on RECURRENCE-SCALING-AUDIT.md are not retained. "the frozen preregistration is named" stays (`'RECURRENCE-SCALING-AUDIT.md' in _sfflat`). Every other clause is backed by a retained predicate.

## R7-TBRIDGE
Deleted:
- The blob-pin clause "; and the preregistration itself is pinned by computed git blob identity, exercised through ... drifted bytes".
- The RT1/ADDITIONS sentence (`_tb_outcome`, m4).
- The horizon-gap sentence (`_tb_horizon`, m5).

"Each contract is mutation-tested" still holds: m1, m1b, m2, m3 and m6 cover the five retained named contracts.
