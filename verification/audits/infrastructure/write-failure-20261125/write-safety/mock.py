"""Mock GitHub transport and mock git runner. No network, no subprocess."""
import copy
from gate import FOOTER


class MockGitHub:
    """modes: 'verbatim'; 'append_if_absent' (the D1 behaviour on text fields named body);
    'append_on_close' (injects the footer into body on a state-only PATCH); 'raise_on_write';
    'status_500'; 'readback_fail_after_write'; 'readback_404'; 'canonicalize_separator' (the
    #1505 behaviour: whitespace before the footer reduced to its two-newline separator)."""

    def __init__(self, issues=None, mode="verbatim"):
        self.issues = copy.deepcopy(issues or {})
        self.mode = mode
        self.writes = []          # every non-GET request that reached the transport
        self.gets = 0
        self.next_number = 9000

    def _alter(self, body):
        if self.mode == "append_if_absent" and not body.endswith(FOOTER):
            return body + FOOTER
        if self.mode == "canonicalize_separator":   # the behaviour observed at #1505
            t = body.rstrip()
            core = FOOTER[2:]
            if t.endswith(core):
                t = t[: -len(core)].rstrip()
            return t + FOOTER
        return body

    def request(self, method, path, payload):
        if method == "GET":
            self.gets += 1
            if self.mode == "readback_fail_after_write" and self.writes:
                raise ConnectionError("read-back connection reset")
            if self.mode == "readback_404" and self.writes:
                return 404, {"message": "Not Found"}
            n = int(path.rstrip("/").split("/")[-1])
            return 200, copy.deepcopy(self.issues[n])
        self.writes.append((method, path, copy.deepcopy(payload)))
        if self.mode == "raise_on_write":
            raise TimeoutError("timed out after sending")
        if self.mode == "status_500":
            return 500, {"message": "error"}
        parts = path.split("/")
        if method == "POST" and parts[-1] in ("issues", "pulls"):
            n = self.next_number; self.next_number += 1
            self.issues[n] = {"number": n, "title": payload["title"],
                              "body": self._alter(payload["body"]), "labels": [], "state": "open"}
            return 201, {"number": n}
        if method == "POST" and parts[-1] == "comments":
            n = self.next_number; self.next_number += 1
            self.issues[n] = {"id": n, "body": self._alter(payload["body"])}
            return 201, {"id": n}
        if method == "POST" and parts[-1] == "labels":
            n = int(parts[-2]); iss = self.issues[n]
            for l in payload["labels"]:
                if l not in [x["name"] for x in iss["labels"]]:
                    iss["labels"].append({"name": l})
            return 200, iss["labels"]
        if method == "DELETE":
            n = int(parts[-3]); iss = self.issues[n]
            iss["labels"] = [x for x in iss["labels"] if x["name"] != parts[-1]]
            return 200, iss["labels"]
        if method == "PATCH":
            n = int(parts[-1]); iss = self.issues[n]
            if "body" in payload:
                iss["body"] = self._alter(payload["body"])
            if "title" in payload:
                iss["title"] = payload["title"]
            if "state" in payload:
                iss["state"] = payload["state"]
                if self.mode == "append_on_close" and not iss["body"].endswith(FOOTER):
                    iss["body"] += FOOTER
            return 200, {"number": n}
        raise AssertionError("unmodelled request %s %s" % (method, path))

    # comment read-back uses issues/<id> in this mock; real comments read back at
    # issues/comments/<id>. The gate's read-back path per operation is part of validation.


class MockGit:
    def __init__(self, refs=None, ancestors=(), rc=0, raise_on_run=False, lie=False):
        self.refs = dict(refs or {})
        self.ancestors = set(ancestors)
        self.rc, self.raise_on_run, self.lie = rc, raise_on_run, lie
        self.runs = []

    def remote_sha(self, remote, ref):
        return self.refs.get(ref)

    def is_ancestor(self, old, new):
        return (old, new) in self.ancestors

    def run(self, argv):
        self.runs.append(list(argv))
        if self.raise_on_run:
            raise OSError("connection lost")
        if self.rc == 0 and not self.lie:
            sha, ref = argv[-1].split(":")
            self.refs[ref] = sha
        return self.rc
