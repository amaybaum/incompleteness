# Corpus correction round CC-2 — the premise ledger's 27 drift and tension items, with the verification surfaces they move: PREREGISTRATION

**Status: candidate freeze (drafted off-repo; stops at the freeze boundary).** This file is the control plane of a
native round under `AGENTS.md` §A.39. It is to be drafted on its pull request from `D` and is final only at the
commit `F` the owner designates; no commit after `F` changes it. The per-item disposition table, the deferred set,
the guardrails, the closure steps and the outcomes below are fixed; nothing outside §3's rows changes under any
outcome.

## The declarations

```v3-round
round CC-2
kind non-sealing
record-directory verification/audits/manuscript/round-cc-2-corpus-correction/
```

```v3-governed-paths
record AM verification/audits/manuscript/round-cc-2-corpus-correction/
record AM verification/receipts/CC-2.json
execution M papers/Substratum.md
execution M papers/Substratum.tex
execution M papers/Substratum.pdf
execution M papers/Main.md
execution M papers/Main.tex
execution M papers/Main.pdf
execution M papers/GR.md
execution M papers/GR.tex
execution M papers/GR.pdf
execution M papers/SM.md
execution M papers/SM.tex
execution M papers/SM.pdf
execution M papers/Structure.md
execution M papers/Structure.tex
execution M papers/Structure.pdf
execution M papers/Explainer.md
execution M papers/Explainer.tex
execution M papers/Explainer.pdf
execution M papers/Methodology.md
execution M papers/Methodology.tex
execution M papers/Methodology.pdf
execution M book/ch02-substratum.md
execution M book/ch05-gauge-structure.md
execution M book/ch09-universality.md
execution M book/The-Incompleteness-of-Observation-FULL.md
execution M book/The-Incompleteness-of-Observation-FULL.tex
execution M book/The-Incompleteness-of-Observation-FULL.pdf
execution M verification/coverage/LEDGER.json
execution M verification/lean/edge_rigidity_probe.py
```

The record directory holds this preregistration, the round's frozen controls `controls.py` (stage C1) and the
result note. The receipt path is `verification/receipts/CC-2.json`. Every other path the round changes is an
execution path listed above: eleven manuscript sources, the sixteen built artifacts regenerated from them, and
the two verification surfaces the release gate reads against those sources — the proof-coverage ledger and the
edge-rigidity probe. No Lean module, no other verification tool, `verification/ROADMAP.md`, the workflow, and no
other round's record change under any outcome.

## The objects

- **`D`** = `6d335d0ad7a19092b6a10098afcea162a632a402`, the head of `main` after `CC-1`'s halted record landed (push run
  37147553791, every job green). Every execution
  path of this round is byte-identical at `D` to its state at `0f2687b7`, the premise ledger's audited base (the
  halted landing changed record paths only), so every ledger anchor is a live line and no manuscript, the ledger
  or the probe has moved since the audit.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation (if any) and the receipt commit, as §A.39 defines them.

## 1. Scope and boundary

**Provenance.** Round `CC-1` (`verification/receipts/CC-1.json`, halted under the specification's `S12`) froze
the same 27 items with the same dispositions and the same 60 substitutions, applied them at its candidate `E`
`342fb68f0196a77c9085ac981f01266fd86eb869`, and halted because that candidate's exact-head run 37143464345 failed
two checks reading files its governed paths did not name: the release gate's `coverage` step and the
`edge_rigidity_probe` guard `R7-A6P`. This round governs those two files and carries, as frozen instances
(§3.2), exactly the consequences the 60 substitutions have on them. Nothing else is added: no item, no
substitution, no disposition changes from `CC-1`'s freeze.

**In scope.** The 27 drift/tension items of the premise ledger (checkpoint 1 §5: T-A1-1, T-A2-1, T-A2-2,
T-A2-3, T-A3-1, T-A3-2, T-A4-1, T-A6-1, T-A6-2, T-HT1-1, R1–R13; checkpoint 2 §6: T-E-1 … T-E-4), each with
exactly one of three dispositions (§2); the six verification-surface instances of §3.2 that those dispositions
force; and nothing else.

**Out of scope, by construction (no textual change at any site for these reasons).**
- Level 3A results: EXPOSED, AT-RANK, R4-CLOSED, LEMMA-3A, the octahedral diagnostic.
- The SELECT thread (selection principle, ORD∞ / TRANS / EO / V4′, the round-2 target theorem).
- 3B claims (edge-permutivity as mechanism, the rule matrix, the H factor).
- Round-2 provenance material (LIMCLOSE-C, completed-body availability, representation-vs-selection framing).
- The ledger's architecture (representation → H-T1 → H-T2 → realization; G / R4 / Q layering; OBS-1 as a
  manuscript notion). These are round 2, after 3B.
- Any banking of 3A as a verification round (a separate decision, not assumed here).
- Any new claim, any reorganization beyond what a listed correction requires, any count change not forced by a
  listed correction.

**Rule of the round.** A site is edited only if its item's disposition is CORRECT-IN-PLACE or REMOVE/QUALIFY
ASSERTION, and then only with the frozen replacement text of §3. If executing a listed correction would require
stating anything from the out-of-scope list, the item is halted at execution and reported, not improvised.

## 2. The three dispositions

| Disposition | Meaning | Manuscript rule applied |
|---|---|---|
| **CORRECT-IN-PLACE** | the sentence is wrong or over-scoped relative to its own derivation; rewrite it to what the derivation supports, in the paper's register | §A.27 correct in place; §A.32/§A.33 register |
| **REMOVE/QUALIFY ASSERTION** | a status word (theorem / derived / proved) or a listed result is not supported by the cited chain; remove the assertion or downgrade the status label using the corpus's **own existing** qualification, keep the derivation | §A.30 remove the assertion, keep the derivation; never assert-then-qualify |
| **DEFER-TO-ROUND-2** | a correct statement at the site cannot be written without the representation/realization/selection or OBS architecture, or without a Track-II interpretation; **literally no textual change** | — |

## 3. Per-item disposition table (frozen with the preregistration)

§3 is the authorization: the file at `E` equals the file at `D` with exactly the substitutions listed, each `old`
occurring exactly once at `D` (verified before this freeze, all 60 manuscript instances, 59 distinct old literals, and
the six verification-surface instances of §3.2), and nothing else changes.
Mirrors are listed as their own instances; a `FULL.md` instance whose old and new are byte-identical to its
chapter instance is stated by reference to it. The machine-readable form of this table — every instance literal —
is embedded in `controls.py` (stage C1), and `controls.py` must agree with this table instance by instance.

