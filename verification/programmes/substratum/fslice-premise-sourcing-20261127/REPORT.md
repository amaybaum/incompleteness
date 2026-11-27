# FSLICE-PS-1: can N-2, N-8 and N-9 be sourced from native OI dynamics? Report

**WIP / UNVERIFIED. Model-written research record, paper-only, pending independent review. No
premise is adopted, weakened or changed (§A.29, §A.50 item 6). Nothing is proposed for the
manuscripts.**

- **Plan:** `PLAN.md` in this directory, commit `158f4155c9b80f220bb6543b11e04497c3ec0328`,
  committed alone before this report. No deviation from its rule, controls or stopping
  conditions.
- **Accountable Issue:** #1217; programme #1169. Work package, authorization and Goal link are as
  in PLAN.md: WP-2, and #1169 comment 7208939261 (amaybaum, 2026-11-27T03:22:49Z).
- **Pinned main commit [P]:** `13c05b4fe666c2e128eed1213874be9b8208982d`.
- **Labels:**
  - [A]: exact hand algebra here;
  - [W]: reasoning here;
  - [P]: text quoted at [P];
  - [FS], [L2], [A-rec], [C3], [SMD-SRC]: results of the input records of PLAN §1. These are
    model-reviewed paper derivations, used as named conditional inputs (§A.46 item 7).
- **Evidence layer:** mathematical derivation on paper. No computation was run, and no Lean was
  built.

## 0. Summary

| Question | Class (PLAN §4) | Decisive argument |
| --- | --- | --- |
| Q2: N-2, label-independent J (LI) | **R:** reduces to H-PF, read with its positive-frequency clause. **I** if that clause is dropped | H-PF names the positive-frequency J_F = D(−D²)^(−1/2) of the update F ([L2] §2.1, §5, §6), which on V_rest is a single operator, independent of the label. Proposition P's slice-dependent pairs are not positive-frequency for F. Read with respect to F², the positive-frequency structure is not tamed (§2.2). Without the clause, Proposition P's family meets every remaining premise |
| Q8: N-8, centred reading φ = Φ_n ∘ P_rest | **R:** reduces to H-PF, with its positive-frequency clause read as a property of φ along trajectories. **I** under the formula-only reading (ρ_W) | Lemma PF [A]: a real-linear φ that equals Φ_n on V_rest and is positive-frequency along every trajectory of the support vanishes on the static labels, which oscillate at frequencies 0 and π. The formula's natural extension H-PF_u is not positive-frequency (§3.3) |
| Q9: N-9, SMD on the full law | **I** on every carrier, without the label-sector reading (ρ_T), and on even L under every reading (ρ_P, new). **R** (to SMD on the fluctuation law) only under the label-sector reading on sectors with zero staggered label, which includes every sector on odd L | ρ_T and ρ_P meet every stated premise, every carried premise, N-2, N-8 and SMD on P_rest∗ρ, and violate N-9 (§4) |

**Routes closed or conditional for N-9 (§4):**
- Main's measure selection gives a custodially scalar state, so Theorem 5 is vacuous on it.
- Extremality makes the labels deterministic, but by [A-rec] Proposition B no extremal state on T
  realizes Theorem 5's conclusion.
- A jointly Gaussian stationary state satisfies N-9 [A]. Joint Gaussianity is unstated and stronger
  than SMD.

**Outcome against the rule (PLAN §4).**
- **Native derivation:** no N_k is class D, so none is derived from native OI dynamics.
- **Independence:** at least one N_k remains an independent premise. N-9 is class I under every
  admitted reading on carriers with even L; on odd L it is class I except under the label-sector
  reading.
- **Reductions:** N-2 and N-8 are not additional to the carried bridge premise H-PF when H-PF is
  read with its own positive-frequency clause. H-PF itself remains unsourced.

All controls are green (§5).

**What it would change.**
- Under the positive-frequency reading of H-PF, the candidate-premise set of F-slice R2 shrinks
  from {N-2, N-8, N-9} to {N-9}.
