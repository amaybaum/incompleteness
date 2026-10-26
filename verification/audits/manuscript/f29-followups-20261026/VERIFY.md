# F29 follow-ups: verification before editing

Base: `main` at `c967d6a9`. Finding: Issue #931 and its comment of 2026-10-26; the correction of
clause (iii) is #932 (`0e11285d`), recorded in `../f29-witness-quantifier/`. Line numbers are
those at `c967d6a9`; the edits change no line count.

## The established theorem

`papers/Main.md:516–522`: (ii) $\iff$ (iii), where

- (ii) (`:520`): at some accessible order $k$, $I(X_{<k}; X_{k+1} \mid X_k) > 0$;
- (iii) (`:522`): *for some accessible order $k$ and every finite accessible horizon
  $K \geq k+1$*, $\mathcal{S}$ arises from marginalizing a deterministic bijection with (C1),
  (C3) and (C4) history readback at $k$.

The proof (`:608`) gives (iii) $\Rightarrow$ (ii) by the readback lemma (`:167–170`) and
(ii) $\Rightarrow$ (iii) by the finite-horizon process dilation (`:496–500`) at each $K$. The
Remark at `:610` states that the order is bound within (iii) and that the unrestricted
every-horizon form of (iii) is false. The Remark at `:614` states the existential reading: (ii)
holds iff some per-horizon (C1)–(C4) realization exists.

Notation: a horizon $K$ carries the law of $(X_0, \ldots, X_K)$. A gap at order $k$ compares
$P(X_{k+1} \mid X_{<k}, X_k)$ and so needs $K \geq k+1$.

## Item 1: unrestricted every-horizon statements

### Site 1: `papers/Explainer.md:373`

> the process is non-Markovian on accessible timescales ⟺ it arises, on each finite accessible
> horizon, from marginalizing a deterministic bijection under C1, C3, C4

**What it claims.** The left side is global. The right side quantifies over every finite
accessible horizon, with no order anchoring the (C4) readback. This is the unrestricted
every-horizon form that `Main.md:610` states is false.

**Why it fails.** The failure is in the forward direction, and it occurs for non-Markovian laws:

- A horizon $K = 1$ supports no order-$k$ gap with $k \geq 1$.
- More generally, a horizon ending before the first memory witness restricts $\mathcal{S}$ to a
  Markovian law. By the pushforward identity (`Main.md:584`), a (C4) gap in any faithful
  realization of that law would be a differing next-step conditional of the law itself, so no
  such realization exists.
- Example: the law $L$ of the probe, and N2 of #932's `acceptance.py`. Each has a witness at
  order 2 only. At $K = 2$ the restriction is memory-free, so the right side fails while the
  left side holds.

**Hypotheses that would keep the stronger form.** The site restricts to non-Markovian
processes, but that does not make the unrestricted form true, as the example shows. The only
exact strong form is the per-witness statement of `Main.md:610`: $M_t > 0$ $\iff$ for every
$K \geq t+1$ there is a faithful realization with readback at $t$. That statement is anchored
at a witness $t$, which this site does not name. **Verdict: outdated; correct to the
witness-anchored form.**

### Site 2: `book/appendix-b-derivations.md:454–455`, mirrored at `book/The-Incompleteness-of-Observation-FULL.md:6221–6222`

> accessible non-Markovianity of the visible process is equivalent, on each finite accessible
> horizon, to embedded observation under C1, C3, C4 …
> $$\text{Accessible non-Markovianity on } V \iff \text{Embedded observation of } (S,\varphi)
> \text{ with C1, C3, C4, per finite accessible horizon}$$

**What it claims.** The theorem is stated "in the form of [Main §3.4]", with a global left
side and "on each finite accessible horizon" quantifying the right side. Read literally, this
is the same unrestricted every-horizon form as Site 1, and it fails for the same reason.

There is one charitable reading under which it is true: the horizon-local biconditional, "for
each $K$, the $K$-law has memory iff the $K$-law has a C1/C3/C4 realization". That reading is
not the theorem Main proves. Since the site presents itself as Main's theorem, it is corrected
to Main's (iii). **Verdict: outdated; correct to the witness-anchored form.** The two lines
were byte-identical between the chapter and FULL before the edit, and they are again after it.

### Checks on each corrected statement

The corrected text is the same at all three places:

> for some accessible order $k$, on each finite accessible horizon $K \geq k+1$, (realization)
> under C1, C3, C4, with the readback at $k$

This is (iii) of `Main.md:522`.

