## SC-28 confirmation at `df061d64` (one commit on `42bc4050`, read-only)

**Verdict: ACCEPT WITH CHANGES.** R1, R2 and R3, decision 2, decision 6b and the eight optionals are applied correctly. Two problems remain. The new R4 derivation in SM :1211 is mathematically sound but proves the wrong thing: it does not support Part A's hypothesis. And the R1 sentence in Main :706 and GR :368 now contradicts GR §5. A third, smaller fix is in SM :294. All three are short edits.

### Required

**Q1. SM :1211, Part A (R4 / decision 6b): the E derivation does not support the hypothesis it is attached to.**
- The algebra is right. E(a,b) = a·a + b·b − a·Nb is conserved and even under T:(a,b)↦(b,a), over ℤ and over ℤ/qℤ.
- The problem is that the exact linear rule conserves a whole family of such forms, not just E. For every polynomial p, E_p(a,b) = a·p(N)a + b·p(N)b − a·N p(N) b is conserved by the same argument. So the rule's orbits lie in joint level sets, and a level set of E is never a single cycle.
- I checked this by exhaustive enumeration of the linear rule on rings L = 3, 4, 5 with q = 2, 3, 5:
  - E is conserved and T-even, and E_N is also conserved.
  - Every E-level set splits into many cycles: 33–54 at (3,3), about 225 at (4,3), about 4,500 at (4,5).
- SM itself says the same: pure linear dynamics is integrable (sub-torus orbits), and full-shell sampling rests on the rounding nonlinearity (:294, :296). A map that includes that nonlinearity is not shown to conserve E. Your question was whether the realized map is exactly the linear rule. The corpus is ambiguous: :296 calls the linear ℤ/qℤ rule "the exact dynamics", but :294's diagnostics contrast a "rounded bijection" with a "linear control".
- So Part A now conditions on "cycle ergodicity on the level set" of a conserved quantity of the one map for which that ergodicity provably fails. The added line is a new claim without support in this role, so it is not an acceptable one-line addition.
- What the conclusion actually needs is smaller. T-reversibility (TφT = φ⁻¹, §5) holds for any update of the form (a,b) ↦ (R(a) − b, a), rounded or not. So T maps cycles to cycles, and ρ∘T = ρ holds exactly when ρ is uniform on a single cycle that T maps to itself.
- Fix:
  - Drop the E sentence.
  - State Part A as "conditional on cycle ergodicity of the realized bijection on a T-invariant set carrying ρ".
  - Mirror the label in the bold heading and the closing sentence. The heading currently reads "on the energy shell carrying ρ" and should say T-invariant.
  - Update the README row to match.
- Otherwise decision 6b is applied consistently: the bold heading, "this step holds unconditionally", Part B, and the closing "both parts carrying gap (i)'s cycle-ergodicity residual".

**Q2. Main :706 and GR :368: "no identification of an entropy with a substratum quantity is derived" is too broad.**
- In GR the very next sentence identifies the horizon entropy with σ·N_modes, a substratum boundary-mode count, as GR §5 does.
- Restore the scope: "no identification of CLPW's entropy with a substratum quantity".
- ch07 :199 ("no entropy identification") should say the same, mirrored in FULL.

**Q3. SM :294 (decision 6a): "Chaos is necessary for full-shell sampling" is unsupported.**
- Ergodicity does not require positive Lyapunov exponents.
- The corpus supports only this: breaking the integrability of the linear rule is necessary, and chaos does not by itself give a single cycle.
- Suggested wording: "Breaking integrability is necessary for full-shell sampling; chaos does not establish it: no theorem shows …".
- The rest of 6a is right: the chaos is "demonstrated numerically", there is no single-cycle theorem, the measurements are limited to the sizes, ensembles and protocols sampled, and "chat-track" is gone at SM :294 and Structure :1115, with zero corpus hits.

### Checks that passed
- **R1 (Main :706, GR :368, ch07 :199 and FULL).**
  - "Finite-dimensional" is scoped to the full matrix algebra on each finite region.
  - The quasilocal C*-completion is cited with no state or representation selected: GR §3.3, and Main §3.4, which is correct since Main :584 lies in §3.4.
  - "No von Neumann closure, no relation to CLPW's observer-dressed algebra … is derived; whether the construction reproduces CLPW's algebra and its entropy is open."
  - No UHF or II₁ remark was added. Q2 is the only issue.
- **R2.** "σ of one boundary mode summed over the N_modes of §5, which recovers S_dS under the §3 calibration" matches GR §5 (σA/ε² = A/4l_p²).
- **R3.** The README now names 𝒢_sub as the substratum gauge group (Substratum §4, Theorem 24), with no log|𝒢_sub| computation and no finite order given. The "structurally forced" count is corrected to 3. The `9ff27719` decision is cited as provenance only.
- **Decision 2.** Type II and the dS cancellation appear only as open questions: "open research questions" in ch07, "is open" in Main and GR. Nothing is asserted as a result.
- **Optionals.**
  - Main :176: "uses no form of (C2) … timescale form not necessary … (C2-structural) holds by reversibility (§1.3)", plus the ε ≤ 1 − 1/n_V range. Correct, matching Main :76 and :463.
  - Main :706 (Slagle–Preskill) is exact:
    - S ⟺ D ⟺ Q_fb on finite horizons (Main :82(1)).
    - The continuous-time law is additional structure (GR §3.3, Main :584).
    - "Operational QM follows only with the added principles" matches the OI⁺ characterization, with each principle independently necessary (Main :580). An optional tightening is "exact finite operational QM", the proved scope.
  - "Does not bear on this" is deleted.
  - ch18 :180 now states Γ_n = I almost surely, with φ^N = id giving Γ_N = I. Correct.
  - ch18 :191: the zero configuration is fixed, so there are at least two cycles. Correct for the cited linear rule. Every update of the form R(a) − b with R(0) = 0 also fixes zero.
  - ch18 :174 and :193, ch09 :106 and ch02 :32 are harmonized to "exact"/"finite" recurrence, with :174 separating it from Poincaré's theorem.
  - Every chapter edit is in FULL: 7 lines changed each side, and 0 chapter lines missing.
- **Main :532.** "t_R is the Poincaré recurrence time of any realizing substrate" is accurate for finite substrates. Each state's return time exists and equals its cycle length, and the theorem uses t_R only as a scale (t ≪ t_R). It is a naming difference from the ch18 harmonization, not an error, so I see no need to move a canonical fingerprint. Harmonize only if a fingerprint re-affirmation is already planned.
- **Nothing else changed.** The diff touches only Main, GR, SM, Structure, ch02, ch07, ch09, ch18, FULL (each with `.tex`/`.pdf` where applicable) and the track README.
  - Stamps match for Main, GR, SM, Structure and FULL.
  - Page counts are unchanged (SM 147, Structure 99).
  - The added-lines register scan is clean.
  - The release gate passes 21 steps; only lean-axioms fails, as expected locally.
  - `edge_rigidity_probe`: ALL CHECKS PASS.

I removed the worktree I created and ran no gc or prune.
