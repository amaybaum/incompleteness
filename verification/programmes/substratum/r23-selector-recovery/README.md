# R23: recovery of substrate reconstruction / observable gauge uniqueness

**State:** exploratory scientific research; NOT a frozen, accepted or publication-ready result.
**Owner direction:** prioritize root-cause recovery of material downgrades before advancing stronger manuscript/Introduction claims.
**Track:** #983, under the existing broader downgrade register #970; correction ledger #946. The source-correction preview is stacked PR #982, with SC-44 #980 and SC-45 #981 separate.
**No merge, no new physical premise, no status upgrade.**

## The significant downgrade

The original Substratum Theorem 23 claimed that observations (E1–E7) and assumptions (A1–A6) uniquely determine the local propagating substratum modulo a *complete* four-family gauge group. The currently defensible result fixes specific **structural outputs within a selected cubic-lattice branch**, conditional on additional premises.

This is **material**, not editorial: it removes an explanatory uniqueness claim. Even if the numerical SM retrodictions of the selected model were unchanged, their derivation from the bare OI observer and structural hypotheses is not established. Source corrections must remain, regardless of future research outcome.

## Two logically independent proof gaps

**R23-A: selection of the physical branch.** E4 and A3–A5 by themselves do not select the nearest-neighbor second-order rule. The branch also uses H-link, m=1, the octahedral representation, amplitude-scale gauge and further physical hypotheses. The old Stage-2 assertion that each step (a)–(f) is iff is unproved. The correct target must quantify over all admissible candidate systems and prove uniqueness of a stated *operational invariant*, not define all alternatives away.

**R23-B: inverse/gauge classification.** The previous Lemma 24.1 is refuted: same channel family for every time does not imply conjugacy of the generating reversible map (Lean `ST3_pairC`, `ST4_pairC`). Equal *block-word traces* plus block spanning imply hidden unitary conjugacy on the same carrier (Lean `WT3_spanning_iff` and the one-sided strengthening), but the OI observable set may not provide those word traces; full block spanning and the precise allowed finite-state relabellings are unestablished. The original Theorem 24(i) arbitrary fixed-interface relabelling is false by exact four-state counterexample (SC-45). All-partitions equivalence differs from a fixed readout.

**Neither gap is repaired by assuming its conclusion.**

## First exploratory result: a bounded-rule selection obstruction

`exploratory/finite_radius_witness.py` defines two reversible second-order rules over $\mathbb F_7$ on a 7-by-7-by-7 periodic cubic lattice:
$$
(x_{t+1})_n = \sum_{r\in R} a_r \sum_{i=1}^3[(x_t)_{n+r e_i}+(x_t)_{n-r e_i}] - (x_{t-1})_n .
$$
Rule A: $R=\{1\},\ a_1=1/3$. Rule B: $R=\{1,2\},\ a_1=a_2=1/6$, arithmetic modulo 7. Both are finite, deterministic, invertible by solving for $x_{t-1}$, linear, center-free in the *current* field, translation invariant and invariant under the 48 signed permutations of the axes. Both have constant-mode coefficient 2. Their single-step impulse support is 6 versus 12 cells, so they are not the same fixed-site update and differ in microscopic coupling range.

**Evidence:** exact local Python reasoning/replay, not Lean certification. A test of one impulse under all 48 signed axis symmetries and a translation, with inverse control, is illustrative; the algebraic inversion formula and symmetry of the shell sums supply the general mathematical reason. Distinct neighbor support disproves selection of the nearest-neighbor operator from **those local premises alone**. It does *not* show both models satisfy all E1–E7, have the same physical dispersion/speed, Bell correlations, coherent instruments, SM matter or GR coupling. Those demands remain to be imposed as independent, preregistered falsifiers in any general-model-uniqueness claim.

