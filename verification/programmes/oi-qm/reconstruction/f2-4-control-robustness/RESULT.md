# F2-4 — control of E1-L across generator choices and sizes: result

Research record on a research branch. It is not a native round and not adopted, and it is not for
merge without separate review. It changes no status and proposes no manuscript text.

## Provenance

- **Rules.** `RULES.md` was committed at `4cc8f612`, before any decisive computation.
- **Amendment.** `amendments/amendment-1.md` was committed at `d241eacb`, after a development run
  and before the recorded runs. It corrects OD-2's two-site link set to the per-direction product.
  - The development run printed `VERDICT VOID`, because K-D1neg with `u ⊗ u` failed at every `q`.
  - That run's OD-2 tokens are discarded.
- **Files.**
  - `f2_4_exact.py`, sha256 `0a71536bb707b2d63507838b93c3da63b662b07c67ad899961682a23888dc85e`.
  - `f2-4-exact-output.txt`, its full stdout, sha256 `dcb2b72444847cbba71fce50640c90c2e0ef694d349beb25f284830905442639`.
  - The script imports F2-2's `f2_2_exact.py` (sha256 `246adb2b…`), and through it F2-1's
    `e1_exact.py` (sha256 `e7d257bb…`), both by path and unchanged (K0).
  - numpy is used only for AD-X's modular rank.
- **Replay.** `python3 -I f2_4_exact.py` was run twice, in parallel, and the outputs are
  byte-identical. A run takes about 19 min alone and about 30 min with two in parallel. These are local runs, not `check-run`
  attestations.

## Verdict, as printed

```
TOKEN   F24-AD-GENERAL                 [W] AD; corroborated exactly at (3,2), (3,3), (5,2): yes
TOKEN   F24-CF-DENSE-ALL-N(q)          yes [CHAIN W]       for q = 3, 5, 7, 11, 13
TOKEN   F24-SELF-DENSE-ALL-N(q)        yes [SP, PROD W]    for q = 3, 5, 7, 11, 13
TOKEN   F24-OD3                        yes
VERDICT F24-ROBUST-GENERAL
```

Every control passed:

- K0;
- K-frozen at `q = 3`, 5, 7 and at `(3,2)`;
- K-indep (i)–(v);
- K-D1neg at `N = 1` and `N = 2` for every `q`;
- K-D2neg for every `q`;
- K-AD-mut at `(3,2)` and `(3,3)`.

## 1. Cells

### AD-X — all-duration algebra, `R_cf`

The dimension modulo the identity is a modular lower bound, reduced modulo
`p ≡ 1 (mod 8q)` (`p = 33554137` at `q = 3`, `33554201` at `q = 5`).

| size | full | `M0` principal | `M1` bilinear | `M2` lifted | token |
| --- | --- | --- | --- | --- | --- |
| (3,2) | 80 | 80 | 80 | 80 | `F24-AD-FULL` |
| (3,3) | 728 | 728 | 728 | 728 | `F24-AD-FULL` |
| (5,2) | 624 | 624 | 624 | 624 | `F24-AD-FULL` |

- A lower bound equal to the full dimension certifies fullness.
- `R_self`'s principal member at `(3,2)` is full, 80.
- **K-indep (ii).** At `(3,2)`, F2-1's exact closure over `ℚ(ζ₂₄)` gives 80, 80, 22 and 16 for
  `M1`, `M2`, no translations and local pair generators. These equal the modular values.
- **K-AD-mut.**
  - At `(3,2)`: 22 without translations and 16 with local pair generators, both exact.
  - At `(3,3)`: at least 363 without translations, and 24 with local pair generators.
    - 24 is also the written upper bound `N(q² − 1)`: every generator is then a sum of one-site
      terms. So it is exact.
    - 363 is a lower bound only.
- **K-frozen.** F2-2's values reproduce: 80, 22 and 40 at `(3,2)`.

### OD-1 — one site

