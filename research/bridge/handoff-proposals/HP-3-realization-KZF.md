# HP-3 — the exotic pair K(Z_F) is realized by embedded observers (branch (a)), exactly

From `research/bridge`, node B4. Proposed for the countermodels thread and for the overview. It resolves the item that
the stage-6 note §6 and R6 §8 left "open at L, either way". The coordinator routes.

**Proposition HP-3.** There is a finite deterministic reversible model with the following components.
- **Visible:** a step counter and a record.
- **Hidden:** two wing registers, each holding the normalized joint table; seeds; a stack.
- **Instruments:**
  - `cnot`, `actC nflip` and `actT nflip`, as bijections of the register values;
  - local sharp measurements with measure-and-prepare update; A's intervention writes B's register (parameter
    dependence);
  - the joint measurement `{y, E00 − y}`, with `y` certified in K(Z_F).
- **Preparation:** `4 z_(1,1)`.
- **Grid:** `G = 20`.

The model has these properties.
1. Its outcome law equals the K(Z_F) GPT law exactly on all listed protocols.
2. Its axis statistics reconstruct `4 z_(1,1)`, which is not quantum: as a comparison, `tr(M P) = −2`.
3. `S_CHSH = 14/5`.
4. It is operationally no-signalling, and local measurements commute operationally.
5. Each step map is injective on its reachable configurations.
6. The two registers agree.
7. The token's `S`, `cyc3` and `R_z(θ)`, which the isolated token has, are not pair instruments. Each gives a negative
   threshold before a valid K(Z_F) joint measurement: `−1/2`, `−1/2`, `−2/5`.
8. The same probes are valid on `Q3`, from `phiW`: `1/2`, `1/2`, `9/20`.

Evidence: [X] `experiments/b4_realization.py`, R1–R13 (13/13, replay byte-identical).

**Reading.** INDEPENDENCE survives embedding. The single stated H-level clause whose addition excludes K(Z_F) is the
spectator clause read at the hidden level (OI⁺-1). Its disguise test fails. Main.md:562 ("not a uniqueness theorem")
is thereby exhibited for a cone in `W 3`.

Evidence: `NOTES-B4.md`; `experiments/b4_realization.{py,out,replay.out}`.
