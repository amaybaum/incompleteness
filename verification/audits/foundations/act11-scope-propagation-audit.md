# Act 11 scope propagation — relative-evolution nonuniqueness and the non-Markovianity vocabulary

Owner-called, publication-only, written from `main` at
`e4e04ebcef936bce2fc27f61ed56f83ca8562a4d`, the merge of Track B act 11 (#589).
This file is committed alone before any manuscript is touched.

The round propagates two already-settled scope results and does **no new mathematics**.

1. **Act 11 / `GL2`:** visible OI data plus ordinary coherent lifting do not by themselves select a
   unique relative quantum evolution. The proved witness consists of two coherent lifts of the same
   visible family, related by a time-dependent visibility-preserving right action in the strong
   anchored class, whose frozen visible relative candidate differs. `GL3` separately proves that a
   constant right action cancels from every relative object. `GI2` is a lift-space result only: its
   own theorem proves that its exhibited non-weak-gauge pair has identical relative objects at every
   pair of times. The stronger combined target — same visible family, outside the weak class, and
   different relative evolution — remains open.
2. **P-indivisibility / non-Markovianity scope:** stochastic P-indivisibility is not generic quantum
   non-Markovianity. For general CPTP families a CP-divisible evolution can induce a P-indivisible
   computational-basis population process because the intermediate quantum map may consume
   coherences absent from the population law. Inside the framework's diagonal-preserving /
   permutation-dilation class, P-indivisibility is a valid obstruction to a CPTP intermediate map;
   outside that class it is not to be identified with generic open-system non-Markovianity.
   Accessible finite-horizon memory / information backflow, recurrence-scale stochastic
   P-indivisibility, and generic quantum non-Markovianity are therefore three distinct notions.

The authoritative inputs are unchanged and are consumed, not re-adjudicated:

- `verification/programmes/oi-qm/track-b/act-11-coherent-lift-gauge/result.md` and
  `OIBridge/CoherentLiftGauge.lean` at the merge above;
- the existing Main scope remark headed **“P-indivisibility is not quantum non-Markovianity”** and
  its exact Hadamard countercontrol in `papers/oi_lattice_code/foundations/c1_cp_scope_probes.py`;
- the existing architecture guard that rejects the generic implication
  “CP-indivisibility implies non-monotonic trace distance” and keeps the ancilla-assisted
  CP-divisibility witness separate from system-only trace-distance revival.

## The items, fixed in advance

### Item 1 — Main: state the Act 11 boundary where the equivalence is stated

At the finite observable-law equivalence / operational-completion discussion in `papers/Main.md`,
state in manuscript voice:

> The exact correspondence `S ⇔ D ⇔ Q_fb` is a representability theorem at the finite
> observable-law layer, not a selection theorem for relative unitary evolution. For dilated
> processes, the same visible family can admit coherent unitary lifts whose relative candidates
> differ under a time-dependent visibility-preserving deformation. Ordinary coherence therefore
> does not by itself make the relative evolution unique. A constant deformation cancels from the
> relative object. A uniqueness claim needs an additional selection condition beyond visible-law
> representability and ordinary coherence.

The same paragraph must immediately bound itself:

- it does **not** alter `S ⇔ D ⇔ Q_fb` as the exact finite observable-law correspondence;
- it does **not** say OI and QM are inequivalent;
- it does **not** say what the additional condition is;
- it does **not** say a connection / gauge fixing cannot suffice;
- `GI2` is **not** used as a relative-evolution no-go;
- the stronger pair that is both outside the weak class and different in relative evolution remains
  open.

The abstract / introduction summary is corrected only as needed so that no sentence reads as though
finite-law representability plus an arbitrary coherent dilation already selects a unique physical
relative evolution. The existing statement that full operational QM requires additional completion
structure is preserved and sharpened, not replaced.

### Item 2 — the explanatory and book mirrors of the Act 11 boundary

Propagate the same bounded statement, at the appropriate level of detail, to the maintained mirrors
that summarize the Main equivalence:

- `papers/Explainer.md`;
- `book/ch01-observation.md`;
- `book/ch00-introduction.md` **only if** its current summary implies selection of a unique relative
  quantum evolution rather than representability;
- `book/glossary.md`, in the characterization / correspondence entries as needed;
- `book/ch09-universality.md` and `book/ch18-beyond.md` **only where** their current summaries turn
  representation into uniqueness;
- `README.md`, if the one-line Main summary would otherwise invite that reading;
- `book/The-Incompleteness-of-Observation-FULL.md` at every mirror of a changed book passage.

Legitimate statements of finite-law representability, the operational completion theorem under its
separate added principles, and exact fixed-basis Born representation survive unchanged unless their
local wording conflates representation with selection.

### Item 3 — make the non-Markovianity vocabulary unambiguous corpus-wide

The manuscript hierarchy is fixed as follows:

1. **Accessible memory / information backflow** — the framework's finite-horizon visible-law notion
   used by the characterization theorem and the C1/C3/C4 memory discussion.
2. **Stochastic P-indivisibility** — failure of stochastic divisibility of the visible population
   law, including the recurrence-scale theorem on a fixed finite reversible representative.
3. **Generic quantum non-Markovianity** — an open-system quantum notion whose exact meaning depends
   on the quantum divisibility / information-backflow criterion being used.

The round must not write any unconditional equivalence among those three notions.

The existing Main scope remark is the anchor and is preserved in substance. At the first summary
surface in each maintained document that currently says “accessible non-Markovianity” or simply
“non-Markovianity” for the framework's finite-horizon theorem, either:

- replace the phrase by **accessible finite-horizon memory / information backflow**, or
- retain “accessible non-Markovianity” only with an explicit local definition that this is the
  framework's visible-law memory/backflow term and **not** generic CPTP non-Markovianity.

The recurrence/P-indivisibility theorem is then named separately where relevant. In particular the
round must preserve the already-established distinction that C1/C3/C4 support the accessible-memory
statement, while recurrence/non-permutation hypotheses are what carry the P-indivisibility result.

Known surfaces from the pre-edit census that must be checked, whether or not each ultimately needs a
word change:

- `papers/Main.md`, `papers/Explainer.md`, `papers/GR.md`, `papers/Substratum.md`;
- `README.md`;
- `book/ch01-observation.md`, `book/glossary.md`, `book/appendix-b-derivations.md`,
  `book/appendix-c-objections.md`, `book/ch09-universality.md`, `book/ch18-beyond.md`;
- every corresponding occurrence in `book/The-Incompleteness-of-Observation-FULL.md`.

The execution must also grep all `papers/*.md`, `papers/*.tex`, `book/*.md`, the full-book source,
and maintained generated forms for paraphrases. A hit not listed above is not exempt: it is either
corrected or recorded as a legitimate non-target use.

### Item 4 — preserve the quantum divisibility scope exactly

Where the stochastic/quantum bridge is explained, the admissible statement is:

> In the framework's diagonal-preserving quantum realizations, a hypothetical CPTP intermediate map
> induces a stochastic intermediate map on the visible diagonal algebra; therefore stochastic
> P-indivisibility rules out CP-divisibility for that class.

The following stronger readings are forbidden:

- `P-indivisible ⇔ quantum non-Markovian` for arbitrary CPTP families;
- `CP-indivisible ⇒ system-only trace-distance revival` as a necessary implication;
- C1–C4 alone imply recurrence-scale P-indivisibility;
- generic quantum non-Markovianity is synonymous with the framework's accessible-memory theorem.

The existing Hadamard counterexample and the ancilla-assisted CP-divisibility qualification remain
available as the controls; they are not weakened or removed.

### Item 5 — verification / registry / generated surfaces

In the same execution commit:

- move the Act 11 census family from `kernel-only` to the propagated/current state with manuscript
  anchors actually created by this round; the theorem/evidence scope remains exactly that of the
  merged result;
- add a propagation guard, `R7-A11P` (name may be mechanically adjusted only for collision), that
  pins the Act 11 boundary, `GI2`'s lift-space-only reading, the stronger open target, and the
  three-level non-Markovianity vocabulary, with mutation controls for the principal over-readings;
- add the round to `verification/README.md` in the existing propagation-round style;
- rebuild every affected `.tex` / `.pdf` and the book through the canonical `build.sh` route, or
  fail the round. No source/generated mismatch is admissible.

No frozen Track B control plane or result note is edited.

## The constraints, fixed in advance

- **Publication-only.** No Lean theorem, definition, proof, probe result, source adjudication, or
  roadmap research status is added, changed, or removed.
- **No new P0 answer.** The combined target “same visible + outside weak class + different relative
  evolution” remains open. This propagation round does not search for it.
- **No new physical interpretation.** In particular, no statement that a connection, gauge choice,
  channel selection, or any named mechanism is sufficient or insufficient is introduced.
- **No generic non-Markovianity claim.** The manuscript may use “accessible non-Markovianity” only
  as a locally defined framework term for visible finite-horizon memory/backflow.
- **Manuscript voice only.** No Act numbers, theorem labels (`GL2`, `GI2`, etc.), kernel identifiers,
  review history, branch/PR language, or verification process appears in manuscript prose.
- **Correct forward, do not narrate.** Superseded wording is replaced in place; the manuscript does
  not explain that an earlier version said something stronger.
- **Whole-corpus propagation.** Changed book passages are mirrored in `FULL.md`; generated forms are
  rebuilt; legitimate uses of “non-Markovianity” in external/general discussions are preserved.

## Tests, fixed in advance

**E1 — Act 11 boundary.** Main and every maintained equivalence summary that requires the correction
state representability ≠ unique relative-evolution selection; ordinary coherent lifting is
insufficient for uniqueness; the added condition is unnamed. Admissible outcome: all relevant
surfaces agree.

**E2 — GI2 bound.** No manuscript or summary says that the lift-space result proves non-gauge
ambiguity in relative evolution, that the missing structure is larger than gauge fixing, or that a
connection cannot suffice. The stronger combined target is explicitly open at the principal Main /
Explainer / book statement. Admissible outcome: zero over-readings.

**E3 — three-level vocabulary.** Principal explanatory surfaces distinguish accessible
finite-horizon memory/backflow, stochastic P-indivisibility, and generic quantum non-Markovianity.
Admissible outcome: distinction explicit; no unconditional equivalence among the three.

**E4 — quantum bridge scope.** The diagonal-preserving hypothesis travels with the
P-indivisibility ⇒ CP-indivisibility statement; the Hadamard counterexample survives; system-only
trace-distance revival is not presented as necessary for CP-indivisibility. Admissible outcome: all.

**E5 — C1/C3/C4 scope.** No manuscript says C1/C3/C4 alone imply recurrence-scale
P-indivisibility. Their characterization statement is in the accessible-memory/backflow currency;
recurrence/non-permutation assumptions are named separately where P-indivisibility is invoked.
Admissible outcome: zero conflations.

**E6 — mirrors and registry.** Changed markdown, paper `.tex`, book full source, PDFs, census,
verification README and guard all agree; the Act 11 census entry has real manuscript anchors and no
stronger status than the merged theorem. Admissible outcome: all.

**E7 — re-grep.** The execution reports the corpus-wide surviving counts for “accessible
non-Markovianity”, “P-indivisib*”, “CP-indivisib*”, “relative evolution”, and the principal forbidden
paraphrases. Every survivor is classified as intended or legitimate non-target use. Admissible
outcome: no stale contradictory surface.

**E8 — checks.** Release gate, foundations probes, manuscript/architecture guards, census, canonical
builds and dropped-glyph checks all green. No kernel count change attributable to this publication
round. Admissible outcome: all green.

## What the round does not do

It does not prove a new theorem, close P0, decide the stronger combined target, choose a connection
or gauge principle, revise the finite observable-law equivalence, identify P-indivisibility with a
generic notion of quantum non-Markovianity, reopen the Bell/locality corrections, change D3 or D5,
or propagate any stronger interpretation of Act 11 than the merged result permits.

Status: preregistered; manuscript execution follows only after this file exists as its own commit.
