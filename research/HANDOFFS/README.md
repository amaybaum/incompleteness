# Handoffs between research threads (protocol)

A handoff carries one result from the thread that established it to a thread that can use it, without changing
the receiving thread's assumptions silently.

1. **Source.** The result must be committed on the source thread's branch with its evidence (commit id, path,
   status label, scripts and outputs, replay).
2. **Write-up.** The coordinator writes `HO-<n>-<source>-to-<target>-<topic>.md` here (on `research/overview`): the
   statement, its status label (CERTIFIED / CONDITIONAL on named items / CONJECTURE / FAILED), the exact evidence
   pointers (branch, commit, path, sha256), what the receiving thread may assume (stated as the exact proposition)
   and what it may not (scope limits, open conditions). Version 1. A later change is a new version
   (`HO-<n>-v2-…`), never an edit in place.
3. **Receipt.** The receiving thread copies the handoff into `research/<target>/inbox/` on its own branch with a
   commit whose message names the handoff and version, and records in its `LOG.md` whether and how it relies on
   it. Until that commit exists, the thread does not rely on the result.
4. **Index.** The table below lists every handoff with its state. The coordinator fills the "received" column from
   the receiving thread's commit.

| id | from | to | result | version | received (commit) |
|---|---|---|---|---|---|
| HO-1 | bridge | countermodels | exact finite embedded-observer realization of K(Z_F) in branch (a) (CONDITIONAL) | v1 | — |
| HO-2 | bridge | equivalence, countermodels (origin may receive) | finite and locally finite substrata cannot carry the sufficient composite actions; R1 obstruction `10/9`; towers ⇒ abelian identity component (CONDITIONAL on [L]); Conjecture B3.C | v1 | origin `8f0c832a` (as a constraint only); equivalence, countermodels pending |
| HO-3 | bridge | origin | locality of registers is Bell-local and hosts no candidate pair; GR.md:326 marker (hold) | v1 | origin `8f0c832a` (scope only) |
| HO-4 | countermodels | bridge | KZ1–KZ12, the realization-facing properties of K(Z_F) (CONDITIONAL); composition-clause proposal | v1 | — |
| HO-5 | origin | bridge | A_miss ⟺ (b) for `R_z(t)` ∧ (b) for `J = cyc3`; SRC/SPEC dependency; Lemma P (CONDITIONAL) | v1 | — |
| HO-6 | equivalence | bridge | one formal map (two-token dictionary + `ContextStable` transfer) would serve K2(c) and Kₙ (interface request; W-DESC CONJECTURE) | v1 | — |
| HO-7 | equivalence | countermodels | three exact objects: Ω₄, the swapped gate, the `2^k` class (CONJECTURE, exact) | v1 | — |
| HO-8 | equivalence | origin | minimal sourcing targets on the K route (per-row labels) | v1 | origin `8f0c832a` (as a list of targets at their labels) |
| HO-9 | origin | bridge, equivalence | the exclusive measure-and-re-prepare readout is the one open Origin premise; KB-D's exclusivity excluded on the stated access; SRC via KB-D token-only; passive finite-rank towers carry no infinite-order datum; density at the balanced angle (SO(3); SO(6) at level three) | v1 | — |

The equivalence thread's HP-1 (proposed ROADMAP wording for row K) is addressed to the coordinator, not to a thread;
it is recorded in `research/OVERVIEW.md` under round-ready findings and is not a handoff.
