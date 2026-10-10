"""CC-2 frozen controls (stage C1). Self-contained: the 60 substitution instances of the preregistration's section 3
are embedded below (EDITS), with the deferred sites, the re-grep phrases and the out-of-scope term list.

usage: controls.py --check D|E [--repo DIR] [--base DIR]
  --check D : every instance's old occurs exactly once in its file, new absent; deferred sites present (D census).
  --check E : every instance's old absent and new present; each governed source equals the base file with exactly its
              instances substituted; deferred sites byte-identical to base; re-grep counts equal the E column; the
              A.32/A.33 added-lines scan and the claim-surface sweep over the diff of governed sources are clean; the
              mirror property holds; every edited paper's .tex source-sha256 stamp matches its .md.
       --self-test : runs D on the base, builds a simulated E in a temporary copy and runs E on it, and checks that a
              mutated copy (one substitution missing; one extra prohibited phrase) fails.
The base is a tree at D (default: the repository's `git show D:` of each file is NOT used; a directory is required).
"""
import sys
import os
import json
import re
import subprocess
import glob
import hashlib
import shutil
import tempfile
import argparse

D_COMMIT = '6d335d0ad7a19092b6a10098afcea162a632a402'  # the CC-2 halted landing on main; filled at drafting
FULL = 'book/The-Incompleteness-of-Observation-FULL.md'
PAPERS = ['Substratum', 'Main', 'GR', 'SM', 'Structure', 'Explainer', 'Methodology']
CHAPTERS = ['book/ch02-substratum.md', 'book/ch05-gauge-structure.md', 'book/ch09-universality.md']
SOURCES = [f'papers/{p}.md' for p in PAPERS] + CHAPTERS + [FULL]
LEDGER = 'verification/coverage/LEDGER.json'
PROBE = 'verification/lean/edge_rigidity_probe.py'
VERIF = [LEDGER, PROBE]   # the two verification surfaces this round governs

