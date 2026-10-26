# NP-AVG-1 Stage 0, Layer 1: erratum E1

**Status: in effect.** E1 takes effect under `../LAYER1-FREEZE.md` with this text: its independent
review (`../../review/E1-REVIEW.md`), the diff-only re-check of its second revision
(`../../review/E1-RECHECK-r2.md`, ACCEPT WITH NITS), and that re-check's nits N1–N6, applied here.
It governs the frozen Layer-1 specification where it applies, as stated below. No v8 result
exists: S1a has not run on v8's configuration class, and no v8 closure, count or shared-tip count
has been computed. `E1-CHANGES-r2.md` maps each review item, nit and ruling to its edit.

## 0. Relation to the freeze

- **The frozen object.** `../r5/STAGE0-PLAN-r5.md`, SHA-256
  `1a30188e70804644a6ff65b3114ab82f8be40a2b056d0e2862ce595a8982847e`, frozen at
  `f33d8d63a14b3bbaa3c1eb1e52aeffcb55b0c966` (`../LAYER1-FREEZE.md`). Line numbers below ("L1
  line n") refer to that file. `r5/`, `code-r5/`, `design-r5/` and `LAYER1-FREEZE.md` are not
  edited and stay byte-identical. `E1-check/` verifies the plan's SHA-256 and every quotation below
  at its stated lines.
- **How E1 governs.** Each item quotes the frozen text it governs and gives a replacement or an
  added definition. Where an item applies, its text is read in place of, or beside, the quoted
  passage. All other frozen text governs unchanged. Tags of the form E1-T1, E1-F3 … name items of
  this erratum. The equivalences of r5 §1 are written "equivalence E1" … "equivalence E4".
- **Its review.** `LAYER1-FREEZE.md` states: "A change is an append-only amendment, with its own
  independent review." The independent review of E1 is `../../review/E1-REVIEW.md`; its
  follow-up analysis of the owner's rulings is `../../review/E1-ANALYSIS.md`; the diff-only
  re-check of the second revision is `../../review/E1-RECHECK-r2.md` (SHA-256
  `98f092f3a722d12a3fc43ece2a85daa189362ceb6f5d7b3ae92e0ba132120e5e`). The orbit-reduction result
  and Lemma G-D are also set out, outside the specification, in `E1-NOTE-symmetry-and-G-D.md`. A
  later change is a new amendment, not an edit of E1.
- **Timing and neutrality.** The rulings were given, and E1 is fixed, before any S1a or k ≤ 2
  output exists on v8, as rule T's neutrality clause (L1 lines 1013–1016) and owner decision O-b
  (L1 lines 88–90) require. The toy-class values cited below (for example the toy S1a's L_A = 15
  and L_G = 7, and the 595 toy records of F_G) are toy geometry. They carry no information about
  v8.
- **Not touched.** The masking law (§2), the geometry, the equivalences E1–E4, the search domain
  (§1, §12 S1), the survivor definitions (§3), the propositions and proof obligations (§4), and
  the labels and their precedence (§5). Each item states what it does change.

## 1. The owner's rulings

All rulings are by the owner, amaybaum, on 2026-10-26. The first four answered the owner decisions
of `../../review/LAYER2-REVIEW.md` (lines 283–304), adopting the review's recommendations at the
lines cited in each item. The next ones answered `../../review/E1-REVIEW.md` (lines 180–204) and
are quoted, where `../../review/E1-ANALYSIS.md` quotes them, as it quotes them. The last five rows
were given during the re-check of the second revision (`../../review/E1-RECHECK-r2.md`).

| question | answer, verbatim |
| --- | --- |
| Rule T: an append-only Layer-1 erratum fixing T1, T2 and T5, with T3 and T4 as notes | "Approve erratum" |
| F3: C7's scope | "Reviewer's scope" |
| F6: the degeneracy cross-tabulations | "Erratum: add 4 counts" |
| κ: the launch margin and budget (S7) | "Decide later" (κ and S7 remain undecided) |
| C7 set 2, re-decided | "Preserve the full 595-record G-convention population unless the reviewer proves that orbit reduction preserves all required results, including multiplicities, ties, and failure detection … If it is redundant, document that finding rather than silently removing the check."; "Retain the approved shared-tip closure scope, including G's 595 records" |
| the sampling unit of H₁₀₀ and H₁₀₀₀ | "Every record index" |
| the counts | "Treat 58 as the current baseline unless the reconciliation establishes that additional nonredundant cells are mathematically required."; "explicit count definitions and a reconciliation table" |
| S1a's status | "Give S1a its own diagnostic status, not an overriding success label" |
| the reference recomputation of L_A and L_G in σ | "Add it" |
| the "geometric fact only" wording of rule T's zero branch | "Approved, with qualification. Rule T may be used as a geometric property of the specified closure. It must not be presented as a probabilistic result, empirical observation, or independent theorem about the full model" |
| C7, per-record evaluation | "Approved. Retain per-record evaluation across all 595 G-convention records. The planted-fault evidence demonstrates why representative-only evaluation is insufficient." |
| the revised C7 check set (set 2 closure-free under G) | "Approved in principle … The reviewer must confirm that the revised definition is mathematically justified and does not merely target the planted example." Confirmed: `E1-RECHECK-r2.md` §4 proves T_G = F_G ∪ (T_G ∩ Surv_G) for every record, from Lemma G-D and L1 §3 alone |
| Lemma G-D in C7's reference computation | "Conditionally approved. Keep full reference computation as the default. Permit the shortcut only after proving its equivalence to the reference computation over the complete specified domain, including failure behavior. Otherwise, retain it as a non-executing optimization proposal." (§9) |
| counts and S1a | "Approved. Retain 58 counts, independent S1a diagnostic status, and the reference recomputation of L_A and L_G." |
| the four departures of the second revision from `E1-ANALYSIS.md` §D | "Independent review required. All four must be explicitly accepted …" Accepted: `E1-RECHECK-r2.md` §1 |

## 2. Notation used below

- **U** = {(x, 23) : x ∈ Reg}. Its context Ctx(U) is the union of every item's samples, since the
  samples of (x, t) are those of (x, 23) at slices up to t (L1 §1); this is the context of S1a
  (L1 lines 985–986).
- **ℛ** is the record space of L1 §1 (singles, and pairs at distinct sites; k ≤ 2), with N
  records indexed by `record_at` over [0, N) (L1 §5b item 1).
- **ret^ρ_c(R)** is the retained set of record R under convention c ∈ {A, G} and rule
  ρ ∈ {L3′, L3} (L1 §2). It contains non-fixed quantities only.
- **Pair of c:** (7, 8) under A, (−1, 0) under G (L1 §2).
- **e-tip** and **reach in e:** as L1 §4 defines them (L1 lines 268–272): for q = (c, t) of type
  T and depth d, and an axis direction e, the e-tip of q is its near tip c + d·e on q's near slice
  (q itself when d = 0), and its reach in e is c·e + d.
- **Source cells:** the site-times ((−8, 0, 0), 0), ((−7, 0, −1), 0) and ((−7, 0, 1), 0) (L1 §1,
  equivalence E4; "a source cell at slice 0", L1 line 228).

## 3. Item E1-T1: the bound rule T reads

**Frozen text** (L1 lines 994–998):
> Its inputs are objective counts from S1a only:
> - L_A, the number of non-fixed quantities in the global bound under A whose cone
>   contains a Φ cell;
> - L_G, the number of quantities in the global bound under G with a seed tip whose
>   cone contains a source cell.

and (L1 lines 985–986): "the closures under A and G of the union of all items' samples, which is
the C9 bound".

**Ruling:** "Approve erratum" (amaybaum, 2026-10-26), adopting the review's T1 recommendation
(`LAYER2-REVIEW.md` lines 84 and 286): "the L3′ bound, with L3 reported".

**Replacement.** In rule T, "the global bound under A" is ret^{L3′}_A(U), and "the global bound
under G" is ret^{L3′}_G(U). L_A and L_G are computed on these sets only. The same two counts
computed on ret^{L3}_A(U) and ret^{L3}_G(U), written L_A^{L3} and L_G^{L3}, are recorded in
`result.json` beside L_A and L_G. They are reported only and are not inputs to rule T.

**What changes.** Rule T's trigger parameter is fixed to one of the two readings the frozen text
admits. By PO4, ret^{L3′}_c(U) ⊆ ret^{L3}_c(U), so L_A ≤ L_A^{L3} and L_G ≤ L_G^{L3}: under this
reading rule T proposes S1b in a subset of the cases in which the L3 reading would. The
L_A = L_G = 0 consequence holds under this reading, because survivors are defined by L3′ ("The
labels use L3′", L1 line 181), so S_A(R) ⊆ ret^{L3′}_A(U) and S_G(R) ⊆ ret^{L3′}_G(U) (§6, note
E1-T4). No masking law, domain, label or control changes. C9's "global closure bound" (L1
line 599) is not governed by this item.

