# EQ4-P audit (research only; nothing adopted, frozen or governed)

Thread: `scratchpad/eq4/P/` (RESULT.md, NOTES.md, p1–p13, x1–x16). Base: certified main `bcbc516f`, read-only snapshot
`scratchpad/eq/base/`. Audit files: this note; `audit_eq4p.py` (+ `.out`, `.replay.out`; failed runs kept as
`.run1.*`, `.run2.*`); `replayEQ4P/` (independent replay harness and outputs).

## 1. Integrity

- **The anomaly the thread recorded is sourced.** HEAD moved from `bc3bf9bc` to `f0d37906` during the thread. The
  reflog's three entries in the thread's window are this session's own logged preflight writes:
  - 06:11:37Z: checkout of the new `claude/eq4f-preflight` at `bcbc516f`, from the detached `bc3bf9bc`;
  - 06:58:18Z: checkout of `claude/network-tool-access-8jtdhm`;
  - 06:58:32Z: the EQ4-F preflight commit `f0d37906`.

  There was no second writer. The thread made no git writes, and its evidence reads only the base snapshot.
- **Base manifest at audit time:** `sha256sum -c --quiet` over 1317 entries is silent, exit 0.

## 2. Replay

The harness is my own, `replayEQ4P/replay.py`. Each copy is byte-checked against the thread's script, run with
`python3 -I -B` from a separate directory, and its stdout compared byte for byte with the thread's recorded output.

- **13 exact probes p1–p13: all byte-identical,** exit 0, empty stderr. `eq4_lib.py` copy identical (`cc2c6aca`).
- **10 exact explorations: 9 byte-identical; x13_c1_greedy differs.** The only difference is a printed wall-clock
  time (`[0.1s]` vs `[0.2s]`). With the eight timing fields masked, the output is identical.
- x3 also prints timings; it matched only because the times agreed. The thread's `RUN-X-OK` therefore depends on
  timing, and x13 is a harness flaw (elapsed time in stdout), not a content difference.
- Explorations are leads, not evidence. No certified probe is affected.
- **Strict verdict of my harness: `VERDICT NOT RENDERED`.** The cause is the timing field above.

## 3. Independent exact checks — `audit_eq4p.py`

**Independence.** The script imports nothing from the thread. It has its own int64 operator calculus with tracked
scale factors, its own Bareiss determinants, rank and principal-minor PSD test, its own double description, and its
own written decomposition for K_A. Sympy is used only for symbolic identities.

**Runs.**
- Run 1: harness error. A sympy `Mul` was multiplied by a Python `bool` after 11 passing checks; no verdict was
  printed.
- Run 2: 35/36. M2 failed because of my own wrong coefficient: 2·P₁₁ instead of P₁₁ in the expected F and G
  combinations. A diagnostic listing every PT block form showed that all pieces are forms and that the ν identity holds.
- Run 3: **36/36, `VERDICT AUDIT-EQ4P-INDEPENDENT-EXACT`**; the replay is byte-identical.
- The decision rule was fixed before run 1. One pre-run correction: C2 first asserted "largest eigenvalue exactly ½
  on every cut", which is false on two cuts, so it was changed to "≤ ½" (§5, item 3).

