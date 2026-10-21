# Node 9 draft: design questions for the owner, and literature status

These notes go with `PREREG.md` (DRAFT, NOT FROZEN). They are not part of the preregistration. Each open question must
be disposed of before the freeze.

## Closed by owner decision, 2026-10-21

**Q1. First model: closed.** Option A first; Option B next on the same engine and R-MENU; Option C as a side
calibration of PREREG §1.4. The option descriptions are kept below for B and C.

- **Option A** (PREREG §4): pointer x and record cells h ∈ ℤ₂^{2n}, φ = identity; reading ω(u, h) into a pointer kicks h
  along u by a fresh bath bit; local Bell branch. Its first computation is M0 (PREREG §4.1). The earlier note that the
  expected outcome is "M1/M2 pass" is withdrawn as unscoped. What is on record [rec, review of 390e252f and owner check]:
  the seven-state single-toy-bit menu admits purification with the tested partner, and its convex closure contains
  mixed states without purification among the tested pure joint states. Neither reading is a prediction for Prep(𝓘)
  under §1.2.
- **Option B: complementary destructive readouts with a coupling-locality principle (aimed at M3).** MC6 P5 on ℤ₂², with
  the principle "each coupling step reads one record cell and refreshes the others it touches", meant to justify
  withholding Y. Under generated preparations the weight *w* is set by what the operations prepare from the counting
  measure, a question MC6 and MC7 did not ask. Risks: close to the gbit (if *w* = 1 is preparable, M5-L fails); the
  principle is easy to vary on a two-cell carrier; R-MENU (ii) may fail by construction. Beyond-target prediction: the
  POM value as a function of preparation depth, against (2+√2)/4.
- **Option C: a hidden direction register under the counting measure (aimed at M3 and M5).** λ from an *N*-point
  symmetric set on a circle; the readout along a writes sign(λ·a) and resamples λ uniformly on the half-circle about the
  outcome. Parity obliviousness should hold by antipodal symmetry; the linear response 1 − θ/π bounds POM by 3/4 in the
  continuum [W, unreviewed]. Reaching (2+√2)/4 needs a Born-tuned weighting the counting measure does not supply.
  Beyond-target prediction: the linear response law instead of Malus's cos² law, raw-direct and refuted by experiment
  [Q].

**Q2. Hidden-label control: closed.** The split into K-HL0 (label response-irrelevant), K-HL1 (label readable) and
K-MENU (label reachable only through a restricted complementary set; MC6 P5 and the gbit) is accepted. Added: K-HL1
runs the premise check of PREREG §1.4. If an allowed experiment reveals parity, the POM premise fails and the score is
printed "POM premise not met", not compared with 3/4.

**Q3. Fixed prior: closed.** The hidden prior is fixed within a realization; the model starts from the counting measure
and generates every other preparation operationally. Main.md:60 makes the fixed prior a realization datum, names the
counting measure the default, and permits structured preparations. Fixing the counting measure is therefore a model
choice, not a requirement of Main.md. The draft's earlier "one realization, one prior" reading as an inference from
Main.md is replaced by this statement in PREREG §0.

**Q4. Heralded conditioning: closed.** Included from the start as generator (g6): selection on every physically
recorded outcome of nonzero probability, keeping that outcome's success probability and the actual post-measurement
state, back-action included. Control K-HERALD [rec, owner check 2026-10-21]. The earlier note that feed-forward
reproduces heralding in Option A is dropped; with (g6) included it decides nothing.

## Open before freeze

**QA. Option A's clean-ancilla declaration as a principle.** The draft declares the visible pointers, each at 0, as the
only clean ancillas, and no hidden cell supplied in a known state. R-MENU (v) needs this stated as a physical principle,
not as an unstated absence. A swap of a clean pointer with a record cell would prepare a definite record bit (the
owner's swap example); whether Π_BA's predicate excludes it is computed under R-MENU (ii), but the wording of Π_BA and of
the declaration must be fixed first.

**QB. Option A's beyond-target prediction.** Candidates: (i) |S| ≤ 2 for every composite (a raw-direct conflict with
Bell experiments [Q]); (ii) the sequential readout law on non-commuting stabilizer sequences (compare MC6 A1, 234
protocols); (iii) no-cloning or no-broadcasting of non-commuting records. Pick one, or state another.

**QC. M0's restriction criterion.** The draft criterion for "the restriction purification needs" is support ≥ 2^*n* for
every preparable state of h conditioned on all visible records, with the number of determined record functionals
printed beside it. The two are not equivalent (a support of size ≥ 2^*n* bounds the affine span from below, not
conversely). Please confirm the support form, or name another.