| `q` | free patterns | `R_cf` orbits | D1 (`R_cf`, with the free half-layer) | D2 (first word) | `R_self` orbits |
| --- | --- | --- | --- | --- | --- |
| 3 | 4 | 2 | all | `hX` for all | 1 |
| 5 | 8 | 6 | all | `hX` for all | 1 |
| 7 | 8 | 12 | all | `hX` for all | 1 |
| 11 | 8 | 30 | all | `hX` for all | 1 |
| 13 | 8 | 42 | all | `hX` for all | 1 |

- **K-D1neg.** Without the half-layer, and with `u` in its place, the orbits stay separate:
  `(q² − 1)/4` blocks.
- **K-D2neg.** No certificate is issued on `X`, `u` or `uX`.
- **K-indep (v).** At `q = 3` and 5, `R_h ∪ R_{h†}` equals F2-2's `adjoint_relation`.

### OD-2 — two sites, `R_cf`, without any coupling half-layer

| `q` | `R_cf` orbits at `N = 2` | one component, every free pattern |
| --- | --- | --- |
| 3 | 4 (8, 8, 16, 48) | yes |
| 5 | 6 (24, 24, 48, 48, 240, 240) | yes |
| 7 | 8 | yes |
| 11 | 12 | yes |
| 13 | 14 | yes |

- The sound subset sufficed at every `q`; the full link set was not needed.
- **K-indep (i).** At `(3,2)`, the per-direction product equals F2-2's exact relation of `h ⊗ h`
  for every pattern.
- **K-indep (iii).** The sound subset lies inside the exact relation.
- **K-D1neg.** `u ⊗ u` leaves the orbits separate at every `q`.

### OD-3 — RED corroborated

- `R_cf`'s integer-time symplectic part has one orbit, so it is transitive on nonzero vectors, at
  `(3,3)`, `(5,3)`, `(7,3)` and `(3,4)`.
- Each orbit contains a one-site vector, as RED requires.
- **K-indep (iv).** At `(3,3)`, the reduced generating set (`J` and the single-edge leaps) and the
  full set of `R_cf` leaps give the same orbits.
- Transitivity is measured at these sizes only. RED, which is what CHAIN uses, is proved for every
  `N ≥ 3`.

## 2. Written statements [W]

**Conventions.** These are E1's.

- A line `v = (x, ξ) ∈ 𝔽_q^{2N} ∖ {0}` names the Weyl operator `W(v)`. Here `x` is the shift part and
  `ξ` the phase part.
- `⟨·,·⟩` is the symplectic form.
- `W(v)W(w) = τ^{⟨v,w⟩} W(v+w)` with `τ` a primitive `q`-th root of unity. Hence
  `[W(v), W(w)] = (τ^{⟨v,w⟩} − τ^{−⟨v,w⟩}) W(v+w)`, which is nonzero iff `⟨v,w⟩ ≢ 0`.
- The leap of a coupling `M` acts on lines as `L(M)(x, ξ) = (Mx − ξ, x)`.
  - `J := L(0)` acts sitewise as `(x, ξ) ↦ (−ξ, x)`.
  - `L(M) = J·T_M`, where `T_M(x, ξ) = (x, ξ − Mx)`.
  - `T_M T_{M′} = T_{M+M′}`, so `R_cf`'s leaps generate the same group as `J` and the single-edge
    leaps.
  - `U_M := J T_M J⁻¹` acts as `(x, ξ) ↦ (x + Mξ, ξ)`.

### AD — all-duration fullness

Fix an odd prime `q`, `N ≥ 1`, either repertoire, and any generator choice for which E1-L is
defined. Let `𝔤` be the real Lie algebra generated by the all-duration generators, and `𝔤_ℂ` its
complex span.

