"""LOC-1 preflight: the expected result of the drafting-time preflight, read from its deterministic outputs.

Reads the eleven stdout files and the two data files the preflight scripts write, from the directory given,
and prints one JSON object: the deterministic content the preregistration's section 9 relies on (counts,
statuses, class and stratum sizes, control and mutation outcomes) and the sha256 of every file it was read
from.  Timings are written to stderr by the scripts and are not read here.  Standard library only.

Run:  python3 -I preflight_expected.py DIR > preflight-expected.json
"""
import hashlib
import json
import os
import re
import sys

SOURCES = ("sizes.out", "scope_T.out", "f34_count_indep.out", "f34_enum.out", "f34_enum_kdepall.out",
           "c21_search.out", "c21_witness.json", "c21_replay.out", "c21_replay_mut.out", "c21_sampler.out",
           "c21_samples.json")
INPUTS = ("c21_engine.py", "c21_search.py", "c21_replay.py", "c21_replay_mut.py", "c21_sampler.py",
          "f34_enum.py", "f34_count_indep.py", "scope_T.py", "frozen_inputs.json", "sizes.py")


def fail(msg):
    sys.stderr.write("preflight_expected: %s\n" % msg)
    sys.exit(2)


def lines(d, name):
    with open(os.path.join(d, name), encoding="utf-8") as fh:
        return fh.read().split("\n")


def one(pattern, ls, name):
    hits = [m for m in (re.match(pattern, L) for L in ls) if m]
    if len(hits) != 1:
        fail("%s: %d lines match %r" % (name, len(hits), pattern))
    return hits[0]


def ints(s):
    return [int(x) for x in re.findall(r"-?\d+", s)]


RUN = re.compile(r"^RUN (.+?)\s+(exist|all)\s+(FOUND|NONE|ALL|EXHAUSTED)\s+found\s+(\d+)\s+tested\s+(\d+)\s+"
                 r"accepted\s+(\d+)\s+leaves\s+(\d+)\s+rules (\S+)\s+order (\S+)(.*)$")


