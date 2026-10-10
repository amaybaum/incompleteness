#!/usr/bin/env python3
"""I2 tally of INVENTORY.md for RESULT.md §0 (stage 6, Q-EX-FULL, step 1).

DECISION RULE (fixed before the first run; it classifies by the text of each record, it decides nothing):
- A record is a block starting `### I2.<n> — <name>`; its first bullet `- kind: K · level: L · status: S · flag: F`.
- kind class: the text of K up to the first ' (' or ';' or ' and ' (lower-cased, trimmed).
- primary level: the first of H, O, P, M, G, X appearing in L.
- status class: first matching prefix of S among: 'proved [K]', 'proved [M]', 'assumed', 'conditional-on',
  'empirically motivated', 'open', 'refuted', 'scope statement'; a status beginning '(ii) ⟺ (iii) proved [M]' or
  'theorem for' or 'Bell-locality proved [M]' or 'theorem proved [M]' or 'equivalence proved [K]' or
  'classification proved [K]' or 'lemma proved [M]' or 'Theorem 1a proved [M]' or 'A.5–A.7 proved [M]' or
  'propositions proved [M]' or 'permutation unitarity proved [K]' or '(T) assumed' or "`DC1` unrevised" is
  classed by its first proof/assumption keyword; anything else is 'other' and is listed.
- flag: 'do not assume' iff F starts with it.
- bridge: counted 'none at L' iff the record's bridge text contains 'none at L'; 'transfer denied by the corpus' iff
  that phrase occurs in the record.
Output deterministic; counts and the id lists per class.
"""
import re
from collections import OrderedDict

STATUS = ["proved [K]", "proved [M]", "assumed", "conditional-on", "empirically motivated", "open", "refuted",
          "scope statement"]


def main():
    text = open("INVENTORY.md", encoding="utf-8").read().split("\n")
    recs = []
    cur = None
    for l in text:
        m = re.match(r"^### I2\.(\d+) — (.*)$", l)
        if m:
            cur = {"id": int(m.group(1)), "name": m.group(2), "body": []}
            recs.append(cur)
            continue
        if cur is not None:
            cur["body"].append(l)
    kinds, levels, stats, flags = OrderedDict(), OrderedDict(), OrderedDict(), []
    other = []
    none_at_l = 0
    denied = []
    for r in recs:
        head = next(b for b in r["body"] if b.startswith("- kind:"))
        parts = [p.strip() for p in head[2:].split(" · ")]
        f = {p.split(":", 1)[0]: p.split(":", 1)[1].strip() for p in parts if ":" in p}
        k = re.split(r" \(|;| and ", f["kind"])[0].strip().lower()
        kinds.setdefault(k, []).append(r["id"])
        lv = next((c for c in f["level"] if c in "HOPMGX"), "?")
        levels.setdefault(lv, []).append(r["id"])
        s = f["status"]
        cls = None
        for c in STATUS:
            if s.startswith(c):
                cls = c
                break
        if cls is None:
            hits = [(s.find(c), c) for c in STATUS if s.find(c) >= 0]
            cls = min(hits)[1] if hits else "other"
            if cls == "other":
                other.append(r["id"])
        stats.setdefault(cls, []).append(r["id"])
        if f.get("flag", "").startswith("do not assume"):
            flags.append(r["id"])
        body = "\n".join(r["body"])
        if re.search(r"bridge: none at L", body):
            none_at_l += 1
        if "transfer denied by the corpus" in body:
            denied.append(r["id"])
    print("records %d" % len(recs))
    for title, d in (("kind", kinds), ("level", levels), ("status", stats)):
        print("BY %s" % title)
        for k, v in d.items():
            print("  %-28s %3d  %s" % (k, len(v), ",".join(str(x) for x in v)))
    print("flag do-not-assume %d  %s" % (len(flags), ",".join(str(x) for x in flags)))
    print("bridge 'none at L' %d of %d" % (none_at_l, len(recs)))
    print("transfer denied by the corpus %d  %s" % (len(denied), ",".join(str(x) for x in denied)))
    print("status unclassified %d  %s" % (len(other), ",".join(str(x) for x in other)))


if __name__ == "__main__":
    main()
