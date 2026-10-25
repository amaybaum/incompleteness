# OI-PE-1: pseudoentropy, deterministic randomness and observer access

Research thread, opened 25 October 2026 from `main` at
`c37700ad7d1bf099c59010e941ca06ffc4c12e3d` (the drafting snapshot). Exploratory research only.

This thread is not a native V3 round. It introduces no postulate and adopts no premise.

## Question

Under a finite reversible substratum, the visible record is a deterministic function of the initial state. The thread
asks four things:
- whether such a record can be indistinguishable from a genuinely random source to a restricted observer;
- for which observers, at which horizons, and at what resource cost;
- how this relates to computational pseudoentropy;
- whether a persistent hidden seed can stand in for independently supplied randomness across repeated measurements.

## Anchors in the corpus

These are the statements the thread tests or depends on. The thread changes none of them.

- **The book's claim of unpredictability.** `book/ch18-beyond.md:104–114` and its mirror at `FULL.md:4922–4932`:
  - outcome randomness is the observer's reduced description of a deterministic bijection;
  - "the randomness is unpredictable by any embedded observer regardless of its origin, so the cryptographic properties
    depend on unpredictability rather than on ontic vs epistemic status".
  - PE-01 to PE-03 test the second sentence against explicit observer classes.
- **The fair-coin realization.** `papers/Main.md:172`: the fair coin is realized by the §3.4 dilation construction, on a
  finite horizon, from a hidden tape.
- **The capacity condition.** `papers/Main.md:78`, (C3): $\log_2|\mathcal{C}_H| \ge I^*$. It is a data-processing bound
  and is saturated.
- **The finite-horizon scope.** `papers/Main.md:82`: every theorem quoted there holds on a fixed finite accessible
  horizon.
- **Bounded persistent memory.** The research under #911 (`a2_memory_v8/`, not on `main`) proves the following, on one
  protocol, for controllers with finite whole state, a time-independent update and B fresh fair bits per slot: complete-
  record total variation from quantum theory tends to 1. PE-03 coordinates with it and adopts none of its controller
  constructions as OI mechanisms.

## Three notions, kept distinct

Let a finite bijection $\varphi$ act on $\mathcal{C}_V \times \mathcal{C}_H$, and let $\mu$ be an initial law on it.
The visible record is $X_{0:K}$.

1. **Shannon entropy.** The record is a function of the initial state, so
   $H(X_{0:K}) \le H(\mu) \le \log_2|\mathcal{C}_V \times \mathcal{C}_H|$ for every $K$. PE-01 states and checks this
   bound and its consequences. It is elementary and is not claimed as new.
2. **Computational pseudoentropy.** These are the established definitions, used as stated in their sources:
   - HILL (Håstad–Impagliazzo–Levin–Luby): indistinguishability, at size $s$ and advantage $\varepsilon$, from some
     distribution of min-entropy at least $k$;
   - the metric and Yao variants (Barak–Shaltiel–Wigderson).

   Asymptotic statements need families indexed by a security parameter. A finite instance supports only concrete
   $(s, \varepsilon)$ statements, and the thread makes no others.
3. **OI observational indistinguishability.** For a stated class $\mathcal{P}$ of permitted protocols on the visible
   sector, the advantage is $\max_{p \in \mathcal{P}} \mathrm{TV}$ between the record laws. The access restriction is
   informational: $h$ is not read. A computational bound is a separate, additional hypothesis.

The thread never identifies any two of these without an explicit formal map (AGENTS.md, Code Review Rules: bridge and
no-go scope).

## Stages

**PE-01: a minimal deterministic model.**
- Build a finite reversible generator. Each of the following is given explicitly: the hidden seed, the visible output
  map, the initial law, and the observer classes.
- Exact results, in rational arithmetic or by exhaustive enumeration: the record entropy, and the distinguishing
  advantage for each observer class at each horizon.
- Controls:
  - a positive control, an observer class whose advantage is provably 0 at the stated horizons;
  - a negative control, an observer class that distinguishes, with its advantage computed exactly;
  - an exactness control, which checks that the generator is a bijection and that the enumerated laws sum to 1.

**PE-02: computational versus physical observers.**
- State when indistinguishability against a size-$s$ circuit class implies indistinguishability against a protocol
  class $\mathcal{P}$, and the converse. Each direction is a separate question with its own status (§A.34).
- Each claim names its witnesses in both directions.
- Cryptographic results are cited, never rederived as OI results.

**PE-03: persistent hidden memory.** Prospective; it begins only after PE-01 and PE-02 are reviewed.
- Compare a fixed hidden seed with independently supplied randomness across repeated measurements.
- Compare complete joint-record laws over increasing depth, together with the resources each side uses.

**PE-04: implications for quantum reconstruction.** Prospective, as PE-03.
- Test whether a mechanism that survives PE-03 meets the complete-record, adaptive-measurement and outgoing-carrier
  requirements of #910 to #912.
- Keep finite-precision approximation separate from exact quantum equivalence.

## Decision rules (stated before any computation)

- **Advantages are exact.** They are computed exactly where an exact computation is available. Floating point never
  certifies a zero, an equality or a separation.
- **Verdict text is generated from the measured values.** A verdict printed over a failed or vacuous control is void.
- **Classification of each result:** PROVED, CONDITIONAL (its hypothesis named), COUNTEREXAMPLE (an explicit finite
  instance), or OPEN.
- **Productivity test (§A.31).** A result counts only if it is strictly stronger than the restatement "a deterministic
  record has bounded entropy", and it either constrains a corpus claim or exposes a hidden assumption.
- **Favorable branches get the most scrutiny.** When a branch favors the framework, it is pressure-tested hardest.
- **Each stage's results are its own package**, under this directory, with a plan pinned before execution, structured
  outputs and an independent review.

## Literature to read in full before any closure claim

None of these is relied on yet.
- J. Håstad, R. Impagliazzo, L. Levin, M. Luby, "A pseudorandom generator from any one-way function", SIAM J. Comput.
  28 (1999).
- B. Barak, R. Shaltiel, A. Wigderson, "Computational analogues of entropy", RANDOM-APPROX 2003.
- S. Vadhan, C. J. Zheng, "Characterizing pseudoentropy and simplifying pseudorandom generator constructions", STOC 2012.
- J. L. Massey, "Shift-register synthesis and BCH decoding", IEEE Trans. Inf. Theory 15 (1969). This is the
  linear-complexity distinguisher for linear generators.
- Z. Ji, Y.-K. Liu, F. Song, "Pseudorandom quantum states", CRYPTO 2018.
- S. Aaronson et al., "Quantum pseudoentanglement", arXiv:2211.00747.
- A. Bouland, B. Fefferman, U. Vazirani, "Computational pseudorandomness, the wormhole growth paradox, and constraints
  on the AdS/CFT duality", arXiv:1910.14646. It is relevant to the black-hole audit under #917.

## Authority limits

This thread does not claim any of the following:
- that OI guarantees cryptographic security;
- that deterministic dynamics creates Shannon entropy;
- that pseudoentropy reproduces quantum mechanics or solves the native measurement problem.

The thread involves no manuscript change, special workflow dispatch, theorem designation or merge without separate
owner approval.

## First milestone

PE-01 and PE-02. The goal is an independently reviewed finite example that separates actual entropy from
observer-relative unpredictability, together with an explicit counterexample showing where the analogy fails.
