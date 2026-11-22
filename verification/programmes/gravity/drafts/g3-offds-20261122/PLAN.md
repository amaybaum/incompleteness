# G3-OFFDS: the off-de-Sitter horizon functional, temperature and exchange law (plan)

**Standing.** Preregistration of a paper-only research unit (AGENTS.md §A.29, §A.31 depth-first
form). It is committed before any result. It adopts no premise and edits no manuscript, Lean
module, registry or shared record.

- **Authorization.** Owner `amaybaum`,
  [#1169 c.7076731666](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7076731666),
  2026-11-22, item 2, Gravity (#873): "The earlier prohibition on new gravitational-mechanism units
  (c.7044998279) is lifted explicitly for this one bounded, paper-only investigation. Investigate
  the off-de-Sitter energy functional, the horizon temperature and the exchange law, and whether
  they discriminate among G3-HOM's three completions. No new physical premise may be adopted. No
  numerical experiment and no manuscript change is authorized." Common safeguards: item 3 of the
  same comment. No successor round (item 5).
- **Accountable Issue.** #873.
- **Snapshot `D`.** `main` at `413b0bb88f39cad901befcf4684355c7ee39480b`. `GR:n` is line `n` of
  `papers/GR.md` there; `Str:n` of `papers/Structure.md`. Both are read only.
- **Sources.** G3-HOM, `verification/programmes/gravity/drafts/g3-hom-20261119/RESULT.md` (R1–R3,
  Node 4); G3-W1, `verification/programmes/gravity/drafts/g3-w1-20261120/RESULT.md` (47 excluded
  classes of conserved additive real quantity); G3-CF,
  `verification/programmes/gravity/drafts/g3-coupling-feasibility-20261118/G3-COUPLING-FEASIBILITY.md`;
  #873's body and its calculation milestone; GR:40, GR:56, GR:58, GR §3.1, §7.1, §7.2; Str:409, Str:459.
- **A1 retirement ledger check.** `origin/research/a1exit-deletion-20261121` at
  `fef0f1589d66ae6e120b14e73b0ebb70b316e4c7`, file
  `verification/audits/foundations/a1exit-deletion-20261121/ledger.json`, was read before this
  commit. It names 44 paths. None lies under `verification/programmes/gravity/`, and none is a path
  this unit writes. This unit writes only inside
  `verification/programmes/gravity/drafts/g3-offds-20261122/`.

## Goal link (§A.47)

The item served is G3 (#873), the vacuum-energy half of OI's research target (§A.29): whether the
horizon budget of GR §7.2 can act as a gravitating homogeneous source with a definite w(z) and
Λ_eff. G3-HOM Node 4 named the missing input as the off-de-Sitter surface, its temperature and the
exchange law. This unit decides, on paper, whether the corpus together with standard results fixes
those three inputs and thereby selects one of G3-HOM's completions, or which input is minimal for
selecting one. It does not decide which completion matches data.

## Preregistered question

Q. For the three completions of G3-HOM,

- R1: the Hubble-radius (apparent-horizon) rule, E = S·T with T = H/2π, which G3-HOM 2.1
  identifies with the Misner–Sharp mass;
- R2: E = S·T_A on the apparent horizon with GR:56's Kodama–Hayward temperature
  T_A = (H/2π)|1 + Ḣ/(2H²)|, giving a w = 0 tracker as a separate component;
- R3: E = S·T on the event horizon with T = 1/(2πR_E), Li's c = 1 law,

identify (a) the off-de-Sitter energy functional and the surface that carries it, (b) its
temperature on a horizon with no Killing field, and (c) the exchange law between the attributed
component and matter, as far as the corpus and standard results fix them; and decide whether (a)–(c)
discriminate among R1–R3.

**Decision rule (fixed now; the verdict text is generated from the node verdicts).**

- *Selected.* Exactly one of R1–R3 is consistent with the listed inputs together with one named
  selection premise taken from the standard literature, and each other candidate contradicts a
  listed input or that premise. The premise is named, labelled (I) or (N) with its source, and not
  adopted.
- *None selected.* At least two candidates stay consistent with every listed input under every
  premise examined. The verdict then names the minimal discriminating input: the smallest subset of
  {surface, temperature, exchange law} whose specification separates them.
- *INCONCLUSIVE.* The consistency of some candidate with the inputs cannot be decided on paper
  within this unit.

A selection that holds only under a named premise is reported as conditional on it. A candidate is
"excluded" only for the class of constructions stated where it is excluded.

## Assumptions

Each is marked (N), native to the corpus at `D`, or (I), imported from the literature or from a
supplied background. None is adopted by this unit; each is a premise of the paper argument that
uses it.

| ID | Assumption | Mark | Source |
|---|---|---|---|
| A-FLRW | The emergent background is flat FLRW with supplied H(t); Einstein's equations with total (ρ, p) | (I) | Supplied background, as in GR §7.2 and G3-HOM |
| A-FL | Horizon first-law normalization dE = κ dA/(8πG) and area entropy S = A/(4G) on the calibration | (N) conditional | GR §3.1, §5 (under H-count and the GR §8.5 conditions) |
| A-dS | Exact-de-Sitter calibration: the attributed component alone reproduces ρ = 3H²/(8πG), w = −1 | (N) | GR:56, G3-HOM 3.3 |
| A-PART | The causal partition is the cosmological event horizon, when present | (N) | GR:40 |
| A-AREA | The counted area is that of the apparent horizon R_A = 1/H | (N) | GR:56 |
| A-TA | The flat-FLRW apparent-horizon temperature is T_A = (H/2π)\|1 + Ḣ/(2H²)\| | (N) as quoted; (I) in origin | GR:56, citing the Kodama–Hayward surface gravity |
| A-KH | Kodama–Hayward completion: in spherical symmetry the Kodama vector gives a conserved current whose charge is the Misner–Sharp mass; the horizon is the trapping horizon; κ is the Kodama–Hayward surface gravity; the first law is Hayward's unified first law | (I) | Kodama, Prog. Theor. Phys. 63, 1217 (1980); Hayward, PRD 53, 1938 (1996); Hayward, CQG 15, 3147 (1998) |
| A-CK | Cai–Kim apparent-horizon first law: −dE = T dS with heat the matter flux at fixed radius and T = 1/(2πR_A) | (I) | Cai and Kim, JHEP 02 (2005) 050 |
| A-HDE | Holographic attribution ρ = λ S·T/V spread uniformly (the family of G3-HOM Node 4) | (I) | G3-HOM; Li (2004); Hsu (2004) |
| A-Q | Exchange laws of the form Q in ρ̇_x + 3H(1 + w)ρ_x = −Q | (I) | GR:382 (Type I examples); interacting holographic literature |

A-KH and A-CK are candidate selection premises, examined and not adopted. GR:56 states that a
Kodama–Hayward extension of the calibration "is not established here"; the unit does not establish
it.

## Productivity test (§A.31, fixed in advance)

The unit is a gem iff it yields a fact strictly stronger than the restatement of G3-HOM Node 4 ("the
surface, temperature and exchange law are missing"), and that fact either (i) excludes at least one
of R1–R3 for a stated class under a named premise, (ii) shows that one of the three missing inputs
is not needed, or is fixed, for a stated family, or (iii) exposes a hidden assumption of G3-HOM,
GR §7.2 or GR:56–58. Anything else is a non-gem (coherence relabelling), recorded only.
INCONCLUSIVE is an allowed outcome and is not a failure of the unit.

## Nodes (depth-first order)

1. The energy functional and its surface: what the corpus states off de Sitter; what A-KH and A-CK
   supply; whether E = S·T is a first-law energy off de Sitter.
2. The temperature on a non-Killing horizon: T_A against 1/(2πR), on the apparent and event
   horizons; whether the temperature is fixed by first-law consistency alone.
3. The exchange law: what A-KH fixes; what the exact-de-Sitter control fixes; how the w(z) of each
   candidate depends on Q.
4. Discrimination: apply the decision rule.
5. Consistency with W1-0 and G3-W1's exclusions; consequence for GR:58's counting derivation off de
   Sitter.

Each node closes with an explicit check (algebra, citation or source line) and a verdict. On the
branch most favourable to the framework, a skeptical pass is made before it is accepted.

## Stop conditions

- The question is answered under the decision rule.
- A branch requires a computation, a numerical experiment, a Lean development or a manuscript edit:
  that branch stops and its item is recorded MISSING.
- A branch would require adopting a premise: it stops, and the premise is recorded as a hypothesis.
- Three consecutive passes yield no NEW finding (fixed point).

## Labels in the record

ESTABLISHED (derived on paper in the record, or a quoted standard result, at the stated scope),
ASSUMED (a premise of the table above), MISSING (not supplied by the corpus or by this unit). Paper
derivation, literature and conjecture are kept distinct. A negative result names the exact class of
constructions it excludes.
