# Q-868-H unit 1: heralds on native two-wing U′ preparations — validity, closure, quantum compatibility

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09), revision r2. Pending fresh independent review.** Nothing here
is adopted, promoted or proposed for the manuscripts. No premise is adopted and no new assumption is introduced. A
review ACCEPT, if reached, authorizes nothing further.

- **Accountable home:** #868. Parent programme #1169; status source #914 (row O-K2(P)).
- **Authorization:** owner (amaybaum), 2026-11-09, #868 c.6742050189, verbatim:
  > "(1) Q-868-H, paper analysis plus independent review only. Can one native OI construction prepare two-wing joint
  > states whose heralded branches stay inside both the native test set and OI's admissible state set? It covers
  > failures, herald probabilities, conditional states, repetition and composition, with no quantum states supplied as
  > inputs. Three outcomes are reported separately: validity, closure, and quantum compatibility. No outcome implies
  > another without proof. No computation, construction changes, new assumptions or execution."
  > "a drive that can generate the phase is not a derivation of that drive from OI, and the phase-vs-layer-flow
  > independence keeps its Lean-proved scope."

  "No computation" means no computation on an OI mechanism; exact checks of paper claims on generic mathematical
  objects are allowed if labelled (#1210 c.6739250392; #1211 c.6739843458). The native preparations below are
  enumerated **by hand**. The two probes (§10) check only Pauli-matrix and table facts; they encode no OI rule,
  encoding, coupling or preparation. The drive and the layer flow play no part in this unit.
- **Inputs:** `reassess/868/ASSESS-868.md` r3a (sha256 `d97c4b6b17bea9675d02a697e5164862471dad840dfbe9b54532baacd6788e1b`),
  which defines Q-868-H (§7 there), Lemma H (§4.1), witness w3 and the J-labels; its review `review/REVIEW-868-r3.md`
  (`2a5014a526399437754ecba4a8d8496ead456c33f10483c1b723acd170f0fd1d`, ACCEPT WITH NITS).
- **Corpus:** `git fetch origin main`; every source read with `git show fd539e15:<path>`
  (`fd539e150759a6ea51ab279aeeac80fc06050ade`). `origin/main` had moved to `cac5d264` when fetched; nothing after
  `fd539e15` was read. No `--depth`, `gc` or `prune`. No git or GitHub write.

Abbreviations: **QP** = `verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md`
(W; on `main`; its PROOF-RECOVERY.md is model-reviewed); **AP1** = `apparatus-1-20261107/DESIGN.md` (W; three model
review rounds); **M1D** = `mechanism-1-20261107/DESIGN.md`; **M2D** = `mechanism-2-20261108/DESIGN.md`;
**MI1** = `minacc-1-20261108/{DESIGN,RESULT}.md` (all under the same `reconstruction/` directory).

***

## 0. Summary

**Setting (§2).** Two wings A, B, each carrying QP's U′ encoding: a carrier cell `(z₁, x₁)` and a parity cell
`(z₂, x₂)` of the same colour, `f_z = z₁`, `f_x = x₁`, `f_y = z₁ + x₁ + z₂ + x₂`, parity `p = z₂ + x₂` (QP:443-451).
Carried as stated, with their status unchanged: N1, A4 (`k_ii = 0`), `q = 2`, N2 (with H-INF-μ for an infinite
hidden sector), P1 = SA-1(b), P2 = SA-1(c), P3, E-iso, H-PREP, WL, and **NNB**. NNB is QP's supplied conditional
premise (not adopted). U′'s Y read, `S` and `H` need it. ASSESS §7's posit list omits it; §2.2 explains why it is
carried here and what survives without it ("tier N").

**Validity (V): PASS** (native Pauli product tests, with NNB carried) [A + X]. Every two-wing preparation the stated
access builds yields product-test tables that are mixtures of products of cube vertices, a deterministic local model
with the pre-read configuration as the hidden variable (§4). So every permitted product test is nonnegative and every
remote herald lies in the cube cone. This includes heralded, postselected, repeated and sequentially composed
branches. The proof uses only that a read registers a linear functional of the current configuration (SA-1(a)),
wing-local kicks (E-iso, WL) and two-wing setting independence. The last is Main §3.3 hypothesis (iv), retained there
as a posit, not derived (Main:406-407), and supplied here through P3's external controller. The premises of (V) are
therefore SA-1(a), P3 with (iv), E-iso and WL, and NNB for the Y read. It does not use P1, P2, N2, Lemma 3 or
Lemma Q. All reachable tables also lie in `maxCone(eball 3)`, but full-ball tests are not supplied (stop S2), so that
is a fact about tables, not an operational validity.

**Closure (C): PASS, conditional and scoped** [A from AP1 Lemma 3 and QP Lemma Q, W]. Under P1, P2, N2, A4 at `q = 2`,
E-iso, WL and H-PREP, every remote herald, after any native read on one wing in any branch, leaves the other wing in
the octahedron. The single-wing dictionary is sound relative to the encoded subtheory: the wing's law on
`(f_x, f_y, f_z)` is fixed by its Bloch vector. The class is closed under repetition and under sequential
composition with every native operation, adaptive ones included (§5). Countercontrols that must break it do break
it while (V) survives: with P1 removed, or SA-1(c) removed, a remote herald puts B at Bloch `(±1, 0, ±1)`, outside
the octahedron and inside the cube. This is a native witness of (V) ⇏ (C) (§5.4). Scope limits: the octahedron
point is not a complete single-wing description under the full native access (QP node 8: parity-cell reads), and
the product table is not a complete two-wing description (§6.3).

**Quantum compatibility (QC): FAIL** [A + X]. The comparison map is the fixed U′ identification with the Pauli-table
map `ρ_T = ¼ Σ T_ab σ_a ⊗ σ_b`, with joint reads mapped to Lüders reads of `σ_a ⊗ σ_b` (§6.1). The Φ⁺ table is
natively reachable on some branches: Lemma P (§2.3) determines `pp` with carrier-only cross-wing couplings, and
`H_A; CNOT` then gives Φ⁺ (E3); so does E4 with `τ_Y`. A failure scoped to one status of `pp` therefore does not
carry the verdict on its own. The verdict rests on QC-2, which holds for every status of `pp` at the coupling. Under
the stated access E2 (QC-1) and E4 without `τ_Y` (SWAP/2) are also native non-quantum tables. Four scoped failures,
all from native preparations, none from a supplied quantum state:
- **QC-1** (branches with `pp` undetermined at the coupling): QP node 10's table `(I + XX + ZZ)/4`, eigenvalue −1/4.
  On such branches every table with two determined correlators is type 2, with eigenvalue −1/4. The zero completion
  is derived here (N2 with Lemma 3), not chosen.
- **QC-2** (any parity supply, independent or correlated, any value): from encoded `Z₊Z₊`, the native sequences
  `H_A; CNOT` and `S_A; H_A; CNOT` give opposite ⟨YY⟩. The comparator gives Φ⁺ for both, so at least one native
  outcome is non-quantum, with eigenvalue −1/2 or −1/4. This uses only whole encoded Cliffords and the graded
  coupling, so it survives QP's premise I.
- **QC-3** (lone parity translation): the native translation `z₂^A += 1` (P2 via H-PREP, no NNB) acts on two-wing
  tables as the partial transpose. It takes the natively reachable Φ⁺ table to SWAP/2, eigenvalue −1/2.
- **QC-4** (joint two-wing reads, not product tests): on every native state the Mermin–Peres row and column outcome
  sums both equal `p_A + p_B`. At least one line therefore disagrees with QM with probability ≥ 1/2.

In tier N (NNB not carried) only Z/X are read. Every reachable Z/X table then has a quantum completion. This is a
non-selective pass and settles nothing about the U′ body (§6.5).

**Directions (§A.34), each with its witness (§7).** (C) ⇒ (V): octahedron ⊂ cube. (V) ⇏ (C): the P1-removed remote
herald. (V) ⇏ QC and (C) ⇏ QC: QC-1 and QC-2 states satisfy both. QC ⇏ (C), at property level: the product state
`|0⟩ ⊗ (cos(π/8)|0⟩ + sin(π/8)|1⟩)` is quantum and leaves B at `(1/√2, 0, 1/√2)`, outside the octahedron, under every
A herald. It is a non-native logical witness, not an input; no native witness exists among the classes considered
(§7). QC ⇒ (V): PSD ⇒ block-positive (L).

**Stops.**
- **S1:** without NNB, the Y read, `S` and `H` are not supplied. The U′ body's Pauli test set is then incomplete.
- **S2:** non-Pauli product tests are not supplied (J6), so full-ball operational validity cannot be tested.
- **S3 (closed):** `p_A + p_B` can be determined with cross-wing couplings limited to carrier cells (Lemma P, §2.3).

**Effect on #868 (§8).**
- *J5:* holds on native Pauli tests by (V). It holds with closure under P1/P2/N2, which are supplied posits, not
  derived ones.
- *J7:* on a branch the native graded coupling acts as the table `cnot` iff, whenever one of `XZ`, `YY`, `XY`, `YZ`
  or its sum with `pp` is determined, `pp` is determined with value 1 for `XZ`, `YY` and 0 for `XY`, `YZ` (§6.2). No
  preparation of a given product table makes it do so for every native continuation (QC-2).
- *J2:* the native composite is not locally tomographic relative to its encoded Pauli product tests (J2's product-test
  tables) and native operations, through `p_A + p_B` (§6.3).
- *K2 route:* `hH2` fails for the native table cone: SWAP/2 is native and `cnot(SWAP/2)` is negative on a Pauli
  product (§8). Within its stated scope (U′, linear N + NNB, `q = 2`, the stated posits, with or without premise I),
  the native U′ composite is not a quantum composite.

***

## 1. Conventions

- **Layers:** K kernel; P paper proof on `main`; W research record on `main`, model-reviewed (§A.46.7: not
  verification); A derivation in this file, unreviewed; X exact check on generic objects in this unit's probes
  (computation-supported only); L literature.
- **Columns** (as in ASSESS §1): (i) well-defined; (ii) follows from independently justified OI principles; (iii)
  reproduces QM. Column (iii) never supports column (ii).
- **Distinctions kept apart:**
  - configuration carrier vs the encoded U′ carrier: everything here is encoded;
  - available vs derived: every posit keeps its source's status;
  - mixing vs the full rules: no mixing operation is used;
  - product-test validity vs quantum joint states.
- **Two senses of "herald."**
  - *Supply herald*: AP1's success flag `h` on a supplied cell.
  - *Remote herald*: Lemma H's vector `h_a(ω) = P(α)·(1, r^B|α)` on wing B after outcome α of a read on wing A.
  - Unqualified, "herald" means a remote herald.
- **Notation.** `ω` is the cell symplectic form (AP1 §4.1), pairing `z_i` with `x_i`. `Q*(f) = Σ_i f_{z_i} f_{x_i}`
  (QP Lemma Q). Functionals are written as pullbacks, as in QP node 8. `pp := p_A + p_B`. A *branch* is the
  conditional law given every record, supply herald and setting.

## 2. Setting, access and what is carried

### 2.1 The construction (QP, as stated)

| element | content | QP / AP1 anchor | status |
| --- | --- | --- | --- |
| U′ encoding | as in §0; `ω(f_a, f_b) = 1` for `a ≠ b`; `Q*(f_a) = 0`; `Q*(p) = 1` | QP:443-451, 527-534 | mathematical representation (E-U′) |
| Z, X reads | native minimal reads of `z₁`, `x₁`: record the slot, kick the conjugate by the meter's unknown `w` | AP1 §4.1–4.2; QP:537 | native step under P1, P2, P3, E-iso |
| Y read | `L` conjugation of the X read; `L = Na ∘ C12`, linear, `f_x∘L = f_y` | QP:538-545, 562-572 | needs NNB (`Na`) |
| `S`, `H` | `S = τ∘L`: `f_x∘S = f_y + 1`, `f_y∘S = f_x`, `f_z∘S = f_z`, `p∘S = p + 1`; `H`: `f_z ↔ f_x`, `f_y∘H = f_y + 1`, `p∘H = p + 1` | QP:575, 611-615 | need NNB |
| Pauli translations | `z₁ += 1`, `x₁ += 1`: preserve `p` | QP:607-619 | P2 via H-PREP |
| parity translation `τ_Y` | `z₂ += 1`: flips `f_y` and `p` only; acts as `Y ↦ −Y` | QP:728-731 (Lemma R) | P2 via H-PREP, no NNB |
| graded coupling ("CNOT") | between carrier cells A and B; `f_y^A ↦ f_y^A + f_x^B`, `f_y^B ↦ f_y^B + f_z^A` | QP:748-751 | P3 (cross-wing arming); graded, no NNB |
| same-colour transvection | mediator commutator, `m` returned | QP:279-282 | P3 |

*Reading of the graded coupling [A].* QP states its action on `f_y^A` and `f_y^B` and that it "acts on the encoded
functionals as a CNOT" between carrier cells. With a transvection `z_B += z_A`, `x_A += x_B` this gives
- `f_x^A ↦ f_x^A + f_x^B`, `f_z^B ↦ f_z^A + f_z^B`, `f_x^B`, `f_z^A` fixed,
- QP's two stated images,
- `p_A`, `p_B` unchanged, since the parity cells are not touched.

QP's own consequence ("the determined functionals are `f_x^A + f_x^B` and `f_z^A + f_z^B`") follows from this reading.

### 2.2 Why NNB is carried, and tier N

- U′ is defined in QP as Route NNB (QP:443-456). Its Y read, `S` and `H` contain `Na`/`Nb`.
- Without NNB, Lemma G1's grading makes every record single-sector (QP:267-268). `f_y` mixes sectors (`z₁ + z₂` and
  `x₁ + x₂` lie in opposite sectors), so no record equals `f_y`.
