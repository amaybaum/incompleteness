# H-NEQ: the exact projected-memory template

The cosmological model-input gate remains **OPEN**. No selected completion
fixes its update, observer partition, initial law, cosmological mode readout
and clock jointly. This follow-up supplies the exact equation those choices
determine and evaluates it for Main §2.4's actual minimal model. It selects
no cosmological completion and analyses no observational data. Main §4.5's
conditional mixing premise is retained;
Main §4.6 already distinguishes an effective gap from finite Koopman dynamics.

Evidence: [W] universal written algebra; [X] finite rational controls.
Classification: ELABORATING on the consistency axis; block elimination and
the finite recurrence obstruction are confirming mathematics.

## Exact source-to-projection equation [W]

Fix a finite bijection phi, a surjective partition f:S→O, and a strictly
positive stationary prior pi. U pushes distributions forward along phi.
P sums probabilities over each partition cell. Let R lift a macro law using
the fixed conditional prior: R_(s,a)=pi_s/pi(f=a) when f(s)=a, otherwise zero.
Then PR=I, D=RP is a projection, and Q=I-D. This lift is a bookkeeping choice;
the real microscopic state is not reset to its image after each time step.

Set p_t=P rho_t, eta_t=Q rho_t and

    A=PUR, B=PU, C=QUR, E=QUQ.

The two exact equations are p_(t+1)=A p_t+B eta_t and
eta_(t+1)=C p_t+E eta_t, since rho_t=R p_t+eta_t and Q eta_t=eta_t.
Iterating the second yields

    p_(t+1) = A p_t + B E^t eta_0
               + sum_(j=0)^(t-1) B E^(t-1-j) C p_j.

The empty sum at t=0 matters. A is stochastic and preserves P pi, but its
repeated application is generally a reset comparison, not this source's
projected evolution. The initial hidden term and memory terms are derived,
rather than independently fitted relaxation parameters. A varying partition
or time-dependent update needs a separately derived nonautonomous formula.

## Exact autonomy has a sharp finite-domain limit [W]

Suppose one matrix A gives P U rho=A P rho for every microscopic law rho.
Applying this to each point mass shows that f(phi(s)) depends only on f(s).
Thus phi induces a deterministic macro map g. Surjectivity of phi and f
makes g surjective; finiteness makes it bijective. A is therefore a
permutation, with no strictly decaying eigenmode. This conclusion requires
autonomy for every microscopic initial law, not just one prepared family.

Even on the lifted family Rp, the exact macro propagators K_t=P U^t R
are periodic: U^L=I for the finite permutation's order L, and K_L=I.
If K_t=A^t for all t, then A^L=I. A stochastic matrix with a stochastic
inverse is a permutation: nonnegative inverse-product zero entries force
each column to have one nonzero support. Hence an exact, indefinitely
decaying autonomous law cannot be inferred for this fixed finite closed
source. Approximate closure on a named prerecurrence window, effective
baths, conditioned histories, changing partitions and infinite limits
remain distinct possibilities. This result does not refute conditional EM.

## Nonvacuous finite control [X]

For the cycle 0→1→2→3→0, partition {0,1}/{2,3}, uniform prior and initially
lifted macro law (1,0), the direct projected laws are

    (1,0), (1/2,1/2), (0,1), (1/2,1/2), (1,0).

The one-step A maps every law to (1/2,1/2); its powers already fail at t=2.
Here eta_0=0, so the discrepancy tests the memory term itself. A point mass
at 0 has a nonzero initial hidden term, testing that separate clause.
The generic checker passes 13,704 exact checks over 492 cases. It computes
direct trajectories by state-index reallocation and compares them with
independently assembled projection/lift matrices and memory sums. These are
two computational paths in one stdlib checker, not independent authorship.
The four-cycle adds seven checks and five countercontrols. Each countercontrol
runs a corrupted input through the same checks, which must reject it: the
recurrence with its memory terms omitted, the recurrence with its initial
hidden term omitted, and an invalid bijection, partition and stationary prior.
The saved output replays byte for byte. `evidence.json` states the recipe and
the replay's provenance; SHA256SUMS digests the files.
The examples test block elimination; they discharge no (C1)–(C4) observer
realization or cosmological mode readout.

## The manuscript's actual minimal model [W, X]

Main §2.4 specifies twelve states (x,h), x=0,1 and h=1,...,6. The update
flips x for h=1,2 and swaps h=3↔4 and h=5↔6 at fixed x. The observer reads
x and the conditional hidden preparation is uniform. This gives U²=I and

    A = [[2/3,1/3],[1/3,2/3]], K_2=P U² R=I,
    B C = I−A² = (4/9) [[1,−1],[−1,1]].

The off-diagonal block of U²=I gives B E=−A B on the hidden subspace.
Consequently the exact memory coefficients are

    B E^j C = (−1/3)^j (4/9) [[1,−1],[−1,1]].

The one-step comparison has a spectral gap, and even its memory kernel
decays geometrically, yet the true visible law returns every two steps.
Thus neither that comparison gap nor decay of the memory coefficients
alone is a source for scalar visible relaxation. This evaluates the actual
construction, rather than transferring a reset-model calculation into it.
The literal index checker adds 25 source-model checks, verifying all twelve
point-state updates and the first eight memory coefficients. It adds 378
checks of the full projected recurrence against literal index evolution,
from all twelve point states and both lifted visible laws over nine steps.
Replacing E by −E, which gives the kernel ratio +1/3, is rejected. The total is
14,120 checks, six of them countercontrols. It checks the model's quoted probability
construction; it does not certify every observer-condition claim or give
it a cosmological mode or scale-factor interpretation.

## What must be supplied next

A physical completion must specify the update, partition, initial law,
mode response and clock; then derive A, C, E and the initial hidden term.
A scalar Hubble-order decay additionally needs a controlled closure and
error bound, a source for its rate coefficient, and a post-exit/readout rule.
The template fixes where each input enters; the four-cycle comparison
supplies none of those physical choices. No native F, execution, receipt,
adopted theorem or maintained manuscript classification changes.

The general projection-with-memory method is discussed by Chorin, Hald and
Kupferman, [PNAS 97 (2000), 2968–2973](https://doi.org/10.1073/pnas.97.7.2968).
No theorem from that comparison is used as a premise: the finite equations
above follow by explicit block elimination.
