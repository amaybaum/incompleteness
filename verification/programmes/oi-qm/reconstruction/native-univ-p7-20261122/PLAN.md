# NATIVE-UNIV, round 7: direct-contact pairs and fully shared coupling sites at the NU9 cube (plan)

**Standing.** Writer's plan, committed before the record it governs. The commit order establishes
the order of the commits only. Paper only: no computation, no script, no replay, no Lean.

**Authorization.** Owner `amaybaum`,
[#1169 c.7078857457](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7078857457),
2026-11-22T12:04:30Z: "This decision is the authorization for a paper-only NATIVE-UNIV round 7",
with the unit "Native universality (#1461), round 7: Direct-contact pairs and fully shared coupling
sites, which the round-6 necessary condition requires of any working NU9 design", building on
round 6 at `7cb3420a`. Its safeguards apply in full: paper only, a preregistered plan, explicit
assumptions and a stop condition; a negative result names the exact class it excludes; no
computation (NU9-CHECK included), no pull request, merge, comment, description edit or other
automated GitHub write; no change to `papers/`, `book/` or any file in the A1 retirement ledger; a
positive result does not authorize its implementation. Rule selection (PM-D5, #1454) is not
touched, and no other rule is substituted. The branch is pushed only, with a byte-for-byte check
after every push (write-integrity halt, #1169 c.7076910606 and c.7078857457).

**Goal link (§A.47).** Serves #1461 (tier high, provisional; feasibility first). Round 6's
necessary condition AW-NU-6 (with its (N3)) leaves two classes of bare-NU9 designs open: direct
contacts, and arrangements in which every coupling site is shared. The work decides, for each
class as defined below, whether it can supply a leak-free controlled turn or signal interaction
around the NU9 cube, or which stated sub-class is excluded. It does not decide whether R_q is
universal in Definition U.

**Base and inputs.** Branch `research/native-univ-p7-20261122`, cut from `7cb3420a` (head of the
round-6 branch, which stays as it is). Inputs, at their standing:
- `R6`: round 6, `…/native-univ-p6-20261122/NOTE.md` (W2 pieces, L6–L10, T-IND′, Theorem H and
  its branch tables, AW-NU-6, MISSING); independently reviewed at #1461 c.7078048790, delta-checked
  at c.7078088815 and exact-head checked at c.7078116539; not on `main`.
- `R5`: round 5, `…/native-univ-p5-20261122/NOTE.md` (L1–L5, T-IND, Theorem T); reviewed at #1549
  c.7077076211 and c.7077118425; not on `main`.
- `R4`: round 4 (NU9); hand re-derived in review; exact re-run NU9-CHECK pending and not
  authorized; not on `main`.
- `PT`: PLANAR-TURN, `…/native-univ-p3-20261121/` (J1/J2, the outcome definitions); preregistered,
  not run.
- `P2N`, `F1`: NU1–NU6; reviewed; not on `main`.
- `U1`, `U2`, `MQ`: UNIV-1, UNIV-2 and MEAS-Q on `main` (Lemma 2.1, the W2 background and signal
  E2, segments E6, R1–R8, MQ1–MQ2).

**A1 retirement ledger check.** Before the first commit, `origin research/a1exit-deletion-20261121`
was fetched read-only and `verification/audits/foundations/a1exit-deletion-20261121/ledger.json`
read at its head `b1b0522`. It lists no path under `…/native-univ-*`; its only path under
`verification/programmes/oi-qm/reconstruction/` is in `native-y-continuation-20261024/`. Every path
this round writes is under `…/native-univ-p7-20261122/`, which is not ledgered.

## Question (preregistered)

In Q = `R_q` on `ℤ³` at a uniform background `c`, with a bare NU9 breather on the cube `C` and
straight W2 pieces (rays, finite segments, lines; R6 §1), does either of the following classes give
a leak-free controlled turn or signal interaction around the cube?

- **(a) Direct contact.** At least one site of a piece is adjacent to a site of `C` or of another
  piece. Named members: the thick J1 analogue, two pieces on perpendicular axes with at least one
  pair of adjacent sites ("adjacent arms"); and a head-on input arm (R6 placements `H00`, `H10`,
  `H11`: end at ℓ1-distance 1 from `C`, at least two sites) together with an output arm.
- **(b) Fully shared coupling sites.** No piece is adjacent to `C`, at least one matched piece lies
  within ℓ1-distance 2 of `C`, and every coupling site (a site outside the allowed region adjacent
  to `C` and to a matched piece) is adjacent to at least two matched pieces.

Contact geometry is classified by which parts (the cube, each piece) are adjacent. Endpoints keep
their restricted W2 values (R6 §1). Phases: the breather at any of its 10 phases, each matched
piece in any of its four W2 backgrounds, an unmatched piece in any. The signal is U1 E2's W2 signal
(U2 K0), launched on a piece at distance ≥ 8 from every other part, toward the gadget.

If either class gives one, give the gadget with every tick written out. If neither does, give a
scoped obstruction for the sub-class actually covered.

Depth-first order (§A.12, §A.31):
1. Fix the classes and what a controlled turn and a signal interaction need of them (R5 §1,
   R6 §1: an admissible no-input orbit; a signal leaving on another piece; an orbit that differs
   from the free superposition).
2. Find which parts of a gadget can influence which in a leak-free run, for any gadget, and what
   that leaves of (a) and (b).
3. For what remains in which the breather takes part, decide admissibility of the no-input orbit,
   reusing R6's lemmas and branch tables only where their hypotheses are checked to hold.
4. Only where an admissible no-input orbit exists and the breather takes part, go on to the signal.

## Assumptions

| Id | Assumption | (N)/(I) | Where it is supported |
|---|---|---|---|
| A-rule | Q's update, run as RZ around `c` inside U1 Lemma 2.1's window | (N) | `main` (U1) |
| A-bg | a uniform background `c`; W2 pieces and the breather as designed initial patterns, a scope condition | (N), scope condition | U1 E2, E6 (`main`) |
| A-comp | the two space-time parity components evolve independently | (N) | F1 NU1 (reviewed, not on `main`) |
| A-conf | MQ1 and MQ2 | (N) | `main` |
| A-NU9 | the NU9 orbit, confined to `C` with ternary boundary | (N) | R4, independent hand re-derivations; not on `main`; exact re-run pending, not authorized |
| A-R5 | R5's L1–L5 and T-IND as proved there | (N) | R5, independently reviewed; not on `main` |
| A-R6 | R6's L6–L10, T-IND′, Theorem H and its branch tables (first-leak ticks and the sites listed) | (N) | R6, independently reviewed and re-derived by hand in review; not on `main` |
| A-E6 | a W2 signal that reaches a segment end leaves the line sector | (N) | U1 E6 (`main`; an exact computation recorded there, cited, not re-run) |
| A-def | leak relative to the allowed region; controlled turn and signal interaction as in R5 §1 and R6 §1, with an admissible (leak-free and periodic) no-input orbit | definition | PT §1–3, U2 R1, R6 §1 |

No quantum, operational or measurement assumption is imported. No premise is adopted.

## Productivity test (fixed now)

- **Gem iff one of:**
  - (i) an explicit gadget in class (a) or (b) with a hand-certified leak-free controlled turn or
    signal interaction around the cube, every tick written out;
  - (ii) a scoped obstruction: a hand-checkable theorem, conditional on A-NU9, that excludes a
    stated sub-class of (a) or (b) not already excluded by U1, U2, PT, R4, R5 or R6;
  - (iii) a structural lemma that constrains every gadget with W2 pieces, strictly stronger than
    R5's L1–L5 and R6's L6–L10 as stated.
- **INCONCLUSIVE** is an allowed outcome: the record then states where the derivation stopped and
  what it would need.
- **Non-gem:** a restatement of R5 or R6, or a definitions-only record.

## Rules and stop conditions

- **Layer.** Every result is a statement about Q's configuration dynamics.
- **Labels.** (N)/(I) by assumptions; ESTABLISHED / ASSUMED / MISSING for every result; every result
  that uses NU9 carries "conditional on A-NU9". A negative result names the exact class it excludes
  and claims nothing about R_q's universality. A necessary geometric condition is stated as a
  condition on designs, not as universality or non-universality. A positive gadget would be a
  building block only.
- **Reuse.** R5's and R6's lemmas are used only after their hypotheses are checked for the case at
  hand, explicitly in the text.
- **Hand-checkability.** Every orbit is written out tick by tick, or follows from a stated lemma.
- **Skepticism (§A.31).** A branch or class favourable to the framework gets maximum skepticism: its
  standing is stated without extrapolation.
- **Stop when:**
  - the question is answered for a stated class, positively or negatively; or
  - a branch needs more than about 30 ticks, or more cases than can be written out by hand; it is
    recorded as MISSING with the step reached; or
  - the next step needs a computation (described, not run); or
  - three consecutive passes yield no NEW finding (§A.31 fixed point).
- No successor round is opened. The result returns for a separate owner decision.
