"""Write gate v2 prototype: exact read-back plus a bounded transport-difference allowlist.

Prototype only, mock transport only; not adopted. gate.py stays the operational mechanism until
the owner approves a replacement. This module reuses gate.py by import (operations, pre-checks,
refspec checks, push path, read-back paths, grants) and adds:

  * content-integrity verification separated from transport-difference detection: the gate fixes
    and hashes the expected text (the text sent) before the write and compares the stored text
    byte for byte; only when they differ does it ask transport_rules.classify whether exactly one
    owner-adopted rule permits the difference. The gate itself knows no transformation and carries
    no footer formatting;
  * outcomes: "exact" -> accepted; "permitted" -> accepted, with a discrepancy record (complete
    sent and stored texts, SHA-256 of each, unified and character-level diff, rule id and version,
    time) written to the evidence directory; "rejected" -> halt, with sent, stored and diff kept;
  * per-mechanism halt markers: HALT.<operation> (and HALT.push) block only that mechanism; the
    global marker HALT (the same name gate.py uses) blocks every mechanism and is written for
    failures not attributable to one operation (an unknown operation). Markers are checked before
    anything else, created exclusively, never overwritten and never removed by the gate.
"""
import difflib, hashlib, itertools, json, os, re, time

import gate as G
import transport_rules as TR
from gate import OPERATIONS, Halted, precheck_text, check_refspec, run_plan, main  # noqa: F401

GLOBAL_MARKER = "HALT"
_seq = itertools.count()


