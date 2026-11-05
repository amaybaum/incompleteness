# A3. Equal-time independence of disjoint cells under `π_0`

**Governs:** the citations of "TA (c4)" at base lines 206, 234 and 243.

**Replacement.** At each of those lines the result cited is the following, proved as Proposition IND in
`verification/programmes/oi-qm/reconstruction/k1-rdy-pref-proofs-20261105/PROOFS.md` §4, on `main` at
`4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` (its independent review, model-authored: `REVIEW.md` §1 in the same
directory):

> For every tick `t` and every pair of disjoint cell sets `X, Y`, under `π_0` the variables `X_t` and `Y_t` are
> independent and each is uniform. Hence, for cell sets `W` and `E` and `w ∈ 𝐑^W`, `π_0(E_t = 0 | W_t = w) = q^{−|E∖W|}`
> if `w` is `0` on `W ∩ E`, and `0` otherwise. In particular it is `q^{−|E|}` for every `w` when `W ∩ E = ∅`.

TA (c4) is provenance. The proof uses that `π_0` is uniform on the product space `S` and φ-invariant
(`verification/programmes/oi-qm/reconstruction/k1-rdy-proofs-20261105/LEMMAS.md`, Lemma P1).