# ---- EDITS: embedded verbatim from the preregistration (section 3) ------------------------------------------------
CIP, RQA = 'CORRECT-IN-PLACE', 'REMOVE/QUALIFY ASSERTION'
EDITS = [
 # ---- T-A1-1 ---------------------------------------------------------------------------------------------------
 dict(item='T-A1-1', disp=CIP, file='papers/Substratum.md', source='L-A1 §T-A1-1 (LEDGER 492–512)',
  old="In particular, P-indivisibility — established on the minimal finite representative by recurrence ($\\varphi^N = \\mathrm{id}$, [Main §2.3]) — holds on every member; on infinite-deep-sector members, where recurrence is unavailable, the accessible-timescale backflow lemma ([Main §2.3]) establishes the same conclusion without recurrence. The two routes agree where both apply and jointly cover the orbit; A1's choice of the finite representative is therefore a convenience of proof, not a physical restriction.",
  new="In particular, every statement expressible through the accessible-timescale transition law transfers across the orbit. P-indivisibility at the recurrence scale — established on the minimal finite representative by recurrence ($\\varphi^N = \\mathrm{id}$, [Main §2.3]) — is not such a statement: it holds on the finite members, and on infinite-deep-sector members, where recurrence is unavailable, the accessible-timescale backflow lemma ([Main §2.3]) gives the accessible-window property it states, a different and weaker conclusion. A1's choice of the finite representative is therefore a convenience of proof for accessible-timescale content; recurrence-scale content is stated for the finite representative."),
 dict(item='T-A1-1', disp=CIP, file='papers/Main.md', source='L-A1 §T-A1-1 (LEDGER 492–512)',
  old="consumed here by the recurrence step of §2.3 and by §4.6, whose conclusions accordingly hold on the finite representative and, being boundary-only in content, on every member of the gauge class (the transfer stated and proved as a corollary in the companion substratum construction);",
  new="consumed here by the recurrence step of §2.3 and by §4.6, whose conclusions hold on the finite representative; those expressible through the accessible-timescale transition law hold on every member of the gauge class (the transfer stated and proved as a corollary in the companion substratum construction), while the recurrence-scale conclusion of §2.3 is a statement about the finite representative;"),
 # ---- T-A2-1 (guardrail 1) --------------------------------------------------------------------------------------
 dict(item='T-A2-1', disp=CIP, file='papers/GR.md', source='L-A2 (LEDGER 342, 359–362); guardrail 1',
  old="would still produce (U1)–(U3), and — under H-slope, H-frame and H-Hawking at its horizon — $\\hbar = c^3 \\epsilon^2/(4G)$, $\\epsilon = 2\\,l_p$ and the area law with its $1/4$ coefficient, provided the partial-trace machinery and thermal self-consistency hold.",
  new="would still produce (U1)–(U3). The calibration $\\hbar = c^3 \\epsilon^2/(4G)$, $\\epsilon = 2\\,l_p$ and the area law with its $1/4$ coefficient use in addition, on the classical side, the symmetric detailed-balance rate ratio used above — obtained on the OI branch from microreversibility under the stated time-reversal-even coarse-state condition; for general non-bijective dynamics that ratio is an additional condition, supplied neither by S1–S4 nor by H-slope, H-frame and H-Hawking, and the calibration holds for such a substratum only where it is established, with the partial-trace machinery and thermal self-consistency."),
 dict(item='T-A2-1', disp=CIP, file='papers/GR.md', source='L-A2 (LEDGER 342); guardrail 1',
  old="if in addition H-slope, H-frame and the H-Hawking conditions hold at its horizon, so do (C1$'$)–(C3$'$) with the same numerical content.",
  new="if in addition H-slope, H-frame and the H-Hawking conditions hold at its horizon, together with the symmetric detailed-balance rate ratio used above — obtained on the OI branch under the stated time-reversal-even coarse-state condition, and an additional condition for general non-bijective dynamics — so do (C1$'$)–(C3$'$) with the same numerical content."),
 # ---- T-A2-2 ---------------------------------------------------------------------------------------------------
 dict(item='T-A2-2', disp=CIP, file='papers/Main.md', source='L-A2 (LEDGER 343)',
  old="The characterization theorem is accordingly conditional on finite reversible substratum dynamics — an empirically motivated reconstruction, not a pure derivation.",
  new="The physical reading of the characterization theorem — the identification of nature with a finite reversible substratum — is accordingly conditional on that representation choice, an empirically motivated reconstruction rather than a pure derivation; the law-level equivalence of §3.4 itself holds for every finite-horizon law."),
 # ---- T-A2-3 ---------------------------------------------------------------------------------------------------
 dict(item='T-A2-3', disp=CIP, file='papers/Main.md', source='L-A2 §T-A2-3 (LEDGER 381–387)',
  old="so it is excluded by the observed unitarity of quantum dynamics; a merge that leaves no statistical trace is removable,",
  new="so it is excluded wherever the observed statistics are of that doubly stochastic class under the uniform prior; a merge that leaves no statistical trace is removable,"),
 dict(item='T-A2-3', disp=CIP, file='papers/Main.md', source='L-A2 §T-A2-3 (LEDGER 381–387)',
  old="the first empirical (the observed unitarity of quantum dynamics), the second structural (finiteness and recurrence).",
  new="the first empirical (the observed statistics, in the uniform-prior doubly stochastic scope), the second structural (finiteness and recurrence)."),
 dict(item='T-A2-3', disp=CIP, file='papers/Substratum.md', source='L-A2 §T-A2-3 (LEDGER 381–387); mirror',
  old="a non-injective descent either leaves a statistical trace — excluded by the observed unitarity of quantum dynamics — or leaves none,",
  new="a non-injective descent either leaves a statistical trace — excluded where the observed statistics are of the doubly stochastic class that the uniform-prior marginal of a bijection produces — or leaves none,"),
 dict(item='T-A2-3', disp=CIP, file='papers/Substratum.md', source='L-A2 §T-A2-3 (LEDGER 381–387); mirror',
  old="partly anchored by one empirical input, the observed unitarity;",
  new="partly anchored by one empirical input, the observed statistics in that scope;"),
 dict(item='T-A2-3', disp=CIP, file='papers/Methodology.md', source='L-A2 §T-A2-3 (LEDGER 381–387); mirror',
  old="so such merges are excluded by the *observed unitarity* of quantum dynamics, an evidential input rather than a further axiom.",
  new="so such merges are excluded where the observed statistics are of that doubly stochastic class under the uniform prior, an evidential input rather than a further axiom."),
 dict(item='T-A2-3', disp=CIP, file='papers/Main.md', source='L-A2 §T-A2-3 (LEDGER 381–387); mirror Main.md:706 (iii)',
  old="close the hidden-sector margin using one *empirical* input — the observed unitarity of quantum dynamics — and one structural principle,",
  new="close the hidden-sector margin using one *empirical* input — the observed statistics, in the uniform-prior doubly stochastic scope — and one structural principle,"),
 # ---- T-A3-1 ---------------------------------------------------------------------------------------------------
 dict(item='T-A3-1', disp=CIP, file='papers/SM.md', source='L-A3 §T-A3-1 (LEDGER 944–956)',
  old="*The entanglement entropy of a spatial region V in the wave equation scales as $S(V) = \\eta\\,|\\partial V|$. This holds for both the linear wave equation over $\\mathbb{R}$ and the mod-q wave equation over $\\mathbb{Z}/q\\mathbb{Z}$.*",
  new="*For the linear wave equation over $\\mathbb{R}$, the entanglement entropy of a spatial region V scales as $S(V) = \\eta\\,|\\partial V|$ [3]. For the mod-q wave equation over $\\mathbb{Z}/q\\mathbb{Z}$, in the uniform state class, the mutual information between V and its complement is bounded by the boundary: $I(V;\\,V^c) \\le |\\partial V| \\log_2 q$.*"),
 dict(item='T-A3-1', disp=CIP, file='papers/SM.md', source='L-A3 §T-A3-1; mirror at :146 (i)',
  old="In the reference state class used by the mod-$q$ proof, the entropy measure scales as $S(V)=\\eta\\,|\\partial V|$ (area-law lemma above); the real Gaussian statement has its own ground-state/regularity hypotheses.",
  new="In the reference state class used by the mod-$q$ proof, the entropy measure is bounded by the graph boundary, $I(V;\\,V^c)\\le|\\partial V|\\log_2 q$ (area-law lemma above); the proportional form $S(V)=\\eta\\,|\\partial V|$ is the real Gaussian statement, with its own ground-state/regularity hypotheses."),
 dict(item='T-A3-1', disp=CIP, file='papers/SM.md', source='L-A3 §T-A3-1; mirror at :156 (i)',
  old="proved for Gaussian systems over $\\mathbb{R}$ [3] and for any nearest-neighbor dynamics over $\\mathbb{Z}/q\\mathbb{Z}$ via the spatial Markov property (area-law lemma above).",
  new="proved for Gaussian systems over $\\mathbb{R}$ [3]; for nearest-neighbor dynamics over $\\mathbb{Z}/q\\mathbb{Z}$ the spatial Markov property gives the boundary bound of the area-law lemma above, not the proportional form."),
 dict(item='T-A3-1', disp=CIP, file='papers/SM.md', source='L-A3 §T-A3-1; mirror at :78',
  old="The *area law* follows from the spatial Markov property on any graph with range-1 dynamics.",
  new="The *area-law bound* — mutual information across a region's boundary at most proportional to the boundary — follows from the spatial Markov property on any graph with range-1 dynamics."),
 dict(item='T-A3-1', disp=CIP, file='papers/SM.md', source='L-A3 §T-A3-1; mirror at :106',
  old="the uniform-class Markov area law holds,",
  new="the uniform-class Markov area-law bound holds,"),
 dict(item='T-A3-1', disp=CIP, file='book/ch05-gauge-structure.md', source='L-A3 §T-A3-1; book mirror ch05:37',
  old="The *area law* — that entanglement entropy of a region scales as its boundary rather than its volume — follows from the spatial Markov property on any graph with range-1 dynamics.",
  new="The *area-law bound* — that the information shared across a region's boundary is at most proportional to the boundary rather than the volume — follows from the spatial Markov property on any graph with range-1 dynamics."),
 dict(item='T-A3-1', disp=CIP, file=FULL, source='L-A3 §T-A3-1; FULL mirror of ch05:37',
  old="The *area law* — that entanglement entropy of a region scales as its boundary rather than its volume — follows from the spatial Markov property on any graph with range-1 dynamics.",
  new="The *area-law bound* — that the information shared across a region's boundary is at most proportional to the boundary rather than the volume — follows from the spatial Markov property on any graph with range-1 dynamics."),
 # ---- T-A3-2 (guardrail 3) --------------------------------------------------------------------------------------
 dict(item='T-A3-2', disp=CIP, file='papers/SM.md', source='L-A3 §T-A3-2 (LEDGER 958–968); guardrail 3',
  old="The *area* of a region V is the number of edges crossing from V to its complement.",
  new="The *graph boundary* $|\\partial V|$ of a region V — the quantity the area-law bound below is stated in — is the number of edges crossing from V to its complement."),
 dict(item='T-A3-2', disp=CIP, file='book/ch05-gauge-structure.md', source='L-A3 §T-A3-2; book mirror ch05:37; guardrail 3',
  old="The *area* of a region $V \\subset S$ is the number of edges crossing from $V$ to its complement.",
  new="The *graph boundary* $|\\partial V|$ of a region $V \\subset S$ — the quantity the area-law bound is stated in — is the number of edges crossing from $V$ to its complement."),
 dict(item='T-A3-2', disp=CIP, file=FULL, source='L-A3 §T-A3-2; FULL mirror of ch05:37; guardrail 3',
  old="The *area* of a region $V \\subset S$ is the number of edges crossing from $V$ to its complement.",
  new="The *graph boundary* $|\\partial V|$ of a region $V \\subset S$ — the quantity the area-law bound is stated in — is the number of edges crossing from $V$ to its complement."),
 # ---- T-A4-1 ---------------------------------------------------------------------------------------------------
 dict(item='T-A4-1', disp=CIP, file='papers/Substratum.md', source='L-A4 §T-A4-1 (LEDGER 585–593)',
  old="The dynamics $\\varphi$ does not depend on a choice of \"center\" site; equivalently, $\\varphi$ commutes with lattice translations up to gauge. (Required to derive the wave equation in Stage 2.",
  new="The dynamics $\\varphi$ does not depend on a choice of \"center\" site, in two senses used below: $\\varphi$ commutes with lattice translations up to gauge, and the update at a site contains no explicit copy of that site's present value ([SM §4.1]). (The second sense is what the wave-equation derivation of Stage 2 uses."),
 dict(item='T-A4-1', disp=CIP, file='papers/Substratum.md', source='L-A4 §T-A4-1 (LEDGER 585–593)',
  old="(b) *Wave equation.* Center independence (A4), isotropy (E4), and linearity (A5) uniquely select,",
  new="(b) *Wave equation.* Center independence (A4, in its functional sense: no self-term), isotropy (E4), and linearity (A5) uniquely select,"),
 dict(item='T-A4-1', disp=CIP, file='papers/Substratum.md', source='L-A4 §T-A4-1 (LEDGER 585–593)',
  old="the unique second-order linear dynamics on a lattice that is translation-invariant, isotropic, and reversible has the form",
  new="the unique second-order linear dynamics on a lattice that is translation-invariant, isotropic, reversible and free of a self-term has the form"),
 dict(item='T-A4-1', disp=CIP, file='book/ch02-substratum.md', source='L-A4 §T-A4-1; book mirror ch02:82',
  old="*(A4) Center independence.* The dynamics does not depend on a choice of preferred site or origin; $\\varphi$ commutes with lattice translations up to gauge. This is required to derive the wave equation in Stage 2 below.",
  new="*(A4) Center independence.* The dynamics does not depend on a choice of preferred site or origin: $\\varphi$ commutes with lattice translations up to gauge, and the update at a site contains no explicit copy of that site's present value. The second property is what the derivation of the wave equation in Stage 2 below uses."),
 dict(item='T-A4-1', disp=CIP, file=FULL, source='L-A4 §T-A4-1; FULL mirror of ch02:82',
  old="*(A4) Center independence.* The dynamics does not depend on a choice of preferred site or origin; $\\varphi$ commutes with lattice translations up to gauge. This is required to derive the wave equation in Stage 2 below.",
  new="*(A4) Center independence.* The dynamics does not depend on a choice of preferred site or origin: $\\varphi$ commutes with lattice translations up to gauge, and the update at a site contains no explicit copy of that site's present value. The second property is what the derivation of the wave equation in Stage 2 below uses."),
 # ---- T-A6-1 ---------------------------------------------------------------------------------------------------
 dict(item='T-A6-1', disp=RQA, file='papers/SM.md', source='L-A6 §T-A6-1 (LEDGER 741–748)',
  old="so $\\mathrm{Re\\,Tr}(P)$ is gauge-invariant — it is the Wilson plaquette action [4], now derived rather than postulated.",
  new="so $\\mathrm{Re\\,Tr}(P)$ is gauge-invariant: the gauge-invariant functional from which the Wilson plaquette action [4] is built. That the link dynamics is governed by this functional is not derived here."),
 dict(item='T-A6-1', disp=RQA, file='book/ch05-gauge-structure.md', source='L-A6 §T-A6-1; book ch05:147',
  old="The framework's derivation of local $\\mathrm{SU}(3) \\times \\mathrm{SU}(2) \\times \\mathrm{U}(1)$ gauge invariance is therefore complete. The gauge group is fixed by the cubic decomposition of the six link directions; the amplitude-scale-invariance argument reduces $\\mathrm{U}(n)$ to $\\mathrm{SU}(n)$ for $n \\geq 2$; background independence promotes the global commutant to a local gauge symmetry; the resulting structure is the Wilson plaquette action, with the link variables $M(\\mathbf{n}, \\hat{e}_j)$ as the gauge connections. The Standard Model gauge theory is derived rather than postulated, with each step a theorem in the framework's chain.",
  new="The framework's derivation of local $\\mathrm{SU}(3) \\times \\mathrm{SU}(2) \\times \\mathrm{U}(1)$ gauge invariance, on the H-link/H-cust branch, is therefore complete at the level of the symmetry. The gauge group is fixed by the cubic decomposition of the six link directions; the amplitude-scale-invariance argument reduces $\\mathrm{U}(n)$ to $\\mathrm{SU}(n)$ for $n \\geq 2$; background independence promotes the global commutant to a local gauge symmetry; the gauge-invariant plaquette functional from which the Wilson action is built follows, with the link variables $M(\\mathbf{n}, \\hat{e}_j)$ as the gauge connections. What is derived is the gauge symmetry; that the link dynamics is the Wilson action is not derived."),
 dict(item='T-A6-1', disp=RQA, file=FULL, source='L-A6 §T-A6-1; FULL mirror of ch05:147',
  old="The framework's derivation of local $\\mathrm{SU}(3) \\times \\mathrm{SU}(2) \\times \\mathrm{U}(1)$ gauge invariance is therefore complete. The gauge group is fixed by the cubic decomposition of the six link directions; the amplitude-scale-invariance argument reduces $\\mathrm{U}(n)$ to $\\mathrm{SU}(n)$ for $n \\geq 2$; background independence promotes the global commutant to a local gauge symmetry; the resulting structure is the Wilson plaquette action, with the link variables $M(\\mathbf{n}, \\hat{e}_j)$ as the gauge connections. The Standard Model gauge theory is derived rather than postulated, with each step a theorem in the framework's chain.",
  new="The framework's derivation of local $\\mathrm{SU}(3) \\times \\mathrm{SU}(2) \\times \\mathrm{U}(1)$ gauge invariance, on the H-link/H-cust branch, is therefore complete at the level of the symmetry. The gauge group is fixed by the cubic decomposition of the six link directions; the amplitude-scale-invariance argument reduces $\\mathrm{U}(n)$ to $\\mathrm{SU}(n)$ for $n \\geq 2$; background independence promotes the global commutant to a local gauge symmetry; the gauge-invariant plaquette functional from which the Wilson action is built follows, with the link variables $M(\\mathbf{n}, \\hat{e}_j)$ as the gauge connections. What is derived is the gauge symmetry; that the link dynamics is the Wilson action is not derived."),
 # ---- T-A6-2 (guardrail 2) --------------------------------------------------------------------------------------
 dict(item='T-A6-2', disp=RQA, file='papers/SM.md', source='L-A6 §T-A6-2 (LEDGER 750–760); §A.30; guardrail 2',
  old="**Theorem** (Discrete Einstein equation). *For the state-dependent wave equation on a bounded-degree graph G(x) satisfying constraints (i)–(iii), the Jacobson thermodynamic argument produces:*",
  new="**Discrete Einstein equation** (conditional; see step (iv) of the proof). *For the state-dependent wave equation on a bounded-degree graph G(x) satisfying constraints (i)–(iii), the Jacobson thermodynamic argument, where its curvature step holds, produces:*"),
 dict(item='T-A6-2', disp=RQA, file='papers/SM.md', source='L-A6 §T-A6-2; label consistency at :146 (iv)',
  old="and the discrete Einstein theorem above is not established by the cited chain.",
  new="and the discrete Einstein equation above is not established by the cited chain."),
 dict(item='T-A6-2', disp=RQA, file='papers/Substratum.md', source='L-A6 §T-A6-2; mirror Substratum.md:130',
  old="the Einstein theorem of [SM §3.1] is formulated on $G(x)$",
  new="the discrete Einstein equation of [SM §3.1] is formulated on $G(x)$"),
 # ---- R1 -------------------------------------------------------------------------------------------------------
 dict(item='R1', disp=CIP, file='papers/Substratum.md', source='L-A5 drift R1 (LEDGER 175); SM.md:226–228',
  old="with propagation speed $v = \\alpha$. The constant $\\alpha = 1$ is fixed by relativistic causality with maximum signal speed $c$ realized at the lattice cutoff.",
  new="with coupling coefficient $\\alpha$. The coefficient is neither the propagation speed nor free to be set to $1$: causal support travels at most one lattice edge per update whatever its value, and on the observer-level normalized branch it equals $1/d$ ([SM §4.1, Remark])."),
 dict(item='R1', disp=CIP, file='book/ch02-substratum.md', source='L-A5 drift R1; book ch02:98',
  old="propagating with speed $v = \\alpha$. The coupling constant $\\alpha$ is fixed by relativistic causality with maximum signal speed $c$ realized at the lattice cutoff.",
  new="with coupling coefficient $\\alpha$. The coefficient is not the propagation speed: causal support travels at most one lattice edge per update whatever its value, and on the observer-level normalized branch it equals $1/d$."),
 dict(item='R1', disp=CIP, file=FULL, source='L-A5 drift R1; FULL mirror of ch02:98',
  old="propagating with speed $v = \\alpha$. The coupling constant $\\alpha$ is fixed by relativistic causality with maximum signal speed $c$ realized at the lattice cutoff.",
  new="with coupling coefficient $\\alpha$. The coefficient is not the propagation speed: causal support travels at most one lattice edge per update whatever its value, and on the observer-level normalized branch it equals $1/d$."),
 # ---- R2 -------------------------------------------------------------------------------------------------------
 dict(item='R2', disp=CIP, file='papers/Structure.md', source='L-A5 drift R2 (LEDGER 176); Structure.md:219, Substratum.md:268',
  old="OI's [SM §4.1] necessity argument for linearity rests on $q$-gauge invariance ([SM §2.7]): the alphabet size $q$ in $\\mathbb{Z}/q\\mathbb{Z}$ is gauge, and only linear dynamics produces $q$-independent emergent physics; nonlinear dynamics over $\\mathbb{Z}/q\\mathbb{Z}$ generically have $q$-dependent emergent physics ($x^2 \\bmod 3$ vs $x^2 \\bmod 5$ are algebraically distinct), violating the $q$-gauge invariance theorem.",
  new="OI's [SM §4.1] necessity argument for linearity rests on amplitude-scale gauge (§4.1 above; [Substratum §4]), an adjoined operational input that the $q$-size gauge of [SM §2.7] does not entail. The $q$-gauge invariance theorem adds a consistency statement: nonlinear dynamics over $\\mathbb{Z}/q\\mathbb{Z}$ generically have $q$-dependent emergent physics ($x^2 \\bmod 3$ vs $x^2 \\bmod 5$ are algebraically distinct), violating it."),
 # ---- R4 -------------------------------------------------------------------------------------------------------
 dict(item='R4', disp=CIP, file='book/ch02-substratum.md', source='L-A5 drift R4 (LEDGER 178); Substratum.md:100, :266–268',
  old="*(A5) Linearity.* The wave equation governing $\\varphi$ is linear. Nonlinear alternatives are not ruled out as theoretical possibilities but would require a separate derivation chain not developed here.",
  new="*(A5) Linearity.* The wave equation governing $\\varphi$ is linear. This is a sharpened stipulation: it is equivalent to amplitude-scale gauge — the unobservability of the absolute field scale — which is an adjoined operational input rather than a theorem; nonlinear alternatives are excluded exactly to the extent that input is assumed, and would otherwise require a separate derivation."),
 dict(item='R4', disp=CIP, file=FULL, source='L-A5 drift R4; FULL mirror of ch02:84',
  old="*(A5) Linearity.* The wave equation governing $\\varphi$ is linear. Nonlinear alternatives are not ruled out as theoretical possibilities but would require a separate derivation chain not developed here.",
  new="*(A5) Linearity.* The wave equation governing $\\varphi$ is linear. This is a sharpened stipulation: it is equivalent to amplitude-scale gauge — the unobservability of the absolute field scale — which is an adjoined operational input rather than a theorem; nonlinear alternatives are excluded exactly to the extent that input is assumed, and would otherwise require a separate derivation."),
 # ---- R5 -------------------------------------------------------------------------------------------------------
 dict(item='R5', disp=CIP, file='papers/SM.md', source='L-A5 drift R5 (LEDGER 179)',
  old="Each site now carries a K-component vector $\\boldsymbol{\\phi}(\\mathbf{n}, t) \\in (\\mathbb{Z}/q\\mathbb{Z})^K$. The general second-order linear update is",
  new="Each site carries a K-component vector $\\boldsymbol{\\phi}(\\mathbf{n}, t)$; the update below is stated on the observer-level branch of Corollary 1b, so its components are observer-level field values, not the $\\mathbb{Z}/q\\mathbb{Z}$ alphabet of the substratum. The general second-order linear update is"),
 dict(item='R5', disp=CIP, file='book/ch05-gauge-structure.md', source='L-A5 drift R5; book ch05:101',
  old="The matrix $M$ is the substratum's sole free parameter at this level.",
  new="The matrix $M$ is the sole free parameter of this branch at this level."),
 dict(item='R5', disp=CIP, file=FULL, source='L-A5 drift R5; FULL mirror of ch05:101',
  old="The matrix $M$ is the substratum's sole free parameter at this level.",
  new="The matrix $M$ is the sole free parameter of this branch at this level."),
 # ---- R6 -------------------------------------------------------------------------------------------------------
 dict(item='R6', disp=CIP, file='book/ch02-substratum.md', source='L-A2 drift R6 (LEDGER 403); Main.md:62, Substratum.md:94',
  old="*(A2) Determinism.* The dynamics $\\varphi: S \\to S$ is a bijection — deterministic and reversible. This is the input from Lemma 3 of Chapter 1.",
  new="*(A2) Determinism.* The dynamics $\\varphi: S \\to S$ is a bijection — deterministic and reversible. Its status is two-part (Chapter 1, Lemma 3): the bijective substratum is a representation choice — the minimal recurrent bijective representative of the hidden dynamics — and injectivity is anchored by a dilemma argument with one structural prong (finiteness and recurrence) and one empirical prong (the observed statistics)."),
 dict(item='R6', disp=CIP, file=FULL, source='L-A2 drift R6; FULL mirror of ch02:78',
  old="*(A2) Determinism.* The dynamics $\\varphi: S \\to S$ is a bijection — deterministic and reversible. This is the input from Lemma 3 of Chapter 1.",
  new="*(A2) Determinism.* The dynamics $\\varphi: S \\to S$ is a bijection — deterministic and reversible. Its status is two-part (Chapter 1, Lemma 3): the bijective substratum is a representation choice — the minimal recurrent bijective representative of the hidden dynamics — and injectivity is anchored by a dilemma argument with one structural prong (finiteness and recurrence) and one empirical prong (the observed statistics)."),
 # ---- R7 -------------------------------------------------------------------------------------------------------
 dict(item='R7', disp=CIP, file='book/ch02-substratum.md', source='L-A1 drift R7 (LEDGER 565); Main.md:62, :706 (ii)',
  old="*(A1) Finiteness.* The configuration space $S$ is finite. This is the input from Lemma 1 of Chapter 1, supported empirically by E3 (the holographic bound implies a finite Hilbert-space dimension cutoff).",
  new="*(A1) Finiteness.* The configuration space $S$ is finite. Lemma 1 of Chapter 1 delivers finiteness of the observer's distinguishable states; the extension to all of $S$ is a posit, read as the choice of the minimal finite representative and supported by E3 (the holographic bound read as a dimension cutoff)."),
 dict(item='R7', disp=CIP, file=FULL, source='L-A1 drift R7; FULL mirror of ch02:76',
  old="*(A1) Finiteness.* The configuration space $S$ is finite. This is the input from Lemma 1 of Chapter 1, supported empirically by E3 (the holographic bound implies a finite Hilbert-space dimension cutoff).",
  new="*(A1) Finiteness.* The configuration space $S$ is finite. Lemma 1 of Chapter 1 delivers finiteness of the observer's distinguishable states; the extension to all of $S$ is a posit, read as the choice of the minimal finite representative and supported by E3 (the holographic bound read as a dimension cutoff)."),
 # ---- R8 -------------------------------------------------------------------------------------------------------
 dict(item='R8', disp=CIP, file='book/ch09-universality.md', source='L-A1 drift R8 (LEDGER 566); Substratum.md:92',
  old="*A1 (finiteness).* The framework requires finite $|S|$. Matrix models with $N \\to \\infty$ limits violate this strictly, but for any finite $N$ the bridge is consistent. The bridge would require $N$ to be physically finite — meaning the matrix model is not taken to its continuum limit but is treated as itself the fundamental description. This is a substantive interpretive choice that distinguishes the framework's bridge from standard matrix-model interpretations.",
  new="*A1 (finiteness).* The framework's representative has finite $|S|$. Matrix models with $N \\to \\infty$ limits violate this strictly, but for any finite $N$ the bridge is consistent. Since the extension of finiteness beyond the observer's distinguishable states is a choice of representative rather than a further fact (Chapter 2), the bridge requires a finite-$N$ representative — the matrix model not taken to its continuum limit — without asserting that $N$ is physically finite. This distinguishes the framework's bridge from standard matrix-model interpretations."),
 dict(item='R8', disp=CIP, file=FULL, source='L-A1 drift R8; FULL mirror of ch09:197',
  old="*A1 (finiteness).* The framework requires finite $|S|$. Matrix models with $N \\to \\infty$ limits violate this strictly, but for any finite $N$ the bridge is consistent. The bridge would require $N$ to be physically finite — meaning the matrix model is not taken to its continuum limit but is treated as itself the fundamental description. This is a substantive interpretive choice that distinguishes the framework's bridge from standard matrix-model interpretations.",
  new="*A1 (finiteness).* The framework's representative has finite $|S|$. Matrix models with $N \\to \\infty$ limits violate this strictly, but for any finite $N$ the bridge is consistent. Since the extension of finiteness beyond the observer's distinguishable states is a choice of representative rather than a further fact (Chapter 2), the bridge requires a finite-$N$ representative — the matrix model not taken to its continuum limit — without asserting that $N$ is physically finite. This distinguishes the framework's bridge from standard matrix-model interpretations."),
 # ---- R11 ------------------------------------------------------------------------------------------------------
 dict(item='R11', disp=CIP, file='papers/SM.md', source='L-A6 drift R11 (LEDGER 729–731, 799); SM.md:100',
  old="## 3. Background Independence and the Selection of d = 3",
  new="## 3. Background Independence as State-Dependent Geometry, and the Selection of d = 3"),
 dict(item='R11', disp=CIP, file='papers/Explainer.md', source='L-A6 drift R11; Explainer.md:882',
  old="| **Structural foundations** | $d = 3$, coupling graph ontology, $q$-gauge, background independence | Substratum |",
  new="| **Structural foundations** | $d = 3$, coupling graph ontology, $q$-gauge, background independence (state-dependent geometry) | Substratum |"),
 # ---- R12 ------------------------------------------------------------------------------------------------------
 dict(item='R12', disp=CIP, file='papers/Main.md', source='L-A3 drift R12 (LEDGER 937, 1014)',
  old="By the bounded coupling degree of $\\varphi$, this round trip stays within $\\Sigma_{\\text{loc}}(V)$ for $t \\leq \\tau_S$.",
  new="By the bounded per-step range of $\\varphi$ (its causal cone), this round trip stays within $\\Sigma_{\\text{loc}}(V)$ for $t \\leq \\tau_S$."),
 # ---- R13 ------------------------------------------------------------------------------------------------------
 dict(item='R13', disp=CIP, file='papers/SM.md', source='L-A3 drift R13 (LEDGER 938, 999, 1015)',
  old="*Proof.* C1: $G_\\varphi$ is connected and V is a proper subgraph, so ∂V ≠ ∅. The wave equation couples nearest neighbors; any edge in ∂V produces non-trivial dynamical coupling.",
  new="*Proof.* C1: $G_\\varphi$ is connected and V is a proper subgraph, so ∂V ≠ ∅; every edge of $G_\\varphi$ is a dynamical coupling of φ, so any edge in ∂V produces non-trivial dynamical coupling."),
 # ---- T-E-1 ----------------------------------------------------------------------------------------------------
 dict(item='T-E-1', disp=CIP, file='papers/Substratum.md', source='L-E T-E-1 (LEDGER 1245, 1282)',
  old="(E1) **Unitary quantum mechanics.** The observed physics is quantum mechanical: states are vectors in a complex Hilbert space, time evolution is unitary, observables are self-adjoint operators, measurement outcomes follow the Born rule.",
  new="(E1) **Unitary quantum mechanics.** The observed physics is described, to the precision tested, by quantum mechanics: states as vectors in a complex Hilbert space, unitary time evolution, self-adjoint observables, Born-rule outcome statistics."),
 # ---- T-E-2 ----------------------------------------------------------------------------------------------------
 dict(item='T-E-2', disp=CIP, file='papers/Substratum.md', source='L-E T-E-2 (LEDGER 1247, 1283)',
  old="This is supported by holographic bounds [1, 2]; the cosmological horizon has finite area so the bound applies.",
  new="This is a theoretical input — the holographic bounds [1, 2], which are not themselves observed — applied to the cosmological horizon, whose finite area makes the bound apply."),
 dict(item='T-E-2', disp=CIP, file='book/ch02-substratum.md', source='L-E T-E-2; book ch02:60',
  old="This is the holographic bound, supported by black-hole thermodynamics and the cosmological horizon's finite entropy.",
  new="This is the holographic bound — a theoretical bound rather than a direct observation — supported by black-hole thermodynamics and applied to the cosmological horizon."),
 dict(item='T-E-2', disp=CIP, file=FULL, source='L-E T-E-2; FULL mirror of ch02:60',
  old="This is the holographic bound, supported by black-hole thermodynamics and the cosmological horizon's finite entropy.",
  new="This is the holographic bound — a theoretical bound rather than a direct observation — supported by black-hole thermodynamics and applied to the cosmological horizon."),
 dict(item='T-E-2', disp=CIP, file='book/ch02-substratum.md', source='L-E T-E-2; book ch02:54 (count phrase)',
  old="The reconstruction draws on seven structural facts about observed physics, each well-established by experiment:",
  new="The reconstruction draws on seven structural inputs about observed physics, six established by experiment and one (E3) a theoretical bound:"),
 dict(item='T-E-2', disp=CIP, file=FULL, source='L-E T-E-2; FULL mirror of ch02:54',
  old="The reconstruction draws on seven structural facts about observed physics, each well-established by experiment:",
  new="The reconstruction draws on seven structural inputs about observed physics, six established by experiment and one (E3) a theoretical bound:"),
 # ---- T-E-4 ----------------------------------------------------------------------------------------------------
 dict(item='T-E-4', disp=CIP, file='papers/Substratum.md', source='L-E T-E-4 (LEDGER 1251, 1285); §A.24',
  old="The observed cosmological structure satisfies $\\rho_s / \\rho_{\\text{crit}} \\approx 1$ (spatial flatness near critical density).",
  new="The cosmological parameter inferred from observation under the standard cosmological model satisfies $\\rho_s / \\rho_{\\text{crit}} \\approx 1$ (spatial flatness near critical density); it is an inferred quantity, not a directly measured one."),
 dict(item='T-E-4', disp=CIP, file='book/ch02-substratum.md', source='L-E T-E-4; book ch02:68',
  old="The observed cosmological structure has spatial flatness near the critical density: $\\rho_s / \\rho_{\\text{crit}} \\approx 1$.",
  new="The cosmological parameter inferred from observation under the standard cosmological model is spatial flatness near the critical density: $\\rho_s / \\rho_{\\text{crit}} \\approx 1$."),
 dict(item='T-E-4', disp=CIP, file=FULL, source='L-E T-E-4; FULL mirror of ch02:68',
  old="The observed cosmological structure has spatial flatness near the critical density: $\\rho_s / \\rho_{\\text{crit}} \\approx 1$.",
  new="The cosmological parameter inferred from observation under the standard cosmological model is spatial flatness near the critical density: $\\rho_s / \\rho_{\\text{crit}} \\approx 1$."),
]

