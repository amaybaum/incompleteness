# Independent review: Layer-1 erratum E1 (NP-AVG-1 Stage 0)

**Object.**
- `stage0/amendments/E1-LAYER1-ERRATUM.md`: SHA-256
  `c00b448659d1df4a48c843c3a2eb85ae6e2b35d683896f0780c2cd48de1512ab`, at `21d25752` on PR #935.
- `E1-check/`: `e1_check.py` `fdcd7d26…d6b0` and `e1_check.out` `b12159a1…816f`.

**Read against:**
- the frozen `r5/STAGE0-PLAN-r5.md` (`1a30188e…847e`);
- `LAYER1-FREEZE.md`;
- `review/LAYER2-REVIEW.md`, byte-identical to my review;
- Layer 2 r2 at `4a51c675`.

**Read-only.** Nothing was edited or committed, and nothing ran on v8's class. My outputs are in
`S/npavg/review-e1/`.

## Verdict: ACCEPT WITH CHANGES. E1 does not take effect yet

**What is sound.**
- E1-T1, E1-T5, the notes E1-T3 and E1-T4, and E1-F6 implement their rulings exactly, are
  unambiguous against r5, and change nothing beyond the ruling.
- E1-T2's σ is faithful to Layer 2's definition and neutral.
- The check replays exactly, and its countercontrols fail when they should.

**What blocks.** E1-F3 implements the ruled C7 scope literally, but that ruling adopted my
recommendation, and my recommendation rested on a false premise. Its second set is either
redundant or expensive and uninformative (§3). The owner should re-decide that set with the
correct facts. Three smaller items need text fixes.

## 1. Replay and the check (task 4)

**Replay.**
- `python3 -I -B e1_check.py` exits 0 in 4 s, and its output is byte-identical to `e1_check.out`.
  Under `-O` it is byte-identical too.
- It writes nothing. The worktree stayed clean.

**Quotations.** I re-read every r5 line range E1 cites:
- 88–90, 128–132, 140 and 161–164;
- 181–182, 218–219, 228 and 253–260;
- 268–272, 302–306, 338–339 and 392;
- 463–464, 475, 481 and 553–559;
- 576–577, 586–592, 599 and 662–664;
- 776, 985–986, 994–1016, 1033–1035 and 1041–1042.

Each quotation matches. The review's lines 283–304 match the rulings table.

**The countercontrols can fail.** On a scratch copy (`cc/`):
- **A changed word** on a quoted line of `LAYER2-REVIEW.md` (line 286) makes the check exit 2,
  with `A.quotes_at_stated_lines` failing.
- **A one-character edit** to r5 line 1010 makes the check exit 2, with both
  `A.quotes_at_stated_lines` and `A.r5_sha256_equals_freeze_record` failing.
- **The built-in countercontrols fire:**
  - Part B: drop one added count, and the closure reopens for each of the four;
  - Part E: a predicate that is not C4v-invariant makes the full and orbit-reduced values
    differ (392 and 280 against 128).

## 2. The items (tasks 1 to 3)

**E1-T1: accepted.**
- The ruling is applied exactly: L_A and L_G come from ret^{L3′}_c(U), and the L3 values are
  reported only.
- It adds and loosens nothing. Since ret^{L3′} ⊆ ret^{L3}, rule T fires in a subset of the L3
  reading's cases.
- It leaves C9 unaffected.

**E1-T2: accepted, with R3 and R4.** It is faithful to Layer 2's definition as implemented at
`4a51c675`.
- **Inclusion beyond r1.** It includes the L3-bound reference checks, which came from my L2-R8.
  Layer 2 r1 §4, which the ruling named, lacked them. This is a tightening that only adds non-OK
  cases, and it should be named as such (R4).
- **Unambiguous where it matters.** Rule T reads only whether σ = OK, so the order of cases 1–3
  matters only for the recorded name.
