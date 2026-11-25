# r6: requirements needing confirmation or fresh authorization

Every requirement of r6 whose decision basis is not a class (i) record (the owner's own words on GitHub): the 44 requirements marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." and the two requirements unmarked by F4 (R6.DENY.1, R6.DENY.2). For each: its exact current wording, quoted mechanically from DESIGN-r6.md; its decision basis and class; its purpose; the consequences of authorizing and of not authorizing it; the safeguards affected; and whether it permits something an earlier design prohibited (flagged). Nothing here is adopted: every requirement of r6 takes effect only by r6's adoption, and an authorization of one requirement does not authorize another or a group.

Flagged (permits something an earlier design prohibited, or narrows a check): R6.STAT.4, R6.PUR.9, R6.PUR.11, R6.RULE.2, R6.RULE.4, R6.RULE.8, R6.DENY.5, R6.DENY.6, R6.CTRL.15, R6.PLAN.8, OBL-3, OBL-6.

| Requirement | Decision basis | Class | Flag |
|---|---|---|---|
| R6.STAT.4 | v6.0e line 95 | iii | yes |
| R6.STAT.8 | 7093128173 | ii |  |
| R6.PUR.8 | V5-D1; V5-D2 | ii |  |
| R6.PUR.9 | V5-D1 | ii | yes |
| R6.PUR.11 | v6.0e line 95 | iii | yes |
| R6.ANCH.14 | S1-D2 | iii |  |
| R6.CTX.1 | v3 D1-D4 | ii |  |
| R6.CTX.4 | v3 D1-D4 | ii |  |
| R6.CTX.12 | v3 D1-D4 | ii |  |
| R6.OUT.14 | R-D labels; A-D labels | iii |  |
| R6.OUT.15 | R-D labels | iii |  |
| R6.PROF.9 | R-D labels; v5.5.9 final D2 | iii |  |
| R6.RULE.2 | S1-D1 to S1-D3 | iii | yes |
| R6.RULE.4 | S1-D1 to S1-D3 | iii | yes |
| R6.RULE.7 | S1-D2 | iii |  |
| R6.RULE.8 | S1-D2 | iii | yes |
| R6.RULE.9 | S1-D2 | iii |  |
| R6.REC.6 | DI-2 | ii |  |
| R6.REC.7 | DI-2 | ii |  |
| R6.REC.14 | S1-D2 | iii |  |
| R6.REC.18 | R-D labels; v6.0e line 54 | iii |  |
| R6.REC.19 | v6.0e line 31; v6.0e line 54 | iii |  |
| R6.REC.20 | v6.0e line 54 | iii |  |
| R6.REC.21 | v6.0e line 54 | iii |  |
| R6.REC.22 | v6.0e line 54 | iii |  |
| R6.REC.24 | R-D labels | iii |  |
| R6.DENY.5 | V5-D1; S1-D2; V5-D2; S1-D1 to S1-D3 | ii, iii | yes |
| R6.DENY.6 | V5-D1 | ii | yes |
| R6.CTRL.7 | V5-D1 | ii |  |
| R6.CTRL.14 | V5-D1; S1-D1 to S1-D3 | ii, iii |  |
| R6.CTRL.15 | V5-D1 | ii | yes |
| R6.CTRL.17 | R-D labels | iii |  |
| R6.CTRL.19 | S1-D2 | iii |  |
| R6.CTRL.22 | DI-2 | ii |  |
| R6.CTRL.23 | R-D labels | iii |  |
| R6.CTRL.24 | S1-D2; R-D labels | iii |  |
| R6.PLAN.8 | v3 D1-D4 | ii | yes |
| R6.A1CFG.7 | V5-D1 | ii |  |
| R6.EVID.4 | S1-D2 | iii |  |
| R6.EVID.5 | S1-D2 | iii |  |
| OBL-1 | S1-D2 | iii |  |
| OBL-3 | V5-D1; S1-D2; V5-D2; S1-D1 to S1-D3 | ii, iii | yes |
| OBL-6 | V5-D1 | ii | yes |
| OBL-15 | S1-D2 | iii |  |
| R6.DENY.1 | none (F4) | no decision cited |  |
| R6.DENY.2 | none (F4) | no decision cited |  |

Not a requirement, listed for completeness: the row of sec. 33 "DR-1d, DR-2 | obsolete: dropped deny candidates (rationale in the appendix); never reused" rests on V5-D1 (class (ii)). Withdrawing V5-D1 would not reinstate DR-1d or DR-2 under those identifiers: a retired identifier is never reused (AGENTS.md sec. A.30); a rule of either form would take a new identifier (V4-COMPARISON.md).

***

## R6.STAT.4

Decision basis: `v6.0e line 95`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.STAT.4** Owner authorization is procedural. The approvals AGENTS.md requires (sec. A.50: freezing
> and designating the plan, dispatching its trials, executing it, merging into `main`; sec. A.45 rule 3
> and sec. A.51 for work) are given by the owner and quoted with author and time in the record that
> relies on them (AGENTS.md sec. A.42 item 7). The tool neither reads nor checks them. No check of this
> design is waived by r6, and every later step keeps its own owner gate (sec. 19).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-012. Controls: none (procedural boundary).

- Purpose: Fixes the boundary between technical verification and owner authorization: approvals are procedural, quoted in the relying record, and the tool neither reads nor checks them.
- If authorized: The tool accepts a run on a plan commit `F` whose technical identity checks hold, whether or not the owner designated it; only the owner's procedural confirmation and the quoted record establish approval.
- If not authorized: r6 states no boundary for authorization; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5). v6.0e (adopted, #1169 comment 7130449822) contains the same boundary, so withdrawal would need a replacement statement.
- Safeguards affected: Removes, relative to v5.5.9, the automated detection of an undesignated plan or an unapproved authority change; every technical identity check (R6.REC.18 to R6.REC.22) is kept.
- FLAG, earlier designs: v5.5.9 (final decision D4) required automated verification of owner authorization through the authority record, versioned comment forms and numeric owner id 7273571; r6, like v6.0e, does not.

***

## R6.STAT.8

Decision basis: `7093128173`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.STAT.8** Landing order. The owner decision recorded by the coordinating session in #1169 comment
> 7093128173 (posted from the `amaybaum` account, 2026-11-23T06:13:50Z; a session-written record that
> quotes no owner words) approved in principle that the tool lands first, that the plan's `PREREG.md` is
> amended and re-frozen so that every mandatory check of its sec. 11 passes as written, and that the four
> trees are distinguished (sec. 20). It superseded the execution-exception route of comment 7092885251.
> The steps it held (implementation, push, pull request, merge and the plan edit) are each governed by
> their own owner record; r6 releases none of them. Before adoption the decision is quoted in r6 in the
> owner's own words, byte-exact from the comment if it holds them, or as the owner restates it (RE-26);
> since the comment holds no owner words, the owner restates it.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: RV-002. Controls: none (governance record).

- Purpose: Records the landing order of the exception-free route: the tool lands first, then PREREG.md is amended and re-frozen so that every mandatory check of sec. 11 passes as written, with the four trees distinguished.
- If authorized: r6 records the route as the basis of its gate order (sec. 32); the steps it held stay governed by their own owner records.
- If not authorized: The gate order of sec. 32 loses its recorded basis and would need another; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserves the absence of an execution exception and the requirement that the plan passes as written.

***

## R6.PUR.8

Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words; `V5-D2`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.PUR.8** Lexically unanchored paraphrases. The deny rules close only forms with a fixed lexical
> anchor. A paraphrase without such an anchor cannot be closed by a regular expression. On added text,
> the outcome is at least REVIEW_REQUIRED only for the classes that the plan's pinned `resid` rule file
> (sec. 12) or another review profile matches. Those classes are the content of the plan's rule files,
> which are control inputs pinned at `F`, not requirements of the tool. For the rule files current when
> r6 was drafted they are, informatively:
>
> - a finiteness word together with a posit noun (posit, premise, axiom, assumption, hypothesis) within
>   a 60-character window of one sentence;
> - a state-space noun (configuration, state or phase space) followed by "is finite" or a similar
>   copula;
> - "finite set", with at most one word between;
> - "substratum", "universe" or "world" followed within 40 characters by "is", "be", "being" or "are",
>   an optional article and at most one word, and "finite";
> - "finite number" or "finite count" of states, configurations, elements, points or sites.
>
> A paraphrase outside the classes the pinned rule files match stays outside the tool; its detection
> rests on the plan's independent review of the exact head. Constructed examples outside those classes,
> which PASS when added: "the six posits of the substratum", "six assumptions about the substratum",
> "The posit ledger lists fourteen.", "the fourteen-item posit ledger" and "$A_1$–$A_6$". The plan's
> original literal item 7 misses each of these too. The two examples of R6.PUR.9 are not part of this
> requirement.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-055. Controls: V15, V21, V26.

- Purpose: States the coverage limitation for lexically unanchored paraphrases: only the classes the pinned `resid` rule file or another review profile matches reach REVIEW_REQUIRED.
- If authorized: Constructed paraphrases outside the pinned classes PASS; the tool claims no complete semantic detection; the classes are plan-record content frozen at `F` (OBL-3).
- If not authorized: The limitation is unstated, which would leave the tool's coverage claim undefined; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Matches v6.0e sec. 1 and the limitation recorded in #1169 comment 7099655517. The REVIEW guarantee for the listed classes holds only once the reviewed `resid` record is frozen at `F`; resid-b and resid-c rest on V5-D2. None of the listed constructed examples matches the form of DR-1d or DR-2 (computed, V4-COMPARISON.md), so dropping those rules did not change their outcome; whether any other v4 rule caught them was not determined in this round.

***

## R6.PUR.9

Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.PUR.9** For decision at adoption (not adopted by this draft): the residual for the deny rule
> DR-2. The two texts "the framework's sixth structural property, finiteness of the bijection" (control
> V4) and "The framework's sixth structural property is finiteness of the substratum" (control V27)
> match no deny rule once DR-2 is not in the active rule set, and PASS when added; the plan's original
> literal item 7 misses both. Whether the tool's expected outcome for these texts is PASS (an accepted
> residual) or FAIL (the expectation of DR-2's form restored) is an owner decision at adoption (RD-14, Q10), with
> these options:
>
> - (a) confirm the accepted residual: V4, V27 and V27-glossary expect PASS and V15 REVIEW_REQUIRED,
>   kept so that a change in their outcome is visible;
> - (b1) restore the FAIL expectation of V4, V27 and V27-glossary, which needs a plan rule record of the
>   DR-2 form in the plan's active rule set under a new identifier (DR-2 is retired and never reused,
>   sec. 33), while V15 stays REVIEW_REQUIRED through `resid`;
> - (b2) as (b1), and restore V15's FAIL expectation as well, which needs a second plan rule record, of
>   the DR-1d form, under a second new identifier (DR-1d is retired, sec. 33); a rule of the DR-2 form
>   does not match V15's text.
>
> The decision covers V4, V27, V27-glossary and V15 together, which rest on the same decision V5-D1
> (RE-1). For each row, (a) selects the candidate "reversal adopted" and (b2) the candidate "reversal
> rejected"; (b1) selects "reversal rejected" for V4, V27 and V27-glossary and "reversal adopted" for
> V15. Until it is made, each of the four rows carries both candidate expectations, each marked
> "not authoritative; decided at r6 adoption", and an `expect` of outcome DEFERRED; the gate reports
> `deferred-expectation` for each and never holds on it (R6.GATE.9). Outstanding evidence, a named
> blocker on adoption of this requirement: the owner decision V5-D1 that dropped DR-2 is recorded only
> in paraphrase, in the session-written #1169 comment 7099655517 (ME-6); its text is to be recorded by
> the owner.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-055, RE-1. Controls: V4, V27, V27-glossary, V15.

