# Chapter 15
# Quantum Engineering — Hardware, Software, and the BEC Experiment

***

## 15.1 What this chapter develops

Chapter 14 established the framework's content in computational complexity theory: BQP, under that chapter's explicit model hypotheses, as the computational class accessible to embedded observers, the Extended Church-Turing Thesis as a conditional result under the same hypotheses, the conjectured BPP–BQP separation as the cost of partial observation. The framework's content there is theoretical at the foundational level — a structural characterization, under those hypotheses, of what computations a qualifying observer can perform — the universal quantum (BQP-form) ECT resting on the additional global-coverage premise, with any super-BQP demonstration falsifying coverage first and the framework-plus-model conjunction only with further argument.

This chapter develops the framework's content in *engineered quantum systems* — the specific predictions for current and near-future quantum hardware platforms, the engineering implications of the framework's C1–C4 architecture, and the cleanest near-term experimental test of the proposed capacity-controlled memory mechanism — a proposal-level prediction, not a test of the characterization theorems (§15.2). The framework's distinctive prediction is that engineered quantum systems are not just noise-limited devices struggling against an adversarial environment but are *natural C1–C4 systems* whose dynamics is structurally non-Markovian. This reframing has concrete engineering consequences across superconducting qubit error correction, quantum sensing with NV centers, and the restricted quantum-statistical regime that current experiments are beginning to access.

Eight pieces occupy the chapter.

Section 15.2 develops the framework's reframing for engineered quantum systems: the environment as programmable quantum memory rather than as adversarial noise. The framework's C1–C4 architecture applies to engineered systems whose retention windows, set by $\tau_S/\tau_B$, fall within device run lengths — making the framework's content empirically relevant for current hardware platforms.

Sections 15.3 and 15.4 consider memory in superconducting qubits and tests of history-aware decoding. Two-level systems are one candidate carrier. In the reported Willow aggregate comparison, lag-based predictability rose with cycle depth, with individual detections and carrier attribution unresolved.

Sections 15.5 and 15.6 consider engineered baths and sensing. Detecting return in the relevant coherent signal and showing an equal-resource gain require specified device controls and readouts.

Sections 15.7 and 15.8 propose a capacity-dependent revival model and a test in a flowing Bose–Einstein condensate (BEC). The test requires calibrated capacity and timing factors and a two-preparation revival estimator.

The chapter closes with a discussion of the relationship between the framework's engineering predictions and the DSW horizon decoherence program from Chapter 9 §9.7. The BEC analogue-gravity setup tests in a laboratory system what the DSW analysis derives theoretically for astrophysical horizons; the convergence between the framework's content and the mainstream DSW program is significant. The framework's reach into engineering is therefore not isolated but is part of a broader convergence in mainstream physics on horizon decoherence as a fundamental phenomenon.

## 15.2 The environment as programmable quantum memory

Standard quantum engineering treats the environment as an adversary: decoherence destroys quantum information, and the goal is to isolate qubits from their surroundings as completely as possible. Better materials, deeper cryogenics, more careful shielding — the implicit design philosophy is that quantum systems should approach the closed-system limit, with the environment as an unavoidable nuisance to be minimized.

The framework's content suggests a fundamentally different design philosophy. Instead of isolating a qubit from all environmental coupling, *engineer* the C1–C4 memory architecture and realize the target quantum process as its finite-test shadow ([Main §3.4]) — the conditions do not by themselves select the operational mechanism. The hidden sector is not noise but *programmable quantum memory* — a resource that stores correlations written during one gate operation and returns them during subsequent operations. The bath becomes a design variable rather than a constraint.

A controllable environment could retain records that affect later gates. Its usefulness depends on the type of returned information, available controls and the task.

