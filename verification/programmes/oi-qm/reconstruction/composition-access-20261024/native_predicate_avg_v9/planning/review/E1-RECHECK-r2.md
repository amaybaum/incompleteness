# Diff-only re-check: erratum E1, revision 2

**Object.**
- The range `47e16576..d2d5e92f` on PR #935, limited to E1:
  - `stage0/amendments/E1-LAYER1-ERRATUM.md` (SHA-256 `4db591ad…ce8b`);
  - `E1-CHANGES-r2.md` (`d08b888f…8237`);
  - `E1-check/` (`e1_check.py` `0aff51b7…9ea7`, `e1_check.out` `15261d85…ce20`).
- Read against r1 (`c00b4486…12ab`), my `E1-REVIEW.md` and my `E1-ANALYSIS.md`. The committed
  copies are byte-identical to mine.
- It includes the owner's decisions of 2026-10-26 relayed during the re-check.

**Read-only. Toy instances only.** Nothing ran on v8. My outputs are in `S/npavg/review-e1/r2/`.

## Verdict: ACCEPT WITH NITS

E1 r2 applies R1–R5 and my §D text faithfully. I accept all four departures. σ case 2 (d) and the
precedence are correct. The check replays exactly, and its countercontrols fail when they should.

**Six nits**, N1–N6 below, are text-only:
- three record the owner's decisions of 2026-10-26, which came after r2 was written;
- three tighten statements that are true but under-qualified.

None changes a definition, a population, a count or a label. Once they are applied, E1 can take
effect without a further review round. The nits are mechanical, but they must be applied before
E1 is in effect, because N1 governs whether the G-D shortcut may execute.

## 1. Fidelity (task 1)

**R1–R5** are applied as E1-CHANGES-r2 maps them:
- R1: the record-index samples, with the hash rule;
- R2: T_A ⊆ Surv_A, and set 2 under G is (T_G ∩ Surv_G) ∪ F_G;
- R3: σ 3 (c) reads the computed closure, and shard completeness is not an input;
- R4: the Layer 2 r2 attribution, L2-R8, and the certification argument;
- R5: the tag convention and "equivalence E1/E2".

**My §D text.** `E1-check` part L confirms that nine §D blocks and eight §10 rows stand verbatim. I
spot-checked §4, §6a, §7 and §8 by eye.

**The four departures: all accepted.**
1. **"As drafted" written out, and one clause of the computed-closure definition dropped.
   Accepted.**
   - The written-out definitions match r1's in content.
   - The dropped clause was "Where the two differ, C8 fails and the run is VOID". Its role passes
     to the new per-record check, "C7 fails on R if … the run's reported (carried) result for R
     differs from R's direct closure", which is VOID. That check is stronger: it covers every
     record of C7's scope, not only C8's sampled orbits. Outside C7's scope, carried-against-direct
     comparison remains C8's, as in L1. The specification is preserved.
2. **G-D permission changed to: full `s0ref` by default, G-D only with approval. Accepted.** This
   is more conservative than my text, and it matches the owner's later ruling ("Keep full
   reference computation as the default"). See N1 for recording that ruling.
3. **The rank statement corrected. Accepted.** My "every list carries rank 3 per degeneracy" was
   wrong: the frozen 54 carries rank 1 for D6 and D9. The corrected sentence is exact. It
   preserves the intended specification: 58 has rank 3 per degeneracy, so it is complete, and 62
   adds only determined cells.
4. **Parentheses in the §D6 rows. Accepted.** They name the `E1-check` parts and mark the G-D row
   "(when the G-D form is approved, §9)". The wording is unchanged.

The other edits listed in E1-CHANGES-r2 ("Other edits", and the §6a "What changes" and
checkpoint) add no requirement beyond the rulings.

## 2. σ case 2 (d) and the precedence (task 2)

- **Case 2 (d)** is correct and faithful. VOID if L_A or L_G, recomputed from the L3′ bounds with
  `s0ref`'s explicit cones and tips, differs from production. The L3 values are reported, not a
  σ condition, since the ruling names L_A and L_G.
- **The precedence** matches "S1a its own diagnostic status, not an overriding success label":
  - rule T is evaluated iff σ = OK;
  - σ never overrides the run label;
  - a σ failure enters the label as an INCOMPLETE, VOID or MISMATCH reason;
  - "A run cannot pass because σ = OK if any other mandatory check fails";
  - an outcome evaluated in a failed run is recorded beside its label, with no S1b proposal
    without the owner.
- **The certification argument** is correct.
- **Evidence** (`E1-check` part K): the recomputation agrees (15 and 7 for L3′ and L3), a
  perturbed count fires 2 (d), and Layer 2 r2's `label` keeps VOID, MISMATCH and INCOMPLETE under
  σ = OK.
- **My countercontrol.** I mutated `l2merge.label` on a scratch copy so that VOID is ignored.
  `K.sigma_OK_never_overrides_a_failing_label` fails (exit 2).

## 3. C7's independent detection capability, and orbit reduction (task 3)

