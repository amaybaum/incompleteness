# Final scientific review: "Observational Incompleteness: From Deterministic Dynamics to Quantum Observations"

- **Object:** `verification/audits/manuscript/introductory-paper-20261025/draft/Introduction-r11.md`, branch
  `draft/oi-introductory-paper-20261025` at `873121be`. Line numbers below refer to this file.
- **Corpus read at:** `17b830bc` (the paper's pin) and `c967d6a9` (current `main`, after #937). All corpus files were read
  from `git show` snapshots. Between the two commits `papers/Main.md`, `verification/lean-mathlib/`, `tools/` and
  `verification/programmes/black-hole-information/` are byte-identical. `papers/GR.md` (24+/26−) and 21 `book/` files
  changed.
- **Lean evidence:** `papers/introduction_repro/` on the branch. The `.lean` sources were read at `17b830bc`.
- **Scope:** the owner's standard of 2026-10-26. The review reports findings and does not rewrite. Weinberg 1989 (line 140)
  and the CT06, Har04 and Sha79 VERIFY markers are owner-recorded gates and are not counted as defects.

## Verdict: REVISE (minimal)

Two findings block. Each has a fix of one clause or one hash, and neither calls for new content:

- **B1.** Theorem 4 is stated without the structural hypotheses on the operational theory that the checked theorem assumes.
  Read literally, the "if" direction is false.
- **B2.** The corpus pin `17b830bc` predates #937. At that commit [GR] contradicts §4 on the value of Λ.

The other eight findings are non-blocking nits. Everything else checked holds:

- Theorem 1 and its directions.
- Theorem 2 and its stated limits.
- The Corollary's two directions.
- Theorem 3 and the stochastic-inverse lemma.
- §3.3.
- §5 against GR App. A.7 and BH-01/BH-02.
- §4 against `main`.
- All of Appendix B's arithmetic.
- The 28 Appendix A identifiers and line numbers.
- The axiom record.
- Register (§A.32/§A.33).

Once B1 and B2 are applied, the paper meets ACCEPT WITH NITS.

***

## Blocking findings

### B1 — Theorem 4 drops the operational theory's structural hypotheses (lines 114, 116, 118)

**Quote (114):**

> Fix a nonempty finite system and an operational theory specifying which finite outcome families of linear maps are
> available on the system and at every ancilla level [GR §3.3].

**Quote (116):**

> *…are exactly the normalized finite Kraus instruments if and only if conditions (i)–(v) hold.*

**Evidence.** The checked statement is `exactAll_iff_physical_general (T : FiniteOperationalTheory A)`
(GeneralCarrier:100). The structure `FiniteOperationalTheory` (OperationalAssembly.lean:594) is more than an
availability family. Its fields require:

- the identity to be available (`avail_id`);
- closure under classical coarse-graining (`avail_coarse`, `availExt_coarse`);
- feed-forward instrument composition (`availExt_bind`);
- an available uniformly mixed ancilla preparation (`prepAvail_uniform`, `prepAvail_post`);
- an available, spectator-independent native readout of the ancilla (`readout_avail`, `readout_local`);
- ancilla discard (`prepAvail_discard`).

GR §3.3 (line 216 at both commits) states part of this: "closed under coarse-graining and outcome-conditioned composition,
with a spectator-independent local readout of the ancilla". The paper omits it.

These fields carry the "if" direction. Take an availability specification that offers every channel (one-outcome family)
at every level and no instrument with more than one outcome:

- (i) holds: channels are valid.
- (ii) holds: system channels lift to level one.
- (iii) holds: the spectator extension of a channel is a channel.
- (iv) holds: every unitary channel is available.
- (v) holds: attach–act–discard yields a channel.

Two-outcome Kraus instruments are not available, so the conclusion fails. So "for an operational theory specifying which
families are available" with (i)–(v) does not imply exactness. The checked theorem avoids this because a readout and
composition are part of every `FiniteOperationalTheory`.

This is conditional → unconditional overreach (Code Review Rules), and "machine-checked" (line 118) is attached to it.

**Minimal fix.** In line 114, after "…at every ancilla level", insert GR's clause: ", closed under coarse-graining and
outcome-conditioned composition, with a uniformly prepared ancilla, ancilla discard and a spectator-independent local
readout of the ancilla". The shorter clause GR uses would also do.

### B2 — The corpus pin `17b830bc` predates #937, and at that pin [GR] contradicts §4 (lines 30, 196, 205, 261)

**Quote (261):** "**Corpus** (repository commit `17b830bc`, …)". [Main], [GR] and [Book] are resolved at that commit.

**Evidence.** At `17b830bc`, `papers/GR.md` still carries the statements that #937 (`c967d6a9`) corrected.

GR:366 at `17b830bc` says:

> This is not a prediction awaiting future data — the observed vacuum energy sits at the classical geometric scale
> $\rho\sim H^2/G$, the value the framework expects.

GR:547 at `17b830bc` lists:

> | Cosmological constant | $\rho_\Lambda\sim H^2/G$ | observed value | no discrepancy |

GR:24 and GR:32 at `17b830bc` say the CC problem "is dissolved" without qualification.

The paper says the opposite, consistently with `main`:

- line 147: "It does not explain the observed value of Λ, which enters as a cosmological input";
- line 179: "No prediction of the value of Λ";
- line 153: "the proposal reinterprets the problem and does not resolve it".

A reader who resolves [GR] at the pinned commit therefore finds the cited source asserting what the paper denies. The paper's
own statements all agree with `main` (see Check 4), so only the pin is stale.

**Minimal fix.** Change the corpus commit on line 261 to `c967d6a9` (or the landing `main`). The Lean pins on lines 30,
196 and 205 can stay at `17b830bc`: `verification/lean-mathlib`, `tools/` and `papers/Main.md` are byte-identical at
`c967d6a9` (`git diff --stat 17b830bc c967d6a9` over those paths is empty), so Appendix A's line numbers and the
`introduction_repro` record hold unchanged. If line 30 is also moved, add one sentence saying the Lean tree is identical.
Every section the paper cites in GR, Main, Book and BH exists with the same content at `c967d6a9`.

***

## Non-blocking findings

### N1 — The capacity bound's "machine-checked" lacks the caveat Theorem 2 carries (line 84)

**Quote:** "A realization of a law whose conditional past–future information reaches $I^*$ needs
$|\mathcal C_H|\ge2^{I^*}$ (machine-checked)."

**Evidence.** `card_hidden_ge_two_pow_Istar` (C3Necessity:117) is stated for `HiddenMemory.Realization`. That structure
is a bijection together with an arbitrary joint law on (history, present, hidden), and $I^*$ is a maximum over a finite
nonempty family of such slices sharing one hidden alphabet. Identifying a realization's time-$t$ law with that joint law is
the same unformalized step that line 80 states for Theorem 2.

**Minimal fix.** Change "(machine-checked)" to "(machine-checked for joint laws of history, present and hidden state,
with the same unformalized time-$t$ identification as Theorem 2)", or use the shorter "(machine-checked in the same form
as Theorem 2)".

