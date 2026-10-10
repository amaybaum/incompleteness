# messages2 notes — clauses deleted per tag

## R7-A11P
Deleted:
- "Nothing new is proved here, so the only failure mode is the manuscript saying MORE than the theorem supports, and the guard is weighted accordingly." (a claim about the round that no predicate tests; "(publication only)" already appears in the descriptor, which is kept)
- "The propagation preregistration is pinned BY BLOB rather than by the commit that carried it, blob identity being what survives rebase." (freeze pin `_a11p_freeze_pin`, removed)
- "(E4, E5 and E18 re-pinned by the act 12 propagation, R7-A12P)" (provenance and revision-history note about the guard, not a tested property)
- "THE APPEND-ONLY SCOPE AMENDMENT adds the open-frontier surfaces and is pinned by blob on the same principle as the original freeze." (`_a11p_amendment_pin` and its drift control, removed)
- "at 19.2.12" (section locator; `_a11p_ch19_frontier` tests the "Two frontiers, not one" text, not where it sits)
- "Eighteen named contracts, ... plus two freeze-pin drift controls" -> "Twenty mutation controls." (16 contracts retained; m1–m20 all retained)
Uncertain:
- Kept "THE OVER-READING THE ACT 11 EXECUTION PR WAS BLOCKED FOR" word for word. It names the over-reading that `_a11p_gi2_not_a_no_go` and m1/m2 test. It is not a chronology claim, but it does refer to a past PR.

## R7-RNC
Deleted:
- "a SEALING round under A.37" -> "a round" (sealing/lifecycle)
- "and ANSWERS it AGAINST the freeze's own central prediction" (a preregistration prediction; not tested)
- The whole "The freeze rated RN3 (a)'s sign ... ON O_3 ITSELF" sentence, and "Both reversals ... five mutation controls" (rn3a/outcome predicates, removed)
- The whole CARRIER RULE sentence (`_rnc_carrier_rule`, removed)
- From the RN1 sentence: "C_3 is checked COMPUTED ...", "no strictness ...", "no implication between the one-time row and the re-anchored row ...", "four mutation controls". Kept only "the converse is refused in terms", which `_rnc_lean_defs` tests in the docstring (m35).
- The RN2, N_3/S_3, RN0 and RN4 sentences (removed predicates)
- "in both directions" in the P0 other-part clause. `_rnc_roadmap` checks only "is untouched". The "either direction" string was in `_rnc_status_rule`, which is removed.
- From the budget sentence: "The frozen TWO-slot budget ... slot 1 fired and the conditional slot recorded UNUSED" and "five mutation controls" (`_rnc_budget`, removed). Rejoined as "The module is checked holding exactly one top-level def and no sorry, axiom or native_decide anywhere."
- The twelve-line axiom table sentence, the FIVE DISCREPANCIES sentence, chronology, archive pins, seal-integrity, "ACTS 13's, 14's AND 15's SEALS", and the final counts
Uncertain:
- The descriptor keeps "on which the merged record said NOTHING about the pair". I treated it as part of the descriptor.
- `_rnc_lean_defs` also checks that the docstring carries non-adoption and "No verdict travels between carriers". The old message had no surviving clause that describes this, so nothing was added.

## R7-RNT
Deleted:
- "a SEALING round under A.37" -> "a round"
- "The three notions are checked landing in the freeze's wording", "named at the step where each is used" and "NO CONVERSE established by either implication, three mutation controls". Kept "maps fixed BEFORE the quantifiers" and "CLOSURE CONJUNCTS LOAD-BEARING", which the docstring check in `_rnt_lean_defs` tests. The sentence was rejoined with the TWISTED form as its subject.
- In the lift sentence: "with both frozen obligations proved and reported separately", "the ANCHOR CARRIED AND NOT MOVED" and "two mutation controls"
- In RNT3: "landing as the EXACT law on BOTH SIDES ...", the intertwining-conjunct clauses, "coincidence ... observation" and "four mutation controls". Kept "the two sides are checked NEVER MERGED" (docstring, m34).
- RNT4 (a) in full. In RNT4 (b): "EARNED ONLY BY ITS OWN EXHIBITED PAIRS" and "three mutation controls".
- The RNT5 and RNT6 sentences
- Scope edges: "no same-initial-orbit test, P0 untouched, and the NORMATIVE QUESTION refused ..." and "four mutation controls". Kept "no ladder, no census, no rigidity headline" because the docstring string in `_rnt_lean_defs` tests it.
- ACT 19 BOUNDARY: "control plane and closure READ AND NOT EDITED", "execution branch NOT CITED AS SETTLED" and "three mutation controls". Kept "UNCERTIFIED NOT REPORTED AS REFUTED" (docstring).
- Budget: "with all seven fired including both conditional slots" and "seven mutation controls"
- The ordering obligation records, discrepancies, predictions/abstentions, chronology, pins, seal-integrity, seals and the final counts
Uncertain:
- "The lift is checked landing as ONE named declaration": the only support is `RelabelLift` appearing once in the exact def list. It was kept.
- "RNT3's two sides" and "In RNT4 (b) ... the verdict": the docstring strings are general ("a verdict on one is not a verdict on the other", "Every verdict of this round ..."), not tied to RNT3 or RNT4 (b) by name.