**The statements in E1 r2 are correct.**
- "On a record where C0, C17 and C18 all run, C7 is implied by them (proved)."
- "C7's distinct contribution is its independent algorithm and its coverage of sets 1–4."
- The redundancy is "recorded, not grounds for removal".

**The orbit-reduction paragraph is correct and rests on proofs, not toy observation.** It claims
equivalence for verdicts, multiplicities and set membership, from C4v-equivariance of the
specification. It denies equivalence for failure detection, for a structural reason: a
member-only fault changes no carried result. F2 illustrates this; the proof does not depend on it.

Two statements need qualifying (N2, N3).

## 4. The owner's decisions folded in (items 1–5 of the coordinator's message)

**Item 2: is the closure-free F_G definition mathematically justified in general, not only
against F1? Yes.**

*Proof*, for every record R ∈ ℛ under the specification:
1. Lemma G-D gives ret_G(R) = In(R) ⊔ W(Out(R)).
2. Suppose two retained quantities share a near tip.
   - If both are in In(R), then R ∈ F_G.
   - Otherwise one is in W(Out(R)), which is then non-empty, so R ∈ Surv_G (S_G = W(Out(R)),
     Corollary (i)). Hence R ∈ T_G ∩ Surv_G.
3. Conversely, In(R) ⊆ ret_G(R), so F_G ⊆ T_G.
4. Hence T_G = F_G ∪ (T_G ∩ Surv_G) for every R.

