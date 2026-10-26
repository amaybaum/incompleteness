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

The independent scientific review of the Introduction draft (`S/paper/sci-review/REVIEW.md` §1.2) checked this exactly with `S/paper/sci-review/probe/card_exact.py` (sha256 `fabb115b…c642`). The output file `card_exact.out` (sha256 `ad598e3c…dc1e`) records the following, for an arbitrary symbolic input $\rho=\begin{pmatrix}a&b\\c&d\end{pmatrix}$:

- **Uniform burn card.**
  - $\Phi_1(\rho)=\operatorname{tr}(\rho)\,I/2$ and $\Phi_2(\rho)=\rho$.
  - The instrument $I_o(\rho)=\tfrac14\sigma_o\rho\sigma_o$, $o\in\{0,x,y,z\}$, sums to $\Phi_1$. Each $I_o$ is completely positive, with $\sum_o K_o^\dagger K_o=I$.
  - The channels $\Psi_o=\mathrm{Ad}_{\sigma_o}$, applied after $I_o$, give $\sum_o\Psi_o\circ I_o=\Phi_2$. Its Choi matrix equals that of $\mathrm{id}$.
  - So **a classical-memory decomposition exists**, in exactly the sense of Main:702 (Bäcker–Beyer–Strunz).
- **Initialized slot.**
  - $J(\Phi_1)$ has rank 2, so every outcome-conditioned processing is measure-and-prepare.
  - $J(\mathrm{id})$ has partial-transpose spectrum $\{1,1,1,-1\}$.
  - So **no decomposition exists**, which confirms Main:702.
- **CP-indivisibility** holds in both cases. $\Lambda\circ\Phi_1$ has rank at most 1 as a linear map, while $\mathrm{id}$ has rank 4, so no linear divisor exists, let alone a completely positive one.

The drafter's earlier numerical check, `S/paper/draft/probe/swap_memory.py`, agrees.

## Corrected wording

Replace the clause at each site.

**OUTLINE-r4 §5-h and SOURCES-r4 §5-h.** In place of "this swap realization admits no classical-memory decomposition (Main:702)", use:

> With the uniform burn card the two-step family admits a classical-memory decomposition in the sense of Bäcker, Beyer and Strunz (instrument $\rho\mapsto\tfrac14\sigma_o\rho\sigma_o$, channels $\mathrm{Ad}_{\sigma_o}$); with the hidden slot initialized to a fixed card the swap admits none (Main:702).

**CONTRIBUTION-r4 non-claim 13.** Use:

> On card inputs its statistics are classical stochastic ones; under the unitary embedding its one-step channel is entanglement-breaking and its two-step family, though CP-indivisible (Main:326), admits a classical-memory decomposition; it violates no Bell inequality.

**RECHECK-r4, RC-A row.** Read "no classical-memory decomposition (Main:702)" as applying to the initialized-slot swap only. The row's other entries stand: classical on card inputs; constant entanglement-breaking one-step channel; identity two-step map; CP-indivisible (Main:326); no Bell violation.

**What is already corrected.** The Introduction draft carries this wording at §4.3 and in §6.5 item 6 (`S/paper/draft/Introduction-r2.md`).

**What needs no change.** Main:702 is correct for what it states, so no Main or book site needs a change.
