# Independent proof review: the cone argument (ARP-2 / Q-C2-1)

**Verdict: PROVED UNDER STATED EXTRA HYPOTHESES.** The conclusion holds once the window is required to be invariant,
and the complete proof under that requirement is in §3. Two further hypotheses are also stated there.

- **The missing hypothesis is STAB:** `span O_K = span O_{K−1}`, the orbit span is invariant within the window.
- **As the design uses the argument, with no STAB, it is a GAP.**
- **The general implication is refuted:** a constant herald on the window plus CONS on the window does not imply that
  the window-fitted `β` has only roots of unity on the unit circle. Exact counterexamples (§4) show this at `K = 1` and
  `K = 2`, with VAL holding, and at `K = 3` without VAL. All are in the abstract class of nonnegative branch matrices
  the argument reasons about.
- **Not established:** whether the gadget's own rounds at `K = 6` or `K = 12` can exploit the gap. That would require
  evaluating C's decisive orbits, which this review does not do.

The design must stop relying unconditionally on the following, until the fix in §6 is adopted:
- "C's positives can only show orders 3 or 6";
- "C cannot instantiate ENC-G";
- remark R1's finite-order scope sentence;
- r6's "a rotation by `arccos(3/5)` is excluded on paper for this protocol class".

No decision token relies on the argument.

- **Reviewer.** An independent model reviewer that did not write the sketch. Paper argument plus exact probes. No C
  gadget orbit was evaluated, and no B fragment was built from OI data. Every branch matrix below is an abstract
  nonnegative matrix on U′'s 16 configurations, not a round of the frozen gadget.
- **Objects reviewed.**
  - `DESIGN-DS.md` r9 (`f4d1c078841f0381313a3a4ea436b47baad48ae3eef4c7f392c8cd91687bbd4b`), §6 "What can be found".
  - The sketch's long form in `r6/DESIGN-DS-r6.md` §6, which r7–r9 cite by name ("cone argument").
  - The uses in `preregistration.draft.md` r9a (`9692dc40…`): hazard 7 and the scope sentences.
  - The r10 table *Sketches under independent review*, in the r10 draft current during this review (`656d2202…`).
- **Owner instruction** (#1169 c.6735014875, amaybaum, 2026-11-09T07:52:50Z): "Each review should check the complete
  proof, assumptions, counterexamples, and whether the result depends on quantum structure that OI has not generated.
  A failed proof review should block reliance on that sketch, not automatically invalidate the rest of Q-C2-1."

***

## 1. The exact claim and its hypotheses as used

**r9 text.** "With a constant herald, unit-modulus eigenvalues are roots of unity (cone argument; Tam–Schneider, not
read first-hand). With rational reach their orders are 1, 2, 3, 4 or 6. A positive can only be of the R60 type
(`{1, e^{±iπ/3}}`) or the `S_3` type (`{−1, ω, ω²}`). C cannot instantiate OICORE-1's ENC-G."

**r6 long form.** "With a constant herald `q` on the span `V` of an orbit, the conditioned map `B|_V` preserves the
polyhedral cone `V ∩ ℝ₊ⁿ`. Its Perron vector lies in that cone, so its spectral radius equals `q`. Unit-modulus
eigenvalues of `B|_V / q` are then peripheral and, for polyhedral cones, roots of unity … With rational reach, a
rational 3×3 linear part has roots of unity of order 1, 2, 3, 4 or 6 only."

**The object it is applied to.** Decision rule C computes W-CL on `β`, where `Φ = (α, β)` is fixed by `R_op(πΛ_0)` and
`R_op(πΛ_{a,0})`. CONS(K) checks `Φ` only on the window `j < K` (prereg r6 *Quantities*, carried into r9a). HC(K)
checks herald constancy only on `O_{K−1}`. `K = 12` for C-EXPOSURE and `K = 6` for C-SIZE-DEPENDENT.

So the claim the design needs is:

