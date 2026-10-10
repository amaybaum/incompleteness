# Coordinator's audit of thread Z (COUNTERMODELS), stage 4 (Q-EX) — 2026-10-10, 16:00Z–16:20Z

Audited record: `pt/Z/RESULT.md` (`dca18d91…`, 318 lines), `pt/Z/NOTES.md` (`8d5e8815…`, 323 lines),
`.start_marker` (`a51825c9…`), the six exact scripts z1, z2c, z2e, z3, z4, z5 and the three [N] scripts z2a, z2b,
z2d with their outputs. Governing text: `pt/PROTOCOL-STAGE4.md` (`d3da2811…`), amendment-2 labels, the owner's notes
5 and 6. References fixed before Z reported: `PRE-AUDIT-QEX.md` (14:47Z) and `PRE-AUDIT-Z.md` (15:52Z,
`preaudit_z.py` 9/9). The four distinctions of owner note 4 are kept apart: reproducibility (§2), correctness
(§3–§4), run history (§2, §3), the strongest warranted conclusion (§6). Y and Z are evaluated independently (owner
note 6); their overlap is compared in §5 only after each stands on its own evidence.

## 1. Integrity (green)

- `pt/Z/` holds 54 files: the marker, NOTES, RESULT, nine scripts with `.out`, `.err`, `.replay.out`, `.replay.err`,
  and the two kept failed runs (Z's "55 entries" counts one more than the files present; every file Z names is
  present and nothing else is). The 26 distinct sha256 values quoted in RESULT §4 (nine scripts, nine
  outputs, the six kept failed-run files, NOTES, marker) re-verify with `sha256sum -c` (`z_listed_hashes.txt`, this
  directory): 26/26 OK. The 18 `.err` files of successful runs and replays hash to `28d3b9e8…` (`exit 0`); the two
  failed-run `.err` files hash as Z states (`4418fafe…` crash trace, `e55d5e90…` `exit 143`).
- Z's start (14:24:43Z), end (15:56:27Z) and post-write (16:00:28Z) checks are as recorded: manifests, base HEAD
  `9f9f8257…` with empty porcelain, protocol hashes and sidecars, no bytecode, sweep clean (only `Y/`, `Z/`, `audit/`
  newer than the marker, all excluded). Z read `pt/X/x7_numeric.py` (a stage-3 record, allowed) and
  `CompositeDimension.lean` at L for transcription; it did not read `pt/Y/`, `OWNER-*`, `audit/reviews/` or
  `audit/aborted-launches/`; it wrote only in `pt/Z/`. No git write, network, publication or sub-agent.
- The launch message's "eight protocol hashes" listed seven (coordinator's slip). Z took `PROTOCOL-NS.md`
  (`4f61891f…`) as the eighth and checked it by hash only, without reading it; harmless either way.
- Z's amendment record (NOTES N1) quotes the coordinator's message verbatim, and Z's own derivation of the CNOT
  decomposition preceded it (N1), as Y's did.

## 2. Reproducibility (distinct from correctness)

- **Z's own replays:** 9/9 byte-identical on stdout and stderr (`cmp` of `z*.out/.err` against `z*.replay.*`,
  re-run by the coordinator: 9/9 IDENTICAL).
- **Coordinator's replays** (`replay/`, 16:02–16:05Z, run from `pt/Z` as working directory with `python3 -I -B`):
  stdout and stderr 9/9 IDENTICAL to Z's originals (`REPLAY-LOG.txt`, `0d8dd2db…`). The three [N] scripts replay
  identically as well (fixed seeds), though they certify nothing.
- **Kept failed runs:** `z1_swap.run1.*` crashed on its summary line after all checks had printed (sympy booleans
  summed); run 2 coerced the flags and nothing else. `z2e_s2_surgery.run1.*` produced no output and was killed after
  ten CPU-minutes in a symbolic trigonometric simplification (exit 143); run 2 re-parametrized the circle rationally.
  Neither affects a result; both are kept with their reasons in NOTES N7–N8.