- Purpose: States the deferred decision on the V4 reversal and its three consistent resolutions.
- If authorized: The owner decides at r6 adoption among (a), (b1) and (b2); until then the four rows stay DEFERRED and do not count toward S13.
- If not authorized: The deferral and the option statement are lost; the four rows would have no stated decision procedure; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserves the quoted deferral instructions; adds that a rejection needs a new rule identifier (F5) and that V15 needs a DR-1d-type rule (F6).
- FLAG, earlier designs: Resolution (a) permits V4, V27 and V27-glossary to PASS and V15 to be REVIEW_REQUIRED, where v2's demonstration expected V4 FAIL and v4 expected V4 and V15 FAIL `deny-match` (DR-2, DR-1d). Deferred (V4-COMPARISON.md).

***

## R6.PUR.11

Decision basis: `v6.0e line 95`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.PUR.11** Approval is outside the tool. The tool verifies which exact plan, configuration, tool and
> evaluated commits a run checked, and identifies them in its result. Whether that plan is the one the
> owner approved is confirmed by the owner, procedurally (R6.STAT.4). No output, outcome, field or
> control of the tool states or implies that a plan, a record, a run or a result was approved or
> authorized. Admitted record directories are named "admitted", never "authorized" (sec. 21).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-057. Controls: B4-MEANING.

- Purpose: Keeps approval outside the tool: no output, outcome, field or control states or implies approval or authorization.
- If authorized: Outputs carry no approval vocabulary (B4-MEANING); admitted record directories are "admitted".
- If not authorized: option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5); B4-MEANING would lose its requirement.
- Safeguards affected: Prevents a technical result from being read as an authorization; it removes no technical check.
- FLAG, earlier designs: Same removal as R6.STAT.4 relative to v5.5.9.

***

## R6.ANCH.14

Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.ANCH.14** Boundary cases.
>
> - A splice overlaps a site if `start < site_end` and `end > site_start`. A zero-length splice at an
>   interior offset also overlaps. A splice that only touches a site's boundary does not.
> - A hit line is "in a splice image" if it contains the splice's offset in `X`. Empty images are
>   included (for example D029 at Substratum.md:268).
> - A removed site (empty image) has no replacement region; the line holding its offset is reported with
>   the removal, not counted as a region line.
> - A last line without LF is a line. Its span ends at end of file.
> - A site's span is its line's bytes plus its terminating LF. A splice that starts at the site line's LF
>   therefore overlaps the site, and the replacement region includes the lines it inserts.
>
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-110, E-111. Controls: B1, B2, B3, B4, B6.

- Purpose: Fixes the boundary cases of splice overlap and site spans (the LF-inclusive span of Stage 1 D4).
- If authorized: A splice starting at a site line's LF overlaps the site; the replacement region includes inserted lines (215 region lines rather than 203).
- If not authorized: The boundary cases are unspecified; the region count would not be determined; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter than v4 (more regions attributed).

***

## R6.CTX.1

Decision basis: `v3 D1-D4`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTX.1** Preregistration. The context rule was decided at S0, before any implementation output. It
> is stated per frozen s3 value and per indicator. Its authority is r6's adoption. Its counts at `T1'`
> are reported, never tuned.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-076. Controls: none (definition).

- Purpose: Preregisters the context rule at S0, per frozen s3 value and indicator, with its counts reported and never tuned.
- If authorized: The mapping is fixed before any counts; T1' counts cannot be used to adjust it.
- If not authorized: The context rule loses its preregistration requirement; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserves preregistration (v3 D2).

***

## R6.CTX.4

Decision basis: `v3 D1-D4`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTX.4** Meaning. Context is required for meaning exactly when the frozen record does not establish
> that the qualification is visible on the site's own line. A `per unit` status stays on the required
> side: it means the qualification was established by a unit's correction, which may sit in a
> neighbouring sentence. The mapping from each frozen s3 value to `meaning_context` is part of the A1
> configuration (sec. 27):
>
> | Frozen s3 value | Sites at `E` (informative) | `meaning_context` |
> |---|---|---|
> | visible (names the hypothesis); rewritten at deletion | 194 | false |
> | visible (P0/P1/P2 disposition) | 144 | false |
> | visible (applied splice) | 5 | false |
> | visible (none: the (NR) corollary ...) | 3 | false |
> | n/a | 136 | false |
> | not determined: Q3 census | 81 | true |
> | not determined | 28 | true |
> | per unit regression audit (#1468) | 45 | true |
> | per unit Q1 corrections (Step 2) | 28 | true |
> | per unit Step-2 phase | 15 | true |
> | per unit R6 corrections (Step 2) | 9 | true |
> | per unit R1/R2 scoping | 8 | true |
> | per unit Q2 | 1 | true |
>
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-079, RV-012, V2-032. Controls: K1, K3, K4.

- Purpose: Defines when context is required for meaning and fixes the s3-to-`meaning_context` mapping, with `per unit` on the required side.
- If authorized: Sites with a `per unit` status require context (12 meaning-context failures rather than 8).
- If not authorized: The mapping, or the `per unit` reading, is undecided; narrowing `per unit` to false would remove 4 failures; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter reading kept (v3 D2: "per unit stays true").

***

## R6.CTX.12

Decision basis: `v3 D1-D4`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTX.12** For LIST and TABLE sites the neighbour context of R6.CTX.2 is kept in addition to the
> structure contexts of R6.CTX.11: a change of either gives the result of R6.CTX.6.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1367. Controls: K7.

- Purpose: Keeps the neighbour context for LIST and TABLE sites in addition to the structure contexts.
- If authorized: A change of either context gives the result of R6.CTX.6.
- If not authorized: Only the structure contexts would apply to LIST and TABLE sites; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter than D2's wording; the v4 review found it correct.

***

## R6.OUT.14

Decision basis: `R-D labels`, class (iii) no GitHub record; `A-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.OUT.14** Durable evidence (A-D5, C3, R-D5). Acceptance is recorded only by landing it on `main` in
> a landing record, the result commit. The landing merges only with the owner's approval (AGENTS.md
> sec. A.50 item 1), which the record quotes with author and time; the tool does not read or check that
> quotation. The record commits:
>
> - the result, compressed deterministically: `result.json.gz`, the gzip of the exact result bytes with
>   a modification time of 0, no file name, compression level 9 and the operating-system field 255; the
>   sha256 of the uncompressed bytes decides, and the compressed bytes' sha256 is recorded as well;
> - the admission snapshot of sec. 11, and its sha256;
> - the reproducibility recipe: the commits, including `F` and `T`; the configuration, pin table,
>   engine, adapter and workflow blob hashes; the exact command; and the tool version.
>
> CI run ids, job ids and log references are recorded as provenance only (AGENTS.md sec. A.42 item 2).
> Committing a result preserves it; it never makes an invalid run acceptable. The predicate of
> R6.OUT.12 is re-checked from the committed data before the landing merges.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-097. Controls: TR46.

- Purpose: Requires acceptance to be recorded only by an owner-approved landing record on `main` that commits the deterministic compressed result, the admission snapshot and the reproducibility recipe.
- If authorized: No result is accepted until it lands; a compressed blob whose uncompressed hash differs is refused (TR46); CI identifiers are provenance only.
- If not authorized: Durable evidence for tool results is unstated in r6, although AGENTS.md sec. A.42 items 1-2 and sec. A.50 item 1 still require its substance; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserves v5.5's durable evidence; the clause "the tool does not read or check that quotation" is the same boundary as R6.STAT.4.

***

## R6.OUT.15

