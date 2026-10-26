import re,sys
src=open(sys.argv[1]).read()
def cut_between(start,end_excl,repl=""):
    global src
    i=src.index(start); j=src.index(end_excl,i)
    src=src[:i]+repl+src[j:]
# App A: two columns
lines=src.split("\n"); out=[]
for l in lines:
    if l.startswith("| ") or l.startswith("|---"):
        cells=[c.strip() for c in l.strip().strip("|").split("|")]
        if l.startswith("|---"): out.append("|---|---|"); continue
        out.append("| "+cells[0]+" | "+cells[1]+" |")
    else: out.append(l)
src="\n".join(out)
# 6.4: drop pointer items 1-3,10
cut_between("1. **The operational-lifting layer.**","4. **Formalization**","Open problems 1–3 are §6.1 (which of (iii)–(v) a substratum supplies), §6.2 (selection of the relating evolution) and §2.3 (the quadratic exponent); the black-hole steps are listed in §5.4. Further:\n\n")
src=src.replace("10. **The black-hole steps** of §5.4.\n","")
# 2.2 independent prior paragraph compress
cut_between("  Main also gives a realization in which","- **$D\\Rightarrow","  A realization with hidden prior independent of $x_0$ is also given [Main §3.4, Theorem (finite-horizon process dilation)]; it is proved on paper.\n")
# biconditional paragraph compress
cut_between("Theorem 2 yields a biconditional","Two further bounds","Consequently $M_t>0$ holds exactly when every faithful realization carries readout-relevant hidden memory at $t$: forward by (a) in each realization, converse by (a) in the realization of Theorem 1. Both directions use the vanishing criterion for conditional mutual information, proved on paper.\n\n")
open(sys.argv[2],'w').write(src)
