"""Write every arithmetic claim the LOC-1 arithmetic controls certify, for the independent check (research development).

The claims are captured from the controls themselves, not regenerated: s16_layer.self_test() is run unchanged with
recording wrappers around the module-level names it calls (load_engine, planted, run, brute_classes), so each
instance, each engine result and each brute-force class set recorded is the one K-arith-16 saw.  The field and place
claims of cyclo16.py, and the replay arithmetic of replay_cyclo16.py, are recorded on seeded elements.

The output is read by indep_arith_check.py, which imports nothing from this directory.  No target object is
evaluated: every instance is synthetic.

Run:  python3 -I -B emit_claims.py OUT.json [--full]
"""
import json
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cyclo16  # noqa: E402
import replay_cyclo16  # noqa: E402
import s16_layer  # noqa: E402
from cyclo16 import ODD, PLACE, Q16, SM64, galois, norm, rand_elem, trace  # noqa: E402


def enc(x):
    """An entry as its 8 power-basis coordinates, written as strings."""
    if isinstance(x, Q16):
        return x.to_json()
    if isinstance(x, (int, Fraction)) and not isinstance(x, bool):
        return [str(Fraction(x))] + ["0"] * 7
    raise TypeError(type(x))


def encm(mats):
    return [[[enc(x) for x in row] for row in M] for M in mats]


def capture_layer(full):
    rec = {"engines": [], "planted": [], "runs": [], "brute": []}
    tags = {}
    orig = {k: getattr(s16_layer, k) for k in ("load_engine", "planted", "run", "brute_classes")}

    def load_engine(path=s16_layer.ENGINE_PATH, layered=True, place=PLACE, expect_sha=s16_layer.ENGINE_SHA256,
                    extra=None):
        mod = orig["load_engine"](path, layered=layered, place=place, expect_sha=expect_sha, extra=extra)
        if not layered:
            tag = "plain"
        elif extra:
            tag = "extra:" + ",".join(sorted(extra))
        elif int(place) == int(PLACE) and place.w == PLACE.w:
            tag = "layered"
        else:
            tag = "layered-place(p=%d,w=%d)" % (int(place), place.w)
        tags[id(mod)] = tag
        rec["engines"].append({"tag": tag, "sha256": mod.SOURCE_SHA256, "rebound": list(mod.REBOUND)})
        return mod

    def planted(mod, rng, m, n, zero_p=0):
        M, sig = orig["planted"](mod, rng, m, n, zero_p=zero_p)
        rec["planted"].append({"m": m, "n": n, "zero_p": zero_p, "matrix": encm([M])[0], "sigma": list(sig)})
        return M, sig

    def run(mod, mats, m, n, mode, rules="RWVP", arith="modp", mut=None, budget=10 ** 7):
        eng, status, found, counts = orig["run"](mod, mats, m, n, mode, rules=rules, arith=arith, mut=mut,
                                                 budget=budget)
        rec["runs"].append({"engine": tags.get(id(mod), "?"), "mats": encm(mats), "m": m, "n": n, "mode": mode,
                            "rules": rules, "arith": arith, "mut": mut, "budget": budget, "status": status,
                            "found": sorted(list(f) for f in found), "counts": list(counts),
                            "order": list(eng.order)})
        return eng, status, found, counts

    def brute_classes(mod, mats, m, n, order):
        out = orig["brute_classes"](mod, mats, m, n, order)
        rec["brute"].append({"engine": tags.get(id(mod), "?"), "mats": encm(mats), "m": m, "n": n,
                             "order": list(order), "classes": sorted(list(c) for c in out)})
        return out

    for k, f in (("load_engine", load_engine), ("planted", planted), ("run", run), ("brute_classes", brute_classes)):
        setattr(s16_layer, k, f)
    try:
        ok, lines = s16_layer.self_test(full=full)
    finally:
        for k, f in orig.items():
            setattr(s16_layer, k, f)
    rec["self_test_ok"] = ok
    rec["self_test_lines"] = lines
    return rec


def capture_field(n):
    """Seeded elements with cyclo16's and replay_cyclo16's results on them."""
    rng = SM64(0x51160020)
    rows = []
    for _ in range(n):
        a, b = rand_elem(rng), rand_elem(rng)
        ra = replay_cyclo16.Cyc.from_strings(a.to_json())
        rb = replay_cyclo16.Cyc.from_strings(b.to_json())
        row = {"a": a.to_json(), "b": b.to_json(),
               "cyclo16": {"sum": (a + b).to_json(), "prod": (a * b).to_json(), "norm": str(norm(a)),
                           "trace": str(trace(a)), "sigma": {str(k): galois(a, k).to_json() for k in ODD},
                           "rho": a % PLACE},
               "replay": {"sum": [str(x) for x in ra.add(rb).coords()], "prod": [str(x) for x in ra.mul(rb).coords()],
                          "norm": str(ra.norm()), "sigma": {str(k): [str(x) for x in ra.sigma(k).coords()]
                                                            for k in (3, 5, 7, 15)},
                          "rho": replay_cyclo16.rho(ra, int(PLACE), PLACE.w)}}
        if a:
            row["cyclo16"]["inv"] = a.inverse().to_json()
            row["replay"]["inv"] = [str(x) for x in ra.inv().coords()]
        rows.append(row)
    return rows


def main(argv):
    if not argv or argv[0].startswith("-"):
        print(__doc__)
        return 2
    full = "--full" in argv[1:]
    known = {
        "zeta": cyclo16.zeta(1).to_json(), "one_minus_zeta_norm": str(norm(Q16((1,)) - cyclo16.zeta(1))),
        "sqrt2": (cyclo16.zeta(2) - cyclo16.zeta(6)).to_json(),
        "one_plus_sqrt2_norm": str(norm(Q16((1,)) + cyclo16.zeta(2) - cyclo16.zeta(6))),
        "cyclotomic_unit_norms": {str(a): str(norm((Q16((1,)) - cyclo16.zeta(a)) / (Q16((1,)) - cyclo16.zeta(1))))
                                  for a in (3, 5, 7)},
    }
    doc = {"schema": "loc1-arith-claims", "version": 1, "full": full,
           "place": {"p": int(PLACE), "w": PLACE.w, "lo": 1 << 61, "valid": PLACE.valid()},
           "engine_sha256": s16_layer.ENGINE_SHA256, "rebound": list(s16_layer.REBOUND),
           "known": known, "field": capture_field(200 if full else 40), "layer": capture_layer(full)}
    with open(argv[0], "w", encoding="ascii") as fh:
        json.dump(doc, fh, sort_keys=True, separators=(",", ":"))
        fh.write("\n")
    L = doc["layer"]
    print("emitted %d field rows, %d engine loads, %d planted, %d runs, %d brute-force sets; K-arith-16 self-test %s"
          % (len(doc["field"]), len(L["engines"]), len(L["planted"]), len(L["runs"]), len(L["brute"]),
             "ALL PASS" if L["self_test_ok"] else "FAILURE"))
    return 0 if L["self_test_ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