For a stronger recovery theorem, search for a **noncircular selector** stated before seeing the model, e.g. a physically justified locality radius, operational instrument response, dispersion relation including higher orders, no extra hidden branches or coupling-spectrum restriction. Prove its consequences across the specified class and run controls with the selector removed. No selector is adopted here.

## Recovery obligations

| ID | Question | Result required for restoration | Current status |
|---|---|---|---|
| R23-A1 | Does A3 bounded degree, A4 center independence, A5 linearity plus relevant isotropy fix the nearest-neighbor rule? | Global uniqueness theorem or an explicit independently justified missing hypothesis | **Open.** Two reversible cubic-symmetric rules differ under the tested subset |
| R23-A2 | What fixes H-link (m=1), representation and amplitude-scale physical premise? | Necessary conditions from independent observational/physical structure, not retrodictive choices | **Open** |
| R23-A3 | Do the exact E1–E7 conditions rule out alternatives that agree at accessible scales? | Precise physically testable observational model, completeness/identifiability theorem or countermodel | **Open** |
| R23-B1 | Which OI observables (fixed partition / all partitions; transitions / coherent channels / multi-time process) are preserved? | Execute frozen 24.1B under its older type-P lifecycle; no inference replacing a missing quotation | **Frozen, unexecuted at last check** |
| R23-B2 | What hypotheses make `BlockSpanning` equivalent to `HiddenCommutantTrivial`? | Execute frozen 24.1C under its Lean sealing lifecycle; do not consume 24.1B conclusions | **Frozen, unexecuted at last check** |
| R23-B3 | Does equality of actual observable data give block-word traces, and does hidden unitary imply an allowed physical relabelling? | New separately frozen proof, with Pair C and fixed-interface four-state controls | **Open** |
| R23-C | Can one assemble the observed local branch with Bell and gravitating cosmological matter without importing output laws? | Physical coupling map, no-signaling/Bell and gravity checks on *one* mechanism | **Open** |

## The larger material-downgrade dependency matrix

This list is a *priority classification*, not an assertion that every item has been solved. Each row must link to exact source and separate evidence before any upgrade. The umbrella #970 retains the complete historical inventory.

| Priority | Scientific loss | Main root requirement | Tracking |
|---|---|---|---|
| **P0** | Substratum reconstruction uniqueness and full four-family gauge completeness | R23-A/B/C as above; restored only by proof or explicit physical selector | #983, #980–#982 |
| **P0** | Exact QM physical emergence / Bell and coherent instrument equivalence | Derive noncircular emission/readout/instrument map and H-Bell composite/curvature compatibility | #970 track 6; #885 / Main operational bridge |
| **P0** | Gravity CC dissolution and dark-sector interpretation | Derive G3 **matter-to-boundary coupling** and physical stress-energy response; do not confuse with gauge level G3 | SC-37; #970 track 5 |
| **P1** | Page curve counted prediction G11 | Nonvacuous scrambling/decoupling mechanism with correct initial ensemble and cut, plus independent computation/proof | SC-36; owner removed G11 from counted Class C |
| **P1** | SM Theorem 3, staggered/center-independence/Higgs route | Exact microscopic/observer map, separate theorem for physical Higgs interpretation | #970 track 1; #965/#966 |
| **P1** | Hidden predictive-memory and C3 necessity K3→K2 | Kernel bridge from realized time-t joint law and correct supremum/max interpretation | #970 track 2 |
| **P1** | Locality/continuity/recurrence claims | Correct topologies, interval hypotheses and countermodels; quantify where the stronger versions survive | #970 track 3 |
| **P1** | OI-specific cycle statistics, ergodicity and Gaussianization | Prove actual dynamics' recurrent components and applicable measure/typicality, not random-permutation analogy | #970 track 4 |
| **P1** | Horizon gravity operator algebra and de Sitter response | Construct operator/representation and physical de Sitter cancellation from dynamics, or record obstruction | #970 track 5 |
| **P2** | Remaining corpus downgrades and proof-tier corrections | Map each changed claim to governed research, counterexample, or explicit rationale for no upgrade | #970 track 7; #946 |

