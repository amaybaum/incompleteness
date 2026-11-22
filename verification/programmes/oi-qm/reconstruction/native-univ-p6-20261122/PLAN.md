# NATIVE-UNIV, round 6: rays and finite segments ending next to the NU9 cube (plan)

**Standing.** Writer's plan, committed before the record it governs. The commit order establishes
the order of the commits only. Paper only: no computation, no script, no replay, no Lean.

**Authorization.** Owner `amaybaum`,
[#1169 c.7077598984](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7077598984),
2026-11-22T10:08:36Z, item 2, native universality (#1461): "The NU9 turn geometry: rays and finite
segments adjacent to the cube, using the native rule only. Decide whether they give a viable
connection mechanism. Distinguish necessary geometric conditions from demonstrated computational
universality. NU9-CHECK and every computational experiment stay unauthorized." Item 3 (safeguards)
applies in full. Rule selection (PM-D5, #1454) is not touched. No pull request, PR description,
Issue body or comment is written from this round (write-integrity halt, #1169 c.7076910606 and
c.7077598984); the branch is pushed only.

**Goal link (§A.47).** Serves #1461 (tier high, provisional; feasibility first). The work decides,
for the class of straight W2 rays and finite W2 segments that end next to a bare NU9 breather
(the thick analogue of PT's J1/J2), whether the class can supply a leak-free controlled turn or
signal interaction in Q, or whether a stated sub-class is excluded. It does not decide whether R_q
is universal in Definition U.

**Base and inputs.** Branch `research/native-univ-p6-20261122`, cut from `2cdc220f` (head of #1549,
round 5). #1549 stays as it is. Inputs, at their standing:
- `R5`: round 5, `…/native-univ-p5-20261122/` (definitions, L1–L5, T-IND, Theorem T, event tables;
  independently reviewed at #1549 c.7077076211 and delta-checked at c.7077118425); not on `main`.
- `R4`: round 4, `…/native-univ-p4-20261121/` (NU9; hand re-derived in review; exact re-run
  NU9-CHECK pending and not authorized); not on `main`.
- `PT`: PLANAR-TURN, `…/native-univ-p3-20261121/` (#1515): J1/J2, the outcome definitions T,
  T-STATEFUL, R6-NULL, Q-LEAK, Q-EMIT and the return requirement for no-input orbits;
  preregistered, not run.
- `P2N`, `F1`: NU1–NU6 (#1499, #1489); reviewed; not on `main`.
- `U1`, `U2`, `MQ`: UNIV-1, UNIV-2 and MEAS-Q on `main` (Lemma 2.1, the W2 background and segments
  E2/E6, R1–R8, MQ1–MQ2).

**A1 retirement ledger check.** Before the first commit, `origin research/a1exit-deletion-20261121`
was fetched read-only and `verification/audits/foundations/a1exit-deletion-20261121/ledger.json`
read at its head `ea1029d`. It lists no path under `…/native-univ-*`; its only path under
`verification/programmes/oi-qm/reconstruction/` is in `native-y-continuation-20261024/`. Every path
this round writes is under `…/native-univ-p6-20261122/`, which is not ledgered.

## Question (preregistered)

In Q = `R_q` on `ℤ³` at a uniform background `c`, with a bare NU9 breather (allowed region: the
3 × 3 × 3 cube plus the pieces), do straight W2 rays and finite W2 segments that end next to the
cube give a viable connection mechanism, that is, a leak-free controlled turn or signal
interaction? If not, for exactly which geometric class is it excluded?

Depth-first order (§A.12, §A.31):
1. Define rays and segments: the W2 values they carry, their endpoint behaviour and the
   background. Prove what R5's lemmas need of them (closedness, confinement, (W)).
2. A connection needs an admissible no-input orbit first (U2 R1; PT §3(a): leak-free and
   periodic). Decide it for one piece, over every placement up to symmetry in which an end lies
   within ℓ1-distance 2 of the cube, and every phase and background.
3. Extend to several pieces where R5's lemmas allow.
4. Only where an admissible no-input orbit exists, go on to the signal.
5. Extract any constraint that holds at a piece end for every gadget, not only the bare one.

## Assumptions

| Id | Assumption | (N)/(I) | Where it is supported |
|---|---|---|---|
| A-rule | Q's update, run as RZ around `c` inside U1 Lemma 2.1's window | (N) | `main` (U1) |
| A-bg | a uniform background `c`; W2 pieces and the breather as designed initial patterns, a scope condition | (N), scope condition | U1 E2, E6 (`main`) |
| A-comp | the two space-time parity components evolve independently | (N) | F1 NU1 (reviewed, not on `main`) |
| A-conf | MQ1 and MQ2 | (N) | `main` |
| A-NU9 | the NU9 orbit | (N) | R4, independent hand re-derivations; not on `main`; exact re-run pending, not authorized |
| A-R5 | R5's L1–L5 and T-IND as proved there | (N) | R5, independently reviewed; not on `main` |
| A-def | leak relative to the allowed region `A = K ∪ pieces` (not its closure); controlled turn and signal interaction need an admissible no-input orbit | definition | PT §1–3, U2 R1 (preregistered / `main`) |

No quantum, operational or measurement assumption is imported. No premise is adopted.

## Productivity test (fixed now)

- **Gem iff one of:**
  - (i) an explicit gadget in the class with a hand-certified leak-free controlled turn or signal
    interaction, every tick written out;
  - (ii) a scoped obstruction: a hand-checkable theorem, conditional on A-NU9, that excludes a
    stated class of NU9 gadgets with rays or segments, not already excluded by U1, U2, PT, R4 or
    R5;
  - (iii) a structural lemma that constrains every gadget with a W2 piece end, strictly stronger
    than R5's L1–L5 as stated.
- **INCONCLUSIVE** is an allowed outcome: the record then states where the derivation stopped and
  what it would need.
- **Non-gem:** a restatement of R5 for full lines, or a definitions-only record.

## Rules and stop conditions

- **Layer.** Every result is a statement about Q's configuration dynamics.
- **Labels.** (N)/(I) by assumptions; ESTABLISHED / ASSUMED / MISSING for every result; every result
  that uses NU9 carries "conditional on A-NU9". A negative result names the exact class it excludes
  and claims nothing about R_q's universality. A positive gadget would be a building block only,
  not universality.
- **Hand-checkability.** Every orbit is written out tick by tick, or follows from a stated lemma.
- **Skepticism (§A.31).** A branch that does not leak gets maximum skepticism: every site that can
  change is listed at every tick, and its standing is stated without extrapolation.
- **Stop when:**
  - the question is answered for a stated class, positively or negatively; or
  - a branch needs more than about 30 ticks, or more cases than can be written out by hand; it is
    recorded as MISSING with the step reached; or
  - the next step needs a computation (described, not run); or
  - three consecutive passes yield no NEW finding (§A.31 fixed point).
- No successor round is opened. The result returns for a separate owner decision.
