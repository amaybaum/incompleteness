"""Introduction-r15.md = r14 + the landing review's findings (L1-L3).

L1 restates the readback bound with a common present state and joint probabilities, as Main §2.3 states it at
b64919cd. L2 repins the corpus commit to b64919cd, at which every cited pointer reads as at c967d6a9 apart from
that lemma; the Lean sources are identical. L3 gives the provenance comments full repository paths, because the
paper lands under papers/. Each edit is an exact replacement with a stated count; every other sentence is
byte-identical to r14.
"""
import sys

src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()
log = []


def rep(tag, old, new, count=1):
    global t
    n = t.count(old)
    assert n == count, (tag, n, old[:80])
    t = t.replace(old, new)
    log.append("%s(%d)" % (tag, n))


rep("L1", "If two visible histories of length $k$ with a common endpoint, each of probability at least $p_0$, induce",
    "If two values of $X_{<k}$ followed by a common present state $X_k$, each of joint probability at least $p_0$, "
    "induce")
rep("L2", "whose Lean sources are identical at the corpus commit `c967d6a9`",
    "whose Lean sources are identical at the corpus commit `b64919cd`")
rep("L2", "**Corpus** (repository commit `c967d6a9`,", "**Corpus** (repository commit `b64919cd`,")
rep("L3", "(draft/review/references/",
    "(verification/audits/manuscript/introductory-paper-20261025/draft/review/references/", count=7)

open(dst, "w", encoding="utf-8").write(t)
print("applied: %s" % "; ".join(log))
