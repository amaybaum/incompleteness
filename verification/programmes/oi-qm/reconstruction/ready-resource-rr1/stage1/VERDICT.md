# RR-1 stage 1: verdict

**STAGE-VOID.** The stage gate S0 fails, so no candidate token is issued and no candidate classification stands.

## Why
- **Frozen protocol:** `preregistration.md` in the parent directory, at `c41e0e6f` (blob `77a471ac`). It is unchanged.
- **The ambiguity:** its G7 pin-ablation step ("each given π_0 on its cells", PR:95–98) does not say how to treat a cell pinned by two overlapping inventory items. The independent review (`REVIEW.md`) rules this genuinely ambiguous.
- **The stop rule:** a step not decidable on paper ends in UNRESOLVED (PR:24–25, 98). So the positive control POS-1 stops at UNRESOLVED(G7), and S0 fails (PR:74–75, 107).

## What the void does and does not mean
- It records under-specification in the frozen text, not a control failing on substance. The review notes, as a diagnostic only, that POS-1's pass condition holds under each reading taken separately.
- It is **not** a negative physics result.
- `RESULT.md` is the execution record as written, unrepaired. Its tokens are void with the stage.

## Carried forward to any successor (from `REVIEW.md`)
- Fix the overlap rule and the source-table order (Findings 1–2).
- C3's G7(3) stop is decidable from the sources: q8 = (0, x⊕u, 0) on all 4096 rows. Its stated step is wrong (Finding 3).
- C2 stops at G1, not G7 (Finding 4). C4's stated reason needs correcting (Finding 5).
- The low-severity findings are 6–12.

## Status
Recorded on owner approval in chat on 2026-11-01: "Record `STAGE-VOID` on #1025 … Do not issue candidate classifications or interpret the void as a negative physics result. A successor requires a separately reviewed and authorized amendment."

No successor, amendment or re-run is authorized.
