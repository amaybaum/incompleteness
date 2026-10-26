import re,sys
src=open(sys.argv[1]).read()
def rep(start,end_excl,repl):
    global src
    i=src.index(start); j=src.index(end_excl,i)
    src=src[:i]+repl+src[j:]
rep("Five conditions are in play:","**Theorem 4**","Five conditions are in play: (i) valid probabilities, (ii) trivial-ancilla consistency, (iii) inert spectators, (iv) full reversible control, and (v) iterated composition.\n\n")
rep("Marginalizing a reversible dynamics","The question is how much","Marginalizing a reversible dynamics over an unobserved register produces three features usually associated with quantum theory: stochastic laws; conditional memory, in which the visible past carries information about the visible future beyond the present; and failure of stochastic divisibility, in which would-be intermediate transition maps acquire negative entries.\n\n")
rep("Three notions are kept apart","No unconditional implication","Three notions are distinct [Main §3.2]: (1) accessible finite-horizon memory, $M_t>0$; (2) stochastic P-indivisibility of the visible population law; (3) quantum non-Markovianity under a chosen divisibility or backflow criterion. ")
rep("Assume three things:","Then the turnover","Assume (1) the mass-loss law $dM/dt=-\\alpha/M^2$ with constant $\\alpha$, (2) $S_{\\mathrm{BH}}\\propto M^2$, and (3) a constant ratio $\\beta$ of the radiation's coarse-grained entropy gain to the black-hole entropy lost. ")
rep("Theorem 1 concerns fixed-basis observable statistics.","On a fixed finite carrier","Theorem 1 concerns fixed-basis observable statistics. Operational quantum mechanics also requires coherent preparations, noncommuting interventions and composites, all represented simultaneously by one standard instrument theory. ")
rep("- **Without recovery.**","### 5.2","Exhaustive enumeration at small size gives both separations: 1,376 of the 40,320 bijections of $\\{0,1\\}^3$ give zero accessible advantage for a binary message with one register unread after two emissions, and sixty non-injective maps of $\\{0,1\\}^2$ recover a message exactly under complete access. Bijective dynamics with complete endpoint access gives exact recovery, and with a set $K$ of inaccessible endpoint values $P_{\\mathrm{succ}}\\ge1/|K|$; these conditions are sufficient, not necessary [BH-01].\n\n")
open(sys.argv[2],'w').write(src)
