"""Introduction-r13.md = r12 + the two nits of the r12 confirmation (W1, W2).

Each edit is an exact, uniquely matching replacement on r12, so every unchanged sentence stays byte-identical to r12.
"""
import sys

src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()
log = []


def rep(tag, old, new):
    global t
    n = t.count(old)
    assert n == 1, (tag, n, old[:80])
    t = t.replace(old, new)
    log.append(tag)


# --- W1: ancilla discard keeps the outcome family (prepAvail_discard; avail_iff_availExt_one, LevelOneSeam:128) ---
rep("W1", "with the ancilla then discarded, is an available operation on the system [GR §3.3].",
    "with the ancilla then discarded, is an available instrument on the system with the same outcomes [GR §3.3].")

# --- W2: why the Lean pin and the corpus pin differ ---
rep("W2", "at commit 17b830bcd0ecc36e10eff5b9eeca03bdd7198d86, by building",
    "at commit 17b830bcd0ecc36e10eff5b9eeca03bdd7198d86, whose Lean sources are identical at the corpus commit "
    "`c967d6a9`, by building")

open(dst, "w", encoding="utf-8").write(t)
print("applied %d edits: %s" % (len(log), "; ".join(log)))
