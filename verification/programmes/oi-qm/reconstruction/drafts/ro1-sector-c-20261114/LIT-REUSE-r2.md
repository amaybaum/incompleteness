# LIT-REUSE, r2: first-hand reading of performed experiments that use one entangled source more than once

**Purpose.** Record what performed experiments that measure the same entangled pair, or the same
particle, more than once in a Bell or correlation setting actually did and reported, with
raw-direct observables separated from derived ones (§A.24). The note serves S3 unit U3
(`S3-U3-r3.md`, §§2.2, 4.1–4.4, 5.1–5.2, 10.3 and owner question 4), whose agreement half of
AC-1 is stated as conditional on "a performed experiment that measures one entangled source twice per wing, with a
setting change between the uses, and whose raw complete local-history records show
setting-independence", and, for L-3, "repeatability at repeated settings on both wings". The note
records what the papers report. It does not assess U3's reasoning, adopts no premise and changes no
classification. Where a row maps a paper to a U3 case, the mapping is the writer's and is labelled
as such.

**Authorization.** Owner decision on Issue #1169, comment 6892563291 (`amaybaum`,
2026-11-15T09:49:19Z): "Q4: yes, the performed experiments that use one source twice are read
first-hand." Paper-only: no repository edits, commits, pushes, Issue changes, computation or Lean.

**Read date.** 2026-11-15. **Writer:** Claude. **Review:** r1 reviewed in `REVIEW-LIT-REUSE-r1.md`
(ACCEPT WITH CHANGES); this revision applies its required changes C1–C6 and optional points O1–O5,
as listed in `RESPONSE-LIT-REUSE-r1.md`. Nothing else is changed.

**Method.**
- Full texts were read where an open arXiv version exists. The PDF was converted to text and the
  text read by the writer, figures through their captions and axis labels. The arXiv version is the
  version read; differences from the published version are possible.
- Bibliographic data and DOIs were checked against Crossref. Publisher abstracts were read from
  OpenAlex (Choi et al. 2020; Mao et al. 2023) and Crossref (Xiao et al. 2024).
- The Optica site (opg.optica.org) did not resolve from the reading environment, so no Optica full
  text was read. No APS or Nature page was read directly.