Decision basis: `R-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.OUT.15** Offline replay (C3, F2). `replay --snapshot <path> --out DIR` recomputes the result from
> git objects and the committed snapshot alone. Admission is taken from the snapshot and written as
> `"admission": {"mode": "replay", ...}`. For op C, every delegated and native class is decided from the
> snapshot's delegated evidence (sec. 11). Replay does not call the host, clone the repository, build
> PDFs or rerun any checker. It re-applies the tool's own verification rules of sec. 13 to the recorded
> host records, hashes and checker outputs and to the git objects, for example: the TeX stamps and path
> set; LEDGER.json against `H` plus its splices and the recorded census values; SC-42's committed file
> against the recorded `--verbose` output; and the recorded `pdf` and `ci` records against `X`'s ids and
> the artifact hash. Every recorded result file must hash to the sha256 recorded beside it. Apart from
> the admission field, the replay's output equals the committed result byte for byte (canonical JSON,
> R6.OUT.19), for op B and op D results as well as for op C results. A replay is never acceptable as a new
> run. One thing remains host-attested and cannot be reproduced offline: that the snapshot was genuine
> when it was taken.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-098. Controls: TR45-opB.

- Purpose: Specifies offline replay from git objects and the committed snapshot alone, re-applying the tool's verification rules to the recorded host records.
- If authorized: A committed result can be re-established without the host; a replay is never acceptable as a new run.
- If not authorized: No offline replay is specified, so a committed result could be re-checked only by a new host run; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Adds a check (TR45-opB); the snapshot's genuineness at capture stays host-attested.

***

## R6.PROF.9

Decision basis: `R-D labels`, class (iii) no GitHub record; `v5.5.9 final D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.PROF.9** **Where the tool is stricter than P.** The tool computes and records P's per-edit
> result for items 5 and 6 in every case, including a refusal, so no item-5 or item-6 verdict differs
> from P's. It refuses three kinds of input that P, which has no splices, would not refuse, each because
> it is an invalid or ambiguous input: (i) a splice for the variant P does not select (the frozen ledger
> then misrepresents the frozen edit list); (ii) one splice covering two edits (the ledger schema gives
> each splice exactly one edit `id`), even where its bytes equal P's combined application; (iii) chained
> edits: a later edit's selected occurrence lies wholly or partly inside an image an earlier edit
> inserted, or spans the point where an earlier edit's image, possibly empty, was inserted, so that in
> the segment model it crosses more than one segment. No set of disjoint splices at `H` can express such
> an application, and a frozen plan containing one is invalid.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-121. Controls: S11-58g, S11-57c, S11-58j, S11-58k.

- Purpose: States the three input classes the tool refuses beyond P, while recording P's per-edit items 5 and 6 results in every case.
- If authorized: Unselected-variant splices, two-edit splices and chained edits are refused; no item-5 or item-6 verdict differs from P's.
- If not authorized: These inputs would not be refused; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter than P.

***

## R6.RULE.2

Decision basis: `S1-D1 to S1-D3`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.RULE.2** **Allow rule.** Its fields: `id` (never reused); `profiles` it addresses;
> `scope.files`, exact paths, mirrors named explicitly; `matcher.literal`, which must contain the
> trigger, defined as the profile match span of each fingerprinted sentence at `recorded_at`;
> `matcher.context`, required co-occurring literals in the sentence or its neighbouring sentences (for
> example the enumerated list); `matcher.negative`, literals or regexes that must not match;
> `context_required`; `max_instances`, equal to the number of fingerprints; `fingerprints`, each
> `{file, sentence_sha256, context_sha256, negative_allowance}`, where the optional `negative_allowance`
> maps a negative literal to the number of its matches in that exact fingerprinted sentence;
> `recorded_at`, the commit at which the fingerprints were taken; `positive_examples` and
> `negative_examples`, at least one of each, which become controls; `reason`, the semantic reason in one
> or two sentences; `author`. The reviewer and the review are a separate review record bound by blob
> (sec. 11). Owner approval is procedural and is not a rule field (R6.REC.3).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-128, V2-048, RV-015. Controls: A6r, A8r, A7r, E-A6r, E-A8r, lint-ok.

- Purpose: Defines the allow-rule schema, including the fingerprint field `negative_allowance` (S1-D1 option B).
- If authorized: A fingerprint may carry an exact per-literal allowance bound to one sentence.
- If not authorized: The schema has no allowance; W1-c's lines would FAIL `rule-negative-match`, contradicting RT-D, unless `finit` were dropped from the negative list; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: A narrowly bounded exception to the negative matcher; the alternative (dropping `finit` from the list) would weaken it for every sentence. The last sentence ("Owner approval is procedural") rests on the line-95 decision.
- FLAG, earlier designs: v5.1 had no allowance, so W1-c's lines were FAIL `rule-negative-match`; option B permits one exact match per fingerprinted sentence.

***

## R6.RULE.4

Decision basis: `S1-D1 to S1-D3`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.RULE.4** For a hit, the steps run in this order:
> 1. If no allow rule has the hit's file in scope, with a literal covering the trigger and a context
>    matcher that holds, the hit stays REVIEW_REQUIRED `unclassified`.
> 2. If any deny profile matches the sentence, the result is FAIL `deny-match`. Deny takes precedence.
> 3. The rule's negative matcher is applied to the whole sentence, with every negative literal counted.
>    The allowance for the sentence is the `negative_allowance` of a fingerprint only if all of the
>    following hold, and is zero otherwise: the hit's file is the fingerprint's `file`; the sentence's
>    sha256 equals the fingerprint's `sentence_sha256`; the context sha256 equals the fingerprint's
>    `context_sha256`, whether or not the rule sets `context_required`; and that fingerprint has not
>    already granted its allowance to another sentence in this tree. If, for any negative literal, the
>    sentence has more matches than the allowance grants, the result is FAIL `rule-negative-match`. The
>    allowance is bound to one fingerprint, that is, one fingerprinted sentence at one fingerprinted
>    location; it is never a global count and cannot be used by any other sentence, file or location.
> 4. If the sentence or, when required, the context differs from every fingerprint, the result is
>    REVIEW_REQUIRED `rule-fingerprint-mismatch`.
> 5. If the rule has already been applied `max_instances` times in the tree, the result is FAIL
>    `rule-overreach`.
> 6. Otherwise the hit is classified by the rule.
>
> A fingerprint with no `negative_allowance` grants none. A literal's matches are counted as
> non-overlapping matches of the literal (or regex) in the sentence's source bytes. The explanation of
> the hit records each step with its result (sec. 7).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-130, V2-050, V2-052. Controls: L1, L2, L3, L4, S1r, V7a, V7c, A5r, A5r-generic, E-L1, E-L3,
> E-S1r, rule-negative, WB1, WB4, WB6, WB7.

- Purpose: Fixes the order of allow-rule application, with deny taking precedence and the allowance bound to one fingerprint once per tree.
- If authorized: A negative-literal match is tolerated only within one exact sentence's allowance at one location, once per tree; anything else FAILs.
- If not authorized: As for R6.RULE.2; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: As for R6.RULE.2; deny still overrides everything.
- FLAG, earlier designs: As for R6.RULE.2.

***

## R6.RULE.7

Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.RULE.7** **Case.** Literal entries of an allow rule's negative matcher are matched
> case-insensitively, for every allow rule; a regex entry keeps its own flags. Allowances count
> case-insensitive matches. **Matching on source bytes.** Every literal of an allow or deny rule
> (trigger, context, negative, fingerprinted sentence) is matched against the source bytes of the file
> as committed, after the splitter's whitespace normalization (sec. 8), never against rendered text
> (for example a context literal `\mathrm{SU}(3)`, as the source line holds it, not "SU(3)").
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-133. Controls: WB15, L2, V7a.

- Purpose: Matches negative literals case-insensitively and matches every rule literal on source bytes (Stage 1 D8).
- If authorized: Literals cannot be evaded by case or by rendering differences.
- If not authorized: Case and rendering are unspecified; a context literal could be matched against rendered text; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter.

***

## R6.RULE.8

Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.RULE.8** **`rule-stale` scoping.** REVIEW_REQUIRED `rule-stale` (a fingerprinted sentence no
> longer present) is evaluated on every tree except those that are proper ancestors of the rule's
> `recorded_at`, computed from parsed parents (R6.REC.17). A candidate `X`, `C`, `L` or `M`, and
> `recorded_at` itself, are always evaluated. `result.json` lists, per tree, the rules not evaluated for
> staleness and why. At `recorded_at` a missing fingerprint is a lint failure of the rule (R6.RULE.10),
> not a `rule-stale` item.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-134, V2-028. Controls: S2r, WB5, E-S2r, GV3.

- Purpose: Scopes `rule-stale`: not evaluated on proper ancestors of `recorded_at`; always evaluated on the candidates and on `recorded_at`, with skipped rules listed (Stage 1 D7).
- If authorized: A fingerprint missing on an ancestor of `recorded_at` raises no item; at `recorded_at` it is a lint failure.
- If not authorized: The scope of `rule-stale` is unspecified; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Narrows where `rule-stale` is raised (proper ancestors are excluded); every candidate and `recorded_at` stay covered, and the skipped rules are reported.
- FLAG, earlier designs: Narrows v2: DESIGN-v2.md sec. 3.3 (V2-028) makes `rule-stale` REVIEW_REQUIRED whenever "a rule's fingerprinted instance occurs nowhere in the tree", with no scope; r6, like v6.0e (E-134), does not raise it on proper ancestors of `recorded_at`, where the fingerprinted text had not yet been written.

***

## R6.RULE.9

Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.RULE.9** **Residual testing.** No rule ever deletes text from the line or sentence before
> testing. A classified hit's sentence is tested whole, with the classified literal in place: every
> deny profile (step 2) and the rule's negative matcher (step 3) are applied to the whole sentence, and
> every other profile's hits in it are decided on their own.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-134, V2-051. Controls: V7a, WB2, WB12, A5r.

- Purpose: Forbids deleting text before testing: a classified hit's sentence is tested whole.
- If authorized: Deny profiles and negative matchers see the whole sentence.
- If not authorized: Residual testing by deletion would be possible; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter than v2's residual-test mutation.

***

## R6.REC.6

Decision basis: `DI-2`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.REC.6** A record fails, with FAIL `record-invalid`, on any of these: a schema or field error, or
> a missing field; no review record naming exactly this record's blob, or a review record naming another
> blob; `reviewer` equal to `author`; a review whose `verdicts` do not cover every item id of the record,
> or any item not `accept`; a duplicated item id or verdict; a `reviewer` value that points to a tool
> run, a CI run, a check run or an Issue (a URL or run id rather than a person); a record entry at a
> path that is not a regular file (R6.REC.17); a record not read from the git object store.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-140, E-141. Controls: O1, O2, O3, O5, R3-F2, R4-B3, R4-B3-DUP, R5-N6, GV6.

