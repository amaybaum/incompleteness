# Q-868-H unit 1: dispositions of the r1 review findings (r1 → r2)

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** This is a change note, not a review. Nothing is
adopted. No git or GitHub write was made.

- **r1:** `r1/Q868H-UNIT1.md`, sha256 `428cc283087657377fe0329a1e07b6f1b01b98e7a733df82e56e163bd3651d49`. It is a
  byte copy of the reviewed file.
- **r2:** `Q868H-UNIT1.md`, sha256 `1e128f286b14be3294cb8411e21f0b4b4516cbc9985fc2589fb6362a752179e6`.
- **Review:** `review/REVIEW-Q868H-UNIT1.md`, sha256
  `bd82f3fc469348945a838183f052c28c527ee6f43e7fc91c4157abd1a8cfb520` (verified). Verdict REVISE (narrow); blockers
  B1–B2; nits N1–N8.
- **Authorization:** #868 c.6742050189. Paper analysis only, with exact generic checks; no computation on an OI
  mechanism.
- **Sources:** every source was re-read with `git show fd539e15:<path>`. No `--depth`, `gc` or `prune` was used. The
  copies in `src/` are byte-identical to the extracts.
- **New probe:** `probes/r2_generic_checks.py` (`ad8285ec…5b29a`), output `probes/r2_generic_checks.out`
  (`b0f9950a…dbcda8`). It has 20 checks, 0 failures and exits 0. It imports only `sympy`, `itertools` and `sys`, and no
  earlier probe. It encodes no OI rule, encoding, coupling, cell swap or preparation.
  - Run 1 failed R1b and R2a: an eigenvalue helper dropped multiplicities. The helper was fixed, and no expectation
    changed.
  - Run 2 passed 19 of 19 checks.
  - R1d was added for run 3.
  - All three outputs are kept beside the probe.
  - The r1 probe was re-run, and its output is byte-identical to `q868h_generic_checks.out`.

Each finding was verified by hand and against the sources before it was applied. The verdicts are unchanged:
**(V) PASS, (C) PASS conditional, QC FAIL.**

***

## Blockers

### B1. QC-1's universal sentence is false, and S3 is not a stop. **Accepted.**