The implications are concrete. A qubit isolated from all environmental coupling has $\tau_S/\tau_B \to 0$ and behaves as an ideal closed quantum system at the qubit's own timescale, with decoherence eventually limiting performance through residual coupling. A qubit deliberately coupled to an engineered slow, high-capacity hidden sector — a built realization of C1–C4's persistence and capacity — with $\tau_S/\tau_B \sim 10^{-1}$ exhibits qualitatively different dynamics: memory of earlier gates where the bath's record is read back (C4), partial coherence revivals at the bath's correlation timescale where that return also revives distinguishability, and a non-Markovian noise structure that correlation-aware error correction can exploit.

**Engineering conditions.** A record carried by a bath must persist and affect the next-step visible law at fixed present. The ratio $\tau_B/\tau_S$ is a timescale estimate for candidate retention windows. Coupling, readback and measured signal determine the size of a correction.

**The cumulative pattern.** The framework's predictions across the engineered quantum systems summarize as follows.

| Domain | System / Bath | $\tau_S/\tau_B$ | Current relevance |
|--------|--------------|-----------------|-------------------|
| Cosmology | Observer / trans-horizon | $10^{-32}$ | Framework's home ground |
| Enzymes | Active site / scaffold | $10^{-9}$ to $10^{-12}$ | Chapter 13: consistent with data |
| Quantum sensing | NV spin / lattice defects | $10^{-6}$ | Approaching relevance |
| Quantum computing | Qubit / TLS | $10^{-3}$ | At the threshold |
| Atomic clocks | Atom / cavity | $\sim 10^{-6}$ | Potentially measurable |
| Engineered baths | Designed coupling | up to $10^{-1}$ | Future architectures |

A long retention window motivates a search for a matched-present history effect. A divisibility test and a measurement of any logical or sensing benefit are separate comparisons.

The remaining sections develop the framework's specific engineering content at each of these scales, with testable predictions for current and near-future quantum hardware platforms.

## 15.3 Superconducting qubits and TLS noise

Superconducting qubits — transmons, fluxonium, and similar architectures — are the leading commercial platform for quantum computing. Companies including IBM, Google, Rigetti, and IQM have demonstrated processors with hundreds to thousands of physical qubits, with active programs targeting fault-tolerant quantum computing at scale. The framework's content provides specific predictions for the noise structure that limits current performance and the design principles that could improve it.

**The TLS bath.** Superconducting qubits are fabricated as thin-film Josephson junctions on amorphous oxide substrates. The amorphous oxide contains *two-level systems* (TLS) — structural defects that flip between two configurations at characteristic rates determined by the local atomic environment. The TLS distribution is broad, with rates ranging from microseconds to seconds, and the TLS density is approximately $10^4$-$10^6$ per cubic micrometer for typical aluminum-oxide barriers. A transmon qubit typically couples to several hundred to several thousand TLS through its electromagnetic field.

**The framework's C1–C4 conditions for the transmon-TLS system.**

*C1 (coupling).* The TLS couple to the transmon through their electric dipoles, with coupling strengths varying from kHz to MHz depending on the TLS proximity to the qubit's electric field maxima. The coupling is continuous and bidirectional — qubit excitations can transfer to TLS and vice versa.

*C2 (memory persistence).* Transmon gate operations occur on $\tau_S \sim 10$-100 ns timescales. The TLS bath has correlation times $\tau_B \sim 1$-100 $\mu$s. The ratio: $\tau_S/\tau_B \sim 10^{-3}$ for typical operating conditions. This is twenty-nine orders of magnitude larger than the cosmological case, placing transmon-TLS dynamics squarely in the framework's slow-bath regime, with a retention window of $\sim 10^3$ gates.

*C3 (capacity).* A TLS bath has candidate record states. Its usable capacity depends on which states can retain distinguishable histories and influence the measured qubit.

*C4 (history readback).* A TLS record would satisfy C4 if histories with the same measured present gave different next-step laws through that record. The contrast and its attribution require measurements.

