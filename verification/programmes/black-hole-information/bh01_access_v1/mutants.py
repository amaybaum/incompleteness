#!/usr/bin/env python3
"""Mutants for checks.py: each control of PLAN.md section 5 is shown able to fail.

Usage (from any directory):
    python3 -I -B mutants.py [--out DIR]

Writes mutants-output.json into DIR (default: this file's directory). A mutant counts
as caught only when its targeted control reports failure on the named case. In-process
mutants replace one function of checks.py; source mutants run a modified copy of
checks.py in a child process. Exit status 0 iff every mutant is caught and every
unmutated baseline passes; otherwise 1.
"""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKS = os.path.join(HERE, "checks.py")


def load():
    spec = importlib.util.spec_from_file_location("bh01_checks", CHECKS)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def inprocess(name, target, patch, probe):
    """patch(mod) mutates a fresh module; probe(mod) returns True when the control passes."""
    mod = load()
    baseline = probe(mod)
    mod = load()
    patch(mod)
    passed = probe(mod)
    return {"mutant": name, "target": target, "kind": "in-process",
            "baseline_control_passes": baseline, "mutant_control_passes": passed,
            "caught": baseline and not passed}


def k3_probe(mod):
    mod.LEDGER = mod.Ledger()
    mod.named_k2_instances()
    return not any(c.startswith("K2:identity_direct_read") for c in mod.LEDGER.k3_fail)


def d1_probe(mod):
    tv = mod.named_examples()["swap_in_swap_out"]["cumulative_tv"]
    return mod.nondecreasing(tv)


def patch_support(mod):
    orig = mod.support

    def mutant(space, msg_regs, prior):
        return orig(space, msg_regs, {r: "blank" for r in prior})
    mod.support = mutant


def patch_tv(mod):
    orig = mod.total_variation
    mod.total_variation = lambda c0, c1, N: 2 * orig(c0, c1, N)


def patch_disjoint(mod):
    def mutant(cm, messages):
        sets = [set(cm[m]) for m in messages]
        for i in range(len(sets)):
            for j in range(i + 1, len(sets)):
                if sets[i] | sets[j]:
                    return False
        return True
    mod.records_disjoint = mutant


def patch_perms(mod):
    orig = mod.all_permutations
    mod.all_permutations = lambda n: orig(n)[:-1]


def patch_rank(mod):
    orig = mod.gf2_rank
    mod.gf2_rank = lambda rows: orig(list(rows)[:-1])


def patch_record(mod):
    orig = mod.make_record
    mod.make_record = lambda dtraj, schedule, t, mode: orig(dtraj, schedule, t, "snapshot")


