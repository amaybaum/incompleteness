# Review of Q-868-H unit 1 (heralds on native two-wing U′ preparations)

**Model-written independent review (Claude Code subagent, 2026-11-09). Not human verification; a model review is not
verification under §A.46.7.** Authorizes nothing. No git or GitHub write was made.

- **Under review:** `q868h/Q868H-UNIT1.md`, sha256 `428cc283087657377fe0329a1e07b6f1b01b98e7a733df82e56e163bd3651d49`
  (hash verified before reading).
- **Authorization checked:** #868 c.6742050189 (amaybaum, 2026-11-09T14:07:16Z), read with `gh api`. Scope: paper
  analysis plus independent review; three outcomes reported separately; no outcome implies another without proof; no
  quantum states as inputs; no computation on an OI mechanism (exact generic checks allowed, per the unit's cited
  #1210/#1211 rulings).
- **Accepted input:** `reassess/868/ASSESS-868.md` r3a, sha256 `d97c4b6b…8e1b` (verified). Used for Q-868-H (§7),
  Lemma H (§4.1), w3, J2/J5/J7 (§4.2), §4.3.
- **Sources read at `fd539e15`** (`git show`, no `--depth`/`gc`/`prune`): QP `DESIGN.md` in full (sha256
  `11d89c04…32b9`); AP1 §3.1, §3.4–3.5, §4.1–4.7, §5.1 (`dd13bf29…ac0c`); Main §3.3 (:360-429) and :564 (`6144cd4a…6366`);
  M2D :50-72, :248-252, :280-284 (`9451b6ac…1353`); `CompositeDimension.lean` :877, :1049; `EqvK2MaxCone.lean`
  :140-230; `K2Guard.lean` :143; `EffectSpace.lean` :411.
- **Reviewer probes** (generic only; each self-contained, imports only `sympy`/`itertools`/`sys`, no earlier probe;
  `python3 -I`, sympy 1.14.0; all exit 0, 40 checks, 0 failures). None encodes an OI rule, U′ encoding, coupling,
  record law or preparation; every native fact below is derived by hand from QP's stated formulas.

  | file | sha256 | checks |
  | --- | --- | --- |
  | `rv_qc1.py` | `063bba2f…09a2` | 6: spectrum of `(I+XX+ZZ+tYY)/4`; PSD iff `t = −1`; `(XX)(ZZ) = −YY`; all 72 two-correlator tables at −1/4 |
  | `rv_qc2.py` | `64790f30…abcb` | 10: comparator H, S table actions vs QP's pullbacks; both QC-2 paths give Φ⁺; full CNOT sign table |
  | `rv_qc3.py` | `919f0337…1a37` | 6: partial transpose (independent reshape implementation) = Y-row flip on a generic table; Φ⁺ ↦ SWAP/2 |
  | `rv_qc4.py` | `aeab798e…c447` | 9: Mermin–Peres products and commutation; QM line parities on every joint eigenvector; formal F₂ line sums |
  | `rv_hh2.py` | `8b2fd6f6…f93a` | 3: `cnot(SWAP/2)` is −1/2 on a Pauli product; control |
  | `rv_scope.py` | `47722b3a…c9b3` | 6: Pauli-setting CHSH on Bell states; comparator herald for X-then-Z reads; ball/octahedron memberships |

  Outputs `rv_*.out` beside them. The unit's own probe (`1977dfb8…eb9`) was re-run: exit 0, output byte-identical to
  `q868h_generic_checks.out` (`cd38be73…f704`); its contents are Pauli/table facts only.

***

## Verdict: REVISE (narrow)

The three headline outcomes stand: **(V) PASS, (C) PASS conditional, QC FAIL**, each independently verified. Two
blockers are text-scope defects, not verdict changes: a universal QC-1 sentence is refuted by a hand construction
from QP's stated operations, which also closes stop S3; and the QC ⇏ (C) witness does not separate the two outcomes at
one level (§A.34). Both fixes are local.

## Blockers

- **B1 (QC-1 universal; S3 misidentified).** "With independent product parity supplies, every entangled-type native
  table is non-quantum" (§6.2 QC-1) is false under R-narrow, and S3 is decidable by hand: `pp` can be determined with
  carrier-only cross-wing couplings (§3 below). Scope the sentence to branches with `pp` undetermined at the coupling,
  close S3, drop the R-wide marks on E3/E4/QC-3/§6.3, and update owner question 2.
- **B2 (QC ⇏ (C) witness, §7).** In the P1-removed class the continuation that breaks (C) also breaks QC: its herald
  `(±1, 0, ±1)` is outside the Bloch ball, while the comparator for the same reads gives `±e_x` (`rv_scope` B5d–e). The
  witness separates only "PSD prepared table" from "(C) of its continuations". Restate the row at that level, or give a
  property-level witness and say it is not native (§4 below).

## Nits

- **N1.** §7 row (C) ⇒ (V): "(V) holds unconditionally here" contradicts §0. (V) rests on SA-1(a), P3, E-iso, WL and,
  for Y, NNB; say "without P1, P2, N2".
- **N2.** §0 and §6.0 attribute setting independence to AP1 C1. C1 is a one-wing derivation. Two-wing measurement
  independence is Main §3.3 hypothesis (iv), "retained as a posit … not derived" (Main:406-407), supplied here through P3's external
  controller. List P3 and (iv) among (V)'s premises.
- **N3.** C6 (§6.0, §9 row 2): "answered for U′ composites" should carry its conditions: (iv) via P3, Main's (ii)/(iii)
  via E-iso/WL, Pauli settings only (non-Pauli settings not supplied, S2). Also note the green is non-selective at
  stabilizer scope (Bell states with Pauli settings reach only |CHSH| = 2, `rv_scope` B5a). Pauli settings do separate
  non-stabilizer quantum states (B5b, eigenvalue 2√2).
- **N4.** §10 gives the QP DESIGN hash as `11d89c04…ac0c`; the file at `fd539e15` is `11d89c04…32b9`.
- **N5.** QC-4 compares joint two-wing reads, which the §6.1 map does not cover. Add the extension to §6.1: a joint
  read of `f_a^A + f_b^B` maps to a Lüders read of `σ_a ⊗ σ_b`.
- **N6.** §6.3 / §8 J2: "identical tables on every native product test" holds for **encoded Pauli** product tests,
  which is J2's "product-test tables". It fails for all native local reads. In E3's parity cells, both
  `z₂^A + z₂^B` and `x₂^A + x₂^B` are determined. Raw slot reads of the parity cells, which are native minimal reads (QP
  node 7, node 8 item 1), form a wing-local product test, and it distinguishes `pp = 0` from `pp = 1`. State the
  local test set explicitly. Whether some pair is indistinguishable under all native local reads is not shown.
- **N7.** §0 / §8 "`hH2` fails for the native table cone" has no displayed witness. One: SWAP/2 is native (E4 without
  `τ_Y`); `cnot(SWAP/2) = (I + X⊗I + I⊗Z − X⊗Z)/4` takes −1/2 on `(−x) ⊗ (−z)` (`rv_hh2`); every native table is
  Pauli-valid by (V); so `cnot(SWAP/2)` is not in the cone.
- **N8.** The "parity matches" condition (§0 J7, §6.2) is entry-dependent; state it. Inputs with XZ or YY support need
  `pp = 1`; inputs with XY or YZ support need `pp = 0`. The derivation is in §5.

***

## 1. Validity (V) — PASS confirmed

**What the proof uses.** In a product test the record pair is `(f_a^A(s), f_b^B(s))`, with `s` the pre-test
configuration. This needs three things:
- **Registration.** A read copies a slot (AP1 §4.1, SA-1(a)), and the Y read is the X read conjugated by `L`. QP
  `f_x∘L = f_y` and `f_y∘L = f_x` give `f_x∘L^{−1} = f_y`. `Na` and `C12` are involutions over F₂, so `L^{−1}` is
  available.
- **Kick locality.** Kicks stay on the reading wing (E-iso, WL).
- **Setting independence.**

The model is deterministic and local, with `s`, together with each wing's meter unknowns, as the hidden variable. Any
A-local event leaves B with a law over configurations, so its Bloch vector lies in the cube. This holds for raw,
ancilla and multi-record reads too, and for postselected or composed branches. The proof uses none of P1, P2, N2,
Lemma 3 or Lemma Q; I confirm that. It does use P3/(iv), which the §0 list omits (N2).

**AP1 C6.** C6 requires that "any two-wing SA-1 must be Bell-local (CHSH ≤ 2)". The (V) model is a screened local
completion in the sense of Main §3.3:
- (ii)/(iii) hold through E-iso and WL;
- (iv) holds through P3;
- the ⊥ branches are herald-independent of setting and carrier (AP1:679; unit F1);
- tier N (SA-1 proper, Z/X) is covered by §6.5.

So "answered", in the unit's own word, holds with those conditions named (N3). "Settles" would overreach on two
counts: the unit is unreviewed paper analysis, and C6 sits in a frozen record. The unit says "answered", not
"settles".

Consistency with Main: Main:564 and §3.3 say that the framework's adopted Bell branch needs ontic parameter dependence.
The stated U′ class has none (WL, E-iso), so its Bell-locality is what Main predicts for this class. §6.4's exclusion
of state-dependent rules covers H-Bell's preparation-indexed adjacency.

## 2. Closure (C) — PASS (conditional) confirmed

**Remote herald identity.** B's determined encoded functionals given A's records lie in `D ∩ B`:
- this set is isotropic (AP1 Lemma 3, which needs P1 and P2);
- `Q* ≡ 0` on it (QP Lemma Q(iii), which needs A4, `q = 2`, P1 and P2);
- on B's triple, `Q*(f_a + f_b) = 0 + 0 + ω = 1` and `Q*(p_B) = 1`.

So the determined set is `{0}` or `{0, f_a}`. Under N2 every other functional of the triple is exactly uniform, so the
Bloch vector is in `{0, ±e_a}`. Mixtures land in the octahedron.

**Dictionary.** The law of the 3-bit triple is fixed by the expectations of its seven nonzero functionals. The four
with `Q* = 1` (the `f_a + f_b` and `p`) are 0 in every branch, so the law is fixed by the Bloch vector. Encoded
continuations are pullbacks of encoded functionals plus constants (QP:569-575, 611-615), so the dictionary is sound
relative to the encoded subtheory. Lemma T and the claim "every maximal `D_E` has dimension 3 and contains `pp`" were
re-derived:
- `pp` is singular and in the radical;
- a totally singular `U` meets the radical inside `{0, pp}`;
- `U`'s image in the 4-dimensional nondegenerate quotient has dimension at most 2.

**Countercontrols.** All three were re-derived by hand.
- *P1 removed.* AP1 C9's route reads the registered meter's `w`. A then knows `f_x^A(s)` and `f_z^A(s)`, and B gets
  `(±1, 0, ±1)` because `p_B = pp + p_A` stays uniform. That point is outside the octahedron and the ball and inside
  the cube (`rv_scope` B5e).
- *SA-1(c) removed.* The same herald (AP1 C4).
- *N2 removed.* The bias gives `(±1, 0, ±|1−2p|)`, as in AP1's ledger row at :824.

(V) survives each removal: (V) does not use P1, P2 or N2. The scope statements in §5.3 are accurate:
- QP node 8: under raw parity-cell reads the octahedron point is not a complete description;
- every posit except A4 is supplied, not derived;
- single-wing closure is not two-wing completeness.

## 3. B1 in full: `pp` is determinable under R-narrow (S3 closes)

Only operations the unit lists in §2.3 are used; everything is derived by hand from QP's stated formulas.
1. Supply carriers ready with `z₁^A = 0` and `x₁^B = 0` known (P2). Apply the cross-wing graded carrier–carrier
   transvection `z₁^A += z₁^B`, `x₁^B += x₁^A`. This is R-narrow; it is the unit's own E4 carrier step. It gives
   `z₁^A + z₁^B = 0` and `x₁^A + x₁^B = 0`.
2. On each wing, apply QP's graded cell swap `W = C12∘C21∘C12` (QP node 8; mediator, graded, no NNB, wing-local). The
   z-chain is `(z₁, z₂) → (z₁, z₁+z₂) → (z₂, z₁+z₂) → (z₂, z₁)`, and the x-chain likewise, so `W` swaps the cells.
3. The parity cells now carry the correlation, so `pp = (z₂^A + z₂^B) + (x₂^A + x₂^B) = 0` is determined. This is
   allowed by Lemma Q (`Q*(pp) = 0`) and by WL (the parity cells stay wing-local). The new carriers are the former
   independent parity supplies, for example `Z₊Z₊`.
4. `H_A; CNOT` then gives `⟨YY⟩ = (−1)^{f_x^A + f_z^B + pp_after} = (−1)^{0+0+1} = −1`. This is the Φ⁺ table, which is
   quantum.

So, from independent product supplies under R-narrow, a native protocol reaches a quantum entangled table. That
refutes QC-1's universal sentence as written. Applying `τ_Y` instead gives SWAP/2 under R-narrow.

Consequences:
- QC-1's verdict-bearing content (E2, −1/4; every type-2 table at −1/4, `rv_qc1` Q1f) stands once scoped;
- QC-2 already covers every `pp` status, so the QC FAIL verdict is unaffected;
- the R-wide marks on E3, E4, QC-3 and §6.3 are unnecessary;
- owner question 2 does not bear on any witness.

## 4. B2 in full: QC ⇏ (C)

The (C) failure in the unit's witness sits at the herald after P1-removed continuations. At that level QC also fails:
- `(1, 0, 1)` corresponds to no qubit state, since `(I + X + Z)/2` has eigenvalue `(1 − √2)/2`;
- the comparator's herald for "A reads X, then Z" on Φ⁺ is `±e_x` (`rv_scope` B5d–e).

The P1-removed class also contains E2, so class-level QC fails there too.

What is shown is: *a PSD prepared table does not imply (C) for its continuations.* No native class has QC at class
level, so no native witness of class-level QC ⇏ (C) exists. A property-level witness is the comparator itself. The
product state `|0⟩ ⊗ (cos(π/8)|0⟩ + sin(π/8)|1⟩)` is quantum, and its B point `(1/√2, 0, 1/√2)` is outside the
octahedron (`rv_scope` B5f). It is not a native preparation, and it is used only as a logical witness, not as an input
to the construction.

The other five rows were checked one direction at a time, each at class level:
- **(C) ⇒ (V):** holds. A herald in the octahedron cone gives nonnegative `P(α)(1 ± r_b)/2` and lies in the cube cone
  (ASSESS r3 W2).
- **(V) ⇏ (C):** the P1-removed class keeps (V) and fails (C). Correct.
- **(V) ⇏ QC** and **(C) ⇏ QC:** E2 in the stated class (NNB for `H`). Correct.
- **QC ⇒ (V):** PSD ⇒ block-positive (L). Correct.

## 5. Quantum compatibility — each item re-derived

Native sides were derived by hand from QP's formulas; comparator sides were checked with generic probes. In every
item the native preparation follows from QP's stated operations. No quantum state is supplied.

- **QC-1.** E2 is QP node 10:
  - preparation: `Z₊Z₊` from P2 carriers with `z = 0` known; `H_A` via QP's `R` word plus `z₂ += 1` (NNB); the graded
    coupling (P3);
  - pullbacks: XX pulls back to `f_x^A` (0 after `H`), ZZ to `f_z^B` (0), and YY to `XX + ZZ + pp`, with `pp` uniform
    from independent supplies;
  - zeros: N2 makes every functional outside `D_E` exactly uniform; Lemma T, via Lemma 3 and Lemma Q, bounds the
    types.

  The resulting table is `(I + XX + ZZ)/4`, with minimum eigenvalue −1/4 (`rv_qc1` Q1b). PSD forces `⟨YY⟩ = −1`
  (Q1a, Q1c–e).
- **QC-2.**
  - *Path 1, `H_A; CNOT`.* `p_A` flips. The coupling pulls YY back to `f_x^A + f_z^B + pp` (hand: `f_y^A + f_x^B +
    f_y^B + f_z^A = (f_x^A + p_A) + (f_z^B + p_B)`), so `⟨YY⟩ = (−1)^{π+1}`.
  - *Path 2, `S_A; H_A; CNOT`.* `p∘(H∘S) = p`, so `⟨YY⟩ = (−1)^π`.
  - *Comparator.* QP's pullbacks of `S` and `H` agree with the comparator's table actions (`rv_qc2` C2a–b), and both
    paths give Φ⁺ (C2c–e).
  - *Any parity supply.* This includes branch mixtures: path 1 gives `⟨YY⟩ = u` and path 2 gives `−u`, and with
    `XX = ZZ = 1` PSD needs `⟨YY⟩ = −1`, so both cannot be quantum (C2i–j).
  - *Premise I.* Only whole `S` and `H`, known-0 supplies and the even graded coupling are used, and a determined `π`
    is reachable with graded couplings alone (§3). So the claim survives premise I.
  - *Label.* ELABORATING is defensible and conservative: product-table failure for correlated parities is not stated
    in QP node 10, which fails that case only through joint reads.
- **QC-3.**
  - *Native side.* `z₂^A += 1` flips `f_y^A` and `p_A` only (QP:728-731).
  - *Comparator.* Partial transpose on A is exactly the Y-row negation on a fully generic table (`rv_qc3` T3b, with a
    wing-B control), and it maps Φ⁺ to SWAP/2 with eigenvalue −1/2 (T3d–e). Φ⁺ is native (E4 + `τ_Y`, or §3).
- **QC-4.**
  - *Native side.* By hand, `ω(f_x^A + f_z^B, f_z^A + f_x^B) = 1 + 1 = 0`, and similarly for the other pairs; `pp` lies
    in the radical on `E₂`.
  - *Comparator.* The line sums equal `p_A + p_B` (formal F₂ identity, `rv_qc4` M4g–i). In QM the row bits sum to 0 and
    the column bits to 1 on every joint eigenvector (M4e–f). Hence `P(row ok) + P(column ok) = 1`.
  - Needs N5.

**Two further findings.**
- *Not locally tomographic.* `Z₊Z₊` with `pp = 0` and with `pp = 1` have identical **encoded** product tables, since
  no product-form functional involves `pp`. They differ under the native continuation `H_A; CNOT; (Y, Y)`. Correct for
  encoded tests (J2's sense); scope the wording (N6).
- *Coupling = table `cnot` only when the parity matches.* Correct, and the matching value depends on the entry. Native
  pullbacks:
  - XZ ↦ YY + `pp`, YY ↦ XZ + `pp`, XY ↦ YZ + `pp`, YZ ↦ XY + `pp`;
  - the others carry no `pp`.

  The quantum signs are −, −, +, + (`rv_qc2` C2g–h). The conflicting supports are XZ/YZ, XZ/XY, YY/XY and YY/YZ, and
  each pair sums to a `Q* = 1` functional, so they never co-occur in a branch. "Matching" is therefore consistent per
  branch. No single preparation-time value of `pp` works for all inputs, which agrees with QC-2 (N8).

## 6. Stops

- **S1:** correct. Under graded couplings a record is single-sector (Lemma G1), even with feedforward, which only
  adds constants per branch. `f_y` mixes sectors. Adaptive native `S` is open, not excluded, in QP §4.3, and S1 says
  "not supplied", which is accurate.
- **S2:** correct (J6).
- **S3:** misidentified; it closes by §3 (B1).

## 7. Method, scope and register

- **Authorization.** Hand enumeration of native preparations is paper analysis, as authorized. Neither probe, the
  unit's or this review's, encodes an OI rule, encoding, coupling or preparation, so both stay within "exact generic
  checks only".
- **Columns.** The three-column separation is kept, and column (iii) is never used to support column (ii).
- **Register.** All-caps tokens are identifiers or status labels only. There is no self-narration or reader
  instruction.
- **§A.31 labels.** Proportionate; no NEW is claimed.
- **Negatives.** These are scoped to U′, linear N with NNB, `q = 2` and the stated posits (§6.4), apart from B1's
  sentence.
- **Implications.** No outcome is inferred from another, apart from B2's level mix.

## 8. Required for ACCEPT

Apply B1 and B2. Applying N1–N8 is recommended. No verdict changes, no new computation and no new premise are needed.
