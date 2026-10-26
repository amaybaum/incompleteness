"""Merge matrix/part-B1..B5.json into matrix.json and check coverage against inventory/claims.json.

Each claim (and each direction sub-claim) must appear exactly once. Where two parts carry the same id (B5 mapped
I-123 and I-124, which lie in B2's range), the row from the part whose range owns the id is kept, and the other is
recorded under `duplicates`.
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

missing = [i for i in want if i not in rows]
extra = [i for i in rows if i not in set(want)]
order = {i: k for k, i in enumerate(want)}
merged = sorted(rows.values(), key=lambda r: order.get(r["id"], 10**9))
verdicts = collections.Counter(r["verdict"] for r in merged)
status = collections.Counter(r["proof_status"] if isinstance(r["proof_status"], str) else r["proof_status"].get("status", str(r["proof_status"])) for r in merged)
json.dump({"rows": merged, "duplicates": dups, "missing": missing, "extra": extra,
           "verdicts": dict(verdicts), "proof_status": dict(status)},
          open("matrix.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("rows", len(merged), "want", len(want), "missing", missing, "extra", extra)
print("duplicates", dups)
print("verdicts", dict(verdicts))
print("status", dict(status))
sys.exit(1 if missing else 0)
