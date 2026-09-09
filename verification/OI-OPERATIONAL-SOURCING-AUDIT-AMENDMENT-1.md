# Operational sourcing at the Arc C boundary — Amendment 1: the empty carrier in consequence 3

Base: `main` at `7f13cb64bf815e0b1333bc862ce9ab623177cb2e`.

Amends `verification/OI-OPERATIONAL-SOURCING-AUDIT.md`, frozen at commit
`15e29b25f97319303738031b1bc87a364bb9c714`, blob
`e9ca45351b58354564552471aa8fe81537a8e557`, merged to `main` by PR #551.

This is an **append-only, execution-affecting amendment**, committed before the work it affects, as
the frozen execution discipline requires. The preregistration itself is immutable and is not edited.

## The defect

S1's consequence 3, as frozen, reads:

> **The augmented class is everything.** For every finite `T` with decidable equality and every
> unitary `W` on `T`, `W` occurs — up to the relabelling that implementation classes are already
> invariant under — as the unitary of a representation of some OI-realizable family.

**This is false at `T = ∅`, and the obstruction is one the merged corpus already proves.**

`QfbData.IsLaw` requires the initial law to be normalized:

```lean
def QfbData.IsLaw (Q : QfbData V) : Prop :=
  Q.U ∈ Matrix.unitaryGroup Q.Bas ℂ ∧ (∀ b, 0 ≤ Q.init b) ∧ ∑ b, Q.init b = 1
```

A sum over an empty index type is `0`, and `0 ≠ 1`, so **no lawful datum has an empty basis**. This
is exactly the argument the merged Arc C module already runs, in
`OIBridge/QuantumRepresentationT3.lean`:

```lean
theorem nonempty_of_qStar {Γ : ℕ → Matrix V V ℝ} (h : QStar Γ) : Nonempty V := by
  obtain ⟨Q, hQ, _, _⟩ := h
  have hb : Nonempty Q.Bas := by
    by_contra hemp
    rw [not_nonempty_iff] at hemp
    have : ∑ b : Q.Bas, Q.init b = 0 := Finset.sum_of_isEmpty _
    rw [hQ.2.2] at this
    exact one_ne_zero this
  exact ⟨Q.read hb.some⟩
```

So the empty type cannot be the basis of any representation at all, and no padding construction can
place the unique matrix on `∅` there. The universally quantified form of consequence 3 is therefore
not merely hard at the empty carrier — it is false.

The defect is in the preregistration, not in the execution. It was found at the S1 core checkpoint,
before any work on consequence 3 or S3a began.

## The repair

**1. Consequence 3 is narrowed to nonempty finite carriers.** It now reads:

> **The augmented class is everything, at every nonempty carrier.** For every **nonempty** finite `T`
> with decidable equality and every unitary `W` on `T`, `W` occurs — up to the relabelling that
> implementation classes are already invariant under — as the unitary of a representation of some
> OI-realizable family.

The relabelling step remains load-bearing and remains subject to the frozen requirement that it be
proved or the consequence reported as unproved.

**2. S3a's conclusion is preserved at all finite carriers, by splitting the two cases.** The
trivialization S3a reports is that the representation-augmented access contains every unitary on
every finite carrier, and that conclusion survives intact:

- at every **nonempty** finite carrier, from consequence 3 as narrowed;
- at the **empty** carrier, from the stated access itself, with no appeal to representation. On an
  empty type there is exactly one matrix, which is therefore the identity, and the base `permClass`
  architecture already contains it (`permClass_arch`). The case is vacuous rather than argued.

So representation padding supplies all nonempty-carrier unitaries, the stated access supplies the
empty-carrier case, and S3a's reported disqualification is unchanged: a criterion that returns
*Sourced* for every resource has no discriminating power.

The report must state the split where it states the trivialization. Presenting S3a's conclusion as
though a single uniform argument covered every finite carrier would misdescribe the proof.

## What this does not change

- **S1's core is unaffected**: the padded datum, its unitarity, the Born factorization, and the
  arbitrary-ancilla quantification. That core is proved and committed on the execution PR #554; it
  is **execution content, not frozen material**, and remains subject to final exact-head review like
  everything else on that PR. Only this preregistration and its amendments are frozen.
- **The invariance chain is unaffected** and may proceed.
- **Consequences 1 and 2 are unaffected** and may proceed. Both are existential over representations
  of a given family and never quantify over an empty carrier.
- **S2 and S3b are unaffected.** Both are proved and kernel-clean and committed on the execution PR
  #554 — **not merged to `main`** — and neither mentions consequence 3. Their standing is that of
  reviewed execution content awaiting final exact-head review, not of settled corpus.
- Every control, the disposition criterion and its precedence, the outcome taxonomy, the evidence
  hierarchy, the non-doings and the execution discipline stand unchanged.

## Execution hold

**No work on consequence 3 or on S3a occurs until this amendment is frozen and merged.** Work on the
invariance chain and on consequences 1 and 2 continues meanwhile, under the preregistration as
frozen.

**Ancestry, not chronology.** After this amendment is frozen and merged to `main`, the execution PR
#554 **absorbs that merge** before any consequence 3 or S3a execution commit is made. The ordering is
then checkable from the history — every such commit descends from the merge carrying the amendment —
rather than merely attested by the order in which the work happened. This is the same standard the
preregistration's own execution discipline sets for the freeze.

This amendment is itself a control-plane PR, which the frozen discipline declares the exception to
the one-PR-per-round rule; there is still exactly one execution/result PR for the round.

## Provenance

Found at the S1 core checkpoint review of PR #554, at head
`b6cd82fb3f3d0e7c6a58361f341b12f8cf166cdb`. Verified against the merged sources before drafting:
`QfbData.IsLaw` in `OIBridge/QuantumRepresentation.lean` and `nonempty_of_qStar` in
`OIBridge/QuantumRepresentationT3.lean`.

Status: **draft amendment; nothing here is frozen until the reviewer approves an exact commit and
blob, and no consequence 3 or S3a work begins until it is merged.**
