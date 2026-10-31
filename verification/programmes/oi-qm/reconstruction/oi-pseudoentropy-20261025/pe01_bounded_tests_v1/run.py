"""PE-01 runner.

  python3 -I -B run.py list                               shard ids, one per line (the CI matrix)
  python3 -I -B run.py shard ID --mode M --out DIR
        writes DIR/ID.json (deterministic measurement: commit, recipe, preflight, controls,
        measurements) and DIR/ID.provenance.json (run id, timings; not part of the replay). While it
        runs it keeps DIR/ID.partial.json current after every completed block (A1: an unfinished
        shard keeps the cells it completed and its controls).
  python3 -I -B run.py incomplete ID --out DIR --reason TEXT
        turns DIR/ID.partial.json (if any) into DIR/ID.incomplete.json with the reason
  python3 -I -B run.py replay ID --mode M --against DIR --out DIR2
        reruns a shard and requires its measurement JSON to be byte-identical (RP)
  python3 -I -B run.py collect DIR --mode M --out DIR2     merges shards into measurements.json

Modes: smoke (the §8 local row, n <= 5), test (the result scope with an unpinned local A2 stub named
by PE01_TEST_A2; never a result), result (the preregistered run). A run refuses to start if TH or
PIN fails (PLAN.md §5); result and test modes also refuse while an open item of pe01/pending.py is
not resolved by A2's block.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from pe01 import collect as COL  # noqa: E402
from pe01 import params as P  # noqa: E402
from pe01 import pending  # noqa: E402
from pe01 import shard as S  # noqa: E402
from pe01.exact import canonical  # noqa: E402

MODES = ("smoke", "test", "result")


def recipe(argv):
    return "python3 -I -B %s/run.py %s" % (P.REL, " ".join(argv))


def refuse(msg):
    sys.stderr.write("REFUSED: %s\n" % msg)
    sys.exit(3)


def preflight(mode):
    pf = P.preflight(mode)
    if not pf["pass"]:
        refuse("; ".join(pf["reasons"]))
    return pf


def run_shard(sid, mode, out):
    pf = preflight(mode)
    ctl = S.Controls()
    timing = {}
    t0 = time.time()
    head = {"schema": "pe01-shard/2", "shard": sid, "mode": mode, "commit": pf["PIN"]["run_commit"],
            "tree": pf["PIN"]["run_tree"],
            "recipe": recipe(["shard", sid, "--mode", mode, "--out", "<dir>"]),
            "preflight": {"TH": pf["TH"], "PIN": {k: v for k, v in pf["PIN"].items() if k != "code_tree_clean"},
                          "code_tree_clean": pf["PIN"]["code_tree_clean"]},
            "pending": pending.PENDING}
    part = os.path.join(out, sid + ".partial.json")

    def prog(label, meas):
        with open(part, "wb") as f:
            f.write(canonical(dict(head, controls=ctl.rec, measurements=meas, status="partial")))

    S.PROGRESS = prog
    if sid == "controls":
        meas = S.shard_controls(mode, ctl)
    elif sid == "tape":
        meas = S.shard_tape(mode, ctl)
    else:
        parts = sid.split("-")
        n = int(parts[0][1:])
        fam = parts[1]
        if mode == "smoke" and n > 5:
            refuse("smoke mode covers n <= 5 only")
        if len(parts) == 3 and parts[2] == "m3":
            if mode == "smoke":
                refuse("the m = 3 sweep is not part of the smoke scope")
            meas = S.shard_m3(n, fam, mode, ctl, timing)
        else:
            meas = S.shard_family(n, fam, mode, ctl, timing)
    timing["total"] = time.time() - t0
    payload = dict(head, controls=ctl.rec, measurements=meas)
    return payload, timing, part


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    cmd = argv[0]
    mode = argv[argv.index("--mode") + 1] if "--mode" in argv else "result"
    if mode not in MODES:
        refuse("unknown mode %s" % mode)
    if cmd == "list":
        for sid in S.shard_ids():
            print(sid)
        return 0
    if cmd in ("shard", "replay"):
        sid = argv[1]
        out = argv[argv.index("--out") + 1]
        os.makedirs(out, exist_ok=True)
        payload, timing, part = run_shard(sid, mode, out)
        data = canonical(payload)
        with open(os.path.join(out, sid + ".json"), "wb") as f:
            f.write(data)
        if os.path.exists(part):
            os.remove(part)
        prov = {"shard": sid, "run_id": os.environ.get("GITHUB_RUN_ID", "local"),
                "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "local"),
                "job": os.environ.get("GITHUB_JOB", "local"), "commit": payload["commit"],
                "recipe": payload["recipe"], "display_timing_seconds": timing}
        with open(os.path.join(out, sid + ".provenance.json"), "w") as f:
            json.dump(prov, f, sort_keys=True, indent=1)
            f.write("\n")
        if cmd == "replay":
            ref = os.path.join(argv[argv.index("--against") + 1], sid + ".json")
            same = open(ref, "rb").read() == data
            print("RP %s: %s" % (sid, "byte-identical" if same else "DIFFERS"))
            return 0 if same else 1
        fails = [k for k, v in payload["controls"].items() if not v["pass"]]
        print("%s: %s (%.1fs)" % (sid, "controls green" if not fails else "FAILED " + ",".join(fails), timing["total"]))
        return 0 if not fails else 1
    if cmd == "incomplete":
        sid = argv[1]
        out = argv[argv.index("--out") + 1]
        reason = argv[argv.index("--reason") + 1]
        os.makedirs(out, exist_ok=True)
        if os.path.exists(os.path.join(out, sid + ".json")):
            return 0
        part = os.path.join(out, sid + ".partial.json")
        rec = json.load(open(part)) if os.path.exists(part) else {"shard": sid, "controls": {}, "measurements": {}}
        rec["status"] = "incomplete"
        rec["reason"] = reason
        rec["run_id"] = os.environ.get("GITHUB_RUN_ID", "local")
        rec["completed_cells"] = rec.get("measurements", {}).get("completed_cells", [])
        with open(os.path.join(out, sid + ".incomplete.json"), "wb") as f:
            f.write(canonical(rec))
        if os.path.exists(part):
            os.remove(part)
        return 0
    if cmd == "collect":
        src = argv[1]
        out = argv[argv.index("--out") + 1]
        return COL.collect(src, out, mode)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
