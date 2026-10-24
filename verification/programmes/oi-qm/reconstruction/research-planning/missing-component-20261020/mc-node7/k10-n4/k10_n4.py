#!/usr/bin/env python3
"""Node 7 control K-10 at n = 4, run on the committed probe without editing it. Python 3 stdlib and git.

  python3 -I -B -u k10_n4.py --objects DIR [--fetch] [--self-test-only]

K-10 (PREREG section 4.3 and section 5, amendment A-2): under counting-type priors, membership of A_CHSH(n) equals the
no-signalling boxes with entries in (1/n)Z, and the eight-coordinate program equals the 256-count program. The probe
k10.py at a501b418 checks n = 1, 2, 3 in main(); its functions by_mixtures(n, vecs) and by_coordinates(n) take n as a
parameter. This driver runs those committed functions at n = 4 and compares their sets exactly as main() does at
n <= 3 (m == c). It adds no logic to the check. Its additions are controls:
  - the probe's blob is verified (git blob id and sha256) and executed from exactly the verified bytes;
  - self-test, before n = 4: main() is run and its output must equal the committed k10.run1.out byte for byte; the
    driver's own per-n line must equal that file's line n for n = 1, 2, 3;
  - coverage: the number of multisets the committed by_mixtures visits is counted (a pass-through wrapper on the
    probe's combinations_with_replacement) and must equal C(256 + n - 1, n);
  - an independent closed-form count of the eight-coordinate boxes must equal len(by_coordinates(n));
  - negative controls, which must each give FAILS through the same verdict predicate: a box removed from one side,
    the two forms at different n, a mutant probe whose no-signalling test accepts everything, a mutant probe whose
    coordinate range drops the value n, and a truncated enumeration.
All arithmetic is integer: boxes are count vectors, and the sets are compared exactly.

Last line: K10 N4 HOLDS (exit 0), K10 N4 FAILS (exit 1), or K10 N4 UNVERIFIED (exit 2) when the source could not be
fetched or verified or a self-test control did not behave as required, in which case no n = 4 verdict is printed.

--fetch creates DIR as a new bare repository and fetches commit a501b418 by its full id from the public repository with
no credential (GH_TOKEN and GITHUB_TOKEN removed from git's environment, system and global configuration ignored,
credential helper and http.extraHeader reset, prompts off). Nothing is checked out and nothing is written elsewhere.
"""
import argparse
import contextlib
import hashlib
import io
import itertools
import math
import os
import subprocess
import sys
import types

sys.dont_write_bytecode = True

URL = "https://github.com/amaybaum/incompleteness.git"
COMMIT = "a501b4189d7f1ada923d76179fa6a38a1a83b408"   # research/missing-component-20261020, node 7
NODE = "verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/mc-node7"
# path under NODE: (git blob id, sha256). PREREG.md is the frozen preregistration (blob unchanged since 73a27ba1).
PINS = {
    "PREREG.md": ("12edcd1a14e1fc6f890fd234d19ae524fb9fdf39",
                  "99834efa540bbf0d2f6cd84bc819daa71b7d612864775285785e033739ebd3bc"),
    "amendments/AMENDMENTS.md": ("f0931b408854b9fc5a7e689af516ca20d7cc5806",
                                 "e5f52135df3d3af8e99cc67464f23d2bea442de82d175bc8c4f408607dd6d076"),
    "probe/SHA256SUMS": ("ce17f602b86649852bfceaaf9f6d3881f91fac95",
                         "e5f772a52efa7e62bd976d64847fbf42e0b9f89d8553c2256911f520d6bc3c48"),
    "probe/k10.py": ("25c83510866350e3316dcba29cc257b779865d88",
                     "e63d1e15336e38598601213205a2f7ca336b7e8d079223139cdaef2184722d43"),
    "probe/k10.run1.out": ("b330973fb06398da1c899d1a18d25ae47464c8f5",
                           "a573d96196e1a920051c0e17dab38266321126e7db2aca43c434afc01cfb6d5d"),
}
COMMITTED_COUNTS = {1: 16, 2: 136, 3: 752}   # k10.run1.out, both forms
SCRUB = ("GH_TOKEN", "GITHUB_TOKEN", "GIT_ASKPASS", "SSH_ASKPASS", "GIT_CONFIG_PARAMETERS", "GIT_CONFIG_COUNT")
TIMEOUT_S = 600


class Unverified(Exception):
    pass


def git_env():
    env = {k: v for k, v in os.environ.items() if k not in SCRUB and not k.startswith("GIT_CONFIG_KEY_")
           and not k.startswith("GIT_CONFIG_VALUE_")}
    env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0", GIT_ASKPASS="/bin/false")
    return env


