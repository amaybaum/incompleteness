# OIQM-UNBOUNDED P2: a compatible tower with a native observation interface (plan)

**Standing.** WIP / UNVERIFIED. This plan was committed before any derivation. It covers a paper-only
unit authorized at #1169 c.7066630306. It runs no computation, adopts no premise, edits no manuscript,
and changes no reviewed record. Issue #1500. It is stacked on #1504 at `31594967`.

## 1. Target

The target is one construction that is compatible across carrier sizes, as defined in the #1504 NOTE
§3: embeddings (T1), dynamics (T2), the observation interface (T3), and states (T4). It must carry two
things:

- **(a)** a coherence pair at every size, compatible with the embeddings and the dynamics. This is a
  creator (not MIO-type) and a detector (not DIO-type), in the sense of OPRES Theorem C (#1511 at
  `7669e511`). The two are separate obligations (#1169 c.7066541026).
- **(b)** a native observation interface whose readout reach grows without bound, as Proposition U
  (#1504) requires.

The unit either constructs such a tower under stated (I) imports, or proves an obstruction that names
the premise it cannot do without.

## 2. Fixed inputs and constraints

- **R-READ** (whether native readout effects lie in the configuration algebra) is unresolved. No node
  may assume either answer. A result that depends on it is stated for each branch.
- **Axiom 2 recurrence** questions stay routed to the owner (#1504 AW-U3). They are not decided here.
- **The A1 retirement** (#1477) is not treated as landed. It is not taken to establish the existence or
  consistency of an infinite system.
- **D-W** (GATE-A r5 #1503 at `fd3cb064`, §2.2) is cited and not rebuilt. Kernel results are cited and
  not duplicated.

## 3. Nodes, walked depth-first

1. **N1, compatibility of the coherence pair.** Do creator and detector status survive inert-spectator
   extension, region inclusion and conjugation by the substratum dynamics? Are they also reflected by
   them, so that each holds in both directions?
2. **N2, coupling through R-READ.** What does each branch of R-READ do to (a) and to (b)? Proposition U
   and OPRES Theorem C are the inputs.
3. **N3, construction or obstruction on each branch.** Each branch names its imports and checks
   T1 to T4 clause by clause.
4. **N4, the operational scope.** Does Proposition U strengthen to a per-setting statement? How does
   D-W sit on a site-factorized finite-alphabet carrier?

## 4. Productivity test, fixed now

The unit is a **gem** if it delivers at least one of the following:

- (a) a construction of a tower meeting the target under (I) imports, with every import named and
  every compatibility clause checked;
- (b) an obstruction whose premise is shown unavoidable by a countermodel in which that premise is
  dropped;
- (c) a reduction of the target to a strictly smaller, named question;
- (d) an exposed hidden assumption in the target or in a reviewed input.

Restating reviewed results, or relabelling them, is a **non-gem** and is recorded only. Favourable
branches get maximum skepticism.

## 5. Allowed outcomes, reported per scope

The scopes are representational (Born form on configurations, under KIN) and operational (record
laws). Each scope reports exactly one of:

- **CONSTRUCTION** (I, with imports listed);
- **OBSTRUCTION** (premise named, with its unavoidability witness);
- **INCONCLUSIVE** (the missing step named).

INCONCLUSIVE is an admissible result and is not a failure.

## 6. Computation

None is run. Any PR-U1-type computation is preregistered only: its question, its exact decision
method, and controls that must fail for a known reason. An undecided result must be recorded as an
outcome in its own right.