### T-A1-1 — CORRECT-IN-PLACE

**T-A1-1.1** `papers/Substratum.md` — source: L-A1 §T-A1-1 (LEDGER 492–512)

old:

```text
In particular, P-indivisibility — established on the minimal finite representative by recurrence ($\varphi^N = \mathrm{id}$, [Main §2.3]) — holds on every member; on infinite-deep-sector members, where recurrence is unavailable, the accessible-timescale backflow lemma ([Main §2.3]) establishes the same conclusion without recurrence. The two routes agree where both apply and jointly cover the orbit; A1's choice of the finite representative is therefore a convenience of proof, not a physical restriction.
```

new:

```text
In particular, every statement expressible through the accessible-timescale transition law transfers across the orbit. P-indivisibility at the recurrence scale — established on the minimal finite representative by recurrence ($\varphi^N = \mathrm{id}$, [Main §2.3]) — is not such a statement: it holds on the finite members, and on infinite-deep-sector members, where recurrence is unavailable, the accessible-timescale backflow lemma ([Main §2.3]) gives the accessible-window property it states, a different and weaker conclusion. A1's choice of the finite representative is therefore a convenience of proof for accessible-timescale content; recurrence-scale content is stated for the finite representative.
```

**T-A1-1.2** `papers/Main.md` — source: L-A1 §T-A1-1 (LEDGER 492–512)

old:

```text
consumed here by the recurrence step of §2.3 and by §4.6, whose conclusions accordingly hold on the finite representative and, being boundary-only in content, on every member of the gauge class (the transfer stated and proved as a corollary in the companion substratum construction);
```

new:

```text
consumed here by the recurrence step of §2.3 and by §4.6, whose conclusions hold on the finite representative; those expressible through the accessible-timescale transition law hold on every member of the gauge class (the transfer stated and proved as a corollary in the companion substratum construction), while the recurrence-scale conclusion of §2.3 is a statement about the finite representative;
```

### T-A2-1 — CORRECT-IN-PLACE

**T-A2-1.1** `papers/GR.md` — source: L-A2 (LEDGER 342, 359–362); guardrail 1

old:

```text
would still produce (U1)–(U3), and — under H-slope, H-frame and H-Hawking at its horizon — $\hbar = c^3 \epsilon^2/(4G)$, $\epsilon = 2\,l_p$ and the area law with its $1/4$ coefficient, provided the partial-trace machinery and thermal self-consistency hold.
```

new:

```text
would still produce (U1)–(U3). The calibration $\hbar = c^3 \epsilon^2/(4G)$, $\epsilon = 2\,l_p$ and the area law with its $1/4$ coefficient use in addition, on the classical side, the symmetric detailed-balance rate ratio used above — obtained on the OI branch from microreversibility under the stated time-reversal-even coarse-state condition; for general non-bijective dynamics that ratio is an additional condition, supplied neither by S1–S4 nor by H-slope, H-frame and H-Hawking, and the calibration holds for such a substratum only where it is established, with the partial-trace machinery and thermal self-consistency.
```

**T-A2-1.2** `papers/GR.md` — source: L-A2 (LEDGER 342); guardrail 1

old:

```text
if in addition H-slope, H-frame and the H-Hawking conditions hold at its horizon, so do (C1$'$)–(C3$'$) with the same numerical content.
```

new:

```text
if in addition H-slope, H-frame and the H-Hawking conditions hold at its horizon, together with the symmetric detailed-balance rate ratio used above — obtained on the OI branch under the stated time-reversal-even coarse-state condition, and an additional condition for general non-bijective dynamics — so do (C1$'$)–(C3$'$) with the same numerical content.
```

### T-A2-2 — CORRECT-IN-PLACE

**T-A2-2.1** `papers/Main.md` — source: L-A2 (LEDGER 343)

old:

```text
The characterization theorem is accordingly conditional on finite reversible substratum dynamics — an empirically motivated reconstruction, not a pure derivation.
```

new:

```text
The physical reading of the characterization theorem — the identification of nature with a finite reversible substratum — is accordingly conditional on that representation choice, an empirically motivated reconstruction rather than a pure derivation; the law-level equivalence of §3.4 itself holds for every finite-horizon law.
```

### T-A2-3 — CORRECT-IN-PLACE

**T-A2-3.1** `papers/Main.md` — source: L-A2 §T-A2-3 (LEDGER 381–387)

old:

```text
so it is excluded by the observed unitarity of quantum dynamics; a merge that leaves no statistical trace is removable,
```

new:

```text
so it is excluded wherever the observed statistics are of that doubly stochastic class under the uniform prior; a merge that leaves no statistical trace is removable,
```

**T-A2-3.2** `papers/Main.md` — source: L-A2 §T-A2-3 (LEDGER 381–387)

old:

```text
the first empirical (the observed unitarity of quantum dynamics), the second structural (finiteness and recurrence).
```

new:

```text
the first empirical (the observed statistics, in the uniform-prior doubly stochastic scope), the second structural (finiteness and recurrence).
```

**T-A2-3.3** `papers/Substratum.md` — source: L-A2 §T-A2-3 (LEDGER 381–387); mirror

old:

```text
a non-injective descent either leaves a statistical trace — excluded by the observed unitarity of quantum dynamics — or leaves none,
```

new:

```text
a non-injective descent either leaves a statistical trace — excluded where the observed statistics are of the doubly stochastic class that the uniform-prior marginal of a bijection produces — or leaves none,
```

**T-A2-3.4** `papers/Substratum.md` — source: L-A2 §T-A2-3 (LEDGER 381–387); mirror

old:

```text
partly anchored by one empirical input, the observed unitarity;
```

new:

```text
partly anchored by one empirical input, the observed statistics in that scope;
```

**T-A2-3.5** `papers/Methodology.md` — source: L-A2 §T-A2-3 (LEDGER 381–387); mirror

old:

```text
so such merges are excluded by the *observed unitarity* of quantum dynamics, an evidential input rather than a further axiom.
```

new:

```text
so such merges are excluded where the observed statistics are of that doubly stochastic class under the uniform prior, an evidential input rather than a further axiom.
```

**T-A2-3.6** `papers/Main.md` — source: L-A2 §T-A2-3 (LEDGER 381–387); mirror Main.md:706 (iii)

old:

```text
close the hidden-sector margin using one *empirical* input — the observed unitarity of quantum dynamics — and one structural principle,
```