### N2 — §3.4 attributes the imported unboundedness to sources other than the one [Main] uses (line 130)

**Quote:** "…explicit tasks are given by Galvão and Hardy [GH03] and Montina [Mon08], and Montina reports Hardy's
result that the number of ontic states cannot be finite [Mon08; Har04]. … the factorization is proved, and the
unboundedness is imported [Main §3.4, Proposition (…)]."

**Evidence.** Main:538 imports the unboundedness of nonnegative rank from Heinosaari–Kerppo–Leppäjärvi–Plávala
([Main ref. 55], PRA 109, 032627 (2024)), with Garner–Müller [56] as an alternative. It cites neither GH03, Mon08 nor
Har04. The paper's chain to "cannot be finite" runs through Har04, which is marked VERIFY as unread and is cited only as
reported in Mon08. The conclusion holds, but a reader who follows "[Main §3.4]" finds a different import.

**Minimal fix.** Add "[HKLP24]" (as cited in Main) to the "imported" clause, keeping GH03 and Mon08 as illustrations.
Alternatively, say "imported in [Main] from [HKLP24]".

### N3 — The black-hole computations are not in the DOI deposit the data statement names (lines 198–201; refs 269–271)

**Quote (198):** "The probes and the black-hole computations [BHa; BHb] are released under the MIT License (concept DOI
10.5281/zenodo.19060318), at these repository paths: … `verification/programmes/black-hole-information/`".