- N-1 (the extension reading) and H-PF remain.
- This is a finding for the owner. No status is changed.

## 1. Setting and carried conditions

The setting is that of [FS]:
- carrier T = (Z/L)^d at αμ = 1/d, M = μI_6, b_A1 = 0;
- V = V_0 ⊕ V_π ⊕ V_rest, with stationary support L_0 ⊕ V_rest (link 9 of [FS] §2);
- P_rest is the spectral projection;
- J_F is defined on V_rest;
- Φ_n(y) = ℓ_n(y) − iℓ_n(J_F y);
- R_ext = id on V_null ⊕ R(w) on V_rest.

**Carried conditions C*:** LIN, LIFT, b_A1 = 0, L-SDS, lane 2's Theorem 1, H-link, H-cust, H5,
H-PF, TPC, and SMD on P_rest∗ρ. Of these:
- LIN is posited (A5).
- LIFT and the SM:232 bridge are open.
- The rest are unstated in the papers ([A-rec] §2, §5).

The state is "a hypothesis on the solution rather than a consequence of the dynamics" (SM:136
[P]).

## 2. Q2: N-2, label independence

### 2.1 Routes from the stated structure

- **R2.1, the native structure.** [FS] Proposition P gives a one-parameter family (J_t, J_{−t}) of
  tamed complex structures on the two slices of a staggered label sector. The family is
  intertwined by F and the translations. Neither the stated premises nor taming exclude it
  (countercontrol N-a).
- **R2.2, naturality under the symmetries of F.** The staggered shift τ_c relates the two slices,
  and it is not a symmetry of F: τ_c⁻¹ F τ_c x = Fx − 2cv ([C3] §5.2). Equivariance of J under the
  symmetries of the dynamics therefore cannot identify the structures on S_+ and S_− [A]. The
  constant shift σ_c is a symmetry, but it only relates c-sectors. Each of those is a single
  F-invariant slice, on which J is already J_F.
- **R2.3, the custodial action.**
  - P2a's covariance Φ^J(R(w)x) = wΦ^J(x), for R(w) = I⊗X + K⊗Y, forces K = J [A]. Expanding
    both sides gives ℓ_n(Kx) = ℓ_n(Jx) and ℓ_n(JKx) = −ℓ_n(x) for every n.
  - The slice-dependent actions R_±(w) = I⊗X + J_±⊗Y form a group action on the support that
    commutes with F and the translations, since F J_± = J_∓ F. So P1 and P2e do not force LI either
    [A].
  - P2a is in any case a step Theorem 5 needs (countercontrol N-d), so it could not supply a class D
    or R.

**Class D:** none found.

### 2.2 Reduction to H-PF [A]

H-PF is "SM's φ is the J-linear positive-frequency field Φ of the real lift" ([L2] §5). [L2]
identifies that J as "the positive-frequency J_F = D(−D²)^(−1/2)" (§6, item 1), "+i on the
eigenvectors of F with eigenvalue e^{iθ}, θ ∈ (0, π), and −i on their conjugates" (§2.1).

1. **J_F does not depend on the label.** On the F-slice the deviation dynamics on V_rest is F for
   every label ([FS] §3.1). So D = (F − F⁻¹)/2 on V_rest, and with it J_F, is one operator,
   independent of the label.
2. **The family is not positive-frequency for F.** On E = P ⊕ N ([FS] §3.3), P is F-positive at k
   and N is F-negative at k + π. J_t = iS_t with S_t ≠ diag(1, −1) for t ≠ 0. So J_t is not +i on
   the F-positive vectors of N's conjugate partner, and is not J_F's sign pattern.
