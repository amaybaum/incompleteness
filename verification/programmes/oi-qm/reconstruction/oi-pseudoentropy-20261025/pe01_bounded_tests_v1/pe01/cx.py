"""CX: the counterexample conditions (a)-(f) of PLAN.md §6 item 4, evaluated from a witness record's
fields alone. Standard library only, so that verdict.py depends on nothing else.
"""
import copy
import re
from fractions import Fraction

PRIMARY = ("G_lin", "G_filt", "G_clk")
NS = range(3, 9)
DELTA_CX = Fraction(1, 8)
W = 3
RAT = re.compile(r"^(1-)?-?[0-9]+(/([0-9]+|2\^[0-9]+))?$")


def exact(s):
    if not isinstance(s, str) or not RAT.match(s):
        raise ValueError("EX3: non-exact value %r" % (s,))
    if s.startswith("1-"):
        return 1 - exact(s[2:])
    if "/2^" in s:
        a, e = s.split("/2^")
        return Fraction(int(a), 1 << int(e))
    return Fraction(s)


def _all_ge(vals, signed):
    try:
        return all((exact(a) if signed else abs(exact(a))) >= DELTA_CX for a in vals)
    except (ValueError, TypeError):
        return False          # a malformed value refuses (d); it never crashes the checker


def conditions(w, theta_by_n, controls_green, reading="abs"):
    """Return the list of failed conditions among (a)-(f); empty means all hold.

    reading (open item D-SIGN) selects condition (d): 'abs' reads adv_pred = |Pr - 1/2| >= 1/8 at
    every K' (the literal §2 definition); 'signed' requires the same chi to give Pr - 1/2 >= 1/8 at
    every K' (one orientation over the whole window)."""
    failed = []
    if not isinstance(w, dict):
        return ["a", "b", "c", "d", "e", "f"]
    n = w.get("n")
    # (a) phi is G_lin, G_filt or G_clk (the fixed G_x(p_n), open item WIT-A) with n in range, EX6
    if not (w.get("generator") in PRIMARY and n in NS and w.get("EX6") is True):
        failed.append("a")
    # (b) O in P^emb(m) as explicit tables with its readout clock; EX1, EX7, EX8, IM3
    o = w.get("observer") or {}
    tables = all(isinstance(o.get(k), list) for k in ("rho0", "rho1", "a", "chi"))
    clocked = isinstance(w.get("clock_bits"), int)
    if not (tables and clocked and all(w.get(k) is True for k in ("EX1", "EX7", "EX8", "IM3"))):
        failed.append("b")
    # (c) K <= K_cx
    K = w.get("K")
    if not (isinstance(K, int) and isinstance(w.get("K_cx"), int) and K <= w["K_cx"]):
        failed.append("c")
    # (d) the same O and chi give adv_pred >= 1/8 exactly at every K' in [K - 3, K], K >= 3
    win = w.get("window")
    key = "pred_minus_half" if reading == "signed" else "adv_pred"
    adv = w.get(key)
    ok_d = isinstance(K, int) and K >= W and win == list(range(K - W, K + 1)) and isinstance(adv, list) \
        and len(adv) == W + 1 and _all_ge(adv, reading == "signed")
    if not ok_d:
        failed.append("d")
    # (e) every control is green
    if controls_green is not True:
        failed.append("e")
    # (f) footprint (FP) <= theta
    th = theta_by_n.get(str(n)) if (n is not None and theta_by_n) else None
    if not (isinstance(w.get("footprint"), int) and th is not None and w["footprint"] <= th):
        failed.append("f")
    return failed


def classify(w, theta_by_n, controls_green, reading="abs"):
    f = conditions(w, theta_by_n, controls_green, reading)
    if not f:
        return "COUNTEREXAMPLE", f
    if f == ["f"]:
        return "unrestricted-footprint witness", f
    if f == ["c"]:
        return "recurrence-scale measurement", f
    return "measurement", f


def base_witness():
    """A synthetic record meeting (a)-(f), for the self-test only."""
    K = 31
    return {
        "generator": "G_filt", "n": 8, "subclass": "selftest", "m": 1,
        "observer": {"rho0": [0, 1], "rho1": [1, 0], "a": [0, 0], "chi": [0, 1]},
        "K": K, "window": list(range(K - W, K + 1)), "adv_pred": ["1/8", "3/16", "1/4", "1/8"],
        "pred_minus_half": ["1/8", "3/16", "1/4", "1/8"],
        "K_cx": 127, "footprint": 7, "clock_bits": 5, "EX6": True, "EX1": True, "EX7": True, "EX8": True,
        "IM3": True,
    }


def selftest(theta_by_n):
    """The three mutants of §5 (CX), under both readings of (d): each must be refused on exactly its
    own condition, and the base record accepted. Two more: a sign-alternating window is refused on
    (d) under the signed reading only, and a malformed value is refused on (d), not a crash."""
    out = {"base_accepted": {}, "mutants": {}}
    b = base_witness()
    K = b["K"]
    low = Fraction(1, 8) - Fraction(1, 1 << (K + 2))
    for rd in ("abs", "signed"):
        out["base_accepted"][rd] = conditions(b, theta_by_n, True, rd) == []
        m1 = copy.deepcopy(b)
        m1["adv_pred"][2] = m1["pred_minus_half"][2] = "%d/%d" % (low.numerator, low.denominator)
        m2 = copy.deepcopy(b)
        m2["footprint"] = theta_by_n[str(b["n"])] + 1
        m3 = copy.deepcopy(b)
        m3["K"] = b["K_cx"] + 1
        m3["window"] = list(range(m3["K"] - W, m3["K"] + 1))
        m4 = copy.deepcopy(b)
        m4["pred_minus_half"][1] = "-3/16"           # |.| unchanged: alternates in sign
        m5 = copy.deepcopy(b)
        m5["adv_pred"][0] = m5["pred_minus_half"][0] = "0.125"
        cases = [("window value 1/8 - 2^(-K-2)", m1, ["d"]), ("footprint theta+1", m2, ["f"]),
                 ("K = K_cx + 1", m3, ["c"]), ("sign-alternating window", m4, ["d"] if rd == "signed" else []),
                 ("malformed value", m5, ["d"])]
        for name, mw, want in cases:
            got = conditions(mw, theta_by_n, True, rd)
            out["mutants"]["%s [%s]" % (name, rd)] = {"refused_on": got, "expected": want, "pass": got == want,
                                                      "reported_as": classify(mw, theta_by_n, True, rd)[0]}
    out["pass"] = all(out["base_accepted"].values()) and all(v["pass"] for v in out["mutants"].values())
    return out