**Evidence.** `.gitattributes` at `17b830bc` and at `c967d6a9` contains `verification/programmes export-ignore`, with the
comment "Release archives (the GitHub zipball Zenodo deposits) omit the verification round records and audits". So the
BH-01/BH-02 directory is in the repository but not in the Zenodo archive under the concept DOI. `papers/oi_lattice_code/`
is not excluded. The directory is also absent from the paper's own branch at `873121be`; it is present at `17b830bc` and
`c967d6a9`.

**Minimal fix.** Say the black-hole computations are in the repository at the pinned commit and are not part of the
release archive, or drop the DOI from that clause.

### N4 — The abstract says "which of these", where the body says (iii)–(v) (line 12 vs 120, 174, 184)

**Quote (12):** "Open are which of these a physical substratum supplies".

**Evidence.** The body (120, 174, 184) and GR §3.3 restrict the open question to (iii)–(v), the substantive principles;
(i) and (ii) are well-formedness conditions.

**Minimal fix.** Write "which of the substantive conditions (iii)–(v) a physical substratum supplies", or "which of
these" → "which of the last three".

### N5 — Theorem 3's hypothesis does not fix the object $\Gamma_t$ depends on (line 92)

**Quote:** "*Let $\varphi$ be a bijection of a finite set.*"

**Evidence.** $\Gamma_s$ (line 90) is the rooted visible matrix of a partitioned system with a hidden prior. The checked
form (RecurrenceHorizon:148) takes a `RootedRealization`, which carries a bijection of $V\times H$ and one fixed hidden
prior shared by every root (CausalReadback.lean:178). The checked theorem does not use bijectivity, so the statement is
not too strong, but its object is under-specified.

**Minimal fix.** Write "Let $\varphi$ be a bijection of $\mathcal C_V\times\mathcal C_H$ with a fixed hidden prior".

### N6 — §6.2 item 4 overstates what kind of result all of §5 is (line 176)

**Quote:** "the results of §5 concern finite toy models, each proved on paper or checked exhaustively at small size or by
exact arithmetic."

**Evidence.** §5 also reports GR Theorems A.8–A.9 (line 163). These are conditional theorems on arbitrarily large
configuration spaces, resting on H-scramble and H-decouple; they are not finite toy computations. The sentence fits only
the [BHa; BHb] results.

**Minimal fix.** Write "the results of §5 reported from [BHa; BHb] concern finite toy models, …".

### N7 — "(C4) coincides with $M_t>0$, by the Corollary" cites the wrong witness (line 86)

**Evidence.** As line 86 defines it, (C4) says that two histories with the same present induce different next-step laws.
It coincides with $M_t>0$ by the vanishing criterion for conditional mutual information [CT06]. The Corollary supplies the
hidden mediation, not the equivalence. Under §A.34 each direction of a stated coincidence should cite its witness; here
both directions rest on [CT06], which is not machine-checked.

**Minimal fix.** Write "…coincides with $M_t>0$ by the vanishing criterion [CT06], and the Corollary places it in the
hidden state".

### N8 — A source comment carries an internal identifier (line 254)

