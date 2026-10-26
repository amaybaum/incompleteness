# Erratum to the Introduction design records, revision 4: the card-table classical-memory clause

This erratum covers records at `verification/audits/manuscript/introductory-paper-20261025/design/` (branch `draft/oi-introductory-paper-20261025`). Those records are kept as written, and this note records the correction (§A.27, §A.42 item 4).

## The defect

Four sites state or imply that the card game of ch01 §1.11 "admits no classical-memory decomposition", citing Main:702.

| Site | Text |
|---|---|
| `OUTLINE-r4.md:226` (§5-h) | "… and this swap realization admits no classical-memory decomposition (Main:702)" |
| `SOURCES-r4.md:135` (§5-h row) | "… and the realization has no classical-memory decomposition" |
| `review/RECHECK-r4.md:19` (the RC-A check row) | "… CP-indivisible (Main:326); no classical-memory decomposition (Main:702) …" |
| `CONTRIBUTION-r4.md:182–185` (non-claim 13) | Cites Main:702 for the two-step map being non-entanglement-breaking. That map is the identity, so the statement is true. Main:702, however, concerns a different realization, and the non-claim omits that the card game's memory is classical in the sense of Main:702 |

Main:702 (§4.5) proves the no-decomposition result for the swap $\varphi(x,h)=(h,x)$ **with an initialized hidden slot**. That realization has two-step maps $\rho\mapsto|0\rangle\langle0|$ and $\rho\mapsto\rho$. Its argument is that every Kraus operator of the first map has one-dimensional range.

The card game has a burn card that is **uniform** and independent of the hole card. Main:702 says nothing about that preparation, and for it the conclusion is reversed.

## The check

The claim is settled by hand. For every $2\times2$ matrix $X$, the Pauli-twirl identity

$$\sum_{o\in\{0,x,y,z\}}\sigma_o X\sigma_o=2\operatorname{tr}(X)\,I$$

holds, with $\sigma_0=I$. Everything below follows from it and from the two embeddings.

- **Uniform burn card.**
  - $\Phi_1(\rho)=\operatorname{tr}(\rho)\,I/2$ and $\Phi_2(\rho)=\rho$.
  - The instrument $I_o(\rho)=\tfrac14\sigma_o\rho\sigma_o$, $o\in\{0,x,y,z\}$, sums to $\Phi_1$ by the identity. Each $I_o$ is completely positive, with Kraus operator $K_o=\tfrac12\sigma_o$ and $\sum_o K_o^\dagger K_o=I$.
  - The channels $\Psi_o=\mathrm{Ad}_{\sigma_o}$, applied after $I_o$, give $\sum_o\Psi_o\circ I_o(\rho)=\sum_o\tfrac14\sigma_o^2\rho\,\sigma_o^2=\rho=\Phi_2(\rho)$.
  - So **a classical-memory decomposition exists**, in exactly the sense of Main:702 (Bäcker–Beyer–Strunz).
- **Initialized slot.**
  - $\Phi_1(\rho)=\operatorname{tr}(\rho)\,|0\rangle\langle0|$, and $J(\Phi_1)$ (output factor first) has rank 2 with range $|0\rangle\otimes\mathbb C^2$. So every CP map below $\Phi_1$ is $|0\rangle\langle0|\operatorname{tr}(E\,\cdot)$ for some $0\le E\le I$, and every outcome-conditioned processing is measure-and-prepare, hence entanglement-breaking.
  - $\Phi_2=\mathrm{id}$ is not entanglement-breaking: $J(\mathrm{id})$ has partial-transpose spectrum $\{1,1,1,-1\}$.
  - So **no decomposition exists**, which confirms Main:702.
- **CP-indivisibility** holds in both cases. Both $\Phi_1$ are constant on trace-one inputs, so $\Lambda\circ\Phi_1$ has rank at most 1 as a linear map, while $\mathrm{id}$ has rank 4. No linear divisor exists, and so no completely positive one.

**Provenance only.** The scientific review of the Introduction draft reproduced these statements by exact symbolic computation for an arbitrary input $\rho=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. Its script and output are retained in this audit directory at `../draft/review/scientific/probe/card_exact.py` (sha256 `fabb115b48c92dfc1db3aeadde1bf85cc2ded23f8ac3d66c9a453ef0c830c642`) and `card_exact.out` (sha256 `ad598e3c6356b8b1b58aff7aa6b48f7caa7abc09f7582c950e35d09558a9dc1e`). The drafter's numerical check, `../draft/probe/swap_memory.py`, agrees. The correction does not rest on either script.

## Corrected wording

Replace the clause at each site.

**OUTLINE-r4 §5-h.** In place of "this swap realization admits no classical-memory decomposition (Main:702)", use:

> With the uniform burn card the two-step family admits a classical-memory decomposition in the sense of Bäcker, Beyer and Strunz (instrument $\rho\mapsto\tfrac14\sigma_o\rho\sigma_o$, channels $\mathrm{Ad}_{\sigma_o}$); with the hidden slot initialized to a fixed card the swap admits none (Main:702).

**SOURCES-r4 §5-h.** In place of "and the realization has no classical-memory decomposition", use:

> and with the uniform burn card the two-step family admits a classical-memory decomposition in the sense of Bäcker, Beyer and Strunz (instrument $\rho\mapsto\tfrac14\sigma_o\rho\sigma_o$, channels $\mathrm{Ad}_{\sigma_o}$), while with the hidden slot initialized to a fixed card the swap admits none (Main:702)

**CONTRIBUTION-r4 non-claim 13.** Use:

> On card inputs its statistics are classical stochastic ones; under the unitary embedding its one-step channel is entanglement-breaking (Main:286) and its two-step family, though CP-indivisible (Main:326), admits a classical-memory decomposition; it violates no Bell inequality (ch01:286).

**RECHECK-r4, RC-A row.** Read "no classical-memory decomposition (Main:702)" as applying to the initialized-slot swap only. The row's other entries stand: classical on card inputs; constant entanglement-breaking one-step channel; identity two-step map; CP-indivisible (Main:326); no Bell violation.

**Where the corrected wording appears.** The Introduction draft carries it at §4.3 and in §6.5 item 6 (`../draft/Introduction-r2.md` and later revisions).

**What needs no change.** Main:702 is correct for what it states, so no Main or book site needs a change.
