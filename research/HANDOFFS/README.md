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
| HO-1 | bridge | countermodels | exact finite embedded-observer realization of K(Z_F) in branch (a) (CONDITIONAL) | v1 | countermodels `d8a1461b` (context only) |
| HO-2 | bridge | equivalence, countermodels (origin may receive) | finite and locally finite substrata cannot carry the sufficient composite actions; R1 obstruction `10/9`; towers ⇒ abelian identity component (CONDITIONAL on [L]); Conjecture B3.C | v1 | origin `8f0c832a` (as a constraint only); equivalence `d14140db`; countermodels `d8a1461b` (B3.C's statement and coverage only) |
| HO-3 | bridge | origin | locality of registers is Bell-local and hosts no candidate pair; GR.md:326 marker (hold) | v1 | origin `8f0c832a` (scope only) |
| HO-4 | countermodels | bridge | KZ1–KZ12, the realization-facing properties of K(Z_F) (CONDITIONAL); composition-clause proposal | v1 | bridge `e29b6a42` (answered by HO-11) |
| HO-5 | origin | bridge | A_miss ⟺ (b) for `R_z(t)` ∧ (b) for `J = cyc3`; SRC/SPEC dependency; Lemma P (CONDITIONAL) | v1 | bridge `e29b6a42` (SPEC side answered by HO-12) |
| HO-6 | equivalence | bridge | one formal map (two-token dictionary + `ContextStable` transfer) would serve K2(c) and Kₙ (interface request; W-DESC CONJECTURE) | v1 | bridge `e29b6a42` (answered by HO-12) |
| HO-7 | equivalence | countermodels | three exact objects: Ω₄, the swapped gate, the `2^k` class (CONJECTURE, exact) | v1 | countermodels `d8a1461b` (Ω₄'s definition only; answered by HO-15) |
| HO-8 | equivalence | origin | minimal sourcing targets on the K route (per-row labels) | v1 | origin `8f0c832a` (as a list of targets at their labels) |
| HO-9 | origin | bridge, equivalence | the exclusive measure-and-re-prepare readout is the one open Origin premise; KB-D's exclusivity excluded on the stated access; SRC via KB-D token-only; passive finite-rank towers carry no infinite-order datum; density at the balanced angle (SO(3); SO(6) at level three) | v1 | — (round 3) |
| HO-10 | bridge | countermodels, equivalence | Conjecture B3.C holds CONDITIONAL on claim (D): a compact pair group with `cnot` and abelian identity component leaves an exotic cone (reachability theorem CONJECTURE, written proof); the finite/locally finite route closed without conjecture | v1 | — (round 3) |
| HO-11 | bridge | countermodels | HO-4's proposal tested: the excluding clause is family membership (matrix form CERTIFIED independent of the sealed core); clause (4) is the composite action for the given instruments; Stab_loc(K(Z_F)) = V4 | v1 | — (round 3) |
| HO-12 | bridge | origin, equivalence | the SPEC side: a transfer needs (D1), (D2) exact and the clause (T) = SPEC_P(φ) ∧ SPEC_P(NOT); A_miss ⟺ (T) ∧ SPEC_P(J) (relocation); `⟨cnot, actC J, actT J⟩` = the Clifford group of order 11520; A_miss splits into a continuous abelian and a finite half | v1 | — (round 3) |
| HO-13 | equivalence | bridge, origin | the K2 schema's complete written proof (A_miss enters only at reachability; no spectral theorem); two exact operations `R_z(θ₀)`, `cyc3` on one token suffice given H3; the finite clause fails at reachability | v1 | — (round 3) |
| HO-14 | equivalence | countermodels | `⟨cnot, actT R_z(π/2), actT cyc3⟩` has order 384 and `φ₀` is unreachable: a concrete target for an explicit exotic cone | v1 | — (round 3) |
| HO-15 | countermodels | equivalence | Aut(Ω₄) = O(3) × ℤ₂, orbits = level sets of `s⁴`; `c*` constant on smooth bodies (assumption-watch marker for K∞-Trans); Ω₄'s cone self-dual for no inner product | v1 | — (round 3) |
| HO-16 | countermodels | bridge | B3.C from the cone side: an explicit exotic cone for a 2-torus with two product eigenlines; the eigenline-orbit mechanism (EBF); the residual region | v1 | — (round 3) |

The equivalence thread's HP-1 (proposed ROADMAP wording for row K) and HP-5 (the Level III wording marker and S6's
revised kernel cost) are addressed to the coordinator, not to a thread; they are recorded in `research/OVERVIEW.md`
and are not handoffs.
