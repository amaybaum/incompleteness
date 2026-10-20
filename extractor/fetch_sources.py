#!/usr/bin/env python3
"""Fetch, without credentials, the commits the assembler reads: the two pinned extractor commits on main and each
target's commit from extractor/targets.json, into one new bare repository. Python 3 stdlib and git.

  python3 -I fetch_sources.py --objects DIR
  python3 -I fetch_sources.py --self-test [--work DIR]

For each commit C it runs, in DIR (created with `git init --bare`):
  git fetch --no-tags --no-recurse-submodules --depth=1 https://github.com/amaybaum/incompleteness.git C
and then checks that C is present as a commit. The repository is public, so no credential is used: GH_TOKEN and
GITHUB_TOKEN are removed from git's environment, system and global git configuration are ignored, the credential
helper and http.extraHeader are reset to empty on the command line, and terminal prompts are off. A commit is
fetched by its full 40-digit id only; nothing else is accepted. Nothing is checked out: the assembler reads blobs
with `git cat-file` and checks their ids. Exit 0 when every commit is present, 3 otherwise.

The extractor commits:
  main at 809fa9d6 (verification/audits/evidence-retention/extract_result.py, blob e6f69713): the extractor;
  main at b96662e6 (the same path, blob 05c41bce): the extractor the round's earlier records name, read as a
  cross-check of the governed modules, the gate, the build line and the markers.
"""
import argparse
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True  # never leave bytecode beside the sources
HERE = os.path.dirname(os.path.abspath(__file__))