> **(C★)** For a round `π` with nonnegative branch matrix `B` on the carrier laws, if HC(K) and CONS(K) hold, then
> every unit-modulus eigenvalue of the window-fitted `β` is a root of unity, of order in `{1, 2, 3, 4, 6}`.

## 2. Step-by-step check of the sketch

Write `A = B/q`, `N(μ) = (1ᵀμ, R(μ)) ∈ ℝ⁴`, `Ã = [[1, 0], [α, β]]`, and `W_j = span{π^iΛ : Λ ∈ Q, i < j}`.

| step (r6 text) | status |
| --- | --- |
| (a) `B|_V` preserves the polyhedral cone `V ∩ ℝ₊ⁿ` | Rigorous **when `V` is `B`-invariant**. The span of the full forward orbit is invariant, since `Bμ = q(μ) πμ`. But the design certifies herald constancy and CONS only on the window. See (d) |
| (b) "Its Perron vector lies in that cone, so its spectral radius equals `q`" | **Non sequitur, fillable.** A Perron vector gives `ρ ∈ spec`, not `ρ = q`. The correct reason: with a constant herald on `V`, `1ᵀB = q1ᵀ` on `V`. So `1ᵀB^nμ = qⁿ 1ᵀμ`, `B^n/qⁿ` is bounded on the cone, the cone spans `V`, and so `ρ ≤ q`. Also `q ∈ spec` because `1ᵀ|_V` is a left eigenvector. Hence `ρ = q` |
| (c) peripheral eigenvalues of a polyhedral-cone-preserving map are roots of unity (Tam–Schneider, not read) | **True in the power-bounded case needed here. Proved below without the citation** (Lemma Q.1), via the polytope `P = V ∩ Δ` and the Lemma P mechanism |
| (d) the link from `spec(B|_V/q)` to `spec(β)` | **Missing.** The sketch never states it. It holds when `N A = Ã N` on an `A`-invariant subspace that `N` maps onto ℝ⁴ (Lemma Q.2). CONS(K) gives `N A = Ã N` on `W_K`, which need not be `A`-invariant |
| (e) rational 3×3 `β` ⇒ orders `{1, 2, 3, 4, 6}` | Rigorous. A cyclotomic factor of a rational cubic has degree `φ(m) ≤ 3`, so `φ(m) ∈ {1, 2}`. A non-real unit pair `e^{±iθ}` forces the third root to equal `det β ∈ ℚ`, so the pair's quadratic is rational |
| (f) "a positive can only be R60 or S₃ type" | Rigorous, given (C★): exact enumeration of conjugation-closed root-of-unity multisets of size ≤ 3 (`probe_lemma_p.py` §1) |

## 3. Complete proof under the extra hypotheses

**Hypotheses.**
- **H1 (HC(K)).** `1ᵀBμ = q > 0` for every `μ ∈ O_{K−1}`.
- **H2 (CONS(K)).** `N(πμ) = Ã N(μ)` for every `μ ∈ O_{K−1}`.
- **H3 (STAB).** `span O_K = span O_{K−1}`, i.e. `W_{K+1} = W_K`.
- **H4.** `R(Q)` affinely spans ℝ³. The QA family gives `R(Q) = V₀`; this needs `Λ_{y,b}`.
- **H5 (rational reach).** `β ∈ ℚ^{3×3}`.

`B ≥ 0` entrywise is the native form of a branch matrix (REACHABLE §1.4).

**Lemma Q.1 (polytope lemma, any dimension).** Let `P` be a polytope with affine hull `H`, and `Φ: H → H` affine with
`Φ(P) ⊆ P`. Then the unit-modulus eigenvalues of the linear part of `Φ` are semisimple roots of unity.

*Proof.* Steps 1–7 of the Lemma P proof (`REVIEW-LEMMA-P.md` §2) use only that `P` is a polytope, bounded and
full-dimensional in `H`. Each step carries over verbatim:
- power-boundedness;
- semisimplicity;
- a fixed point by Cesàro averaging;
- the spectral projection and `Ψ`;
- `Φ` permuting the vertices of `Ψ(P)`;
- finite order on the peripheral subspace. ∎