This uses only Lemma G-D (from PO7 and L1 §2's frame) and L1 §3's definitions. F1 played no part.
The reason for the closure-free form is general: a set defined by a computed closure can be
emptied by the fault it is meant to catch, while F_G is a function of Q⁰(R) alone. F1 is one
instance of that.

**Can some other fault class escape?** Yes: over-elimination of genuine survivors.
- **Which part is exposed.** The part (T_G ∩ Surv_G), and set 1, use the *computed* survivor
  status. A production fault that eliminates a true survivor, where R has no in-frame tie, removes
  R from sets 1 and 2.
- **Where such faults are still caught.**
  - in-run: only by sets 3 and 4, at 1 in 100 and 1 in 1,000, and by the sampled C11 (i), C17 and
    C18;
  - pre-flight: by the planted controls C3, C11 (iii) and C15.
- **This is not new.** It is L1 §4's acknowledged asymmetry: "MISMATCH … cannot detect
  over-elimination".
- **A closure-free superset of the survivors exists, by the frozen propositions:**
  - by P_G, Surv_G ⊆ E_G := {R : Out(R) has a shared *eligible* near tip};
  - by P_A, Surv_A ⊆ I_A.
- **Toy sizes** (`eg_probe.out`): E_G has 12 records and I_A 1,071 of 1,400. The toy frequencies
  carry no information about v8.

Adding E_G to C7's scope under G would close this escape cheaply. It is beyond the current
ruling, so it is owner decision O1 below. Under A the corresponding superset, I_A, is the frozen
literal scope, which the ruling deliberately samples.

**Item 3: does the G-D shortcut meet the owner's bar?**

*Proof of equivalence over the whole domain, including the detection of production faults.*
- By Lemma G-D, for every R ∈ ℛ and both rules, In(R) ∪ W(Out(R)) = GSS(Ctx(R)).
- The proof uses only PO7 and the frame's definition, which hold for every quantity of the
  domain, at every t ≥ −1. It does not use the toy class.
- So both reference forms, *as specified*, return the same set for every record.
- For any production output P, faulty or not, C7's verdict [P(R) = ref(R)] is therefore
  identical under either form. Every production fault is detected identically.

The bar is met for production faults. It is not met for faults in the reference implementation
itself, because the two forms exercise different code paths: G-D never evaluates in-frame covers.
Such a fault is not a production fault, and it fails safe: it produces a spurious C7 failure,
VOID, not a missed one. Except in the coincidence of a reference fault matching a production
fault on the same record, it cannot hide a production fault.

The cross-check E1 r2 already requires when G-D is approved (G-D against the full form on the
whole toy class and on every record of sets 3–4) bounds that residual. So the shortcut may
execute, under the owner's conditional approval, provided E1 records this proof and the
cross-check (N1). Without N1, E1 r2's text already keeps it non-executing ("needs the owner's
approval"). That is safe, but it is out of date.

**Item 4** (58 counts, S1a as an independent diagnostic, the L_A/L_G recomputation): consistent
with E1 r2. N1 records the approvals.

**Item 5** (the four departures): accepted explicitly in §1.

## 5. Structural properties (task 4)

- **Lemma G-D** is stated in E1-F3 as "proved here; a proof obligation of this erratum", with its
  proof.
- **The toy observations are separated.** The 595 of 1,400, the 15 and 7, and so on are confined
  to §0 ("toy geometry … no information about v8") and §11.
- **Classification.** E1 does not class the lemma as ELABORATING; `E1-ANALYSIS.md` §E does.
  Within a Layer-1 erratum that is appropriate, but a pointer helps (N4).

## 6. The check, and what changed (tasks 5 and 6)

**The check replays.** `e1_check.py` exits 0, all 55 checks pass, and its output is byte-identical
to `e1_check.out`, normal and `-O`, in 18 s.

**Countercontrols** (my scratch copy, `r2/cc/`):

| perturbation | result |
| --- | --- |
| a word changed in a quoted ruling in `E1-ANALYSIS.md` | exit 2: `A.quotes_at_stated_lines` and `L.section_D_blocks_verbatim` fail |
| the precedence sentence in the erratum weakened ("A run passes because σ = OK …") | exit 2: `L.section_D_blocks_verbatim` fails |
| `l2merge.label` made to ignore VOID | exit 2: `K.sigma_OK_never_overrides_a_failing_label` fails |

The built-in controls behave as stated:
- F1 is caught 595 of 595 by the per-record set 2, and 0 by the computed-closure mutant;
- F2 is caught 312 of 312 by direct per-record checking, 0 by the representative-only check, and
  shows no wrong reported result;
- the perturbed L_A count fires case 2 (d).

**Nothing else changed.** Between `47e16576` and `d2d5e92f`, the only files changed are E1's three
files, `review/E1-ANALYSIS.md` and `review/e1-analysis/` (byte-identical to mine), and the planning
`README.md` and `SHA256SUMS`. Untouched: `r5/`, `code-r5/`, `design-r5/`, `LAYER1-FREEZE.md` and
`layer2/`. The frozen plan's SHA-256 is verified by part A.

## Nits (apply before E1 takes effect)

**N1. Record the owner's decisions of 2026-10-26.**
- In §1's table:
  - C7 per-record evaluation over all 595 G records: "approved";
  - revised check set: "approved in principle";
  - counts and S1a: "approved".
- In §9, replace the G-D bullet with:
  > **Lemma G-D in C7's reference computation.** Conditionally approved (amaybaum, 2026-10-26):
  > "Keep full reference computation as the default. Permit the shortcut only after proving its
  > equivalence to the reference computation over the complete specified domain, including failure
  > behavior." The proof: by Lemma G-D, for every R ∈ ℛ and both rules, In(R) ∪ W(Out(R)) =
  > GSS(Ctx(R)), using only PO7 and the frame's definition, which hold on the whole domain; so for
  > every production output P, faulty or not, C7's verdict is the same under either reference
  > form, and production faults are detected identically. The equivalence does not cover faults in
  > the reference implementation itself; these fail safe (a spurious C7 failure, VOID), and the
  > cross-check of the G-D form against the full form, on the whole toy class and on every record
  > of sets 3 and 4, guards them. The full form remains the default; the G-D form executes only
  > when Layer 2 enables it with that cross-check.

**N2. The C17 ∧ C18 implication.** In E1-F3 "What changes", write "On a record where C0, C17 and
C18 all run (with the closure code's retained/logged partition of Q⁰, a code invariant), C7 is
implied by them (proved)".

**N3. Unions of orbits.** In "Orbit reduction", replace "sets are unions of orbits" with "sets 1
and 2, and I_c, are unions of orbits; the record-index samples H₁₀₀ and H₁₀₀₀ are not, which is
one reason C7 is computed per record".

**N4. Classification pointer.** After Lemma G-D's ∎, add "(Its classification under §A.31 —
ELABORATING, a corollary of PO7 and L1 §2 — and the toy observations are in
`../../review/E1-ANALYSIS.md` §E.)"

**N5. The residual escape.** In E1-F3 "What changes", add:
> Over-elimination of a true survivor without an in-frame tie removes its record from sets 1 and
> 2; in-run it is caught only by sets 3 and 4 and the sampled C11 (i), C17 and C18, and in
> pre-flight by C3, C11 (iii) and C15 (L1 §4's asymmetry).

**N6. Status line.** Once N1–N5 are applied, change the status line to "in effect".

## Owner decision

**O1. Optional. Close the residual escape under G.** Add E_G = {R : Out(R) has a shared eligible
near tip} to C7's scope under G, as set 5. It is closure-free and contains Surv_G by P_G. On the
toy class it is 12 of 1,400 records; v8's size is unknown and computable without any closure in
the dry run. It would be a further amendment, not part of E1. Under A the analogous superset, I_A,
is the frozen literal scope, which the ruling samples at 1 in 100.

## Where the two findings belong

I agree with a single standalone note beside E1, for example
`stage0/amendments/E1-NOTE-symmetry-and-G-D.md`, written after this verdict. One note is enough
(§A.28: repo minimalism).
- **Part 1.** "Symmetry reduction can preserve ordinary values while failing to preserve fault
  detection." State the theorem (verdict and multiplicity equivalence under equivariance), the
  structural reason (carried results never exercise member-only faults), and F2 as the toy
  illustration.
- **Part 2.** Lemma G-D, as a separately identifiable result: statement, proof, the §A.31 class
  (ELABORATING), its corollaries (T_G = F_G ∪ (T_G ∩ Surv_G), and Surv_G ⊆ E_G by P_G), and the
  toy observations, labelled as such.

It should not be placed in the Layer-1 erratum, which governs the specification, nor in Layer 2,
which implements it. E1 only cites it.
