#!/usr/bin/env python3
"""M2/M3 for DESIGN-r2: insert every current marker string into every batch-1 positive control, as a
separate sentence and as a coordinated clause; r2 must still FAIL (M2); the current checker must
accept a non-trivial share of the sentence insertions (M3). Usage: m2_r2.py CURRENT_CHECKER"""
import sys, os, json, importlib.util
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location("pr", os.path.join(H, "proto.r2.py")); pr = importlib.util.module_from_spec(s); s.loader.exec_module(pr)
s = importlib.util.spec_from_file_location("cc", sys.argv[1]); cc = importlib.util.module_from_spec(s); s.loader.exec_module(cc)
FIX = json.load(open(os.path.join(H, "licences-fixture.json"))); EMPTY = json.load(open(os.path.join(H, "licences.json")))
marks = list(cc.MARKERS) + list(cc.OI_MARKERS)
pos = [c for c in json.load(open(os.path.join(H, "controls.json"))) if c["expect"] == "FAIL"]
def cur(par):
    for rx, why, mk in [(a, b, cc.MARKERS) for a, b in cc.CLAIMS] + [(a, b, cc.OI_MARKERS) for a, b in cc.OI_CLAIMS]:
        if rx.search(par) and not any(k in par for k in mk):
            return "FAIL"
    return "PASS"
res = Counter(); cur_acc = 0; n_sent = 0; bad = []
for c in pos:
    t = c["text"].rstrip()
    for m in marks:
        forms = {"sentence": t + " The text notes " + m + ".",
                 "clause": (t[:-1] if t.endswith(".") else t) + ", and the text notes " + m + "."}
        for form, txt in forms.items():
            for name, L in (("fixture", FIX), ("empty", EMPTY)):
                v, _ = pr.verdict_for(txt, c["rule"], c.get("context", ""), L)
                res[(form, name, v)] += 1
                if v != "FAIL":
                    bad.append((c["id"], form, name, m, v))
            if form == "sentence":
                n_sent += 1; cur_acc += cur(txt) == "PASS"
print("markers", len(marks), "positives", len(pos))
for k, v in sorted(res.items()): print(k, v)
print("M2 non-FAIL:", len(bad)); [print(b) for b in bad[:20]]
print("M3 current checker accepts", cur_acc, "of", n_sent, "sentence insertions")
