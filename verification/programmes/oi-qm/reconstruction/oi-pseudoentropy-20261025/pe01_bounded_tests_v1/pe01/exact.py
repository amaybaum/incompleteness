"""Exact values and their serialization (EX3).

Every number on the verdict path is a Python int or a fractions.Fraction. In JSON an exact value
is a string "p/q" or "p" (never a JSON float). Floats appear only under keys named "display_*",
which no verdict code reads.
"""
import json
import re
from fractions import Fraction

import numpy as np

RAT = re.compile(r"^-?[0-9]+(/([0-9]+|2\^[0-9]+))?$")


class ExactnessError(AssertionError):
    pass


def ex3(v, where=""):
    """EX3: the type assertion on a verdict input. Returns v."""
    if isinstance(v, bool) or not isinstance(v, (int, Fraction)):
        raise ExactnessError("EX3: non-exact verdict input at %s: %r (%s)" % (where, v, type(v).__name__))
    return v


def q(v, where=""):
    """Serialize an exact number."""
    if isinstance(v, (np.integer,)):
        v = int(v)
    ex3(v, where)
    if isinstance(v, Fraction):
        d = v.denominator
        if d == 1:
            return str(v.numerator)
        if d > 65536 and d & (d - 1) == 0:
            return "%d/2^%d" % (v.numerator, d.bit_length() - 1)
        return "%d/%d" % (v.numerator, d)
    return str(v)


def parse(s, where=""):
    """Parse an exact number serialized by q(); refuses anything else (EX3 on the read side)."""
    if not isinstance(s, str) or not RAT.match(s):
        raise ExactnessError("EX3: non-exact serialized value at %s: %r" % (where, s))
    if "/2^" in s:
        a, e = s.split("/2^")
        return Fraction(int(a), 1 << int(e))
    return Fraction(s)


def walk_display_free(obj, path="$"):
    """EX3 on a whole JSON tree: no float anywhere outside keys starting with 'display_'."""
    if isinstance(obj, float):
        raise ExactnessError("EX3: float at %s" % path)
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(k, str) and k.startswith("display_"):
                continue
            walk_display_free(v, path + "." + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk_display_free(v, "%s[%d]" % (path, i))


def canonical(obj):
    """Canonical JSON bytes: sorted keys, fixed separators, trailing newline (RP compares these)."""
    walk_display_free(obj)
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode()


def frac_from_counts(num, den):
    return Fraction(int(num), int(den))


def horizons(curve, deltas, exact_flags=None):
    """K_zero and K_delta from an exact curve {K: value} over a contiguous K range starting at 0.

    K_zero: largest K with adv = 0 exactly at every K' <= K (-1 if adv(0) != 0).
    K_delta: least K with adv >= delta, or None (reported with the scope K <= K_cap).
    exact_flags (optional) marks values that are only lower bounds; a lower bound >= delta still
    certifies adv >= delta, but a lower bound below delta leaves K_delta undetermined, and a lower
    bound equal to 0 leaves K_zero undetermined from that K on.
    """
    Ks = sorted(curve)
    assert Ks == list(range(Ks[0], Ks[-1] + 1)) and Ks[0] == 0, "curve must be contiguous from 0"
    kzero = -1
    kzero_exact = True
    for K in Ks:
        v = curve[K]
        ex3(v, "curve")
        isx = exact_flags is None or exact_flags[K]
        if v == 0 and isx:
            kzero = K
            continue
        if v == 0 and not isx:
            kzero_exact = False
        break
    out = {"K_zero": kzero, "K_zero_determined": kzero_exact, "K_cap": Ks[-1]}
    for d in deltas:
        kd = None
        determined = True
        for K in Ks:
            v = curve[K]
            isx = exact_flags is None or exact_flags[K]
            if v >= d:
                kd = K
                break
            if not isx:
                determined = False
        out["K_delta[%s]" % q(d)] = kd
        out["K_delta_determined[%s]" % q(d)] = determined
    return out
