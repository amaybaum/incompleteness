# G3-HCOUNT: does native OI dynamics justify H-COUNT-1? (plan)

**Standing.** Preregistration of a paper-only research unit (AGENTS.md §A.29, §A.31 depth-first
form). It is committed before any result. It adopts no premise, H-COUNT-1 included, and edits no
manuscript, Lean module, registry or shared record. Tiny exact symbolic checks are permitted; no
numerical search and no expensive computation is run.

- **Authorization.** Owner `amaybaum`,
  [#1169 c.7079945577](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7079945577),
  2026-11-22T13:37:40Z, Gravity (#873): "does native OI dynamics justify H-COUNT-1, in particular
  that hidden-sector counting depends only on conserved shell energy? The writer examines the open
  W1-0 conserved shell-energy obligation, tests whether an additional conserved shell variable is
  required, separates deductions from native dynamics from independently imposed thermodynamic
  assumptions, and determines whether the conditional G3-TEMP temperature law can be strengthened.
  Stop condition: a proof, a counterexample, or an explicit statement of the missing native
  mechanism. H-COUNT-1 is not adopted and no gravitational manuscript is modified without a
  separate decision." Safeguards of the same comment: paper-only; this plan committed before
  substantive research; no new numerical searches or expensive computation; independent
  separate-session review; no manuscript or ledgered-file changes, no pull requests, no merges.
- **Goal link (§A.47).** Serves G3 (#873), the vacuum-energy half of the research target. The unit
  decides whether H-COUNT-1, the premise of G3-TEMP's conditional temperature law, follows from
  OI's native dynamics or is an additional assumption, and which part of it is load-bearing. It
  does not decide which temperature law matches data.
- **Accountable Issue.** #873.
- **Branch and base.** `research/g3-hcount-20261122`, created from
  `c92dd48d0eedbe68d8539704263f6d4b49793798` (G3-TEMP accepted head, branch
  `research/g3-temp-20261122`). The G3-TEMP branch is not modified.
- **Snapshot `D`.** The papers at `c92dd48d` are those of `main` at
  `413b0bb88f39cad901befcf4684355c7ee39480b` (no paper differs). `GR:n`, `Main:n`, `SM:n`, `Sub:n`
  are lines of `papers/GR.md`, `papers/Main.md`, `papers/SM.md`, `papers/Substratum.md` there.
  All are read only.
- **Sources.** G3-TEMP `NOTE.md` and `PLAN.md` at `c92dd48d`; G3-OFFDS `NOTE.md` (as G3-TEMP cites
  it); G3-HOM `RESULT.md` (Node 1, W1-0 at RD6); G3-W1 `RESULT.md` (47 excluded classes, §4 scope);
  the W1-1 record `verification/programmes/physical-realization/w1-1-20261112/` (`STATUS.md`,
  `W1-1-REPORT-r4.md`: W1-0, W1-min, W1-min′, the H-count comparison); GR:56, GR:58, GR:60,
  GR:70, GR:74–88, GR:144; SM:292–298 (shell ergodicity, cycle structure), SM:539 (checkerboard);
  Main:736 (posit ledger, items (iv), (v), (viii), (x), (xi), (xiii)).

## Preregistered question

Q. H-COUNT-1 (G3-TEMP §3.1) states: (a) a shell energy E of the hidden sector is defined on every
admissible state, and the hidden sector's energy-dependent entropy is one history-independent,
strictly increasing function s_H(E) of E alone; (b) s_H(E) = ηA + const; (c) exact de Sitter of
every radius is admissible, with the first law at κ = 1/R and one calibration. Which components
of H-COUNT-1 follow from OI's native dynamics (the bijection φ with the posit-ledger structure of
Main:736), which are refuted by it on a stated class, and which are independently imposed? In
particular: does the native dynamics supply a conserved shell energy (W1-0), and does it force a
further conserved shell variable on which the count depends? Can G3-TEMP's conditional law,
T = 1/(8πGηR) on the counted surface (ħ/(2πR) under GR:88's calibration conditions), be derived
under weaker premises than H-COUNT-1?

## Assumptions

(N): native to the corpus at `D`, with its corpus status. (T): a thermodynamic or measure
assumption imposed independently of φ. None is adopted; each is a premise of the argument that
uses it, and every conclusion carries its premises.

| ID | Assumption | Mark | Source |
|---|---|---|---|
| N-BIJ | φ a bijection of a finite configuration set (A1 representative) | (N); total finiteness an open posit | Main §1.2; Main:736 (ii), (iii) |
| N-2ND | Second-order form x(t+1) = F(x(t)) − x(t−1), F_n reading current values at finitely many sites | (N) posit of the selected model | Main:736 (xiii) |
| N-NN | Nearest-neighbour range on the simple-cubic graph | (N) posit | Main:736 (x) |
| N-CI | Center independence: translation covariance; F_n contains no copy of x_t(n) | (N) posit | Main:736 (xi) |
| N-BIP | The coupling graph carries the checkerboard (ℤ³, or a quotient whose period vectors have even coordinate sum) | (N) condition | SM:539 |
| N-REV | Time-reversal invariance with reversal-even coarse states | (N) as used | GR:70 |
| T-SHELL | A real-valued conserved shell energy exists (W1-0) | open | GR:58, GR:88; W1-1; G3-HOM; G3-W1 |
| T-MEAS | Maximal-entropy invariant measure compatible with the records | (N) posit, "not derived" | Main:736 (iv) |
| T-MIX | Hidden-sector mixing / single-cycle sampling of shells | (N) open hypothesis | Main:736 (v); SM:292–294 |
| T-AREA | Whole-hidden-sector count equals the boundary count (W1) | additional assumption per W1-1 | GR:58; W1-1 §8 |
| G3-TEMP set | N-dS, N-FL, N-UNIV, N-AREA, N-PART, N-SLOPE, I-FLRW, as in G3-TEMP `PLAN.md` | as there | G3-TEMP |

## Decision rule (fixed now; verdict text generated from the node verdicts)

For each component of H-COUNT-1, and for the question "is a further conserved shell variable
required", one of:

- **Derived.** It follows from (N) items listed with their status; reported as conditional on
  every item used.
- **Refuted on a class.** A stated set of (N) items, on a stated class of rules or energies,
  contradicts it; the class is named exactly.
- **Imposed.** It does not follow from (N) items and is supplied only by a (T) item; the (T) item
  is named.
- **Open.** None of the above within this unit; the missing native mechanism is stated.

The strengthening question is answered **strengthened** if G3-TEMP's law is derived from a premise
set strictly weaker than H-COUNT-1 (each dropped or weakened clause named), **unchanged** if no
weaker set is found, and **weakened** if a clause of H-COUNT-1 is shown inconsistent with (N) items
so that the law loses support. The overall outcome is one of: proof, counterexample, missing
native mechanism; a mixed outcome lists each by component.

## Productivity test (§A.31, fixed in advance)

The unit is a gem iff it yields a fact strictly stronger than the restatement "H-COUNT-1 is
assumed, W1-0 is missing" (G3-TEMP §6), and that fact either (i) derives or refutes a stated
component of H-COUNT-1 from (N) items on a stated class, or (ii) derives G3-TEMP's law under a
strictly weaker premise set, or narrows the conditions under which T_A remains reachable, or (iii)
exposes a hidden assumption in H-COUNT-1, GR:58 or G3-TEMP. Otherwise it is a non-gem, recorded
only. "Open" is an allowed outcome and is not a failure of the unit.

## Nodes (depth-first order)

1. Decomposition of H-COUNT-1 into components (existence of a conserved shell energy; dependence
   on E alone; one function across histories; area count; de Sitter family and calibration), each
   with its corpus status.
2. W1-0: the corpus trace after G3-TEMP; what native structure (Node 3's) implies for the classes
   G3-W1 lists as not excluded.
3. Is a further conserved shell variable required? The conserved functions of a finite bijection;
   whether N-2ND + N-NN + N-CI + N-BIP force a second conserved shell variable for every conserved
   energy of a stated class; the RD6 instance.
4. Does a further conserved variable change the counting temperature? An exact identity relating
   the one-variable slope to the fixed-variable slopes; the role of T-MEAS and concentration; the
   sublattice symmetry.
5. Strengthening: G3-TEMP's law under a weaker premise set, if one exists, with the corrections
   stated.
6. History independence and the moving partition: whether "one function across histories" is
   native.
7. The T_A route: what a second shell variable must satisfy to produce T_A, and whether any native
   candidate satisfies it.
8. Separation of native deductions from imposed assumptions, and the overall verdict.

Each node closes with an explicit check (algebra, citation, source line, or a tiny exact check)
and a verdict with its support layer. On any branch favourable to the framework, a skeptical pass
is made before it is accepted.

## Stop conditions

- Each component and the second-variable question is answered under the decision rule.
- A branch requires a numerical search, a Lean development, an expensive computation or a
  manuscript edit: that branch stops and its item is recorded open, with the missing mechanism.
- A branch would require adopting a premise: it stops, and the premise is recorded as a hypothesis.
- Three consecutive passes yield no NEW finding (fixed point).

There is no successor round.

## Labels in the record

ESTABLISHED (derived on paper here [W], a tiny exact check [EC], a quoted standard result [L], or a
source fact [S], at the stated scope), ASSUMED (a premise of the table above or a named hypothesis,
not adopted), MISSING (supplied neither by the corpus nor by this unit). [W] derivations are not
independently reviewed and not kernel-checked. A negative result names the exact class it
excludes.
