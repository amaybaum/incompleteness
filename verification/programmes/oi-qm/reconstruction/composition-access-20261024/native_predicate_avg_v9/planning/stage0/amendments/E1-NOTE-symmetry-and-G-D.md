# Orbit reduction and fault detection; the G decomposition (NP-AVG-1 Stage 0)

A note beside erratum E1 (`E1-LAYER1-ERRATUM.md`). It states two results that arose in E1's
review. It governs nothing; E1 governs the specification and cites this note.

**Sources.**
- `../../review/E1-ANALYSIS.md`, §A (C7 and orbit reduction) and §E (classification).
- `../../review/E1-RECHECK-r2.md` (SHA-256
  `98f092f3a722d12a3fc43ece2a85daa189362ceb6f5d7b3ae92e0ba132120e5e`), §3 and §4.
- `../r5/STAGE0-PLAN-r5.md` ("L1"), frozen at `f33d8d63`.

**Labels.** *Proved* marks a written argument from the stated assumptions. *Observed (toy)* marks a
number on the toy class: 3D, n = 2, region ball(1), last slice 6, port (0, 0, −2); 1,400 records
in 488 C4v orbits. Observed numbers say nothing about v8. Nothing in this note was computed on
v8's configuration class.

## Part 1. Symmetry reduction can preserve ordinary values while failing to preserve fault detection

### Setting

- ℛ is a finite set of records, and Γ is a finite group acting on ℛ. Here Γ = C4v, acting on the
  record space of L1 §1.
- V is a set of values with a Γ-action. Here V holds retained sets, and g acts on site-times.
- f : ℛ → V is the specification, and it is **equivariant**: f(gR) = g·f(R) for all g and R.
  Here f is the L3′ closure under a convention, equivariant by L1 §1 (equivalence E4) and PO4.
- P : ℛ → V is an implementation, possibly faulty: the production closure.
- ref : ℛ → V is a reference implementation of f.
- **An orbit-reduced run** fixes, for each orbit, a representative rep(R), and for each record an
  element g_R ∈ Γ with g_R·rep(R) = R. It evaluates P on representatives only, and *reports* the
  value P̂(R) := g_R·P(rep(R)) for every R.

### Proposition 1 (what the reduction preserves; proved)

If ref is equivariant, then for every R ∈ ℛ:

[P̂(R) = ref(R)] ⇔ [P(rep(R)) = ref(rep(R))].

The following consequences hold:
- every count of records satisfying a predicate D(R, v), evaluated at v = P̂(R), equals the sum
  over representatives of the orbit size times D(rep(R), P(rep(R))), provided D is invariant under
  (R, v) ↦ (gR, g·v);
- membership in any Γ-invariant set of records is constant on orbits.

*Proof.* P̂(R) = g_R·P(rep(R)) and ref(R) = g_R·ref(rep(R)), and g_R acts bijectively on V. This gives
the equivalence. For the counts, D(R, P̂(R)) = D(g_R·rep(R), g_R·P(rep(R))) = D(rep(R), P(rep(R))) by
invariance, so each orbit contributes its size times the representative's value. ∎

So verdicts, multiplicities and set membership computed from reported values are the same under
the reduction as without it.

### Proposition 2 (what the reduction does not preserve; proved)

Let P′ be any implementation that agrees with P on every representative: P′(rep(R)) = P(rep(R)) for
all R. Then P̂′ = P̂ on all of ℛ. In particular, if P = f on every representative, every check, count
or verdict computed from reported values takes the same value for P′ as for a correct
implementation, whatever P′ does on non-representative records.

*Proof.* P̂′(R) = g_R·P′(rep(R)) = g_R·P(rep(R)) = P̂(R). ∎

**The structural reason.** In an orbit-reduced run, the implementation is never evaluated on a
non-representative record. A fault confined to non-representative orbit members therefore leaves
every reported value unchanged. Such a fault is detectable only by evaluating the implementation
directly on such a record and comparing the result with the reference, or with the reported
value.

**Scope.** The result holds for any orbit-reduced check whose reported values are taken from
representatives. In NP-AVG-1 Stage 0 that covers:
- a C7 check on carried closures;
- the carried counts and observer classes under C8;
- any gate run on representatives only.