# Verification-surface instances (section 3.2): the consequences of the manuscript substitutions on the
# two files the release gate reads against them. V-1..V-3 are the coverage ledger; V-4, V-5 the probe.
VERIF_EDITS = [
 dict(item='V-1', disp='LEDGER', file=LEDGER, source='T-A1-1: the corollary at Substratum.md:262 re-fingerprinted by the census',
  old='      "fingerprint": "9330e1f409e986c0",',
  new='      "fingerprint": "f7e912991de09137",'),
 dict(item='V-2', disp='LEDGER', file=LEDGER, source='T-A3-1: the unnamed area-law lemma at SM.md:118; its id follows its body',
  old='      "id": "SM:L-unnamed-332dde89",',
  new='      "id": "SM:L-unnamed-ff7b7d06",'),
 dict(item='V-2', disp='LEDGER', file=LEDGER, source='T-A3-1: the same lemma, fingerprint',
  old='      "fingerprint": "332dde89a60f07d3",',
  new='      "fingerprint": "ff7b7d068e326e1f",'),
 dict(item='V-3', disp='LEDGER', file=LEDGER, source='T-A6-2: the Theorem header at SM.md:140 is removed, so the statement leaves the census (kernel GAP, no checks, no backlog row)',
  old='    {\n      "id": "SM:T-unnamed-f1d3c661",\n      "paper": "papers/SM.md",\n      "line": 140,\n      "kind": "Theorem",\n      "label": "",\n      "fingerprint": "f1d3c6619bfdb644",\n      "area": "sm",\n      "assumptions": "see the statement",\n      "checks": [],\n      "kernel": "GAP",\n      "delta": "not formalized",\n      "note": ""\n    },\n',
  new=''),
 dict(item='V-4', disp='PROBE', file=PROBE, source='T-A6-1: guard R7-A6P sub-check P5 delimits SM.md section 3.1 by the phrase the correction removes',
  old="    _end = _31.find('now derived rather than postulated.')",
  new="    _end = _31.find('That the link dynamics is governed by this functional is not derived here.')"),
 dict(item='V-5', disp='PROBE', file=PROBE, source='T-A6-1: the docstring of the same sub-check names the old delimiter',
  old='    the word is absent from the gauge passage (the heading through the Wilson action "now derived\n    rather than postulated"), and no proof-kernel language appears anywhere in the section. The',
  new='    the word is absent from the gauge passage (the heading through the plaquette functional, up to\n    its closing sentence), and no proof-kernel language appears anywhere in the section. The'),
]
ALL_EDITS = EDITS + VERIF_EDITS
# predicted census facts at E (tools/proof_census.py): id -> (paper, line, fingerprint); removed ids are absent
CENSUS_AT_E = {
 'SUBSTRATUM:C-effective-finiteness-gauge-class-transfer': ('papers/Substratum.md', 262, 'f7e912991de09137'),
 'SM:L-unnamed-ff7b7d06': ('papers/SM.md', 118, 'ff7b7d068e326e1f'),
}
CENSUS_ABSENT_AT_E = ['SM:T-unnamed-f1d3c661', 'SM:L-unnamed-332dde89']
CANONICAL_AT_D, CANONICAL_AT_E = 130, 129
PROBE_SENTINEL = 'That the link dynamics is governed by this functional is not derived here.'

