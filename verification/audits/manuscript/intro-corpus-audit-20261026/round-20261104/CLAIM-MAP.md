# Claim map: `papers/Introduction.md` against `main` `f5c281ae`

Round 2026-11-04 of the #941 audit. **Not independently reviewed.** Every row is the writer's
reading and is provisional until the independent review recorded on #918.

- **Introduction lines** are those of `69079058` (this round's corrected text; 483 lines). Where a
  correction of this round changed the claim, the row gives the corrected wording's status and the
  finding ID.
- **Sources** are `file:line` at `main` `f5c281ae10a913ec68fa41b3b839ad0b164979cd` unless stated.
  Lean identifiers are in `verification/lean-mathlib/OIBridge/`; every baseline identifier of
  Appendix A resolves at the line Appendix A gives, both at `17b830bc` and at `f5c281ae` (checked by
  reading the sources; no build was run).
- **Class** (owner guidance, 2026-11-04): exactly one of *proved*, *conditional*, *posit*, *open*,
  *refuted*. A proved claim carries its support **layer**: K kernel-checked; A exact algebra;
  E exhaustive finite computation; P paper derivation; N numerical/instance computation;
  L external literature (imported; the literature's proof, not OI's). A row whose chain mixes
  layers names each link; the claim takes its weakest link.
- **Verdict**: supported as stated / overstated / outdated / unsupported / underclaim.
- Literature rows keep "the literature proves X" apart from "OI proves X": an imported result
  supports the Introduction's statement of what the literature says, not a derivation from OI's
  premises.

## A. Claims that still need a correction or an owner decision

These rows are also findings in `README.md` §3. Every other row (part B) is supported as stated on
the writer's reading.

| ID | Lines | Claim | Class | Layer / hypotheses | Source | Verdict | Finding |
|---|---|---|---|---|---|---|---|
| C-116 | 116 | Constant-on-fibre criterion, initial/current/hidden singleton criteria and two-reading swap identification are machine-checked | proved | K, but census family `RecordFibreIdentification` is `kernel-only` with note "No publication-facing promotion … before successful CI and independent proof review" | `lean-manuscript-census.json` family "known-model nonempty record-fibre…"; Substratum:348–360 (P, Prop. 24.5) | overstated relative to the census contract (statement itself matches the module) | F-14 |
| C-126 | 126–132 | Actual finite-permutation trajectory capacity bound, finite-block supremum and entire-future bound are machine-checked | proved | K in `TrajectoryMemory`, `FullFutureMemory`; both families `kernel-only`, no manuscript anchor | census families "actual finite-permutation trajectory bridge…", "entire visible future…" | overstated relative to the census contract | F-14 |
| C-158 | 158, 174, 322, App. A 360 | Positive rooted return, common period and recurrence-cycle indivisibility from a non-permutation rooted matrix are machine-checked | proved | K in `RootedRecurrenceBridge` (`kernel-only`); the anchored route is Theorem 3 (`pIndivisible_of_rooted_identity_return_of_overlap`, current) plus paper steps (Main:139 says $\Gamma_L=I$ and the non-permutation→overlap step are proved on paper) | Main:137–139; census | overstated relative to the census contract | F-14 |
| C-238 | 17, 238, 320, 328 | Which of (iii)–(v) a physical substratum supplies is open | open | — | GR:228 (question isolated); GR:260: finite bijective read-write dynamics with the stated access supplies neither the quarter phase (`onesFixing_not_phasesAvailable`, `PhaseSource`) nor continuous state mixing (`readWriteSourced_not_qm`, `ReadWriteControl`); both families current | underclaim: the bare-substratum part is settled negatively in the kernel; what remains open is a substratum with further intervention principles | F-18 (OD-2) |
| C-252 | 252–258 | §3.4 reports the finite-substratum obstruction only | proved | P (factorization) + L (unboundedness, HKLP24) | Main:560; Main:22 and §3.4 gluing / uniform-continuum (ε) theorems, Main:566–602 | underclaim (the ε-realization half is omitted) | F-19 (OD-3, R-07/R-40) |
| C-174r | 174, App. A 356 | Indivisibility at some return horizon is machine-checked from the routed form of (C4) | proved | K: `routed_forces_indivisible_somewhere` (seed-conditioned reading). The storage-time reading `routedAtStorage_forces_indivisible_somewhere` is the one matching the Introduction's gloss | Main:147 (both readings, neither implies the other); census families current | supported, incomplete (one of two formalizations; owner disposition OD-5 cites storage-time as primary) | F-20 |
| C-304s | 304 | Hiding the message completely is as in perfect secret sharing, Shamir's scheme the standard example [Sha79] | proved | L (Sha79 not read first-hand; not on arXiv) + P (BHa C4 rank law) | `bh01_access_v1/REPORT.md`:125–132 | unsupported as cited until read | F-21 (OD-8) |
| C-314 / C-316 | 314–316, 322 | Finite coherent-subspace entropy profile [CE] and sequential-release construction [CR] are proved on paper | proved | P with exact controls; [CE] independently accepted in-tree (`independent-core/review.md`); [CR] has no retained independent review (#970) | `verification/audits/manuscript/page-coherent-recovery-20261028/` on #918 only (not on `main`) | [CE] supported; [CR] listed under "Established mathematical results" without independent review | F-15, F-16 |
| C-304 | 304, 306, 322 | BHa counts (1,376 of 40,320; 60; 32) and the $1/\vert \mathcal U\vert $ floor | proved | E (exhaustive enumeration, reproducible from `checks.py`, `result.json`) + P (floor, C2) | `bh01_access_v1/REPORT.md`:18, :21, :101–111, :148–155 | supported; the record's own status line reads "exploratory research, unreviewed for adoption" while its review directory exists | F-23 |
| C-371 | 371 | GR and the Book "include the scoped SC-36 reconciliation from `021850d9` and the Book regress correction from `a2be1e45`" | — (pin) | — | both commits diverge from `main` and from #918's head (GitHub compare API, 2026-11-04) | content used is on `main` (GR:839–853; `book/ch03-structural-realism.md`:218); pins off `main` | F-17 |
| C-387 | 387, 389 | [CE], [CR] "source checkpoint `bdcbd32`, `2624d49`" | — (pin) | — | both diverge from `main` and from #918's head; the cited proof and control blobs are byte-identical in #918's tree | support off `main` until #918 lands; commit reachability unresolved | F-15 |

## B. Claims supported as stated

### Abstract and §1

| ID | Lines | Claim | Class | Layer / hypotheses | Source | Verdict |
|---|---|---|---|---|---|---|
| C-001 | 17, 33 | OI: every physical observer is a proper part of a reversible deterministic system, resolves finitely many visible configurations, records only visible marginals | posit (physical hypothesis) | — | Main:44, :56, :62 (bijective substratum a representation choice; total finiteness a posit) | supported |
| C-002 | 17, 31, 33 | Finiteness of the whole system is a posit of the finite models, not a consequence of embedding | posit | — | Main:62; Main:113; Main:726 ledger item (ii) | supported (Main:720/722/726 reconciliation owned by #1015) |
| C-003 | 17, 39, 67–71 | Theorem 1: $\mathsf S_K=\mathsf D_K=\mathsf Q_K$ at every finite horizon | proved | K: `finite_horizon_equivalence` (Equivalence:462), `S_imp_D` :422, `D_imp_Qfb` :294, `Qfb_imp_S` :245 | Main:548–554 | supported |
| C-004 | 17, 83 | Known components (Egri et al.; Barandes) stated as one machine-checked theorem | proved | K + L (attribution) | Main:548–554; EGGH26 (not re-read this round) | supported (attribution traced by #942, provenance) |
| C-005 | 17, 99–114 | Every faithful realization carries the law's conditional memory in its hidden state | proved | K for a joint law (`unavoidable_hidden_predictive_memory`, HiddenMemory:185); P for the time-$t$ reading | Main:604–612 | supported |
| C-006 | 17, 160, 168 | Rooted forecasts P-indivisible somewhere in the recurrence cycle whenever some rooted table is not a permutation, in particular whenever a visible step is non-deterministic, hidden prior shared and independent | conditional (shared independent hidden prior; finite bijection) | K (Theorem 3 + stochastic-inverse lemma) + P (history/non-deterministic step → non-permutation) | Main:137–141 | supported |
| C-007 | 17, 160, 168, 174 | With full-support visible prior, equivalent to $M_k>0$ at some $k<L$ | conditional (full support) | P, each direction identified at L174 (§A.34): ⇐ Main:137; ⇒ Main:141 | Main:141 | supported |
| C-008 | 17, 226–236 | Theorem 4: available families exactly the normalized finite Kraus instruments iff (i)–(v), given complex matrix kinematics and tensor composites | conditional (assumed kinematics) | K: ⇒ `physical_of_exactAll`; ⇐ `exactAll_of_physical_general`; assembled `exactAll_iff_physical_general` | GR:216–218 | supported |
| C-009 | 17, 238 | Neither the kinematics nor the conditions follow from bare OI | proved (negative, for the stated theories) | K: `oi_alone_not_qm`, `five_way_minimality` | GR:220 | supported |
| C-010 | 17, 278 | OI places the zero-point sum and the effective $\Lambda$ at different levels | proved (descriptive) | P | GR:356 ("Descriptive distinction established") | supported |
| C-011 | 17, 300–306 | OI separates conservation of black-hole information from accessible recovery | proved (finite toy models) | E + P | C-304 | supported, scope finite toy |
| C-012 | 17, 334 | Open: completion conditions a substratum supplies, Born exponent, field equations | open | — | GR:228; Main:556; GR:356 | supported in part; see C-238 (F-18) |
| C-013 | 23, 25, 187–198 | Two-card game: one shuffle 1/2, two shuffles 1, peek 1/2, Markov 1/2; classical statistics | proved | A (exact enumeration, hand-checkable) | Book ch01 §1.11 (`book/ch01*`:265); Main:720 swap realization | supported |
| C-014 | 29 | Hidden states compatible with the same visible state *can* send it to different futures | proved | P | Main:105 (corpus side reads universally; routed, R-30) | supported |
| C-015 | 31, 53 | Prior is part of the realization datum; counting measure a maximal-entropy default | posit (selection principle) | — | Main:56, :60, :726 ledger (iv) | supported |
| C-016 | 33, 116 | A quantity is identified exactly when constant on the compatible initial states | proved | P (Prop. 24.5); K core (see C-116) | Substratum:348–360 | supported (paper); machine-check claim: F-14 |
| C-017 | 33 | No uncertainty relation constrains fixed-readout visible laws | proved | K (via Theorem 1) | Main:594 | supported |
| C-018 | 35 | An exactly decoupled deeper register can be added without changing the visible law, under Theorem 24(iii)'s preparation assumptions | proved | P | Substratum:256–261 | supported |
| C-019 | 35 | Restricted invariances do not classify every deeper implementation or prove the regress ends | open | — | Substratum:60; Book ch03:218 | supported |
| C-020 | 41 | Results of §§3.2–3.5 proved in [GR] and [Main]; §5 in unpublished research records | proved / records | — | GR §3.3; Main §§3.3–3.4; BH records | supported (record status: F-23) |
| C-021 | 43 | Conventions: "machine-checked", "proved on paper", "exact probe" | — (definition) | — | — | corrected this round (E1, F-01) |

### §2.1–2.3

| ID | Lines | Claim | Class | Layer / hypotheses | Source | Verdict |
|---|---|---|---|---|---|---|
| C-022 | 55–59 | Definitions of $\mathsf S_K$, $\mathsf D_K$, $\mathsf Q_K$ | — (definition) | — | Main:548–552 | supported |
| C-023 | 75, 77 | Trajectory-storing realization with clock; hidden-register picture | proved | K (`S_imp_D`) | Main:554 | supported |
| C-024 | 77 | Independent-prior realization for rational conditional kernels at positive-probability histories; arbitrary visible initial law; response-table extension for arbitrary kernels; proved on paper with exact probes | proved | P + N (exact rational instances; "exact probe" as defined at L43 after E1) | Main:518–522 | supported (after E1) |
| C-025 | 79 | $\mathsf D_K\subseteq\mathsf Q_K$ by the permutation unitary; $\mathsf Q_K\subseteq\mathsf S_K$ is the Born rule | proved | K (`D_imp_Qfb`, `Qfb_imp_S`, `permMatrix_mem_unitaryGroup`) | Main:554 | supported |
| C-026 | 83 | EGGH26 Prop. 13/16, LP17 Prop. 1.5, Bar25/Bar23/Bar26 §4, SGD19 Eq. (3) attributions | — (attribution) | L, not re-read this round | traced by #942 (provenance) | not re-checked this round |
| C-027 | 83 | One-step $\vert \mathcal C_V\vert ^2$ ancilla dilation of [Main §3.1] is that of [Bar26, Thm 3.3] | proved | P (Main) + L (Bar26 read first-hand, arXiv:2608.04354v1 Thm 3.3, eqs. (43), (50)) | Main:212–216 | supported (up to index conventions); [Sch21] use removed (E10, F-09) |
| C-028 | 89 | Markov laws lie in all three classes | proved | K | Main:556 | supported |
| C-029 | 91 | $p=\vert U\vert ^2$ is definitional in $\mathsf Q_K$; permutation unitaries do not select the exponent | proved | A | Main:556 | supported |
| C-030 | 93 | One fixed finite realization has an $L$-periodic law; no exact all-time realization of a nonperiodic law by one fixed substratum | proved | P | Main:640 | supported |
| C-031 | 95 | No record of one repeated measurement can by itself rule out a partly hidden deterministic account | proved | K (Theorem 1) | Main:556 | supported |

### §2.4 Where the memory lives

| ID | Lines | Claim | Class | Layer / hypotheses | Source | Verdict |
|---|---|---|---|---|---|---|
| C-032 | 101–112 | Theorem 2 (a)–(c) | proved | K for a joint law (`pushforward_identity` :83, `distinguishability_floor` :114, `capacity_floor` :170, `unavoidable_hidden_predictive_memory` :185); P for the time-$t$ reading | Main:604–612 | supported |
| C-033 | 118 | Memory witness exists exactly when $M_t>0$ | proved | L (vanishing criterion of CMI, [CT06]; standard) | Main:99 | supported (CT06 locator: OD-8) |
| C-034 | 120–122 | Corollary: $M_t>0$ iff every faithful realization carries readout-relevant hidden memory; directions identified | proved | P (both directions named; converse uses `S_imp_D`) | Main:99, :612 | supported |
| C-035 | 122 | Every reversible world run from the start stores its whole visible past | proved | P | Main:99, :612 | supported |
| C-036 | 124 | $\vert \mathcal C_H\vert \ge2^{I^*}$ | proved | K (`card_hidden_ge_two_pow_Istar`, C3Necessity:117) | Main:514 | supported |
| C-037 | 124 | Least hidden predictive memory over deterministic completions equals $I(X_{<t};X_{>t}\mid X_t)$, equals $M_t$ iff the stated CMI vanishes; bijective realizations carry $H(X_{<t}\mid X_t)$ | proved | K lower bound for bijective (`c3_necessity_via_hidden`); P for non-injective, attainment and equality condition | Main:616 | supported |
| C-038 | 124 | Pinsker floor $M_t\ge p_0\delta^2/\ln2$ | proved | P (the probe computes information quantities in floating point, Main:176; tag removed, E2) | Main:173–176 | supported (after E2) |
| C-039 | 134 | (C1)–(C4) are diagnostics, not hypotheses of Theorem 1; (C1) follows from (C4); (C3) holds by the capacity bound | proved | P (+K for C3) | Main:72, :82, :618 | supported |
| C-040 | 134 | (C2-structural) holds by reversibility in every bijective realization; (C2-slow) one mechanism | proved | P | Main:76, :82 | supported |
| C-041 | 134 | Necessity of (C2) in the coupling-step model: $M_k>0$ forces a realized hidden conditional at TV $\ge\varepsilon_{\min}$ from $\pi_H$ without mixing hypothesis; slow-bath form under it | proved (persistence form); conditional (slow-bath form: mixing hypothesis) | P (+ instance check `c2_mixing_probes.py`) | Main:469–476 | supported |
| C-042 | 136 | (C1)–(C3) without readback: fair coin with zero conditional memory on arbitrarily long horizons | proved | P + N (instance) | Main:178 | supported |
| C-043 | 138 | Proof status of Theorem 2 parts | — (status) | — | Main:99, :606 | supported |

### §2.5 Recurrence and indivisibility

| ID | Lines | Claim | Class | Layer / hypotheses | Source | Verdict |
|---|---|---|---|---|---|---|
| C-044 | 142–152 | Rooted family, shared independent prior, rows for probability-zero roots, card-game illustrations | — (definitions, worked examples) | A (hand-checkable) | Main:137, :141 | supported |
| C-045 | 148 | Stochastic divisor contracts TV; "only if" half of [RHP14, Thm 2.4]; [BD16, Prop. 1 and Cor. 1] | proved | P; L read first-hand: arXiv:1405.0303v2 Thm 2.4 (iff; text uses "only if"); arXiv:1408.7062v3 Prop. 1 (semiclassical), Cor. 1 (classical) | Main:121 | supported (after E12) |
| C-046 | 154 | Theorem 3 (rooted overlap and return) | proved | K: `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148; family current) | Main:143–145 | supported |
| C-047 | 160 | Corollary: non-permutation $\Gamma_s$, $0<s<L$ ⇒ not P-divisible on $\{0,\dots,L\}$ | proved | K (Theorem 3 + `isPermMatrix_of_stochastic_inverse`) + P (non-permutation → overlap; $\Gamma_L=I$); kernel-only bridge: C-158 | Main:137–139 | supported (machine-check wording: F-14) |
| C-048 | 160 | Histories with common endpoint, memory witnesses and non-deterministic visible steps supply a non-permutation $\Gamma_s$, also for Markov laws | proved | P | Main:137, :141 | supported |
| C-049 | 164–170 | Window/cycle discussion; accessible windows short compared with $L$; indivisibility does not separate laws at accessible orders | proved / definition | P | Main:141, :159 | supported |
| C-050 | 166 | Example $X_3=X_0$: $M_1=0$, $M_2=1$ bit; every deterministic completion keeps $X_0$ at time 2 | proved | A (hand-checkable; data processing) | Main:616 (states the same law at $t=1$) | supported |
| C-051 | 172 | Doukas states the contraction argument concurrently as a no-revival obstruction [Dou26, Prop. 1] | — (attribution) | L read first-hand: arXiv:2602.22095v3 §4.2.1, Prop. 1 (Chapman–Kolmogorov composability ⇒ no TV revival; ℓ1 contraction; no overlap or return) | — | supported (after E11) |
| C-052 | 172 | Square stochastic matrix: two rows share a column iff not a permutation; lemma [BB12, Problem 23] machine-checked | proved | K (`isPermMatrix_of_stochastic_inverse`) + P | Main:133–135, :139 | supported |
| C-053 | 172 | Monotone distance necessary, not sufficient, for P-divisibility | proved | P + N (`translation_probes.py`) | Main:121 | supported |

### §2.6 Examples

| ID | Lines | Claim | Class | Layer / hypotheses | Source | Verdict |
|---|---|---|---|---|---|---|
| C-054 | 178–183 | Six-hidden-state model: $\Gamma_1$, $\Gamma_2=I$, negative candidate divisor, $\Gamma_1^2$ entries, conditionals 1 and 1/3, $a/(2-a)$ | proved | A | Main:184–200 | supported; "minimal" removed (E3, F-02) |
| C-055 | 185 | XOR law: P-divisible on $\{0,1,2\}$ with $I(X_0;X_2\mid X_1)=1$ bit; = [RHP14, Eq. (15)] up to flipping; in [Dou26, App. A] | proved | A; L: Dou26 App. A read first-hand (arXiv:2602.22095v3, App. A: $x_2=x_0\oplus x_1$); RHP14 Eq. (15) not re-read this round | Main:141 | supported |
| C-056 | 185 | A finite reversible realization of the XOR law with independent hidden odds fails to chain somewhere in its cycle | conditional (shared independent prior; finite) | P | Main:141 | supported |
| C-057 | 196, 198 | Card table: $\Gamma_1=\tfrac12J$, $\Gamma_2=I$ P-indivisible; anticorrelated deal divisible; peek variants | proved | A | Main:720 | supported |
| C-058 | 200 | Bell ceiling for the card protocol under the stated locality, independence and every-run hypotheses | conditional (stated hypotheses) | P + L (Bell/CHSH) | Main:366; Book §1.11 | supported |

### §3 Quantum emergence

| ID | Lines | Claim | Class | Layer / hypotheses | Source | Verdict |
|---|---|---|---|---|---|---|
| C-059 | 204 | Correspondence alone does not give QM, for three reasons | proved | K (Theorem 1, `oi_alone_not_qm`) + P | Main:556; GR:220 | supported |
| C-060 | 210 | Revival of distinguishability within a window makes the family P-indivisible there | proved | P | Main:159 | supported |
| C-061 | 212 | No unconditional implication among the three notions is asserted; accessible memory does not force window P-indivisibility | proved | A (XOR) | Main:340 | supported |
| C-062 | 212 | Permutation unitary from a diagonal hidden state: P-indivisibility ⇒ CP-indivisibility | conditional (diagonal hidden state) | P | Main:328–332 (Main does not state $\mu_H$ diagonal: routed, #1028) | supported (Introduction states the hypothesis) |
| C-063 | 212 | Hadamard family CP-divisible with P-indivisible populations | proved | A (exact over $\mathbb Q(\sqrt2)$) | Main:336 | supported |
| C-064 | 216 | Card table embedded: one-step channel $\rho\mapsto\operatorname{tr}(\rho)I/2$ entanglement-breaking; two-step identity; CP-indivisible | proved | A + P (Main CP theorem) | Main:292, :332 | supported |
| C-065 | 216 | Memory classical in the sense of [BBS24] via the Pauli twirl; a fixed hidden card admits no such decomposition | proved | A (identity $\sum_o\sigma_oX\sigma_o=2\operatorname{tr}(X)I$ now stated) + P (fixed card: Main:720) | Main:720 | supported (after E9) |
| C-066 | 220 | [BLP09] one-directional witness; [BJA17] for bijective maps with $(d+1)$-dim ancilla; [Cal26] contrast | — (attribution) | L, not re-read this round | Main:338 (BJA17 = [9]) | supported for BJA17 via Main; others not re-read |
| C-067 | 224–232 | Operational setting and conditions (i)–(v) | — (definitions) | — | GR:216 | supported |
| C-068 | 238 | Each condition independent of the other four and of the observation process (qubit theories) | proved | K (`five_way_minimality`, RankGapTheory:702) | GR:220 | supported |
| C-069 | 240 | Sufficiency rests on Stinespring/Kraus/Ozawa | proved | K + L | GR:218 | supported |
| C-070 | 242–250 | Coherent lifts can differ by a time-dependent right action with different relating evolutions (exhibited pair); constant deformation cancels (general); trivial-ancilla lifts: rooted families equal iff one-step matrices equal | proved | K (`gl2_strong_gauge_moves_relative_candidate`, `gl3_constant_gauge_preserves_relative`, `rooted_eq_iff_slice_eq` both directions, `bridge_traj`, `realData_traj_stochastic`) | Main:22, :646 | supported (heading scoped, E7, F-06) |
| C-071 | 256 | A fixed realization with $N$ ontic configurations generates only behaviour matrices factoring nonnegatively through $N$ states | proved | P | Main:560 | supported |
| C-072 | 256 | Simulating a qubit needs unbounded classical memory; explicit tasks [GH03], [HKLP24, Thm 4]; Montina reports Hardy's result [Mon08; Har04] | proved (literature) | L read first-hand: arXiv:quant-ph/0110166v3 abstract; arXiv:2308.07727v4 Thm 4; arXiv:0711.4770v2 pp. 1–2. Har04 not read (cited as reported by Mon08) | Main:560 (imports [55]) | supported (after E13); the literature proves the unboundedness, OI does not |
| C-073 | 256 | No fixed finite realization reproduces a qubit's full prepare-and-measure theory | proved | P (factorization) + L (unboundedness) | Main:560 | supported |
| C-074 | 264 | Coupling-graph causal cone | proved | P | Main:362–366 | supported |
| C-075 | 264 | Bell ceiling under (i)–(iv) and every-run recording | conditional (i)–(iv), every-run | P + L | Main:366 | supported |
| C-076 | 268 | Completion reproducing quantum Bell correlations gives up (ii)/(iii) or (iv) | proved (from C-075) | P | Main:404–407, :772 | supported |
| C-077 | 268 | Framework retains measurement independence as a posit and adopts ontic parameter dependence with operational no-signalling | posit | — | Main:406–414 | supported |
| C-078 | 268 | Nearest-neighbour cubic update alone cannot supply that dependence outside the causal cone | proved | P | Main:416 | supported |
| C-079 | 268, 270, 324 | H-Bell: preparation-indexed graph supplies the dependence with no-signalling and the gravitational continuum limit — open | open (named hypothesis) | — | Substratum:131–133 (all three clauses); Main:416, :429 (response-dependence and no-signalling part only) | supported (after E8, F-07) |

### §4 Cosmological constant

| ID | Lines | Claim | Class | Layer / hypotheses | Source | Verdict |
|---|---|---|---|---|---|---|
| C-080 | 274, 276 | Vacuum-energy estimate exceeds observed value by ~120 orders [Wei89] | proved (literature) | L, not re-read | GR:364–366 | supported (standard) |
| C-081 | 276 | Mismatch equals de Sitter entropy up to a cutoff-convention factor, a dimensional identity | proved | A | GR:364–366 | supported |
| C-082 | 278 | A uniform shift of the emergent Hamiltonian changes no visible transition probability | proved | A | GR:356, :581 | supported |
| C-083 | 282–286 | Proposed resolution: if the field equations take the targeted form, the zero-point sum is not a source | conditional (field-equation form; G3) | — | GR:356, :637 | supported |
| C-084 | 288–294 | The two completions share substratum, partition and visible laws; deciding needs the G3 coupling theorem, open | open | — | GR:356, :637 | supported |
| C-085 | 296 | Related proposals [EvEMU11; KP14; Vol06] | — (attribution) | L, not re-read | — | not re-checked |

### §5 Black-hole information

| ID | Lines | Claim | Class | Layer / hypotheses | Source | Verdict |
|---|---|---|---|---|---|---|
| C-086 | 300 | Statement of the information problem [Haw76; Pag93; Pag13] | — (attribution) | L: [Pag93] entry now arXiv:hep-th/9306083v2, read first-hand (abstract and opening paragraph state the problem); Haw76, Pag13 not re-read | — | supported (after E14, F-13) |
| C-087 | 302–306 | Toy model, counts and floor | proved | E + P | C-304 row | supported |
| C-088 | 310 | Configuration-state ensemble with aligned bipartition: H-scramble has no instance; Theorems A.8–A.9 as stated do not establish a nonvacuous Page curve | proved | P | GR:839, :847–851 | supported |
| C-089 | 312 | Thm A.7 limits; proper energy shell; recovery needs coherent preparation — open | open | — | GR:811–819, :853 | supported |
| C-090 | 314 | Coherent-subspace entropy formula and mean bounds | proved | P + exact controls; independently accepted [CE] | page-coherent-recovery record (on #918 only) | supported (retention: F-15) |
| C-091 | 316 | Sequential-release construction; mirror Bell tent; definite clock required | proved | P + exact controls; no retained independent review | same record | see F-16 |

### §6 and back matter

| ID | Lines | Claim | Class | Layer / hypotheses | Source | Verdict |
|---|---|---|---|---|---|---|
| C-092 | 320 | Summary sentences | mirrors of C-003–C-012 | — | — | supported (C-238 caveat) |
| C-093 | 322 | Established results list and their layers | — (status) | — | rows above | supported except F-14, F-16 |
| C-094 | 324 | Fixed-basis statistics are, at every finite horizon, visible laws of an embedded observer, if OI holds | conditional (OI as physics; bijective representation choice) | — | Main:62, :556, :640 | supported (after E4, F-03) |
| C-095 | 328–332 | Open problems 1–5 | open | — | GR:216, :228; Main:556, :640, :720; Main:469 | supported (after E5, E6) |
| C-096 | 334 | Application open problems | open | — | GR:356, :853, :863; GR App. A.6 | supported |
| C-097 | 340 | Baseline declarations checked at `17b830bc` with Lean 4.33.0, Mathlib v4.33.0; each reports exactly the three standard axioms | proved (kernel record) | K; expected result in `papers/introduction_repro/` (#918 only) | `17b830bc` is an ancestor of `main` (GitHub compare); OIBridge sources of the cited modules equal at `f5c281ae` except a comment in `C3Necessity.lean` | not re-run (no build authorized); pin reachable |
| C-098 | 340 | Additional modules at checkpoints `4f962b6`, `3d54ae74`, `a958bc54`, `96a3020b` | proved (kernel) | K | each checkpoint is an ancestor of `main`; module blobs equal at `f5c281ae` | pins supported; publication status F-14 |
| C-099 | 342 | Probes released under MIT at the stated paths; source snapshot `55e3217b` | — (provenance) | — | `55e3217b` ancestor of `main` | supported |
| C-100 | 352–363 | Appendix A identifiers and line numbers | proved (kernel) | K | resolved at `17b830bc` and `f5c281ae` (see header) | supported (F-14 for the four kernel-only families; F-20) |

**Counts.** 111 rows: 100 in part B and 11 in part A. By class, as tallied from the Class
column: proved 75, conditional 9, posit 4, open 8, refuted 0; definitions, attributions, pins and
status statements 14; one summary row that mirrors others. A row that states both a proved form and
a conditional form (C-041) is counted once, as proved. No claim of the Introduction is refuted on
`main` at `f5c281ae` on the writer's reading.