**Checkpoint (§A.41).** `result.json` records, under `rule_T`, the bound's rule (L3′), and L_A and
L_G read from the L3′ fields of `s1a.json`, with L_A^{L3} and L_G^{L3} in a separate field. A
Layer-2 self-test case in which the L3′ and L3 values lead to different outcomes must give the
L3′ outcome. `E1-check` part G recomputes all four values from the toy `s1a.json` bounds.

## 4. Item E1-T2: S1a's status

**Frozen text** (L1 lines 1010–1011):
> If S1a is VOID, MISMATCH or INCOMPLETE, rule T is not evaluated and S1b and S1c are not
> proposed (R4-5).

The frozen text defines none of the three statuses for S1a.

**Ruling:** "Approve erratum" (amaybaum, 2026-10-26), adopting the review's T2 recommendation
(`LAYER2-REVIEW.md` lines 85 and 287): "S1a's status as Layer 2 §4 defines it"; then "Give S1a its
own diagnostic status, not an overriding success label" and, for the reference recomputation of
L_A and L_G, "Add it" (amaybaum, 2026-10-26).

**Added definition.** S1a's status σ ∈ {OK, VOID, MISMATCH, INCOMPLETE} is a diagnostic status
of the S1a computation (the owner, 2026-10-26: "Give S1a its own diagnostic status, not an
overriding success label"). It transcribes Layer 2 r2 (`4a51c675`, `l2s1a.run` and
`l2merge.merge`), including the reference checks of the L3 bound that L2-R8 added; those only add
non-OK cases. The first matching case applies:

1. **INCOMPLETE** if (a) S1a's structured output is missing, which includes every case in which
   S1a refused to start for want of certificate items 1, 2, 3, 6 or the dry run (item 7); or
   (b) its normal and `-O` outputs are not byte-identical, or one is missing; or (c) its code or
   configuration digest differs from the frozen Layer-2 manifest.
