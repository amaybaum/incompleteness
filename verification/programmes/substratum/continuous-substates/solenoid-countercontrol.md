# SUBSTATE-1: an infinite reversible carrier with an exactly Markov visible factor

**Research-only exact paper proof and finite exhaustive regression.** Not Lean-checked, not the interacting OI model. Tracking #1007 and draft #1009.

## Carrier and readout

Let the 3-solenoid be the compact abelian group

\[
\Sigma_3=\varprojlim(\mathbb R/\mathbb Z,\,[3]).
\]

Its elements are compatible circle coordinates \(x=(x_0,x_1,\ldots)\) with \(3x_{j+1}=x_j\bmod 1\). Normalized Haar measure projects to the uniform circle measure on every coordinate. The continuous automorphism \(A(x)=3x\) has inverse \(A^{-1}(x)=(x_1,x_2,\ldots)\); multiplication by one third is therefore valid on this carrier, even though not on the circle alone. Both directions preserve Haar.

The visible bit is 0 when the first circle coordinate is in \([0,1/2)\), and 1 otherwise. For every \(t\ge0\), the first coordinate of \(A^t x\) is \(3^t x_0\bmod1\). Thus the entire forward visible law is the binary coding of the tripling map on the circle with a uniform initial point.

This is an illustrative autonomous group automorphism, **not** the OI gauge-coupled 3-D wave map nor the missing microscopic-to-observer projection.

## Exact all-horizon proposition

**Proposition.** The visible process is a stationary homogeneous two-state Markov chain with

\[
P=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix}.
\]

For every finite visible word \(a_0,\ldots,a_h\),

\[
\Pr(X_0=a_0,\ldots,X_h=a_h)
  =\tfrac12\prod_{j=0}^{h-1}P_{a_j,a_{j+1}}.
\]

Its rooted transition matrices therefore obey

\[
\Gamma_t=P^t=\frac12
 \begin{pmatrix}1+3^{-t}&1-3^{-t}\\1-3^{-t}&1+3^{-t}\end{pmatrix}.
\]

For every positive integer \(t\), \(\Gamma_t\ne I\), and the family is P-divisible via \(\Gamma_t=\Gamma_sP^{t-s}\). Despite its continuous reversible carrier, this observable process has neither positive conditional Markov memory nor the identity-return recurrence obstruction.

**Proof.** Partition the circle into the two half-intervals \(I_0,I_1\). On each source interval \(I_a\), the map \(u\mapsto3u\bmod1\) has two affine inverse branches covering the complete target half \(I_a\), and one branch covering the opposite half \(I_{1-a}\). Every branch has expansion factor 3. Thus a uniform conditional distribution on \(I_a\) moves to \(I_b\) with probability \(2/3\) if \(a=b\), and \(1/3\) otherwise. Conditioning on the target interval leaves a **uniform** distribution within it, since each inverse branch contributes equal constant density. Induction on the full observed word proves the Markov factorization, not just a two-time marginal. Haar is preserved, so the chain is stationary. The constant and alternating eigenvectors of \(P\) have eigenvalues 1 and \(1/3\), yielding the formula for \(P^t\). The off-diagonal entry \((1-3^{-t})/2\) is positive for all \(t>0\). □

The circle factor map is many-to-one, but the underlying solenoid automorphism is **bijective**. Hidden-state Poincaré recurrence (almost everywhere) is consistent with both decaying visible correlations and an exactly Markov visible law.

## Exact integer controls

The companion script solenoid_markov_probe.py enumerates all \(2\cdot3^h\) circle partition atoms with endpoints \(k/(2\cdot3^h)\) and integer midpoint arithmetic, for horizons \(h=0,\ldots,7\). It compares every one of the \(2^{h+1}\) visible words against the Markov product law, checks rooted matrices, matrix powers, total probability, and positive-time non-return. Independent three-time controls include

\[
P(000)=2/9,\quad P(001)=1/9,\quad
P(100)=1/9,\quad P(101)=1/18.
\]

The exact finite enumeration does **not** substitute for the all-horizon argument.

## Verdict and scope

**FAIL** for the claim that merely allowing division by 3 on an infinite compact reversible hidden carrier supplies visible recurrence, hidden memory, or quantum operational capability. It does not. This is not a no-go for different measurable partitions, interactions, settings, or coherent controlled operations. In particular this countercontrol neither selects a Wilson/Yang–Mills action nor proves full QM equivalence.

The next decisive physical experiment must specify one microscopic dynamics, invariant prior, measurable readout and **selectable intervention** from the same ontology. The control with interventions switched off must then lose the claimed genuinely quantum operational resource. Do not confuse this mathematical carrier with the observer-level normalized wave operator of SM §4.1.