def run_copy(src, flags, workdir, tag):
    path = os.path.join(workdir, tag + "_checks.py")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(src)
    outd = os.path.join(workdir, tag + "_out")
    os.mkdir(outd)
    proc = subprocess.Popen([sys.executable, "-I"] + flags + [path, "--out", outd],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc, outd


def finish(proc, outd):
    out, err = proc.communicate()
    rp = os.path.join(outd, "result.json")
    data = None
    if os.path.exists(rp):
        with open(rp, "rb") as fh:
            data = fh.read()
    return proc.returncode, out.decode("utf-8", "replace"), data


def source_mutants():
    with open(CHECKS, encoding="utf-8") as fh:
        src = fh.read()
    res = []
    anchor_bij = 'def is_bijection(table):\n    """Independent bijectivity check: the image is the whole domain."""\n'
    anchor_res = '        "verdict_text": lines,\n'
    anchor_main = "def main(argv):\n"
    if src.count(anchor_bij) != 1 or src.count(anchor_res) != 1 or src.count(anchor_main) != 1:
        return [{"mutant": "source-anchors", "caught": False, "note": "anchor not found exactly once"}]
    m_void = src.replace(anchor_bij, anchor_bij + "    return True\n")
    m_assert = src.replace(anchor_main, anchor_main + "    assert True\n")
    m_det = src.replace(anchor_res, anchor_res + '        "mutant_optimize_flag": sys.flags.optimize,\n')
    with tempfile.TemporaryDirectory() as wd:
        jobs = {
            "void": run_copy(m_void, ["-B"], wd, "void"),
            "assert": run_copy(m_assert, ["-B"], wd, "assert"),
            "base_B": run_copy(src, ["-B"], wd, "base_B"),
            "base_O": run_copy(src, ["-B", "-O"], wd, "base_O"),
            "det_B": run_copy(m_det, ["-B"], wd, "det_B"),
            "det_O": run_copy(m_det, ["-B", "-O"], wd, "det_O"),
        }
        done = {k: finish(*v) for k, v in jobs.items()}
    rc, out, data = done["void"]
    res.append({"mutant": "is_bijection accepts every map, end-to-end", "target": "K1 / VOID path",
                "kind": "source", "exit_status": rc, "printed_VOID": out.startswith("VOID"),
                "result_written": data is not None,
                "caught": rc == 2 and out.startswith("VOID") and data is None})
    rc, out, data = done["assert"]
    res.append({"mutant": "an assert statement added to main", "target": "source scan (no assert)",
                "kind": "source", "exit_status": rc, "printed_VOID": out.startswith("VOID"),
                "result_written": data is not None,
                "caught": rc == 2 and out.startswith("VOID") and data is None})
    b_ok = done["base_B"][0] == 0 and done["base_O"][0] == 0 and done["base_B"][2] is not None \
        and done["base_B"][2] == done["base_O"][2]
    d_same = done["det_B"][2] is not None and done["det_B"][2] == done["det_O"][2]
    res.append({"mutant": "optimization flag written into result.json", "target": "K6",
                "kind": "source", "baseline_identical_B_vs_O": b_ok,
                "mutant_identical_B_vs_O": d_same, "caught": b_ok and not d_same})
    return res


def main(argv):
    out_dir = HERE
    if "--out" in argv:
        out_dir = argv[argv.index("--out") + 1]
    results = []
    results.append(inprocess("is_bijection accepts every map", "K1 known_nonbijection_rejected",
                             lambda m: setattr(m, "is_bijection", lambda t: True),
                             lambda m: m.run_controls()["K1"]["known_nonbijection_rejected"]))
    results.append(inprocess("hidden prior ignored (hidden registers fixed at 0)", "K2 one_time_pad_R_alone",
                             patch_support, lambda m: m.run_controls()["K2"]["one_time_pad_R_alone"]))
    results.append(inprocess("total variation without the 1/2 factor", "K2 identity_direct_read",
                             patch_tv, lambda m: m.run_controls()["K2"]["identity_direct_read"]))
    results.append(inprocess("disjointness decoder uses union", "K3 on identity_direct_read",
                             patch_disjoint, k3_probe))
    results.append(inprocess("permutation enumeration truncated", "K4 S8_count",
                             patch_perms, lambda m: m.run_controls()["K4"]["S8_count"]))
    results.append(inprocess("GF(2) rank skips the last row (off-by-one row loop)", "K5 identity_cases",
                             patch_rank, lambda m: m.run_controls()["K5"]["identity_cases"]))
    results.append(inprocess("records not accumulated", "D1 on swap_in_swap_out",
                             patch_record, d1_probe))
    results.extend(source_mutants())
    all_caught = all(r.get("caught") for r in results)
    doc = {"schema": "bh01-access-v1/mutants", "mutants": results, "all_caught": all_caught,
           "count": len(results), "caught": sum(1 for r in results if r.get("caught"))}
    with open(os.path.join(out_dir, "mutants-output.json"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(doc, sort_keys=True, indent=1, ensure_ascii=True) + "\n")
    for r in results:
        print("%-8s %s -> %s" % ("CAUGHT" if r.get("caught") else "MISSED", r["mutant"], r.get("target", "")))
    print("caught %d of %d" % (doc["caught"], doc["count"]))
    return 0 if all_caught else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
