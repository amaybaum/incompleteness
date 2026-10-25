"""Merge shard outputs into measurements.json: the verdict inputs and each shard file's digest.

Shard status (A1): complete (DIR/<id>.json), incomplete (DIR/<id>.incomplete.json: started, not
finished; its completed cells and controls are kept), not run (neither). Checkpoint status:
  failed       evaluated somewhere and failed  -> the stage is VOID
  unevaluated  a primary shard is not complete, or a replay record is missing -> INCOMPLETE
  green        otherwise.
A missing or incomplete m = 3 shard leaves its cells "not run" or "incomplete" and does not by
itself make the stage incomplete; a failure inside one voids the stage (A1).
measurements.json carries only verdict inputs (statuses, controls, horizons, tags inputs, K0
summaries, windows, witnesses, AR, TH) and the sha256 of every shard file, which holds the full
lossless curves. Every file is held to SIZE_BUDGET.
"""
import hashlib
import json
import os

from . import cx, params as P, shard as S
from .exact import canonical, parse, unrle, walk_display_free

SIZE_BUDGET = 20 * 1024 * 1024
REQUIRED = ("EX1", "EX2", "EX3", "EX4", "EX5", "EX6", "EX7", "EX8", "IM1", "IM2", "IM3", "IM4", "IM5", "IM6",
            "PC", "NC", "SY", "MO", "FP", "CX", "K0", "RP", "PIN", "TH", "AR")
SMOKE_SCOPE = tuple(c for c in REQUIRED if c != "RP")


