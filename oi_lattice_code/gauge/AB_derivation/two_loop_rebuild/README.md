# two_loop_rebuild/

From-scratch rebuild of the 2-loop staggered VP computation for the $\delta_0$ threshold (SM §6.2), undertaken after an audit (see `../PI_S_CONVENTION_AUDIT.md`) found the prior `two_loop_vp.py` implementation used a scheme-locked $\Pi_s$ convention.

## Status: held in reserve

The rebuild produced partial results (6 of 7 topologies computed) that differ substantially from the prior "8 ± 2" value. The paper (SM §6.2) uses the empirical δ_0 = 10.02 from the U(1) row as the primary source; this rebuild is not used for any derived quantity.

## Files

- **`scalar_bubble_SE.py`** — scalar bubble with fermion-line SE insertion (dominant piece)
- **`vector_SE_insertion.py`** — vector bubble with SE insertion
- **`seagull_SE_insertion.py`** — seagull diagrams with SE insertion
- **`vertex_correction.py`** — vertex correction with internal gauge
- **`sails_correction.py`** — sails (crossed) diagram, 8-γ Dirac trace via explicit Euclidean γ matrices
- **`run_sails_n8.py`** — driver for the computationally expensive N=8 sails calculation

## Conversion

Raw lattice integrands → δ_0 units via `δ_0 = 5.8125 · raw / Π_s = (23.25/4) · raw / Π_s`, verified against the session-k scalar-bubble-SE piece to 3-digit agreement.

## Results at N=8, m=0.05 (δ_0 units)

| Piece | Contribution |
|-------|--------------|
| Scalar bubble SE | +60.2 |
| Vector bubble SE | −0.50 |
| Scalar seagull | −0.01 |
| Vector seagull | −0.07 |
| Vertex correction | +8.13 |
| Sails (N=8 extrap) | ~+4.7 |
| Ghost 2-loop | negligible (verified) |
| **Total** | **≈ +72** |

## Running

Each file is standalone, using the grid/propagator infrastructure compatible with `../paper_pi_s.py`:

```bash
python3 scalar_bubble_SE.py     # ~30 s at N=8
python3 vector_SE_insertion.py  # ~1 min at N=8
python3 seagull_SE_insertion.py # ~1 min at N=8
python3 vertex_correction.py    # ~2 min at N=8
python3 sails_correction.py     # ~5 min at N=6 (use run_sails_n8.py for N=8)
```
