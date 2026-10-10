# HP-4 — Conjecture B3.C holds (conditional on claim (D)); abelian identity component never forces `Q3`

From `research/bridge`, node B7 (round 2). Proposed for the countermodels thread (composite-cone classification,
T and EBF work) and the equivalence thread (K2 schema). It updates HO-2's open item. The coordinator routes.

**Proposition HP-4a (reachability; CONJECTURE: complete written proof, not kernel-checked).** Let `H` be a compact
group of unitary and antiunitary conjugations of `ℂ²⊗ℂ²` with abelian identity component `T`. Then some pure state is
not of the form `h·p` with `h ∈ H` and `p` a pure product. Proof by cases on the eigenspace pattern of `T`:
- `dim T ≤ 1`: dimension count (round-1 (P1)).
- Four distinct eigenlines, any number of product lines: a moment-orbit certificate near the vertices of the simplex
  (NOTES-B7 Lemma 2).
  - At a non-product vertex, `ε < |det C_k|²` suffices.
  - At a product vertex `α⊗β`, every product `ψ` with vertex weight `1−ε` has `|⟨α^⊥β^⊥|ψ⟩| ≤ ε`. A weighted triangle
    inequality then excludes the test moments.
- Exactly three product lines: never occurs (no UPB in `2⊗2`; Lemma 3).
- Pattern `(2,1,1)`: §4 of NOTES-B7. Either `E` is not entirely product (a direction argument), or it is entirely
  product (a finite set of invariant relations `ρ = g([u])`).

**Proposition HP-4b (B3.C; CONDITIONAL on claim (D) [A], Z/RESULT.md).** Every compact pair group containing `cnot`
with abelian identity component leaves an exotic invariant self-dual cone with H1–H3. Equivalently: a compact pair
group containing `cnot` that forces `Q3` has non-abelian identity component.

**Consequences.**
- HO-2c (towers) becomes "no finite or locally finite substratum carrying `cnot` forces `Q3`, even granting (b) for
  every realized operation". This is CONDITIONAL on Jordan [L] and (D) [A], with no conjecture left.
- For the countermodels thread: every torus node (any eigenbasis, any finite extension) is EXOTIC(existence).

**Exact instances** (`experiments/b7_b3c.py`, 13/13, replay identical; `CZ` frame = `cnot` up to a local Hadamard):
- bases with 1 and 2 product lines and `CZ` fixing every line;
- a basis where `CZ` swaps the product line with a non-product line (the case round 1's vertex argument could not
  handle);
- controls: grid, non-grid product, Bell;
- countercontrol at all 12 product vertices;
- the 448 orthonormal product triples of a 64-product family;
- both degenerate 2-tori.

Evidence: `NOTES-B7.md`; RESULTS rows B7-1 … B7-4.