1. **Ad-invariance.**
   - For a generator `G`, `Ad_{e^{2πiG}} = e^{2πi ad_G}` preserves `𝔤`.
   - `u^{⊗N} ∝ e^{2πiG_free}` and `X_k ∝ e^{2πiG_X^{(k)}}`, for any choice of either generator.
   - `Z_k ∝ u^{⊗N} X_k (u^{⊗N})†`, because `J(a, 0) = (0, a)` at one site.
   - So `Ad` of every Weyl operator, and `Ad_{u^{⊗N}}`, preserve `𝔤_ℂ`.
2. **Lines.**
   - `Ad_{X_k}` and `Ad_{Z_k}` act on `W(v)` by the character `v ↦ ω^{⟨e,v⟩}`, and distinct `v` give
     distinct characters.
   - A subspace invariant under them is therefore spanned by the `W(v)` it contains. The projector
     onto one character is an average over the Weyl group.
   - So `𝔤_ℂ ∩ sl(q^N) = span{W(v) : v ∈ S}` for a set `S` of lines.
3. **Closure of `S`.**
   - (a) `v ∈ S ⟹ −v ∈ S`, because `𝔤_ℂ = 𝔤 + i𝔤` is closed under `†` and `W(v)† ∝ W(−v)`.
   - (b) `S` is closed under the sitewise `J`, by `Ad_{u^{⊗N}}`.
   - (c) `v, w ∈ S` with `⟨v,w⟩ ≢ 0` gives `v + w ∈ S`, by the bracket formula.
4. **Seeds.**
   - *Translations.* `G_X^{(k)}` is a function of `X_k`, since `X_k` has one-dimensional
     eigenspaces, so `G_X^{(k)} = Σ_a c_a X_k^a`. It is not scalar, because `X_k` is not. So some
     `(a e_k, 0)` with `a ≠ 0` lies in `S`, at every site `k`.
   - *Pairs.* For `i < j` and `m ≠ 0`, the single-edge coupling `m(E_ij + E_ji)` lies in both
     repertoires, and its layer is the one gate `δ_ij(m)`. Suppose its generator `G` had no line
     supported on both sites. Then `G = A_i + B_j + c` and `e^{2πiG}` would be a product. But
     `δ_ij(m) = diag(ω^{−m y_i y_j})` has operator-Schmidt rank `q`: its reshaped matrix is a
     Fourier matrix. So `S` holds a line with support exactly `{i, j}`.
   - This holds for every generator of `δ_ij(m)`. `Γ_comm` is needed only for the candidate's
     definition, since a single-gate layer needs no commutation.
5. **The closure lemma.**
   - *One site.* At one site, take `(a, 0)` and `J(a, 0) = (0, a)`. Then:
     - `⟨(a,0),(0,a)⟩ = ±a² ≠ 0`, which gives `(a, a)`;
     - adding `(0, a)` repeatedly gives `(a, ja)`, and adding `(a, 0)` gives `(ja, a)`. Each step
       has form value `±a² ≠ 0`.
     - `(a, ja) + (−a, 0)` gives `(0, ja)` for `j ≠ 0`, and symmetrically `(ja, 0)`;
     - `(ja, 0) + (0, ka)` gives `(ja, ka)`.

     Multiples of `a` exhaust `𝔽_q`, so every nonzero one-site vector at every site is in `S`.
   - *Adjusting a component.* Take `v ∈ S` with `v_i ≠ 0` and a target `t ≠ 0`.
     - If `⟨v_i, t⟩ ≠ 0`, add the one-site `(t − v_i) e_i`, whose form with `v` is `⟨v_i, t⟩`.
     - Otherwise pass through an `s` with `⟨v_i, s⟩ ≠ 0 ≠ ⟨s, t⟩`.

     So any nonzero component of a vector in `S` can be set to any nonzero value.
   - *Growing the support.* Take `v ∈ S` with support `T`, `i ∈ T`, `j ∉ T`, and a pair seed `p` on
     `{i, j}`.
     - Set `v_i = s` with `⟨s, p_i⟩ ≠ 0` and `s ≠ −p_i`.
     - Then `⟨v, p⟩ = ⟨s, p_i⟩ ≠ 0`, and `v + p ∈ S` has support `T ∪ {j}`.
   - Every pair has a seed, so every support and every value is reached:
     `S = 𝔽_q^{2N} ∖ {0}`.
