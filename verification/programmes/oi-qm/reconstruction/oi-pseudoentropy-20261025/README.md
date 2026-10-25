# OI-PE-1: pseudoentropy, deterministic randomness and observer access

Research thread, opened 25 October 2026 from `main` at
`c37700ad7d1bf099c59010e941ca06ffc4c12e3d` (the drafting snapshot). Exploratory research only.

This thread is not a native V3 round. It introduces no postulate and adopts no premise. Corpus line numbers below are at
the drafting snapshot.

## Question

The visible record of a finite reversible substratum is a deterministic function of the initial state. Within a fixed
horizon, the corpus already settles exact reproduction. This thread asks what happens for **one fixed realization**
$(\mathcal{C}_V \times \mathcal{C}_H, \varphi, \mu)$ as the horizon or the protocol class grows:
- For which observers is the record indistinguishable from a genuinely random reference source?
- How far, and at what resource cost?
- Does that indistinguishability survive repeated and adaptive measurement?
- How does it relate to computational pseudoentropy?

The corpus claim under audit is `book/ch18-beyond.md:114` (mirrored at `FULL.md:4932`): "The randomness is unpredictable
by any embedded observer regardless of its origin, so the cryptographic properties depend on unpredictability rather
than on ontic vs epistemic status." The thread treats this sentence as a claim to test, not as a premise.
- Tests against finite, explicit observer classes can refute its universal form. They cannot establish it.
- A positive result is stated only for the observer class it was computed for.

## What the corpus already settles

These are the baseline. The thread restates none of them as new.

- **Record entropy is bounded.** `papers/Structure.md:1256` gives the sharp form:
  - the visible factor of a finite reversible substratum has zero entropy rate under every invariant prior;
  - the randomness an embedded observer records is bounded by $\log|\mathcal{C}_V \times \mathcal{C}_H|$;
  - that randomness is exhausted at recurrence scale.
- **Exact reproduction within a horizon.** `papers/Main.md:496–500` (finite-horizon process dilation, with the
  response-table extension for arbitrary priors) reproduces any finite-horizon law exactly, so its total variation is 0
  against every observer. The hidden tape $\mathbb{Z}_D^K$ grows with the horizon $K$. `papers/Main.md:172` uses this
  construction for the fair coin, at "arbitrarily long accessible horizons", one realization per horizon.
- **The per-horizon qualifier is load-bearing.**
  - `papers/Main.md:476` and `:538`: the equivalence chooses the realization per finite-horizon law.
  - `papers/Main.md:536–538`: no fixed finite realization hosts generic combs as the horizon grows, and no fixed
    $N$-state model reproduces the qubit exactly.
  - `papers/Main.md:82`:
    - layer (1) holds per horizon;
    - layer (3) includes approximation to arbitrary finite accuracy;
    - layer (4) is conditional, not a theorem.
- **Pre-loaded seeds and approximation.**
  - `papers/Main.md:544–560`: finite realization and gluing, in ε-form. It uses uniform pre-loaded seeds and a
    read-only program register charged as a resource.
  - `papers/Main.md:576`: uniform continuum realization to mutual ε-density at fixed $d$, $m$, $K$ and $\varepsilon$.
- **Capacity.** `papers/Main.md:78` and `:492`, (C3): $\log_2|\mathcal{C}_H| \ge I^*$, where
  $I^* = \sup_t I(X_{<t}; X_{>t} \mid X_t)$ is a conditional mutual information, not a record entropy. The bound is tight:
  some realizations attain it.

## Related corpus statements the thread bears on

- **Predicted correlations.** `book/ch18-beyond.md:56–58` predicts correlations between successive outcomes at order
  $\tau_S/\tau_B \approx 10^{-32}$. This is the "10^{-32} level" the claim under audit cites.
- **Bell.** `book/ch18-beyond.md:110`: the framework keeps measurement independence and takes ontic parameter
  dependence. That matters for certified randomness, which relies on no-signalling against the adversary.
