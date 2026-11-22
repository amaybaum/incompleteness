# NATIVE-UNIV, round 5: thick gadgets around the NU9 breather (plan)

**Standing.** Writer's plan, committed before the record it governs. The commit order establishes
the order of the commits only. Paper only: no computation, no script, no replay, no Lean.

**Authorization.** Owner `amaybaum`,
[#1169 c.7076731666](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7076731666),
2026-11-22T08:46:51Z, item 2: "Native universality (#1461): thick gadgets. Investigate non-planar
gadgets built around the NU9 breather, for controlled turns and signal interactions. Paper-only
feasibility and obstruction arguments are permitted. NU9-CHECK, computational experiments and
rule-selection work remain unauthorized." Item 3 (common safeguards) applies in full. Rule
selection (PM-D5, #1454) is not touched.

**Goal link (§A.47).** Serves #1461 (tier high, provisional; feasibility first). The work decides,
for a named class of finite non-planar gadgets built around NU9, whether the class can contain a
leak-free controlled turn or signal interaction in Q, or whether it is excluded. It does not decide
whether R_q is universal in Definition U.

**Base and inputs.** Branch `research/native-univ-p5-20261122`, cut from `b9d8ce76` (head of #1523,
round 4, delta-confirmed). #1523 stays as it is. Inputs, at their standing:
- `R4`: round 4, `…/native-univ-p4-20261121/` (NU9; hand re-derived in review; exact re-run
  NU9-CHECK pending and not authorized); not on `main`.
- `PT`: PLANAR-TURN, `…/native-univ-p3-20261121/` (#1515): the leak-free transfer criterion and
  the outcome definitions T, T-STATEFUL, R6-NULL, Q-LEAK, Q-EMIT; preregistered, not run.
- `P2N`: `…/native-univ-p2-20261121/` (#1499): NU3, NU4, NU6, with the corrected NU5 reading
  (PT DESIGN §6); confirmed in review; not on `main`.
- `F1`: `…/native-univ-feasibility-20261121/` (#1489): NU1, NU2; reviewed; not on `main`.
- `U1`, `U2`, `MQ`: UNIV-1, UNIV-2 and MEAS-Q on `main` (Definition U, Lemmas 2.1–2.2, the W2
  line and signal, R1–R8, MQ1–MQ3).

**A1 retirement ledger check.** Before the first commit, `origin research/a1exit-deletion-20261121`
was fetched read-only and `verification/audits/foundations/a1exit-deletion-20261121/ledger.json`
read at its head `fef0f15`. No ledgered path lies under `…/native-univ-*`; the only ledgered path
under `verification/programmes/oi-qm/reconstruction/` is in `native-y-continuation-20261024/`. Every
path this round writes is under `…/native-univ-p5-20261122/`, which is not ledgered.

## Question (preregistered)

Can a finite non-planar gadget built around the NU9 period-10 breather realize, in Q = `R_{2^16}`
on `ℤ³` at a uniform background `c`, (a) a leak-free controlled turn of a W2 signal, or (b) a
leak-free signal interaction? If not, for exactly which class of such gadgets is either excluded?

Depth-first order (§A.12, §A.31):
1. Fix the definitions (thick gadget, controlled turn, signal interaction), consistent with
   Definition U (U1 §2), PT §1–2 and U2's R1–R6.
2. The first necessary condition is a leak-free no-input orbit (U2 R1; PT's class excludes
   Q-LEAK). Decide it first for the simplest member of the class: the bare breather (allowed region
   = the breather's cube plus straight W2 lines) with one line, over every placement and every
   relative phase. Then several lines.
3. Only where a leak-free no-input orbit exists, go on to the signal.
4. Extract any structural constraint that holds for every thick gadget, not only the bare one.

## Assumptions

| Id | Assumption | (N)/(I) | Where it is supported |
|---|---|---|---|
| A-rule | Q's update `x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q` on representatives (SM:294), as RZ around `c` inside U1 Lemma 2.1's window | (N) | `main` (U1) |
| A-bg | a uniform background `c` with the window of every derivation stated; W2 lines and the W2 signal as designed initial patterns | (N), scope condition | U1 E2, U2 K0 (`main`) |
| A-comp | the two space-time parity components evolve independently | (N) | F1 NU1 (reviewed, not on `main`); U2 A1 (`main`) |
| A-conf | MQ1 and MQ2 (one-step and windowed confinement) | (N) | `main` |
| A-NU9 | the NU9 orbit | (N) | R4, independent hand re-derivation; not on `main`; exact re-run pending |
| A-def | the leak-free transfer criterion (allowed region `lines ∪ K`, not its closure) | definition | PT §1 (preregistered) |

No quantum, operational or measurement assumption is imported. No premise is adopted.

## Productivity test (fixed now)

- **Gem iff one of:**
  - (i) an explicit thick gadget with a hand-certified leak-free controlled turn or signal
    interaction (every tick written out, with an exact certificate in PT's sense);
  - (ii) a scoped obstruction: a hand-checkable theorem that excludes a stated class of gadgets
    built around NU9, where the class is not already excluded by U1, U2, PT's design or R4;
  - (iii) a structural lemma that constrains every thick gadget attached to W2 lines (not only
    NU9-based ones) and is strictly stronger than NU3–NU9 and MQ1–MQ3 as stated.
- **INCONCLUSIVE** is an allowed outcome: the record then states the step at which the derivation
  stopped and what it would need.
- **Non-gem:** a restatement of NU3–NU9 or of R4 §3, or a definitions-only record.

## Rules and stop conditions

- **Layer.** Every result is a statement about Q's configuration dynamics. None concerns effects,
  instruments, accessible algebras or readouts.
- **Labels.** (N)/(I) by assumptions; ESTABLISHED / ASSUMED / MISSING for every result; paper
  derivation, literature and conjecture kept distinct. A negative result names the exact class it
  excludes and claims nothing about R_q's universality.
- **Hand-checkability.** Every orbit is written out tick by tick, or follows from a stated lemma. No
  exact orbit is claimed beyond what is derived.
- **Skepticism (§A.31).** A positive branch (a leak-free coexistence of breather and line, or an
  interaction) gets maximum skepticism: every site that can change is listed at every tick.
- **Stop when:**
  - the question is answered for a stated class, positively or negatively; or
  - a branch needs more than about 30 ticks or more cases than can be written out by hand; it is
    then recorded as MISSING with the step reached; or
  - the next step would need a computation (it is then described, not run); or
  - three consecutive passes yield no NEW finding (§A.31 fixed point).
- No successor round is opened. The result returns for a separate owner decision.