Within such a run, the guards against member-only faults are the checks that evaluate members
directly:
- C8 on its sampled, flagged and survivor orbits;
- E1-F3's per-record C7 on sets 1–4.

Proposition 2 does not need the reference to be equivariant. If the reference is not equivariant,
a reference fault confined to members is equally invisible to a representative-only check.

**Consequence in E1** (E1-F3). C7 on its scope is computed per record. For each record R, it
compares R's direct production closure with R's reference closure, and R's reported (carried)
result with its direct closure.

### Illustration (observed, toy)

The planted faults are in `E1-ANALYSIS.md` §A2 and `E1-check` part I, under convention G:
- **F1** drops every retained in-frame quantity whose near tip is shared, on every record. It is
  equivariant.
- **F2** applies F1 to non-representative records only.

| fault | records with a wrong direct result | records with a wrong reported result | caught by a representative-only check | caught by the per-record check |
| --- | --- | --- | --- | --- |
| F1 | 595 | 595 | on 283 representatives | 595 |
| F2 | 312 | 0 | 0 | 312 |

F2 is a planted fault. Whether any such fault exists in the production code is not known; the
proposition shows only that a representative-only check cannot see one.

## Part 2. Lemma G-D, the G decomposition

### Assumptions

- **(L1 §2) Eligibility and the frame.** Under convention G, a tip is eligible iff it lies outside
  the frame. The frame is the union of the G-convention cones (slices −1 and 0) of Φ, V, p and the
  even port samples, which are in every context.
- **(L1 §2) Elimination.** Under L3′, a non-fixed quantity is eliminated if some eligible tip of
  it lies in the cone of no other currently retained quantity, fixed quantities included. The rule
  is iterated to its fixed point, which is the greatest self-supporting subset (PO4). L3 is L3′
  without the far tips, with the same cones.
- **(PO7)** A quantity at t ≥ 0 with |c| + t ≤ 8 has its whole cone inside the frame. A quantity
  at t ≥ 0 has a seed (eligible) tip iff |c| + t > 8, and one at slice −1 iff |c| > 7. A quantity
  at slice −1 is B type at depth 0, and its cone is itself.
- **(L1 §3) Survivors.** S_G(R) is the set of retained quantities with at least one seed tip, and
  R is a G-survivor iff S_G(R) ≠ ∅.

### Definitions

- **Q⁰(R)** is the set of non-fixed quantities of Ctx(R).
- **In(R)** is the set of q ∈ Q⁰(R) with no seed tip, and **Out(R)** the set of those with a seed
  tip.
- **W(X)**, for X ⊆ Q⁰(R), is the greatest subset Y ⊆ X such that every eligible tip of every
  y ∈ Y lies in the cone of some y′ ∈ Y with y′ ≠ y.
- **F_G** = {R : In(R) has a shared near tip}.
- **T_G** = {R : ret_G(R) has a shared near tip}.
- **E_G** = {R : Out(R) has a shared eligible near tip}.

Here a set Q *has a shared near tip* iff two distinct elements of Q have equal e-tips for some
axis direction e (E1-F3).

### Statement (proved)

For every record R, and for both L3′ and L3:

ret_G(R) = In(R) ⊔ W(Out(R)).

*Proof.*
1. Eligible tips lie outside the frame (L1 §2).
2. The cones of the fixed quantities lie inside the frame, since the frame is defined as the union
   of their cones and those of the even port samples.
3. The cones of the quantities of In(R) lie inside the frame. For t ≥ 0 this is PO7. For t = −1
   the cone is the quantity itself, at |c| ≤ 7 on slice −1, which lies in the frame.
4. Hence no fixed quantity and no quantity of In(R) covers an eligible tip.
5. A quantity of In(R) has no eligible tip, so it is never eliminated, and In(R) ⊆ ret_G(R).
6. A quantity of Out(R) is eliminated iff it has an eligible tip covered by no other retained
   quantity. By step 4, only retained quantities of Out(R) can cover it. The fixed point on Out(R)
   is therefore W(Out(R)).