**Verification (by hand, from QP's stated operations at `fd539e15`):**
1. *Cross-wing carrier step.* Ready carriers with `z₁^A = 0` and `x₁^B = 0` known undergo the graded transvection
   `z₁^A += z₁^B`, `x₁^B += x₁^A`. This leaves `z₁^A + z₁^B = 0` and `x₁^A + x₁^B = 0` determined. It is r1's own E4
   carrier step, and it is R-narrow.
2. *QP's cell swap.* QP:612 defines the cell swap `W = C12 ∘ C21 ∘ C12`. QP:562-563 gives `C12` as `z₂ += z₁`,
   `x₁ += x₂`, through a mediator, and `C21` exchanges the roles of the two cells. The chains are
   `(z₁, z₂) → (z₁, z₁+z₂) → (z₂, z₁+z₂) → (z₂, z₁)` and `(x₁, x₂) → (x₁+x₂, x₂) → (x₁+x₂, x₁) → (x₂, x₁)`. `W` is
   graded, wing-local (its mediator is local under WL) and needs no NNB.
3. *Parity determined.* After `W` on each wing, `z₂^A + z₂^B = 0` and `x₂^A + x₂^B = 0`, so `pp = 0` is determined.
   `Q*(pp) = 0` (Lemma Q permits it), and the parity cells stay wing-local.
4. *The Φ⁺ table.* With parity supplies `z₂ = 0` known on both wings, the new carriers are `Z₊Z₊`. `H_A` flips `p_A`
   (QP:615), giving `pp = 1`, with `f_x^A = 0`.
   - The coupling's pullbacks (§2.1) give
     `YY ↦ f_y^A + f_x^B + f_y^B + f_z^A = (f_x^A + p_A) + (f_z^B + p_B) = f_x^A + f_z^B + pp`, with value 1, so
     `⟨YY⟩ = −1`.
   - `XX ↦ f_x^A`, with value 0, and `ZZ ↦ f_z^B`, with value 0.
   - The table is `(I + XX − YY + ZZ)/4`, the Φ⁺ table. It is PSD (r2 R1a–b), and the comparator's
     `CNOT (H ⊗ I)|00⟩` gives the same table.
5. *Premise I.* Steps 1–3 use known-0 supplies and graded couplings only, and step 4 uses the whole `H`. So the
   construction also survives premise I.

So independent product supplies under R-narrow reach a quantum entangled table, and r1's sentence is refuted.

**Changes in r2:**
- **§2.3.** New **Lemma P** (relative parity under R-narrow), carrying steps 1–3 and the chains above. The sentence
  "Every verdict below holds under both. Where a witness needs R-wide, it is marked." is replaced by "Every verdict and
  every witness below holds under R-narrow, through Lemma P."
- **§6.2 QC-1.** The scope is now "branches with `pp` undetermined at the coupling". The false universal sentence is
  replaced by two statements:
  - On such a branch, two determined correlators make the table type 2, since type 3 needs `pp ∈ D_E` (Lemma T). The
    table is then non-quantum.
  - Independent product supplies do not confine a protocol to such branches: Lemma P, then `H_A; CNOT`, gives the
    quantum Φ⁺ table (E3).
- **§0 QC.** The QC-1 bullet is re-scoped in the same way, with "type 2, with eigenvalue −1/4".
  - New sentences state that Φ⁺ is natively reachable on some branches (Lemma P with `H_A; CNOT`, i.e. E3; and E4
    with `τ_Y`). They also state that the verdict rests on QC-2, which holds for every status of `pp` at the coupling.
  - One precision is added (see "Additions" below): under the stated access, E2 and E4 without `τ_Y` (SWAP/2) are
    also native non-quantum tables.
- **R-wide marks dropped:**
  - E1 (D_E column: "+ `pp` only if built by Lemma P");
  - E3 (rebuilt from Lemma P's `Z₊Z₊`, R-narrow);
  - E4 (Lemma P with parity supplies `z₂^A = 0`, `x₂^B = 0`; R-narrow, tier N);
  - QC-3 ("R-narrow, E4 through Lemma P");
  - §6.3 (the pair is now Lemma P, and Lemma P followed by `τ_Y`);
  - §8 J7 ("With `pp` determined (Lemma P, R-narrow)").
- **S3 is closed** in §0 Stops and in §11: "`pp` is determined by a carrier–carrier coupling followed by QP's wing-local
  cell swap on each wing (Lemma P)".
- **Owner question 2** is updated: no outcome and no witness depends on the reading, since R-narrow reaches every
  witness through Lemma P. The answer fixes only the access wording.
- **§9** gains a row for Lemma P: ELABORATING (QP node 8's `W`; node 7's relative parity).
- **§9 gate row:** "Φ⁺ and SWAP/2 tables both reachable under R-narrow by graded couplings, the wing-local cell swap
  and translations".

**Re-grep.** "R-wide" survives only in its definition (§2.3) and in owner question 2. "S3 (partial)", "entangled-type"
and "R-wide for E4" have zero hits.

### B2. The QC ⇏ (C) witness mixes levels. **Accepted.**

**Verification:**
- r1's witness (E4 with `τ_Y`, then a P1-removed continuation) shows only that a PSD prepared table does not imply (C)
  for its continuations.
- At the herald that breaks (C), QC also fails.
  - `(±1, 0, ±1)` is outside the Bloch ball: `(I + X + Z)/2` has eigenvalue `(1 − √2)/2` (r2 R3a).
  - The comparator's herald for the same reads on Φ⁺ (A reads X, then Z) is `±e_x` (R3b).
- So the row did not separate QC from (C) at one level.
- The property-level witness `|0⟩ ⊗ (cos(π/8)|0⟩ + sin(π/8)|1⟩)` has been checked:
  - it is rank-1 and PSD with trace 1;
  - B's Bloch vector is `(1/√2, 0, 1/√2)`, which has L1 norm `√2 > 1`, so it lies outside the octahedron;
  - every A Pauli outcome of positive probability leaves B there;
  - control: `(1/2, 0, 1/2)` lies inside the octahedron (R2a–e).

**Changes in r2:**
- **§7, the QC ⇒ (C) row** is now "**fails** (property level)", with the non-native product-state witness. In the
  table cell, `\|` is escaped so the Markdown table renders.
- **§7, new note** "*The QC ⇏ (C) witness.*" It states four things:
  - the witness is logical only, not an input;
  - no native witness exists among the classes considered here;
  - QC also fails at the P1-removed herald (R3a–b);
  - r1's native statement holds at its own level: a PSD prepared table does not imply (C) for its continuations.
- **§0 Directions** carry the same property-level witness and its non-native status.

**Precision beyond the review (made, not refused).** The review's §4 says "the P1-removed class also contains E2". That
holds. For the class-level sentence over *all* §5.4 countercontrols, r2 uses E4 without `τ_Y` instead of E2. With N2
removed, biased unknowns can make E2's undetermined entries nonzero. E4's determined entries `XX = YY = ZZ = +1` do
not depend on N2. No quantum state has them, whatever its other entries, because `SWAP = (II + XX + YY + ZZ)/2` has
eigenvalues ±1, so `⟨XX⟩ + ⟨YY⟩ + ⟨ZZ⟩ ≤ 1` (new check R1d). The review's "no native class has QC" is stated in r2 as
"no native witness exists among the classes considered here". r2 does not quantify over every native class.

***

## Nits

### N1. "(V) holds unconditionally" contradicts §0. **Accepted.**

r1 §0 lists (V)'s premises, so "unconditionally" was wrong. In r2, §7 row (C) ⇒ (V) reads "(V) holds here without
P1, P2 or N2 (§6.0)".

### N2. Setting independence is Main §3.3 (iv), not AP1 C1. **Accepted.**

**Verification:**
- AP1 C1 is the one-wing condition: supply, carrier source and heralds independent of `(s, s′)` (AP1:674; the
  earlier gate C1 is at AP1:436).
- Main §3.3 states (iv), "the interventions act on one common pre-setting ensemble, so `p(Ω | a, b) = p(Ω)`", and
  Main:406-407 says: "Measurement independence is retained as a posit about the initial condition, not derived".

**Changes in r2:**
- **§0 (V)** names two-wing setting independence as Main §3.3 (iv), a posit there (Main:406-407), supplied through
  P3's external controller. It lists (V)'s premises as SA-1(a), P3 with (iv), E-iso and WL, and NNB for the Y read.
- **§6.0** carries the same attribution, with "AP1 C1 is its one-wing counterpart".
- **§2.4** gains a row: "(iv) two-wing measurement independence", with column (ii) **no** (a posit, supplied through
  P3).
- **§11 owner question 3** states (V) with these premises.
- **§10** now lists Main §3.3 (:360-412) as read.

### N3. C6 "answered" needs its conditions; the green is non-selective at stabilizer scope. **Accepted, and extended.**

**Changes in r2.** §6.0 says "answered for U′ composites under these conditions". The conditions are:
- (iv) through P3;
- Main's (ii) and (iii) through E-iso and WL;
- `⊥` heralds independent of setting and carrier (AP1:679; F1);
- Pauli settings only (S2).

§6.0 then adds:
- At stabilizer scope this answer does not discriminate: every two-qubit stabilizer state with Pauli settings has
  `|CHSH| ≤ 2`.
- A hand argument backs this: with distinct settings, correlators sharing a setting anticommute, so at most two are ±1;
  with equal settings, CHSH is twice one correlator.
- Pauli settings do separate non-stabilizer quantum states: `XX + XZ + ZX − ZZ` has eigenvalue `2√2`.

§9 row 2 carries the conditions and "non-selective at stabilizer scope". "Settles" is not used.

**Extension.** The review checked the four Bell states. r2 R4a–b checks all 60 two-qubit stabilizer states, generated
by the generic Clifford action on `|00⟩`, over all Pauli setting choices: the maximum `|CHSH|` is 2. R4c checks the
`2√2` operator.

### N4. QP's hash. **Accepted.**

Verified: `git show fd539e15:…/quarter-phase-native-20261107/DESIGN.md | sha256sum` gives
`11d89c04d6c1edcd0ec811822a10decc2133cc615936f22103b166d13dce32b9`. In r2, §10 reads `11d89c04…32b9`. r1's `…ac0c` was
AP1's tail. The other six source hashes were re-verified and match r1's truncations.

### N5. QC-4 is outside the §6.1 map. **Accepted.**

§6.1 gains a bullet, **Joint reads**: a native joint read of `g = f_a^A + f_b^B` (along `J g`) maps to the Lüders read
of `σ_a ⊗ σ_b`, with bit 0 mapped to +1. §0 QC mentions the extension.

### N6. "Identical tables on every native product test" holds only for encoded tests. **Accepted.**

**Verification.** QP node 7's table says reciprocal access reads `z₂` or `x₂`. Node 8, item 1, says those slots are
readable. After Lemma P, `z₂^A + z₂^B = 0` and `x₂^A + x₂^B = 0` are determined, and `τ_Y` (`z₂^A += 1`) flips the
first. So raw parity-cell slot reads, which form a wing-local product test, distinguish `pp = 0` from `pp = 1` in this
pair.

**Changes in r2:**
- **§6.3** title: "relative to its encoded product tests". The first bullet says "every encoded Pauli product test,
  which are J2's product-test tables".
- **§6.3** conclusion: "relative to encoded product tests and native operations".
- **§6.3** new bullet: it states the local test set, gives the raw-read distinction, and says "Whether some pair with
  equal encoded tables and different `pp` is indistinguishable under all native wing-local reads is not shown."
- **§4** E3/E4 remark: "no encoded product test reads (§6.3)".
- **§0 J2**, **§8 J2** ("Under all native wing-local reads it is not shown") and **§9** carry the same scope.

### N7. `hH2` has no displayed witness. **Accepted.**

**Verification:** SWAP/2 is native (E4 without `τ_Y`, now R-narrow). `cnot(SWAP/2) = (I + X⊗I + I⊗Z − X⊗Z)/4` takes
−1/2 on `(−x) ⊗ (−z)`. By hand: `¼(1 + a·t_A + t_B·b + aᵀCb) = ¼(1 − 1 − 1 − 1)`. Control: SWAP/2 is nonnegative on
all 36 Pauli product effects (r2 R5a–c). By (V), every native table is nonnegative on Pauli products, and so is the
cone they generate.

**Change in r2:** §8 K2 route displays this witness. §0 K2 route cites it.

### N8. The parity condition depends on the entry. **Accepted.**

**Verification by hand from the §2.1 pullbacks** (`f_x^A ↦ f_x^A + f_x^B`, `f_z^B ↦ f_z^A + f_z^B`,
`f_y^A ↦ f_y^A + f_x^B`, `f_y^B ↦ f_y^B + f_z^A`, others fixed):
- `XZ ↦ YY + pp`, `YY ↦ XZ + pp`, `XY ↦ YZ + pp` and `YZ ↦ XY + pp`.
- The other 11 products map without `pp`: `XI↔XX`, `IZ↔ZZ`, `YI↔YX`, `IY↔ZY`, `ZI`, `IX`, `ZX` fixed.
- The comparator's signs are −, −, +, + on the four and + on the other 11 (r2 R6a–c).
- Matching therefore requires, on a branch, that whenever `g` or `g + pp` is determined for some
  `g ∈ {XZ, YY, XY, YZ}`, `pp` is determined with value 1 for `XZ`, `YY` and 0 for `XY`, `YZ`.
- The conflicting pairs never co-occur. Each of `XZ+XY = f_z^B + f_y^B`, `XZ+YZ = f_x^A + f_y^A`,
  `YY+XY = f_x^A + f_y^A` and `YY+YZ = f_y^B + f_z^B` has `Q* = 1`, also with `pp` added, since `pp` is singular and in
  the radical. (K3) excludes all of them.

**Changes in r2:**
- **§6.2** new paragraph, **Gate-matching condition**, carrying the above. It notes that E2 fails the condition and
  E3 meets it.
- **§0 J7** states the condition in place of "happens to match".
- **§8 J7** adds "`pp = 1` for `XZ` or `YY` support, `pp = 0` for `XY` or `YZ` support".
- **§9** gate row: "exactly under the entry-dependent `pp` condition (§6.2)".

***

## Refusals

None. Two points go beyond the review's wording, and both are stated above:
- **B2:** the class-level sentence uses E4 rather than E2, so that it also covers the N2-removed class, and it is
  scoped to the classes considered.
- **N3:** the stabilizer-scope check covers all 60 stabilizer states.

## Additions forced by the changes (no other edits)

- **Header:** "revision r2". "The one probe" becomes "The two probes". §1's X layer reads "this unit's probes".
- **§0 QC:** under the stated access, E2 (QC-1) and E4 without `τ_Y` (SWAP/2) are also native non-quantum tables.
  - This keeps "the verdict rests on QC-2" from implying that the stated-access class needs QC-2 to fail.
  - QC-2 is the item that holds for every status of `pp` at the coupling.
- **§10:** the r2 probe record (hashes, check families, runs 1–3).

Not changed:
- r1's truncated AP1 (`…0c`) and M2D (`…353`) hashes. Both are consistent with the files, and no finding concerns
  them.
- No verdict, premise, classification label, other section or wording outside these items.
