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
  * two levels of containment (AGENTS.md section A.49 rule 3 as amended in PR #1566):
      - run level: a sequence is one Gate2 instance and, beyond it, the whole writer process. After
        any Halted, and after any exception during a write or push, the instance and every other
        Gate2 instance in the process refuse every further write and push, whatever the caller
        does with the exception. Nothing in this module clears that latch;
      - beyond the run: the global marker HALT (the same name gate.py uses), which stops every
        mechanism for every later process using the halt directory, is written for every failure
        except a read-back mismatch for which every condition of rule 3 holds: the outcome is known,
        read-back succeeded with no unsent-field, label or state failure, every rejected field
        difference is tail-confined (transport_rules.tail_confined), and no other operation's
        marker is outstanding. Only then is the marker HALT.<operation> written instead, which
        blocks that operation alone;
  * a later sequence writes nothing while any operation marker lacks its companion file
    HALT.<operation>.notified, which a person creates by hand once the evidence is kept and the
    owner has been told (rule 3); the gate never creates it;
  * discrepancy records are written only after every field and check of the write has passed;
  * a halt marker embeds the complete evidence texts, so a failed evidence-file write loses none.
    Markers are checked before anything else, created exclusively, never overwritten and never
    removed by the gate. The check of a marker and the write that follows are not atomic across
    processes.
"""
import difflib, hashlib, itertools, json, os, re, time

import gate as G
import transport_rules as TR
from gate import OPERATIONS, Halted, precheck_text, check_refspec, run_plan, main  # noqa: F401

GLOBAL_MARKER = "HALT"
NOTIFIED_SUFFIX = ".notified"
_seq = itertools.count()
# Run-level latch for this writer process: one entry per halt. Any entry stops every Gate2 instance
# in the process. There is no function that clears it.
_SEQUENCE_STOP = []


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
        self._stopped = None

    # -- run-level containment -------------------------------------------------------------------
    def _check_sequence(self):
        """Refuse every write and push once this sequence (instance or process) has halted."""
        if self._stopped is not None or _SEQUENCE_STOP:
            raise Halted("sequence stopped after an earlier halt: %s"
                         % (self._stopped if self._stopped is not None else _SEQUENCE_STOP[0]))

    def _latch(self, reason):
        if self._stopped is None:
            self._stopped = reason
        _SEQUENCE_STOP.append(reason)

    def _guarded(self, what, fn):
        self._check_sequence()
        try:
            return fn()
        except Halted as e:
            self._latch(str(e))
            raise
        except BaseException as e:     # anything else during a write: outcome unknown
            self._latch("%s: %s" % (type(e).__name__, e))
            self._mech = None
            self._halt("unknown outcome: exception during %s: %s: %s" % (what, type(e).__name__, e))

    # -- markers ---------------------------------------------------------------------------------
    def marker_path(self, mech):
        if mech is None:
            return self.halt_path
        if mech != "push" and mech not in OPERATIONS:
            raise ValueError("unknown mechanism %r" % (mech,))
        return os.path.join(self.halt_dir, GLOBAL_MARKER + "." + mech)

    def _operation_markers(self):
        """Names of the operation markers present: every HALT.<x> except the .notified files."""
        return sorted(n for n in os.listdir(self.halt_dir)
                      if n.startswith(GLOBAL_MARKER + ".") and not n.endswith(NOTIFIED_SUFFIX))

    def _check_clear(self):
        for p in (self.halt_path, self.marker_path(self._mech)):
            if os.path.lexists(p):
                raise Halted("halt marker present: %s" % os.path.basename(p))
        try:
            pending = [n for n in self._operation_markers()
                       if not os.path.lexists(os.path.join(self.halt_dir, n + NOTIFIED_SUFFIX))]
        except OSError as e:
            raise Halted("halt directory unreadable: %s" % e)
        if pending:
            raise Halted("owner not yet told of the halt recorded in %s (no %s file)"
                         % (pending[0], pending[0] + NOTIFIED_SUFFIX))

    def _halt(self, reason, scope=None, **evidence):
        """Latch the sequence, keep the evidence, write the marker, raise Halted.
        scope None: the global marker. scope <operation>: that operation's marker only; passed
        solely by _containment_scope's decision."""
        self._latch(reason)
        mech = scope
        tag = "%s-%d-%d" % (mech or "global", os.getpid(), next(_seq))
        rec = {"reason": reason, "scope": "operation" if mech else "global",
               "mechanism": mech or "global", "pid": os.getpid(),
               "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        if mech:
            rec["resume"] = ("later sequences write nothing until %s exists, created by hand once "
                             "the evidence is kept and the owner told; this operation stays "
                             "suspended until a recorded owner decision" % (
                                 GLOBAL_MARKER + "." + mech + NOTIFIED_SUFFIX))
        ev = {}
        for k, v in evidence.items():
            if isinstance(v, str):
                name = "halt-%s-%s.txt" % (tag, k)
                ev[k] = {"file": name, "sha256": sha256(v), "text": v}
                try:
                    fd = os.open(os.path.join(self.evidence_dir, name),
                                 os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
                    with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
                        f.write(v)
                except OSError as e:     # the text stays embedded in the marker
                    ev[k]["file"] = None
                    ev[k]["error"] = str(e)
            else:
                ev[k] = v
        rec["evidence"] = ev
        try:   # O_EXCL: never overwrite an earlier marker, which records the first failure
            fd = os.open(self.marker_path(mech), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(rec, f, indent=1, sort_keys=True, ensure_ascii=False)
                f.flush()
                os.fsync(f.fileno())
        except FileExistsError:
            pass
        except OSError as e:          # the sequence is latched whatever happens to the marker
            reason = "%s (marker not written: %s)" % (reason, e)
        raise Halted(reason)

    # -- outcome decision (separate from transport-difference detection) -----------------------
    def _classify(self, op, field, sent, stored):
        return TR.classify(sent, stored, self.rules, field)

    def _containment_scope(self, op, expected, stored, failures, other):
        """Rule 3's narrowing, decided mechanically. Returns op only when every condition holds,
        else None (the global marker). Reached only after the write returned an expected status,
        a created object's id was known and read-back succeeded: the outcome is known."""
        if other:                                   # unsent-field, label or state failure
            return None
        for field, kind in failures:
            if kind != "rejected":                  # e.g. classification failed
                return None
            got = stored.get(field)
            if not TR.tail_confined(expected[field].decode("utf-8"), got):
                return None
        try:
            outstanding = [n for n in self._operation_markers() if n != GLOBAL_MARKER + "." + op]
        except OSError:
            return None
        if outstanding or os.path.lexists(self.halt_path):
            return None
        return op

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
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=1, sort_keys=True, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
        return path

    # -- text writes ---------------------------------------------------------------------------
    def write(self, op, target=None, fields=None, labels=None, label=None):
        """Perform exactly one write. Returns Result(stored, outcomes, records); raises Halted.
        After any Halted, this and every Gate2 instance in the process refuse further writes."""
        return self._guarded("write %s" % (op,),
                             lambda: self._write(op, target, fields, labels, label))

    def _write(self, op, target, fields, labels, label):
        self._mech = None
        self._check_clear()                       # global marker and pending notifications first
        spec, reg = OPERATIONS.get(op), self.registry.get(op)
        if spec is None or reg is None:
            self._halt("unknown operation %r" % (op,))
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
        # Every field and check is evaluated before anything is accepted or recorded.
        outcomes, permitted, failures, other, reasons, evidence = {}, [], [], [], [], {}
        for k in sorted(expected):
            sent = expected[k].decode("utf-8")    # the frozen expected text, not the live dict
            got = stored.get(k)
            shown = got if isinstance(got, str) else repr(got)
            if isinstance(got, str) and got.encode("utf-8") == expected[k]:
                outcomes[k] = ["exact", None]
                continue
            try:
                cls, rule_id = self._classify(op, k, sent, got)
            except BaseException as e:
                outcomes[k] = ["error", None]
                failures.append((k, "classification-failed"))
                reasons.append("classification failed for %s of %s %s: %s: %s"
                               % (k, op, rb_target, type(e).__name__, e))
                evidence.update({k + ".sent": sent, k + ".stored": shown})
                continue
            outcomes[k] = [cls, rule_id]
            if cls == "permitted":
                permitted.append((k, sent, got, rule_id))
            elif cls != "exact":
                failures.append((k, "rejected"))
                reasons.append("read-back mismatch in %s of %s %s (rejected: no permitted "
                               "transformation)" % (k, op, rb_target))
                evidence.update({k + ".sent": sent, k + ".stored": shown,
                                 k + ".diff": unified(sent, got) if isinstance(got, str) else ""})
        if before is not None:          # fields not sent must be byte-identical: no allowlist
            for k in ("title", "body"):
                if k not in expected and before.get(k) != stored.get(k):
                    other.append(k)
                    reasons.append("unsent field %s changed by %s %s" % (k, op, rb_target))
                    evidence.update({"unsent-%s.before" % k: str(before.get(k)),
                                     "unsent-%s.stored" % k: str(stored.get(k))})
        if op == "issue.close" and stored.get("state") != "closed":
            other.append("state")
            reasons.append("state read-back is not closed")
        if op in ("labels.add", "labels.remove"):
            names = sorted(x["name"] for x in stored.get("labels", []))
            want = set(x["name"] for x in before.get("labels", []))
            want = want | set(labels or []) if op == "labels.add" else want - {label}
            if names != sorted(want):
                other.append("labels")
                reasons.append("label read-back mismatch: %s != %s" % (names, sorted(want)))
        if failures or other:
            scope = self._containment_scope(op, expected, stored, failures, other)
            self._halt("; ".join(reasons), scope=scope, **evidence)
        records = []                    # only now, after every field and check has passed
        for k, sent, got, rule_id in permitted:
            try:
                records.append(self._record(op, rb_target, k, sent, got, rule_id))
            except BaseException as e:  # an accepted difference without its record is not accepted
                self._halt("discrepancy record could not be written: %s: %s"
                           % (type(e).__name__, e), sent=sent, stored=got,
                           records_already_written=list(records))
        return Result(stored, outcomes, records)

    # -- pushes: gate.py's path and guards, under the same run-level latch ---------------------
    def push(self, remote, sha, branch_ref):
        return self._guarded("push", lambda: self._push(remote, sha, branch_ref))

    def _push(self, remote, sha, branch_ref):
        self._mech = None
        self._check_clear()
        self._mech = "push"                       # an existing HALT.push also blocks pushes
        return G.Gate.push(self, remote, sha, branch_ref)