**Quote:** `<!-- Source of the decomposition below: ERRATUM-r4 (design record), by the Pauli-twirl identity; not a corpus
derivation. -->`

**Evidence.** Pandoc drops the comment from the PDF, but the `.md` is the published manuscript source and §A.27 asks for
manuscript voice with no internal filenames. The decomposition it introduces is correct (checked below) and is a two-line
verification stated in full.

**Minimal fix.** Delete the comment at landing. The owner-sanctioned VERIFY gates are unaffected.

***

## The seven checks

### 1. Claim vs evidence: 27 citations spot-checked

Each citation below was read at `17b830bc`. All support the paper's statement except where a finding is named.

| Paper line | Cited source | Verdict |
| --- | --- | --- |
| 20 | Main §1.2, Remark (status of the early commitments) (Main:62): bijection a representation choice, total finiteness a posit, near-unitarity the motivation | ✓ |
| 38 | Main §1.2, Remark (the measure as a realization datum) (Main:60) | ✓ |
| 48–54 | Main §3.4, Theorem (finite-horizon equivalence) (Main:526) and `finite_horizon_equivalence` | ✓ |
| 56 | Main §3.4, Theorem (finite-horizon process dilation) (Main:496): rational law, prior independent of $x_0$ | ✓ |
| 60 | Main §3.1: $n^2$ suffices at one step (Main:210) | ✓ |
| 64 | Main §3.4, Remark (diagnostics) (Main:596) | ✓ |
| 68 | Main §3.4, Remark (consolidation) (Main:618): $L$-periodic law, no all-time realization of a nonperiodic law | ✓ |
| 74–80 | Main §3.4, Theorem (unavoidable hidden predictive memory) (Main:582), plus the HiddenMemory sources | ✓ |
| 82 | Main §1.5 (Main:97): both directions, `S_imp_D`, vanishing criterion not formalized | ✓ |
| 84 | Main §2.3, Lemma (accessible backflow from readback) | ✓; constant re-derived (Check 6); see N1 |
| 86 | Main §1.3: (C1) and (C3) follow from (C4), (C2) a physical-regime premise | ✓; see N7 |
| 94 | Main §2.3: monotonicity necessary, not sufficient | ✓ |
| 96 | Main §2.3, Lemma (stochastic inverse) and Theorem (history readback + finite recurrence) (Main:133–137) | ✓ |
| 106 | Main §3.2, Theorem (CP-indivisibility) (Main:326) | ✓; the proof uses only diagonal preservation, so the paper's "diagonal hidden state" generalization of Main's uniform $\rho_H$ is valid |
| 106 | Main §3.2, Remark (Hadamard) (Main:330) and Remark (three notions) (Main:334) | ✓ |
| 108 | Main §3.4, Remark (representation, not explanation) (Main:616) | ✓ |
| 114–120 | GR §3.3 (GR:216–220): conditions (i)–(v), the theorem, `five_way_minimality`, `oi_alone_not_qm` | ✓ except B1 |
| 124 | Main §3.4, Remark (scope: representability…) (Main:624) | ✓ |
| 130 | Main §3.4, Proposition (Main:538) | ✓ conclusion; see N2 |
| 136 | Main §3.3 Bell ceiling and H-Bell (Main:22, 380, 394) | ✓ |
| 22, 184 | Main §4.5: no memory-witness test established (Main:702) | ✓ |
| 143–145 | GR §6.2 (GR:356): offset invisible to quantum data, coupling open at G3, the $\rho_C g_{\mu\nu}$ pair | ✓ |
| 161 | BHa REPORT and result.json: 1376/40320; $P_{\rm succ}\ge1/|K|$; 32 non-injective violators; sufficient, not necessary | ✓ |
| 163 | BHa item F: "timescale ordering does not supply it" | ✓ |
| 163 | GR App. A.7 and Thms A.8–A.9 (GR:807–870): H-scramble fails on definite configurations, H-decouple, proper shells, single trajectory, GSL open (A.6), QES agreement not established | ✓ |
| 163 | BHb C1 and C6(a)–(d) | ✓ |
| 163 | Book §7.6 (islands conjectural) and §18.5 (Page curve conditional) | ✓ |
| 184 | GR §2.2 (GR:52): (C4) a named realization condition, not discharged at the cosmological cut | ✓ |
| 222–229 | Main §2.4 minimal model | ✓ |
| 252 | Main §3.2, Remark (failure of (C1)) (Main:286): constant channel, entanglement-breaking | ✓ |
| 237–246 | Book §1.11 card table | ✓ |