**A test of memory-bearing noise.** Compare the next error law after different histories matched at the present. A characteristic ratio $\tau_B/\tau_S\sim10^3$ gates motivates a choice of windows in the illustrative bath. It does not determine the size or even the existence of a readback effect.

Independent errors are a standard comparison. A Markov model with leakage, drift or a latent state can also produce correlated error records.

**Candidate empirical tests.**

*Lagged correlations.* Error correlations across gate separations can guide choice of timescales for the matched-present test. Correlations can persist in a Markov model with additional state variables.

*Higher-order statistics.* Conditional multi-time comparisons can test a declared history effect. P-indivisibility requires a separate witness for a specified map family.

*Surface-code logical errors.* A model of physical noise and a specified decoder can be used to predict and compare logical errors.

Correlated errors have been reported for several carriers, including cosmic-ray events and quasiparticles. The Willow comparison reported in [Complexity §8.2] finds an aggregate trend with depth relative to its detector-error model. The stricter analysis yields no defensible individual detections, and the backflow proxy is null in those streams. Carrier attribution and a measured decoder gain remain open.

## 15.4 Correlation-aware error correction

A history-aware decoder can use diagnostic past observations in addition to the current syndrome. Its performance depends on the code, noise, decoder comparison and implementation costs.

**A proposed decoder comparison.** Test a correlation-aware decoder against a specified baseline at matched physical operating conditions. The illustrative $\tau_B/\tau_S$ gives one candidate range of lags. The test needs to estimate which past observations add predictive information and how that information affects logical error.

The size of the reduction is not derived: converting the correlation length into an overhead requires a code, decoder and noise spectrum (§15.9).

Compare noise models and decoders on the same device regime at matched code distance, physical error rate and readout. The comparison should account for training, decoding latency and the resources needed at the target logical error rate.

Any overhead reduction would depend on those measured system and decoder properties.

**Falsification conditions.** A matched comparison can reject a predicted gain for the specified noise model, decoder and device regime. A separate test of C4 can reject a proposed history effect on the chosen window.

The aggregate syndrome observations motivate these comparisons. They leave the performance and mechanism tests open.

## 15.5 Coherence extension through engineered baths

An engineered bath could extend usable coherence if its dynamics restores the phase-sensitive signal needed by the device. This requires a comparison with matched controls.

**A candidate mechanism.** In a model with coherent coupling to a slow bath, some quantum information can transfer to and return from the bath. Which part returns to the logical or readout degrees of freedom depends on the model.

An exponential $e^{-t/T_2}$ is a common coherence benchmark. A rooted population revival certifies a divisibility failure for that map family. To claim coherent recovery, measure phase-sensitive revival for the relevant state preparations and controls.

How long the recovered signal persists depends on amplitude, coupling and other decoherence channels. The timing ratio alone leaves the achievable coherence extension open.

**Concrete platform: qubit coupled to a spin chain.** A specific platform implementing the framework's prediction is a qubit coupled to a linear chain of $L$ ancillary spins. The chain serves as the engineered hidden sector. Its correlation timescale scales as $\tau_B \sim L^z$ (where $z$ is the dynamical exponent — for a Heisenberg chain, $z = 1$). Its capacity scales exponentially as approximately $2^L$ states.

By tuning the chain length $L$ — the lengths below are illustrative estimates from $\tau_B \sim L^z$, not derived critical lengths — the framework's prediction is:

- Short chain ($L \lesssim 5$, $\tau_B \sim \tau_S$): how far the dynamics departs from the Markov benchmark, and whether any record survives to readback, depends on the coupling, the chain's conditional mixing and its readback; the ratio $\tau_B/\tau_S$ alone establishes neither memorylessness nor record survival.
- Long chain ($L \gtrsim 20$, $\tau_B \gg \tau_S$): memory-bearing regime where the chain retains its record and reads it back (C4). Correlations written at gate $k$ can then return at later gates, within a retention time of order $\tau_B/\tau_S$ gates under uniform erosion, partially restoring coherence. P-indivisibility of the qubit's population law on such windows is a further property, certified only by a divisibility witness.
Whether a record survives to readback depends on the chain's conditional mixing, not on a threshold in $\tau_B/\tau_S$; where a record survives and the chain reads it back (C4), the visible law carries accessible finite-horizon memory. On a fixed finite reversible representative, where recurrence returns the visible map to the identity and a readback gap forces a non-permutation rooted map, that memory also shows up as stochastic indivisibility of the visible population law across the recurrence cycle. Neither statement is a claim about generic open-system non-Markovianity of a quantum channel, which is a different notion and does not follow from either.

Spin chains, controllable nuclear spin baths and phonon modes offer candidate platforms. A platform test must verify that the returned record affects the chosen coherent signal and compare it with the appropriate control.

**Implications for hardware development.** The bath-as-resource philosophy has implications for hardware-development priorities. Current investment is concentrated on isolation and noise reduction. The framework's prediction is that complementary investment in engineered-bath architectures could produce comparable or larger gains at lower hardware cost. Whether this prediction generates commercial uptake depends on whether early demonstrations of the framework's predicted coherence extension are achieved at sufficient scale to be competitive with continued isolation improvements.

## 15.6 Quantum sensing with NV centers

Nitrogen-vacancy (NV) centers in diamond are the leading platform for room-temperature quantum sensing — magnetic field measurement, temperature sensing, biological imaging, and related applications. Current NV sensitivity is limited by the spin coherence time $T_2$ of the NV electron spin, with standard Markovian models predicting that improvements in sensitivity require improvements in $T_2$. The framework proposes that sensitivity can be improved beyond the Markovian $T_2$ limit through exploitation of information backflow from the diamond lattice's slow phonon and nuclear-spin baths, where those baths' return revives distinguishability.

**The C1–C4 architecture of NV centers.** The NV center's electron spin couples to multiple baths in the diamond lattice: phonons (acoustic vibrations of the diamond crystal), nuclear spins ($^{13}$C nuclei in natural-isotope diamond, P nuclei in synthetic diamond), and paramagnetic impurities (other defect centers). Each bath contributes to decoherence at characteristic timescales.

The relevant timescale separations are: NV electron-spin dynamics at $\tau_S \sim 10$-100 ns; phonon-bath correlation times $\tau_B \sim 1$-10 ms; nuclear-spin bath correlation times $\tau_B \sim 1$-100 ms. The ratio: $\tau_S/\tau_B \sim 10^{-5}$ to $10^{-6}$ — within the framework's slow-bath regime where memory effects become predictable.

**The proposed sensing mechanism.** An NV-center bath can affect the time dependence of the measured signal. A population revival or a slow bath mode leaves open whether the phase-sensitive signal used by the protocol recovers.

Sensing protocols that exploit the revival — measuring at the backflow time rather than during the initial decay — could push sensitivity beyond the Markovian-assumed $T_2$ limit.

**Sensitivity.** Standard NV magnetometry sensitivity is $\delta B \sim 1/(\gamma \sqrt{T_2 \cdot T_{\text{meas}}})$, where $\gamma$ is the gyromagnetic ratio and $T_{\text{meas}}$ is the total measurement time. Where the bath's return at $\tau_B$ revives distinguishability (information backflow), each measurement recovers information that Markovian protocols assume is lost.

Sensitivity depends on interrogation time, visibility, noise and readout under the same resource budget. A measured revival is relevant if it improves the signal-to-noise comparison with a specified reference protocol.

**Empirical test.** Characterize the bath and measure the phase-sensitive signal across candidate interrogation times. Compare the resulting sensitivity at matched total resources with the reference protocol. A gain then has the scope of that device and protocol.

