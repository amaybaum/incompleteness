"""Write gate v2 prototype: exact read-back plus a bounded transport-difference allowlist.

Prototype only, mock transport only; not adopted. gate.py stays the operational mechanism until
the owner approves a replacement. This module reuses gate.py by import (operations, pre-checks,
refspec checks, push path, read-back paths, grants) and adds:

  * one verification procedure for every operation: the gate fixes and hashes the expected text
    (the text sent) before the write, compares the stored text byte for byte, and compares every
    field the write did not send, the labels and the state with what the operation should leave
    (the pre-write read, or the values a new object has). Only when a sent text differs does it ask
    transport_rules.classify whether exactly one owner-adopted rule permits the difference; it
    accepts that only on an operation validated under the allowlist (registry "allowlist": True)
    or on a single-write (validation) grant, so a mechanism validated by exact read-back stays
    exact until revalidated (section A.51 item 2). The gate knows no transformation;
  * outcomes: "exact" -> accepted; "permitted" (where admitted) -> accepted, with a discrepancy
    record; anything else -> halt, with sent, stored and diff kept;
  * one containment mechanism, the halt store: files in the halt directory, mirrored in this
    process by _HALTED. The plan's identity is taken from the plan record PLAN in that store,
    written once before the run (record_plan) and never rewritten while it exists; a gate is
    refused when the record is missing or names another plan id than the caller's, at construction
    and at every check of the store, so a process cannot substitute a new id on restart. Every
    halt and every refusal ends the sequence: it is recorded in memory and in the plan latch
    HALT-PLAN.<plan_id>, which every process of the plan reads at every check of the store (see
    below), so neither catching the exception nor restarting a process continues the plan; only
    an owner decision removes the latch (by hand). Beyond the sequence, the global marker HALT
    (the name gate.py uses) is written for every failure except a read-back mismatch for which
    every condition of section A.49 rule 3 holds; then HALT.<operation> is written instead, and a
    later sequence writes nothing while it lacks HALT.<operation>.notified, which a person creates
    by hand once the owner has been told. A stale .notified companion, or an operation marker that
    already exists, makes the halt global;
  * the narrowing needs a footer-shaped tail (transport_rules.footer_shaped_tail): the stored
    text is the sent content followed only by newlines and at most one exact copy of the
    attribution footer. That shape decides only the extent of a stop, never acceptance;
  * discrepancy records are written only after every field and check of the write has passed; a
    halt marker embeds the complete evidence texts;
  * the pre-write check also refuses any text field the write would send (every body and title, of
    every operation) that contains a less-than sign immediately followed by an exclamation mark
    (lt_bang_violations; owner decisions of 2026-11-25). The reason names the field and every
    position; the text is never altered, and the writer must reword it. This one refusal does not
    stop the sequence (owner decision, amaybaum, 2026-11-25, subject to the reviewer confirming
    compatibility with section A.51): it raises Refused, which is not Halted, after every other
    pre-check has passed and before any request, writes no marker and no latch, and gives back a
    single-write grant the write had taken. Every other pre-check and containment rule is unchanged.
The store is checked (_check_clear) for a write at its start, again once the operation is known
(before the pre-write read) and again immediately before the write request, but not before the
read-back request; for a push at its start only (by gate2 and again by gate.py's push, which calls
the same check), before any git command, but not again before the remote-ref reads or git push
itself. Markers are created exclusively, never overwritten and never removed by the gate. A check
and the requests that follow it are not atomic across processes or threads; writers are
single-threaded.
"""
import difflib, hashlib, itertools, json, os, re, time

import gate as G
import transport_rules as TR
from gate import OPERATIONS, Halted, precheck_text, check_refspec, run_plan, main  # noqa: F401

GLOBAL_MARKER = "HALT"
NOTIFIED_SUFFIX = ".notified"
PLAN_PREFIX = "HALT-PLAN."
PLAN_RECORD = "PLAN"
PLAN_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,99}")
_seq = itertools.count()
# The halt store's in-process copy: one entry per halt or refusal in this process. Any entry stops
# every Gate2 in the process, also when a marker file could not be written. Nothing clears it.
_HALTED = []


# A less-than sign immediately followed by an exclamation mark. GitHub stored comment 7172299731
# with the exclamation mark of this sequence removed (inside a code span); text containing it is
# refused before any request and never altered (owner decisions, amaybaum, 2026-11-25T19:31:10Z
# and 2026-11-25T20:29:25Z).
LT_BANG = "<" + "!"


