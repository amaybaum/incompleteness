# HO-10 (v1) — bridge → countermodels, equivalence: Conjecture B3.C holds conditional on claim (D); an abelian identity component never forces `Q3`

**From** `research/bridge` (round 2, node B7). **To** `research/countermodels` (composite-cone classification; nodes
C10 and the EBF work) and `research/equivalence` (the K2 schema). Updates HO-2's open item (HO-2 is not edited; this
is a new handoff). Written by the coordinator from the source thread's committed record; version 1, 2026-10-10.

## Statements and labels

1. **Reachability theorem** (B7-1). Let `H` be a compact group of unitary and antiunitary conjugations of `ℂ²⊗ℂ²`
   whose identity component is abelian. Then some pure state is not of the form `h·p`, `h ∈ H`, `p` a pure product.
   Cases: `dim H₀ ≤ 1` (round-1 (P1)); four distinct eigenlines with any number of product lines (a uniform
   moment-orbit certificate near the vertices of the simplex, Lemma 2 — at a non-product vertex `ε < |det C_k|²`
   suffices, at a product vertex a weighted triangle inequality excludes the test moments); exactly three product
   lines never occurs (no unextendible product basis in `2⊗n` [L], Lemma 3); the degenerate pattern `(2,1,1)` by a
   separate argument (NOTES-B7 §4). Label: CONJECTURE (complete written proof, not kernel-checked; no named premise
   beyond [L] in Lemma 3).
2. **B3.C** (B7-2). Every compact pair group containing `cnot` with abelian identity component leaves an exotic
   invariant self-dual cone with H1–H3. Equivalently: a compact pair group containing `cnot` that forces `Q3` has
   non-abelian identity component. Label: CONDITIONAL (on claim (D) of the audited stage-4 record [A], which rests on
   EBF [A]; the reachability step is item 1).
3. **Consequences** (B7-4). No fixed finite pair substratum and no directed tower of finite pair substrata realizing
   `cnot` forces `Q3`, even granting (b) for every realized operation at every stage. Label: CONDITIONAL (Jordan's
   theorem [L]; claim (D) [A]) — no conjecture left in HO-2c. For the countermodels thread: every torus node (any
   eigenbasis, any finite extension) is EXOTIC (existence).

**Exact instances** (`experiments/b7_b3c.py`, 13/13, replay identical; `CZ` frame = `cnot` up to a local Hadamard):
bases with 1 and 2 product lines and `CZ` fixing every line; a basis where `CZ` swaps the product line with a
non-product line; controls (grid, non-grid product, Bell); the countercontrol at all 12 product vertices; the 448
orthonormal product triples of a 64-product family; both degenerate 2-tori. Robustness run `b7b_generic.py`: the
certificate succeeds on 12 generated bases and the countercontrol fails at all 13 product vertices; its verdict is
B7B-FAILED Z1 because one generated basis had 2 product lines where 1 was designed (a generator defect, kept as is).

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `3686049e` (round-2 commits `e29b6a42` … `3686049e`) |
| proposal | `research/bridge/handoff-proposals/HP-4-B3C-proved.md`, sha256 `9a3063865ef96e4852f358ea0848fba850f3c4824976dfb81946c63123fa765f` |
| results | `research/bridge/RESULTS.md` sha256 `dc17220ca389c7c69198f3b85c9c52a7f96d4f15070389d2ba13013bc9725298` (rows B7-1 … B7-5); `NOTES-B7.md` `16ffbef99d5ff76d6e88168eabceb83b11b3035162e0b1e879f4218f5f402d68` |
| scripts, outputs | `experiments/b7_b3c.py` `810b51075d9faf9a886019a527e2493058894c5ec620053ade5c21ba0a68886e` / `.out` `f94bbbd1fb5ebda9ee9ada43befebe4fcb0bbf0d41a993a7916f323c917d79ba`; `b7b_generic.py` `6cf7f51a…` / `.out` `9e1cbe81…` |
| coordinator audit | `indep_checkB2.py` run 2 5/5 — X1 confirms Lemma 2's certificate on instance I1, Lemma 2(b) on explicit products and Lemma 3 on 180 orthonormal product triples; the written proof read (Lemma 2, Lemma 3, the `(2,1,1)` case) — `research/AUDITS/2026-10-10-round2/AUDIT-BRIDGE-R2.md` |

## What the receiving threads may assume

Items 1–3 at their labels. **Countermodels:** the residual region of C10.3 (simple-spectrum tori in which `G` carries
every entangled eigenline onto a product eigenline; degenerate 2-tori) is covered by item 2 at CONDITIONAL on (D),
through item 1 — existence only; explicit constructions there remain open (HO-16 is the cone-side companion).
**Equivalence:** item 2 is claim D's first half in the form "an abelian identity component never suffices", the
complement of the K2 schema's "a local `su(2)` with `cnot` forces `Q3`" (NOTES-E10; HO-13).

## What they may not assume

- that item 1 is kernel-checked, or that claim (D) is certified — (D) is an audited stage-4 record resting on EBF;
- that any specific exotic cone is exhibited for a given group (existence only, except where the countermodels
  thread has explicit cones);
- anything about groups with non-abelian identity component.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-10 v1` and records in its `LOG.md`
whether and how it relies on it.
