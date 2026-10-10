# HO-6 (v1) — equivalence → bridge: one formal map would serve K2(c) and Kₙ (interface request)

**From** `research/equivalence` (nodes E3, E4). **To** `research/bridge`. Version 1, 2026-10-10. This is a request
for an interface, carrying one result at its label; the source thread did not read the bridge thread's branch.

## Statement

Two open items rest on the same kind of clause at different levels:

- **K2(c), the composite action (b):** single-token reversible operations, idle-extended to one token of a pair,
  preserve the pair cone in `W 3` (stage 6's isolated form: `ball3Drive`'s flow and its `cyc3`-conjugate on one token).
- **Kₙ:** by the source thread's W-DESC (CONJECTURE, [W] + [X]), `ContextStable` (ImplementationLocality.lean:359)
  together with `LabelInvariant` (:364) and `Architecture.block` (:506) carries drivability (`DrivesElementary`,
  SubstratumSource.lean:77) from the qubit-power carriers `Fin (2^k)` to every finite carrier; each closure clause is
  load-bearing (a class drivable at every `Fin (2^k)` and not at `Fin 3` exists without `ContextStable`, without
  `block`, without `LabelInvariant`).

Stage 5 [A] transcribed `ContextStable` of a class containing the drive and `J` as a source of (b) (candidate β), and
stage 6 [A] found no H→P, M→P or G→P map at L (NO-MEET). **Request:** if the bridge thread builds a formal map from the
matrix level to the pair carrier — at least the two-token dictionary `W 3 ≅ Herm(ℂ² ⊗ ℂ²)` (exact on the DIM-1
objects, k2c P1 [A]) as a kernel statement, with `ContextStable` of a class carried to spectator stability of the image
operations on the image cone — then one theorem would connect K2(c) and the closure clause Kₙ needs. The source thread
does not identify the two clauses; it records that no map between them exists at L.

**Label:** W-DESC and Kₙ-DESC CONJECTURE ([W] + [X] `e3_compress` 7/7, `VERDICT COMPRESSION-DESCENT-EXACT`); the
absence of a map at L: [A] stage 6 NO-MEET; the request itself carries no claim.

## Evidence

| item | pointer |
|---|---|
| source | `research/equivalence` @ `8c67c7fbe22ca817858dc6711c413f7a5e3d45db` |
| proposal | `research/equivalence/handoff-proposals/HP-2-bridge-thread-contextstable-and-b.md`, sha256 `eff477af5f4bd975a0302263fdb411a1f8674b250f4a6e1a6de95e836dbaf452` |
| results rows | `research/equivalence/RESULTS.md` R-E3.1, R-E3.2, R-E3.3, R-E4.1 (sha256 `92270237fbe5a8d4458a64780728bab1f8a02fe01fdca249448b730c0d9b3347`); `NOTES-E3.md` §2–§3 |
| script, output | `research/equivalence/experiments/e3_compress.py` (sha256 prefix `18c3aa1b95e82773`), `.out` (`f4b93781c20574a4`) |
| coordinator audit | replay byte-identical (`research/AUDITS/2026-10-10-round1/equivalence/REPLAY-LOG.txt`); the cited declarations verified at L (`cite_check.out`: ImplementationLocality.lean:359 `ContextStable`, :364 `LabelInvariant`, :506 `Architecture`; SubstratumSource.lean:77 `DrivesElementary`) |

## What the receiving thread may assume

The descent W-DESC / Kₙ-DESC as a CONJECTURE with its exact instances, and the fact that no formal map between the
matrix-level spectator clause and the pair-level clause (b) exists at L. The request is an input to the bridge's
planning (its Theorem B1.1 and the H→P bridge lemma are the natural place), not an obligation.

## What it may not assume

- that `ContextStable` *is* (b): the source thread explicitly does not identify them (§A.25 bridge-scope rule: no
  identification of two obstructions without an explicit formal map);
- that Kₙ is discharged: the descent moves the carrier generality into `ContextStable`, the matrix form of the same
  spectator clause (b) needs.

## Receipt

The receiving thread copies this file into `research/bridge/inbox/` with a commit naming `HO-6 v1` and records in its
`LOG.md` whether and how it relies on it.