# re-grep phrases: (phrase, predicted count at D, predicted count at E) over papers/*.md + book/*.md
REGREP = [
 ('establishes the same conclusion', 1, 0), ('convenience of proof, not a physical restriction', 1, 0),
 ('provided the partial-trace machinery', 1, 0),
 ('conditional on finite reversible substratum dynamics', 1, 0),
 ('excluded by the observed unitarity', 2, 0), ('observed unitarity of quantum dynamics', 4, 0),
 ('scales as $S(V) = \\eta', 1, 1), ('The *area law*', 3, 0), ('The *area* of a region', 3, 0),
 ('translation-invariant, isotropic, and reversible', 1, 0),
 ('now derived rather than postulated', 1, 0), ('is therefore complete.', 2, 0),
 ('**Theorem** (Discrete Einstein equation)', 1, 0), ('discrete Einstein theorem', 1, 0),
 ('fixed by relativistic causality', 3, 0), ('propagation speed $v = \\alpha$', 1, 0),
 ('rests on $q$-gauge invariance', 1, 0), ('separate derivation chain not developed here', 2, 0),
 ("substratum's sole free parameter", 2, 0), ('This is the input from Lemma', 4, 0),
 ('The framework requires finite $|S|$', 2, 0), ('physically finite', 2, 2),
 ('## 3. Background Independence and the Selection', 1, 0),
 ('By the bounded coupling degree of', 1, 0), ('couples nearest neighbors; any edge', 1, 0),
 ('The observed physics is quantum mechanical', 1, 0), ('supported by holographic bounds', 1, 0),
 ('seven structural facts', 2, 0), ('The observed cosmological structure', 3, 0),
]

