"""K-arith-16's round-trip clause: P0's Q(zeta_16) class to the layer's power-basis coordinates and back, exactly
(LOC-1 preregistration §7: "Each target built with P0's class enters the layer through its eight power-basis
coordinates; K-arith-16 checks that they round-trip exactly").  Research development.

P0's p0_exact.py builds every frozen lift at import, so it is never imported or run here.  Only its class C16 and
the four definitions C16 uses (ZERO, ONE, q, zeta) are taken from its syntax tree and executed, after the source's
sha256 is checked against the pin of §2.1.  Before F the self-test applies the round trip to seeded synthetic C16
elements and matrices only; to_layer() is the stage-2 entry point for the targets.

    load_c16(path)     the class and its helpers, from the pinned source, without executing anything else
    coords(x)          the 8 Fractions c_k / d of a C16 element
    to_layer(mats)     each entry as a layer element (cyclo16.Q16), after checking C16 -> coordinates -> Q16 ->
                       coordinates -> C16 returns the same element; raises on any difference

Run:  python3 -I -B p0_roundtrip.py --self-test [P0_EXACT_PY]
"""
import ast
import hashlib
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
P0_SHA256 = "00cb032b71dce6eb994864e8e18bf6748192f38a644898a9c3685d453ecd155c"     # §2.1, p0_exact.py
TAKE = {"C16", "ZERO", "ONE", "q", "zeta"}


def load_c16(path):
    src = open(path, "rb").read()
    if hashlib.sha256(src).hexdigest() != P0_SHA256:
        raise ValueError("p0_exact.py is not the pinned file")
    tree = ast.parse(src.decode("utf-8"))
    keep, names = [], set()
    for node in tree.body:
        if isinstance(node, (ast.ClassDef, ast.FunctionDef)) and node.name in TAKE:
            keep.append(node)
            names.add(node.name)
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and node.targets[0].id in TAKE:
            keep.append(node)
            names.add(node.targets[0].id)
    if names != TAKE:
        raise ValueError("p0_exact.py lacks %s" % sorted(TAKE - names))
    mod = ast.Module(body=keep, type_ignores=[])
    ns = {"__name__": "p0_c16", "__builtins__": __builtins__}
    exec("from math import gcd", ns)
    exec(compile(mod, "p0_exact.py[C16]", "exec"), ns)
    return ns


def coords(x):
    return tuple(Fraction(c, x.d) for c in x.c)


def from_coords(ns, cs):
    d = 1
    for f in cs:
        d = d * f.denominator // __import__("math").gcd(d, f.denominator)
    return ns["C16"](tuple(int(f * d) for f in cs), d)


def _layer():
    """The layer's arithmetic: design/ in a record directory, loc-1-arith/ beside this directory in research."""
    for d in (os.environ.get("LOC1_LAYER_DIR"), os.path.join(os.path.dirname(HERE), "design"),
              os.path.join(os.path.dirname(HERE), "loc-1-arith")):
        if d and os.path.isfile(os.path.join(d, "cyclo16.py")):
            sys.path.insert(0, d)
            import cyclo16
            return cyclo16
    raise SystemExit("cyclo16.py (the layer's arithmetic) not found in design/ or loc-1-arith/")


def to_layer(ns, mats, conv=coords):
    cy = _layer()
    out = []
    for M in mats:
        R = []
        for row in M:
            r = []
            for x in row:
                y = cy.Q16(conv(x))
                back = from_coords(ns, y.c)
                if back != x or tuple(y.c) != coords(x):
                    raise ValueError("round trip failed for %r" % (x,))
                r.append(y)
            R.append(r)
        out.append(R)
    return out


def self_test(path):
    lines, ok = [], True

    def rep(name, passed, detail=""):
        nonlocal ok
        ok &= bool(passed)
        lines.append("%s %-64s %s" % ("PASS" if passed else "FAIL", name, detail))

    ns = load_c16(path)
    rep("C16 and its helpers loaded from the pinned source alone", set(TAKE) <= set(ns),
        "sha256 %s; executed %s" % (P0_SHA256[:12], ",".join(sorted(TAKE))))
    rep("nothing else of p0_exact.py was executed (no frozen lift, no configuration)",
        not any(k in ns for k in ("C21", "L21", "CONFS", "OUT", "FAIL")))
    cy = _layer()
    C16, zeta = ns["C16"], ns["zeta"]
    s = 0x52545249
    els = []
    for _ in range(60):
        cs, d = [], 0
        for _ in range(8):
            s = (s * 6364136223846793005 + 1442695040888963407) % (1 << 64)
            cs.append(int(s >> 40) % 13 - 6)
        s = (s * 6364136223846793005 + 1442695040888963407) % (1 << 64)
        d = 1 + int(s >> 40) % 9
        els.append(C16(tuple(cs), d))
    els += [ns["ZERO"], ns["ONE"], zeta(1), zeta(15), ns["q"](3, 7)]
    bad = [x for x in els if from_coords(ns, cy.Q16(coords(x)).c) != x]
    rep("round trip C16 -> coordinates -> Q16 -> C16 on %d seeded elements" % len(els), not bad, "%d failures" % len(bad))
    hom = 0
    for a, b in zip(els[0::2], els[1::2]):
        qa, qb = cy.Q16(coords(a)), cy.Q16(coords(b))
        hom += cy.Q16(coords(a + b)) == qa + qb and cy.Q16(coords(a * b)) == qa * qb and \
            cy.Q16(coords(a.conj())) == cy.conj(qa)
    rep("C16 and Q16 agree on sums, products and conjugates (%d pairs)" % (len(els) // 2), hom == len(els) // 2)
    M = [[els[(3 * i + j) % len(els)] for j in range(16)] for i in range(16)]
    try:
        L = to_layer(ns, [M])
        rep("to_layer() on a seeded synthetic 16 x 16 matrix", len(L[0]) == 16 and len(L[0][0]) == 16)
    except ValueError as e:
        rep("to_layer() on a seeded synthetic 16 x 16 matrix", False, str(e))
    for name, conv in (("a conversion that drops the denominator", lambda x: tuple(Fraction(c) for c in x.c)),
                       ("a conversion that reverses the coordinates", lambda x: tuple(reversed(coords(x))))):
        try:
            to_layer(ns, [M], conv=conv)
            rep("NEG " + name, False, "NOT detected")
        except ValueError:
            rep("NEG " + name, True, "detected")
    import tempfile
    fd, tmp = tempfile.mkstemp(suffix=".py")
    os.close(fd)
    try:
        open(tmp, "wb").write(open(path, "rb").read() + b"\n")
        try:
            load_c16(tmp)
            rep("NEG a p0_exact.py one byte longer is refused", False)
        except ValueError:
            rep("NEG a p0_exact.py one byte longer is refused", True)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
    lines.append("p0_roundtrip self-test: %s" % ("ALL PASS" if ok else "FAILURE"))
    return ok, lines


def default_source():
    """The pinned file, where this tree has it: the predicted record's objects/, or a path in the environment."""
    env = os.environ.get("LOC1_P0_EXACT")
    if env:
        return env
    return None


def main(argv):
    if argv[:1] == ["--self-test"]:
        path = argv[1] if len(argv) > 1 else default_source()
        if not path:
            print("p0_roundtrip self-test: NOT RUN (no pinned p0_exact.py given; pass its path or set LOC1_P0_EXACT)")
            return 3
        ok, lines = self_test(path)
        print("\n".join(lines))
        return 0 if ok else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