- **Colbeck–Renner.** `book/appendix-c-objections.md:58–62`: the framework's response to Colbeck–Renner.
- **The observer's computational model.** `papers/Computation.md:15–17`: the conditional BQP observer model, and the
  framework's silence on asymptotic complexity.
- **The choice of μ.** `papers/Main.md:708`: the posit ledger, including the maximal-entropy measure posit.
- **#911's bounded-memory result.** Reported, unlanded, internally reviewed:
  `verification/programmes/oi-qm/reconstruction/states-dynamics-audit-20261024/a2_memory_v8/REPORT.md` at
  `bafb38d672cbc63f9bf9ef26225ad995fa02c5c9`. It concerns finite-precision approximation of quantum theory, not OI
  (its line 7). Its claims:
  - On one protocol, a controller with finite whole state, a time-independent update and B fresh fair bits per slot has
    complete-record total variation from quantum theory tending to 1.
  - The obstruction is arithmetic: dyadic fresh bits against a run law with ratio 4/5.
  - Escaping it needs unboundedly many persistent states. A retained-seed reset escapes; bounded private memory with
    unbounded public state is open.
  - Its fresh bits are an instance of the independently supplied randomness PE-03 compares with a fixed seed. PE-03
    adopts none of its controllers as an OI mechanism.

## Three notions, kept distinct

Let a finite bijection $\varphi$ act on $\mathcal{C}_V \times \mathcal{C}_H$, with an initial law $\mu$. The record
$R_K$ is the visible trajectory $X_{0:K}$, plus the settings when a protocol supplies them.

**1. Information-theoretic.**
- For a passive record, $R_K$ is a function of the initial state. So
  $H_\infty(R_K) \le H(R_K) \le H(\mu) \le \log_2|\mathrm{supp}\,\mu|$.
- With external settings the bound holds conditional on them.
- With a prepared visible $x_0$, the relevant support is $\mathcal{C}_H$.
- Against a reference law uniform on an alphabet $A$, the unrestricted distinguisher has
  $\mathrm{TV} \ge 1 - |\mathrm{supp}\,\mu|/|A|^K$.
- This rules out exact fair randomness beyond $H(\mu)$ bits. It does **not** make the output predictable to a bounded
  observer: a secure pseudorandom generator, under its assumptions, stretches a short seed into a much longer output that
  bounded tests cannot tell from random. Keeping these two facts apart is the core of PE-01 and PE-02.

**2. Computational (pseudorandomness and pseudoentropy).** Each notion is used as its source states it, with the entropy
measure, the quantifier order and the distinguisher class named:
- **HILL** (Håstad–Impagliazzo–Levin–Luby 1999).
  - Shannon entropy: there exists $Y$ with $H(Y) \ge k$ such that, for every distinguisher of size $s$, the advantage is
    at most $\varepsilon$.
  - The min-entropy form is due to Barak–Shaltiel–Wigderson.
- **Metric** (Barak–Shaltiel–Wigderson 2003). The quantifiers are reversed: for every distinguisher there exists some
  $Y$ of high min-entropy. Its relation to HILL against bounded circuits is treated by Barak–Shaltiel–Wigderson and by
  Reingold–Trevisan–Tulsiani–Vadhan 2008.
- **Yao** (Yao 1982). Defined by incompressibility.
- **Pseudorandomness** is the special case of indistinguishability from the uniform law itself.

Each use states whether distinguishers are Boolean or [0,1]-valued, classical or quantum (Chen–Chung–Lai–Vadhan–Wu), and
how many samples they receive. A finite instance supports only concrete $(s, \varepsilon)$ statements, and the thread
makes no asymptotic claim from one.

**3. OI observational indistinguishability.** For a stated protocol class $\mathcal{P}$ and a named reference law $Q$,
the advantage is
$\mathrm{adv}_{\mathcal{P}}(\mu, Q) = \max_{p \in \mathcal{P}} \mathrm{TV}(P^{\varphi,\mu}_p, Q_p)$.
- $P^{\varphi,\mu}_p$ is the record law of protocol $p$ under the realization.
- $Q_p$ is the record law under the reference: independent fair outcomes, or the quantum prediction for $p$.