**Lemma Q.2 (intertwining).** Let `W` be `A`-invariant, `N A = Ã N` on `W`, and `N(W) = ℝ⁴`. Then
`(λ − 1) χ_β(λ) = χ_Ã(λ)` divides `χ_{A|W}(λ)`.

*Proof.* `ker N ∩ W` is `A`-invariant: if `Nw = 0` then `NAw = ÃNw = 0`. `Ã` is the map that `A|_W` induces on
`W/(ker N ∩ W) ≅ ℝ⁴`. The characteristic polynomial of an induced quotient map divides that of the map. ∎

**Theorem (C★ under H1–H5).** Let `W = W_K`.
1. By H3, `A W ⊆ W`. Indeed `A π^{K−1}Λ = π^KΛ ∈ span O_K = W`, and `A = B/q` agrees with `π` on `O_{K−1}` by H1.
2. By H1, `1ᵀA = 1ᵀ` on `W`.
3. `P = W ∩ Δ` (`Δ` the probability simplex) is a polytope containing `O_{K−1}`, so it is full-dimensional in
   `H = W ∩ {1ᵀ = 1}`. `A ≥ 0` gives `A(P) ⊆ P`.
4. Lemma Q.1: the unit eigenvalues of `A|_{W ∩ ker 1ᵀ}` are roots of unity. `spec(A|_W) = {1} ∪ spec(A|_{W ∩ ker 1ᵀ})`,
   since `W ∩ ker 1ᵀ` is invariant and the quotient is 1-dimensional with eigenvalue 1.
5. By H2 and linearity, `N A = Ã N` on `W`. By H4, `N(W) ⊇ N(span Q) = ℝ⁴`.
6. Lemma Q.2: every eigenvalue of `β` is an eigenvalue of `A|_W`. So every unit eigenvalue of `β` is a root of unity.
7. By H5, the order is in `{1, 2, 3, 4, 6}`.
8. By §2(f), a W-CL positive is R60 type or S₃ type. ∎

**How restrictive H3 is.**
- `dim W_1 = 4`, computed exactly in probe §1: `Λ_{a,1} = 2Λ_0 − Λ_{a,0}`.
- The `W_j` grow strictly until they stabilize, inside ℝ¹⁶. So H3 holds automatically for `K ≥ 13`.
- At `K = 12`, H3 can fail only if `dim W_j = 3 + j` for every `j ≤ 13`, i.e. the span grows by exactly one dimension
  at each of the twelve steps. This is narrow, but not excluded.
- At `K = 6` (C-SIZE-DEPENDENT), H3 can fail broadly.
- H3 is computable exactly from `O_K`, which the checker already builds for VAL(K).

## 4. Counterexample to (C★) without H3 (exact; `probe_cone.py`, certificate `cone_k1_certificate.json`)

**Construction (abstract class, `K = 1`).**
- Columns `B δ_x = w(x) ℓ_x`, with `w(x) = 8qP(v(x))`. Here `v(x) = (χ_x, χ_y, χ_z)(x) ∈ {±1}³`, and `P` is a zero-mean
  law on the eight sign vectors.
- `ℓ_x` is the product law with `R(ℓ_x) = G(v)/P(v)`.
- `P` and `G` solve the one-step linear program for a prescribed `β`.
- `β = S D S⁻¹`, with `D = diag(rot(arccos 3/5), −1/4)` and `S` a fixed rational matrix with quarter entries.
- `q = 261/640`.

**Verified exactly.**
- `B ≥ 0`, with column sums ≤ 1.
- The herald equals `q` on all seven QA laws (HC(1)).
- CONS(1) holds on all seven, with `α = 0`.
- VAL(1) holds.
- `χ_β = (4λ + 1)(5λ² − 6λ + 5)/20`, which contains `λ² − (6/5)λ + 1`. Its roots are `e^{±i arccos(3/5)}`, which are
  not roots of unity.
