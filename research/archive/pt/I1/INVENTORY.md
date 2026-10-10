# I1 INVENTORY — foundations (stage 6, Q-EX-FULL, step 1; L = `9f9f8257…`)

Thread I1 records; the inventory records and decides nothing. Schema as `PROTOCOL-STAGE6.md` §Step 1.
Paths are relative to `pt/base/`; kernel modules are `verification/lean-mathlib/OIBridge/<M>.lean`
written `<M>.lean:<line>`. Exact statements: quoted inline; where a docstring or sentence is long the
record quotes its operative clause and the full exact text is in `statements.out` under the key
`[S:<name>]` (kernel) or `[S:<file>:<line>]` (manuscript), produced by `statements.py` from the
corpus byte for byte. An ellipsis `…` marks an abridgement inside a quotation.

**Field conventions.**
- `status` uses the protocol's set. Where the record that fixes the status is a manuscript proof
  with no kernel anchor, the status reads `proved [manuscript, not K]` — the manuscript's own
  claim, recorded as such, never read as [K]. Kernel theorems are `proved [K]` (each is in a
  module carrying `#print axioms` lines; no `axiom`/`opaque` occurs in any I1 module: census (a)).
- `level`: H hidden deterministic history / substratum; O single-system operational (K programme);
  P pair cone; M matrix-level operational theory (`FiniteOperationalTheory`); G general carrier;
  X manuscript physical layer.
- `bridge`: for every I1 record the field to level P is **`none at L`** unless stated otherwise;
  the mechanical evidence is `bridge_check.out` (no module at L imports both an I1 module and
  `CompositeDimension`/`K2Guard`: VERDICT NO-MODULE; same for the K∞ modules) and
  `bridge_check2.out` (no module imports both `OperationalAssembly` — the M-level carrier — and a
  pair-cone module: VERDICT NO-MODULE). Where a record carries an H→M transfer, it is named.
- `bearing` ∈ {direct constraint on `K` or (b_min); constrains the single-token structure the pair
  inherits; constrains the composite only through <bridge>; none at L}.
- `flag`: `do not assume` only for the protocol's list; `—` otherwise.

***

## A. The observation base (manuscript; level H)

