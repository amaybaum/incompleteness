# Track D preregistration: status of (C2-structural); stronger C2 forms vs accessible-window P-indivisibility

Frozen before any computation. Base: `6bc2c4af10863c2cdfd9f5c1b88abdc8b64f9ed0` (detached worktree `trackD/wt`).
All Python runs as `python3 -I -B`; all arithmetic is `fractions.Fraction` / integer. No floating point
enters any verdict.

## 1. Objects

- **Bijective realization (class B).** Finite sets V (|V| = n_V), H (|H| = n_H), a bijection
  phi of V x H, an initial law nu on V x H. Default nu = uniform on V x H (counting measure,
  Lemma 3); then root X_0 and H_0 are independent and H_0 ~ mu_H = uniform. State Z_t = phi^t(Z_0),
  X_t = pi_V(Z_t), H_t = pi_H(Z_t).
- **Non-injective / staged completion (class N).** A deterministic, possibly non-injective and
  stage-dependent, map Z_{t+1} = F_t(Z_t). The canonical predictive quotient T(P) of Main §3.4 is the
  instance used: hidden state at stage t = the visible future tail.
- **Coarse-grained stochastic description (class S).** A hidden-state Markov model: Z_t = (X_t, G_t)
  Markov with a fixed stochastic kernel, G a coarse hidden variable; the visible law is computed from
  the model, not fitted.
- **Rooted family.** Gamma_t(a, j) = mu_H{h : pi_V phi^t(a, h) = j} for every root a (Main §2.3).
  In class S: Gamma_t(a, j) = P(X_t = j | X_0 = a) with G_0 drawn from a fixed law independent of X_0.
- **P-divisible on {0..n}.** For every 0 <= s < t <= n there is a row-stochastic Lambda with
  Gamma_t = Gamma_s Lambda (Main §2.3 definition).
- **Gap at order k** (C4 witness, Main §1.3). Under the default prior, two distinct positive-probability
  histories (x_0..x_k), (x'_0..x'_k) with x_k = x'_k and different next-step laws P(X_{k+1} | ...).
  Equivalent (exact) to M_k > 0; decided here by exact comparison of conditional laws.
- **Accessible window.** {0..n} with n <= L - 1, L the order of phi (recurrence: Gamma_L = I).
  In class S: any finite n.

## 2. Forms of (C2) examined

- **C2s-b (as stated, §1.3/§3.4):** the retention required by clause (b): for every gap pair at order t,
  ||mu_p - mu_p'||_TV >= delta.
- **C2s-full:** the visible past is recoverable from the time-t state: H(X_<t | X_t, H_t) = 0.
- **C2s-supp:** posteriors of distinct positive-probability histories with a common endpoint have
  disjoint supports (TV = 1).
- **F2 (persistent readback):** a gap at every order t = 1..n-1 of the window {0..n}.
- **F2max:** F2 with delta = 1 at every order (maximal gap).
- **F3 (visible non-remixing):** for every order t in the window, some history-conditional next-step
  law differs from K-bar_{x_t} = sum_h mu_H(h) K(x_t, h; .) (the fresh-hidden kernel of the
  physical-memory theorem). Under the counting measure this is to be checked against F2.
- **Time-homogeneity (TH):** single fixed bijection / fixed kernel, stationary initial law.
- **(EM)-type:** class S with a hidden kernel that mixes (spectral gap of the hidden channel > 0) and
  C2-slow (mixing slow relative to the step).

## 3. Decision rules

R1 (Q1, class B). C2s-full and C2s-supp are declared **automatic in class B** iff a paper proof is
given AND the exhaustive check finds zero violations over every bijection at
(n_V, n_H) = (2,2), (2,3), (3,2), (2,4), every t = 1..L (horizon capped at L), with the countercontrol
green (a non-injective map must be detected as violating C2s-supp / C2s-full).