A large improvement in NV sensitivity at room temperature would be transformative for biological imaging, medical diagnostics, and geophysical sensing applications. The framework's prediction is therefore not isolated theoretical content but a specific commercial design target with empirical accessibility on existing hardware. Falsification would come from demonstration that backflow-aware protocols do not improve integrated sensitivity over the Markovian protocol on the same hardware across multiple NV platforms — suggesting that backflow in these baths, where present, is too small or too thermally averaged to be exploited.

## 15.7 The restricted quantum-statistical regime in engineered systems

Beyond the revival effects developed in §§15.3-15.6 where a slow bath's return revives distinguishability, the mechanism proposal predicts a *restricted quantum-statistical regime* at marginal hidden capacity: partial distinguishability revival, $0 < \mathcal{N} < 1$ (Chapter 18 §18.3). In this regime — on the mechanism proposal's hypothesis — engineered systems exhibit dynamics whose memoryless operational modeling — divisible-channel accounts of preparation and intervention — gives out, while the quantum representation at the transition-statistics layer is retained ([Main §3.4]); any stronger operational-failure reading is a mechanism-proposal claim, stated as such, and the regime is distinguished from complete revival and from no revival by distinguishability-revival measurements, not by the memory test alone.

**The structural condition.** C3 is sufficient memory capacity — $N_H \gg N_V$ is the comfortable physical regime, not the condition itself ([Main §3.4]) — and is required for the memory-bearing sector at full strength. Capacity bounds memory without fixing revival. The capacity floor caps $M_t$ at $\log_2|\mathcal{C}_H|$, so a one-state hidden sector forces $M_t = 0$ ([Main §3.4]). A capacity margin does not by itself produce revival: adjoining an idle hidden register to the XOR control of [Main §2.3] enlarges its hidden capacity without changing its visible law, which carries memory with $\mathcal{N} = 0$ on a window containing that memory. The mechanism proposal hypothesizes that comparable capacities, $N_H/N_V \sim 1$, produce partial revival — the restricted quantum-statistical regime, explicitly not a quantum-membership scale, since every finite law at every $\mathcal{N}$ admits both the quantum representation and a deterministic hidden realization ($S \iff D$, [Main §3.4]).

In engineered systems, the hidden capacity is *controllable*. By designing the hidden-sector capacity (the number of TLS in a superconducting qubit's substrate, the number of nuclear spins in an NV center's bath, the length of an engineered spin chain), the engineer sets the capacity ceiling on accessible memory — the theorem-level content; the mechanism proposal hypothesizes that this choice positions the system on the revival scale $\mathcal{N}$. This is a new design degree of freedom whose predicted empirical consequences, on that proposal, are distinct from continuous-decoherence accounts of the quantum-classical boundary.

**The framework's prediction.** In the restricted quantum-statistical regime, the mechanism proposal predicts that multi-time correlation functions show structural signatures distinct from both memoryless quantum modeling and memoryless classical probability — proposal-level claims about the accessible dynamics, not about representability ([Main §3.4]). Specifically:

*Multi-time joint distributions.* C4 excludes a memoryless Markov description of the declared visible statistics. A rooted map family can still be P-divisible on that window. Revivals require a separate distinguishability comparison. The fixed-basis representation applies to the finite law in both cases ([Main §3.4]).

*Memory saturation.* Accessible memory is capped by hidden capacity, $M_t \le \log_2|\mathcal{C}_H|$ ([Main §3.4]). The mechanism proposal predicts that distinguishability revival falls below its saturated value at marginal capacity, $r = N_H/N_V < 1$, with the form $\mathcal{F}(r)$ below; no further saturation pattern is specified.

*Capacity dependence.* The mechanism proposal's model gives the normalized revival measure as $\mathcal{F}(r)$, with $\mathcal{F} \to 1$ for $r \gg 1$ (saturated revival, $\mathcal{N} = \mathcal{N}_{\max}$ at small $\tau_S/\tau_B$, §15.8), $\mathcal{F} \to 0$ for $r \ll 1$ (no revival), and $\mathcal{F}(r) = 2r - r^2$ for $r < 1$, increasing on that range. This functional form is distinctive and falsifiable: it is the framework's PROPOSED model prediction — proposed, not theorem-derived (see below) — for how revival falls from saturated to none as capacity is reduced.