2. **VOID** if, on any of the four bound closures ret^ρ_c(U) (c ∈ {A, G}, ρ ∈ {L3′, L3}):
   - (a) C0 fails: the production context of U differs from `s0ref`'s;
   - (b) C17 fails: by `s0ref`'s cones and tips, a quantity of the bound has a free eligible tip;
   - (c) C18 fails: a logged elimination is not justified by `s0ref`;

   or if (d) L_A or L_G, recomputed from the L3′ bounds with `s0ref`'s explicit cones and tips,
   differs from the production value (ruling: "Add it"). The L3 values are recomputed the same
   way and any difference is reported; it is not a σ condition, since the ruling names L_A and
   L_G. For the L3 closures,
   (b) and (c) use near tips only.
3. **MISMATCH** if (a) a fixed quantity appears in the elimination log of a bound closure; or
   (b) ret^{L3′}_c(U) ⊄ ret^{L3}_c(U); or (c) the in-run C9 gate fails on a record R of an
   accepted shard. In (c), ret_c(R) is the run's computed closure of R (E1-F3), and the gate fails
   if ret^{L3′}_c(R) ⊄ ret^{L3}_c(R), or ret^{L3′}_c(R) ⊄ ret^{L3′}_c(U), or
   ret^{L3}_c(R) ⊄ ret^{L3}_c(U).
4. **OK** otherwise.

σ reads C9 only on accepted shards. Shard completeness is not an input of σ; it determines the
run's INCOMPLETE label under L1 §5. The order of cases 1–3 fixes only the recorded name.

**Precedence.** Rule T is evaluated iff σ = OK. σ never overrides the run's label, which L1 §5
generates from every mandatory check. A failure in case 1, 2 or 3 enters that label as an
INCOMPLETE, VOID or MISMATCH reason respectively. A run cannot pass because σ = OK if any other
mandatory check fails (the owner, 2026-10-26). When rule T is evaluated in a run whose label is
VOID, MISMATCH or INCOMPLETE, its outcome is recorded with that label beside it. No S1b proposal
is made from such a run without the owner's separate decision.

**Why σ = OK certifies the bound** (the argument the precedence rests on). C0 gives
Ctx_prod(U) = Ctx_ref(U). The closure code partitions Q⁰ into the retained and the logged (a
code invariant). C18 then gives that no logged elimination removed a member of the greatest
self-supporting subset (GSS), so GSS ⊆ computed. C17 gives that the computed bound is
self-supporting, so computed ⊆ GSS. With 2 (d), the inputs of rule T are certified by `s0ref`
independently of the production code and of the records' closures.

**What changes.** The frozen line 1010 is given a definite meaning. The inputs of σ are validity
facts about S1a's computation and the bound's consistency with the records' closures. σ does not
read the k ≤ 2 label, whether any survivor appears, or the direction of any result, so the
neutrality clause (L1 lines 1013–1016) holds. σ is diagnostic: it adds reasons to the run's label
under L1 §5 and never replaces it. No masking law, domain or label changes.

**Checkpoint (§A.41).**
- `result.json` records σ and the reasons, under `S1a.status`.
- Layer-2 self-test cases cover each of the conditions 1 (a)–(c), 2 (a)–(d) and 3 (a)–(c), each
  giving `not_evaluated`; a mutant that evaluates rule T on a non-OK status must be killed at one
  of them.
- Case 2 (d): a self-test with a perturbed production count gives VOID.
- A Layer-2 label self-test: σ = OK with another failing check gives that check's label.
- `E1-check` part K recomputes L_A and L_G from the toy L3′ bounds with `s0ref`'s cones and tips,
  and checks that a perturbed production count fires case 2 (d).

## 5. Item E1-T5: the quantity counted by L_G

**Frozen text** (L1 lines 997–998):
> L_G, the number of quantities in the global bound under G with a seed tip whose
> cone contains a source cell.

**Ruling:** "Approve erratum" (amaybaum, 2026-10-26), adopting the review's T5 recommendation
(`LAYER2-REVIEW.md` lines 88 and 288): "a quantity with a seed tip, whose cone contains a source
cell".

**Replacement.** L_G is the number of quantities q ∈ ret^{L3′}_G(U) such that both of the
following hold:
- (i) q has a seed tip: some tip of q (L1 §2: a near or far tip in the pair (−1, 0)) is
  eligible, that is, outside the frame (L1 lines 161–164);
- (ii) the G-convention cone of q (L1 §2) contains a source cell.

Condition (ii) concerns the cone of q, not the cone of the tip. L_G^{L3} (E1-T1) is the same count
on ret^{L3}_G(U). By PO7 (L1 line 306), (i) holds iff |c| + t > 8 for q = (c, t) with t ≥ 0, and
iff |c| > 7 for q at slice −1. The same condition results with near tips alone, so the count does
not depend on which tip set the seed test uses. A quantity counted by L_G is one that, if retained
in a record's closure, belongs to S_G (L1 lines 218–219) and carries G-linkage (L1 line 228).

**What changes.** One of the two readings is fixed. The other is degenerate. A tip u is a depth-0
quantity whose cone is {u}. Under that reading, (ii) would require an eligible tip to be a source
cell. Source cells lie in the frame (L1 line 140), so they are not eligible, and L_G = 0 for every
bound whatever is computed. The fixed reading is the only one under which L_G depends on the bound.
No masking law, domain or label changes.

**Checkpoint (§A.41).** `s1a.json`'s L_G is computed by the quantity reading (Layer 2's
`l2s1a.linked_counts` does so). A Layer-2 self-test on a planted bound requires a nonzero value,
and a tip-reading mutant must be killed there. `E1-check` part G gives 7 on the toy L3′ bound,
equal to the toy `s1a.json`, and 0 under the tip reading.

## 6. Notes E1-T3 and E1-T4