def _load_targets_module():
    spec = importlib.util.spec_from_file_location("ktoken_targets", os.path.join(HERE, "targets.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


T = _load_targets_module()
URL = "https://github.com/amaybaum/incompleteness.git"
EXTRACTOR_COMMITS = ("809fa9d6fc931d7a75027ad72d6d2d4b03b722a5", "b96662e6be4f537502c772db369ea32a35b213a8")
SHA = re.compile(r"[0-9a-f]{40}\Z")
TIMEOUT_S = 300
SCRUB = ("GH_TOKEN", "GITHUB_TOKEN", "GIT_ASKPASS", "SSH_ASKPASS", "GIT_CONFIG_PARAMETERS", "GIT_CONFIG_COUNT")


class SourceError(Exception):
    pass


def git_env():
    env = {k: v for k, v in os.environ.items() if k not in SCRUB and not k.startswith("GIT_CONFIG_KEY_")
           and not k.startswith("GIT_CONFIG_VALUE_")}
    env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0", GIT_ASKPASS="/bin/false")
    return env


def git_cmd(objects, *args):
    return ["git", "-C", objects, "-c", "credential.helper=", "-c", "http.extraHeader=", "-c", "core.askPass=",
            "-c", "protocol.file.allow=user"] + list(args)


def run(cmd, runner=None):
    p = (runner or subprocess.run)(cmd, capture_output=True, timeout=TIMEOUT_S, env=git_env())
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def fetch(objects, commits, url=URL, runner=None):
    """Returns {commit: "ok" | reason}. objects must not exist yet."""
    for c in commits:
        if not isinstance(c, str) or not SHA.match(c):
            raise SourceError("refused: %r is not a full commit id" % (c,))
    if os.path.lexists(objects):
        raise SourceError("refused: %s exists" % objects)
    rc, _, err = run(["git", "init", "-q", "--bare", objects], runner)
    if rc:
        raise SourceError("git init failed: %s" % err.strip()[-200:])
    out = {}
    for c in dict.fromkeys(commits):
        rc, _, err = run(git_cmd(objects, "fetch", "-q", "--no-tags", "--no-recurse-submodules", "--depth=1", url, c),
                         runner)
        if rc:
            out[c] = "fetch failed (exit %d): %s" % (rc, (err.strip().splitlines() or [""])[-1][:200])
            continue
        rc, typ, _ = run(git_cmd(objects, "cat-file", "-t", c), runner)
        out[c] = "ok" if rc == 0 and typ.strip() == "commit" else "absent after fetch"
    return out


def all_commits(targets):
    return list(EXTRACTOR_COMMITS) + [t["commit"] for t in targets]


def self_test(work=None):
    base = tempfile.mkdtemp(prefix="sources-selftest-", dir=work)
    fails, n = 0, 0

    def case(name, ok):
        nonlocal fails, n
        n += 1
        fails += not ok
        print("  %s  %s" % ("ok  " if ok else "FAIL", name))
    try:
        src = os.path.join(base, "src")
        env = dict(git_env(), GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.invalid", GIT_COMMITTER_NAME="t",
                   GIT_COMMITTER_EMAIL="t@example.invalid")
        subprocess.run(["git", "init", "-q", src], check=True, env=env, capture_output=True)
        heads = []
        for i in range(3):
            with open(os.path.join(src, "f.txt"), "w") as f:
                f.write("v%d\n" % i)
            subprocess.run(["git", "-C", src, "add", "-A"], check=True, env=env, capture_output=True)
            subprocess.run(["git", "-C", src, "-c", "commit.gpgsign=false", "commit", "-q", "-m", "c%d" % i],
                           check=True, env=env, capture_output=True)
            heads.append(subprocess.run(["git", "-C", src, "rev-parse", "HEAD"], check=True, env=env,
                                        capture_output=True, text=True).stdout.strip())
        # allow fetching a reachable non-tip commit by id, as GitHub does
        subprocess.run(["git", "-C", src, "config", "uploadpack.allowReachableSHA1InWant", "true"], check=True, env=env)
        url = "file://" + src
        objs = os.path.join(base, "o1")
        res = fetch(objs, [heads[0], heads[2], heads[0]], url)
        case("two commits (one listed twice) are fetched by id, the older one not a branch tip",
             res == {heads[0]: "ok", heads[2]: "ok"})
        rc, body, _ = run(git_cmd(objs, "cat-file", "blob", heads[0] + ":f.txt"))
        case("a fetched commit's blob is readable with cat-file", rc == 0 and body == "v0\n")
        rc, _, _ = run(git_cmd(objs, "rev-parse", "--verify", "-q", "refs/heads/master"))
        case("no branch is created in the bare repository", rc != 0)
        res = fetch(os.path.join(base, "o2"), ["0" * 40], url)
        case("an unknown commit is reported, not raised", res["0" * 40].startswith("fetch failed"))
        for bad in ("e12c1573", "E" * 40, "--upload-pack=x", heads[0] + "\n"):
            try:
                fetch(os.path.join(base, "o3"), [bad], url)
                ok = False
            except SourceError:
                ok = not os.path.exists(os.path.join(base, "o3"))
            case("refused before any command: %r" % bad[:20], ok)
        try:
            fetch(objs, [heads[0]], url)
            ok = False
        except SourceError:
            ok = True
        case("an existing objects directory is refused", ok)
        saved = {k: os.environ.get(k) for k in ("GH_TOKEN", "GITHUB_TOKEN")}
        os.environ["GH_TOKEN"], os.environ["GITHUB_TOKEN"] = "tok-a", "tok-b"
        seen = []

        def spy(cmd, **kw):
            seen.append((cmd, kw.get("env") or {}))
            return subprocess.CompletedProcess(cmd, 0, b"commit\n", b"")
        try:
            fetch(os.path.join(base, "o4"), [heads[1]], URL, spy)
        finally:
            for k, v in saved.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v
        f_cmds = [c for c, _ in seen if "fetch" in c]
        case("the fetch carries no token: GH_TOKEN and GITHUB_TOKEN are removed from git's environment",
             seen and all("GH_TOKEN" not in e and "GITHUB_TOKEN" not in e for _, e in seen)
             and not any("tok-" in " ".join(c) for c, _ in seen))
        case("credential helper and extra headers are reset, global and system config ignored, prompts off",
             f_cmds and all("credential.helper=" in c and "http.extraHeader=" in c for c in f_cmds)
             and all(e.get("GIT_CONFIG_NOSYSTEM") == "1" and e.get("GIT_CONFIG_GLOBAL") == os.devnull
                     and e.get("GIT_TERMINAL_PROMPT") == "0" for _, e in seen))
        case("production fetches name only the public repository URL and a full commit id, depth 1",
             f_cmds and all(c[-2] == URL and SHA.match(c[-1]) and "--depth=1" in c for c in f_cmds))
        targets = T.load()["targets"]
        case("the commit list is the two extractor commits and exactly the listed targets' commits",
             all_commits(targets) == list(EXTRACTOR_COMMITS) + [t["commit"] for t in targets])
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print("sources self-test: %d of %d cases ok" % (n - fails, n))
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--objects")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--work")
    a = ap.parse_args(argv)
    try:
        targets = T.load()["targets"]
    except T.TargetsError as e:
        print("sources refused: %s" % e)
        return 3
    if a.self_test:
        return 1 if self_test(a.work) else 0
    if not a.objects:
        ap.error("--objects is required")
    try:
        res = fetch(a.objects, all_commits(targets))
    except (SourceError, subprocess.TimeoutExpired) as e:
        print("sources failed: %s: %s" % (type(e).__name__, str(e)[:300]))
        return 3
    for c, r in res.items():
        print("source %s %s" % (c, r))
    return 0 if all(r == "ok" for r in res.values()) else 3


if __name__ == "__main__":
    sys.exit(main())