No witness → theorem, finite → universal, or necessary → sufficient overreach was found, apart from B1. Existential
statements are worded existentially:

- line 124: "can differ" (`gl2` is an explicit witness);
- line 120: "for each condition there is a qubit theory";
- line 161: counts given as counts.

### 2. Equivalences (§A.34)

| Line | Equivalence | Witnesses |
| --- | --- | --- |
| 50–54 | $\mathsf S_K=\mathsf D_K=\mathsf Q_K$ | Three one-way theorems are named (`S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S`), and the reverse inclusions are the compositions inside `finite_horizon_equivalence` (Equivalence:466–468). ✓ |
| 82 | Corollary, "exactly when" | Each direction's witness is stated: Thm 2(a) in every realization, and Thm 2(a) in one realization from `S_imp_D`. Both use the unformalized vanishing criterion, as stated. ✓ |
| 116–118 | Theorem 4, iff | ⇒ is `physical_of_exactAll`; ⇐ is `exactAll_of_physical_general`. ✓ as directions; hypotheses per B1 |
| 126 | Visible-equality quotient | slice ⇒ trajectory law is `bridge_traj`; rooted ⇒ slice is the forward direction of `rooted_eq_iff_slice_eq`. ✓ |
| 86 | "(C4) coincides with $M_t>0$" | See N7 |
| 106 | BJA17 CP-divisibility ⇔ ancilla distinguishability | Attributed to an external theorem with its scope ("bijective dynamical maps"). ✓ |

### 3. "Machine-checked"

Every use was located and matched to Appendix A:

| Line | Use | Appendix A declaration |
| --- | --- | --- |
| 12 | abstract | the two results, each with one unchecked step |
| 30 | convention | — |
| 54 | Theorem 1 | Theorem 1 entry |
| 80 | Theorem 2, scope stated | Theorem 2 entry |
| 82 | non-machine steps named | — |
| 84 | capacity bound | capacity entry (N1) |
| 94 | Theorem 3 | Theorem 3 entry |
| 96 | lemma and routed readback | lemma and readback entries |
| 118 | Theorem 4 | Theorem 4 entry |
| 124 | gl2 and gl3 | relating-evolution entry |
| 186 | open item | — |
| 196 | recipe | — |
| 203–216 | Appendix A | — |

No use refers to the physical theory or its interpretation.

**Appendix A identifiers.** All 28 identifiers exist at the stated module:line at `17b830bc`; each line was printed and
matched. `papers/introduction_repro/results-121598983127.json` contains all 28 under `expected`, and its README records
each with exactly `[propext, Classical.choice, Quot.sound]`.

**Lean statements read against the paper's description:**

- `finite_horizon_equivalence`: the classes `Stochastic`, `RevRealizable` and `QfbRealizable` match §2.1. $\mathsf D$
  allows a correlated initial law; $\mathsf Q$ has a diagonal initial law, measures at every step with collapse, and reads
  out through `read : Bas → V`.
- `unavoidable_hidden_predictive_memory`, `pushforward_identity`, `distinguishability_floor` and `capacity_floor`: (a)–(c)
  exactly as displayed, stated for a joint law, as line 80 says.