**E1-T3, the cost clause.** Frozen text (L1 lines 1008–1009): "**In either case,** if the
dry-run cost estimate exceeds S7's budget, the search is reported as not undertaken for cost."
Ruling: "Approve erratum" (amaybaum, 2026-10-26), with T3 as a note (`LAYER2-REVIEW.md` lines 86
and 290).

Note: the clause refers to the dry-run cost estimate of the search that rule T would put forward
(S1b, or S1c). That dry run exists only within S1b's, or S1c's, own preregistration. The clause is
therefore not evaluable in Stage 0, and `result.json` records it as "not evaluable in Stage 0". In
the L_A = L_G = 0 branch no search is undertaken, and the clause has no object. No text, budget or
decision changes. S7 is not touched.

Checkpoint: the `rule_T.cost_clause` field of `result.json`, which Layer 2 writes.

**E1-T4, the citations of rule T's consequence.** Frozen text (L1 lines 1001–1002): "No record
whose items lie in Reg × {−1, …, 23}, of any size, has a linked survivor (PO4)." Ruling: "Approve
erratum" (amaybaum, 2026-10-26), with T4 as a note (`LAYER2-REVIEW.md` lines 87 and 290).

Note: the citation "(PO4)" is read as citing four facts. With E1-T1 and E1-T5, they give the
consequence. Let R be any finite set of items in Reg × {−1, …, 23}, and c ∈ {A, G}.
1. **Context nesting** (L1 §1). Ctx(R) ⊆ Ctx(U): the samples of (x, t) are the even-class
   samples of (x, 23) at slices up to t, and the fixed quantities and port samples are in every
   context.
2. **Monotonicity** (PO4, L1 line 303). A larger context retains a superset, so
   ret^{L3′}_c(R) ⊆ ret^{L3′}_c(U).
3. **Record-independence of the frame** (L1 §2, lines 161–164). Eligibility under G is defined
   by the frame, the union of the G cones of Φ, V, p and the even port samples, which are in every
   context. The two closures in 2 therefore use one eligibility predicate.
4. **Record-independence of seed-tip status** (PO7, L1 line 306). Whether q has a seed tip
   depends on q alone, so S_G(R) ⊆ {q ∈ ret^{L3′}_G(U) : q has a seed tip}.

A Φ-linked survivor of R under A is therefore a quantity counted by L_A, and a G-linked survivor
under G one counted by L_G. The converse is not claimed: L_A > 0 does not imply that any record
has a linked survivor. Nothing changes.

Checkpoint: a document property, checked by E1's independent review, and by the re-review of
Layer 2's PO-L2-7.

## 6a. Item E1-T6: the standing of rule T's consequence

**Frozen text** (L1 lines 1001–1004):
> **L_A = 0 and L_G = 0.** No record whose items lie in Reg × {−1, …, 23}, of any size, has a
> linked survivor (PO4). The report states this geometric fact only; law failure beyond k ≤ 2
> is not claimed, since PO8 covers at most two Φ triples in clear (R4-5; the wording is
> pending owner confirmation, §12). S1b and S1c are not undertaken.

and (L1 lines 1033–1035): "**Pending owner:** rule T's L_A = L_G = 0 consequence is the geometric
statement only (the default above). A law statement for k > 2 would need a new proof obligation
generalising PO8."

**E1-T6, the standing of rule T's consequence.** Ruling: "geometric fact only": "Approved, with
qualification. Rule T may be used as a geometric property of the specified closure. It must not
be presented as a probabilistic result, empirical observation, or independent theorem about the
full model" (amaybaum, 2026-10-26). The pending-owner marks at L1 lines 1001–1004 and 1033–1035
are resolved accordingly. The L_A = L_G = 0 branch reads: "No record whose items lie in
Reg × {−1, …, 23}, of any size, has a linked survivor under the specified closure (L3′, the
declared conventions and frame). This is a geometric property of that closure. It is not a
probabilistic result, an empirical observation, or an independent theorem about the full model,
and no law statement is made beyond k ≤ 2." `result.json` records this text under
`rule_T.statement_scope`.

**What changes.** The text of the zero branch's statement and its standing; "S1b and S1c are not
undertaken" stands. The trigger, its inputs, the masking law, the domain and the labels do not
change.

**Checkpoint (§A.41).** `result.json` `rule_T.statement_scope` carries the text above verbatim.

## 7. Item E1-F3: C7's scope

**Frozen text** (L1 lines 556–559, C7):
> It must agree on every survivor, on every record containing a shared tip, and on a deterministic
> 1-in-1,000 sample of the rest. The sampling rule is a Layer-2 configuration constant under
> certificate item 1 (N6).

The following frozen text also refers to C7's scope:
- L1 line 1041 (S5, open at its proposed value): "**S5.** C7 sampling: 1 in 1,000, plus every
  survivor and every tie."
- L1 line 475 (certificate item 4): "- C7 on its sample;".
- L1 lines 463–464 (certificate item 1): "including C7's 1-in-1,000 and C8's 1-in-100 (N6)".

**Ruling:** "Reviewer's scope" (amaybaum, 2026-10-26), adopting `LAYER2-REVIEW.md` lines 292–300;
re-decided with the corrected facts of `E1-REVIEW.md` (lines 103–118, 182–193): "Preserve the full
595-record G-convention population unless the reviewer proves that orbit reduction preserves all
required results, including multiplicities, ties, and failure detection … If it is redundant,
document that finding rather than silently removing the check." and "Every record index"
(amaybaum, 2026-10-26). `E1-ANALYSIS.md` §A3 proves that orbit reduction does not preserve failure
detection (fault F2), so the population is kept in full: "Approved. Retain per-record evaluation
across all 595 G-convention records." (amaybaum, 2026-10-26; §1).