def git(objects, *args):
    cmd = ["git", "-C", objects, "-c", "credential.helper=", "-c", "http.extraHeader=", "-c", "core.askPass=",
           "-c", "gc.auto=0", "-c", "maintenance.auto=false", "-c", "fetch.writeCommitGraph=false"] + list(args)
    p = subprocess.run(cmd, capture_output=True, timeout=TIMEOUT_S, env=git_env())
    return p.returncode, p.stdout, p.stderr.decode("utf-8", "replace")


def fetch(objects):
    if os.path.lexists(objects):
        raise Unverified("refused: %s exists" % objects)
    p = subprocess.run(["git", "init", "-q", "--bare", objects], capture_output=True, env=git_env())
    if p.returncode:
        raise Unverified("git init failed")
    rc, _, err = git(objects, "fetch", "-q", "--no-tags", "--no-recurse-submodules", "--depth=1", URL, COMMIT)
    if rc:
        raise Unverified("fetch of %s failed (exit %d): %s" % (COMMIT, rc, (err.strip().splitlines() or [""])[-1][:200]))


def git_blob_id(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def read_pinned(objects):
    rc, typ, _ = git(objects, "cat-file", "-t", COMMIT)
    if rc or typ.strip() != b"commit":
        raise Unverified("commit %s absent" % COMMIT)
    out = {}
    for rel, (blob, sha) in PINS.items():
        rc, rev, _ = git(objects, "rev-parse", "%s:%s/%s" % (COMMIT, NODE, rel))
        tree_blob = rev.decode().strip()
        rc2, data, _ = git(objects, "cat-file", "blob", tree_blob or "0" * 40)
        got = (tree_blob, git_blob_id(data) if rc2 == 0 else "", hashlib.sha256(data).hexdigest() if rc2 == 0 else "")
        ok = rc == 0 and rc2 == 0 and got == (blob, blob, sha)
        print("  %s  %s  blob %s  sha256 %s" % ("ok  " if ok else "FAIL", rel, got[0][:12] or "-", got[2][:12] or "-"))
        if not ok:
            raise Unverified("%s does not match its pin (blob %s, sha256 %s)" % (rel, blob, sha))
        out[rel] = data
    sums = out["probe/SHA256SUMS"].decode().splitlines()
    for rel in ("probe/k10.py", "probe/k10.run1.out"):
        line = "%s  %s" % (PINS[rel][1], rel.split("/", 1)[1])
        if line not in sums:
            raise Unverified("SHA256SUMS lacks %r" % line)
    print("  ok    SHA256SUMS lists k10.py and k10.run1.out at their pinned sha256")
    return out


def load_probe(src, mutate=None):
    """Executes exactly the given bytes as module 'k10' (not '__main__', so main() does not run on load)."""
    text = src.decode("utf-8")
    if mutate is not None:
        old, new = mutate
        if text.count(old) != 1:
            raise Unverified("mutant anchor %r not unique" % old)
        text = text.replace(old, new)
    mod = types.ModuleType("k10")
    mod.__file__ = "k10.py@%s" % COMMIT[:8]
    exec(compile(text, mod.__file__, "exec"), mod.__dict__)
    return mod


def counted(mod, drop_last=False):
    """Pass-through wrapper on the probe's combinations_with_replacement: yields the same tuples, counts them."""
    box = {"visited": 0}
    real = itertools.combinations_with_replacement

    def cwr(pool, r):
        prev = None
        for t in real(pool, r):
            if prev is not None:
                box["visited"] += 1
                yield prev
            prev = t
        if prev is not None and not drop_last:
            box["visited"] += 1
            yield prev
    mod.combinations_with_replacement = cwr
    return box


def closed_form_count(n):
    """Number of (pA, pB, j) with all four 2x2 tables nonnegative: an independent count of by_coordinates(n)."""
    total = 0
    for pA0, pA1, pB0, pB1 in itertools.product(range(n + 1), repeat=4):
        prod = 1
        for a in (pA0, pA1):
            for b in (pB0, pB1):
                prod *= max(0, min(a, b) - max(0, a + b - n) + 1)
        total += prod
    return total


def measure(mod, n, n_coord=None, drop=False, drop_last=False):
    box = counted(mod, drop_last=drop_last)
    vecs = mod.pair_vectors()
    m = mod.by_mixtures(n, vecs)
    c = mod.by_coordinates(n if n_coord is None else n_coord)
    if drop:
        c = set(c)
        c.discard(min(c))
    return {"n": n, "n_mix": len(m), "n_coord": len(c), "equal": m == c, "visited": box["visited"],
            "expected_visited": math.comb(256 + n - 1, n), "closed_form": closed_form_count(n)}


def holds(r):
    return (r["equal"] and r["n_mix"] == r["n_coord"] and r["visited"] == r["expected_visited"]
            and r["n_coord"] == r["closed_form"])


def probe_line(r):
    """The probe's own per-n line (k10.py main())."""
    return (f'n={r["n"]}: mixtures of n response pairs that are no-signalling: {r["n_mix"]}; no-signalling boxes with '
            f'entries in (1/n)Z by eight coordinates: {r["n_coord"]}; equal: {r["equal"]}')


def control_line(r):
    return ("n=%d: multisets visited %d of C(%d, %d) = %d; eight-coordinate closed-form count %d"
            % (r["n"], r["visited"], 255 + r["n"], r["n"], r["expected_visited"], r["closed_form"]))


def self_test(src, run1):
    fails = 0

    def case(name, ok):
        nonlocal fails
        fails += not ok
        print("  %s  %s" % ("ok  " if ok else "FAIL", name), flush=True)

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        load_probe(src).main()
    case("committed main() reproduces k10.run1.out byte for byte (sha256 %s)" % PINS["probe/k10.run1.out"][1][:12],
         buf.getvalue().encode("utf-8") == run1)
    lines = run1.decode("utf-8").splitlines()
    for n in (1, 2, 3):
        r = measure(load_probe(src), n)
        print("    " + probe_line(r))
        print("    " + control_line(r))
        case("n=%d: driver's line equals k10.run1.out line %d" % (n, n), probe_line(r) == lines[n - 1])
        case("n=%d: both forms %d boxes, as committed; verdict predicate holds" % (n, COMMITTED_COUNTS[n]),
             r["n_mix"] == r["n_coord"] == COMMITTED_COUNTS[n] and holds(r))
    # Negative controls: each is a mutated equality, and must fail through the same predicate used at n = 4.
    # Each also names the component of the predicate it targets, which must catch it on its own.
    unequal = lambda r: not r["equal"]
    negatives = [
        ("one box removed from the eight-coordinate side (n=2)", lambda: measure(load_probe(src), 2, drop=True),
         unequal),
        ("mixtures at n=2 against coordinates at n=3", lambda: measure(load_probe(src), 2, n_coord=3), unequal),
        ("mutant probe: no-signalling test accepts every box (n=2)",
         lambda: measure(load_probe(src, ("def nosig(c):\n", "def nosig(c):\n    return True\n")), 2), unequal),
        ("mutant probe: coordinate range omits the value n (n=2)",
         lambda: measure(load_probe(src, ("rng = range(n + 1)", "rng = range(n)")), 2),
         lambda r: unequal(r) and r["n_coord"] != r["closed_form"]),
        ("truncated enumeration: last multiset not visited (n=2)",
         lambda: measure(load_probe(src), 2, drop_last=True),
         lambda r: r["visited"] != r["expected_visited"]),
    ]
    for name, f, targeted in negatives:
        r = f()
        case("negative control fails as required: %s [mix %d, coord %d, equal %s, visited %d/%d, closed form %d]"
             % (name, r["n_mix"], r["n_coord"], r["equal"], r["visited"], r["expected_visited"], r["closed_form"]),
             not holds(r) and targeted(r))
    print("  self-test: %d failed" % fails, flush=True)
    return fails == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--objects", required=True)
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--self-test-only", action="store_true")
    a = ap.parse_args()
    print("K-10 at n = 4 on node 7's committed probe, commit %s" % COMMIT, flush=True)
    try:
        if a.fetch:
            fetch(a.objects)
            print("  ok    fetched %s by id from %s with no credential" % (COMMIT, URL))
        files = read_pinned(a.objects)
        print("self-test (n <= 3 and negative controls):", flush=True)
        if not self_test(files["probe/k10.py"], files["probe/k10.run1.out"]):
            raise Unverified("a self-test control did not behave as required")
    except Unverified as e:
        print("UNVERIFIED: %s" % e)
        print("K10 N4 UNVERIFIED")
        return 2
    if a.self_test_only:
        print("self-test only: n = 4 not run")
        return 0
    print("n = 4 (one job, the committed by_mixtures(4, vecs) and by_coordinates(4)):", flush=True)
    r = measure(load_probe(files["probe/k10.py"]), 4)
    print("  " + probe_line(r))
    print("  " + control_line(r))
    verdict = "HOLDS" if holds(r) else "FAILS"
    print("K10 N4 %s: mixtures no-signalling %d; eight-coordinate %d; equal %s; multisets visited %d of C(259, 4) = %d; "
          "closed-form count %d" % (verdict, r["n_mix"], r["n_coord"], r["equal"], r["visited"],
                                    r["expected_visited"], r["closed_form"]))
    return 0 if verdict == "HOLDS" else 1


if __name__ == "__main__":
    sys.exit(main())