**Recovery principle.** No paper status can be upgraded from `open`, `conditional`, `GAP`, `K2` to a stronger one merely because a proof obligation has been renamed or moved into hypotheses. Distinguish theorem strength, assumption selectivity, phenomenological matching and physically independently justified input.

## Workflow and gates

1. Keep this as an active **research-only** draft, separate from manuscript-correction PRs and immutable frozen research rounds.
2. Freeze the next exact proposition and positive/negative controls under the repository's native-round protocol before any result-designated computation. This file is **not that freeze**.
3. The user already authorized 24.1B and 24.1C execution, but each must be launched under its own preserved merge-base and protocol, not from this branch.
4. Independent reviewer tests exact math, counterexamples, assumptions and interpretation, with Lean axioms and CI at the designated exact head. The old `WT3` and `ST3` results are retained unchanged.
5. Publish repaired source and propagated references only when proof standards are met, with separate exact-SHA merge approval. Until then the conservative theorem wording in #982 remains the publication-safe status.

**No merges or PR authorizations implied.**

## Conditional selector lemma (mathematical, not physical) — exploratory

A *positive* result identifies exactly one possible extra premise that could recover a restricted wave-rule uniqueness theorem. **It does not show that OI supplies that premise.**

Let $p:\mathbb Z^3\setminus\{0\}\to[0,1]$ be finitely supported, normalized ($\sum_d p_d=1$) and invariant under signed permutations of coordinates (cubic symmetry). Define a real second-order spatial-wave dispersion by
$$
\cos\omega(k)=\sum_d p_d\cos(k\cdot d).
$$
At small $k$, the symmetry cancels all off-diagonal second moments and makes
$$
\omega(k)^2=\frac{\mathbb E_p|d|^2}{3}|k|^2+O(|k|^4).
$$
Since each nonzero integer displacement has $|d|^2\ge1$, the infrared speed coefficient obeys
$$
c_{\rm lat}^2=\frac{\mathbb E_p|d|^2}{3}\ge\frac13.
$$
If **equality** $c_{\rm lat}^2=1/3$ is additionally required, the nonnegative sum of terms $p_d(|d|^2-1)$ is zero, so every active displacement has $|d|^2=1$, i.e. it is one of the six nearest axial neighbors. Cubic symmetry and normalization then force **exactly** $p_{\pm e_i}=1/6$. Conversely, those six weights give equality. This proves the **unique positive nearest-neighbor effective spatial kernel** within the stated class.

No Lean formalization or independent review has been performed. `exploratory/positive_kernel_selector.py` exhausts a denominator-6 grid of four cubic-orbit mixtures using rational arithmetic, and tests that dropping either **no self-loop** or **nonnegativity** permits a non-nearest kernel with the same second moment.

**Critical physical limitations.** The physical OI substratum uses finite-field/mod-$q$ reversible update rules; there is no intrinsic nonnegative order on the modular coefficients. A real nonnegative *observer-level spatial kernel* would need an independent construction from that substratum. Likewise, the dimensionless equality $c_{\rm lat}^2=1/3$ is **not derived from A1–A6**, and choosing it to recover the desired cubic wave equation would be circular as a fundamental explanation. Physical lattice spacing, time-step normalization and a mechanism relating observed light cones to this dispersion must be derived or independently measured. Without those bridges the lemma is a useful conditional rigidity result, **not a restoration of Theorem 23's uniqueness**.

**Next falsifiable target:** derive (or find a counterexample to) the proposition that OI's finite reversible observer dynamics induces a *nonnegative, normalized, center-free spatial transfer kernel* with a fixed dimensionless infrared speed on the actual accessible degrees of freedom. Test that premise against signed-coupling, self-loop, alternative-shell and observational-gauge controls, and do not assume the value (1/3) merely to obtain the desired conclusion.

