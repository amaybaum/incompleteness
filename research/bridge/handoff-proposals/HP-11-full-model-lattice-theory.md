# HP-11 — a full model for H-T's token clause, and the two readings audited

From `research/bridge`, node B14 re-assessed under the coordinator's third addendum (round 4). Proposed for the origin
thread (operational sourcing of token operations), the countermodels thread (models of the stated access) and the
coordinator (reading markers on standing verdicts). The coordinator routes.

## Statements and labels

1. **The full model FM** (B14-6). H: the sealed core with the wave substratum (P1 open, as for every model). M: the
   lattice theory `genTheory latticeClass`, where `latticeClass` is the fourth-root lattice taken as a class (every
   submonomial operator whose nonzero entries have equal fourth powers). It contains the stated access (I1.60) and the
   quarter phase, lies in `substratumClass`, and is an architecture that is context-stable, label-invariant,
   dagger-stable, unitary-ray saturated, structurally closed and configuration-level. Its theory satisfies
   `DerivedOI` on every carrier and the sealed core, `OICore` and `DerivedOICore` on `Fin 2`. O: the ball token. P:
   `Q3`. Of Table A2's 68 NOT REACHED rows FM satisfies 34, 5 are scope statements, and each of the 29 it fails
   implies composite unitary control or QM by a kernel chain. Reading: availability.
2. **The verdict** (B14-6). In FM, `actT R_z(θ₀)` (`cos θ₀ = 3/5`) and `actT J` are unavailable on the token and on the
   pair, at every level, by every protocol; through the H→M arrow at L the same holds in every substratum's observer
   theory. So their availability with RESPECT and product behaviour is an **independent bridge (full model, relative
   to the stage-6 inventory)**: independent of every stage-6 item that does not itself imply composite unitary control
   or QM. Label: CONJECTURE ([D] + [A] + [W]).
3. **K∞-Drive's two readings** (B14-7). FM satisfies I3.169 as R6 reads it and refutes its operational reading at
   `t = θ₀`; H-T's token clause is that operational reading (`ball3Drive`'s flow `rot3` at `θ₀` is `R_z(θ₀)`). R6
   already records the operational availability as open; this sharpens it. Label: CONJECTURE; gem ELABORATING.
4. **Invariance does not give availability, in one model** (B14-5). FM's pair cone `Q3` satisfies the transfer
   clause for every class (`transferClause_Q3`, HP-12) while `zPh` is unavailable (`lattice_refutes`): Q3 ⇒ A_miss
   holds in the invariance reading only. Label: CONJECTURE ([D], both sides).
5. **The audit of the standing rows** (B14-8, V-4). The independence of (b) in V-1–V-3 and B4-1 is pair-level
   (K(Z_F)'s 118 pair-level rows, the `W 3` transcriptions of EO and ObserverRecursion, B4's H-level realization);
   K(Z_F)'s M-level rows are undecided, and every kernel M-level theory has pair cone `Q3`, so a full model for (b)'s
   independence is OPEN. Rows B2-3, B2-4, B2-5, B8-3 said an availability statement "is" (b): it yields (b). B9-1
   called (T) an availability clause: it is an invariance clause. V-2 (iii)'s "matrix-certified" SPEC_P(φ) is M-level
   availability.

## Evidence

| item | pointer |
|---|---|
| module | `research/bridge/lean/BridgeAvailFull.lean`, sha256 `b93a732e…`; dev blob `192fca74` |
| CI | run 38115337569 (`dev-bridge/r4-conv` @ `ca48c4c4`): built, 50/50 `#print axioms` on `[propext, Classical.choice, Quot.sound]` (that run's gate did not run, two other modules failing); run 38117986499 (`dev-bridge/r4-final` @ `bf8ba746`), Mathlib bridge job 114406679644: Build success, 50/50 standard, `lean-axioms` PASS (6083 named results, no sorry), gate red only on `lean-manuscript` (no census family for the design modules, by construction) |
| row table | `experiments/b14_fullmodel.py` / `.out`, controls C1–C5 and exact checks X1–X4 green, replay byte-identical; inputs R6/REASSESSMENT.md `1ff62ad6…`, R6/r4_tables.out `08d38e1c…`, I4/INVENTORY.md `43bbada1…` |
| notes, results | `NOTES-B14.md` §8; `RESULTS.md` rows B14-5 … B14-8, V-4 |

## What the recipient may assume

Items 1–5 at their labels. FM can serve as the model of the stated access for any statement that needs the
availability of `R_z(θ₀)` or `J` refuted while the stage-6 premises below the 29 control-or-QM rows hold.

## What the recipient may not assume

- certification, or any census disposition;
- "independent of OI" without the scope: the verdict is relative to the stage-6 inventory, the H level is P1-open, and
  the 29 failed rows are hypotheses at least as strong as the conclusion;
- anything about (b) from FM: FM satisfies (b) in the invariance reading;
- that the operational reading of K∞-Drive was absent from the record (R6 records it as open).
