# Hydrodynamics round H-D-SR — source reconciliation for the entailment question and the two statements of A5: RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`d222e5c6f248bddf8327303523a71b5f82a050d4`, merged into `main` as
`62970976a06b3f25553970095ee23cab82100f83` (PR #635) — the freeze's mandated execution base.

The round is **type P throughout**. It proves nothing, writes no Lean, takes no limit, and edits no
source. Its deliverable is an inventory of what the sources say about one question and about the
relation between two gauge freedoms, reported by quotation with coordinates, together with the
recorded finding that the record does not adjudicate the disagreement it contains.

**The round label `H-D-SR` is an identifier, not an ordinal.** It is not a rung of the H1–H7 ladder,
it is not `H-C`, and its `SR` target prefix is not the programme's `S1`–`S5` continuum-breakdown
branch and not rounds `S-A`/`S-B`. No `HD`/`HC`/`HI`/`HO` taxonomy label is applied to anything by
this round.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `62970976a06b3f25553970095ee23cab82100f83` (merge of PR #635) |
| This round's frozen control plane | `preregistration.md`, blob `d222e5c6f248bddf8327303523a71b5f82a050d4`, **pinned by content and verified at the base before any target was executed** |
| The repository conventions | `AGENTS.md`, blob `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` — the blob the freeze pins |
| The substratum axioms, the gauge-group section and its status notes | `papers/Substratum.md`, blob `9ac6b732e8786897cade416b67c3f7f1df81ab84` — the blob the freeze pins |
| The alphabet-as-gauge section, the linearity lemma and [SM §6] | `papers/SM.md`, blob `26d6cbfb230c105eb00a979c2b69c363568455dd` — the blob the freeze pins |
| The observation hierarchy and the conditional-forcing remark | `papers/Structure.md`, blob `84a7ede451a917513dd488477c93180f5f8c0486` — the blob the freeze pins |
| The posit ledger | `papers/Main.md`, blob `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` — the blob the freeze pins |
| `papers/Explainer.md` | blob `b0926875346305ef053995fc10695353df64de68` — the blob the freeze pins |
| `papers/Methodology.md` | blob `1d332b0c9256e33861af0ce3b5598091b63d30a1` — the blob the freeze pins |
| `papers/Complexity.md` | blob `dd38c5b39797433b6f5de469f5711fd38b116441` — the blob the freeze pins |
| `book/ch02-substratum.md` | blob `519188eac9e4c347d7f01eb5b559cfb01df48ea9` — the blob the freeze pins |
| `book/ch03-structural-realism.md` | blob `9de441661c3a0e1132724df4aa392010dde8ed8b` — the blob the freeze pins |
| `book/ch05-gauge-structure.md` | blob `0f55ef3a7b5fca4172073f330f373f4b16542402` — the blob the freeze pins |
| `book/ch06-matter-content.md` | blob `44ef4bd812b174e881592a02bcbf768cf1af09ad` — the blob the freeze pins |
| `book/appendix-c-objections.md` | blob `f6bc786a4923db3dd08488d8ec43d7e1f9fc7a6a` — the blob the freeze pins |
| `book/The-Incompleteness-of-Observation-FULL.md` | blob `9674614cbb55b58b7492f1e4b65a4f09e82e91b5` — the blob the freeze pins |
| The verification roadmap | `verification/ROADMAP.md`, blob `c356e9b5f857ef18a992d67df613b9db96a949d7` at the base (the freeze records `4f9af3d3…`) — **discrepancy D1** |
| The verification README | `verification/README.md`, blob `d25eb2d44d0aa324c095930f40174296fd0f2279` at the base (the freeze records `585dd145…`) — **discrepancy D2** |
| The chronology guard | `verification/lean/edge_rigidity_probe.py`, blob `55e7c3e3139741521bc5aeac6add56f557be5943` at the base (the freeze records `dc30d365…`) — **discrepancy D3**; consumed as context and **not modified** |
| The programme roadmap | `../PROGRAMME.md`, blob `b7b24112a462aee083c3e8f3c2980283b38cd10f` — the blob the freeze pins; read for its §8 one-line state and not edited |
| Round H-A, the frozen control plane | `../round-h-a-source-audit/preregistration.md`, blob `934cd6aff1cfb07b823c9b131693ee59bb98c632` |
| Round H-A, the result | `../round-h-a-source-audit/result.md`, blob `56d34463cf6b68bf28d9ab99b6e09f9fa287d826` |
| Round H-B, the frozen control plane | `../round-h-b-reversible-fluid-substratum/preregistration.md`, blob `37cc9dae301ee10d55adb73b296aa2fc7d0578e3` |
| Round H-B, the result | `../round-h-b-reversible-fluid-substratum/result.md`, blob `dc03b582ed718d374c471b27403b282a295d5c85` |
| Round H-D, the frozen control plane | `../round-h-d-a5-status-adjudication/preregistration.md`, blob `a2398c3954f13ac458184c70df8f1ec6b321cc9b` |
| Round H-D, the result | `../round-h-d-a5-status-adjudication/result.md`, blob `f80dd8832955cb7f17e9712ccdafae364a4059e3` |
| The substratum interface | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` |
| Round H-A's module | `verification/lean-mathlib/OIBridge/HydroSourceAudit.lean`, blob `fd5f54d8cbba4f68b67335c111d39a2add0c642f` |
| Round H-B's module | `verification/lean-mathlib/OIBridge/HexLatticeGas.lean`, blob `374db0387337960888a67f4e98609446c8a1b871` |
| The A6 definition round | `verification/lean-mathlib/OIBridge/BackgroundIndependence.lean`, blob `5ec9fe52835642724d0685d9b920f613874279d6` |
| The A5-consuming interface audit outside hydrodynamics | `verification/lean-mathlib/OIBridge/StochasticInterface.lean`, blob `0f4d1b1625e9c5c5070750bab04c9c989f0f0d04` |
| The manuscript-axiom audit, kernel side | `verification/lean-mathlib/OIBridge/ManuscriptAxioms.lean`, blob `f7befdc7b5e814677e6220d91e06fc35b8950c49` |

**Blob check against the freeze, performed before any target was executed.** Twenty-seven of the
thirty pinned blobs are the blob at the base. **Three moved**, and each movement was diffed against
the freeze's blob before the round proceeded: `verification/ROADMAP.md`, `verification/README.md`
and `verification/lean/edge_rigidity_probe.py`. All three movements are one addition apiece, and all
three are the landing of **one sibling round of another programme** that merged into `main` before
this control plane did. **No text this round reads for the entailment question or for either
statement of A5 moved**, at any file. The three movements are recorded as discrepancies D1–D3 below,
with the diffs named. **The freeze is not repaired.**

**The anti-contamination invariant, applied.** The freeze's invariant reads:

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

D1–D3 are exactly that case. The sibling material present at the base is **not an input to this
round**, is cited in no determination, and carries no target. Its presence at the base is a fact
about the base. In particular, the hydrodynamics programme's concurrent H3 round has a directory at
the base carrying a preregistration; the freeze excludes that round in terms — not scoped, not
consumed, not depended on — and **its directory was excluded from this round's sweeps and was not
read**. That exclusion is recorded here as a boundary of the sweeps, in `SR-2`'s surface statement
below. No finding of this round is evidence for or against H3 in either direction.

**Parallel-track separation holds.** Nothing here consumes or produces evidence for the OI → QM
chain (Track B, Track I), for Bell, or for gravity. Their manuscript sections are read as the
location of a statement and for nothing else; that reading is a source audit and not an import of
evidence.

## Outcome, in one line

**The round landed where the freeze predicted, at every target, at every predicted sign and
strength.** Five statements of the entailment question stand at the execution base, four in the open
form and one resolved in the negative, reported as five and quoted with coordinates; the named and
bounded sweep enlarges the inventory by further statements about the principle's status and about
its relation to the `q`-size freedom, including two that say in their own words that the two
freedoms are instances of one master principle and that they are distinct; the entailment question
is **posed nowhere on the surface outside those five**, the book in particular carrying the
principle and the size freedom without posing the question; **no passage on the record adjudicates
between the two forms**; the two statements of A5 are two, with no identification theorem in the
tree; H-D's three answers appear on none of the three propagation surfaces; and every passage quoted
from `papers/` is byte-identical to the text at H-D's own execution base. **No target landed against
prediction, and no target's strength moved.** The round adopts neither form, resolves nothing, edits
no source, and makes none of the three owner decisions it names.

## `SR-0` — locating controls

The seven charter passages, H-D's status rule 11 in full, and H-D's `A5S-0a` outcome paragraph, each
located and quoted at the mandated base with its coordinate. Nothing was absent.

**1. The frozen discipline as executed** — `../round-h-d-a5-status-adjudication/result.md:490–494`:

> **The frozen discipline, observed.** This round **adopts neither form over the other**, **edits no
> manuscript**, and **resolves no divergence**. **The propagation question is named here for the
> owner and the round stops**: five statements of the entailment question stand in the corpus, four
> in the open form and one resolved in the negative, and whether the negative resolution should
> propagate to the other four is an owner decision this round records and does not make.

**2. H-D's discrepancy D6** — `../round-h-d-a5-status-adjudication/result.md:871–880`:

> **D6 — `A5S-2d`: the entailment-question record grew by two.** The freeze names three statements:
> the parenthetical at [Substratum §3.1] (A5), the closing sentence of [SM §2.7], and
> [Substratum §4]'s formalization-status note. Two further statements stand in the corpus, both in
> the **open** form: [Substratum §3.1]'s **closing paragraph**, in the same section as the
> parenthetical, and **[SM §6]**, which records the map-uniqueness as inheriting the principle's
> "open status". **Five statements now stand, four open and one resolved in the negative.**

and, at `:879–880`:

> **Neither form is adopted, no manuscript is edited, and the divergence is not resolved.**
> **The propagation question is named for the owner at `A5S-2d` and this round stops there.**

**3. H-D's status rule 9** — `../round-h-d-a5-status-adjudication/preregistration.md:691–692`:

> **No manuscript is edited, and no divergence found in the corpus is resolved by this round.**
> `A5S-2d`'s finding is recorded and named for the owner.

**4. The falsifier column for `A5S-2d`, this round's licence for the wider sweep** —
`../round-h-d-a5-status-adjudication/preregistration.md:575`, the falsifier cell of the row:

> a further statement elsewhere in the corpus; it is added to the record

**5. On the two statements of A5** —
`../round-h-d-a5-status-adjudication/preregistration.md:69–72`:

> **The kernel's A5 is additivity of `F`; the manuscripts' A5 is linearity of the wave equation.**
> These are two statements, related by the kernel's instance theorem `waveSubstratum_A5` for the one
> rule where both are in play. **No identification theorem between them exists in the tree, and this
> round does not build one** (`A5S-0a`, hazard 11).

**6. H-D's chronology control 4** —
`../round-h-d-a5-status-adjudication/result.md:917–918`:

> **Whether the `R7-HY*` family should be extended to cover prose-only rounds of this programme is
> an owner decision this round records and does not make.**

**7. H-D's discrepancy D7** — `../round-h-d-a5-status-adjudication/result.md:893–896`:

> **H-D's D7, carried at this mention — the start-state record of what H-D leaves open.**
> **The §8 refresh is therefore left to the later action status rule 11 names**, and when that action
> is taken, status rule 11 fixes the words it must carry — the three answers and **both**
> disqualification-rule consequences, in the freeze's own wording and nothing stronger.

**`SR11-words` — H-D's status rule 11 in full**, quoted and not paraphrased, from
`../round-h-d-a5-status-adjudication/preregistration.md:698–706`:

> 11. `../PROGRAMME.md` §8's one-line state, when a later action refreshes it, carries the three
>     answers and **both** disqualification-rule consequences in the words this file uses, and
>     nothing stronger. If the round lands where it predicts, that is: "no derivation of A5 from bare
>     OI was found on the record searched and the counterexample question is undecided, so whether A5
>     is a bare-OI requirement is undecided; A5 is used at located steps of the reconstruction,
>     quantum-specific on the present record; its necessity for Navier–Stokes is undecided; and no
>     established ground disqualifies H-B's candidate either as an OI-admissible candidate or as a
>     candidate for the targeted limit, with OI-substratum admissibility of the A1–A4, ¬A5 class
>     remaining open."

**This wording is settled and is reproduced here as quotation.** No target of this round proposes,
ranks or amends it. H-B's guardrail is carried at this mention of H-B: *H-B shows that A5 is not
needed to obtain a promising reversible fluid candidate with the right microscopic ingredients; it
does not yet show that A5 is unnecessary for an actual Euler/Navier–Stokes limit.*

**H-D's `A5S-0a` outcome paragraph** — `../round-h-d-a5-status-adjudication/result.md:80–88`:

> **These are two statements.** A search of the tree at the mandated base returns **no theorem
> identifying them**. What the tree carries is `waveSubstratum_A5`
> (`SubstratumInterfaceAudit.lean`, line 211), an instance result: the one rule for which both are
> in play satisfies the kernel predicate. An identification would have to quantify over rules that
> the kernel's `Rule` interface does not constrain to be wave-like, and no such statement exists.
> **This round does not build one.**
>
> **Outcome: positive — the two statements are recorded as two, and no identification is found.
> Evidence type P. Full strength**, as predicted.

**Outcome: positive — all nine located and quoted at the base, none absent. Evidence type P. Full
strength**, as predicted.

## `SR-1` — the five statements, re-read and reported as five

Each of H-D's D6 statements, re-read at the mandated base, quoted with its coordinate, with the
words carrying its form quoted inside the quotation. **The five are reported separately and none is
merged into another.**

| # | coordinate | the statement, quoted at the base | the words carrying the form | form |
| --- | --- | --- | --- | --- |
| 1 | `papers/Substratum.md:100` | "(A5) **Linearity.** The wave equation for $\varphi$ is linear. (Equivalent to amplitude-scale gauge invariance — that the field-value scale is unphysical — via the linearity-equivalence lemma of [SM §4.1]; hence necessary *given* that gauge principle and "partly derived" in exactly that sense. **Whether the $q$-size gauge freedom of [SM §2.7] entails amplitude-scale gauge is an identified open step**; pending it, nonlinear alternatives are excluded precisely to the extent amplitude-scale gauge is assumed, and would otherwise require a separate derivation.)" | "is an identified open step" | `form-open` |
| 2 | `papers/Substratum.md:104` | "… A5 (linearity) is equivalent to amplitude-scale gauge invariance via the linearity-equivalence lemma of [SM §4.1], hence partly derived — necessary *given* amplitude-scale gauge, **with whether [SM §2.7]'s $q$-size gauge entails it left as an identified open step**." | "left as an identified open step" | `form-open` |
| 3 | `papers/SM.md:92` | "… This amplitude-scale (additive-automorphism) gauge is what the §4.1 linearity argument invokes; **whether it is entailed by the $q$-size statement above, or is an additional principle, is an identified open structural question**." | "is an identified open structural question" | `form-open` |
| 4 | `papers/SM.md:791` | "The identification's *kinematic* half — which measure, and which map — is thereby raised to theorem level, conditional on the additive-automorphism (amplitude-scale) gauge principle it invokes, which [Substratum §4, Theorem 24, *Status*] classifies as an adjoined operational input rather than a theorem (§2.7); **the map-uniqueness therefore inherits that principle's open status**." | "inherits that principle's open status" | `form-open` |
| 5 | `papers/Substratum.md:268` | "*Formalization status of the linearity step (resolved as a sharpened axiom, not a closure).* … **The question of whether the $q$-*size* gauge freedom of [SM §2.7] *entails* amplitude-scale gauge resolves in the negative, and sharply**: the weak reading of §2.7 (size-independence of predictions) does not reach rescaling at fixed $q$; the strong reading (arbitrary relabellings of $\mathbb{Z}/q\mathbb{Z}$ are gauge) *overshoots* … The principled object that delivers exactly what is needed without overshooting is the **additive-automorphism** group $x \mapsto \lambda x + c$ ($\lambda$ a unit)…" | "resolves in the negative, and sharply" | `form-neg` |

**Four in the open form, one resolved in the negative — the distribution H-D's D6 records.** Row 3's
open form and row 5's negative resolution are statements of the **same** question in the sources'
own vocabulary: row 3 asks whether the amplitude-scale (additive-automorphism) gauge "is entailed by
the $q$-size statement above", and row 5 asks whether "the $q$-*size* gauge freedom of [SM §2.7]
*entails* amplitude-scale gauge". **Both phrasings are recorded and they are not merged.**

Where the five differ in what they say beyond their form, the difference is recorded and not
normalized: rows 1 and 2 state the question as a step pending inside A5's own status; row 3 states it
as a structural question about which principle is primitive, offering "an additional principle" as
the alternative; row 4 states no question of its own and records an **inherited** status, attaching
it to a different object (the map-uniqueness of [SM §6]); row 5 states an answer and gives grounds
for it, and in the same paragraph names the **additive-automorphism** group as the object that
"delivers exactly what is needed without overshooting".

**Recorded reading 1 of the freeze is confirmed at the base**, coordinate for coordinate and form for
form.

**The frozen sentence for the outcome reached — FIVE-AS-RECORDED:**

> Five statements of the entailment question stand on the record at the execution base, quoted
> with coordinates in this note: four carry the open form and one carries the resolution in the
> negative. They are reported as five separate statements, none merged into another, and neither
> form is adopted over the other.

**Outcome: positive. Evidence type P. High strength**, as predicted.

## `SR-2` — the sweep beyond H-D's record

**The surface, named and bounded.** `papers/*.md`; `book/*.md`; `verification/programmes/**/*.md`;
`verification/audits/**/*.md`; `verification/README.md`; `verification/ROADMAP.md`; and
`verification/lean-mathlib/OIBridge/*.lean` (165 modules at the base). The searches run over the
surface were: `amplitude-scale` / `amplitude scale`; `additive-automorphism` / `additive
automorphism`; `entail` in all its forms; `identified open step`, `open structural question`,
`inherits that principle's open status`; `resolves in the negative`, `does not entail`, `not
entailed`, `overshoot`; and the size-freedom vocabulary `q-size`, `alphabet-size`, `alphabet size`.

**What is off the surface, recorded with the finding.** `.tex` and `.pdf` renderings are **out of the
surface**, and this note says so. The hydrodynamics programme's concurrent H3 round directory is
excluded in terms by the freeze and **was not read**, so no statement standing there — if any does —
is in this inventory; that is a boundary of the sweep and not a claim about what lies inside it.
`book/The-Incompleteness-of-Observation-FULL.md` is a concatenation of the chapter files, and a
statement found there is reported at **both** coordinates and counted **once**.

**A sweep's surface is not a claim that every file on it was quoted; it is a claim about what a named
search over a named surface returned.**

### `SR-2a` — further statements about the principle's status or its relation to the `q`-size freedom

Every statement the sweep returned that bears on the relation between the `q`-size gauge freedom and
the amplitude-scale principle, or on the principle's status, and that is not among `SR-1`'s five.
Each is classified by its own quoted words. **`form-other` is this freeze's bookkeeping category and
is never attributed to a source**; where a passage carries a status and nothing about the relation,
that is said in the row.

| coordinate | quoted at the base | what it says, in its own words | form |
| --- | --- | --- | --- |
| `papers/Substratum.md:264` | "… so amplitude-scale gauge is **one instance of the framework's master principle** that *observationally indistinguishable transformations are gauge* — **the same principle behind generators (i)–(iv) and the $q$-size freedom of §2.7**, not an ad hoc addition. Two derivations invoke it: the linearity equivalence of [SM §4.1] … and the $SU(N)$ reduction of Stage 2(d) above; its status as an operational input rather than a theorem … is set out in the *Status* note immediately below." | the two freedoms are instances of one master principle; the principle is an operational input | `form-other` |
| `papers/Substratum.md:266` | "*Status (open, referee-grade).* Amplitude-scale gauge is **adjoined as an explicit operational principle**: **it is not one of (i)–(iv)** — generator (i) over-counts … **and (ii) is alphabet-*size* only** — so the results invoking it are conditional on it. … Amplitude-scale gauge therefore has the status of an operational input on a par with center independence and isotropy, not a theorem; **whether it is independently warranted by the observer architecture is the question flagged for external review**." | the principle is adjoined and not a generator; it is distinct from generator (ii), which is size only; a **different** open question is flagged — independent warrant by the observer architecture, not entailment | `form-other` |
| `papers/Substratum.md:252` | "*(Scope.)* … a site-wise *nonlinear* relabelling of the alphabet preserves $G_\varphi$ but alters the field-amplitude dispersion $\omega(k)$ of [SM §4.1] … **The relabellings preserving $\omega(k)$ as well are exactly the additive-automorphism (affine) ones — the amplitude-scale subgroup (Remark below).**" | the amplitude-scale relabellings are exactly the dispersion-preserving ones, a subgroup of generator (i) | `form-other` |
| `papers/Substratum.md:219` | "A5 (linearity) is the strongest restriction; it is equivalent to amplitude-scale gauge invariance (linearity-equivalence lemma, [SM §4.1]), so nonlinear wave equations on finite lattices are the separate class one obtains exactly when that gauge principle is dropped." | a status statement about A5 and the principle; poses no question of entailment | `form-other` |
| `papers/Structure.md:219` | "the forcing runs through *amplitude-scale* gauge (the unobservability of the absolute field scale), which [Substratum §4, Theorem 24, *Status*] **classifies as an adjoined operational input rather than a theorem** ([SM §2.7]) — **its independent warrant by the observer architecture being an open, referee-grade question**. Linearity is therefore forced *given* that operational principle, not unconditionally." | a status statement; the open question it names is **independent warrant**, not entailment | `form-other` |
| `papers/SM.md:236` | "The strongest non-QM argument retained here is **the amplitude-scale-gauge lemma**: if the embedded observer has no access to an absolute field-amplitude scale, base-point-independent first differences force an affine rule, and the center-free branch reduces it to a linear one." | a status statement about what the lemma delivers and on what hypothesis | `form-other` |
| `papers/SM.md:338` | "The reduction from the natural unitary stabilizer to the Standard-Model group carries **the separate amplitude-scale-gauge/background-independence premises** discussed in §4.6." | a status statement: the principle is a premise, and a separate one | `form-other` |
| `book/ch05-gauge-structure.md:47` = `book/The-Incompleteness-of-Observation-FULL.md:1372` | "It is realized as the additive (affine) relabellings $\boldsymbol{\phi} \mapsto \lambda\boldsymbol{\phi}$ of the alphabet being gauge, and is **one instance of the framework's master principle** that observationally indistinguishable transformations are gauge — **the same principle behind the four $\mathcal{G}_{\text{sub}}$ generators and the alphabet-*size* freedom, from which it is nonetheless *distinct***. It is an **explicit adjoined operational principle** of $\mathcal{G}_{\text{sub}}$ … results that invoke it are conditional on it." | the two freedoms are instances of one master principle **and** the principle is distinct from the size freedom; the principle is adjoined | `form-other` |
| `book/ch05-gauge-structure.md:17` = `FULL:1342` | "the **physical Standard-Model carrier is not yet forced**: it additionally requires H-link single-copy and H-cust, followed by **the amplitude-scale/background-independence premises already recorded**." | a status statement: the principle is a recorded premise | `form-other` |
| `book/appendix-c-objections.md:269` = `FULL:6497` | "The audit also identifies **two inputs that are not derived in this sense and are recorded as such: the amplitude-scale gauge principle (treated in the substratum development as an operational input rather than a theorem)** and the identification of the propagation modes with the gauge-carrying components." | a status statement: the principle is an input, not derived | `form-other` |
| `verification/programmes/substratum/a6-instantiation/result.md:158–159` (and `preregistration.md:355–356`) | "the singleton-`K` rescalings are **the amplitude-scale freedom the manuscripts assign to A5, not the internal-index freedom of the sixth assumption**" | a distinctness statement separating the amplitude-scale freedom from A6's internal-index freedom | `form-other` |
| `verification/programmes/substratum/a6-background-independence/result.md:151–152` (and `preregistration.md:285`) | "the degenerate statement is not the manuscripts' A6 … which is **the amplitude-scale freedom the manuscripts assign to A5** — `Substratum.md:100`: "amplitude-scale gauge invariance — that the field-value scale is unphysical"" | the same distinctness statement, in the merged verification record | `form-other` |
| `verification/audits/foundations/phase-source-audit.md:75` and `:259` | "P4, the internal-index and amplitude-scale gauge | `[Substratum §3.1]` A5 (amplitude-scale gauge invariance), A6 … | … | (D1): gauge of the description, no operation named" | a sourcing row placing the principle at [Substratum §3.1] and recording it as gauge of the description | `form-other` |
| `verification/lean-mathlib/OIBridge/A6Instantiation.lean:320–321` | "round 1's degeneracy verdict — the singleton-`K` rescalings are the amplitude-scale freedom the manuscripts assign to A5, not the internal-index freedom of the sixth assumption — **stands for `waveSubstratum`**" | the same distinctness statement, in the kernel tree's prose | `form-other` |
| `verification/lean-mathlib/OIBridge/BackgroundIndependence.lean:50–51` | "the degenerate statement is not the manuscripts' A6 (**the singleton-`K` rescalings are the A5 amplitude-scale freedom**), and the wave substratum's A6 status at manuscript level stays a gap." | the same distinctness statement | `form-other` |
| `verification/lean-mathlib/OIBridge/HexLatticeGas.lean:94–96` and `:682` | "It lies in **the class obtained by dropping A5's amplitude-scale gauge principle**; **whether that class is admissible as an OI substratum is an owner decision this round does not make**, and it is recorded as open." | a status statement about a class defined by dropping the principle, and an owner decision recorded as open | `form-other` |

**Not in the inventory, and why, recorded.** `papers/Substratum.md:162`, `papers/SM.md:292`,
`papers/SM.md:368`, `papers/Main.md:706`, `book/ch02-substratum.md:102`,
`book/ch03-structural-realism.md:74`, `book/ch05-gauge-structure.md:127`, `:129`, `:131`, `:133`,
`:147`, `:185`, `:194`, `:196` and `book/ch06-matter-content.md:8` **invoke or apply** the principle
at a derivation step without stating anything about its status or about its relation to the `q`-size
freedom. They are located uses, which H-D's `A5S-2` already enumerated at H-D's own scope, and they
are recorded here as located and as carrying no statement of the kind `SR-2a` enumerates.
`verification/audits/foundations/a6-covariance-propagation-audit.md:290` records that the manuscript
lines naming the premise "name the premise without asserting a reading and are **unchanged**", which
is a statement about that audit's own propagation and is recorded as such.

**H-B's guardrail is carried at this mention of H-B:** *H-B shows that A5 is not needed to obtain a
promising reversible fluid candidate with the right microscopic ingredients; it does not yet show
that A5 is unnecessary for an actual Euler/Navier–Stokes limit.*

**Hazard 2, observed.** Two rows above say in their own words that the two freedoms are **distinct**
(`papers/Substratum.md:266`, `book/ch05-gauge-structure.md:47`), and two say that they are
**instances of one master principle** (`papers/Substratum.md:264`,
`book/ch05-gauge-structure.md:47`, which says both). The freeze names both of those as `form-other`
examples. **None of them is sorted into `form-open` or `form-neg` by this round**, and none is read
as evidence for either form.

**The frozen sentence for the outcome reached — THE RECORD GROWS:**

> The named and bounded sweep enlarges the record by the statements tabulated in this note, each
> quoted with its coordinate and classified by its own words; the enlargement is an addition to
> the inventory and changes the form of no statement already in it.

**Outcome: positive. Evidence type P. Medium strength**, as predicted — a corpus-wide sweep is
exactly where a missed passage is the plausible error, and this is a statement about the surface
named above and about nothing off it.

### `SR-2b` — further statements of `Q-ent` itself

**The determination.** On the named and bounded surface, **`Q-ent` is posed nowhere outside `SR-1`'s
five.** The searches for the open form's phrasings (`identified open step`, `open structural
question`, `inherits that principle's open status`) returned, across the whole surface, the four
`SR-1` open coordinates in `papers/` and nothing else in any source; their remaining hits are H-D's
own result note and preregistration recording those same four, and this round's own freeze. The
searches for the negative form's phrasings (`resolves in the negative`, `does not entail`, `not
entailed`, `overshoot`) returned `papers/Substratum.md:268` and, elsewhere, only statements about
other questions entirely — `DerivedOICore` and the controllability resource
(`verification/programmes/substratum/route-b-audit.md:15`, `:219`, `:265`;
`verification/audits/foundations/flow-endpoint-audit.md:244`; `verification/README.md:912`),
quasilocal instrument availability
(`verification/lean-mathlib/OIBridge/InstrumentAvailability.lean:46`, `:333`;
`verification/audits/operational/instrument-completion-audit.md:303`), and schema implication
(`verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/preregistration.md:222`).
**None of those bears on `Q-ent`.**

**The book, determined as `SR-2b` requires.** The book carries the amplitude-scale principle and it
carries the alphabet-size freedom, and it **does not pose the entailment question**. The decisive
comparison is between the book's own parallel of [SM §2.7] and [SM §2.7] itself.
`papers/SM.md:92` closes:

> This amplitude-scale (additive-automorphism) gauge is what the §4.1 linearity argument invokes;
> whether it is entailed by the $q$-size statement above, or is an additional principle, is an
> identified open structural question.

`book/ch05-gauge-structure.md:45` = `FULL:1370`, the same material in the book, closes:

> This is generator (ii) of the substratum gauge group $\mathcal{G}_{\text{sub}}$ developed in
> Chapter 2 §2.5.

The book's chapter then states the principle at `book/ch05-gauge-structure.md:47` = `FULL:1372`,
where what it says about the relation is that the principle is "one instance of the framework's
master principle … the same principle behind the four $\mathcal{G}_{\text{sub}}$ generators and the
alphabet-*size* freedom, **from which it is nonetheless *distinct***". `book/ch02-substratum.md:44`
records the alphabet size as gauge — "The alphabet $q$ is gauge: there is no answer to find, because
the question is empty" — and poses no entailment question.

**The finding is that the book is silent on `Q-ent`** — not that it answers it in either direction.
The distinctness statement at `:47` is recorded as what it says, a `form-other` statement in
`SR-2a`'s table, and **is not read as a resolution of `Q-ent` in the negative**; the freeze names "a
statement that they are distinct" as a `form-other` example, not as `form-neg`.

Two further regions carry an **open question that is not `Q-ent`** and are recorded here so they are
not miscounted: `papers/Substratum.md:266` and `papers/Structure.md:219` both flag *whether the
principle is independently warranted by the observer architecture* as open. That is a different
question from whether the `q`-size freedom entails the principle. **Both are recorded as what they
say and neither is counted as a sixth statement of `Q-ent`.**

**The frozen sentence for the outcome reached — SILENCE:**

> On the named and bounded surface, the regions tabulated in this note carry the amplitude-scale
> gauge principle without posing the entailment question. **The finding is that they are silent on
> it** — not that they answer it in either direction.

**Outcome: negative, as predicted. Evidence type P. Medium strength**, as predicted — a negative on a
sweep is a statement about the sweep and about nothing off it.

## `SR-3` — does anything on the record adjudicate between the forms?

**The search, named and bounded.** The whole of `SR-2`'s surface, for a passage that does any of the
four things the freeze enumerates: states which of `form-open` and `form-neg` governs; states that
the two are one statement; states that the record is divided; or states that the negative resolution
reaches the statements carrying the open form. The searches run were those listed under `SR-2`'s
surface, together with a search for adjudication-shaped language across the five statements' own
files and the book chapters carrying the principle — `supersede`, `takes precedence`, `governs`,
`authoritative statement`, `the record is divided`, `inconsistent with`, `contradicts`.

**The result: nothing on the surface says any of those four things.**

- **No passage states which form governs.** The four open statements state the question as open and
  say nothing about the fifth; the fifth states an answer and says nothing about the four.
- **No passage states that the two are one statement.**
- **No passage states that the record is divided.** The only place in the whole surface where the
  five statements are gathered and their disagreement is put on the record is H-D's own result note,
  which gathers them precisely in order to record that it does **not** resolve them:
  "**Neither form is adopted, no manuscript is edited, and the divergence is not resolved.**"
  (`../round-h-d-a5-status-adjudication/result.md:879`).
- **No passage states that the negative resolution reaches the statements carrying the open form.**
  `papers/Substratum.md:268` states its answer and gives grounds for it, and on a bounded reading of
  that paragraph and of the section it sits in ([Substratum §4], the substratum gauge group, whose
  section heading is at `papers/Substratum.md:246`) it makes no statement about
  `papers/Substratum.md:100`, `:104`, `papers/SM.md:92` or `papers/SM.md:791`, about the record
  being divided, or about propagation of any kind.

**A passage that could be read as implying one of those things, but does not say it, is not
evidence.** `papers/Substratum.md:268` is a **party to** the disagreement, being `SR-1`'s fifth
statement; it is not an adjudication **of** it. Reading it as one would be the reconstructive
inference the evidence rule forbids, and it is hazard 1 exactly: the reader who knows the programme
supplying the bridging sentence the record does not contain. **This round does not supply it.**

**Where the sources disagree and the record does not adjudicate, recording the disagreement is the
outcome, not a defect to resolve.**

**The frozen sentence for the outcome reached — NO ADJUDICATION FOUND:**

> On the named and bounded search this note describes, **no passage on the record adjudicates
> between the open form and the resolution in the negative**: none states which governs, none
> states that the two are one statement, none states that the record is divided, and none states
> that the negative resolution reaches the statements carrying the open form. **The disagreement
> stands on the record unadjudicated, and recording it is this round's finding.** This round adopts
> neither form, resolves nothing, and edits no source; the propagation question stays the owner
> decision H-D named.

**Outcome: negative, as predicted. Evidence type P. High strength**, as predicted — high and not
full because the strength rests on the sweep, and the sweep is bounded by the surface named above.

**Hazard 4, observed.** The finding is *no adjudication was found on this named surface*, not *no
adjudication exists*. The surface is stated with the finding and is not a claim about what lies off
it.

## `SR-4` — the two statements of A5, re-determined

**`A5-ker`, the kernel's A5** — `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean:101–102`:

> /-- **(A5) LINEARITY**: the rule is additive over the alphabet. -/
> `def A5 : Prop := ∀ c c' : 𝒮.ι → 𝒮.V, 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'`

**`A5-ms`, the manuscripts' A5** — `papers/Substratum.md:100`:

> (A5) **Linearity.** The wave equation for $\varphi$ is linear.

**These are two statements** at the execution base: the kernel's is additivity of the substratum
rule over the alphabet, quantified over every `𝒮` of the `Substratum` structure; the manuscripts' is
linearity of the wave equation.

**The identification search, named and bounded.** The surface is
`verification/lean-mathlib/OIBridge/*.lean`, 165 modules at the base. Three searches:

1. **By name, for `A5`.** Seven modules mention `A5` at all: `A6Instantiation.lean` (15
   occurrences), `Averaging.lean` (1), `BackgroundIndependence.lean` (1), `HexLatticeGas.lean` (13),
   `HydroSourceAudit.lean` (8), `StochasticInterface.lean` (10), `SubstratumInterfaceAudit.lean`
   (8). Six declarations carry `A5` in their name: `SubstratumInterfaceAudit.A5` (`:102`, the
   predicate), `SubstratumInterfaceAudit.waveSubstratum_A5` (`:211`),
   `A6Instantiation.linkSubstratum_A5` (`:147`), `A6Instantiation.pk3e_A5` (`:306`),
   `HexLatticeGas.hexSubstratum_A5_witness` (`:641`) and `HexLatticeGas.hexSubstratum_not_A5`
   (`:685`).
2. **For the unfolded additivity hypothesis** `F (c + c') = F c + F c'`. It occurs as the predicate
   body at `SubstratumInterfaceAudit.lean:102`; as an explicit hypothesis `hF` at
   `HydroSourceAudit.lean:126`, `:138`, `:157`, `:171`; and in the prose of
   `HexLatticeGas.lean:41`, `:637`, `:681` describing the failure witness. `WeylLift.lean:236`,
   `:251` and `:575` carry additivity of `vsum` and a character identity, which are statements about
   other objects.
3. **For cross-module citation of every name found.** `waveSubstratum_A5` is cited at
   `HydroSourceAudit.lean:21`, `:99`, `:199`, `:203`, `:205`, `:211`, `:816` and at
   `StochasticInterface.lean:103`, `:135` — in every case **consumed as the additivity hypothesis**
   of a further result. `linkSubstratum_A5` is cited at `A6Instantiation.lean:309`, `:495`, `:581`
   and `pk3e_A5` at `:592`. `hexSubstratum_A5_witness` is cited at `HexLatticeGas.lean:687`, `:1192`
   and `hexSubstratum_not_A5` at `:1193`.

**The search returns no theorem identifying `A5-ker` with `A5-ms`.** Every declaration found is one
of three things: the predicate itself; an **instance** result, stating that a named carrier
satisfies the predicate (`waveSubstratum_A5` for the wave rule, `linkSubstratum_A5` and `pk3e_A5`
for the link-coupled carrier); or a **negative witness**, stating that a named carrier fails it
(`hexSubstratum_A5_witness`, `hexSubstratum_not_A5`). None of them quantifies over rules that the
kernel's `Rule` interface does not constrain to be wave-like, which is what an identification would
have to do. `waveSubstratum_A5` is the instance result for the one rule where both statements are in
play.

**This round builds no identification and records none as needed.** The definition budget is zero.

Each kernel statement cited here keeps the evidence level of the round that proved it and is
restated no more broadly than the theorem carrying it; citing it here promotes nothing. H-B's
guardrail is carried at this mention of `hexSubstratum_A5_witness` and `hexSubstratum_not_A5`: *H-B
shows that A5 is not needed to obtain a promising reversible fluid candidate with the right
microscopic ingredients; it does not yet show that A5 is unnecessary for an actual
Euler/Navier–Stokes limit.*

**The frozen sentence for the outcome reached — TWO STATEMENTS, NO IDENTIFICATION:**

> The kernel's A5 and the manuscripts' A5 are two statements at the execution base, and the named
> and bounded search of the Lean tree returns no theorem identifying them; `waveSubstratum_A5` is
> an instance result for the one rule where both are in play. This round builds no identification
> and records none as needed.

**Outcome: positive. Evidence type P. High strength**, as predicted — high and not full because the
base is later than H-D's, and the finding is a statement about the named search over the 165 modules
present at it.

## `SR-5` — the propagation surfaces, a census

**This is a census, not a propagation. This round edits none of the three files** and adjudicates no
entry as correct or incorrect.

| file | do H-D's three answers appear? | what the bounded search returned |
| --- | --- | --- |
| `../PROGRAMME.md` §8's one-line state (`:227–229`) | **no** | A search of the whole file for `H-D` returns **no occurrence**. §8's one-line state carries round H-A, at `:229` — "Round H-A, the source audit of the concrete wave representative, is executed at evidence level 2 … the advection obligation is HI conditional on `ZMod q`-linear coarse variables …" — and round H-B, at `:229` — "H-B: one candidate executed in the A1–A4, ¬A5 class; OI-compatibility of the class open (`round-h-b-reversible-fluid-substratum/result.md`)." Neither of H-D's three answers, and neither disqualification-rule consequence, appears. |
| `verification/ROADMAP.md` | **no** | A search of the whole file for `H-D` returns **no occurrence**. The file carries a hydrodynamics H-A section at `:732` and a hydrodynamics H-B section at `:749`, with their own result and preregistration pointers at `:744`, `:746`, `:768` and `:770`. |
| `verification/README.md` | **no** | A search of the whole file for `H-D` returns **no occurrence**. The file carries a hydrodynamics H-A entry at `:1983` and a hydrodynamics H-B entry at `:2279`. |

**Recorded reading 6 of the freeze is confirmed at the base**, for all three files.

**The wording for comparison.** Because H-D's three answers appear nowhere on the three files, there
is no found text to compare against `SR11-words`. `SR11-words` is quoted in full at `SR-0` above, as
quotation and not as a choice. **This round proposes, ranks and amends no wording**, and the words of
any later refresh are settled by H-D's status rule 11 and are not open.

**Hazard 5, observed.** The census noticed three surfaces lacking H-D's answers and **added them to
none of them.** `SR-5` enumerates a surface; it does not act on it. The companion failure — treating
status rule 11's wording as open — is likewise not committed: the wording is reproduced above as
quotation.

**The frozen sentence for the outcome reached — ABSENT FROM ALL THREE:**

> At the execution base, H-D's three answers appear on none of `../PROGRAMME.md` §8's one-line
> state, `verification/ROADMAP.md` or `verification/README.md`. The census is recorded; **this
> round edits none of the three**, and which later action carries out the already-worded refresh
> is left to the owner, with its surface enumerated here.

**Outcome: negative, as predicted. Evidence type P. High strength**, as predicted.

H-B's guardrail is carried at this section's mentions of H-B: *H-B shows that A5 is not needed to
obtain a promising reversible fluid candidate with the right microscopic ingredients; it does not
yet show that A5 is unnecessary for an actual Euler/Navier–Stokes limit.*

## `SR-6` — the stability of the quoted passages between H-D's base and this round's base

**The blob comparison.** H-D's mandated execution base is
`f81ed6bf660b7b324df93aa466288fe074a021b9`. The four `papers/` blobs there, and at this round's
execution base `62970976a06b3f25553970095ee23cab82100f83`:

| file | blob at H-D's base | blob at this round's base | moved? |
| --- | --- | --- | --- |
| `papers/Substratum.md` | `9ac6b732e8786897cade416b67c3f7f1df81ab84` | `9ac6b732e8786897cade416b67c3f7f1df81ab84` | no |
| `papers/SM.md` | `26d6cbfb230c105eb00a979c2b69c363568455dd` | `26d6cbfb230c105eb00a979c2b69c363568455dd` | no |
| `papers/Structure.md` | `84a7ede451a917513dd488477c93180f5f8c0486` | `84a7ede451a917513dd488477c93180f5f8c0486` | no |
| `papers/Main.md` | `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` | `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` | no |

**All four blobs are equal across the two bases**, and they are the blobs H-D's result note records
at H-D's base and the blobs this round's freeze pins. **No file differs, so no diff is taken and no
passage moved.** Every passage this note quotes from `papers/` — `Substratum.md:100`, `:104`,
`:219`, `:252`, `:264`, `:266`, `:268`; `SM.md:92`, `:236`, `:338`, `:791`; `Structure.md:219` — is
therefore byte-identical to the text at H-D's mandated execution base.

**Recorded reading 7 of the freeze is confirmed at the execution base**, which is later than the base
that reading was taken at and which sibling landings could have moved. They did not move these four.

**Hazard 8, observed.** H-D's own D1–D3 are movements of blobs between H-D's freeze and H-D's base,
which H-D diffed and recorded. They are not source disagreements and they are not this round's
subject. `SR-6` asks only whether the passages **this round quotes** moved between the two bases, and
the answer is that they did not.

**The frozen sentence for the outcome reached — IDENTICAL:**

> Every passage this note quotes from `papers/` is byte-identical to the text at H-D's mandated
> execution base, on the blob comparison recorded here.

**Outcome: positive, as predicted. Evidence type P. Medium strength**, as predicted.

## `SR-7` — the assembled reconciliation record, and the owner decisions named

### The record, assembled

**The inventory (`SR-1`, `SR-2a`, `SR-2b`).** Five statements of the entailment question stand at the
execution base — `papers/Substratum.md:100`, `papers/Substratum.md:104`, `papers/SM.md:92` and
`papers/SM.md:791` in the open form, and `papers/Substratum.md:268` resolved in the negative — each
quoted above with its coordinate and with the words carrying its form. Sixteen further coordinates
bear on the principle's status or on its relation to the `q`-size freedom without stating `Q-ent`,
each quoted and classified by its own words; among them, two say the two freedoms are instances of
one master principle and two say they are distinct. On the named and bounded surface `Q-ent` is
**posed nowhere** outside the five, and the book carries both the principle and the size freedom
**without posing it**.

**The adjudication finding (`SR-3`).** No passage on the record adjudicates between the two forms.
The disagreement stands on the record unadjudicated.

**The A5-statement finding (`SR-4`).** `A5-ker` and `A5-ms` are two statements, and the named and
bounded search of the 165 OIBridge modules returns no theorem identifying them.

**The propagation census (`SR-5`).** H-D's three answers appear on none of the three files of
`prop-surface`.

**The stability record (`SR-6`).** Every passage quoted from `papers/` is byte-identical across the
two bases.

### The three owner decisions, named and made nowhere

**Decision 1 — whether the negative resolution propagates to the statements carrying the open
form.** H-D's own words, at `../round-h-d-a5-status-adjudication/result.md:491–494`:

> **The propagation question is named here for the owner and the round stops**: five statements of
> the entailment question stand in the corpus, four in the open form and one resolved in the
> negative, and whether the negative resolution should propagate to the other four is an owner
> decision this round records and does not make.

**State: open. This round records the disagreement and makes this decision nowhere.** It adopts
neither form, ranks them in no order, states no preference between them, and recommends nothing. The
inventory above is what this round delivers to the decision, and it is an inventory and not an
argument for either side.

**Decision 2 — whether the `R7-HY*` guard family extends to prose-only rounds of this programme.**
H-D's own words, at `../round-h-d-a5-status-adjudication/result.md:917–918`:

> **Whether the `R7-HY*` family should be extended to cover prose-only rounds of this programme is
> an owner decision this round records and does not make.**

**State: open. This round makes it nowhere, and it is itself a prose-only round that adds no guard.**
It owns no seal state, creates none, and takes ownership of changing none.

**Decision 3 — which later action carries out the refresh of `../PROGRAMME.md` §8.** H-D's own words,
at `../round-h-d-a5-status-adjudication/result.md:893–896`:

> **H-D's D7, carried at this mention — decision 3, where this round records the state of that open question.**
> **The §8 refresh is therefore left to the later action status rule 11 names**, and when that action
> is taken, status rule 11 fixes the words it must carry — the three answers and **both**
> disqualification-rule consequences, in the freeze's own wording and nothing stronger.

**State: open — and only in one respect. The wording is not the open question and is not this
round's to choose.** H-D's status rule 11 already fixes the words that refresh must carry, and
`SR11-words` is that wording, quoted in full at `SR-0` above. **What H-D left open, and all that is
open, is which later action performs the already-worded refresh.** `SR-5` enumerates that action's
surface — three files, none of which carries H-D's answers at the execution base — so that the action
has its surface enumerated before it acts. **This round is not that action and does not appoint
itself that action.**

**Naming a decision is not making it, and this round makes none of the three.**

**The frozen sentence for the outcome reached — ASSEMBLED, THREE DECISIONS NAMED:**

> The reconciliation record is assembled in this note, and the three owner decisions H-D
> recorded — the propagation of the negative resolution, the reach of the `R7-HY*` guard family to
> prose-only rounds, and which later action carries out the refresh of `../PROGRAMME.md` §8 whose
> words status rule 11 already fixes — are named here and made nowhere.

**Outcome: positive. Evidence type P. Full strength, conditional on `SR-1`–`SR-6`**, as predicted.

## What these outcomes do NOT license

- **Nothing here answers the entailment question.** This round reports what each source says and
  stops. No sentence of this note states, as this round's own finding rather than as a quotation of
  a source, that the `q`-size gauge freedom entails amplitude-scale gauge, that it does not entail
  it, that the question is settled, or that the question is open.
- **Nothing here reconciles the sources.** This note does not say that the sources agree, that the
  disagreement is only apparent, that read properly the statements say the same thing, or that the
  open statements are to be read in light of the negative resolution. A reader who knows the
  programme can supply the bridging sentence; **this round may not**, and has not.
- **Nothing here is a propagation.** No source is edited, no wording is aligned, no status is
  refreshed. `SR-5` enumerates a surface; it does not act on it.
- **Nothing here bears on A5's status.** H-D's three answers stand exactly as H-D states them, at
  H-D's own scope and strength, unstrengthened, unweakened, un-re-decided and un-re-derived. The
  sentences "A5 is not a bare-OI requirement" and "A5 is QM-specific and not required by the
  hydrodynamic route" are forbidden here exactly as H-D's status rules 6 and 7 forbid them there,
  and neither is asserted.
- **Nothing here says A5 is unnecessary for an Euler or Navier–Stokes limit**, or that any candidate
  has a hydrodynamic limit. **H-B's guardrail applies at every mention of H-B:** *H-B shows that A5
  is not needed to obtain a promising reversible fluid candidate with the right microscopic
  ingredients; it does not yet show that A5 is unnecessary for an actual Euler/Navier–Stokes limit.*
- **Nothing here characterizes the substratum structure sufficient for hydrodynamics.** That is the
  programme's objective; this round delivers a source inventory and nothing more.
- **Nothing here moves an obligation.** H1–H7 keep their statuses; nothing is closed, discharged or
  relabelled, and no taxonomy label is applied to anything.
- **Nothing here scopes, consumes or depends on H3 as a candidate bridge condition.** No finding of
  this round is evidence for or against it in either direction.
- **Nothing here changes A1–A6, their statuses, or their number.** No condition is added to the
  A-list or to the C-list, and none is named.
- **Nothing here asserts a status for A6.** Whatever status the execution base carries is consumed
  unchanged.
- **Nothing here is a continuum statement.** No limit, no PDE, no scaling map, no closure; the
  `S1`–`S5` branch stays closed.
- **Nothing here bears on the OI → QM chain, Track B, Track I, Bell or gravity**, in either
  direction.
- **Nothing here promotes a cited result.** Every kernel statement cited keeps the evidence level of
  the round that proved it and is restated no more broadly than the theorem carrying it.
- **Nothing here makes an owner decision.** `SR-7` names three and makes none.
- **No label is written "for OI."** Every finding above is a statement about a named object: a
  passage, a file, a coordinate, a statement, a theorem.

## Discrepancies recorded

**Every divergence between the freeze and what the execution found at the base is recorded here and
repaired nowhere. The freeze is immutable and is unedited.**

**D1 — `verification/ROADMAP.md` is not the blob the freeze pins.** The freeze's start-state table
records `4f9af3d3e8a2d5d66ff063c94a388d2c7c04f218`; the blob at the execution base is
`c356e9b5f857ef18a992d67df613b9db96a949d7`. The diff is **31 added lines and no deletion**: an
executed-round paragraph and two link lines for a round of the **physical-realization** programme
that merged into `main` before this control plane did. **No hydrodynamics row moved, and no line this
round reads for `SR-5` moved**: the hydrodynamics H-A and H-B sections at `:732` and `:749` are
present and unchanged, and the file carries no `H-D` occurrence either before or after the addition.
The added material is **not consumed** by this round, is cited in no determination, and carries no
target — the anti-contamination invariant governs.

**D2 — `verification/README.md` is not the blob the freeze pins.** The freeze records
`585dd145186dae654f58e2dc16712550b68ec9e0`; the blob at the execution base is
`d25eb2d44d0aa324c095930f40174296fd0f2279`. The diff is **33 added lines and no deletion**, the
README entry for the same physical-realization round. **No hydrodynamics entry moved**: the H-A entry
at `:1983` and the H-B entry at `:2279` are present and unchanged, and the file carries no `H-D`
occurrence either before or after the addition. The added material is **not consumed** by this round.

**D3 — `verification/lean/edge_rigidity_probe.py` is not the blob the freeze pins.** The freeze
records `dc30d365a06cb3a118d3bdb100c18b9b8c0d799e`; the blob at the execution base is
`55e7c3e3139741521bc5aeac6add56f557be5943`. The diff is **491 added lines and no deletion**: one new
guard block for the same physical-realization round, appended after the existing blocks. **No
`R7-HY*`, `R7-A6*` or `R7-PQT` constant moved.** The file is consumed as context and is **not
modified by this round**; the probe was run at the base and printed `ALL CHECKS PASS`.

**D1, D2 and D3 share one cause**, recorded rather than inferred: the control-plane merge commit's
own message states that "The branch synchronized once, against the main it actually merges into,
after all four siblings landed. The frozen preregistration blob is unchanged by that synchronization,
and the merge touched no ROADMAP row." The start-state table was written before those siblings
landed and pins the blobs as they then stood; the base carries the blobs as they stand after. **The
table is not repaired.**

**D4 — recorded reading 3 understates what `papers/Substratum.md:266` carries.** The freeze's
recorded reading 3 says of that line that it "records the principle as adjoined, not one of Theorem
24's generators, with results invoking it conditional on it. This is a status statement, not a
statement of `Q-ent`." Re-read at the base, the line carries that status **and also** a statement
about the relation between the principle and the `q`-size freedom, in its own words: the principle
"is not one of (i)–(iv) — generator (i) over-counts … and (ii) is alphabet-*size* only". That is a
statement that the two are **distinct**, which the freeze's own `form-other` definition names as a
`form-other` example. The line is therefore recorded in `SR-2a`'s table as `form-other` carrying
both, rather than as a status statement alone. **This is recorded as a divergence from the freeze's
recorded reading and is repaired nowhere; the reading is not evidence at any level above "recorded
reading" by the freeze's own terms, and no target rests on the reading rather than on the line.**

**No other divergence was found.** Recorded readings 1, 2, 4, 6 and 7 were each re-determined at the
base and each holds: the five coordinates and their forms (reading 1); `papers/Substratum.md:264` as
a `form-other` statement (reading 2); the book's carriage of the principle across the five named
chapters and `book/ch05-gauge-structure.md`'s `form-other` statement, with `SR-2b` determining as
reading 4 leaves it to that the book does **not** pose `Q-ent` (reading 4); the absence of any H-D
row from all three of `prop-surface` (reading 6); and the equality of the four manuscript blobs
across the two bases (reading 7). Reading 5 is the freeze's own statement of what it is doing and is
carried out as stated: the surface was extended beyond H-D's to the book and the verification
corpora, and every finding above names the surface it rests on.

## The chronology control

The freeze's control, clause by clause, and what this execution did.

1. **This preregistration is merged alone.** *Verified:* the control-plane merge
   `62970976a06b3f25553970095ee23cab82100f83` (PR #635) has a diff of **exactly one added file**,
   `preregistration.md`, 788 insertions and no other path.
2. **Round H-D's control plane and result note must have merged before this execution begins.**
   *Verified:* both `../round-h-d-a5-status-adjudication/preregistration.md` and
   `../round-h-d-a5-status-adjudication/result.md` are present at the execution base at the blobs the
   freeze pins, and `git merge-base --is-ancestor f81ed6bf660b7b324df93aa466288fe074a021b9` against
   the execution base **succeeds** — H-D's mandated execution base, and with it H-D's landing, is an
   ancestor of this round's base.
3. **The mandated execution base is exactly the merge commit of this control plane's pull request.**
   *Verified:* the execution branch was created from `62970976a06b3f25553970095ee23cab82100f83` and
   from nothing else. **No merge from later `main`, no rebase, no amend, no force-push.** The branch
   will show as behind `main`; that is the ancestry this control certifies, and the resulting
   "behind" state is expected and correct.
4. **The execution's first act is to verify this file's blob at that base**, before any target is
   executed. *Verified:* `git rev-parse` of `preregistration.md` at
   `62970976a06b3f25553970095ee23cab82100f83` returns
   `d222e5c6f248bddf8327303523a71b5f82a050d4`, **equal to the blob the freeze names**. This was the
   first act of the execution and preceded every target.
5. **This note pins the freeze's blob by content** — `d222e5c6f248bddf8327303523a71b5f82a050d4` —
   **and records the base it executed on**, `62970976a06b3f25553970095ee23cab82100f83`. Both values
   appear in the start-state table above.
6. **No new guard file is added by this round, and no existing guard is modified.** *Verified:* this
   execution's diff touches **no file under `verification/lean/`** and **no `.lean` file**. It
   carries the result note alone. `verification/lean/edge_rigidity_probe.py` is consumed as context
   and is untouched; `R7-HY*`, `R7-A6*` and `R7-PQT` are read and not touched. The probe was run at
   the base and printed `edge_rigidity_probe: ALL CHECKS PASS`.
7. **Before certification the execution never absorbs later main.** *Verified:* the execution head's
   ancestry contains no merge whose second parent postdates the base; the branch's first-parent chain
   reaches the base without an intervening merge from later `main`.
8. **Under `§A.37` the landing is `E` → `L` with no archive pin**, the round being **non-sealing**.
   The round owns no seal state, creates none, and takes ownership of changing none. No guard tag is
   reserved, because the definition budget is zero and no kernel object exists for an ancestry guard
   to order.
9. **The claim is scoped to the repository record** at the execution base.

## Definition budget: **ZERO**

**No top-level definition is introduced. No Lean module is added. No existing Lean module is
edited.** No predicate of any kind is defined, and in particular **no identification between
`A5-ker` and `A5-ms` is constructed** — `SR-4` records that none stands in the tree and builds none.

**No proof placeholder, no postulated statement and no decision-procedure escape hatch appears
anywhere in this round**, for the plain reason that **no Lean is written at all**. This note states
that rather than leaving it to be inferred, and it **carries no printed-dependency line**, there
being no kernel object of this round's to print axioms for.

## Evidence level

**Type P throughout.** No target of this round is at evidence level 2. Every determination above is
carried by one of the three things the freeze's evidence rule allows: a verbatim quotation from a
pinned blob with its coordinate; a verbatim quotation from a merged result note or preregistration
with its coordinate; or an explicit recorded statement that the passage sought does not exist, on a
named and bounded search whose surface is stated with the finding.

**No kernel-dependency table appears in this note, and no printed-dependency line**, and this is
stated rather than left to be inferred. The kernel statements cited at `SR-4` carry their own
evidence level from the rounds that proved them; **citing them here promotes nothing**, and each is
reported at its own scope and is not restated more broadly than the theorem carrying it.

**Reconstructive inference carries no target of this round.** No paragraph of this note argues that
the sources must mean anything, and no determination rests on how two passages could be made
consistent. Where the record is silent, the finding recorded is that it is silent; silence is
reported as silence, never as denial and never as assent.

**Strength per target:** `SR-0` full; `SR-1` high; `SR-2a` medium; `SR-2b` medium; `SR-3` high;
`SR-4` high; `SR-5` high; `SR-6` medium; `SR-7` full, conditional on `SR-1`–`SR-6`. **No target
returned UNDECIDED.**

## What this round does not do

It does not: answer the entailment question; adopt, rank or prefer either form of it; edit any
manuscript, book chapter, programme file, roadmap, README, guard, Lean module, merged freeze or
merged result note; carry out any propagation; write or edit any Lean; re-prove any cited result;
construct an identification between the two statements of A5; define any predicate; reopen H-A or
H-B; re-decide the hydrodynamic target or any of H-D's three answers; scope, consume or depend on
H3; assert any status for A6; move, close or discharge any obligation; apply any taxonomy label; take
any limit or assert any PDE, scaling map or closure; make any of the three owner decisions it names;
say anything about Track B, Track I, Bell, gravity or singularities.