DEFERRED_SITES = {   # (file, exact substring that must be byte-identical at E)
 'R3': ('book/ch09-universality.md', "*A5 (linearity).* The framework's emergent dynamics is linear at the visible-sector level."),
 'R9': ('book/ch09-universality.md', "*A4 (center independence).* The framework's predictions are independent of the choice of partition center."),
 'R10': ('book/ch05-gauge-structure.md', "The exact chiral symmetry of the emergent staggered fermions is equivalent to center independence of the substratum dynamics"),
 'T-HT1-1': ('papers/SM.md', "The statements below are made on the companion realization of (iii), where the Markov part and the resummed kernel coincide"),
 'T-E-3': ('papers/Substratum.md', "This requires $d \\geq 3$, since the Weyl tensor vanishes for $d \\leq 2$."),
}

REGISTER = [r'discipline', r'honest', r'should not be read', r'the reader should', r'neither borrows', r'temptation',
            r'\bnow\b', r'no longer', r'current form', r'corrected form', r'as redefined', r'is now settled',
            r'formerly', r'withdraw', r'earlier draft', r'previously']
CAPS = re.compile(r'(?<![\w$\\{(])[A-Z]{4,}(?![\w}])')
OUT_OF_SCOPE = ['EXPOSED', 'AT-RANK', 'R4-CLOSED', 'OBS-R', 'OBS-M', 'OBS-C', 'OBS-∞', 'edge-permutiv', 'ORD∞', 'TRANS',
                'V4′', 'LIMCLOSE', 'octahedr', 'Level 3', '3A', '3B', 'SELECT', 'DRIVE', 'representation level',
                'selection premise', 'H-T1', 'H-T2', 'energy observability']