new:

```text
close the hidden-sector margin using one *empirical* input — the observed statistics, in the uniform-prior doubly stochastic scope — and one structural principle,
```

### T-A3-1 — CORRECT-IN-PLACE

**T-A3-1.1** `papers/SM.md` — source: L-A3 §T-A3-1 (LEDGER 944–956)

old:

```text
*The entanglement entropy of a spatial region V in the wave equation scales as $S(V) = \eta\,|\partial V|$. This holds for both the linear wave equation over $\mathbb{R}$ and the mod-q wave equation over $\mathbb{Z}/q\mathbb{Z}$.*
```

new:

```text
*For the linear wave equation over $\mathbb{R}$, the entanglement entropy of a spatial region V scales as $S(V) = \eta\,|\partial V|$ [3]. For the mod-q wave equation over $\mathbb{Z}/q\mathbb{Z}$, in the uniform state class, the mutual information between V and its complement is bounded by the boundary: $I(V;\,V^c) \le |\partial V| \log_2 q$.*
```

**T-A3-1.2** `papers/SM.md` — source: L-A3 §T-A3-1; mirror at :146 (i)

old:

```text
In the reference state class used by the mod-$q$ proof, the entropy measure scales as $S(V)=\eta\,|\partial V|$ (area-law lemma above); the real Gaussian statement has its own ground-state/regularity hypotheses.
```

new:

```text
In the reference state class used by the mod-$q$ proof, the entropy measure is bounded by the graph boundary, $I(V;\,V^c)\le|\partial V|\log_2 q$ (area-law lemma above); the proportional form $S(V)=\eta\,|\partial V|$ is the real Gaussian statement, with its own ground-state/regularity hypotheses.
```

**T-A3-1.3** `papers/SM.md` — source: L-A3 §T-A3-1; mirror at :156 (i)

old:

```text
proved for Gaussian systems over $\mathbb{R}$ [3] and for any nearest-neighbor dynamics over $\mathbb{Z}/q\mathbb{Z}$ via the spatial Markov property (area-law lemma above).
```

new:

```text
proved for Gaussian systems over $\mathbb{R}$ [3]; for nearest-neighbor dynamics over $\mathbb{Z}/q\mathbb{Z}$ the spatial Markov property gives the boundary bound of the area-law lemma above, not the proportional form.
```

**T-A3-1.4** `papers/SM.md` — source: L-A3 §T-A3-1; mirror at :78

old:

```text
The *area law* follows from the spatial Markov property on any graph with range-1 dynamics.
```

new:

```text
The *area-law bound* — mutual information across a region's boundary at most proportional to the boundary — follows from the spatial Markov property on any graph with range-1 dynamics.
```

**T-A3-1.5** `papers/SM.md` — source: L-A3 §T-A3-1; mirror at :106

old:

```text
the uniform-class Markov area law holds,
```

new:

```text
the uniform-class Markov area-law bound holds,
```

**T-A3-1.6** `book/ch05-gauge-structure.md` — source: L-A3 §T-A3-1; book mirror ch05:37

old:

```text
The *area law* — that entanglement entropy of a region scales as its boundary rather than its volume — follows from the spatial Markov property on any graph with range-1 dynamics.
```

new:

```text
The *area-law bound* — that the information shared across a region's boundary is at most proportional to the boundary rather than the volume — follows from the spatial Markov property on any graph with range-1 dynamics.
```

**T-A3-1.7** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-A3 §T-A3-1; FULL mirror of ch05:37; old and new byte-identical to T-A3-1.6, applied to this file.

### T-A3-2 — CORRECT-IN-PLACE

**T-A3-2.1** `papers/SM.md` — source: L-A3 §T-A3-2 (LEDGER 958–968); guardrail 3

old:

```text
The *area* of a region V is the number of edges crossing from V to its complement.
```

new:

```text
The *graph boundary* $|\partial V|$ of a region V — the quantity the area-law bound below is stated in — is the number of edges crossing from V to its complement.
```

**T-A3-2.2** `book/ch05-gauge-structure.md` — source: L-A3 §T-A3-2; book mirror ch05:37; guardrail 3

old:

```text
The *area* of a region $V \subset S$ is the number of edges crossing from $V$ to its complement.
```

new:

```text
The *graph boundary* $|\partial V|$ of a region $V \subset S$ — the quantity the area-law bound is stated in — is the number of edges crossing from $V$ to its complement.
```

**T-A3-2.3** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-A3 §T-A3-2; FULL mirror of ch05:37; guardrail 3; old and new byte-identical to T-A3-2.2, applied to this file.

### T-A4-1 — CORRECT-IN-PLACE

**T-A4-1.1** `papers/Substratum.md` — source: L-A4 §T-A4-1 (LEDGER 585–593)

old:

```text
The dynamics $\varphi$ does not depend on a choice of "center" site; equivalently, $\varphi$ commutes with lattice translations up to gauge. (Required to derive the wave equation in Stage 2.
```

new:

```text
The dynamics $\varphi$ does not depend on a choice of "center" site, in two senses used below: $\varphi$ commutes with lattice translations up to gauge, and the update at a site contains no explicit copy of that site's present value ([SM §4.1]). (The second sense is what the wave-equation derivation of Stage 2 uses.
```

**T-A4-1.2** `papers/Substratum.md` — source: L-A4 §T-A4-1 (LEDGER 585–593)

old:

```text
(b) *Wave equation.* Center independence (A4), isotropy (E4), and linearity (A5) uniquely select,
```

new:

```text
(b) *Wave equation.* Center independence (A4, in its functional sense: no self-term), isotropy (E4), and linearity (A5) uniquely select,
```

**T-A4-1.3** `papers/Substratum.md` — source: L-A4 §T-A4-1 (LEDGER 585–593)

old:

```text
the unique second-order linear dynamics on a lattice that is translation-invariant, isotropic, and reversible has the form
```

new:

```text
the unique second-order linear dynamics on a lattice that is translation-invariant, isotropic, reversible and free of a self-term has the form
```

**T-A4-1.4** `book/ch02-substratum.md` — source: L-A4 §T-A4-1; book mirror ch02:82

old:

```text
*(A4) Center independence.* The dynamics does not depend on a choice of preferred site or origin; $\varphi$ commutes with lattice translations up to gauge. This is required to derive the wave equation in Stage 2 below.
```

new:

```text
*(A4) Center independence.* The dynamics does not depend on a choice of preferred site or origin: $\varphi$ commutes with lattice translations up to gauge, and the update at a site contains no explicit copy of that site's present value. The second property is what the derivation of the wave equation in Stage 2 below uses.
```