**QD. The construction linking POM and CHSH.** PREREG §2.4 and M5 use a construction mapping POM success *p* to S =
4(2*p* − 1) [rec, owner 2026-10-21]. It should be written out (or cited and read) before freeze if M5 or the
productivity count relies on the link.

**QE. Node-8 reference version.** K-N8 cites the r1 output; the close-out r2 output reproduces the same Pur-E and Pur-U
answers [rec, mc-node8 `probe/CHANGES-r2.md`]. Confirm whether K-N8 should be pinned to r2 at freeze. The mc-node8
review in progress may bear on this.

**Q5. Sizes, depths and ancilla counts.** The proposed parameters:
- M2 at A = one and two systems, each with a same-type purifier (*n* ≤ 4 toy bits; 256 record configurations);
- M3 decoders to depth D = 3, with stability checked at D = 4;
- equivalence and M0 at *k* ≤ 2 ancillas, halting if *k* = 1 and *k* = 2 differ; results are reported for *k* ≤ 2 only
  unless an extension argument is reviewed (PREREG §1.3).

Lemma W makes depth unbounded for equivalence within the declared model, so only decoder optimisation and M0's closure
are depth-bounded. Are these acceptable, and should *n* = 4 go to CI from the start?

**Q6. Scope of M5.** M5-L and M5-A cover POM and CHSH only, and these are linked by QD's construction. Should further
statistics be added, such as the quantum set at NPA level 1, the chained Bell inequalities, or 3-bit POM? Is M5-A's A2
form wanted as a live line, or PARKED from the start?

**Q7. M4 for Option A.** Option A is local-branch, so M4 can only FAIL there (K-BL makes a value above 2 void). A
branch-(a) composite with preparation-indexed edges is a different model, proposed as a later node with K-PR6 and M5-L as
its guards.

**Q8. Tag convention.** [Q] marks unread literature and [corpus] verbatim corpus quotes; [rec, owner …] is added for
owner-supplied checks and readings. The corpus quotes were checked at `eb19f063` (reachable from `main`;
`papers/Main.md` is byte-identical at `main` `af8c59d6`) by an ad hoc substring check at the cited lines; the Main.md:60
quotes added in this revision were checked the same way at `d53febe7`. At freeze, node 8's `quotecheck.py` should be run
with a node-9 fragment list.

**Q9. Left out to keep the node short.** The CDP per-axiom audit (MC8 §6.3–§6.4); C5-IC; the interference diagnostic;
branch-(a) composites; robust (finite-precision) noncontextuality inequalities. The last matters: under ε-agreement PNC
is vacuous (MC6 `leak.py`), so M3 is an exact-equivalence test only.

## Literature status

| source | read? | what was established |
|---|---|---|
| Spekkens et al., PRL 102, 010401 (2009), arXiv:0805.1463 | not by this session | The owner reports that Theorem 2 and its two-bit quantum example give 3/4 and (2+√2)/4 [rec, owner read 2026-10-21]. The task wording remains [Q]. Both values are also recomputed in house by K-PNC and K-QPOM |
| Spekkens, PRA 71, 052108 (2005), quant-ph/0406166 | no, [Q] | A search summary of the abstract: an operational notion of contextuality, and no-go theorems for preparations, transformations and unsharp measurements, with proofs in dimension 2 |
| Spekkens, PRA 75, 032110 (2007), quant-ph/0401052 | no, [Q] | Secondary summaries only: the knowledge-balance principle, no Bell violation or contextuality |
| Bartlett, Rudolph, Spekkens, PRA 86, 012103 (2012), arXiv:1111.5057 | no, [Q] | A search summary: classical Liouville mechanics with a restriction on second moments plus maximum entropy gives Gaussian QM ("ERL") |
| Chiribella, D'Ariano, Perinotti, PRA 84, 012311 (2011), arXiv:1011.6451 | no, [Q] | A search summary lists the axioms: causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning, and purification |

Access: at drafting, WebFetch to arxiv.org, alphaxiv.org and web3.arxiv.org failed (ENOTFOUND), and curl through the
agent proxy got a 403 at CONNECT for arxiv.org, export.arxiv.org, journals.aps.org and semanticscholar.org. One WebFetch
to arxiv.org on 2026-10-21 failed again (ENOTFOUND). Nothing load-bearing rests on a [Q] source: the numbers that decide
M3 come from in-house controls; M2's wording is gated on PC-CDP; attributions are gated on PC-POM, PC-S05, PC-SPK and
PC-BRS.