def c21_search(ls):
    out = {}
    out["k_canon"] = {}
    for L in ls:
        m = re.match(r"^CONTROL K-canon (\d+x\d+) PASS found (\d+) classes, N!/\|G\| = (\d+)$", L)
        if m:
            out["k_canon"][m.group(1)] = [int(m.group(2)), int(m.group(3))]
    s = [i for i, L in enumerate(ls) if L.startswith("== 16 points as 4 x 4")]
    e = [i for i, L in enumerate(ls) if L == "== ablation and arithmetic cross-checks"]
    if len(s) != 1 or len(e) != 1:
        fail("c21_search.out: section markers")
    runs = []
    for L in ls[s[0]:e[0]]:
        if not L.startswith("RUN "):
            continue
        m = RUN.match(L)
        if not m:
            fail("c21_search.out: unparsed RUN line %r" % L)
        k = re.search(r"knuth-estimate accepted (\d+) tested (\d+)", m.group(10))
        runs.append({"name": m.group(1).strip(), "mode": m.group(2), "status": m.group(3),
                     "found": int(m.group(4)), "tested": int(m.group(5)), "rules": m.group(8),
                     "order": m.group(9), "knuth_tested": int(k.group(2)) if k else None})
    for mode in ("exist", "all"):
        rs = [r for r in runs if r["mode"] == mode]
        done = [r for r in rs if r["status"] != "EXHAUSTED"]
        ts = sorted(r["tested"] for r in done)
        n = len(ts)
        summ = {"runs": len(rs), "terminated": n,
                "statuses": {st: sum(1 for r in done if r["status"] == st) for st in sorted({r["status"] for r in done})},
                "rules_order_of_terminated": sorted({"%s %s" % (r["rules"], r["order"]) for r in done}),
                "tested_min": ts[0], "tested_max": ts[-1],
                "tested_sorted_index_n_div_2": ts[n // 2], "tested_sorted_index_n_div_2_minus_1": ts[n // 2 - 1],
                "max_runs": sorted(r["name"] for r in done if r["tested"] == ts[-1]),
                "exhausted": [{"name": r["name"], "tested": r["tested"], "rules": r["rules"], "order": r["order"],
                               "knuth_tested": r["knuth_tested"]} for r in rs if r["status"] == "EXHAUSTED"]}
        line = one(r"^mode %s: (\d+) runs complete; tested nodes min (\d+) median (\d+) max (\d+) " % mode, ls,
                   "c21_search.out")
        if [int(x) for x in line.groups()] != [n, ts[0], ts[n // 2], ts[-1]]:
            fail("c21_search.out: summary line for %s disagrees with its RUN lines" % mode)
        out["mode_" + mode] = summ
    if out["mode_exist"]["terminated"]:
        out["exist_runs"] = [{"name": r["name"], "status": r["status"], "tested": r["tested"]}
                             for r in runs if r["mode"] == "exist"]
    named = {}
    for key, nm, mode in (("p0_P_exist", "P0 control P = H1(x)H1", "exist"), ("p0_P_all", "P0 control P = H1(x)H1", "all"),
                          ("near_identity_frozen", "near-identity I+E(14,15) order=greedy rules=RWVP", "exist"),
                          ("transposition_consecutive", "perm 2.1.1.1.1.1.1.1.1.1.1.1.1.1.1 consecutive [excluded]", "exist"),
                          ("transposition_seeded", "perm 2.1.1.1.1.1.1.1.1.1.1.1.1.1.1 seeded [excluded]", "exist")):
        hit = [r for r in runs if r["name"] == nm and r["mode"] == mode]
        if len(hit) != 1:
            fail("c21_search.out: run %r %s" % (nm, mode))
        named[key] = {"status": hit[0]["status"], "found": hit[0]["found"], "tested": hit[0]["tested"]}
    out["named_runs"] = named
    ctl = [L for L in ls if L.startswith("CONTROL ")]
    out["controls"] = {"lines": len(ctl), "pass": sum(1 for L in ctl if " PASS" in L), "fail": sum(1 for L in ctl if " FAIL" in L),
                       "k_ablation": sum(1 for L in ctl if L.startswith("CONTROL K-ablation PASS")),
                       "k_arith": sum(1 for L in ctl if L.startswith("CONTROL K-arith PASS")),
                       "k_collision": sum(1 for L in ctl if L.startswith("CONTROL K-collision PASS"))}
    out["mutations"] = {m.group(1): m.group(2) for m in (re.match(r"^MUTATION (\S+)\s+(DETECTED|NOT DETECTED)", L) for L in ls) if m}
    out["verdict"] = one(r"^C21 PREFLIGHT: (.*)$", ls, "c21_search.out").group(1)
    return out


def f34(ls, name):
    out = {}
    out["points"] = ints(one(r"^points of PG\(3,3\): (\d+)$", ls, name).group(1))[0]
    m = one(r"^decompositions enumerated: (\d+)\s+formula .* = (\d+)\s+\(\|GL\(4,3\)\| = (\d+)", ls, name)
    out["decompositions"], out["formula"], out["gl43"] = [int(x) for x in m.groups()]
    out["controls"] = {m.group(1): m.group(2) for m in (re.match(r"^CONTROL (\S+) (PASS|FAIL)", L) for L in ls) if m}
    out["k_dep"] = one(r"^CONTROL K-dep PASS (.*)$", ls, name).group(1)
    rules = {}
    for L in ls:
        m = re.match(r"^rule (\S+) (deg_max histogram|\(deg_max, e\) histogram|min deg_max|natural decomposition|"
                     r"planted rows\(S\) decomposition)[: =]+(.*)$", L)
        if m:
            rules.setdefault(m.group(1), {})[m.group(2)] = m.group(3).strip()
    out["rules"] = rules
    out["mutations"] = {m.group(1): m.group(2) for m in (re.match(r"^MUTATION (\S+)\s+.*: (DETECTED|NOT DETECTED)", L) for L in ls) if m}
    out["verdict"] = one(r"^F34 PREFLIGHT: (.*)$", ls, name).group(1)
    return out


def main():
    if len(sys.argv) != 2:
        fail("usage: preflight_expected.py DIR")
    d = sys.argv[1]
    src = {}
    for f in SOURCES:
        p = os.path.join(d, f)
        if not os.path.isfile(p):
            fail("missing %s" % f)
        with open(p, "rb") as fh:
            b = fh.read()
        src[f] = {"bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}
    res = {}
    ls = lines(d, "sizes.out")
    res["sizes"] = {"rows": [L for L in ls[1:] if L.startswith("leg ")], "formula_controls": one(r"^formula controls: (\S+)$", ls, "sizes.out").group(1)}
    ls = lines(d, "scope_T.out")
    rows = []
    for L in ls[1:]:
        m = re.match(r"^(\S+)\s+(.+?)\s{2,}(Q-part|Q-set|both)\s+(\d+)\s+(\d+|-)\s+(\d+)$", L)
        if m:
            rows.append({"case": m.group(1), "shape": m.group(2).strip(), "quotient": m.group(3), "i0_ambient": int(m.group(4)),
                         "i1_ambient": None if m.group(5) == "-" else int(m.group(5)), "group_order": int(m.group(6))})
    res["scope_T"] = {"rows": rows, "orbit_check": one(r"^orbit counts equal \|X\|/\|G\| in every case \(free actions\): (\S+)$", ls, "scope_T.out").group(1)}
    ls = lines(d, "f34_count_indep.out")
    res["f34_count_indep"] = {"points": ints(one(r"^projective points .*: (\d+)$", ls, "f34_count_indep.out").group(1))[0],
                              "ordered_4_tuples": ints(one(r"^ordered independent 4-tuples of points: (\d+)$", ls, "f34_count_indep.out").group(1))[0],
                              "unordered_4_sets": ints(one(r"^unordered independent 4-sets of points: (\d+)$", ls, "f34_count_indep.out").group(1))[0],
                              "verdict": one(r"^INDEPENDENT COUNT: (.*)$", ls, "f34_count_indep.out").group(1)}
    res["f34_enum"] = f34(lines(d, "f34_enum.out"), "f34_enum.out")
    res["f34_enum_kdep_all"] = f34(lines(d, "f34_enum_kdepall.out"), "f34_enum_kdepall.out")
    res["c21_search"] = c21_search(lines(d, "c21_search.out"))
    ls = lines(d, "c21_replay.out")
    m = one(r"^REPLAY records (\d+)\s+witnesses re-verified (\d+)\s+brute-forced shapes (\d+)\s+planted checks (\d+)\s+"
            r"permutation checks (\d+)\s+no-class samples (\d+)\s+truncated witness lists (\d+)$", ls, "c21_replay.out")
    keys = ("records", "witnesses_reverified", "bruteforced_shapes", "planted_checks", "permutation_checks",
            "no_class_samples", "truncated_witness_lists")
    res["c21_replay"] = dict(zip(keys, [int(x) for x in m.groups()]))
    res["c21_replay"]["verdict"] = one(r"^REPLAY: (.*)$", ls, "c21_replay.out").group(1)
    ls = lines(d, "c21_replay_mut.out")
    res["c21_replay_mut"] = {"mutations": {m.group(1): m.group(2) for m in (re.match(r"^REPLAY-MUTATION (\S+)\s+on .*?\s(DETECTED|NOT DETECTED)$", L) for L in ls) if m},
                             "verdict": one(r"^REPLAY MUTATIONS: (.*)$", ls, "c21_replay_mut.out").group(1)}
    ls = lines(d, "c21_sampler.out")
    cls = one(r"^classes by stratum: \[(.*)\]\s+sum (\d+)\s+\(total classes (\d+)\)$", ls, "c21_sampler.out")
    pl = one(r"^ordered placements of 0\.\.3 by stratum: \[(.*)\] \(total (\d+)\)$", ls, "c21_sampler.out")
    dr = one(r"^draws (\d+) to fill 4 x 500; draws per stratum \[(.*)\]; duplicate classes rejected (\d+)$", ls, "c21_sampler.out")
    def pairs(s):
        return [[int(a), int(b)] for a, b in re.findall(r"\((\d+), (\d+)\)", s)]

    res["c21_sampler"] = {"placements_by_stratum": pairs(pl.group(1)), "placements_total": int(pl.group(2)),
                          "classes_by_stratum": pairs(cls.group(1)), "classes_sum": int(cls.group(2)), "classes_total": int(cls.group(3)),
                          "draws": int(dr.group(1)), "draws_by_stratum": pairs(dr.group(2)), "duplicates_rejected": int(dr.group(3)),
                          "distinct_classes": ints(one(r"^.*distinct classes (\d+)$", ls, "c21_sampler.out").group(1))[0],
                          "sample_list_sha256": one(r"^sample list sha256 ([0-9a-f]{64})$", ls, "c21_sampler.out").group(1),
                          "controls": sorted(set(re.findall(r"CONTROL (\S+) (PASS|FAIL)", "\n".join(ls)))),
                          "product_classes_found": [ints(m.group(1))[0] for m in (re.match(r"^classified 2000 samples on .*: product classes among them (\d+)$", L) for L in ls) if m]}
    with open(os.path.join(d, "c21_witness.json"), encoding="utf-8") as fh:
        W = json.load(fh)
    with open(os.path.join(d, "c21_samples.json"), encoding="utf-8") as fh:
        S = json.load(fh)
    res["data_files"] = {"c21_witness.json": {"records": len(W)}, "c21_samples.json": {"samples": len(S)}}
    doc = {
        "schema": "loc1-preflight-expected",
        "version": 1,
        "form": "derived",
        "holds_at": "no commit: a drafting-time design result of the ten preflight inputs named in 'inputs' by sha256, "
                    "which are self-contained (standard library; they read only their own directory, and "
                    "c21_replay_mut.py also the temporary files it writes); from stage 1 they are the files of the "
                    "LOC-1 record directory's design/",
        "inputs": sorted(INPUTS),
        "recipe": ["copy the ten inputs into an empty directory and run there, in order:",
                   "python3 -I sizes.py > sizes.out", "python3 -I scope_T.py > scope_T.out",
                   "python3 -I f34_count_indep.py > f34_count_indep.out",
                   "python3 -I f34_enum.py > f34_enum.out 2> /dev/null",
                   "python3 -I f34_enum.py --kdep-all > f34_enum_kdepall.out 2> /dev/null",
                   "python3 -I c21_search.py > c21_search.out 2> /dev/null   (writes c21_witness.json)",
                   "python3 -I c21_replay.py > c21_replay.out", "python3 -I c21_replay_mut.py > c21_replay_mut.out",
                   "python3 -I c21_sampler.py > c21_sampler.out 2> /dev/null   (writes c21_samples.json)",
                   "python3 -I preflight_expected.py . > preflight-expected.json",
                   "compare each source with 'sources' and this file with its pinned sha256, byte for byte"],
        "sources": src,
        "not_recorded": "timings: every script writes durations, per-node and per-decomposition costs and peak memory "
                        "to stderr, which differs between runs; nothing here is read from stderr",
        "results": res,
    }
    sys.stdout.write(json.dumps(doc, sort_keys=True, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