- **(a) (iii) ⇒ (ii).** Take $K = k+1$.
  - (C4) at $k$ in a faithful realization of the $(k+1)$-law gives two pasts $p \neq p'$ of
    $X_{<k}$ with a common present $X_k = c$ and different next-step laws. These are laws of
    the realization (`Main.md:80`, (C4)).
  - By the pushforward identity (`Main.md:584`, kernel `pushforward_identity`), they are
    $\mathcal{S}$'s own conditionals $P(X_{k+1} \mid p, c)$ and $P(X_{k+1} \mid p', c)$.
  - The readback lemma (`Main.md:167–170`) then gives
    $I(X_{<k}; X_{k+1} \mid X_k) \geq p_0\delta^2/\ln 2 > 0$, with $p_0$ the smaller of the two
    path probabilities. That is (ii) at $k$ (`Main.md:608`, first sentence).
  - The probe checks the bound exactly on one law (`L.full.readback_bound`), and #932's
    acceptance test checks it at four gaps.
  - **Holds.**
- **(b) (ii) ⇒ (iii).** Let $k$ be an order at which (ii) holds. For each $K \geq k+1$:
  - The process dilation (`Main.md:496–500`) reproduces the full $K$-law, whose restriction
    contains the order-$k$ witness.
  - The realization inherits (C4) at $k$, because the ledger-conditioned kernels reproduce the
    differing past-conditionals (`:500`, `:608`). It satisfies (C1) by `:608` and (C3) with
    $\log_2|\mathcal{C}_H| \geq I^*$ (`:500`).
  - The order $k$ is fixed before $K$ is chosen, which matches the $\exists k\,\forall K$ order
    of the quantifiers.
  - #932's `acceptance.py` re-runs this unchanged (below).
  - **Holds.**
- **(c) Non-vacuity.**
  - For a Markov law, (ii) is false. The corrected right side is also false: any $k$
    satisfying it would be a memory witness, by (a). So the biconditional holds and does not
    hold vacuously. This is case M of `acceptance.py`: "(ii) = False; corrected (iii) = False".
  - The corrected right side is not satisfiable by horizons before the witness, because it
    only quantifies over $K \geq k+1$.
  - The unrestricted form, by contrast, fails for the non-Markovian law $L$ at $K = 2$
    (`L.K2.order1.*` in the probe) and for N2 at $K = 2$ ("K=2: … C4: k=1: none").
  - **Holds.**

## Item 2: history length in the readback lemma, `papers/Main.md:167`

### The text

> two visible histories $p \neq p'$ of length $k$ with a common endpoint, each of probability at
> least $p_0$, induce next-step laws at total-variation distance at least $\delta$. Then
> $I(X_{<k}; X_{k+1} \mid X_k) \geq p_0\delta^2/\ln 2$.

### Indexing in Main

- Trajectories are $(x_0, \ldots, x_K)$ (`:99`, `:496`).
- $X_{<k} = (X_0, \ldots, X_{k-1})$ has $k$ entries, and $X_k$ is the present (`:168`,
  `:520`).
- "Length" counts entries, as in the dilation ledger $(x_0 \ldots x_{c-1})$ at clock $c$
  (`:500`) and the "length-$(K{-}t)$ visible future" (`:600`).

### The defect

A history $p$ of length $k$ "with a common endpoint" reads naturally as a $k$-entry sequence
that ends at the conditioned state. With the endpoint $X_k$, that is $(X_1, \ldots, X_k)$, which
drops $X_0$. Its $k-1$ past entries do not match $X_{<k}$.

The proof (`:170`) shows what the lemma means:

- $w_a$ ranges over values $a$ of $X_{<k}$ given $X_k = c$ ("the conditional mutual information
  given $X_k = c$ is the mixture divergence $\sum_a w_a D(P_a\|\bar P)$");
- "multiplying by $\Pr[X_k = c]$ converts conditional weights to path probabilities", so
  $p_0$ bounds $\Pr[X_{<k} = p, X_k = c]$.

The hypothesis's "length $k$ with a common endpoint" therefore names the wrong object, by one
position.

### Decision

The history is a value of $X_{<k} = (X_0 \ldots X_{k-1})$, of length $k$, followed by the common
present $X_k = c$. The probability bound is on $\Pr[X_{<k} = p, X_k = c]$.

The other consistent fix, histories $x_0 \ldots x_k$ of length $k+1$, was not chosen, for two
reasons:

- the chosen form keeps "length $k$" and the proof's "length-$k$ histories" verbatim;
- it matches the kernel's convention.

### Why it matters

The readback lemma is invoked as (iii) ⇒ (ii) (`:608`, `:717`), where (iii)'s (C4) at $k$ is a
gap between differing past-conditionals over the full past $X_{<k}$ (`:80`, `:500`). Under the
suffix reading, the lemma's hypothesis would not cover such a gap.

The probe's law $L$ shows this ($X_3 = X_0 \oplus X_2$, $k = 2$):

- over pasts $X_{<2}$: $\delta = 1$, $p_0 = 1/8$, CMI = 1 bit;
- over the length-2 window $(X_1, X_2)$: $\delta = 0$.

(The lemma's conclusion stays true under either reading, since a gap on a coarser past still
forces positive CMI on the finer one. The defect is in how the hypothesis matches (C4) at $k$,
not in the bound.)

### Consistency of every invocation after the fix

- **Readback lemma at $K = k+1$** (#932's result.md, `Main.md:610`). The pasts $X_{<k}$, the
  present $X_k$ and the next step $X_{k+1}$ all lie in $(X_0, \ldots, X_{k+1})$. Consistent.
- **Proof, `Main.md:608`, and status table, `:717`.** Both use the lemma's conclusion
  $I(X_{<k}; X_{k+1} \mid X_k)$, which is unchanged. Consistent.
- **Remark, `Main.md:163`.** "LOWER bound on $I(X_{<k}; X_{k+1} \mid X_k)$". Unchanged.
  Consistent.
- **Universal theorem, `Main.md:582–590`.** It writes $\mu_p = P(H_t \mid X_{<t} = p, X_t = x)$
  for "a visible history $p$ ending in $x$", so $p$ is a value of $X_{<t}$, followed by $x$.
  This is the same convention as the fix.
- **Remark, `Main.md:610`.** Its per-witness statement ($M_t > 0$, $K \geq t+1$) uses
  $M_t = I(X_{<t}; X_{t+1} \mid X_t)$ (`:99`). Consistent.
- **Other occurrences.** The lemma's hypothesis has no paraphrase elsewhere. GR:20 cites "the
  readback lemma of [Main §2.3]" by name only. The corpus has no other "histories of length",
  "history of length" or "common endpoint" (see SEARCH.md).
- **Probe.** `c4_backflow_probes.py` (`papers/oi_lattice_code/foundations/`) indexes the same
  way: the past `a` is `(x0,)` at $k = 1$, $c = X_k$, and `p0 = min` of the joint weights
  $P(a, c)$.
- **Other notions of order.**
  - "Step order $k$" in the quantitative-mixing theorem (`:435–437`) is a separate notion
    ($T^{(k)}$ against $T^k$), with its own indexing. It is not touched.
  - The fast-bath lemma (`:159`) bounds an order-$k$ readback gap $\delta_k$ by the number of
    erosion steps, $k-1$. It states no history length and does not invoke the hypothesis of
    `:167`. Whether its exponent counts the same steps under the corrected convention was not
    re-derived here, and it is not touched.

### Lean (read only)

The readback lemma (the Pinsker bound) is not in the kernel. No `.lean` file mentions Pinsker or
the lemma, and `Main.md:608` says that neither direction is formalized.

The nearest kernel object is `OIBridge/HiddenMemory.lean`:

- `Hist` is the type of $X_{<t}$, and `histProb p x` is "`P(X_<t = p, X_t = x)`, the weight of a
  history with its endpoint";
- `nextLaw p x` is $P(X_{t+1} \mid X_{<t} = p, X_t = x)$.

This is the corrected convention: the history is the past $X_{<t}$, paired with the present
$X_t$, and the path probability is the joint weight. **No mismatch.** `verification/lean*` is
untouched.

## Countercontrol

- `python3 -I verification/audits/manuscript/f29-witness-quantifier/acceptance.py` was re-run,
  unchanged, at `c967d6a9`. It exits 0 with verdict ACCEPT.
- Its output is byte-identical to the block recorded in that directory's `result.md`:
  `sha256 c04f737a429605f88b63771799e3ef83462cc9763998fcfef7fbc83fe65886b3`.
- It was re-run after the edits, with the same result.

## Probe

`readback_indexing_probe.py` in this directory. It uses exact rationals, with the CMI as a float
used only for strict signs and the bound, and it checks 12/12.

- **Must fire:** the order-2 gap over $X_{<2}$ for $L$.
- **Must be silent:** the $(X_1, X_2)$ window for $L$, and the $K = 2$ restriction of $L$
  under both indexings.
- **Controls:**
  - $X_3 = X_1 \oplus X_2$: both indexings fire;
  - Markov $X_3 = X_2$: neither fires, and the CMI is 0.

**Scope.** Binary alphabet, one law and two controls, $K \leq 3$. It is a check on indexing,
not a proof of the lemma.

## Verdict

Both items hold as analysed.

- **Item 1.** Correct Explainer:373 and appendix-b:454–455 / FULL:6221–6222 to the
  witness-anchored form. No site satisfies extra hypotheses that would keep the unrestricted
  form.
- **Item 2.** Correct `Main.md:167` and the matching words of its proof at `:170`. Nothing else
  changes.