def read(p):
    return open(p, encoding='utf-8').read()


def check_D(base):
    errs = []
    for i, e in enumerate(ALL_EDITS):
        s = read(os.path.join(base, e['file']))
        if s.count(e['old']) != 1:
            errs.append(f'D: instance {i} ({e["item"]}, {e["file"]}) old count {s.count(e["old"])} != 1')
        if e['new'] and e['new'] in s:
            errs.append(f'D: instance {i} ({e["item"]}) new already present')
    for k, (f, sub) in DEFERRED_SITES.items():
        if sub not in read(os.path.join(base, f)):
            errs.append(f'D: deferred site {k} not found')
    return errs


def expected_E(base):
    out = {}
    for f in SOURCES + VERIF:
        s = read(os.path.join(base, f))
        for e in ALL_EDITS:
            if e['file'] == f:
                s = s.replace(e['old'], e['new'], 1)
        out[f] = s
    return out


def scan_added(texts, base):
    """A.32/A.33 register scan, caps scan and claim-surface sweep over added text (file, text) pairs."""
    errs = []
    for f, t in texts:
        for p in REGISTER:
            if re.search(p, t):
                errs.append(f'E: register hit {p!r} in added text of {f}: {t[:80]}')
        for m in CAPS.finditer(t):
            errs.append(f'E: caps hit {m.group()} in added text of {f}')
        for term in OUT_OF_SCOPE:
            if term in t:
                errs.append(f'E: out-of-scope term {term!r} in added text of {f}: {t[:80]}')
    return errs


