# NP-AVG-1 Stage 0, Layer 1: erratum E1

**Status: draft, append-only, awaiting its independent review.** It governs the frozen Layer-1
specification where it applies, as stated below. No v8 result exists: S1a has not run on v8's
configuration class, and no v8 closure, count or shared-tip count has been computed.

## 0. Relation to the freeze

- **The frozen object.** `../r5/STAGE0-PLAN-r5.md`, SHA-256
  `1a30188e70804644a6ff65b3114ab82f8be40a2b056d0e2862ce595a8982847e`, frozen at
  `f33d8d63a14b3bbaa3c1eb1e52aeffcb55b0c966` (`../LAYER1-FREEZE.md`). Line numbers below ("L1
  line n") refer to that file. `r5/`, `code-r5/`, `design-r5/` and `LAYER1-FREEZE.md` are not
  edited and stay byte-identical; `E1-check/` verifies the plan's SHA-256 and every quotation below
  at its stated lines.
- **How E1 governs.** Each item quotes the frozen text it governs and gives a replacement or an
  added definition. Where an item applies, its text is read in place of, or beside, the quoted
  passage. All other frozen text governs unchanged.
- **Its review.** `LAYER1-FREEZE.md` states: "A change is an append-only amendment, with its own
  independent review." E1 takes effect when that review accepts it. A later change is a new
  amendment, not an edit of E1.
- **Timing and neutrality.** The rulings were given, and E1 is fixed, before any S1a or k ≤ 2
  output exists on v8, as rule T's neutrality clause (L1 lines 1013–1016) and owner decision O-b
  (L1 lines 88–90) require. The toy-class values cited below (for example the toy S1a's L_A = 15
  and L_G = 7) are toy geometry. They carry no information about v8.
- **Not touched.** The masking law (§2), the geometry, the equivalences E1–E4, the search domain
  (§1, §12 S1), the survivor definitions (§3), the propositions and proof obligations (§4), and
  the labels and their precedence (§5). Each item states what it does change.

## 1. The owner's rulings

The owner, amaybaum, 2026-10-26, answered the owner decisions of `../../review/LAYER2-REVIEW.md`
(lines 283–304), adopting the review's recommendations at the lines cited in each item:

| question | answer, verbatim |
| --- | --- |
| Rule T: an append-only Layer-1 erratum fixing T1, T2 and T5, with T3 and T4 as notes | "Approve erratum" |
| F3: C7's scope | "Reviewer's scope" |
| F6: the degeneracy cross-tabulations | "Erratum: add 4 counts" |
| κ: the launch margin and budget (S7) | "Decide later" |

## 2. Notation used below

- **U** = {(x, 23) : x ∈ Reg}. Its context Ctx(U) is the union of every item's samples, since the
  samples of (x, t) are those of (x, 23) at slices up to t (L1 §1); this is the context of S1a
  (L1 lines 985–986).
- **ret^ρ_c(R)** is the retained set of record R under convention c ∈ {A, G} and rule
  ρ ∈ {L3′, L3} (L1 §2). It contains non-fixed quantities only.
- **Pair of c:** (7, 8) under A, (−1, 0) under G (L1 §2).
- **e-tip** and **reach in e:** as L1 §4 defines them (L1 lines 268–272): for q = (c, t) of type
  T and depth d, and an axis direction e, the e-tip of q is its near tip c + d·e on q's near slice
  (q itself when d = 0), and its reach in e is c·e + d.
- **Source cells:** the site-times ((−8, 0, 0), 0), ((−7, 0, −1), 0) and ((−7, 0, 1), 0) (L1 §1
  E4; "a source cell at slice 0", L1 line 228).

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
(`LAYER2-REVIEW.md` lines 85 and 287): "S1a's status as Layer 2 §4 defines it". The definition
below states Layer 2's, as implemented in `layer2/code/l2s1a.py` (`run`) and `l2merge.py`
(`merge`), in Layer-1 terms.

**Added definition.** S1a's status σ is one of OK, VOID, MISMATCH and INCOMPLETE. The merge
computes it from structured files only (certificate item 8). The first matching case applies:

1. **INCOMPLETE** if any of the following holds:
   - (a) S1a's structured output is missing. That includes every case in which S1a refused to
     start: S1a computes only after certificate item 1 (the manifest), item 2 (a passing
     pre-flight for the same code digest), item 3 (a passing mutant campaign), item 6 (the v8
     authorization) and the mandatory dry run (item 7) have passed;
   - (b) its normal and `-O` outputs are not byte-identical, or one of them is missing;
   - (c) its code digest or configuration digest differs from the frozen Layer-2 manifest.
2. **VOID** if a reference check fails on any of the four bound closures ret^ρ_c(U), for
   c ∈ {A, G} and ρ ∈ {L3′, L3}:
   - (a) C0: the production context of U differs from `s0ref`'s context of U;
   - (b) C17: by `s0ref`'s cone and tip code, a quantity of the bound has a free eligible tip;
   - (c) C18: a logged elimination of the bound's closure is not justified by `s0ref`, that is,
     its tip is not a valid, eligible tip of the eliminated quantity uncovered by every quantity
     alive at that moment.

   For the L3 closures, (b) and (c) use near tips only, since L3 is L3′ without the far tips
   (L1 line 182).
3. **MISMATCH** if any of the following holds:
   - (a) C10 (i) on S1a: a fixed quantity appears in the elimination log of one of the four bound
     closures;
   - (b) C9 on U: ret^{L3′}_c(U) ⊄ ret^{L3}_c(U) for c = A or G;
   - (c) the in-run C9 gate fails on some record R of some accepted shard, under either
     convention: ret^{L3′}_c(R) ⊄ ret^{L3}_c(R), or ret^{L3′}_c(R) ⊄ ret^{L3′}_c(U), or
     ret^{L3}_c(R) ⊄ ret^{L3}_c(U).
4. **OK** otherwise.

Rule T reads only whether σ = OK. The order of cases 1–3 decides only the name under which a
non-OK status is recorded.

**Consequences, stated so that none is inferred.**
- σ depends only on S1a's own computation and on the shards' C9 results. The other in-run gate
  failures on shards (C0, C7, C8, C10 (i), C11 (i) and (ii), C17, C18) give the run a VOID or
  MISMATCH label under L1 §5, but leave σ unchanged. Rule T can therefore be evaluated in a run whose label is VOID
  for reasons outside S1a.
- Case 3 (c) coincides with the run's MISMATCH condition "a retained set lies outside the global
  closure bound" (L1 line 339) or "L3′ retains something L3 does not" (L1 line 338).

**What changes.** The frozen line 1010 is given a definite meaning. The inputs of σ are validity
facts about S1a's computation and the bound's consistency with the records' closures. A C9
failure means some record retains a quantity outside the bound, against PO4, so the bound rule T
reads is not a valid bound. σ does not read the k ≤ 2 label, whether any survivor appears, or the
direction of any result, so the neutrality clause (L1 lines 1013–1016) holds. No masking law,
domain or label changes.

**Checkpoint (§A.41).** `result.json` records σ and the reasons, under `S1a.status`. Layer-2
self-test cases cover each of the conditions 1 (a)–(c), 2 (a)–(c) and 3 (a)–(c), each giving
`not_evaluated`, and a mutant that evaluates rule T on a non-OK status must be killed at one of
them.

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

**Not governed by E1.** E1 neither confirms nor changes the wording of the L_A = L_G = 0
consequence, which the frozen text marks as pending owner confirmation (L1 lines 1001–1004 and
1033–1035; `LAYER1-FREEZE.md`, "Not frozen, and not authorized"). The rulings above do not
address it.

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

**Ruling:** "Reviewer's scope" (amaybaum, 2026-10-26), adopting `LAYER2-REVIEW.md` lines 292–300.

**Definitions.**
- **Shared near tip.** For a convention c and a set Q of non-fixed quantities, Q *has a shared
  near tip under c* iff there are q ≠ q′ in Q and an axis direction e such that the e-tip of q
  equals the e-tip of q′, in the pair of c. Eligibility plays no part in this definition.
- **Equivalence with the frozen notion.** Two distinct quantities have equal e-tips iff they have
  the same type, equal reach in e, and sites that differ by a nonzero multiple of e. This is
  PO3 (b)'s "shared tip" (L1 line 302) and the sharing of L1 P_A and P_A-dir (L1 lines 274–280).
  Near tips of F and B type lie on different slices of the pair, so equal e-tips imply equal type.
  `E1-check` part F verifies the equivalence on every pair of quantities in every context of the
  toy class, under A and G: 230,268 (pair, direction) cases. Fixed quantities are excluded from
  Q. A tip at a Φ site-time is treated separately by P_A-dir and PO5, not as a shared tip.
- **Initial context.** Q⁰(R), the non-fixed quantities of Ctx(R): the record samples after E1
  and E2, and the port samples.
- **Computed closure.** ret^{L3′}_c(R) as the production run assigns it: the closure of R's orbit
  representative carried to R by the group action (S4), or R's direct closure where the run
  computes one. Where the two differ, C8 fails and the run is VOID. Since the group maps e-tips to
  (g·e)-tips, "the computed closure has a shared near tip" is constant on each orbit.

**Replacement for L1 lines 556–558.** For each convention c, C7 runs under c on every record of
the following four sets. Its pass condition (L1 lines 553–555 and 392) is unchanged: on each such
record, `s0ref`'s greatest self-supporting subset equals the production retained set the run
assigns to that record.
1. **Surv_c:** every record that is a survivor under c (L1 §3).
2. **T_c:** every record whose computed closure ret^{L3′}_c(R) has a shared near tip under c.
3. **I_c ∩ H₁₀₀:** every record whose initial context Q⁰(R) has a shared near tip under c and
   which lies in the 1-in-100 sample H₁₀₀.
4. **H₁₀₀₀:** every record in the existing 1-in-1,000 sample (L1 lines 557–558).

In sets 1 and 2, "every record" includes every member of every orbit, each with its own reference
context, in the reading Layer 2 applies to "every survivor" (`LAYER2-REVIEW.md` L2-R2). C7 may
also run on further records. A disagreement on any record on which C7 runs is a C7 failure, VOID
under L1 §5.

**The sample H₁₀₀.** It is drawn as C7's existing sample is drawn:
- deterministically, as a fixed function of the record's enumeration index (`record_at`, L1 §5b
  item 1) and of a salt and a stream name frozen in the Layer-2 configuration;