**I1.1 — Axiom 1 (tokened differentiation).** kind axiom · level H · status assumed (the
manuscript's evidential floor, stated "indubitable": Main.md:38, Methodology.md:245) · flag —
- statement: Main.md:38 "**Axiom 1** is the evidential floor: tokened differentiation occurs —
  concrete differentiated content is *registered*, a this-not-that tokened from a locus against a
  remainder; equivalently, *embedded representation occurs*." Methodology.md:245 "> **Axiom 1.**
  *Tokened differentiation occurs.* — Concrete differentiated content is instantiated: there is
  some this-not-that. Indubitable; conceptually primitive."
- provenance: papers/Main.md:38 (§1.2); papers/Methodology.md:245 (§6.1), :226 (§5.4);
  book/ch01-observation.md:22 ("Call this the first axiom."). Kernel: no general predicate; an
  instance image only, the conjunct `(∃ p q : Core, vis p ≠ vis q)` of `SealedCoreIsFiniteOI`
  (OIRealization.lean:300; docstring :287–288 "registered differentiation — the visible readout
  distinguishes states (Axiom 1)") — see I1.42.
- depends_on: — · yields: I1.3; the lemmas I1.6–I1.10 (Main.md:38 "From Axiom 1, by analysis of
  the words "occurs" and "registered," the relational structure, the existence of a dynamics,
  determinism and finiteness per moment follow as lemmas").
- bridge: none at L · bearing: none at L.

**I1.2 — Axiom 2 (recurrence of differentiation).** kind axiom · level H · status assumed
(substantive posit; ROADMAP "declared input, not currently targeted," ROADMAP.md:1455–1461 lists
"recurrence") · flag —
- statement: Main.md:38 "This is **Axiom 2**: differentiation recurs, the temporal domain being
  the minimal such recurrence. Axiom 2 presupposes Axiom 1 … but is not derivable from it".
  Methodology.md:247 "> **Axiom 2.** *Differentiation recurs.* — The principle of Axiom 1 is
  instantiated more than once over, across a further axis. The temporal domain is the minimal such
  recurrence; configurational and temporal instances are the two minimum witnesses, the actual
  count of axes being settled downstream by derivation."
- provenance: Main.md:38; Methodology.md:247 (§6.1), §5.4 (Methodology.md:227); ch01:22 ("Call
  this the second axiom."); ROADMAP.md:1456. Kernel: instance image only, conjunct
  `(∀ p : Core, swapFn (swapFn p) = p)` of `SealedCoreIsFiniteOI` (OIRealization.lean:299;
  docstring :287 "recurrence — every state returns (Axiom 2, here with period two)").
- depends_on: I1.1 (presupposition, Main.md:38) · yields: I1.3; recurrence steps downstream (I2).
- bridge: none at L · bearing: none at L.

**I1.3 — The two-axiom observation base and the non-derivability of Axiom 2 (no-go).** kind
manuscript-principle · level H · status proved [manuscript, not K] (written countermodel) · flag —
- statement: Methodology.md:235 "*Given Axiom 1, "tokened differentiation occurs," the rungs
  relationality, proper-part, dynamics-existence, determinism, finiteness-per-moment, and
  bijectivity follow as lemmas; the recurrence of differentiation — Axiom 2, equivalently the
  existence of more than one moment for the dynamics to act across — does not, and cannot,
  follow.*" Main.md:38 "a structure containing a single tokened differentiation and nothing
  further satisfies Axiom 1 while containing no recurrence, so no analysis of Axiom 1 alone can
  yield Axiom 2 — non-derivability by countermodel."
- provenance: Methodology.md:235 (§5.5), :249–251 (§6.1); Main.md:38.
- depends_on: I1.1, I1.2 · yields: the foundational count used by I1.18.
- bridge: none at L · bearing: none at L.

**I1.4 — The perspectival reading: embeddedness `V ⊊ S` belongs to the primitive.** kind
manuscript-principle · level H · status assumed (an adopted reading; the manuscript calls the
choice "presentational", Main.md:40) · flag —
- statement: Main.md:38 "The proper-part decomposition $V \subsetneq S$ — the observer embedded in
  a whole it does not exhaust — is accordingly constitutive of the primitive rather than a
  downstream posit". Main.md:40 "One could instead read the evidential floor *thinly* … in which
  case the embeddedness $V \subsetneq S$ does not follow and would have to be added as a third,
  independent axiom."
- provenance: Main.md:38, :40; ch01:24 ("on a thinner reading it would be a third posit").
- depends_on: I1.1 · yields: I1.6 (the observer `V ⊊ S`), I1.9.
- bridge: none at L · bearing: none at L.

**I1.5 — The C1–C4 selection condition (domain commitment).** kind hypothesis · level H · status
assumed (a "structural commitment about the framework's domain", Main.md:36) · flag —
- statement: Main.md:36 "that our universe lies in the observer-admitting subset of substrata —
  substrata whose bijection structure satisfies the conditions C1–C4 below for some partition.
  This is the C1–C4 selection condition, not a consequence of the first axiom: a momentary
  registering with no persistent record satisfies the first axiom and fails C2."
- provenance: Main.md:36; Methodology.md:251 ("The hidden-sector conditions C1–C4 are selection
  conditions, not lemmas"), Methodology.md:162 (§4.6).
- depends_on: I1.20–I1.24 · yields: scope of every Main theorem on C1–C4 partitions (Main.md:62).
- bridge: none at L · bearing: none at L.

**I1.6 — Definition of an observation `(S, φ, V)`.** kind definition-as-hypothesis · level H ·
status assumed (the framework's setting) · flag —
- statement: Main.md:44 "**Definition.** An *observation* is a triple $(S, \varphi, V)$: a total
  system $S$, a dynamics $\varphi: S \to S$, and an observer $V \subsetneq S$ — a proper subsystem
  with finitely many distinguishable internal states, coupled to the complement $H = S \setminus V$
  through $\varphi$." Variant, book/ch01-observation.md:26: "… a total system $S$, a deterministic
  dynamics $\varphi: S \to S$, and an observer …" (the book adds "deterministic").
- provenance: Main.md:44, :46; ch01:26; FULL.md mirror. Kernel: instance image `SealedCoreIsFiniteOI`
  (I1.42), whose docstring maps each conjunct to "the manuscript's definition" and Lemmas 1–3.
- depends_on: I1.1, I1.4 · yields: I1.7–I1.15, I1.20–I1.24.
- bridge: none at L · bearing: none at L.

**I1.7 — Dynamics from the composition (semigroup) law.** kind manuscript-principle · level H ·
status proved [manuscript, not K] (cited [45]) · flag —
- statement: Main.md:46 "it follows from a single innocuous premise, that evolution *composes* —
  advancing the state by $t$ and then by $s$ equals advancing it by $t+s$. … in the discrete case
  relevant here it collapses to iteration of a single transition map, $x_t = \varphi^t(x_0)$."
- provenance: Main.md:46; ch01:28. · depends_on: I1.6 · yields: I1.10.
- bridge: none at L · bearing: none at L.

**I1.8 — Lemma 1 (finiteness; finite visible resolution).** kind lemma (manuscript) · level H ·
status proved [manuscript, not K] per Main.md:62 ("only finite visible resolution is a theorem
(Lemma 1)"); its physical support empirically motivated (holographic bound, Main.md:48) · flag —
- statement: Main.md:48 "**Lemma 1** (Finiteness). *The observer has finitely many distinguishable
  internal states, so the visible configuration space $\mathcal{C}_V$ is finite, with a discreteness
  scale $\epsilon$ providing a finite minimal cell volume.*"
- provenance: Main.md:48, :62; Methodology.md §4.5 (rung 7: "Rung 7, in the form Lemma 1 needs,
  is a lemma"); ch01:30. Kernel image: `Fintype.card Core = 8`, conjuncts of
  `SealedCoreIsFiniteOI` (OIRealization.lean:292–294) and `A1Realized` (I1.55).
- depends_on: I1.1, I1.6 · yields: recurrence arguments (I2), I1.23.
- bridge: none at L · bearing: none at L.

**I1.9 — Lemma 2 (causal partition; product decomposition).** kind lemma (manuscript) · level H ·
status assumed (definitional: "not a modeling choice but the definition of embedded observation";
"The product decomposition is idealized", Main.md:50–54) · flag —
- statement: Main.md:50 "**Lemma 2** (Causal partition). *The observer is a proper subsystem:
  $V \subsetneq S$. The complement $H = S \setminus V$ is the hidden sector.*" Main.md:52
  "$$\Gamma = \Gamma_V \times \Gamma_H, \qquad H_{\text{tot}} = H_V + H_H + H_{\text{int}}$$";
  Main.md:54 "follows, with cross-partition correlations entering only through $H_{\text{int}}$.
  The product decomposition is idealized; §4.5 addresses approximation quality."
- provenance: Main.md:50–54; ch01:34. Kernel image: `partIdx` and conjunct
  `(∀ p, (partIdx p).1 = vis p)` (OIRealization.lean:274, :295).
- depends_on: I1.4, I1.6 · yields: I1.15, I1.20 (`H_int ≠ 0`).
- bridge: none at L · bearing: none at L.

**I1.10 — Lemma 3: determinism and reversibility (the bijective representative).** kind lemma
(manuscript) · level H · status empirically motivated / assumed: Main.md:62 "The bijective
substratum is a representation choice — the minimal recurrent bijective representative of the
hidden dynamics; … observed near-unitarity is the empirical input motivating the choice";
ROADMAP.md:1457 lists "the empirical unitarity input used in the determinism-recovery margin" as a
declared input · flag —
- statement: Main.md:56 "**Lemma 3** (Determinism, reversibility, and the selected measure).
  *$\varphi$ is a function with a unique successor for every state (determinism) and, as the
  reversible representative of §1.2, a bijection: distinct states have distinct successors and
  predecessors (injectivity — reversibility)." Variant, ch01:38: "*$\varphi$ is a bijection on
  $S$." Variant, Methodology.md:251: "Everything else in the foundational layer is a lemma: …
  determinism, finiteness-per-moment, and bijectivity", narrowed in Methodology §4.5: "rung 6 is a
  lemma at the visible level, structural-plus-A1 at the substratum level."
- provenance: Main.md:56, :62 (two-pronged argument), :38 ("the bijective (reversible)
  representative is a reconstruction choice motivated by observed near-unitarity"); ch01:38;
  Methodology.md §4.4–§4.5, :251; Substratum.md:94 (A2, I1.64). Kernel images: conjuncts
  `(∀ p q, swapFn p = swapFn q → p = q)` and `(∀ p, sigmaPerm.symm (sigmaPerm p) = p)`
  (OIRealization.lean:296–297); `A2Realized` (I1.55); `Substratum.A2` (I1.57).
- depends_on: I1.1, I1.7, I1.8, I1.11 (finiteness of the total space) · yields: I1.15; every
  realization theorem (D = finite reversible realizations, I2).
- bridge: none at L · bearing: none at L.
- note (status variance, recorded not adjudicated): Methodology.md:251 lists bijectivity among
  lemmas; Main.md:38/:62 call the bijective representative a reconstruction/representation
  choice ("the package is not a set of independent assumptions, and it is not all theorems").

**I1.11 — Total finiteness of the substratum (physical posit).** kind hypothesis · level H ·
status assumed (Main.md:38 "total finiteness of the substratum is a physical posit (status
Remark, §1.4; ledger §4.5)"; ROADMAP.md:1456–1457 declared input "the minimal finite
representative/total-state finiteness choice where consumed") · flag —
- statement: Main.md:62 "total finiteness of that representative is a physical posit, carried in
  the posit ledger (§4.5)".
- provenance: Main.md:38, :62; Methodology §4.5 (the hidden factor's finiteness "is the structural
  assumption A1 of the substratum construction"); Substratum.md:92 (A1, I1.63).
- depends_on: — · yields: I1.10 (bijectivity on the total space), recurrence (I2).
- bridge: none at L · bearing: none at L.

**I1.12 — Lemma 3: the selected measure (maximal-entropy counting measure).** kind hypothesis ·
level H · status assumed ("a selection principle, not uniqueness from invariance alone",
Main.md:56; ROADMAP.md:1458 declared input "maximal-entropy invariant-measure selection") · flag —
- statement: Main.md:56 "On each accessible orbit the invariant measure is unique (uniform on the
  cycle); globally, the counting measure is selected among invariant measures as the
  maximal-entropy one — a selection principle, not uniqueness from invariance alone.*"
- provenance: Main.md:56, :62; ch01:38. Kernel image: conjunct
  `(∀ (g : Gen) (c : ℂ), visWeightStep (.act g) (fun _ => c) = fun _ => c)` (OIRealization.lean:298).
- depends_on: I1.10 · yields: I1.15 (canonical `T = T(φ, 𝒫, μ_inv)`).
- bridge: none at L · bearing: none at L.

**I1.13 — The measure as a realization datum (hidden prior `μ_H`).** kind manuscript-principle ·
level H · status assumed (definitional remark) · flag —
- statement: Main.md:60 "a realization in the sense of §3.4 carries its own fixed hidden prior
  $\mu_H$ as part of the realization datum, and the emergent law is a function of $(\varphi,
  \text{partition}, \mu_H)$".
- provenance: Main.md:60; ROADMAP.md:69 (the observed law "is a function of the triple `(φ, Obs,
  μ)`", I1.76). · depends_on: I1.9, I1.12 · yields: I1.15, I1.76.
- bridge: none at L · bearing: none at L.

**I1.14 — Reversibility as the conservative (fallback) assumption.** kind manuscript-principle ·
level H · status assumed (offered as a postulate alternative to the recovery) · flag —
- statement: Main.md:66 "a reader unwilling to grant that recovery may simply take reversibility
  as the standard postulate it is elsewhere, with no cost to the emergence results."
- provenance: Main.md:66; ch01:38 (same remark). · depends_on: — · yields: I1.10.
- bridge: none at L · bearing: none at L.

**I1.15 — Partition-relativity lemma.** kind lemma (manuscript) · level H · status proved
[manuscript, not K] · flag —
- statement: Main.md:86 "**Lemma (partition-relativity under the canonical invariant measure).**
  *Under the canonical measure of Lemma 3, the emergent description is uniquely determined by the
  partition; … canonically $T = T(\varphi, \mathcal{P}, \mu_{\text{inv}})$, in general
  $T = T(\varphi, \mathcal{P}, \mu_H)$ (§1.3 Remark).*"
- provenance: Main.md:86–92; ch01:79. · depends_on: I1.9, I1.10, I1.12, I1.13 · yields: the
  stochastic law on `C_V` used by every condition (I1.20–I1.24).
- bridge: none at L · bearing: none at L.

**I1.16 — The four layers; a Layer-1 result establishes no Layer-4 claim.** kind
manuscript-principle · level H→X (a level-separation statement) · status assumed (framing) · flag —
- statement: Main.md:99 "**Layer 4 — physical and operational realization** (§3.2, §4,
  companions): interventions (classical comb closed, §3.4; quantum instruments open), coherent
  preparation, Bell and free-choice structure, H-spin' and H-χ', the cosmological realization —
  where the named hypotheses live. A Layer-1 result does not by itself establish any Layer-4 claim."
- provenance: Main.md:97–99. · depends_on: — · yields: I1.17.
- bridge: **the manuscript states the absence**: no Layer-1 (hidden-history) result transfers to
  Layer 4 (composites, instruments) by itself · bearing: none at L (records a non-transfer).

**I1.17 — The layered theorem statement: readback content, and the full operational extension's
additional hypotheses.** kind manuscript-principle · level H→M/X · status: layers (1)–(3) proved
[manuscript; kernel side I2]; layer (4) explicitly conditional on "additional operational-lifting
and composition hypotheses" (open in the manuscript's own terms) · flag —
- statement: Main.md:82 "**(2) Readback content:** C4 is not needed for the existence of a quantum
  representation; it is what makes the OI sector nontrivial. … **(4) Full operational
  extension:** identifying one common *standard local quantum instrument/composite theory* for all
  coherent interventions requires the additional operational-lifting and composition hypotheses
  stated in §3.4." Abstract, Main.md:22: "Two logically separate completion questions remain
  beyond that finite-law result: whether the complete family of coherent interventions and
  composites is represented simultaneously by the standard quantum instrument theory (§3.4) …"
- provenance: Main.md:82, :22; the §3.4 hypotheses themselves (operational-extension boundary,
  Main.md:542) are thread I2's.
- depends_on: I1.20–I1.24 · yields: —
- bridge: **the manuscript states that a transfer from the finite-law layer to composites needs
  additional hypotheses**; none at L supplies them for the pair cone · bearing: constrains the
  composite only through <bridge>: none at L.

**I1.18 — Methodology's rung analysis of the conditions (C1–C4 are selection conditions).** kind
manuscript-principle · level H · status assumed (C2, C3 "substantive conditions"; C1 "follows
conditionally") · flag —
- statement: Methodology.md:162 "C1, non-zero coupling, follows conditionally: a distinction with
  content *about* the complement requires coupling to the complement, on pain of that content
  being unregisterable. C2 (record persistence — slow-bath separation one route) and C3
  (sufficient capacity) are not lemmas — they are substantive conditions satisfied by some
  partitions and not others." … "Rung 8 is correctly treated by the framework as a selection
  condition, not a derivation".
- provenance: Methodology.md:160–162 (§4.6), :251 (§6.1). · depends_on: I1.1 · yields: I1.5.
- bridge: none at L · bearing: none at L.

## B. The hidden-sector conditions C1–C4 (manuscript forms; level H)

**I1.19 — The conditions are diagnostics, not hypotheses.** kind manuscript-principle · level H ·
status assumed (the manuscript's framing of C1–C4's role) · flag —
- statement: Main.md:72 "The four conditions below are diagnostics of a realization rather than
  hypotheses of the characterization: the equivalence of §3.4 quantifies over none of them
  (Remark, *the conditions are diagnostics, not hypotheses*), (C1) and (C3) follow from (C4) in any
  faithful realization, and (C2) is a physical-regime premise." Main.md:594 "(C4) is not an
  independent condition on the realization either: it asserts a readback gap *mediated through
  the hidden state*, and in a faithful realization every correlation is so mediated, so the
  mediation clause is automatic and (C4) coincides with clause (ii) itself."
- provenance: Main.md:72, :594; Methodology.md:162. · depends_on: I1.20–I1.24 · yields: I1.25.
- bridge: none at L · bearing: none at L.

**I1.20 — (C1) Non-zero coupling.** kind condition · level H · status: condition (diagnostic);
necessity proved [manuscript, not K] ("Status: doubly anchored. Necessity — observed
non-Markovian dynamics force C1", Main.md:74); "C1 is *not independent of C4*" (Main.md:74); on
the sealed core proved [K] (`core_hidden_drives_visible`, IndependenceCensus.lean:137) · flag —
- statement: Main.md:74 "**(C1) Non-zero coupling.** $H_{\text{int}} \neq 0$: hidden degrees of
  freedom affect the visible evolution at some accessible step — the conditional law of some
  visible transition depends on the hidden state."
- variants: ch01:53 "**Condition C1 (Non-zero coupling).** $H_{\text{int}} \neq 0$: hidden degrees
  of freedom affect the visible evolution at some accessible step …"; Explainer.md:65 "**C1:
  Non-zero coupling (H_int ≠ 0).** The visible and hidden sectors interact."; Substratum.md:126
  "C1 (non-trivial coupling)". Kernel: no general C1 predicate at L (census (a): none in the I1
  modules; grep of `def …Coupl…` finds none); instance conjunct 1 of `CoreC1C4`
  (IndependenceCensus.lean:188) — I1.39.
- depends_on: I1.9 · yields: I1.17 (2), I1.29, I1.35; the P-indivisibility theorems (I2).
- bridge: none at L · bearing: none at L.

**I1.21 — (C2-structural) Memory persistence.** kind condition · level H · status "a
physical-regime premise, not a structural condition" (Main.md:76) · flag —
- statement: Main.md:76 "**(C2-structural):** a hidden record of visible history, once written,
  persists to the readback that uses it — the retention that clause (b) of the universal
  hidden-memory theorem shows every memory-bearing completion must contain (§3.4)."
- provenance: Main.md:76 (also: "Unqualified "(C2)" in this paper means the persistence
  requirement"); Methodology.md:162; Substratum.md:126 ("C2 (record persistence — the slow bath
  one realization)"). Kernel: instance conjunct 2 of `CoreC1C4`, `∀ p, vis (swapFn (swapFn p)) =
  vis p` (IndependenceCensus.lean:189; `core_visible_period_two` :143, "C2, structurally").
- depends_on: I1.9 · yields: I1.24 (persistence half of readback, Main.md:76).
- bridge: none at L · bearing: none at L.

**I1.22 — (C2-slow) Slow-bath timescale separation.** kind condition · level H/X · status
assumed (physical-regime mechanism; one sufficient mechanism for I1.21; ETH "a well-supported
conjecture rather than a theorem", Main.md:76) · flag —
- statement: Main.md:76 "**(C2-slow):** the timescale mechanism — the hidden sector's
  *coarse-grained mixing time* $\tau_B$, the timescale on which the effective channel degrades a
  stored record of visible history, is long compared to the accessible window: $\tau_S \ll \tau_B$,
  the *inverse* of the Markovian regime. (C2-slow) implies (C2-structural) under the
  uniform-erosion estimate of §2.3 … but not conversely".
- variants (definition of "C2" itself): ch01:55 "**Condition C2 (Slow-bath timescale
  separation).** $\tau_S \ll \tau_B$."; Explainer.md:67 "**C2: Memory persistence (τ_S ≪ τ_B).**".
  The book chapter and the Explainer state C2 in its slow form; Main defines unqualified C2 as
  persistence (I1.21). Recorded, not adjudicated.
- depends_on: — · yields: I1.21 (one-way), I1.30, I1.31. · bridge: none at L · bearing: none at L.

**I1.23 — (C3) Sufficient memory capacity.** kind condition · level H · status: necessity proved
[K] (`C3.c3_necessity`, `card_hidden_ge_two_pow_Istar`, C3Necessity.lean — I1.32); "like C1, C3
follows from C4 within any faithful realization" (Main.md:78) · flag —
- statement: Main.md:78 "**(C3) Sufficient memory capacity.** The hidden sector has enough
  distinguishable states to encode the observed conditional past–future information:
  $\log_2 |\mathcal{C}_H| \geq I^*$, the per-process bound of §3.4."
- variants: ch01:57; Explainer.md:69 "**C3: Sufficient capacity (log₂|C_H| ≥ I\*).**";
  Substratum.md:126. Kernel instance: conjunct 3 of `CoreC1C4` (IndependenceCensus.lean:190–194;
  `core_capacity_saturates` :157, "saturates the capacity bound rather than merely exceeding it").
- depends_on: I1.8 · yields: I1.32 · bridge: none at L · bearing: none at L.

**I1.24 — (C4) History readback.** kind condition · level H · status: condition (the "logically
independent" structural condition, Main.md:602); necessity "immediate given observed
non-Markovianity" (Main.md:80); no general kernel predicate at L for the history-level condition
(CausalReadback.lean:11–12; PhysicalC4Discharge.lean:147–149, :493–494 "No history-level predicate is
defined for it."); physical discharge open (ROADMAP.md:66, I1.74) · flag —
- statement: Main.md:80 "**(C4) History readback.** History-sensitive hidden mediation: on
  accessible windows, hidden degrees of freedom carry information about the visible past into
  future visible conditionals — at some order, two visible histories with the same current state
  induce different next-step laws, mediated through the hidden state. The condition is
  operational; it does not by itself assert a causal write-then-read cycle — a pre-sampled hidden
  variable revealed by the history satisfies it (the response-table construction, §3.4)."
- variants: ch01:59 "**Condition C4 (History readback).** History-sensitive hidden mediation:
  hidden degrees of freedom carry information about the visible past into later visible steps —
  an operational condition, satisfiable even by a pre-sampled hidden variable revealed by the
  history." Kernel: instance conjunct 4 of `CoreC1C4` (IndependenceCensus.lean:195–197;
  `core_history_readback` :176); candidate forms `C4e`, `C4r` (I1.70); realization clause
  `RoutedReadback` (I1.71), `RoutedReadbackAtStorage` (I1.72).
- depends_on: I1.21 (persistence), I1.20 · yields: I1.17 (2), I1.27, I1.29; hidden-memory
  theorems (I2) · bridge: none at L · bearing: none at L.

**I1.25 — Which condition is primitive: only C4 is logically independent.** kind
manuscript-principle · level H · status proved [manuscript, not K] (dependencies "certified by
exhaustive enumeration in `primitive_probes.py`") · flag —
- statement: Main.md:602 "*Remark (which condition is primitive).* Of the three structural
  conditions, only (C4) is logically independent. (C1) follows from it — a readback gap requires
  hidden mediation, and zero-coupling realizations exhibit no gap at any order — and (C3) follows
  by data processing … The equivalence could therefore be stated with (C4) alone."
- provenance: Main.md:602, :74, :78, :72. · depends_on: I1.20, I1.23, I1.24 · yields: I1.19.
- bridge: none at L · bearing: none at L.

**I1.26 — Book variant: the four conditions "logically independent".** kind manuscript-principle
· level H · status: as stated in the book; it differs from I1.25 (recorded, not adjudicated) ·
flag —
- statement: book/ch01-observation.md:71 "The framework's four conditions are therefore
  *logically* independent — each can fail without forcing the others to fail — even though they
  are *physically* correlated for the cosmological partition." ch01:61 "The conditions are
  independent in statement but coupled in content."
- provenance: ch01:61, :71 (and FULL.md mirror); contrast Main.md:602, :74 ("C1 is *not
  independent of C4*"). · depends_on: I1.20–I1.24 · yields: —.
- bridge: none at L · bearing: none at L.

**I1.27 — History readback with finite recurrence forces indivisibility somewhere in the cycle
(and nothing below the return horizon).** kind theorem · level H · status proved [K] at the rooted
interface with the routed form as hypothesis (`routed_forces_return_indivisibility`,
PhysicalC4Discharge.lean:109; `routed_forces_indivisible_somewhere` :122); manuscript form proved
[manuscript] (Main.md:137) · flag —
- statement: Main.md:137 "**Theorem (history readback + finite recurrence implies
  indivisibility).** *For a fixed finite reversible OI representative, genuine C4 history readback
  implies that the rooted visible stochastic process is indivisible somewhere in its full
  recurrence cycle.*" Scope, Main.md:141: "It does **not** say that C4 forces P-indivisibility on
  every accessible short-time window". Kernel (:122): `theorem routed_forces_indivisible_somewhere
  {K : ℕ} {R : RootedRealization V H} (h : RoutedReadback K R) : ∃ n, PIndivisibleWithin n
  (rootedMap R)`; docstring: "This is `[Main]` §2.3's theorem at the rooted interface with the
  routed form as hypothesis".
- depends_on: I1.71 (`RoutedReadback`), recurrence (`rootedMap_periodic`, I2's RecurrenceHorizon)
  · yields: the "unlocks" bound of ROADMAP.md:66 (I1.74).
- bridge: none at L · bearing: none at L.

**I1.28 — Lemma (fast bath erases readback).** kind lemma (manuscript) · level H · status proved
[manuscript, not K] · flag —
- statement: Main.md:159 "**Lemma (fast bath erases readback).** *Suppose the coarse-grained
  channel mixes fast relative to the visible step, $\tau_B \ll \tau_S$, and erodes the stored record
  uniformly, by $e^{-\tau_S/\tau_B}$ per step, across the history pairs at issue. Then for any
  $k \geq 2$ the order-$k$ readback gap obeys*" (bound displayed at Main.md:160–161).
- provenance: Main.md:159–165. · depends_on: I1.22 (negated) · yields: I1.22's role.
- bridge: none at L · bearing: none at L.

**I1.29 — Lemma (accessible backflow from readback).** kind lemma (manuscript) · level H ·
status proved [manuscript, not K] · flag —
- statement: Main.md:167 "**Lemma (accessible backflow from readback).** *Under (C1)–(C3), suppose
  (C4) holds with a gap at order $k$ in the accessible window: two visible histories $p \neq p'$ of
  length $k$ with a common endpoint, each of probability at least $p_0$, induce next-step laws at
  total-variation distance at least $\delta$. Then*" (bound at Main.md:168).
- provenance: Main.md:167–172 (Remark: "(C1)–(C3) admit realizations with zero backflow").
- depends_on: I1.20, I1.21, I1.23, I1.24 · yields: the characterization's (iii)⇒(ii) (I2).
- bridge: none at L · bearing: none at L.

**I1.30 — Theorem (C2 necessity, quantitative mixing form).** kind theorem (manuscript) · level H
· status conditional-on the mixing hypothesis (Main.md:433; "the necessity direction rests on the
mixing hypothesis", Main.md:478) · flag —
- statement: Main.md:433 "**Theorem (C2 necessity, quantitative mixing form).** *Model one coupling
  step as the uniform-prior bijection marginal of §3.2's construction, and between coupling events
  let the hidden sector evolve by any map on the hidden conditional. Suppose the mixing hypothesis
  holds: … every realized post-relaxation hidden conditional, given the visible record to date,
  lies within $\varepsilon$ of $\pi_H$ in total variation. Then the $k$-step visible marginal
  satisfies*" (bound at Main.md:434–437).
- provenance: Main.md:433–445, :478–482; Substratum.md:128 ("C2 is conditional on the
  quantitative mixing hypothesis"). · depends_on: mixing hypothesis (assumed; ETH its motivation,
  Main.md:480; ROADMAP.md:1458 declared input "hidden-sector/effective mixing hypotheses") ·
  yields: I1.22's necessity · bridge: none at L · bearing: none at L.

**I1.31 — Theorem (physical memory: C2, process form) and C2's two roles.** kind theorem
(manuscript) · level H · status conditional-on the conditional-mixing hypothesis · flag —
- statement: Main.md:447 "**Theorem (physical memory: C2, process form).** *Under the
  conditional-mixing hypothesis — every realized hidden conditional lies within $\varepsilon$ of
  $\pi_H$ in total variation at the coupling time — every history-conditional next-step law
  satisfies … uniformly in the history". Main.md:456 "The characterization's realization clause
  needs (C2) only in its limit form — the canonical dilation's bath is static, $\tau_B = \infty$ —
  so the structural equivalence is carried by (C1), (C3), (C4), with (C2) automatic in that limit.
  … (C1)–(C4) are not four necessities of equal standing — (C2)'s necessity is the conditional
  bound above."
- provenance: Main.md:447–456. · depends_on: mixing hypothesis · yields: I1.21/I1.22 status.
- bridge: none at L · bearing: none at L.

**I1.32 — Theorem (C3 necessity) and the per-process capacity corollary.** kind theorem · level
H · status proved [K] (C3Necessity.lean: `c3_necessity` :80, `c3_necessity_via_hidden`,
`Istar_le_log_card`, `card_hidden_ge_two_pow_Istar` :117, `c3_necessity_and_capacity`); the
sustained-backflow reading is NOT proved and is denied without its extra hypothesis (C3Necessity.lean
header; Main.md:492) · flag —
- statement (kernel, C3Necessity.lean:75–82): "**Theorem (C3 necessity), [Main] §3.3.**
  `I(X_<t ; X_>t | X_t) ≤ log₂ m`, at every horizon." `theorem c3_necessity [Nonempty H]
  (R : Realization Hist V H) (L : ℕ) : cmiBits R.w (varHist) (varNow) (varFuture R L) ≤
  Real.logb 2 (Fintype.card H)`. Corollary (:112–118): "**Corollary (per-process capacity bound),
  [Main] §3.3.** `m ≥ 2^{I*}`." Manuscript: Main.md:484–486, :492 ("P-indivisibility alone does not
  force $m \geq n$").
- depends_on: `HiddenMemory.Realization`, `capacity_floor_of_fun` (I2's HiddenMemory.lean) ·
  yields: I1.23's necessity · bridge: none at L · bearing: none at L.

**I1.33 — Existential and universal readings of the conditions.** kind manuscript-principle ·
level H · status proved [manuscript, not K] (per-condition necessity), the two readings
"logically independent" · flag —
- statement: Main.md:612 "The equivalence is existential: (ii) holds iff *some* per-horizon
  (C1)–(C4) realization exists. The necessity analysis is universal and per-condition: any
  deterministic realization of a non-Markovian process has hidden influence at some step (C1),
  memory capacity $m \geq 2^{I^*}$ (C3), and read-back differing past-conditionals (C4); C2's
  necessity holds within the conditional-mixing class." Main.md:614 "The equivalence is a
  representation theorem: every accessible non-Markovian law *admits* a per-horizon C1–C4
  realization. It does not, by itself, explain why the physical universe exhibits such a law".
- provenance: Main.md:612–614. · depends_on: I1.20–I1.24 · yields: —.
- bridge: none at L · bearing: none at L.

**I1.34 — (C1) does not fix the composite: entanglement-breaking is a property of `id ⊗ Φ`.**
kind manuscript-principle (remark with an enumeration) · level H→M (single-system vs `id ⊗ Φ`) ·
status proved [manuscript, not K] (exhaustive enumeration in `papers/oi_lattice_code/coherence/`) ·
flag —
- statement: Main.md:286 "*Remark (failure of (C1)).* Condition (C1) does not suffice. For
  $|V| = |H| = 2$ and $\varphi(x,h) = (h,x)$ one has $T_{ij} = 1/2$ for all $i,j$, yet
  $\Phi(\rho) = I/2$ identically: a constant channel, hence measure-and-prepare. … The obstruction
  is structural: (C1) constrains the diagonal of $\Phi$, whereas entanglement-breaking is a
  property of $\mathrm{id} \otimes \Phi$ and is not fixed by the action on single-system inputs."
- provenance: Main.md:286. · depends_on: I1.20 · yields: —.
- bridge: **the manuscript states the absence**: a single-system condition does not fix the
  `id ⊗ Φ` behaviour · bearing: none at L (records a single-system → composite non-transfer).

**I1.35 — Substratum Stage 1: C1–C4 from E1–E3, A1–A2 and M1-T (conditional structure).** kind
theorem (manuscript, Stage 1 of Theorem 23) · level H/X · status conditional-on M1-T (C1, C3, C4)
and on the mixing hypothesis (C2) (Substratum.md:128) · flag —
- statement: Substratum.md:128 "**Conditional structure.** C1, C3, and C4 for the memory-bearing
  temporal sector are derived from E1–E3, A1–A2 together with **M1-T** — C4 via the hidden-memory
  theorem applied to the stipulated accessible temporal memory/P-indivisibility; conditional on
  M1-T, they hold without further hypothesis. **M1-B** is separate … C2 is conditional on the
  quantitative mixing hypothesis of [Main §3.4]". Output, Substratum.md:124–126: "There exists a
  triple $(S, \varphi, V)$ with $S$ finite, $\varphi$ a bijection on $S$, and $V \subset S$ a
  distinguished subset such that: … The triple satisfies C1 …, C2 …, C3 …, and C4 (history
  readback) for the M1-T temporal sector".
- provenance: Substratum.md:120–136. · depends_on: E1–E3 (I2: physical layer), I1.63, I1.64,
  I1.36 · yields: Theorem 23's later stages (I2).
- bridge: none at L · bearing: none at L.

**I1.36 — Hypothesis M1-T (the observed temporal data lie in the readback sector).** kind
hypothesis · level H/X · status assumed ("a modeling premise about the temporal data, not an
inference from Bell violation", Substratum.md:108) · flag —
- statement: Substratum.md:122 "**M1-T**, the observed temporal quantum data used in Stage 1 lie in
  the accessible history-readback/P-indivisible sector of [Main §2.3–§3.4]; and **M1-B**,
  Bell-violating composites take [Main §3.3]'s measurement-independent, ontically
  parameter-dependent branch with operational no-signaling. M1-T and M1-B are logically distinct".
- provenance: Substratum.md:108, :122, :128. M1-B (Bell composites): out of scope, thread I2.
- depends_on: — · yields: I1.35 · bridge: none at L · bearing: none at L.

**I1.37 — Explainer: the conditions as access conditions on a lossless memory.** kind
manuscript-principle · level H · status assumed (expository restatement) · flag —
- statement: Explainer.md:905 "The framework's results all have a clean interpretation in this
  language. The conditions C1–C4 are access conditions on the memory: C1 means the readable …"
  (full line in `statements.out` [S:Explainer.md:905]); Explainer.md:65–69 state C1, C2 (slow form,
  I1.22), C3.
- provenance: Explainer.md:63–69, :905, :933. · depends_on: I1.20–I1.24 · yields: —.
- bridge: none at L · bearing: none at L.

## C. The sealed OI core and its realization (kernel)

**I1.38 — The shared swap-memory core (carrier, readout, passive step, control).** kind
definition-as-hypothesis (the carrier every core statement is about) · level H · status
definition [K] · flag —
- statement: IndependenceCensus.lean:94 `abbrev Core := VH × Bool`; :96–97 "The observer reads `(v,b)`;
  the middle bit `h` is hidden." `def vis (p : Core) : Bool × Bool := (p.1.1, p.2)`; :99–100 "The
  passive step `σ(v,h,b) = (h,v,b)`." `def swapFn : Core → Core := fun p => ((p.1.2, p.1.1), p.2)`;
  :102–103 "The control `τ(v,h,b) = (v,h,b⊕1)`." `def flipFn : Core → Core := fun p => (p.1, !p.2)`;
  `sigmaPerm`, `tauPerm` (:113, :116); `sigma_tau_commute` [K] (:132).
- provenance: IndependenceCensus.lean:88–133; embedding `coreIdx` (OIRealization.lean:90: "**THE
  EMBEDDING** `((v,h),b) ↦ (h, pack (v,b))`: the hidden bit on the system qubit, the visible pair
  on the ancilla."; module header :15–18). · depends_on: — · yields: I1.39–I1.46.
- bridge: none at L · bearing: none at L.

**I1.39 — `CoreC1C4`: the four conditions on the shared core.** kind hypothesis-structure (`def …
: Prop`) · level H · status proved [K] for the core (`core_isC1C4`, IndependenceCensus.lean:200) ·
flag —
- statement: IndependenceCensus.lean:181–186 "**THE FOUR OI CONDITIONS ON THE SHARED CORE**, as one
  predicate, in canonical order: C1 (non-trivial coupling — the hidden state drives the visible
  future), C2 (memory persistence — the visible stream carries structural memory), C3 (sufficient
  hidden memory capacity — exactly saturated here), and C4 (history readback — the present
  determines neither past nor future, the hidden state does)." :187 `def CoreC1C4 : Prop := (∃ p q
  : Core, vis p = vis q ∧ p ≠ q ∧ vis (swapFn p) ≠ vis (swapFn q)) ∧ (∀ p : Core, vis (swapFn
  (swapFn p)) = vis p) ∧ (Fintype.card Bool = 2 ∧ ∀ r : Bool × Bool, (Finset.univ.filter (fun p :
  Core => vis p = r)).card = 2 ∧ ∀ p q : Core, vis p = r → vis q = r → p ≠ q → vis (swapFn p) ≠
  vis (swapFn q)) ∧ (∃ p q : Core, vis p = vis q ∧ p ≠ q ∧ histTriple p = (false, false, false) ∧
  histTriple q = (true, false, true))`.
- lemma-folded: `core_hidden_drives_visible` (:137, "**C1, literally.**"), `core_visible_period_two`
  (:143, "**C2, structurally.**"), `core_capacity_saturates` (:157, C3), `core_history_readback`
  (:176, "**C4 — history readback.**").
- scope: a property of one eight-state carrier; it is not a general predicate on partitions
  (I1.20–I1.24 have no general kernel form, C3's necessity excepted).
- depends_on: I1.38 · yields: I1.41, I1.42, I1.43.
- bridge: none at L · bearing: none at L.

**I1.40 — The core is observer-minimal.** kind theorem · level H · status proved [K] · flag —
- statement: IndependenceCensus.lean:148–150 "**The core is already observer-minimal**: the
  two-step visible itinerary separates all eight states, so no observational quotient collapses
  it." `theorem core_observer_minimal : ∀ p q : Core, itin p = itin q → p = q`.
- depends_on: I1.38 · yields: I1.41 · bridge: none at L · bearing: none at L.

**I1.41 — C1–C4 do not select the unrestricted operational completion (independence census).**
kind theorem · level H→M (one core, three coherent completions) · status proved [K]
(`oi_core_underdetermines_completion`, IndependenceCensus.lean:811) · flag —
- statement: :798–810 "**THE INDEPENDENCE CENSUS.** One and the same controlled-minimal,
  memory-bearing C1–C4 OI core … carries: 1. a CPTP, classically exact, NON-FUNCTORIAL coherent
  completion; 2. a strict unitary — hence functorial — completion that is NOT tensor-local; 3. a
  functorial AND tensor-local completion whose reachable control Lie algebra is a proper
  subalgebra of `su(D)`. So C1–C4 do not select the unrestricted operational completion." The
  statement's first conjunct is `(CoreC1C4 ∧ ∀ p q : Core, itin p = itin q → p = q)`; its tensor
  locality predicates are `IsLocalOnB` (:549, "A control lift is tensor-local on the `b` factor
  when it acts as `I_vh ⊗ M_b`") and `IsLocalOnVH` (:554) — definitions folded here.
- provenance: IndependenceCensus.lean header :48–61 ("⇒ C1–C4 ⇏ H-functor", "⇒ C1–C4 + H-functor ⇏
  H-tensor", "⇒ C1–C4 + H-functor + H-tensor ⇏ `𝔏₀ = su(D)`"); comb identity
  `threeCompletions_same_classical_comb` (:368).
- depends_on: I1.39, I1.40 · yields: the completion layer (I4).
- bridge: none at L (H→M within one module; no M→P module exists, bridge_check2) · bearing: none
  at L (records that C1–C4 leave the coherent, tensor-local and control structure undetermined).

**I1.42 — `SealedCoreIsFiniteOI`: the axiom-match audit.** kind hypothesis-structure (`def … :
Prop`) with its theorem `sealedCore_is_finiteOI` · level H · status proved [K]
(OIRealization.lean:305) · flag —
- statement: OIRealization.lean:282–290 "**THE FINITE-OI INGREDIENTS OF THE SEALED CORE**, each as
  the manuscript states it: a finite total system (Lemma 1); a proper finite visible subsystem with
  a hidden complement of more than one state (Lemma 2); the explicit product partition visible ×
  hidden (Lemma 2); the dynamics deterministic and injective, hence a bijection with a predecessor
  map (Lemma 3); the counting measure invariant under the passive step and the control (Lemma 3);
  recurrence — every state returns (Axiom 2, here with period two); registered differentiation —
  the visible readout distinguishes states (Axiom 1); coupling through the dynamics across the
  partition (the definition's third feature, which is C1); and the four diagnostics C1–C4." :291
  `def SealedCoreIsFiniteOI : Prop := Fintype.card Core = 8 ∧ … ∧ CoreC1C4` (eleven conjuncts,
  :292–302); :304 "**THE AUDIT PASSES**: the sealed core is a finite OI process in the manuscript's
  sense."
- scope (the module's own claim boundary, OIRealization.lean:53–56): "What remains outside the
  kernel is interpretive only: whether some reading of the manuscript's prose carries a
  cross-partition composition principle not present in the definition, the lemmas, the axioms or
  C1–C4 as stated. The audit found none: the only cross-partition content is the coupling clause,
  which is C1, and C1 is satisfied."
- depends_on: I1.38, I1.39 · yields: I1.45, `A1Realized` (I1.55: `a1_every_theory` uses its first
  conjunct).
- bridge: none at L · bearing: none at L. Kernel images of I1.1, I1.2, I1.6, I1.8–I1.12, I1.20.

**I1.43 — `RealizesSealedOICore T`: the realization predicate.** kind hypothesis-structure (`def …
: Prop`) · level M carrying an H-level core (the H→M transfer object) · status definition [K]; it
appears as hypothesis or conclusion in 94 kernel declarations (census part B) · flag —
- statement: OIRealization.lean:229–233 "**THE SEALED OI CORE, REALIZED IN A THEORY**: the core
  satisfies C1–C4; the passive step and the control are available as the transported permutation
  channels at level four; the actual visible readout is the native ancilla readout and is
  available as a family; and the realized visible comb agrees with the classical OI comb on every
  classical preparation and every finite word." :234 `def RealizesSealedOICore (T :
  FiniteOperationalTheory (Fin 2)) : Prop := CoreC1C4 ∧ T.availExt 4 Unit (fun _ => transport
  coreIdx (correlationExtension sigmaPerm (onesCorr Core))) ∧ T.availExt 4 Unit (fun _ => transport
  coreIdx (correlationExtension tauPerm (onesCorr Core))) ∧ (∀ r : Bool × Bool, transport coreIdx
  (readVisible r) = T.readout 4 (visIdx r)) ∧ T.availExt 4 (Bool × Bool) (fun r => transport coreIdx
  (readVisible r)) ∧ ∀ (steps : List VStep) (w : Core → ℂ), realizedFold steps (Matrix.reindex
  coreIdx coreIdx (Matrix.diagonal w)) = Matrix.reindex coreIdx coreIdx (Matrix.diagonal
  (visWeightFold steps w))`.
- provenance: OIRealization.lean:229–242; `readVisible` (:115, "**THE EMBEDDED OBSERVER'S
  READOUT**: keep the states whose visible pair is `r` — both hidden values survive.").
- depends_on: I1.39, `FiniteOperationalTheory` (OperationalAssembly.lean:594, I4) · yields: I1.44–
  I1.47, I1.50, I1.52, I1.60, I1.79–I1.83.
- bridge: H→M by definition (the core transported into level four of a theory); to P: none at L ·
  bearing: none at L.

**I1.44 — Composite unitary control realizes the sealed core.** kind theorem · level M · status
proved [K] (`realizesSealedOICore_of_control`, OIRealization.lean:252) · flag —
- statement: :251 "**CONTROL REALIZES THE SEALED CORE.**" `theorem realizesSealedOICore_of_control
  (T : FiniteOperationalTheory (Fin 2)) (hctrl : HasCompositeUnitaryControl T) :
  RealizesSealedOICore T`. Lemma-folded instances: `countermodel_realizesSealedOICore` (:260),
  `admissible_realizesSealedOICore` (:263), `fullQuantum_realizesSealedOICore` (:266),
  `relabel_available` (:245).
- depends_on: I1.43; `HasCompositeUnitaryControl` (OperationalAssembly.lean:665, I4: "Universal
  unitary control on EVERY finite ancilla extension") · yields: I1.45, I1.48 (`qm_implies_oiCore`),
  I1.54, CompletedOI's redundancy (I4).
- bridge: M-internal (control ⇒ core); to P: none at L · bearing: none at L.

**I1.45 — The capstone: one finite OI process on both sides of the compositional matrix.** kind
theorem · level M (carrying the H-level core) · status proved [K] (`sameCore_both_sides`,
OIRealization.lean:343; lemma-folded `sameCore_closure_not_inert` :316, `sameCore_inert_not_closure`
:324, `sameCore_both` :333) · flag —
- statement: :340–342 "**THE CAPSTONE.** One and the same finite, reversible, C1–C4
  Observation-Incompleteness process — audited as a finite OI process in the manuscript's sense —
  admits operational completions on either side of the compositional independence matrix, and one
  with both." `theorem sameCore_both_sides : SealedCoreIsFiniteOI ∧ (∃ T, RealizesSealedOICore T ∧
  ExactFiniteEndomorphicQuantumOps T ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ ¬
  InertSpectatorCompositionality T) ∧ (∃ T, … ∧ InertSpectatorCompositionality T ∧ ¬
  IteratedAncillaClosure T) ∧ (∃ T, … ∧ InertSpectatorCompositionality T ∧ IteratedAncillaClosure
  T)` (each `T : FiniteOperationalTheory (Fin 2)`; full text [S:sameCore_both_sides]).
- depends_on: I1.42, I1.44; the witnesses `countermodel`, `admissibleTheory`, `fullQuantum`
  (CompositionalIndependence and predecessors; I4) · yields: I1.46.
- bridge: none at L · bearing: none at L.

**I1.46 — Bare finite OI implies neither compositional principle (inert spectators, iterated
ancilla closure).** kind theorem · level M · status proved [K] (`finiteOI_not_implies_inert`,
OIRealization.lean:360; `finiteOI_not_implies_closure`, :366) · flag —
- statement: :357–359 "**BARE FINITE OI DOES NOT IMPLY EITHER COMPOSITIONAL PRINCIPLE**: realizing
  the audited core, with EXACT system quantum mechanics and full composite unitary control, forces
  neither inert-spectator compositionality nor iterated ancilla closure." `theorem
  finiteOI_not_implies_inert : ¬ ∀ T : FiniteOperationalTheory (Fin 2), RealizesSealedOICore T →
  ExactFiniteEndomorphicQuantumOps T → HasCompositeUnitaryControl T →
  InertSpectatorCompositionality T`; `finiteOI_not_implies_closure` likewise with
  `IteratedAncillaClosure T`. Header claim (OIRealization.lean:50–52): "BARE FINITE OI, as
  formalized by the sealed core, does not imply either compositional existence principle; the two
  principles are genuinely additional to it."
- depends_on: I1.45; `InertSpectatorCompositionality` (SpectatorBridge.lean:223, I4 — a spectator
  clause; "observational independence … is inert-spectator compositionality restated",
  CompletedOI.lean:24–27), `IteratedAncillaClosure` (AncillaClosure.lean:247, I4) · yields: —.
- bridge: **records a non-implication at level M**: the OI core does not yield the matrix-level
  spectator clause; no M→P bridge at L transfers this to the pair cone (bridge_check2.out) ·
  bearing: none at L.

**I1.47 — `OICore` (bare OI).** kind hypothesis-structure (`def … : Prop`) · level M (the core
realized) · status definition [K]; README.md:636–640: "**No ontological necessity**: `OICore` is an
existential realizability condition about a particular four-state gadget, so a containment theorem
about it is not an explanatory one, and nothing shows a hidden sub-quantum level is required —
with density matrices as states, informationally complete measurements exist, so the universally
quantified form of observational incompleteness is false at the quantum-state level." · flag —
- statement: CompletedOI.lean:95–96 "**BARE OI**: the original observation-incompleteness
  principle, unchanged." `def OICore (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  RealizesSealedOICore T`.
- provenance: CompletedOI.lean:96 (the rest of the module is thread I4's); README.md:91–92,
  :631–640. · depends_on: I1.43 · yields: I1.48, the OI⁺ layer (I4), I1.79.
- bridge: none at L · bearing: none at L.

**I1.48 — The forward-redundancy entry for `OICore`.** kind theorem (kernel, module CompletedOI —
recorded here because it fixes `OICore`'s status; the theorems belong to I4's module) · level M ·
status proved [K] (`qm_implies_oiCore` CompletedOI.lean:549, `completedOI_iff_physical` :110,
`oiCore_not_completedOI` :115, `oiCore_forward_redundancy` :557) · flag —
- statement: :546–548 "**QUANTUM MECHANICS REALIZES THE SEALED OI CORE.** … Containment only: the
  route is through full composite unitary control, so this says the quantum class is rich enough
  to build the core's gadget, not that observation explains it." :553–556 "**THE
  FORWARD-REDUNDANCY AUDIT ENTRY**, in one place: containment holds, the core is redundant in the
  forward direction, and the converse fails."
- depends_on: I1.44, I1.47 · yields: README.md:631–640 reading.
- bridge: none at L · bearing: none at L.

## D. Route B: the consequence closure and the substratum theory (kernel)

**I1.49 — `DerivedOI`: the consequence closure of the substratum.** kind hypothesis-structure ·
level M · status definition [K]; quantum mechanics satisfies it (`derivedOI_of_qm`, RouteB.lean:223)
and so does the substratum theory (`substratumTheory_derivedOI`, :290) · flag —
- statement: RouteB.lean:137–140 "**THE CONSEQUENCE CLOSURE, `DerivedOI`**: every theory-level
  predicate the kernel derives from the substratum, in the strongest form it derives it —
  reversible implementation locality (the substratum class is dagger-stable), embedded observation,
  and the availability at every level of the exchanges, the phases and the read-write operators."
  `def DerivedOI (T : FiniteOperationalTheory A) : Prop := ReversibleImplementationLocality T ∧
  EmbeddedObservation T ∧ ExchangesAvailable T ∧ PhasesAvailable T ∧ ReadWriteAvailable T`.
  Folded definitions: `ExchangesAvailable` (:123), `PhasesAvailable` (:128), `ReadWriteAvailable`
  (:133).
- scope (RouteB.lean:49–52): "Consequences proved at the stochastic level (the finite-horizon
  equivalence, hidden predictive memory, C3 necessity, reciprocity, the CT2 path) are theorems
  about processes and dynamics, not predicates on the theory's availability, and constrain no
  candidate."
- depends_on: `ReversibleImplementationLocality` (MicroscopicReversibility.lean:223, I4),
  `EmbeddedObservation` (EmbeddedObservation.lean:123, I4) · yields: I1.50, I1.60.
- bridge: H→M by the sourcing theorems it collects (substratum class → theory); to P: none at L ·
  bearing: none at L. The scope sentence is a kernel-side **non-transfer** record: the
  stochastic-level (H) results, C3 necessity included, constrain no M-level candidate.

**I1.50 — `DerivedOICore`: the closure with the sealed core.** kind hypothesis-structure · level M
· status definition [K] · flag —
- statement: RouteB.lean:145–147 "**THE CONSEQUENCE CLOSURE ON THE TWO-STATE CARRIER** adds the
  sealed OI core." `def DerivedOICore (T : FiniteOperationalTheory (Fin 2)) : Prop := DerivedOI T ∧
  RealizesSealedOICore T`.
- depends_on: I1.43, I1.49 · yields: I1.51–I1.54.
- bridge: none at L · bearing: none at L.

**I1.51 — The falsifier and the Route B target.** kind hypothesis-structure (`FalsifierUnavailable`
RouteB.lean:174, `RouteBTarget` :252) with theorems `target_separates` (:257), `target_not_qm`
(:263) · level M · status definitions [K]; theorems proved [K] · flag —
- statement: :172–175 "**THE FALSIFIER IS UNAVAILABLE**: the rotation `rot` of the two-state carrier
  at level one is not a one-outcome available operation." `def FalsifierUnavailable (T :
  FiniteOperationalTheory (Fin 2)) : Prop := ¬ T.availExt 1 Unit (fun _ => conjChannel rot)`;
  `def RouteBTarget : Prop := ∃ T : FiniteOperationalTheory (Fin 2), DerivedOICore T ∧
  FalsifierUnavailable T`.
- depends_on: I1.50 · yields: I1.53. · bridge: none at L · bearing: none at L.

**I1.52 — The substratum theory realizes the sealed core.** kind theorem · level H→M · status
proved [K] (`substratumTheory_realizesSealedOICore`, RouteB.lean:375; `substratumTheory_derivedOICore`
:380) · flag —
- statement: :374 "**THE SUBSTRATUM THEORY REALIZES THE SEALED OI CORE.** All four clauses close."
  `theorem substratumTheory_realizesSealedOICore : RealizesSealedOICore (substratumTheory (Fin 2))`.
- depends_on: I1.43; `substratumTheory` (the theory the monomial class generates; SubstratumInterface,
  I4) · yields: I1.53 · bridge: H→M (substratum class → the core realized); to P: none at L ·
  bearing: none at L.

**I1.53 — Route B: the closure with the core does not entail phase-free richness.** kind theorem
· level M · status proved [K] (`routeB_target` RouteB.lean:384, `derivedOICore_not_phaseFree`
:395) · flag —
- statement: :392–394 "**THE CLOSURE WITH THE CORE DOES NOT ENTAIL PHASE-FREE RICHNESS** on the
  two-state carrier: a theory satisfying every consequence the kernel derives from the substratum
  and the sealed core, and failing the one conjunct of `OIPlusMin` the substratum does not supply."
  `theorem derivedOICore_not_phaseFree : ∃ T : FiniteOperationalTheory (Fin 2), DerivedOICore T ∧ ¬
  PhaseFreeRichness T`.
- depends_on: I1.51, I1.52; `PhaseFreeRichness` (MinimalRepertoire.lean:423, I4) · yields: —.
- bridge: none at L · bearing: none at L (records that H-sourced content plus the core leaves the
  continuous drive unsupplied at level M).

**I1.54 — Quantum mechanics satisfies the closure with the core.** kind theorem · level M · status
proved [K] (`derivedOICore_of_qm`, RouteB.lean:231; `derivedOI_of_qm` :223) · flag —
- statement: :230 "**AND THE TWO-STATE CLOSURE WITH THE CORE.**" `theorem derivedOICore_of_qm (T :
  FiniteOperationalTheory (Fin 2)) (h : ExactAllFiniteEndomorphicQuantumOps T) : DerivedOICore T`.
- depends_on: I1.44, I1.50 · yields: consistency of I1.51 · bridge: none at L · bearing: none at L.

## E. The substratum axioms A1–A6 (manuscript and kernel)

**I1.55 — Realized-core images of A1 and A2; A1–A6 have no faithful form in the operational
interface.** kind hypothesis-structure (`A1Realized` ManuscriptAxioms.lean:76, `A2Realized` :83,
`A1A2Realized` :90) with theorems `a1_every_theory` (:94), `substratumTheory_A1` (:98),
`substratumTheory_A2` (:103), `substratumTheory_A1A2` (:107), `a2_of_control` (:112) · level M ·
status definitions and theorems proved [K]; the module's own boundary: "They are images, not the
axioms: at the substratum level A1 and A2 are formalization gaps like the rest, absent a sourcing or
identification map from `(S, φ)` into the theory." (ManuscriptAxioms.lean:24–26) · flag —
- statement: :72–75 "**THE REALIZED-CORE IMAGE OF A1**: the configuration space of the realized core
  is finite. … It is an image of A1, not A1: nothing identifies the core with a manuscript
  substratum's `S`." `def A1Realized (_T : FiniteOperationalTheory (Fin 2)) : Prop :=
  Fintype.card Core = 8 ∧ ∀ n : ℕ, Fintype.card (Fin 2 × Fin n) = 2 * n`; :88–89 "The conjunction of
  the two realized-core images. Not the manuscript OI: no manuscript-level conjunct of A1–A6 has a
  faithful form in this interface."
- depends_on: I1.38, I1.42, I1.44 · yields: —.
- bridge: **bridge absent, stated by the kernel**: no identification map from a manuscript
  substratum `(S, φ)` into a `FiniteOperationalTheory` (ManuscriptAxioms.lean:18–21: "nothing in the
  interface identifies that core with a manuscript substratum's `S` and `φ`. So no manuscript-level
  conjunct of A1–A6 is presently a faithful predicate of the bare theory.") · bearing: none at L.

**I1.56 — The configuration-level sourcing bound.** kind hypothesis-structure (`ConfigurationLevel`,
ManuscriptAxioms.lean:125) with theorems `substratumClass_configurationLevel` (:129),
`configurationLevel_iff_le_substratum` (:134), `configurationLevel_availExt_le` (:147),
`configurationLevel_falsifierUnavailable` (:155), `configurationLevel_not_phaseFree` (:169),
`configurationLevel_not_qm` (:175) · level H→M · status proved [K] · flag —
- statement: :122–124 "**A CONFIGURATION-LEVEL ARCHITECTURE**: every admissible implementation
  operator is monomial, a permutation of the configurations composed with a phase". `def
  ConfigurationLevel (𝓘 : ImplementationClass) : Prop := ∀ (S : Type) [Fintype S] [DecidableEq S]
  (K : Matrix S S ℂ), 𝓘 S K → IsMonomial K`; :174 "**NO CONFIGURATION-LEVEL CLASS GENERATES
  QUANTUM MECHANICS** on the two-state carrier."
- scope (ManuscriptAxioms.lean:48–50): "The kernel has no map from a substratum to an
  implementation class, so they bound every sourcing that factors through a configuration-level
  class, and say nothing about sourcings that do not."
- depends_on: `ImplementationClass`, `genTheory`, `IsMonomial` (I4's StructuralClosure /
  SubstratumInterface) · yields: ROADMAP "Settled negatively" rows (I4's scope).
- bridge: H→M bound for configuration-level sourcings only; the kernel states there is no map
  from a substratum to an implementation class; to P: none at L · bearing: none at L.

**I1.57 — The kernel `Substratum` and the predicates A1–A5.** kind hypothesis-structure
(`A1` SubstratumInterfaceAudit.lean:84, `A2` :87, `A3` :91, `A4Exact` :94, `A4` :98, `A5` :102,
`A3Family` :131; structure `Substratum` :60) · level H · status definitions [K]; theorems
`a2_every_substratum` (:106), `a1_of_finite` (:109), `a3_of_fintype` (:115), `a4_of_exact` (:118)
proved [K] · flag —
- statement: :56–59 "**A SUBSTRATUM**: a site type with lattice translations, an additive alphabet,
  and a finite-range second-order rule. … The structure carries no operational notion." :83 "**(A1)
  FINITENESS**: the configuration space is finite." `def A1 : Prop := Finite 𝒮.Conf`; :86 "**(A2)
  DETERMINISM**: the dynamics is a bijection." `def A2 : Prop := Function.Bijective 𝒮.φ`; :89–91
  `def A3 (D : ℕ) : Prop := ∀ i, (𝒮.R.N i).card ≤ D`; :93–94 `def A4Exact : Prop := ∀ (v : 𝒮.ι) (c :
  𝒮.ι → 𝒮.V), 𝒮.R.F (shiftBy v c) = shiftBy v (𝒮.R.F c)`; :101–102 `def A5 : Prop := ∀ c c' :
  𝒮.ι → 𝒮.V, 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'`.
- qualifications (ROADMAP.md:780–783): "A3's single-lattice form is vacuous — `a3_of_fintype`
  bounds the degree by the site count — so A3's content is the family form, not the per-lattice
  one. And A4 is carried up to a gauge parameter, with the exact form recovered at trivial gauge."
- depends_on: `Rule`, `leapEquiv` (SecondOrderCircuit/SecondOrderLayer) · yields: I1.58–I1.60.
- bridge: none at L · bearing: none at L.

**I1.58 — The manuscripts' wave rule satisfies A1–A5.** kind theorem · level H · status proved
[K] (`waveSubstratum_A1` SubstratumInterfaceAudit.lean:185, `_A2` :190, `_A3` :194 (degree `2 * d`),
`_A4Exact` :202, `_A5` :211) · flag —
- statement: `theorem waveSubstratum_A1 [NeZero L] [NeZero q] : (waveSubstratum d L q α).A1`; header
  (:14–16): "The manuscripts' discrete wave rule is an instance, `waveSubstratum`, and satisfies
  A1–A5 as stated."
- depends_on: I1.57 · yields: I1.59, I1.73 (lattice cut) · bridge: none at L · bearing: none at L.

**I1.59 — The observer theory of a substratum (the H→M sourcing arrow) and its limits.** kind
definition-as-hypothesis (`obsTheory`, SubstratumInterfaceAudit.lean:769) with theorems
`obsTheory_rule_independent` (:779), `obs_embeddedObservation` (:819),
`obs_reversibleImplementationLocality` (:823), `obs_sourcedOI` (:827), `obs_not_phasesAvailable`
(:844), `obs_not_control` (:854), `obs_not_phaseFree` (:857), `obs_not_qm` (:860),
`obs_qm_iff_phaseFree` (:864) · level H→M · status proved [K] · flag —
- statement: :767–768 "**THE OBSERVER THEORY OF A SUBSTRATUM**: the sourced theory on its
  configuration space, under the finiteness A1 supplies." `noncomputable abbrev obsTheory :
  FiniteOperationalTheory 𝒮.Conf := permTheory 𝒮.Conf`; `theorem obs_not_qm : ¬
  ExactAllFiniteEndomorphicQuantumOps (obsTheory 𝒮)`. Header (:33–35): "The observer theory depends
  on the substratum only through its configuration space (`obsTheory_rule_independent`):
  configuration-level sourcing consumes nothing of A3–A6."
- depends_on: I1.57, I1.60 · yields: —.
- bridge: **an H→M bridge exists** (substratum ⟶ observer theory, by sourcing theorems); its M-level
  image is not quantum mechanics; to P: none at L · bearing: none at L.

**I1.60 — The sourced theory: `SourcedOI`, and the core realized with no phase.** kind
hypothesis-structure (`SourcedOI` SubstratumInterfaceAudit.lean:619; folded definitions
`IsScaledPartialPerm` :231, `BijectionLevel` :485, `PreservesNonneg` :505) with theorems
`permTheory_realizesSealedOICore` (:740), `permTheory_twoState` (:753), `permTheory_not_qm` (:716),
`sourcedOI_qm_iff_phaseFree` (:654) · level H→M · status proved [K] · flag —
- statement: :616–618 "**THE SOURCED CLOSURE, `SourcedOI`**: the conjuncts of `DerivedOI` other
  than the phases — reversible implementation locality, embedded observation, and the availability
  at every level of the exchanges and the read-write operators." `def SourcedOI (T :
  FiniteOperationalTheory A) : Prop := ReversibleImplementationLocality T ∧ EmbeddedObservation T ∧
  ExchangesAvailable T ∧ ReadWriteAvailable T`; :737–739 "**THE SOURCED THEORY REALIZES THE SEALED
  OI CORE**: the passive step and the control are transported permutations, the readout is the
  native readout, and the comb is the classical comb. No phase is used."
- depends_on: I1.43, I1.49 · yields: I1.59.
- bridge: H→M (the observer's read-write access sources this theory); to P: none at L · bearing:
  none at L.

**I1.61 — A6: four readings, the adopted covariant one identically true on the interface.** kind
hypothesis-structure (`PreservesPointwise` BackgroundIndependence.lean:96, `A6Inv` :104, `A6Glob`
:111, `A6Cov` :131) with theorems `a6glob_of_a6inv` (:138), `a6cov_all` (:161), `d3b_not_a6inv`
(:213) · level H · status: ROADMAP.md:65 "**CONDITIONAL** — the adopted meaning is covariance,
`A6Cov`, which holds identically on every link-coupled rule of the least interface (`a6cov_all`), so
its content is the covariant interface and not a constraint" · flag —
- statement: `theorem a6cov_all (N : ι → Finset ι) (M : ι → ι → (V →+ V)) : A6Cov N M`;
  BackgroundIndependence header: "This module freezes what A6 could mean formally — four readings on
  three interfaces — and tests them on frozen carriers. **It does not try to prove A6 for anything
  physical, and it adopts no reading.**"
- depends_on: I1.57 · yields: I1.62 · bridge: none at L · bearing: none at L.

**I1.62 — A6 instantiation: the packaged K = 6 carrier; the named hypothesis.** kind theorem
(`pk1_packaging` A6Instantiation.lean:242, `pk2a_bridge` :257, `pk3a_A1` :276 … `pk3e_A5` :306,
`cx1_complex_covariance` :411, `cx3b_complex_not_A1` :512) · level H/X · status proved [K] for the
packaged carrier; the row CONDITIONAL on the named hypothesis (ROADMAP.md:738–741: "the
manuscripts' physical substratum is the packaged carrier … that identification is the whole of what
this row tracks. It is a premise no round of this programme discharges") · flag —
- statement: ROADMAP.md:65 "`A1`–`A5` hold of it with `A4Exact` under the translation-invariance
  hypothesis on the link coupling … the complex carrier itself, proved not to satisfy `A1`
  (`cx3b_complex_not_A1`)".
- depends_on: I1.57, I1.61 · yields: SM gauge layer (thread I2, physical layer) · bridge: none at
  L · bearing: none at L.

**I1.63 — Substratum (A1) Finiteness.** kind axiom (structural assumption) · level H · status
assumed ("Two-part status"; ROADMAP declared input "total-state finiteness choice where consumed",
ROADMAP.md:1456–1457) · flag —
- statement: Substratum.md:92 "(A1) **Finiteness.** The configuration space $S$ is finite.
  (Two-part status. E3, with the holographic bound read as a Hilbert-space dimension cutoff … bounds
  what observation reaches … The extension to all of $S$ is then a gauge choice rather than a
  further fact".
- kernel: `Substratum.A1` (I1.57); realized-core image `A1Realized` (I1.55: "an image of A1, not
  A1"). · depends_on: E3 (physical layer, I2) · yields: I1.10, I1.11, I1.35.
- bridge: none at L · bearing: none at L.

**I1.64 — Substratum (A2) Determinism.** kind axiom · level H · status empirically motivated /
assumed ("Two-part status … partly structural and partly anchored by one empirical input") · flag —
- statement: Substratum.md:94 "(A2) **Determinism.** $\varphi: S \to S$ is a bijection
  (deterministic, reversible dynamics). (Two-part status, per the dilemma argument of [Main §2.2]
  … Bijectivity for the dynamics governing registered history is thus partly structural and partly
  anchored by one empirical input, the observed statistics in that scope".
- kernel: `Substratum.A2`, automatic for the second-order form (`a2_every_substratum`, I1.57); image
  `A2Realized` (I1.55). · depends_on: I1.10 · yields: I1.35.
- bridge: none at L · bearing: none at L.

**I1.65 — Substratum (A3) Bounded coupling degree.** kind axiom · level H · status assumed
("conventional for physical systems", Substratum.md:217) · flag —
- statement: Substratum.md:96 "(A3) **Bounded coupling degree.** Each site is coupled to a bounded
  number of neighbors in $\varphi$'s action. (Required for locality and the emergence of a coupling
  graph with well-defined dimension. …)".
- kernel: `A3`, `A3Family` (I1.57; single-lattice form vacuous). · depends_on: — · yields: coupling
  graph / causal cones (thread I2: locality as manuscript statements).
- bridge: none at L · bearing: none at L.

**I1.66 — Substratum (A4) Center independence.** kind axiom · level H · status assumed (anchored
observationally: "the homogeneity of physical law"; "whether it is independently warranted by the
observer architecture remains the question flagged in §1") · flag —
- statement: Substratum.md:98 "(A4) **Center independence.** The dynamics $\varphi$ does not depend
  on a choice of "center" site, in two senses used below: $\varphi$ commutes with lattice
  translations up to gauge, and the update at a site contains no explicit copy of that site's
  present value ([SM §4.1])."
- kernel: `A4Exact`, `A4 G` (I1.57). · depends_on: — · yields: wave equation (SM §4.1; I2).
- bridge: none at L · bearing: none at L.

**I1.67 — Substratum (A5) Linearity.** kind axiom · level H · status assumed (ROADMAP.md:1459
declared input "A5 linearity"; "partly derived" given amplitude-scale gauge, Substratum.md:100) ·
flag —
- statement: Substratum.md:100 "(A5) **Linearity.** The wave equation for $\varphi$ is linear.
  (Equivalent to amplitude-scale gauge invariance — that the field-value scale is unphysical — via
  the linearity-equivalence lemma of [SM §4.1]; hence necessary *given* that gauge principle and
  "partly derived" in exactly that sense."
- kernel: `A5` (I1.57); used by `ensemble_underdetermined` (I1.76). · depends_on: — · yields:
  I1.76 · bridge: none at L · bearing: none at L.

**I1.68 — Substratum (A6) Background independence.** kind axiom · level H · status CONDITIONAL
(ROADMAP.md:65; I1.61–I1.62) · flag —
- statement: Substratum.md:102 "(A6) **Background independence.** The dynamics is covariant under
  spatially-varying internal-index transformations: a site-dependent transformation $G(\mathbf{n})$
  of the internal index is a symmetry of the dynamics provided the coupling data carried on the
  links are transformed with it … The content of the assumption is this covariant interface — the
  coupling is link-valued data on which the transformations act — and once it is in place the local
  transformation law imposes no further condition on the rule."
- kernel: `A6Cov` and the other readings (I1.61); no `Substratum` field (ROADMAP.md:775–776). ·
  depends_on: — · yields: SM gauge derivation (I2) · bridge: none at L · bearing: none at L.

**I1.69 — A1–A6 jointly sufficient, not proved minimal; the classes they exclude.** kind
manuscript-principle · level H · status assumed (sufficiency for the reconstruction, Theorem 23;
"not proved to be minimal") · flag —
- statement: Substratum.md:104 "The theorem's uniqueness claim holds under E1–E7 **and** A1–A6
  jointly; removing any of A3–A6 either requires new derivations or weakens the uniqueness. The set
  A1–A6 is sufficient for the reconstruction but is not proved to be minimal". Substratum.md:204
  "The structural assumptions A1–A6 exclude several broad classes of theory from the outset:".
- provenance: Substratum.md:104, :204–219. · depends_on: I1.63–I1.68 · yields: Theorem 23 (I2).
- bridge: none at L · bearing: none at L.

## F. C4 in the kernel: candidate forms, the realization clause, the physical discharge

**I1.70 — Candidate readback forms `C4e`, `C4r` and the no-go chain to P-indivisibility.** kind
hypothesis-structure (`IsRowStochastic` CausalReadback.lean:48, `PDivisible` :54,
`PIndivisibleWithin` :58, `C4e` :62, `C4r` :67) with theorems `c4e_implies_c4r` (:126),
`c4r_implies_pIndivisible` (:134), `c4e_implies_pIndivisible` (:148), `control_separation` (:295),
`causal_readback_verdict` (:314) · level H (rooted visible marginals) · status proved [K]; the
forms are "candidate" forms, "not asserted to strengthen, imply, or be implied by the manuscript's
history-level condition" (CausalReadback.lean:10–12) · flag —
- statement: :60–61 "**C4e, THE CANDIDATE EXACT MARGINAL-REVIVAL FORM**: two distinct rooted
  preparations whose one-time visible marginals coincide at some time and differ at a later time
  within the horizon." `def C4e (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop := ∃ (a b : V) (s t : ℕ), a ≠
  b ∧ s < t ∧ t ≤ K ∧ Γ s a = Γ s b ∧ Γ t a ≠ Γ t b`; `def C4r … := ∃ (a b : V) (s t : ℕ), a ≠ b ∧
  s < t ∧ t ≤ K ∧ tv (Γ s a) (Γ s b) < tv (Γ t a) (Γ t b)`; `theorem causal_readback_verdict (K :
  ℕ) (Γ : ℕ → Matrix V V ℝ) : (C4e K Γ → C4r K Γ) ∧ (C4r K Γ → PIndivisibleWithin K Γ) ∧ (C4e K Γ
  → PIndivisibleWithin K Γ)`.
- depends_on: `HiddenMemory.tv` (I2) · yields: I1.71 (comparison), I1.27.
- bridge: none at L · bearing: none at L.

**I1.71 — `RoutedReadback`: the manuscripts' realization clause for C4.** kind
hypothesis-structure (PhysicalC4Discharge.lean:68) with theorems `routedReadback_mono` (:80),
`routedReadback_overlap` (:88), `core_store_gap` (:218), `core_not_routedReadback` (:244),
`product_not_routedReadback` (:338), `tapeLedger_not_routedReadback_three` (:473),
`tapeLedger_routedReadback_four` (:510) · level H · status definition [K]; theorems proved [K]
(evidence level 2, ROADMAP.md:852–853) · flag —
- statement: PhysicalC4Discharge.lean:60–66 "**ROUTED READBACK WITHIN A WINDOW** — the manuscripts' realization clause on
  the merged rooted interface, transcribed from the Track I discovery round's frozen parent. W,
  write: … S, store: … R(1), causal read: … R(2), rooted reappearance: the rooted rows at `t`
  differ. Timing: `0 < w ≤ s < t ≤ K`." Header PhysicalC4Discharge.lean:12–15: "`RoutedReadback` is **the manuscripts' own
  realization clause**, formalized … It is **not a new condition**, it is **not** called a
  strengthening of the manuscript's history-level condition, and **nothing is numbered beyond C4**."
  PhysicalC4Discharge.lean:22 "**Nothing in this module says that C4 holds, or fails, at either physical cut.**"
- recorded discrepancy (header :27–35): under the frozen spelling "the sealed C1–C4 core carries
  no routed witness at any window (`core_not_routedReadback`)" (ROADMAP.md:861–862).
- depends_on: `RootedRealization`, `rootedMap`, `marg` (RootedClassification, HiddenMemory; I2) ·
  yields: I1.27, I1.73, I1.74 · bridge: none at L · bearing: none at L.

**I1.72 — `RoutedReadbackAtStorage` and the incomparability of the two readings.** kind
hypothesis-structure (PhysicalC4StorageReadback.lean:69) with theorems
`core_routedReadbackAtStorage_two` (:342), `storageReadback_not_implies_routedReadback` (:488),
`routedReadback_not_implies_storageReadback` (:689), `routedAtStorage_forces_return_indivisibility`
(:244) · level H · status proved [K] · flag —
- statement: ROADMAP.md:888–890 "**The two readings are incomparable as predicates**, by two
  exhibited carriers with exact certificates and in neither direction by a failed search"; :894–896
  "Neither reading is called stronger than the other, neither is called the correct reading of C4,
  and the manuscripts are **silent** on which random variable the realization clause's record is at
  the storage surface".
- depends_on: I1.71 · yields: I1.74 · bridge: none at L · bearing: none at L.

**I1.73 — The lattice cut: `LatticeCutReadback` (the named residual).** kind hypothesis-structure
(PhysicalC4Discharge.lean:633) with `latticeCutReadback_iff` (:640),
`cutRealization_rootedMap_isRowStochastic` (:604), `cutRealization_rootedMap_periodic` (:611) ·
level H (the wave substratum's cut realization) · status open (ROADMAP.md:66: "at the lattice cut
`[SM]` Theorem 22's readback genericity lemma in the form `LatticeCutReadback` over admissible
regions at the return window") · flag —
- statement: ROADMAP.md:903–907 "At the **lattice cut** the datum is already a kernel object —
  `cutRealization (waveSubstratum d L q α) Vs μ` — and the residual is a mathematical job: `[SM]`
  Theorem 22's readback genericity lemma, `LatticeCutReadback d L q α Vs (uniform) (τ_return Vs)`
  for every connected region with `|Vs| ≤ N/3`."
- depends_on: I1.58, I1.71 · yields: I1.74 · bridge: none at L · bearing: none at L.

**I1.74 — ROADMAP P1: Physical C4 discharge at the cosmological and lattice cuts.** kind
obligation (ROADMAP) · level H/X · status open (ROADMAP.md:66 "**OPEN**, and now EXACT") · flag —
- statement: ROADMAP.md:66 "| **P1** | Physical C4 discharge at the cosmological and lattice cuts |
  Physical realization | **OPEN**, and now EXACT: round C4-1 put the manuscripts' realization clause
  in the kernel as `RoutedReadback`, bounded what a discharge would need and what it would buy, and
  made the residual exact **per cut** — at the cosmological cut the finite realization datum
  itself, which the manuscripts describe and do not supply, and then a routed witness within the
  window; at the lattice cut `[SM]` Theorem 22's readback genericity lemma in the form
  `LatticeCutReadback` over admissible regions at the return window | the actual physical
  realization |". Also ROADMAP.md:840–842: "at the cosmological cut C4 is open, and at the lattice
  cut C2 and C4 both remain hypotheses."
- provenance: ROADMAP.md:66, :838–916; round records `programmes/physical-realization/
  round-c4-1-physical-discharge/`, `round-c4-2-storage-readback/`. · depends_on: I1.71–I1.73 ·
  yields: "the actual physical realization" · bridge: none at L · bearing: none at L.

## G. Observer structure: the internal observer, the observation map, the declared inputs

**I1.75 — The internal observer: a passive self-record can only be read (OI-N5).** kind
hypothesis-structure (`Records` InternalObserver.lean:63, `IsInternalObserver` :68) with theorems
`branch_kills_other_block` (:116), `internal_outcome_law` (:150), `internal_complete_iff` (:169),
`no_complete_internal_observer` (:206), `classical_control` (:222), `recordInstr_not_internal` (:315)
· level M (instruments on a finite carrier with a record map) · status proved [K] · flag —
- statement: :66–67 "**An internal observer**: a recording instrument that is passive on the
  record-block algebra." `def IsInternalObserver (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  IsBlockPassiveInstrument blk F ∧ Records blk F`; `theorem no_complete_internal_observer (rec : B →
  O) (hA : 1 < Fintype.card A) [Nonempty B] : ¬ ∃ F : O → Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A ×
  B) (A × B) ℂ, IsInternalObserver (recBlk rec) F ∧ SeparatesBlockStates (recBlk rec) F`. Header:
  "A passive internal observer cannot write a new record; it can only reveal which record was
  already present." (header :22–23) Not claimed (header :40): "Anything about `OICore`: N4 shows passive facts do not
  discriminate it".
- depends_on: `IsBlockPassiveInstrument` (CentralObservation/PassiveObservation) · yields: —.
- bridge: none at L · bearing: none at L.

**I1.76 — ROADMAP P1: the stochastic observer interface — source `(Obs, μ)`.** kind obligation
(ROADMAP) with kernel theorems `ensemble_underdetermined` (StochasticInterface.lean:118),
`waveSubstratum_stochastic_interface_gap` (:191) · level H · status open (ROADMAP.md:69) · flag —
- statement: ROADMAP.md:69 "**OPEN**, with the present architecture bounded negatively:
  `StochasticInterface` proves the invariant ensemble is not uniquely determined on the wave
  substratum under its stated hypotheses (`ensemble_underdetermined`,
  `waveSubstratum_stochastic_interface_gap`), while the observation-map leg is not supplied on
  `Substratum.Conf`. … This is distinct from C4: C4 asks whether hidden history is routed back;
  this row asks which `(Obs, μ)` defines the observed stochastic law in the first place."
- provenance: ROADMAP.md:69, :918–934. Module StochasticInterface.lean not in census (a) part A;
  its two cited theorems are recorded here. · depends_on: I1.57, I1.67 (A5 is a hypothesis of
  `ensemble_underdetermined`) · yields: "a fully sourced physical stochastic law `(φ, Obs, μ)`".
- bridge: none at L · bearing: none at L.

**I1.77 — ROADMAP: declared inputs and conditional hypotheses (status-fixing).** kind obligation
(ROADMAP accounting section) · level H/X · status: each listed premise assumed ("declared input,
not currently targeted") · flag —
- statement: ROADMAP.md:1455–1461 "The manuscripts explicitly carry several substantive premises
  whose current role is to condition a claim, not to sit in the proof queue: recurrence; the
  minimal finite representative/total-state finiteness choice where consumed; the empirical
  unitarity input used in the determinism-recovery margin; maximal-entropy invariant-measure
  selection; hidden-sector/effective mixing hypotheses; spatial isotropy; and A5 linearity. Their
  downstream uses must remain visibly conditional unless a future programme elects to derive or
  replace them. Their absence from the active queue therefore means “declared input, not currently
  targeted,” not “Lean proved.”"
- depends_on: — · yields: the statuses of I1.2, I1.10, I1.11, I1.12, I1.30, I1.31, I1.67.
- bridge: none at L · bearing: none at L.

**I1.78 — ROADMAP interpretation boundary (OI→QM emergence narrower than "all of QM").** kind
manuscript-principle (ROADMAP framing) · level H→M · status assumed (framing; no theorem) · flag —
- statement: ROADMAP.md:44–49 "This statement is deliberately narrower than “all of physical quantum
  mechanics follows from bare OI.” The remaining queue determines how far the emergence extends. The
  operational completion principles remain explicit additional conditions; … Physical C4 asks
  whether the abstract observational structure is discharged at the physical cuts".
- depends_on: — · yields: —.
- bridge: **records that operational completion principles are additional conditions** (no
  transfer from bare OI) · bearing: none at L.

**I1.84 — The finite-horizon observability quotient: OI resolves exactly the itinerary classes.**
kind theorem · level H (a deterministic permutation `φ` of a carrier with a visible labelling
`vis`) · status proved [K] (`branchDomain_span_eq_itineraryInvariant`, ObservabilityQuotient.lean:270;
module not censused whole — recorded for the observer structure, finite resolution) · flag —
- statement: ObservabilityQuotient.lean:270–273 `theorem branchDomain_span_eq_itineraryInvariant (φ :
  Equiv.Perm S) (vis : S → I) (K : ℕ) : Submodule.span ℝ {w : S → ℝ | BranchDomainK φ vis K w} =
  ItineraryInvariantK φ vis K`; docstring :267–269 "the operationally preparable diagonal directions
  are precisely the distinctions the visible record resolves on the accessible window, and nothing
  finer." Header :8–10: "C4 asks only for a readback gap on an accessible window — none of C1–C4
  asserts complete microstate recovery."
- depends_on: I1.9, I1.10 · yields: I1.85; the coherent-lift chain (I3's K∞ modules import it).
- bridge: none at L — the module lies in the import closure of `CompositeDimension` and `K2Guard`
  (bridge_check3.out), but no declaration of the 21 K-programme / pair modules mentions its objects,
  in a signature or anywhere in its source (bridge_check4.out: VERDICT NONE-FOUND) · bearing: none
  at L.

**I1.85 — Bare OI does not make the ontic carrier observable; the minimal passive carrier.** kind
theorem · level H · status proved [K] (PassiveQuotient.lean: `quotient_itinerarySeparating` :222,
`hiddenExt_not_separating` :534, `hiddenExt_same_law` :563, `passiveQuotient_glue_forces_G1` :444;
module not censused whole) · flag —
- statement: :532–533 "**RAW-CARRIER SEPARATION IS NOT DERIVABLE.** Any carrier extends, by an
  observationally inert hidden fibre, to a carrier that is NOT itinerary-separating." :560–562 "**THE
  PASSIVE LAW CANNOT SEE THE FIBRE.** For every prior on the extension with the right base
  marginal, every finite visible trajectory probability agrees with the base — the entire closed
  passive law is preserved while separation fails." Header :8–9: "C1–C4 and the ETH/mixing layer
  CANNOT imply itinerary separation of the raw carrier".
- depends_on: I1.84 · yields: the coherent-lift chain (I3).
- bridge: none at L (as I1.84; bridge_check4.out) · bearing: none at L.

## H. Realization theorems that carry the sealed core in other modules (kernel; level M)

These state that theories realizing the sealed core exist on every side of each completion
condition. They are recorded because the core enters their statements (census (a) part B); the
completion conditions themselves (validity, inert spectators, control, iterated ancilla closure,
system-to-level-one, observer recursion) are thread I4's records.

**I1.79 — Passive incompleteness does not diagnose `OICore`.** kind theorem · level M · status
proved [K] (PassiveIndependence.lean: `label_not_oiCore` :237, `oiCore_to_passive_vacuous` :248,
`passivelyIncomplete_without_oiCore` :255, `passive_not_implies_oiCore` :260,
`passive_nondiscriminating` :269, `sector_diagram` :335) · flag —
- statement: :259–261 "**The converse implication fails.**" `theorem passive_not_implies_oiCore :
  ¬ ∀ T : FiniteOperationalTheory (Fin 2), PassivelyIncomplete T → OICore T`; README.md:747–749
  "So `OICore T → PassivelyIncomplete T` holds for every … `PassivelyIncomplete T → OICore T` fails".
- depends_on: I1.47 · yields: I1.75's "not claimed" clause · bridge: none at L · bearing: none at L.

**I1.80 — Control is independent of the other conditions and of OI realization.** kind theorem
· level M · status proved [K] (DiagonalTheory.lean: `diag_realizesSealedOICore` :358,
`control_independent` :398, `minimality_audit` :415; the witness `diagTheory` also gives
`oiCore_not_completedOI`, I1.48) · flag —
- statement: :397 "**CONTROL IS INDEPENDENT** of the other four conditions and of OI realization."
  `theorem control_independent : ∃ T : FiniteOperationalTheory (Fin 2), CompositeOperationalValidity
  T ∧ InertSpectatorCompositionality T ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧
  RealizesSealedOICore T ∧ ¬ HasCompositeUnitaryControl T`.
- depends_on: I1.43 · yields: I1.81 · bridge: none at L · bearing: none at L.

**I1.81 — Five-way minimality: each completion condition fails in some theory realizing the
core.** kind theorem · level M · status proved [K] (RankGapTheory.lean: `gap_realizesSealedOICore`
:338, `closure_cell_closed` :688, `five_way_minimality` :702; restated in
`operational_classification`, IsometryExtension.lean:257; README.md:73–79) · flag —
- statement: RankGapTheory.lean:696–701 "**FIVE-WAY MINIMALITY.** For each of the five physical
  completion conditions, the same finite OI framework admits a theory satisfying the other four,
  realizing the sealed OI core, and failing exactly that one: validity (`everywhereAvailable`),
  inert spectators (the round-34 countermodel), full control (`diagTheory`), iterated ancilla
  closure (`gapTheory`), system-to-level-one (`systemLoose`)." (signature [S:five_way_minimality]).
  README.md:77–79: "Bare finite OI therefore does not select quantum mechanics (`oi_alone_not_qm`);
  the theorem classifies the OI-compatible completions and does not derive quantum mechanics from
  observation (`oi_compatible_classification`)."
- depends_on: I1.43, I1.80 · yields: GeneralCarrier's `main_result`, `oi_alone_not_qm` (I4).
- bridge: none at L · bearing: none at L.

**I1.82 — The substantive census: every failure pattern of the three substantive principles
realized with the core.** kind theorem · level M · status proved [K] (SubstantiveCensus.lean:
`substantive_census` :986, `no_boolean_relation` :1012; lemma-folded `classTheory_realizes` :394,
`diagGap_realizes` :776, `diagTwoPos_realizes` :828, `capped_realizes` :862, `cappedDiag_realizes`
:891, `cell_none` … `cell_ICK` :927–978) · flag —
- statement: :984–990 "**THE CENSUS**: every failure pattern of the three substantive principles is
  realized by a well-formed theory carrying the sealed OI core." `theorem substantive_census (gI gC
  gK : Bool) : ∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ RealizesSealedOICore T ∧
  (InertSpectatorCompositionality T ↔ gI = true) ∧ (HasCompositeUnitaryControl T ↔ gC = true) ∧
  (IteratedAncillaClosure T ↔ gK = true)`.
- depends_on: I1.43; `WellFormed` (GeneralCarrier, I4) · yields: README.md:84–89.
- bridge: none at L · bearing: none at L.

**I1.83 — The level-one seam and inert spectators are independent of OI realization.** kind
theorem · level M · status proved [K] (LevelOneSeam.lean: `systemLoose_realizesSealedOICore` :320,
`levelOne_independent` :353; LevelOneRecursion.lean: `levelOne_independent_of_recursion` :46;
PhysicalCharacterization.lean: `validity_independent` :343, `inert_independent` :364,
`levelOne_independent'` :375) · flag —
- statement: PhysicalCharacterization.lean:363 "**INERT SPECTATORS ARE INDEPENDENT** of the other
  four conditions and of OI realization." `theorem inert_independent : ∃ T : FiniteOperationalTheory
  (Fin 2), CompositeOperationalValidity T ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T
  ∧ SystemToLevelOne T ∧ RealizesSealedOICore T ∧ ¬ InertSpectatorCompositionality T`.
  LevelOneRecursion.lean:43–45 "**The level-one seam is independent of observer recursion.** A
  theory with composite operational validity, inert spectators, composite unitary control, iterated
  ancilla closure, observer recursion and the sealed OI core, and no system-to-level-one seam."
- depends_on: I1.43 · yields: I1.81 · bridge: none at L · bearing: none at L (M-level: the
  spectator clause is not implied by the core together with the other four conditions).

***

## I. Out-of-scope items met in I1's records (named, not recorded; see CENSUS.md)

Definitions used in the statements above whose records belong to other threads:
`FiniteOperationalTheory` (OperationalAssembly.lean:594), `HasCompositeUnitaryControl` (:665),
`InertSpectatorCompositionality` (SpectatorBridge.lean:223), `IteratedAncillaClosure`
(AncillaClosure.lean:247), `ExactFiniteEndomorphicQuantumOps` (KrausSoundness.lean:134),
`ExactAllFiniteEndomorphicQuantumOps` (LevelOneSeam.lean:186), `PhaseFreeRichness`
(MinimalRepertoire.lean:423), `EmbeddedObservation` (EmbeddedObservation.lean:123),
`ReversibleImplementationLocality` (MicroscopicReversibility.lean:223): thread I4 (the
matrix-level and completion layer; the protocol's do-not-assume flags for observational
independence, reversible richness, observer recursion and the spectator clauses attach there).
`HiddenMemory.Realization`, `capacity_floor_of_fun`, `tv`, `RootedRealization`, `rootedMap`,
`marg`, `RecurrenceHorizon.horizon_verdict`: thread I2 (hidden-memory and recurrence results).
