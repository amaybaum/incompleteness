# A6 background independence — adopting the covariance reading and propagating it: CONTROL PLANE

Owner-called, publication-only, written from `main` at
`999f1b5b3c9d6960233a12698d83c1a56a16fe10`, which carries the merged act 12 scope propagation
control plane (#600) and the merged A6 round 1 execution (#596, sealed head
`d0b8c6e83c32a01a586f947c0dfd9618a8b42a91`, merge `4fb0a6052d33193d442dd2a2cb72f64937177291`).
This file is committed alone, in its own pull request, before any manuscript is touched, and the
execution pull request descends from the commit that merges it. **Blob identity is authoritative.**

The round propagates one owner decision and its consequences for the manuscripts, the `ROADMAP`
row, the verification landing page, the census and the guards, and does **no new mathematics**: no
Lean theorem, definition or proof is added, changed or removed. The authoritative inputs are
consumed, not re-adjudicated.

**Notation.** In this file's own prose the four readings are always suffixed — `A6-cov`, `A6-inv`,
`A6-glob`, `A6-sd` — as round 1's rule requires. The bare name appears only inside quotations,
inside frozen replacement text (which is manuscript text, where the owner decision below licenses
it as the name of the adopted meaning), in the row name `P1 — A6`, and in guard, family, directory
and round names.

## The owner decision this round propagates, verbatim and authoritative

> A6 owner decision: confirmed. Adopt A6-cov as the primary publication meaning of A6: local
> internal transformations act covariantly provided the link/coupling data are transformed with
> them. Keep A6-inv as a separate stronger fixed-background invariance condition, not as something
> silently identified with covariance; keep A6-glob as the global specialization/consequence where
> appropriate; and keep A6-sd completely separate as the state-dependent-geometry principle. The
> formal result is especially important here: A6Cov imposes no further equation once the
> link-coupled transformation law is built into the interface—its content is the covariant
> interface itself, whereas fixed-rule A6Inv is genuinely restrictive and even fails on the frozen
> small witness. So the A6 propagation should rewrite the manuscript around covariance rather than
> pretending the old fixed-rule invariance definition and the later "promotion" language were
> already the same thing.

