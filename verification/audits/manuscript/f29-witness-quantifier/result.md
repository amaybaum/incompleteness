# F29: the witness quantifier in the characterization theorem

Correction of clause (iii) of the characterization theorem (`papers/Main.md` §3.4) and its
paraphrases. Finding and analysis: Issue #931.

## The defect

Clause (iii) quantified over "every $K \geq k+1$, with $k$ an order at which (ii)'s conditional
mutual information is positive", and `papers/GR.md` and `book/glossary.md` (mirrored in
`book/The-Incompleteness-of-Observation-FULL.md`) stated the same condition as "every finite
accessible horizon containing a memory witness".

- Read universally, the condition holds vacuously for a Markov law, which has no memory-witness
  order, while (ii) fails. So (ii) $\iff$ (iii) was false for every Markov law.
- Read existentially over memory-witness orders, (iii) contains (ii), and (iii) $\Rightarrow$ (ii)
  is trivial. The proof states that this direction is the readback lemma.

## The correction

(iii) binds the order itself: *for some accessible order $k$ and every finite accessible horizon
$K \geq k+1$*, $\mathcal{S}$ arises from a deterministic bijection with (C1), (C3) and (C4)
history readback at $k$. The proof is unchanged:
- (iii) $\Rightarrow$ (ii) is the readback lemma at $K = k+1$, the gap being a gap in
  $\mathcal{S}$'s own conditionals by the pushforward identity (universal theorem, (a));
- (ii) $\Rightarrow$ (iii) is the finite-horizon process dilation at each $K$, for an order $k$
  at which (ii) holds.

The remark on the horizon restriction states that any order satisfying (iii) is a memory witness.
No other claim changes.

## Acceptance test

`acceptance.py` (exact rationals; the conditional mutual informations are floats used only for
strict inequalities). For a memoryless process M and two processes with accessible memory
witnesses, N1 (witnesses at orders 1 and 2) and N2 (order 2 only), it builds the process
dilation of the constructive proof from each target's kernels at every horizon $K \leq 3$ and
checks faithfulness, bijectivity, the pushforward identity, (C1), (C3) and (C4) at each order.

| Process | Witness orders | (ii) | corrected (iii) | universal reading of the old (iii) |
|---|---|---|---|---|
| M | none | false | false | true (vacuous) |
| N1 | 1, 2 | true | true | true |
| N2 | 2 | true | true | true |

- (ii) $\Rightarrow$ (iii): at every witness order and every $K \geq k+1$, the dilation is
  faithful and carries (C1), (C3) and (C4) at $k$.
- (iii) $\Rightarrow$ (ii): at every (C4) gap observed, the readback bound
  $I(X_{<k}; X_{k+1} \mid X_k) \geq p_0\delta^2/\ln 2 > 0$ holds.
- For M, the dilation is faithful and carries (C1) but no (C4) gap at any order: the existence
  of a realization alone does not distinguish non-Markovian laws, as `Main.md` §3.4 states.
- Controls: every realization reproduces its target joint law exactly and is a bijection; the
  pushforward identity holds on every history; a mutated quantile step is detected as unfaithful
  in every case; the gap detector finds orders 1 and 2 for N1, order 2 only for N2, and nothing
  for an i.i.d. process.

Run: `python3 -I verification/audits/manuscript/f29-witness-quantifier/acceptance.py`. Output:

```
control M.K2.bijective: PASS
control M.K2.faithful: PASS
control M.K2.mutant_detected: PASS
control M.K2.pushforward: PASS
control M.K3.bijective: PASS
control M.K3.faithful: PASS
control M.K3.mutant_detected: PASS
control M.K3.pushforward: PASS
control N1.K2.bijective: PASS
control N1.K2.faithful: PASS
control N1.K2.mutant_detected: PASS
control N1.K2.pushforward: PASS
control N1.K3.bijective: PASS
control N1.K3.faithful: PASS
control N1.K3.mutant_detected: PASS
control N1.K3.pushforward: PASS
control N2.K2.bijective: PASS
control N2.K2.faithful: PASS
control N2.K2.mutant_detected: PASS
control N2.K2.pushforward: PASS
control N2.K3.bijective: PASS
control N2.K3.faithful: PASS
control N2.K3.mutant_detected: PASS
control N2.K3.pushforward: PASS
control detector.N1_orders_1_2: PASS
control detector.N2_order2_only: PASS
control detector.iid_clean: PASS

M: witness orders W = []; CMI_k (bits) = k=1: 0.000000, k=2: 0.000000; I* = 0.000000
  K=2: |C_H|=432, faithful=True, C1=True, C3=True, C4: k=1: none
  K=3: |C_H|=6912, faithful=True, C1=True, C3=True, C4: k=1: none, k=2: none
  (ii) = False; corrected (iii) = False; biconditional holds: True; as expected: True
  (ii) => (iii) via dilation at every witness order: True; (iii) => (ii) readback bound at every observed gap: True
  original universal-over-witness reading of (iii) = True  (vacuous: no witness order)

N1: witness orders W = [1, 2]; CMI_k (bits) = k=1: 1.000000, k=2: 1.000000; I* = 1.000000
  K=2: |C_H|=108, faithful=True, C1=True, C3=True, C4: k=1: p0=1/4, delta=1
  K=3: |C_H|=864, faithful=True, C1=True, C3=True, C4: k=1: p0=1/4, delta=1, k=2: p0=1/4, delta=1
  readback bound K=2, k=1: I = 1.000000 >= p0 delta^2/ln2 = 0.360674 (margin 0.639326): True
  readback bound K=3, k=1: I = 1.000000 >= p0 delta^2/ln2 = 0.360674 (margin 0.639326): True
  readback bound K=3, k=2: I = 1.000000 >= p0 delta^2/ln2 = 0.360674 (margin 0.639326): True
  (ii) = True; corrected (iii) = True; biconditional holds: True; as expected: True
  (ii) => (iii) via dilation at every witness order: True; (iii) => (ii) readback bound at every observed gap: True
  original universal-over-witness reading of (iii) = True

N2: witness orders W = [2]; CMI_k (bits) = k=1: 0.000000, k=2: 1.000000; I* = 1.000000
  K=2: |C_H|=108, faithful=True, C1=True, C3=True, C4: k=1: none
  K=3: |C_H|=864, faithful=True, C1=True, C3=True, C4: k=1: none, k=2: p0=1/8, delta=1
  readback bound K=3, k=2: I = 1.000000 >= p0 delta^2/ln2 = 0.180337 (margin 0.819663): True
  (ii) = True; corrected (iii) = True; biconditional holds: True; as expected: True
  (ii) => (iii) via dilation at every witness order: True; (iii) => (ii) readback bound at every observed gap: True
  original universal-over-witness reading of (iii) = True

VERDICT: ACCEPT - the corrected (iii) agrees with (ii) on the memoryless process and on both processes with an accessible memory witness, with both proof directions exercised.
```
