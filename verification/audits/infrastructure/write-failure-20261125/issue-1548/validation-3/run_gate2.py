"""Controlled validation write of gate v2 (PROTOCOL-v2 sec. 7) on #1548. One owner-granted write."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "write-safety"))
import gate2
from gate import Halted


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


halt = os.path.join(HERE, "halt")
sent = open(os.path.join(HERE, "sent-body.md"), encoding="utf-8", newline="").read()
reg = {"issue.edit_body": {"validated": False, "send_form": None}}
log = []
gate2.record_plan(halt, "validation-1548-v2")
g = gate2.Gate2(Gh(), NoGit(), halt, "amaybaum/incompleteness", reg, evidence_dir=HERE, log=log,
                plan_id="validation-1548-v2")
g.grant_single_write("issue.edit_body", 1548)
rc = 3
try:
    res = g.write("issue.edit_body", 1548, {"body": sent})
    stored, outcomes, records = res
    with open(os.path.join(HERE, "stored-body.md"), "w", encoding="utf-8", newline="") as f:
        f.write(stored["body"])
    print("OUTCOMES", json.dumps(outcomes), "RECORDS", json.dumps(records))
    rc = 0
except gate2.Refused as e:
    print("REFUSED:", e); rc = 4
except Halted as e:
    print("HALTED:", e)
with open(os.path.join(HERE, "gate-log.json"), "w") as f:
    json.dump(log, f, indent=1, default=str)
sys.exit(rc)