- **Neutral.** σ reads validity facts, never the k ≤ 2 label or a direction.
- **Open point (d), rule T in a VOID-labelled run: sound, no change needed.**
  - σ's VOID cases certify the bound by independent code. C18 (every logged elimination justified
    by the reference) gives computed ⊇ the greatest self-supporting subset. C17 (no retained
    quantity has a free eligible tip) gives computed ⊆ it. C0 gives equal contexts. So an OK bound
    *is* the L3′ closure of U.
  - The run's other gates concern records' closures, not U's. The partition "retained ∪ logged =
    context" holds by construction in the closure code; it is a code invariant like C10 (i).
  - Evaluating rule T in a run that is VOID for record-level reasons therefore uses a certified
    bound. E1 should state this argument rather than only the consequence (R4).
- **Ambiguity in 3 (c).** "ret^{L3′}_c(R) ⊄ …" is about the *computed* closure: the true closure
  always satisfies C9, by PO4. It should cite E1-F3's "computed closure" (R3).
- **Partial shard sets.** σ applies 3 (c) only to *accepted* shards, so a run with a missing shard
  can still have σ = OK. Faithful to the ruling, and given the certification above, harmless.
  Say so explicitly (R3).

**E1-T5: accepted.**
- The quantity's-cone reading is fixed, and the degenerate tip reading's L_G ≡ 0 is shown.
- The seed condition matches PO7 at t ≥ 0 and at slice −1, and it is independent of whether near
  tips or all tips are used. I checked this: the far tips give |c| + t − 1 > 7.

**E1-T3 and E1-T4: accepted.** The four facts listed for E1-T4 are exactly those my PO-L2-7 check
used.

**E1-F6: accepted.**
- "Add 4 counts" is implemented as one survivor cell per (degeneracy, convention), with the plain
  counts as marginals. That is what my recommendation meant: 58.
- Invariance and count preservation are argued correctly. Stabilizers are conjugate within an
  orbit, and equal contexts give equal closures.

**E1-F3: faithful to the ruling's letter, but the ruled scope needs re-decision (R2, owner 1).**
- **The definitions are unambiguous.** The shared near tip is defined over a set Q, and its
  equivalence with PO3 (b) is verified on 230,268 cases. Q⁰ and the computed closure are both
  clear.