| block | what it independently confirms | value |
|---|---|---|
| T | Lemma T on all 64 units: `tr_zp[(Φ⁺_zp⊗1)(Φ⁺_zq⊗y)] = ¼ y(p→q)`; a product link fails on 64/64 units | — |
| U | three five-token steps give `K₀₁₂ ≅ K₃₄₅` with the relabelling (0→3, 1→4, 2→5), factor (¼)³; the (BS*, BS) certificate; W3 ∈ BS* (GHZ marginals I/2), W3 ∉ BS; control positive | **−1/8**; control 1/4 |
| P | 3\|3 Bell-link pigeonhole value; control | **−1/16**; 1/8 |
| N | five-token countermodel lemma: a PSD 2-token effect contracted with PSD pair blocks gives PSD (24 exact instances); SWAP countercontrol non-PSD | — |
| S | twirl ⟨XXX, ZZ1, 1ZZ⟩ (8 elements) = GHZ pinching on 64 units; twirled single-token filter = ¼\|a+d\|² id + ¼\|a−d\|² Z_k + ¼\|b+c\|² X_k + ¼\|b−c\|² X_kZ_k (symbolic, every token; exchanged form false); G of order **192** | — |
| A | K_A: 92 generators pairwise ≥ 0; **own double description of K_A\* returns exactly the 92 generators**; own written decomposition reconstructs 400 random exact points of K_A\* (229 with a negative entry); K_A ∩ R⁸₊ has exactly the 28 rays e_j + e_k; GHZ₊ ∉ K_A; 2W3, 2κ are generators; cone{e_j+e_k, 1−2e_j} is not self-dual (⟨x,y⟩ = −1) | — |
| W | K_tw: t-orbit 24, generator set (36) G-invariant, pairwise ≥ 0; **own double description of K_tw\* returns exactly the 36 generators**; GHZ₊ ∉ K_tw; 2W3 ∈ cone(S_tw) (explicit); sample: 60 random Gaussian-integer B_tw generators twirl into K_tw | — |
| M | PT_k of a symbolic GHZ-diagonal operator: 2×2 blocks with equal diagonals (24 forms); 2⟨ν,z⟩, 2⟨F,z⟩, 2⟨G,z⟩ explicit nonnegative combinations of them; ν = 2W3 + 4GHZ₋; W3 ∈ Z and ⟨GHZ₊, W3⟩ < 0 | ⟨ν, Zν⟩ = **−4**; tr(FG) = **−½** |
| E | hyperdeterminant: CNOT₀₁(\|+⟩Φ⁺) nonzero (¼ normalized), GHZ, ψ₃ (4) nonzero; W, \|000⟩, \|0⟩Φ⁺ zero; the seven-token contraction is the Choi vector of a CNOT (inputs 0, 2; outputs 1, 3), i.e. ¼·C | — |
| C | C² = 4C, Cᵀ = C; largest reduced eigenvalue ≤ ½ on all 7 cuts (attained on ac\|bd and the four 1\|3 cuts); w = I/16 − C/32 | tr(Cw)/tr(w) = **−2/7** |
| J | E2 on the crossing (01\|234, 02\|134): Choi(Λ_x) = PT_R(x); conditional = Λ'_x ⊗ Λ'_y rebuilt from PT_R(x), PT_U(y) on 64 units; without PT_R it fails on 32/64 | — |

## 4. Written arguments checked by reading

- **Lemma T premises.** The pairing is a genuine KT pairing: two bipartitions of one five-token body, products of
  states under one and products of effects under the other. It uses:
  - the one-body clause;
  - Bell state and Bell effect of standalone pairs;
  - closedness and full effects of the intermediate triples.

  It does not use uniform composition or an (o) step. Confirmed.
- **Five-token countermodel.** In any bipartition of at most five tokens, one side has at most two tokens.
  - Its cone is PSD, so its effects are PSD.
  - Conditioning a PN generator on a PSD effect of at most two tokens gives a PN generator of the other side
    (lemma N).
  - prod_mem and the one-body clause are immediate, and PN_n is closed.
  - So the PN hierarchy satisfies KT on every family of at most five tokens, with K₃ = BS ≠ PSD₈. It fails at six
    tokens (P, −1/16). Confirmed.
- **Colouring lemma.** Every vertex of the strand multigraph has odd degree: Z nodes have degree 3, one-token nodes
  degree 1. The auxiliary vertex therefore makes the graph connected and Eulerian. Alternating colours from the
  auxiliary vertex leave no Z vertex monochromatic, including the self-loop case. Confirmed.
  - Scope as stated: networks of one-token, two-token and Z-type three-token nodes only.
- **Sector reduction.** The twirl group consists of real local Paulis, so the twirl commutes with T and with K₃'s LU
  invariance. Hence `(K₃ ∩ GD)^{*GD} = K₃* ∩ GD = T(K₃) ∩ GD = K₃ ∩ GD`. Confirmed.
