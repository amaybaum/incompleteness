import re,sys
src=open(sys.argv[1]).read()
def rep(start,end_excl,repl):
    global src
    i=src.index(start); j=src.index(end_excl,i)
    src=src[:i]+repl+src[j:]
rep("9. **Testability.**","\n\n","")
rep(" Up to flipping the final bit, this is the process","\n\n"," It is the process of [RHP14, Eq. (15)] up to flipping the final bit; see also [DO, App. A].")
rep("- **Sensitivity.**","\n\nThe fraction","- **Sensitivity.** A mass-dependent coefficient moves the fraction, e.g. to $0.7027$ for $\\alpha\\propto M^{-1/2}$ [BH-02, C7].")
rep("This paper presents these results","\n\n","Section 4 gives worked examples, §5 the black-hole application and §6 the limitations; complete arguments are in [Main].")
rep("**Decoupling","\n\n","") if "**Decoupling" in src else None
rep("The incompleteness meant here is","\n\n","The incompleteness meant here is inaccessibility of the hidden sector, present already for a single fixed readout; it is not the joint unsharpness of non-commuting observables [Main §3.4].")
open(sys.argv[2],'w').write(src)
