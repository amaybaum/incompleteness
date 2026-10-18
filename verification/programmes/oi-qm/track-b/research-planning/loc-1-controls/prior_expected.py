"""Expected results of the three prior-disclosure outputs of LOC-1 §13 (research development).

Under the owner's artifact ruling of 2026-10-18 the outputs decomposition_probe.out, factorization_check.out and
closure_design.out are not copied; each is replaced by <name>-expected.json, form derived: the output's
deterministic content, the output's sha256 as the provenance of the extraction, and the recipe that regenerates the
output.  The outputs carry no timing, so their deterministic content is every line, classified:

    check     "PASS <text>" / "FAIL <text>"           status and text
    header    "== <text>"                              a section of the output
    verdict   "EXPLORATORY-VERDICT ...", "controls: ...", "failures: ..."
    record    closure_design's "<config>: dim Z1=.. Z2=.. sum=../.. direct=.. complete=.. Z1=natural1:.. Z2=natural2:.."
              parsed into fields; any other line is kept as text

    python3 -I -B prior_expected.py extract NAME.out SCRIPT.py > NAME-expected.json
    python3 -I -B prior_expected.py compare NAME-expected.json NAME.out     a regenerated output against its expectation
    python3 -I -B prior_expected.py --self-test

extract refuses an output or script whose sha256 is not the one §13 pins.  The extraction runs on the bytes alone:
nothing here runs the prior scripts, which evaluate LOC-1's configurations.  compare is for stage 1, where the
recipe regenerates each output in a fresh copy.
"""
import hashlib
import json
import os
import re
import sys

PINS = {  # §13: output and script sha256
    "decomposition_probe": ("f32b7f820df7b80e2980b1a6409aea6e3e06aba2a3c12fe76e132b020acc527a",
                            "acdd998dd477b3fca26e41210b0f5b1634d0e795d47df4b4c1de1aad6472d40a"),
    "factorization_check": ("9ef260e7b54d7f339da5e3a29a30f8e62f00866c4993e82576689513f898d363",
                            "52694d4afd14c472ec9e7e265dae19183651e57cc284346d8d36981953a29126"),
    "closure_design": ("88921a9967bb57581e084323a206481baf5bce18f0d7d73f9fc6d97cfb5cb1d8",
                       "bb33939e6da3bd9c5638e547605d4541dae19118f6b564484fa007c34b3a7ed3"),
}
CHECK = re.compile(r"^(PASS|FAIL) (.*)$")
HEADER = re.compile(r"^== (.*)$")
VERDICT = re.compile(r"^(EXPLORATORY-VERDICT .*|controls: .*|failures: .*)$")
CLOSURE = re.compile(r"^(.+?): dim Z1=(\d+) Z2=(\d+) sum=(\d+)/(\d+) direct=(True|False) complete=(True|False) "
                     r"Z1=natural1:(True|False) Z2=natural2:(True|False)$")


def content(text):
    raw = text.split("\n")
    if raw and raw[-1] == "":
        raw.pop()
    items = []
    for n, l in enumerate(raw, 1):
        m = CHECK.match(l)
        if m:
            items.append({"line": n, "kind": "check", "status": m.group(1), "text": m.group(2)})
            continue
        m = HEADER.match(l)
        if m:
            items.append({"line": n, "kind": "header", "text": m.group(1)})
            continue
        m = VERDICT.match(l)
        if m:
            items.append({"line": n, "kind": "verdict", "text": m.group(1)})
            continue
        m = CLOSURE.match(l)
        if m:
            g = m.groups()
            items.append({"line": n, "kind": "record", "config": g[0], "dimZ1": int(g[1]), "dimZ2": int(g[2]),
                          "dimSum": int(g[3]), "dim": int(g[4]), "direct": g[5] == "True",
                          "complete": g[6] == "True", "Z1_natural": g[7] == "True", "Z2_natural": g[8] == "True"})
            continue
        items.append({"line": n, "kind": "record", "text": l})
    return {"lines": len(raw), "ends_with_newline": text.endswith("\n"), "items": items,
            "checks": {s: sum(1 for i in items if i.get("status") == s) for s in ("PASS", "FAIL")}}


def render(item):
    k = item["kind"]
    if k == "check":
        return "%s %s" % (item["status"], item["text"])
    if k == "header":
        return "== " + item["text"]
    if k == "verdict" or "text" in item:
        return item["text"]
    return "%s: dim Z1=%d Z2=%d sum=%d/%d direct=%s complete=%s Z1=natural1:%s Z2=natural2:%s" % (
        item["config"], item["dimZ1"], item["dimZ2"], item["dimSum"], item["dim"], item["direct"], item["complete"],
        item["Z1_natural"], item["Z2_natural"])


