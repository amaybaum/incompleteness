# A1-EXIT R6 — lemmas L6, L7, L9 on infinite hidden carriers: result

**Status.** Writer's paper-only research record, accepted after independent non-author review on
[PR #1467](https://github.com/amaybaum/incompleteness/pull/1467) (round 1 at `62a4332b`, REVISE,
[comment 7048283597](https://github.com/amaybaum/incompleteness/pull/1467#issuecomment-7048283597); round 2 at
`8ecb3b12`, ACCEPT-WITH-NITS,
[comment 7048749116](https://github.com/amaybaum/incompleteness/pull/1467#issuecomment-7048749116); a
final-head check of `81718175`, relayed by the coordinating session and not posted, answered at
`1aae7562` (§12); the edits of `1aae7562` reviewed after landing, ACCEPT,
[comment 7050047312](https://github.com/amaybaum/incompleteness/pull/1467#issuecomment-7050047312)) and
landed by owner decision, recorded at
[#1169 comment 7049542030](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7049542030)
(`amaybaum`, 2026-11-20T20:11:42Z). Targets, classification rule, disguised-A1 test and controls were
fixed in `PREREG.md` (commit `8fb6b663`, pushed before this file and unchanged since). Every proof
below is a [W] paper derivation by the writer, not kernel-checked, and checked by those reviews;
computations are exact (`fractions.Fraction`), in `r6_controls.py`, with outcomes in
`r6_controls.json`. No manuscript, Lean, registry, book or mirror edit; no premise adoption. A1 (Main
posit ledger item (ii)) remains open and unadopted. Step 2 (manuscript propagation) is queued, not
authorized. The reviews are answered in §12.

**Authorization, goal link, source pin.** As `PREREG.md`: owner `amaybaum`,
[#1169 comment 7047514209](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7047514209),
2026-11-20T18:31:48Z, Step 1 row R6, "Valid proofs, or an explicit finite-only restriction of the
unsupported conclusions | Paper-only research record". Source pin `main` at
`9db518844df62151979acf6aac1d487b59c44907`; `M:n`, `Sub:n`, `GR:n`, `Intro:n`, `AppB:n`, `FULL:n`,
`ch02:n` are line `n` of `papers/Main.md`, `papers/Substratum.md`, `papers/GR.md`,
`papers/Introduction.md`, `book/appendix-b-derivations.md`,
`book/The-Incompleteness-of-Observation-FULL.md`, `book/ch02-substratum.md` at the pin.

**Reproduction (§A.42 item 1).** At this record's commit:
`python3 -I verification/audits/foundations/a1exit-r6-20261120/r6_controls.py OUT.json` exits 0 and
writes `OUT.json` byte-identical to the committed `r6_controls.json` (deterministic; about 2.5 min,
standard library only).

## 1. Verdict (generated from the classifications in §§3–5)

| Target | Part | Statement (short) | Proof status | Layer | Disguised-A1 test | Class |
|---|---|---|---|---|---|---|
| T6 | (i)–(iv) | Hidden-prior mixture family `Φ_t = Σ_π ρ(E_t(π)) Ψ_π` on a measurable hidden space: equals Main's family on finite `H`; CPTP; diagonal-preserving with populations `Γ_t`; P-indivisibility of `Γ` ⇒ CP-indivisibility | proved [W], reviewed; finite recovery exhaustive (K1) | paper + exact finite computation | passed (odometer, K3b) | **INF** |
| T6 | P witness on infinite carriers | non-permutation `Γ_s` ⇒ P-indivisible | not by itself (K3a countermodel); under (NR) M:131 [paper, on `main`], under RIGID compactness [Lean, on `main`] | paper / Lean / exact | (NR) passed (K3b) | **WEAK** (named condition (NR) or (RIG)) |
| T6-K (α) | diagonal preservation, constant-vector state | Koopman unitary on `ℂ^V ⊗ L²(H,ρ)` with the normal hidden state `\|ψ⟩⟨ψ\|`, `ψ` the normalized constant function, preserves diagonals | refuted on every carrier, finite ones included: exact countermodel (swap, `\|H\| = 2`, K2(i)), lifted to a diffuse carrier by T9(a) | exact + paper | — | **REFUTED** (outside the four preregistered classes; §12 D1) |
| T6-K (β) | diagonal preservation, diagonal normal state | Single-unitary (permutation or isometry) dilation with a diagonal normal hidden state | proved for every purely atomic `ρ`, countably infinite ones included (§3.2, countable carriers); undefined on a carrier with a diffuse part, where no diagonal normal state exists (Prop. 6.7: non-existence, not a countermodel) | paper | purely atomic laws are not A1 (countably infinite carriers qualify) but fail the preregistered diffuse-exhibit test | **outside the four preregistered classes** (holds on purely atomic laws; undefined on diffuse ones; §12 D1) |
| T6-K (γ) | diagonal preservation, other non-diagonal normal states | Finite `H`: some permutation breaks it for every non-diagonal `μ_H`; diffuse `ρ`: whether every normal state fails for some `F` | finite `H`: proved [W] (Prop. 6.9); diffuse: not shown | paper | — | finite: refuted for every non-diagonal state; diffuse: **OPEN** |
| T6-K | CP theorem, `\|V\| = 2` | Koopman family with the constant vector, `F` preserving `c ⊗ ρ` | proved [W] (Lemma 6.8), consistent with K2 (0 countermodels in 244 728 decided pairs; 0 violations of the lemma's identity) | paper + exact | passed | **INF** (`\|V\| = 2`, under `c⊗ρ` invariance) |
| T6-K | CP theorem, `\|V\| ≥ 3` | same | no countermodel among 1 104 decided pairs at `(3,2)`, 3 312 + 6 144 undecided | exact (partial) | — | **OPEN** (not consumed by M9) |
| T7 | all | C2 quantitative theorem (M:459) and physical-memory theorem (M:473) on any measurable hidden space, any reference probability | proved [W], reviewed | paper | passed (Bernoulli, K3a) | **INF** |
| T9 | (a) | decoupled factor on a Hilbert space of any dimension, normalized state (normal for the Schrödinger form; any state for the Heisenberg form), any unitary or isometric dynamics: reduced channel family unchanged | proved [W] | paper | passed | **INF** |
| T9 | (b) | classical factor `(A, α)`, `α` a probability, any measurable map: mixture and rooted families unchanged | proved [W] | paper | passed | **INF** |
| T9 | (c) | Theorem 24(i) relabelling on a measurable hidden carrier | proved [W] under ρ-preservation; countermodel without it (K4) | paper + exact | passed | **WEAK** (σ preserves ρ) |
| T9 | (d) | Corollary (iii) exact transfer to such factors | proved [W] from (a), (b) | paper | passed | **INF** |
| T9 | (e) | Hilbert-space factor adjoined to the mixture base on a diffuse carrier (added after review round 1) | proved [W], immediate | paper | passed | **INF** |

Consumers (§2): **M9** — the implication "P witness ⇒ CP-indivisibility" holds on infinite carriers
(INF); the full chain from a non-permutation rooted map holds under (NR) or (RIG) (WEAK); Main's
statement "the CP-indivisibility theorem of §3.2 … [is a statement] about finite representatives"
(M:732) is no longer forced. **M16** — INF. **M21** — the deep-sector gauge reading extends to
decoupled normalized factors of any cardinality and any own dynamics (INF); coupled infinite deep
sectors stay outside (unchanged: GR Appendix B for finite windows, H-BD at leading order). **C8** —
(i) WEAK (ρ-preserving relabelling), (iii) and Corollary (iii) INF; recurrence-scale content of the
base is outside R6 (REMAINDER: inherits M4/M7).

Gem-finding output (§A.31; §8): one **NEW** finding (the hidden-prior premise of Main's diagonal
lemma has no normal Hilbert-space form on diffuse carriers, so REMAINDER's proposed Koopman shape
for L6 is the wrong object), three **ELABORATING** (Lemma 6.8; reference-prior independence and
read-σ-algebra form of T7; exact visible return without total recurrence, T9(d)), one **CONFIRMING**
(T6 needs no invariance and no bijectivity, only fibre injectivity).

## 2. Consumers and where finiteness enters

| Consumer | Current text | Proof at the pin | Where finiteness enters |
|---|---|---|---|
| M9 | M:268 Setup (`𝒞_H` finite "under the total-finiteness posit"); M:282–286 channel with `ρ_H = I_m/m`; M:328 Lemma (diagonal preservation) for `Tr_H[U^t(ρ⊗μ_H)U^{−t}]`; M:332 Theorem (CP-indivisibility, framework scope); M:742 table row; M:60 and M:732 item (ii) list it among statements about finite representatives; mirrors AppB:92 (Theorem B.2.5, "from a non-permutation rooted map and finiteness"), FULL:5769 | Diagonal lemma: "A permutation unitary conjugates a diagonal state to a diagonal state; the partial trace of a diagonal state is diagonal." CP theorem: stochastic `M_kj` from `Λ`, contrapositive | (1) `H` finite so `U` is a permutation matrix on `ℂ^m` and `μ_H` a diagonal density matrix; (2) the P witness comes from §2.3 Step 1 (finite order). The CP argument itself uses finiteness of `V` only (REMAINDER M9; ROOTS R4) |
| M16 | M:459 Theorem (C2 necessity, quantitative mixing form) "Model one coupling step as the uniform-prior bijection marginal"; M:473 Theorem (physical memory: C2, process form), `K̄_{x_k} := Σ_h π_H(h) K(x_k,h;·)`; M:732 item (ii) list | TV contraction "pushing two hidden distributions through the same channel"; Fannes–Audenaert on `V` | Sums over `h` and the uniform prior on finite `𝒞_H`; the phrase "given … `H_k = h`" conditions on a point event. The entropy step uses finite `V` only |
| M21 | M:60 ("A finite factor adjoined … leaves every visible transition probability unchanged …; a deep sector that the dynamics couples …, and an infinite hidden sector, are outside that statement"); M:732 item (ii) ("a finite factor … evolved by its own permutation") | Partial trace with `Tr σ_A = 1` (Sub:266 proof (iii)) | The factor is finite and its dynamics a permutation; no infinite statement proved (Sub:262) |
| C8 | Sub:253 (i) "any bijection σ … with uniform hidden prior"; Sub:257–262 (iii) "Adjoin a finite factor `A` … This is a finite, fixed-interface result; an infinite extension requires its own normalized measure or trace-class state and a well-defined evolution, and is not established by finite uniform counting"; Sub:268 Corollary (iii) "Infinite extensions need a separately specified normalized state or measure and dynamics" | Sub:266 | (i) every bijection preserves the uniform prior on finite `𝒞_H`; (iii) finite `A`, permutation `W` |

## 3. T6 — L6: the CP-indivisibility family on a measurable hidden carrier

### 3.1 Statement

**Hypotheses (𝒽6).** (H6.1) `V` finite, `|V| ≥ 2`. (H6.2) `(H, 𝓗)` a measurable space and
`F : V × H → V × H` measurable for `2^V ⊗ 𝓗`; write `F^t(x, h) = (A_t(x,h), K_t(x,h))`. (H6.3) the
coincidence sets `C_t(x,y) = {h : K_t(x,h) = K_t(y,h)}` lie in `𝓗` for all `t, x, y` — implied by
measurability of the diagonal of `H × H`, hence by `H` standard Borel (more generally countably
separated with a measurable diagonal). (H6.4) fibre injectivity: for every `t ≥ 1` and `h`,
`x ↦ F^t(x, h)` is injective — implied by injectivity of `F`. (H6.5) `ρ` a probability on `H`.

No invariance of any law, no bijectivity, no recurrence, no finite support.

**Patterns.** For `t` and `h`, the pattern `π_t(h) = (f, ~)` is the map `f = A_t(·, h) : V → V` and
the equivalence relation `x ~ y ⇔ h ∈ C_t(x,y)`. Patterns range over the finite set
`V^V × {equivalence relations on V}`. `E_t(f, ~) = {h : π_t(h) = (f, ~)}` is a finite Boolean
combination of the sets `{h : A_t(x,h) = a}` (measurable sections of a measurable map into the
discrete `V`) and `C_t(x,y)` (H6.3), so it lies in `𝓗`; the `E_t(·)` partition `H`. By (H6.4),
`x ~ y` and `f(x) = f(y)` force `F^t(x,h) = F^t(y,h)`, hence `x = y`: `f` is injective on each class
of every pattern that occurs. The **pattern channel** is `Ψ_{f,~}(|x⟩⟨y|) = [x ~ y] |f(x)⟩⟨f(y)|`.

**Definition (hidden-prior mixture family).**
`Φ_t := Σ_{(f,~)} ρ(E_t(f,~)) Ψ_{f,~}`, equivalently `Φ_t(σ) = ∫_H Ψ_{π_t(h)}(σ) ρ(dh)` with a
finitely-valued integrand (no Bochner integration needed).

**Theorem 6 (L6, measurable form).** Under 𝒽6:
1. *(finite recovery)* if `H` is finite and `F` a bijection, `Φ_t(σ) = Tr_H[U^t(σ ⊗ μ_H)U^{−t}]`
   with `U` the permutation unitary of `F` and `μ_H = Σ_h ρ(h)|h⟩⟨h|`, Main's family (M:328) with
   the diagonal hidden prior;
2. *(CPTP)* each `Φ_t` is completely positive and trace preserving;
3. *(diagonal preservation)* `Φ_t(|x⟩⟨x|) = Σ_b Γ_t(x,b) |b⟩⟨b|` with
   `Γ_t(x,b) = ρ{h : A_t(x,h) = b}`, the rooted family of M:131 (and of RIGID
   `rootedFamily_productLaw` when `F` is a bimeasurable bijection preserving a product law `ν ⊗ ρ`);
4. *(CP-indivisibility)* if `(Γ_t)` is not P-divisible on `{0, …, n}`, there are `0 < t_1 < t_2 ≤ n`
   with no positive trace-preserving — in particular no CPTP — `Λ` such that `Φ_{t_2} = Λ ∘ Φ_{t_1}`.

### 3.2 Proof [W]

(1) `Tr_H[U^t(|x⟩⟨y| ⊗ μ_H)U^{−t}] = Σ_h ρ(h) Tr_H |F^t(x,h)⟩⟨F^t(y,h)|`
`= Σ_h ρ(h) [K_t(x,h) = K_t(y,h)] |A_t(x,h)⟩⟨A_t(y,h)| = Φ_t(|x⟩⟨y|)`. Control K1 compares the
two by independent code paths (explicit matrix products versus the pattern sum).

(2) For a pattern that occurs, put `K_C = Σ_{x ∈ C} |f(x)⟩⟨x|` for each class `C`. Then
`Σ_C K_C |x⟩⟨y| K_C^† = [x ~ y] |f(x)⟩⟨f(y)|` and, `f` being injective on `C`,
`Σ_C K_C^† K_C = Σ_C Σ_{x ∈ C} |x⟩⟨x| = I`. So `Ψ_{f,~}` is CPTP, and `Φ_t` is a convex combination
of CPTP maps with weights `ρ(E_t(·))` summing to `ρ(H) = 1`.

(3) `Ψ_{f,~}(|x⟩⟨x|) = |f(x)⟩⟨f(x)|`; summing with weights,
`Φ_t(|x⟩⟨x|) = Σ_b ρ{h : A_t(x,h) = b} |b⟩⟨b|`. Linearity extends this to every diagonal input.

(4) `F^0 = id` gives `Γ_0 = I`, and `Γ_t = Γ_0 Γ_t` with `Γ_t` row-stochastic (ρ is a probability),
so a failing pair `(s, t)` of CR `PDivisible` has `s ≥ 1`. Put `t_1 = s`, `t_2 = t`. If
`Φ_{t_2} = Λ ∘ Φ_{t_1}` with `Λ` positive and trace preserving, `M_{kj} = ⟨j|Λ(|k⟩⟨k|)|j⟩` is
row-stochastic and, by (3),
`Γ_{t_2}(i,j) = ⟨j|Λ(Σ_k Γ_{t_1}(i,k)|k⟩⟨k|)|j⟩ = Σ_k Γ_{t_1}(i,k) M_{kj}`, a stochastic divisor;
contradiction. This is Main's argument (M:334) verbatim; only (3) changed. ∎

**Dilation (Stinespring), Prop. 6.6 [W].** For each `t`, with `r_t(x,h) = min{y : y ~ x}` for a fixed
order of `V`, the map `(W_t|x⟩)(h) = |A_t(x,h)⟩ ⊗ |r_t(x,h)⟩` is an isometry
`ℂ^V → L²(H, ρ; ℂ^V ⊗ ℂ^V) = ℂ^V ⊗ L²(H,ρ) ⊗ ℂ^V`
(`⟨W_t y, W_t x⟩ = ρ{h : F^t(x,h) = F^t(y,h)} = δ_{xy}` by (H6.4)) and
`Tr_{L²(H,ρ) ⊗ ℂ^V}[W_t σ W_t^*] = Φ_t(σ)`. `L²(H,ρ)` is separable when `𝓗` is countably generated
(standard Borel). Because the integrand is finitely valued, a finite environment also suffices:
`W_t|x⟩ = Σ_π √ρ(E_t(π)) |f_π(x)⟩|π⟩|r_π(x)⟩` into `ℂ^V ⊗ ℂ^{patterns} ⊗ ℂ^V`. Both are per-time
dilations; a single unitary `U` with `Φ_t = Tr[U^t(σ ⊗ ω)U^{−t}]` for all `t` and a normal `ω` is
constructed below only for purely atomic `ρ`.

**Countable hidden carriers [W].** If `ρ` is purely atomic (countable support, finite or infinite) and
`F` injective on `V × H` with `H` countable, then on `ℓ²(V × H)` (separable) the operator
`U|x,h⟩ = |F(x,h)⟩` is an isometry (a unitary when `F` is a bijection), `μ_H = Σ_h ρ(h)|h⟩⟨h|` is a
normal diagonal state, and the computation of (1) gives `Tr_H[U^t(σ⊗μ_H)U^{*t}] = Φ_t(σ)`. Main's
Hilbert-space form therefore holds verbatim on countably infinite hidden carriers. The same holds for a purely atomic `ρ` on an uncountable `H` (`F` injective): with `S` the countable support of `ρ`, put `H_0 = S` and `H_{n+1} = H_n ∪ π_H F(V × H_n) ∪ π_H F^{−1}(V × H_n)` (preimages where they exist; countable because `F` is injective); then `H_∞ = ∪_n H_n` is countable, `F(V × H_∞) ⊆ V × H_∞` and `F^{−1}(V × H_∞) ⊆ V × H_∞`, so `U` restricted to `ℓ²(V × H_∞)` (separable) is an isometry, and a permutation unitary when `F` is a bijection; `μ_H` is supported in `H_∞`, and every point `F^t(x,h)` with `h ∈ S` that the computation of (1) uses lies in `V × H_∞`. The channel identity, CPTP and diagonal preservation need only the isometry (with `U^{*t}` for `U^{−t}`). (Added after review round 2.)

### 3.3 T6-K: the Koopman form named in REMAINDER

**Prop. 6.7 [W] (no normal diagonal hidden state on a diffuse carrier).** Let `ρ` have a non-zero
diffuse (non-atomic) part. No density operator `D` on `L²(H,ρ)` commutes with the multiplication
algebra `L^∞(H,ρ)` while being supported on the diffuse part. *Proof.* `L^∞(H,ρ)` is maximal
abelian on `L²(H,ρ)`, so a commuting `D` is a multiplication operator `M_g`. `D` is trace class,
hence compact; if `|g| > ε` on a set `B` of positive diffuse measure, `L²(B)` is infinite-dimensional
(non-atomic) and `M_g` is bounded below by `ε` on it, contradicting compactness. So `g = 0` on the
diffuse part. ∎ Consequently Main's proof step "a permutation unitary conjugates a diagonal state to
a diagonal state" (M:330), whose input `σ ⊗ μ_H` must be diagonal, has no normal-state analogue on
`L²(H,ρ)` for diffuse `ρ`; on `ℓ²(H)` with `H` uncountable the diagonal states are normal only for
atomic laws, and `ℓ²(H)` is non-separable (P1, P2).

**Countermodel (diagonal preservation fails for the Koopman form).** Take the Koopman unitary of `F`
on `ℂ^V ⊗ L²(H,ρ)` (unitary when `F` preserves `c ⊗ ρ`, `c` counting on `V`) and the normal hidden
state `|ψ⟩⟨ψ|`, `ψ` the normalized constant function — the canonical normal state whose restriction
to `L^∞(H,ρ)` is `ρ`. For the swap `F(x,h) = (h,x)` at `|V| = |H| = 2`, `ρ` uniform,
`Φ_1(|0⟩⟨0|) = [[1/2, 1/2], [1/2, 1/2]]` (K2(i), exact): not diagonal. The model lifts to a diffuse
carrier by T9(a): `H' = H × [0,1)`, `ρ' = u_H ⊗ Leb`, `F' = F × id`, `ψ' = ψ ⊗ 1`; the factor
`L²[0,1)` in the normal state `|1⟩⟨1|` is decoupled and normalized, so the channel is unchanged.
What is shown: the literal L6 ("Koopman dilation channel family on `ℂ^V ⊗ L²(H,ρ)` and its
diagonal preservation") fails for its canonical normal state, on finite and diffuse carriers; on
finite `H` it fails for every non-diagonal normal state (Prop. 6.9); on a carrier with a diffuse part
no diagonal normal state exists (Prop. 6.7). Not shown: that every non-diagonal normal state on
`L²(H,ρ)` with diffuse `ρ` fails for some `F` (plausible; OPEN). The object that generalizes Main's
family on every carrier is the mixture family of Theorem 6, which corresponds to the hidden
"definite probabilities" reading already used at Intro:111.

**Prop. 6.9 [W] (finite `H`: diagonal preservation for every permutation forces a diagonal prior;
added after review round 1).**
Let `H` be finite, `|V| ≥ 2`, and `μ_H` a density matrix on `ℂ^H` with `μ_H(h,h') ≠ 0` for some
`h ≠ h'`. Then some bijection `F` of `V × H` has `Φ_1(|0⟩⟨0|) = Tr_H[U(|0⟩⟨0| ⊗ μ_H)U^*]` not
diagonal. *Proof.* Fix `k ∈ H`; set `F(0,h) = (0,k)`, `F(0,h') = (1,k)`, and send the other points
`(0,g)` to distinct points `(0,k_g)` with `k_g ≠ k` (there are `|H| − 2 ≤ |H| − 1` of them); extend to
a bijection of `V × H`. Then
`⟨0|Φ_1(|0⟩⟨0|)|1⟩ = Σ_{g,g'} μ_H(g,g') [F(0,g) = (0,m), F(0,g') = (1,m) for some m]`, and the only
such pair is `(g,g') = (h,h')`, so the entry is `μ_H(h,h') ≠ 0`. ∎ With Main's lemma (M:328, a
diagonal `μ_H` is preserved by every permutation) this gives both directions separately (§A.34): on
finite `H`, every permutation dilation preserves diagonals exactly when `μ_H` is diagonal. (A scratch
exact check of the construction at `|V| = 2`, `|H| = 3` returned the off-diagonal entry `μ_H(h,h')`;
it is not a preregistered control and is not in `r6_controls.py`.)

**Lemma 6.8 [W] (CP theorem for the Koopman form at `|V| = 2`).** Let `|V| = 2`, `F` a bimeasurable
bijection preserving `c ⊗ ρ`, and `Φ^K_t(σ) = Tr_{L²}[U^t(σ ⊗ |1⟩⟨1|)U^{−t}]`. Then
`Φ^K_t(|0⟩⟨0|) − Φ^K_t(|1⟩⟨1|) = (1 − 2q_t) Z` with `Γ_t = (1 − q_t)I + q_t X`, and P-indivisibility
of `Γ` implies that no positive trace-preserving `Λ` has `Φ^K_{t_2} = Λ ∘ Φ^K_{t_1}`. *Proof.* With
`A_x = F^t({x} × H)`, `(U^t(|x⟩ ⊗ 1))(a,k) = 1_{A_x}(a,k)`, so
`⟨0|Φ^K_t(|x⟩⟨x|)|1⟩ = ρ{k : (0,k), (1,k) ∈ A_x}`. With `f = 1[(0,·) ∈ A_0]`, `g = 1[(1,·) ∈ A_0]`,
invariance gives `∫f + ∫g = (c⊗ρ)(A_0) = 1`, and `A_1` is the complement of `A_0`, so the `x = 1`
coherence is `∫(1−f)(1−g) = 1 − ∫f − ∫g + ∫fg = ∫fg`: the coherences agree. Invariance also makes
`Γ_t` doubly stochastic (M:280 remark), so `Γ_t = (1−q_t)I + q_t X` and the diagonal difference is
`(1−2q_t)Z`. For such matrices a stochastic divisor `Γ_{t_2} = Γ_{t_1}Λ` exists iff
`|1−2q_{t_2}| ≤ |1−2q_{t_1}|` (`Λ = (1−r)I + rX` with `1−2r = (1−2q_{t_2})/(1−2q_{t_1})`; for
`q_{t_1} = 1/2` both sides require identical rows). A positive trace-preserving `Λ` contracts the
trace norm of the Hermitian traceless difference: `|1−2q_{t_2}| ≤ |1−2q_{t_1}|`. ∎ K2 is consistent:
0 violations of the coherence identity over every searched `(F, t)` at `|V| = 2`, and 0 countermodels
in 244 728 exactly decided P-indivisible pairs (595 912 pairs with singular `Φ_{t_1}`, which the
lemma covers and the search did not decide). At `|V| = 3` (exploratory extension, added after the
preregistration and reported separately): 0 countermodels in 1 104 decided pairs, 3 312 undecided
(singular `Φ_{t_1}`) and 6 144 undecided (singular `Γ_{t_1}`) — OPEN.

### 3.4 Disguised-A1 test and pathologies

**Diffuse exhibit (K3b; added after the preregistration, which named only the Bernoulli model of
K3a).** `H = {0,1}^ℕ` with the fair Bernoulli (Haar) law, `F(x,h) = (x ⊕ h_0, odo h)`,
`odo` the dyadic odometer. `H` is uncountable, `ρ` non-atomic, `F` a bimeasurable bijection with no
periodic point, so no finite order or exact return anywhere. Exact on cylinders, `t ≤ 8`: every
`Φ_t` is CPTP and diagonal-preserving with populations `Γ_t`; `Γ_1 = [[1/2,1/2],[1/2,1/2]]`,
`Γ_2 = [[0,1],[1,0]]`, so `Γ` is not P-divisible on `{0,1,2}`, and `Φ_1` identifies the two diagonal
inputs while `Φ_2` separates them, so no linear `Λ` exists: CP-indivisibility exhibited on a carrier
with no finite structure. 𝒽6 passes the §3 test of the preregistration: (a) fails for this model,
(b) none of finite order, exact return or a uniform probability on the whole carrier is assumed, (c)
no hypothesis is a finiteness property renamed ((H6.3) holds on every standard Borel space).

**P witness (K3a).** The Bernoulli skew product `F(x,h) = (x ⊕ h_0, σh)` on `{0,1} × {0,1}^ℤ` has
`Γ_t = [[1/2,1/2],[1/2,1/2]]` for every `t ≥ 1` (exact, `t ≤ 8`) and is P-divisible on `{0, …, 8}`:
a non-permutation `Γ_1` on an infinite carrier does not by itself supply a P witness. The full
M9 chain therefore needs (NR) (M:131, already on `main`, paper) or RIGID's compactness
(`ObservableRigidity.exists_pIndivisibleWithin_of_nonPermutation`, Lean); K3b satisfies (NR) at
`(s,n) = (1,4)` (`Γ_4 = I`, K3 `NR_at_s1_n4`). Here **(RIG)** denotes RIGID's hypotheses as the
kernel states them: a bimeasurable bijection `T` of a measurable carrier preserving a probability
`μ` (for the product convention, `μ = ν ⊗ ρ`, `rootedFamily_productLaw`, ObservableRigidity.lean:388),
a finite readout `X` with positive root masses and `|V| ≥ 2`, and compact closure in `L²(μ)^V` of the
joint forward orbit of the cell indicators (`hcard`, `hcompact`, ObservableRigidity.lean:274–275);
the conclusion used is `exists_pIndivisibleWithin_of_nonPermutation` (:358). This compactness
supplies REC-1's subsequential rigidity, also written (RIG) in REMAINDER row M4.
(NR) is not disguised A1: K3b satisfies it with no
finite structure.

**Pathologies.** P1 (non-normal states): Theorem 6 uses no hidden density operator; `ρ` enters only
through `ρ(E_t(·))`. Prop. 6.7 shows why a density-operator formulation fails on diffuse carriers.
P2 (non-separable): avoided; the dilations above are separable under standard Borel `𝓗` or
finite-dimensional; `ℓ²(H)` for uncountable `H` is flagged and not used. P3 (non-measurable sets):
(H6.3) is exactly what makes `E_t(·)` measurable; without a measurable diagonal (e.g. a set of
cardinality above the continuum, or an uncountable set with the countable–cocountable σ-algebra)
`C_t(x,y)` can fail to be measurable and `Φ_t` is undefined; standard Borel excludes this.
In both diffuse exhibits (K3a, K3b) the hidden update does not read `x`, so every coincidence set is
all of `H`: they exercise (H6.3) and (H6.4) only trivially. Non-trivial coincidence sets and fibre
injectivity are exercised by K1 (finite carriers) and by the reviewer's independent check on
fibre-injective non-bijective maps (§12).

**Class.** T6 (i)–(iv): INF. P witness: WEAK, condition (NR) or (RIG). T6-K, diagonal
preservation, split by the reference state: (α) the constant-vector state is REFUTED on every
carrier, finite ones included; (β) a diagonal normal state gives a valid single-unitary form exactly
for purely atomic `ρ`, countably infinite ones included, and is undefined (not refuted) on a carrier
with a diffuse part (Prop. 6.7); (γ) on finite `H` every non-diagonal normal state fails for some
permutation (Prop. 6.9), and on diffuse carriers the corresponding claim is OPEN. (α) and (β) fall
outside the four preregistered classes (§12 D1). CP theorem for the constant-vector form: INF at
`|V| = 2` under `c ⊗ ρ` invariance, OPEN at `|V| ≥ 3`. M9 is served by Theorem 6, not by T6-K.

## 4. T7 — L7: physical-memory theorem on a measurable hidden space

### 4.1 Statement

**Hypotheses (𝒽7).** `V` finite, `n_V = |V| ≥ 2`; `(H, 𝓗)` any measurable space; random variables
`X_j ∈ V`, `H_j ∈ H` on one probability space; a Markov kernel `K(x, h; y)` (each `h ↦ K(x,h;y)`
measurable, `Σ_y K = 1`); **(M1) coupling-step model, integrated form:** for every `k`, every visible
history `x_{≤k}` with `P(X_{≤k} = x_{≤k}) > 0`, every `B ∈ 𝓗` and `y ∈ V`,
`P(X_{≤k} = x_{≤k}, H_k ∈ B, X_{k+1} = y) = ∫_B K(x_k,h;y) P(X_{≤k} = x_{≤k}, H_k ∈ dh)`;
a reference probability `π_H` on `H`, arbitrary. Write `μ_{x≤k} = P(H_k ∈ · | X_{≤k} = x_{≤k})`
(elementary conditioning on an event of positive probability) and
`TV(μ,π) = sup_{B ∈ 𝓗} |μ(B) − π(B)|`. For the quantitative form, (M0) `P(H_0 ∈ · | X_0 = x) = π_H`
for each `x` with positive mass, `T := K̄`, `T^{(k)}(x,y) = P(X_k = y | X_0 = x)`.

**Theorem 7 (L7) [W].** Under 𝒽7, with `ε ≥ TV(μ_{x≤k}, π_H)` for every positive-probability
history (resp. every history of length `1 ≤ j < k` for (e)):
(a) `‖P(X_{k+1} | x_{≤k}) − K̄_{x_k}‖_TV ≤ ε`, `K̄_x = ∫ K(x,h;·) π_H(dh)`;
(b) `‖P(X_{k+1} | x_{≤k}) − P(X_{k+1} | x_k)‖_TV ≤ 2ε`;
(c) for `ε ≤ 1 − 1/n_V`, `I(X_{<k}; X_{k+1} | X_k) ≤ 2[ε log(n_V − 1) + h(ε)]`;
(d) persistence form: `M_k > 0` forces `max_{x≤k} TV(μ_{x≤k}, π) ≥ ε_min(M_k, n_V)` **for every
probability `π` on `H`**;
(e) under (M0), `‖T^{(k)} − T^k‖_TV ≤ (k−1)ε` (M:459), with optimality inherited from the finite
example of M:469 as a special case.
(f) In (a)–(e), `TV` may be replaced by `TV_𝒢`, the distance of the restrictions to any
sub-σ-algebra `𝒢` for which every `h ↦ K(x,h;y)` is `𝒢`-measurable (the read σ-algebra), and
`TV_𝒢 ≤ TV`.

### 4.2 Proof [W]

**Lemma 7.0 (kernel contraction).** For probabilities `μ, π` on `H` and a kernel `K` into finite `V`:
`½ Σ_y |∫ K(h;y)(μ − π)(dh)| ≤ TV(μ, π)`. *Proof.* `Δ = μ − π` has `Δ(H) = 0`; by the Hahn
decomposition `|Δ|(H) = 2Δ^+(H) = 2 TV(μ,π)`, and
`½ Σ_y |∫ K(h;y) Δ(dh)| ≤ ½ Σ_y ∫ K(h;y) |Δ|(dh) = ½ |Δ|(H)`. If each `K(·;y)` is `𝒢`-measurable,
`∫ K dΔ = ∫ K d(Δ|_𝒢)`, giving (f). ∎

(a) By (M1), `P(X_{k+1} = y | x_{≤k}) = ∫ K(x_k,h;y) μ_{x≤k}(dh)`; Lemma 7.0 with `π = π_H`.
(b) `P(· | x_k)` is a convex combination of the `P(· | x_{≤k})` over positive-probability histories
ending at `x_k`, so it is within `ε` of `K̄_{x_k}` by convexity of `TV`; triangle inequality.
(c) `I = E[H(P(·|X_k)) − H(P(·|X_{≤k}))]`; both laws are within `ε` of `K̄_{X_k}`, and the classical
Fannes–Audenaert bound `|H(p) − H(q)| ≤ δ log(n_V − 1) + h(δ)` for `TV(p,q) ≤ δ ≤ 1 − 1/n_V`,
monotone in `δ` there, gives each term at most `ε log(n_V−1) + h(ε)`. This step uses finite `V` only.
(d) (a)–(c) hold for every `π`; take `ε` the realized maximum; the existence and range of `ε_min` are
as at M:473.
(e) `T^{(j+1)}(x_0,y) − (T^{(j)}T)(x_0,y) = Σ_{x_1..x_j} P(x_1..x_j | x_0)[(μ_{x≤j}K_{x_j})(y) −
(π_H K_{x_j})(y)]`, whose row TV is at most `Σ P(·) TV(μ_{x≤j}, π_H) ≤ ε` by Lemma 7.0; (M0) gives
`T^{(1)} = T`; telescoping through `A_j = T^{(j)}T^{k−j}` and right-multiplication by a stochastic
matrix (a contraction of the max-row TV norm) gives the bound, as at M:469. ∎

Every sum over `h` in Main's proofs becomes an integral against a finite signed measure; no
regular conditional distribution is needed because `V` is finite and only positive-probability
visible histories are conditioned on. The phrase "given … `H_k = h`" (M:473) conditions on a point
event, null for diffuse laws; (M1) is its integrated form and is the hypothesis that should be
stated on a measurable carrier (P3).

### 4.3 Disguised-A1 test, observations

**Diffuse exhibit.** K3a's Bernoulli skew product with `K(x,h;y) = [y = x ⊕ h_0]`, `π_H` the
Bernoulli law: 𝒽7 holds on an uncountable carrier with a non-atomic law; no finite structure is
assumed. 𝒽7 passes the test. **Class: INF** (all parts).

**Observation 7.1 [W] (no reference-law selection).** By (d) the persistence form needs no choice of
`π_H`: positive conditional memory bounds the TV-radius of the set of realized hidden conditionals
about every probability on `H`. Unlike M1/M2 (REMAINDER R1), the physical-memory theorem consumes no
selected hidden law.

**Observation 7.2 [W] (timescale form).** (i) If between couplings the hidden sector evolves by a
bimeasurable bijection `S` preserving `π_H`, then `TV(S_*μ, π_H) = TV(S_*μ, S_*π_H) = TV(μ, π_H)`
(a bimeasurable bijection preserves `TV` between any two laws), on finite and infinite carriers alike: full-TV relaxation never occurs
under exact reversible hidden dynamics. (ii) For `TV_𝒢` with `𝒢` generated by a finite partition and
`S` mixing for `π_H`, `μ ≪ π_H` gives `TV_𝒢(S^n_*μ, π_H) → 0` (mixing applied to `dμ/dπ ∈ L¹` against
the finitely many atoms). A permutation of a finite set preserving `π_H` is mixing for `π_H` only if
`π_H` is a point mass: if its support has more than one point, the permutation has finite order `N`
and `S^N = id` precludes mixing.
So the timescale (slow-bath) form of M:473 read through (f) has an exact mechanism on infinite
carriers with mixing hidden dynamics and only an approximate one on finite representatives
(consistent with M:451, "For a finite reversible realization there is no relaxation in the strict
sense"). This is an elaboration; it changes no consumer's class.

## 5. T9 — L9: decoupled factors of any cardinality

**(a) Coherent form [W].** Hypotheses: a base given by Hilbert spaces `ℂ^V`, `K_H` (any), a normal
state `ω_H`, a unitary or isometry `U` on `ℂ^V ⊗ K_H` (with `U^{*t}` for `U^{−t}`) — this includes
Main's finite family and the countable and purely atomic forms of §3.2; a factor Hilbert space `K_A` of any dimension (separable or not), a state `σ_A` with
`σ_A(1) = 1`, and any unitary or isometry `W` on `K_A`. Claim: for every `t` and visible input `ρ_V`,
`Tr_{HA}[(U⊗W)^t(ρ_V ⊗ ω_H ⊗ σ_A)(U⊗W)^{*t}] = Tr_H[U^t(ρ_V ⊗ ω_H)U^{*t}]` when `σ_A` is normal; in
the Heisenberg form the same identity holds for every state `σ_A`. *Proof.* `(U⊗W)^t = U^t ⊗ W^t`;
for trace-class `X` and `Y`, `Tr_A(X ⊗ Y) = X · Tr Y`, and `Tr(W^tσ_AW^{*t}) = Tr(σ_A W^{*t}W^t) = 1`.
Heisenberg: `(U⊗W)^{*t}(Z ⊗ 1_H ⊗ 1_A)(U⊗W)^t = (U^{*t}(Z⊗1)U^t) ⊗ 1_A`. For a non-normal `σ_A`
the product functional `ω ⊗ σ_A` (with `ω` the normal state `ρ_V ⊗ ω_H` composed as in the base) is a
state on the minimal C*-tensor product `B(ℂ^V ⊗ K_H) ⊗_min B(K_A)`; it extends to the von Neumann
tensor product by Hahn–Banach, not uniquely, but every extension takes on `Y ⊗ 1_A` the value
`ω(Y) σ_A(1) = ω(Y)`, which is all the identity uses. ∎

**(e) Hybrid form [W].** A Hilbert-space factor adjoined to the mixture base of 𝒽6 on any (including
diffuse) carrier: with `K_A`, a normal `σ_A` and a unitary or isometry `W` as in (a), define
`Φ'_t(σ) = Tr_A Σ_π ρ(E_t(π)) (Ψ_π ⊗ Ad_{W^t})(σ ⊗ σ_A)`. Since `Tr_A Ad_{W^t}(σ_A) = 1`,
`Φ'_t = Φ_t`. This is immediate from the definitions; it covers Step-2 #10–#13 for a quantum factor
on a diffuse base.

**(b) Classical form [W].** Hypotheses: base as 𝒽6; factor `(A, 𝒜, α)` with `α` a probability and
`W : A → A` any measurable map (injectivity not needed). Claim: the mixture family and the rooted
family of `F × W` under `ρ ⊗ α` equal those of `F` under `ρ`. *Proof.* `(F×W)^t(x,(h,a)) =
(A_t(x,h), (K_t(x,h), W^t a))`: fibre injectivity holds, the coincidence set is `C_t(x,y) × A`, so
every pattern set is `E_t(π) × A` and `(ρ⊗α)(E_t(π) × A) = ρ(E_t(π))`; likewise
`(ρ⊗α){(h,a) : A_t(x,h) = b} = Γ_t(x,b)`. ∎

**(c) Relabelling (Theorem 24(i)) on a measurable carrier [W].** For a bimeasurable bijection `σ`
of `H` and `π(v,h) = (v, σh)`, `F' = πFπ^{−1}` has pattern sets `E'_t(π) = σ(E_t(π))`, so
`Φ'_t[ρ] = Φ_t[(σ^{−1})_*ρ]`: the family is unchanged when `σ` preserves `ρ`. For fibre-dependent
`σ_v` each preserving `ρ`, `Γ'_t(x,b) = ρ(σ_x{h : A_t(x,h) = b}) = Γ_t(x,b)`. Without
ρ-preservation the conclusion fails: K4, `F(x,h) = (x ⊕ [h < 1/2], h)` on `[0,1)` with Lebesgue
measure and `σ(h) = h²` changes `Γ_1` from `[[1/2,1/2],[1/2,1/2]]` to `[[3/4,1/4],[1/4,3/4]]`, while
the Lebesgue-preserving reflection leaves it unchanged (K4 evaluates hand-derived interval
preimages exactly; it is arithmetic, not an independent search). On finite `𝒞_H` every bijection
preserves the uniform prior, which is why Sub:253 needs no condition. **Class: WEAK** (σ preserves
ρ; passes the test, the reflection of `[0,1)` being an exhibit).

**(d) Exact transfer [W].** By (a) and (b), every statement expressible through the fixed-interface
family `{Φ_t}` or `{Γ_t}` transfers exactly between the base and its extension by such a factor at
every time. Example: a finite base with `F^L = id` has `Φ_L = id`; adjoining `A = ℤ`, any
probability `α` on `ℤ` and `W(a) = a + 1` gives a total system on an infinite carrier with no
periodic point and no invariant probability of the form `ρ ⊗ α`, whose visible family still has
`Φ_L = id`. Exact visible return therefore implies neither recurrence, nor finiteness, nor an
invariant law of the total system, which sharpens Sub:268's "it does not imply recurrence of every
unobserved sector".

**Disguised-A1 test and pathologies.** Exhibits: `K_A = L²[0,1)` with `|1⟩⟨1|`; `(A, α) = ([0,1), Leb)`.
P1: (a) states the normal requirement for the Schrödinger form and admits non-normal states in the
Heisenberg form. P2: `K_A` may be non-separable; nothing in the proof uses separability. P4: the
normalization `σ_A(1) = 1` (resp. `α(A) = 1`) is used exactly once, as the factor `Tr σ_A`; for an
unnormalizable "uniform" factor (`I` on infinite-dimensional `K_A`, counting measure on infinite
`A`) that factor is `+∞` and the identity is undefined, so these are excluded by hypothesis.
**Class: (a), (b), (d), (e) INF; (c) WEAK.** Coupled infinite deep sectors are not covered (GR Appendix
B, finite windows; H-BD at leading order) and are not claimed.

## 6. Controls (from `r6_controls.json`, schema `a1exit-r6-controls/1`, `all_pass: true`)

| Id | Outcome |
|---|---|
| K1 | PASS: 26 352 exact comparisons (every bijection at `(2,2)`, `(2,3)`, `(3,2)`, three rational priors including non-uniform and degenerate, `t ≤ 6`): 0 mismatches between the pattern sum and Main's partial trace; every mixture channel CPTP and diagonal-preserving with rooted populations |
| K2 | PASS (internal: Koopman populations equal rooted maps in every case). (i) swap: off-diagonal `1/2` — diagonal preservation fails. (ii) preregistered search `(2,2)`, `(2,3)`, `(2,4)`, `t ≤ 12`: 840 640 P-indivisible pairs, 244 728 decided, 0 countermodels, 595 912 undecided (singular `Φ_{t_1}`); 0 violations of Lemma 6.8's coherence identity. (iii) exploratory `(3,2)`, `t ≤ 8`: 4 416 P-indivisible pairs, 1 104 decided, 0 countermodels |
| K3 | PASS. K3a Bernoulli: CPTP, diagonal-preserving, `Γ_t = J/2` for `t = 1, 2, …`, P-divisible on `{0,…,8}`. K3b odometer: CPTP, diagonal-preserving, `Γ_2 = X`, `Γ_4 = I`, (NR) holds at `(1,4)`, not P-divisible at `(1,2)`, no linear divisor of the mixture channels there |
| K4 | PASS: `σ(h) = h²` changes `Γ_1`; reflection does not |

Decision rule application (PREREG §4): K1 green, so T6's INF class stands. K2: no countermodel at
the preregistered sizes, which Lemma 6.8 explains at `|V| = 2`; recorded, not used as a proof.

## 7. Step-2 manuscript corrections (queued; not applied; each needs its own authorization)

Generalizations required for A1-EXIT if the classifications are accepted (sites that state as
unproved, or as finite-only, a result now proved; true as written but stale for the objective):
**G**. Precision defects in the current text, evidenced here: **P**. Consequential edits that become
necessary only if a G item is applied: **G′**. Optional generalizations, not needed by A1-EXIT
unless Step 2 chooses them: **O**. Each needs §A.25
propagation to its mirrors.

| # | Site | Kind | Correction |
|---|---|---|---|
| 1 | M:328 Lemma (diagonal preservation) | P | State that `μ_H` is the diagonal density matrix of a hidden probability; for every non-diagonal `μ_H` some permutation breaks the lemma (Prop. 6.9; K2(i) for the constant vector) |
| 2 | M:328–334 | G | Add the measurable-carrier form: for a probability `ρ` on a measurable hidden space with measurable coincidence sets and a fibre-injective measurable `F`, the family `Φ_t(σ) = ∫ Ψ_{π_t(h)}(σ) ρ(dh)` (equal to the displayed family on finite `H`) is CPTP and diagonal-preserving with populations `Γ_t` of M:131, and the CP-indivisibility theorem holds for it with the P witness of the (NR) corollary (M:131). Any remark on the Koopman form states only what is shown: the constant-vector normal state fails, and no diagonal normal state exists on a diffuse part |
| 3 | M:60 status Remark, list of results resting on the finite representative ("the CP-indivisibility theorem of §3.2") | G | The CP theorem uses the finite representative only through its P witness; under (NR) it holds on measurable carriers |
| 4 | M:732 item (ii), "the CP-indivisibility theorem of §3.2, the physical-memory theorem of §3.4 … are statements about finite representatives" | G | Remove both from that list; add (NR) as the weaker condition for the CP theorem's P witness, as already done for §2.3 |
| 5 | M:742 table row "CP-indivisibility of `{Φ_t}`" | G | "Proved for the hidden-prior (diagonal-preserving) channel family on finite or measurable hidden carriers; …" |
| 6 | AppB:92 and FULL:5769 Theorem B.2.5 "(from a non-permutation rooted map and finiteness)" | G | "… and finiteness, or the near-return condition (NR)"; proof's "permutation dilations with uniform ancilla" extended as in #2 |
| 7 | M:459 Theorem (C2 necessity, quantitative) "Model one coupling step as the uniform-prior bijection marginal" | G | A measurable coupling step on a measurable hidden space with reference probability `π_H` (uniform in the finite model), (M0) for the first step |
| 8 | M:473 Theorem (physical memory) "given the whole visible past and `H_k = h`"; `K̄ := Σ_h π_H(h)K` | G + P (the conditioning on `H_k = h`) | State (M1) in integrated form; `K̄ = ∫ K π_H(dh)`; any measurable hidden space |
| 9 | M:473 contrapositive | O | Persistence form for every reference probability (Theorem 7(d)); read-σ-algebra form (f) |
| 10 | M:60 ("A finite factor adjoined …; … an infinite hidden sector, are outside that statement") | G | A factor of any cardinality, prepared independently in a normalized state or law and evolved by its own dynamics, leaves every visible channel unchanged; a coupled deep sector stays outside |
| 11 | M:732 item (ii) ("when that sector is a finite factor … evolved by its own permutation"; "by such a finite decoupled enlargement") | G | As #10 |
| 12 | Sub:257–262 Theorem 24(iii), with its proof at Sub:266, title and the sentence "This is a finite, fixed-interface result; an infinite extension requires its own normalized measure or trace-class state and a well-defined evolution, and is not established by finite uniform counting" | G | Statement for a factor Hilbert space of any dimension, normalized (normal) state, unitary or isometric dynamics; classical form; unnormalizable factors excluded |
| 13 | Sub:268 Corollary (iii) "Infinite extensions need a separately specified normalized state or measure and dynamics before any such comparison can be made" | G | Transfer holds for normalized decoupled factors of any cardinality; add the T9(d) example only if wanted (O) |
| 14 | Sub:92 (A1 entry: "Theorem 24(iii) gives an exact freedom to adjoin independently prepared finite decoupled factors … Infinite extensions require specified normalized measures or states and well-defined dynamics; the finite identity does not supply that construction") | G | As #12 |
| 15 | ch02:144 and FULL:774 ("Infinite factors require a separately specified normalized state or measure and well-defined dynamics; finite uniform counting does not supply that extension") | G | As #12 |
| 16 | Sub:50, Sub:54, Sub:60, Sub:201; Str:154; Meth:467; Complexity:206; ch02:28, ch02:134, ch03:80, ch03:142, ch04:172, appendix-c:106 and their FULL mirrors (FULL:658, 764, 941, 1003, 1276, 6261) | O | Each says "finite" decoupled factor; true as written. Generalize only if Step 2 chooses to; otherwise no edit (§A.25 minimal change) |
| 17 | Sub:253 Theorem 24(i) | O | Measurable form: relabellings preserving the hidden law |
| 18 | M:336 Remark (scope: P-indivisibility is not quantum non-Markovianity), "the framework's channels are in that class" | G′ (with #2) | Include the measurable mixture family in "the framework's channels" |
| 19 | Str:53 ("infinite or boundary-coupled extensions are not covered ([Substratum §4, Theorem 24(iii)])") | G′ (with #12) | Infinite normalized decoupled factors covered; boundary-coupled stay outside |
| 20 | ch02:32 and FULL:662 ("An infinite extension requires its own normalized state or measure and well-defined dynamics"); ch02:44 and FULL:674 ("Infinite extensions require specified normalized states or measures and dynamics") | O | True as written (L9 needs a normalized state or law); may add that, once specified and decoupled, they leave the channel unchanged |
| 21 | Meth:353, ch03:220 and FULL:1081 ("finite" decoupled factor) | O | True as written; as #16 |

Sites checked and needing no change: Intro:111 ("whose hidden part starts with definite
probabilities") already states the diagonal premise; GR:138 (recurrence-scale P-indivisibility
for an infinite deep sector, via the readback lemma and (NR)) and ch18:192 (an infinite deep hidden
sector needs its own normalized state or measure and dynamics) are true as written; Main:74, :97, :182, :636, :744, Sub:129, :137 and glossary:27, :39 cite the
physical-memory theorem without a finiteness clause.

## 8. Gem-finding record (§A.31)

Productivity test (fixed here before the branches were walked in §§3–5, after the preregistration):
a gem is a fact strictly stronger than "the proof generalizes" that constrains a consumer or exposes
a hidden assumption.

- **NEW — assumption-watch marker AW-R6-1 (definite hidden prior).** Main's diagonal lemma (M:328)
  depends on the hidden reference being diagonal ("definite probabilities", Intro:111). On a diffuse
  hidden carrier no normal state has that property (Prop. 6.7), the canonical normal choice breaks
  diagonal preservation (K2(i)), and on finite `H` every non-diagonal normal state does (Prop. 6.9).
  A generalization of the §3.2 channel apparatus that holds on every carrier is the classical mixture
  over hidden points (Theorem 6); whether some non-diagonal normal state on a diffuse carrier preserves
  diagonals for every `F` is open (expected not).
  Cross-propagation: any result that uses the unitary realization `(𝓗_H, U_φ, ρ_H)` with
  `ρ_H = I_m/m` (M:286; the uniqueness statements of [Structure] Props. 9.7a–9.7b that M:286 says
  depend on it) inherits this marker; R6 does not audit them.
- **ELABORATING — Lemma 6.8.** For `|V| = 2` the Koopman form's coherences cancel in the difference
  of diagonal outputs, so the CP theorem survives the loss of diagonal preservation there.
- **ELABORATING — Observations 7.1, 7.2.** The physical-memory theorem consumes no selected hidden
  law; full-TV relaxation is impossible under exact reversible hidden dynamics, finite or infinite,
  and read-σ-algebra relaxation is exact under mixing only on infinite carriers.
- **ELABORATING — T9(d).** Exact visible return does not imply total recurrence, finiteness or an
  invariant law.
- **CONFIRMING — T6.** No invariance, bijectivity or recurrence is used by the channel family; the
  only finiteness that remains in M9's chain is the P witness, already covered by (NR).

Favorable branches were pressure-tested (§A.31): the T6 INF reading was checked against the literal
L6 phrasing (false for the constant-vector state; the diagonal-normal-state form holds only on
purely atomic laws; §3.4 Class, §12 D1) and against the P-witness premise
(K3a shows it is not free).

## 9. Lean candidacy (not built)

| Item | Candidate? | Shape |
|---|---|---|
| T6 (2)–(4) | Yes | Finite pattern sum with weights `(ρ : Measure H).real (E_t π)`; Kraus form of each pattern channel; diagonal entries equal `ObservableRigidity.rootedFamily`-style masses; the CP step reuses `CausalReadback.PDivisible` with `Λ` only positive and trace-preserving. Coincidence-set measurability as a hypothesis |
| T6 Lemma 6.8 | Possible | 2×2 algebra plus one measure identity |
| T7 (a), (b), (e), (f) | Yes | `ProbabilityTheory.Kernel`, Hahn decomposition of a signed measure; (c) needs a Fannes–Audenaert lemma not in Mathlib (heavier) |
| T9 (b) | Yes, easiest | Near copy of `rootedFamily_productLaw` (`Measure.prod_prod`, `measure_univ`) |
| T9 (a) | No (now) | Infinite-dimensional partial trace on trace-class operators is not available in Mathlib |

## 10. Off-`main` references (§A.42 item 8)

| Reference | Attached claim | Classification |
|---|---|---|
| #1169 comment 7047514209 | authorization, goal link | provenance (owner record, quoted) |
| #1454, #1169 (Issues) | accountable planning | provenance |
| `8fb6b663` (PREREG commit on this branch) | that the rule preceded classification | support, not provenance: the claim depends on commit order. It is on `main` only if the PR lands by a merge commit that keeps `8fb6b663` and `62a4332b` reachable; a squash or rebase landing would leave it unsupported |
| this branch and its draft PR | tracking | provenance |

Every proof, control and cited result used above is in this directory or on `main` at the pin
(REMAINDER, RIGID, MREC, CR, Main, Substratum, GR, the book files). No support off `main`.

## 11. What an independent reviewer must check

1. That `PREREG.md` is unchanged since `8fb6b663` and preceded this file; that the extension at
   `|V| = 3`, the odometer exhibit K3b, Prop. 6.9 and the gem-finding productivity test are labelled
   as added after it.
2. Theorem 6: pattern-set measurability from (H6.3); fibre injectivity ⇒ injectivity of `f` on
   classes ⇒ TP; the CP step uses only positivity and trace preservation of `Λ`; `s ≥ 1`.
3. That the mixture family is the correct generalization of Main's family (K1 and the computation
   in 3.2(1)), and that Main's `μ_H` is diagonal by the setup's identification (M:268).
4. Prop. 6.7 (MASA commutant, compactness on a diffuse part) and the swap countermodel's lift.
5. Lemma 6.8, including the double-stochasticity input and the singular case `q = 1/2`.
6. Theorem 7: Lemma 7.0; that (M1) is the right integrated form of M:473's model; Fannes–Audenaert
   range and monotonicity; the telescoping in (e) and the role of (M0).
7. T9(a) Heisenberg form for non-normal states; (b) coincidence sets `C_t × A`; (c) the K4
   countermodel; (d) the non-recurrent example.
8. That no hypothesis is disguised A1 (exhibits K3a, K3b, `[0,1)`, `L²[0,1)`), and that the WEAK
   conditions ((NR)/(RIG), ρ-preservation) each do work (K3a, K4).
9. Step-2 list completeness: re-grep "CP-indivisib", "physical-memory", "physical memory",
   "finite factor", "finite decoupled", "decoupled finite", "Infinite extensions", "Infinite
   factors" across `papers/` and `book/` (including FULL); confirm M/P/O assignments.
10. Re-run `r6_controls.py` and compare with `r6_controls.json`.

## 12. Answer to the review of `62a4332b` (round 1, REVISE, record only)

| Item | Answer |
|---|---|
| B1 | The T6-K row is split (§1, §3.4 Class): (α) constant-vector state REFUTED on every carrier; (β) diagonal normal state valid exactly for purely atomic laws and undefined on diffuse ones; (γ) other non-diagonal normal states refuted on finite `H` (Prop. 6.9), OPEN on diffuse carriers. **D1 (deviation from the preregistered rule):** the rule's four classes (INF, WEAK, FIN, OPEN) have no class for a target false on finite carriers ((α)) or for a target whose object does not exist on part of the infinite domain ((β)); both are recorded outside the classes rather than forced into FIN. The rule is not amended; the gap is recorded here |
| B2 | Narrowed at §3.3, §8 (AW-R6-1) and Step-2 #1, #2 to what is shown; the finite-`H` proof is added as Prop. 6.9; the diffuse case is stated as open |
| Nit 1 | K3b labelled as added after the preregistration (§3.4) |
| Nit 2 | (RIG) defined with its kernel locations (§3.4) |
| Nit 3 | Step-2 kinds re-marked: G (generalization required for A1-EXIT), P (#1 and the conditioning in #8), G′, O |
| Nit 4 | Rows #18–#21 added; the reason for leaving GR:138 and ch18:192 unchanged corrected |
| Nit 5 | Hybrid form T9(e) added |
| Nit 6 | Non-normal Heisenberg form stated on the minimal C*-tensor product, with the non-unique extension (§5(a)) |
| Nit 7 | Observation 7.2(ii) requires a support of more than one point |
| Nit 8 | `8fb6b663` reclassified as support; landing by merge commit required (§10) |
| Nit 9 | Trivial coincidence sets of K3a/K3b noted (§3.4) |
| Round 2 | Prop. 6.9 labelled as added after review; §3.2 countable-carrier construction extended to purely atomic laws on uncountable `H` via the countable set `H_∞` closed under `F` and `F^{−1}`; final-head check: the closure now includes preimages, so the restriction is a permutation unitary when `F` is a bijection, and the channel identity is stated to need only the isometry; T9(a) admits an isometric base `U` accordingly |

No class confirmed by the review changed. `PREREG.md`, `r6_controls.py` and `r6_controls.json` are
unchanged by this revision.
