# Stage-3 integration note — the self-dual-cone uniqueness problem Q-SD (research only; L = `9f9f8257`)

Written by the coordinator after auditing threads U (`pt/U/`) and X (`pt/X/`) and the review thread NS
(`pt/audit/reviews/NS/`). Governing texts: `PROTOCOL-STAGE3.md` (`1a649168…`), `PROTOCOL-NS.md` (`4f61891f…`), and the
stage-1/2 protocols they name. Holds unchanged: no repository change, branch, PR, CI run, governed round or
publication. Evidence levels as in the protocols: [K] certified at L, [D] design module, [W] written argument, [X]
exact computation, [N] numerical, [L] unverified literature.

## 0. Bottom line

**Q-SD is EXOTIC, at level (i) and at level (ii).** The hypotheses H1 (every product state `prodState x y`, `x, y` in
the closed ball), H2 (`cnot`-invariance; at level (ii) invariance under the whole even native class, the order-16
group `⟨cnot, Ad(Z⊗I), Ad(I⊗Z), transpose⟩`) and H3 (`K = dualW K`) do not force `K = Q3`. Exact countermodels:

| cone | defect set `Z` | level | `K ∩ V+` | found by |
|---|---|---|---|---|
| `K(E0) = (Q3 ∩ E0*) + ℝ₊E0` | `{E0}`, `E0 = E00 + E13 − E22` | (i) | exotic (contains `E0`) | U (`K★`), X (`K1`) |
| `K(Z_F)` | the four Bell-type defects `(E00 + s₁E13 + s₂E22 − s₁s₂E31)/4`, orbit of stage 2's `F` | (i) and (ii) | exotic | U (`K_F`), X (`K4`) |
| `K({F, cnot F})` | `F = E00/2 − T_ψ/4` and its `cnot` image (orthogonal) | (i) | exactly `Q3 ∩ V+` | U (`K_F2`), X |
| `K(e_c)`, `e_c = E00 + c(E13 − E22)` | one defect, `c ∈ (1/2, 1]` | (i) | exotic | X |

Every cone is `(Q3 ∩ Z*) + cone Z` for a finite set `Z` of pairwise `ipW`-orthogonal, `cnot`-permuted tables outside
`Q3`, each with exactly one negative eigenvalue `−a` and all other eigenvalues `≥ a` (the exact condition for the
surgery to be self-dual: X's characterization; U's projection lemma). H1 holds by symbolic sum-of-squares identities
over the whole ball (never a finite test); H2 and the level-(ii) group exactly; H3 by two independent written
proofs (U's Theorem S, X's SD1/SD2) over exact certificates. Each cone contains a non-positive table and misses a
pure state (`G` for `K(E0)`, `T_ψ` for the Bell-type cones), as the owner's incomparability consequence requires;
the witness pairs are Gaussian-rational. The two threads never read each other and converged on the same
construction, the same seed (`F` is one of the four Bell-type defects) and the same level-(ii) obstruction
(`⟨E0, Ad(Z⊗I)E0⟩ = −1`: no level-(ii) cone contains `E0`).

**Audit status.** Replays: 16 of 16 thread scripts reproduce stdout byte for byte. Independent exact check written
without either thread's code: **25/25 CONFIRMED** (`pt/audit/X/indep_checkQSD.py`, run 4; a concurrent execution byte-identical on stdout and stderr; runs 1–3 kept, each failed on a harness error of the coordinator's own, listed in AUDIT-X). Written
proofs reviewed step by step with no gap found: SD1, the self-duality characterization, SD2, Theorem S with its
pure-state reduction and the exact projection identities, the local Wigner theorem (two independent proofs, U by
slices and a cross ratio, X by Jordan maps and a Clifford triple), EBF, the decomposability exclusion. One missing
argument was supplied (IE1 fails for `K(Z_F)`); one minor procedural breach was recorded (X's temporary file outside
its directory, hash lines only, deleted, no effect). Details: `pt/audit/X/AUDIT-X.md`, `pt/audit/U/AUDIT-U.md`.