## R7-PC4S
Deleted:
- "a SEALING round under A.37" -> "a round", and "and on top of that one preregistered sign REVERSED"
- The chronology sentence (blob pin, drift control, ancestry)
- The archive-pins sentence, including "and the note is checked to say so"
- The seal clause of ROUND 1 IS HELD IMMUTABLE ("in both senses", `_PC4_*` constants, "three mutation controls", "since an archive seal belongs ..."). The note-report half was kept.
- "and 'CS2 repairs round 1's falsified prediction'" (m6 / `_pc4s_cs2`, removed). "both mutation-tested" -> "mutation-tested" (m5).
- In the upward-reading sentence: "it is NOT called the correct reading of C4", the conditional-law identity clause and the manuscripts-SILENT clause. "each mutation-tested" -> "mutation-tested" (m9).
- The CS5, CS2/CS6/CS3-b/toy-instance, CS3-c and CS4 sentences
- "and the axiom table checked one clean line per named result" (`_pc4s_axiom_table`, removed)
- The H-Bell sentence, ARCHIVE MODE and the final counts
Uncertain:
- Kept the descriptor tail "so what can go wrong is the READING, in two directions at once". It is framing, and both directions (round 1 untouched; not a new condition) are still tested.
- `_pc4s_lean_defs` also checks the docstring "Nothing in this module says that C4 holds, or fails, at either physical cut" (m21). The old message covers this only as "the docstring slide ... mutation-tested", and that was kept.

## R7-CGR
Deleted:
- "a SEALING round under A.37 through the MANIFEST PROTOCOL"
- "each with its own route, verdict rule and failure interpretation, executed in the order ..., the gate read ..., A26-3 closed ..., act 12's ... consumed UNCHANGED" (freeze content, execution order and consumption; not tested)
- "The control-plane blob pinned with a drift control" and "the chronology verdict the validator's through one keyed call on CGR"
- The ordering obligation "RE-RUN FROM GIT on every head" with its commit-chain clauses: stage-A commit, module commit, "exactly the ten shared lemmas", verdict commits, "at any commit from the module commit to the certified object", "at every such commit", "no A26-3 theorem, no rigidity theorem without A26-2-RIGID", "the census theorem stating the branch the note carries". Also its synthetic-git negatives (fabricated SHA, out-of-order chain, verdict theorem/coincidence lemma in the module commit, other-branch census theorem, rigidity theorem, A26-3 theorem) and "on synthetic data".
- Kept the per-module properties that `_cgr_lean` tests at the head: three frozen definitions verbatim and no other declaration, the one import, geometry, relabelling, no transpose/conjugation, Fourier core. Also kept the five head mutations m12, m12b, m12c, m13 and m13b. They are rejoined under "the module carrying ...".
- The whole note-distinctions list. Only "the frozen P0 sentence with its one substitution VERBATIM in the ROADMAP after act 25's" (`_cgr_p0`, m11/m11b) survives.
- "thirty-six mutation controls, the locating controls read from git at B, and this round's seal state ..."
Uncertain:
- Kept "a GATED round" in the descriptor. The gate reading itself is not tested.
- m13c (a missing axiom line) had no named slot in the old mutation list and was not added. It is covered by "with their axiom lines".
- `_cgr_p0` also requires the sentence in the result note and the Case A line. The old message named only the ROADMAP, so nothing was added.

## R7-SGT
Deleted:
- The boxed outcome, the central result sentence, the three boundaries, ST0(c) and ST1 (removed note predicates)
- ST2: "and the bounded wording"
- ST4: "the frozen exact-product deep-sector model stated and bounded", "both relabellings checked", "the widening to approximate decoupling" and "the skipped relabelling". "all mutation-tested" -> "both mutation-tested" (m19, m20).
- The post-round sentence, non-licences, P1 label and no-manuscript clauses
- "with both conditional slots recorded fired for stated reasons" (budget-table record in the note)
- The chronology sentence, ARCHIVE MODE and the final counts
Uncertain:
- Kept "ST3 ... non-trivial statistics". I read it as the `trace U = 2 ∧ trace U' = 0` conjuncts that `_sgt_st3_kernel` checks.
- Kept "Six of six definition slots fire and no seventh" on the strength of the exact six-name def list.