- Status labels: **FULL** (whole text read, version stated); **ABSTRACT** (abstract only);
  **LOCATED** (title and identifier seen in a search listing; nothing of the content read);
  **NOT READ**. A statement in a record that the paper does not make, but that the writer draws
  from what it states, is marked *[writer's reading]*. Nothing below is taken from memory. A
  quantity not found in the text read is marked "not reported in the version read".

**What U3 asks of an experiment.** The headline is U3 r3 §10.3: "a performed experiment that
measures one entangled source twice per wing, with a setting change between the uses, and whose raw
complete local-history records show setting-independence", and, for L-3, "repeatability at repeated
settings on both wings". The policy patterns the two lemmas compare (U3 r3 §§5.1, 5.2) give the
reading grid. A policy `(s₁, s₂)` is a wing's setting at its first and second use.
- (G1) **Two uses per wing.** One entangled source, each wing measured twice, with each wing's two
  settings chosen per configuration (RQ-REU).
- (G2) **Complete local histories held.** Both outcomes of each wing kept per event: fresh-output
  form (each outcome a separate record) or same-register form (only the parity `a₁ ⊕ a₂`).
  Per-event fresh-output records determine the parity as well, so they serve both forms.
- (G3) **L-2's comparison, (k3).** The compared wing *repeats* its own setting, Alice `(x, x)`,
  while the remote wing either repeats or changes its setting, Bob `(0, 0)` against `(0, 1)`; and the
  mirror pairs, Alice `(0, 0)` and `(0, 1)` with Bob `(y, y)`. What is compared is the law of the
  compared wing's two-use history across those remote policies.
- (G4) **L-3's comparison, (k3′), and the law (9).** The compared wing repeats its setting, Alice
  `(x, x)`, while the remote wing's *first* setting varies, Bob `(0, y₂)` against `(1, y₂)` for one
  fixed `y₂`, and the mirror pairs; with a projective first use, the outcome repeats at the repeated
  setting (`a₂ = a₁`), which is the repeatability half of §10.3.
- (G5) Raw data: counts per event or per configuration; postselection, heralding, accidental
  subtraction; setting choice per event or per acquisition; whether the published record is the
  complete record.

***

## 1. Per-paper records

### 1.1 Schiavon et al. 2017

| Field | Record |
|---|---|
| Citation | M. Schiavon, L. Calderaro, M. Pittaluga, G. Vallone, P. Villoresi, "Three-observer Bell inequality violation on a two-qubit entangled state", *Quantum Sci. Technol.* 2, 015010 (2017), doi:10.1088/2058-9565/aa62be |
| Version read | arXiv:1611.02430v1, FULL |
| Source | Polarization-entangled photon pairs, singlet, PPKTP in a Sagnac interferometer, 404.5 nm pump |
| Uses | Alice: one projective use. Bob's photon: Bob1 then Bob2 on the same photon. Bob1 is a weak (controllable-strength) measurement, a controlled-phase gate between polarization and an interferometer path ancilla; Bob2 is projective |
| Settings and timing | Fixed per acquisition: 16 acquisitions (wave-plate and glass-plate configurations) per pair of CHSH values, 30 s each. The paper states that "the three observers choose randomly between the two possible measurements"; the version read describes the settings as set by wave-plate configurations, not by a per-event random choice |
| First-use record | Bob1's outcome is the interferometer output port. "In our setup, we look at one single output port at a time, swapping \|2⟩ and \|3⟩ by tilting the glass plate." The first outcome is therefore fixed by configuration, not detected per event |
| Second-use record format | Bob2's outcome is detected per event at a PBS with two SPADs, in coincidence with Alice. Joint frequencies `p(a, b₁ \| x, y₁)` and `p(a, b₂ \| x, y₂)` are assembled across acquisitions. No per-event record of `(b₁, b₂)` |
| Postselection, heralding | Coincidence detection; "we did not subtracted accidental coincidences". No herald |
| Raw data reported | CHSH values only, with Poissonian errors; average coincidence rate about 700 counts/s; no count tables |
| Key numbers | At ε = 1.049 ± 0.002, eight trials: I⁽¹⁾ = 2.125 ± 0.003 and I⁽²⁾ = 2.096 ± 0.003. At ε = 1.053 ± 0.002, five trials: I⁽¹⁾ = 2.114 ± 0.003 and I⁽²⁾ = 2.064 ± 0.003 |
| Completeness | No raw event data published; no data-availability statement in the version read |
| Bearing on U3 (writer's mapping) | One wing used twice, the other once: G1 and G3 are not met. The first use is unsharp, so G4 is not met. The second use reads the photon after Bob1's interaction; within the quantum description this is a post-measurement update, case (S) of U3 §2.2 |

### 1.2 Hu et al. 2018

| Field | Record |
|---|---|
| Citation | M.-J. Hu, Z.-Y. Zhou, X.-M. Hu, C.-F. Li, G.-C. Guo, Y.-S. Zhang, "Observation of non-locality sharing among three observers with one entangled pair via optimal weak measurement", *npj Quantum Inf.* 4, 63 (2018), doi:10.1038/s41534-018-0115-x |
| Version read | arXiv:1609.01863v3, FULL |
| Source | Polarization-entangled singlet pairs at 798 nm, PPKTP in a Sagnac loop |
| Uses | Alice: one projective use. Bob1: optimal weak measurement (F² + G² = 1) with a path pointer between beam displacers. Bob2: projective, on the same photon |
| Settings and timing | Fixed per acquisition. "For each fixed θ … we have implemented 64 trials"; coincidences recorded in 6 s windows |
| First-use record | "the outcomes of Bob1 are actually obtained by Bob2 in our photonic experiment." In the setup used, "specific outcome +1(−1) can be selected by rotating HWP1 and HWP4": one outcome per configuration |
| Second-use record format | Each three-observer probability `P(a, b₁, b₂ \| x, y₁, y₂)` "is obtained by the final coincidence detection" for one configuration. Joint statistics only, assembled across configurations |
| Postselection, heralding | Coincidence detection; no herald; accidental handling not stated in the version read |
| Raw data reported | S values with Poissonian error bars (Fig. 4); source visibilities |
| Key numbers | θ = 18.4°: S_A−B1 = 2.20 ± 0.02, S_A−B2 = 2.17 ± 0.02; double violations at θ ∈ {16.4°, 18.4°, 20.5°} "with approximately 10 standard deviations" |
| Completeness | "The data that support the findings of this study are available from the corresponding author upon reasonable request." |
| Bearing on U3 (writer's mapping) | As 1.1: one-wing reuse, unsharp first use; G1, G3 and G4 not met; quantum description case (S) |

### 1.3 Feng et al. 2020

| Field | Record |
|---|---|
| Citation | T. Feng, C. Ren, Y. Tian, M. Luo, H. Shi, J. Chen, X. Zhou, "Observation of nonlocality sharing via not-so-weak measurements", *Phys. Rev. A* 102, 032220 (2020), doi:10.1103/PhysRevA.102.032220 |
| Version read | arXiv:1912.02979v2, FULL |
| Source | Polarization-entangled pairs at 808 nm, type-II BBO |
| Uses | Alice: one projective use. Bob1: optimal weak measurement with a spatial ancilla, precision factor G tunable. Bob2: projective on the same photon, with Bob1's and Bob2's observables chosen as functions of G |
| Settings and timing | Fixed per configuration; nine values of G |
| First-use record | Simplified setup: "when the input photon is found in central spatial mode, it indicates that an optimal weak measurement … with +1 outcome has been implemented"; rotating HWP1 and HWP4 selects the −1 outcome. One outcome per configuration |
| Second-use record format | Bob2 at a PBS. Joint statistics only |
| Postselection, heralding | Coincidence detection; postselection on the central spatial mode for Bob1's outcome |
| Raw data reported | CHSH values with Poissonian error bars (Fig. 4) |
| Key numbers | G = 0.8: I⁽¹⁾ = 2.214 ± 0.011, I⁽²⁾ = 2.168 ± 0.007. G = 0.96: I⁽¹⁾ = 2.028 ± 0.024, I⁽²⁾ = 2.047 ± 0.020 |
| Completeness | No raw data published; no data-availability statement in the version read |
| Bearing on U3 (writer's mapping) | As 1.1 |

### 1.4 Foletto et al. 2020

| Field | Record |
|---|---|
| Citation | G. Foletto, L. Calderaro, A. Tavakoli, M. Schiavon, F. Picciariello, A. Cabello, P. Villoresi, G. Vallone, "Experimental Certification of Sustained Entanglement and Nonlocality after Sequential Measurements", *Phys. Rev. Applied* 13, 044008 (2020), doi:10.1103/PhysRevApplied.13.044008 |
| Version read | arXiv:1906.07412v2, FULL |
| Source | Polarization-entangled pairs, PPKTP in a Sagnac interferometer, state (\|00⟩ + \|11⟩)/√2 |
| Uses | Alice: up to three sequential measurements on one photon (two unsharp, µ₁ ≈ 0.34, µ₂ ≈ 0.19, then projective µ₃ = 0), with a history-dependent unitary before each step. Bob: one projective use, whose setting depends on Alice's history |
| Settings and timing | "The choice of measurement bases is not made in real time, photon by photon … but, rather, at fixed temporal intervals." Exposure 20 s per configuration; Alice's history is "externally" chosen and Bob's plates set "that Bob would use if he received such a message" |
| First-use record | "One exit of each is blocked"; wave-plate orientations select "which branch of the tree is implemented by the one path of our setup". Each history of outcomes is fixed by configuration |
| Second-use record format | One detector each for Alice and Bob; coincidence counts per configuration, "proportional to the joint probability of obtaining the combination of outcomes under test" |
| Postselection, heralding | "We operate under the fair-sampling assumption"; locality loophole open ("classical communication between Alice and Bob … cannot be physically excluded"); detection efficiencies about 1 % (Alice) and 8 % (Bob) |
| Raw data reported | Nine CHSH values and twelve entanglement-witness values, each per history (Tables I, II, IV), with Poissonian errors; total about 3 × 10⁴ coincident events |
| Key numbers | Step 1: S = 2.15 ± 0.01. Step 2: 2.13, 2.07, 2.12, 2.09 (± 0.01). Step 3: 2.48, 2.53, 2.47, 2.46 (± 0.03) |
| Completeness | No raw data published; no data-availability statement in the version read |
| Bearing on U3 (writer's mapping) | One-wing reuse with adaptive, history-dependent settings on both wings; G1 and G3 not met; first uses unsharp, so G4 not met. The repeated choice A₀ at steps 1 and 2 (histories "+1\|0; −1\|0") is a repeated observable under an unsharp first use, with differing outcomes reported as distinct histories |

### 1.5 Foletto et al. 2021

| Field | Record |
|---|---|
| Citation | G. Foletto, M. Padovan, M. Avesani, H. Tebyanian, P. Villoresi, G. Vallone, "Experimental test of sequential weak measurements for certified quantum randomness extraction", *Phys. Rev. A* 103, 062206 (2021), doi:10.1103/PhysRevA.103.062206 |
| Version read | arXiv:2101.12074v2, FULL |
| Source | Polarization-entangled pairs, PPKTP Sagnac, \|ψ₁⟩ = (\|HH⟩ + \|VV⟩)/√2 |
| Uses | Alice: one projective use. Bobs: two Mach–Zehnder weak measurements and a third projective measurement on the same photon |
| Settings and timing | "we do not choose the bases randomly, and do not record random outcomes from each measurement, but only expectation values, hence this is not a true Bell experiment." Exposure about 60 s and 30 s per configuration |
| First-use record | Wave plates set "the outcomes that correspond to the photons that pass through the only exit of the PBDs that is connected to the rest of the setup" |
| Second-use record format | Coincidence counts per configuration, time tagger with 80 ps resolution and ±1 ns window |
| Postselection, heralding | Coincidence detection; locality and detection loopholes stated open |
| Raw data reported | Min-entropy per step (Table I, Fig. 6) |
| Key numbers | Hmin,1 = 0.13 ± 0.002 (ξ₁ = 0.4, step 2 projective: 0.38 ± 0.04 and 0.13 ± 0.02 for the two histories); with a third step the CHSH-like inequality was not violated, Hmin,3 = 0 |
| Completeness | No raw data published |
| Bearing on U3 (writer's mapping) | As 1.1 |

### 1.6 Padovan et al. 2024

| Field | Record |
|---|---|
| Citation | M. Padovan, G. Foletto, L. Coccia, M. Avesani, P. Villoresi, G. Vallone, "Secure and robust randomness with sequential quantum measurements", *npj Quantum Inf.* 10, 94 (2024), doi:10.1038/s41534-024-00879-w |
| Version read | arXiv:2309.12286v2, FULL (experimental sections and Supplementary Methods E read in full) |
| Source | Polarization-entangled pairs at about 810 nm, \|ϕ⁺⟩ |
| Uses | Alice: one projective use. Bob1: weak measurement (MZI); Bob2: projective on the same photon |
| Settings and timing | "we did not include the random inputs but only scanned all the measurement settings one by one"; exposure 100 s (about 3 × 10⁵ coincidences) |
| First-use record | "By selecting one outcome at a time with an external HWP, the MZI realizes the Kraus operators" |
| Second-use record format | Coincidence counts per configuration; 1 ps time tagger, ±0.55 ns window |
| Postselection, heralding | Fair sampling; detection and locality loopholes stated open; "since we are scanning the measurements one by one, we are effectively using different states for each measurement" |
| Raw data reported | ⟨S₁⟩, ⟨S₂⟩, ⟨S_c⟩ and Hmin for three runs (Table I); a non-sequential CHSH run on the same states (Table II) |
| Key numbers | Run 1: ⟨S₁⟩ = 2.292 ± 0.002, ⟨S₂⟩ = 2.421 ± 0.003, ⟨S_c⟩ = 2.738 ± 0.003. Non-sequential ⟨S⟩ = 2.761 ± 0.003 (run 1) |
| Completeness | Data-availability statement: "Data is available from the corresponding author upon reasonable request." |
| Bearing on U3 (writer's mapping) | As 1.1. Table II is a fresh-pair (single-use) CHSH run on the same apparatus, the comparison case for (N)-type fresh runs |

### 1.7 Xiao et al. 2022 (projective first use)

| Field | Record |
|---|---|
| Citation | Y. Xiao, Y.-X. Rong, X.-H. Han, S. Wang, X. Fan, W.-C. Li, Y.-J. Gu, "Experimental recycling of Bell nonlocality with projective measurements", arXiv:2212.03815 (2022). Crossref lists a paper by Xiao, Rong, Wang, Han, Xu and Gu, "Experimental sharing of Bell nonlocality with projective measurements", *New J. Phys.* 26, 053019 (2024), doi:10.1088/1367-2630/ad48af; that it is the published form of the arXiv text is not established here. Its Crossref abstract matches the arXiv content ("by stochastically combining no more than two different projective measurement strategies"; "11 standard deviations"), which supports the identification without establishing it |
| Version read | arXiv:2212.03815v1, FULL |
| Source | Polarization-entangled pairs cos ϕ\|HH⟩ + sin ϕ\|VV⟩, PPKTP Sagnac, ϕ tunable |
| Uses | Alice: one projective use. Bob: projective (basis projection or identity) on the photon, then a unitary U_y, then Charlie: projective on the same photon. Strategies λ ∈ {1, 2, 3} are mixed with probability p via two paths of an unbalanced interferometer, weighted by variable ND filters |
| Settings and timing | Fixed per configuration; p set by filter attenuation and measured by blocking each path in turn |
| First-use record | Bob uses linear polarizers (one outcome per configuration). The strategy label λ is not recorded per event *[writer's reading: it follows from the unbalanced interferometer and from the measurement of p by blocking each path; the paper does not state it]* |
| Second-use record format | Charlie: HWP and PBS. Coincidence counts per configuration |
| Same-axis repeat in the stated settings | Case λ = 1 sets B₀ = cos φ σ₁ + sin φ σ₃ with U₀ = I and C₀ = −C₁ = cos φ σ₁ + sin φ σ₃: at y = 0 Charlie measures Bob's axis after a projective first use. The frequency of c = b (or c = −b) is not reported in the version read |
| Postselection, heralding | Coincidence detection; no herald |
| Raw data reported | S_AB and S_AC with Poissonian errors, as functions of p, φ, θ and ϕ |
| Key numbers | Cases 1+2, p = 0.83207 ± 0.0015: S_AB = 2.0451 ± 0.0015, S_AC = 2.0676 ± 0.0014. Cases 1+3, p = 0.3256 ± 0.0012: S_AB = 2.1056 ± 0.0013, S_AC = 2.0927 ± 0.0013 |
| Completeness | No raw data published; no data-availability statement in the version read |
| Bearing on U3 (writer's mapping) | One-wing reuse with a projective first use, the only such configuration in the set read. It contains the same-axis repeat G4 needs on one wing, but no repeatability figure is reported. The double violation uses a shared-strategy label that, on the writer's reading above, is not recorded, so each event's complete record would not contain λ. G1, G3 and G4's remote variation not met |

### 1.8 Mao et al. 2022 (network, per-event record of both uses)

| Field | Record |
|---|---|
| Citation | Y.-L. Mao, Z.-D. Li, A. Steffinlongo, B. Guo, B. Liu, S. Xu, N. Gisin, A. Tavakoli, J. Fan, "Recycling nonlocality in a quantum network", arXiv:2202.04840 (2022). Crossref lists a paper by the same nine authors, "Recycling nonlocality in quantum star networks", *Phys. Rev. Research* 5, 013104 (2023), doi:10.1103/PhysRevResearch.5.013104; its abstract (OpenAlex) repeats the arXiv abstract with one added sentence ("we show that the ability to recycle nonlocality can be independent of the size of the network"). That it is the published form of the arXiv text is not established here |
| Version read | arXiv:2202.04840v1, FULL |
| Source | Three independent SPDC sources (BBO pairs, 390 nm pulses split three ways), each emitting \|Φ⁺⟩; generation probability about 0.02 per pulse |
| Uses | Central party A: one projective use on each of three photons. In each branch k: B_k,1 an unsharp measurement (Sagnac CNOT with path meter, strength η), then B_k,2 projective on the same photon |
| Settings and timing | 64 measurement settings in the network test, set by wave plates (HWP and QHQ boxes). How settings were changed between acquisitions is not stated in the version read; random choice appears only in the protocol. *[Writer's reading: fixed per acquisition.]* |
| First-use and second-use record format | Per event: "the photon detection event reported by one of the four single-photon detectors per pulse corresponds to exactly one of the four outcome combinations (b_k,1, b_k,2)". Both outcomes are separate records of each detection event (fresh-output form). "All photon detection events are time-tagged" |
| Postselection, heralding | Six-photon coincidences within 5 ns at 0.7 s⁻¹ (80 MHz repetition); results conditioned on the six-fold coincidence |
| Raw data reported | 5550 six-photon events over 64 settings; network quantities S_s; per-branch pairs (CHSH₁, CHSH₂) |
| Key numbers | Per-branch (CHSH₁, CHSH₂): (2.1834 ± 0.0116, 2.1997 ± 0.0074), (2.1755 ± 0.0114, 2.1072 ± 0.0075), (2.1685 ± 0.0114, 2.1991 ± 0.0073). Network S_avg = 1.100 ± 0.030 (3-local), 1.085 ± 0.024 (bi-local) |
| Completeness | Time-tagged events stated; not published in the version read; no data-availability statement found |
| Bearing on U3 (writer's mapping) | Per-event fresh-output record of both uses on the reused wing, the form G2 asks for, but on one wing only. Unsharp first use, so G4 not met; G1 and G3 not met |

### 1.9 Zhu et al. 2022 (two-sided sequential)

| Field | Record |
|---|---|
| Citation | J. Zhu, M.-J. Hu, C.-F. Li, G.-C. Guo, Y.-S. Zhang, "Einstein-Podolsky-Rosen steering in two-sided sequential measurements with one entangled pair", *Phys. Rev. A* 105, 032211 (2022), doi:10.1103/PhysRevA.105.032211 |
| Version read | arXiv:2102.02550v2, FULL (main text and Supplementary Materials) |
| Source | Singlet pairs, type-I BBO, 404 nm pump; fidelity 98.76 ± 0.08 % |
| Uses | **Both wings used twice**: Alice1 and Bob1 optimal weak measurements, then Alice2 and Bob2 projective, on the same photons |
| Settings and timing | n = 6 settings for the first pair and n = 6 or 10 for the second; strengths θ_A1 = θ_B1 ∈ {π/36, π/12, 0.34, 5π/36, 7π/36} and further (θ_A, θ_B) points; 10 s integration per configuration. *[Writer's reading: settings fixed per configuration, inferred from the HWP-selected outcome.]* The steering quantity is S_n = (1/n) Σ_m \|C(x_m, y_m)\| (their Eq. (7)): Alice1 and Bob1 share the setting index k, and Alice2 and Bob2 share the index l (Eqs. (9)–(10)); "the measurement directions of Alice and Bob are chosen to be opposite". The Bell part (Supplement §B, Fig. S1) uses x₀ = Z, x₁ = X and two Bob settings; which setting combinations were acquired is not stated |
| First-use record | "Since only middle path out of BD2 is retained, the components … are post-selected"; the outcome −1 is realized by adjusting a HWP. One first-use outcome per wing per configuration |
| Second-use record format | "Coincidence events between four detectors are registered"; "The joint probability distributions for different measurement settings and outcomes are extracted from these coincidence counts" |
| Postselection, heralding | Coincidence detection; path postselection for the weak-measurement outcome |
| Raw data reported | Steering quantities S_n; Bell quantities in Supplementary Fig. S1. Marginals of either wing's two-use outcomes are not reported in the version read |
| Key numbers | At θ_A = θ_B = 0.34: violations 0.0493 ± 0.0029 of S₆^{A1−B1}, 0.0485 ± 0.0020 of S₆^{A2−B2} and 0.0636 ± 0.0023 of S₁₀^{A2−B2} (bounds B₆ = 0.5393, B₁₀ = 0.5236). Supplement: double Bell-CHSH violation "is observed only when Alice1 or Bob1 performing almost no measurement" |
| Completeness | No raw data published; no data-availability statement in the version read |
| Bearing on U3 (writer's mapping) | The only photonic experiment read with two uses on each wing (G1). In the steering data the two wings' settings are matched (shared indices k and l), so with one wing's policy held, the remote wing's policy is determined with it: no remote policy is varied, and G3 and G4's comparisons are not available from these data. With n₁ = n₂ = 6, the sum in Eq. (10) runs over pairs (k, l) from one set of directions, which includes k = l, a repeated own setting *[writer's reading of Eq. (10)]*. The Bell-test configurations are not stated. First uses unsharp, so G4's repeatability does not apply. First-use records are configuration labels, not per-event detections |

### 1.10 White et al. 2016 (two-sided, superconducting)

| Field | Record |
|---|---|
| Citation | T. C. White, J. Y. Mutus, J. Dressel, et al., "Preserving entanglement during weak measurement demonstrated with a violation of the Bell–Leggett–Garg inequality", *npj Quantum Inf.* 2, 15022 (2016), doi:10.1038/npjqi.2015.22 |
| Version read | arXiv:1504.02707v2, FULL (main text) |
| Source | Two Xmon transmon qubits in the singlet state (Bell qubits β₁, β₂), each with an ancilla (α₁, α₂), on one linear chain of four qubits |
| Uses | **Both Bell qubits measured twice**: an ancilla measurement of strength φ ∈ [0, π/2] (projective at φ = π/2, none at φ = 0) at angle a (qubit 1) or b (qubit 2), then a rotation and projective readout at a′ or b′ |
| Settings and timing | One fixed configuration: a = 0, b = π/4 for the ancilla measurements, a′ = π/2, b′ = 3π/4 for the final readouts. "the data for each measurement angle is encoded on a distinct qubit"; "all four qubits are read out" |
| First-use and second-use record format | Per shot, each of the four qubits is read out separately (fresh-output form, per shot) |
| Postselection, heralding | No postselection stated; "near unit detection efficiency". The ancilla average is rescaled by a data-based calibration factor that sets the measured ground-state average to 1, so the ancilla correlators are calibrated, not raw. Locality is not enforced ("such an interaction cannot be ruled out here") |
| Raw data reported | The correlator ⟨C⟩ and its four terms against measurement strength φ (Fig. 3); 600,000 iterations per point; error bars ±10 standard deviations of the mean |
| Key numbers | BLGI violated "with 27 standard deviations of certainty"; ⟨C⟩ approaches about 2.5 at the weakest strengths |
| Completeness | No raw shot data published in the version read |
| Bearing on U3 (writer's mapping) | Two uses per wing (G1) with a setting change on each wing (a → a′, b → b′), and G2 per shot, in a single fixed configuration. Neither wing repeats its own setting and no remote policy is varied, so neither G3's nor G4's comparison is available. The first use is tunable up to projective strength (φ scanned from 0 to π/2; the text reports data "For projective angles φ ≈ π/2"); G4's repeatability fails because the settings change between the uses, not because of the strength |

### 1.11 Higgins et al. 2015

| Field | Record |
|---|---|
| Citation | B. L. Higgins, M. S. Palsson, G. Y. Xiang, H. M. Wiseman, G. J. Pryde, "Using weak values to experimentally determine 'negative probabilities' in a two-photon state with Bell correlations", *Phys. Rev. A* 91, 012113 (2015), doi:10.1103/PhysRevA.91.012113 |
| Version read | arXiv:1112.3664v3, FULL |
| What was done | Alice's photon: weak Ẑ measurement (displacement ∆r ≈ 150 µm on an ≈ 820 µm mode, knowledge K ≈ 0.024), then postselection in X̂; Bob: one projective use (P̂ or Q̂). "our experiment does not constitute a Bell test" |
| Record format | The weak outcome is not recorded per event: a slit is scanned across the beam (10 s per step, repeated 70 times) and weak-valued probabilities are computed from count rates |
| Postselection | Polarization postselection; "We subtract these accidental coincident counts from our results" |
| Bearing on U3 (writer's mapping) | Ensemble weak values, not per-event two-use records; G1–G4 not met |

### 1.12 Repeatability on one system (not a Bell setting)

| Field | Kirchmair et al. 2009 | Leupold et al. 2018 |
|---|---|---|
| Citation | G. Kirchmair, F. Zähringer, R. Gerritsma, M. Kleinmann, O. Gühne, A. Cabello, R. Blatt, C. F. Roos, *Nature* 460, 494–497 (2009), doi:10.1038/nature08172; title (abridged): "… experimental test of quantum contextuality" | F. M. Leupold, M. Malinowski, C. Zhang, V. Negnevitsky, J. Alonso, J. P. Home, A. Cabello, *Phys. Rev. Lett.* 120, 180401 (2018), doi:10.1103/PhysRevLett.120.180401; title (abridged): "Sustained … quantum contextual correlations from a single ion" |
| Version read | arXiv:0904.1655v2, FULL | arXiv:1706.07370v2, FULL |
| System | Two ⁴⁰Ca⁺ ions in one trap; sequential QND measurements of two-qubit observables by mapping and fluorescence detection | One ⁴⁰Ca⁺ ion as a qutrit; 53 million sequential QND projective measurements of 13 observables |
| Repeated observable | Sequences A_i A_j A_i are measured; p_err[A_i A_j A_i], "the probability that measuring A_j introduces a change on the value of A_i", enters the inequality ⟨X_DHV⟩ ≤ 2 | Repeatability R_u, the fraction of identical outcomes in two consecutive measurements of A_u (their Eq. (9)) |
| Settings | Fixed sequences per configuration | Chosen in real time by a quantum random number generator, latency below 50 µs |
| Record format | Each measurement's outcome recorded per run | Each outcome recorded per measurement |
| Raw data and completeness | None published in the version read | "The complete raw dataset is publicly available from an open repository" (tiqi.ethz.ch, public datasets; the repository was not opened). The paper states that the dataset "does not include the data purged in real time by the computer system due to long sequences of dark measurements" (subsequences with more than 55 dark results in a row, attributed to leakage out of the qutrit space, purged and restarted from the same v₀), and that of 54.5 million measurements about 1 million were ignored because of a thresholding error, leaving "almost 53.5 million" evaluated. *[Writer's reading: the published record is therefore not the complete record of all measurements performed, and the real-time purge is triggered by observed outcomes.]* |
| Key numbers | ⟨X_KS⟩ = 5.46(4) for the singlet. ⟨X_DHV⟩ = 2.23(5) > 2 was measured on a different state, Ψ ∝ \|↑↑⟩ + iγ\|↓↑⟩ + γ\|↑↓⟩ + i\|↓↓⟩ with γ = √2 − 1, using the Mermin–Peres square with σ_y and σ_z exchanged, for which ⟨X_KS⟩ = 5.22(10). Individual p_err values are not stated in the main text read | Repeatability "above 99.6 %", with deviations "on the order of 10⁻³" and R_h1 = 0.9967(2) the lowest; no detectable backward-in-time context signalling, small forward-in-time traces attributed to coherent-operation imperfections |
| Bearing on U3 (writer's mapping) | Same-observable repeats on one system. Not a wing of a Bell pair, so they bear on G4's repeatability only as single-system data, not on G1, G3 or G4's remote variation | As left; the published dataset is the only raw record in the set read, and its completeness is limited as stated above |

### 1.13 Items located but not read as experiments

- **Choi et al. 2020**, "Demonstration of simultaneous quantum steering by multiple observers via
  sequential weak measurements", *Optica* 7, 675 (2020), doi:10.1364/OPTICA.394667. **ABSTRACT**
  only (OpenAlex); full text **NOT READ** because opg.optica.org did not resolve. The abstract
  reports "simultaneous triple violations of the quantum steering inequality among four observers
  for a bipartite entangled system". Record format, settings and raw data are not known from the
  abstract.
- **Liu, Liu, Fang, Li, Wang**, "Both qubits of the singlet state can be steered simultaneously by
  multiple independent observers via sequential measurement", arXiv:2102.12166v1, FULL: numerical
  theory, no experiment.
- **Cheng, Liu, Baker, Hall**, "Recycling qubits for the generation of Bell nonlocality between
  independent sequential observers", arXiv:2109.03472v3, **ABSTRACT**: theory, not an experiment.
- **Cabello**, "Bell nonlocality between sequential pairs of observers", arXiv:2103.11844, and
  **Cheng, Liu, Baker, Hall**, "Limitations on sharing Bell nonlocality between sequential pairs
  of observers", arXiv:2102.11574; Crossref: *Phys. Rev. A* 104, L060201 (2021),
  doi:10.1103/PhysRevA.104.L060201: **LOCATED** only. The review of r1
  reports, at search-result level, that the first proposes an experiment with two Alices and two Bobs
  and the second proposes a test; neither is a performed experiment on that report, and neither was
  read here.

***

## 2. Summary against the reading grid

| Paper | Wings reused | First-use instrument | Per-event record of both uses | Settings | Same-axis repeat reported | Raw data published |
|---|---|---|---|---|---|---|
| Schiavon 2017 | one | weak | no (port per configuration) | per acquisition | no | no |
| Hu 2018 | one | weak, optimal | no (outcome per configuration) | per acquisition | no | on request |
| Feng 2020 | one | weak, optimal | no | per acquisition | no | no |
| Foletto 2020 | one (three uses) | unsharp, unsharp, projective | no (one branch per configuration) | per interval, history-dependent | no | no |
| Foletto 2021 | one (three uses) | weak | no | per acquisition | no | no |
| Padovan 2024 | one | weak | no | scanned | no | on request |
| Xiao 2022 | one | projective | no (polarizer per configuration; λ unrecorded) | per acquisition | contained in settings, not reported | no |
| Mao 2022 | one per branch | unsharp | yes (four detectors, time-tagged) | per acquisition | no | no |
| Zhu 2022 | **both** | weak, optimal | no (path postselection per configuration) | scanned, with the two wings' indices matched | no | no |
| White 2016 | **both** | ancilla, tunable up to projective | yes (per shot, four qubits) | one fixed configuration | no | no |
| Higgins 2015 | one | weak (ensemble) | no | fixed | no | no |
| Kirchmair 2009 | single system | projective QND | yes | fixed sequences | p_err used, values not stated in text read | no |
| Leupold 2018 | single system | projective QND | yes | QRNG, real time | R_u > 99.6 % | yes (open repository; real-time purges and about 1 million thresholding-affected measurements excluded) |

No paper read reports an XOR-only (same-register) record. Heralding is used in none; all photonic
results are conditioned on coincidence detection under fair sampling, and none of the Bell-type
experiments read reports space-like separation of the wings (the open locality loophole is stated
explicitly in Foletto 2020, Foletto 2021 and Padovan 2024; White 2016 states that an interaction
between adjacent qubits "cannot be ruled out here").

## 3. Findings for U3 (what the read set contains)

- **R-1 (G1).** Two of the experiments read measure both wings of one entangled pair twice: Zhu et al.
  2022 (photons, steering, the two wings' setting indices matched) and White et al. 2016 (transmons,
  one fixed configuration). Every other Bell-type experiment read reuses one wing only.
- **R-2 (G3).** No experiment read realizes the policy pattern of L-2's (k3): one wing repeating its
  own setting while the remote wing's policy varies. In Zhu et al.'s steering data the two wings'
  settings are matched, so the remote policy is never varied with the own policy fixed; the
  combinations acquired for their Bell test are not stated. White et al. change the setting on both
  wings in a single configuration, with no repeated own setting and no remote variation. No paper
  read reports the law of one wing's two-use outcome pair under different remote policies.
- **R-3 (G4).** No experiment read realizes (k3′)'s pattern (repeated own setting, varied remote
  first setting) on two-use wings, and no paper read reports a repeat of the same axis on one wing of
  an entangled pair after a projective first use. Xiao et al. 2022's stated case-1 settings contain such a repeat, and
  its frequency is not reported. Same-observable repeatability is reported for single trapped-ion
  systems: R_u above 99.6 % (Leupold et al. 2018) and p_err entering ⟨X_DHV⟩ = 2.23(5), measured on a
  non-singlet two-ion state (Kirchmair et al. 2009).
- **R-4 (G2).** Per-event records of both uses on the reused wing are stated in Mao et al. 2022 (four
  detectors per branch, time-tagged) and White et al. 2016 (per-shot readout of each qubit). Such
  fresh-output records determine the parity record as well. In every other photonic experiment
  read, the first-use outcome is fixed by configuration (one exit or port per acquisition), so the
  joint two-use table is assembled across acquisitions taken at different times. Padovan et al. state,
  of their scan, "since we are scanning the measurements one by one, we are effectively using
  different states for each measurement".
- **R-5 (G5).** One paper read publishes its raw dataset: Leupold et al. 2018, a single-ion
  experiment, whose public dataset excludes the subsequences purged in real time on long dark runs
  and about 1 million measurements affected by a thresholding error. No Bell-type experiment read
  publishes raw event data; two state availability on request (Hu et al. 2018, Padovan et al.
  2024). Settings are fixed or scanned per acquisition in every Bell-type
  experiment read; Foletto et al. 2021 state that their data are "only expectation values, hence this
  is not a true Bell experiment".
- **R-6 (status for U3 owner question 4).** On the papers read, the agreement condition of U3 §10.3
  (a performed experiment measuring one entangled source twice per wing with a setting change, whose
  raw complete local-history records show setting-independence and, for L-3, repeatability at
  repeated settings on both wings) is not met by any single experiment. The two two-sided experiments
  read do not realize the policy patterns the lemmas compare: Zhu 2022 matches the two wings'
  settings and uses weak first uses; White 2016 changes both wings' settings in one fixed
  configuration. Both report correlators, not per-wing two-use marginals, and neither publishes raw
  records. The only published raw dataset and the repeatability data read are single-system
  (Leupold 2018, Kirchmair 2009). Choi et al. 2020 was not read in full. This is a finding about the
  papers read, not about the literature as a whole.

## 4. Sources

Read in full (arXiv versions): 1611.02430, 1609.01863, 1912.02979, 1906.07412, 2101.12074,
2309.12286, 2212.03815, 2202.04840, 2102.02550, 1504.02707, 1112.3664, 0904.1655, 1706.07370,
2102.12166. Abstract only: doi:10.1364/OPTICA.394667 and doi:10.1103/PhysRevResearch.5.013104
(OpenAlex), doi:10.1088/1367-2630/ad48af (Crossref), arXiv:2109.03472. Located only:
arXiv:2103.11844, arXiv:2102.11574. Bibliographic checks: Crossref
records for each DOI cited above.