3. **The F² reading is not available.** Read with respect to the slice-preserving dynamics F², the
   positive-frequency structure J_{F²} is not tamed:
   - for θ ∈ (π/2, π), an F-positive vector z has F²-eigenvalue e^{2iθ}, with 2θ ∈ (π, 2π);
   - so J_{F²} = −i on z;
   - its Krein sign h(z, z) = 2iω(z, z̄) > 0 ([L2] Theorem 1);
   - so ω(J_{F²}x, x) = Re h(−z, z) < 0 for x = z + z̄.

   Taming therefore excludes the F² reading. Every tamed positive-frequency reading gives J_F.
4. **The carrier structure is the same J.** H-PF identifies the carrier's complex structure (H6-M)
   with the J of φ on phase space. This is the meaning of "J-linear", not P2a's covariance. So the J
   of H6-Φ is J_F, and LI holds.

**Direction (§A.34):** H-PF, with its positive-frequency clause, implies N-2. The converse is not
claimed.

**If the clause is dropped,** so that φ is merely "J-linear for a tamed J commuting with the
dynamics on each slice", Proposition P's family meets every remaining premise, and N-2 is class I.

**Class of Q2:** R (H-PF, positive-frequency clause); I without the clause.

## 3. Q8: N-8, the centred reading

### 3.1 Routes from the stated structure

- **R8.1, the native interface.** At Main's specified partitions the observer registers site values
  ([C3] §4.1), and these contain the labels. Theorem 5's φ is not the registered real field; it is
  fixed only by the bridge H-PF. No stated premise defines φ on the labels. Class D: none.
- **R8.2, the amplitude-scale gauge** (SM:96; Substratum:270–272, "*Status (open).*"). If its
  translation clause were physical, a physical φ would be invariant under x ↦ x + c(1, 1)𝟙, so φ
  would vanish on the constant labels [A]. This route is conditional, and its warrant is open
  ([C3] §4.2 and O1; SM:811 names the additive-automorphism group, which excludes translations). It
  supplies nothing for the staggered labels: τ_c is neither a relabelling nor a symmetry of F
  ([C3] §5.2). It is partial at best.

### 3.2 Lemma PF: the positive-frequency clause forces label-blindness [A]

Let φ be real-linear on L_0 ⊕ V_rest, with φ = Φ_n on V_rest. Suppose that along every trajectory
x(t) = F^t x of the support, the function t ↦ φ(x(t)) has spectral support in the open
positive-frequency arc {e^{iθ} : θ ∈ (0, π)}, or in its mirror under the opposite sign convention.
Then φ vanishes on L_0, and φ = Φ_n ∘ P_rest.

*Proof.*
- The support contains the trajectories with y = 0: l(t) = c(1, 1)𝟙 + (−1)^t a(1, −1)s.
- φ(l(t)) = φ_c + (−1)^t φ_a, where φ_c is the value of φ on the constant part and φ_a on the
  staggered part.
- This function has spectral support in {1, −1}, frequencies 0 and π, which lie outside the open
  arc. So φ_c = φ_a = 0.
- By real-linearity, φ(l + y) = φ(y) = Φ_n(y).
∎

**Consistency with the definition.** On V_rest, Φ_n = 2ℓ_n ∘ Π_+, where Π_+ is the Riesz projection
of F onto the eigenvalues e^{iθ}, θ ∈ (0, π) [A]. For real y, y = y_+ + ȳ_+ and J_F y = iy_+ − iȳ_+,
so ℓ_n(y) − iℓ_n(J_F y) = 2ℓ_n(y_+). Π_+ annihilates V_null, whose spectrum is {±1}. So the
spectral form 2ℓ_n ∘ Π_+, defined on all of V, is Φ_n ∘ P_rest. This is the positive-frequency part
of the real field in the usual sense.

### 3.3 The formula reading (countercontrol N-b)

- **H-PF_u.** The formula ℓ_n(x) − iℓ_n(Jx), with J defined only on V_rest, extends most simply as
  ℓ_n(x) − iℓ_n(J_F P_rest x) = ℓ_n(l) + Φ_n(y). This is H-PF_u of [FS] §6. Its label term
  ℓ_n(l(t)) = c + (−1)^t s_n a has frequencies 0 and π [A]. So H-PF_u is not a positive-frequency
  field: it violates H-PF's own clause.