- **K_A self-duality, own written proof.** Sort x ∈ K_A*, and let `a = max(0, −x₁)`.
  - If a = 0: then s ≥ 2x₈, so x ∈ cone{e_j + e_k}.
  - If a > 0: subtract `b(1−2e₁) + c(1−2e₈+2e₁)·`(on the sorted chamber: `1−2e_min`, `1−2e_min+2e_max`) with
    `c = max(0, x₈ + 2a − s/2)`, `b = a − c`. The K_A* constraints `x₁ + x₂ ≥ 0`, `s − 2x₈ ≥ 0` and
    `s − 2x₈ + 2x₁ ≥ 0` make the remainder nonnegative with max ≤ half its sum.
  - This is a different proof from the thread's and agrees with it (A2, A3).

## 5. Findings and corrections

1. **The six-token gem holds** (U, T, §4). KT on the three five-token subfamilies of {0..5}, with:
   - the pair premises,
   - closedness and full effects,
   - the one-body clause,

   derives `K₀₁₂ ≅ K₃₄₅` and excludes (BS*, BS) at −1/8.
   - **Correction to my EQ3 audit, finding (b).** I wrote that triple-level uniformity is "presupposed" by the EQ3
     exclusions. That is right about EQ3's derivation, but KT restricted to six tokens *derives* it, through the mixed
     triples. My audit's scope words ("every family the thread derives") were accurate; its implied conclusion — that
     a wall stated without uniformity must handle cross-related triple cones — is resolved.
   - EQ4-P's RESULT paraphrases the audit as "(BS*, BS) survives every family", which drops those scope words.
2. **The five-token countermodel holds**: case 5 at families of ≤ 5 tokens. The sector models K_A (c = 0) and K_tw
   (c = 1) are self-dual and G-invariant, and they satisfy the twirled filter conditions (S2). So the GHZ-diagonal
   sector conditions do not decide the six-token wall.
3. **Prose inaccuracy, no consequence.** NOTES N2.3 says "largest Schmidt weight of c/2 is ½ on each cut".
   - On ab|cd (input|output) and on ad|bc the largest weight is ¼ (C2).
   - The needed bound, ≤ ½ on every cut, holds, so w ≥ 0 on products and −2/7 stand.
4. **P/A/C wording to tighten before any of this enters a governed text.**
   - (a) "Purification and transitivity … are necessary in the owner's sense". The written proof of
     P ∧ IE₂ ⇒ A goes through K_n = PSD_n. Its density step uses the universality of {native gate, local unitaries}
     (EQ2's generation result), which is [L, unverified] here. So the statement is: *necessary relative to P,
     conditional on that universality result*.
   - (b) "Choi availability … IE₂ in disguise (both directions proved)": proved means written proofs with exact
     ingredients. Nothing is kernel-checked. Direction (c) rests on (ii)⇒(i), whose orbit lemma and density step are
     written (instances exact).
   - (c) "Uniform composition is derived, not assumed": scope is the triple level inside six tokens (k-groups inside
     2k tokens). It uses KT's one-body clause, which is part of P.
5. **Harness flaw.** Explorations x3 and x13 print elapsed times, so their byte-identical replay is not stable. No
   certified probe is affected.
6. **Replayed but not independently re-derived:**
   - F, G ∈ B_tw* (p1 T1);
   - the written block argument S_tw = twirl(B_tw) (my W5 is a 60-point sample, consistent);
   - the general orbit lemma of E3 (ii)⇒(i) (instances only);
   - the six-token reduction (p7);
   - the purification support lemma (p9);
   - every float exploration.

## 6. Standing after the audit

- **Classification confirmed.** Case 5 at ≤ 5 tokens. Undecided between cases 1 and 5 at six tokens. Uniformity,
  S₃ symmetry, LU/filter invariance and co-self-duality are derived inside six tokens.
- **The wall as the thread names it:** a GHZ-free, co-self-dual K₃ with GD section K_A (or another sector solution)
  that extends to K₄, K₅ and K₆ under every six-token crossing constraint. The c = 1 analogue is open as well.
- **Missing principle.** Choi availability is IE₂ restated relative to P. Purification and transitivity (as cone
  automorphisms) are implied by IE₂ relative to P, conditional on the universality citation; whether either is
  sufficient is open.
- **Nothing kernel-checked.** The thread's cheapest decisive formal items, F-b (−1/8 and −1/16 certificates) and F-c
  (the K_A sector model), are confirmed independently here at the exact-arithmetic level.
