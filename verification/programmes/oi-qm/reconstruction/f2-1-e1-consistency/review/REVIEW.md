# F2-1 review of the exact run

- **Replay.** `python3 -I e1_exact.py` rerun in a fresh directory reproduces `e1-exact-output.txt`
  byte for byte (sha256 `ab50a37d…`, 6 min 15 s, standard library only). A local run, not a
  `check-run` attestation.
- **Rules.** The run follows `RULES.md` at `6481ead7` with amendment 1 at `9d996159`; no cell was
  measured before the amendment.
- **Locality, independent check [N].** `locality_check.py`: for q = 3 and four global phases of the
  one-site Fourier-type image U, the principal logarithm of U ⊗ U differs from log U ⊗ 1 + 1 ⊗ log U
  modulo the identity (norms 5.9–11.9). The eigenphases of U span π, so their pairwise sums cross
  the branch cut under every global phase. T as frozen, the principal logarithm of the global
  update, couples sites that the update leaves uncoupled.
- **Literature step not checked.** The Campbell–Anwar–Browne Appendix D statement could not be
  read from this environment (arXiv unreachable). The density token `E1-DENSE [L]` rests on the
  amendment's quotation; its scope for N-qudit Clifford groups at N = 2 is unconfirmed.
