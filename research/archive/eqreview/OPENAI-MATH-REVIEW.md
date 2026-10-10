# Review of the "OpenAI Math vs. Incompleteness" comparison

Side review. No repository change, round or adoption follows from it.

**What was read.**
- **openai/math.** A read-only shallow clone of the public repository at `/home/user/openai/math`. HEAD is
  `fd4aeeb2ee4f…`, the commit the comparison names. Its contents were treated as untrusted data: read with
  grep/sed, nothing executed.
- **Incompleteness.** The certified base `bcbc516f` (read-only archive).

## Verdict

- **Facts.** The comparison's factual claims check out at the stated commits.
- **Comparator.** The recommendation to add a statement-comparison check is sound and genuinely additive. Its value is
  statement fidelity, not axiom checking: the repo already enforces the same three-axiom rule.
- **Overstated.** "Family 271 is the most promising immediate opportunity for H∞" is overstated for this programme.
  Family 271 is continuous-time Hamiltonian dynamics and KMS equilibrium on a represented algebra. That is structure
  Incompleteness deliberately does not claim, and it sits off the critical path; see the H∞ review.
- **Useful finds.** Two narrow items are worth acting on, by checks rather than migration (§3).

## 1. Facts checked

**openai/math, at `fd4aeeb2`:**

| claim | finding | source |
|---|---|---|
| 719 manuscripts in 372 families | confirmed | `README.md` |
| 300 formalized top-line results (~42%) | confirmed: "300 / 719 = ~42%" | `history.md`, October 7, 2026 |
| Results published at several stages of verification; unformalized ones may have issues | confirmed, nearly verbatim | `README.md` |
| 3 withdrawn on October 7 after a sign error; 14 revised | confirmed. A sign error in "Algebraicity of Weil classes on split abelian eightfolds" invalidated a stabilization-trace cancellation argument and constructions used by two dependent papers. Also: 14 papers revised, 13 citation updates, 6 new formalizations | `history.md` |
| 722 initially | consistent (719 + 3), but not stated as such in `history.md` | — |
| Lean v4.34.1 and many dependencies | confirmed. Mathlib is pinned at commit `d13f23b7`, alongside about 40 other packages. The Lean tree under `lean/OAI` is about 122k files and 26M lines | `lean/lean-toolchain`, `lean/lake-manifest.json` |
| Comparator framework, and the Heisenberg configuration | confirmed. It uses `leanprover/comparator` with `landrun` and `lean4export`. `Heisenberg.json` names a challenge module, a solution module, one theorem and the permitted axioms {propext, Quot.sound, Classical.choice}. The 218-line reference file contains one `sorry`, as a specification | `lean/ComparatorChallenges/` |
| Families 271, 280, 287 and 325 | the scope descriptions match the per-family notes | `lean/docs/{271,280,287,325}.md` |

**Incompleteness, at `bcbc516f`:**

| claim | finding |
|---|---|
| Lean v4.33.0 | confirmed. Mathlib is pinned to the tag `v4.33.0`, the only dependency (`verification/lean-mathlib/lakefile.toml`) |
| Thousands of axiom-checked declarations | confirmed: the certified gate reports 5860 `#print axioms` lines |
| Frozen statements, census, coverage and axiom checks | confirmed: `tools/lean_axiom_check.py`, `tools/lean_manuscript_census.py` (§A.35), `tools/coverage_check.py`, and the freeze comparisons in the round controls |
| No independent statement-comparison check | confirmed. "Comparator" in the repo refers only to protocol-shadow comparisons in the infrastructure rounds |

## 2. Where the comparison overreaches