- Purpose: Lists the conditions under which a record fails lint with `record-invalid`.
- If authorized: Records without an exact review, with self-review, incomplete verdicts or non-person reviewers FAIL.
- If not authorized: The record lint loses its failure conditions; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter.

***

## R6.REC.7

Decision basis: `DI-2`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.REC.7** **Supersession and lineage**, for every record kind that carries `supersedes`. Each
> `supersedes` names a `{path, blob_sha256}` that exists in the object store at or before `F` and is a
> record of the same kind, schema and lineage; a first record has `supersedes: null`. A record's lineage
> is its `record_id`, a non-empty string at the record's top level; for the configuration it is its
> `config_id` (sec. 25). `record_id` is immutable within a lineage: a superseding record has the same
> kind, schema and `record_id` as the record it names. Sharing a `record_id` within one lineage is not
> reuse; a `record_id` carried by two records that do not lie on one `supersedes` chain is. Each of the
> following is FAIL `record-invalid`:
> - a chain naming an id or blob that never existed as a record (for example an off-repository draft);
> - a record without a valid `record_id` (missing, empty or not a string) that supersedes another
>   record or is named by a `supersedes`;
> - a `supersedes` naming a record whose kind, schema or `record_id` differs, at any step of the chain;
> - a `supersedes` naming a predecessor that does not itself pass this lint, read from the object store
>   at or before `F` and verified independently of the superseding record (its own review and, where it
>   widens the record it supersedes, its widening review);
> - a cycle in a `supersedes` chain;
> - ambiguous ancestry: two records superseding the same predecessor, among the records in the audit
>   directory and the plan's record directory at `F` and the records the run reads; or a lineage with
>   two heads used in one run, a head being a record of the lineage that no other record the run reads
>   (the records the configuration references and every record their chains name) supersedes;
> - a reused `record_id`.
>
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-141. Controls: S4a, LN1, LN2, LN3, LN4, LN5, LN6, LN7, LN8, LN10, R6-G6.

- Purpose: Specifies supersession and lineage of records by `record_id` (DI-2, option A, narrow).
- If authorized: Chains to nonexistent records, kind or schema changes, cycles, ambiguous ancestry and reused ids FAIL `record-invalid`.
- If not authorized: Lineage is unspecified; superseding records could change kind or identity; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter.

***

## R6.REC.14

Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.14** **Examples and fingerprints.** Each fingerprint must be reproduced by a sentence of its
> named file at `recorded_at`. Each example and countercontrol must behave as stated. Every fingerprinted
> sentence, read at `recorded_at` in its named file, must be classified PASS by its own rule through
> steps 1-6 of R6.RULE.4, with its own allowance. Every `negative_allowance` must equal, literal by
> literal, the number of matches of that negative literal in its fingerprinted sentence, and may name
> only literals of the rule's negative matcher. A rule's positive examples include each fingerprinted
> sentence in full, not a fragment of it. Otherwise the record fails the lint (FAIL `record-invalid`).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-163. Controls: A6r, A8r, A9r, A11r, WB10, WB11.

- Purpose: Requires each fingerprinted sentence to PASS its own rule and each allowance to equal the exact literal count (Stage 1 D1).
- If authorized: A rule whose own sentence does not PASS, or whose allowance is inexact, is `record-invalid`.
- If not authorized: The lint would not catch a self-contradictory rule; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: New and stricter.

***

## R6.REC.18

Decision basis: `R-D labels`, class (iii) no GitHub record; `v6.0e line 54`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.18** **Execution identity.** An acceptable result is computed by the tool files and run by
> the workflow that the configuration at `F` pins, in the repository it names:
> 1. **The run record.** The tool reads its own run record by the run id the host assigns, from the
>    host's REST API in the repository the job runs in: the repository id, the head repository id, the
>    event, the head branch, the workflow path and the run's `head_sha`. `T`, the tool commit, is that
>    `head_sha`. The run's `repository.id` and `head_repository.id` must both equal the configuration's
>    `repository_id`, and its `event` must be `push` or `workflow_dispatch`.
> 2. **The tool's files and the workflow.** `T`'s tree is read through the verified reader. Under
>    `tools/ledger_coverage/`, together with the entry point `tools/ledger_coverage.py`, it must hold
>    exactly the files of the configuration's `tool.files`, each a regular file whose blob sha256 equals
>    its pin; a further file, a missing file, a differing blob, or a symlink, submodule or other
>    non-regular entry refuses. The run record's workflow path must equal `tool.workflow.path`, and the
>    blob at that path in `T` must equal `tool.workflow.blob_sha256`. The workflow runs the tool with
>    `python3 -I -B` from a checkout of `T`. Before evaluating anything, the tool compares the entry point
>    and every file under `tools/ledger_coverage/` in that checkout with `T`'s tree: the same set of
>    paths, each byte-identical. Any difference, including a file on disk that `T` does not hold (for
>    example a compiled-bytecode file), refuses.
> 3. **Evaluated commits are inputs.** The commits evaluated (`X`, `C`, `L`, `M`, `H` and `E`) are
>    explicit full ids, read through the verified reader and recorded. They are never the run's
>    `head_sha`.
> 4. **The consumer repeats it.** The consumer repeats points 1-3 and the `uses:` check of point 5 for
>    the producing run itself (sec. 7), from the host's REST API and from its own verified object store,
>    against the configuration at `F` that the landing record names. A run whose repository, head
>    repository or event fails point 1, a `head_sha` other than the `T` the result records, or a tool or
>    workflow blob that differs from the configuration's pins is non-acceptance.
> 5. **Nothing unpinned executes.** In every run of the pinned workflow, no file outside `tool.files`,
>    the pinned workflow, the actions it names by commit id and the interpreter's own standard library
>    executes in the job, before or after the tool's own checks. The delegated and native checker runs
>    are outside this rule and are governed by sec. 13 (R6.DELEG.3).
> 6. **The tool commit is on `main`.** The tool refuses (ERROR `CONFIG_UNREVIEWED`, before any
>    evaluation) unless the run record's `head_branch` is `main`. The consumer requires `T` to lie on the
>    first-parent chain of `M`, the `main` resolved by `git ls-remote` as sec. 23 states, walked by the
>    verified reader.
>
> No command-line option, environment value or other configuration field sets `tool` or
> `repository_id`; they are read only from the configuration at `F`.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-147, E-148, E-149, E-150, E-155. Controls: TR14, TR14-tool, TR15, TR28-tool, TR28-consumer,
> TR29, TR29-tool, TR30, TR48, TR50, TR51, TR52, EI1, EI2, EI2-consumer, EI3, EI5, EI14.

- Purpose: Binds an acceptable result to the tool files, workflow and repository pinned by the configuration at `F`, with the tool commit on `main`.
- If authorized: Runs from another repository or event, off `main`, or with unpinned or extra tool files are refused, by the tool and by the consumer.
- If not authorized: Execution identity is unspecified; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserves v5.5.9's technical identity guarantees, pinned through the configuration at `F` rather than the authority record.

***

## R6.REC.19

Decision basis: `v6.0e line 31`, class (iii) no GitHub record; `v6.0e line 54`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.19** **The pre-run pin check.** The first step after the checkout and the fetch of `F`,
> before the entry point or any file of the checkout runs, is one fixed inline step of the pinned
> workflow, whose `name:` is exactly `pre-run pin check`, run as `python3 -I -S -B -c '<program>'` with
> the program given in the workflow text on its single `run:` line, so that it executes no file of the
> checkout. The workflow fetches `F` by its full id. The step refuses unless the environment value
> `GITHUB_REF` is `refs/heads/main` and `F` matches `^[0-9a-f]{40}$`. It reads the configuration blob at
> `F` with `git cat-file blob`, at the path the run passes to the tool as `--config`, and takes
> `tool.files`. It examines the entry point and the directory `tools/ledger_coverage/` on disk with
> `os.lstat`, never following a link: `tools` and every other parent directory of a checked path must be
> a real directory; every entry must be a regular file or a directory; the set of regular-file paths must
> equal the paths of `tool.files` exactly; and each file's sha256 must equal its pin. Any failure, a
> missing `F` or configuration, or an unreadable `tool.files` fails the step, and the job ends before any
> tool code runs. A workflow blob with no such step, more than one, or a `run:` value that is not one
> such line is refused by the review and fails the controls, whose runner extracts the program by this
> rule.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-151. Controls: EI8, EI9, EI10, EI11, EI12, EI13, EI15.

- Purpose: Specifies the pre-run pin check that runs before any file of the checkout.
- If authorized: The job ends before any tool code runs if a tool file is missing, extra or differs from its pin.
- If not authorized: An unverified file could execute before the tool's own checks; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserves the v5.5.9 pre-run check restored in v6.0c.

***

## R6.REC.20

Decision basis: `v6.0e line 54`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.20** **The import path.** The workflow invokes `python3 -I -B tools/ledger_coverage.py`. The
> entry point does not insert any directory of the checkout into `sys.path`; it loads the package
> `tools/ledger_coverage/` by its location. Before any import of a module not already loaded at
> interpreter start (only `sys` and `os` precede it), the entry point refuses unless the interpreter runs
> in isolated mode and no `sys.path` entry lies inside the checkout. The refusal is ERROR, exit 65, with
> the stop class `NOT_ISOLATED`, written to stderr as one JSON object with that class and the reason (RE-14). Because it fires
> before any import, it writes no `result.json`; it is, with USAGE, one of the two documented cases that
> write no `result.json`. The implementation exits 65 with a message and no class today; that is a
> verification defect, corrected in the tool revision.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-152. Controls: EI6.

- Purpose: Requires an isolated interpreter with no `sys.path` entry inside the checkout before any import.
- If authorized: A shadow module (for example hashlib.py) cannot execute; the refusal is ERROR `NOT_ISOLATED`.
- If not authorized: Import isolation is unspecified; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter than v5.5.9 (control EI6). Records a known implementation defect (exit 65 with no class).

