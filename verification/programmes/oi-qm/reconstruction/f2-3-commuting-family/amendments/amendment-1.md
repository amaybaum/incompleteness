# F2-3 amendment 1 (2026-10-15, before any decisive computation)

Append-only amendment to `../RULES.md`, made before `f2_3_exact.py` exists. It changes one clause of
K-gen and nothing else.

**K-gen, third condition.** The frozen text requires the correction K to be "supported inside one
eigenspace class of the gate". The exponentiation e^{2πi(G₀+K)} = e^{2πiG₀} · e^{2πiK} = δ(m) needs
only that K commutes with G₀ and has integer spectrum. The correction (1 − C⊗C)/2 of M_C commutes
with every eigenprojector of δ(m) but spans several classes, so the clause as written would fail
for a valid generator.

The condition reads instead:

- K is block-diagonal with respect to the gate's eigenspace classes, that is, K commutes with every
  eigenprojector of δ(m);
- for M_φ and for the R_star member, K lies inside a single class, and this is checked as well.

The first two conditions (K Hermitian with K² = K; [K, G₀] = 0) are unchanged.