def lt_bang_violations(t, field):
    """The pre-write refusal of LT_BANG in a text field the gate would send. Returns a list with
    one explanation naming the field and every position (0-based character offset, 1-based line
    and column), or an empty list. Never changes the text; a non-string is left to precheck_text."""
    if not isinstance(t, str) or LT_BANG not in t:
        return []
    pos, i = [], t.find(LT_BANG)
    while i != -1:
        pos.append(i)
        i = t.find(LT_BANG, i + 1)

    def where(i):
        line = t.count("\n", 0, i) + 1
        return "offset %d (line %d, column %d)" % (i, line, i - (t.rfind("\n", 0, i) + 1) + 1)
    return ["field %s contains '<' immediately followed by '!' at %s; GitHub has stored such text "
            "with the '!' removed, so it is not sent and is not altered: reword the %s so that no "
            "'<' is immediately followed by '!' (no automatic substitution is made)"
            % (field, ", ".join(where(i) for i in pos), field)]


class Refused(Exception):
    """The write was refused before any request, for the less-than/exclamation sequence only. Not
    a Halted: the sequence continues, and the writer may send a reworded text. Attributes: op,
    target, field, reason."""

    def __init__(self, op, target, field, reason):
        super().__init__(reason)
        self.op, self.target, self.field, self.reason = op, target, field, reason


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


def _label_names(obj):
    labels = obj.get("labels")
    if not isinstance(labels, list):
        return labels
    return sorted(set(x["name"] for x in labels))