- A two-record read of `z₁ + z₂` and then `x₁ + x₂` determines `f_y`, but it is not the encoded Y read. It registers
  `z₁ + z₂` separately: on a state with `z₂` known it also reveals `f_z`. It also randomizes `p`.
- **Tier N** is the class without NNB. Its encoded tests are Z and X only.
- Y eigenstates are still natively preparable in tier N [A]. Take ready cells with `z₁ = 0` and `x₂ = 0` known, and
  apply `C21` (`z₁ += z₂`, `x₂ += x₁`). This determines `z₁ + z₂ = 0` and `x₁ + x₂ = 0`, hence `f_y = 0`. Both are
  graded and they commute.
- So in tier N the body is the octahedron but the test set is incomplete (stop S1).
- The main analysis carries NNB with QP's status (supplied, conditional, not adopted). Every verdict states whether
  it needs NNB.

### 2.3 The stated access

- **Supplies.** Independent P2 ready cells, each with exactly one known slot (value 0, or 1 through H-PREP), the
  other slot uniform and independent (SA-1(c), AP1:297-300). Hidden cells have no known slot (N2, H-INF-μ).
- **Operations.** P3-armed graded couplings within and across wings (through mediators for same-colour pairs), NNB
  couplings within a wing, constant translations, native minimal reads (P1: registration is terminal),
  discarding, adaptive record-conditioned armings and translations (QP:145-148), and H-PREP conditioning.
