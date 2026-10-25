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
RAT = re.compile(r"^-?[0-9]+(/([0-9]+|2\^[0-9]+))?$")


def exact(s):
    if not isinstance(s, str) or not RAT.match(s):
        raise ValueError("EX3: non-exact value %r" % (s,))
    if "/2^" in s:
        a, e = s.split("/2^")
        return Fraction(int(a), 1 << int(e))
    return Fraction(s)


def conditions(w, theta_by_n, controls_green):
    """Return the list of failed conditions among (a)-(f); empty means all hold."""
    failed = []
    n = w.get("n")
    # (a) phi is G_lin, G_filt or G_clk with n in range, and passes EX6
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
    adv = w.get("adv_pred")
    ok_d = isinstance(K, int) and K >= W and win == list(range(K - W, K + 1)) and isinstance(adv, list) \
        and len(adv) == W + 1 and all(exact(a) >= DELTA_CX for a in adv)
    if not ok_d:
        failed.append("d")
    # (e) every control is green
    if controls_green is not True:
        failed.append("e")
    # (f) footprint (FP) <= theta
    th = theta_by_n.get(str(n)) if n is not None else None
    if not (isinstance(w.get("footprint"), int) and th is not None and w["footprint"] <= th):
        failed.append("f")
    return failed


def classify(w, theta_by_n, controls_green):
    f = conditions(w, theta_by_n, controls_green)
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
        "K_cx": 127, "footprint": 7, "clock_bits": 5, "EX6": True, "EX1": True, "EX7": True, "EX8": True,
        "IM3": True,
    }


def selftest(theta_by_n):
    """The three mutants of §5 (CX): each must be refused, on its own condition only."""
    out = {"base_accepted": False, "mutants": {}}
    b = base_witness()
    out["base_accepted"] = conditions(b, theta_by_n, True) == []
    K = b["K"]
    m1 = copy.deepcopy(b)
    m1["adv_pred"][2] = "%d/%d" % ((Fraction(1, 8) - Fraction(1, 1 << (K + 2))).numerator,
                                   (Fraction(1, 8) - Fraction(1, 1 << (K + 2))).denominator)
    m2 = copy.deepcopy(b)
    m2["footprint"] = theta_by_n[str(b["n"])] + 1
    m3 = copy.deepcopy(b)
    m3["K"] = b["K_cx"] + 1
    m3["window"] = list(range(m3["K"] - W, m3["K"] + 1))
    for name, mw, want in (("window value 1/8 - 2^(-K-2)", m1, ["d"]), ("footprint theta+1", m2, ["f"]),
                           ("K = K_cx + 1", m3, ["c"])):
        got = conditions(mw, theta_by_n, True)
        out["mutants"][name] = {"refused_on": got, "expected": want, "pass": got == want,
                                "reported_as": classify(mw, theta_by_n, True)[0]}
    out["pass"] = out["base_accepted"] and all(v["pass"] for v in out["mutants"].values())
    return out