- **Other extensions.** The extension through 𝒥 = id ⊕ J_F gives (1 − i)ℓ_n(l) + Φ_n(y), which
  fails in the same way [A].
- **Formula-only reading.** If H-PF is read as the formula alone on V_rest, with no constraint on
  the labels, then H-PF_u is admissible. Witness ρ_W ([FS] §6) then meets every stated and carried
  premise and violates N-8, which is class I.

**Class of Q8:** R (H-PF, with its positive-frequency clause applied on the support); I under the
formula-only reading.

## 4. Q9: N-9, SMD on the full law

### 4.1 Routes

- **R9.1, measure selection** (Main:60 [P]: the "selection among orbits is fixed by maximal entropy
  compatible with the observer's records"). Under Proposition 4b's hypotheses the selected measure's
  observer image is custodially scalar ([A-rec] Proposition C), so H5 fails and Theorem 5 is vacuous
  on it. This route supplies no condensate state, so it does not source N-9.
- **R9.2, the records fix the labels; the label-sector reading** [A].
  - **The labels are registrable.** The labels can be read asymptotically from one visible site's
    itinerary:
    - c = lim_T (1/T) Σ_{t<T} u_n(t);
    - a = lim_T (1/T) Σ_{t<T} (−1)^t s_n u_n(t).

    These limits hold because F, and also −F, have no eigenvalue 1 on V_rest, so the Cesàro means
    of the V_rest part vanish. This is consistent with Main:44, since one visible site suffices.
  - **The label-sector reading.** Read Theorem 5's state as the stationary state conditioned on the
    registered labels: a label sector (c, {±a}). Conditioning on F-invariant functions preserves
    F-invariance.
  - **(a) Sectors with a = 0** (every sector when L is odd). The labels are deterministic, so
    Stab(ρ) = Stab(P_rest∗ρ) under R_ext, and Stab(C) = Stab(C_rest). N-9 is then equivalent to SMD
    on the sector's fluctuation law: class R.
  - **(b) Sectors with a ≠ 0.** The slice (the sign of a) stays random within the sector, so a
    residual joint dependence is possible. Witness ρ_P (§4.2) shows it.
  - **Conditioning on the slice.** Conditioning on the slice as well gives a law invariant under F²
    but not under F, which violates L-SDS as stated.
- **R9.3, extremality** (countercontrol N-e) [A].
  - If ρ is ergodic for the group generated by F and the translations, then c is a.s. constant and
    {±a} is a.s. constant, since these are invariant functions. So the labels are deterministic up
    to the sign of a.
  - P_rest∗ρ is then ergodic as well, being a factor of ρ.
  - By [A-rec] Proposition B, the identity component of Stab(P_rest∗ρ) contains U(3)×U(2)×U(1) only
    if the T_1 and E blocks of Σ_c vanish. Since Stab(ρ) ⊆ Stab(P_rest∗ρ), no extremal state
    realizes Theorem 5's conclusion with distinct block values.
  - So the route that makes the labels deterministic by extremality excludes the conclusion itself.
    This is conditional on [A-rec] Proposition B, which is model-reviewed.
- **R9.4, joint Gaussianity** [A].
  - If ρ is jointly Gaussian on L_0 ⊕ V_rest, the vanishing of the label–fluctuation cross moments
    under stationarity ([FS] §3.1) makes the labels independent of y.
  - Then Stab(ρ) = Stab(P_rest∗ρ), and P_rest∗ρ is Gaussian, so SMD holds on it. N-9 follows.
  - Joint Gaussianity is unstated: "the stationary law and Gaussian limit of the realized scalar
    dynamics" are open (SM:290 [P]). It is stronger than SMD.
  - [SMD-SRC]'s Gaussianity theorem holds on Z with 0 < abs(μ) < 1, where there are no labels. It
    does not reach T at μ = 1.
  - This is a conditional source only.
- **R9.5, label–fluctuation independence.** It is sufficient ([FS] §3.4), and unstated.

### 4.2 Witnesses (countercontrol N-c)

**ρ_T** ([FS] §3.4, model-reviewed): constant labels c = ±e (e ∈ A_1), a = 0, conditionals 2ν|_S
and 2ν|_{S^c}. Checked against each admitted premise:

| Premise | Holds on ρ_T |
| --- | --- |
| LIN, LIFT, b_A1 = 0 | the setting |
| L-SDS | F-stationary, finite moments |
| translation and O invariance | yes |
| H5, O-equivariance | Σ_c from ν = N(0, C_0), distinct κ_b |
| TPC | C = eeᵀ ⊕ C_0, with eeᵀ ∝ P_{A_1} |
| H-PF with its positive-frequency clause (so N-2 and N-8) | yes; H-PF constrains the field, not the state |
| SMD on P_rest∗ρ_T = ν | yes, ν is Gaussian |

It violates N-9. It is not a single label sector, so it applies without the label-sector reading.
It exists for every L ≥ 7, odd or even.

**ρ_P (new) [A]:** a single label sector with a ≠ 0. Take:
- L even, and large enough that some k_0 has a(k_0) ∉ {±2} and the momenta ±hk_0 and π ∓ hk_0
  (h ∈ O, the rotation group) are pairwise distinct [W];
- c = 0, a ∈ {±e′} with e′ ∈ A_1;
- ν = N(0, C_0), with C_0 = Σ_b κ_b G⁻¹ ⊗ P_b and the κ_b distinct.

*The quadratic form.* Let z_k(y) ∈ C^6 be the F-positive component of y at momentum k, in an
O-equivariant normalisation, and set

    q_2(y) = Re Σ_{h∈O} z_{hk_0}(y)ᵀ z_{π−hk_0}(y)

(bilinear, not sesquilinear). Then:
- **F-odd.** z_k(Fy) = e^{iθ}z_k(y) and z_{π−k}(Fy) = e^{i(π−θ)}z_{π−k}(y), and the product of the
  phases is −1. So q_2 ∘ F = −q_2.
- **T_j-odd.** The translation characters multiply to e^{ik_j}e^{i(π−k_j)} = −1.
- **O-invariant,** by averaging, with hπ = π; zᵀz′ is invariant under the real link representation.
- q_2 is real, nonzero and indefinite.

*The witness.* Let S = {q_2 > 0}. Then F S = T_j S = S^c up to a null set, hS = S, and ν(S) = ½,
since q_2 ∘ F⁻¹ = −q_2 has the law of q_2. Define

    ρ_P = ½ δ_{a=e′} ⊗ 2ν|_S + ½ δ_{a=−e′} ⊗ 2ν|_{S^c}.

*Properties.*
- **Invariance.** F and T_j map (e′, 2ν|_S) to (−e′, 2ν|_{S^c}), so ρ_P is F-stationary,
  translation-invariant and O-invariant.
- **Second moments.** P_rest∗ρ_P = ν, so SMD holds on the fluctuation law, and Σ_c has distinct
  values. The cross moments vanish, because S = −S. TPC holds.
- **A stabilizer element is lost.** Let w_φ = e^{iφP_T1} with e^{2iφ} ≠ 1; then w_φ ∈ Stab(C). R(w_φ)
  acts on z_k as w_φ, so q_2′ = q_2 ∘ R(w_φ)⁻¹ multiplies the T_1 part of the pairing by e^{−2iφ}.
  - **Not S.** Take y_0 with only T_1-components at the pair (k_0, π − k_0) and z^T z′ = e^{iψ},
    where cos ψ > 0 > cos(ψ − 2φ). Then q_2(y_0) > 0 > q_2′(y_0). A neighbourhood of positive
    ν-measure lies in S ∖ R(w_φ)S.
  - **Not S^c.** Take y_1 with E-components and z^T z′ = 1. Then q_2(y_1) = q_2′(y_1) = 1 > 0. A
    neighbourhood lies in S ∩ R(w_φ)S.
  - So R(w_φ)S is neither S nor S^c up to a null set. Under any translation-commuting extension,
    which fixes the labels on SU(6) and at most rotates them through det (Lemma L of [FS]),
    w_φ ∉ Stab(ρ_P).
- **N-9 fails** on ρ_P, while ρ_P is a single label sector (0, {±e′}) satisfying every premise of
  the table above.

### 4.3 Class of Q9

- **Without the label-sector reading:** I (ρ_T), on every L ≥ 7.
- **Under the label-sector reading, L even, sectors with a ≠ 0:** I (ρ_P).
- **Under the label-sector reading, sectors with a = 0** (every sector on odd L): R, reducing to SMD
  on the sector's fluctuation law.
- **Class D:** none (R9.1–R9.5).

## 5. Controls

| Id | Result | Status |
| --- | --- | --- |
| P-1 | At abs(μ) < 1, L_0 = 0 and P_rest = I. LI is Theorem 1's uniqueness; Lemma PF is vacuous; N-9 is SMD on ρ. None is non-trivial | green |
| P-2 | Under H-ZM the quotient identifies the slices and removes the labels, so N-2, N-8 and N-9 hold ([FS] C+2) | green |
| N-a | Proposition P's family is counted as excluded only by H-PF's positive-frequency clause (§2.2), never by the native structure (§2.1) | green |
| N-b | H-PF_u is checked against the positive-frequency clause by its spectral content (§3.3), and is admitted under the formula-only reading | green |
| N-c | ρ_T and ρ_P are checked premise by premise (§4.2) | green |
| N-d | P2a's covariance is used for no class D or R (§2.1, R2.3) | green |
| N-e | The extremality route is tested against [A-rec] Proposition B (R9.3) | green |
| X-1 | Fixed-string re-extraction at [P]: Main:44 "the observer is not the whole"; Main:60 "selection among orbits is fixed by maximal entropy compatible with the observer's records"; SM:136 "is a hypothesis on the solution rather than a consequence of the dynamics"; SM:290 "the stationary law and Gaussian limit of the realized scalar dynamics" | green |

**Power.** P-1 and P-2 cannot fail on the reductions; they check the setting only. N-b and N-c are
the decisive countercontrols.

## 6. Passes, productivity and classification

- **Pass 1 (Q2).** R2.1–R2.3 closed; reduction to H-PF; the F² reading excluded by taming.
- **Pass 2 (Q8).** R8.1–R8.2; Lemma PF; the formula reading.
- **Pass 3 (Q9).** R9.1–R9.5; ρ_T re-checked; ρ_P constructed.
- **Pass 4 (skepticism on the favourable reductions in Q2 and Q8).**
  - The reductions depend on reading H-PF's positive-frequency clause on the support.
  - The alternative readings are stated, with class I.
  - Lemma PF uses only the trajectories with y = 0.
  - No NEW finding.

Stopping condition 1 holds.

**Productivity (PLAN §7): gem.** Each N_k receives a class more informative than "candidate
premise". The candidate-premise set reduces, under a stated reading of a premise already carried,
from three to one, and the remaining one is confirmed independent by a new single-sector witness.

| Class | Findings |
| --- | --- |
| NEW | Lemma PF (the positive-frequency clause forces label-blindness); ρ_P (N-9 independent within a single label sector) |
| POSITIVE | H-PF implies N-2 (§2.2); joint Gaussianity implies N-9 (R9.4); the label-sector reduction for a = 0 (R9.2) |
| ELABORATING | R9.3 (extremality against Proposition B); R2.2 (τ_c is not a symmetry, so naturality cannot give LI) |
| CONFIRMING | ρ_T, re-checked against the admitted premises |

Correctness bands unchanged: consistency-axis work (§A.23).

## 7. Scope

- Carrier T at the massless point, the linear lift, b_A1 = 0, and SM Theorem 5's consumers only.
- Carrier Z, H-PF-int and the consumers outside Theorem 5 are not addressed.
- Nothing concerns the Z/q level.
- H-PF, L-SDS, TPC, SMD on the fluctuation law, LIN, LIFT and the SM:232 bridge remain carried and
  unsourced.
- **Independence is relative to a stated set.** Each independence claim is relative to the stated
  premises of Main and SM, C*, and the other premises named in each witness check. It is not a claim
  that no extension of OI could supply N_k.

## 8. Open nodes

- **O-1 (owner reading).** Is H-PF's "positive-frequency" clause read on the stationary support?
  Then N-2 and N-8 are not additional (class R). If it is read as the formula on V_rest only, both
  are class I.
- **O-2 (owner reading).** Is Theorem 5's state a label sector fixed by the observer's records
  (R9.2)? Then N-9 reduces to SMD on sectors with a = 0 and stays independent on staggered sectors
  (ρ_P).
- **O-3.** Joint Gaussianity on T at μ = 1 (R9.4), and any T-analogue of [SMD-SRC]'s clustering
  theorem. This is for the SMD clustering unit's attention, and is not investigated here.
- **O-4.** The conditioned selected measure. Whether Main's measure selection, conditioned on
  registered labels, yields a condensate state is not examined. [A-rec] Proposition C concerns the
  unconditioned image.
- **O-5.** The lower bound on L for ρ_P (the distinct-momenta condition) is stated as [W].
- **O-6.** H-PF itself remains unsourced ([A-rec] §5).

## 9. Findings for routing (listed, not edited)

1. **[FS] PRESERVATION §2, the status of N-2 and N-8.** They are implied by H-PF read with its
   positive-frequency clause on the support (§2.2, §3.2). This is for the owner's reading O-1.
   Route: #1217.
2. **[FS] §3.4, N-9.** It is independent even within a single label sector on even L (ρ_P). It
   reduces to SMD on sectors with zero staggered label under the label-sector reading. Route:
   #1217.

## 10. References not on `main` (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
| --- | --- | --- |
| #1169 comment 7208939261 | authorization | provenance: no result uses it |
| #1169 comment 7199704501 | work package | provenance |
| commit `158f4155` (PLAN.md) and the commit adding this report | preregistration order | support on `main` once merged without squash; not before |
| [FS], [L2], [A-rec], [C3], [SMD-SRC] records | inputs to §2–§4 | support on `main` at [P] |

Support off `main`: none.

## 11. Verification status and remediation (§A.46 item 4)

**This table authorizes no work.**

| Claim | Status | Missing | Issue | What would resolve it |
| --- | --- | --- | --- | --- |
| §2.2: H-PF implies N-2; the F² reading is untamed | unreviewed hand algebra | independent review | #1217 | recorded review |
| R2.2, R2.3: naturality and the custodial action do not force LI | unreviewed | independent review | #1217 | recorded review |
| Lemma PF and §3.3 | unreviewed | independent review | #1217 | recorded review |
| R9.2: label registrability and the a = 0 reduction | unreviewed | independent review | #1217 | recorded review |
| R9.3: extremality against Proposition B | unreviewed; conditional on [A-rec] Proposition B (model-reviewed) | independent review | #1217 | recorded review |
| R9.4: joint Gaussianity implies N-9 | unreviewed | independent review | #1217 | recorded review |
| ρ_T re-check | relies on [FS] §3.4 (model-reviewed) | independent non-model verification | #1217 | recorded review |
| ρ_P | new, unreviewed; the L bound is [W] | independent review; an exact finite control on a small even torus (needs authorization) | #1217 | review; authorized control |
| Outcome (no class D; N-9 class I on even L under every reading; N-2 and N-8 class R under O-1's positive-frequency reading) | conditional on the readings O-1 and O-2 and on C* | owner readings; review | #1217 | owner decisions; review |
