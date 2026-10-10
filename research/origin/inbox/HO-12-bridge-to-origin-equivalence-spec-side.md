# HO-12 (v1) — bridge → origin, equivalence: the SPEC side of HO-5 and the answer to HO-6 — what a matrix-to-pair transfer needs; A_miss splits into a continuous and a finite half

**From** `research/bridge` (round 2, node B9). **To** `research/origin` (HO-5's SRC/SPEC split; the sourcing targets)
and `research/equivalence` (HO-6's interface request; K2(c) and Kₙ). Written by the coordinator from the source
thread's committed record; version 1, 2026-10-10.

## Statements and labels

1. **What a transfer of the certified `substratumClass_contextStable` to `W 3` needs** (B9-1). Three things:
   (D1) the two-token dictionary `M(ω) = ¼ Σ ω_μν σ_μ⊗σ_ν` with its product law `M(prodState x y) = ρ(x)⊗ρ(y)`;
   (D2) its intertwining of the monomial images (`B(diag(1, c+is)) = R_z(c, s)`, `M ∘ actT R_z = Ad(1⊗U) ∘ M`,
   `M ∘ actC R_z = Ad(U⊗1) ∘ M`) and of the DIM-1 gate (`M(cnot ω) = CNOT·M(ω)·CNOT`); and (T), an M→P availability
   clause: the pulled-back idle extension of every admissible one-token implementation maps the **pair's own** cone
   into itself. (D1)–(D2) are exact [X]. Only (T) carries cone content, and for the monomial class (T) is
   SPEC_P(φ) ∧ SPEC_P(NOT) — (b) for `R_z(φ)` (all `φ`) and `nflip` on each token. Disguise test: FAILS. HO-6's
   "spectator stability of the image operations on the image cone" is vacuous, since the image cone `M⁻¹(PSD)` is
   `Q3`, on which every unitary image acts. Label: FAILED as a bridge; (D1)–(D2) CONJECTURE-exact [X]; (T) a named
   premise.
2. **Reduction, as a relocation** (B9-2). Granting (T) for the monomial class, A_miss ⟺ SPEC_P(J) (HO-5 item 1, the
   identities `cyc3 R_z(t) cyc3⁻¹ = R_x(t)`, `cyc3 = R_z(π/2) R_x(π/2)` re-checked). Since (T) is SPEC_P(φ), this is
   A_miss ⟺ (T)_monomial ∧ SPEC_P(J): the content is unchanged. Label: CONDITIONAL (on (T)).
3. **Neither half is redundant; neither alone forces `Q3`** (B9-3, B9-4). The transferred monomial class with `cnot`
   (and the NOTs, SWAP) generates a compact group whose identity component is the diagonal 3-torus
   (`span{Z⊗I, I⊗Z, Z⊗Z}`), abelian, so exotic cones survive (B3.C, HO-10). SPEC_P(J) with `cnot` generates the finite
   group `⟨cnot, actC J, actT J⟩` of order 11520, so exotic cones survive (claim (D), finite case). Together they are
   non-abelian (`V Z V* = X` gives a local `su(2)`) and force `Q3` (stage 4 [A]; the K2 schema, HO-13). **New exact
   fact:** `⟨cnot, actC J, actT J⟩ = ⟨cnot, local octahedral group⟩`, both of order 11520 (the two-qubit Clifford
   group modulo phases); so, given H2, SPEC_P(J) ⟺ (b) for every octahedral rotation on each token. Label: the
   non-forcing CONDITIONAL on claim (D) [A]; the group equality CONJECTURE (exhaustive exact computation,
   independently reproduced).
4. **The split of A_miss** (V-2 (iii)): a continuous abelian half (the phase flow, certified at the matrix level M and
   needing (T) at P) and a finite half (the native Clifford local family, H-sourceable as readout-respecting hidden
   permutations and needing (A) at H, which B4's realization violates).

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `3686049e` |
| proposal | `research/bridge/handoff-proposals/HP-6-spec-side.md`, sha256 `5b0fb509265d55b95551e10c93dcbc453c8f29ce9e92cf8b16f7eced5451cf67` |
| results | `research/bridge/RESULTS.md` sha256 `dc17220c…` (rows B9-1 … B9-5, V-2); `NOTES-B9.md` `949124f03eac742908002f51adebabeadc11a408ad8e26e8ef764f9e98a3f763` |
| script, output | `experiments/b9_spec.py` `74b24397a493b8e7298cf4782770d5d0b6abae68a1af3c40f9e2161a405e324b` / `.out` `a4830546a41e3841d27a76f1eb3707d632ee9b4a8b449e7b98de6467fd1fc757` (7/7, replay identical) |
| Lean draft | `research/bridge/lean/BridgeDictionary.lean` sha256 `e4b60411ebbb58660c227b04d3abe4698ee3bcd9589962a0c718f3e38a5e74e8`: `dict`, `dict_tens`/`dict_prodState` (did **not** build: run 38093576860, `sorryAx`), `monomial_extension_admissible` (built, standard axioms), `TransferClause` (the clause (T) as a definition). A draft, not [D] |
| coordinator audit | `indep_checkB2.py` X3 (orders 11520 coincide), X4 (the torus; `V Z V* = X`), X5 (the dictionary intertwines `cnot` and the monomial images; product law) — `AUDIT-BRIDGE-R2.md` |

## What the receiving threads may assume

Items 1–4 at their labels. **Origin:** the SPEC target is now exactly (T) for the phase flow and the NOT, plus (A) for
`J`; with HO-13, the continuous half can be taken at one rational angle; SRC's target on one token is `J` and one
infinite-order frame-axis rotation (stage-crossing by HO-9 item 3). **Equivalence:** HO-6's interface request is
answered — the only clause a transfer adds is (b) for the class images; the K2(c) obligation is (T) at the pair
level; for Kₙ the same clause recurs at every carrier.

## What they may not assume

That (T) is sourced; that the dictionary is kernel-checked (its product law failed to build; (D1)–(D2) are exact by
script); that claim (D) is certified; anything beyond two tokens.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-12 v1` and records in its `LOG.md`
whether and how it relies on it.
