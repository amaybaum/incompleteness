"""PE-01 verdict, generated from the measurement JSON alone (PLAN.md §6).

  python3 -I -B verdict.py MEASUREMENTS.json --out DIR      writes DIR/verdict.json and DIR/verdict.txt
  python3 -I -B verdict.py MEASUREMENTS.json --check        regenerates and runs the VG self-test only

Every number in the text is read from the measurements. VOID takes precedence: if an evaluated
checkpoint failed, the text names the failed checkpoints and prints nothing else. If a checkpoint
or a primary shard was not evaluated, the text is INCOMPLETE (no verdict) and names what is
missing. Horizons are printed from the shards' exactness and determined flags: only statements
whose values are exact and whose horizons are determined stand under PROVED (exhaustive finite);
bounds and intervals are printed as such. The VG self-test regenerates the verdict and compares,
flips each passing control flag in a copy (each must yield VOID naming it), and requires the text
check to fail on a text without the resource-model limitation sentence.

Where amendment A2 fixes the reading of condition (d) (D-SIGN), sections 1-4 and the verdict class
are computed under that reading alone, and the other reading is printed after them as a
sensitivity analysis (section 5) that does not govern. The VG self-test then also requires that
removing or changing every sensitivity row, and adding a synthetic sensitivity COUNTEREXAMPLE,
leave the governing class and the governing text byte-identical.
"""
import copy
import hashlib
import json
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pe01 import cx  # noqa: E402  (standard library only)

CORE = "is a consequence of the selected resource model: memory + clock + output <= theta. It is not a limit OI imposes on observers."
D8, D4 = Fraction(1, 8), Fraction(1, 4)
SCOPE = {
    "emb_m1_all": "all 16 observers with m = 1, every F",
    "emb_m1_passive": "the 4 passive observers with m = 1, every F",
    "emb_m2_all": "all 9216 observers with m = 2, every F",
    "emb_m2_passive": "the 576 passive observers with m = 2, every F",
    "emb_m3_passive": "passive observers with m = 3 up to simultaneous conjugacy fixing v_0 (306432 canonical forms)",
}
for _m in (1, 2, 3, 4):
    SCOPE["plin_m%d" % _m] = "passive linear filters with m = %d (a = 0; every (A, b) through its class)" % _m


def limitation(theta_by_n):
    """The §7 limitation sentence for the theta the measurements record."""
    if not theta_by_n:
        return "The horizon bound K < 2^(theta-m-1) (theta not recorded) " + CORE
    off = {int(n) - v for n, v in theta_by_n.items()}
    if off == {-1}:
        return "The horizon bound K < 2^(n-m) (theta = n+1) " + CORE
    if off == {0}:
        return "The horizon bound K < 2^(n-m-1) (theta = n) " + CORE
    return "The horizon bound K < 2^(theta-m-1) (theta by n: %s) %s" % (theta_by_n, CORE)


