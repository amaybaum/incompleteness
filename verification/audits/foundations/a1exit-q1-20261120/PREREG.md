# A1-EXIT Q1 — lattice restrictions: preregistration

**Status.** Paper-only research record, preregistration. Written and pushed before any consumer is
classified. No manuscript, Lean or registry edit; no premise adoption; no merge. A1 (Main posit
ledger item (ii)) and A4 (`papers/Substratum.md`:98) are unchanged.

**Authorization.** Owner `amaybaum`,
[#1169 comment 7047514209](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7047514209),
2026-11-20, Step 1 table, row Q1: "lattice restrictions (#1454 P2-Q1) | A4's finite periodic
lattice, and the fermion theorems on ℤ^d (Theorems 2, 3, 8, 8b, 10, 12, 13; SM:539; SM:1536) |
Prove the applicable extension, identify weaker lattice requirements, or keep a finite-only
restriction | Paper-only research record". The four safeguards of that record apply: no disguised
A1; no forced proof; no silent promotion; no premature deletion.

**Goal link (§A.47).** #1454 row P2-Q1, serving the owner's A1-exit objective (#1169 comment
7047514209). This unit decides, for each named consumer of A4's lattice clause, whether it holds on
`ℤ^d`, on which periodic quotients it holds, and which manuscript sentences Step 2 would have to
correct. It does not decide A4's final form, which belongs to the A1-EXIT ledger and a later owner
decision.

