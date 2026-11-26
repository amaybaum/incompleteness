import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gate2
from gate import Halted
B = "/tmp/claude-0/-home-user-incompleteness/8a0f23ba-ffa7-50df-a785-676e090e9917/scratchpad/board"
class Gh:
    def request(self, method, path, payload):
        args = ["gh", "api", "-i", "-X", method, path]; inp = None
        if payload is not None:
            args += ["--input", "-"]; inp = json.dumps(payload)
        r = subprocess.run(args, input=inp, capture_output=True, text=True); out = r.stdout
        head, _, body = out.partition("\r\n\r\n") if "\r\n\r\n" in out else out.partition("\n\n")
        if not head.startswith("HTTP"): raise RuntimeError("no status line rc=%d" % r.returncode)
        return int(head.split()[1]), (json.loads(body) if body.strip() else None)
class NoGit:
    def run(self, a): raise RuntimeError("no git")
    def remote_sha(self, *a): raise RuntimeError("no git")
    def is_ancestor(self, *a): raise RuntimeError("no git")
halt = os.path.join(HERE, "halt"); reg = json.load(open(os.path.join(HERE, "registry-v2.json")))["operations"]
pid = "board-planning-blocks-20261126"; gate2.record_plan(halt, pid); log = []
g = gate2.Gate2(Gh(), NoGit(), halt, "amaybaum/incompleteness", reg, evidence_dir=HERE, log=log, plan_id=pid)
rc = 0
for n in [int(x) for x in sys.argv[1:]]:
    before = open(f"{B}/{n}.before2.md", encoding="utf-8", newline="").read()
    after = open(f"{B}/{n}.after2.md", encoding="utf-8", newline="").read()
    cur = subprocess.run(["gh","api",f"repos/amaybaum/incompleteness/issues/{n}","--jq",".body"],capture_output=True,text=True).stdout
    if cur.endswith("\n"): cur = cur[:-1]
    if cur != before: print(n, "SKIP: current body differs from before2"); rc = 5; break
    try:
        stored, outcomes, records = g.write("issue.edit_body", n, {"body": after})
        open(os.path.join(HERE, f"{n}.stored.md"), "w", encoding="utf-8", newline="").write(stored["body"])
        print(n, "OUTCOMES", json.dumps(outcomes), "RECORDS", json.dumps(records))
    except gate2.Refused as e: print(n, "REFUSED:", e); rc = 4; break
    except Halted as e: print(n, "HALTED:", e); rc = 3; break
json.dump(log, open(os.path.join(HERE, "gate-log.json"), "w"), indent=1, default=str)
sys.exit(rc)