- So W-CL fires with a non-root-of-unity pair, contradicting (C★) at `K = 1`.
- Consistently with §3: `dim W_1 = 4` and `dim W_2 = 8` (H3 fails), and the herald takes seven distinct values on
  `π(Q)` (HC(2) fails).
- The window simply does not see the branch matrix's dynamics on an invariant span.

**A two-step window (`K = 2`; certificate `cone_window_K2_certificate.json`, verified from `B` alone).**
- An explicit rational 16×16 `B` with every entry ≥ 0.0018 and column sums ≤ 1. `q = 502/577`.
- HC(2), CONS(2) on all seven QA laws and VAL(2) all hold.
- `χ_β = (32λ − 5)(5λ² − 6λ + 5)/160`, so W-CL fires with the same non-root-of-unity pair.
- `rank span O_1 = 8`, `rank span O_2 = 12`, so STAB(2) fails.
- The window can therefore be fooled over more than one composition.

**A three-step window (`K = 3`; certificate `cone_window_K3_certificate.json`).**
- An explicit rational `B` with every entry ≥ 0.0004 and column sums ≤ 1. `q = 126/187`.
- HC(3) and CONS(3) hold, and `χ_β ∋ 5λ² − 6λ + 5`, so the stated implication (C★) fails at `K = 3`.
- VAL(3) fails: some orbit image leaves the unit ball. So this is not a VAL-valid W-CL positive.
- The ranks are `12` and `16`. The span is full at `O_3`, so STAB holds automatically from `K = 4` on, and §3 then
  forbids extending this `B` to `K = 4`.

**What the certificates show about the mechanism.**
- A window counterexample needs the orbit span still to be growing at step `K`.
- Each extra step of window costs at least one dimension of the 16. Here the spans grow `4 → 8 → 12 → 16`.
- At `K = 12` the span would have to grow by exactly one dimension per step (§3).
- That is why `K = 12` is a narrow gap and `K = 6` a broad one. It is also consistent with the numerical search
  stalling at `K = 4` and `K = 6`, though it does not explain that stall rigorously.

**Why this is the right class.** The r6 sketch argues about any nonnegative branch matrix with a constant herald on
an orbit span ("the conditioned map `B|_V`"), not about the gadget specifically. The counterexample sits in that class.
It is not claimed to be realizable by any gadget round, and nothing here evaluates the gadget.

**Positive side results (exact certificates, paper).**
- **Orthogonal maps are confined at every window.** For any constant herald, rows `c_i` of a one-step `β` lie in the
  zonoid `{c : c·d ≤ E_{P_w}|d·v| ∀d}` of the herald-weighted law `P_w`. Then
  `Σ_i ‖c_i‖² ≤ E_{P_w}‖βv‖₁ ≤ √3 · E_{P_w}‖βv‖₂`. For orthogonal `β` both sides equal 3, which forces `βv ∈ {±1}³` on
  the support of `P_w`, and a rank argument then excludes rotations such as `rot_z(arccos 3/5)` and R60.
- **The probe certifies the simplest instance.** The z-rotation by `arccos(3/5)` needs `P_w(v_x ≠ v_y) ≥ 7/10` and
  `P_w(v_x = v_y) ≥ 7/10` at once.
- **What the counterexample can and cannot be.** It must use a non-orthogonal `β`. For the rotation itself, a herald
  of 1 is already impossible by the zonoid bound with `P_w` uniform.
- **These do not repair (C★).** W-CL is spectral and accepts non-orthogonal `β`.

**Numerical exploration (floating point, not evidence).** `explore_cone_numeric.py` minimizes the HC(K), CONS(K) and
target-factor residuals over nonnegative `B`, with a 150 s budget per `K`:
- `K = 1, 2, 3`: residuals `1.5e−13`, `4.7e−13` and `8.3e−13`.
- With an entry floor, which gives the positivity margin needed for exact reconstruction, `K = 2` and `K = 3` reach
  `1.7e−13` and `1.9e−13`. Those two solutions were exactified as above.
