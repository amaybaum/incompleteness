# Node 9 draft: open design questions for the owner, and literature status

These notes go with `PREREG.md` (DRAFT, NOT FROZEN). They are not part of the preregistration. Each question must be
disposed of before the freeze.

## Q1. Which model to compute first (needed for §4)

All three options are stated in OI terms. Each fixes the prior to the counting measure and generates its preparations
under §1.2.

**Option A: the boundary toy bit under symplectic back-action, Π_BA (the draft's default).**
- *Construction.* A pointer x and record cells h ∈ ℤ₂^{2n}, with φ = identity. Reading ω(u, h) into a pointer kicks h
  along u by a fresh bath bit. Record bijections preserve the readable functionals. The Bell branch is local.
- *For it:*
  - It is the smallest realization in which C5-P acts (*n* = 2), so it follows the depth-first order on the primary
    target.
  - Its controls are tight: K-SPK is its expected image.
  - It tests whether node 8's obstruction was produced by the node-8 preparation menu (point-mass priors given as
    realization data). The hand check in PREREG §0 suggests M1 passes.
  - It tests whether a principle stated in OI terms survives ancillas, composition and mechanical derivation of
    Ops(Π), through R-MENU (i)–(iv). That is new relative to MC6's A1 and P5.
- *Against it:*
  - The expected outcome is largely predictable from the toy-theory literature [Q]: M1/M2 pass, M3 fails (PNC), M4
    fails (local), and M5-A fails (Lemma F).
  - Its productivity rests mainly on gem clause (a) or (d).
  - It cannot answer the contextuality part of the question.
- *Beyond-target prediction options:* (i) |S| ≤ 2 for every composite (a raw-direct conflict with Bell experiments
  [Q]); (ii) the sequential readout law on non-commuting stabilizer sequences (compare MC6 A1, 234 protocols);
  (iii) no-cloning or no-broadcasting of non-commuting records. Pick one, or state another.

**Option B: complementary destructive readouts with a coupling-locality principle (aimed at M3).**
- *Construction.* This is MC6 P5 on ℤ₂² with a principle: "each coupling step reads one record cell and refreshes the
  others it touches". The principle is meant to justify withholding Y, which reads two cells.
- *For it:*
  - It aims directly at M3.
  - Under the generated-preparation rule the weight *w* is no longer free: it is set by what the operations can
    prepare from the counting measure. Whether *w* is then fixed is a sharp question MC6 and MC7 did not ask. They
    treated *w* as a prior datum, and MC7 screened measure readings with free priors.
  - It tests whether autonomous hidden dynamics, or composition with an ancilla, restores the withheld Y readout, as
    waiting did in K-SWAP.
- *Against it:*
  - It is close to MC6 P5 and to the gbit. If *w* = 1 is preparable, M5-L fails (POM = 1).
  - A coupling-locality principle on a two-cell carrier is easy to vary.
  - R-MENU (ii) may fail by construction.
- *Beyond-target prediction:* the POM value it predicts as a function of the preparation depth, and whether it exceeds
  (2+√2)/4.

**Option C: a hidden direction register (geometric, Kochen–Specker 1967 type [Q]) under the counting measure (aimed at
M3 and M5).**
- *Construction.* The record cells hold a direction λ from an *N*-point symmetric set on a circle. The readout along
  axis a writes sign(λ·a) into the pointer, then resamples λ uniformly on the half-circle about the outcome, using bath
  cells. A preparation is a readout followed by feed-forward.
- *For it:*
  - Parity obliviousness should hold exactly, by antipodal symmetry, over all adaptive sequences. Each readout fully
    resets the record, so later statistics depend on the outcome alone.
  - The counting measure gives the linear response P(+ | ψ, a) = 1 − θ/π. In the continuum this bounds POM by 3/4: the
    angles sum to at least 2π by the triangle inequality [W, unreviewed, drafting observation].
  - So the model is ontically contextual, its parity mixtures having different supports, while operationally it stays
    at the PNC bound. That would illustrate PREREG §1.4: records and different ontic distributions are not
    contextuality.
- *Against it:*
  - The continuum answer is known at drafting. The discretized answer must be computed, and it can overshoot or
    undershoot.
  - Reaching (2+√2)/4 needs the Lambertian weighting ∝ λ·ψ. That weighting is tuned to the Born rule (Q-typed), and the
    counting measure does not supply it. The route is closed for this model unless a principle selects that measure.
- *Beyond-target prediction:* the linear response law instead of Malus's cos² law. It is raw-direct and refuted by
  experiment [Q], a clean, decisive miss.

**Recommendation.** Option A first, then B, which takes over A's engine and R-MENU unchanged. C is a cheap one-day side
computation, worth running as a calibration of §1.4 whatever the choice.

## Q2. The countercontrol with a hidden label (correction to the design brief, owner decision needed)

The brief says a classical model with an inaccessible preparation label "must not exceed 3/4 once parity-obliviousness
is enforced over all allowed experiments". That holds in two of three cases:
- **the label is response-irrelevant**, so no allowed experiment's statistics depend on it (K-HL0). The operational
  theory is then that of the classical bit. Expected ≤ 3/4;