**The functional form $\mathcal{F}(r) = 2r - r^2$.** The quadratic dependence is MOTIVATED by the $1/\omega$ Planckian spectral falloff combined with the framework's structural conditions in the marginal-capacity regime. A detailed derivation is not packaged in this release, and the functional form is accordingly a proposed model prediction rather than a theorem-derived one (prediction-status appendix); the structural heuristic is that the lowest-frequency modes (which carry the most entanglement) are removed first as capacity is reduced, with the quadratic form being the integrated effect of this preferential removal.

The functional form distinguishes the proposal's prediction from the alternative accounts considered. The particular alternative models analyzed in §15.8's control set produce either continuous exponential decay of the revival measure (with no structural transition) or first-order linear behavior $\mathcal{F}(r) = r$ at marginal capacity — a claim about that comparison class, not about open-system models generically. The quadratic $2r - r^2$ form is distinctive of the proposed mechanism among the alternatives considered, and is empirically diagnostic of it.

**Candidate test platforms.** The model associates marginal revival with comparable *accessible* capacities, $N_H/N_V\sim1$. Realizing that regime requires a measurement model and independent calibration.

*BEC analogue-gravity systems.* Varying $L_{\text{super}}$ changes the modeled modes in §15.8. Their effective capacity also depends on the measured flow and condensate parameters.

*Engineered spin chains.* Varying chain length changes the nominal dimension. Which chain states are accessible depends on coupling, preparation and readout.

*Designed photonic systems.* Controllable defect modes could provide a way to vary capacity. The experiment would need to determine the modes used by the measured dynamics.

**Diagnostic measurements.** The mechanism proposal's prediction of the restricted quantum-statistical regime is diagnosable through distinguishability-revival measurements. The key observable is the revival measure $\mathcal{N}$ of Chapter 18 §18.3: the largest increase, over the accessible window, of the total-variation distance between the visible population laws of two initially distinguishable preparations evolved through the system (the trace distance of their diagonal states). Its dependence on $r$ — on the proposal, the $2r - r^2$ form — is the proposed empirical signature.

The next section considers a BEC experiment for the proposed capacity law.

***

## 15.8 The BEC analogue-gravity experiment

A flowing BEC with sonic horizons offers a candidate test of the proposed capacity-dependent revival form $\mathcal F(r)=2r-r^2$. The experiment needs a calibrated map from the apparatus to the model and a measured revival for two preparations.

**The analogue-gravity setup.** A flowing BEC produces a sonic horizon where the flow velocity equals the speed of sound. Phonons emitted in the supersonic region cannot propagate against the flow back into the subsonic region — exactly analogous to how photons inside a black hole event horizon cannot escape to infinity. The Hawking-Unruh effect predicts that the sonic horizon should emit thermal phonons at a temperature determined by the flow's velocity gradient — analogue Hawking radiation.

The Steinhauer group at the Technion has demonstrated this experimentally over the past decade. Their setup uses a Rb-87 BEC in an elongated trap, with a step in the trap potential producing a region of supersonic flow that acts as the analogue horizon. The experimental observation of analogue Hawking radiation and the measurement of its thermal spectrum has been progressively refined; their 2016 paper provided the first observation, with subsequent work refining the measurement.

**The framework's modification.** The framework's content goes beyond reproducing analogue Hawking radiation. The mechanism proposal predicts that the distinguishability revival $\mathcal{N}$ of the subsonic-region phonon dynamics depends on the *capacity* of the supersonic-region (hidden-sector) phonon modes, with the dependence following the proposed model form $\mathcal{F}(r) = 2r - r^2$ for $r = N_H^{\text{eff}}/N_V < 1$.

