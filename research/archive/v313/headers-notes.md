# headers.json: clauses deleted per tag, and judgement calls

Method: for each tag I read the retained predicates, helpers and mutations in guard5.py (for R7-PC4S, in guard_na.py, per the coordinator's correction). I also cross-checked against the new message in messages.json and the messages*-notes.md reasoning. A hazard stays only if a retained predicate or mutation still tests it. Every "SEALING / under A.37 / MANIFEST PROTOCOL", chronology, pin, drift, seal, archive and ordering-from-git clause was deleted. Lines were wrapped with textwrap at width 98 plus the '# ' prefix.

Global:
- The first lines of R7-TCF and R7-TRJ are kept verbatim at 101 characters. Rule 4 (do not change the title form) wins over rule 5 here, because wrapping would split the `---- ... ----` title. No lint enforces 100, and 275 comment lines in guard5.py already exceed it.
- The first lines of R7-OGS, R7-OGC and R7-CGR (105-106 chars) were run-on titles, not `----`-closed. They were re-wrapped with the rest of the paragraph and still open `# ---- R7-XXX:`.
- Words that remain are content pins, not seal pins. "pins PROGRAMME.md's one-line state" (HYB), "R7-PC4 pins" a ROADMAP sentence (PC4S), "this guard pins verbatim" (OGS), and "pinned to its equation" (OLN/OLG/OGS/OGC/CGR). PC4S keeps "seal constants" on purpose (see below). PFR/PRA keep "not against a constant" (see below).
- Where the ordering re-run was the verb carrying the check list, "re-runs the ordering obligation MECHANICALLY from git on every head --" became "checks" (OLN, OLG, OGS, OGC, CGR). This is a minimal joining edit.

## R7-HYA
- Deleted: "every target was predicted positive with its reason recorded in the freeze, so what can go wrong is the STATUS ... not the landing" (prediction and landing framing, as in the message).
- Deleted the hazards H0's HI; H3a non-closure / timescale; H4 as PDE; S-branch; H-B read as prejudiced. No retained predicate tests them.
- Deleted: "pins the chronology in both halves".
- Kept: H1-c no-go / q rescue (docstring strings), H2b HI outright (m24), "a mutation control per contract" (each of the 4 predicates has one), and the seven-slot budget (`_hya_lean_defs` + m23; the message keeps it too).

## R7-HYB
- Deleted: "with every target predicted positive and its reason recorded"; "again".
- Deleted the hazards q-gauge test manufactured; "or as a defect"; non-additivity into advection; non-closure / sector measure vs local equilibrium; timescale, PDE, d = 3, S-branch.
- Deleted: "pins the chronology in both halves".
- Kept: the status rule (docstring + PROGRAMME line, m23/m25), sector qualifier (docstring "statement on Γ" + m9), sixth-order bound not isotropy at all orders (docstring), PROGRAMME pin, and the eight-slot budget.

## R7-PC4
- Deleted: "the toy instance at four sites promoted to Theorem 22's genericity lemma" (m4 removed); "the two inference residues quietly repaired ... instead of recorded" (residue predicate removed; the docstring's "recorded discrepancy" is a different discrepancy, the rootedPosterior spelling); "H-Bell entered".
- Deleted the whole falsified-prediction sentence ("On top of those ... freeze left unedited"), including "the sealed C1-C4 core".
- Deleted: "pins the chronology in both halves"; "holds the module to the frozen six-slot budget" (the message also dropped the budget, since only the four fired defs are checked).
- Judgement: kept "C4 declared discharged at a cut". `_pc4_lean_defs` requires "Nothing in this module says that C4 holds, or fails, at either physical cut", and m14 mutation-tests "The module settles C4 at the lattice cut".

## R7-PC4S (revised per coordinator: `_pc4s_round1_seal` retained)
- "A SEALING round under AGENTS.md A.37 that" became "A round that".
- Deleted: "or its guard block" (nothing checks round 1's guard block).
- Deleted: "called the correct reading of C4"; "a reading attributed to manuscripts ... SILENT"; "the sealed core or the four-site torus read as a physical discharge"; "the conditional-law identity read as a claim about the corpus"; the "H-Bell entered ..." clause; and the whole "one preregistered sign REVERSED -- CS5-b ..." sentence.
- Deleted: "pins the chronology in both halves".
- Kept: "its seal constants touched" (hazard 1) and "checks round 1's seal constants unmoved". Both are tested by `_pc4s_round1_seal`, which reads PC4's seal record and requires the values round 1 set, with three mutations. Also kept the TWO-slot budget (m20) and the ROADMAP sentence written alongside (`_pc4s_round1_untouched`).
- Judgement: the sealed-core / four-site-torus hazard was deleted even though m21 tests a generic docstring non-licence, because the core/torus-specific reading is not what is tested.

## R7-HYE
- "A SEALING round" became "A round".
- Deleted: "a positive HE2-f read as surjectivity, or" (the message dropped "not surjectivity"); "HE5-unstatable or a wrong-shape outcome converted into a no-go"; "HE4-a's non-discrimination ..."; "a continuum object, a timescale, a PDE, d = 3, the S-branch"; "lane D's A5 question ..."; "a new condition named".
- Deleted: "in the freeze's own words" (as in the message); "pins the chronology in both halves"; "checks that round H-A's and round H-B's seal constants are untouched -- this round adds R7-HYE and its own three and alters nothing else".
- Kept: HE3 not closure, the seam (m30), the "on im Ψ" restriction (m22), site-independent (m23), H-B not reported closed and no extremal claim (docstring), and the SIX-slot budget.
- Judgement: kept the explanatory "which is exactly what ... HE4-b proves the round does not have". It states a fact about the round, not a check.
- Fixed "site -independent" to "site-independent". This was a line-wrap artifact in the old text, not a new word.

## R7-TCF
- "A SEALING round under AGENTS.md A.37 that" became "A round that". Deleted ", against the freeze's own central prediction".
- Deleted: the freeze-rating / "the round reached line 1" sentence; "reporting the reversal as if it had been predicted, or hiding it"; "act 14's PQ3 (b) on O_1 above all"; the CF2/CF3/CF4 necessary-conditions hazard; the CF0 SILENCE hazard; "enlarging GL3 ... GL2, CT4 and CL1 ...".
- Deleted: "pins the chronology in both halves, holds the module to the frozen TWO-slot budget with the conditional slot recorded unused, and checks act 13's and act 14's seal constants unmoved". The budget went too: only the one def is checked, as in the message.
- "So the failure modes" became "The failure modes", since its antecedent was deleted.
- Kept: the N/S seam (m3-m5), act 14 recorded not repaired (m6-m7), O_2 not carried (docstring "travels to no other carrier"), CF1 matrices (m11), and CT3 (d) anti-conflation (m19-m20).

## R7-RNC
- "A SEALING round under AGENTS.md A.37 that" became "A round that". Deleted "and answers it AGAINST the freeze's own central prediction" and the RN3 rating/outcome sentence.
- Deleted the hazards: the reversal hazard, refinement as strictness/implication, RN2 as two thirds of a witness, S_3/N_3, repairing act 14's PQ4 (c), enlarging PQ3-d+/GL2/CT4/CL1, RN0 SILENCE, and "in both directions".
- Deleted the chronology/budget/seal sentence and the whole "Chronology clause 9 is honoured by EXCLUSION ..." paragraph.
- "So the failure modes" became "The failure modes".
- Judgement: kept the full verdict-travel hazard with its three sub-examples. `_rnc_lean_defs` requires "No verdict travels between carriers, in any direction", and m48 tests the ROADMAP O_3 verdict not travelling. The message had dropped the carrier-rule sentence (its note predicate is gone), but the hazard itself is still tested.
- Kept: RN1 not an equivalence (m35), P0's other part untouched (`_rnc_roadmap`), and CT3 (d) (m23-m26).

## R7-TRJ
- "A SEALING round under AGENTS.md A.37 taking" became "A round taking".
- Deleted the hazards: POINTWISE narrowing (|A| rank bound); line 2 / line 1 routes; a candidate reading unlicensed data (SP4); the uniform-phase relation; refuting a NEIGHBOURHOOD; "or SH1 beyond its strength".
- Deleted: "pins the chronology ... FOUR-slot budget with two slots fired and two recorded unused ... seal constants unmoved" and the "Chronology clause 9" paragraph.
- Judgement: kept four hazards the message had dropped, because retained predicates test them:
  - reversed quantifiers: docstring + m39, ROADMAP "quantifiers are ∃ C ∀ S";
  - enlarging line 4: docstring "four named propositions and is not exhaustive", ROADMAP "at one exhibited configuration";
  - GL2 pair ONE trajectory: docstring;
  - TG3 enlarged: m40.
  Also kept: axes not merged (m55), line 3 ruled out (m56), and act 16's positive (m26-m29).
- The "So the failure modes" wording is unchanged: its antecedent (the two-findings sentence) survives.

## R7-XTS
- "A SEALING round under AGENTS.md A.37 whose" became "A round whose". Kept "BOUNDED EXISTENCE ON TWO CO-EQUAL AXES" as the descriptor (rule 3), although the message dropped "BOUNDED-EXISTENCE".
- Deleted: "the shared structural theorem that RUNS FIRST (...TJ1 cited at the step ...)"; "the two ladders with their frozen labels"; "SPLIT-CONFIGURATION non-triviality"; "a properness witness OUTSIDE the admissible set"; "reporting a DEGENERATE propagation as propagation"; and the "Chronology clause 9" paragraph.
- "and" was dropped before "the specific errors".
- Judgement: kept "a generator law that DOES NOT DESCEND". `_xts_roadmap` requires "written at orbit level so that it descends", with no mutation.
- Judgement: kept "ENLARGING a bounded no-go". m34 tests "The candidate lists are closed and are not exhaustive", which is the guard against enlarging a no-go over a closed list.
- Judgement: kept "a candidate CHANGING TYPE". It is in THE CLAUSE, carried verbatim (m22-m24).

## R7-RNT
- "A SEALING round under AGENTS.md A.37 taking" became "A round taking" ("A" stays at the end of line 1).
- Deleted: "the three notions landing in the freeze's wording with" (the message did the same); "with its two frozen obligations"; "EXACT" and "as a universally quantified equality of matrices and never as an existential over the output"; "the second earned only by its OWN exhibited pairs"; "RNT5 reported as TWO components ... NO GLOBAL LABEL"; and the "Chronology clause 9" paragraph.
- Judgement: kept "the intertwining law reported PER SIDE". The docstring's "two sides ... a verdict on one is not a verdict on the other" (m34) is the retained check.
- Kept: the non-sequitur (m35), no uniqueness claim (docstring), and the classification NOT APPLIED (THE CLAUSE, m22/m23).

## R7-OLT
- Deleted: the "A SEALING round under A.37 through the MANIFEST PROTOCOL: ... NO CONSTANT" sentence; the control-plane blob pins and drift controls; the whole "What can go wrong ... ORDER OF EVENTS and the READING: ..." sentence (every hazard was a note-reading or ordering check, and none is retained); the ordering-obligation re-run with its synthetic negatives; and all result-note distinctions except the P0 sentence.
- Result: "The guard holds the result note to the frozen P0 sentence present VERBATIM in the ROADMAP." `_olt_p0` checks the sentence in both the note and the ROADMAP.
- Not described, because the old header never mentioned them: the eight-def check. Also not described: `_olt_supersessions`, which still checks SI3 manifest/seal accessor strings in the guard source. The message notes flagged the same point.

## R7-OLN
- Deleted: the SEALING/MANIFEST sentence; the blob pin/drift sentence; the hazards "a rung restated", "failure of factorization read as interaction ...", "a FREE label claimed from a search" and "act 21's historical verdicts rewritten"; the stage-A/module-commit ordering; "at any commit from the module commit to the certified object"; "at every such commit"; "three" (synthetic negatives); and all note distinctions except the P0 sentence.
- Joining edit: "or" between the two surviving hazards.
- Judgement: kept "ORDER OF EVENTS and the READING" and "after the outcome was known". The head check (m12, the candidate pinned to the exchange) catches any swap, including a post-hoc one. Delete these phrases if you want no ordering language at all.
- Kept the descriptor, including "consumed UNCHANGED" and the ZERO budget.

## R7-OLG
- Deleted from the descriptor: "with a fixed execution order, one verdict commit per target" (execution order) and "and a mechanically checked outcome vector" (a retired check). Kept "a witness-authorization matrix" as freeze design.
- Deleted: the SEALING/MANIFEST sentence; blob/drift; the hazards "a verdict revealed before its commit", "a verdict inferred from another target's", "a FREE label", "an independence of rungs" and "act 21's or act 22's verdicts rewritten"; the ordering re-run clauses (stage-A, module commit, the verdict-commit order G1-G4, first presence at the verdict commit); and all note distinctions except the P0 sentence.
- Kept: "a witness slid onto a later rung" (m13b, witness named in another section) and "a definition slipped ..." (m12).

## R7-OGS
- Deleted from the descriptor: "a fixed execution order, one verdict commit per executed target, a gate read between targets" and "a mechanically checked outcome vector". Kept "GATED" and the route-authorization matrix.
- Deleted: the SEALING/MANIFEST sentence; blob/drift; the hazards "a verdict revealed before its commit", "a verdict inferred ...", "a universal label from a search", "an independence read off four cells", "a characterization of the isometries" and "the freeze's reading repaired ..."; the ordering re-run clauses; and all note distinctions except the P0 sentence.
- Joining edit: "or" before the last hazard.
- Kept "the geometry's equation ... altered" and "the geometry pinned". `_ogs_geometry_pinned` is retained, although the message dropped the geometry mutation, which does not exist.

## R7-OGC
- Deleted from the descriptor: the execution order, verdict commits and gate read (with "the key hazard's form of it: ISO3's route is run only if ISO2 classified internally"), and "a mechanically checked outcome vector".
- Deleted: "after a first execution attempt without it was ruled unlanded and the chronology replayed from B".
- Judgement: "the ISO1 verdict commit carries" became "ISO1 carries", deleting "the" and "verdict commit". The normal-form theorem is still pinned by `_ogc_word_pinned` (m13e/m13f).
- Deleted: the SEALING/MANIFEST sentence; blob/drift; the hazards "a verdict revealed ...", "a verdict inferred ...", "a universal label ...", "a classification imported ...", "a weaker domain substituted ...", "ISO3's route run without ISO2's label" and "the freeze's reading repaired ..."; the ordering re-run clauses; "anywhere"; "ISO3's route theorems present only under ISO2's opening label"; and all note distinctions except P0.
- "the one import" became "the import", following the message (only a prefix is checked).
- Kept "no ISO4 theorem": the exact theorem list is checked at the head.

## R7-CGR
- Deleted from the descriptor: the execution order, verdict commits, the gate read "in two forms" (extension form, rigidity form) and "a mechanically checked outcome vector".
- Deleted: the SEALING/MANIFEST sentence; blob/drift; and the hazards "a verdict revealed ...", "a coincidence lemma slipped into the module commit" (a module-commit check), "a verdict inferred ...", "a universal label ...", "a count or a dimension asserted from a computation outside the kernel", "a classification imported ...", "a weaker domain or a path metric substituted ...", "a negative label earned by a parameter ...", "the positive route run without the extension", "the corollary executed without the rigidity label" and "the freeze's reading repaired ...".
- Also deleted: the ordering re-run clauses, "anywhere", "no coincidence statement in the module commit", "the census theorem stating the branch the note carries", and all note distinctions except the P0 sentence (with its one substitution, m11b).
- Judgement: kept "no A26-3 theorem and no a26_2_rigid_single". `_cgr_lean` requires the exact theorem list at the head, which excludes both. The message had dropped this clause, while OGC's message kept the analogous "no ISO4 theorem".
- Kept "the one import" as written. The message kept it too.

## R7-NLV
- Deleted: "chronology" from the list of what is checked, and "No closed-round guard is changed." (the latter is a statement about other rounds' guards and seal integrity; the message dropped its analogue).
- Judgement: kept "domains" (the Γ₀ pin and the `(Fin 2)`/`(Fin 16)` exclusions in `_nlv_module_ok`) and "scope" (the StrictNatural `(0 : Fin 1)` form and the ProperAt/FactorizesOnProduct exclusions).

## R7-PFR
- Deleted: "chronology" (twice: the checked list and "and every chronology clause"), and "No closed-round guard is changed."
- Judgement: kept "not against a constant". I read it as "the mutation passes through the gating predicate rather than being compared to a fixed value", not as a legacy seal constant. It is ambiguous; delete it if you read it as seal-related.
- Kept "domains" (the config-* checks) and "scope" (the census 'scope' record).

## R7-PRA
- Same deletions and the same "not against a constant" judgement as R7-PFR. Scope is also checked by p-no-factorization / p-scope-mut.

## Observations outside this task (not acted on)
- guard5.py still carries orphan lifecycle code and comments in some retained blocks:
  - OLT keeps a `for _olt_f ...: def _olt_drift` loop under "# the two drift controls";
  - OLN, OLG, OGS and OGC keep "# the drift control: ..." comments;
  - NLV's `_NLV_REQUIRED` still lists seal/manifest/chronology note strings, used only in two for-loops that build mutants and check nothing.
- `_olt_supersessions` and `_oln_supersession` are retained but test SI3 manifest/seal accessor strings and `_MANIFEST_BASELINE` in the guard source, which is lifecycle machinery.
