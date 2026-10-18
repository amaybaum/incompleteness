"""Builds LOC-1's predicted stage-1 record directory from git objects, and checks it with K-obj, K-design and K-prior
(research development; preregistration §12, stage 1).

Every file is read with `git cat-file` from an exact (commit, path), never from a working copy:

    preregistration.md   PREREG_COMMIT (the control plane the tree is predicted for)
    objects/<copy>       §2.1's source commit and research-planning/<copy>
    design/<file>        §9's rows: the working-material commit's preflight files (the two retained outputs from
                         its run1/), and any further row from the dev commit's loc-1-arith/
    prior/<file>         §13's copied rows: the scripts from the working-material commit, the expected results from
                         the dev commit's loc-1-controls/prior-expected/
    code/<file>          the round's code under development, from the dev commit's loc-1-controls/ (not yet pinned)

retained/F/ cannot exist before F and is not predicted.  Nothing in the tree is executed.

Run:  python3 -I -B build_predicted_tree.py REPO PREREG_COMMIT DEV_COMMIT OUT_DIR
      prints each file with its source, then the K-obj, K-design and K-prior verdicts, and, with REPO's object
      store, the git tree id of the predicted record directory (written to a scratch object store under OUT_DIR)
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import controls  # noqa: E402

RECORD = "verification/programmes/oi-qm/track-b/round-loc-1-identification-dependence"
RP = "verification/programmes/oi-qm/track-b/research-planning"
WORKING = "08c336263cf871632d4129a45aa43f79cb44e73c"       # tmp/loc1-working-material-20261017
RUN1_OUTPUTS = {"c21_search.out", "c21_witness.json"}
PRIOR_SRC = {"decomposition_probe.py": "loc1-working-material/prior/thread-b-explore/decomposition_probe.py",
             "closure_design.py": "loc1-working-material/prior/thread-b-explore/closure_design.py",
             "factorization_check.py": "loc1-working-material/prior/factorization-check/factorization_check.py"}
CODE = ("controls.py", "clq.py", "p0_roundtrip.py", "prior_expected.py", "retain_run.py", "build_predicted_tree.py")


def git(repo, *a, binary=False):
    r = subprocess.run(["git", "-C", repo] + list(a), capture_output=True)
    if r.returncode:
        raise SystemExit("git %s: %s" % (" ".join(a), r.stderr.decode()))
    return r.stdout if binary else r.stdout.decode()


def blob(repo, commit, path):
    return git(repo, "cat-file", "blob", "%s:%s" % (commit, path), binary=True)


def build(repo, prereg_commit, dev_commit, out):
    rec = os.path.join(out, "record")
    if os.path.exists(rec):
        raise SystemExit("%s exists" % rec)
    text = blob(repo, prereg_commit, RECORD + "/preregistration.md")
    obj, design, prior = controls.tables(text.decode("utf-8"))
    plan = [("preregistration.md", prereg_commit, RECORD + "/preregistration.md")]
    for r in obj:
        plan.append(("objects/" + r["file"], r["commit"], RP + "/" + r["file"]))
    for r in design:
        f = r["file"]
        if f in RUN1_OUTPUTS:
            plan.append(("design/" + f, WORKING, "loc1-working-material/preflight/run1/" + f))
        elif f.startswith("runs/"):
            plan.append(("design/" + f, dev_commit, RP + "/loc-1-controls/design-runs/" + f[5:]))
        else:
            try:
                git(repo, "cat-file", "-e", "%s:loc1-working-material/preflight/%s" % (WORKING, f))
                plan.append(("design/" + f, WORKING, "loc1-working-material/preflight/" + f))
            except SystemExit:
                for sub in ("loc-1-arith", "loc-1-controls"):
                    try:
                        git(repo, "cat-file", "-e", "%s:%s/%s/%s" % (dev_commit, RP, sub, f))
                    except SystemExit:
                        continue
                    plan.append(("design/" + f, dev_commit, RP + "/" + sub + "/" + f))
                    break
                else:
                    raise SystemExit("no source for design/%s" % f)
    for r in controls.copied_prior(prior):
        f = r["file"]
        if f in PRIOR_SRC:
            plan.append(("prior/" + f, WORKING, PRIOR_SRC[f]))
        else:
            plan.append(("prior/" + f, dev_commit, RP + "/loc-1-controls/prior-expected/" + f))
    pinned = {r["file"] for r in design}
    for f in CODE:
        if f not in pinned:                               # a file pinned in design/ is not copied twice
            plan.append(("code/" + f, dev_commit, RP + "/loc-1-controls/" + f))
    for dst, c, src in plan:
        p = os.path.join(rec, dst)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "wb").write(blob(repo, c, src))
    return rec, plan


def tree_id(repo, rec, scratch):
    """The git tree id of the record directory, computed in a scratch object store that borrows REPO's objects."""
    env = dict(os.environ, GIT_DIR=scratch, GIT_INDEX_FILE=os.path.join(scratch, "index"))
    if not os.path.isdir(scratch):
        subprocess.run(["git", "init", "-q", "--bare", scratch], check=True, capture_output=True)
        objs = subprocess.run(["git", "-C", repo, "rev-parse", "--git-path", "objects"], capture_output=True,
                              text=True).stdout.strip()
        with open(os.path.join(scratch, "objects", "info", "alternates"), "w") as fh:
            fh.write(os.path.abspath(os.path.join(repo, objs)) + "\n")
    subprocess.run(["git", "read-tree", "--empty"], env=env, check=True)
    for root, _, fs in os.walk(rec):
        for f in sorted(fs):
            p = os.path.join(root, f)
            h = subprocess.run(["git", "hash-object", "-w", p], env=env, capture_output=True, text=True,
                               check=True).stdout.strip()
            rel = os.path.relpath(p, rec).replace(os.sep, "/")
            subprocess.run(["git", "update-index", "--add", "--cacheinfo", "100644,%s,%s" % (h, rel)], env=env,
                           check=True)
    return subprocess.run(["git", "write-tree"], env=env, capture_output=True, text=True, check=True).stdout.strip()


def main(argv):
    if len(argv) != 4:
        print(__doc__)
        return 2
    repo, pc, dc, out = argv
    rec, plan = build(repo, pc, dc, out)
    for dst, c, src in plan:
        print("%-52s %s:%s" % (dst, c[:12], src))
    res = controls.check_record(rec)
    for name, ok, det in res:
        print("%s %-9s %s" % ("PASS" if ok else "FAIL", name, "; ".join(det[:6])))
    print("predicted record directory tree %s" % tree_id(repo, rec, os.path.join(out, "scratch.git")))
    return 0 if all(r[1] for r in res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
