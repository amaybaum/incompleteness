# Gate 1 (scientific accuracy): focused confirmation of PR #918 r25 at `366da4bb`

**Verdict: ACCEPT.** Changes D, E, R2 and R3 are each accurate against Main §2.3, §3.3 and GR §3.3, and the exact statements and coverage are unchanged. The two findings below are optional.

I compared `72e41201` (the same paper as r24 `e64b2a4c`) with `366da4bb`, read-only. I used a detached worktree, now removed, and committed, pushed and commented nothing. Line numbers refer to `366da4bb`.

## 1. Change D (L130): confirmed
**The three things are kept apart:**
- **(i) The actual observations.** "the dealer always starts with red. What the observer actually sees is red at every step, with no uncertainty; what happens from a black start under that preparation is never observed."
- **(ii) The hypothetical comparison.** "The rooted family still asks what the same dynamics and the same hidden preparation would produce from black: that forecast is part of the mathematical comparison, not something this observer measures."
- **(iii) The return horizon, distinct from the recurrence.** "Both forecasts return to certainty at step 2, a return horizon, while the whole world completes its cycle only at its recurrence time, step 3."

**Nothing suggests the observer can reach a black start experimentally, or that hidden odds are chosen per root.**
- The face-down odds are "the same" for both starts.
- "letting the hidden odds change with the start would compare different rules" appears only as the excluded contrast.

**The example is realizable as stated.** I recomputed it exactly.
- Visible states {R, B}, hidden states {0, 1, 2}, and a shared prior uniform on {0, 1}.
- The bijection is φ(R,0)=(R,0), φ(R,1)=(R,1), φ(R,2)=(B,2), φ(B,0)=(R,2), φ(B,1)=(B,1), φ(B,2)=(B,0).
- After one step, the red row is a point mass on R and the black row is (½, ½), so the rows overlap at R.
- After two steps the table is the identity, which makes step 2 a return horizon.
- φ has order 3, so L = 3.
- By Theorem 3 with s = 1 and n = 2, the family is not P-divisible on {0, 1, 2}. That is "fail to chain over the first two steps".
- From every red start the state is fixed, so "no dealt game ever looks uncertain" holds.

**"The overlap comes only from the start that is never dealt" is correct in Main §2.3's sense.**
- Main §2.3 says the failure can occur "possibly only through a row of a root of visible probability zero".
- This example is also an instance of Main's Scope caveat: "a non-permutation row may belong to a root of visible probability zero while the realized law has no gap".
- The sentence does not place the overlap in a single row.

**"A different deck and shuffle" cannot be confused with the swap game.** The new rule is described separately: red stays red, while black may show either colour. In the swap game, both rows are ½J.

**It does not read as a proof.** It is an example placed before the formal statements, with a [Main §2.3] pointer.

## 2. Change E (L146): confirmed
- **The two cases.** The paragraph opens "Two cases differ" and contains "remain established under the theorem's hypotheses, but neither is an accessible observational witness". Main §2.3 Scope supports this: "an observer's statistics are its restriction to accessible windows, and on them the memory is witnessed only by a gap at an accessible order".
- **"the failure of chaining it implies across the cycle" is correct.** A memory witness of order k < L, two positive-probability histories with a common endpoint, gives a non-permutation Γ_s with 1 ≤ s ≤ min(k, L−1). That makes the family not P-divisible on {0, …, L}, with no full-support assumption needed (Main §2.3, Theorem).
- **"which (C4) asserts" matches the paper's (C4)** at L122: "history readback, a memory witness at some accessible order".
- **The four-bit ending reads** "an observer whose observations reach time 3 may detect the memory, while one whose windows end at time 2 cannot detect it through this record". This is accurate, and "may" correctly allows for statistical detection.
- **No conflation.** The paragraph speaks only of conditional memory and the failure of chaining. Hidden predictive memory is not invoked, and P-indivisibility is not equated with memory.

## 3. R2 (§6, L300): confirmed
- The new text reads "Given determinism and an outcome in every run, Bell's theorem leaves two options, giving up ontic parameter independence or measurement independence; with measurement independence retained, quantum Bell correlations then require ontic parameter dependence, whose realization on the substratum without usable signalling and with the gravitational continuum limit is the open hypothesis H-Bell".
- This matches Main §3.3. There, a completion gives up (ii)+(iii), which secure ontic parameter independence, or (iv), measurement independence. H-Bell requires the prepared graph family to "preserve operational no-signaling and satisfy a curvature/metric convergence condition".
- Both alternatives are now stated.

## 4. R3 (L206): confirmed
The gloss reads: "the experimenter can do nothing, combine operations and lump outcomes together, prepare an evenly mixed helper, read the helper without disturbing the system, and discard it". It maps one to one onto the GR §3.3 structure as stated at L206, and onto `FiniteOperationalTheory`:

| Gloss | Structure |
|---|---|
| do nothing | contains the identity |
| combine operations | outcome-conditioned composition |
| lump outcomes together | coarse-graining |
| prepare an evenly mixed helper | uniformly mixed ancilla preparation |
| read the helper without disturbing the system | spectator-independent readout, identity on the system for product inputs |
| discard it | ancilla discard |

## 5. Unchanged material: confirmed
- Every exact statement is word for word as in r24. I checked:
  - Theorems 1–4;
  - both corollaries, with the §2.4 Corollary byte-identical;
  - the Γ_t definition and the plain P-divisibility paragraph;
  - the labelled paragraphs of §§4–6;
  - the Bell paragraphs.
- The ledger is unchanged, so no ID is retired. `coverage_check` reports OK (134 statements).
- Nothing is weakened.

## Optional findings
- **O1 (L130).** "The rooted family" is used one paragraph before its definition at L132. A short gloss would help: "The rooted family, the table of forecasts from every start, still asks …". The anchor is L132, where Γ_t is defined.
- **O2 (L206).** The gloss does not separately mention that an available operation may follow the helper's preparation. "Combine operations" covers it in plain terms, so this is optional. The anchor is GR §3.3 and `prepAvail_post`.

## 6. The owner's two final questions
- **Is every substantive claim supported by its evidence and assumptions?** Yes.
- **Does the paper communicate the strongest results without unnecessary weakening?** Yes.
  - Theorems 1–4 and the recurrence Corollary, including its full-support equivalence and the zero-probability-root caveat, are stated at proved strength.
  - The new example shows that caveat concretely, and it is realizable exactly as described.