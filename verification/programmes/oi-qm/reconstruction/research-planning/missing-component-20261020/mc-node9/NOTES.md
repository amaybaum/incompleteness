# Node 9 draft: design questions for the owner, and literature status

These notes go with `PREREG.md` (DRAFT, NOT FROZEN). They are not part of the preregistration. Each open question must
be disposed of before the freeze.

## Closed by owner decision, 2026-10-21

**Q1. First model: closed.** Option A first; Option B next on the same engine and R-MENU; Option C as a side
calibration of PREREG §1.4.

- **Option A** (PREREG §4): pointer and record cells h ∈ ℤ₂^{2n}, φ = identity; reading ω(u, h) kicks h along u by a
  fresh bath bit; local Bell branch; first computation M0 (§4.1). On record [rec, review of 390e252f and owner check]:
  the seven-state single-toy-bit menu with the tested one-toy-bit partner admits purification; its convex closure,
  against the tested pure joint states, contains mixed states without purification. Neither is a prediction for
  Prep(𝓘) under §1.2.
- **Option B (aimed at M3).** MC6 P5 on ℤ₂² with the principle "each coupling step reads one record cell and refreshes
  the others it touches", meant to justify withholding Y; *w* is set by what the operations prepare from the counting
  measure. Risks: the gbit (if *w* = 1 is preparable, M5-L fails); a principle easy to vary on two cells; R-MENU (ii)
  failing by construction. Beyond-target prediction: POM value against preparation depth, versus (2+√2)/4.
- **Option C (aimed at M3 and M5).** A hidden direction λ from an *N*-point symmetric set on a circle; the readout along
  a writes sign(λ·a) and resamples λ on the half-circle about the outcome. The linear response 1 − θ/π bounds POM by
  3/4 in the continuum [W, unreviewed]. Beyond-target prediction: the linear law instead of Malus's cos², raw-direct and
  refuted by experiment [Q].

**Q2. Hidden-label control: closed.** K-HL0, K-HL1 and K-MENU, with K-HL1 running the premise check of PREREG §1.4.

**Q3. Fixed prior: closed.** Fixed within a realization, starting from the counting measure; every other preparation is
generated. A model choice, since Main.md:60 permits structured preparations (PREREG §0).

**Q4. Heralded conditioning: closed.** Generator (g6) with back-action; control K-HERALD.

## Closed in draft revision 2, 2026-10-21

**QA. Option A's operation rule and clean-ancilla declaration: partially closed.** Two failure classifications are
defined (PREREG §2.2): an explicit violating preparation is M0 lost; a stated but unjustified operation restriction is
R-MENU unmet. The revision-1 rule ρ₀ is M0 lost by K-SYMP's witness [rec, owner check 2026-10-21]. The candidate Π_ω
(reversible record maps preserve the read/disturb pairing ω) is to be evaluated, not adopted; for it both
classifications are open. Main.md:290's update is symplectic, but that does not show that OI's available operations
enforce the rule (PREREG §4, claim table); the elementary pointer construction names the resource assumption "pointer
conjugates are never supplied clean" as a candidate independent postulate, and K-SYMP2 shows the distinction it
protects is load-bearing. Still open: QA′ below.

**QB. Beyond-target prediction: closed.** The sequential-readout repeatability postdiction of PREREG §4, derived from the
frozen read coupling; an independent postdiction, not a new quantum prediction. |S| ≤ 2 in the local branch stays
prerecorded.

**QC. Restriction criterion: closed.** Named "the proposed preparation restriction" (support ≥ 2^*n*); an invariant to
test, neither a general necessity nor a sufficient condition for purification. The determined-functional count stays a
diagnostic.

**QD. The POM–CHSH link: closed.** Written out as Lemma S [W] (PREREG §2.4): S_CHSH = 8*p* − 4, no-signalling from parity
equivalence, with the physical qualification that the common extension must exist in the model.

**QE. Node-8 reference version: closed.** K-N8 is pinned to MC8 `probe/p8s1.r2.run1.out` (sha256 `b5ce288c…bd951`) at
`78913467`, reviewed ACCEPT WITH NOTES; its 46 realization lines equal r1's [rec, coordinator check 2026-10-21]. MC8
A-5 corrects A-4's wording and changes no outcome.

## Open before freeze