7. L3 has a subset of L3′'s tips and the same cones, so steps 1–6 hold for L3 unchanged. ∎

The proof uses only PO7 and the frame's definition, both of which hold for every quantity of the
domain at every slice t ≥ −1. It does not use the region's size or the toy class.

### Corollaries (proved)

1. **G-survival is internal to Out(R).** S_G(R) = W(Out(R)), since In(R) has no seed tip. So
   G-survival and G-linkage depend on Out(R) alone. In particular, the fixed quantities Φ, V and p
   take no part in G-survival except through the frame's definition.
2. **T_G = F_G ∪ (T_G ∩ Surv_G)** (`E1-RECHECK-r2.md` §4). Suppose two retained quantities share a
   near tip.
   - If both are in In(R), then R ∈ F_G.
   - Otherwise one of them is in W(Out(R)), which is then non-empty, so R ∈ Surv_G by
     Corollary 1.

   Conversely, In(R) ⊆ ret_G(R), so F_G ⊆ T_G. F_G is a function of Q⁰(R) alone and needs no
   closure.
3. **In-frame ties are inert.** A tie between quantities of In(R) involves no eligible tip, and
   the quantities of In(R) cover no eligible tip and are never eliminated. Such a tie affects none
   of the following: W(Out(R)), S_G(R), G-linkage, the L_G input of rule T (whose quantities have a
   seed tip, E1-T5), or any label.
4. **Closure-free supersets of the survivors** (`E1-RECHECK-r2.md` §4). Surv_G ⊆ E_G, by P_G: a
   ρ-maximal element of a non-empty S_G(R) ⊆ Out(R) shares each of its aligned near tips, a seed,
   with another element of S_G(R). Likewise Surv_A ⊆ I_A by P_A, where I_A is the set of records
   whose initial context has a shared near tip under A. P_G and P_A are L1's propositions, resting
   on PO3, PO5 and PO7.
5. **The reference computation.** Under G, the reference closure equals W(Out(R)) ∪ In(R) on every
   record (`E1-RECHECK-r2.md` §4). For every production output, faulty or not, C7's verdict is
   therefore the same under either reference form. The equivalence does not extend to faults in
   the reference implementation itself, since the two forms run different code paths; such faults
   produce spurious C7 failures (VOID), not missed ones. Using this form is conditionally approved
   and does not execute until the owner confirms that the proof meets the bar (E1 §9).

### Classification

**ELABORATING** under §A.31 (`E1-ANALYSIS.md` §E). The lemma is a short consequence of PO7 and of
the frame's definition in L1 §2, and it states the light-cone structure of the initial pair as a
decomposition. It yields a closure-free definition of C7's set 2 under G, exposes a fault that a
closure-defined set 2 would hide (F1), and allows a cheaper reference computation. It adds no new
fact about the dynamics.

### Observations (toy)

These are toy-class numbers, from `E1-check` part H and `E1-ANALYSIS.md` §A1:
- The decomposition holds on all 1,400 records, for L3′ and L3, against the production closure and
  the full `s0ref` closure. It also holds on 12 planted toy-geometry records, all of which are A-
  and G-survivors.
- T_G = F_G = 595 of 1,400 records, in 283 orbits. None of these ties is eligible, and the class
  has no survivors.
- E_G has 12 of 1,400 records, all of them in F_G. I_G has 667 records and I_A 1,071.

The frequencies reflect the toy geometry: region ball(1), the frame, and the port (0, 0, −2).

### What remains unproved or open

- **The v8 sizes of F_G and E_G.** Both can be computed without any closure in the dry run. Neither
  has been computed.
- **The reference implementation's G-D form.** The lemma concerns the specification. That the G-D
  code path computes it is checked on the toy class only. A fault in that code is not covered by
  the proof; the cross-check against the full form guards it, and it fails safe.
- **The production engine on v8.** That it computes the specified closure on v8's records is what
  C7, C17 and C18 check in the run; nothing here proves it.
- **Beyond the masking closure.** The inertness of in-frame ties is a statement about the masking
  closure and its labels only. Nothing is claimed about their bearing on any law question
  (Stage 1).
- **E_G in C7's scope** is owner decision O1, optional and not adopted (E1 §9).