def check_E(repo, base, skip_census=False):
    errs = []
    exp = expected_E(base)
    for f in SOURCES + VERIF:
        s = read(os.path.join(repo, f))
        if s != exp[f]:
            errs.append(f'E: {f} != base with exactly its substitutions')
    for i, e in enumerate(ALL_EDITS):
        s = read(os.path.join(repo, e['file']))
        if e['old'] in s:
            errs.append(f'E: instance {i} ({e["item"]}) old still present')
        if e['new'] and e['new'] not in s:
            errs.append(f'E: instance {i} ({e["item"]}) new absent')
    for k, (f, sub) in DEFERRED_SITES.items():
        if sub not in read(os.path.join(repo, f)):
            errs.append(f'E: deferred site {k} changed')
    # re-grep over the whole corpus
    corpus_D = {f: read(f) for f in glob.glob(os.path.join(base, 'papers/*.md')) + glob.glob(os.path.join(base, 'book/*.md'))}
    corpus_E = {f: read(f) for f in glob.glob(os.path.join(repo, 'papers/*.md')) + glob.glob(os.path.join(repo, 'book/*.md'))}
    for ph, cd, ce in REGREP:
        d = sum(s.count(ph) for s in corpus_D.values())
        ee = sum(s.count(ph) for s in corpus_E.values())
        if (d, ee) != (cd, ce):
            errs.append(f'E: re-grep {ph!r}: D {d} (predicted {cd}), E {ee} (predicted {ce})')
    # added-text scans: once E == base + substitutions holds, the added text is exactly the new strings
    errs += scan_added([(e['file'], e['new']) for e in EDITS], base)   # manuscript text only; V-instances are code and data
    # mirror property
    full = read(os.path.join(repo, FULL))
    for ch in CHAPTERS:
        for l in read(os.path.join(repo, ch)).splitlines():
            if l.strip() and l not in full:
                errs.append(f'E: mirror: line of {ch} not in FULL.md: {l[:80]}')
    # the census at E: the re-affirmed entries, the removed one, the canonical count, and the gate step itself
    if not skip_census:
        try:
            rows = json.loads(subprocess.run([sys.executable, 'tools/proof_census.py', '--json'], cwd=repo,
                                             capture_output=True, text=True, timeout=600).stdout)
            byid = {r['id']: r for r in rows}
            for cid, (paper, line, fp) in CENSUS_AT_E.items():
                r = byid.get(cid)
                if not r or (r['paper'], r['line'], r['fingerprint']) != (paper, line, fp):
                    errs.append(f'E: census {cid}: {None if not r else (r["paper"], r["line"], r["fingerprint"])} != {(paper, line, fp)}')
            for cid in CENSUS_ABSENT_AT_E:
                if cid in byid:
                    errs.append(f'E: census still carries {cid}')
            if len(rows) != CANONICAL_AT_E:
                errs.append(f'E: canonical statements {len(rows)} != {CANONICAL_AT_E}')
            led = json.load(open(os.path.join(repo, LEDGER), encoding='utf-8'))
            if len(led['entries']) != CANONICAL_AT_E:
                errs.append(f'E: ledger entries {len(led["entries"])} != {CANONICAL_AT_E}')
            cov = subprocess.run([sys.executable, 'tools/coverage_check.py'], cwd=repo, capture_output=True, text=True, timeout=900)
            if cov.returncode != 0:
                errs.append('E: coverage_check fails: ' + cov.stdout.strip().splitlines()[-1][:160])
        except Exception as ex:  # the census tools are part of the check; their absence is a failure
            errs.append(f'E: census/coverage tools failed: {ex}')
    sm = ' '.join(read(os.path.join(repo, 'papers/SM.md')).split())
    a = sm.find('### 3.1 Background independence'); b = sm.find('### 3.2 Why d = 3', a)
    if not (0 <= a < b) or sm[a:b].count(PROBE_SENTINEL) != 1:
        errs.append('E: the probe sentinel does not occur exactly once in SM.md section 3.1')
    # staleness stamps
    for p in PAPERS:
        tex = os.path.join(repo, f'papers/{p}.tex')
        if os.path.exists(tex):
            m = re.search(r'% source-sha256: ([0-9a-f]{64})', read(tex))
            h = hashlib.sha256(open(os.path.join(repo, f'papers/{p}.md'), 'rb').read()).hexdigest()
            if not m or m.group(1) != h:
                errs.append(f'E: stale .tex stamp for {p}')
    return errs