R2 (Q1, class N). C2s-full is **not automatic in class N** iff an exact instance (canonical predictive
quotient of an explicit law) has two positive-probability histories with a common endpoint and
identical hidden posteriors. C2s-b is **a consequence in every deterministic and every Markovian
hidden-state completion** iff a paper proof is given; exhaustive corroboration is not required.

R3 (Q3). For each form F in {C4 alone, F2, F2max, F3, TH, EM-type}: **refuted** as a route to
accessible-window P-indivisibility iff an exactly verified countermodel exists that satisfies F (and C1,
C4) on a window {0..n} with n >= k+1 for the gap order k (n >= 2 for F2), within the accessible range,
and whose rooted family is P-divisible on {0..n}: every divisor Lambda returned by the exact LP is
re-verified (nonnegative, rows sum to 1, Gamma_s Lambda = Gamma_t exactly). **Proved** iff a paper proof
covers the form. Otherwise **open**, naming the missing assumption. A verdict prints only if all controls
below are green.

R4. Report for each size: the number of bijections with a gap, the largest n_div - (k_min + 1), the
largest window n on which F2 holds together with P-divisibility, and one exact countermodel per
refuted form (smallest size found, lexicographically first).

## 4. Controls (all must be green)

C-LP+ : Markov family Gamma_t = T^t for a fixed non-permutation stochastic T: LP feasible for all pairs.
C-LP+x: the XOR law (X_1 uniform independent of X_0, X_2 = X_0 xor X_1): rooted family divisible on
        {0,1,2} with Lambda = I, gap at order 1 (Main §3.4 two-notions remark).
C-LP- : §2.4 minimal model: Gamma_1 = [[2/3,1/3],[1/3,2/3]], Gamma_2 = I: LP infeasible, with an exact
        Farkas certificate verified.
C-2x2 : for n_V = 2 an independent closed-form divisibility test (invertible Gamma_s: Gamma_s^{-1}Gamma_t
        stochastic; singular Gamma_s: Gamma_t must have identical rows) agrees with the LP on every
        pair tested in the search.
C-rec : recurrence theorem of Main §2.3: every bijection with a gap at some order has n_div < L
        (indivisible on {0..L}). Zero exceptions required.
C-gap : §2.4 minimal model shows a gap at order 1 (1 vs 1/3); a decoupled bijection (T a permutation
        for every root, phi(x,h) = (sigma(x), tau_x(h))) shows no gap at any order.
C-bij : the countercontrol of R1.

## 5. What would change the plan

If any control fails, the affected verdict is void and is reported as such; no re-tuning of the
decision rules after results are seen.

## Amendment 1 (appended before the computations it governs; nothing above is changed)

Reason: reading `verification/lean-mathlib/OIBridge/PhysicalC4StorageReadback.lean` showed that the
kernel already carries the strongest storage-and-routing predicate in the corpus,
`RoutedReadbackAtStorage K R` (write W, storage-time store S on Law(H_s | X_s = x, X_0 = a), causal
read R(1), rooted reappearance R(2)). It is the natural "stronger structural C2 + routing" form.
Results of runs already made (controls, sc16_search, c2_bijective_checks, lfsr_family,
em_countermodel, revival_check) are unaffected and are not re-run.

- **F4 := RoutedReadbackAtStorage(K)**, transcribed exactly from the Lean definition, with the
  prior of the realization (uniform in the exhaustive search).
- R5. F4 is **refuted** as a route to accessible-window P-indivisibility iff an exactly verified
  bijective rooted realization satisfies F4 at K and is P-divisible on {0..K} with K <= L-1.
  Exhaustive search at (2,2),(2,3),(3,2),(2,4) under the uniform prior, all K <= L-1; plus one
  explicit (EM)/(C2-slow) bijection (hidden-modulated flip rate, ledger write) on window K = 4.
- C-F4 (control): the predicate implementation must report F4 false on a decoupled bijection
  (no write) and true on the Lean-certified core carrier if it can be transcribed; at minimum it must
  report false whenever the rooted rows at t coincide for every t <= K (R(2) negative control, LFSR).
