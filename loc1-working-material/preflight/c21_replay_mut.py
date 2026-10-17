"""LOC-1 preflight: mutation controls for the independent replay.  Each mutated witness file must make
c21_replay.py print DISAGREES.  The mutated copies live in a temporary directory that is removed on exit.
Run:  python3 -I c21_replay_mut.py [WITNESS.json]   (default: c21_witness.json in this directory)"""
import sys
import os
import json
import tempfile
import subprocess

here = os.path.dirname(os.path.abspath(__file__))
wpath = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "c21_witness.json")
with open(wpath) as fh:
    W = json.load(fh)


def first(pred):
    return next(k for k, r in enumerate(W) if pred(r))


def corrupt(r):
    s = r["found"][0]
    s[0], s[1] = s[1], s[0]


def drop(r):
    r["found"].pop()
    r["found_total"] = len(r["found"])


def dup(r):
    r["found"].append(list(r["found"][0]))
    r["found_total"] = len(r["found"])


def fake(r):
    r["status"] = "FOUND"
    r["found"] = [list(range(16))]
    r["found_total"] = 1


muts = [
    ("corrupt-witness", first(lambda r: r["name"].startswith("planted dense") and r["found"]), corrupt),
    ("drop-class", first(lambda r: r["name"] == "small 3x3 identity"), drop),
    ("duplicate-class", first(lambda r: r["name"] == "small 2x4 identity"), dup),
    ("fake-perm-class", first(lambda r: r["name"].startswith("perm 16 ") and r["status"] == "NONE"), fake),
]
ok_all = True
with tempfile.TemporaryDirectory() as tmp:
    for name, k, f in muts:
        V = json.loads(json.dumps(W))
        f(V[k])
        path = os.path.join(tmp, name + ".json")
        with open(path, "w") as fh:
            json.dump(V, fh, sort_keys=True, separators=(",", ":"))
        res = subprocess.run([sys.executable, "-I", os.path.join(here, "c21_replay.py"), path],
                             capture_output=True, text=True)
        det = "DISAGREES" in res.stdout
        ok_all &= det
        print("REPLAY-MUTATION %-16s on %-44s %s" % (name, W[k]["name"], "DETECTED" if det else "NOT DETECTED"))
print("REPLAY MUTATIONS:", "ALL DETECTED" if ok_all else "SOME NOT DETECTED")