***

## R6.REC.21

Decision basis: `v6.0e line 54`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.21** **The workflow's executable dependencies.** The pinned workflow executes only the
> pre-run check, the entry point, fixed `git` commands and the actions it names by commit id. The tool
> and the consumer check the workflow blob at `T` by a line rule on its raw text, with no YAML parser.
> The blob is refused if any line:
> - contains `uses`, in any letter case, and does not match
>   `^\s*(- )?uses: <owner>/<repo>[/<path>]<AT><40 lowercase hex>\s*$`, where `<AT>` denotes the
>   at-sign character (U+0040), written here by name, and with literal `<owner>` and `<repo>` names;
> - begins, after its indentation and any number of `-` or `---` markers each followed by whitespace
>   (the prefix `^\s*((-|---)\s+)*`), with `"`, `'`, `{`, `[`, `?`, `&`, `*` or `!`;
> - contains a colon followed by any whitespace and then `{`, `[`, `&`, `*` or `!` (the pattern
>   `:\s+[{[&*!]`).
>
> The rule only refuses; a form it refuses that YAML would read harmlessly is written another way in the
> pinned workflow.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-153. Controls: EI7, EI7-tool.

- Purpose: Refuses unpinned workflow dependencies by a raw-text line rule.
- If authorized: Workflows with unpinned `uses` or the listed YAML forms are refused.
- If not authorized: Workflow dependencies are unchecked; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter than v5.5.9.

***

## R6.REC.22

Decision basis: `v6.0e line 54`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.22** **Workflow content review.** The rest of the workflow's content is checked against this
> list when the configuration's review covers `tool.workflow`, and the pin then fixes it: its triggers and
> inputs (the run receives `F` and the configuration path as inputs, and a run without them fails the
> pre-run check); `permissions` read-only except artifact upload; a GitHub-hosted `runs-on`, with no
> `container:` and no `services:`; no `env`, `GITHUB_ENV` or `GITHUB_PATH` change of `PATH`, `LD_*`,
> `GIT_*` or `PYTHON*`; no `shell:` override; the named actions only (no `setup-*` action, and no
> composite or docker action that installs or downloads executables or refers to other actions by tag);
> the exact run lines (the fetch of `F`, the pre-run check, and the entry point's command); the inputs
> reach the shell only through `env:`, and the fetch of `F` is `git fetch --no-tags -- origin "$F"`, with
> no `run:` line interpolating `${{ inputs.* }}`; no `continue-on-error`, and no `if:` on the steps after
> the pre-run check; no reusable workflow.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-154. Controls: TR15, TR50, EI7.

- Purpose: Lists the workflow content the review checks before the pin fixes it.
- If authorized: Triggers, permissions, runners, environment, actions and run lines are reviewed against a fixed list.
- If not authorized: The workflow review has no fixed list; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserved.

***

## R6.REC.24

Decision basis: `R-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.24** **The admission object.** `result.json` records `config.admission`, an object with a
> `mode` field: `"chain"`, `"control-harness"` or `"replay"`. Its mode is `"chain"` only when
> configuration admission and execution identity held, and only then does it carry `snapshot`:
> - the run record fields read: run id, repository id, head repository id, event, workflow path and
>   `head_sha` (`T`); the workflow file's blob sha256 at `T`; the tool blob hashes at `T`;
> - the evaluated commits `E`, `H`, `X`, `C`, `L` and `M`;
> - `F`, the pin table's `{path, blob_sha256}`, and the configuration's and its review record's
>   `{path, blob_sha256}`;
> - the delegated evidence, for every delegated and native class of sec. 13, at `X` and, where `C`
>   differs, at `C`: the host records the tool read for the class, as the host returned them, in
>   canonical JSON; the sha256 of every artifact and result file the class used; the outputs of every
>   checker the tool ran natively (for each run, the checker blob sha256, the exact command line, the
>   working directory, the exit status, and the complete bytes of each result file it wrote and of each
>   output the class compares); and the class's own recorded re-derivations;
> - the sha256 of the canonical JSON of the snapshot itself.
>
> Only `"chain"` is acceptable (sec. 7). The control harness (sec. 17) may admit a draft configuration
> without its chain; its results carry `mode: "control-harness"` (with any simulated snapshot the control
> supplies, never mode `"chain"`), are written as `control-result.json` with `"harness": true`, and are
> never written as an acceptable result. The offline replay writes `mode: "replay"`.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-158, E-159, E-145. Controls: TR5, TR5-sim, X11, TR45-opB, TR46.

- Purpose: Defines the admission object and its three modes; only `"chain"` is acceptable.
- If authorized: Harness and replay results can never be written as acceptable results.
- If not authorized: The admission modes are unspecified; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserved.

***

## R6.DENY.5

Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words; `S1-D2`, class (iii) no GitHub record; `V5-D2`, class (ii) session-written record on GitHub, no owner words; `S1-D1 to S1-D3`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.DENY.5** **Outstanding rule content.** The content of the plan's rule records is transferred to
> the plan amendment as outstanding obligations, each a named blocker on the execution it gates (sec.
> 32): the deny rules DR-1, DR-3, DR-4 and DR-5 with their definitions and patterns (the identifiers
> DR-1d and DR-2 are retired, sec. 33, and never reused); the W1 allow rules, including W1-c's
> fingerprints and its `negative_allowance`; the W2 allow rules, replacing P's corresponding
> `RESIDUAL_ALLOW` and `EXPLAINED` entries and its blanket `(A1)` strip; and the `resid` pattern with its
> parts resid-a, resid-b and resid-c.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1001, E-1002, E-1003, E-1004, E-1005, E-1006, E-1020, E-1021, E-1022, E-1024, E-1025,
> E-1026, E-1027, E-1032. Controls: none (OBL-3).

- Purpose: Transfers the rule content to the plan amendment as outstanding obligations (named blockers).
- If authorized: The plan cannot reach the gated steps until the deny rules, the W1 and W2 allow rules and `resid` exist as reviewed records.
- If not authorized: The rule content would have no stated obligation; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Adds a blocker; leaving out resid-b and resid-c (V5-D2) would weaken REVIEW coverage (V26); W1-c's allowance is the bounded exception of S1-D1; the W2 allow rules rest on no owner decision.
- FLAG, earlier designs: W1-c's `negative_allowance` as for R6.RULE.2.

***

## R6.DENY.6

Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.DENY.6** **Accepted residual: V4 and V27 (for decision at adoption; not adopted by this
> draft).** The question: with the deny rules DR-1, DR-3, DR-4 and DR-5 and the review profiles of the
> A1 configuration, the added text of control V4 ("the framework's sixth structural property, finiteness
> of the bijection") and of control V27 ("The framework's sixth structural property is finiteness of the
> substratum", added alone and as the edited glossary line) produce no hit of any review or deny profile.
> The expectation for both would then be PASS with zero hits, recorded as an accepted residual after the
> candidate rule DR-2, which caught V4, was not adopted. That decision (V5-D1) is recorded only in
> paraphrase, in the session-written #1169 comment 7099655517. Consequences of confirming: an added sentence that asserts finiteness as an ordinal
> structural property of the bijection or substratum, in the forms of V4 and V27, passes the tool
> undetected; the original item 7 check also misses it; its detection rests on review outside the tool;
> V4 and V27 are kept as controls so that a change in their outcome is visible. Consequence of
> restoring: V4 (and V27) expect FAIL `deny-match`, which requires a plan rule record that catches them
> (a rule of the DR-2 form under a new identifier, since DR-2 is retired and never reused (sec. 33);
> plan content under R6.DENY.1, reviewed with the deny set), and the
> reconciliation of that rule against the negative examples. The owner decides at adoption among (a)
> confirming the PASS expectation knowingly, (b1) restoring the FAIL expectation of V4, V27 and
> V27-glossary, with V15 REVIEW_REQUIRED, and (b2) restoring it for V15 as well, which needs a second
> new rule, of the DR-1d form, since a rule of the DR-2 form does not match V15's text (R6.PUR.9). Until then the
> expectations are deferred. The decision covers V4, V27, V27-glossary and V15 together (RE-1). Until it is made, each of the four
> rows carries both candidate expectations, each marked "not authoritative; decided at r6 adoption",
> and the gate reports `deferred-expectation` for it and never holds (sec. 16.5).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1001, V2-080, RE-1. Controls: V4, V27, V27-glossary, V15.

- Purpose: States the accepted-residual question for V4 and V27 and its consequences, for decision at adoption.
- If authorized: As for R6.PUR.9.
- If not authorized: As for R6.PUR.9.
- Safeguards affected: As for R6.PUR.9.
- FLAG, earlier designs: As for R6.PUR.9.

***

## R6.CTRL.7

Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTRL.7** A control-only input is a pinned object (commit, path, git blob id and sha256) named by
> one control in the controls file. It is read only by the control that names it, changes no profile's
> scope and no production result, and adding or changing one changes the controls file and is reviewed
> with it. No historical text is constructed for this purpose. DR-3's witness is such an input: the
> sentence of `AGENTS.md` at `H`, lines 37-39 (blob 12a9281fb88c14395b6715a3bf4b4f6b030f433c, sha256
> d87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27), which RT-DR3W scans at `H` and,
> as its countercontrol, in `X_rep` (R6.EVID.8), whose `AGENTS.md` is `H`'s with the ledger's splices
> applied.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1011, E-1013, E-1014, E-1015, OC-3. Controls: RT-DR3W.

- Purpose: Defines control-only inputs and fixes DR-3's witness as the sentence of AGENTS.md at `H`, lines 37-39.
- If authorized: DR-3 is tested on a real sentence; the production scan is not widened; no historical text is constructed as a witness.
- If not authorized: DR-3 would have no real witness; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserves v6.0e; rests on V5-D1's second limb.

***

## R6.CTRL.14

Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words; `S1-D1 to S1-D3`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.CTRL.14** The rule controls are L1-L4, V1-V27 (V7a, V7b, V7c; no V8), A1r-A12r, S1r, S2r,
> WB1-WB15, N-W, their engine analogues and the rule-lint controls. v2's class `rule-invalid` is
> `record-invalid` (exit 20) throughout. V2 FAILs by DR-3 and V3 by DR-4; v2's fingerprint-mismatch and
> residual-test basis for them is superseded, since no rule deletes text and overlap is strict (sec.
> 10). V1 FAILs by DR-1, alternative b. The deny rules and the seed allow rules are plan records adopted
> with the amended plan; the controls use the current rule files as pinned control inputs and test the
> rule mechanism (sec. 12).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1106, E-1107, E-1108, E-1109, E-1110, E-1111, E-1112, E-1113, E-1114, E-1115, E-1116, E-1117, E-1118, E-1119, E-1120, E-1121, E-1122, E-1123, E-1124, E-1125, E-1126, E-1127, E-1128, E-1129, E-1130, E-1131, E-1132, E-1133, E-1135, E-1136, E-1137, E-1138, E-1139, E-1140, E-1141, E-1142, E-1143, E-1144, E-1145, E-1146, E-1147, E-1148, E-1149, E-1150, E-1151, E-1192, E-1193, E-1194, E-1195, E-1196, E-1197, E-1198, E-1199, E-1200, E-1201, E-1202, E-1203, E-1204, E-1205, E-1206, E-1232, V2-074, V2-075, V2-076, V2-077, V2-078, V2-079, V2-081, V2-082, V2-083, V2-084, V2-085, V2-086, V2-087, V2-088, V2-089, RV-050, RV-052. Controls: A1r, A2r, A3r, A4r, A5r, A5r-generic, A6r, A7r, A8r, A9r, A10r, A11r, A12r, E-A1r, E-A2r, E-A3r, E-A6r, E-A8r, E-L1, E-L3, E-S1r, E-S2r, L1, L2, L3, L4, S1r, S2r, V1, V2, V3, V3-countercontrol, V4, V5, V6, V7a, V7b, V7c, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V27-glossary, WB1, WB2, WB3, WB4, WB5, WB6, WB7, WB8, WB9, WB10, WB11, WB12, WB13, WB14, WB15, lint-ok, rule-negative.

- Purpose: Fixes the rule controls (L, V, A, S, WB, N-W and lint) and the basis of V1-V3.
- If authorized: The control set is fixed; the V4-group rows follow the separate decision.
- If not authorized: The rule controls are unlisted; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserves v6.0e's controls.

***

## R6.CTRL.15

Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTRL.15** V4 adds "the framework's sixth structural property, finiteness of the bijection" to
> the file of a W1 rule. Under the deny set without DR-2 the sentence produces no hit, so the run is
> PASS: this is the V4 reversal. What it permits: a reintroduction of the counted premise in the form
> "sixth structural property, finiteness of ..." passes the deny profiles and the residual profile
> unclassified by any FAIL, and the original item 7 misses it as well. Its consequence: the tool does
> not detect that form, and detection rests on review of the residual hits. The reversal rests on an
> owner decision recorded only in paraphrase (V5-D1, in the session-written #1169 comment 7099655517). It is adopted or rejected by the owner at r6's adoption;
> approving this draft does not adopt it. Until that decision, V4, V27, V27-glossary and V15 each
> carry both candidate expectations, marked "not authoritative; decided at r6 adoption", and the gate
> reports `deferred-expectation` for each (RE-1). If the reversal is rejected, V4's expectation is FAIL `deny-match` and the deny set
> needs a rule matching that form, under a new identifier (DR-2 is retired and never reused, sec. 33),
> which is a plan-record change (sec. 12). V27 tests a sentence of the
> same form and rests on the same decision, as do V27-glossary and V15, whose candidates are
> REVIEW_REQUIRED `unclassified` and FAIL `deny-match`; V15's FAIL candidate needs, in addition, a rule
> of the DR-1d form under a second new identifier, since a rule of the DR-2 form does not match V15's
> text (R6.PUR.9, resolutions (b1) and (b2)).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: V2-080, RE-1. Controls: V4, V27, V27-glossary, V15.

- Purpose: Describes the V4 reversal: what it permits and its consequence.
- If authorized: As for R6.PUR.9.
- If not authorized: As for R6.PUR.9.
- Safeguards affected: As for R6.PUR.9.
- FLAG, earlier designs: As for R6.PUR.9.

***

## R6.CTRL.17

Decision basis: `R-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.CTRL.17** Split and dependent rows. RT-O9's own checks (the expected set of record-directory
> entries computed independently from the stand-in `F` tree, compared exactly; no unequal path; no
> `side-change-unclassified`) run and are gated whenever RT-O9 runs, independently of RT-L2. Its clause
> that RT-L2 still holds is the separate row RT-O9-L2, which depends on RT-L2 and is NOT RUN with
> RT-L2's release condition. TR45's op-C half is the row TR45-opC, NOT RUN until delegated evidence is
> recorded by native runs at `X` and `C`. EI14's branch-dispatch half is the row EI14-dispatch, NOT RUN
> until a dispatch of the pinned workflow on a branch holding `T'` is made, after the tool lands, under
> a launch the owner approves; EI14's other cases stay in EI14. The consumer halves of EI7, TR15, TR50,
> TR51 and TR52 are rows of their own (EI7-consumer, TR15-consumer, TR50-consumer, TR51-consumer,
> TR52-consumer), implemented in the tool revision; until then the gate reports them missing.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1218. Controls: RT-O9, RT-O9-L2, TR45-opB, TR45-opC, EI14, EI14-dispatch, EI7,
> EI7-consumer, TR15-consumer, TR50-consumer, TR51-consumer, TR52-consumer.

