# SUBSTATE-2 / FIXED-SCALE-1 — frozen test specification (research only)

**Preregistered before computation.** Draft PR #1011 / issue #1010.
This models **one fixed** reversible level-to-level interaction, not a
physical OI derivation, quantum instrument or Yang–Mills action.
No manuscript changes or adoption of new premises.

## Actual single infinite model

The state is \(x=(a,r,c)\), with two bits \(a,r\in\mathbb F_2\)
and a bi-infinite tape \(c=(c_i)_{i\in\mathbb Z}\in\{0,1\}^\mathbb Z\).
Use product-fair measure. Define the left shift \(Sc\) by
\((Sc)_i=c_{i+1}\). The single fixed reversible rule is

\[
T(a,r,c)=(a\oplus r\oplus c_0,\;r,\;Sc).
\]

The inverse reads \(c=S^{-1}c'\), then
\(a=a'\oplus r\oplus c_0\). This is a continuous homeomorphism
of a compact totally disconnected Cantor-like product space,
preserving product-fair measure: for each fixed tape and r,
the map on a is a permutation; the tape shift is measure preserving.

The **finite visible record** is
\(O_t=(a_t,c_t)\) with \(c_t\) the tape value at index t,
so \(|V|=4\). The hidden bit r is static and physically unavailable.
Future observations can depend on arbitrarily remote *initial*
tape coordinates as time grows; there is no second dynamical rule
for each depth. Treat the index as internal hierarchical resolution,
not as spatial dimension without further sourcing.

## Predicted exact infinite-law conclusions

For any \(t\ge0\),
\[
 a_t=a_0\oplus(t\bmod2)r\oplus
       \bigoplus_{j=0}^{t-1}c_j,\qquad O_t=(a_t,c_t).
\]

Under product-fair measure:
- \(\Gamma_0=I_4\), and for **every** \(t\ge1\), the rooted
  transition \(\Gamma_t=J_4/4\), each row uniform. Hence the
  family **is P-divisible** on \(\mathbb N\), even though
  there is no common exact visible return time.
- For every \(t\ge1\), \(r=a_{t-1}\oplus a_t\oplus c_{t-1}\)
  is recovered from the earlier two visible records.
  Given just \(O_t\), r is unbiased and the next a-bit
  is fair; given \(O_{t-1},O_t\), the next a-bit is fixed.
  Thus **conditional memory**
  \(I(O_{t-1};O_{t+1}\mid O_t)=1\) bit exactly.
  Note that the next fresh tape bit remains fair even
  given the entire prior visible history.
- The visible process has **no positive common exact
  return**: at time L, \(c_L\) is independent of \(c_0\),
  and \(P(O_L=O_0)\le 1/2\).
- All observations are continuous finite-valued maps
  on the Cantor hierarchy. For any fixed horizon,
  a finite prefix suffices, but the necessary depth
  grows with time. Hence the infinite trajectory
  cannot be controlled by one finite prefix.

This tests the possible strict separation between
**two-time P-divisibility** and **multi-time predictive
memory**; do NOT infer quantum CP-divisibility or
composable instruments from either.

## Mandatory negative controls and boundaries

1. **Remove the static hidden feedback:** use
   \(T_0(a,r,c)=(a\oplus c_0,r,Sc)\), with identical
   source/readout. The visible process is first-order
   classical Markov because \(a_{t+1}=a_t\oplus c_t\).
   Its three-time conditional memory is zero.
2. **Uncoupled observation:** monitor only \(c_t\).
   This is iid fair and has neither hidden memory
   nor exact common return, though the carrier is reversible.
3. **Finite cyclic approximations:** take n tape bits
   \(c_0,\ldots,c_{n-1}\) with cyclic left rotation,
   same a/r coupling and uniform counting measure.
   Exhaustively check n=3,4,5,6,7,8,9 (maximum
   \(2^{n+2}=2048\) full states) and finite windows
   \(1\le t<n\). The finite cyclic variants
   **necessarily** have some global permutation period,
   so do **not** assert the infinite no-return verdict
   for them. At \(t=n\), a tape bit repeats, changing
   the rooted map; this is a boundary/finite-size
   countercontrol.
4. **Observed law:** calculate all length-three
   joint record probabilities (32 supported triples,
   each with mass 1/32, when n>=3), the 4x4 rooted
   channel family for \(1\le t<n\), and conditioned
   next-a distributions both with and without prior
   visible record. Full-finite exact integers only.
5. **Prefix witness:** for every desired depth m,
   find two tapes agreeing on initial positions
   \(0,\ldots,m-1\), with different \(c_m\), such
   that their observable record differs at time m.
   This is a mathematical depth witness, not a
   physically realized access mechanism.
6. **No tuning/no novel physics claims:** the
   same T, prior and pi apply to every n and every
   tested protocol, without changing a kernel
   after seeing desired observables. No classical
   memory witness is promoted into QM interference,
   Bell nonlocality, Wilson action, log-periodic
   scaling or physical boundary entropy.

**Decision rule:** accept a *mathematical fixed-rule*
counterexample showing arbitrarily deep future
sensitivity and predictive memory with a P-divisible
rooted law **only if all exact controls pass**;
otherwise REVISE and retain failures. Even PASS is
a **classical** mechanism and remains an unsourced OI
physical extension. Next test requires independent
physically sourced intervention/QM/YM discriminants.