def extract(out_path, script_path):
    name = os.path.basename(out_path)[:-4]
    if name not in PINS:
        raise SystemExit("not a §13 output: %s" % out_path)
    data, script = open(out_path, "rb").read(), open(script_path, "rb").read()
    if hashlib.sha256(data).hexdigest() != PINS[name][0] or hashlib.sha256(script).hexdigest() != PINS[name][1]:
        raise SystemExit("%s or its script is not the file §13 pins" % name)
    c = content(data.decode("utf-8"))
    rebuilt = "\n".join(render(i) for i in c["items"]) + ("\n" if c["ends_with_newline"] else "")
    if rebuilt.encode("utf-8") != data:
        raise SystemExit("the extraction does not determine %s.out byte for byte" % name)
    return {
        "schema": "loc1-prior-expected", "version": 1, "name": name, "form": "derived",
        "holds_at": {"script": "prior/%s.py" % name, "script_sha256": PINS[name][1],
                     "note": "the script is copied byte for byte into prior/ at stage 1; the result holds for it"},
        "source": {"file": "%s.out" % name, "bytes": len(data), "sha256": PINS[name][0],
                   "note": "the digest is provenance of the extraction; the output is not copied (owner's artifact "
                           "ruling of 2026-10-18)"},
        "recipe": ["python3 -I -B %s.py > %s.out   (in a fresh copy of prior/; the script reads no file)" % (name, name),
                   "python3 -I -B prior_expected.py compare %s-expected.json %s.out" % (name, name)],
        "compared": "every line, in order; the rendering of the items reproduces the output byte for byte",
        "content": c,
    }


def compare(exp_path, out_path):
    exp = json.load(open(exp_path, encoding="utf-8"))
    data = open(out_path, "rb").read()
    got = content(data.decode("utf-8"))
    fails = []
    if got != exp["content"]:
        a, b = exp["content"]["items"], got["items"]
        diff = [i for i in range(max(len(a), len(b))) if i >= len(a) or i >= len(b) or a[i] != b[i]]
        fails.append("%d item(s) differ, first at item %d" % (len(diff), diff[0] if diff else -1))
    return fails


def dump(doc):
    return json.dumps(doc, indent=1, sort_keys=True, ensure_ascii=True) + "\n"


def self_test(srcdir):
    lines, ok = [], True

    def rep(name, passed, detail=""):
        nonlocal ok
        ok &= bool(passed)
        lines.append("%s %-62s %s" % ("PASS" if passed else "FAIL", name, detail))

    import tempfile
    for name in PINS:
        out, scr = os.path.join(srcdir, name + ".out"), os.path.join(srcdir, name + ".py")
        doc = extract(out, scr)
        d1, d2 = dump(doc), dump(extract(out, scr))
        rep("%s: extraction is deterministic" % name, d1 == d2, hashlib.sha256(d1.encode()).hexdigest()[:16])
        with tempfile.TemporaryDirectory() as t:
            e = os.path.join(t, name + "-expected.json")
            open(e, "w").write(d1)
            rep("%s: the pinned output compares equal" % name, not compare(e, out),
                "%d lines, %d PASS, %d FAIL" % (doc["content"]["lines"], doc["content"]["checks"]["PASS"],
                                                doc["content"]["checks"]["FAIL"]))
            text = open(out, encoding="utf-8").read()
            mut = os.path.join(t, name + ".out")
            open(mut, "w").write(text.replace("PASS", "FAIL", 1) if "PASS" in text else text.replace("True", "False", 1))
            rep("NEG %s: a changed status is detected" % name, bool(compare(e, mut)))
            lines_ = text.split("\n")
            open(mut, "w").write("\n".join(lines_[:-2] + lines_[-1:]))
            rep("NEG %s: a dropped line is detected" % name, bool(compare(e, mut)))
    lines.append("prior_expected self-test: %s" % ("ALL PASS" if ok else "FAILURE"))
    return ok, lines


def main(argv):
    if argv[:1] == ["extract"] and len(argv) == 3:
        sys.stdout.write(dump(extract(argv[1], argv[2])))
        return 0
    if argv[:1] == ["compare"] and len(argv) == 3:
        f = compare(argv[1], argv[2])
        print("prior_expected compare: %s" % ("; ".join(f) if f else "EQUAL"))
        return 1 if f else 0
    if argv[:1] == ["--self-test"] and len(argv) == 2:
        ok, lines = self_test(argv[1])
        print("\n".join(lines))
        return 0 if ok else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