- Purpose: Splits dependent rows: RT-O9's own checks run independently of RT-L2; TR45-opC and EI14-dispatch are NOT RUN until their evidence exists; consumer halves are rows.
- If authorized: No actual failure is hidden behind a dependent NOT RUN.
- If not authorized: Dependent clauses would be merged with independent checks; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserved (Q6, Q14).

***

## R6.CTRL.19

Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.CTRL.19** The real-tree controls run in CI on real objects: RT-A, RT-E, RT-H0, RT-T0, RT-T, RT-C,
> RT-D, RT-D-gr58, RT-DR, RT-DR3W, RT-I7, RT-I7A, SW1, SW2, item11-T1p, N-W, RT-M, RT-SHIFT, RT-X, RT-L,
> RT-L2, RT-O9 and RT-O9-L2. v1's `verify-record` is `record` and `check-coverage` is `coverage`. Every
> figure a runner asserts today that is reproducible from inputs on `main` (among them RT-H0's 113/7/7,
> RT-A's and RT-E's 697, the RT-DR counts at `H`, RT-T0's site and region counts, RT-I7's split at `H`,
> RT-I7A and RT-C, and RT-D's 45 `resid` lines) is an asserted count in the expectation file, not an
> informational figure. A control whose verdict reads only what `H` and the ledger determine runs on
> `X_rep` (R6.EVID.8); a figure that needs T1' itself is an acceptance reference only for a run that has
> T1' among its inputs; its standing as evidence follows sec. 31. RT-C is PASS only with contract
> evidence; without it the expected result is the one the expectation file states for missing
> evidence. RT-T is NOT RUN until every reviewed record of sec. 14 exists. The two `not determined`
> H..T1' cases of sec. 6 are RET FAILs, and RT-T's expectation says so; it does not claim that no RET
> FAIL exists.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1134, E-1176, E-1177, E-1178, E-1179, E-1180, E-1181, E-1182, E-1183, E-1184, E-1185, E-1186, E-1187, E-1188, V1-115, V1-117, V1-119, V2-099, V2-100, V2-101, V2-103, V2-104, V2-105, V2-162, V2-163, V2-164, RV-028, RV-051, E-091, E-1010, V1-132, V1-136, OC-3. Controls: N-W, RT-A, RT-C, RT-D, RT-D-gr58, RT-DR, RT-DR3W, RT-E, RT-H0, RT-I7, RT-I7A, RT-L, RT-L2, RT-O9, RT-O9-L2, RT-T, RT-T0, RT-X, SW1, SW2, item11-T1p.

- Purpose: Lists the real-tree controls and makes reproducible figures asserted counts.
- If authorized: Figures become asserted counts; T1'-bound figures are conditional (OBL-23).
- If not authorized: Figures would be informational; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter.

***

## R6.CTRL.22

Decision basis: `DI-2`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTRL.22** The record controls are O1-O9 (O4 retired), N1, S4a, LN1-LN8 and LN10 (LN9 retired),
> and the record-lint controls R3-F2, R4-B3, R4-B3-DUP, R5-N6 and R6-G6. O1, O2, O3, O5 and O7 assert
> an emitted FAIL `record-invalid`, not only a lint problem; O6 asserts the emitted outcome, not only the
> absence of an ERROR.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1154, E-1155, E-1156, E-1157, E-1158, E-1159, E-1160, E-1161, E-1331, E-1332, E-1333, E-1334, E-1335, E-1336, E-1337, E-1338, E-1339, E-1340. Controls: LN1, LN2, LN3, LN4, LN5, LN6, LN7, LN8, LN10, O1, O2, O3, O5, O6, O7, O8, O9, R3-F2, R4-B3, R4-B3-DUP, R5-N6, R6-G6, S4a.

- Purpose: Lists the record controls and requires emitted FAIL `record-invalid`, not only a lint problem.
- If authorized: Record controls assert the emitted outcome.
- If not authorized: The record controls are unlisted; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter.

***

## R6.CTRL.23

Decision basis: `R-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.CTRL.23** The delegation controls are G1-G9 and G-A1; the output controls are X1-X11,
> S7-schema-and-checker, ACCEPT-SCHEMA and B4-MEANING; the admission, execution-identity and
> object-integrity controls are TR1-TR3, TR5, TR5-sim, TR13-TR15, TR14-tool, TR28-tool, TR28-consumer,
> TR29, TR29-tool, TR30, TR45-opB, TR45-opC, TR46, TR48, TR50-TR52 and their consumer halves, EI1-EI15
> with EI2-consumer, EI7-tool, EI7-consumer and EI14-dispatch, GV1-GV7 with GV6-disk, GV7-tool and
> GV7-consumer, the cache controls GV-CACHE, GV-CACHE-AFTER-READ, GV-CACHE-IMMUTABLE and GV-CACHE-KEY,
> CHAIN-REFUSAL, ADM-CONFIG-AT-F, CONFIG-LINT, O3-FILTER and K1-GRAPH. v1's RT-A' (op A with `--pin H`)
> is X1. GV4 includes the HP-merge case; EI6 includes its third case and the `json.py` and
> `importlib.py` shadow files; EI5 and EI7 include their countercontrols. TR1 applies to chain
> admission only.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1162, E-1163, E-1164, E-1224, E-1225, E-1226, E-1227, E-1228, E-1229, E-1165, E-1166, E-1167, E-1168, E-1169, E-1170, E-1171, E-1172, E-1173, E-1174, E-1207, V2-096, V2-097, E-1208, E-1209, E-1210, E-1211, E-1212, E-1213, E-1214, E-1215, E-1216, E-1217, E-1219, E-1220, E-1221, E-1222, E-1223, E-1246, E-1247, E-1248, E-1249, E-1250, E-1251, E-1252, E-1253, E-1254, E-1255, E-1256, E-1257, E-1258, E-1259, E-1260, E-1261, E-1262, E-1263, E-1264, E-1265, E-1266, E-1267, V1-116. Controls: G1, G2, G3, G4, G5, G6, G7, G8, G9, G-A1, ACCEPT-SCHEMA, B4-MEANING, S7-schema-and-checker, X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11,
> ADM-CONFIG-AT-F, CHAIN-REFUSAL, CONFIG-LINT, EI1, EI2, EI2-consumer, EI3, EI4, EI5, EI6, EI7, EI7-consumer, EI7-tool, EI8, EI9, EI10, EI11, EI12, EI13, EI14, EI14-dispatch, EI15, GV1, GV2, GV3, GV4, GV5, GV6, GV6-disk, GV7, GV7-consumer, GV7-tool, GV-CACHE, GV-CACHE-AFTER-READ, GV-CACHE-IMMUTABLE, GV-CACHE-KEY, K1-GRAPH, O3-FILTER, TR1, TR2, TR3, TR5, TR5-sim, TR13, TR14, TR14-tool, TR15, TR15-consumer, TR28-consumer, TR28-tool, TR29, TR29-tool, TR30, TR45-opB, TR45-opC, TR46, TR48, TR50, TR50-consumer, TR51, TR51-consumer, TR52, TR52-consumer.

- Purpose: Lists the delegation, output, admission, execution-identity and object-integrity controls.
- If authorized: The control set is fixed.
- If not authorized: These controls are unlisted; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserved.

***

## R6.CTRL.24

Decision basis: `S1-D2`, class (iii) no GitHub record; `R-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.CTRL.24** The plan-mapping controls are S11-1 to S11-14 (S11-2 composed of S11-2a, S11-2b and
> S11-2c) and the per-edit controls S11-56, S11-57a-d, S11-58a-f and S11-58g-k. S11-56 tests the tool's
> side only: the equality of its result with the plan's own checker is an outstanding obligation (sec.
> 18). S11-7 is implemented in the tool revision; it plants a literal and a DR-5 match and requires both
> to FAIL.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1234, E-1235, E-1236, E-1237, E-1238, E-1239, E-1240, E-1241, E-1242, E-1243, E-1244, E-125. Controls: S11-1, S11-2, S11-2a, S11-2b, S11-2c, S11-3, S11-4, S11-5, S11-6, S11-7, S11-8, S11-9, S11-10, S11-11, S11-12, S11-13, S11-14, S11-56, S11-57a, S11-57b, S11-57c, S11-57d, S11-58a-f, S11-58g, S11-58h, S11-58i, S11-58j, S11-58k.