The model varies capacity with $L_{\text{super}}$ through the calibrated inputs of the formula below. For $r\geq1$ the capacity factor saturates. For $0<r<1$ it is reduced according to the proposed quadratic form. The observable amplitude also includes the timing factor and the scale $\mathcal N_{\max}$.

**The framework's full prediction.** Including both the capacity (C3) and the memory-timescale (C2) factors, the framework's prediction is
$$\frac{\mathcal{N}(L_{\text{super}})}{\mathcal{N}_{\max}} = \mathcal{F}\!\left(\frac{N_H^{\text{eff}}(L_{\text{super}})}{N_V}\right) \cdot \left(1 - \frac{\tau_S}{\tau_B(L_{\text{super}})}\right),$$
with $N_H^{\text{eff}} = \min(L_{\text{super}}/\pi\xi,\; \kappa_s L_{\text{super}}/\pi c_s)$ (where $\xi$ is the healing length, $\kappa_s$ is the surface gravity, $c_s$ is the speed of sound), $N_V = \kappa_s L_{\text{sub}}/\pi c_s$ (where $L_{\text{sub}}$ is the subsonic region length), and $\tau_B = L_{\text{super}}/|v - c_s|$.

The test needs an independent calibration of the parameters in $r=N_H^{\text{eff}}/N_V$, the timing factor and the amplitude scale $\mathcal{N}_{\max}$. A large-$r$ configuration with small $\tau_S/\tau_B$ is a candidate reference for the scale.

**The experimental protocol.** The proposal uses a black-hole–white-hole pair in a flowing BEC. The proposed scan in $L_{\text{super}}$ illustrates the range over which one would calibrate the modes and estimate revival.

1. Prepare the BEC and allow Hawking radiation to reach stationarity (approximately 10 ms).
2. Measure the density profile at a sequence of times separated by approximately 0.1 to 1 ms.
3. Repeat approximately $10^3$ times per $L_{\text{super}}$ value.
4. Compute $G_{\text{sub}}^{(2)}(\Delta t)$ as an auxiliary measure of temporal density correlations. Its oscillations or nonmonotonicity cannot estimate the revival of distance between two preparations.
5. Prepare two specified initial perturbations and estimate their visible population distributions at matched times and controls. Use the total-variation distance $D(t)$ and test for an increase across the declared window to estimate $\mathcal N$ for those preparations.

**Controls.** A comparison must measure or hold fixed the capacity and timing factors that the model does not intend to vary.

*Reference without the supersonic region.* Estimate the same two-preparation quantity in a matched reference as a baseline for intrinsic dynamics and readout artifacts.

*C2 test.* When changing flow at fixed $L_{\text{super}}$, measure $\kappa_s$, $c_s$ and $\xi$ and verify or model any change in $r$. The timing factor can be tested separately if the capacity ratio and other relevant conditions are controlled.

*Thermal test.* Temperature changes can affect the sound speed, healing length, surface gravity and relaxation. Measure or match the capacity ratio and timing factor across thermal controls before attributing a residual change.

**Size of the modeled effect.** For calibrated $r=0.5$ and $r=0.25$, the capacity factor alone is 0.75 and 0.4375 respectively. Actual normalized revival multiplies these values by the timing factor. The lengths that yield the quoted ratios depend on the measured BEC parameters.

The noise of density autocorrelation measurements constrains that auxiliary observable. Uncertainty in the revival statistic depends on estimation of two distributions, preparation and measurement errors, and temporal sampling.

Estimate uncertainty for the chosen two-preparation statistic, including time correlations, finite-sample bias from estimating distances and maxima, and uncertainty in the calibration of $r$ and $\mathcal N_{\max}$. The achievable precision remains to be established for that protocol.

**Comparison with backgrounds.** The proposed $2r-r^2$ dependence can be compared with alternatives at matched timing and readout. An experiment needs models of the same revival observable for the relevant backgrounds.