6. **Conclusion.** `𝔤_ℂ ⊇ sl(q^N)`, and `𝔤 ⊆ u(q^N)` is a real form of it. Hence
   `𝔤 ⊇ su(q^N)`. ∎

Only (i) and the seeds are used:

- the translations;
- `u^{⊗N}`, any free generator;
- one single-edge coupling per pair, any generator.

So the statement covers `Γ_comm` and both repertoires at every `q` and `N`. Removing the
translations or making the pair generators local breaks it (K-AD-mut).

### MONO, PROD

- **MONO.** A larger generating set has a larger closure. Irreducibility of the adjoint action, and
  the existence of an element of infinite order modulo scalars, pass to it.
- **PROD.**
  - `h` is diagonalizable with root-of-unity eigenvalues, so `h^r = 1` for some `r`.
  - Then `(h^{⊗N}X_1)^r = (hX)^r ⊗ 1`.
  - If `h^{⊗N}X_1` had finite order modulo scalars, so would `(hX)^r`, and hence `hX`.

  ∎

### RED — `R_cf`, `N ≥ 3`

The moves are `T_M`, `U_M` and `J`, for zero-diagonal symmetric `M`.

- **Lemma A (clearing `ξ` away from a site).** If `x_l ≠ 0`, let
  `M = Σ_{k≠l} (ξ_k/x_l)(E_kl + E_lk)`. Then `T_M` clears `ξ_k` for every `k ≠ l`.
- **Reduction.** Let `v = (x, ξ) ≠ 0`. If `x = 0`, apply `J`. So assume `x_l ≠ 0`, and apply
  Lemma A, giving `(x, ξ′_l e_l)`.
  - **If `ξ′_l ≠ 0`.** `J` gives `(−ξ′_l e_l, x)`. Lemma A at `l` then gives a one-site vector.
  - **If `ξ′_l = 0`,** the vector is `(x, 0)`.
    - *`|supp x| = 1`:* it is already one-site.
    - *`|supp x| = 2 = |{l, b}|`:*
      - `J` gives `(0, x)`.
      - `U_{E_kl + E_lk}`, with a third site `k`, gives `(x_l e_k, x)`.
      - Lemma A at `k` gives `(x_l e_k, 0)`.
    - *`|supp x| ≥ 3`:*
      - Take distinct `a, b, l` in the support.
      - `T_{E_ab + E_ba}` gives `(x, −Mx)`.
      - Lemma A at `l` leaves `ξ′_l = 2x_a x_b / x_l ≠ 0`, since `q` is odd.
      - The first case applies.
- **Joining sites.**
  - `T_{c(E_ij + E_ji)}` maps `(x e_i, 0)` to `(x e_i, −cx e_j)`.
  - `J` gives `(cx e_j, x e_i)`.
  - Lemma A at `j` gives `(cx e_j, 0)`.

∎

### CHAIN

- **D1.**
  - At `N = 1` and `N = 2` it is computed (OD-1, OD-2).
  - At `N ≥ 3`, the components of the orbit graph joined by the free half-layer's links are found
    in three steps:
    1. By RED, every component contains a one-site line.
    2. `J` and the free half-layer act on the one-site lines at site `i` exactly as at `N = 1`,
       because `Ad_{h^{⊗N}}` acts on `W(v e_i)` as `Ad_h` at site `i`. So OD-1's `N = 1`
       connectivity joins all one-site lines at each site.
    3. By RED's last step, `(x e_i, 0)` and `(cx e_j, 0)` lie in one orbit. One component remains.
- **D2.** By PROD, from OD-1's certificate for `hX`. The word `h^{⊗N}X_1` lies in every
  one-duration repertoire.