**Source pin.** `main` at `9db518844df62151979acf6aac1d487b59c44907` (the merge of #1460). `SM:n`, `Sub:n`,
`Main:n` are lines of `papers/SM.md`, `papers/Substratum.md`, `papers/Main.md` at the pin. O-A4 is
`verification/audits/foundations/o-a4-20261120/RESULT.md`; A1-PHASE2 is
`verification/audits/foundations/a1-scope-phase2-20261120/PREREG.md` (§12–§14).

## 1. Notation

SM:222 already declares the carrier `Λ = ℤ^d` and says that under A1 and A4 the bijection acts on a
finite periodic quotient of `Λ`. To avoid a clash with that `Λ`, this record writes the **period
lattice** as `P ⊂ ℤ^3` (the brief's and O-A4 §7's `Λ`) and the quotient carrier as `X_P = ℤ^3/P`.
`P = 0` is `ℤ^3` itself. `P̄` is the image of `P` in `𝔽_2^3`. `D_3 = {b : b_1+b_2+b_3 even}`.
A corner is `η ∈ {0,1}^3`, with character `χ_η(n) = (−1)^{η·n}`.

## 2. Consumers (fixed before classification)

**Primary consumers (named by the authorization and by A1-PHASE2 §12).**

| ID | Site at pin | Content used |
|---|---|---|
| C2 | SM:286 Theorem 2 | staggered phases, `D_st^2 = −¼□_lat` |
| C3 | SM:302 Theorem 3 | parity sectors, opposite-parity hopping |
| C8 | SM:434 Theorem 8 | eight corners, four taste pairs, action of `O` |
| C8b | SM:440 Theorem 8b | corner couplings `μ(η) = σ(η)/d` |
| C10 | SM:456 Theorem 10 | three triplet tastes "related by cubic symmetry, hence degenerate" |
| C12 | SM:535 Theorem 12 | checkerboard = staggered ε-grading (spin⊗taste reconstruction) |
| C13 | SM:543 Theorem 13 | visible-sector grading identity, Schur complement over the hidden sublattice |
| C539 | SM:539 Remark | bipartite structure (already conditioned) and the spin–taste sentence |
| C1536 | SM:1536 | "bipartite checkerboard structure" among the substratum's exact discrete symmetries |
| CA4 | Sub:98 (A4), with SM:202, SM:222, Sub:157 | "finite periodic lattice, the quotient of a rank-`d` lattice by a finite-index sublattice" |

**Secondary consumers (corpus census).** `checks/q1_census.py` lists every line of `papers/*.md`
and `book/*.md` that matches one of five pattern families: G4 (A4's finite class: "finite periodic
lattice", "periodic quotient", "finite-index sublattice", "period lattice"), G1 ("bipartite",
"checkerboard"), G2 (Brillouin-zone corners, "2^3 = 8", "staggered phase", "staggered-to-Dirac"), G3
(`O_h`, "cubic symmetry", the group `O`), and the theorem labels of the primary consumers. At the
pin it finds 216 distinct lines (G4 13, G1 51, G2 31, G3 95, labels 54; families overlap); the list
is `checks/q1_census.json`. Each hit receives one disposition in RESULT.md:

- **R** (restates): the line asserts on the substratum lattice one of bipartiteness, the existence
  of the eight corners or the staggered blocking, a cubic symmetry acting on the carrier, or A4's
  finite class. It takes the class of the primary consumer it restates, and is a correction
  candidate if it carries no condition the class needs.
- **I** (inherits): the line uses a primary consumer's conclusion by citation, or uses tastes or
  sectors as emergent labels. No separate correction unless the cited consumer is corrected in a
  way that changes the citing sentence's truth.
- **S** (stencil or abstract): the line concerns the local stencil on `ℤ^3`, an abstract graph (for
  example SM Proposition 20's `C_4` ring), a point group as abstract algebra, or the observer-level
  isotropy results of SM §3.1/§4.1 already classified by O-A4 rows 13–16. Not a Q1 consumer;
  O-A4's classification stands.
- **N** (unrelated): another sense of the word ("bipartite entanglement", Structure's or Main's own
  Theorem 2, Juno's own theorem numbering, bibliography).

## 3. Classification rule (fixed before classification)

Each primary consumer receives two verdicts.

**Verdict on `ℤ^3` (or `ℤ^d`).**
- **(i) holds on `ℤ^d`** iff every step of its proof is valid on `ℤ^d` with the same local data:
  identities between finite-range operators acting on all functions `ℤ^d → R`, kernel theorems
  quantified over an arbitrary index type, Fourier analysis on the continuous Brillouin torus, or
  representation theory of a finite point group that acts on `ℤ^d`. The proof or kernel citation is
  given, with its layer: **[L]** kernel theorem (cited, not built here), **[E]** exact algebra or
  exact finite computation in `checks/`, **[W]** paper derivation.
- **(iv) open** if no such proof is found and no countermodel either.
- **(iii) finite-only** iff some step needs a finite site set or configuration space (finite trace,
  normalized counting measure, finite determinant, finite order) and a documented recovery attempt
  (Code Review Rules, "theorem recovery before concession") finds no replacement. Failure to recover
  is recorded as (iv), not as disproof, unless a countermodel on `ℤ^d` exists.

**Verdict on periodic quotients `X_P`.**
- **(ii) holds on a stated class** `W = {X_P : P satisfies Q}`, with `Q` stated as an iff where the
  consumer's lattice content is a character or symmetry condition, and otherwise as a sufficient
  condition labelled as such. Each `Q` is tested on at least one lattice that satisfies it and one
  that fails it, by exact computation.

**Disguised-A1 test (safeguard 1).** A class `W` passes iff
- (DA1) `W` contains a carrier whose configuration space is infinite: `P = 0` must satisfy `Q`
  (kernel: `WaveSubstratumUnbounded.waveZ_not_A1`, `verification/lean-mathlib/OIBridge/`);
- (DA2) `Q` constrains only the period lattice's parity or symmetry and implies no bound on the
  number of sites or configurations;
- (DA3) `Q` is the condition the consumer's proof uses, not a finite-index condition added beside it.

**Productivity test (§A.31).** The unit is a gem iff it yields, for at least one consumer, a lattice
condition strictly sharper or strictly different from O-A4 row 18's blanket "`Λ ⊂ 2ℤ^3` for the
corners, even-sum for the checkerboard", with a countermodel or a proof, or locates a finite-only
step. Otherwise it is relabelling and is recorded as such.

## 4. Controls (§A.41 invariant → checkpoint)

| ID | Invariant | Checkpoint |
|---|---|---|
| K1 | Positive control: Theorem 3 holds on `ℤ^d` and must come out (i) | Kernel `ChiralCenterRecovery.scalar_center_chiral_iff` is quantified over an arbitrary type `X` with a parity map and both parities present; `checks/q1_checks.py` verifies on a window of `ℤ^3` that nearest-neighbour hopping is odd-supported for the coordinate-sum parity |
| K2 | Positive control: the staggered generator relations of Theorem 2 hold on `ℤ^3` | `q1_checks.py` verifies every field of `Staggered.Gens` (`verification/lean/OI_Staggered_Relations.lean`) as local identities at every site of a window of `ℤ^3`, and the kernel of `(Σ_i A_i)^2` against the two-step stencil |
| K3 | Negative control: O-A4's countermodels reproduce | cubic tori `L = 3, 5`: not bipartite, 1 corner of 8; `L = 4, 6`: 8 corners; skew even-sum quotient `⟨(4,0,0),(0,4,0),(1,1,4)⟩`: bipartite, 4 corners; cubic torus `L = 4`: vertex stabilizer of order 720, `L = 6`: 48 (O-A4 §7.1, §7.2, §11 D–E) |
| K4 | Negative control: odd cubic tori do not carry the staggered relations | `q1_checks.py` finds a failing `Gens` field at `L = 3, 5` (as `verification/lean/staggered_relations_probe.py` S6) |
| K5 | The disguised-A1 test is live | The class "finite-index `P` with `P ⊂ 2ℤ^3`" must fail DA1; the class "`P ⊂ 2ℤ^3`" must pass |
| K6 | Paper-only scope | `git diff --stat` against the pin lists only files under this directory |

If K1–K5 do not all hold, no verdict is printed: the checks script exits non-zero and RESULT.md
records the failure instead of classifications.

## 5. Planned exact checks (bounded; stdlib Python; well under 30 min CPU)

- **A** Corner characters, checkerboard and staggered phases on `X_P` for the cubic tori
  `L = 2..6`, rectangular tori with sides in `{2,…,6}`, and skew quotients, compared with the
  closed-form conditions (`χ_η` defined iff `η·b` even for `b ∈ P`).
- **B** The `Gens` relations as matrices on tori and as local identities on a `ℤ^3` window (K2, K4).
- **C** Graph automorphisms (vertex stabilizers) of selected quotients and their action on the
  corner characters: whether some automorphism maps the `X_1` corner line to the `X_3` corner line.
- **D** Hypercube blocking `n = 2y + η` on `X_P`: well defined or not.
- **E** Cubic-invariant period lattices by exhaustive Hermite-normal-form enumeration to a stated
  index bound.
- **F** Corner couplings `σ(η)/d` as eigenvalues of the normalized neighbour average on `X_P`.

The verdict of each check is the script's exit status; printed lines are diagnostics (§A.44).

## 6. Decision rule for Step 2 corrections

A correction is proposed for a manuscript sentence iff (a) the sentence asserts a consumer's
conclusion on a carrier class that the manuscripts admit (`ℤ^3` by SM:222, or a finite periodic
quotient by A4), and (b) the verdicts above show the conclusion false on part of that class, or
its proof invalid there. The proposed text is the minimal condition that makes the sentence true,
stated in the paper's register. Corrections are proposed, not applied. A sentence that is true on
the admitted class gets no correction, whatever its wording.

## 7. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7047514209 | Authorization | Provenance; quoted with author |
| #1454, #1450, #1441 | Accountable Issue; routing source; O-A4's review | Provenance; the content used (O-A4, A1-PHASE2 §12–§14) is on `main` at the pin |