And, earlier in the same direction: "Once chosen, propagate it and remove the GAP."

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Round 1's control plane (the four readings, the least interface, the frozen witnesses) | `verification/programmes/substratum/a6-background-independence/preregistration.md`, blob `afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3` |
| Round 1's result (`D1`–`D4`, the one-directional distinction, what none of it licenses) | `verification/programmes/substratum/a6-background-independence/result.md`, blob `331b1928adde22d5c716a92adb864b523d0c09b8` |
| Round 1's module: `siteAct`, `PreservesPointwise`, `A6Inv`, `A6Glob`, `linkF`, `gaugeLink`, `A6Cov`, sixteen named results | `verification/lean-mathlib/OIBridge/BackgroundIndependence.lean`, blob `5ec9fe52835642724d0685d9b920f613874279d6` |
| The substratum-interface audit (Q1's row for the sixth assumption, `interface-audit.md:106`) and the manuscript-axiom audit (the bare-carrier finding) | `verification/programmes/substratum/interface-audit.md`, blob `e4e0d02bfa67ea428391c0df77ad36f2689b87a3`; `verification/programmes/substratum/manuscript-axiom-audit.md`, blob `53eb9d646c51475553c3df47caec17077ab5471f` |
| The queue row `P1 — A6` (`GAP`) and its section "P1 — A6, and what is and is not already represented" (`ROADMAP.md:42`, `:289–337`), and the label vocabulary (`:22–30`) | `verification/ROADMAP.md`, blob `5aa4235bf895b7c114feff406cc156d117bdb755` |
| The verification landing page | `verification/README.md`, blob `a5fb10e2e83a9493b815ba8d35dbf5e4ed9ea976` |
| The guard file: `R7-A6D` at `:13146–13682`, `_a6d_roadmap_row` at `:13386`, `_a6d_m25` at `:13600`; `_rbr_strong_ancestry` at `:9862`, `_rbr_archive_ancestry` at `:9895` | `verification/lean/edge_rigidity_probe.py`, blob `1c76095343d47832ec75a66e2d34bfa3d18d38bd` |
| The census: family "A6 background independence, round 1: definition and interface audit (substratum)", module `BackgroundIndependence`, `kernel-only`, no anchors (`:860–868`) | `verification/lean-manuscript-census.json`, blob `75dc27bd505bf57fb4a8b2f3e1f34541e3e875b6` |
| The surfaces this round edits, at the start state | `papers/Substratum.md` `0ada99357ffd6f475beb1fab4adaa597dc4eae9d`; `papers/SM.md` `bad76808e6ab708732edcb3c6294236aa052cf34`; `papers/Structure.md` `dd5432d70b2a4ab2238a08ea0f30a5101d6ac898`; `book/ch02-substratum.md` `1744db4e09d03a206bcc1a2fc724281957ca369b`; `book/ch05-gauge-structure.md` `0a5cfb0b23ff605d19ac09efa8efe71a2ea1aa35`; `book/ch09-universality.md` `09a4aa76e06b7199b648a688d993694abe5f7218`; `book/appendix-b-derivations.md` `c395edb358d249a6948b090de5ea96b8300ddab9`; `book/glossary.md` `74a99799ceccefdc3c61baccbd31ac7b49f47afe`; `book/The-Incompleteness-of-Observation-FULL.md` `1b5499fc415295152de4a2f06c791391cf2fde71` |
| The surfaces this round reads and re-pins unchanged | `papers/Main.md` `deedef7a0053c6fa7054cad6bc1f9e5ee6580517`; `papers/Explainer.md` `79d1de2a368af7a239860203f03fb32acc58bc70`; `papers/GR.md` `0258ccb7a5ef02877a01638428ae7ab8ba91bf71`; `papers/Methodology.md` `1d332b0c9256e33861af0ce3b5598091b63d30a1`; `book/ch03-structural-realism.md` `9de441661c3a0e1132724df4aa392010dde8ed8b`; `book/ch04-methodology.md` `dfd00b9817fcdb1febc830b221bc4075a7c5f9a1` |
| The control plane this file is modelled on | `verification/audits/foundations/act12-scope-propagation-audit.md`, blob `1d471eddde3bc0df8b7dbf26ddf642c4af6783b5` (merged as #600) |
| The strengthened chronology mechanism, carried forward by name | `verification/programmes/oi-qm/track-b/act-10-anchor-robustness/preregistration.md`, blob `2e92464dca3809558959d240314dbaf9eaa1c500` |

Line coordinates below refer to these blobs. **The act 12 propagation execution lands before this
round executes** (see the chronology section) and touches `papers/Main.md`, `papers/Explainer.md`,
`book/ch01-observation.md`, `book/ch19-open-problems.md`, `book/glossary.md`, the full-book source,
`verification/README.md`, the census, the guard and the rebuilt binary artifacts. The execution of
this round therefore reads those files at its own base, reports their blobs there, and locates every
frozen passage **by content**, never by the line numbers recorded here; a passage whose quoted text
is not found verbatim at the execution base is a failed round, not a passage to be approximated.

## What is being propagated, in the merged result's own terms

1. **The adopted meaning is `A6-cov`.** `A6Cov N M` on link-coupled rules: for every site-dependent
   transformation `g : ι → AddAut V` and every configuration,
   `linkF N (gaugeLink g M) (g · c) = g · (linkF N M c)`, with the link coupling transported,
   `gaugeLink g M i j = g i ∘ M i j ∘ (g j)⁻¹`, and no pointwise-preservation hypothesis. This is
   the transformation law of `SM.md:112` with the second-order term carried by the leap.
2. **Its content is the interface, not a constraint** (`a6cov_all`, level 2): `∀ N M, A6Cov N M`.
   Once the link-coupled transformation law is built in, no further equation is imposed on the
   rule. **Bounded, as round 1 froze it:** a statement about the frozen `A6Cov` on link-coupled
   rules over a finite alphabet; not "local gauge invariance is trivial"; not a statement about the
   derivation of `SM.md:114` on the complex lift, which is outside the interface.
3. **`A6-inv` is a separate, stronger, fixed-background condition.** `A6Inv F M`: the rule and the
   coupling are held fixed and the transformation acts on the configuration alone. On link-coupled
   rules the distinction is one-directional — `A6-cov` always holds, `A6-inv` sometimes fails, no
   rule satisfies `A6-inv` and fails `A6-cov` — and `A6-inv` is genuinely restrictive: it fails on
   the frozen two-site carrier (`d3b_not_a6inv`); on the constant-coupling rule it is rigid on a
   single edge (`d4a_single_edge`: commutation with the rule and one edge `j ∈ N i` give
   `g i (M₀ v) = M₀ (g j v)`; `d4b_edge_rigidity`: with `M₀` injective and `g` preserving `M₀`
   pointwise, `g i = g j` on every edge), so that a transformation in the pointwise stabilizer
   differing across one edge refutes it (`d4b_not_a6inv_of_nonconstant`); and at the manuscripts'
   symmetric point `M = μ I_6`, where the pointwise stabilizer is everything (`addAut_zmod_smul`),
   it fails (`d4b_symmetric_point`, `d4b_mu_id`). These are the reasons it is not the adopted
   meaning: taken as the definition it would refute the manuscripts' own rule for exactly the
   site-dependent transformations the gauge reading needs.
4. **`A6-glob` is the global specialization and consequence.** `A6-inv ⟹ A6-glob`
   (`a6glob_of_a6inv`); it holds for every constant-coupling rule (`a6glob_constLink`) and at the
   symmetric point, and on `waveSubstratum` (`d2ii_wave_a6glob`), where the singleton-index form
   of `A6-inv` fails at `q = 3` (`d2i_wave_not_a6inv`) — facts about the degenerate form, labelled
   so. It is the global commutant symmetry from which `[SM §3.1]`'s local gauge reading proceeds:
   the specialization of the adopted meaning to transformations constant across the lattice that
   leave the coupling itself unchanged, so that nothing needs transporting.
5. **`A6-sd` is a different principle under a shared name.** The state-dependent coupling graph of
   `SM.md:100` — `s(t+1) = φ_{s(t)}(s(t))`, the graph a function of the configuration — is a
   structural property of a rule family, not an invariance under any group; it is not formalized;
   it is the object the Bell branch's preparation-indexed adjacency uses (`Main.md:392`). It is not
   the structural assumption of `[Substratum §3.1]`, and the manuscripts will say so in place.
6. **The non-licences, verbatim from the merged result and carried forward whole:** nothing says
   the sixth assumption holds of the physical substratum, or fails of it; nothing touches the
   Standard-Model gauge-group derivation — Theorems 5 and 7 of `SM`, H-link, H-cust, the `(3,2,1)`
   decomposition, the condensate stabilizer and the reduction to `SU(3) × SU(2) × U(1)` are neither
   consumed nor judged; the complex-lift covariance of `SM.md:112–114` is **not kernel-checked**;
   nothing is about Track B, `P0`, the fibre-Gram classification or hydrodynamics; whether A4 and
   the sixth assumption overlap (`Substratum.md:104`) is not decided; which of `μ I_6` and the
   block-scalar equivariant object "the cubic-symmetric coupling matrix" denotes is not decided,
   `M` being a parameter of every reading.

The owner's summary of the message, which the manuscripts must carry and not exceed: **the sixth
assumption is covariance with the link data transformed; its content is the covariant interface
itself; the fixed-background invariance is a separate, stronger condition and fails where the
gauge reading needs it not to; the global symmetry is the specialization; the state-dependent graph
is another principle.**

## The `ROADMAP` label — the recommendation, with reasons

**Recommended: `CONDITIONAL`.** The vocabulary (`ROADMAP.md:22–30`) is read literally:

- **`GAP`** — "the formal interface has **no predicate for it at all**" — is false after adoption:
  `A6Cov` is the adopted predicate, defined and proved on the least interface.
- **`DERIVED`** — "Kernel-proved and propagated to the manuscript" — would overclaim. What is
  kernel-proved is that `A6Cov` holds for every link-coupled rule of the interface. Nothing is
  proved of the manuscripts' substratum: `A6Cov` is a predicate of a neighbourhood function and a
  link coupling over a finite alphabet, not of a `Substratum`; no `Substratum` packaging of the
  manuscripts' `K = 6` link-coupled rule exists (round 1's conditional slot 8, unused); the one
  substratum built in the interface, `waveSubstratum`, has a singleton internal index, on which the
  statement is degenerate; and the complex lift on which `[SM §3.1]` conducts the gauge derivation
  — unitary `G(n)`, complex-valued `φ` — is outside the interface by decision. "The substratum
  satisfies A6" is therefore not a kernel statement, and a `DERIVED` row would say it is.
- **`OPEN`** — "no closing construction or theorem" — misdescribes a row that has a closing theorem
  on the interface it is stated on.
- **`EXTERNAL`**, **`INDEPENDENT`**, **`ACTIVE`** do not apply.
- **`CONDITIONAL`** — "Formally present, carrying a named hypothesis this programme has not
  discharged. The manuscript states the hypothesis; the row tracks it." — is exactly true. The
  predicate is formally present and proved. The named, undischarged hypothesis is **that the
  manuscripts' substratum instantiates the link-coupled interface on which `a6cov_all` is stated**:
  in its finite-alphabet half, that the `K = 6` link-coupled rule on `(ℤ/qℤ)^6`, packaged as a
  `Substratum`, is an instance — a packaging job the programme has not done; in its complex-lift
  half, that the covariance of `SM.md:112–114` holds on an interface the programme has not built.
  The manuscripts state the assumption itself, as the covariant interface, and the row tracks what
  separates that statement from a kernel statement about their object.

One point of imperfect fit is recorded so that the owner sees it: the queue's other `CONDITIONAL`
rows carry **physical** hypotheses (H-link, H-state), whereas this row's named hypothesis is one of
**formalization scope**. The label is recommended anyway because it is the only one whose stated
meaning is true of the row; the row text below names the hypothesis explicitly so that nobody reads
the label as a physical premise the manuscripts have added.

**The manuscript-axiom audit's separate finding stands unchanged**: no manuscript-level conjunct of
A1–A6 is a faithful predicate of the **bare operational theory**, which has no distinguished
substratum. That is about a different carrier and is neither touched nor weakened by this round.

## The items, fixed in advance

Every replacement below is frozen as to content; the execution may adjust punctuation and
sentence order only where the surrounding paragraph requires it, and must report any such
adjustment. Manuscript voice throughout: no round numbers, theorem labels, kernel identifiers,
reading suffixes, review history, branch or pull-request language, no dated notes, and no narration
of what an earlier version said. In the manuscripts the adopted meaning is named simply by the
assumption's own label, which the owner decision licenses; the other three readings are named in
words where they appear — "the stronger fixed-background condition" (`A6-inv`), "the global commutant
symmetry" (`A6-glob`), "the state-dependent coupling graph" (`A6-sd`) — and never by suffix.

### Item 1 — `papers/Substratum.md:102`: the definition, rewritten around covariance

The current text asserts `A6-inv` word for word and places the promotion outside the assumption:

> (A6) **Background independence.** The dynamics is invariant under spatially-varying
> internal-index transformations that preserve the cubic-symmetric coupling matrix pointwise. The
> promotion of the resulting global commutant symmetry to local gauge invariance is then a
> derivation step ([SM §3.1]) — not part of the assumption itself.

It is replaced, in place, by:

> (A6) **Background independence.** The dynamics is covariant under spatially-varying
> internal-index transformations: a site-dependent transformation $G(\mathbf{n})$ of the internal
> index is a symmetry of the dynamics provided the coupling data carried on the links are
> transformed with it, $M(\mathbf{n}, \hat{e}_j) \to G(\mathbf{n})\,M(\mathbf{n}, \hat{e}_j)\,G(\mathbf{n}+\hat{e}_j)^{-1}$
> ([SM §3.1]). The content of the assumption is this covariant interface — the coupling is
> link-valued data on which the transformations act — and once it is in place the local
> transformation law imposes no further condition on the rule. A6 is not the stronger
> fixed-background condition that the same transformations leave the dynamics invariant with the
> coupling held fixed and preserved pointwise: for an invertible constant coupling that condition
> forces the transformation to agree across every coupled pair of sites, and at the symmetric point
> of the coupling matrix it fails for every transformation that differs across a coupled pair. The
> global commutant symmetry — the transformations constant across the lattice that leave the
> coupling itself unchanged, the specialization of A6 in which nothing needs transporting — is
> what the local gauge reading of [SM §3.1] proceeds from. The state-dependent coupling graph of
> [SM §3.1], under which the graph itself evolves with the state, is a separate principle that
> shares the name and is not A6.

What each sentence rests on, for the record and not for the manuscript: the first two sentences are
`A6Cov` and `a6cov_all` on the finite-alphabet interface; "agree across every coupled pair of sites"
is `d4a_single_edge` with `d4b_edge_rigidity` (injective constant coupling); "fails for every
transformation that differs across a coupled pair" at the symmetric point is
`d4b_not_a6inv_of_nonconstant` with `d4b_mu_id`; the global commutant symmetry is `A6Glob`; the last
sentence is round 1's `D1` at `SM.md:100`. No sentence of the definition claims anything about the
complex lift.

### Item 2 — `papers/Substratum.md:104`, `:162`, `:220`: the use-sites, made consistent with the definition

- **`:104`** — "A4 (center independence) and A6 (background independence) overlap in physical
  content (A6 promotes the symmetry that A4 constrains)" — is **unchanged**. Under the adopted
  meaning the promotion is what the assumption supplies (round 1's reading (c)), so the sentence's
  verb is consistent with the definition and needs no repair; whether the overlap claim itself
  holds is not this round's and is not touched.
- **`:162`**, Stage 2 step (d), final sentence — "Background independence (A6) then promotes the
  remaining global $SU(3) \times SU(2) \times U(1)$ to local gauge invariance ([SM §3.1])." — is
  replaced by:

  > Background independence (A6) — covariance under site-dependent transformations, the link
  > coupling transformed with them — then promotes the remaining global $SU(3) \times SU(2) \times U(1)$
  > to local gauge invariance ([SM §3.1]).

  Everything else in step (d) is preserved verbatim.
- **`:220`** — "- A6 (background independence) is standard for gauge theories." — is replaced by:

  > - A6 (background independence), as covariance under local internal-index transformations with
  > the link coupling transformed alongside, is the standard gauge-theoretic requirement; the
  > stronger fixed-background invariance, with the coupling held fixed, is a separate condition
  > and is not what A6 asserts.

- **`:132`, `:144`, `:188`, `:190`, `:192`, `:198`, `:204`, `:209`, `:211`, `:222`, `:232`** consume
  A1–A6 by name, as inputs, as a class, or in the exclusion list ("Theories violating center
  independence, linearity, or background independence (violate A4–A6)"), carry no reading, and
  are **unchanged**.

### Item 3 — `papers/SM.md` §3.1: the shared name disambiguated, the transformation law made the content

The heading `SM.md:98` "### 3.1 Background independence" is **kept**: the section is where both
principles live and cross-references to `[SM §3.1]` throughout the corpus depend on it.

- **`:100`** — currently

  > The companion paper [Main] treats the coupling graph as fixed. In general relativity, the
  > spacetime geometry is dynamical. If space is the coupling graph, background independence
  > requires the graph to evolve with the state: s(t+1) = φ_{s(t)}(s(t)), where each φ_s is a
  > bijection but G_{φ_s} varies with s.

  is replaced by:

  > The companion paper [Main] treats the coupling graph as fixed. In general relativity, the
  > spacetime geometry is dynamical. If space is the coupling graph, background independence in
  > the geometric sense — the state-dependent-geometry principle of this section — requires the
  > graph to evolve with the state: s(t+1) = φ_{s(t)}(s(t)), where each φ_s is a bijection but
  > G_{φ_s} varies with s. This principle is not the structural assumption (A6) of
  > [Substratum §3.1], which is covariance of the dynamics under site-dependent internal-index
  > transformations with the link coupling transformed alongside (below); the two share a name and
  > are different requirements, a coupling that depends on the state and a coupling that
  > transforms under a gauge group being different objects.

  `:102`–`:108` (bijectivity automatic; the three constraints; the ring construction) are
  preserved verbatim: they are `A6-sd`'s own content and the round does not touch it.
- **`:110`** — currently "… Background independence is then the premise promoting the surviving
  global stabilizer to the local gauge reading developed below. …" — the middle sentence is
  replaced by:

  > Background independence in the sense of (A6) — covariance under site-dependent
  > transformations with the link coupling transformed alongside — is then the premise carrying
  > the surviving global stabilizer to the local gauge reading developed below.

  The paragraph's heading, its H-link + H-cust scoping and its closing sentence ("Without H-link,
  Theorem 7 remains a theorem about geometric links rather than a proof of the physical gauge
  carrier.") are preserved verbatim. The conditional carrier reading is not weakened or
  strengthened.
- **`:112`** — the transformation law
  $\phi(\mathbf{n}) \to G(\mathbf{n})\,\phi(\mathbf{n}), \quad M(\mathbf{n}, \hat{e}_j) \to G(\mathbf{n})\,M(\mathbf{n}, \hat{e}_j)\,G(\mathbf{n}+\hat{e}_j)^{-1}$
  — is preserved verbatim: under the adopted meaning it **is** the content of the assumption.
- **`:114`** — currently begins "The wave equation is invariant. This is local gauge invariance.
  The link variable $M(\mathbf{n}, \hat{e}_j)$ transforms as a gauge connection: …". The first two
  sentences are replaced by:

  > The wave equation is carried to itself: this is the covariance that (A6) asserts, and once the
  > link variable is data transported in this way the local transformation law imposes no further
  > condition on the rule. This is local gauge invariance.

  The remainder of `:114` (the connection, the plaquette, the adjoint transformation, the Wilson
  action "now derived rather than postulated") is preserved verbatim.

**What this does and does not say about the kernel.** The covariance identity on the complex lift
is the manuscript's own elementary computation and is stated as mathematics in manuscript voice;
**it is not kernel-checked**, and no sentence frozen here implies that it is: `a6cov_all` is a
statement about the frozen `A6Cov` on link-coupled rules over a finite alphabet, and the complex
lift — unitary `G(n)`, complex-valued `φ`, the condensate — is outside the interface by round 1's
decision. The manuscripts carry no kernel citations (manuscript voice), and the census anchors of
Item 8 are placed on the finite-alphabet definition and its book mirror, never on §3.1's complex-lift
sentences, so that the registry does not assert coverage the kernel does not have.

- **`:36`** ("§3 establishes background independence …"), **`:338`**, **`:368`**, **`:1456`**
  ("amplitude-scale-gauge/background-independence premises"; "the condensate-stabilizer/
  background-independence route") name the premise without asserting a reading and are
  **unchanged**; `:36` uses the section's geometric sense, which `:100` disambiguates in place.

### Item 4 — `papers/Structure.md` §6.6 and the other papers

- **`Structure.md:311`** — the clause "OI's A6 requires invariance under local *spatial*
  transformations, but BFSS has no spatial structure beyond the matrix index" is replaced by
  "OI's A6 requires covariance under spatially varying internal-index transformations, with the
  link coupling transformed alongside, but BFSS has no spatial structure beyond the matrix index";
  the rest of `:311`, including "Whether matrix-internal gauge invariance plays the role A6 requires
  depends on the matrix-spatial bridge", is preserved verbatim. `:136` (the list, name only),
  `:324` (the tally row) and every other mention are **unchanged**.
- **`papers/Main.md`** is read, not edited: `:358` defines the coupling graph by one-step
  dependency and `:392` cites `[SM §3.1]`'s state-dependent graph for preparation-indexed
  adjacency; neither carries a reading of the sixth assumption, and after Item 3 the graph they
  cite is named in `SM.md` as the state-dependent-geometry principle. Re-pinned unchanged.
- **`papers/GR.md:669`** ("A6 (background independence) is required for the SM gauge-group
  derivation but not for the partition-geometry results"), `:260`, `:342`;
  **`papers/Methodology.md:339`, `:345`, `:367`, `:369`** (the A1–A6 class); **`papers/Explainer.md:882`**
  (the table row, name only) carry no reading and are re-pinned unchanged.
- **`papers/Explainer.md:813`** — "Background independence is achieved through state-dependent
  bijections, with the discrete Einstein equation identified as the Ollivier-Ricci curvature
  condition." — is **left unchanged**: it names the state-dependent-geometry principle of `SM.md`
  §3.1 in that section's own sense, does not attach the assumption's label to it, and after Item 3
  the section it summarizes says in place that the two principles are different. It does not
  conflict with the adopted meaning.

### Item 5 — Book: Chapter 2's definition, Chapter 5 §5.5, Chapter 9, Appendix B

- **`book/ch02-substratum.md:86`** — currently

  > *(A6) Background independence.* The dynamics is invariant under spatially varying
  > internal-index transformations that preserve the coupling structure pointwise. The promotion
  > of the resulting global symmetry to local gauge invariance is a derivation step rather than an
  > assumption.

  is replaced, in parallel with Item 1, by:

  > *(A6) Background independence.* The dynamics is covariant under spatially varying
  > internal-index transformations: a site-dependent transformation of the internal index is a
  > symmetry provided the coupling data carried on the links are transformed with it. The content
  > of the assumption is this covariant interface — the coupling is link-valued data on which the
  > transformations act — and once it is in place the local transformation law imposes no further
  > condition on the rule. It is not the stronger fixed-background condition that the same
  > transformations leave the dynamics invariant with the coupling held fixed, which for an
  > invertible constant coupling forces the transformation to agree across every coupled pair of
  > sites and fails at the symmetric point of the coupling matrix for every transformation that
  > differs across a coupled pair; the global commutant symmetry — the transformations constant
  > across the lattice that leave the coupling unchanged — is the specialization from which the
  > local gauge reading of Chapter 5 proceeds. The state-dependent coupling graph, under which the
  > graph itself evolves with the state, is a separate principle that shares the name.

  `:94`, `:102` ("Background independence (A6) then promotes the global … to local gauge
  invariance" — the promotion verb, licensed as in Item 2), `:118`, `:122` are **unchanged**.
- **`book/ch05-gauge-structure.md:141`** — the paragraph's last sentence, "The promotion from
  global to local gauge invariance is performed by the framework's commitment to background
  independence.", is replaced by:

  > The step from global to local is what background independence (A6) supplies: the local
  > transformations act covariantly once the coupling data on the links are transformed with them.

  The paragraph's first two sentences are preserved verbatim.
- **`book/ch05-gauge-structure.md:143`** — the whole paragraph, which currently identifies the
  assumption with a state-dependent coupling ("Background independence, established in the
  framework's prior content, requires the coupling structure to be dynamical rather than fixed: the
  coupling matrix $M$ depends on the state …"), is replaced by:

  > Background independence, as the reconstruction's assumption A6 states it, is a covariance
  > requirement: a site-dependent internal-index transformation is a symmetry of the dynamics
  > provided the coupling data on the links are transformed with it. It is not the requirement
  > that the coupling structure be held fixed and left invariant — for an invertible coupling that
  > stronger fixed-background condition holds only for transformations that agree across every
  > coupled pair of sites — and it is not the state-dependent coupling graph $G(x)$ on which the
  > Bell branch of Chapter 1 rests, under which the graph itself evolves with the state; those are
  > different principles that share a name. The matrix structure at each site has eigenvalue
  > multiplicities $(3, 2, 1)$ because spatial isotropy holds locally, and the coupling on each
  > link, $M(\mathbf{n}, \hat{e}_j)$, is the data the site-dependent transformations act on; the
  > commutant $\mathrm{U}(3) \times \mathrm{U}(2) \times \mathrm{U}(1)$ acts at each site, and the
  > resulting gauge transformations are site-dependent.

- **`book/ch05-gauge-structure.md:145`** — the transformation law and the plaquette — is preserved
  verbatim: it is the covariance statement. **`:147`** ("background independence promotes the
  global commutant to a local gauge symmetry") is preserved verbatim, the promotion verb being
  licensed. `:13`, `:17`, `:19`, `:133`, `:153`, `:194`, `:196` name the premise and are
  **unchanged**.
- **`book/ch09-universality.md:207`** — currently uses the words in a third sense (no fixed
  spacetime background): "*A6 (background independence).* The framework operates in a
  background-independent way — the substratum is the background, with spacetime emergent. Matrix
  models with explicit background spacetime are not background-independent in this sense; the
  bridge would require the matrix model to be of background-independent form (BFSS in its M-theory
  interpretation, for instance, where spacetime emerges from the matrix dynamics)." Left as it
  stands, the item would attribute the emergent-spacetime sense to the assumption. It is replaced
  by:

  > *A6 (background independence).* The framework's assumption is covariance under spatially
  > varying internal-index transformations, with the link coupling transformed alongside;
  > separately, the framework has no fixed spacetime background — the substratum is the
  > background, with spacetime emergent — and that is a different sense of the same words. Matrix
  > models with explicit background spacetime are not background-independent in the
  > emergent-spacetime sense; the bridge would require the matrix model to be of
  > background-independent form (BFSS in its M-theory interpretation, for instance, where
  > spacetime emerges from the matrix dynamics), and whether its matrix-internal gauge covariance
  > then plays the role the assumption requires depends on that matrix-spatial bridge.

  This keeps the item's matrix-model content and its verdict, in agreement with `Structure.md`
  §6.6 after Item 4.
- **`book/appendix-b-derivations.md:317`** — the parenthetical gloss "Background independence — the
  requirement that the dynamics be invariant under local choices of basis within each eigenspace —
  promotes this global commutant to local gauge invariance." is replaced by:

  > Background independence — covariance of the dynamics under site-dependent choices of basis
  > within each eigenspace, the link coupling transforming with them — promotes this global
  > commutant to local gauge invariance.

  `:327` ("(iv) Background independence promotes the global commutant to local gauge invariance.")
  is **unchanged**.
- **`book/ch03-structural-realism.md:34`, `:44`, `:74`, `:78`; `book/ch04-methodology.md:10`,
  `:22`, `:26`, `:28`; `book/ch06-matter-content.md:8`** name the assumption or the promotion and
  carry no reading; **unchanged**, re-pinned.
- **`book/The-Incompleteness-of-Observation-FULL.md`** mirrors every changed book passage byte for
  byte (at the start-state blob: `:727` for Chapter 2, `:1466` and `:1468` for Chapter 5, `:2677`
  for Chapter 9, `:6074` for Appendix B, and the glossary section beginning at `:6549`; located by
  content at the execution base).

### Item 6 — Glossary

`book/glossary.md` gains one entry, between **Axiom 2 (Finiteness).** and **Barandes
correspondence.**, in the glossary's house style (bold term, definition in manuscript voice,
"Developed in …"):

> **Background independence (A6).** The sixth of the framework's structural assumptions A1–A6:
> the substratum dynamics is covariant under spatially varying internal-index transformations, a
> site-dependent transformation being a symmetry provided the coupling data carried on the links
> are transformed with it. The content of the assumption is the covariant interface itself — the
> coupling is link-valued data the transformations act on — and once that is in place the local
> transformation law imposes no further condition on the rule. It is distinct from the stronger
> fixed-background condition that the same transformations leave the dynamics invariant with the
> coupling held fixed, which for an invertible coupling forces agreement across every coupled pair
> of sites; from the global commutant symmetry, its specialization to transformations constant
> across the lattice that leave the coupling unchanged, from which the local gauge reading
> proceeds; and from the state-dependent coupling graph, a separate principle sharing the name,
> under which the graph itself evolves with the state. Where the framework says it has no fixed
> spacetime background, with spacetime emergent, that is a third sense of the words and not this
> assumption. Developed in Chapter 2 §2.4 and Chapter 5 §5.5.

The entry is mirrored in the full-book source's glossary section.

### Item 7 — `verification/ROADMAP.md`: the row and the section

**The row** (`ROADMAP.md:42`) is replaced by exactly this line:

```
| **P1** | A6 — background independence / local gauge covariance | Substratum | **CONDITIONAL** — the adopted meaning is covariance, `A6Cov`, which holds identically on every link-coupled rule of the least interface (`a6cov_all`), so its content is the covariant interface and not a constraint; the named hypothesis is that the manuscripts' substratum instantiates that interface: the `K = 6` link-coupled rule is not packaged as a `Substratum` (the interface's `waveSubstratum` has a singleton internal index) and the complex lift on which `[SM §3.1]` conducts the gauge derivation is outside the interface; `A6-inv` is a separate, stronger fixed-background condition, refuted on the frozen two-site carrier and at the symmetric point `M = μ I_6` (`d3b_not_a6inv`, `d4b_mu_id`); `A6-glob` its global specialization (`a6glob_of_a6inv`); `A6-sd` a different principle under a shared name | the complete A1–A6 formal package |
```

**The section** "P1 — A6, and what is and is not already represented" (`ROADMAP.md:289–337`) is
replaced in full by the following; the two attached qualifications and the bare-carrier paragraph
are carried over verbatim from the current section.

> ### P1 — A6, and what is and is not already represented
>
> **The adopted meaning is covariance.** By owner decision, propagated to the manuscripts by the
> round linked below, the sixth structural assumption means `A6-cov`: local internal-index
> transformations act covariantly provided the link coupling is transformed with them,
> `gaugeLink g M i j = g i ∘ M i j ∘ (g j)⁻¹`. `BackgroundIndependence.lean` states it on
> link-coupled rules, `A6Cov N M`, and proves it for every neighbourhood function and link
> coupling (`a6cov_all`): once the link-coupled transformation law is built into the interface no
> further equation is imposed on the rule, so its content is the covariant interface itself, not
> a constraint. The definition at `Substratum.md:102`, the use-sites that say the assumption
> "promotes" the global symmetry to local gauge invariance, and the transformation law of
> `SM.md:112–114` are one reading and are written as one.
>
> **Why the row is `CONDITIONAL`, and neither `DERIVED` nor `GAP`.** The predicate exists and is
> proved, so the row is not a gap. Nothing is proved of the manuscripts' substratum, so the row is
> not derived: `A6Cov` is a predicate of a neighbourhood function and a link coupling over a
> finite alphabet, not of a `Substratum`; no `Substratum` packaging of the manuscripts' `K = 6`
> link-coupled rule exists (round 1's conditional slot 8, unused), and the one substratum built in
> the interface, `waveSubstratum`, has a singleton internal index, on which the statement is
> degenerate; and the complex lift on which `[SM §3.1]` conducts the gauge derivation — unitary
> `G(n)`, complex-valued `φ` — is outside the interface by decision. The named hypothesis the row
> carries is that the manuscripts' substratum — the `K = 6` link-coupled rule on `(ℤ/qℤ)^6` and
> its complex lift — instantiates the link-coupled interface on which `a6cov_all` is stated.
> Discharging the first half is a packaging job on the finite alphabet; the second needs an
> interface the programme has not built. Until then "the substratum satisfies A6" is a manuscript
> assumption with a formal predicate behind it, not a kernel statement about the manuscripts'
> object, and the covariance of `SM.md:112–114` on the complex lift is not kernel-checked.
>
> **The three readings that are not the adopted one, kept distinct.** `A6-inv` (`A6Inv F M`),
> invariance of a fixed rule under site-dependent transformations preserving the site coupling
> pointwise, is a separate and strictly stronger fixed-background condition — no rule satisfies
> `A6-inv` and fails `A6-cov` — and it is genuinely restrictive: it fails on the frozen two-site
> link-coupled carrier (`d3b_not_a6inv`); on the constant-coupling rule it is rigid on a single
> edge (`d4a_single_edge`, `d4b_edge_rigidity`), so that a transformation in the pointwise
> stabilizer differing across one edge refutes it (`d4b_not_a6inv_of_nonconstant`); and at the
> manuscripts' symmetric point `M = μ I_6` it fails (`d4b_symmetric_point`, `d4b_mu_id`). That is
> why it is not the adopted meaning: as the definition it would refute the manuscripts' own rule
> for exactly the site-dependent transformations the gauge reading needs. The manuscripts name it
> as a separate condition that the assumption does not assert. `A6-glob` (`A6Glob F M`), the
> constant-`g` specialization (`a6glob_of_a6inv`), holds for every constant-coupling rule
> (`a6glob_constLink`), at the symmetric point, and on `waveSubstratum` (`d2ii_wave_a6glob`,
> beside the degenerate singleton-index `A6-inv` failing at `q = 3`, `d2i_wave_not_a6inv`, facts
> about the degenerate form and labelled so); it is the global commutant symmetry from which
> `[SM §3.1]`'s local reading proceeds, the specialization of the adopted meaning to
> transformations constant across the lattice that leave the coupling unchanged. `A6-sd`, the
> state-dependent coupling graph of `SM.md:100`, is a structural property of a rule family and not
> an invariance under any group; it is not formalized, it is the object the Bell branch's
> preparation-indexed adjacency uses, and `SM.md` §3.1 says in place that it is a different
> principle under a shared name.
>
> `SubstratumInterfaceAudit.lean` carries a `Substratum` structure holding the manuscript
> substrate data, and against it: **A1, A2 and A5 stated outright; A3 with the degree as a
> parameter and in family form; A4 with the gauge as a parameter**; the sixth assumption's
> predicate lives in `BackgroundIndependence.lean`, on the link-coupled interface, and not on
> `Substratum`. The manuscripts' discrete wave rule is an instance, `waveSubstratum`, satisfying
> A1–A5 as stated.
>
> **Two qualifications this row keeps attached, because dropping either would overstate the
> position.** A3's single-lattice form is vacuous — `a3_of_fintype` bounds the degree by the site
> count — so A3's content is the family form, not the per-lattice one. And A4 is carried up to a
> gauge parameter, with the exact form recovered at trivial gauge.
>
> **A separate and still-true statement, about a different carrier.** `ManuscriptAxioms.lean`
> records that no manuscript-level conjunct of A1–A6 is a faithful predicate of the **bare
> operational theory**, which has no distinguished substratum: there A1 and A2 have realized-core
> *images*, and images are not the axioms. That finding is about the operational interface; the
> paragraphs above are about the substratum structure. Both hold, of different objects.
>
> → [`MANUSCRIPT-AXIOM-AUDIT.md`](programmes/substratum/manuscript-axiom-audit.md),
> [`SUBSTRATUM-INTERFACE-AUDIT.md`](programmes/substratum/interface-audit.md),
> [`lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`](lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean),
> [`lean-mathlib/OIBridge/BackgroundIndependence.lean`](lean-mathlib/OIBridge/BackgroundIndependence.lean)
> → [A6 round 1 result](programmes/substratum/a6-background-independence/result.md) (`D1`–`D4`, the
> one-directional distinction, the degenerate form labelled so, and what none of it licenses)
> → [A6 round 1 preregistration](programmes/substratum/a6-background-independence/preregistration.md)
> (the four readings, the least interface, the frozen witnesses, and the twelve hazards)
> → [A6 covariance propagation](audits/foundations/a6-covariance-propagation-audit.md) (the owner
> decision, the frozen manuscript wording, the label's reasons, and the named hypothesis)

No other `ROADMAP` row, section or research status is edited.

### Item 8 — Verification landing page, census, guards and generated surfaces, in the same execution commit

- **`verification/README.md` — current state.** Add the round, in the existing propagation-round
  style, immediately before the paragraph that begins "`.github/workflows/verify.yml` runs" (and
  therefore after the act 12 propagation paragraph where that has landed), with this content, the
  first sentence's blob, commit and base filled in from the record:

  > The substratum A6 covariance propagation (`audits/foundations/a6-covariance-propagation-audit.md`,
  > preregistration blob `<blob>`, committed alone as `<commit>`, written from `main` at
  > `999f1b5`) is publication-only and owner-called. It adopts `A6-cov` as the publication meaning
  > of the sixth structural assumption — local internal-index transformations act covariantly
  > provided the link coupling is transformed with them — and rewrites the manuscripts' definition
  > around it: `Substratum.md`'s definition of the sixth assumption states the covariant interface and that the local
  > transformation law imposes no further condition on the rule once the coupling is link-valued
  > data; names the stronger fixed-background invariance as a separate condition the assumption
  > does not assert, with its rigidity across every coupled pair of sites and its failure at the
  > symmetric point; names the global commutant symmetry as the specialization the local gauge
  > reading proceeds from; and names the state-dependent coupling graph of `SM.md` §3.1 as a
  > different principle under a shared name, which `SM.md` §3.1 says in place. `SM.md` §3.1's
  > transformation law is written as the content of the assumption and its invariance as the
  > covariance identity, with no claim that the complex-lift statement is kernel-checked:
  > `a6cov_all` is on the finite-alphabet link-coupled interface and the complex lift is outside
  > it. Chapter 2, Chapter 5 §5.5, Chapter 9, Appendix B and the glossary carry the same meaning
  > at their level, mirrored in the full-book source, and `Structure.md` §6.6 states the
  > assumption as covariance. The `ROADMAP` row `P1 — A6` carries `CONDITIONAL` in place of `GAP`:
  > the predicate `A6Cov` exists and holds identically on link-coupled rules, and the named
  > undischarged hypothesis is that the manuscripts' substratum — the `K = 6` link-coupled rule,
  > not packaged as a `Substratum`, and its complex lift, outside the interface — instantiates that
  > interface; not `DERIVED`, because nothing is proved of the manuscripts' object. The historical
  > round records that describe the gap as it stood — the substratum-interface round, the
  > frozen-sourcing and stochastic-interface rounds, the interface audit's Q1 table and round 1's
  > own record — are untouched. The census family moves to `current` with the anchors the round
  > creates. `R7-A6D`'s row contract is re-pinned to the new row and its label mutation to a
  > `DERIVED` overclaim, and nothing else in it changes. Nothing about the Standard-Model
  > gauge-group derivation, Track B, `P0` or hydrodynamics; no kernel change. Guard `R7-A6P`.

- **`verification/README.md` — historical round records, LEFT UNTOUCHED.** The following sentences
  describe what an earlier round consumed and are pinned by that round's guard; the execution must
  not "helpfully" edit them:
  - `:1005` "A6 is a gap and has no predicate, the alphabet carrying no internal index and the
    manuscript statement admitting two readings the round does not adjudicate" — the
    substratum-interface round; pinned by `R7-SUB` (`'A6 is a gap'` in `_rd1`, guard `:3772`);
  - `:1629` "The architecture is frozen exactly as it stands, A6 a gap with no predicate and not
    filled" — the frozen-sourcing round; pinned by `R7-FSS` (guard `:6383–6386`), together with the
    census note of that family (`_fs_fam[0]['note']`, guard `:6365–6372`);
  - `:1662` "The architecture is frozen, A6 a gap with no predicate and not filled" — the
    stochastic observer-interface round; pinned by `R7-SOI` (guard `:6538`, `:6555`);
  - `:1035` "that A6 holds or fails for any substratum" (in the substratum-source round's
    not-claimed list), `:315`, `:917–951`, `:1028` — consumption by name, unchanged;
  - `:2042–2061` — round 1's own record ("the `ROADMAP` carries A6 as a `GAP` because …"; "No
    reading is adopted, the `ROADMAP` label is unchanged, and no manuscript is edited") — describes
    round 1 and is unchanged; the new paragraph above is where the current state lives.
  - Likewise untouched, outside the README: `interface-audit.md:106` (the Q1 verdict table's row
    for the sixth assumption, a historical audit record); the whole of `manuscript-axiom-audit.md`; round 1's
    `preregistration.md` and `result.md` (blob-pinned, see the guard plan); the module docstring of
    `BackgroundIndependence.lean` ("adopts no reading", true of round 1); the census notes of the
    frozen-sourcing and stochastic-interface families; and the `R7-A6D` header comment
    (`:13148–13156`), which describes round 1.
- **Census.** The family "A6 background independence, round 1: definition and interface audit
  (substratum)" moves from `kernel-only` to `current`, with manuscript anchors actually created by
  this round and placed only where the kernel's scope reaches — the finite-alphabet definition and
  its book mirror, never `SM.md` §3.1's complex-lift sentences:
  - `papers/Substratum.md` — `"provided the coupling data carried on the links are transformed with it"`;
    `"the local transformation law imposes no further condition on the rule"`;
    `"forces the transformation to agree across every coupled pair of sites"`;
  - `book/ch02-substratum.md` — `"the local transformation law imposes no further condition on the rule"`;
  - `book/glossary.md` — `"**Background independence (A6).**"`.

  The family's `note` is amended **append-only**, by one sentence after "No manuscript propagation
  in this round.": "PROPAGATED by the A6 covariance propagation round
  (audits/foundations/a6-covariance-propagation-audit.md): A6-cov adopted as the publication
  meaning by owner decision, the manuscripts' definition rewritten around covariance with A6-inv
  named as a separate stronger fixed-background condition, A6-glob as the global specialization and
  A6-sd as a different principle under a shared name; the ROADMAP row P1 -- A6 carries CONDITIONAL,
  the named hypothesis being that the manuscripts' K = 6 link-coupled rule and its complex lift
  instantiate the link-coupled interface; the theorem and evidence scope are exactly those of the
  merged result, and the complex-lift covariance of SM.md:112-114 is not kernel-checked." The
  round-1 text of the note is not edited.
- **Guard `R7-A6D`, amended in exactly two places and no others**, recorded in the guard's own
  comment:
  - `_a6d_roadmap_row` (A18, `:13386–13395`): the row clause
    `'| **P1** | A6 — background independence / local gauge covariance | Substratum | **GAP** | the complete A1–A6 formal package |' in r`
    is re-pinned to the full new row string of Item 7 (whitespace-flattened, as `_A6DROAD` is);
    the two link clauses and the result-note clause
    `'**The `ROADMAP` row `P1 — A6` keeps its `GAP` label**' in t` are **unchanged** — the result
    note is not edited and still records, truly, that round 1 left the label in place.
  - `_a6d_m25` (`:13600–13603`): re-pinned to replace `**CONDITIONAL**` by `**DERIVED**` in the
    new row and to expect `_a6d_roadmap_row(r=_a6d_m25)` false.
  - The `check('R7-A6D', …)` message clause "The ROADMAP row P1 -- A6 is checked to keep its GAP
    label, absent owner direction, with the propagation a paragraph and links only; a label change
    is mutation-tested." is corrected to "The ROADMAP row P1 -- A6 is checked to carry the
    CONDITIONAL label the owner decision of the covariance propagation set, with round 1's result
    note still recording that round 1 left the GAP label in place; a DERIVED overclaim is
    mutation-tested."
  - **Untouched:** `_A6D_BASE` (`8792801beeeccbf0673db137cae83e6663d21fba`), the preregistration
    pin `afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3` in `_a6d_freeze_pin`, `_A6D_SEALED_HEAD`
    (`d0b8c6e83c32a01a586f947c0dfd9618a8b42a91`), `_A6D_MERGE`
    (`4fb0a6052d33193d442dd2a2cb72f64937177291`), the header comment, and every other contract
    (A1–A17, A19–A22) and mutation control (`m1`–`m24`, `m26`–`m31`, the drift control). In
    particular `_a6d_no_manuscript` (A19) and `_a6d_no_reading_adopted` pin the **result note's**
    sentences, which remain true of round 1 and are not edited. No other guard reads
    `ROADMAP.md` (the guard file's only `ROADMAP.md` read is `_A6DROAD`, `:13163`).
- **Guard `R7-A6P`**, placed immediately before `# ---- R7-A6D` (after `R7-A12P` where it has
  landed; name mechanically adjusted only on collision), mirroring the `R7-A12P` plan:
  - **P1** — this file's blob pinned **by content**, through `_bb_blob`, to the SHA recorded at
    the control-plane commit, with a drift control (one byte appended fails the pin);
  - **P2** — execution ancestry via `_rbr_strong_ancestry(_A6P_BASE, target, …)` with
    `_A6P_BASE` this control plane's merge commit, and archive mode via
    `_rbr_archive_ancestry(_A6P_BASE, _A6P_SEALED_HEAD, _A6P_MERGE)` once the sealed head and
    merge are pinned after exact-head review and merge (`_A6P_SEALED_HEAD = None` until then);
  - **P3** — round 1's `preregistration.md` and `result.md` pinned by content to
    `afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3` and `331b1928adde22d5c716a92adb864b523d0c09b8`, so
    that "the result note is not edited" is a checked fact and not a promise;
  - **P4** — `Substratum.md:102`'s frozen definition present: the covariance clause, "imposes no
    further condition on the rule", "is not the stronger fixed-background condition", "agree across
    every coupled pair of sites", "a separate principle that shares the name and is not A6";
    `:162`'s gloss and `:220`'s sentence present; the `A6-inv` wording "invariant under
    spatially-varying internal-index transformations that preserve the cubic-symmetric coupling
    matrix pointwise" absent from the definition;
  - **P5** — `SM.md:100`'s "This principle is not the structural assumption (A6)" present with
    the state-dependent equation preserved; `:110`'s and `:114`'s frozen sentences present; the
    transformation law of `:112` preserved; "kernel" absent from §3.1;
  - **P6** — `Structure.md:311`'s clause present; `ch02:86`, `ch05:141`, `ch05:143`, `ch09:207`,
    `appendix-b:317` frozen text present, `ch05:145` preserved, and the "requires the coupling
    structure to be dynamical rather than fixed" identification absent from Chapter 5;
  - **P7** — the glossary entry present in `book/glossary.md`, and every changed book passage
    byte-identical in the full-book source;
  - **P8** — the `ROADMAP` row equal to Item 7's line, and the section carrying "**Why the row is
    `CONDITIONAL`, and neither `DERIVED` nor `GAP`.**", the named hypothesis sentence, "is not
    kernel-checked", and the three-readings paragraph;
  - **P9** — the README paragraph of Item 8 present, and each historical sentence listed above
    still present verbatim;
  - **P10** — the census family `current`, every anchor present in its file, the round-1 note text
    unchanged as a prefix, no anchor in `papers/SM.md`;
  - **P11** — the frozen non-licences absent from every frozen surface, this file, the `ROADMAP`
    section and the README paragraph: "holds of the physical substratum" in the affirmative,
    "kernel-checked on the complex lift", "the Standard-Model gauge group is thereby derived",
    joint identification of the readings;
  - **Mutation controls**, each on the exact over-reading it exists to catch: (m1) the definition
    written back as `A6-inv` ("invariant … with the coupling held fixed" as the assumption);
    (m2) `A6-inv` and `A6-cov` identified ("is the same as the fixed-background condition" in place
    of "is not the stronger fixed-background condition"); (m3) `A6-sd` identified with `A6-cov`
    (`SM.md:100`'s "is not the structural assumption" written as "is the structural assumption");
    (m4) the Standard-Model gauge-group derivation declared settled by the assumption (an added
    "the Standard-Model gauge group is thereby derived without further hypothesis" at `SM.md:114`);
    (m5) complex-lift covariance declared kernel-checked in the `ROADMAP` section; (m6) the row's
    label written `**DERIVED**`; (m7) "holds of the physical substratum" asserted in the README
    paragraph; (m8) a census anchor placed in `papers/SM.md`; (m9) the glossary entry removed;
    (m10) the full-book mirror diverging from Chapter 2 by one word; (m11) one byte appended to
    round 1's result note; (m12) the Chapter 5 "dynamical rather than fixed" identification written
    back.
- **Rebuild** every affected `.tex` / `.pdf` (`papers/Substratum`, `papers/SM`, `papers/Structure`)
  and the book through the canonical `build.sh` route — never raw pandoc — or fail the round; no
  source/generated mismatch is admissible; the dropped-glyph and page-count checks are part of the
  build's acceptance.
- No Lean file, no round-1 artifact, no other `ROADMAP` status, and no Track B or hydrodynamics
  surface is edited.

## The chronology control

- **Sequencing.** The act 12 scope propagation control plane (#600) is merged at `999f1b5b…`; its
  execution pull request — Main, Explainer, Chapter 1, Chapter 19, glossary, full-book source,
  README, census, guard, and a `build.sh` rebuild of the TeX, PDF and book artifacts — is being
  executed and merges before this control plane. **This control plane's merge commit must descend
  from the act 12 propagation execution's merge commit.** Its execution, based on this control
  plane's merge commit and never updated from later `main`, therefore starts from a tree that
  already carries the act 12 edits to the glossary, the full-book source, the README, the guard
  and the rebuilt binary artifacts, and cannot collide with that pull request on any of them. If
  at the moment this control plane is to be merged the act 12 execution has not merged, this
  control plane waits; it is not merged first.
- This file is merged **alone**; the execution pull request is based on exactly the merge commit of
  this control-plane pull request and is never updated from later `main`.
- `R7-A6P` pins this file's blob **by content** and certifies the execution ancestry in act 10's
  strengthened form, by name: the real `pull_request.head.sha` in PR CI, never the synthetic merge
  commit; the base `B` an ancestor of the head `H` **and** every commit of `git rev-list H ^B` a
  descendant of `B`; recovery of `B`, `H` and every enumerated commit performed by the guard
  itself, a failed recovery failing the check; fail-closed with no fallback.
- **Archive mode** (the rule adopted on 2026-09-13, PR #599): once the execution pull request has
  merged, the guard re-runs the same strong check against the **sealed execution head pinned by
  SHA together with its merge commit** — the pinned merge's second parent must equal the sealed
  head, and both must be reachable from the current target — fail-closed. The pins are added in a
  follow-up that records the sealed head after exact-head review and merge; until then the guard
  runs in execution mode.
- **No execution object before the freeze.** No manuscript edit, guard, census change, `ROADMAP`
  edit or rebuilt artifact of this round exists in the tree before this file is merged; the single
  permitted content of this pull request is this file.

## The constraints, fixed in advance

- **Publication-only.** No Lean theorem, definition, proof, probe result, source adjudication, or
  research status other than the `P1 — A6` row is added, changed, or removed.
- **The readings stay four objects on three interfaces.** `A6-inv` is never identified with
  `A6-cov`; `A6-sd` is never identified with either; `A6-glob` is named as the specialization and
  consequence. In the manuscripts they are named in words, never by suffix.
- **Never overclaim.** Every kernel citation in this file, the `ROADMAP` and the README names the
  exact theorem and its interface scope. The complex-lift derivation of `SM.md` §3.1 is not
  kernel-checked and no text implies it is. Nothing says the assumption holds of the physical
  substratum. Nothing about the Standard-Model gauge-group derivation being settled, in either
  direction; the H-link + H-cust conditional carrier reading is preserved as it stands. Nothing
  about Track B, `P0` or hydrodynamics.
- **The bare-carrier finding stands.** The manuscript-axiom audit's gap verdict for the sixth
  assumption on the bare operational theory is untouched.
- **Manuscript voice only.** No round numbers, theorem labels, kernel identifiers, reading suffixes,
  review history, branch or pull-request language, dated notes, or verification process in
  manuscript prose; superseded wording is replaced in place, never narrated.
- **Historical records are not edited.** The list in Item 8 is exhaustive for this round and is
  what the execution leaves alone; a record found outside the list that describes the gap as it
  stood is reported, not edited.
- **Whole-corpus propagation.** Changed book passages are mirrored in the full-book source;
  generated forms are rebuilt through `build.sh`.
- **The guard amendment is scoped.** `R7-A6D` changes in exactly the two places and the one message
  clause named in Item 8, and nowhere else.

## Tests, fixed in advance

**E1 — the definition.** `Substratum.md` and Chapter 2 each define the sixth assumption as
covariance with the link coupling transformed, state that its content is the covariant interface and
that the local transformation law imposes no further condition on the rule, name the stronger
fixed-background condition as separate with its edge rigidity and its symmetric-point failure, name
the global commutant symmetry as the specialization, and name the state-dependent coupling graph as
a separate principle. Admissible outcome: both, in parallel.

**E2 — the use-sites agree with the definition.** `Substratum.md:104`, `:162`, `:220`, `SM.md:110`,
Chapter 2 `:102`, Chapter 5 `:141`, `:147`, Chapter 3 `:74`, Appendix B `:317`, `:327` each use
"promotes" or its gloss in the covariant sense and none reintroduces the fixed-background invariance
as the assumption. Admissible outcome: all.

**E3 — the shared name disambiguated.** `SM.md:100` names the state-dependent-geometry principle and
states that it is not the structural assumption; Chapter 5 `:143` carries no
identification of the assumption with a state-dependent coupling; Chapter 9 `:207` and the glossary
name the emergent-spacetime sense as a third sense; `Explainer.md:813` is unchanged and does not
conflict. Admissible outcome: all.

**E4 — the transformation law as the content.** `SM.md:112` is preserved verbatim, `:114` states the
covariance identity as what the assumption asserts, and neither `SM.md` §3.1 nor Chapter 5 §5.5
claims or implies a kernel check of the complex-lift statement. Admissible outcome: exactly that.

**E5 — the label.** The `ROADMAP` row equals Item 7's line, the section carries the reasons the
label is `CONDITIONAL` and neither `DERIVED` nor `GAP`, the named hypothesis is stated in both,
and the bare-carrier paragraph and the two attached qualifications are carried over verbatim.
Admissible outcome: all.

**E6 — the historical records.** Every sentence in Item 8's untouched list is present verbatim at
the execution head; `R7-SUB`, `R7-FSS`, `R7-SOI` pass without edit; round 1's `preregistration.md`
and `result.md` are at their pinned blobs. Admissible outcome: all.

**E7 — `R7-A6D` amendment scope.** Exactly `_a6d_roadmap_row`'s row clause and `_a6d_m25` are
re-pinned, the message clause is corrected, both blob pins and the sealed-head and merge pins are
unchanged, and every other contract and mutation control passes without edit. Admissible outcome:
exactly that.

**E8 — `R7-A6P`.** Contracts P1–P11 pass and every mutation control m1–m12 fails its contract.
Admissible outcome: all.

**E9 — mirrors and registry.** Changed markdown, generated TeX, PDFs, full-book source, census,
verification README and guards agree; the census family is `current` with real anchors on the
finite-alphabet definition and its book mirror only, no anchor in `papers/SM.md`, and no stronger
status than the merged theorem. Admissible outcome: all.

**E10 — non-licences.** No surface says the assumption holds of the physical substratum, identifies
two readings, declares the complex-lift covariance kernel-checked, declares the Standard-Model
gauge-group derivation settled, or mentions Track B, `P0` or hydrodynamics in this connection.
Admissible outcome: zero.

**E11 — re-grep.** The execution reports corpus-wide surviving counts for "background
independence", "background-independent", "(A6)", "A6 (background independence)", "promotes",
"state-dependent", "invariant under spatially", "preserve the cubic-symmetric coupling matrix
pointwise", "coupling structure pointwise", "dynamical rather than fixed"; every survivor is
classified as intended, name-only, `A6-sd`-sense, emergent-spacetime-sense, or legitimate
non-target use, and no surface still states the fixed-background invariance as the assumption.
Admissible outcome: no stale contradictory surface.

**E12 — checks.** Release gate, `voice_check`, `claims_check`, `artifact_placement_check`, the
foundations probes, manuscript and architecture guards, census, canonical builds and dropped-glyph
checks all green; no kernel count change attributable to this publication round. Admissible outcome:
all green.

## What the round does not do

It does not prove a new theorem, package the `K = 6` link-coupled rule as a `Substratum`, build a
complex-lift interface, formalize `A6-sd`, decide the A4/A6 overlap or the denotation of "the
cubic-symmetric coupling matrix", say that the assumption holds of the physical substratum, touch
the Standard-Model derivation chain or H-link, H-cust or H-Bell, touch Track B, `P0` or
hydrodynamics, edit any round-1 artifact or any historical round record, change any `ROADMAP`
status other than the `P1 — A6` row, or enter the Lemma 24.1 round.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative**: the commit SHA locates the tree, the blob SHA is what the guard compares.
- Once merged, this file is immutable; execution-affecting corrections are append-only amendments,
  separately frozen and merged before the work they affect.
- **This PR carries this file alone.**
- **Then exactly one execution PR**, based on the merge commit of this one — which must itself
  descend from the act 12 propagation execution's merge commit — carrying the manuscript edits of
  Items 1–6, the `ROADMAP` row and section of Item 7, the README paragraph, the census change, the
  `R7-A6D` amendment and the `R7-A6P` guard of Item 8, and the `build.sh` rebuild of the affected
  TeX, PDF and book artifacts.
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. the execution base (this control plane's merge commit) and the act 12 propagation execution's
   merge commit it descends from, with the blobs of every edited and re-pinned surface at the base;
2. each Item's replacement text as it landed, with any punctuation or sentence-order adjustment
   reported, and the kernel result each frozen sentence rests on stated at its interface scope;
3. the `ROADMAP` row and section as they landed, and the label `CONDITIONAL` with its named
   hypothesis and the reasons `DERIVED` and `GAP` were not used;
4. the untouched historical records, listed and confirmed present verbatim;
5. the `R7-A6D` amendment, confined to the two pins and the message clause, and `R7-A6P`'s
   contracts and mutation controls, each reported passing or failing as designed;
6. the census change, with each anchor and its file;
7. the re-grep counts of E11 with every survivor classified;
8. the builds, the dropped-glyph and page-count checks, and the release gate;
9. what the round does not do, in this file's wording.

Status: preregistered; manuscript execution follows only after this file is merged alone, after the
act 12 propagation execution has merged.
