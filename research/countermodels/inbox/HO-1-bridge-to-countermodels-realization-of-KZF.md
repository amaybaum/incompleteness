# HO-1 (v1) — bridge → countermodels: the exotic pair K(Z_F) is realized by embedded observers, exactly

**From** `research/bridge` (node B4). **To** `research/countermodels`. Written by the coordinator from the source
thread's committed record; version 1, 2026-10-10.

## Statement

There is a finite deterministic reversible model, built with the framework's reversible machinery (Main.md:544–558) in
its adopted Bell branch (a) (Main.md:392), with: a visible step counter and record; two hidden wing registers each
holding the normalized joint table, seeds and a stack; instruments `cnot`, `actC nflip`, `actT nflip` as bijections of
the register values, local sharp measurements with measure-and-prepare update (A's intervention writes B's register:
parameter dependence), and the joint measurement `{y, E00 − y}` with `y` certified in K(Z_F); preparation `4 z_(1,1)`;
seed grid `G = 20`. Its properties:

1. its outcome law equals the K(Z_F) GPT law exactly on all listed protocols;
2. its axis statistics reconstruct `4 z_(1,1)`, which is not quantum (`tr(M P) = −2` as a comparison);
3. `S_CHSH = 14/5`;
4. it is operationally no-signalling and local measurements commute operationally;
5. each step map is injective on its reachable configurations;
6. the two registers agree;
7. the token's `S`, `cyc3` and `R_z(θ)` (available to the isolated token) are not pair instruments: each gives a
   negative threshold before a valid K(Z_F) joint measurement (`−1/2`, `−1/2`, `−2/5`);
8. the same probes are valid on `Q3` from `phiW` (`1/2`, `1/2`, `9/20`).

**Label:** CONDITIONAL (on branch (a) and the general finite response construction — the framework's adopted options,
Main.md:392; not the SM/GR lattice representative). The source thread's reading: INDEPENDENCE of (b) survives embedding;
the single stated H-level clause whose addition excludes K(Z_F) is the spectator clause read at the hidden level
(OI⁺-1), which fails the disguise test.

## Evidence

| item | pointer |
|---|---|
| source branch, commit | `research/bridge` @ `5f4089a4500a59943c33ba13656b2530824068c5` (proposal file last changed at `0e601e17`) |
| proposal | `research/bridge/handoff-proposals/HP-3-realization-KZF.md`, sha256 `9c6762870e3797cfe83b41a3861de29ca519735f81b394c400532474d7c1d607` |
| results rows | `research/bridge/RESULTS.md` rows B4-1, B4-2, B4-3; sha256 `eac88347fa62fec0a7c74a221b913ed288c6c74ea696e1269a817d72697796ba` |
| script, output | `research/bridge/experiments/b4_realization.py` (sha256 prefix `aecb983a4aa5128a`), `.out` (`0206b3c43886dbae`), R1–R13 13/13, `VERDICT B4-REALIZATION-EXACT`; full hashes in `research/AUDITS/2026-10-10-round1/EVIDENCE-HASHES.txt` |
| coordinator audit | replay byte-identical (`research/AUDITS/2026-10-10-round1/bridge/REPLAY-LOG.txt`); independent check `indep_checkB.py` X4 (CHSH 14/5 for `phiW` and every defect), X5 (measure-and-prepare law = GPT law exactly, probabilities in [0, 1], no-signalling marginals, every threshold on the 20-grid), X3 (thresholds `−1/2, −1/2, −2/5` against `Q3` controls `1/2, 1/2, 9/20`): CONFIRMED, run 2, replay identical |

## What the receiving thread may assume

Exactly the proposition above, at its label. In particular: an exact finite embedded-observer realization of K(Z_F)
exists in branch (a); the realization question that the stage-6 note §6 and R6 §8 left open at L is decided in the
existence direction for this class of realizations.

## What it may not assume

- that the realization satisfies the SM/GR lattice representative's constraints (C1)–(C4), or is the framework's
  canonical substratum — it is a model in the adopted general finite response class;
- any statement about (b) stronger than item 7: the token operations `S`, `cyc3`, `R_z(θ)` are not pair instruments
  *in this realization*; nothing here derives or refutes (b) at L;
- that any of this is kernel-checked: nothing in HO-1 is CERTIFIED.

## Receipt

The receiving thread copies this file into `research/countermodels/inbox/` with a commit naming `HO-1 v1` and records
in its `LOG.md` whether and how it relies on it.