**QA′. Π_ω and the resources of Option A.** Whether Π_ω is a principle or a menu (R-MENU); the clean-ancilla
declaration, including the pointer-conjugate postulate, as a principle (R-MENU (v)); the first construction task of
PREREG §4.1, the pointer coupling built from the declared lattice dynamics with clean resources accounted for, and
whether it needs any further postulate.

**Q5. Sizes, depths and ancilla counts.** The proposed parameters:
- M2 at A = one and two systems, each with a same-type purifier (*n* ≤ 4 toy bits; 256 record configurations);
- M3 decoders to depth D = 3, with stability checked at D = 4;
- equivalence and M0 at *k* ≤ 2 ancillas, halting if *k* = 1 and *k* = 2 differ; results are reported for *k* ≤ 2 only
  unless an extension argument is reviewed (PREREG §1.3);
- the reachability budgets b_r (fresh bath bits) and b_h (heralding repetitions), with the termination argument that
  makes M0's closure complete at that scope (PREREG §1.2, layer 2).

Lemma W makes depth unbounded for equivalence, not for reachability. Are these acceptable, and should *n* = 4 go to CI
from the start?

**Q6. Scope of M5.** M5-L and M5-A cover POM and CHSH only, linked by Lemma S (PREREG §2.4). Should further statistics
be added, such as the quantum set at NPA level 1, the chained Bell inequalities, or 3-bit POM? Is M5-A's A2 form wanted
as a live line, or PARKED from the start?

**Q7. M4 for Option A.** Option A is local-branch, so M4 can only FAIL there (K-BL makes a value above 2 void). A
branch-(a) composite with preparation-indexed edges is a different model, proposed as a later node with K-PR6 and M5-L as
its guards.

**Q8. Tag convention.** [Q] marks unread literature and [corpus] verbatim corpus quotes; [rec, owner …] is added for
owner-supplied checks and readings. The corpus quotes were checked at `eb19f063` (reachable from `main`;
`papers/Main.md` is byte-identical at `main` `af8c59d6`) by an ad hoc substring check at the cited lines; the Main.md:60
quotes were checked the same way at `d53febe7`, and the Main.md:290 and Main.md:320 quotes of revision 2 at `c81f2df4`.
At freeze, node 8's `quotecheck.py` should be run with a node-9 fragment list.

**Q9. Left out to keep the node short.** The CDP per-axiom audit (MC8 §6.3–§6.4); C5-IC; the interference diagnostic;
branch-(a) composites; robust (finite-precision) noncontextuality inequalities. The last matters: under ε-agreement PNC
is vacuous (MC6 `leak.py`), so M3 is an exact-equivalence test only.

## Literature status

| source | read? | what was established |
|---|---|---|
| Spekkens et al., PRL 102, 010401 (2009), arXiv:0805.1463 | not by this session | The owner reports that Theorem 2 and its two-bit quantum example give 3/4 and (2+√2)/4 [rec, owner read 2026-10-21]. The task wording remains [Q]. Both values are also recomputed in house by K-PNC and K-QPOM |
| Spekkens, PRA 71, 052108 (2005), quant-ph/0406166 | no, [Q] | A search summary of the abstract: an operational notion of contextuality, and no-go theorems for preparations, transformations and unsharp measurements, with proofs in dimension 2 |
| Spekkens, PRA 75, 032110 (2007), quant-ph/0401052 | no, [Q] | Secondary summaries only: the knowledge-balance principle, no Bell violation or contextuality; PREREG §4 (ii)'s expected M3 FAIL of Option A rests on this |
| Bartlett, Rudolph, Spekkens, PRA 86, 012103 (2012), arXiv:1111.5057 | no, [Q] | A search summary: classical Liouville mechanics with a restriction on second moments plus maximum entropy gives Gaussian QM ("ERL") |
| Chiribella, D'Ariano, Perinotti, PRA 84, 012311 (2011), arXiv:1011.6451 | no, [Q] | A search summary lists the axioms: causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning, and purification |

Access: at drafting, WebFetch to arxiv.org, alphaxiv.org and web3.arxiv.org failed (ENOTFOUND), and curl through the
agent proxy got a 403 at CONNECT for arxiv.org, export.arxiv.org, journals.aps.org and semanticscholar.org. One WebFetch
to arxiv.org on 2026-10-21 failed again (ENOTFOUND). Nothing load-bearing rests on a [Q] source: the numbers that decide
M3 come from in-house controls; M2's wording is gated on PC-CDP; attributions are gated on PC-POM, PC-S05, PC-SPK and
PC-BRS.
