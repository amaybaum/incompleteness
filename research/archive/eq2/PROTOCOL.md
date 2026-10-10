# EQ2 threads A–C — design-only protocol (owner request, 2026-10-08)

**Status.** Design only. Nothing produced here is adopted, frozen or governed. No governed proof round is chosen until
the coordinator compares the three results and the owner reviews them separately.

## The owner's decisions

These are recorded decisions, not adopted premises.

- **D1 — equivalence.** The target is operational equivalence with a coherent family of representations: one per
  token, not one fixed orientation per system type.
  - The representations preserve states, effects, probabilities, available operations, composition and idle extension.
  - The stricter per-type result is a separate theorem. It names the extra exchange symmetry it needs.
- **D2 — dimension.** The gate route is the primary route to d = 3. The continuous route continues independently, and
  neither route's assumptions substitute for the other's.
- **D3 — IE₂.** IE₂ is the native idle-extension obligation that corresponds to observational independence.
  - It is an instance or consequence, not an equivalence of definitions.
  - `ObservationalIndependence` is `HasParallelReferenceExtension` over an already matrix-based theory. A typed bridge
    from native IE₂ is therefore required.
- **Layering.** The eventual target is "native operational premises ⟺ finite quantum theory up to operational
  equivalence".
  - **Layer (I):** given coherent charts, the native premises hold ⟺ the presented theory is QM. Layer (I) stays
    explicitly conditional, and it does not close K∞, K2 or Kₙ.
  - **Layer (II):** chart existence. K∞, K2 and Kₙ close here.

## Required reading, before anything else

- `scratchpad/eqreview/INTEGRATION-DESIGN.md`: design v2. This is the current state.
- `scratchpad/eqreview/SYNTHESIS.md` and `scratchpad/eqreview/REVIEW.md`.
- `scratchpad/eq/{A,B,C,D,E}/RESULT.md`: the five completed threads. Read their NOTES.md only where needed.
- `scratchpad/bal/LEDGER.md`: the balanced-NOT thread.

## Limits (all threads)

1. **Base.**
   - Certified main `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58`, read-only at `scratchpad/eq/base/` (manifest
     `scratchpad/eq/base.manifest.sha256`). Never write inside it.
   - Git history only through read-only git (`git -C /home/user/incompleteness show|log|cat-file|grep <rev> ...`).
   - No git command that writes: checkout, worktree, branch, commit, stash, reset, fetch, push, gc, tag.
2. **Writes.** Write only inside `scratchpad/eq2/<X>/`. Never modify `/home/user/incompleteness`, another directory
   under `scratchpad/`, or any earlier ledger. Do not read the other eq2 threads' directories.
3. **No outward actions.** No branches, PRs, commits, pushes, CI dispatch, freezes, round records, receipts, ROADMAP or
   manuscript edits, GitHub writes or comments, or artifact publishing. No premise adoption. Do not spawn agents.
4. **No Lean/lake.** There is no local toolchain; the kernel runs only in CI.
   - Lean text drafted here is a candidate, labelled UNBUILT.
   - "Kernel-proved" requires a landed identifier at `bcbc516f`, cited `file:line`.
   - Mathlib availability that you cannot check locally is labelled unverified. The pin is in
     `verification/lean-mathlib/lake-manifest.json` at the base.
5. **Exact arithmetic.** Use Fractions, exact sympy or exact algebraic numbers for every claimed identity, rank, sign
   or inequality. Floating point is labelled exploration only and certifies nothing.
6. **No hidden premises.** Name every hypothesis. A failed implication is answered by the smallest explicit
   countermodel, checked exactly, together with the named missing premise.
7. **Depth-first** (§A.12, §A.31). Fix a productivity test first. Walk one avenue to a result or a genuine wall, and
   number the branch nodes with a verdict at each.
8. **Controls.** A computational verdict prints only over green controls. A favourable branch gets maximum skepticism
   and a countercontrol, and a sign can be an artifact (§A.21). Record harness errors; never hide them.
9. **Converse test.** Check every proposed principle against finite-dimensional complex QM (it must hold there) and
   against at least one non-quantum foil.
10. **Literature before closure.** Theorem numbers you have not checked against the source are labelled unverified.
11. **Prior work.** Earlier ledgers are off-repo research, not kernel results. Re-verify anything you rely on, and do
    not redo settled work.
12. **Determinism.** Run scripts as `python3 -I -B`. Outputs stay in the thread directory and must replay
    byte-identically. Record a replay.

## Deliverable

`scratchpad/eq2/<X>/RESULT.md`, plus a running `NOTES.md` and the scripts, with these sections:

1. **Finding** — one paragraph.
2. **Target theorem(s)** — precise statements (Lean-level, UNBUILT), each with its layer ((I) or (II-k)) and direction
   (forward or converse).
3. **Hypotheses ledger** — every hypothesis, with:
   - its status: kernel identifier / exact / written / literature / unsourced;
   - whether QM satisfies it;
   - its independence evidence (a countermodel) where known.
4. **Missing lemmas** — kernel (with the `file:line` context), Mathlib (verified or unverified) and exact certificates.
5. **Formalization strategy** — rounds or modules, cost (cheap / moderate / heavy), the controls and countercontrols a
   governed round would need, and the order.
6. **Research questions** — THEOREM ROUTE / INDEPENDENT PREMISE (with countermodel) / COUNTEREXAMPLE / OPEN (with the
   named wall), with evidence.
7. **Evidence and probe log** — scripts, outputs, sha256 hashes and replays.

If writing `RESULT.md` fails, put the full report in the final message.
