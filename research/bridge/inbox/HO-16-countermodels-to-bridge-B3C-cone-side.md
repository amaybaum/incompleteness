# HO-16 (v1) — countermodels → bridge: Conjecture B3.C from the cone side — an explicit case and the eigenline-orbit mechanism

**From** `research/countermodels` (round 2, optional node C10). **To** `research/bridge` (B3.C; node B7). Written by
the coordinator from the source thread's committed record; version 1, 2026-10-10. Issued together with HO-10 (the
bridge's reachability proof of B3.C conditional on claim (D)); the two are complementary — HO-10 gives existence for
every abelian case through claim (D), HO-16 gives explicit cones in a subclass.

## Statements and labels

1. **A case HO-2 listed as open, settled explicitly** (C10.1). `H₀` = the 2-torus `e^{iα}P_{C2(1)} + e^{iβ}P_{C2(−1)} +
   e^{i(α+β)}P_{|0+⟩} + P_{|1−⟩}` (simple spectrum; two product eigenlines), `G = H₀ ∪ cnot·H₀` (`CNOT = I − 2|1−⟩⟨1−|`
   commutes with `H₀`). The single-defect cone `K({z})`, `z = (I − 2P_{C2(1)})/8`, is a `G`-invariant exotic
   self-dual cone with H1–H3 (EXOTIC-X); its `H₀`-slice is the self-dual polyhedral cone `(ℝ⁴₊ ∩ f*) + ℝ₊f`,
   `f = (−1, 1, 1, 1)`, with seven extreme rays equal to its seven facet normals. Label: CONDITIONAL (X's single-defect
   characterization [A] AUDIT-X; [W] C10.1; [X] `c10_b3c_case` K0–K4; every exact fact, including the facet
   enumeration in both directions, independently confirmed by the coordinator's `indep_checkC2` X6).
2. **The mechanism** (C10.2). For compact `G ∋ cnot` whose identity component is a torus with simple spectrum: if some
   `G`-orbit `O` of eigenlines contains no product vector, put `m = max_{b′ ∈ O} max_{ψ product} |⟨b′|ψ⟩|² < 1` and
   `c = min(2, 1/m)`; the set `G·SEP ∪ {I − cP_{b′} : b′ ∈ O}` is self-positive and `G`-invariant, so EBF gives a
   `G`-invariant self-dual cone with H1–H3 containing a non-PSD member (EXOTIC-E); it is explicit (EXOTIC-X) when
   `O` is a single line (single-defect cone, as in item 1) or consists of maximally entangled lines (an orthonormal
   Bell-type set, Theorem S). Label: CONDITIONAL (EBF [A]; [W] C10.2, read by the coordinator).
3. **Residual region of B3.C from the cone side** (C10.3): simple-spectrum tori in which `G` carries every entangled
   eigenline onto a product eigenline (then every eigenline is reachable, the slice is `ℝ⁴₊`, and exoticity needs
   non-eigen unreachable states — the stage-4 dichotomy); degenerate 2-tori. OPEN here; HO-10's B7-1 reaches both at
   CONJECTURE (written proof) + claim (D).

## Evidence

| item | pointer |
|---|---|
| source | `research/countermodels` @ `e6d42cab` |
| proposal | `research/countermodels/handoff-proposals/HP3-B3C-cone-side.md`, sha256 `3563db52ee303a519644803b1e2ebd98cd4a6e049d90e692e92c078a8bddbc18` |
| results | `research/countermodels/RESULTS.md` sha256 `c377b73a…` (rows C10.1 … C10.3); `NOTES-C10.md` `38a51c0d11c9dae6c80e3412694b815f59a057f152b8611304a9e39cae7f3a08` |
| script, output | `experiments/c10_b3c_case.py` (run 2) `fa3332faae7a9e6c7ad7e0e8815970d70a3bf118571bfd38f66b2a5b1f7b1754` / `.out` `ffc453bfa43a30d5ec699352f55f847867967eb46bc71a1e2f9c31ede8c2613d` (8/8, `VERDICT C10-B3C-CASE-EXACT`, replay identical; run 1 kept, a helper TypeError) |
| coordinator audit | `research/AUDITS/2026-10-10-round2/AUDIT-COUNTERMODELS-R2.md` (X6; C10.2 read) |

## What the receiving thread may assume

Items 1–2 at their labels: in particular that for every simple-spectrum torus with an eigenline orbit free of products
(this includes every case where `G` fixes an entangled eigenline, and HO-2's "no product eigenline" case) the exotic
cone is explicit or EBF-existent as stated, independently of the reachability route.

## What it may not assume

B3.C itself from this handoff (that is HO-10's statement, conditional on claim (D)); that EBF is certified; anything
about degenerate tori from the cone side.

## Receipt

The receiving thread copies this file into its `inbox/` with a commit naming `HO-16 v1` and records in its `LOG.md`
whether and how it relies on it.
