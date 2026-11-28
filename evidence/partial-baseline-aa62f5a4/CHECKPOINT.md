# CHECKPOINT — a11-baseline-aa62f5a4 (RECONSTRUCTED evidence, this session; NOT the original Codex workspace evidence)

1. Worktree SP/a11-baseline-aa62f5a4/wt detached at aa62f5a47454983d0b3ac771450a78118fbaaab7, tree 60fbb0789dc5a3ba1ece60c83e22fcc24ee8b175, clean status (0 entries). Disk 12G free.
2. Procedure source: .github/workflows/ledger-coverage.yml job `suite` (phase tool-acceptance). No prior run of this workflow exists on the host (runs list empty).
3. Inputs: tool-acceptance F = synthetic fixture snapshot S (with CFG path in it), M = synthetic M_rep; TOOL_BASE = origin/main 9be526b6. Codex's S/B/M commits (e.g. S 2cca4002, B 1cf0c02b, M 5312bb2b; later refreshed fixture at 9cef4d22) are absent from the local store and from origin's 2269 advertised refs. No configuration (retirement-config.json, execution-control-config.json, a1-staging-transition.json) exists in the branch tree or on main. No generator on the branch builds S/B/M.
4. Next: write run.sh; run the F-independent steps with timing.
5. run.sh written (mirrors workflow suite job; PARTIAL mode without F/CFG/M). Started in background. self-test exit 0 (0.3s, 97/97), engine exit 0 (8.7s).
6. Checked origin/staging/a1-allow-root-20261127 (8f668f55): carries draft live-staging files under a1exit-deletion-20261121/ (unreviewed WIP), but no configuration and it is not the synthetic fixture; not used.
7. SW1/SW2 are produced by a1_controls.py (sweeps on unless --skip-sweeps); the workflow runs a1_controls without --skip-sweeps, so they are on the CI route; here they are blocked anyway (a1_controls is F-dependent).
8. Partial run complete (~100 s); gate GATE_FAIL 20, 323/114/182; replay identical; BASELINE.md written. Worktree clean; preview objects private. Monitors stopped.