*Bogoliubov–de Gennes dynamics.* Standard BdG calculations describe mode mixing and occupation in the given flow. A quantitative comparison requires computing the two-preparation statistic under the same conditions.

*Other backgrounds.* Interaction-driven dynamics, losses and trap noise can affect the measured signal. Their effects need independent controls and an uncertainty estimate on the actual statistic.

**Relation to DSW horizon decoherence.** The BEC analogue-gravity test is structurally related to the Danielson-Satishchandran-Wald (DSW) horizon decoherence program developed in Chapter 9 §9.7. DSW prove within standard QFT in curved spacetime that Killing horizons impart fundamental decoherence on nearby quantum superpositions, with rate determined by horizon geometry. The framework's BEC analogue-gravity test extends DSW's analysis to the *capacity-controlled regime* (marginal hidden capacity) that DSW does not address.

The convergence is theoretical. DSW derive within standard physics a feature the framework's universality-class commitments share — horizons impose decoherence, with geometry setting the relevant parameters — and add no empirical evidence for the framework. The BEC analogue-gravity test provides empirical access to the framework's distinctive content (capacity-controlled revival in the restricted quantum-statistical regime) in a laboratory apparatus. The two are complementary: DSW for theoretical convergence at the universality-class level, BEC for an empirical test of the distinctive content of the restricted quantum-statistical regime.

**Implications.**

Agreement with $\mathcal F(r)=2r-r^2$ after the calibration and background comparisons would support the proposed capacity-dependent mechanism in the tested system.

A calibrated null result could constrain the mechanism in the tested range if the experiment has adequate power for the predicted amplitude.

A reliably different dependence on capacity under matched conditions would reject the proposed curve for that setup.

The BEC scenario defines a possible mechanism test. Feasibility depends on implementing the paired-preparation readout, calibrating the model inputs and estimating the uncertainty.

## 15.9 Chapter close

This chapter proposes engineering comparisons for accessible memory, revival and device performance.

**Engineering tests.**

1. *Correlation-aware error correction.* Compare specified decoders at matched code and noise conditions (§15.4). The size of any gain remains open.

2. *Coherence extension through engineered baths.* Test phase-sensitive recovery and its duration under specified bath and control dynamics (§15.5).

3. *Backflow-aware NV sensing.* Compare measured sensitivity with a matched reference. The result depends on coherent signal recovery, readout and resource accounting (§15.6).

4. *Restricted quantum-statistical regime.* Engineered systems at marginal hidden capacity ($N_H/N_V \sim 1$) are predicted, on the mechanism proposal, to show the proposed $\mathcal{F}(r) = 2r - r^2$ form (§15.7). Diagnosable through distinguishability-revival measurements.

5. *BEC analogue-gravity test.* Calibrate capacity and timing, and estimate revival from two preparations with suitable controls (§15.8).

**Three categories of empirical exposure.**

The chapter's content sorts into three empirical categories.

*Decoder benchmark.* Reported aggregate syndrome trends motivate a matched comparison of logical error and resource costs.

*Signal tests.* The engineered-bath and NV proposals need readout for the relevant coherent signal and matched reference protocols.

*Capacity test.* The BEC and other candidate platforms need calibration of the parameters and a revival estimator.

The effect on logical error, coherence or sensitivity is a separate outcome in each specified device test.

These comparisons apply the finite-horizon memory and divisibility diagnostics to proposed hardware mechanisms.

**Forward pointers.** Chapters 16 and 17 develop candidate clinical and bioinformatics applications with their own empirical and modeling premises.

The framework's empirical reach across Chapters 13-17 is concentrated at the application level — specific predictions for biology, computing, engineering, medicine, and bioinformatics. The framework's content here in quantum engineering is the bridge between the foundational chapters (1-9) and the applied chapters (13-17), demonstrating that the framework's structural commitments at the substratum level produce specific quantitative predictions across multiple engineering domains.

***