**T-A4-1.5** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-A4 §T-A4-1; FULL mirror of ch02:82; old and new byte-identical to T-A4-1.4, applied to this file.

### T-A6-1 — REMOVE/QUALIFY ASSERTION

**T-A6-1.1** `papers/SM.md` — source: L-A6 §T-A6-1 (LEDGER 741–748)

old:

```text
so $\mathrm{Re\,Tr}(P)$ is gauge-invariant — it is the Wilson plaquette action [4], now derived rather than postulated.
```

new:

```text
so $\mathrm{Re\,Tr}(P)$ is gauge-invariant: the gauge-invariant functional from which the Wilson plaquette action [4] is built. That the link dynamics is governed by this functional is not derived here.
```

**T-A6-1.2** `book/ch05-gauge-structure.md` — source: L-A6 §T-A6-1; book ch05:147

old:

```text
The framework's derivation of local $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ gauge invariance is therefore complete. The gauge group is fixed by the cubic decomposition of the six link directions; the amplitude-scale-invariance argument reduces $\mathrm{U}(n)$ to $\mathrm{SU}(n)$ for $n \geq 2$; background independence promotes the global commutant to a local gauge symmetry; the resulting structure is the Wilson plaquette action, with the link variables $M(\mathbf{n}, \hat{e}_j)$ as the gauge connections. The Standard Model gauge theory is derived rather than postulated, with each step a theorem in the framework's chain.
```

new:

```text
The framework's derivation of local $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ gauge invariance, on the H-link/H-cust branch, is therefore complete at the level of the symmetry. The gauge group is fixed by the cubic decomposition of the six link directions; the amplitude-scale-invariance argument reduces $\mathrm{U}(n)$ to $\mathrm{SU}(n)$ for $n \geq 2$; background independence promotes the global commutant to a local gauge symmetry; the gauge-invariant plaquette functional from which the Wilson action is built follows, with the link variables $M(\mathbf{n}, \hat{e}_j)$ as the gauge connections. What is derived is the gauge symmetry; that the link dynamics is the Wilson action is not derived.
```

**T-A6-1.3** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-A6 §T-A6-1; FULL mirror of ch05:147; old and new byte-identical to T-A6-1.2, applied to this file.

### T-A6-2 — REMOVE/QUALIFY ASSERTION

**T-A6-2.1** `papers/SM.md` — source: L-A6 §T-A6-2 (LEDGER 750–760); §A.30; guardrail 2

old:

```text
**Theorem** (Discrete Einstein equation). *For the state-dependent wave equation on a bounded-degree graph G(x) satisfying constraints (i)–(iii), the Jacobson thermodynamic argument produces:*
```

new:

```text
**Discrete Einstein equation** (conditional; see step (iv) of the proof). *For the state-dependent wave equation on a bounded-degree graph G(x) satisfying constraints (i)–(iii), the Jacobson thermodynamic argument, where its curvature step holds, produces:*
```

**T-A6-2.2** `papers/SM.md` — source: L-A6 §T-A6-2; label consistency at :146 (iv)

old:

```text
and the discrete Einstein theorem above is not established by the cited chain.
```

new:

```text
and the discrete Einstein equation above is not established by the cited chain.
```

**T-A6-2.3** `papers/Substratum.md` — source: L-A6 §T-A6-2; mirror Substratum.md:130

old:

```text
the Einstein theorem of [SM §3.1] is formulated on $G(x)$
```

new:

```text
the discrete Einstein equation of [SM §3.1] is formulated on $G(x)$
```

### R1 — CORRECT-IN-PLACE

**R1.1** `papers/Substratum.md` — source: L-A5 drift R1 (LEDGER 175); SM.md:226–228

old:

```text
with propagation speed $v = \alpha$. The constant $\alpha = 1$ is fixed by relativistic causality with maximum signal speed $c$ realized at the lattice cutoff.
```

new:

```text
with coupling coefficient $\alpha$. The coefficient is neither the propagation speed nor free to be set to $1$: causal support travels at most one lattice edge per update whatever its value, and on the observer-level normalized branch it equals $1/d$ ([SM §4.1, Remark]).
```

**R1.2** `book/ch02-substratum.md` — source: L-A5 drift R1; book ch02:98

old:

```text
propagating with speed $v = \alpha$. The coupling constant $\alpha$ is fixed by relativistic causality with maximum signal speed $c$ realized at the lattice cutoff.
```

new:

```text
with coupling coefficient $\alpha$. The coefficient is not the propagation speed: causal support travels at most one lattice edge per update whatever its value, and on the observer-level normalized branch it equals $1/d$.
```

**R1.3** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-A5 drift R1; FULL mirror of ch02:98; old and new byte-identical to R1.2, applied to this file.

### R2 — CORRECT-IN-PLACE

**R2.1** `papers/Structure.md` — source: L-A5 drift R2 (LEDGER 176); Structure.md:219, Substratum.md:268

old:

```text
OI's [SM §4.1] necessity argument for linearity rests on $q$-gauge invariance ([SM §2.7]): the alphabet size $q$ in $\mathbb{Z}/q\mathbb{Z}$ is gauge, and only linear dynamics produces $q$-independent emergent physics; nonlinear dynamics over $\mathbb{Z}/q\mathbb{Z}$ generically have $q$-dependent emergent physics ($x^2 \bmod 3$ vs $x^2 \bmod 5$ are algebraically distinct), violating the $q$-gauge invariance theorem.
```

new:

```text
OI's [SM §4.1] necessity argument for linearity rests on amplitude-scale gauge (§4.1 above; [Substratum §4]), an adjoined operational input that the $q$-size gauge of [SM §2.7] does not entail. The $q$-gauge invariance theorem adds a consistency statement: nonlinear dynamics over $\mathbb{Z}/q\mathbb{Z}$ generically have $q$-dependent emergent physics ($x^2 \bmod 3$ vs $x^2 \bmod 5$ are algebraically distinct), violating it.
```

### R4 — CORRECT-IN-PLACE

**R4.1** `book/ch02-substratum.md` — source: L-A5 drift R4 (LEDGER 178); Substratum.md:100, :266–268

old:

```text
*(A5) Linearity.* The wave equation governing $\varphi$ is linear. Nonlinear alternatives are not ruled out as theoretical possibilities but would require a separate derivation chain not developed here.
```

new:

```text
*(A5) Linearity.* The wave equation governing $\varphi$ is linear. This is a sharpened stipulation: it is equivalent to amplitude-scale gauge — the unobservability of the absolute field scale — which is an adjoined operational input rather than a theorem; nonlinear alternatives are excluded exactly to the extent that input is assumed, and would otherwise require a separate derivation.
```

**R4.2** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-A5 drift R4; FULL mirror of ch02:84; old and new byte-identical to R4.1, applied to this file.

### R5 — CORRECT-IN-PLACE

**R5.1** `papers/SM.md` — source: L-A5 drift R5 (LEDGER 179)

old:

```text
Each site now carries a K-component vector $\boldsymbol{\phi}(\mathbf{n}, t) \in (\mathbb{Z}/q\mathbb{Z})^K$. The general second-order linear update is
```

new:

```text
Each site carries a K-component vector $\boldsymbol{\phi}(\mathbf{n}, t)$; the update below is stated on the observer-level branch of Corollary 1b, so its components are observer-level field values, not the $\mathbb{Z}/q\mathbb{Z}$ alphabet of the substratum. The general second-order linear update is
```

**R5.2** `book/ch05-gauge-structure.md` — source: L-A5 drift R5; book ch05:101

old:

```text
The matrix $M$ is the substratum's sole free parameter at this level.
```

new:

```text
The matrix $M$ is the sole free parameter of this branch at this level.
```

**R5.3** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-A5 drift R5; FULL mirror of ch05:101; old and new byte-identical to R5.2, applied to this file.

### R6 — CORRECT-IN-PLACE

**R6.1** `book/ch02-substratum.md` — source: L-A2 drift R6 (LEDGER 403); Main.md:62, Substratum.md:94

old:

```text
*(A2) Determinism.* The dynamics $\varphi: S \to S$ is a bijection — deterministic and reversible. This is the input from Lemma 3 of Chapter 1.
```

new:

```text
*(A2) Determinism.* The dynamics $\varphi: S \to S$ is a bijection — deterministic and reversible. Its status is two-part (Chapter 1, Lemma 3): the bijective substratum is a representation choice — the minimal recurrent bijective representative of the hidden dynamics — and injectivity is anchored by a dilemma argument with one structural prong (finiteness and recurrence) and one empirical prong (the observed statistics).
```

**R6.2** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-A2 drift R6; FULL mirror of ch02:78; old and new byte-identical to R6.1, applied to this file.

### R7 — CORRECT-IN-PLACE

**R7.1** `book/ch02-substratum.md` — source: L-A1 drift R7 (LEDGER 565); Main.md:62, :706 (ii)

old:

```text
*(A1) Finiteness.* The configuration space $S$ is finite. This is the input from Lemma 1 of Chapter 1, supported empirically by E3 (the holographic bound implies a finite Hilbert-space dimension cutoff).
```

new:

```text
*(A1) Finiteness.* The configuration space $S$ is finite. Lemma 1 of Chapter 1 delivers finiteness of the observer's distinguishable states; the extension to all of $S$ is a posit, read as the choice of the minimal finite representative and supported by E3 (the holographic bound read as a dimension cutoff).
```

**R7.2** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-A1 drift R7; FULL mirror of ch02:76; old and new byte-identical to R7.1, applied to this file.

### R8 — CORRECT-IN-PLACE

**R8.1** `book/ch09-universality.md` — source: L-A1 drift R8 (LEDGER 566); Substratum.md:92

old:

```text
*A1 (finiteness).* The framework requires finite $|S|$. Matrix models with $N \to \infty$ limits violate this strictly, but for any finite $N$ the bridge is consistent. The bridge would require $N$ to be physically finite — meaning the matrix model is not taken to its continuum limit but is treated as itself the fundamental description. This is a substantive interpretive choice that distinguishes the framework's bridge from standard matrix-model interpretations.
```

new:

```text
*A1 (finiteness).* The framework's representative has finite $|S|$. Matrix models with $N \to \infty$ limits violate this strictly, but for any finite $N$ the bridge is consistent. Since the extension of finiteness beyond the observer's distinguishable states is a choice of representative rather than a further fact (Chapter 2), the bridge requires a finite-$N$ representative — the matrix model not taken to its continuum limit — without asserting that $N$ is physically finite. This distinguishes the framework's bridge from standard matrix-model interpretations.
```

**R8.2** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-A1 drift R8; FULL mirror of ch09:197; old and new byte-identical to R8.1, applied to this file.

### R11 — CORRECT-IN-PLACE

**R11.1** `papers/SM.md` — source: L-A6 drift R11 (LEDGER 729–731, 799); SM.md:100

old:

```text
## 3. Background Independence and the Selection of d = 3
```

new:

```text
## 3. Background Independence as State-Dependent Geometry, and the Selection of d = 3
```

**R11.2** `papers/Explainer.md` — source: L-A6 drift R11; Explainer.md:882

old:

```text
| **Structural foundations** | $d = 3$, coupling graph ontology, $q$-gauge, background independence | Substratum |
```

new:

```text
| **Structural foundations** | $d = 3$, coupling graph ontology, $q$-gauge, background independence (state-dependent geometry) | Substratum |
```

### R12 — CORRECT-IN-PLACE

**R12.1** `papers/Main.md` — source: L-A3 drift R12 (LEDGER 937, 1014)

old:

```text
By the bounded coupling degree of $\varphi$, this round trip stays within $\Sigma_{\text{loc}}(V)$ for $t \leq \tau_S$.
```

new:

```text
By the bounded per-step range of $\varphi$ (its causal cone), this round trip stays within $\Sigma_{\text{loc}}(V)$ for $t \leq \tau_S$.
```

### R13 — CORRECT-IN-PLACE

**R13.1** `papers/SM.md` — source: L-A3 drift R13 (LEDGER 938, 999, 1015)

old:

```text
*Proof.* C1: $G_\varphi$ is connected and V is a proper subgraph, so ∂V ≠ ∅. The wave equation couples nearest neighbors; any edge in ∂V produces non-trivial dynamical coupling.
```

new:

```text
*Proof.* C1: $G_\varphi$ is connected and V is a proper subgraph, so ∂V ≠ ∅; every edge of $G_\varphi$ is a dynamical coupling of φ, so any edge in ∂V produces non-trivial dynamical coupling.
```

### T-E-1 — CORRECT-IN-PLACE

**T-E-1.1** `papers/Substratum.md` — source: L-E T-E-1 (LEDGER 1245, 1282)

old:

```text
(E1) **Unitary quantum mechanics.** The observed physics is quantum mechanical: states are vectors in a complex Hilbert space, time evolution is unitary, observables are self-adjoint operators, measurement outcomes follow the Born rule.
```

new:

```text
(E1) **Unitary quantum mechanics.** The observed physics is described, to the precision tested, by quantum mechanics: states as vectors in a complex Hilbert space, unitary time evolution, self-adjoint observables, Born-rule outcome statistics.
```

### T-E-2 — CORRECT-IN-PLACE

**T-E-2.1** `papers/Substratum.md` — source: L-E T-E-2 (LEDGER 1247, 1283)

old:

```text
This is supported by holographic bounds [1, 2]; the cosmological horizon has finite area so the bound applies.
```

new:

```text
This is a theoretical input — the holographic bounds [1, 2], which are not themselves observed — applied to the cosmological horizon, whose finite area makes the bound apply.
```

**T-E-2.2** `book/ch02-substratum.md` — source: L-E T-E-2; book ch02:60

old:

```text
This is the holographic bound, supported by black-hole thermodynamics and the cosmological horizon's finite entropy.
```

new:

```text
This is the holographic bound — a theoretical bound rather than a direct observation — supported by black-hole thermodynamics and applied to the cosmological horizon.
```

**T-E-2.3** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-E T-E-2; FULL mirror of ch02:60; old and new byte-identical to T-E-2.2, applied to this file.

**T-E-2.4** `book/ch02-substratum.md` — source: L-E T-E-2; book ch02:54 (count phrase)

old:

```text
The reconstruction draws on seven structural facts about observed physics, each well-established by experiment:
```

new:

```text
The reconstruction draws on seven structural inputs about observed physics, six established by experiment and one (E3) a theoretical bound:
```

**T-E-2.5** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-E T-E-2; FULL mirror of ch02:54; old and new byte-identical to T-E-2.4, applied to this file.

### T-E-4 — CORRECT-IN-PLACE

**T-E-4.1** `papers/Substratum.md` — source: L-E T-E-4 (LEDGER 1251, 1285); §A.24

old:

```text
The observed cosmological structure satisfies $\rho_s / \rho_{\text{crit}} \approx 1$ (spatial flatness near critical density).
```

new:

```text
The cosmological parameter inferred from observation under the standard cosmological model satisfies $\rho_s / \rho_{\text{crit}} \approx 1$ (spatial flatness near critical density); it is an inferred quantity, not a directly measured one.
```

**T-E-4.2** `book/ch02-substratum.md` — source: L-E T-E-4; book ch02:68

old:

```text
The observed cosmological structure has spatial flatness near the critical density: $\rho_s / \rho_{\text{crit}} \approx 1$.
```

new:

```text
The cosmological parameter inferred from observation under the standard cosmological model is spatial flatness near the critical density: $\rho_s / \rho_{\text{crit}} \approx 1$.
```

**T-E-4.3** `book/The-Incompleteness-of-Observation-FULL.md` — source: L-E T-E-4; FULL mirror of ch02:68; old and new byte-identical to T-E-4.2, applied to this file.

### Deferred (no textual change)

- **R3** — book/ch09-universality.md:205
- **R9** — book/ch09-universality.md:203
- **R10** — book/ch05-gauge-structure.md:97
- **T-HT1-1** — papers/SM.md:248–252, :274
- **T-E-3** — papers/Substratum.md:84; papers/SM.md:170

### Re-grep phrases (corpus-wide, papers/*.md + book/*.md): predicted count at D → at E

| phrase | D | E |
|---|---|---|
| `establishes the same conclusion` | 1 | 0 |
| `convenience of proof, not a physical restriction` | 1 | 0 |
| `provided the partial-trace machinery` | 1 | 0 |
| `conditional on finite reversible substratum dynamics` | 1 | 0 |
| `excluded by the observed unitarity` | 2 | 0 |
| `observed unitarity of quantum dynamics` | 4 | 0 |
| `scales as $S(V) = \eta` | 1 | 1 |
| `The *area law*` | 3 | 0 |
| `The *area* of a region` | 3 | 0 |
| `translation-invariant, isotropic, and reversible` | 1 | 0 |
| `now derived rather than postulated` | 1 | 0 |
| `is therefore complete.` | 2 | 0 |
| `**Theorem** (Discrete Einstein equation)` | 1 | 0 |
| `discrete Einstein theorem` | 1 | 0 |
| `fixed by relativistic causality` | 3 | 0 |
| `propagation speed $v = \alpha$` | 1 | 0 |
| `rests on $q$-gauge invariance` | 1 | 0 |
| `separate derivation chain not developed here` | 2 | 0 |
| `substratum's sole free parameter` | 2 | 0 |
| `This is the input from Lemma` | 4 | 0 |
| `The framework requires finite $|S|$` | 2 | 0 |
| `physically finite` | 2 | 2 |
| `## 3. Background Independence and the Selection` | 1 | 0 |
| `By the bounded coupling degree of` | 1 | 0 |
| `couples nearest neighbors; any edge` | 1 | 0 |
| `The observed physics is quantum mechanical` | 1 | 0 |
| `supported by holographic bounds` | 1 | 0 |
| `seven structural facts` | 2 | 0 |
| `The observed cosmological structure` | 3 | 0 |

### 3.1 Deferred set (frozen; no textual change)

| Item | Site | Why a correction would require round-2 material |
|---|---|---|
| R3 | book ch09 (A5 restated at visible-sector level) | stating the right level needs the substrate-route / observer-route (Koopman) distinction of L-A5 — the representation architecture |
| R9 | book ch09 (A4 restated as partition-center independence) | separating A4-T / A4-S / A4-P and saying which the book means needs L-A4's four-claim split and the descent theorem framing |
| R10 | book ch05 (substrate A4-S equated with emergent chiral symmetry) | the level crossing can only be stated with the substrate / emergent / observer layering |
| T-HT1-1 | SM.md:248–250, :274 (field-theory observer is OBS-C, a degenerate point of OBS-M) | the correction is the OBS-1 observer-notion separation itself |
| T-E-3 | Substratum.md:84; SM.md:170 (E5's d ≥ 3 inference is Einstein-gravity-specific) | the finding is a Track-II circularity for the GR/SUBSTRATE BRIDGE; stating it is an interpretation, not a correction |

### 3.2 Verification-surface instances (frozen)

The release gate reads two files against the manuscript sources, and the substitutions above move both. Each
consequence is an instance of the same form, applied in S1 together with the substitution that forces it. The
`new` text of V-3 is empty: the entry is removed.

**V-1** `verification/coverage/LEDGER.json` — forced by T-A1-1.1. The census (`tools/proof_census.py`)
fingerprints the statement text of the corollary at `papers/Substratum.md` line 262; the entry
`SUBSTRATUM:C-effective-finiteness-gauge-class-transfer` is re-affirmed on the rewritten corollary with its
mapping unchanged: `kernel` `GAP`, `delta` `not formalized`, no checks. The corollary's claim narrows (the
transfer across the gauge class is stated for what the accessible-timescale transition law expresses); what the
ledger records of it does not change.