- **Cross-wing coupling scope.** ASSESS §7 says "couplings P3 may arm between the wings' carrier cells". Two
  readings:
  - *R-wide*: any cell of the two encoded carriers. This allows correlated parity cells, QP node 10's "correlated but
    local parities".
  - *R-narrow*: carrier cells only.

  Every verdict and every witness below holds under R-narrow, through Lemma P.
- **Lemma P (relative parity under R-narrow) [A, from QP node 8's cell swap].** Supply ready carriers with
  `z₁^A = 0` and `x₁^B = 0` known, and ready parity cells with one known slot each, value 0 (P2).
  1. Apply the cross-wing graded carrier–carrier transvection `z₁^A += z₁^B`, `x₁^B += x₁^A` (the encoded CNOT with
     control B; the same carrier step as E4). Then `z₁^A + z₁^B = 0` and `x₁^A + x₁^B = 0` are determined.
  2. On each wing apply QP's graded cell swap `W = C12 ∘ C21 ∘ C12` (QP:612), with `C12`: `z₂ += z₁`, `x₁ += x₂`
     (QP:562-563, through a wing-local mediator) and `C21`: `z₁ += z₂`, `x₂ += x₁`. By hand,
     `(z₁, z₂) → (z₁, z₁ + z₂) → (z₂, z₁ + z₂) → (z₂, z₁)` and `(x₁, x₂) → (x₁ + x₂, x₂) → (x₁ + x₂, x₁) → (x₂, x₁)`,
     so `W` exchanges the two cells.
  3. The parity cells now carry the correlation: `z₂^A + z₂^B = 0` and `x₂^A + x₂^B = 0`, so `pp = 0` is determined.
     The carriers are the former parity supplies with their known slots (e.g. `z = 0` on both wings: `Z₊Z₊`).

  Every step is graded, either wing-local or carrier–carrier; no NNB, no translation and no parity–parity coupling is
  used. `Q*(pp) = 0`, so Lemma Q permits the determination, and the parity cells stay local to their wings (WL).
  `τ_Y` (or `S`) on one wing then gives `pp = 1`.
- **WL.** Each wing's parity cell, mediators and meters are local to it during reads. A shared parity cell signals
  (QP:413-418, :556) and is excluded.

### 2.4 Restrictions used, by column

| restriction | (i) | (ii) from independently justified OI principles? | (iii) reproduces QM? |
| --- | --- | --- | --- |
| N1, A4 (`k_ii = 0`), `q = 2` | yes | native (Substratum A4/A5; QP ledger) | n/a |
| P1 = SA-1(b), P2 = SA-1(c) | yes | **no**: supplied physical posits (AP1:419-420, "New physical posit") | single-wing stabilizer scope; composite no (§6) |
| P3, E-iso | yes | **no**: supplied posit and idealization (AP1:421) | n/a |
| (iv) two-wing measurement independence | yes | **no**: Main §3.3 hypothesis (iv), a posit, not derived (Main:406-407); supplied here through P3's external controller | n/a |
| H-PREP | yes | **no**: open named hypothesis (AP1:418) | n/a |
| N2 | yes | native counting measure applied through H-PREP; H-INF-μ for an infinite hidden sector (QP:777) | n/a |
| NNB | yes | **no**: supplied conditional premise, not adopted (QP:783, 805-831) | gives `S`, `H`; also gives Lemma R's second reflection |
| WL | yes | design condition; its necessity follows from the C-NS requirement (QP:784), itself a branch requirement (Main:414, :429) | n/a |
| premise I (counterfactual scope only, §6.2) | yes | **no**: target-defined, contradicts P3 (QP:785, 833-844; M1D CC-RECON) | — |

***

## 3. The reachable class (paper analysis)

**Proposition K (branch structure) [A from AP1 Lemma 3 and QP Lemma Q(iii), W].** Fix any finite protocol built by
the stated access (§2.3), adaptive or not, with or without NNB, on any number of cells and any hidden sector. In every
branch:
- (K1) the law of all active slots is uniform on an affine subspace;
- (K2) its determined functionals form a subspace `D` that is isotropic for `ω`;
- (K3) `Q* ≡ 0` on `D`.

*Proof.*
- (K1): each step is an affine bijection; each registration conditions on a linear functional's value; unknowns
  are uniform and independent (N2, SA-1(c)); marginals of uniform affine laws are uniform affine.
- (K2): AP1 Lemma 3 (AP1:533-561). Its proof needs only symplectic ticks (NNB's symmetric, centre-free coupling is
  symplectic by AP1:479-483), one known functional per ready cell, and terminal registration.
- (K3): QP Lemma Q(iii) (QP:484-495), stated for all of N, adaptive included, and for NNB couplings.
- Record-controlled translations change values, not `D`. Coarse-graining over records gives mixtures of such
  branches. ∎

**Consequences on the two-wing encoded span** `E₂ = span{f_a^A, f_a^B}` (6-dimensional; it contains `p_A`, `p_B`).
- **(Q-form) [A].** On one wing, `Q*(α f_x + β f_y + γ f_z) = αβ + αγ + βγ`, since the polar form of `Q*` is `ω`.
  Its only nonzero singular vectors are `f_x`, `f_y`, `f_z`. The functionals `f_a + f_b` (`a ≠ b`) and `p` have
  `Q* = 1`. `p` lies in the radical of `ω` restricted to the wing's encoded span (`ω(p, f_a) = 1 + 1 = 0`).
- **(D_E).** In a branch, the determined encoded set `D_E = D ∩ E₂` is totally singular for `Q_A ⊕ Q_B`.
  `pp = p_A + p_B` is singular and lies in the radical, so it can be adjoined to any totally singular subspace.
  Every maximal `D_E` therefore has dimension 3 and contains `pp`.
- **Lemma T (table types) [A].** Every branch table `T_ab = E[(−1)^{f_a^A + f_b^B}]` (`a, b ∈ {0, x, y, z}`,
  `f_0 = 0`) has entries in {0, ±1} and is of exactly one type:
  - **0**: `I/4`;
  - **P**: a product of single-wing points in {0, ±e_a};
  - **1**: zero marginals and one correlator `± σ_a ⊗ σ_b`;
  - **2**: zero marginals and two correlators `± σ_a ⊗ σ_{π(a)}`, `± σ_c ⊗ σ_{π(c)}` (`a ≠ c`), with `pp ∉ D_E`;
  - **3**: zero marginals and a full signed permutation `s_a σ_a ⊗ σ_{π(a)}`, with `pp ∈ D_E` and
    `s_x s_y s_z = (−1)^{pp}`.

  *Proof.*
  - A product-form functional `f_a^A + f_b^B` is singular.
  - Two correlators sharing an index have a sum of type `f_b^B + f_{b′}^B`, with `Q* = 1`. So the correlators form a
    partial permutation.
  - A determined marginal `f_a^A` excludes every correlator `f_c^A + f_b^B` with `c ∉ {0, a}`, since `ω = 1`. The
    remaining correlators `f_a^A + f_b^B` are determined iff `f_b^B` is. That gives type P.
  - The three correlators of a full permutation sum to `pp`. With two correlators, the third is determined iff
    `pp ∈ D_E`, with value fixed by the other two and `pp`.
  - Any functional of `E₂` not in `D_E` is non-constant on the affine support, hence exactly uniform (N2). So every
    other entry is 0. ∎

**Remote herald identity [A].** Let wing A's reads produce records `R_A`. Wing B's conditional law given `R_A` is the
B-marginal of the branch given `R_A`. Its determined B-functionals form `D ∩ (B-functionals)`, which is isotropic
by (K2). So at most one of `f_x^B`, `f_y^B`, `f_z^B` is determined. By (K3), no `f_a^B + f_b^B` and no `p_B` is
determined. B's law on its encoded triple is therefore the uniform law on a level set `{f_a^B = β}` or the uniform
law. Its Bloch vector is in {0, ±e_a}.

***

## 4. Hand enumeration of the native two-wing preparations

Each row is built from the operations in §2.1. "Herald prob." is the probability of the remote herald by a read on A,
per branch. "B | A" is B's conditional Bloch vector. Supply-herald success is independent of carrier and settings
(AP1:679), so conditioning on it changes nothing below. Every probability of a finite protocol is dyadic (AP1:625-626).

| # | preparation (stated access only) | NNB? | `D_E` (branch) | table type | herald prob. on A-read `c` | B \| A |
| --- | --- | --- | --- | --- | --- | --- |
| E1 | product: each wing's carrier ready with a known slot (`Z±`, `X±`), or the `C21` construction (`Y±`, §2.2); independent parity cells | no | `{f_a^A, f_b^B}` (+ `pp` only if built by Lemma P) | P | 1 or 0 if `c = a`; ½ otherwise | B's marginal (no steering) |
| E2 | QP node 10: E1 at `Z₊Z₊`, then `H_A`, then the graded coupling; independent parity supplies | yes (`H`) | `{XX, ZZ}`, `pp` undetermined | 2: `(I + XX + ZZ)/4` | ½ for every `c` | `c = x`: `±e_x`; `c = z`: `±e_z`; `c = y`: 0 |
| E3 | as E2, from Lemma P's `Z₊Z₊` with `pp = 0` (R-narrow); `τ_Y` on one wing gives `pp = 1` | yes (`H`) | `{XX, ZZ, pp}` | 3: `⟨YY⟩ = (−1)^{pp_after}` | ½ | `±e_{π(c)}` for every `c` |
| E4 | graded-only Bell table (R-narrow; tier N): Lemma P with parity supplies `z₂^A = 0`, `x₂^B = 0`, so the carriers are then ready with `z_A = 0`, `x_B = 0` and `pp = 0`; `C` across, giving `z_A + z_B = 0`, `x_A + x_B = 0` | no | `{XX, ZZ, pp}` | 3: SWAP/2 if `pp = 0`, Φ⁺ table if `pp = 1` | ½ | `±e_c` |
| E5 | any Ek, then `τ_Y` on A | no | `f_y^A`-entries flip, `pp` flips | same type, Y row negated | unchanged | `y`-component negated |
| E6 | any Ek, then wing-local encoded Cliffords, Pauli translations, further graded couplings, reads, discards, feedback | per op | by pullback | by Lemma T | ½, 1, 0 per branch; dyadic mixtures | in {0, ±e} per branch |
| E7 | coarse-graining (forgetting records), random choice of preparation | — | mixture | convex combination | weighted | octahedron |

Remarks [A]:
- *E2 is QP's construction.* After `H_A`, `f_x^A = 0` (pullback of `f_z`). The coupling pulls `XX` back to `f_x^A`
  and `ZZ` back to `f_z^B`, so both are determined; `YY = XX + ZZ + pp` is not. The zero entries elsewhere follow
  from Lemma T. That is the "zero completion" ASSESS §4.3 took from QP's N2 rule; here it is derived.
- *E3/E4: the table's Y⊗Y sign is set by the hidden `pp`, which no encoded product test reads (§6.3).* E4 without `τ_Y` gives SWAP/2,
  a non-quantum table, and with `τ_Y` gives the Φ⁺ table. No stated principle selects either.
- *Failure modes (all scoped to the stated access):*
  - **F1** supply-herald failure (⊥): independent of carrier and settings (AP1:679); conditioning is harmless for
    every outcome.
  - **F2** unheralded defective meter (AP1:615-620): a different instrument, with a uniform, uninformative record.
    B is unaffected.
  - **F3** shared parity cell: signalling (QP:413-418); excluded by WL.
  - **F4** P1 violated: closure breaks, validity holds (§5.4).
  - **F5** SA-1(c) violated (a sharp ready cell): as F4 (AP1:677).
  - **F6** biased unknowns (N2 fails): closure breaks (AP1:824), validity holds.
  - **F7** odd-cycle winding (H-FIN), E-iso failure, centre terms (Route U, QP:430-441), or a state-dependent graph
    (MI1: `G_σ` loses Lemma Q(iii) protection): outside the stated class, not analysed.
- *Repetition.* Fresh supplies are independent (SA-1(c)), so repeated runs are i.i.d. under N2 (H-INF-μ). Reusing a
  cell (e.g. a retained meter with its kick variable, AP1 §4.5) is a sequential composition, so it lies in E6.
  Supplies are a #1147 resource.
- *Sequential composition.* E6: the class of Proposition K is closed under every stated operation, because K1–K3 hold
  for every protocol in it.

***

## 5. Closure (C)

### 5.1 Statement and decision rule (ASSESS §7, fixed before this work)

(C) passes iff every remote herald, by any natively available read on one wing, over every preparation and heralded
continuation the stated access builds, leaves the other wing in the octahedron with the single-wing dictionary
sound. One explicit herald outside fails it. A missing preparation or read stops it.

### 5.2 Verdict: PASS, conditional on P1, P2, N2 (+ H-INF-μ), A4 at `q = 2`, E-iso, WL, H-PREP; NNB for the Y read

- *Octahedron.* The remote herald identity (§3): per branch, B's Bloch vector lies in {0, ±e_a}. A remote herald by
  any record event (coarse-grained, failure-flagged, adaptive) is a nonnegative combination of branch heralds, so it
  lies in the octahedron cone.
  - This covers every native read on A: encoded Pauli reads, raw slot reads of A's parity cell, reads of ancillas
    and mediators, and two-record reads.
  - It also covers reads on A after any composition.
- *Dictionary (single wing).* Within a branch, the B-law on `(f_x, f_y, f_z)^B` is fixed by its Bloch vector (§3).
  For mixtures this holds too: every `Q* = 1` functional of the encoded span has expectation 0 in every branch.
  - Encoded single-wing protocols move only within the encoded span. A read of `f_a` shifts `f_b` by
    `w·ω(f_b, f_a)` with a fresh uniform `w`. `S`, `H` and the Pauli translations pull encoded functionals back to
    encoded functionals plus constants (QP:569-575, 611-615).
  - So every encoded continuation's record law is a function of the Bloch vector. The dictionary is sound relative
    to the encoded subtheory (QP's A2 induction, QP:580-601, extended to conditional inputs).
- *Repetition and composition.* Closed (§4, E6), since Proposition K holds for every protocol in the class.

### 5.3 Scope of the pass

- **Encoded dictionary only.** Under the full native access the octahedron point is not a complete description of a
  wing. A raw read of `z₂` distinguishes knowledge states with the same Bloch vector, e.g. `S` versus `I` on `Z₊`
  with `z₂` known (QP:630-632). This is QP's single-wing finding and is not composite-specific.
- **Single-wing closure is not two-wing completeness.** The two-wing product table does not fix the encoded
  two-wing law (§6.3).
- **Column (ii).** Every load-bearing posit except A4 is supplied (§2.4). The pass shows the stated posits close the
  native composite's heralds inside the native body. It does not source J5 from independently justified OI
  principles.

### 5.4 Countercontrols (must break (C), and do; (V) survives each) [A from AP1, W]

1. **P1 removed** (AP1 C9, AP1:682). On E3/E4 (`XX`, `ZZ` determined), A reads `f_x^A`, then reads its meter's kick
   slot (learning `w`), then reads `f_z^A`. A then knows `f_x^A(s)` and `f_z^A(s)` of the pre-read configuration.
   B's conditional has `f_x^B` and `f_z^B` both determined; `p_B` stays undetermined, so `f_y^B` does too. Bloch
   `(±1, 0, ±1)`: in the cube, outside the octahedron and outside the ball (probe J1). This is ASSESS's w3 gap,
   realized natively by steering.
2. **SA-1(c) removed** (sharp ready meter, `w` known; AP1:677). The same herald.
3. **N2 removed** (a biased kick `P(w = 1) = p ≠ ½`). B's conditional `f_z^B` is biased, giving points such as
   `(1, 0, |1 − 2p|)`, outside the octahedron (cf. AP1:824).

In each case (V) holds by §6's argument, which uses none of P1, P2 or N2. The verdict of §5.2 is therefore not
vacuous: it rests on exactly these posits.

***

## 6. Validity (V) and quantum compatibility (QC)

### 6.0 Validity (V): PASS on native Pauli product tests [A; X: probe I1–I3]

*Argument.* In a product test (read `a` on A, `b` on B), each read first registers the current value of its encoded
functional. For Z and X that is the slot copy (AP1:487-491). For Y it is the X read conjugated by the linear `L`, with
no translation (QP:538-541). The kick changes only conjugate slots on the reading wing (E-iso, WL), and
`ω(f_b^B, f_a^A) = 0`. Settings are chosen by P3's external controller, independently of the configuration: this is
Main §3.3 hypothesis (iv), a posit there, not derived (Main:406-407); AP1 C1 is its one-wing counterpart. Hence the
joint record is `(f_a^A(s), f_b^B(s))` with `s` drawn from the branch law. The table is a mixture of products of cube vertices
`v_W(s) = ((−1)^{f_x^W(s)}, (−1)^{f_y^W(s)}, (−1)^{f_z^W(s)})`. Each such product gives 0 or 1 on every product of
Pauli sharp effects (probe I3). So:
- every permitted product test, and every coarse-graining or randomized mixture of them, is nonnegative;
- every remote herald is a nonnegative combination of `(1, v)` with `v` a cube vertex, i.e. it lies in the cube cone,
  the dual of the native tests (ASSESS r3 W1).

The same holds for any conditioned or postselected sub-ensemble, since a conditional of a mixture is a mixture. Main
§3.3 and Main:564 [P] state the same structure for Bell locality ("a measurement-independent deterministic
completion with one-step own-wing setting interventions … is Bell-local"). M2D Theorem NC's CHSH ≤ 2 (M2D:65-71) is
consistent with it. AP1's deferred C6 (AP1:679) is answered for U′ composites under these conditions: (iv) through
P3; Main's (ii) and (iii) through E-iso and WL; `⊥` branches whose heralds are independent of setting and carrier
(AP1:679; F1); and Pauli settings only, since non-Pauli settings are not supplied (S2). Under them the native product
statistics are Bell-local. At stabilizer scope this answer does not discriminate: every two-qubit stabilizer state
with Pauli settings also has `|CHSH| ≤ 2` [A; X: r2 R4a–b]. By hand: with distinct settings on each wing, two CHSH
correlators that share a setting anticommute, so at most two of the four are ±1 on a stabilizer state; with equal
settings on a wing, CHSH is twice one correlator. Pauli settings do separate non-stabilizer
quantum states: `XX + XZ + ZX − ZZ` has eigenvalue `2√2` (R4c).

*Examples (probe I1, I2).* QP's node-10 table `(I + XX + ZZ)/4` is the uniform mixture of 16 such products. SWAP/2 is
the uniform mixture of 8.

*Full-ball tables [A + X: C1–C3].* Every Lemma-T table lies in `maxCone(eball 3)`. Types 0 and P are products of
ball points. Types 1–3 have zero marginals and a signed partial-permutation block `C` with `|Cᵀa| ≤ |a|`, so
`1 + aᵀCb ≥ 1 − |a||b| ≥ 0` (Lemma H (⇐)). The control `(I + XX + XZ)/4` is negative on a ball product (C3). Full-ball
tests are not supplied (J6; stop S2), so this is a fact about the tables, not an operational validity.

*Skepticism (§A.31).* This pass is favourable and cheap. Executed reads have nonnegative probabilities, and a local
deterministic model exists. It is informative only together with QC (§6.2), which shows that the valid tables
include non-quantum ones.

### 6.1 The comparison map (stated before the QC checks)

- **Map.** Fix E-U′ for all settings (QP:786). Map the encoded Pauli read `a` on wing W to `σ_a`, and outcome bit 0
  to +1 ("bit 0 = +", QP:596). A preparation's product-test table `T` maps to `ρ_T = ¼ Σ_{a,b} T_ab σ_a ⊗ σ_b`.
- **Compatibility of a preparation.** `ρ_T ⪰ 0`. Pauli product tables are tomographically complete for two qubits,
  so `ρ_T` is then the unique matching quantum state.
- **Compatibility of an operation.** Its action on tables equals the comparator's action (I1, QP:108-113).
- **Joint reads.** A native joint read of `g = f_a^A + f_b^B` (along `J g`, QC-4) maps to the Lüders read of
  `σ_a ⊗ σ_b`, with outcome bit 0 mapped to +1.
- **Inputs.** No quantum state is supplied as input. The comparator enters only as column (iii).

### 6.2 QC verdict: FAIL

- **QC-1** (branches with `pp` undetermined at the coupling; R-narrow suffices; NNB for `H`).
  - E2 gives `(I + XX + ZZ)/4`, eigenvalue −1/4 (probe A1).
  - Every type-2 table has minimum eigenvalue −1/4 (probe B4). Two determined commuting correlators force the third
    to ±1 for any quantum state, and type 2 has it at 0.
  - The coupling leaves `pp` unchanged. So on a branch with `pp` undetermined at the coupling, a resulting table with
    two determined correlators is type 2 (type 3 needs `pp ∈ D_E`, Lemma T) and is non-quantum.
  - Independent product supplies do not confine a protocol to such branches. Lemma P determines `pp` from them under
    R-narrow, and `H_A; CNOT` then gives the Φ⁺ table (E3), which is quantum.
- **QC-2** (every parity supply; R-narrow suffices; NNB for `S`, `H`; survives premise I) [A + X: F1–F3, A1, A2].
  Start from encoded `Z₊Z₊` with `pp` in any status (determined with value π, or undetermined).
  - Path 1, `H_A; CNOT`: `H` flips `p_A`, giving `X₊Z₊` with `pp = π + 1`. The coupling pulls `YY` back to
    `f_x^A + f_z^B + pp`, so `⟨YY⟩ = (−1)^{π+1}`.
  - Path 2, `S_A; H_A; CNOT`: `S` fixes `Z₊` and flips `p_A`, then `H` flips it back, so `⟨YY⟩ = (−1)^π`.
  - In both paths `XX = ZZ = +1` and every other entry is 0.
  - The comparator gives Φ⁺ for both paths (`S|0⟩ = |0⟩`; F1, F2), with `⟨YY⟩ = −1`.
  - If π is determined, one path gives `(I + XX + YY + ZZ)/4 = SWAP/2`, eigenvalue −1/2 (A2). If π is undetermined,
    both paths give `(I + XX + ZZ)/4`, eigenvalue −1/4.
  - Only whole encoded Cliffords and the graded coupling are used. QP's premise I, which permits odd linear parts
    only together with their `p`-flipping translations, does not exclude this. No rule fixing `pp` at preparation
    helps either.
  - This is QP's subtheory-relative contextuality (`S` versus `I` on `Z₊`, QP:630-632), which the entangling coupling
    turns into a product-test difference.
- **QC-3** (lone `τ_Y`; R-narrow, E4 through Lemma P; no NNB to build, NNB to read Y) [A + X: E1, E2].
  - `τ_Y` on A negates every `T_{y,b}`. On two-wing tables that is exactly the partial transpose on A (probe E1).
  - It maps E4's Φ⁺ table to SWAP/2, eigenvalue −1/2 (E2).
  - This is the composite form of QP's C-CP failure "within N already" (QP:728-731) and of ASSESS §4.3 item 2
    (K2-GUARD-1).
- **QC-4** (joint two-wing reads; outside product tests; NNB and cross-wing conjugation) [A + X: G1–G3].
  - The row `{f_x^A + f_z^B, f_z^A + f_x^B, f_y^A + f_y^B}` and the column `{XX, ZZ, YY}` functionals each pairwise
    commute (`ω = 1 + 1 = 0`) and each sum to `pp`.
  - A read along `J g` with `g ∈ E₂` changes neither the line's other members nor `pp`, since `pp` lies in the
    radical.
  - So sequential joint reads of either line give outcome sum = the pre-read `pp`.
  - QM gives row sum 0 and column sum 1 on every state (G1, G2). On every native state,
    `P(row correct) + P(column correct) = P(pp = 0) + P(pp = 1) = 1`.
  - This is QP node 10's argument (QP:758-764), extended to undetermined `pp`.

**Sign rule, for the record [X: B1–B3].** A type-3 table with pairing π and signs `s` is PSD iff
`s_x s_y s_z = −sgn(π)`. Natively `s_x s_y s_z = (−1)^{pp}`. So a type-3 branch is quantum iff `(−1)^{pp} = −sgn(π)`.
- Local encoded odd Cliffords flip both sides, so they preserve quantumness of type-3 tables. Their table action
  equals the comparator's signed axis permutation on the acted wing (QP A2).
- The failure enters only through `pp`'s status at the moment the coupling creates the correlation. QC-2 shows no
  status of `pp` makes this right for all native continuations.

**Gate-matching condition [A; X: r2 R6a–c].** By hand from the §2.1 pullbacks, the native coupling pulls the output's
`XZ`, `YY`, `XY`, `YZ` back to the input's `YY + pp`, `XZ + pp`, `YZ + pp`, `XY + pp`. It pulls every other Pauli
product back to a Pauli product without `pp`. The comparator's `cnot` pairs the same products, with signs −, −, +, +
on these four and + on every other (R6a–c).
- So on a branch the native coupling acts as the table `cnot` iff the following holds: whenever some
  `g ∈ {XZ, YY, XY, YZ}` of the input, or `g + pp`, is determined, `pp` is determined, with value 1 for
  `g ∈ {XZ, YY}` and 0 for `g ∈ {XY, YZ}`.
- The two requirements never arise on one branch. Each of the pairs `XZ/XY`, `XZ/YZ`, `YY/XY`, `YY/YZ` sums, alone or
  with `pp`, to a `Q* = 1` functional, which (K3) excludes from `D`.
- E2 fails the condition (`XZ` determined, `pp` not); E3 with `pp_after = 1` meets it.
- No single preparation-time value of `pp` serves every input, in agreement with QC-2.

### 6.3 The native composite is not locally tomographic relative to its encoded product tests [A]

- `Z₊Z₊` with `pp = 0` (Lemma P) and with `pp = 1` (Lemma P, then `τ_Y` on one wing) have identical tables on every
  encoded Pauli product test, which are J2's product-test tables: `pp` is not product-form, and no product-form
  element changes.
- They are distinguished by the native sequence `H_A; CNOT; (Y, Y)` (QC-2) and by a native joint read of `pp`.
- So J2, relative to encoded product tests and native operations, fails in the U′ composite.
- The finding is scoped to encoded tests. Raw slot reads of the parity cells are native minimal reads (QP node 7;
  node 8, item 1) and form a wing-local product test. After Lemma P, `z₂^A + z₂^B` and `x₂^A + x₂^B` are determined
  and `τ_Y` flips the first, so these reads distinguish the pair above. Whether some pair with equal encoded tables
  and different `pp` is indistinguishable under all native wing-local reads is not shown.
- The single-wing encoded description is complete for single-wing encoded protocols (§5.2), so the extra two-wing
  parameter is the relative parity `pp`, readable by a joint read and steering later product tables.
- This sits beside M2D's remark that Theorem NC needs spanning, tomographically complete equivalences (M2D:65-71,
  250, 282).

### 6.4 What the failures do not show

- They do not show that no OI composite is quantum. They concern the U′ encoding, linear N with NNB, `q = 2` and the
  stated posits.
- They do not touch the configuration carrier (Main:564's interface) or any non-linear or state-dependent rule
  (M2D, MI1).
- They do not depend on the drive or the layer flow.
- They supply no column-(ii) reason for or against any posit.

### 6.5 Tier N (NNB not carried)

- Only Z, X reads exist on each wing. `S`, `H` and the Y read are not supplied (stop S1).
- (V) and (C) hold on Z/X tests by the same arguments, with the diamond in place of the octahedron (AP1 Lemma 4).
- For QC on Z/X tables [A + X: H1, H2]: each branch's Z/X sub-table is a product, a single correlator, or one of
  `{XX, ZZ}`, `{XZ, ZX}` with signs, and each has a PSD completion. Mixtures complete by mixing the completions.
- This is a **non-selective** pass: real two-qubit (rebit) tables pass the same test. The completion's YY entry need
  not equal the native `f_y` correlation (E4 without `τ_Y` has native `⟨YY⟩ = +1`; its completion uses −1). It is not
  a dictionary for the U′ body.

***

## 7. Directions (§A.34)

| relation | status | witness |
| --- | --- | --- |
| (C) ⇒ (V) | holds | octahedron ⊂ cube (ASSESS r3 W2); and (V) holds here without P1, P2 or N2 (§6.0) |
| (V) ⇒ (C) | **fails** | P1-removed remote herald `(±1, 0, ±1)` from E3/E4 (§5.4): (V) holds, (C) fails |
| (V) ⇒ QC | **fails** | E2 (QC-1): valid on Pauli tests, eigenvalue −1/4 |
| (C) ⇒ QC | **fails** | E2 and the QC-2 states satisfy (C) under the posits and fail QC |
| QC ⇒ (C) | **fails** (property level) | non-native: the product state `\|0⟩ ⊗ (cos(π/8)\|0⟩ + sin(π/8)\|1⟩)` is quantum, and every A herald leaves B at `(1/√2, 0, 1/√2)`, outside the octahedron (r2 R2a–e) |
| QC ⇒ (V) | holds (L) | PSD ⇒ block-positive; on Pauli tests directly |

*The QC ⇏ (C) witness.* It is a logical witness only, not an input to any construction. No native witness exists
among the classes considered here. The stated access and each §5.4 countercontrol class contain E4 without `τ_Y`,
whose determined entries are `XX = YY = ZZ = +1`. No quantum state has these, whatever its other entries, since
`⟨SWAP⟩ ≤ 1` bounds their sum by 1 (r2 R1d). So each of these classes fails QC.
At the P1-removed herald that breaks (C), QC fails as well: `(±1, 0, ±1)` lies outside the Bloch ball (r2 R3a), and
the comparator's herald for the same reads on Φ⁺ is `±e_x` (R3b). What the native P1-removed continuation of E4 with
`τ_Y` shows is the weaker statement that a PSD prepared table does not imply (C) for its continuations.

The three outcomes are proved separately. No verdict above is inferred from another.

## 8. Effect on ASSESS-868's ledger (scoped; nothing adopted)

- **J5 (validity).** On native Pauli tests for U′ composites: holds by (V), independently of SA-1(c). The sufficient
  route through closure needs P1, P2 and N2, all supplied. ASSESS's remark that "validity itself is not shown to
  inherit that status" is confirmed: (V) does not use them. The locus is unchanged: the composite preparations'
  heralds.
- **J7 (table `cnot`).**
  - ASSESS says the native gate "does not act as the table `cnot`" on `(x₊, z₊)`. That is right for independent
    parities.
  - With `pp` determined (Lemma P, R-narrow) the gate gives the Φ⁺ table on `X₊Z₊` iff `pp = 1` (E3). In general it
    acts as the table `cnot` exactly under §6.2's entry-dependent condition: `pp = 1` for `XZ` or `YY` support,
    `pp = 0` for `XY` or `YZ` support.
  - QC-2 shows that no parity status of a given product table makes the gate act as the table `cnot` for every
    native continuation, with or without premise I.
- **J2 (local tomography).** Fails relative to encoded Pauli product tests (J2's product-test tables) and native
  operations (§6.3). Under all native wing-local reads it is not shown.
- **K2 route.** The native table cone is not `cnot`-invariant in the table sense (`hH2`). Witness [A + X: r2 R5a–c]:
  SWAP/2 is native (E4 without `τ_Y`); `cnot(SWAP/2) = (I + X⊗I + I⊗Z − X⊗Z)/4` takes −1/2 on the Pauli product
  effect `(−x) ⊗ (−z)`; every native table, and so every element of the cone they generate, is nonnegative on Pauli
  products by (V); so `cnot(SWAP/2)` lies outside the cone. `hH1` at full-ball scope is not supplied (non-Pauli
  preparations).
- **J3, J8, J13** are untouched. Every preparation here is stabilizer-scope and uses no pair source beyond P2
  supplies and P3 couplings.
- **#1210 M3 (SA-1(c), QM-only).** The closure pass rests on SA-1(c). So the shared column-(ii) gap ASSESS §6 names
  is confirmed for (C) and absent for (V).

## 9. §A.31 classification

Productivity test as in ASSESS §8. Labels are relative to `git grep` at `fd539e15` over `verification/` and
`papers/` for "relative parity", "p_A + p_B", "tomograph" and "U′". The hits are QP:53, :509, :557, :753-764 and
:947; AP1:726; M2D:250, :282; the MR-1 records; and the COMP-1 and PC-1 preregistrations. None states §6.3 or QC-2.

| finding | label |
| --- | --- |
| Proposition K and Lemma T (two-wing branch structure; table types; maximal `D_E` contains `pp`) | ELABORATING (AP1 Lemma 3, QP Lemma Q, applied to `E₂`) |
| Lemma P: `pp` determined from independent supplies with carrier-only cross-wing couplings | ELABORATING (QP node 8's cell swap `W`; node 7's relative parity) |
| (V) by a cube-vertex local model; AP1 C6 answered for U′ composites under (iv) via P3, E-iso/WL and Pauli settings, non-selective at stabilizer scope | CONFIRMING (Main §3.3 and :564 [P]; M2D Theorem NC) |
| (C) for remote heralds under P1/P2/N2, with the encoded-dictionary scope | ELABORATING (AP1 Lemma 4 to remote heralds) |
| Native realization of (V) ⇏ (C) under P1 or SA-1(c) removal | ELABORATING (AP1 C4, C9 used by steering; ASSESS w3) |
| Node-10 zero completion derived, not chosen | ELABORATING |
| All native tables block-positive | ELABORATING (ASSESS G4 to every type) |
| Native gate equals the table `cnot` exactly under the entry-dependent `pp` condition (§6.2); Φ⁺ and SWAP/2 tables both reachable under R-narrow by graded couplings, the wing-local cell swap and translations | ELABORATING (QP node 10, node 8, Lemma R) |
| QC-2: product-table failure for every parity supply, surviving premise I | ELABORATING (QP node 8 item 2 with node 10; LWE Discussion via QP). Strongest finding; not labelled NEW because it is a direct composition of two stated QP facts |
| §6.3: no local tomography relative to encoded product tests and native operations, through `pp` | ELABORATING (QP:557 relative parity readable; M2D's tomographic-completeness caveat) |
| QC-4 on every native state | CONFIRMING (QP node 10), with the undetermined-`pp` case added |
| ASSESS §7's posit list omits NNB | scope finding (not scientific) |

**Assumption-watch markers.**
- *A composite of a hidden-parity single-system mechanism inherits a hidden relative parity that product tests do not
  read and entangling couplings convert into product-test differences.* Any proposal reusing U′-type encodings for
  composites (Q-B, NNB work) should test QC-2's two-path pair.
- *Validity on native tests is supplied by any deterministic local model with wing-local reads.* A validity pass is
  uninformative about quantumness unless paired with a selective comparison.

No NEW finding is claimed.

## 10. Verification scope

- **Probe** (generic objects only; exact sympy 1.14.0; `python3 -I`; imports no earlier probe; no OI rule,
  encoding, coupling or preparation is encoded): `probes/q868h_generic_checks.py`
  (sha256 `1977dfb8c6f1974dc0d4ff6f445485547c49dfece4dae6c6232c7927ccd70eb9`), output `probes/q868h_generic_checks.out`
  (`cd38be73aa74b26d62b4562e907773163a8b42a5399ef457f1869233327ff704`): 27 checks, 0 failures, exit 0.
  - A1–A3 named tables; B1–B4 the sign rule over 48 signed permutations and 72 two-correlator tables; C1–C3
    full-ball product values with a negative control; D1–D2 CNOT conjugations; E1–E2 partial transpose as the
    Y-row sign flip (generic symbolic table); F1–F3 the comparator for QC-2's two paths, with a control; G1–G3 the
    Mermin–Peres identities; H1–H2 Z/X completions, with a control; I1–I4 cube-vertex mixtures; J1 body membership.
  - Run 1 (`q868h_generic_checks.run1.out`, `4a43977b…dfcb1`) and run 2 (`.run2.out`, `6296f936…e6f6`) had 26
    checks, all passing.
    - Between runs 1 and 2 two control labels (F3, I4) were reworded to state what they check; no check changed.
    - B4 was added for run 3. No expectation was changed.
- **Probe r2** (same scope and rules; imports only `sympy`, `itertools`, `sys`; imports no earlier probe):
  `probes/r2_generic_checks.py` (sha256 `ad8285ecb355dd8b6e1091eecb2b79209754da7fd68dd03fa8ad85c02d45b29a`), output
  `probes/r2_generic_checks.out` (`b0f9950af596b4d160f4909a252af274df6480645f6a647a8c319f6136dbcda8`): 20 checks,
  0 failures, exit 0; a second run is byte-identical.
  - R1a–d the comparator's `CNOT (H ⊗ I)|00⟩` table, Φ⁺ PSD, SWAP/2 at −1/2, and `⟨XX⟩ + ⟨YY⟩ + ⟨ZZ⟩ ≤ 1`; R2a–e the
    QC ⇏ (C) product-state witness, with a control; R3a–b the P1-removed herald outside the ball and the comparator's
    `±e_x`; R4a–c CHSH with Pauli settings over the 60 two-qubit stabilizer states (generated by the Clifford action
    on `|00⟩`) and the `2√2` operator; R5a–c the `hH2` witness, with a control; R6a–c the comparator's CNOT signs on
    all 15 Pauli products.
  - Run 1 (`r2_generic_checks.run1.out`, `3a380ff6…0428ec`) failed R1b and R2a: the eigenvalue helper dropped
    multiplicities. The helper was fixed; no expectation changed. Run 2 (`.run2.out`, `f1146443…b8f908`) had 19
    checks, all passing. R1d was added for run 3; the other 19 lines are unchanged.
- **Hand analysis (A):** §§2–7. The native preparations were enumerated by hand from QP's stated operations. No
  script enumerates, simulates or encodes them. The F₂ facts (`Q*`, `ω` on `E₂`, the pullbacks) are hand
  computations from QP's stated formulas.
- **Read in full:** QP `DESIGN.md`; ASSESS-868 r3a; REVIEW-868-r3.
- **Read in part:**
  - AP1 §3.1, §3.4 ledger, §4.1–4.7, §5.1 table (:275-310, :411-421, :462-700, :815-840);
  - QP PROOF-RECOVERY head and §1;
  - M1D §2.3–2.6 and node 1 (:320-505);
  - M2D §0 (:50-135) and the grep hits for C-COMP, Bell and tomography;
  - MI1 RESULT §0 and node 5 (:30-60, :340-360), and its DESIGN head;
  - Main:218 and :564 in full, and §3.3 (:360-412);
  - kernel declarations located at `fd539e15`: `lor_toOp_of_maxCone` (CompositeDimension.lean:1049),
    `lor_pair_bound` (:877), `no_candidateCone_cnot_reflY` (K2Guard.lean:143),
    `pairCone_eq_Q3_of_drive_maxCone` (EqvK2MaxCone.lean:153), `pairCone_eq_Q3_of_sharp_available` (:204),
    `maxConeOf` (EffectSpace.lean:411). Statements were read, not rebuilt.
- **Not read:** `two-system-interface.md`, `correlation-recombination-20261107`, LWE first-hand (QP's reading is
  relied on), the feedback/control RESULT, M2D nodes beyond §0, and the book. Negative statements are bounded by
  this list.
- **Source file hashes** (as extracted from `fd539e15`):
  - QP DESIGN `11d89c04…32b9`;
  - AP1 `dd13bf29…0c`;
  - M1D `7071f5e2…9667`;
  - M2D `9451b6ac…353`;
  - MI1 DESIGN `f2e15276…0f47`, RESULT `4ef745c2…af52`;
  - Main `6144cd4a…6366`.

## 11. Stops and owner questions (neutral)

**Stops, with what is missing.**
- **S1.** Without NNB, the U′ Y read and `S`, `H` are not supplied. The Y read needs a mixed-sector record, and Lemma
  G1 forbids one under graded couplings. NNB is a supplied conditional premise, not adopted.
- **S2.** Non-Pauli product tests are not supplied (J6; #867). Operational validity at full-ball scope cannot be
  tested.
- **S3 (closed).** Under R-narrow, `pp` is determined by a carrier–carrier coupling followed by QP's wing-local cell
  swap on each wing (Lemma P, §2.3).

**Owner questions.**
1. **NNB in the Q-868-H setting.** ASSESS §7's posit list omits NNB, which U′'s Y read, `S` and `H` contain. This
   unit carried NNB with QP's status and reported tier N separately (§6.5). Should later work on #868 carry NNB
   explicitly, or restrict to tier N?
2. **Cross-wing coupling scope.** Should "couplings between the wings' carrier cells" (ASSESS §7) include the parity
   cells (R-wide)? No outcome and no witness depends on the answer: R-narrow reaches every witness through Lemma P
   (§2.3). The answer fixes only the wording of the access in later #868 work.
3. **Recording.** After fresh review, should #868's planning block record the scoped result? That result is: (V)
   holds on native Pauli product tests under SA-1(a), P3 with (iv), E-iso and WL; (C) holds conditionally on supplied
   posits; and QC fails for U′ composites (including under premise I).
   Recording it would be a planning change only, with no status change.
