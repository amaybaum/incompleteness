# F29 follow-ups: change note

This change carries out the two items that Issue #931 left open after #932 (`0e11285d`).

- **Branch:** `fix/f29-followups-20261026`.
- **Base:** `main` at `c967d6a9`.
- **Verification:** `VERIFY.md`, which also analyses both proof directions and non-vacuity.
- **Corpus search:** `SEARCH.md`.
- **Probe:** `readback_indexing_probe.py`.

## Owner decision (amaybaum, 2026-10-26), verbatim

> Prepare both remaining items as one narrow PR:
> 1. "Unrestricted 'every horizon' claims: Correct the Explainer, Appendix B, and FULL mirror to match the theorem actually established on main. Preserve the stronger statement only where its additional hypotheses are explicitly satisfied." The known sites are papers/Explainer.md:373 and book/appendix-b-derivations.md:454–455, plus the FULL mirror.
> 2. "Off-by-one at Main.md:167: Align the history-length convention with X_{<k} and X_k, checking the surrounding definitions and proof references."

## Changes, old → new

### 1. `papers/Explainer.md:373`

**Old:**

> the process is non-Markovian on accessible timescales ⟺ it arises, on each finite accessible
> horizon, from marginalizing a deterministic bijection under C1, C3, C4 (C2 …

**New:**

> the process is non-Markovian on accessible timescales ⟺ for some accessible order k it
> arises, on each finite accessible horizon K ≥ k+1, from marginalizing a deterministic
> bijection under C1, C3, C4, with the readback at k (C2 …

The same line also changes "The old three-way biconditional is retired: representability …"
to "No two of representability, memory and P-indivisibility are equivalent: representability …".
The old sentence was not part of the defect; it is changed because the §A.32/§A.33 added-lines
battery flags the revision-history phrase on any line the diff adds. The replacement is the
independent review's (`review/REVIEW.md`, finding 1): an unqualified "no three-way
biconditional holds" would be false beside the S⟺D⟺Q_fb biconditional the same paragraph
asserts. Every finite law is representable, while memory and P-indivisibility are not
universal, and memory does not force P-indivisibility, so no two of the three are equivalent.

### 2. `book/appendix-b-derivations.md:454`, mirrored at `FULL.md:6221`

**Old:**

> accessible non-Markovianity of the visible process is equivalent, on each finite accessible
> horizon, to embedded observation under C1, C3, C4 (C2 …

**New:**

> accessible non-Markovianity of the visible process is equivalent to embedded observation
> under C1, C3, C4 for some accessible order $k$ on each finite accessible horizon
> $K \geq k+1$, with the readback at $k$ (C2 …

### 3. `book/appendix-b-derivations.md:455`, mirrored at `FULL.md:6222`

**Old:**

```
$$\text{Accessible non-Markovianity on } V \iff \text{Embedded observation of } (S, \varphi) \text{ with C1, C3, C4, per finite accessible horizon}$$
```

**New:**

```
$$\begin{aligned} &\text{Accessible non-Markovianity on } V \\ \iff{}& \exists k\ \forall K \geq k+1:\ \text{embedded observation of } (S, \varphi) \text{ on horizon } K \\ &\text{with C1, C3, C4, readback at } k \end{aligned}$$
```

The display is set on three lines. The old single-line display ran past the right margin in
the PDF, and its last word was cut off.

### 4. `papers/Main.md:167`, the readback lemma

**Old:**

> two visible histories $p \neq p'$ of length $k$ with a common endpoint, each of probability
> at least $p_0$, induce next-step laws …

**New:**

> two visible histories $p \neq p'$ of length $k$, values of
> $X_{<k} = (X_0, \ldots, X_{k-1})$ followed by a common present state $X_k = c$, each with
> $\Pr[X_{<k} = p,\, X_k = c] \geq p_0$, induce next-step laws …

### 5. `papers/Main.md:170`, the proof of the lemma

**Old:**

> Condition on the common endpoint $c$ and let $w_a$ be the conditional weights of the
> length-$k$ histories,

**New:**

> Condition on the common present state $c$ and let $w_a = \Pr[X_{<k} = a \mid X_k = c]$ be
> the conditional weights of the length-$k$ histories,

## What does not change

- The characterization theorem, (ii), (iii) and its proof (`Main.md:516–522`, `:608`, `:610`).
- The lemma's bound, $I(X_{<k}; X_{k+1} \mid X_k) \geq p_0\delta^2/\ln 2$.
- Every other site found by the search (`SEARCH.md`), including the "⟺ C1/C3/C4 per accessible
  horizon" slogans, which are correct as stated.
- `verification/lean*` is untouched. The Lean convention in `OIBridge/HiddenMemory.lean` is
  `histProb p x = P(X_<t = p, X_t = x)`, which already matches item 2.

## Derived artifacts

Rebuilt with `sh ./build.sh Main Explainer` and `sh ./build.sh --book`. No glyphs were dropped.

| Artifact | Pages before | Pages after |
|---|---|---|
| `papers/Main.pdf` | 90 | 90 |
| `papers/Explainer.pdf` | 69 | 69 |
| Book (FULL) | 555 | 555 |

The `.tex` and `.pdf` files are regenerated in the same commit.

## Checks

All of the following report OK, and the §A.32/§A.33 added-lines scan has zero hits:

- `tools/claims_check.py`, `voice_check.py`, `duplicate_check.py`, `staleness_check.py` and
  `lean_manuscript_census.py`;
- `papers/oi_lattice_code/mirror_check.py`, with 0 chapter lines absent from FULL;
- `papers/oi_lattice_code/architecture_check.py`, with 259 invariants and 0 violations.

#932's `acceptance.py` was re-run unchanged. Its output is byte-identical to its recorded
result.

## Correctness bands

Bands unchanged. These are consistency corrections, and they add no new evidence.

## Review fixes (independent review of `2b660c93`, `review/REVIEW.md`)

- **Explainer:373** — the wording above (finding 1).
- **Explainer:353** (finding 2) — "⟺ embedded observation under C1, C3, C4 (per finite accessible horizon)" →
  "⟺ embedded observation under C1, C3, C4 (for some accessible order $k$, on each finite accessible horizon
  $K \geq k+1$, with the readback at $k$)". It is a theorem statement twenty lines above :373, and its parenthetical
  admitted the every-horizon reading this change corrects. The citation-list slogans (Substratum:111 and :126,
  Explainer:1021, appendix-b:22 and :406, appendix-c:106, ch02:90) stay as classified in `SEARCH.md`.
- **Coverage ledger** — `verification/coverage/LEDGER.json`, entry `MAIN:L-accessible-backflow-from-readback`: the
  readback lemma's statement at Main:167 changed, so its fingerprint moves (`1bf64869e7938d80` → `afbdefe369fdd5a0`).
  Re-affirmed: the mapping to `c4_backflow_probes.py` ("readback lemma") holds under the corrected convention, the
  level stays P, and the delta stays "no Lean statement" (the lemma is not in the kernel).