**What it means for the programme.** Self-duality is not the selecting principle. The certified pair data plus
self-duality, even with the full even native symmetry, admits non-quantum state spaces. Any derivation of `Q3` from
embedded observation must add a premise that fails on the exotic cones. The audited class results say which
premises would do it, and which would not:

| premise added to H1–H3 | outcome | evidence |
|---|---|---|
| homogeneity (the automorphism group acts transitively on the interior; symmetric cone) | UNIQUE-IN-CLASS: only `Q3` | [W + L: Jordan–von Neumann–Wigner] (X); every exotic cone is non-homogeneous |
| `K` a linear (or `ipW`-orthogonal) image of `Q3` | UNIQUE-IN-CLASS | [W + X] orthogonal (both threads; local Wigner proved); [W + X + L: `Aut(PSD₄)`] linear |
| local-unitary invariance (flagged: local operations on entangled states) | UNIQUE-IN-CLASS | [W + L: Schmidt] (X); IE1 fails on every exotic cone |
| `cnot`-invariance, even-class invariance, closedness, admissibility, self-duality | none selects | the exotic cones satisfy all of them |
| decomposability, Lorentz type | NO-EXOTIC-IN-CLASS (no member satisfies H1–H3 at all) | [W + X] |
| spectrahedrality (`{w : M(w) ⪰ 0}`) | not settled | `K(E0)` is a spectrahedral shadow; whether it is a spectrahedron is open |
| the commuting torus `actC Rz ∘ actT Rx` (flagged) | exotic members exist, none exhibited | [W: EBF, non-constructive] |

