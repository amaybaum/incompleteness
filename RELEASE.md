# RELEASE — freeze record (batch b141, review 51, 2026-08-16)

This file records the frozen state of the release so the artifact is
self-describing. The freeze was reached through an adversarial review
sequence — reviews 31–51, batches b119–b141 — with the final reviewer
verdict: freeze-ready without qualification, at every layer
(mathematics, Main, build/package, book corpus).

## Certified results, at their stated scopes

1. **Representation.** $S \iff D \iff Q_{\mathrm{fb}}$: every finite
   observable law of a deterministic substratum admits a fixed-basis
   unitary quantum representation, and conversely — proved, all
   finite laws (`sdq_probes.py`, exact, 1,488 realizations).
2. **Memory.** $M_t > 0 \iff$ unavoidable readout-relevant hidden
   predictive memory — proved for every faithful completion
   (`memory_probes.py`, exact, 1,464 realizations). The memory sector
   is the discriminating content; representability is universal.
3. **Classical-dimension no-go.** No fixed finite classical carrier
   reproduces full qubit operational behavior, under the ordinary
   operational interface (preparation → finite ontic carrier → freely
   chosen measurement) — the elementary factorization half proved
   inline; the unbounded-dimension half imported (Heinosaari–Kerppo–
   Leppäjärvi–Plávala, arXiv:2308.07727; PRA 109, 032627 (2024))
   (`nogo_probes.py`, exact over $\mathbb{Q}(\sqrt3)$).
4. **ε-realization, unconditional.** Every $d$-dimensional adaptive
   quantum experiment of horizon $K$ has a finite reversible
   deterministic realization within any $\varepsilon$: exact-ring
   regime certified end to end; finite-bit regime proved via the
   instrument-level fixed-point Rounding Lemma
   ($C_{d,R} = 48Rd^4$, family-wide $R$), the
   clipping–normalization Corollary with deterministic fallback, and
   the proved negativity-ledger recurrence — total
   $\|P_R - P_Q\|_{\mathrm{TV}} \leq K(m{-}1)/G + 12K^2C_{d,R}2^{-b}$
   (`opglue_probes.py`, 21 checks including the actual simulator
   kernel with exact mass conservation). One controlled dynamics
   serves all protocols; density is the maximum the no-go permits, so
   class identity is deliberately not claimed.

Canonical predictive quotient (a purification ingredient), the
finite-test density Corollary at fixed $(d, m)$, and the maximal-
equivalence summary are stated in Main §3.4 with their exact scopes.

## Verification snapshot at freeze

Foundation suites **28/28** · architecture guard **148 invariants, 0
violations, 0 self-test failures** · citations **103, 0 broken, 0
duplicate bibliography numbers** · book/chapter mirror **0 absent
lines** · rendered-text sweeps clean on all retired formulations.
Pages: Main 79 · SM 136 · book 537 (all 12 papers rebuild). Page
counts may vary ±1 across TeX/pandoc versions; a canonical-toolchain
rebuild is required before DOI deposit.

## Reproduction

    sh ./build.sh              # all papers
    sh ./build.sh Main SM      # named papers
    sh ./build.sh --book       # the consolidated book
    cd papers/oi_lattice_code
    bash run_all_probes.sh     # 28 suites + citation/architecture/mirror guards
    OI_ARCH_FULL=1 python3 architecture_check.py

## Open items surviving the freeze — by design

1. **The selection theorem** (route (ii)) — the next mathematical
   project: operational translation of the canonical predictive
   quotient; tomographic injectivity; continuous reversibility.
2. Named optimizations: the negativity ledger's $K^2$ (one extra
   $\log_2 K$ bit; a polish, not a gap); the variational VALUE
   question.
3. $\mathcal{F}(r) = 2r - r^2$ is a proposed model form (derivation
   unpackaged); shipping a derivation re-upgrades it.
4. Owner options: renaming the "partially-quantum" label (kept as a
   backflow-strength label with explicit not-a-membership
   disclaimers); shipping review notes inside the repo.

## Corrections of record (the honesty ledger)

The b125 polytope proof was invalid and was replaced by the
classical-dimension form, with the SIC counterexample certified. The
b127 bibliography insertion collided with existing numbers and was
repaired, with the citation checker hardened to enforce uniqueness.
Freeze declarations at b138/b139 were premature at the book layer and
were corrected by the review-48/49 semantic sweeps. Concurrency
events (three) were handled by coordination notes with single-writer
verification per batch.
