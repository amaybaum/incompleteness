"""Merge matrix/part-B1..B5.json into matrix.json and check coverage against inventory/claims.json.

Each claim (and each direction sub-claim) must appear exactly once. Where two parts carry the same id (B5 mapped
I-123 and I-124, which lie in B2's range), the row from the part whose range owns the id is kept, and the other is
recorded under `duplicates`. Verdicts the synthesis resolved differently (matrix/resolutions.json) are
applied, with the mapper's verdict kept as `mapper_verdict`; chain-link layer corrections (matrix/chain-relabels.json)
are applied with the mapper's layer kept as `mapper_layer`.

Order with step 7: merge_matrix.py, then evidence/scripts/E4_aggregate.py (which reads matrix.json and writes
evidence.json), then merge_matrix.py again (which copies each row's evidence level from evidence.json), then
matrix/scripts/render_matrix.py. E4_aggregate.py --check fails if matrix.json's levels differ from evidence.json's.
"""
import json, sys, collections

RANGES = {"B1": (1, 91), "B2": (92, 171), "B3": (172, 245), "B4": (246, 312), "B5": (313, 385)}


def num(i):
    return int(i.split("-")[1].split(".")[0])


claims = json.load(open("inventory/claims.json", encoding="utf-8"))
want = []
for c in claims:
    want.append(c["id"])
    for s in (c.get("direction") or {}).get("sub_claims", []) or []:
        want.append(s["id"])

rows, dups = {}, []
for part, (lo, hi) in RANGES.items():
    for r in json.load(open(f"matrix/part-{part}.json", encoding="utf-8")):
        own = lo <= num(r["id"]) <= hi
        r["_part"] = part
        if r["id"] in rows:
            keep_new = own and not (RANGES[rows[r["id"]]["_part"]][0] <= num(r["id"]) <= RANGES[rows[r["id"]]["_part"]][1])
            dups.append({"id": r["id"], "kept": part if keep_new else rows[r["id"]]["_part"],
                         "dropped": rows[r["id"]]["_part"] if keep_new else part})
            if keep_new:
                rows[r["id"]] = r
        else:
            rows[r["id"]] = r

# Chain-link layer corrections (matrix/chain-relabels.json); each names its link by index and source.
relabels = json.load(open("matrix/chain-relabels.json", encoding="utf-8"))
for i, fixes in relabels.items():
    if i.startswith("_"):
        continue
    for fx in fixes:
        ln = rows[i]["chain"][fx["index"]]
        if ln["source"] != fx["source"] or ln["layer"] != fx["from"]:
            sys.exit("chain-relabels.json: %s link %d does not match (%s, %s)" % (i, fx["index"], ln["layer"], ln["source"]))
        ln["mapper_layer"] = ln["layer"]
        ln["layer"] = fx["to"]
        ln["relabel_reason"] = fx["reason"]

res = json.load(open("matrix/resolutions.json", encoding="utf-8"))
for i, v in res.items():
    if i.startswith("_"):
        continue
    r = rows[i]
    if "verdict" in v:
        r["mapper_verdict"] = r["verdict"]
        r["verdict"] = v["verdict"]
    r["resolution"] = {"finding": v.get("finding"), "reason": v["reason"], "by": v.get("by", "synthesis")}
    for k in ("proof_status", "proposed_fix"):
        if k in v:
            r["mapper_" + k] = r.get(k)
            r[k] = v[k]

# Step 7: each row's evidence level, as evidence/scripts/E4_aggregate.py computed it into evidence.json.
import os
if os.path.exists("evidence.json"):
    ev = json.load(open("evidence.json", encoding="utf-8"))["claims"]
    for i, r in rows.items():
        r["evidence_level"] = ev[i]["evidence_level"]
        r["evidence_basis"] = ev[i]["basis"]

missing = [i for i in want if i not in rows]
extra = [i for i in rows if i not in set(want)]
order = {i: k for k, i in enumerate(want)}
merged = sorted(rows.values(), key=lambda r: order.get(r["id"], 10**9))
verdicts = collections.Counter(r["verdict"] for r in merged)
status = collections.Counter(r["proof_status"] if isinstance(r["proof_status"], str) else r["proof_status"].get("status", str(r["proof_status"])) for r in merged)
summary = {"rows": merged, "duplicates": dups, "missing": missing, "extra": extra,
           "verdicts": dict(verdicts), "proof_status": dict(status)}
if all("evidence_level" in r for r in merged):
    summary["evidence_levels"] = dict(collections.Counter(r["evidence_level"] for r in merged))
json.dump(summary,
          open("matrix.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("rows", len(merged), "want", len(want), "missing", missing, "extra", extra)
print("duplicates", dups)
print("verdicts", dict(verdicts))
print("status", dict(status))
sys.exit(1 if missing else 0)