**Route refuted.** "Uniform pair self-duality (with the certified pair hypotheses and the native gate) ⇒ FCC", and
"⇒ IE1", are refuted exactly: for uniform `K(E0)`, `fourVal(E0, E0, cnot p(e2,e3), cnot p(e1,e2)) = −1`; for uniform
`K(Z_F)`, `−1/2`; `Ad(Z⊗I)` carries `E0` out of `K(E0)` and a generic local rotation carries each Bell-type defect out of
`K(Z_F)`. This closes stage 2's two self-duality rows (S3 §1.2 rows 7 and 9) and S2's self-duality lead as routes to
`Q3`. The four-token route (S3's SDC: P3 ∧ OVL4 ∧ CSD2) is untouched: OVL4 is a four-token principle that no pair
cone decides.

**The strongest warranted conclusion, in the owner's words and with its scope.** *The tested self-duality and
CNOT-invariance assumptions are insufficient to characterize finite-dimensional quantum mechanics uniquely.* Scope:
this is established at the level where the test was run — the two-qubit pair carrier `W 3` of the K programme,
with the certified product data (H1), the certified native gate and its even class (H2), and `ipW`-self-duality
(H3) — by exact countermodels, not by a general theorem about every carrier; and it narrows the equivalence problem
by naming assumptions that cannot select the quantum cone alone, without establishing which additional assumption
is necessary. Reproducibility (every script replayed byte for byte, including a concurrent replay of the
coordinator's check) and correctness (the written proofs reviewed, the independently implemented checks, the
convergence of two isolated threads) are separate layers of the evidence and are recorded separately in the audits.

**Labels (amendment 2), relative to L.** Q-SD: EXOTIC. The pair cone `Q3`, FCC and IE1 are INDEPENDENT of
`H1 ∧ H2 ∧ H3` and of `H1 ∧ H2(ii) ∧ H3` (valid countermodels: the exotic cones); stage 2 had them INDEPENDENT of the
certified premises alone, so the independence survives adding self-duality and the even-class symmetry. No label
of the certified corpus changes. Bands unchanged (consistency-axis work).

## 1. The construction and why it is hard to vary

The surgery `K(Z) = (Q3 ∩ Z*) + cone Z` has one free choice, the defect set `Z`, and the exact self-duality
condition on a single defect is a trichotomy (X): `e ⪰ 0` (then `K(e) = Q3`), or exactly one negative eigenvalue
`−a` with the rest `≥ a` (exotic), or neither (not self-dual, with an explicit witness `uu†`, `u = (g + f)/√2`). The
countercontrols fail exactly where the condition fails: `e_{3/2}` (second eigenvalue below `a`), the partial
transpose of a non-maximally entangled pure state (U's `(ψψ†)^Γ`, `ψ = 2|00⟩ + |11⟩`), the scaled defects
`(I − 3P_s)/8`, non-orthogonal orbits (U: `{aE00 ± E13 ± E22}`, refuted for every `a ∈ (√2, 2)` at the instance
`a = 3/2`), and defects not fixed or permuted by `cnot` (`Y1 = E0^Γ`, `F` alone). H1 holds for the exotic cones by
closed-form identities (`ipW(E0, prodState x y) = 1 + x₁y₃ − x₂y₂`, twice which is a sum of squares plus
`(1 − |x|²) + (1 − |y|²)`), so nothing was tuned to the 36 axis products.

**Equivariant Barker–Foran (X, [W], confirmed).** For a compact group `G` of `ipW`-orthogonal maps with a nonzero
fixed vector, every closed `G`-invariant subdual cone extends to a `G`-invariant self-dual cone. So the "extension
can stall" worry of AUDIT-S3 cannot occur for `cnot`, the even class or the torus (all fix `E00`); the content of
the uniqueness question lies entirely in the seed, never in the extension step. U reached the same reformulation
("a maximal invariant self-positive cone is self-dual iff its dual lies in `{y : ⟨y, cnot y⟩ ≥ 0}`") and used it to
find the seed `(Q3 ∩ E0*) + ℝ₊E0`.

**The `V+` reduction is not decisive.** `K(E0) ∩ V+` is an exotic self-dual cone of `V+ ≅ Herm(3) ⊕ ℝ` containing
`K_gen+`, and `K({F, cnot F})` has `K ∩ V+ = Q3 ∩ V+` exactly while `K ≠ Q3` (its exotic content lies in the `V−`
fibres). So neither direction of the owner's ten-dimensional reduction can settle Q-SD.

**Necessary conditions on any `K` satisfying H1–H3** (U, exact): `K ⊆ K_E ∩ {y : ⟨y, cnot y⟩ ≥ 0}`, and this is a
proper restriction of the corridor `K_gen ⊆ K ⊆ K_E` (`Y1 = E0^Γ ∈ K_E` has `⟨Y1, cnot Y1⟩ = −1`). A cone containing
`E0` misses exactly the open `E0`-cap of pure states.

## 2. Consequences for the stage-2 standing picture

- **S3 (composition consistency).** Rows 7 and 9 (self-duality as a route to FCC/IE1): route refuted. The [L]
  step in ORTH.W ("hence `Ψ ∈ Aut(Q3)` up to partial transposes") is now proved [W + X], twice. The SDC route is
  unchanged.
- **S2 (pair system from data).** The self-duality lead (D1's closure through `K = K*`) is closed negatively; the
  witnesses `E0`, `F`, `G`, `T_ψ` keep their audited roles and now sit inside exact cones.
- **DS (double slit).** Unaffected in content; its composite-level statements that rest on the pair cone being `Q3`
  keep that as an assumption, which stage 3 shows is not supplied by self-duality.
- **The owner's three consequences and two technical points** (witness-pair form; `V+` reduction; the corridor with
  positive `E00`-component and the compact trace-one section; finite axis tests as a bound only; Gaussian-rational
  witnesses): all confirmed exactly and all used by the threads' certificates.

## 3. What remains, and candidate next targets (nothing launched; for the owner's decision)

1. **The selecting premise.** The sharpest positive statement available is UNIQUE-IN-CLASS for homogeneous cones:
   `Q3` is the only *symmetric* cone satisfying H1–H3 [W + L]. An observer-native source of homogeneity at the pair
   level would close the cone question; the single-system analogue in the corpus is the transitivity premise that
   gives the ball (TRB-1's `BoundaryTransitive`, [K]). Whether a pair-level transitivity is derivable from embedded
   observation, or is a new principle, is an Origin-type question. Candidate target, not a result.
2. **The [L] inputs.** The homogeneous-cone row rests on the Jordan–von Neumann–Wigner classification; the
   linear-image row on `Aut(PSD₄)`; the LU row on Schmidt. These are classical theorems; if the owner wants the rows
   at [W] they need a written reduction or a Mathlib anchor (none located in this session).
3. **Open mathematical questions, low priority for the programme:** whether every exotic cone is a surgery; whether
   any is a spectrahedron; an explicit torus-invariant exotic cone (exists by EBF).
4. **The owner's direction at the gate (note 4): the next target is an EXOTIC exclusion theorem** — the
   observer-native principle that rules out the surgery cones while retaining `Q3`, with its necessity tested by
   countermodels, and the minimum additional condition for a full equivalence proof identified. A draft protocol
   (Q-EX: a fixed candidate lattice of symmetry and structural conditions, each node to receive retention /
   exclusion / necessity / observer-nativity verdicts; two reductions to seed the threads — reachability of all
   pure states from products under the generated group ⇒ UNIQUE, and a maximally entangled state with overlap
   ≤ 1/2 to the reachable set ⇒ EXOTIC via EBF; one-token full rotation symmetry already decided UNIQUE by the
   first reduction, pending exact checks) is held in the coordinator's drafts and is launched only after this
   archive, per the owner's order of work.
5. **Priority 2, Origin (queued, unchanged):** Discrete Origin (a substratum-sourced non-monomial coherent mixer with
   its preparation/reuse/readout protocol; Hadamard-sandwich witness) and Continuous Origin (the minimal
   repertoire's driven transition, `oiPlusMin_iff_qm`). Stage 3 sharpens their framing: the Origin question now has a
   second face — sourcing the selecting premise for the pair cone — beside sourcing the single-system coherent
   operation.
6. **Review thread NS** (`pt/audit/reviews/NS/RESULT.md`, audited in `pt/audit/NS/AUDIT-NS.md`; replays 3/3
   byte-identical; independent check 24/24). The supplied fluid/horizon analysis paraphrases the hydrodynamics
   programme faithfully but drops its gate (hypothesis L9: no singularity question before an explicit
   microscopic-to-continuum map). Its "precise OI mechanism" — regular finite approximants, a singular continuum
   limit, bounded energy — is generic: inviscid Burgers from `−sin x` blows up at `t = 1` while every
   energy-conserving Galerkin truncation is globally regular, and a fully observed finite bijective family has the
   same shape with nothing hidden; the route "that shape ⇒ hidden-sector transfer" is refuted exactly. The input
   runs together two notions of "hidden" (the complement of a coarse-graining map, which is Mori–Zwanzig's and the
   corpus note's own; and OI's observer-level hidden sector): an assumption-watch marker on the corpus's own note.
   H-B's closure failure (`hb3a_no_closure` [K]) is the generic H3 closure gap, also proved for the linear wave rule,
   not hidden-sector evidence. Mori–Zwanzig is already a certified corpus theorem (`mz_identity` [K]). The September
   2026 claims are not checkable at L and nothing depends on them. The framework-specific target is UNRESOLVED and
   not statable at L; the proposed test is not executable at L (no continuum map, no 3D carrier with a limit, no
   transfer functional, no known unforced singular profile). No corpus label changes. Keep: the forcing and
   dimension caveats, and the attribution-or-not target shape under NS's §3.4 controls (a closed-truncation control
   and a fully observed control are mandatory). Not launched and not proposed for launch: the hydrodynamics branch
   stays where its own programme puts it (H-C next, on the owner's carrier decision).

## 4. Evidence log

Thread records (unchanged since each thread's end; hashes re-verified by the coordinator):

| record | sha256 |
|---|---|
| `pt/X/RESULT.md` | `69ea7b3525bfd56f6b4f5fc5ac71fa88dd3abb23acdb13f07dc0e1d7b3fe38ba` |
| `pt/X/NOTES.md` | `88ea03fb15236709c22b6b81d419347cd982fc92fa79ce6c1099bca0f7b643fe` |
| `pt/U/RESULT.md` | `4999fef697ab086689ac39926f58d55222cce4b1b9d402e324933bf1df832f9d` |
| `pt/U/NOTES.md` | `40cc1e214ddb1b72d83ce276128ca04bb12eb47982b3b44ba7b27e61d504af34` |
| `pt/audit/reviews/NS/RESULT.md` | `8485f4f77ecb5485bc110e2d8ee59174de312b5ce42ab7423cddc031eb5f190e` |
| `pt/audit/reviews/NS/NOTES.md` | `f34b4314ca5725f838a3e8264840a7b0820eb4929e36d5356f12a20c3ba15706` |

Thread scripts: X eight (`x1`–`x8`, hashes in X RESULT §4, all 37 lines re-verified), U eight (`u1_struct` …
`u5_level2_N`, hashes in U RESULT §4, re-verified), NS three (`ns2`, `ns4`, `ns5`, hashes in NS RESULT §6,
re-verified). Replays by the coordinator: X 8/8, U 8/8, NS 3/3, stdout byte-identical (`pt/audit/{X,U,NS}/replay/`).
Kept failed runs: X `x5` run 1, U `u5_kf` run 1, NS `ns4` run 1 and `ns5` run 1, each a harness or own-claim error
caught by the thread's decision rule, each recorded in the thread's NOTES.

Coordinator's checks (decision rules in each header; run 1 kept where it failed on a harness error):

| script | result | runs | replay | sha256 (script / final out) |
|---|---|---|---|---|
| `pt/audit/X/indep_checkQSD.py` | 25/25 CONFIRMED | 4 (run 1 20/25: five harness errors; run 2 24/25: the countercontrol's predicted boundary, corrected to `t² > 3/7` by an exact derivation; run 3: a tuple-indexing crash in the corrected line; all listed in AUDIT-X) | identical (concurrent execution) | `518b4952…` / `cdd04849…` |
| `pt/audit/NS/indep_checkNS.py` | 24/24 CONFIRMED | 2 (run 1 23/24: one harness error, A5) | identical | `756d5e5f…` / `74082517…` |
| `pt/audit/stage3-inputs/qsd_owner_consequences.py` | 6/6 | 2 (run 1 harness) | identical | as recorded in OWNER-NOTE-STAGE3-AUDIT.md |
| `pt/audit/stage3-inputs/qsd_owner_note2.py` | 4/4 | 2 (run 1 harness) | identical | as recorded in OWNER-NOTE2-STAGE3-AUDIT.md |
| `pt/audit/reviews/coherence-note/povm_identity.py` | 4/4 | 1 | identical | as recorded in REVIEW-COHERENCE-NOTE.md |

Audit notes: `pt/audit/X/AUDIT-X.md`, `pt/audit/U/AUDIT-U.md`, `pt/audit/NS/AUDIT-NS.md` (hashes in the evidence
manifest). Owner notes received during stage 3, verbatim, under `pt/audit/stage3-inputs/`: `OWNER-NOTE-STAGE3-AUDIT.md`,
`OWNER-NOTE2-STAGE3-AUDIT.md`, `OWNER-NOTE3-ORIGIN-RUNGS.md`, `OWNER-NOTE4-STAGE3-GATE.md` (hashes in the manifest). Launch records: `pt/STAGE3-LAUNCH-LOG.md`, `pt/audit/STAGE3-RELAUNCH-LOG.md` (U launches 1–2 and X launch 1
aborted on an output-size error after the session model changed; markers kept under `pt/audit/aborted-launches/`;
the successful launches ran with the Opus model and a write-in-parts constraint).

## 5. Integrity

- Coordinator's checks at 12:57Z (before the audits) and 13:25Z (after NS's end): the six `pt/` manifests and
  `ns.manifest.sha256` OK; `pt/base` HEAD `9f9f8257a980a1819fbbc1dc0019917cf8678626`, status clean, no bytecode;
  the seven protocol hashes unchanged.
- Every thread's own start and end checks were green (X RESULT §5, U RESULT §5, NS RESULT §7); the directory mtime X
  flagged is U's creation; the three new entries NS observed under `pt/audit/` are the coordinator's audit
  directories; X's one procedural slip (a temporary hash list written one level above `pt/` and deleted at once) is
  recorded in AUDIT-X with no effect on any result. No anomaly; nothing quarantined.
- No repository write, branch, PR, CI run, GitHub call, network fetch or publication by any thread or by the
  coordinator during stage 3; git commands read-only. The holds stand.
