# A6. Disclosure of evaluations made before acceptance

**Governs:** base line 252 (the row "No execution before authorization") and base lines 303–313 ("Drafting checks").

**Addition.** Line 312's "No candidate row was evaluated" is the statement of the base's writer. Before the base was
accepted on 2026-11-02, candidate rows were evaluated elsewhere:

- the base's independent review (#1031 comment 6567537517), hand check HC-A, evaluated two B-pl rows: `π_0`, with
  `μ(E=0) = 1/8` and `NB` false, and P3, with `μ_O(E=0) = 1/4` and `NB(μ_O)` false;
- a coordinating-session paper diagnostic marked UNREVIEWED, #1031 comment 6567152798 (posted 01:49Z), evaluated P3 at
  the instance; #914 comment 6567198108 cites it.

P3's rule was fixed by K-12(b) (#914 comment 6566997020, posted 01:36Z) before both, and P3's rows are listed as fixed in
advance (lines 232–235). No P1 member row is reported evaluated in either.

**Status of the hand checks.** HC-1 (lines 303–310) and the review's HC-A to HC-D are computational claims with no
retained recipe or output. They are provenance and are not a ground for any gate. The values the controls use are
derived on paper in `verification/programmes/oi-qm/reconstruction/k1-rdy-pref-proofs-20261105/PROOFS.md`, on `main` at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` (its independent review,
model-authored: `REVIEW.md` §1 in the same directory): `E` (§1),
CC-ABS's `r(w)` (§4) and the shell counts of CC-LEDGER (§5). Each control's pass condition is decided at execution.

**Line 252.** The drafting log of this round, from `D` to `F`, lists reads and paper derivations only.