**Definitions.**
- *Shared near tip*: for a set Q of non-fixed quantities, a convention c and an axis direction e,
  Q has a shared near tip under c iff there are q ≠ q′ in Q such that the e-tip of q equals the
  e-tip of q′, in the pair of c. Eligibility plays no part. Two distinct quantities have equal
  e-tips iff they have the same type, equal reach in e, and sites that differ by a nonzero
  multiple of e; this is PO3 (b)'s "shared tip" (L1 line 302) and the sharing of P_A and P_A-dir
  (L1 lines 274–280). Fixed quantities are excluded from Q.
- *Q⁰(R)*: the non-fixed quantities of Ctx(R): the record samples after equivalences E1 and E2,
  and the port samples.
- *In(R), Out(R)* (convention G): the quantities of Q⁰(R) without, respectively with, a seed tip.
  By PO7, q = (c, t) is in Out(R) iff |c| + t > 8 for t ≥ 0, or |c| > 7 for t = −1.
- *Lemma G-D* (proved here; a proof obligation of this erratum): for every R and both rules,
  ret_G(R) = In(R) ⊔ W(Out(R)), where W(X) is the greatest subset of X whose every eligible tip
  lies in the cone of another of its elements. *Proof:* eligible tips lie outside the frame
  (L1 §2); the cones of the fixed quantities lie inside it by its definition, and those of In(R)
  by PO7 (t ≥ 0) or because a slice −1 quantity's cone is itself at |c| ≤ 7; so neither covers an
  eligible tip; quantities of In(R) have no eligible tip and are never eliminated; hence Out(R)
  is reduced exactly to W(Out(R)). The same holds for L3. ∎ (Its classification under §A.31 —
  ELABORATING, a corollary of PO7 and L1 §2 — and the toy observations are in
  `../../review/E1-ANALYSIS.md` §E.)
- *Computed closure*: ret^{L3′}_c(R) as the production run assigns it: the closure of R's orbit
  representative carried to R by the group action (S4), or R's direct closure where the run
  computes one. Since the group maps e-tips to (g·e)-tips, "the computed closure has a shared near
  tip" is constant on each orbit.

**The scope.** For each convention c, C7 runs on every record of the following sets. The
population is the record space ℛ, indexed by `record_at`, with every record counted:
1. **Surv_c:** every record that the run computes to be a survivor under c.
2. **Set 2:**
   - under A: T_A, the records whose computed closure has a shared near tip. T_A ⊆ Surv_A,
     because ret_A contains non-fixed quantities only (proved), so set 2 adds no record under A;
   - under G: (T_G ∩ Surv_G) ∪ F_G, where F_G = {R : In(R) has a shared near tip}. By Lemma G-D
     this equals T_G under the specification. F_G is computed from Q⁰(R) without any closure,
     so a fault that destroys a tie cannot remove its record from the set. The ruling retains
     these records ("Retain the approved shared-tip closure scope, including G's 595 records"),
     although their ties are inert by Lemma G-D.
3. **I_c ∩ H₁₀₀:** every record whose initial context Q⁰(R) has a shared near tip under c and
   whose record index lies in the 1-in-100 sample H₁₀₀.
4. **H₁₀₀₀:** every record whose record index lies in the 1-in-1,000 sample H₁₀₀₀.

**The samples** (R1; the owner: "Every record index"). H₁₀₀ and H₁₀₀₀ are drawn over every record
index i ∈ [0, N). Record i is in the sample of stream X at rate r iff the first eight bytes of
SHA-256(salt | X | i), read as a big-endian integer, are 0 mod r. The salt and the stream names
are configuration constants under certificate item 1, frozen before any v8 output; the two
streams are distinct.

**The check on each record R of the scope.**
- R's production closure is computed directly on R.
- R's reference closure is computed in R's own reference context.
- C7 fails on R if they differ, or if the run's reported (carried) result for R differs from R's
  direct closure.
- The reference closure is the full `s0ref` closure. Computing it under G as W(Out(R)) ∪ In(R),
  by Lemma G-D, is conditionally approved and does not execute until the owner confirms the proof
  recorded in §9. Once it is confirmed and Layer 2 enables the G-D form, Layer 2 checks this form
  against the full `s0ref` closure on the whole toy class and on every record of sets 3 and 4, and
  a difference is a C7 failure.
- A C7 failure is VOID under L1 §5. C7 may run on further records.

**Orbit reduction.** Orbit representatives may replace records only where an equivalence is
proved for every required result. For C7 verdicts on reported results, multiplicities and
set membership it is proved (C4v-equivariance of the specification; sets 1 and 2, and I_c, are
unions of orbits; the record-index samples H₁₀₀ and H₁₀₀₀ are not, which is one reason C7 is
computed per record).
For failure detection it is not: a fault confined to a non-representative member changes no
carried result. C7 on its scope is therefore computed per record, as above.

**Coverage reporting.** Each shard writes, and `result.json` sums, per set 1–4 and per
convention:
- records checked and failed;
- orbits touched;
- the sum of the touched orbits' sizes.