def self_test(base):
    e1 = check_D(base)
    tmp = tempfile.mkdtemp()
    for d in ('papers', 'book', 'verification'):
        shutil.copytree(os.path.join(base, d), os.path.join(tmp, d))
    for f, s in expected_E(base).items():
        open(os.path.join(tmp, f), 'w', encoding='utf-8').write(s)
    e2 = [x for x in check_E(tmp, base, skip_census=True) if 'stale .tex' not in x]
    # mutation 1: one substitution missing
    f0 = os.path.join(tmp, EDITS[0]['file'])
    s0 = read(f0)
    open(f0, 'w', encoding='utf-8').write(s0.replace(EDITS[0]['new'], EDITS[0]['old'], 1))
    m1 = [x for x in check_E(tmp, base, skip_census=True) if 'stale .tex' not in x]
    open(f0, 'w', encoding='utf-8').write(s0)
    # mutation 2: the scanner itself, on prohibited added text
    m2 = scan_added([('x', 'The discipline maintained throughout is now settled, MESOSCOPIC, and R4-CLOSED.')], base)
    shutil.rmtree(tmp)
    print(f'SELF-TEST: D errors {len(e1)}; simulated E errors {len(e2)}; mutation-missing caught {len(m1) > 0} ({len(m1)}); '
          f'mutation-register caught {len(m2) > 0} ({len(m2)})')
    ok = not e1 and not e2 and m1 and m2
    print('SELF-TEST', 'OK' if ok else 'FAILED')
    return ok


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', choices=['D', 'E'])
    ap.add_argument('--self-test', action='store_true')
    ap.add_argument('--repo', default='.')
    ap.add_argument('--base', required=True)
    a = ap.parse_args()
    if a.self_test:
        sys.exit(0 if self_test(a.base) else 1)
    errs = check_D(a.base) if a.check == 'D' else check_E(a.repo, a.base)
    for x in errs:
        print(x)
    print(f'CC-2 controls --check {a.check}:', 'OK' if not errs else f'FAILED ({len(errs)})')
    sys.exit(0 if not errs else 1)
