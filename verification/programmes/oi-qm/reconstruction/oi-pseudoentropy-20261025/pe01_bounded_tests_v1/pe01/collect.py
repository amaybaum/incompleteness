"""Merge shard outputs into measurements.json, with the cross-shard controls (PLAN.md §5).

A shard is complete when DIR/<id>.json exists, incomplete when DIR/<id>.incomplete.json exists
(started, did not finish; its reason and completed cells are kept), and not run otherwise (A1).
A checkpoint is green only if it was evaluated and every evaluation passed. Checkpoints of a
missing primary shard are not evaluated, so the stage cannot be green; a missing or incomplete
m = 3 shard leaves its cells "not run" or "incomplete" (A1), and a failure inside one voids the stage.
"""
import json
import os
from fractions import Fraction

from . import cx, params as P, shard as S
from .exact import canonical, parse, walk_display_free

REQUIRED = ("EX1", "EX2", "EX3", "EX4", "EX5", "EX6", "EX7", "EX8", "IM1", "IM2", "IM3", "IM4", "IM5", "IM6",
            "PC", "NC", "SY", "MO", "FP", "CX", "K0", "RP", "PIN", "TH", "AR")
SMOKE_SCOPE = ("EX1", "EX2", "EX3", "EX4", "EX5", "EX6", "EX7", "EX8", "IM1", "IM2", "IM3", "IM4", "IM5", "IM6",
               "PC", "NC", "SY", "MO", "FP", "CX", "K0", "PIN", "TH", "AR")


def smoke_ids():
    return ["controls", "tape"] + ["n%d-%s" % (n, f) for n in (3, 4, 5) for f in S.FAMS]