def _now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


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
                 evidence_dir=None, log=None, rules=None, *, plan_id):
        if not (isinstance(plan_id, str) and PLAN_ID.fullmatch(plan_id)):
            raise ValueError("plan_id must match %s" % PLAN_ID.pattern)
        super().__init__(transport, git, os.path.join(halt_dir, GLOBAL_MARKER), repo, registry,
                         allowed_branches, evidence_dir or halt_dir, log)
        self.halt_dir = halt_dir
        try:                                  # the plan id comes from the plan record only
            self.plan_id = self._plan_record(plan_id)
        except Halted as e:
            _HALTED.append("refused: %s" % e)
            raise
        self.plan_path = os.path.join(halt_dir, PLAN_PREFIX + self.plan_id)
        self.rules = TR.REGISTRY if rules is None else rules
        self._mech = None

    # -- the halt store ----------------------------------------------------------------------------
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

    def _plan_record(self, supplied):
        """The plan id recorded in the halt store's plan record, which must equal the id the
        caller supplied. Raises Halted when the record is missing, unreadable or names another
        id; the gate never writes the record and never takes the caller's id in its place."""
        path = os.path.join(self.halt_dir, PLAN_RECORD)
        try:
            with open(path, encoding="utf-8") as f:
                rid = json.load(f)["plan_id"]
        except (OSError, ValueError, KeyError, TypeError) as e:
            raise Halted("no readable plan record %s (written once before the run): %s: %s"
                         % (PLAN_RECORD, type(e).__name__, e))
        if not (isinstance(rid, str) and PLAN_ID.fullmatch(rid)):
            raise Halted("plan record %s names no valid plan id" % PLAN_RECORD)
        if supplied != rid:
            raise Halted("plan id %r differs from the plan record's %r" % (supplied, rid))
        return rid

    def _check_clear(self):
        """The one halt check: this process's copy of the store, then the global marker, this
        plan's latch, this mechanism's marker, the plan record and pending notifications."""
        if _HALTED:
            raise Halted("sequence stopped after an earlier halt in this process: %s" % _HALTED[0])
        for p in (self.halt_path, self.plan_path, self.marker_path(self._mech)):
            if os.path.lexists(p):
                raise Halted("halt marker present: %s" % os.path.basename(p))
        self._plan_record(self.plan_id)
        try:
            pending = [n for n in self._operation_markers()
                       if not os.path.lexists(os.path.join(self.halt_dir, n + NOTIFIED_SUFFIX))]
        except OSError as e:
            raise Halted("halt directory unreadable: %s" % e)
        if pending:
            raise Halted("owner not yet told of the halt recorded in %s (no %s file)"
                         % (pending[0], pending[0] + NOTIFIED_SUFFIX))

    @staticmethod
    def _write_marker(path, rec):
        """Create a marker exclusively and fsync it. True, "exists" or an error text."""
        try:
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(rec, f, indent=1, sort_keys=True, ensure_ascii=False)
                f.flush()
                os.fsync(f.fileno())
            return True
        except FileExistsError:
            return "exists"
        except OSError as e:
            return str(e)

    def _latch(self, rec):
        """End the sequence: in this process and in the plan latch, which only the owner removes."""
        _HALTED.append(rec["reason"])
        return self._write_marker(self.plan_path, dict(rec, plan_id=self.plan_id))

    def _guarded(self, what, fn):
        try:
            return fn()
        except Refused:              # nothing was sent and nothing is latched (lt_bang_violations)
            raise
        except Halted as e:          # a refusal also ends the sequence (a halt has latched already)
            if not getattr(e, "latched", False):
                self._latch({"reason": "refused: %s" % e, "pid": os.getpid(), "time": _now()})
            raise
        except BaseException as e:   # anything else during a write: outcome unknown
            self._mech = None
            self._halt("unknown outcome: exception during %s: %s: %s" % (what, type(e).__name__, e))

    def _halt(self, reason, scope=None, **evidence):
        """Keep the evidence, latch the sequence, write the marker, raise Halted.
        scope None: the global marker. scope <operation>: that operation's marker only; passed
        solely by _containment_scope's decision."""
        mech = scope
        tag = "%s-%d-%d" % (mech or "global", os.getpid(), next(_seq))
        rec = {"reason": reason, "scope": "operation" if mech else "global",
               "mechanism": mech or "global", "pid": os.getpid(), "time": _now()}
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
        notes = []
        r = self._latch(rec)
        if r is not True and r != "exists":
            notes.append("plan latch not written: %s" % r)
        if mech:
            r = self._write_marker(self.marker_path(mech), rec)
            if r is not True:            # an earlier marker or an unwritable one: stop everything
                notes.append("operation marker %s: halt made global" % (
                    "already present" if r == "exists" else "not written (%s)" % r))
                rec = dict(rec, scope="global", escalated_from=mech)
                mech = None
        if mech is None:
            r = self._write_marker(self.halt_path, rec)
            if r is not True and r != "exists":
                notes.append("global marker not written: %s" % r)
        e = Halted(reason + ("" if not notes else " (%s)" % "; ".join(notes)))
        e.latched = True
        raise e

    # -- outcome decision (separate from transport-difference detection) -----------------------
    def _classify(self, op, field, sent, stored):
        return TR.classify(sent, stored, self.rules, field)

    def _allowlist_applies(self, reg):
        """Section A.51 item 2: a single-write (validation) write, or an operation validated under
        the allowlist. An operation validated by exact read-back only stays exact."""
        return not reg.get("validated") or reg.get("allowlist") is True

    def _containment_scope(self, op, expected, stored, failures, other):
        """Rule 3's narrowing, decided from the write, its read-back and the halt store. Returns op
        only when every condition holds, else None (the global marker). Reached only after the
        write returned an expected status, a created object's id was known and read-back
        succeeded: the outcome is known."""
        if other:                                   # unsent-field, label or state failure
            return None
        for field, kind in failures:
            if kind != "rejected":                  # e.g. classification failed
                return None
            if not TR.footer_shaped_tail(expected[field].decode("utf-8"), stored.get(field)):
                return None
        try:
            outstanding = [n for n in self._operation_markers() if n != GLOBAL_MARKER + "." + op]
        except OSError:
            return None
        companion = self.marker_path(op) + NOTIFIED_SUFFIX
        if outstanding or os.path.lexists(self.halt_path) or os.path.lexists(companion):
            return None                             # a stale companion would hide this halt
        return op

    def _expected_state(self, op, before, labels, label):
        """What every field the write did not send must read back as, for every operation: title
        and body as before, labels and state as before except as the operation changes them; a
        new Issue or pull request has no labels and is open; a comment carries neither."""
        if op == "comment.create":
            return {}
        if before is None:
            want = {"labels": [], "state": "open"}
        else:
            want = {"title": before.get("title"), "body": before.get("body"),
                    "labels": _label_names(before), "state": before.get("state")}
        if op == "labels.add":
            want["labels"] = sorted(set(want["labels"] or []) | set(labels or []))
        elif op == "labels.remove":
            want["labels"] = sorted(set(want["labels"] or []) - {label})
        elif op == "issue.close":
            want["state"] = "closed"
        for k in OPERATIONS[op]["text"]:
            want.pop(k, None)
        return want

    def _refuse(self, op, target, field, reason):
        """The non-stopping refusal: no request, no marker, no latch, no evidence file."""
        self.log.append(("refused", op, str(target), field))
        raise Refused(op, target, field, "refused before sending, nothing sent: " + reason)

    def _record(self, op, target, field, sent, stored, rule_id):
        rule = TR.rule_by_id(rule_id, self.rules)
        rec = {"kind": "permitted-transport-difference", "operation": op, "target": target,
               "field": field, "repo": self.repo, "plan_id": self.plan_id, "time": _now(),
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
        After any Halted, this plan and every Gate2 in the process refuse further writes. Refused
        (the less-than/exclamation sequence only) ends nothing: a reworded text may be sent."""
        return self._guarded("write %s" % (op,),
                             lambda: self._write(op, target, fields, labels, label))

    def _write(self, op, target, fields, labels, label):
        self._mech = None
        self._check_clear()                       # the store first, before anything else
        spec, reg = OPERATIONS.get(op), self.registry.get(op)
        if spec is None or reg is None:
            self._halt("unknown operation %r" % (op,))
        self._mech = op
        self._check_clear()                       # this mechanism's marker, before any request
        fields = dict(fields or {})
        key = (op, str(target))
        took_grant = False
        if not reg.get("validated"):
            if key not in self.grants:
                self._halt("operation %s is not validated and has no single-write grant" % op)
            self.grants.discard(key)              # consumed before the write
            took_grant = True
        if set(fields) != set(spec["text"]):
            self._halt("fields %s do not match operation %s" % (sorted(fields), op))
        for k, v in fields.items():
            bad = precheck_text(v)
            if isinstance(v, str):
                bad += TR.send_form_violations(reg.get("send_form"), v, k)
            if bad:
                self._halt("pre-check refused field %s: %s" % (k, "; ".join(bad)),
                           sent=v if isinstance(v, str) else repr(v))
        for k, v in fields.items():               # only after every other pre-check has passed
            bad = lt_bang_violations(v, k)
            if bad:
                if took_grant:                    # nothing is sent: the grant is not used up
                    self.grants.add(key)
                self._refuse(op, target, k, bad[0])
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
        if "created" not in spec:
            before = self._get(self._readback_path(op, target))
        self._check_clear()                       # again, immediately before the write request
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
        allow = self._allowlist_applies(reg)
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
            if cls == "permitted" and allow:
                permitted.append((k, sent, got, rule_id))
                continue
            failures.append((k, "rejected"))
            reasons.append("read-back mismatch in %s of %s %s (%s)" % (
                k, op, rb_target,
                "rejected: permitted by %s, but %s is held to exact read-back until validated "
                "under the allowlist" % (rule_id, op) if cls == "permitted"
                else "rejected: no permitted transformation"))
            evidence.update({k + ".sent": sent, k + ".stored": shown,
                             k + ".diff": unified(sent, got) if isinstance(got, str) else ""})
        for k, want in sorted(self._expected_state(op, before, labels, label).items()):
            got = _label_names(stored) if k == "labels" else stored.get(k)
            if got != want:                       # exact: no allowlist for what was not sent
                other.append(k)
                reasons.append("%s read-back differs from what %s %s should leave: %r != %r"
                               % (k, op, rb_target, got, want))
                evidence.update({"unsent-%s.expected" % k: json.dumps(want, ensure_ascii=False),
                                 "unsent-%s.stored" % k: json.dumps(got, ensure_ascii=False)})
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

    # -- pushes: gate.py's path and guards, under the same halt store --------------------------
    def push(self, remote, sha, branch_ref):
        return self._guarded("push", lambda: self._push(remote, sha, branch_ref))

    def _push(self, remote, sha, branch_ref):
        self._mech = None
        self._check_clear()
        self._mech = "push"                       # an existing HALT.push also blocks pushes
        return G.Gate.push(self, remote, sha, branch_ref)


def record_plan(halt_dir, plan_id):
    """Write the plan's persistent record, PLAN in the halt store, naming plan_id. Done once
    before the run, as part of fixing the plan, never by the gate and never per process. Refuses
    (FileExistsError) while a record exists. The record is not deleted, replaced or rewritten
    while the plan is active, and a plan whose sequence a halt has ended stays active until a
    recorded owner decision resolves that halt."""
    if not (isinstance(plan_id, str) and PLAN_ID.fullmatch(plan_id)):
        raise ValueError("plan_id must match %s" % PLAN_ID.pattern)
    path = os.path.join(halt_dir, PLAN_RECORD)
    r = Gate2._write_marker(path, {"plan_id": plan_id, "time": _now()})
    if r == "exists":
        raise FileExistsError("plan record already exists: %s" % path)
    if r is not True:
        raise OSError("plan record not written: %s" % r)
    return path