- `card_hidden_ge_two_pow_Istar`: $2^{I^*}\le|H|$ with $I^*$ a maximum over finitely many slices sharing $H$ (N1).
- `isPermMatrix_of_stochastic_inverse`: the one-sided inverse case, `A*B=1 ∨ B*A=1`.
- `pIndivisible_of_rooted_identity_return_of_overlap`: overlap of distinct rows at $s$, `rootedMap R n = 1`, $s<n$, gives
  `¬PDivisible n`. `PDivisible` matches line 90's definition. Reversibility is unused (N5).
- `routed_forces_indivisible_somewhere`: from `RoutedReadback K R`, there is $n$ with `PIndivisibleWithin n`. It goes
  through `horizon_verdict` and does not use the stochastic-inverse lemma, as "by the route of Theorem 3" says.
- `gl2_strong_gauge_moves_relative_candidate` (existential, explicit $2\times2$ data) and
  `gl3_constant_gauge_preserves_relative` (constant $K$ cancels from $U_tKK^\dagger U_s^\dagger$). Both match line 124.
  `CoherentLift` has no composition clause; the source notes that the cocycle is vacuous for relative candidates, so the
  paper's "compose exactly across times" adds no hypothesis.
- `bridge_traj`, `rooted_eq_iff_slice_eq` and `realData_traj_stochastic`: they match line 126, with trivial ancilla,
  uniform initial law and identity readout.
- `exactAll_iff_physical_general`, `five_way_minimality` and `oi_alone_not_qm`: they match lines 116–120, except for the
  structural hypotheses (B1).

### 4. Applications, against `main` `c967d6a9` after #937

**Cosmological constant (§4, lines 141–153).** These statements agree with `main` GR:

- the descriptive distinction is stated, with no "established" overclaim;
- the coupling is open at G3, and the proposal is conditional on it;
- the target equation is stated conditionally;
- the remaining vacuum term is not computed;
- Λ is an input, and $H^2/G$ is the Friedmann normalization (`main` GR:338);
- "the de Sitter entropy up to a numerical factor … a dimensional identity, not an independent prediction" (`main`
  GR:366);
- electroweak and QCD transitions need the same open step (`main` GR:583).

Comparison with trace-free gravity and sequestering is clean.

**Horizon entropy and ħ.** The paper states neither the $1/4$ coefficient nor the ħ calibration. Horizon entropy appears
only as the dimensional identity on line 149, which is within the owner's "at most as consistency".

**Black holes (§5).** §5 is consistent with GR App. A.7 at both commits (unchanged by #937), with BH-01 and BH-02, and with
Book §7.6 and §18.5 at `main`. Both applications are stated as non-resolutions (lines 12, 26, 153, 163, 192).

No paper statement disagrees with `main`. The pinned corpus does disagree with the paper (B2).

### 5. Internal consistency

Abstract, body and conclusion agree on:

- the scope of Theorem 1;
- memory as the discriminating content;
- the completion conditions not implied by OI;
- relating-evolution nonselection;
- both applications as non-resolutions.

Status words are used consistently: "machine-checked" and "proved on paper" follow line 30's conventions; "conditional",
"open", "not established" and "not derived" are used as in the corpus. The only mismatch found is N4. The
"(each with one step not machine-checked)" of line 12 is accurate for both results: the time-$t$ identification, and the
passage from history-level (C4) to a non-permutation rooted map.

### 6. Mathematics stated in the paper

All checked and correct:

- **Line 84, the Pinsker constant.** Conditioning on the endpoint, Pinsker gives $D\ge(2/\ln2)\mathrm{TV}^2$ bits. With
  $\mathrm{TV}^2+\mathrm{TV}'^2\ge\delta^2/2$ and weights at least $p_0$, this gives $I\ge p_0\delta^2/\ln2$.
- **Line 66.** The 0/1 permutation entries make $|U|^p$ independent of $p$.
- **Line 68.** $\varphi^L=\mathrm{id}$ makes every sample path, and so the law, $L$-periodic.
- **Line 90.** A stochastic divisor contracts total variation.
- **Lines 145–147, sign conventions.** $T^{\rm vac}=-\rho_Cg$; the $\rho_C g_{\mu\nu}$ pair matches GR:356.
- **Line 149.** $\rho_{\rm QFT}/\rho_\Lambda\sim M_{\rm Pl}^2/H^2\sim S_{\rm dS}$.
- **Line 161.** $1/|M|\ge1/|\mathcal U|\Rightarrow|\mathcal U|\ge|M|$.
- **B.1.**
  - $\Gamma_1=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix}$, $\Gamma_2=I$, $\Gamma_1^{-1}=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$.
  - $\Gamma_1^2$ has diagonal $5/9$ and off-diagonal $4/9$.
  - $P(x_2{=}0\mid x_1{=}1,x_0{=}0)=1$.
  - $P(x_2{=}0\mid x_1{=}1)=(a/3)/(a/3+2(1-a)/3)=a/(2-a)$, which is $1/3$ at $a=1/2$.