- at rate 1 in 100, on its own stream, distinct from the 1-in-1,000 stream, so that the two
  samples are separate draws;
- before, and independently of, any closure result.

The rate, the salt and the stream name are configuration constants under certificate item 1. They
are added to the list at L1 lines 463–464 and frozen with the Layer-2 manifest before any v8
output. The rule the Layer-2 draft uses for its other samples (`LAYER2-PLAN.md` §3.3) is this: an
index i is in the sample of stream X at rate R iff the first eight bytes of
SHA-256(salt | X | i), read as a big-endian integer, are 0 mod R. H₁₀₀ is drawn over the same
unit as H₁₀₀₀. The frozen text leaves the sampling rule, its unit included, to the Layer-2
configuration (L1 lines 558–559). The Layer-2 draft draws its C7 samples over the indices of orbit
representatives.

**Consequential replacements.**
- L1 line 1041 (S5) reads: "C7 sampling: every survivor; every record whose computed closure has
  a shared near tip; a deterministic 1-in-100 sample of the records whose initial context has a
  shared near tip; and the deterministic 1-in-1,000 sample (E1-F3)".
- L1 line 475 reads: "C7 on its scope (E1-F3);".

**What changes.** This changes C7's pass condition, by changing the set of records on which
agreement is required. It changes no masking law, domain or label. Since ret^{L3′}_c(R) ⊆ Q⁰(R),
T_c ⊆ I_c. The new scope is therefore the frozen literal scope (Surv_c ∪ I_c, plus the base
sample), except that the records of I_c outside Surv_c ∪ T_c are checked at 1 in 100 instead of
all. A C7 disagreement confined to unsampled records of that set is no longer seen. C11 (i) and
C18 still re-check individual eliminations on their samples and on every survivor (L1 lines
662–664 and 481), and C17 checks the fixed point.