def smoke_ids():
    return ["controls", "tape"] + ["n%d-%s" % (n, f) for n in (3, 4, 5) for f in S.FAMS]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def collect(src, out, mode):
    ids = S.shard_ids() if mode != "smoke" else smoke_ids()
    shards, data = {}, {}
    oversize = []
    for sid in ids:
        p = os.path.join(src, sid + ".json")
        pi = os.path.join(src, sid + ".incomplete.json")
        pv = os.path.join(src, sid + ".provenance.json")
        prov = json.load(open(pv)) if os.path.exists(pv) else {}
        if os.path.exists(p):
            raw = open(p, "rb").read()
            if len(raw) > SIZE_BUDGET:
                oversize.append((sid, len(raw)))
            data[sid] = json.loads(raw)
            shards[sid] = {"status": "complete", "sha256": sha(raw), "bytes": len(raw)}
        elif os.path.exists(pi):
            raw = open(pi, "rb").read()
            inc = json.loads(raw)
            shards[sid] = {"status": "incomplete", "sha256": sha(raw), "reason": inc.get("reason"),
                           "completed_cells": inc.get("completed_cells", []), "controls": inc.get("controls", {})}
        else:
            shards[sid] = {"status": "not run"}
        for k in ("run_id", "run_attempt", "job"):
            if k in prov:
                shards[sid][k] = prov[k]
        rp = os.path.join(src, sid + ".rp.json")
        if os.path.exists(rp):
            shards[sid]["replay_identical"] = json.load(open(rp))["identical"]
    if oversize:
        print("collect: REFUSED, shard files over the %d-byte budget: %s" % (SIZE_BUDGET, oversize))
        return 2
    ctl = {}

    def add(name, ok, where, failures=()):
        r = ctl.setdefault(name, {"pass": True, "checks": 0, "failures": [], "shards": []})
        r["checks"] += 1
        if where not in r["shards"]:
            r["shards"].append(where)
        if not ok:
            r["pass"] = False
            r["failures"].extend([str(f)[:300] for f in (list(failures)[:5] if failures else [where])])

    commits = {d["commit"] for d in data.values()}
    modes = {d["mode"] for d in data.values()}
    for sid, d in sorted(data.items()):
        for name, r in d["controls"].items():
            add(name, r["pass"], sid, r["failures"])
        pf = d["preflight"]
        add("TH", pf["TH"]["pass"], sid, pf["TH"]["reasons"])
        add("PIN", pf["PIN"]["pass"], sid, pf["PIN"]["reasons"])
        try:
            walk_display_free(d)
            add("EX3", True, sid)
        except AssertionError as e:
            add("EX3", False, sid, [str(e)])
    for sid, st in shards.items():
        if st["status"] == "incomplete":
            for name, r in st["controls"].items():
                add(name, r["pass"], sid + " (incomplete)", r["failures"])
    if len(commits) > 1 or len(modes) > 1 or (modes and modes != {mode}):
        add("PIN", False, "collect", ["shards from different commits or modes: %s %s" % (sorted(commits), sorted(modes))])
    unevaluated = []
    for sid, st in shards.items():
        if st["status"] != "complete" and not sid.endswith("-m3"):
            unevaluated.append("shard %s %s" % (sid, st["status"]))
    # cross-shard checks
    for n in P.NS:
        a, b = data.get("n%d-lin" % n), data.get("n%d-filt" % n)
        if a and b:
            ok, why = nc2_specificity(n, a["measurements"], b["measurements"])
            add("NC", ok, "n%d specificity" % n, [why] if not ok else ())
        for fam in S.FAMS:
            fs, m3 = data.get("n%d-%s" % (n, fam)), data.get("n%d-%s-m3" % (n, fam))
            if fs and m3:
                for msg, ok in m3_inclusions(fs["measurements"], m3["measurements"]):
                    add("MO", ok, "n%d-%s %s" % (n, fam, msg))
    pf0 = (data.get("controls") or next(iter(data.values())))["preflight"] if data else None
    th = pf0["TH"]["theta_by_n"] if pf0 else None
    cxs = cx.selftest(th) if th else {"pass": False}
    add("CX", cxs["pass"], "collect self-test", [] if cxs["pass"] else [json.dumps(cxs)[:300]])
    arr = data["controls"]["measurements"]["AR"] if "controls" in data else None
    witnesses = []
    for sid, d in sorted(data.items()):
        for w in d["measurements"].get("witnesses", []):
            w = dict(w, shard=sid)
            if arr is not None:
                want = arr["K_cx"][w["generator"]][w["n"] - 3]
                add("CX", w["K_cx"] == want, "witness K_cx vs AR", ["%s n=%d: %s vs %s" % (w["generator"], w["n"], w["K_cx"], want)])
            witnesses.append(w)
    if mode == "result":
        for sid in data:
            rp = shards[sid].get("replay_identical")
            if rp is None:
                unevaluated.append("RP %s (no replay record)" % sid)
            else:
                add("RP", rp is True, sid, ["replay differs"])
    scope = REQUIRED if mode != "smoke" else SMOKE_SCOPE
    controls = {}
    for name in REQUIRED:
        if name in ctl:
            controls[name] = ctl[name]
        elif name in scope:
            controls[name] = {"pass": None, "checks": 0, "failures": [], "shards": [], "status": "not evaluated"}
            unevaluated.append("checkpoint %s" % name)
        else:
            controls[name] = {"pass": None, "checks": 0, "failures": [], "shards": [], "status": "not in smoke scope"}
    failed = sorted(k for k in scope if controls[k]["pass"] is False)
    status = "void" if failed else ("incomplete" if unevaluated else "green")
    meas = {
        "schema": "pe01-measurements/2",
        "mode": mode,
        "commit": next(iter(commits)) if len(commits) == 1 else sorted(commits),
        "run": {"run_id": os.environ.get("GITHUB_RUN_ID", "local"),
                "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "local")},
        "recipe": "python3 -I -B %s/run.py collect <dir> --mode %s --out <dir>" % (P.REL, mode),
        "plan_blob": pf0["PIN"]["plan_blob"] if pf0 else None,
        "a1_blob": pf0["TH"]["a1_blob"] if pf0 else None,
        "a2": pf0["TH"].get("A2") if pf0 else None,
        "theta_by_n": th,
        "K_LP_by_n": pf0["TH"]["K_LP_by_n"] if pf0 else None,
        "m3_passive_scope": pf0["TH"]["m3_passive_scope"] if pf0 else None,
        "m3_passive_K_cap": pf0["TH"]["m3_passive_K_cap"] if pf0 else None,
        "shards": shards,
        "controls": controls,
        "control_scope": list(scope),
        "status": status,
        "failed": failed,
        "unevaluated": unevaluated,
        "cx_selftest": cxs,
        "AR": arr,
        "pending": pf0 and next(iter(data.values()))["pending"],
        "horizons": horizon_entries(data),
        "windows": {sid: d["measurements"].get("windows", {}) for sid, d in sorted(data.items()) if "windows" in d["measurements"]},
        "shard_info": {sid: {k: d["measurements"].get(k) for k in ("n", "family", "K_max", "K_cap", "K_cx", "scope", "smoke_scope")}
                       for sid, d in sorted(data.items()) if sid not in ("controls", "tape")},
        "witnesses": witnesses,
    }
    os.makedirs(out, exist_ok=True)
    b = canonical(meas)
    if len(b) > SIZE_BUDGET:
        print("collect: REFUSED, measurements.json would be %d bytes" % len(b))
        return 2
    with open(os.path.join(out, "measurements.json"), "wb") as f:
        f.write(b)
    print("collect: %d shards complete, status %s" % (len(data), status))
    return 0


def _h(rec):
    return {k: rec.get(k) for k in ("K_zero", "K_zero_determined", "K_delta", "K_delta_determined", "K_cap", "all_exact")}


def horizon_entries(data):
    """The verdict inputs for §1-style horizon statements: per (shard, class, level, generator)."""
    out = []
    for sid, d in sorted(data.items()):
        m = d["measurements"]
        if "classes" not in m:
            continue
        tags = m.get("tags_input", {})
        for c in sorted(m["classes"]):
            if c == "U" and sid.endswith("-m3"):
                continue
            for g in sorted(m["classes"][c]):
                rec = m["classes"][c][g]
                e = dict(shard=sid, cls=c, level="K1", generator=g, n=m["n"], kind="curve", **_h(rec))
                e["tags"] = tags.get("K1", {}).get(c, {}).get(g, {})
                out.append(e)
        for c in sorted(m.get("k0", {})):
            rec = m["k0"][c]
            for form in ("worst", "average"):
                r = rec.get(form)
                if not r:
                    continue
                e = dict(shard=sid, cls=c, level="K0-" + form, generator="family", n=m["n"])
                if "lower" in r:
                    e.update(kind="interval", lower=_h(r["lower"]), upper=_h(r["upper"]),
                             exact_everywhere=all(unrle(r["exact"])))
                else:
                    e.update(kind="curve", **_h(r))
                e["tags"] = tags.get("K0", {}).get(c, {}).get(form, {})
                out.append(e)
            if rec.get("randomized"):
                rz = rec["randomized"]
                e = dict(shard=sid, cls=c, level="K0-randomized", generator="family", n=m["n"], kind="curve",
                         values=rz["values"], all_positive=rz["all_positive"], K_LP=rz["K_LP"])
                out.append(e)
    return out


def _vals(rec, key="values"):
    return [parse(x) for x in unrle(rec[key])]


def m3_inclusions(fam_meas, m3_meas):
    """MO across the family and m = 3 shards, pointwise on the common K range: passive m = 2 <= passive
    m = 3 and passive linear filters m = 3 <= passive m = 3 (distinguishing and prediction)."""
    res = []
    c3 = m3_meas["classes"]
    cf = fam_meas["classes"]
    for g in c3.get("emb_m3_passive", {}):
        for suf in ("", "_pred"):
            b = _vals(c3["emb_m3_passive" + suf][g])
            for c in ("emb_m2_passive" + suf, "plin_m3" + suf):
                if c in cf and g in cf[c]:
                    a = _vals(cf[c][g])
                    res.append(("%s <= emb_m3_passive%s on %s" % (c, suf, g), all(x <= y for x, y in zip(a, b))))
    return res


def nc2_specificity(n, lin, filt):
    """At every K where the records of both G_filt and G_lin are injective: U equal, and B2 at
    lambda = n+1 on G_filt <= that on G_lin, strictly smaller at some such K."""
    el = unrle(lin["entropy"]["G_lin"]["count_multisets"])
    ef = unrle(filt["entropy"]["G_filt"]["count_multisets"])
    M = 1 << (n + 1)
    ul = _vals(lin["classes"]["U"]["G_lin"])
    uf = _vals(filt["classes"]["U"]["G_filt"])
    bl = _vals(lin["classes"]["B2"]["G_lin"], "lambda_n_plus_1")
    bf = _vals(filt["classes"]["B2"]["G_filt"], "lambda_n_plus_1")
    ks = [K for K in range(len(el)) if el[K] == [[1, M]] and ef[K] == [[1, M]]]
    if not ks:
        return False, "no K with both records injective"
    eq = all(ul[K] == uf[K] for K in ks)
    le = all(bf[K] <= bl[K] for K in ks)
    lt = any(bf[K] < bl[K] for K in ks)
    return eq and le and lt, "n=%d: U equal %s, B2 <= %s, strict somewhere %s" % (n, eq, le, lt)