Every use states:
- whether $Q$ is a fixed law (a pseudorandomness-type notion) or ranges over a high-entropy class (a pseudoentropy-type
  notion, compared with item 2);
- one run or $r$ independent runs;
- whether settings are part of the record, and that settings are chosen measurement-independently of the hidden state;
- **whether the observer knows $\varphi$ and $\mu$.**

The access restriction is informational: $h$ is never read. A computational bound is a separate, additional hypothesis.

Knowing the law is not knowing the seed. Every use names the observer's knowledge as one of three levels:
- **(K0)** It knows neither $\varphi$ nor $\mu$.
- **(K1)** It knows $\varphi$ and $\mu$, but not the initial state. It conditions $\mu$ on the record it has seen. What it
  can predict at horizon $K$ is fixed by that posterior, and the thread computes it; it is not assumed.
  - Every visible trajectory of a finite bijection is periodic. Its period divides the length of the initial state's
    orbit, so it is at most $L$, the maximal orbit length, and $L \le |\mathcal{C}_V \times \mathcal{C}_H|$.
  - By Fine–Wilf, two such trajectories that agree on $2L$ consecutive symbols agree everywhere.
  - A computationally unbounded K1 observer therefore predicts perfectly from that length on. Shorter records may leave
    it uncertain.
- **(K2)** It knows the initial state. That amounts to reading $h$, which is outside the observer classes this thread
  considers.

What the claim under audit assumes about observer knowledge and record length is the thread's first assumption-watch
item.

The thread never identifies any two of the three notions without an explicit formal map (AGENTS.md, Code Review Rules:
bridge and no-go scope).

## Stages

**PE-01: one fixed generator, three observer classes.**
- Build a finite reversible generator. Each of the following is given explicitly: the hidden seed, the visible output
  map, $\mu$, the horizon range and the reference law.
- Compute, exactly, the record entropies and the advantage of each of the following against the same generator:
  - an unrestricted observer, with no computational bound, at knowledge level K0 and at K1;
  - a computationally bounded observer, with its class stated: circuit size, or a named structured class such as linear
    tests via Berlekamp–Massey;
  - a physically restricted OI observer, given by a stated protocol class $\mathcal{P}$ on the visible sector.
- Controls:
  - **Positive control.** A non-trivial observer class, one that contains a test which fires on some other stated
    generator, whose advantage on this generator is provably 0. A constant test does not count.
  - **Negative control.** An observer class that distinguishes for its stated reason, for example support size or linear
    complexity, with the advantage computed exactly. A mutant that removes that reason must remove the advantage.
  - **Exactness control.** The generator is a bijection, and the enumerated laws sum to 1.
- The stage's own plan carries the §A.41 invariant→checkpoint table.

**PE-02: computational versus physical observers.**
- State when indistinguishability against a stated distinguisher class implies indistinguishability against a protocol
  class $\mathcal{P}$, and the converse. Each direction is a separate question with its own status (§A.34).
- Each claim names its witnesses in both directions.
- Cryptographic results are cited, never rederived as OI results.

**PE-03: persistent hidden memory.** Prospective; it begins only after PE-01 and PE-02 are reviewed.
- Compare one fixed hidden seed with independently supplied randomness, across repeated and adaptive measurements.
- Compare complete joint-record laws over increasing depth, together with the resources each side uses: seed length, the
  program register, workspace.