## R7-AUDB
Deleted:
- "the audit records why bidirectionality and H-scramble do not close it" (line `'strengthened form of C1' in _cc and 'H-scramble' in _cc`, removed). "the audit claims neither that C4 holds nor that it fails at the cut" was kept (`_asserted(_cc, _bad)`, retained).
- Revision-history wording changed, per rule 4: "no longer infer" -> "do not infer" and "no longer lists" -> "does not list". This is a minimal negation and not a pure deletion, because deleting "no longer" alone would invert the meaning.
Uncertain:
- The trailing duplicate sentence "Claims neither that C4 holds nor that it fails at the cut." is kept word for word, since it is still tested.
- Nothing in the old message described the removed audit-table and freeze checks (CONCRETE-CUT table cells, FREEZE), so nothing further needed deleting.

## R7-HYA
Deleted:
- "in which every target was predicted positive with its reason frozen, so what can go wrong is the STATUS each finding is reported under, not the landing" (preregistered predictions and landing framing). The descriptor is cut to "a SOURCE AUDIT".
- The chronology sentence and the whole H0 sentence
- H1: "read EXACTLY as THIS candidate field under THIS rule failing q-gauge invariance" and "the inflation and the rescue both mutation-tested" (note mutations, removed). Retained m6 tests the {2,4} set, which the old message did not frame as a mutation.
- H2: "with Corollary 1a consumed and not contradicted", "the counts the fully symmetric 2 versus 1" and "the level-3 fallback UNUSED"
- H3: "checked HO with NO timescale separation preregistered or asserted and no local-equilibrium statement either way". Rejoined as "H3 is checked with the witness pinned ...".
- The H4 and note sentences, ARCHIVE MODE and the final counts
Uncertain:
- Kept "the dimension count reached at kernel level". I read it as `symInvariantQuartic_iff` with `∃! xy : ℝ × ℝ`, which `_hya_h2_kernel` checks. Deleted "the counts the fully symmetric 2 versus 1" because the "1" (isotropic) count is not checked by any retained kernel string.
- The descriptor framing was deleted rather than kept, unlike PC4S, because it relied on the prediction clause and mentioned landing.

## R7-RCH
Deleted:
- "the amendment carries the controlling horizon definition and the no-periodicity warning verbatim" (reads of RECURRENCE-TIGHTNESS-AUDIT-AMENDMENT-1.md, removed)
- "while the layer section draws on the rooted realization solely for row-stochasticity": no retained string tests "solely for row-stochasticity". Deleted under rule 5.
Uncertain:
- Kept "the preregistration and its controlling amendment are named in the module". The adjective "controlling" is descriptive; the check is only that the names appear.
- Kept "the tightness question being neither answered nor prejudged and no accessibility claim made". The registry-note strings ('separate tightness question', 'no accessibility claim is made for the horizon itself') and the README forbidden strings test it.

## R7-OLT
Deleted:
- "a SEALING round under A.37 through the MANIFEST PROTOCOL," -> "a round", and "frozen BEFORE any census" (ordering)
- The control-plane blob pins, chronology verdict and ordering-obligation re-run with its synthetic negatives
- The whole note-distinctions list except the frozen P0 sentence VERBATIM in the ROADMAP
- "eleven mutation controls, the locating controls read from git at B, and this round's seal state read mode-aware from the prospective declaration or its record, never from a constant"
Uncertain:
- `_olt_supersessions` (retained) tests guard-source strings: two SHAs and the SI3 manifest accessor/baseline names ("nothing of this round's state is a legacy constant"). The only old clause close to it is the seal-state/prospective-declaration clause, which rule 2 requires deleting. The new message therefore describes nothing that this predicate tests. The caller may want a clause for it, or may want to reconsider retaining it.

## R7-NLV
Deleted:
- "frozen blob", "one keyed manifest authority", "actual first-parent chronology", "A27-0 before A27-1", "all eight records", "three scoped attestations after one prior-knowledge disclosure", "exact outcome vector and status sentences", "unchanged earlier verdicts", "THE CLAUSE three times" and "mode-aware seal state" (freeze, authority, ordering, note and seal checks, all removed)
- "full-domain predicates" and "strict-versus-twisted boundary": unsure whether these name properties of the hash-pinned statements in `_nlv_module_ok` (the `StrictNatural`/`TwistedNatural (0 : Fin 1)` and `ProperAt`/`FactorizesOnProduct` exclusions) or note content. Deleted under rule 5. Any statement-level property is still covered by "26 pinned statements".
- "No closed-round contract is edited." (a statement about the guard's own edit history; no retained predicate tests it)