1. **Family 271 does not match OI's adopted scope.**
   - **The algebra.** The Heisenberg reference statement builds its quasilocal algebra as the norm closure of
     single-site matrix units represented on ℓ² of finitely supported configurations: one fixed representation.
   - **The dynamics.** `finiteDynamics` is exp(itH_Λ), and its infinite-volume limit is taken in continuous time t ∈ ℝ.
   - **The main result.** Existence of KMS equilibrium states.
   - **Incompleteness's position.** Its Level III selects no representation and has discrete time. A continuous-time
     generator is proved not to be determined by the discrete dynamics (`continuous_extension_not_unique`), and both the
     continuous-time generator and representation selection are listed as "Deliberately not prioritized".

   The nearest live H∞ item is the two-way characterization with finite-support operations, and it needs neither.

   One real link does exist. For a fixed site space, the Heisenberg `QuasiLocal` should satisfy the axioms of
   Incompleteness's `QuasilocalSystem`: unital injective *-homomorphisms from the region matrix algebras, compatible,
   commuting on disjoint regions, with dense union. If so, `canonEquiv` makes the two independently developed algebras
   canonically *-isomorphic. That would cross-validate the two formalizations; it would not close any obligation. It is
   expected, not checked, and it needs a toolchain port.

2. **Families 280, 287 and 325 are described accurately but have little bearing on current obligations.**
   - **280** (conformal nets) belongs to the long-range QFT branch.
   - **287** (free group factors) lies on no path.
   - **325** (Crouzeix) gives operator-norm bounds for functional calculus. The one H∞-adjacent missing lemma, the
     instrument audit's Q2, needs the positive-map bound ‖Φ‖ = ‖Φ(1)‖ (Russo–Dye type). Searching for "Russo" finds
     only Russo's formula in percolation.

3. **No shortcut for the real bottleneck.** Track B (Theorem A′) needs the closed-subgroup theorem, Yamabe, and the Lie
   correspondence. A search of the OAI Lean tree finds no closed-subgroup theorem and no Yamabe by name. `LieGroup`
   occurs in 763 files, but nothing I found supplies these results. This is search-level evidence, not exhaustive.

## 3. Narrow finds worth acting on (checks, not migration)

1. **`Matrix.PosSemidef.kronecker`.** openai/math uses it by dot notation with no local definition (for example
   `OAI/InformationTheory/Entanglement/Coherence.lean:39`), so it is a Mathlib lemma at their pin. Track A's
   Pauli/twin package needs exactly this: Kronecker products of PSD matrices are PSD. **Checked afterwards: it is
   present at the `v4.33.0` pin** as `Matrix.PosSemidef.kronecker` (`Mathlib/Analysis/Matrix/Order.lean:213`, over
   `[RCLike 𝕜]` with `[Finite n] [Finite m]`, alongside `PosDef.kronecker`), in the local source tree at tag
   `v4.33.0` = `db584cd6`. Grep only; not compiled. So no port is needed for this lemma.
2. **Comparator, as a statement-fidelity check for flagship theorems.**
   - **What it adds.** An independently written, small reference statement, certified by kernel replay to be exactly
     what the implementation proves.
   - **Where it would have caught a real error.** In the §A.34 incident, the manuscript said "iff" where the kernel
     proved uniqueness. A reference statement written from the manuscript's claim would have had no matching proved
     theorem, so the comparator check would have failed.
   - **Candidates:** `three_of_nativeGate` (CompositeDimension:2748), `oiPlus_iff_qm` (CarrierGeneralOIPlus:207), and
     the K2 classification once it exists (in its operational form, per D1).
   - **Two precisions:**
     - Comparator matches constants. "Independent reference definitions" therefore means the reference owns the
       definitions and the implementation proves the reference theorem through a bridge. For the bespoke definitions
       (`W d`, `NativeGate`, …) that bridge is real work.
     - The tools (`comparator`, `landrun`, `lean4export`) would run in CI (§A.40). Keep it design-only, as the comparison
       itself suggests.

## 4. The external-review entry point

The idea is sound. Three points:
- **Partial pieces exist.** The ROADMAP's "Programme interpretation boundary", the K section's finite-route diagram, and
  "Declared inputs and conditional hypotheses" already cover parts of it.
- **Repo minimalism (§A.28).** A new file must be needed, maintained and process-free. That favours a section of the
  existing landing page (`verification/README.md`) generated from a maintained source, over a new document.
- **Timing.** The "derived versus assumed premises" table is what the EQ2 comparison will produce. Writing it before the
  three tracks report would mean rewriting it at once.

## 5. Agreed

- The unit counts are not comparable: top-line results versus declarations.
- Neither formalization nor governance replaces independent review. Internal work moves consistency, not correctness
  (§A.23).
- The October 7 cascade is a fair illustration of why dependency tracking matters.