- `K = 4` and `K = 6`: residuals `2.7e−7` and `2.9e−7`. This is inconclusive: it is neither a solution nor evidence of
  infeasibility.

The design's `K = 12` was not attempted. Nothing here bears on gadget rounds. The exploration neither supports nor
refutes (C★) at `K = 6` or `K = 12`. Those remain the GAP stated at the top.

## 5. Assumptions, typed; quantum structure

| assumption | type |
| --- | --- |
| `B ≥ 0` branch matrices from configuration counting under N2, with conditioning on registered values | B (N2 candidate strengthened; forward conditioning and P1 as typed in the ledger) |
| HC(K), CONS(K), and **H3/STAB** | measured on records and laws (H3 not currently computed) |
| H4: `Λ_{y,b} ∈ Q` | H-PREP (open hypothesis) plus NNB (supplied conditional premise) |
| H5: rational reach | N2 plus bounded protocols (B) |
| Tam–Schneider | an imported mathematical citation, not read first-hand. **Removed:** Lemma Q.1 replaces it |
| "R60 type / S₃ type / Clifford class" | imported comparator (the signed-permutation spectra), confined to the witness's definition |

**Quantum structure.** None. The argument is Perron–Frobenius and convex geometry on nonnegative matrices and bias
coordinates. No Hilbert space, Born weight, unitarity or Clifford/stabilizer formalism enters beyond the comparator
label.

## 6. §A.34 directionality, and what relies on the argument

**Direction.** The argument is a one-way implication: H1–H5 ⇒ positives are R60 or S₃ type. The design uses it only in
that direction, as an upper bound on what a positive can show. Nothing uses a converse, such as "R60 type is reachable".
The direction is right. The defect is the missing hypothesis H3, not a reversed implication.

| reliance | survives? |
| --- | --- |
| Hazard 7 (r9a), "C's positives can only show orders 3 or 6" | **Only with H3.** As written: no. |
| DESIGN-DS §6, "C cannot instantiate OICORE-1's ENC-G" | **Only with H3**, per instance |
| Remark R1, scope sentence ("a finite-order positive …") | R1's group theory is independent of the cone argument and holds. `⟨O, R60⟩` is infinite, and its closure is `SO(3)`, since no finite subgroup of `SO(3)` properly contains `O` and `O` fixes no axis. The scope sentence that a positive *is* of finite order needs H3 |
| r6's "a rotation by `arccos(3/5)` is excluded on paper for this protocol class" (r7–r9 carry it by reference) | **No.** It is refuted at `K = 1, 2` (VAL-valid) and `K = 3` in the abstract class (§4). For gadget rounds at `K = 6, 12` it is open unless H3 holds |
| Every C token, W-CL's computation, C-35 | **Unaffected.** W-CL factors the exact characteristic polynomial and fires on irrational pairs. C-35 tests exactly that, and no gate reads the cone argument |
| The arithmetic statement "every probability is rational; nothing bears on irrational or approximate gates" | **Unaffected** (H5 alone) |

**Fix: cheap, exact, no decisive evaluation before `F`.** Freeze a reported (non-gating) field
`STAB(K) = [rank span O_{K−1} = rank span O_K]` for every instance where W-CL is reported.
- Restate the hazard as: "for instances with `STAB(K)`, a W-CL positive can only be R60 or S₃ type (orders 3 or 6);
  without `STAB(K)` the spectrum is reported without that bound."
- Apply the same condition to the ENC-G sentence and to R1's scope sentence.
- Alternative: add a CONS/HC check at `K = 13`, where STAB holds automatically. This costs one more application per
  orbit.
- A control with teeth for the new field: this review's `K = 1, 2` certificates give `STAB = false`, with HC, CONS
  and VAL holding and W-CL firing on an irrational pair. The idle (zero-tick) round leaves the carrier law unchanged, so it
  gives `STAB = true`.

The r10 table *Sketches under independent review* already withholds exactly the right statements on failure. Under
this verdict, its "cone argument" row applies until the STAB field and the restated sentences are adopted. Once they
are adopted, the statements may be restored in their STAB-conditioned form.