- **Coordinator's independent check** `indep_checkZ.py` (written without Z's code): run 2 29/29
  `INDEP-Z-CONFIRMED`, replayed byte-identically. Run 1 (kept as `indep_checkZ.run1.*`) 27/29, both failures
  countercontrols of my own design: P4c demanded a strictly positive value at the Bell boundary c = 1/2, where the
  pair formula is exactly 0; G7c expected a rotated Bell state to keep m < 1 under `G_H`, but `G_H` carries every
  sampled maximally entangled state to a product (G5 shows m = 1 for all five). The other 27 lines are identical
  across the two runs.
- **Pre-audit script** `preaudit_z.py`: run 3 9/9, replay identical; runs 1–2 kept (my own derivation slips,
  recorded in `PRE-AUDIT-Z.md`).

## 3. Correctness: independent checks

| Z claim | coordinator's check | result |
|---|---|---|
| the circle-1 Bell defects form the Lorentz cone `L1 = {−uE12 − ūE21 + Λ(E33+E44) : |u| ≤ Λ}` with dual `2|y12| ≤ y33 + y44` | K1 (symbolic in γ) | confirmed |
| Z's `y` lies in `K_T*`: in `L1* ∩ L2*`, and `y = q0 + ℓ1(u0, 7/17)` with `q0` PSD, `|u0|² = 1613/10000 ≤ 49/289` | K2, K3 (exact PSD by characteristic coefficients) | confirmed |
| Z's `w = vv† + ℓ1(ζ, 17)` lies in `K_T*` (`|ζ| ≤ 17`, `2|w12| = w33 + w44`, `w34 = 0`) | K4 | confirmed |
| `tr(yw) = −6/625`, `ipW = −24/625`: `K_T` not self-dual | K5; K6c (members of `K_T` pair ≥ 0 with y and w) | confirmed |
| pair obstruction `tr(yw) = c − 1/(4c)` for two Bell-type defects at overlap c; −301/900 at c = 9/25; +399/1600 at 16/25 | P1 (symbolic), P2, P3 (realized on Φ⁺ and a rotated Φ⁺ at overlap 9/25) | confirmed |
| NOTES N15: generalized seeds, `⟨y,w⟩ = 4c − (1−α)²/G`, negative at c = 0 for α ∈ (1/2, 1) | P4, P4c | confirmed |
| S3 seed: `ψ_a = (15,−1,7,7)/18` has `|det|² = 784/6561` on the torus orbits of `ψ_a` and `CNOTψ_a`; `f = 1/2 + 5√137/162 ≤ 7/8`; `ρ(e)ψ_a = −ψ_a/32`; seed pairs ≥ 0 with reachable states | S1–S4 (symbolic in β; 40 exact reachable states) | confirmed |
| no Bell-type defect at S3: the two AM–GM families are sent to products by CNOT | S5 (symbolic in γ); S6c | confirmed |
| S3-z seed: `ψ_t = (7,4,0,4)/9`, min|det| = 16/81, `f = 1/2 + √5537/162 ≤ 24/25` | S7 | confirmed |
| orders 16, 48, 128, 32, 64, 192, 23040; `Stab_Cl(Z_F)` = 1536; `⟨G16,SWAP⟩` acts on the four defects with image of order 24 | G1, G2 (closure of signed permutations of the 16 tables; exhaustive) | confirmed |
| `G_S` orbit of `e_F`: 8 defects, off-diagonal pairings {0, 1/8} | G3 | confirmed |
| conjecture refutation: the `X⊗I`, `Y⊗I` marginals of `cnot T` are `C11`, `C21`, the `I⊗Z` marginal of `cnot·Ad(I⊗H) T` is `C31` | G4 (symbolic correlation matrix); G5 (five maximally entangled states, m = 1 under `G_H`) | confirmed |
| seeds `m = 4160/6561` (`G_H`), `6272/6561` (`G_Cl`) for `ψ_a`; `α = 9/10`, `99/100` admissible | G6 (exhaustive), G7c, G8 (`min|det| = 49/162`, `17/162`) | confirmed |
| axis Lie closures at level (i): control (3,4,0) → 2, (3,0,4) → 4; target (0,3,4) → 2, (3,4,0) → 4 | A1 | confirmed |

Not independently recomputed: Z's [N] margins (guidance only, by Z's own rule), the exact symmetry group's
identity component `T³_F` beyond the ingredients in G2 (the monomial-matrix argument is reviewed in §4), and z1's
particular witnesses for the countercontrols (the same conclusions hold with the coordinator's witnesses,
`PRE-AUDIT-Z.md` P5c, P7).