def check_exact_tree(obj, path="$"):
    if isinstance(obj, float):
        raise ValueError("EX3: float at %s" % path)
    if isinstance(obj, dict):
        for k, v in obj.items():
            if not (isinstance(k, str) and k.startswith("display_")):
                check_exact_tree(v, path + "." + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            check_exact_tree(v, "%s[%d]" % (path, i))


def check_text(text):
    """A verdict text that is neither VOID nor INCOMPLETE must carry the limitation sentence."""
    if text.startswith("VOID") or text.startswith("INCOMPLETE"):
        return True
    return CORE in text and "The horizon bound K < 2^(" in text


def void_names(text):
    head = "VOID: failed checkpoint(s):"
    if not text.startswith(head):
        return []
    return [x.strip() for x in text[len(head):].strip().split(",") if x.strip()]


def h_text(e):
    """Horizon statement from a curve entry's values-derived fields and determined flags."""
    cap = e["K_cap"]
    zs = ("K_zero = %d" % e["K_zero"]) if e["K_zero_determined"] else ("K_zero >= %d (not determined beyond)" % e["K_zero"])
    parts = [zs]
    for d in ("1/8", "1/4"):
        kd, det = e["K_delta"][d], e["K_delta_determined"][d]
        if det:
            parts.append("K_%s = %s" % (d, kd) if kd is not None else "K_%s = null (adv < %s at every K <= %d)" % (d, d, cap))
        else:
            parts.append("K_%s <= %d" % (d, kd) if kd is not None else "K_%s undetermined (no certified value >= %s in K <= %d)" % (d, d, cap))
    return ", ".join(parts) + " (scope K <= %d)" % cap


def interval_text(e):
    lo, hi = e["lower"], e["upper"]
    z = "K_zero in [%d, %d]" % (hi["K_zero"], lo["K_zero"])
    out = [z]
    for d in ("1/8", "1/4"):
        a, b = hi["K_delta"][d], lo["K_delta"][d]
        out.append("K_%s in [%s, %s]" % (d, a if a is not None else "> %d" % hi["K_cap"], b if b is not None else "null"))
    return ", ".join(out) + " (scope K <= %d)" % lo["K_cap"]


def horizons_of(values):
    vals = [cx.exact(v) for v in values]
    kz = -1
    for K, v in enumerate(vals):
        if v == 0:
            kz = K
        else:
            break
    kd = {nm: next((K for K, v in enumerate(vals) if v >= d), None) for d, nm in ((D8, "1/8"), (D4, "1/4"))}
    return kz, kd, len(vals) - 1


def unrle(runs):
    out = []
    for x, c in runs:
        out.extend([x] * c)
    return out


def tag(e):
    """Productivity tag (§6 item 5; open item TAG-L), COVERED-corpus first. candidate-NEW is never
    assigned here: it needs the §9 literature check."""
    t = e.get("tags", {})
    c = e["cls"]
    if c in ("U", "U_bayes"):
        return "COVERED-corpus (support bound, Structure.md:1256)"
    if t.get("L3_corpus"):
        return "COVERED-corpus (B4 at or beyond its counting horizon)"
    if t.get("L1"):
        return "COVERED-literature (L1: B1 fires on G_lin at K = n+1)"
    if t.get("L2"):
        return "COVERED-literature (L2: Berlekamp-Massey / Gustavson-Rueppel closed form at lambda = n+1)"
    if t.get("L4"):
        return "COVERED-literature (L4: the NC-1 value max(0, 1 - 2^(n-K)))"
    if e.get("generator") == "G_dec":
        return "control generator"
    return "untagged: eligible for candidate-NEW review only after the §9 literature check"


def region_cell(meas, gname, n, m):
    reg = (meas.get("AR") or {}).get("region", {}).get("n+1", {})
    row = reg.get(str(n))
    if not row or m > 4:
        return None, False
    col = ("G_lin", "G_filt", "G_clk").index(gname)
    return row[m - 1][col], True


READINGS = ("abs", "signed")
VALUE_FIELD = {"abs": "adv_pred", "signed": "pred_minus_half"}
VALUE_LABEL = {"abs": "|Pr - 1/2|", "signed": "Pr - 1/2"}
SENS_HEAD = "5. Sensitivity analysis (does not govern): condition (d) under the %s reading."


def other_reading(rd):
    return [r for r in READINGS if r != rd][0]


def witness_lines(meas, th, green, readings, tagged):
    """Section 2 rows for the given readings of (d), and the witnesses meeting (a)-(f) under them.

    Each reading reads only its own rows: its window rows, the candidates selected under it
    (found_under), and the reading-keyed fields of those candidates. A candidate selected only
    under another reading never enters this reading's rows or its COUNTEREXAMPLE list."""
    L, counter = [], []
    for sid, info in sorted(meas["shard_info"].items()):
        if sid not in meas["windows"]:
            continue
        gname = {"lin": "G_lin", "filt": "G_filt", "clk": "G_clk"}[info["family"]]
        n = info["n"]
        for sub, byrd in sorted(meas["windows"][sid].items()):
            m = int(sub.split("_m")[1][0])
            cell, known = region_cell(meas, gname, n, m)
            cell_s = ("admissible region cell (theta = n+1): [%d, %d]" % tuple(cell)) if cell else \
                "admissible region cell (theta = n+1) empty: 'no admissible witness' here is a fact about the resource model"
            for rd in readings:
                ws = [w for w in meas["witnesses"] if w["shard"] == sid and w["subclass"] == sub
                      and rd in w.get("found_under", [])]
                rows = [r for r in byrd.get(rd, []) if r[1]]
                tagr = (" [reading %s]" % rd) if tagged else ""
                scope_s = "%s; K <= %s" % (SCOPE.get(sub, sub), info.get("K_max") or info.get("K_cap"))
                if not rows:
                    L.append("  %s n=%d %s%s: no witness within the enumerated scope at any footprint (%s). %s." % (
                        gname, n, sub, tagr, scope_s, cell_s))
                    continue
                fam_rows = [r for r in rows if r[2]]
                L.append("  %s n=%d %s%s: windows at %d K values (first K = %d); family-wide windows at %d K values. %s." % (
                    gname, n, sub, tagr, len(rows), rows[0][0], len(fam_rows), cell_s))
                kinds = []
                byK = {}
                for w in sorted(ws, key=lambda x: x["K"]):
                    byK.setdefault(w["K"], []).append(w)
                for K in sorted(byK):
                    # one line per K: a COUNTEREXAMPLE if one is among the candidates, else the first;
                    # every candidate at K enters the COUNTEREXAMPLE test and the attribution
                    graded = [(w,) + cx.classify(w, th, green, rd) for w in byK[K]]
                    for w, kind, fails in graded:
                        if "d" not in fails:
                            kinds.append(kind)
                        if kind == "COUNTEREXAMPLE":
                            counter.append((rd, w))
                    w, kind, fails = next((g for g in graded if g[1] == "COUNTEREXAMPLE"), graded[0])
                    L.append("    K=%d: %s (failed: %s); selected under reading %s; %s at K'=%s: %s; footprint %d "
                             "(theta %d); table size %d bits; K_cx=%d; K0 status: %s; windows in subclass at K: %s, "
                             "family-wide: %s; %s." % (
                                 w["K"], kind, ",".join(fails) or "none", rd, VALUE_LABEL[rd],
                                 w["window"], ", ".join(w[VALUE_FIELD[rd]]), w["footprint"], th[str(n)],
                                 w["table_size_bits"], w["K_cx"],
                                 "witness on every phi of the family" if w["K0_status"][rd] else "not family-wide",
                                 w["window_count_in_subclass"][rd], w["family_window_count"][rd], w["realization"]))
                if "COUNTEREXAMPLE" not in kinds:
                    if "unrestricted-footprint witness" in kinds:
                        L.append("    Attribution%s: unpredictability in this combination is attributed to resources; "
                                 "a limitation of the resource model (§7)." % tagr)
                    else:
                        L.append("    Attribution%s: no witness meeting (a)-(f) within the enumerated scope at any footprint." % tagr)
    return L, counter


def sensitivity_lines(meas, th, green, rd):
    """The sensitivity section: (d) under the non-governing reading. Its rows and its classification
    are printed after the governing text and never enter the stage outcome or the verdict class."""
    L = ["", SENS_HEAD % rd,
         "   Printed as A2 requires; the governing verdict above is computed without any row of this section."]
    wl, counter = witness_lines(meas, th, green, [rd], tagged=False)
    L.extend(wl)
    L.append("   Sensitivity classification: %s under %s." % (
        "COUNTEREXAMPLE (%d witness(es) meeting (a)-(f))" % len(counter) if counter else "no COUNTEREXAMPLE", rd))
    return L


def governing_part(text):
    """The text before the sensitivity section."""
    i = text.find("\n" + SENS_HEAD.split(":")[0])
    return text if i < 0 else text[:i + 1]


def generate(meas):
    """Return (verdict_class, text)."""
    check_exact_tree(meas)
    ctl = meas["controls"]
    scope = meas["control_scope"]
    failed = sorted(k for k in scope if ctl[k]["pass"] is False)
    if failed:
        return "VOID", "VOID: failed checkpoint(s): %s\n" % ", ".join(failed)
    unev = sorted(set(meas.get("unevaluated", [])) | {"checkpoint %s" % k for k in scope if ctl[k]["pass"] is not True})
    if unev:
        return "INCOMPLETE", "INCOMPLETE (no verdict): not evaluated: %s\n" % "; ".join(unev)
    mode = meas["mode"]
    th = meas["theta_by_n"]
    res = (meas.get("a2") or {}).get("resolutions", {})
    sign_rule = res.get("D-SIGN")
    L = []
    if mode == "smoke":
        L.append("SMOKE OUTPUT: NOT A RESULT. Local smoke scope only; checkpoints outside it were not evaluated.")
    if mode == "test":
        L.append("TEST OUTPUT: NOT A RESULT. Result scope under an unpinned local A2 stub.")
    L.append("PE-01 verdict, generated by verdict.py from measurements.json. Every number below is read from it.")
    L.append("Run %s; commit %s; PLAN.md blob %s; A1 blob %s; A2: %s." % (
        meas["run"]["run_id"], meas["commit"], meas["plan_blob"], meas["a1_blob"],
        ("blob %s, %s" % (meas["a2"]["a2_blob"], meas["a2"].get("source"))) if res else "none"))
    L.append("theta by n: %s. K_LP(n): %s. Passive m = 3 scope: option (%s), caps %s." % (
        th, meas["K_LP_by_n"], meas["m3_passive_scope"], meas["m3_passive_K_cap"]))
    L.append("Readings of the open items: %s." % (", ".join("%s = %s" % kv for kv in sorted(res.items())) if res
                                                   else "none fixed; each computed reading is printed"))
    if sign_rule in READINGS:
        L.append("Governing rule for condition (d): %s (A2). Sensitivity: %s." % (sign_rule, other_reading(sign_rule)))
    L.append("Checkpoints green: %s." % ", ".join("%s(%d)" % (k, ctl[k]["checks"]) for k in scope))
    nd = {k: v["status"] for k, v in meas["shards"].items() if v["status"] != "complete"}
    if nd:
        L.append("Shards not complete (their cells carry no verdict): %s." % ", ".join("%s: %s" % kv for kv in sorted(nd.items())))
    L.append("")
    proved, bounds = [], []
    for e in meas["horizons"]:
        head = "  [%s] %s %s on %s, n=%s: " % (e["shard"], e["cls"], e["level"], e["generator"], e["n"])
        if e["kind"] == "interval":
            line = head + "interval; " + interval_text(e)
            if e.get("exact_everywhere"):
                proved.append(line + ". Tag: " + tag(e) + ".")
            else:
                bounds.append(line + ". Tag: " + tag(e) + ".")
            continue
        if e["level"] == "K0-randomized":
            kz, kd, cap = horizons_of(unrle(e["values"]))
            kza, kda, _ = horizons_of(unrle(e["all_positive"]))
            proved.append(head + "exact LP, K <= K_LP = %d: K_zero = %d, K_1/8 = %s, K_1/4 = %s; all-positive pattern: K_zero = %d, K_1/8 = %s." % (
                e["K_LP"], kz, kd["1/8"], kd["1/4"], kza, kda["1/8"]))
            continue
        determined = e["K_zero_determined"] and all(e["K_delta_determined"].values())
        note = ""
        if e["level"] == "K0-worst" and e["cls"].startswith("emb_m") and "m3" not in e["cls"]:
            note = " (deterministic tests: a lower bound on the randomized worst case)"
        line = head + h_text(e) + note + ". Tag: " + tag(e) + "."
        (proved if (e["all_exact"] and determined) else bounds).append(line)
    L.append("1. Horizons. PROVED (exhaustive finite): each statement quantifies only over the named class, "
             "knowledge level, generator, n and the stated K scope. Embedded distinguishing curves (optimal F) "
             "are measurements bearing on the second clause of book/ch18-beyond.md:114; they are not COUNTEREXAMPLEs.")
    L.extend(proved)
    L.append("")
    L.append("1b. Bounds and intervals (not PROVED): values here are certified lower bounds, or intervals "
             "exact only where their ends coincide; the horizons are bounds and bear on no verdict.")
    L.extend(bounds)
    # ---- witnesses
    L.append("")
    green = meas["status"] == "green" and mode == "result"
    if sign_rule in READINGS:
        L.append("2. Prediction witnesses (§6 item 4), per (generator, n, observer subclass); never pooled. "
                 "Condition (d) is read under the governing rule %s; only the candidates selected under it enter "
                 "this section and the stage outcome." % sign_rule)
        wl, counter = witness_lines(meas, th, green, [sign_rule], tagged=False)
    else:
        L.append("2. Prediction witnesses (§6 item 4), per (generator, n, observer subclass); never pooled.")
        L.append("   Condition (d) is printed under both readings (open item D-SIGN): 'signed' = the same chi "
                 "gives Pr - 1/2 >= 1/8 at every K'; 'abs' = |Pr - 1/2| >= 1/8 at every K'.")
        wl, counter = witness_lines(meas, th, green, list(READINGS), tagged=True)
    L.append("   Condition (a) is read as the fixed G_lin(p_n), G_filt(p_n), G_clk(p_n); other family members "
             "enter through the K0 status only, which is conservative toward the claim under audit.")
    L.extend(wl)
    # ---- limitation and region
    L.append("")
    L.append("3. " + limitation(th))
    ar = meas.get("AR") or {}
    reg = ar.get("region", {}).get("n+1", {})
    L.append("   Admissible region for theta = n+1, recomputed from the measured Z(phi) and K_cx(phi) "
             "(cells G_lin | G_filt | G_clk; '-' empty):")
    for n in sorted(reg, key=int):
        cells = []
        for m, row in enumerate(reg[n], start=1):
            cells.append("m=%d: %s" % (m, " | ".join("-" if c is None else "[%d,%d]" % tuple(c) for c in row)))
        L.append("     n=%s  %s" % (n, "; ".join(cells)))
    L.append("   Z(phi): %s; l_med(phi): %s; K_cx(phi): %s." % (ar.get("Z"), ar.get("l_med"), ar.get("K_cx")))
    bind = all(c is None or c[1] < ar["K_cx"][g][int(n) - 3]
               for n, rows in reg.items() for row in rows for c, g in zip(row, ("G_lin", "G_filt", "G_clk"))) if reg else None
    if bind:
        L.append("   In every non-empty cell the footprint bound lies below K_cx, so (f) implies (c) at theta = n+1.")
    L.append("   The fixed clock charge can overcharge an observer whose memory already keeps time, so (f) is "
             "conservative toward the claim under audit.")
    L.append("")
    if counter:
        L.append("4. Stage outcome: COUNTEREXAMPLE to the universal form of book/ch18-beyond.md:114 under reading %s of "
                 "(d), by %d witness(es) meeting (a)-(f). It refutes only the universal form; it says nothing about the "
                 "realization of the actual world, nor about the 10^-32 statement." % (
                     ",".join(sorted({rd for rd, _ in counter})), len(counter)))
    else:
        L.append("4. Stage outcome: no COUNTEREXAMPLE within the enumerated scope. COVERED findings are tagged above; "
                 "bounded theorems need a written proof under independent review. Otherwise OPEN.")
    L.append("   No finite result here establishes the universal form. No asymptotic, circuit-security, "
             "cryptographic-security or quantum-reproduction claim is made.")
    cls = mode.upper() if mode != "result" else ("COUNTEREXAMPLE" if counter else "NO-COUNTEREXAMPLE")
    if sign_rule in READINGS:
        L.extend(sensitivity_lines(meas, th, green, other_reading(sign_rule)))
    return cls, "\n".join(L) + "\n"


def strip_sensitivity(meas, gov):
    """A copy with every sensitivity row removed: the other reading's window rows, the candidates
    selected only under it, and its keyed fields and value list on every remaining candidate."""
    o = other_reading(gov)
    m = copy.deepcopy(meas)
    for cells in m["windows"].values():
        for byrd in cells.values():
            byrd.pop(o, None)
    kept = []
    for w in m["witnesses"]:
        if gov not in w.get("found_under", []):
            continue
        w["found_under"] = [gov]
        for k in ("K0_status", "window_count_in_subclass", "family_window_count"):
            if isinstance(w.get(k), dict):
                w[k].pop(o, None)
        w.pop(VALUE_FIELD[o], None)
        kept.append(w)
    m["witnesses"] = kept
    return m


def flip_sensitivity(meas, gov, favorable):
    """A copy with every sensitivity row changed: window counts toggled, keyed fields inverted, and
    each candidate selected only under the other reading made to meet (favorable) or fail every
    value condition."""
    o = other_reading(gov)
    m = copy.deepcopy(meas)
    for cells in m["windows"].values():
        for byrd in cells.values():
            for r in byrd.get(o, []):
                r[1] = 0 if r[1] else 1
                r[2] = 0 if r[2] else 1
    vals = ["1/4"] * (cx.W + 1) if favorable else ["0"] * (cx.W + 1)
    for w in m["witnesses"]:
        for k in ("K0_status",):
            if isinstance(w.get(k), dict) and o in w[k]:
                w[k][o] = not w[k][o]
        for k in ("window_count_in_subclass", "family_window_count"):
            if isinstance(w.get(k), dict) and o in w[k]:
                w[k][o] = w[k][o] + 1
        w[VALUE_FIELD[o]] = list(vals)
        if gov not in w.get("found_under", []):
            w[VALUE_FIELD[gov]] = list(vals)
            w["footprint"] = 0 if favorable else 1 << 20
    return m


def forge_green(meas):
    """A copy read as a green result, so that (e) can hold and a COUNTEREXAMPLE can be printed."""
    m = copy.deepcopy(meas)
    m["mode"], m["status"] = "result", "green"
    return m


def inject_sensitivity_witness(meas, gov):
    """A copy carrying one synthetic candidate selected only under the other reading, meeting
    (a)-(f) under both readings, with its window row. The cell is one the governing reading also
    has window rows in where there is one, so that a governing section reading this candidate
    would print it. None if no cell admits one."""
    o = other_reading(gov)
    m = copy.deepcopy(meas)
    cells = [(not any(r[1] for r in m["windows"][sid][sub].get(gov, [])), sid, sub)
             for sid, info in sorted(m["shard_info"].items()) if sid in m["windows"]
             and isinstance(info.get("K_cx"), int) and info["K_cx"] >= cx.W
             and str(info.get("n")) in (m.get("theta_by_n") or {}) for sub in sorted(m["windows"][sid])]
    for _, sid, sub in sorted(cells):
        info = m["shard_info"][sid]
        K = info["K_cx"]
        w = cx.base_witness()
        w.update({"generator": {"lin": "G_lin", "filt": "G_filt", "clk": "G_clk"}[info["family"]], "n": info["n"],
                  "shard": sid, "subclass": sub, "m": int(sub.split("_m")[1][0]), "K": K,
                  "window": list(range(K - cx.W, K + 1)), "K_cx": K, "footprint": 0,
                  "adv_pred": ["1/4"] * (cx.W + 1), "pred_minus_half": ["1/4"] * (cx.W + 1), "found_under": [o],
                  "K0_status": {o: True}, "window_count_in_subclass": {o: 1}, "family_window_count": {o: 1},
                  "table_size_bits": 0, "realization": "synthetic record (VG only)"})
        m["witnesses"] = list(m["witnesses"]) + [w]
        m["windows"][sid][sub].setdefault(o, []).append([K, 1, 1])
        return m
    return None


def _governing(m):
    """(class, governing text) of a copy; a generation error is recorded, never raised."""
    try:
        c, t = generate(m)
        return c, governing_part(t), t
    except Exception as e:      # noqa: BLE001  (a self-test case fails; it does not crash the verdict)
        return "ERROR %s: %s" % (type(e).__name__, e), None, ""


def sensitivity_selftest(meas, text):
    """The governing class and text must not read any sensitivity row: removing or changing every
    row, on the measurements and on a copy read as a green result, leaves both byte-identical; a
    synthetic candidate meeting (a)-(f), selected only under the sensitivity reading, is printed as a
    COUNTEREXAMPLE in the sensitivity section and changes neither."""
    gov = (meas.get("a2") or {}).get("resolutions", {}).get("D-SIGN")
    if gov not in READINGS:
        return {"applicable": False, "pass": True}
    cls0, _ = generate(meas)
    if cls0 in ("VOID", "INCOMPLETE"):
        # no governing section is printed, so there is nothing for a sensitivity row to reach
        return {"applicable": False, "reason": "class %s prints no witness section" % cls0, "pass": True}
    out = {"applicable": True, "section_present": text.count(SENS_HEAD % other_reading(gov)) == 1
           and governing_part(text) != text, "unchanged": {}}
    fg = forge_green(meas)
    base = {"measured": (cls0, governing_part(text)), "green-copy": _governing(fg)[:2]}
    for src_name, src in (("measured", meas), ("green-copy", fg)):
        for vname, var in (("removed", strip_sensitivity(src, gov)),
                           ("flipped-favorable", flip_sensitivity(src, gov, True)),
                           ("flipped-unfavorable", flip_sensitivity(src, gov, False))):
            out["unchanged"]["%s/%s" % (src_name, vname)] = _governing(var)[:2] == base[src_name]
    inj = inject_sensitivity_witness(fg, gov)
    if inj is None:
        out["injected"] = {"available": False}
    else:
        c, g, t = _governing(inj)
        sens = t[len(g or ""):].split("\n")
        out["injected"] = {"available": True, "governing_unchanged": (c, g) == base["green-copy"],
                           "detected_in_sensitivity": g is not None and len(sens) > 1 and "COUNTEREXAMPLE (" in sens[-2]}
    out["pass"] = (out["section_present"] and all(out["unchanged"].values()) and out["injected"].get("available") is True
                   and out["injected"]["governing_unchanged"] and out["injected"]["detected_in_sensitivity"])
    return out


def vg_selftest(meas, text):
    out = {"regenerated_identical": generate(meas)[1] == text, "flips": {}, "text_check": {}}
    for k in meas["control_scope"]:
        if meas["controls"][k]["pass"] is not True:
            continue
        m2 = copy.deepcopy(meas)
        m2["controls"][k]["pass"] = False
        cls, t2 = generate(m2)
        out["flips"][k] = cls == "VOID" and k in void_names(t2)
    probe = "PE-01 verdict (probe).\n3. " + limitation(meas["theta_by_n"]) + "\n"
    out["text_check"]["accepts_generated"] = check_text(text) and check_text(probe)
    out["text_check"]["rejects_without_sentence"] = not check_text(probe.replace(CORE, ""))
    out["sensitivity"] = sensitivity_selftest(meas, text)
    out["pass"] = (out["regenerated_identical"] and all(out["flips"].values())
                   and out["text_check"]["accepts_generated"] and out["text_check"]["rejects_without_sentence"]
                   and out["sensitivity"]["pass"])
    return out


def main(argv):
    src = argv[0]
    out = argv[argv.index("--out") + 1] if "--out" in argv else None
    raw = open(src, "rb").read()
    meas = json.loads(raw)
    try:
        cls, text = generate(meas)
        vg = vg_selftest(meas, text)
        if not vg["pass"]:
            prev = void_names(text) if cls == "VOID" else []
            cls, text = "VOID", "VOID: failed checkpoint(s): %s\n" % ", ".join(prev + ["VG"])
    except Exception as e:      # the verdict is never silently missing
        cls, vg = "INCOMPLETE", {"pass": False, "error": "%s: %s" % (type(e).__name__, e)}
        text = "INCOMPLETE (no verdict): verdict generation failed: %s: %s\n" % (type(e).__name__, e)
    if "--check" in argv:
        print(json.dumps({"class": cls, "VG": vg}, indent=1, sort_keys=True))
        return 0 if vg.get("pass") else 1
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "verdict.json"), "w") as f:
        json.dump({"class": cls, "text": text, "VG": vg, "measurements_sha256": hashlib.sha256(raw).hexdigest(),
                   "measurements_commit": meas.get("commit"), "run": meas.get("run")}, f, sort_keys=True, indent=1)
        f.write("\n")
    with open(os.path.join(out, "verdict.txt"), "w") as f:
        f.write(text)
    print(cls)
    return 1 if "error" in vg else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