Under G, set 2 includes records whose shared near tips lie in the frame, since in-frame quantities
are retained with every tip ineligible. On the toy class, 595 of the 1,400 records have a G closure
with a shared near tip, and in none of them is the shared tip eligible; under A the count is 0
(`E1-check` part F; toy only).

**Checkpoint (§A.41).**
- Each shard writes, and `result.json` sums, C7's tallies per set 1–4 (checked, failed).
- The configuration digest includes H₁₀₀'s rate, salt and stream (certificate item 1).
- Layer-2 self-tests: the H₁₀₀ draw is deterministic and non-empty on the toy class; a planted
  record whose computed closure has a shared near tip is C7-checked; and a mutant that skips set 2
  is killed there.
- The dry run's C7 cost term is computed under this scope (L2-R6).
- `E1-check` part F checks the definition's equivalence with PO3 (b), and reports the toy
  frequencies.

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
and 304.

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

Here R ranges over the record space of L1 §1: 3,225 singles and 5,160,000 pairs on v8, and 1,400
records on the toy class.
- R is **masking-equivalent** iff some record R′ ≠ R of that space has an equal even-class
  context: Ctx(R′) = Ctx(R), with odd-class samples dropped (E2) and identity merges applied (E1)
  (L1 lines 128–132).
- R's **stabilizer** is {g ∈ C4v : g·R = R}, R being read as an unordered set of items. It is
  **nontrivial** iff it contains an element other than the identity.
- **Survivor under c** is as L1 §3 defines it, with L3′.

The plain counts stay on the list. With them each added cross-tabulation is complete: its
non-survivor cell is the plain count minus N_ME,c or N_ST,c.

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

## 9. Not governed: κ and S7

The launch margin κ and S7's budget (L1 line 1042) are not changed by E1. The owner's answer was
"Decide later".

## 10. Invariant → checkpoint (§A.41)

