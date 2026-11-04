# PC-1 — status

The preregistration (frozen at `948b30c1`), its amendments and the stage-2 records of runs 1
and 2 are kept unchanged. This note states their standing on `main`; it edits none of them.

**Strict result: `INCONCLUSIVE (void)`.**

- **Stage 1.** Three Python checks, SC-1 to SC-3, were run before the PC★ freeze, which the
  owner's stage-1 authorization excluded (`amendments/PC-star-disposition.md:14–20`). Under
  clause 0(vi) of the frozen decision rule the stage-1 token is `INCONCLUSIVE (void)` (`:24–27`).
- **Stage 2, run 1.** `INCONCLUSIVE (void)` under 0(vi) (`stage2/RESULT.md:22`). Its CI and review rows
  read *pending* (`:114–119`). The run is resolved in `stage2/run-2/RESULT.md:11–17`: draft-PR
  CI run 41231679739 at `f14b59b2`, `Build` failed and `Release gate` was skipped, so the void
  reasons are 0(vi) and 0(v).
- **Stage 2, run 2.** `INCONCLUSIVE (void)` under 0(vi); both kernel steps succeeded at its head,
  so 0(v) is not added (`stage2/run-2/RESULT.md:34–35`, `:109–111`).

**Scientific finding, carried only under an owner exception.** Among the 25 candidates screened,
none is admissible; the obstruction is G★ item 3 for native couplings
(`stage2/run-2/RESULT.md:36–40`; `amendments/PC-star-disposition.md:29–32`). The owner's
one-time exception that carries it is PR #1022 comment 6547077354 (amaybaum,
2026-10-31T17:56:33Z). It is not the unit's token and not a no-go.

**Review limitations.**

- `stage2/run-2/review.json` records verdict CONFIRM at `0979a53e`. Its reviewer is recorded as
  "independent read-only reviewer (Claude subagent, coordinated session
  013T6pfKuv5mi3MXtKjH2tZb)": a read-only agent coordinated by the session that wrote these
  records.
- The reviews cited as independent for the paper proofs P-1 to P-3 and for the screening finding
  (`amendments/PC-star-disposition.md:19–20`, `:29–30`) are not on `main`.
- The finding and the paper proofs are therefore not independently validated on `main`, and are
  not premises until they are (AGENTS.md §A.46 item 7). The kernel statements of
  `OIBridge.PC1Controls` are kernel-checked; the census lists the module as kernel-only.