- **Density.** D1 and D2 give density by F2-2's inference [W]. Neither uses a coupling half-layer,
  so MONO extends the result to every coupling choice.

∎

### SP — `R_self`

- The leaps of all symmetric `M` give `J` and every `T_M`, hence every `U_M`.
- The group `G` they generate is all of `Sp(2N, q)`:
  - For `M = cE_kk`, `T_M` is the symplectic transvection along `(0, e_k)` with parameter `c`.
  - `G` is transitive on nonzero vectors. Take `(x, ξ)` with `x ≠ 0`; if `x = 0`, apply `J`
    first.
    - `M ↦ Mx` is onto `𝔽_q^N` on symmetric `M`, so some `T_M` gives `(x, 0)`.
    - `J`, then a suitable `U_M`, then `T_M` give `(e_1, 0)`.
  - Conjugating one transvection by `G` therefore gives every transvection, since
    `gτ_{v,c}g⁻¹ = τ_{gv,c}`.
  - Transvections generate `Sp(2N, q)`.
- This is corroborated by F2-2's group orders at `(3,1)`, `(5,1)`, `(7,1)` and `(3,2)`, and by
  OD-1's single `R_self` orbit at every listed `q`.
- `Sp(2N, q)` is transitive on nonzero vectors, and the integer-time group contains every Weyl
  operator. So D1 holds from the integer-time group alone, and PROD gives D2.

∎

## 3. Findings

1. **All-duration control is full for every generator choice, at every odd prime and every size.**
   - This holds under both repertoires and is proved in general [W, AD].
   - It is corroborated exactly at `(3,2)`, `(3,3)` and `(5,2)`, by:
     - the principal member;
     - the bilinear `Γ_diag` lift;
     - a lifted `Γ_diag` member with non-principal free and translation patterns.
   - The proof uses three things: the translation generators, the free layer's time-1 image
     `u^{⊗N}`, and the non-locality of one pair generator per pair. Nothing about the coupling
     generators' diagonal values or logarithm choices enters.
   - This closes two open items:
     - F2-2's: `Γ_spec` robustness under `R_cf` at `(3,2)`;
     - F2-3's: `R_cf` fullness at `N ≥ 3` over `Γ_diag`.
   - The robustness is universal. It is not an existence statement and not a generic one.
