# Reversible infinite-tape XOR counterexample

Research-only mathematical construction. Paper proof; no Lean certification or native physical sourcing is claimed. The construction was first recorded in [#1007](https://github.com/amaybaum/incompleteness/issues/1007#issuecomment-6529586144).

### Exact autonomous model and normalized state

Let \(\Omega=\mathbb Z/3\mathbb Z\times(\{0,1\}^2)^{\mathbb Z}\), with state \((p,(A_k,B_k)_{k\in\mathbb Z})\). Use uniform phase \(p\in\{0,1,2\}\), and independent fair binary pairs \((A_k,B_k)\) for every integer \(k\), giving a normalized product probability measure \(\mu\). Set \(C_k=A_k\oplus B_k\).

The measurable **finite** observable at phase \(p\) is the bit \(\pi(p,\mathbf{A},\mathbf{B})=(A_0,B_0,C_0)_p\). The bijection \(T\) advances the phase: at \(p=0,1\) increment \(p\) and retain the tape; at \(p=2\) reset phase to 0 and shift the bilateral block tape by one (\((A_k,B_k)\mapsto(A_{k+1},B_{k+1})\)). The inverse decrements phase and shifts the tape back at the wrap. This map preserves \(\mu\), including the phase. It is a reversible *uncountable* hidden-carrier construction with one visible bit and a common invariant normalized initial state.

To express it in the **independently prepared visible-root + common hidden-prior form**, take \(V=\{0,1\}\) and \(H=\{0,1,2\}\times\{0,1\}\times(\{0,1\}^2)^{\mathbb Z\setminus\{0\}}\), with \(x\sim\mathrm{Bern}(1/2)\) independent of \(h=(p,z,\text{other blocks})\). Recover block zero by
- \(p=0\): \((A_0,B_0)=(x,z)\);
- \(p=1\): \((A_0,B_0)=(z,x)\);
- \(p=2\): \((A_0,B_0)=(z,z\oplus x)\).

This is a measure-preserving bimeasurable bijection \(\Psi:V\times H\to\Omega\). Conjugate the update by \(\Psi\); the resulting time-homogeneous dynamics on \(V\times H\) remains a measurable, measure-preserving bijection with the *same* hidden prior at both roots.

### All-time result (paper-level exact proof, not Lean-certified)

For any two distinct times \(s<t\), the observed bits \(X_s=\pi(T^s\omega)\), \(X_t=\pi(T^t\omega)\) are independent and uniform. Conditional on each phase, this follows because \((A_k,B_k,A_k\oplus B_k)\) are **pairwise independent** fair bits within each block and distinct blocks are independent; averaging over phases preserves their joint law. In particular, for **every** integer \(t\ge1\),
\[
\Gamma_0=I_2,\qquad
\Gamma_t=J_2:=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix}.
\]
Thus \(\Gamma_t=\Gamma_s\Lambda_{s,t}\) with row-stochastic \(\Lambda_{0,t}=J_2\) for \(t>0\), and \(\Lambda_{s,t}=I_2\) for \(1\le s<t\). **The rooted two-time family is P-divisible for all finite times.** No global identity return \(\Gamma_L=I\) occurs for \(L>0\).

Nevertheless the **three-time visible law is not Markovian**. For \(X_0,X_1,X_2\), the initial phase equals zero with probability \(1/3\), making the aligned triple \((A_0,B_0,A_0\oplus B_0)\); at the other two phases the triple contains independent bits from distinct blocks. Therefore the exact joint probability is \(1/6\) for each even-XOR-parity triple, \(1/12\) for each odd-parity triple. Consequently, for every \(a,b\):
\[
\Pr(X_2=a\oplus b\mid X_0=a,X_1=b)=2/3,\quad
\Pr(X_2=a\oplus b\mid X_1=b)=1/2.
\]
The conditional law changes by \(1/6\) despite a common present state, giving C4 history readback on a **two-step accessible window**. The precise conditional mutual information is
\[
I(X_0;X_2\mid X_1)=1-h_2(2/3)\simeq0.081704165946\text{ bits}>0.
\]

### OI diagnostics / scope

- **C1:** YES (hidden-to-visible influence: the next observable bit depends on the hidden block/phase).
- **C2-structural:** YES (the local pair is retained over the aligned three-read cycle and mediates the history-sensitive conditional; the full map is invertible). **C2-slow** is **not** established or required by this countercontrol.
- **C3:** YES (hidden tape has more than enough capacity for positive accessible conditional memory).
- **C4:** YES by the explicit \(1/6\) next-law gap at order 1, not by assuming the observer was selected because it is P-indivisible.
- **No additional physical claim:** no explicit 3-D OI wave update, horizon entropy, sourced measurement-intervention menu, Yang–Mills action, full quantum instrument structure, or proof of a causal *write-then-read* mechanism beyond Main's weaker C4 meaning. It is a mathematical dynamics-and-interface counterexample, not a native physical realization.
- **Finite-S theorem preserved:** on a finite carrier, recurrence forces a later \(\Gamma_L=I\) and obstructs P-divisibility when \(\Gamma_s\) is non-permutation. Here \(S\) is infinite and no such global visible return occurs, so there is no contradiction.
- **Universal representation survives:** the exact finite-horizon \(S\Leftrightarrow D\Leftrightarrow Q_{\mathrm{fb}}\) claim applies to these finite visible words. It does not imply stochastic P-indivisibility or full operational QM.


## Bounded reproduction

Run `python3 -I -B verification/programmes/substratum/continuous-substates/infinite_xor_probe.py`. It enumerates all input blocks/phases through horizon 7, checks normalization, root pair independence and the three-time memory gap with exact fractions. Python optimization does not disable its checks. This finite regression does not establish the all-time result; that follows from the pairwise-independence proof above. The finite-S recurrence theorem retains its original finite-carrier premises.