## 4. Correctness: proofs reviewed

- **Claim D.** Identical in content to Y's dichotomy (Y1.3), found independently: for `α = max(1/2, f(ψ)) < 1` the
  seed `αE00 − T_ψ/4` is `(2α)·(I − (1/α)ψψ†)/8`, Y's cap defect with `c = 1/α`; the three identities, closedness
  (`⟨E00, e⟩ = α − 1/4 > 0`) and the converse are sound. The dimension corollary is sound.
- **S1, the stabilizer.** The non-PSD extreme rays of `K(Z_F)` are exactly the four defects (pairing `e_s = q + Σλ_t e_t`
  with `T_s` gives `λ_s ≥ 1`; pointedness gives `λ_s = 1`; then `q = −Σ_{t≠s}λ_t e_t` is PSD only if all `λ_t = 0`,
  since its eigenvalue on `ψ_s` is `−Σλ_t/8`). An element of 𝒜 preserving `K(Z_F)` preserves `Q3` and `E00`, so it
  permutes the defects exactly, hence is monomial in `{ψ_s}`. Identity component the diagonal torus (dimension 3),
  component group `S4 × Z2` with `⟨G16, SWAP⟩` a complement (image of order 24, kernel `{id, T}`; T central because
  every generator is real): sound, and G2 confirms the exact ingredients.
- **S2.** The group `T²_c·G16` with component group of order 8 (`Ad(Z⊗I)` lies in the torus): sound. The
  classification of Bell seeds as `C1 ∪ C2` (invariants `A = c₀₊c₁₋`, `B = c₀₋c₁₊` fixed by the torus and negated/
  swapped/conjugated by the generators; parallelogram identity and AM–GM): sound. The overlap bound on the whole
  reachable set follows from every point of the circles and every image being maximally entangled: sound; EBF gives
  EXOTIC(existence), also for the larger group `⟨T³, G16⟩`. The `K_T` refutation is confirmed exactly (K1–K6c); its
  logic is valid: two elements of `K_T*` pair negatively, so `K_T* ≠ K_T`. The residual (torus-fixed tables are
  diagonal in the product basis, so every exotic torus-invariant `K` contains a continuous family of non-PSD elements)
  is sound and rules out any finite surgery for S2.