2. **One-duration density does not depend on the coupling generators at all.**
   - D1 holds from the integer-time group and the free half-layer alone:
     - at `N = 1` and `N = 2`, computed for `q ≤ 13`;
     - at every `N ≥ 3`, by RED.
   - D2 holds from the free word `h^{⊗N}X_1` (PROD).
   - By MONO, density therefore holds for every coupling generator choice. That includes every
     diagonal logarithm choice and every non-diagonal member of `Γ_comm` at `N = 2`.
   - At `q = 3, 5, 7, 11, 13` it holds at every `N` and for every free pattern of `Γ_spec(u)`.
   - The coupling half-layers change which gates are available at one duration (F2-3's C2). They
     do not affect density.
3. **`R_self` is a separate positive control, and its result is not transferred.**
   - Its integer-time group is the full Clifford group at every `N` (SP). D1 needs nothing else.
   - With PROD, density follows at the same `q`, by a different argument.
4. **The remaining dependence on `q` is in two one-site certificates and one two-site
   certificate.** These are:
   - D1 under `R_cf` at `N = 1`;
   - the word `hX` at `N = 1`;
   - the coupling-free D1 at `N = 2`.

   All three hold at `q ≤ 13`. A proof for every odd prime is open, so the one-duration statement
   is not claimed beyond `q = 13`.
5. **A defect in the frozen rule, caught by its own control.**
   - The two-site link set as frozen over-joined orbits.
   - The `u ⊗ u` countercontrol detected it in the development run, while the equality check K-indep
     (i) could not have.
   - Amendment 1 fixes it before the recorded runs.
   - Assumption-watch marker: *a merged two-direction relation does not tensor; take products per
     direction.*

## 4. Classification (owner framing)

| family | all-duration fullness | one-duration density |
| --- | --- | --- |
| coupling generators (`Γ_comm`, including all of `Γ_diag`) | universal, every `q`, `N` [W] | universal [MONO], at `q ≤ 13`, every `N` |
| translation generators | universal [W] | integer time only; not a parameter |
| free layer, `Γ_spec(u)` | universal [W] | universal at `q ≤ 13`, every `N` |
| free layer, `Γ_all(u) ∖ Γ_spec(u)` | universal [W] | not decided; F2-2 found two Clifford square roots of `u` at `q = 7` |

- **Extension-dependent.** Everything is conditional on E1-L (R1–R4, `T_loc`, T1–T3, correction 1)
  and on inherited complex kinematics. Nothing is OI-derived.
- **Consistency axis only.** No empirical confrontation; correctness bands unchanged.
- **Evidence levels.**
  - AD, MONO, PROD, RED, CHAIN and SP are written proofs, not kernel-checked.
  - The OD cells are exact.
  - AD-X is an exact lower bound, tied to F2-1's exact closure at `(3,2)`.

## 5. What unitary control does not supply: the next round's questions

Full or dense unitary control is a statement about the operations available on an already given
state space. It supplies none of the following, and nothing here infers them.

- **Preparation.**
  - *What it needs:* at least one pure fiducial state, available at a known tick. Dense control then
    approximates every pure state from it.
  - *Open:*
    - whether E1-L's registration (R1–R4) yields a pure registered configuration;
    - whether it yields only the counting-measure prior's mixtures;
    - which physical process in the substratum prepares it.
- **Measurement.**
  - *What it needs:* a readout in some basis, with its statistics given by the Born rule. Every
    other basis is then reached by control followed by that readout.
  - *Available:* F2-1 measured the Born law against the rooted law on finite words, for registered
    starts.
  - *Open:* a measurement model, meaning what in the substratum realizes the readout, and its
    back-action.
- **Holding a state.**
  - *The difficulty:* the leap dynamics never stops. Holding a state means implementing the
    identity over whole ticks.
  - *What is already available:* the coupling-free tick is `u^{⊗N}`, of order 4 modulo phases, so
    every fourth coupling-free tick is the identity exactly.
  - *Open:* whether that is physically selectable, and how errors accumulate between operations.
- **Ancillas.**
  - *What they need:* extra sites that start uncoupled in a known state and can be coupled later.
  - *Available:* F2-2's L1 gives exact independence while they are uncoupled.
  - *Open:* their preparation, which is the first question, and their discarding, which is a
    partial trace with a physical meaning.
- **Composites.**
  - *Inherited, not derived:* the tensor product of sites (R1, complex kinematics).
  - *Open:*
    - whether operationally independent subsystems compose this way;
    - Track B's declared decomposition and hidden factors, which P0 shows locality depends on.

The round that takes these up should state each requirement as an operational resource. It should
then test whether E1-L's registration and leap dynamics provide it, with controls on the counting
measure and on the meter, and without reading any of them off from control.

## 6. Open, and non-claims

**Open.**

- The one-site and two-site certificates for odd primes `q > 13`. A general proof would extend
  CHAIN to every `q`.
- One-duration density for free generators outside `Γ_spec(u)`.
- Time-independent generators for a whole tick, and orientations other than `i < j`.
- The operational requirements of §5.
- The interface to Track B's carriers, which P0 left open. It is kept separate here.

**Non-claims.**

- Density is not exactness: the one-duration sets are countable. Exact availability from all
  durations rests on Jurdjevic–Sussmann [L].
- Unitary control is not operational sufficiency (§5).
- No kernel proof. Local continuity, `Γ_comm`, and the gate-only rule remain added hypotheses
  without a physical source.
- Nothing is said about which alphabet nature uses.