| invariant asserted by E1 | checkpoint |
| --- | --- |
| the frozen files are unchanged and every quotation stands at its stated lines | `E1-check` part A: the SHA-256 of `STAGE0-PLAN-r5.md`, and 59 quotations (42 from the plan, 2 from `LAYER1-FREEZE.md`, 15 from `LAYER2-REVIEW.md`); the git tree identifiers recorded in `LAYER1-FREEZE.md` |
| rule T reads L_A and L_G from the L3′ bound; the L3 values are reported only (E1-T1) | `result.json` `rule_T` fields; Layer-2 self-test with differing L3′ and L3 outcomes; `E1-check` part G |
| rule T is evaluated iff σ = OK, with σ as in E1-T2 | `result.json` `S1a.status` and reasons; Layer-2 self-test cases 1 (a)–(c), 2 (a)–(c), 3 (a)–(c); a status-ignoring mutant killed |
| L_G counts by the quantity's cone (E1-T5) | `s1a.json` L_G; Layer-2 planted-bound self-test with a tip-reading mutant killed; `E1-check` part G (toy: 7, and 0 under the tip reading) |
| the cost clause is recorded as not evaluable in Stage 0 (E1-T3) | `result.json` `rule_T.cost_clause` |
| the consequence rests on §1, §2, PO4 and PO7 (E1-T4) | document property; E1's independent review |
| C7 runs on sets 1–4 of E1-F3, with H₁₀₀ deterministic and frozen before any v8 output | per-set C7 tallies in the shards and `result.json`; configuration digest (certificate item 1); Layer-2 self-tests and a skip-set-2 mutant |
| "shared near tip" is the shared tip of PO3 (b) | `E1-check` part F (every pair of every toy context, under A and G) |
| the count list has 58 counts and cross-tabulates every §3 degeneracy with survivor status | `E1-check` part B, with the drop-one countercontrol |
| the four added counts are preserved by orbit reduction | C8 (pre-flight and in-run); `E1-check` parts C and D, and the non-invariant countercontrol of part E |

## 11. The consistency check (`E1-check/`)

- **Command:** `python3 -I -B e1_check.py`, from `E1-check/`. It reads the frozen plan and Layer
  2's toy-run outputs, and it imports Layer 2's engine on the toy profile only. It refuses v8's
  (dim, n, port), and nothing in it touches v8's class.
- **Output:** `e1_check.out`. Exit 0. Every check passes. The output is byte-identical under
  `python3 -I -B -O`.
- **Part B.** C8's list of 54 leaves exactly four (degeneracy, convention) cross-tabulations
  undetermined: degeneracies 6 and 9 under A and G. With the four added counts the list has 58,
  and none is undetermined. Dropping any one added count reopens the gap, and the countercontrol
  catches each of the four.
- **Part C, the toy class.** The per-record pipeline reproduces the toy run's 32 degeneracy cells,
  its two survivor counts and its two plain counts (masking-equivalent 1,398, nontrivial
  stabilizer 1,176). The added counts are 0 in full and 0 orbit-reduced, because the toy class has
  no survivors, and each plain count equals the sum of its cells.
- **Part D, planted non-vacuity.** The records are three planted 7-item records in the toy
  geometry and their orbits, 12 records: C3's constraint block, the block with its top item one
  slice later on an odd-class slice (masking-equivalent to the block), and the block with its top
  one slice earlier. They are not records of the k ≤ 2 space. The decision rule, fixed before the
  run, was: non-vacuity is shown iff an added count is nonzero there. Every record survives under
  A and G. The added counts are N_ME = 8 and N_ST = 12 under each convention, equal in full and
  orbit-reduced, and the 2×2 tables close.
- **Part E, the countercontrol.** A predicate that is not C4v-invariant, put in place of survivor
  status, makes the orbit-reduced values differ from the full ones (392 against 128, and 280
  against 128). The orbit-reduction comparison can therefore fail.
- **Part F.** The definition's equivalence with PO3 (b) holds on all 230,268 cases, and the
  recomputed count of initial-context shared tips equals the toy run's (739 representative ×
  convention cases). The toy frequencies, over 1,400 records, are toy only:

  | predicate | A | G |
  | --- | --- | --- |
  | initial context has a shared near tip | 1,071 | 667 |
  | L3′ closure has a shared near tip | 0 | 595 |
  | the same, counting eligible tips only | 0 | 0 |

- **Part G.** On the toy `s1a.json` bounds, L_A = 15 and L_G = 7 under L3′, equal to `s1a.json`;
  the L3 values are the same, 15 and 7. The tip reading of L_G gives 0 on both bounds, the source
  cells are in the frame, and the L3′ bounds lie inside the L3 bounds.

SHA-256 values:
- `e1_check.py`: `fdcd7d264076f812be8f072b2e7aab25c8952daf4bcdea02350d545098edd6b0`;
- `e1_check.out`: `b12159a12a573d6abc93ac96895f6ec806c6963cf48d25b362a5466238da816f`.