**What changes.** C7's pass condition changes: it now applies on the scope above. The masking
law, the domain and the labels do not change. Since T_c ⊆ I_c, the scope is the frozen literal
scope except that the records of I_c outside sets 1 and 2 are checked at 1 in 100. C11 (i) and
C18 still re-check eliminations on their samples and on every survivor, and C17 the fixed point.
On a record where C0, C17 and C18 all run (with the closure code's retained/logged partition of
Q⁰, a code invariant), C7 is implied by them (proved). C7's distinct
contribution is its independent algorithm and its coverage of sets 1–4. This redundancy is
recorded, not grounds for removal.
Over-elimination of a true survivor without an in-frame tie removes its record from sets 1 and
2; in-run it is caught only by sets 3 and 4 and the sampled C11 (i), C17 and C18, and in
pre-flight by C3, C11 (iii) and C15 (L1 §4's asymmetry).

**Checkpoint (§A.41).**
- The per-set tallies above.
- The configuration digest covers the salt, the streams and the rates (certificate item 1).
- The dry run computes |F_G|, records and orbits, without any closure, and the C7 cost term from
  it (L2-R6).
- Layer-2 self-tests:
  - the samples are deterministic over record indices;
  - Lemma G-D's form equals the full reference on the toy class;
  - a planted fault that removes in-frame tied quantities (F1) is caught on every affected record
    of set 2;
  - a fault on non-representative members only (F2) is caught by the direct per-record check;
  - a mutant that defines set 2 by the computed closure is killed by F1's case.

**Consequential replacements.**
- L1 line 1041 (S5) reads: "C7 sampling: every survivor; set 2 of E1-F3 (under G, every record
  with an in-frame shared near tip, or a survivor whose computed closure has a shared near tip);
  a deterministic 1-in-100 sample, over record indices, of the records whose initial context has
  a shared near tip; and the deterministic 1-in-1,000 sample over record indices (E1-F3)".
- L1 line 475 reads: "C7 on its scope (E1-F3), per record;".

## 8. Item E1-F6: four added counts

**Frozen text** (L1 lines 253–260, §3):
> **Degeneracies.** Each is counted and cross-tabulated with survivors; none is
> excluded:
> - items at q9, at a Φ site or at the port site, and items on the z-axis;
> - pairs on a common axis line;
> - records with a nontrivial stabilizer;
> - items with t ≤ 0, and items with t = −1;
> - masking-equivalent records (E2);
> - records whose last sample is odd-class.

and (L1 lines 576–577 and 586–588, C8):
> **The reported counts are exactly the following (54 on the toy class; on v8 the same list):**
> […]
> - per convention, every degeneracy of §3 cross-tabulated with survivor status
>   (8 degeneracies × 2);
> - masking-equivalent records; records with a nontrivial stabilizer.

and L1 line 776 (§7): "(the closed list of §6 C8: 54 counts on the toy class, closed against §3)".

**Ruling:** "Erratum: add 4 counts" (amaybaum, 2026-10-26), adopting `LAYER2-REVIEW.md` lines 187
and 304; then "Treat 58 as the current baseline unless the reconciliation establishes that
additional nonredundant cells are mathematically required." and "explicit count definitions and a
reconciliation table" (amaybaum, 2026-10-26). The reconciliation (`E1-ANALYSIS.md` §B) finds no
additional nonredundant cell, so 58 stands.

**Which four.** §3 lists ten degeneracies:
1. items at q9;
2. items at a Φ site;
3. items at the port site;
4. items on the z-axis;
5. pairs on a common axis line;
6. records with a nontrivial stabilizer;
7. items with t ≤ 0;
8. items with t = −1;
9. masking-equivalent records;
10. records whose last sample is odd-class.

C8's list cross-tabulates eight of them with survivor status, per convention: 1–5, 7, 8 and 10,
with two cells each (survivor and not), 32 counts. It gives 6 and 9 as plain counts, with no
survivor cross-tabulation. The four missing cross-tabulations are degeneracies 6 and 9, each under
A and under G.

**The added counts.** For c ∈ {A, G}:
- **N_ME,c** = #{R : R is masking-equivalent and R is a survivor under c};
- **N_ST,c** = #{R : R has a nontrivial stabilizer and R is a survivor under c}.

Here R ranges over the record space ℛ of L1 §1: 3,225 singles and 5,160,000 pairs on v8, and
1,400 records on the toy class.
- R is **masking-equivalent** iff some record R′ ≠ R of that space has an equal even-class
  context: Ctx(R′) = Ctx(R), with odd-class samples dropped (equivalence E2) and identity merges
  applied (equivalence E1) (L1 lines 128–132).
- R's **stabilizer** is {g ∈ C4v : g·R = R}, R being read as an unordered set of items. It is
  **nontrivial** iff it contains an element other than the identity.
- **Survivor under c** is as L1 §3 defines it, with L3′.

The plain counts stay on the list. With them each added cross-tabulation is complete: its
non-survivor cell is the plain count minus N_ME,c or N_ST,c.

**Count convention** (the owner: "explicit count definitions and a reconciliation table"). For a
record predicate D on ℛ:
- n(D) = #{R ∈ ℛ : D(R)};
- n(D, c, v) = #{R ∈ ℛ : D(R) ∧ s_c(R) = v}, with s_c the survivor status under c (L1 §3, L3′).

The eight degeneracies of C8's list are reported as n(D, c, True) and n(D, c, False), with n(D)
implied. For D = nontrivial stabilizer and D = masking-equivalent, the list reports n(D) (frozen)
and n(D, A, True), n(D, G, True) (added). n(D, c, False) = n(D) − n(D, c, True) is determined.
The lists of 58 and of 62 counts both carry rank 3 per degeneracy (the frozen list of 54 carries
rank 1 for D = 6 and D = 9), so 58 is complete and the four non-survivor cells would be redundant.

