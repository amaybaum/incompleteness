# Response to `CHECK-RULEFREE.md`: crosswalk of corrections K1–K8 into `L54-r4.md`

**Authorization.** Owner, PR #1288 comment 6875725169 (`amaybaum`, author association `OWNER`,
2026-11-14T10:12:13Z), read through the GitHub API: a paper-only revision incorporating the
independent checker's eight replacements, with `CONFIRM-r2.md` kept byte-identical and r3 not
rewritten. Not authorized there: editing the frozen review, new mathematics presented as verified,
computation, broadening the theorem, manuscript changes, merging.

**Preservation.** `CONFIRM-r2.md`, `L54-r3.md` and `SUMMARY-r3.md` are unchanged (sha256 prefixes
`28af758d`, `0536038a`, `f398f897`, taken before and after this revision). The K corrections were
written in `CHECK-RULEFREE.md` §9 against lines of `CONFIRM-r2.md` (`CF:n`). r3 does not reproduce
that section's text; it summarizes it in its §9. Each correction is therefore applied where r4
states or refers to the corrected result: mostly in r4 §9, which replaces r3 §9, and in the r3
passages that described the same matters. Where the replacement text had to be adapted to r4's
wording, the row says so.

**Statuses used in r4.** Results of `CONFIRM-r2.md` §6 confirmed by the check: "one author, one
independent check". The checker's own additions (its §8: Proposition M and its countercase,
construction E′ at `τ = 14`, Proposition E's failure of Q2, and the rest of that list): "one
derivation, not checked". None is presented as verified, and none enters the proof of Theorem 1.

| # | Source passage (`CHECK-RULEFREE.md` §9) | Change made in r4, and where | Corrected scope |
|---|---|---|---|
| 1 | K1, replacing CF:186–187 ("not a copy of earlier history made by the rule") | Applied as worded in r4 §9.2, with `D` defined for both modes. The prior statement S1:283–286 (checked at source) is also cited in §7 R1, which described the same overlap. `S1:n` added to the citation forms | The shared coordinate is one time slice listed in two records, filled by the rule's copy (P:201); not a memory register or an outcome; nothing older than one tick; prior statement on `main`; Lemma S is its quantitative form. One author, one independent check |
| 2 | K2, inserting (S6) after CF:240 and the remark after CF:269 | Applied in r4 §9.3: (S6) in Lemma S's hypothesis list; Corollary S1's further uses of fixed `r_O` (P:143) and the empty preparation (AF:389; S2:195, :200); the P:200 remark, verbatim. The same point is added to §7 assessment item 3. r4 §9.3 adds the sentence that Lemma S and Corollary S1 are in that sense definitional, as the authorization's verdict states | Lemma S holds for every pair-form rule and every law, as a consequence of the definitions; Corollary S1 is a property of the tick partition at `τ = 1`, not of any dynamics. One author, one independent check |
| 3 | K3, adding `G_{r_N} = x_{r_{N−1}}` at CF:291 | **Adapted.** r3 did not reproduce the rule table, so there was no CF:291 counterpart. r4 §9.4 states the site set and adds the chain-end rule with the checker's note that it is not reached within the horizon | Proposition E's rule is now fully specified as cited. No change of scope |
| 4 | K4, replacing CF:329–331 ("What the construction is not") | Applied in r4 §9.4, verbatim except that each clause carries its status (Q3′, Q6′: one author, one independent check; Q2: one derivation, not checked). It replaces r3 §9's sentence "the rule is not in 𝓡 and is not R-nl … does not meet Q3′ or Q6′". §6's class-D bullet adds that the rule is not a member of class D | Not an interface of the schema (`F ∉ 𝓡`, site set not in 𝓛, D2 and D7 fail); not R-nl, not class D; a C-PROG-type instance of S4:399–402 for Q5′ alone; fails Q3′, Q6′ and Q2; meets Q5′ only |
| 5 | K5, replacing "Three things, none available to an additive rule" and the last sentence at CF:344–350 | **Adapted.** r3 did not state the "three things"; r4 §9.4 states them with K5's replacement sentence. "The Remark of §6.3" becomes "the Remark of 9.3", and "under the uniform law" becomes "under the uniform product law in initial-condition mode", the scope that Remark has (CF:271–276) | Only the first two of the three features are what Lemma 5 demands and Lemma 1 forbids for an additive rule; the third is available to some additive maps, and not to R-lin under the Remark's conditions |
| 6 | K6, replacing the table row at CF:392 by two rows and CF:398–402 | **Adapted** from table rows to prose in r4 §9.5 ("Memory and selection are separate"), since r4 has no such table. The unrestricted and the label-independent forms are stated with their sources and status; the closing sentence of CF:398–402's replacement is kept. r3 §6's "form of the target" bullet, which said the proof "does not carry over … to a target whose later records may repeat earlier ones", is replaced by a statement that cites §9.5 with that status | AF's target has no place for retained history; a place for it is an interface change (B1.1 and Q2's comparator) and an owner decision. The unrestricted form readmits the decoder; the fixed label-independent retained/outcome split keeps the selection requirement (one derivation, not checked) |
| 7 | K7, replacing outcomes (iii) and (iv) at CF:434–442 | Applied in r4 §9.5 ("What is and is not the source of Theorem 1's failure"), verbatim with status tags. r3 §0's sentence "the result depends on … a target with no persistent classical memory (hypothesis 7)" is replaced by: the proof uses hypothesis 7 as the product form of the target given the classes and does not use the shared slice. r4 §9.5 closes by saying these items describe scope and change neither the statement nor the proof of Theorem 1 | The shared-record mismatch is the source of Lemma S, not of Theorem 1. Theorem 1 holds with the duplicated slice removed (one author, one independent check). Its survival under a label-independent retained/outcome split rests on Proposition M (one derivation, not checked). It is unavailable under a class-level comparison |
| 8 | K8, replacing "At other `τ` in initial-condition mode: open, with a sketch against" at CF:431–433 | Applied in r4 §9.4 ("Initial-condition mode"), with "(ii)" restated as the question it names. r3 §9's "its initial-condition-mode version is a sketch only" is removed. Construction E′ is listed in §8 item 8 among the questions not worked on | Construction E′ at `τ = 14` has one hand derivation and no check, so the case is open. Within the schema, whether the record convention alone makes every rule fail Q5′ is the open question whether R-nl fails Q5′ |