- Purpose: Lists the plan-mapping and per-edit controls; S11-56 tests the tool's side only, and parity with P is an obligation.
- If authorized: The control set is fixed; parity stays outstanding (OBL-1).
- If not authorized: These controls are unlisted; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserved.

***

## R6.PLAN.8

Decision basis: `v3 D1-D4`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.PLAN.8** Item 7 (a corpus grep for `\bA1\b` and related terms with only ledger false positives,
> and zero posit counts "Fourteen", "six structural" and "sixth of") maps, as frozen, to `terms --commit
> X --profile item7-literal`. The literal check is kept as the named countercontrol `item7-literal`, with
> RT-I7. Item 7 as frozen does not pass at T1' or at `X_rep`: seven lines contain the legitimate count of
> the bijection's properties (W1); RT-I7 asserts the counts at `X_rep` (R6.EVID.8), and the measurement
> at T1' is historical. Countercontrol: the H-form
> "Fourteen items" reinstated, which must FAIL in both the literal check and DR-5 (S11-7). DR-5 is a plan
> record. RT-I7A runs the proposed amendment check of R6.PLAN.18 at `H` and at `X_rep` as a test of the
> mechanism.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1275, E-1283, OC-3. Controls: S11-7, RT-I7, RT-I7A.

- Purpose: Maps item 7 as frozen to the literal check, kept as the countercontrol `item7-literal`, with a restatement of item 7 as a plan amendment.
- If authorized: Item 7 as frozen FAILs at T1' and at `X_rep`; passing needs a reviewed plan amendment.
- If not authorized: Item 7 would have either no mapping or the literal grep as the acceptance criterion, which no tree keeping W1's legitimate sentences can pass; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: The literal check survives as a countercontrol; acceptance moves to a reviewed amendment.
- FLAG, earlier designs: Permits the plan to pass, after a reviewed amendment, with item 7's literal grep failing; v3's alternative was that the literal grep must stand.

***

## R6.A1CFG.7

Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.A1CFG.7** Acceptance criterion S13: the configured engine reproduces, item by item, every A1
> control outcome of sec. 17 that the expectation file states, including the record-directory controls
> RDIR-1 to RDIR-25 and RDIR-12b, RT-O9 (with its dependent clause as in OBL-14) and the item-2 controls
> I2-1 to I2-8. Rule outcomes (deny, allow, `resid`) are measured with the plan's rule files as pinned
> control inputs; the rules themselves are plan records adopted at `F` (sec. 12, OBL-3). The expected
> outcomes of V4, V27, V27-glossary and V15 are deferred until the owner's decision on the V4 reversal
> at r6's adoption (RE-1, OBL-6); until then they do not count toward S13.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1436, MC-13, OD-8, RD-14. Controls: GATE-18,
> V5, V15, V27, V7a, V7b, V7c, V23, V24, V25, V26, RT-I7, RT-I7A, RT-DR, RT-DR3W.

- Purpose: States acceptance criterion S13 for the configured engine.
- If authorized: S13 counts every stated A1 control outcome except the four deferred V4-group rows until the decision.
- If not authorized: S13 is unstated; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: S13 is temporarily narrower than v6.0e's, which counted V4, V27 and V15.

***

## R6.EVID.4

Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.EVID.4** Acceptance references. The following figures are acceptance references, each through
> the control named, on the condition of R6.EVID.1. Figures whose control runs on `X_rep` are acceptance
> references through runs whose inputs are all reachable from `main` (R6.EVID.8). The figure whose
> control needs `T1'` itself (item11-T1p) is an acceptance reference only while the objects of `T1'` it
> needs are reachable from `main`, and otherwise a historical measurement (OBL-23).
>
> | Figure | Control | Input |
> |---|---|---|
> | 697 sites; replay errors 0 | RT-A, RT-E | `E`, record commit |
> | 113 `E..H` site changes (`hp-unadjudicated`); 7 HP `context-meaning-unverified`; 7 HP `context-structure-changed` | RT-H0, RT-T0 | `H` |
> | 9 merger groups covering 22 sites | RT-T0 | `H`, `X_rep` |
> | 19 region-attributed sites with untracked HP overlap (18 line-attributed); `papers/Substratum.md:266` with splice D029 | RT-T0 | `X_rep` |
> | 383 unchanged, 197 replaced, 4 removed sites; 215 region lines; 168 sites moved by `H..X_rep` splices | RT-T0 | `X_rep` |
> | 5 RET `context-meaning-unverified`; 3 RET `context-structure-changed` | RT-T0 | `X_rep` |
> | `resid`: 45 REVIEW lines, 17 hit by no other profile; 11 W1/W2 lines PASS | RT-D | `X_rep` |
> | literal item-7 greps at `X_rep`: "six structural" 7, "Fourteen" 0, "sixth of" 0, `\bA1\b` 4 | RT-I7 | `X_rep` |
> | literal item-7 greps at `H`: 11, 1, 2, 179 | RT-I7 (after RD-3) | `H` |
> | deny lines at `H`: DR-1 61 (a 6, b 2, c 55), DR-3 0, DR-4 28, DR-5 1, 86 distinct; at `E` 95 distinct | RT-DR (after RD-3) | `H`, `E` |
> | DR-3 on `AGENTS.md`: one sentence at `H` (lines 37-39), none in `X_rep` | RT-DR3W | control inputs |
> | 95 retired lines, each FAIL `final-unclassified` at `H`; at `H` 86 deny, 123 `final-unclassified`, 209 FAIL lines (93 and 216 with multi-line counting); at `X_rep` 0 deny, 12 `final-unclassified` | RT-I7A (after RD-3) | `H`, `X_rep` |
> | 176 `final-unclassified` lines of the `repo` profile | item11-T1p | `T1'` |
> | 584 sites swept, each with exactly one new RET FAIL | SW2 | `H` |
> | 697 sites swept, each with exactly one new FAIL | SW1 | `E` |
> | 399 splices verified at `H`; 23 corpus files and 21 other ledgered files conform | RT-C (after RD-3) | `H` |
>
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-037, E-038, E-074, E-039, E-042, E-045, E-046, E-047, E-049, E-089, E-090, ME-3, RD-3,
> RD-23, MC-1, MC-2, VD-10, RD-11, OC-3. Controls: RT-A, RT-E, RT-H0, RT-T0, RT-D, RT-I7, RT-DR, RT-DR3W,
> RT-I7A, item11-T1p, SW1, SW2, RT-C.