- **S3.** Group `T²_x ⋊ G16` (Y4's `T·G16`); reachable-set dimension ≤ 5; the seed and the absence of a Bell-type
  defect are confirmed; the `actC Ry` transfer by `Ad(S⊗I)` is sound. Level (ii) inherits the verdict.
- **Finite extensions.** The refutation of the protocol's conjecture is sound (G4) and sharper than needed: `G_H`
  carries every sampled maximally entangled state to a product. Every finite group is EXOTIC(existence) by the
  dimension corollary; the exact seeds are confirmed (G6). `K(Z_F)` is explicit for every subgroup of `Stab_Cl(Z_F)`
  (G2, and `PRE-AUDIT-Z.md` P1, P6).
- **Axis dependence (S3-g).** Z's generated-algebra computation and reachability construction agree with Y3 at
  level (i) (A1). Z's `S3-g` UNIQUE is the same node as Y's `S3[n]` off-frame, decided the same way.
- **Lie-theory step.** The connected subgroup generated by one-parameter groups has the Lie algebra they generate,
  and a closed `K` invariant under generators is invariant under the closure: standard, as in Y.

## 5. Corrections and cross-thread comparison

1. **Level (ii) extrapolation (correction).** Z's §0 and §3 extend EXOTIC(existence) by [W] "to every equatorial
   control axis and every target axis perpendicular to x". That holds for `cnot` alone (level (i), A1). The node
   includes `G16`, whose transpose sends an axis `n` to `(nₓ, −n_y, n_z)` and whose `Ad(I⊗Z)` sends a target axis to
   `(−mₓ, −m_y, m_z)`; for a non-coordinate axis the two images are non-parallel and the closure reaches dimension
   ≥ 4 (A2: control (3,4,0) → 6, target (0,3,4) → 6), so those nodes are UNIQUE at level (ii). Only the coordinate
   axes stay exceptional (A3c), which is Y3's level-(ii) classification. Z's exact verdicts (control x, control y by
   conjugation, target z) are unaffected; the correction narrows Z's [W] sentence to level (i).
2. **Two groups of order 1536.** Y5's "`G16` + control Clifford" (1536) and Z's `Stab_Cl(Z_F)` (1536) are different
   groups: `Ad(H⊗I)` carries `z_(1,1)` out of `K(Z_F)` (`PRE-AUDIT-Z.md` P7), so Y's group does not stabilize `Z_F`.
   Y's node is EXOTIC-E by a cap seed; Z's stabilizer nodes are EXOTIC-X with `K(Z_F)`. Both correct; the integration
   note names them apart.
3. **"Eight hashes."** Coordinator's slip, as for Y.
4. **Z's N4 reading of stage 3's `x7` guidance** ("no violation" never sampled the cross-defect elements) is a
   correct diagnosis of an [N] limitation; no stage-3 label rested on it (X kept the torus row existence-only), so
   nothing changes.

| overlap | Y | Z | agreement |
|---|---|---|---|
| the dichotomy | Y1.3 (cap defect, window `(1, 2]`) | claim D (`α = max(1/2, f)`) | same theorem, independently |
| S1 | EXOTIC-E (seed 517/512) | EXOTIC-X with `K(Z_F)`, stabilizer exact | consistent; Z's is the stronger statement |
| S2 | EXOTIC-E (reachable set `G16·SEP`) | EXOTIC(existence) via `C1 ∪ C2`; explicit cone UNRESOLVED, `K_T` refuted | consistent |
| S3 (`actC Rx`) | EXOTIC-E (c = 4609/4608, no Bell-type route) | EXOTIC(existence) (α = 7/8, no Bell-type defect) | consistent; Z's seed deeper |
| axis dependence | exceptional iff `n ∥ z` or `n ⊥ z` at (i); coordinate axes only at (ii) | same at (i); [W] extrapolation at (ii) corrected (item 1) | consistent after correction |
| finite extensions | all EXOTIC-E; Clifford census 23040, d_min = 5/256 | explicit for `Stab_Cl(Z_F)` subgroups; conjecture refuted; seeds for `G_H`, `G_Cl` | consistent and complementary |
| S4 minimality | minimal among fixed nodes; not minimal once refined (S3[n], R1) | not minimal (S3-g) | consistent |

## 6. Verdict on thread Z

**Reproducible** (replays 9/9 and 9/9; independent check 29/29, replayed identically; pre-audit 9/9) **and correct
as far as reviewed**, with one [W] extrapolation narrowed to level (i) (§5 item 1). Established:

- Every node assigned to Z is EXOTIC: S0, S1, LPT, LPT + SWAP and every subgroup of `Stab_Cl(Z_F)` explicitly with
  the stage-3 cone; S2, S3, S3-z, `G_S`, `G_H`, `G_Cl` and every finite group by existence over exact seeds.
- The protocol's finite-extension conjecture is refuted: `G_H` (order 128) and the Clifford group admit no Bell-type
  defect, yet are exotic.
- The explicit torus-invariant cone left open at stage 3 is not obtained: the only `G16 ⋊ T²`-invariant Bell-type
  surgery is not self-dual (exact pair, −24/625), two Bell-type defects at overlap in (0, 1/2) never give a self-dual
  surgery, and no finite surgery can serve S2. UNRESOLVED, with the obstruction named.
- Necessity evidence for the integration: every symmetry node strictly below S4 that Z examined is EXOTIC except the
  generic-axis node, which is itself UNIQUE; so the minimal UNIQUE symmetry candidates are "cnot plus one generic
  one-parameter local rotation group" (Z's S3-g = Y's S3[n] off-frame), with Y's single off-frame rotation R1 below
  it in the refined lattice.

Rows of the owner's five-row table that Z settles: "weakest sufficient" — the countermodel side of minimality for
every weakening in the fixed lattice (S0, S1, S2, S3, the finite extensions), with S4 shown not minimal in the refined
lattice; "excludes EXOTIC" — nothing further (Z has no countermodel at S4, S5 or H, as required).