- **Facts E1 does not state** (both follow from r5's definitions):
  - **Under A, T_A ⊆ Surv_A, always.** ret contains non-fixed quantities only, so two retained
    quantities sharing a tip make S_A non-empty.
  - **Under G, a retained shared tip that is eligible is a seed tip.** Its owner is then in S_G. So
    T_G ∖ Surv_G is exactly the set of records whose retained ties are all ineligible, that is,
    in-frame.
- **So set 2 adds nothing anywhere except in-frame ties under G.** There my parenthetical "cheap,
  non-vacuous wherever ties are retained" was wrong:
  - in-frame quantities are retained because none of their tips is eligible, not because of ties,
    so these ties carry no tie logic;
  - at "every record, every member" they are costly: 595 of 1,400 toy records, against a G
    reference closure of about 90–280 ms each.

**The drafter's open points.**
- **(a)** Confirmed. Under the "eligible (seed) tips only" reading, set 2 ⊆ Surv under both
  conventions, so it is redundant. The C7 scope then reduces to Surv ∪ (I_c ∩ H₁₀₀) ∪ H₁₀₀₀. That
  is honest about what is checked, and it is cheap. Owner decision 1.
- **(b)** E1 is ambiguous here. It says both "a fixed function of the record's enumeration index"
  and "the same unit as H₁₀₀₀", while Layer 2 draws over representative indices. It must fix the
  unit (R1). I recommend every record index in [0, N), as in r5's "sample of the rest", which
  counts records. A sampled non-representative record is then checked against its carried closure
  with its own reference context. Owner decision 2, with that recommended default.
- **(c)** The cost of "every record" in set 1 is the survivor count times the orbit size, which is
  acceptable (L2-R2). In set 2 it is acceptable only under the eligible reading. Resolved by owner
  decision 1.
- **(d)** Sound; see E1-T2. Only text changes are needed (R3, R4). Optional owner decision 3.
- **(e)** E1 correctly leaves the "geometric fact only" wording pending, since no ruling covers it.
  It should be confirmed before the Layer-2 freeze. Owner decision 4.
- **(f)** 58 is faithful to "add 4 counts" and is information-complete: the plain count is the
  marginal. 62 would add redundant cells. Not needed.

**Neutrality and timing (task 3).**
- Every item is fixed before any v8 result: no S1a, closure or shared-tip count exists on v8.
- No item changes the masking law, the geometry, the domain, the survivor definitions or the
  labels.
- E1-F3 changes C7's pass condition, and E1-F6 extends C8's count preservation, each as ruled.
- κ is untouched. Layer 2 r2 carries κ as an OWNER placeholder, with `launch_within_budget` null,
  so no default is chosen.

## Required changes

**R1. Fix H₁₀₀'s sampling unit.** In E1-F3, replace "H₁₀₀ is drawn over the same unit as H₁₀₀₀.
The frozen text leaves the sampling rule, its unit included, to the Layer-2 configuration … The
Layer-2 draft draws its C7 samples over the indices of orbit representatives." with the owner's
choice. My recommended text:
> H₁₀₀ and H₁₀₀₀ are drawn over every record index i ∈ [0, N); a sampled record that is not its
> orbit's representative is checked against the closure the run assigns to it, with its own
> reference context.

**R2. E1-F3, set 2.** Add the two facts:
> Under A, T_A ⊆ Surv_A. Under G, a record of T_G that is not in Surv_G has only ineligible shared
> tips among its retained quantities.

Then implement owner decision 1. If the eligible reading is chosen, define set 2 with "an eligible
shared near tip" and state that set 2 ⊆ Surv_c.

**R3. E1-T2, case 3 (c).** Write "the computed closure (E1-F3)" for each ret_c(R). Add:
> σ reads C9 only on accepted shards; shard completeness is not an input of σ (it determines the
> run's INCOMPLETE label, L1 §5).

**R4. E1-T2, attribution and the certification argument.**
- Cite Layer 2 r2 (`4a51c675`) as the source of σ, noting that the L3-bound reference checks come
  from L2-R8 and only add non-OK cases.
- Add the argument: "C0, C17 and C18 on ret^{L3′}_c(U) certify, by the reference code, that the
  computed bound is the greatest self-supporting subset of Ctx(U); so evaluating rule T when σ = OK
  uses a certified bound whatever the run's label".
- Layer 2's plan §4 should then be aligned with E1, since the plan and the code currently disagree.

**R5. A naming collision.** The document is "E1", and r5's identity merge is also "E1"
(equivalences E1–E4). Inside the erratum, E1-F6 cites "(E1)" and "(E2)" for the equivalences.
Either rename the erratum (for example "ER1", with tags ER1-T1 …), or write "equivalence E1" and
"equivalence E2" wherever the equivalences are meant.

## Owner decisions

1. **C7 set 2 (re-decision with corrected facts).** My recommendation in `LAYER2-REVIEW.md` (lines
   292–296) called set 2 "cheap, non-vacuous wherever ties are retained". That is wrong:
   - under A it is always contained in the survivors;
   - under G it adds only in-frame ties, which are uninformative, and at "every record" they are
     costly (595 of 1,400 toy records).

   The options:
   - **(i) Eligible (seed) shared tips only.** Set 2 ⊆ Surv, so the effective scope is survivors,
     a 1-in-100 sample of initial-context ties, and the 1-in-1,000 base sample. **Recommended.**
   - (ii) The literal any-tip reading, as drafted.
   - (iii) Drop set 2 and raise the H₁₀₀ rate. That rate is a budget lever, best decided with κ.
2. **The sampling unit of H₁₀₀ and H₁₀₀₀.** Recommended: every record index (R1).
3. **Optional.** Whether σ should also go VOID when L_A or L_G recomputed with `s0ref` cones
   differs from the production count. This is cheap, about 1,600 quantities, but it would add to
   the ruled σ. Recommended yes, as a further amendment item. Shard completeness should stay
   outside σ.
4. **The "geometric fact only" wording** of rule T's zero branch, which remains pending. Recommended:
   confirm it before the Layer-2 freeze.
5. **No decision needed** on 58 against 62: 58 is faithful and information-complete.
6. **Unchanged:**
   - κ and S7 remain open, with no default;
   - E1 takes effect only after R1–R5 and decisions 1–2 are applied, with a diff-only re-check;
   - v8 is not authorized.