- Purpose: Lists the acceptance references and the controls that establish them.
- If authorized: The listed figures are gated through their controls.
- If not authorized: No figure is an acceptance reference; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter.

***

## R6.EVID.5

Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.EVID.5** Historical measurements. The following figures are not acceptance references. No
> control on `main` reproduces them, or they were measured with P's code, at `T1'` by scripts that are not
> retained, or under definitions r6 does not use. They are provenance (sec. A.42 item 2) and are kept in
> the appendix:
> - the s3 categories 346 / 136 / 109 / 106 and the per-merge attribution 48 / 23 / 15 / 15 / 12, and
>   the three two-step HP sites (`papers/Main.md:224`, `papers/Main.md:732`,
>   `papers/Substratum.md:92`);
> - "31 distinct splices" over the `H..T1'` HP overlaps;
> - v4's 203 region lines and its explanation;
> - v4's `resid` figures 287 / 28 / 13 and the four lines added by the v5 widening;
> - P's `classify()` breakdown of the 176 `repo` lines (96 / 31 / 14 / 35), 5486 lines in historical
>   records and 2 in generated artifacts;
> - the 12 meaning-context total, the "per unit" alternative 8, the 52 context changes and their split
>   27 / 22 / 3, and the S0 indicator counts;
> - the per-sentence deny counts under the unversioned "v5 splitter";
> - 84 and 86 hit lines, 200 / 116 / 93 / 16 / 7 unheld lines, 226 distinct lines needing a record, the
>   `ptr` 5 lines at `T1'`, the 4677-blob history search, and the reference rates of the indicator
>   definitions;
> - the parity figures 2822 / 2822, 16905 / 16905, 273, 4000 cases and 401 / 399 (OBL-2);
> - every figure of v6.0e sec. 14 not listed in R6.EVID.4.
>
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-037, E-038, E-039, E-042, E-045, E-046, E-047, E-089, E-040, E-041, E-043, E-044, E-048,
> E-088, E-1356, E-1357, E-1358, E-1359, E-1360, E-1361, E-1362, ME-2, ME-3. Controls: GATE-16.

- Purpose: Lists the historical measurements that are not acceptance references.
- If authorized: These figures stop supporting acceptance and are provenance.
- If not authorized: Their standing is undefined; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: No protection is lost (under AGENTS.md sec. A.42 they could not support an enduring claim); the 4677-blob history search, which supported dropping DR-1d and DR-2, becomes provenance.

***

## OBL-1

Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **OBL-1** P-parity of `register` and `infinity`. The engine's `register` and `infinity` profiles
> implement items 5 and 6 of P's plan as P's frozen checker defines them: per edit and per step of the
> edit list, not per splice, with P's selection, counting and sentence splitting (P's `edits_check.py`,
> blob sha256 2856e58c...d98c, functions `static_new`, `inf_key` and `sentences`). Gates: plan freeze `F`
> and any trial that claims items 5 or 6. Discharged by: a comparison, recorded at `F` by a script
> retained on `main`, of the engine's outputs against P's checker as frozen with the plan. Pending owner confirmation (see PARAPHRASED-DECISIONS.md). Sources:
> E-115, E-1371, ME-1.

- Purpose: Requires P-parity of `register` and `infinity` with P's frozen checker, recorded at `F`.
- If authorized: The plan freeze and any trial claiming items 5 or 6 are blocked until the comparison is recorded.
- If not authorized: Parity would be unrequired; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Adds a blocker.

***

## OBL-3

Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words; `S1-D2`, class (iii) no GitHub record; `V5-D2`, class (ii) session-written record on GitHub, no owner words; `S1-D1 to S1-D3`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **OBL-3** Rule records adopted at `F`. The deny rules DR-1 (alternatives a, b, c), DR-3, DR-4 and
> DR-5; the review profile `resid` (resid-a, resid-b, resid-c); the W1 allow rules with W1-c's
> `negative_allowance: {"finit": 1}`; the W2 allow rules replacing the first two `RESIDUAL_ALLOW`
> entries, their `EXPLAINED` substring entries and the blanket `(A1)` strip; and the converted
> `EXPLAINED` entries are plan records. Each is independently reviewed and adopted with the amended
> plan at `F`. Until then the controls use the current rule files as pinned control inputs. Gates: plan
> freeze `F`. Discharged by: the reviewed rule records frozen at `F`. Pending owner confirmation (see PARAPHRASED-DECISIONS.md). Sources: E-1001, E-1002, E-1003,
> E-1004, E-1005, E-1006, E-1020, E-1021, E-1022, E-1024, E-1025, E-1026, E-1027, OD-8.

- Purpose: Makes the rule records obligations adopted at `F`.
- If authorized: As for R6.DENY.5.
- If not authorized: As for R6.DENY.5.
- Safeguards affected: As for R6.DENY.5.
- FLAG, earlier designs: As for R6.DENY.5.

***

## OBL-6

Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **OBL-6** Accepted residuals and the V4 reversal. With DR-1d and DR-2 dropped, "the framework's sixth
> structural property, finiteness of the bijection" PASSes when added (control V4, whose expectation in
> v2's demonstration was FAIL); "the substratum's sixth axiom, finiteness" is REVIEW only (V15); "The
> framework's sixth structural property is finiteness of the substratum" PASSes (V27). Constructed forms
> outside `resid`'s classes PASS ("the six posits of the substratum", "six assumptions about the
> substratum", "The posit ledger lists fourteen.", "the fourteen-item posit ledger", and "$A_1$" joined to "$A_6$" by an en dash).
> Consequence of the reversal: an added sentence of V4's form reaches PASS without review. Gates: r6's
> adoption (the V4 reversal, adopted or rejected at that step); plan freeze `F` (acceptance of the residual
> forms or further rules, as rule records). Discharged by: the owner's recorded decision on the V4
> reversal at r6's adoption, among the resolutions (a), (b1) and (b2) of R6.PUR.9, and the reviewed rule
> records at `F`, including any new rule identifier that (b1) or (b2) needs.
> The decision covers V4, V27, V27-glossary and V15 together (RE-1).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1365, E-1366, RD-14, Q10.

- Purpose: Records the accepted residuals and the V4 reversal as an obligation discharged at r6 adoption and at `F`.
- If authorized: As for R6.PUR.9.
- If not authorized: As for R6.PUR.9.
- Safeguards affected: As for R6.PUR.9.
- FLAG, earlier designs: As for R6.PUR.9.

***

## OBL-15

Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **OBL-15** Reviewed records for RT-T. RT-T is NOT RUN until every reviewed record of sec. 14's review
> load exists at `F` and verifies: HP adjudications for the 113 `E..H` site changes, context
> adjudications for the meaning-context sites, structure reviews, and hit classification records for the
> replacement-region and unheld hit lines (including `papers/GR.md:58`). RT-T runs at `X_rep` built from
> `F`'s ledger (R6.EVID.8): op B reads only the corpus and the segments `E..H` and `H..X` (R6.PUR.5),
> whose bytes `H` and `F`'s ledger fix for every conforming candidate. Gates: plan freeze `F`; the A1
> retirement execution. Discharged by: RT-T run and PASS with every record: before the designation of
> `F`, on the candidate `F` within its exact-candidate validation (kind 1, OBL-16 (a)); in the
> retirement execution, at the executed candidate (kind 4); both qualify as kind 2 once the round's
> landing is on `main`.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1062, E-1063,
> RD-9, OD-20, OC-3.

- Purpose: Keeps RT-T NOT RUN until every reviewed record of the review load exists at `F`.
- If authorized: Freezing at `F` and execution are blocked until every record exists.
- If not authorized: RT-T would have no release condition; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Stricter.

***

## R6.DENY.1

Decision basis: none cited (unmarked by F4); authorized only by r6's adoption.

Current wording (DESIGN-r6.md):

> **R6.DENY.1** **Rule records are plan records.** The deny rules, the allow rules for the plan's own
> cases, and the review-profile rule `resid` that a configuration uses are rule records of the plan, in
> the schemas of sec. 10. They are frozen and adopted with the amended plan at `F`, after independent
> review, and referenced by the configuration at `F`. The tool's requirement is the rule mechanism:
> sec. 9 (profiles), sec. 10 (schema, application, lint), sec. 11 (records) and sec. 14 (hit
> classification). r6 states no rule content.
> Sources: E-1001, V2-059, V2-060, V2-061, RV-049. Controls: RT-DR, RT-D, RT-D-gr58, L1, L2.

- Purpose: Makes the rule records (deny, plan allow, `resid`) plan records frozen at `F`; the tool's requirement is the rule mechanism.
- If authorized: The tool runs whatever reviewed rule content is frozen at `F`; r6 states no rule content.
- If not authorized: The place of rule content would be undecided; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserved: v6.0e left the rules "for independent review ... not adopted"; verification of rule content moves from the design to the review at `F`.

***

## R6.DENY.2

Decision basis: none cited (unmarked by F4); authorized only by r6's adoption.

Current wording (DESIGN-r6.md):

> **R6.DENY.2** **Controls on pinned rule inputs.** The controls of the rule mechanism use the rule
> files current at the commit under check as pinned control inputs, named with their blobs in the
> expectation file (sec. 16). Acceptance of the mechanism (sec. 18) is its behaviour on those inputs. A
> changed rule file is a changed control input: the affected expectations are re-established in the
> expectation file before the gate can hold.
> Sources: E-1001. Controls: V1, V2, V3, V5, V6, V9, V10, V11, V12, V13, V14, V16, V17, V18, V19, V20,
> V22, N-W, RT-DR3W.

- Purpose: Runs the rule-mechanism controls on the rule files current at the commit under check, as pinned control inputs.
- If authorized: A changed rule file forces the affected expectations to be re-established before the gate can hold.
- If not authorized: The controls' rule inputs are unpinned; option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5).
- Safeguards affected: Preserved.