## 7. Minor findings

- **CN-1.** §2(b): "Perron vector ⇒ `ρ = q`" is a non sequitur. Use the left eigenvector `1ᵀ` and power-boundedness.
- **CN-2.** The sketch cites Tam–Schneider without reading it. Lemma Q.1 makes the citation unnecessary, so drop it or
  keep it as context only.
- **CN-3.** "Orders 3 or 6" (hazard 7) describes the root-of-unity orders in a positive. The R60 type has elements of
  order 1 and 6; the S₃ type has orders 2 and 3. Say "a non-real pair of order 3 or 6".

## 8. Probes

All files are in `review/proofs/`.

| file | sha256 | content |
| --- | --- | --- |
| `probe_cone.py` | `ba4a9aba76f82cb7e4e2417f3c145d003512fe98f9a17cd348d735be65c33869` | Exact. (1) `dim span Q = 4`. (2) The `K = 1` certificate: HC(1), CONS(1), VAL(1), `χ_β ∋ λ² − (6/5)λ + 1`, `dim W_2 = 8`, HC(2) false. (2b) The explicit-`B` certificates for `K = 2, 3`, re-verified from `B` alone: `B ≥ 0`, column sums ≤ 1, HC(K), CONS(K), VAL(K), the factor, STAB(K) false. (3) A stabilized instance: `(λ − 1)χ_β` divides `χ_{A|W}`. (4) The herald-1 certificate. Run as `python3 probe_cone.py cone_k1_certificate.json` from this directory. Prints `ALL CONE PROBES GREEN`; output saved in `probe_cone.out` |
| `cone_k1_certificate.json` | `e67199472530e6753eed86e991636a4fadb930b2b9c56e0456ec6b884cfeb644` | `K = 1`: the exact rationals `q`, `β`, `P` and `G` |
| `cone_window_K2_certificate.json` | `f24a68d902a423018d15c4d92440970e5f17b202cc8b8ea3407ad11269e6ebaf` | `K = 2`: explicit rational `B` and `q` |
| `cone_window_K3_certificate.json` | `713ab65327d291f37059a7dd1560aceb89b86d7731b977106c0941a4405a6831` | `K = 3`: explicit rational `B` and `q` (VAL(3) false) |
| `gen_cone_cert.py` | `2ca85e404551e3fba23c2b41e30ddb6e3cbbf30ab45b28b11b344efa4a895655` | builds the `K = 1` certificate. A float LP finds the candidate, and an exact projection enforces the equalities |
| `gen_cone_window_cert.py` | `afe78ff08731344ca42603f05a33d7424db58d3d63c5f35ef6a42dd09b3311f1` | builds the `K = 2, 3` certificates from the floored float solutions, by exact rational least-norm projection. Run as `gen_cone_window_cert.py K floor-threshold json` |
| `search_k1_candidates.py`, `.json` | `a52f3a5a0b38fa007400128bf78fb6f3b8c7ef351225735934dcf42d492f10a6`, `7c6aae75e62ed2df69d3374f74019877bdea0a117034619373e23636f51ac0aa` | the float search that found the `K = 1` conjugator. Search only |
| `explore_cone_numeric.py` | `aa4647e442a2bdb3638ea09cdbed9c34edd691f6539bd9e47354a08f85f4f0d1` | the float exploration (§4). Not evidence |
| `explore_cone_numeric.json`, `explore_cone_numeric_floor_K2.json`, `explore_cone_numeric_floor_K3.json` | `542d1ebcd34c9e5f409c8066f3a314a0c88d0761b76a1814c60abccc6e6d0103`, `1ecc80a1ea5993b682d56b8ba068a20bdc00523e5aa2cebb9ae81384abcf7452`, `94d607cf11c1fea2bef6c03ce2757fb578834d96edfbbe0d075db0f3691bb2bd` | the float solutions that the generators start from |

Only `probe_cone.py`'s exact checks are relied on. Every float step is a search for a candidate, and the exact verifier
accepts or rejects that candidate independently.
