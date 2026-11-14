# Reviewer check: each double-quoted string (>=12 chars) in Authority's c.<id> blocks (lines 96-182) must occur
# verbatim, after whitespace/markdown normalization, in that comment's body (fetched read-only via the API).
import json, re, sys, glob, os
base = sys.argv[1]; pre = open(sys.argv[2], encoding="utf-8").read().splitlines()
bodies = {os.path.basename(f)[:-5]: json.load(open(f)) for f in glob.glob(os.path.join(base, "*.json"))}
def norm(s):
    s = s.replace("**", "").replace("\n>", " ").replace("|", " ")
    s = re.sub(r"(^|\s)>\s", " ", s)
    return re.sub(r"\s+", " ", s).strip()
text = "\n".join(pre[95:182])
blocks = re.split(r"\n- \*\*c\.(\d+)\*\*", text)
n = bad = 0
for cid, blk in zip(blocks[1::2], blocks[2::2]):
    b = norm(bodies[cid]["body"])
    for q in re.findall(r'"([^"]{12,})"', blk, flags=re.S):
        n += 1
        if norm(q) not in b:
            bad += 1; print("c." + cid, "NOT FOUND:", norm(q)[:120])
print("quotes checked", n, "not found", bad)
