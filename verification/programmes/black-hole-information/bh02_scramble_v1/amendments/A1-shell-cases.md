# Amendment A1 — C6(c) shell cases (before any code was run)

Made after the plan's commit and before `checks.py` existed or any program was run. Basis: a
hand estimate (no program) of the concavity bound `S(Tr_B Π_w / dim Π_w)` for the preregistered
half-filling case `(n, w, |R|) = (6, 3, 3)` gave about 2.0 nats against `S_Page(8, 8)` of about
1.59, so at half filling the concavity bound lies above the Page value and cannot certify a strict
gap either way. The preregistered cases are kept and reported as they come out.

Changes:

1. C6(c) adds the off-half-filling cases `(n, w, |R|) ∈ {(8, 2, 4), (10, 2, 5), (12, 3, 6)}`,
   where the shell's per-mode entropy is below `ln 2`.
2. C6(c) adds two NUMERICAL diagnostics for every case: a seeded Haar-on-shell Monte Carlo mean
   (2000 samples), and the exact sector-decomposition average
   `Σ_j (d_j/D)[S_Page(a_j, b_j) + H_D − H_{d_j}]` (sectors `j` = Hamming weight on `R`,
   `a_j = C(|R|, j)`, `b_j = C(n−|R|, w−j)`, `d_j = a_j b_j`, `D = Σ d_j`; the form given by
   Bianchi and Donà 2019 for a conserved charge), which must agree with the Monte Carlo mean within
   4 standard errors or the diagnostic is reported as failed. The verdict does not rest on the
   sector formula.
3. Decision rule unchanged in form: CONDITIONAL (an unstated hypothesis of Theorem A.8) iff the
   strict inequality `S(canonical) < S_Page(d_R, d_B)` is certified with rigorous log intervals in
   at least one case, original or added; the report lists which cases certify.