| list | for D ∈ {6, 9} | rank per D | redundant listed |
| --- | --- | --- | --- |
| r5 (54) | n(D) | 1 | 0 |
| E1 (58) | n(D), n(D, A, T), n(D, G, T) | 3 | 0 |
| 62 (not adopted) | n(D) and four cells | 3 | 2 |

Masking equivalence is defined relative to ℛ (some R′ ≠ R in ℛ has an equal context); the other
nine degeneracies are intrinsic to R.

**Replacements in C8 and §7.**
- L1 line 577 reads "(58 on the toy class; on v8 the same list)".
- After L1 line 588, add the item: "per convention, masking-equivalent records that are survivors,
  and records with a nontrivial stabilizer that are survivors (4) (E1-F6)".
- L1 line 776 reads "58 counts on the toy class".

The sentence "The list is closed against §3" (L1 lines 591–592) then holds with a survivor
cross-tabulation for every degeneracy. The records of r5's design evidence in §9 (L1 lines 869 and
921–922, which state 54 counts) describe what ran, and stand as records.

**Count preservation.** Both predicates are C4v-invariant:
- C4v maps the record space onto itself and contexts equivariantly, and fixes the fixed
  quantities and the port samples, so R and R′ have equal contexts iff g·R and g·R′ do;
- the stabilizers of the records of one orbit are conjugate.

Survivor status is invariant by equivariance (C8). The added counts are not source-dependent, and
they are orbit-reducible like the other degeneracy cells. C8's count preservation covers all 58.
Records with equal contexts have equal closures, so survivor status is constant on each
masking-equivalence class.

**What changes.** Four reported counts are added. No label, survivor definition, masking law or
domain depends on them. C8's pass condition is extended: count preservation now covers four more
counts, and a discrepancy on any of them is a C8 failure, VOID.

**Checkpoint (§A.41).**
- C8's count preservation over the 58 counts: on the full toy class in pre-flight, and in-run on
  sampled and survivor orbits.
- Layer 2's counts cross-check compares 58 counts.
- `E1-check`:
  - part B, the closure against §3, with its countercontrol;
  - part C, on the toy class: the full and orbit-reduced values are equal, and each plain count
    equals the sum of its two cells;
  - part D, the planted non-vacuity.

## 9. Owner decisions: conditional and open

- **κ and S7.** The launch margin κ and S7's budget (L1 line 1042) are not changed by E1. The
  owner's answer was "Decide later".
- **Lemma G-D in C7's reference computation.** Conditionally approved (amaybaum, 2026-10-26):
  "Keep full reference computation as the default. Permit the shortcut only after proving its
  equivalence to the reference computation over the complete specified domain, including failure
  behavior." The proof: by Lemma G-D, for every R ∈ ℛ and both rules, In(R) ∪ W(Out(R)) =
  GSS(Ctx(R)), using only PO7 and the frame's definition, which hold on the whole domain; so for
  every production output P, faulty or not, C7's verdict is the same under either reference
  form, and production faults are detected identically. The equivalence does not cover faults in
  the reference implementation itself; these fail safe (a spurious C7 failure, VOID), and the
  cross-check of the G-D form against the full form, on the whole toy class and on every record
  of sets 3 and 4, guards them. The full form remains the default. The G-D form stays a
  non-executing optimization proposal ("Otherwise, retain it as a non-executing optimization
  proposal") until the owner confirms that this proof meets the bar, a confirmation taken
  together with κ once the dry run reports |F_G| (records and orbits, computed without any
  closure). Only then may Layer 2 enable it, with that cross-check.
- **O1, optional, not adopted: closing the residual escape under G** (`E1-RECHECK-r2.md`, owner
  decision O1). Add E_G = {R : Out(R) has a shared eligible near tip} to C7's scope under G, as
  set 5. It is closure-free and contains Surv_G by P_G. On the toy class it is 12 of 1,400
  records; v8's size is unknown and computable without any closure in the dry run. It would be a
  further amendment, not part of E1. Under A the analogous superset, I_A, is the frozen literal
  scope, which the ruling samples at 1 in 100.

## 10. Invariant → checkpoint (§A.41)

| invariant asserted by E1 | checkpoint |
| --- | --- |
| the frozen files are unchanged and every quotation stands at its stated lines | `E1-check` part A: the SHA-256 of `STAGE0-PLAN-r5.md`, and the quotations it lists (from the plan, `LAYER1-FREEZE.md`, `LAYER2-REVIEW.md`, `E1-REVIEW.md` and `E1-ANALYSIS.md`); the git tree identifiers recorded in `LAYER1-FREEZE.md` |
| rule T reads L_A and L_G from the L3′ bound; the L3 values are reported only (E1-T1) | `result.json` `rule_T` fields; Layer-2 self-test with differing L3′ and L3 outcomes; `E1-check` part G |
| rule T is evaluated iff σ = OK, with σ as in E1-T2 | `result.json` `S1a.status` and reasons; Layer-2 self-test cases 1 (a)–(c), 2 (a)–(d), 3 (a)–(c); a status-ignoring mutant killed |
| L_G counts by the quantity's cone (E1-T5) | `s1a.json` L_G; Layer-2 planted-bound self-test with a tip-reading mutant killed; `E1-check` part G (toy: 7, and 0 under the tip reading) |
| the cost clause is recorded as not evaluable in Stage 0 (E1-T3) | `result.json` `rule_T.cost_clause` |
| the consequence rests on §1, §2, PO4 and PO7 (E1-T4) | document property; E1's independent review |
| C7 runs per record on sets 1–4 of E1-F3, with H₁₀₀ and H₁₀₀₀ deterministic over record indices and frozen before any v8 output | per-set C7 tallies in the shards and `result.json`; configuration digest (certificate item 1); Layer-2 self-tests; `E1-check` part J |
| "shared near tip" is the shared tip of PO3 (b) | `E1-check` part F (every pair of every toy context, under A and G) |
| the count list has 58 counts and cross-tabulates every §3 degeneracy with survivor status | `E1-check` part B, with the drop-one countercontrol |
| the four added counts are preserved by orbit reduction | C8 (pre-flight and in-run); `E1-check` parts C and D, and the non-invariant countercontrol of part E |
| Lemma G-D | the toy whole-class check (`E1-check` part H, both rules); the per-record check of sets 3–4 (when the G-D form is enabled, §9) |
| set 2 is closure-free under G | F1 self-test and the computed-closure mutant (`E1-check` part I) |
| per-record C7 detects member-only faults | F2 self-test (`E1-check` part I) |
| σ is diagnostic and never overrides the run label | Layer-2 label self-test: σ = OK with another failing check gives that check's label (`E1-check` part K, on Layer 2 r2's `label` and `rule_T`) |
| L_A and L_G reference recomputation | case 2 (d) self-test with a perturbed production count (`E1-check` part K) |
| rule T's statement scope | `result.json` `rule_T.statement_scope` |
| record-index sampling | sampling self-test (`E1-check` part J) |
| coverage reporting, raw and orbit-level | shard and `result.json` fields; `E1-check` part J reports both on the toy class |