old:

```text
      "fingerprint": "9330e1f409e986c0",
```

new:

```text
      "fingerprint": "f7e912991de09137",
```

**V-2** `verification/coverage/LEDGER.json` — forced by T-A3-1 (the area-law lemma at `papers/SM.md` line
118). The lemma is unnamed in the census's sense, so its id is derived from its statement text and moves with
it; the entry keeps its mapping (`GAP`, `not formalized`, no checks). Two instances:

old:

```text
      "id": "SM:L-unnamed-332dde89",
```

new:

```text
      "id": "SM:L-unnamed-ff7b7d06",
```

old:

```text
      "fingerprint": "332dde89a60f07d3",
```

new:

```text
      "fingerprint": "ff7b7d068e326e1f",
```

**V-3** `verification/coverage/LEDGER.json` — forced by T-A6-2.1, which removes the `**Theorem**` header at
`papers/SM.md` line 140. The statement leaves the census; its entry (`GAP`, `not formalized`, no checks, named by
no backlog row and by no `unattached` row) is removed. The ledger's entry count and the census's canonical count
both go from 130 to 129; no document records the count.

old:

```text
    {
      "id": "SM:T-unnamed-f1d3c661",
      "paper": "papers/SM.md",
      "line": 140,
      "kind": "Theorem",
      "label": "",
      "fingerprint": "f1d3c6619bfdb644",
      "area": "sm",
      "assumptions": "see the statement",
      "checks": [],
      "kernel": "GAP",
      "delta": "not formalized",
      "note": ""
    },
```

new: (empty)

**V-4** `verification/lean/edge_rigidity_probe.py` — forced by T-A6-1.1. Guard `R7-A6P`'s sub-check P5
delimits the gauge passage of `papers/SM.md` section 3.1 by the phrase T-A6-1.1 removes; the delimiter becomes
the closing sentence T-A6-1.1 writes, which occurs exactly once in the section at `E`. The passage the sub-check
requires kernel-free is unchanged in extent (the heading through the sentence before the delimiter); every text
the guard pins is unchanged by this round (measured at `CC-1`'s candidate: every pinned passage present, the
delimiter the only failing component).

old:

```text
    _end = _31.find('now derived rather than postulated.')
```

new:

```text
    _end = _31.find('That the link dynamics is governed by this functional is not derived here.')
```

**V-5** `verification/lean/edge_rigidity_probe.py` — the same sub-check's docstring names the old delimiter.

old:

```text
    the word is absent from the gauge passage (the heading through the Wilson action "now derived
    rather than postulated"), and no proof-kernel language appears anywhere in the section. The
```

new:

```text
    the word is absent from the gauge passage (the heading through the plaquette functional, up to
    its closing sentence), and no proof-kernel language appears anywhere in the section. The
```

## 4. Guardrails (frozen)

1. **T-A2-1** (GR.md:669 vs :68–74, stochastic-substratum universality of ħ): narrow the claim to what the
   existing derivation supports — the classical-side microreversibility condition the derivation uses is stated
   as a condition of the result. The Θ-twisted detailed-balance condition of L-A2's replacement obligation
   (A2-GR) is **not** inserted; it stays a ledger obligation until proved.
2. **T-A6-2** (SM.md:140 "Theorem (Discrete Einstein equation)" vs :146 (iv)): remove or downgrade the theorem
   label using the corpus's own qualification at :146 (iv) ("is not established by the cited chain"); the
   derivation stays. The generator / Γ-curvature repair of L-HT2 is **not** introduced.
3. **T-A3-2** (SM.md:146 (i), (iii), |∂V| used as Euclidean area): correct only where the text equates the cubic
   graph-boundary count with isotropic Euclidean area; the Γ-perimeter replacement of L-HT2 is **not** introduced.
   (T-A3-1, the mod-q area-law inequality, is corrected to the inequality its proof gives — a scope correction,
   not a repair.)

## 5. Closure steps (all eight required before landing; each produces a recorded artifact)