## Scoped verdict carried in r4 §9.6 (from the authorization)

1. Classes A, B and C fail Q5′ under the stated additive-rule, target and record conditions.
2. L5.4–L5.6 are decided only within that scope (also r4 headline, §0, §6, prior art).
3. Not a rule-independent interface no-go (also r4 headline, §0, §7 assessment item 2).
4. The rule-free shared-record lemma is definitional (r4 §9.3).
5. The non-additive example witnesses only Q5′, fails other conditions, and is not class D (r4
   §9.4, §6).
6. Retained memory is compatible with the selection requirement under the fixed label-independent
   retained/outcome split (r4 §9.5; one derivation, not checked).
7. Open: R-nl, the gate question, other record conventions, class D (r4 §6, §8, §9.6).

## Other changes in r4

- Title and standing line: the review state as the authorization and coordinator give it; r4 is
  unreviewed until its own confirmation, which the authorization requires before any integration
  proposal.
- §8 item 5: R2 of §7 at general `τ` now points to the Remark of §9.3. Item 7 now says r4 as a whole
  is unreviewed. Item 8 is new: the checker's open questions (`CHECK-RULEFREE.md` §7.4), not worked
  on.
- Prior-art paragraph of §6: "have a definite answer" becomes "are decided, only within the scope
  of the stated additive-rule, target and record conditions".
- No statement, constant or proof step of Theorem 1, Corollary 1a, Proposition 2 or Lemmas 1–5 is
  changed.

## Reading and disclosure

Read for r4: the owner comment above; `CHECK-RULEFREE.md`, whole; `TUNE-1-STEP2-SESSION1.md`
280–287; `TUNE-1-STEP2-SESSION4.md` 397–403; `TUNE-1-STEP2-PROPOSAL.md` 74, 143, 200–201, 226, 433–437,
687; the `CONFIRM-r2.md` lines the corrections cite. The checker's derivations were not re-derived.
Commands: `curl` (one read of the GitHub API), `ls`, `sha256sum`, `wc`, `sed -n`, `grep`, `cut`,
`awk`, and Python text substitutions that build `L54-r4.md` from `L54-r3.md`. No computation on any
OI rule or model; nothing in the repository or either worktree edited, committed, pushed or posted.
