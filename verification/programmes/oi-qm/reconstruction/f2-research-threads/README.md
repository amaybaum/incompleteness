# F2 research threads A–I — research records, not adopted

Base: `main` at `5bfdaba6`. Research records of the reconstruction threads run on 2026-10-14 toward
the programme's F2 endpoint. Nothing here is adopted, certified or a round, and nothing here is
for merge into `main` without separate review. Failed candidates and counterexamples are kept as
evidence. The compiled design modules (pair interface, relative two-NOT transport) are on
`research/pair-interface-design-20261014`.

Evidence labels used throughout: [K] kernel at `5bfdaba6`; [D] compiled design (run cited);
[W] written argument; [X] exact computation; [N] numerical, float64; [L] literature; [U] unsourced.

| file | thread | content |
|---|---|---|
| `A-target-statement.md` | A | finite target statement, hypotheses H0–H28, missing links M0–M9 |
| `B-interface-lemmas.md`, `work-B/` | B | cone ↔ implementation-class interface lemmas; exact checker (57 checks) |
| `C-kn-desc-refresh.md` | C | KN-DESC-1 (#823) refresh at `5bfdaba6` |
| `D-readiness.md` | D | readiness of #821, #822, #824, #825, #830 |
| `E-bell-composite.md`, `work-E/` | E | Bell and composite coverage; correlation clause; exact checker |
| `F-relative-gate.md`, `work-F/` | F | relative two-NOT transport for #822; exact countercontrol probe and mutations |
| `G-stage-test.md` | G | whether the target needs #821's stage-test transport; the countability finding |
| `H-extension-candidates.md`, `work-H/` | H | six candidate extension principles past the frozen-sourcing barrier, ranked; numerical probes |
| `I-f2-sufficiency-target.md` | I | the F2 sufficiency statement, hypothesis table, gap map, redundancies |
| `step4-pair-interface-statement.md` | step 4 | statement of the compiled pair assembly |

`work-H/probe_H.py` replays byte for byte against `work-H/probe_H.out` (33 checks, 0 failures); it
needs NumPy and SciPy and is numerical except where a check is marked EXACT.
