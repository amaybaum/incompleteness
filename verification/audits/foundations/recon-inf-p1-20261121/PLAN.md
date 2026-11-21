# RECON-INF Phase 1: plan

**Status.** Plan, committed before the audit. This is a read-only dependency audit. It edits no
manuscript and does not change #1477, its frozen plan P* or Theorem 23. It adds no new proof and runs
no computation. Accountable Issue: #1531. Thread: #1169.

**Authorization.** Owner decision on #1169,
[comment 7067918791](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7067918791)
(`amaybaum`, 2026-11-21T19:17:59Z): "RECON-INF Phase 1 is authorized as a read-only dependency audit
of Theorem 23, running in parallel with the A1 retirement. [...] Only the audit is authorized; the
mathematical generalization stays deferred."

## 1. Question

Where do Theorem 23 (`papers/Substratum.md` §3) and its dependency chain use finiteness? For each
use, which condition does the step need?

## 2. Baselines

- **B1.** `main` at `df6da1c6101e811acdc7952d5748aff57028e8ed`.
- **B2.** T0, commit `5b6d48b58f45d3032bc33560aa5047c4b400f35a` on `trial/a1exit-T0-55544cc3`. T0 is
  the predicted tree after retirement plan P* (`55544cc3`,
  `verification/audits/foundations/a1exit-deletion-20261121/edits.json` on
  `research/a1exit-deletion-20261121`). It is read only, through `git show`.

P* is authoritative for the intended edits. The audit does not assume that they have landed. Every
B2 reference is checked against the T0 blob, and every ledger edit cited is checked against
`edits.json`.

## 3. Classification categories (owner requirement 2)

Each use of finiteness is classified into one or more of these:

| Code | Category |
|---|---|
| TC | The total configuration space is finite. |
| FL | The lattice is finite (a finite periodic quotient). |
| FR | The observable region is finite: a finite visible alphabet, finite windows, horizons, readout or setting regions, or a finite boundary layer. |
| NL | A normalizable law is enough: a probability law, possibly a specified one, on a carrier of any cardinality. |
| NN | Finiteness is not needed. |

Where a result needs several conditions, the audit records all of them. It also records any other
named hypothesis the step needs on an infinite carrier (for example H-μ, H-cont, H-Bloch, (NR)).
**Reference frame:** the owner's suggested setting `S = A^{ℤ³}`, with `A` finite and a reversible
finite-range cellular automaton. It is used only to name the infinite case. It is not assumed to
support any result.

## 4. Status categories (owner requirement 5)

- **(P)** An infinite-system result that is already proved: cited with its proof layer (Lean, paper
  proof on `main` with review, or standard mathematics).
- **(C)** A conditional candidate: a replacement proved only under named hypotheses that are not
  established, or a record that is still under review.
- **(O)** An extension that is genuinely open.

Local results are not promoted to an infinite-lattice reconstruction.

## 5. Method

1. Enumerate the chain from B1 `Sub:66–195` and its "Critical dependencies" list (`Sub:106–117`).
2. Read each cited result in Main, SM, GR and Structure, and the Lean declarations they cite, in both
   baselines.
3. Integrate the reviewed records already on `main` that classify these steps (§A.19): O-A4, the
   A1-REMAINDER consumer table, P7-B, NR-1, R1-INF, the A1-EXIT ledger, Q1 and R6. Do not repeat
   their work; cite it at the scope those records state.
4. For each use, give exact `file:line` in both baselines, the category codes and the status.
5. Keep three properties apart (owner requirement 3), each with its own row:
   - almost-everywhere recurrence on ℤ³;
   - periodic bounded orbits under NU9;
   - global exact return.

   No implication between them is asserted without a cited proof.
6. Stage 3 (owner requirement 4): locate each place where finite counting is essential and each place
   where a normalized law might suffice. Do not assume that a replacement exists.
7. Answer the review questions that P* routes to scientific review:
   - D022: does Stage 2 need the finite periodic case?
   - D026: is finiteness used anywhere other than Stage 1's exact return and Stage 3's count?

## 6. Productivity test (fixed before the audit)

The audit is **productive** iff it does at least one of the following, with exact references in
both baselines:
- (a) it finds a use of finiteness in the chain that P* D026 does not list, in any category other
  than NN;
- (b) it shows that a use P* attributes to the finite scope is in fact category NL, FR or NN, with a
  proved infinite-system result on `main`.

It is **non-productive** if it only restates the ledger's rows. The outcome is **INCONCLUSIVE** if
the references cannot be fixed in one baseline, or if a classification depends on a record whose
review is still open. The outcome is reported as found.

## 7. Controls

- K1: `git diff --stat origin/main` lists only files in this directory.
- K2: every `file:line` cited is re-read in its baseline before the record is committed.
- K3: no row assigns a status stronger than its cited source's status.

## 8. Boundaries

- No manuscript, Lean, registry or #1477 file is changed.
- No new proof: where combining two cited results would give a new statement, the audit names the
  combination as a candidate and does not assert it.
- No computation is run.
