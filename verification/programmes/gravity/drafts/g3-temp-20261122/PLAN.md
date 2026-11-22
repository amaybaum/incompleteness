# G3-TEMP: does OI's construction fix a temperature law on a non-Killing horizon? (plan)

**Standing.** Preregistration of a paper-only research unit (AGENTS.md §A.29, §A.31 depth-first
form). It is committed before any result. It adopts no premise, runs no computation, and edits no
manuscript, Lean module, registry or shared record.

- **Authorization.** Owner `amaybaum`,
  [#1169 c.7078857457](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7078857457),
  2026-11-22, Gravity (#873): "A native temperature law on a non-Killing horizon, tested and not
  assumed", building on G3-OFFDS at `9b84dbe9`. Safeguards of the same comment: paper-only, a
  preregistered plan with explicit assumptions and a stop condition, a negative result names the
  exact class it excludes, no edit to `papers/`, `book/` or any A1-retirement ledger file, no
  computation, no PR, no merge, no comments or description edits, independent review in a separate
  session, and a positive result authorizes no implementation. Write integrity: #1169 c.7076910606
  (§A.26 halt; branch pushes verified byte for byte).
- **Accountable Issue.** #873.
- **Branch and base.** `research/g3-temp-20261122`, created from `9b84dbe9` (G3-OFFDS head). The
  G3-OFFDS branch is not modified.
- **Snapshot `D`.** The papers at `9b84dbe9` are those of `main` at
  `413b0bb88f39cad901befcf4684355c7ee39480b` (no paper differs). `GR:n`, `Main:n`, `Sub:n` are lines
  of `papers/GR.md`, `papers/Main.md`, `papers/Substratum.md` there. All are read only.
- **Sources.** G3-OFFDS `NOTE.md` at `9b84dbe9` with its reviews (#1545 c.7076925155,
  c.7076975935, c.7076996839); G3-HOM `RESULT.md` and G3-W1 `RESULT.md` under
  `verification/programmes/gravity/drafts/`; W1-0 as recorded in G3-HOM Node 1; GR:40, GR:56, GR:58,
  GR §2.3 (GR:60–90), GR §3.1–3.2 (GR:96–150), GR §7.2; the observer definition, Lemmas 1–3 and the
  partition-relativity lemma of Main §1.2–1.4; Sub on the classical horizon thermodynamics.
  Literature as cited in `NOTE.md`.
- **A1 retirement ledger check.** `origin/research/a1exit-deletion-20261121` was fetched read-only
  at `b1b0522dc8bfab5b4972a4b0d46b328e2a7545a7`, and
  `verification/audits/foundations/a1exit-deletion-20261121/ledger.json` there was read before this
  commit. It names 44 paths. The only gravity path among them is `book/ch07-gravity.md`. None lies
  under `verification/programmes/gravity/`, and none is a path this unit writes. This unit writes
  only inside `verification/programmes/gravity/drafts/g3-temp-20261122/`.

## Goal link (§A.47)

The item served is G3 (#873), the vacuum-energy half of OI's research target (§A.29). G3-OFFDS
found that, without an imported selection premise, the single input deciding between G3-HOM's
completions is the temperature law on a non-Killing horizon (Kodama–Hayward T_A against the
1/(2πR) branch, with the surface needed only in the second). This unit decides, on paper, whether
OI's own construction supplies that input, excludes a candidate, or leaves it undetermined and, if
so, which native ingredient is missing. It does not decide which law matches data.

## Preregistered question

Q. Using only native ingredients (the substratum dynamics, the observer interface and the
trace-out structure, together with the named conditions under which the corpus states its horizon
thermodynamics), does OI fix the temperature T of a non-Killing horizon (the flat-FLRW apparent
horizon R_A or event horizon R_E with Ḣ ≠ 0)? In particular, does it fix T as the Kodama–Hayward
T_A = (H/2π)|1 − ε/2| (ε ≡ −Ḣ/H²), as 1/(2πR) on some surface, or as neither?

## Assumptions

(N): native to the corpus at `D`, with its corpus status. (I): imported. None is adopted by this
unit; each is a premise of the argument that uses it, and every conclusion carries its premises.

| ID | Assumption | Mark | Source |
|---|---|---|---|
| N-OBS | Observation (S, φ, V); finite visible sector (Lemma 1); partition V/H (Lemma 2); bijective representative with selected counting measure (Lemma 3) | (N); Lemma 3's measure is a selection principle, total finiteness an open posit | Main §1.2 |
| N-TRACE | The reduced law T(φ, P, μ_H) is fixed by dynamics, partition and hidden prior; any finite-horizon law has a finite reversible realization | (N), proved (representation equivalence, intervention dilation) | Main §1.4, §1.5, §3.4; GR:76 |
| N-FL | Horizon first law dE = κ dA/(8πG), area count s = σA/ε², hence T_cl = ε²κ/(8πGσ) | (N) conditional; κ an input | GR §3.1 (Jacobson-type) |
| N-COUNT | H-count: the energy-dependent entropy of the hidden sector at the shell scale is the boundary count σA/ε², with E the horizon first-law energy; T_micro = (∂s_H/∂E)⁻¹ | (N) named condition, stated on exact de Sitter | GR:58 |
| N-SLOPE | H-slope / H-spectrum: the observer's infrared detailed-balance slope equals the KMS period τ_K = 2π/κ | (N) named condition; underivable from S1–S4 | GR:74–76, GR:144 |
| N-FRAME | H-frame: the preferred foliation is the comoving one | (N) named condition | GR:88, GR:470 |
| N-UNIV | The calibrated action scale a_* = τ_K/β_E is universal | (N) as stated | GR:78 |
| N-dS | Exact-de-Sitter calibration, where R_E = R_A = 1/H and the Killing structure exists | (N) | GR:56 |
| N-AREA | The counted area is that of R_A | (N) | GR:56 |
| N-PART | The causal partition is the event horizon | (N) | GR:40 |
| I-FLRW | Flat FLRW background with supplied H(t) | (I) | GR §7.2, G3-HOM, G3-OFFDS |
| I-KH | Kodama–Hayward surface gravity and unified first law | (I), comparison only | Kodama (1980); Hayward (1998) |
| I-CK | Cai–Kim apparent-horizon first law with T = 1/(2πR_A) | (I), comparison only | Cai–Kim (2005) |
| I-QFT | Detector, tunnelling or peeling temperatures of quantum fields on dynamical backgrounds | (I), comparison only | literature cited in `NOTE.md` |

I-KH, I-CK and I-QFT appear only as labelled comparisons, never as a premise of a native
conclusion. GR:56's quoted T_A (A-TA of G3-OFFDS) is treated as I-KH, since GR:56 attributes it to
the Hayward–Kodama surface gravity and states that the extension "is not established here".

## Decision rule (fixed now; the verdict text is generated from the node verdicts)

For each premise set examined, one of:

- **Derived.** A temperature law on a non-Killing horizon follows from (N) items alone, each named
  with its corpus status; the conclusion is reported as conditional on every named condition it
  uses.
- **Excluded.** A candidate law (T_A, or 1/(2πR) on a stated surface) contradicts a stated set of
  (N) items; the excluded class of constructions is named exactly.
- **INCONCLUSIVE.** Neither, within this unit; the verdict names the exact native ingredient whose
  absence leaves the law undetermined.

The unconditional verdict is the one for the premise set N-OBS + N-TRACE alone (the bare
construction). Results under named conditions are reported separately and never as unconditional.

## Productivity test (§A.31, fixed in advance)

The unit is a gem iff it yields a fact strictly stronger than the restatement "a native
non-Killing temperature law is MISSING" (G3-OFFDS §6), and that fact either (i) derives or excludes
a candidate law for a stated class under named (N) items, or (ii) shows that a stated native
ingredient cannot supply the law, or (iii) exposes a hidden assumption in GR:56–58, GR §3.2 or
G3-OFFDS. Otherwise the result is a non-gem, recorded only. INCONCLUSIVE is an allowed outcome and
is not a failure of the unit.

## Nodes (depth-first order)

1. Inventory: which native objects carry a temperature, and whether each fixes κ or takes it as
   input.
2. The bare construction (N-OBS + N-TRACE): does it force any rate-ratio law?
3. The counting route (N-COUNT) extended off de Sitter: what T it gives, under which premises.
4. The dynamical route (N-SLOPE, N-FRAME, N-UNIV): what fixes τ_K off Killing; consistency of the
   gap equation off de Sitter; comparison (I-QFT, I-KH, I-CK).
5. Consistency with G3-OFFDS, G3-HOM, G3-W1's 47 excluded classes and W1-0.

Each node closes with an explicit check (algebra, citation or source line) and a verdict. On any
branch favourable to the framework, a skeptical pass is made before it is accepted.

## Stop conditions

- The question is answered under the decision rule for the bare construction and for each premise
  set examined.
- A branch requires a computation, a numerical experiment, a Lean development or a manuscript edit:
  that branch stops and its item is recorded MISSING.
- A branch would require adopting a premise: it stops, and the premise is recorded as a hypothesis.
- Three consecutive passes yield no NEW finding (fixed point).

There is no successor round.

## Labels in the record

ESTABLISHED (derived on paper in the record [W], or a quoted standard result [L], at the stated
scope), ASSUMED (a premise of the table above), MISSING (supplied neither by the corpus nor by this
unit). A negative result names the exact class of constructions it excludes.