- **the label is readable** (K-HL1). Parity obliviousness then fails for any encoding through the label;
- **the label is response-relevant but reachable only through a restricted, complementary set of experiments.** It
  fails here. This is MC6 P5 and the gbit: a classical ontic model whose operational theory is preparation contextual
  with exact parity obliviousness over all of *its* allowed experiments, and success up to 1. This does not conflict
  with Spekkens 2005 [Q]. Contextuality is a property of the operational theory, and a contextual operational theory
  can have a classical, contextual ontological model.

The draft therefore splits the brief's single control into K-HL0, K-HL1 and K-MENU (P5 and the gbit). K-MENU passes M3
for its declared set and must be caught by R-MENU (ii) and, at *w* = 1, by M5-L. Please confirm this split.

## Q3. Generated preparations instead of realization-datum priors (PREREG §0, §1.2)

Main.md:60 allows a structured prior "as part of the realization datum". The draft reads "one realization, one prior":
the prior is the counting measure, and every other preparation comes from operations. Node 8 instead took the prior
menu (F₈ priors, point masses included) as the preparable set. That choice appears to be what put the point masses into
node 8's pure sets.

The reading is A-typed. Please confirm it, or allow a declared finite set of structured priors as part of the model.
That would bring the model back under R-MENU (iii) scrutiny.

## Q4. Heralded conditioning

The draft computes heralded (post-selected) preparations as a sensitivity row only. In Option A, feed-forward correction
reproduces them deterministically. Should heralding be admitted as a preparation (standard in operational
probabilistic theories) or kept out (MC2: renormalized post-selected branches are not outcomes of an available family)?

## Q5. Sizes, depths and ancilla counts

The proposed parameters:
- M2 at A = one and two systems, each with a same-type purifier (*n* ≤ 4 toy bits; 256 record configurations);
- M3 decoders to depth D = 3, with stability checked at D = 4;
- equivalence at *k* ≤ 2 ancillas, halting if *k* = 1 and *k* = 2 differ.

Lemma W makes depth unbounded for equivalence, so only decoder optimisation is depth-bounded. Are these acceptable, and
should *n* = 4 go to CI from the start?

## Q6. Scope of M5

M5-L and M5-A cover POM and CHSH only.
- Should further statistics be added, such as the quantum set at NPA level 1, the chained Bell inequalities, or 3-bit
  POM?
- M5-A is decided negative for finite rational models by Lemma F, as the lemma's consequence. Is the A2 form, a limit
  along a declared family, wanted as a live line, or Parked from the start?

## Q7. M4 for Option A

Option A is local-branch, so M4 can only FAIL there (K-BL makes a value above 2 void). A branch-(a) composite with
preparation-indexed edges is a different model. It is proposed as a later node, with K-PR6 and M5-L as its guards.

## Q8. Tag convention

The brief asks for [lit-read] and [Q]. Node 8 used [Q] for verbatim corpus quotes. To avoid the collision, the draft
uses [Q] for unread literature, as the brief asks, and [corpus] for verbatim corpus quotes.

The corpus quotes were checked at `eb19f063` (reachable from `main`; `papers/Main.md` is byte-identical at `main` `af8c59d6`), ten of ten, by an ad hoc substring check at the cited lines. At freeze,
node 8's `quotecheck.py` should be run with a node-9 fragment list.

## Q9. Things deliberately left out to keep the node short

- The CDP per-axiom audit (MC8 §6.3–§6.4).
- C5-IC.
- The interference diagnostic.
- Branch-(a) composites.
- Robust (finite-precision) noncontextuality inequalities.

The last matters: under ε-agreement PNC is vacuous (MC6 `leak.py`), so M3 is an exact-equivalence test only.

## Literature status

| source | read? | what was established at drafting |
|---|---|---|
| Spekkens et al., PRL 102, 010401 (2009), arXiv:0805.1463 | no, [Q] | A web search confirms title, authors, venue and the existence of a noncontextuality inequality for POM. The values 3/4 and (1+1/√2)/2 were not seen in any source text. They are recomputed in house by K-PNC and K-QPOM |
| Spekkens, PRA 71, 052108 (2005), quant-ph/0406166 | no, [Q] | A search summary of the abstract: an operational notion of contextuality, and no-go theorems for preparations, transformations and unsharp measurements, with proofs in dimension 2 |
| Spekkens, PRA 75, 032110 (2007), quant-ph/0401052 | no, [Q] | Secondary summaries only: the knowledge-balance principle, no Bell violation or contextuality |
| Bartlett, Rudolph, Spekkens, PRA 86, 012103 (2012), arXiv:1111.5057 | no, [Q] | A search summary: classical Liouville mechanics with a restriction on second moments plus maximum entropy gives Gaussian QM ("ERL") |
| Chiribella, D'Ariano, Perinotti, PRA 84, 012311 (2011), arXiv:1011.6451 | no, [Q] | A search summary lists the axioms: causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning, and purification |

Access attempts: WebFetch to arxiv.org, alphaxiv.org and web3.arxiv.org failed with DNS errors (ENOTFOUND). curl through
the agent proxy got a 403 at CONNECT for arxiv.org, export.arxiv.org, journals.aps.org and semanticscholar.org. Nothing
load-bearing rests on a [Q] source:
- the numbers that decide M3 come from in-house controls;
- the wording of M2's verdict is gated on PC-CDP;
- attributions are gated on PC-POM, PC-S05, PC-SPK and PC-BRS.
