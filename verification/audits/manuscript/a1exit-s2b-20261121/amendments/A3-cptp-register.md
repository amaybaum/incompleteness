# S2-B amendment A3: spell out CPTP in the measurable-carrier corollary

**Trigger.** At the catch-up merge `cbdfa82a5`, the SC-42 integration checker's added-text scan reported
three caps hits, `('papers/Main.md', 'caps', 'CPTP')`. All three are in edit E2's corollary at
Main:336/338. The checker is left untouched. Approved by the coordinator under the unit's authorization
(owner `amaybaum`, #1169 comment 7056875845) as a register fix. Meaning is unchanged.

**Edits.** Three edits, with line numbers at `cbdfa82a5`. Each old string is unique in `papers/Main.md`.

| Id | Site | Old | New |
|---|---|---|---|
| R9 | Main:336 | `(b) each $\Phi_t$ is CPTP, and` | `(b) each $\Phi_t$ is completely positive and trace preserving, and` |
| R10 | Main:336 | `with no positive trace-preserving map, in particular no CPTP map, $\Lambda$` | `with no positive trace-preserving map, in particular no completely positive trace-preserving map, $\Lambda$` |
| R11 | Main:338 | `so $\Psi_{t,h}$ is CPTP, and` | `so $\Psi_{t,h}$ is completely positive and trace preserving, and` |