- **B.2.** All two-time matrices are $\tfrac12J$; $\Lambda=I$ works; $I(X_0;X_2\mid X_1)=1$ bit.
- **B.3, table.** The probabilities are $1/2, 1, 1/2, 1/2$.
- **B.3, divisibility.**
  - With equal rows, no $\Lambda$ gives $\Gamma_1\Lambda=I$.
  - The reveal-only or replace-hole-card peek gives probability 1.
  - Anticorrelated cards make $\Gamma_1$ the swap, which is divisible.
- **B.3, channels.**
  - The one-step channel is $\operatorname{tr}(\rho)I/2$ and the two-step channel is the identity, so the family is
    CP-indivisible.
  - With a fixed burn card the maps are $|0\rangle\langle0|$ and the identity, and there is no classical-memory
    decomposition.
  - $\sum_o\sigma_oX\sigma_o=2\operatorname{tr}(X)I$, so $\tfrac14\sum_o\sigma_o\rho\sigma_o=\operatorname{tr}(\rho)I/2$.
  - Conditioning on $o$ with $\sigma_o\cdot\sigma_o$ returns $\tfrac14\rho$ per branch, which sums to $\rho$.

### 7. Register (§A.32/§A.33)

The prose was scanned for the following, with no hits:

- reader instruction;
- revision-history phrases ("now", "no longer", "formerly", "corrected", "in its current form");
- self-assessment adjectives;
- capitals for emphasis.

Capitals appear only in acronyms and in source comments. "The paper claims no new theorem or physical result; its
contribution is expository" (line 28) and "No claim that the viewpoint is new" (line 180) are scope statements, not
self-assessment of the framework. The only register note is N8.

***

## Fixes, in one list

| # | Severity | Line | Fix |
| --- | --- | --- | --- |
| B1 | blocking | 114 | Add GR's structural clause (coarse-graining, outcome-conditioned composition, uniform ancilla and discard, spectator-independent local readout) |
| B2 | blocking | 261 | Repin the corpus to `c967d6a9` or the landing `main`; the Lean pins may stay, since the tree is identical |
| N1 | nit | 84 | Qualify "(machine-checked)" as in Theorem 2 |
| N2 | nit | 130 | Cite HKLP [Main ref. 55] for the imported unboundedness |
| N3 | nit | 198 | Say the BH computations are not in the Zenodo release archive (`export-ignore`) |
| N4 | nit | 12 | "which of these" → "(iii)–(v)" |
| N5 | nit | 92 | "a bijection of $\mathcal C_V\times\mathcal C_H$ with a fixed hidden prior" |
| N6 | nit | 176 | Restrict "finite toy models" to the [BHa; BHb] results |
| N7 | nit | 86 | Cite the vanishing criterion [CT06] for (C4) ⇔ $M_t>0$ |
| N8 | nit | 254 | Delete the internal source comment at landing |