## 11. The consistency check (`E1-check/`)

- **Command:** `python3 -I -B e1_check.py`, from `E1-check/`. It reads the frozen plan, the review
  documents and Layer 2's toy-run outputs, and it imports Layer 2's engine and reference on the
  toy profile only. It refuses v8's (dim, n, port), and nothing in it touches v8's class.
- **Output:** `e1_check.out`. Exit 0. Every check passes. The output is byte-identical under
  `python3 -I -B -O`.
- **Parts A–G** are as in the first revision: quotations; the closure of the 58-count list against
  §3; the toy class's counts; planted non-vacuity (N_ME = 8 and N_ST = 12 under each convention on
  12 planted block records); the non-invariant countercontrol; the shared-near-tip definition;
  and T1 and T5 on the toy S1a bounds.
- **Part H, Lemma G-D and its corollaries.** On all 1,400 toy records, and on the 12 planted
  records (all of them A- and G-survivors), ret_G = In ∪ W(Out) for L3′ and for L3, with W
  computed by `s0ref` without the fixed and in-frame quantities, and the G-D form equals the full
  `s0ref` closure. T_A ⊆ Surv_A, T_G restricted to eligible tips ⊆ Surv_G, and
  T_G = (T_G ∩ Surv_G) ∪ F_G hold on both (toy: T_G = F_G = 595, no survivors). So do the
  closure-free supersets of the survivors given by P_G and P_A: Surv_G ⊆ E_G, with
  E_G = {R : Out(R) has a shared eligible near tip}, and Surv_A ⊆ I_A (toy: E_G has 12 records,
  all in F_G; I_A has 1,071).
- **Part I, planted faults (toy, G).** F1 drops every retained in-frame quantity whose near tip is
  shared; F2 does so on non-representative members only.

  | fault | records affected | computed-closure mutant (set 2 by the computed closure, reported results) | E1-F3 (closure-free set 2, direct per-record check) | representatives only |
  | --- | --- | --- | --- | --- |
  | F1 | 595 | 0 | 595 | 283 |
  | F2 | 312 (no reported result wrong) | 0 | 312 | 0 |

  The mutant is killed by F1's case, and only the direct per-record check catches F2.
- **Part J, record-index sampling.** H₁₀₀ and H₁₀₀₀ are drawn over all 1,400 toy record indices,
  on distinct streams. The draws are deterministic and include non-representative records.
  Coverage per set, as records / orbits touched / sum of their sizes: under A, set 3 12 / 12 / 45
  and set 4 1 / 1 / 4; under G, set 2 595 / 283 / 595, set 3 6 / 6 / 24 and set 4 1 / 1 / 4;
  sets 1, and set 2 under A, are empty. The populations equal those of the reviewer's analysis.
- **Part K, σ.** L_A and L_G recomputed from the toy L3′ bounds with `s0ref`'s cones and tips are
  15 and 7, equal to the production values (the L3 values likewise), and a perturbed production
  count fires case 2 (d). On Layer 2 r2's `label` and `rule_T`, a run with σ = OK and a failing
  VOID, MISMATCH or INCOMPLETE reason keeps that label while rule T is evaluated.
- **Part L, the text of `E1-ANALYSIS.md` §D.** Ten blocks of §D, after the re-check's
  substitutions N2 and N3, and the eight §10 rows stand in this erratum verbatim (blockquote
  markers and line breaks aside). The output lists the four departures, each with its reason; the
  G-D permission text of §D is confirmed absent.
- **Part M, the re-check's nits and the owner's rulings.** The erratum carries N1's §9 text (up to
  "guards them."), N4, N5, N6 and O1, and the five rulings of the re-check, quoted. It does not
  state that the G-D form executes. The source of these texts, `E1-RECHECK-r2.md` and the relayed
  rulings, is not in the repository, so part M checks the erratum against the check's own
  transcription.

SHA-256 values:
- `e1_check.py`: `bf96fb94a7c70837f03edc09101175dc4b4eaa5f043e1d39132a31d1f91ced91`;
- `e1_check.out`: `d2297fb70f9414fb2f0b29454fe35ab1722d611d8a07ef56452eb14ccf3a8542`.