1. **Frozen per-item disposition table** — §3, in the preregistration at F.
2. **Governed-path census before editing** — at F: sha256 of every governed file (papers/*.md, *.tex, *.pdf;
   book/*.md, *.tex, *.pdf); recorded in the round's record directory.
3. **Each correction linked to its frozen ledger source** — §3's source column names the ledger entry, section
   and (where applicable) the exact check file; the ledger files' hashes are recorded.
4. **Mirror propagation in the same commit** — for every edited claim: book/ch*.md ↔ FULL.md, companion papers
   that restate it, abstracts/summaries/tables (§A.25 steps 1–4); each mirror is a row of §3.
5. **.tex/.pdf regeneration or explicit governed failure** — `sh ./build.sh <papers…> --book` for every edited
   source; if the toolchain is absent or a package missing, the generated artifacts are flagged STALE in the
   result note and the commit message (AGENTS.md "Constrained-environment caveat"); never left silently stale.
6. **Before/after re-grep counts** — §3's phrases: counts at D and at E for the whole corpus; the surviving
   count must equal the predicted legitimate-use count stated in §3.
7. **§A.32/§A.33 added-lines scan** — the diff's added lines are scanned for the prohibited phrase families
   (meta-commentary, reader instruction, rhetorical parallelism, self-assessment, label-restating, caps emphasis,
   revision-history voice); any hit blocks E.
8. **Claim-surface sweep** — the diff is scanned for every term of the out-of-scope list (§1): EXPOSED, AT-RANK,
   R4-CLOSED, R4, OBS-R, OBS-M, OBS-C, OBS-∞, edge-permutiv*, ORD∞, TRANS, EO, V4′, LIMCLOSE, octahedr*,
   Level 3, 3A, 3B, SELECT, DRIVE, "representation level", "realization", "selection premise", H-T1, H-T2; any
   hit in an added line blocks E.
9. **Verification surfaces** — at E: `tools/coverage_check.py` passes; the census carries the two re-affirmed
   entries at the predicted line and fingerprint and no longer carries the removed one, with 129 canonical
   statements and 129 ledger entries; the probe's new delimiter occurs exactly once in SM.md section 3.1; and
   `verification/lean/edge_rigidity_probe.py` prints `ALL CHECKS PASS`.

Order of work: F designated → census (step 2) → edits per §3 rows, mirrors in the same commit (steps 3–4) →
build (step 5) → re-grep (6) → scans (7–8) → verification surfaces (9) → result note → E.

## 6. Interpretation limits

- The round changes consistency, not correctness: "bands unchanged" (AGENTS.md honesty conventions). Removing an
  overclaim can only hold or lower correctness; nothing here raises it.
- No change to any claim ID, count or ordinal beyond what a listed correction forces; totals are re-grepped
  corpus-wide after any inventory change (§A.30).
- Historical provenance preserved: the working draft is corrected forward; no dated notes, no "formerly"
  (§A.27, §A.30).
- The round does not resolve any ledger replacement obligation; it only makes the manuscript say what the
  ledger found it already supports.

## 7. Stages

- **C1** — `controls.py` is added to the record directory: it embeds §3's substitutions verbatim as declared
  (file, old, new) instances — 60 manuscript instances, 59 distinct old literals, the duplicate being a
  chapter/`FULL.md` pair, and the six verification-surface instances of §3.2 — and validates each instance by itself: its `old` occurs exactly once in its file at `D`, and at `E` its `old` is
  absent and its `new` present, the file equalling `D`'s with exactly those substitutions (and that deferred sites are
  byte-identical to `D`), computes the re-grep counts of §3 and compares them to the predicted `E` column, runs the
  §A.32/§A.33 added-lines scan and the §1 claim-surface sweep over `git diff D` of the governed sources, checks the
  mirror property (every non-blank line of each edited chapter occurs verbatim in `FULL.md`), and checks every
  edited paper's `.tex` `% source-sha256:` stamp against its source, and runs closure step 9's census, ledger and
  delimiter checks. Its blob is recorded in the result note.
- **S1** — the substitutions of §3 are applied, in one commit, to all eleven sources, and with them the six
  verification-surface instances of §3.2 to the ledger and the probe; `sh ./build.sh Substratum
  Main GR SM Structure Explainer Methodology` and `sh ./build.sh --book` regenerate the sixteen built artifacts in
  the same commit; `controls.py` passes; page counts and dropped-glyph reports are recorded.
- **S2** — the result note is added: the closure-step artifacts (§5), the governed-path census at `F` and `E`, the
  before/after re-grep table, the scans' output, the build report. This is candidate `E`.
- Repairs between S1 and S2 may touch only the built artifacts (a rebuild) or `controls.py`'s reporting; a
  substitution that fails to apply is not repaired in text — the item is halted (§1, rule of the round) and the
  round records it.

## 8. Outcomes

- **`CC-2-CORRECTED`** — every substitution of §3 applied, every closure step green, the deferred sites
  byte-identical to `D`.
- **`CC-2-PARTIAL`** — one or more items halted under the rule of the round; the applied subset is listed with
  the halted items and their reasons; closure steps green on the applied subset.
- **`CC-2-HALTED`** — anything else; the round halts under the specification's `S12`.

No outcome changes correctness bands; the result note states "bands unchanged".

## 9. Hazards and design evidence (measured at `D`, before this freeze)

- **Toolchain.** `sh ./build.sh` on the seven papers and the book at `D` reproduces all seven `.tex` files byte for
  byte (pandoc 3.1.3, TeX Live 2023; PDFs differ only in embedded timestamps); page counts 50 / 87 / 82 / 144 /
  98 / 67 / 540 (Substratum / Main / GR / SM / Structure / Explainer / book); no dropped glyph. Regenerated
  artifacts therefore land with the edits without a provisional-PDF caveat.
- **Uniqueness of every `old`.** All 60 substitutions' `old` strings occur exactly once in their file at `D`; no
  `new` string is already present.
- **Re-grep baseline.** The `D` column of §3's table was measured, and the `E` column computed by applying the
  substitutions to a copy; the two surviving counts (`physically finite` 2 → 2, in R8's corrected sentence; `scales
  as $S(V) = \eta` 1 → 1, the real Gaussian statement) are the legitimate uses §A.25 step 4 preserves.
- **Register.** The §A.32/§A.33 phrase families and the mid-sentence caps regex produce 0 hits on the 60 `new`
  texts. No tool implements this scan in the repository; `controls.py` implements it for this round.
- **Mirror gate.** After the substitutions, every non-blank line of the three edited chapters occurs verbatim in
  `FULL.md` (0 missing), so the release gate's `mirror` step holds at `E` by construction.
- **Every check that reads the manuscripts, measured.** `CC-1`'s candidate `E` carried exactly the 60
  substitutions of §3 with the artifacts rebuilt; its exact-head run 37143464345 ran all 32 jobs, and the only
  failures were the release gate's `coverage` step (four findings: the stale corollary fingerprint, the area-law
  lemma's moved id reported as one missing and one orphaned entry, and the removed theorem's orphaned entry) and
  guard `R7-A6P` of `edge_rigidity_probe` (the delimiter alone; every pinned passage present). Every other gate
  step (`voice`, `claims`, `citation`, `duplicate`, `mirror`, `lean-manuscript`, `staleness`, `v3-receipts`, …),
  every other guard and every other probe shard passed on that tree. §3.2 carries exactly those findings'
  consequences, and the predicted `E` tree (that candidate's tree with §3.2 applied) passes `coverage_check`
  (129 canonical statements) and the probe (`ALL CHECKS PASS`) at `D`. Any failure at `E` is a halt, not a
  repair of text.
- **The re-anchored guard still discriminates.** On the predicted `E` tree with the sentence V-4 anchors on
  removed from `papers/SM.md`, `edge_rigidity_probe` fails on `R7-A6P` alone; restoring the sentence restores
  `ALL CHECKS PASS`. The guard's sub-check P5 therefore reads the corrected passage, not an empty span.
- **`controls.py` on the predicted trees.** Its self-test passes (two mutations caught); `--check D` passes at
  `D`; `--check E` passes on the predicted `E` tree, including closure step 9's census, ledger-count, coverage
  and delimiter checks.
- **Line drift noted.** The ledger's SM.md:250 anchor for T-HT1-1 is at SM.md:252; T-HT1-1 is deferred, so no
  edit depends on it.