def collect(src, out, mode):
    ids = S.shard_ids() if mode == "result" else smoke_ids()
    shards = {}
    data = {}
    for sid in ids:
        p = os.path.join(src, sid + ".json")
        pi = os.path.join(src, sid + ".incomplete.json")
        if os.path.exists(p):
            raw = open(p, "rb").read()
            d = json.loads(raw)
            data[sid] = d
            shards[sid] = {"status": "complete"}
        elif os.path.exists(pi):
            shards[sid] = {"status": "incomplete", "detail": json.load(open(pi))}
        else:
            shards[sid] = {"status": "not run"}
    ctl = {}

    def add(name, ok, where, failures=()):
        r = ctl.setdefault(name, {"pass": True, "checks": 0, "failures": [], "shards": []})
        r["checks"] += 1
        if where not in r["shards"]:
            r["shards"].append(where)
        if not ok:
            r["pass"] = False
            r["failures"].extend(list(failures)[:5] if failures else [where])

    commits = {d["commit"] for d in data.values()}
    modes = {d["mode"] for d in data.values()}
    for sid, d in sorted(data.items()):
        for name, r in d["controls"].items():
            add(name, r["pass"], sid, r["failures"])
        pf = d["preflight"]
        add("TH", pf["TH"]["pass"], sid, pf["TH"]["reasons"])
        add("PIN", pf["PIN"]["pass"], sid, pf["PIN"]["reasons"])
        # EX3: no float on the verdict path, every exact value parses
        try:
            walk_display_free(d)
            add("EX3", True, sid)
        except AssertionError as e:
            add("EX3", False, sid, [str(e)])
    if len(commits) > 1 or len(modes) > 1:
        add("PIN", False, "collect", ["shards from different commits or modes: %s %s" % (commits, modes)])
    # missing primary shards: their checkpoints were not evaluated
    for sid, st in shards.items():
        if st["status"] != "complete" and not sid.endswith("-m3"):
            for name in ("PC", "NC", "SY", "MO", "K0", "EX1"):
                add(name, False, sid, ["%s: shard %s" % (sid, st["status"])])
    # NC-2 specificity (G_filt against G_lin), per n
    for n in P.NS:
        a, b = data.get("n%d-lin" % n), data.get("n%d-filt" % n)
        if not a or not b:
            continue
        ok, why = nc2_specificity(n, a["measurements"], b["measurements"])
        add("NC", ok, "n%d specificity" % n, [why] if not ok else ())
    # CX self-test
    th = None
    if "controls" in data:
        th = data["controls"]["preflight"]["TH"]["theta_by_n"]
    if th is None and data:
        th = next(iter(data.values()))["preflight"]["TH"]["theta_by_n"]
    cxs = cx.selftest(th) if th else {"pass": False}
    add("CX", cxs["pass"], "collect", [] if cxs["pass"] else [json.dumps(cxs)])
    # RP: replay records
    rp = {}
    for sid in data:
        p = os.path.join(src, sid + ".rp.json")
        if os.path.exists(p):
            rp[sid] = json.load(open(p))["identical"]
    if mode == "result":
        for sid in data:
            add("RP", rp.get(sid) is True, sid, ["no replay" if sid not in rp else "replay differs"])
    controls = {}
    scope = REQUIRED if mode == "result" else SMOKE_SCOPE
    for name in REQUIRED:
        if name in ctl:
            controls[name] = ctl[name]
        elif name in scope:
            controls[name] = {"pass": False, "checks": 0, "failures": ["not evaluated"], "shards": []}
        else:
            controls[name] = {"pass": None, "checks": 0, "failures": [], "shards": [], "status": "not in smoke scope"}
    green = all(controls[k]["pass"] is True for k in scope)
    pf0 = (data.get("controls") or next(iter(data.values())))["preflight"] if data else None
    witnesses = []
    for sid, d in sorted(data.items()):
        for w in d["measurements"].get("witnesses", []):
            w = dict(w)
            w["shard"] = sid
            witnesses.append(w)
    meas = {
        "schema": "pe01-measurements/1",
        "mode": mode,
        "commit": next(iter(commits)) if len(commits) == 1 else sorted(commits),
        "recipe": "python3 -I -B %s/run.py collect <dir> --mode %s --out <dir>" % (P.REL, mode),
        "plan_blob": pf0["PIN"]["plan_blob"] if pf0 else None,
        "a1_blob": pf0["TH"]["a1_blob"] if pf0 else None,
        "theta_by_n": th,
        "K_LP_by_n": pf0["TH"]["K_LP_by_n"] if pf0 else None,
        "m3_passive_scope": pf0["TH"]["m3_passive_scope"] if pf0 else None,
        "m3_passive_K_cap": pf0["TH"]["m3_passive_K_cap"] if pf0 else None,
        "shards": shards,
        "controls": controls,
        "controls_green": green,
        "control_scope": list(scope),
        "cx_selftest": cxs,
        "AR": data["controls"]["measurements"]["AR"] if "controls" in data else None,
        "pending": next(iter(data.values()))["pending"] if data else None,
        "results": {sid: d["measurements"] for sid, d in sorted(data.items()) if sid not in ("controls",)},
        "controls_shard": data["controls"]["measurements"] if "controls" in data else None,
        "witnesses": witnesses,
    }
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "measurements.json"), "wb") as f:
        f.write(canonical(meas))
    print("collect: %d shards complete, controls %s" % (len(data), "green" if green else "NOT green"))
    return 0


def nc2_specificity(n, lin, filt):
    """At every K where the records of both G_filt and G_lin are injective: U equal, and B2 at
    lambda = n+1 on G_filt <= that on G_lin, strictly smaller at some such K."""
    el = lin["entropy"]["G_lin"]["count_multisets"]
    ef = filt["entropy"]["G_filt"]["count_multisets"]
    M = 1 << (n + 1)
    ul = [parse(x) for x in lin["classes"]["U"]["G_lin"]["values"]]
    uf = [parse(x) for x in filt["classes"]["U"]["G_filt"]["values"]]
    bl = [parse(x) for x in lin["classes"]["B2"]["G_lin"]["lambda_n_plus_1"]]
    bf = [parse(x) for x in filt["classes"]["B2"]["G_filt"]["lambda_n_plus_1"]]
    ks = [K for K in range(len(el)) if el[K] == [[1, M]] and ef[K] == [[1, M]]]
    if not ks:
        return False, "no K with both records injective"
    eq = all(ul[K] == uf[K] for K in ks)
    le = all(bf[K] <= bl[K] for K in ks)
    lt = any(bf[K] < bl[K] for K in ks)
    return eq and le and lt, "n=%d: U equal %s, B2 <= %s, strict somewhere %s" % (n, eq, le, lt)