def sha256(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def unified(sent, stored):
    """Line diff of the exact texts; a last line without newline is marked as diff(1) marks it."""
    def lines(t):
        ls = t.splitlines(keepends=True)
        if ls and not ls[-1].endswith("\n"):
            ls[-1] += "\n\\ No newline at end of file\n"
        return ls
    return "".join(difflib.unified_diff(lines(sent), lines(stored), "sent", "stored", n=3))


def char_opcodes(sent, stored):
    """Exact character-level edit script: applying it to sent reproduces stored."""
    sm = difflib.SequenceMatcher(None, sent, stored, autojunk=False)
    return [[tag, i1, i2, j1, j2, sent[i1:i2], stored[j1:j2]]
            for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != "equal"]


class Result(tuple):
    """(stored, outcomes, records): outcomes maps field -> [classification, rule_id]."""
    __slots__ = ()

    def __new__(cls, stored, outcomes, records):
        return tuple.__new__(cls, (stored, outcomes, records))
    stored = property(lambda s: s[0])
    outcomes = property(lambda s: s[1])
    records = property(lambda s: s[2])


class Gate2(G.Gate):
    def __init__(self, transport, git, halt_dir, repo, registry, allowed_branches=(),
                 evidence_dir=None, log=None, rules=None):
        super().__init__(transport, git, os.path.join(halt_dir, GLOBAL_MARKER), repo, registry,
                         allowed_branches, evidence_dir or halt_dir, log)
        self.halt_dir = halt_dir
        self.rules = TR.REGISTRY if rules is None else rules
        self._mech = None

    # -- per-mechanism halt ---------------------------------------------------------------------
    def marker_path(self, mech):
        if mech is None:
            return self.halt_path
        if mech != "push" and mech not in OPERATIONS:
            raise ValueError("unknown mechanism %r" % (mech,))
        return os.path.join(self.halt_dir, "HALT." + mech)

    def _check_clear(self):
        for p in (self.halt_path, self.marker_path(self._mech)):
            if os.path.lexists(p):
                raise Halted("halt marker present: %s" % os.path.basename(p))

    def _halt(self, reason, **evidence):
        mech = self._mech
        tag = "%s-%d-%d" % (mech or "global", os.getpid(), next(_seq))
        rec = {"reason": reason, "mechanism": mech or "global", "pid": os.getpid(),
               "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        ev = {}
        for k, v in evidence.items():
            if isinstance(v, str):
                name = "halt-%s-%s.txt" % (tag, k)
                try:
                    fd = os.open(os.path.join(self.evidence_dir, name),
                                 os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
                    with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
                        f.write(v)
                    ev[k] = {"file": name, "sha256": sha256(v)}
                except OSError as e:     # evidence is best effort; the halt itself is not
                    ev[k] = {"file": None, "sha256": sha256(v), "error": str(e)}
            else:
                ev[k] = v
        rec["evidence"] = ev
        try:   # O_EXCL: never overwrite an earlier marker, which records the first failure
            fd = os.open(self.marker_path(mech), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
            with os.fdopen(fd, "w") as f:
                json.dump(rec, f, indent=1, sort_keys=True)
                f.flush()
                os.fsync(f.fileno())
        except FileExistsError:
            pass
        raise Halted(reason)

    # -- outcome decision (separate from transport-difference detection) -----------------------
    def _decide(self, op, target, field, sent, stored):
        """Classify one sent field against its stored text; halt on anything but exact/permitted."""
        try:
            cls, rule_id = TR.classify(sent, stored, self.rules, field)
        except BaseException as e:
            self._halt("classification failed for %s of %s %s: %s: %s"
                       % (field, op, target, type(e).__name__, e), sent=sent,
                       stored=stored if isinstance(stored, str) else repr(stored))
        if cls == "exact":
            return cls, None
        if cls == "permitted":
            return cls, rule_id
        self._halt("read-back mismatch in %s of %s %s (rejected: no permitted transformation)"
                   % (field, op, target), sent=sent,
                   stored=stored if isinstance(stored, str) else repr(stored),
                   diff=unified(sent, stored) if isinstance(stored, str) else "")

    def _record(self, op, target, field, sent, stored, rule_id):
        rule = TR.rule_by_id(rule_id, self.rules)
        rec = {"kind": "permitted-transport-difference", "operation": op, "target": target,
               "field": field, "repo": self.repo,
               "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "rule_id": rule.id, "rule_version": rule.version,
               "rule_description": rule.description,
               "sent": sent, "stored": stored,
               "sent_sha256": sha256(sent), "stored_sha256": sha256(stored),
               "sent_bytes": len(sent.encode("utf-8")), "stored_bytes": len(stored.encode("utf-8")),
               "unified_diff": unified(sent, stored),
               "char_opcodes": char_opcodes(sent, stored)}
        name = "discrepancy-%s-%s-%s-%d-%d.json" % (op, target, field, os.getpid(), next(_seq))
        path = os.path.join(self.evidence_dir, name)
        try:
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(rec, f, indent=1, sort_keys=True, ensure_ascii=False)
                f.flush()
                os.fsync(f.fileno())
        except BaseException as e:      # an accepted difference without its record is not accepted
            self._halt("discrepancy record could not be written: %s: %s" % (type(e).__name__, e),
                       sent=sent, stored=stored)
        return path

    # -- text writes ---------------------------------------------------------------------------
    def write(self, op, target=None, fields=None, labels=None, label=None):
        """Perform exactly one write. Returns Result(stored, outcomes, records); raises Halted."""
        self._mech = None
        self._check_clear()                       # global marker first
        spec, reg = OPERATIONS.get(op), self.registry.get(op)
        if spec is None or reg is None:
            self._halt("unknown operation %r" % (op,))       # global: no mechanism to contain
        self._mech = op
        self._check_clear()                       # this mechanism's marker, before any request
        fields = dict(fields or {})
        key = (op, str(target))
        if not reg.get("validated"):
            if key not in self.grants:
                self._halt("operation %s is not validated and has no single-write grant" % op)
            self.grants.discard(key)              # consumed before the write
        if set(fields) != set(spec["text"]):
            self._halt("fields %s do not match operation %s" % (sorted(fields), op))
        for k, v in fields.items():
            bad = precheck_text(v)
            if isinstance(v, str):
                bad += TR.send_form_violations(reg.get("send_form"), v, k)
            if bad:
                self._halt("pre-check refused field %s: %s" % (k, "; ".join(bad)),
                           sent=v if isinstance(v, str) else repr(v))
        # Expected stored text: the text sent, frozen and hashed now. No normalization.
        expected = {k: v.encode("utf-8") for k, v in fields.items()}
        digests = {k: hashlib.sha256(b).hexdigest() for k, b in expected.items()}
        path = "repos/%s/%s" % (self.repo, spec["path"].format(n=target, label=label))
        payload = dict(fields)
        if op == "issue.close":
            payload = {"state": "closed", "state_reason": "completed"}
        if op == "labels.add":
            payload = {"labels": list(labels or [])}
        before = None
        if spec["method"] in ("PATCH", "DELETE") or op == "labels.add":
            before = self._get(self._readback_path(op, target))
        self.log.append(("write", op, str(target), digests))
        try:
            status, resp = self.t.request(spec["method"], path, payload)
        except BaseException as e:
            self._halt("unknown outcome: %s: %s" % (type(e).__name__, e))
        if status not in spec["ok"]:
            self._halt("unexpected status %r for %s" % (status, op))
        rb_target = (resp or {}).get(spec["created"]) if "created" in spec else target
        if "created" in spec and not (isinstance(rb_target, int) and rb_target > 0):
            rb_target = None
        if rb_target is None:
            self._halt("unknown outcome: no created object id in response")
        stored = self._get(self._readback_path(op, rb_target))
        outcomes, records = {}, []
        for k in sorted(expected):
            sent = expected[k].decode("utf-8")    # the frozen expected text, not the live dict
            got = stored.get(k)
            if isinstance(got, str) and got.encode("utf-8") == expected[k]:
                outcomes[k] = ["exact", None]
                continue
            cls, rule_id = self._decide(op, rb_target, k, sent, got)
            outcomes[k] = [cls, rule_id]
            if cls == "permitted":
                records.append(self._record(op, rb_target, k, sent, got, rule_id))
        if before is not None:          # fields not sent must be byte-identical: no allowlist
            for k in ("title", "body"):
                if k not in expected and before.get(k) != stored.get(k):
                    self._halt("unsent field %s changed by %s %s" % (k, op, rb_target),
                               sent=str(before.get(k)), stored=str(stored.get(k)))
        if op == "issue.close" and stored.get("state") != "closed":
            self._halt("state read-back is not closed")
        if op in ("labels.add", "labels.remove"):
            names = sorted(x["name"] for x in stored.get("labels", []))
            want = set(x["name"] for x in before.get("labels", []))
            want = want | set(labels or []) if op == "labels.add" else want - {label}
            if names != sorted(want):
                self._halt("label read-back mismatch: %s != %s" % (names, sorted(want)))
        return Result(stored, outcomes, records)

    # -- pushes: gate.py's path and guards, contained under the "push" mechanism ---------------
    def push(self, remote, sha, branch_ref):
        self._mech = None
        self._check_clear()
        self._mech = "push"
        return super().push(remote, sha, branch_ref)