**PE-04: implications for quantum reconstruction.** Prospective, as PE-03.
- Test whether a mechanism that survives PE-03 meets the requirements below. The stage plan cites each requirement by PR
  and path before it is used:
  - complete-record composition (#912);
  - adaptive measurement and the outgoing carrier (#911 and #912);
  - native construction (#910).
- Keep finite-precision approximation (`Main.md:576`) separate from exact quantum equivalence.

## Decision rules (stated before any computation)

- **Advantages are exact.** They are computed exactly where an exact computation is available. Floating point never
  certifies a zero, an equality or a separation.
- **Verdict text is generated from the measured values.** A verdict printed over a failed or vacuous control is void.
- **Classification of each result:** PROVED, CONDITIONAL (its hypothesis named), COUNTEREXAMPLE (an explicit finite
  instance), or OPEN.
- **Productivity test (§A.31).** A result counts only if it is strictly stronger than what the corpus already settles,
  that is, the zero-entropy-rate bound of `Structure.md:1256` and the dilation and gluing theorems of `Main.md` §3.4. It
  must also either constrain a corpus claim or expose a hidden assumption. A result that only re-derives those is
  record-only.
- **Favorable branches get the most scrutiny.** When a branch favors the framework, it is pressure-tested hardest.
- **Each stage's results are its own package**, under this directory, with a plan pinned before execution, structured
  outputs and an independent review.

## Literature to read in full before any closure claim

None of these is relied on yet.

Pseudorandomness and pseudoentropy:
- J. Håstad, R. Impagliazzo, L. Levin, M. Luby, "A pseudorandom generator from any one-way function", SIAM J. Comput.
  28(4):1364–1396 (1999).
- A. C. Yao, "Theory and applications of trapdoor functions", FOCS 1982.
- B. Barak, R. Shaltiel, A. Wigderson, "Computational analogues of entropy", RANDOM-APPROX 2003, pp. 200–215.
- O. Reingold, L. Trevisan, M. Tulsiani, S. Vadhan, "Dense subsets of pseudorandom sets", FOCS 2008.
- S. Vadhan, C. J. Zheng, "Characterizing pseudoentropy and simplifying pseudorandom generator constructions", STOC 2012,
  pp. 817–836.
- J. L. Massey, "Shift-register synthesis and BCH decoding", IEEE Trans. Inf. Theory IT-15(1):122–127 (1969). This is the
  linear-complexity distinguisher.

Quantum distinguishers and quantum pseudorandomness:
- Y.-H. Chen, K.-M. Chung, C.-Y. Lai, S. Vadhan, X. Wu, "Computational notions of quantum min-entropy",
  arXiv:1704.07309.
- Z. Ji, Y.-K. Liu, F. Song, "Pseudorandom quantum states", CRYPTO 2018, arXiv:1711.00385.
- S. Aaronson et al., "Quantum pseudoentanglement", arXiv:2211.00747.

Certified randomness:
- R. Colbeck, R. Renner, "No extension of quantum theory can have improved predictive power", Nat. Commun. 2, 411 (2011),
  arXiv:1005.5173.
- S. Pironio et al., "Random numbers certified by Bell's theorem", Nature 464, 1021 (2010), arXiv:0911.3427.

Black holes:
- A. Bouland, B. Fefferman, U. Vazirani, "Computational pseudorandomness, the wormhole growth paradox, and constraints on
  the AdS/CFT duality", arXiv:1910.14646. It is relevant to the black-hole audit under #917.

## Authority limits

This thread does not claim any of the following:
- that OI guarantees cryptographic security;
- that deterministic dynamics creates Shannon entropy;
- that pseudoentropy reproduces quantum mechanics or solves the native measurement problem.

The thread involves no manuscript change, special workflow dispatch, theorem designation or merge without separate
owner approval. A finding about `ch18:114` is reported here; any correction to the book is a separate, owner-approved
change.

## First milestone

PE-01 and PE-02, for one fixed generator. The question: for which of the three observer classes, at which knowledge
level, is the record indistinguishable from the named reference law, and at which horizons?

The outcome rule: each class's advantage is reported as computed, with its controls, and classified by the rules
above. The milestone closes with exactly one of three outcomes, all equally admissible:
- a new bounded theorem;
- a counterexample to the universal form of `ch18:114`;
- a documented finding that the distinction is already covered by the existing OI mathematics (`Structure.md:1256`,
  `Main.md` §3.4), with the covering statement cited.
