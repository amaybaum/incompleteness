"""Second validation write on #1548: canonical footer separator. One owner-granted write."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "write-safety"))
from gate import Gate, Halted, canonical_footer_body


class Gh:
    def request(self, method, path, payload):
        args = ["gh", "api", "-i", "-X", method, path]; inp = None
        if payload is not None:
            args += ["--input", "-"]; inp = json.dumps(payload)
        r = subprocess.run(args, input=inp, capture_output=True, text=True); out = r.stdout
        head, _, body = out.partition("\r\n\r\n") if "\r\n\r\n" in out else out.partition("\n\n")
        if not head.startswith("HTTP"):
            raise RuntimeError("no status line rc=%d" % r.returncode)
        return int(head.split()[1]), (json.loads(body) if body.strip() else None)


class NoGit:
    def run(self, a): raise RuntimeError("no git")
    def remote_sha(self, *a): raise RuntimeError("no git")
    def is_ancestor(self, *a): raise RuntimeError("no git")


draft = open(os.path.join(HERE, "draft-noncanonical.md"), encoding="utf-8", newline="").read()
expected = open(os.path.join(HERE, "expected-body.md"), encoding="utf-8", newline="").read()
assert canonical_footer_body(draft) == expected
reg = {"issue.edit_body": {"validated": False, "send_form": "footer"}}
log = []
g = Gate(Gh(), NoGit(), sys.argv[1], "amaybaum/incompleteness", reg,
         evidence_dir=os.path.dirname(sys.argv[1]), log=log)
g.grant_single_write("issue.edit_body", 1548)
try:
    st = g.write("issue.edit_body", 1548, {"body": expected})
    with open(os.path.join(HERE, "stored-body.md"), "w", encoding="utf-8", newline="") as f:
        f.write(st["body"])
    print("VALIDATION PASS", st.get("updated_at")); rc = 0
except Halted as e:
    print("HALTED:", e); rc = 3
with open(os.path.join(HERE, "gate-log.json"), "w") as f:
    json.dump(log, f, indent=1)
sys.exit(rc)
