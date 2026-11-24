"""Controls of the design (v5.5.8; sec. 10.4, 13.2): admission TR1-TR70 on an in-memory host (TR54-TR70: owner at
creation, DI-1), the acceptance predicate X11 and the durable evidence TR45/TR46, native delegation G4-G9 on a small
on-disk repository, commits after X R16/R17, widening A12r, purity Z9h, the synthetic parts of S4a and Z11, the
lineage controls LN1-LN12 (DI-2), one review verdict per added ledger event (R6-EV), and the controls for the
independent reviews' findings (R3-*, R4-*, R5-*, R6-G1 to R6-G9, TR32 with the engine's own admission snapshot,
TR32-OWN, and R7-B2 and R7-N5*: a snapshot event conflicting with the thread, and one observed event recorded more
than once), and S1-P2-* and S1-Q8: the real-host history reader over a host whose path listing simplifies history
(A and the freeze ledger landed by merge commits), and the empty freeze ledger's fields).

Every control is reported as {id, expected, predicate, actual, status} with status PASS, FAIL, SKIP or NOT RUN
(sec. 10.4, B6). A control that needs the real host (a CI job with the host's API) is NOT RUN here, never PASS.

Usage: python3 -I -B tools/ledger_coverage/adapters/conformance_controls.py OUT_DIR
"""
import copy
import datetime
import gzip
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

here = os.path.dirname(os.path.abspath(__file__))
tools = os.path.dirname(os.path.dirname(here))
if tools not in sys.path:
    sys.path.insert(0, tools)

from ledger_coverage.engine import authority as auth, checker, cli, delegation as delmod, execution as exmod  # noqa
from ledger_coverage.engine import gitobj, purity, util  # noqa: E402
from ledger_coverage.adapters import host_fixture as hf, synthetic_fixture as sf  # noqa: E402

RESULTS = []


def record(cid, expected, predicate, actual, status):
    RESULTS.append({'id': cid, 'expected': expected, 'predicate': predicate, 'actual': actual, 'status': status})


def check(cid, expected, predicate, actual, holds):
    record(cid, expected, predicate, actual, 'PASS' if holds else 'FAIL')


def not_run(cid, expected, why):
    record(cid, expected, None, why, 'NOT RUN')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def stop(res):
    return (res or {}).get('stop', {}).get('class')


def classes(res):
    return sorted({i['class'] for i in (res or {}).get('items', [])})


# ---- the admission world --------------------------------------------------------------------------------------

class TR:
    """A synthetic configuration at commit c, a freeze F with a pin table, and an in-memory host world."""

    def __init__(self, runner):
        self.r = runner
        self.syn = sf.Syn()
        self.pd = sf.patch_doc(self.syn.H, [])
        self.variant = {'patch_sha': sha(self.pd), 'files': {'syn/patch.json': self.pd}}
        self.c, self.p, self.s, self.files = self.syn.build(self.variant)
        self.repo = self.syn.repo

    def world(self):
        return hf.World('syn/PREREG.md')

    def freeze(self, w, listed=None, extra=None, a_bytes=None):
        d = self.p.rsplit('/', 1)[0] + '/'
        if listed is None:
            listed = {p: self.repo.read(self.c, p) for p in self.repo.paths(self.c)
                      if p.startswith(d) and p.endswith('.json')}
        files = {'syn/PREREG.md': hf.pin_table({p[len('syn/'):]: sha(b) for p, b in listed.items()}),
                 auth.authority_path: a_bytes if a_bytes is not None else w.a_bytes}
        files.update(extra or {})
        return self.repo.derive(self.c, files, parents=self.repo.parents(self.c), subject='freeze')

    def refreeze(self, w, owner=None, at=None, retirement_owner=None, a_bytes=None, extra=None, variant=None):
        """F re-frozen after owner changes (sec. 6.3, "Owner at creation"): a configuration whose review chain carries
        owner authorizations by `owner` (the owner in force by default) at time `at` (now by default), and whose
        retirement.owner is `retirement_owner` (the same owner by default)."""
        owner = owner if owner is not None else w.a['owner']['id']
        v = dict(self.variant, auth_owner=owner, auth_time=at or w.tick(),
                 owner=retirement_owner if retirement_owner is not None else owner)
        v.update(variant or {})
        c, p, _, _ = self.syn.build(v)
        assert p == self.p
        old = self.c
        self.c = c
        try:
            return self.freeze(w, a_bytes=a_bytes, extra=extra)
        finally:
            self.c = old

    def run(self, w, F, args=None, control=None, harness=False, environ=None, op=None):
        argv = (op or ['terms']) + ['--config', '%s:%s' % (F, self.p), '--out', self.r.out()] + \
            (args if args is not None else w.args(F)) + ['--commit', self.syn.H]
        ctl = w.control() if control is None else control
        return cli.run(argv, repo=self.repo, harness=harness, stderr=io.StringIO(), control=ctl,
                       environ=environ if environ is not None else {})


def tr_controls(r):
    t = TR(r)
    UNREV = 'ERROR CONFIG_UNREVIEWED, exit 65'

    def refused(code, res):
        return code == 65 and stop(res) == 'CONFIG_UNREVIEWED'

    def show(code, res):
        return {'exit': code, 'stop': stop(res), 'message': ((res or {}).get('stop') or {}).get('message', '')[:160]}

    # positive simulated chain, then each refusal
    w = t.world()
    F = t.freeze(w)
    w.designate(F)
    code, res = t.run(w, F)
    snap = (((res or {}).get('config') or {}).get('admission') or {}).get('simulated_chain', {}).get('snapshot', {})
    fields = ['owner_id', 'authority_sha256', 'authority_versions', 'run', 'main', 'thread', 'owner_comments',
              'impostor_comments', 'freeze_ledger', 'events', 'designation_comment_id', 'pin_table', 'freeze',
              'evaluated', 'invocation']
    check('TR5-sim', 'the whole of sec. 6.3 holds on the in-memory host: every snapshot field recorded; the result '
          'is a control artefact (control-harness), never chain', "exit == 0 and admission.mode == "
          "'control-harness' and all snapshot fields present and harness is true",
          dict(show(code, res), missing=[f for f in fields if f not in snap]),
          code == 0 and res['config']['admission']['mode'] == 'control-harness' and res.get('harness') is True
          and not [f for f in fields if f not in snap])
    not_run('TR5', '`config.admission: "chain"` with every field of sec. 6.3 recorded (positive control, CI only)',
            'needs a run of the pinned workflow in repository 1156244443 with the host API; CI plan in the report')
    # TR1: no --freeze, harness off, no host
    code, res = t.run(w, F, args=[], control={})
    check('TR1', 'a run without --freeze: ' + UNREV, "exit == 65 and stop == 'CONFIG_UNREVIEWED'", show(code, res),
          refused(code, res))
    # TR2: configuration not in the pin table, with a matching --config-sha256
    w2 = t.world()
    F2 = t.freeze(w2, listed={})
    w2.designate(F2)
    code, res = t.run(w2, F2, args=w2.args(F2) + ['--config-sha256', t.s])
    check('TR2', 'a configuration not in F\'s pin table, with a matching --config-sha256: ' + UNREV,
          "exit == 65 and stop == 'CONFIG_UNREVIEWED'", show(code, res), refused(code, res))
    # TR3: review and authorization beside the configuration but not in the pin table
    w3 = t.world()
    F3 = t.freeze(w3, listed={t.p: t.repo.read(t.c, t.p)})
    w3.designate(F3)
    code, res = t.run(w3, F3)
    check('TR3', 'review and authorization beside the configuration, naming its blob, not in F\'s pin table: '
          + UNREV, "exit == 65 and stop == 'CONFIG_UNREVIEWED'", show(code, res), refused(code, res))
    # TR4: retirement.owner differs from A.owner.id
    w4 = t.world()
    w4.a = hf.authority('syn/PREREG.md', owner_id=999)
    t4 = TR(r)
    w4b = hf.World('syn/PREREG.md')
    a_other = hf.jb(hf.authority('syn/PREREG.md', owner_id=999))
    w4b.a_bytes = a_other
    # a world whose A names another owner id, approved and reviewed as its own first version
    w4c = world_with_owner(999)
    F4 = t4.freeze(w4c)
    w4c.designate(F4, author_id=999)
    code, res = t4.run(w4c, F4)
    check('TR4', '`retirement.owner` differing from `A.owner.id`: ' + UNREV, "exit == 65 and stop == "
          "'CONFIG_UNREVIEWED'", show(code, res), refused(code, res))
    # TR6: a designation record inside F, no designation comment
    w6 = t.world()
    F6 = t.freeze(w6, extra={'syn/designation.json': b'{"designate": true}\n'})
    code, res = t.run(w6, F6)
    check('TR6', 'a designation record inside F, no designation comment on the host: ERROR (missing designation)',
          "exit == 65 and stop == 'CONFIG_UNREVIEWED'", show(code, res), refused(code, res))
    # TR7: a designation by another account
    w7 = t.world()
    F7 = t.freeze(w7)
    w7.designate(F7, author_id=31337, login='someone-else')
    code, res = t.run(w7, F7)
    check('TR7', 'a designation comment by another account: ERROR', "exit == 65 and stop == 'CONFIG_UNREVIEWED'",
          show(code, res), refused(code, res))
    # TR8: an owner designation naming a different commit
    w8 = t.world()
    F8 = t.freeze(w8)
    w8.designate('ab' * 20)
    code, res = t.run(w8, F8)
    check('TR8', 'an owner designation naming a different commit: ERROR (F not designated)',
          "exit == 65 and stop == 'CONFIG_UNREVIEWED'", show(code, res), refused(code, res))
    # TR9: caller overrides, one at a time
    tr9 = {}
    w9 = t.world()
    F9 = t.freeze(w9)
    w9.designate(F9)
    for opt in ('--owner', '--repository-id', '--forms', '--thread', '--workflow-path', '--workflow-sha256'):
        code, res = t.run(w9, F9, args=w9.args(F9) + [opt, '1'])
        tr9['option ' + opt] = (code, stop(res))
    for env in ('OI_OWNER_ID', 'OI_AUTHORITY', 'OI_REPOSITORY_ID', 'OI_WORKFLOW_SHA256'):
        code, res = t.run(w9, F9, environ={env: '1'}, control={})
        tr9['environment ' + env] = (code, stop(res))
    for field in ('owner', 'repository', 'workflow', 'forms', 'authority_thread', 'plans'):
        cfg = json.loads(t.repo.read(t.c, t.p))
        cfg[field] = 1
        tr9['configuration field ' + field] = cfg_field_run(t, cfg)
    cfg = json.loads(t.repo.read(t.c, t.p))
    cfg['retirement']['repository'] = 1
    tr9['configuration field retirement.repository'] = cfg_field_run(t, cfg)
    w9b = t.world()
    other_a = hf.jb(hf.authority('syn/PREREG.md', owner_id=999))
    F9b = t.freeze(w9b, a_bytes=other_a)
    w9b.designate(F9b)
    code, res = t.run(w9b, F9b)
    tr9['record in F (an authority record naming another owner)'] = (code, stop(res))
    ok9 = all(v[0] in (64, 65) and v[1] in (None, 'CONFIG_UNREVIEWED', 'CONFIG_INVALID') for v in tr9.values()) and \
        all(v == (65, 'CONFIG_INVALID') for k, v in tr9.items() if k.startswith('configuration field'))
    check('TR9', 'each caller override ignored or refused, never chain on the overridden value; an unknown '
          'configuration field is ERROR CONFIG_INVALID', 'every case exits 64 or 65 (never 0, never chain); every '
          'configuration-field case is (65, CONFIG_INVALID)', tr9, ok9)
    # TR10: caller-built F listing its own files, no owner designation
    w10 = t.world()
    F10 = t.freeze(w10)
    code, res = t.run(w10, F10)
    check('TR10', 'a caller-built F whose pin table lists its own configuration and review files, with no owner '
          'designation: ERROR', "exit == 65 and stop == 'CONFIG_UNREVIEWED'", show(code, res), refused(code, res))
    # TR11: designation edited; edited and restored
    out11 = []
    for edits in (['an earlier text'], ['oi-freeze/1 designate plan=%s round=%s commit=%s' % (hf.PLAN, hf.ROUND, 'x')]):
        w11 = t.world()
        F11 = t.freeze(w11)
        w11.designate(F11, edits=edits)
        out11.append(show(*t.run(w11, F11)))
    check('TR11', 'the designation edited after creation; separately edited and restored: ERROR in both',
          "both exit 65 with stop 'CONFIG_UNREVIEWED'", out11,
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' for o in out11))
    # TR12: a later supersession on the first page; separately beyond the first page
    out12 = []
    for pad in (0, 7):
        w12 = t.world()
        F12 = t.freeze(w12)
        w12.designate(F12)
        for i in range(pad):
            w12.comment(hf.PLAN_ISSUE, 'an ordinary comment %d' % i)
        w12.comment(hf.PLAN_ISSUE, 'oi-freeze/1 supersede plan=%s round=%s commit=%s by=%s'
                    % (hf.PLAN, hf.ROUND, F12, 'cd' * 20))
        out12.append(show(*t.run(w12, F12)))
    check('TR12', 'a later owner supersession of F on the first page; separately beyond it: ERROR for F in both',
          "both exit 65 with stop 'CONFIG_UNREVIEWED'", out12,
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' for o in out12))
    # TR13: a local run with a complete chain on paper
    code, res = t.run(w, F, control={}, environ={})
    check('TR13', 'a local run with a complete chain on paper: no chain admission; never acceptable',
          "exit == 65 and stop == 'CONFIG_UNREVIEWED' and no result has mode 'chain'", show(code, res),
          refused(code, res))
    # TR14: a fork; another repository
    out14 = []
    for mut in ('fork', 'repo'):
        w14 = t.world()
        F14 = t.freeze(w14)
        w14.designate(F14)
        if mut == 'fork':
            w14.h.runs[w14.run_id]['fork'] = True
        else:
            w14.h.runs[w14.run_id]['repository_id'] = 78
            w14.h.add_repo(78, 'someone/repo')
            w14.h.repos[78] = copy.deepcopy(w14.h.repos[hf.REPO_ID])
        out14.append(show(*t.run(w14, F14)))
    check('TR14', 'the same workflow and tool run in a fork, or in another repository: ERROR at the tool',
          "both exit 65 with stop 'CONFIG_UNREVIEWED'", out14,
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' for o in out14))
    # TR15: workflow content differs; same-named workflow at another path
    out15 = []
    for mut in ('content', 'path'):
        w15 = t.world()
        F15 = t.freeze(w15)
        w15.designate(F15)
        if mut == 'content':
            w15.add_main('c2', {hf.WF_PATH: hf.WF + b'# changed\n'})
        else:
            w15.add_main('c2', {'.github/workflows/other/lc.yml': hf.WF})
            w15.h.runs[w15.run_id]['workflow_path'] = '.github/workflows/other/lc.yml'
        out15.append(show(*t.run(w15, F15)))
    check('TR15', 'a workflow at A.workflow.path with other content; separately a same-named workflow at another '
          'path: ERROR at the tool', "both exit 65 with stop 'CONFIG_UNREVIEWED'", out15,
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' for o in out15))
    # TR16: designation in another thread
    w16 = t.world()
    F16 = t.freeze(w16)
    w16.comment(99, 'oi-freeze/1 designate plan=%s round=%s commit=%s' % (hf.PLAN, hf.ROUND, F16))
    check('TR16', 'an owner designation in a thread other than the plan\'s: ERROR', "exit == 65",
          show(*t.run(w16, F16)), refused(*t.run(w16, F16)))
    # TR17: another wording; a near form without the round
    w17 = t.world()
    F17 = t.freeze(w17)
    w17.comment(hf.PLAN_ISSUE, 'do not merge %s' % F17)
    a17 = show(*t.run(w17, F17))
    w17b = t.world()
    F17b = t.freeze(w17b)
    w17b.designate(F17b)
    w17b.comment(hf.PLAN_ISSUE, 'oi-freeze/1 designate plan=%s commit=%s' % (hf.PLAN, F17b))
    b17 = show(*t.run(w17b, F17b))
    check('TR17', 'another wording does not count (ERROR, missing designation); a near form without the round '
          'refuses as ambiguous', "both exit 65; the second names the forms point",
          [a17, b17], a17['exit'] == 65 and b17['exit'] == 65 and 'malformed' in b17['message'])
    # TR18 withdrawal; TR22 two live designations
    w18 = t.world()
    F18 = t.freeze(w18)
    w18.designate(F18)
    w18.comment(hf.PLAN_ISSUE, 'oi-freeze/1 withdraw plan=%s round=%s commit=%s' % (hf.PLAN, hf.ROUND, F18))
    check('TR18', 'an explicit owner withdrawal of F after its designation: ERROR', "exit == 65",
          show(*t.run(w18, F18)), refused(*t.run(w18, F18)))
    w22 = t.world()
    F22 = t.freeze(w22)
    w22.designate(F22)
    w22.designate('ef' * 20)
    check('TR22', 'two live designations of different commits for one round: ERROR', "exit == 65",
          show(*t.run(w22, F22)), refused(*t.run(w22, F22)))
    # TR19: deleted; hidden
    w19 = t.world()
    F19 = t.freeze(w19)
    c19 = w19.designate(F19)
    w19.comments[(hf.REPO_ID, hf.PLAN_ISSUE)].remove(c19)
    a19 = show(*t.run(w19, F19))
    w19b = t.world()
    F19b = t.freeze(w19b)
    w19b.designate(F19b, hidden=True)
    b19 = show(*t.run(w19b, F19b))
    check('TR19', 'the designation deleted; separately hidden: ERROR in both', "both exit 65", [a19, b19],
          a19['exit'] == 65 and b19['exit'] == 65)
    # TR20: owner's login, another id
    w20 = t.world()
    F20 = t.freeze(w20)
    w20.designate(F20, author_id=4243)
    code, res = t.run(w20, F20)
    check('TR20', 'a designation by an account with the owner\'s login but another numeric id: ERROR',
          "exit == 65", show(code, res), refused(code, res))
    # TR21: host unavailable; page failure; count mismatch
    out21 = []
    for mut in ('comments', 'page1', 'skew'):
        w21 = t.world()
        F21 = t.freeze(w21)
        w21.designate(F21)
        for i in range(3):
            w21.comment(hf.PLAN_ISSUE, 'padding %d' % i)
        if mut == 'skew':
            w21.h.count_skew[(hf.REPO_ID, hf.PLAN_ISSUE)] = 1
        else:
            w21.h.fail.add(mut)
        out21.append(show(*t.run(w21, F21)))
    check('TR21', 'the host API unavailable, a page request failing, or a comment count mismatch: ERROR, never a '
          'fallback', "all three exit 65", out21, all(o['exit'] == 65 for o in out21))
    # TR23: F's copy of A differs; an A change merged by another account
    w23 = t.world()
    F23 = t.freeze(w23, a_bytes=hf.jb(hf.authority('syn/PREREG.md', extra={'status': 'other copy'})))
    w23.designate(F23)
    a23 = show(*t.run(w23, F23))
    w23b = t.world()
    new_a = hf.authority('syn/PREREG.md', supersedes={'path': auth.authority_path, 'blob_sha256': sha(w23b.a_bytes)},
                         extra={'status': 'second version'})
    b23 = change_authority(w23b, new_a, merged_by=31337)
    F23b = t.freeze(w23b, a_bytes=w23b.a_bytes)
    w23b.designate(F23b)
    b23 = show(*t.run(w23b, F23b))
    check('TR23', 'F carrying a copy of A that differs from the admitted A; separately a change to A merged by '
          'another account: ERROR in both', "both exit 65", [a23, b23], a23['exit'] == 65 and b23['exit'] == 65)
    # TR24 / TR25: A from a caller file, another ref, F's tree, another repository
    w24 = t.world()
    F24 = t.freeze(w24, a_bytes=hf.jb(hf.authority('syn/PREREG.md', owner_id=4242, extra={'status': 'in F'})))
    w24.designate(F24)
    a24 = show(*t.run(w24, F24, environ={'OI_AUTHORITY_FILE': '/nonexistent/authority.json'}))
    w25 = t.world()
    for cm in ('c1', w25.main):
        w25.h.repos[hf.REPO_ID]['commits'][cm]['files'].pop(auth.authority_path, None)
    F25 = t.freeze(w25)
    w25.designate(F25)
    a25 = show(*t.run(w25, F25))
    check('TR24', 'a caller-supplied authority configuration is never read as A; a run that cannot read A from '
          'main of the attested repository is ERROR', "exit == 65 (A in F differs from main's)", a24,
          a24['exit'] == 65)
    check('TR25', 'A taken from another ref or repository is refused: only main of the attested repository',
          "exit == 65 when main has no A, though F carries one", a25, a25['exit'] == 65)
    # TR26: A changed on main after F's base: without and with its review and authorization
    w26 = t.world()
    new_a = hf.authority('syn/PREREG.md', supersedes={'path': auth.authority_path, 'blob_sha256': sha(w26.a_bytes)},
                         extra={'status': 'second version'})
    old_bytes = w26.a_bytes
    change_authority(w26, new_a, approve=False, review=False)
    F26 = t.freeze(w26, a_bytes=old_bytes)
    w26.designate(F26)
    a26 = show(*t.run(w26, F26))
    w26b = t.world()
    old_b = w26b.a_bytes
    change_authority(w26b, hf.authority('syn/PREREG.md', supersedes={'path': auth.authority_path,
                                                                      'blob_sha256': sha(old_b)},
                                        extra={'status': 'second version'}))
    F26b = t.freeze(w26b, a_bytes=old_b)
    w26b.designate(F26b)
    code, res = t.run(w26b, F26b)
    snap = (((res or {}).get('config') or {}).get('admission') or {}).get('simulated_chain', {}).get('snapshot', {})
    b26 = dict(show(code, res), versions=len(snap.get('authority_versions', [])))
    check('TR26', 'a change to A after F\'s base without its review and authorization: ERROR; with them: admitted '
          'under main\'s A, both blobs recorded', "first exit 65; second exit 0 with two authority versions",
          [a26, b26], a26['exit'] == 65 and b26['exit'] == 0 and b26['versions'] == 2)
    # TR27: F based on a main commit without A
    w27 = t.world()
    F27 = t.repo.derive(t.c, {'syn/PREREG.md': t.repo.read(t.freeze(w27), 'syn/PREREG.md')},
                        parents=t.repo.parents(t.c))
    w27.designate(F27)
    check('TR27', 'F based on a main commit that does not yet contain A: ERROR', "exit == 65",
          show(*t.run(w27, F27)), refused(*t.run(w27, F27)))
    # TR28: tool blob differs from its pin; an extra file under the tool
    out28 = []
    for mut in ('blob', 'extra'):
        w28 = t.world()
        a = json.loads(w28.a_bytes)
        a['engine_pins'] = {'tools/ledger_coverage/engine/x.py': sha(b'x = 1\n')}
        files = {'tools/ledger_coverage/engine/x.py': b'x = 2\n' if mut == 'blob' else b'x = 1\n'}
        if mut == 'extra':
            files['tools/ledger_coverage/engine/y.py'] = b'y = 1\n'
        w28 = world_with_authority(a, files)
        F28 = t.freeze(w28)
        w28.designate(F28)
        out28.append(show(*t.run(w28, F28)))
    check('TR28', 'tool blobs at head_sha differing from A.engine_pins, or an extra file under the tool: ERROR at '
          'the tool', "both exit 65", out28, all(o['exit'] == 65 for o in out28))
    # TR48-TR53 (K7, design v5.5.8): the files permitted under the tool directory at head_sha
    k7(t, check, show)
    # TR29: head_sha not on main's first-parent chain; head_sha = X (no workflow, no tool)
    out29 = []
    for mut in ('branch', 'x'):
        w29 = t.world()
        F29 = t.freeze(w29)
        w29.designate(F29)
        if mut == 'branch':
            w29.h.add_commit(hf.REPO_ID, 'b1', [w29.main], dict(w29.h.repos[hf.REPO_ID]['commits'][w29.main]['files']))
            w29.h.runs[w29.run_id]['head_sha'] = 'b1'
        else:
            w29.h.add_commit(hf.REPO_ID, 'xx', [w29.main], {'doc/s.md': b'x\n'})
            w29.add_main('c2', {})
            w29.h.repos[hf.REPO_ID]['commits']['c2']['parents'] = ['xx']
            w29.h.runs[w29.run_id]['head_sha'] = 'xx'
        out29.append(show(*t.run(w29, F29)))
    check('TR29', 'a run whose head_sha is not on main\'s first-parent chain; separately one whose head_sha is the '
          'evaluated commit: ERROR in both', "both exit 65", out29, all(o['exit'] == 65 for o in out29))
    # TR31-TR36: the freeze ledger
    ledger_controls(t, check)
    # TR37-TR39: forms
    w37 = t.world()
    F37 = t.freeze(w37)
    w37.comment(hf.PLAN_ISSUE, 'oi-freeze/1 designate plan=%s round=%s commit=%s\r\nwith a note'
                % (hf.PLAN, hf.ROUND, F37))
    code37, res37 = t.run(w37, F37)
    check('TR37', 'a designation whose first line ends in CRLF is recognized (one trailing CR removed)', "exit == 0",
          show(code37, res37), code37 == 0)
    out38 = []
    for line in ('oi-freeze/1 designate plan=%s round=%s commit=%s ' % (hf.PLAN, hf.ROUND, F37),
                 'oi-freeze/1 designate  plan=%s round=%s commit=%s' % (hf.PLAN, hf.ROUND, F37),
                 'oi-freeze/1 designate plan=%s round=%s commit=%s' % (hf.PLAN, hf.ROUND, F37.upper())):
        w38 = t.world()
        F38 = t.freeze(w38)
        w38.designate(F38)
        w38.comment(hf.PLAN_ISSUE, line.replace(F37, F38).replace(F37.upper(), F38.upper()))
        out38.append(show(*t.run(w38, F38)))
    check('TR38', 'a trailing space, a doubled space or an uppercase hex id: ERROR (malformed form)',
          "all three exit 65 naming a malformed form", out38,
          all(o['exit'] == 65 and 'malformed' in o['message'] for o in out38))
    out39 = []
    for line in ('oi-freeze/2 designate plan=%s round=%s commit=%%s' % (hf.PLAN, hf.ROUND),
                 'oi-freeze/1 designate round=%s plan=%s commit=%%s' % (hf.ROUND, hf.PLAN)):
        w39 = t.world()
        F39 = t.freeze(w39)
        w39.designate(F39)
        w39.comment(hf.PLAN_ISSUE, line % F39)
        out39.append(show(*t.run(w39, F39)))
    check('TR39', 'an unknown version; keys in another order: ERROR', "both exit 65 naming a malformed form", out39,
          all(o['exit'] == 65 and 'malformed' in o['message'] for o in out39))
    # TR40-TR44: authority changes
    authority_change_controls(t, check, show)
    # TR33/TR34: edits into and out of forms
    w33 = t.world()
    F33 = t.freeze(w33)
    w33.designate(F33)
    w33.comment(hf.PLAN_ISSUE, 'a remark', edits=['oi-freeze/1 withdraw plan=%s round=%s commit=%s'
                                                  % (hf.PLAN, hf.ROUND, F33)])
    check('TR33', 'a withdrawal edited into a comment without a form: ERROR (edit history contained a form)',
          "exit == 65", show(*t.run(w33, F33)), refused(*t.run(w33, F33)))
    w34 = t.world()
    F34 = t.freeze(w34)
    w34.designate(F34, edits=['an old remark'])
    check('TR34', 'an old owner comment edited into a designation: ERROR', "exit == 65", show(*t.run(w34, F34)),
          refused(*t.run(w34, F34)))
    # TR35: the residual
    w35 = t.world()
    F35 = t.freeze(w35)
    w35.designate(F35)
    code35, _ = t.run(w35, F35)
    w35b = t.world()
    F35b = t.freeze(w35b)
    w35b.designate(F35b)
    w35b.h.deletions = [{'comment_id': 1, 'author_id': hf.OWNER_ID}]
    code35b, _ = t.run(w35b, F35b)
    check('TR35', 'a withdrawal posted and deleted before any admission, on a host that reports no deletions: not '
          'detected (residual, no refusal claimed); on a host that reports deletions: ERROR',
          "without deletion events the run is admitted (exit 0, the documented residual); with them exit 65",
          {'no_deletion_events': code35, 'deletion_events': code35b}, code35 == 0 and code35b == 65)
    return t


def k7(t, check, show):
    pin_path = 'tools/ledger_coverage/engine/x.py'
    wf_in = 'tools/ledger_coverage/workflow.yml'

    def world(extra, wf_inside=False, a_override=None):
        a = json.loads(hf.jb(hf.authority('syn/PREREG.md')))
        a['engine_pins'] = {pin_path: sha(b'x = 1\n')}
        if wf_inside:
            a['workflow'] = {'path': wf_in, 'content_sha256': sha(hf.WF)}
        files = {pin_path: b'x = 1\n'}
        if wf_inside:
            files[wf_in] = hf.WF
        w = world_with_authority(a, files)
        if wf_inside:
            w.h.runs[w.run_id]['workflow_path'] = wf_in
        if extra:
            w.add_main('c2', extra)
        F = t.freeze(w)
        w.designate(F)
        return w, F
    out = {}
    w, F = world({}, wf_inside=True)
    out['TR48'] = show(*t.run(w, F))
    a_path = auth.authority_path
    w, F = world({})
    cur = w.h.repos[hf.REPO_ID]['commits'][w.main]['files'][a_path]
    w.add_main('c2', {a_path: cur[:-2] + b' \n'})
    out['TR49'] = show(*t.run(w, F))
    w, F = world({wf_in: hf.WF + b'#'}, wf_inside=True)
    out['TR50'] = show(*t.run(w, F))
    tr51 = {}
    for name, val in (('content', b'{}\n'), ('symlink', ('symlink', 'elsewhere.json')),
                      ('submodule', ('submodule', 'ab' * 20))):
        w, F = world({})
        w.h.repos[hf.REPO_ID]['commits'][w.main]['files'][a_path] = val
        tr51['authority ' + name] = show(*t.run(w, F))
        w, F = world({}, wf_inside=True)
        w.h.repos[hf.REPO_ID]['commits'][w.main]['files'][wf_in] = val if name != 'content' else b'other\n'
        tr51['workflow ' + name] = show(*t.run(w, F))
    w, F = world({'tools/ledger_coverage/engine/extra.py': b'y = 1\n'})
    out['TR52'] = show(*t.run(w, F))
    w, F = world({})
    w.add_main('c3', {'tools/ledger_coverage/authority-copy.json':
                      w.h.repos[hf.REPO_ID]['commits'][w.main]['files'][a_path]})
    out['TR53'] = show(*t.run(w, F))
    check('TR48', 'a head_sha whose tool directory holds exactly the pinned files, the approved authority record and '
          'the approved workflow: accepted (execution identity holds)', "exit == 0", out['TR48'],
          out['TR48']['exit'] == 0)
    check('TR49', 'the authority record at head_sha modified by one byte: ERROR', "exit == 65", out['TR49'],
          out['TR49']['exit'] == 65)
    check('TR50', 'the workflow at A.workflow.path modified by one byte: ERROR', "exit == 65", out['TR50'],
          out['TR50']['exit'] == 65)
    check('TR51', 'a substituted file at either permitted path (other content, a symlink, a submodule): ERROR in each '
          'case', "all six cases exit 65", tr51, all(v['exit'] == 65 for v in tr51.values()))
    check('TR52', 'an additional file under the tool directory, neither pinned nor permitted: ERROR', "exit == 65",
          out['TR52'], out['TR52']['exit'] == 65)
    check('TR53', 'a byte-identical second copy of the authority record at another path: ERROR', "exit == 65",
          out['TR53'], out['TR53']['exit'] == 65)


def cfg_field_run(t, cfg):
    files = {t.p: sf.jb(cfg)}
    c2 = t.repo.derive(t.c, files, parents=t.repo.parents(t.c))
    old_c = t.c
    t.c = c2
    try:
        w = t.world()
        F = t.freeze(w)
        w.designate(F)
        code, res = t.run(w, F)
    finally:
        t.c = old_c
    return code, stop(res)


def world_with_owner(owner_id):
    w = hf.World('syn/PREREG.md')
    a = hf.authority('syn/PREREG.md', owner_id=owner_id)
    return world_with_authority(a, {}, owner_id)


def world_with_authority(a, extra_files, owner_id=None):
    """A fresh world whose first A is `a` (approved, reviewed and merged by its owner), plus files at main."""
    owner_id = owner_id or a['owner']['id']
    w = hf.World.__new__(hf.World)
    w.h = hf.hostmod.MemoryHost()
    w.h.add_repo(hf.REPO_ID, 'fixture/repo')
    w.pin_table_path = 'syn/PREREG.md'
    w.a = a
    w.a_bytes = hf.jb(a)
    w.ledger = {'schema': auth.ledger_schema, 'events': []}
    w.ledger_bytes = hf.jb(w.ledger)
    w.review = hf.jb({'schema': 'oi-review-record/1', 'reviewer': 'reviewer-b',
                      'reviewed': {'path': auth.authority_path, 'blob_sha256': sha(w.a_bytes)}, 'previous': 'none',
                      'method': 'read A', 'verdicts': [{'item': 'A', 'verdict': 'accept'}]})
    w.t, w.cid = 0, 0
    w.comments = {(hf.REPO_ID, hf.PLAN_ISSUE): [], (hf.REPO_ID, hf.AUTH_ISSUE): []}
    w.h.threads = w.comments
    hf.bootstrap(w, owner_id, extra_files)
    return w


def change_authority(w, new_a, merged_by=None, approve=True, review=True, approver=None, edited=False,
                     after=False, quote=None, extra_approver=None):
    """Lands a new A on the world's main through (or around) the authority-change procedure."""
    old_sha = sha(w.a_bytes)
    new_b = hf.jb(new_a)
    new_sha = sha(new_b)
    files = {auth.authority_path: new_b}
    if approve and not after:
        w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (old_sha, quote or new_sha),
                  author_id=approver or w.a['owner']['id'], edits=['x'] if edited else [])
    if extra_approver is not None:
        w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (old_sha, new_sha), author_id=extra_approver)
    if review:
        files[auth.review_path(new_a, new_sha)] = hf.jb({
            'schema': 'oi-review-record/1', 'reviewer': 'reviewer-b',
            'reviewed': {'path': auth.authority_path, 'blob_sha256': new_sha}, 'previous': old_sha,
            'method': 'read both', 'verdicts': [{'item': 'A', 'verdict': 'accept'}]})
    w.add_main('c%d' % (len(w.h.repos[hf.REPO_ID]['commits']) + 1), files,
               merged_by=merged_by if merged_by is not None else w.a['owner']['id'])
    if approve and after:
        w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (old_sha, new_sha),
                  author_id=approver or w.a['owner']['id'])
    w.a, w.a_bytes = new_a, new_b
    return new_b


def authority_change_controls(t, check, show):
    def case(**kw):
        w = t.world()
        old = w.a_bytes
        owner = kw.pop('owner_id', None)
        new_a = hf.authority('syn/PREREG.md', owner_id=owner or hf.OWNER_ID,
                             supersedes={'path': auth.authority_path, 'blob_sha256': sha(old)},
                             extra={'status': 'second version'})
        change_authority(w, new_a, **kw)
        F = t.freeze(w, a_bytes=old)
        w.designate(F, author_id=owner or hf.OWNER_ID)
        return show(*t.run(w, F))
    a40 = case(approve=False)
    check('TR40', 'an A change merged by the owner with no approval comment: ERROR', "exit == 65", a40,
          a40['exit'] == 65)
    a41 = [case(quote='0' * 64), case(after=True)]
    check('TR41', 'an approval quoting another blob hash, or created after the merge: ERROR', "both exit 65", a41,
          all(o['exit'] == 65 for o in a41))
    a42 = case(edited=True)
    check('TR42', 'an approval comment edited: ERROR', "exit == 65", a42, a42['exit'] == 65)
    a43 = case(approver=31337)
    check('TR43', 'an approval by another numeric id: ERROR', "exit == 65", a43, a43['exit'] == 65)
    a44 = case(owner_id=5555)
    a44ok = case(owner_id=5555, extra_approver=5555)
    check('TR44', 'an owner-id change approved only by the old id: ERROR (the new id must approve too)',
          "exit 65 naming the new id's approval when only the old id approves; when the new id approves as well the "
          "authority change is admitted, and admission stops only at point 7 (the fixture configuration names the old "
          "owner id)", [a44, a44ok], a44['exit'] == 65 and 'new id' in a44['message'] and
          a44ok['exit'] == 65 and 'retirement.owner' in a44ok['message'])


def ledger_controls(t, check):
    def ev(kind, F, comment, by=None):
        return {'plan': hf.PLAN, 'round': hf.ROUND, 'kind': kind, 'commit': F, 'by': by,
                'comment_id': comment['id'], 'author_id': comment['author_id'], 'created_at': comment['created_at'],
                'edited': False, 'first_line': auth.first_line(comment['body']),
                'body_sha256': sha(comment['body'].encode())}

    def with_ledger_event(w, event):
        # the whole procedure: authority approval, append comment, review record, owner merge
        w.land_ledger(hf.jb({'schema': auth.ledger_schema, 'events': [event]}))
    out31 = {}
    for mut in ('deleted', 'hidden', 'edited'):
        w = t.world()
        F = t.freeze(w)
        w.designate(F)
        wd = w.comment(hf.PLAN_ISSUE, 'oi-freeze/1 withdraw plan=%s round=%s commit=%s' % (hf.PLAN, hf.ROUND, F))
        with_ledger_event(w, ev('withdraw', F, wd))
        if mut == 'deleted':
            w.comments[(hf.REPO_ID, hf.PLAN_ISSUE)].remove(wd)
        elif mut == 'hidden':
            wd['hidden'] = True
        else:
            wd['edits'] = ['earlier']
        code, res = t.run(w, F)
        out31[mut] = (code, stop(res), ((res or {}).get('stop') or {}).get('message', '')[:100])
    check('TR31', 'a withdrawal committed in the freeze ledger, whose comment is later deleted, hidden or edited: F '
          'stays withdrawn in all three; never reactivated', "all three exit 65", out31,
          all(v[0] == 65 for v in out31.values()))
    # TR32: a supersession in an earlier committed snapshot, comment deleted
    w = t.world()
    F = t.freeze(w)
    w.designate(F)
    sp = w.comment(hf.PLAN_ISSUE, 'oi-freeze/1 supersede plan=%s round=%s commit=%s by=%s'
                   % (hf.PLAN, hf.ROUND, F, 'cd' * 20))
    snapshot = {'events': [ev('supersede', F, sp, by='cd' * 20)]}
    w.add_main('c9', {'syn/freeze/landings/round-1/snapshot.json': hf.jb(snapshot)})
    w.comments[(hf.REPO_ID, hf.PLAN_ISSUE)].remove(sp)
    code, res = t.run(w, F)
    check('TR32', 'a supersession committed in an earlier acceptance snapshot, whose comment is later deleted: the '
          'supersession binds', "exit == 65", (code, stop(res)), code == 65)
    # TR36: ledger missing, unverifiable, conflicting
    out36 = {}
    w = t.world()
    F = t.freeze(w)
    w.designate(F)
    w.add_main('c9', {hf.LEDGER_PATH: None})
    out36['missing'] = t.run(w, F)[0]
    w = t.world()
    F = t.freeze(w)
    w.designate(F)
    w.add_main('c9', {hf.LEDGER_PATH: hf.jb({'schema': auth.ledger_schema, 'events': [{'x': 1}]})})
    out36['unverifiable'] = t.run(w, F)[0]
    w = t.world()
    F = t.freeze(w)
    d = w.designate(F)
    bad = ev('designate', F, d)
    bad['first_line'] = 'something else'
    with_ledger_event(w, bad)
    out36['conflicting'] = t.run(w, F)[0]
    check('TR36', 'the freeze ledger missing, unverifiable, or conflicting with the thread: ERROR',
          "all three exit 65", out36, all(v == 65 for v in out36.values()))
    # TR47: acceptance-time appends without a valid append comment
    out47 = {}
    for mut in ('none', 'other-hash', 'other-id', 'edited', 'hidden', 'other-thread', 'after-merge', 'malformed'):
        w = t.world()
        F = t.freeze(w)
        d = w.designate(F)
        old = w.ledger_bytes
        new = hf.jb({'schema': auth.ledger_schema, 'events': [ev('designate', F, d)]})
        line = 'oi-freeze-ledger/1 append plan=%s round=%s from=%s to=%s' % (hf.PLAN, hf.ROUND, sha(old), sha(new))
        kw = {}
        issue = hf.PLAN_ISSUE
        if mut == 'other-hash':
            line = line.replace(sha(new), '0' * 64)
        elif mut == 'other-id':
            kw = {'author_id': 4243}
        elif mut == 'edited':
            kw = {'edits': ['x']}
        elif mut == 'hidden':
            kw = {'hidden': True}
        elif mut == 'other-thread':
            issue = 99
        elif mut == 'malformed':
            line = line.replace('oi-freeze-ledger/1', 'oi-freeze-ledger/2')
        # the authority approval, the review record and the owner merge are present in every case; only the append
        # comment varies
        w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (sha(old), sha(new)))
        if mut not in ('none', 'after-merge'):
            w.comment(issue, line, **kw)
        w.add_main('c9', dict(hf.ledger_review_file(w.a, new, sha(old)), **{hf.LEDGER_PATH: new}))
        if mut == 'after-merge':
            w.comment(issue, line)
        code, res = t.run(w, F)
        out47[mut] = code
    w = t.world()
    F = t.freeze(w)
    d = w.designate(F)
    with_ledger_event(w, ev('designate', F, d))
    pos = t.run(w, F)[0]
    check('TR47', 'an acceptance-time append to the freeze ledger with no valid append comment (none, other hashes, '
          'other id, edited, hidden, other thread, after the merge, malformed): refused; later admissions refuse',
          "all eight exit 65; the same append with a valid append comment is admitted (exit 0)",
          dict(out47, valid=pos), all(v == 65 for v in out47.values()) and pos == 0)


# ---- corrections after the second independent review (F1, F2, F3) -------------------------------------------------

def f1_controls(t):
    """F1: each freeze-ledger change is approved by the owner of the authority version in force when that ledger
    change merged (sec. 6.3). The owner changes 4242 -> 5555 through a verified authority change; the fixture
    configuration names the old owner, so a run that passes the ledger history stops at point 7 (retirement.owner),
    and a refused ledger history stops naming the freeze-ledger change."""
    NEW = 5555

    def ledger_change(w, approver, via, rnd):
        # an append to the current ledger (the ledger is append-only, sec. 6.3)
        old = w.ledger_bytes
        new = hf.jb({'schema': auth.ledger_schema, 'events': json.loads(old.decode('utf-8'))['events'] + [
            {'plan': hf.PLAN, 'round': rnd, 'kind': 'withdraw', 'commit': 'ab' * 20, 'comment_id': 1,
             'author_id': approver, 'created_at': '2026-11-23T00:00:00Z', 'first_line': 'x'}]})
        # `approver` writes the comment of the named form; the owner in force writes the other, reviews are present and
        # the owner in force merges, so only that comment's author decides
        current = w.a['owner']['id']
        w.comment(hf.PLAN_ISSUE, 'oi-freeze-ledger/1 append plan=%s round=%s from=%s to=%s'
                  % (hf.PLAN, hf.ROUND, sha(old), sha(new)), author_id=approver if via == 'append' else current)
        w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (sha(old), sha(new)),
                  author_id=approver if via == 'authority' else current)
        w.add_main('c%d' % (len(w.h.repos[hf.REPO_ID]['commits']) + 1),
                   dict(hf.ledger_review_file(w.a, new, sha(old)), **{hf.LEDGER_PATH: new}), merged_by=current)
        w.ledger_bytes = new

    def owner_change(w):
        new_a = hf.authority('syn/PREREG.md', owner_id=NEW,
                             supersedes={'path': auth.authority_path, 'blob_sha256': sha(w.a_bytes)},
                             extra={'status': 'second version'})
        change_authority(w, new_a, extra_approver=NEW)

    def scenario(steps):
        w = t.world()
        a1 = w.a_bytes
        for kind, approver, via, rnd in steps:
            if kind == 'owner':
                owner_change(w)
            else:
                ledger_change(w, approver, via, rnd)
        F = t.freeze(w, a_bytes=a1)
        w.designate(F, author_id=w.a['owner']['id'])
        code, res = t.run(w, F)
        msg = ((res or {}).get('stop') or {}).get('message', '')
        return {'exit': code, 'stop': stop(res), 'message': msg[:200],
                'ledger_refused': 'freeze-ledger change' in msg, 'past_ledger': 'retirement.owner' in msg}
    out = {
        'former-owner-append-after-change': scenario([('owner', None, None, None),
                                                      ('ledger', hf.OWNER_ID, 'append', 'r0')]),
        'former-owner-authority-form-after-change': scenario([('owner', None, None, None),
                                                              ('ledger', hf.OWNER_ID, 'authority', 'r0')]),
        'then-owner-before-change': scenario([('ledger', hf.OWNER_ID, 'append', 'r0'),
                                              ('owner', None, None, None)]),
        'new-owner-after-change': scenario([('ledger', hf.OWNER_ID, 'append', 'r0'), ('owner', None, None, None),
                                            ('ledger', NEW, 'append', 'r9')]),
    }
    refused = [out['former-owner-append-after-change'], out['former-owner-authority-form-after-change']]
    valid = [out['then-owner-before-change'], out['new-owner-after-change']]
    check('R3-F1', 'after a verified owner change 4242 -> 5555, a freeze-ledger change merged later and approved only '
          'by 4242 (append form in the plan thread; separately the authority form in the authority thread) is '
          'refused; a ledger change approved by 4242 and merged before the owner change stays valid, and one merged '
          'after it and approved by 5555 is valid',
          "both former-owner cases exit 65 naming the freeze-ledger change; both valid cases pass the ledger history "
          "(admission stops only at point 7, retirement.owner)", out,
          all(o['exit'] == 65 and o['ledger_refused'] for o in refused) and
          all(o['exit'] == 65 and o['past_ledger'] and not o['ledger_refused'] for o in valid))


def f2_controls(r):
    """F2: a side-change class record referenced by the configuration is chain-linted in op C (sec. 6.3): one
    without a review record and an owner authorization gives FAIL record-invalid and classifies nothing."""
    def scenario(with_class, reviewed):
        syn = sf.Syn()
        edits = [('# synthetic', ['# synthetic', '', 'Preface line one.'])]
        pd = sf.patch_doc(syn.H, edits)
        base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}}
        c0, p0, s0, f0 = syn.build(base)
        recs = json.loads(f0[p0])['records']
        M = syn.repo.derive(syn.H, {'notes/side.txt': b'side change on main\n'}, parents=[syn.H], subject='M')
        cls = {'schema': 'oi-side-change-classes/1', 'record_id': 'syn-classes', 'author': sf.WRITER,
               'supersedes': None,
               'classes': [{'id': 'notes', 'prefixes': ['notes/'], 'reason': 'synthetic',
                            'pins': [{'path': 'notes/side.txt', 'git_blob': syn.repo.blob_id(M, 'notes/side.txt'),
                                      'blob_sha256': sha(b'side change on main\n')}]}]}
        files = dict(base['files'])
        v = dict(base)
        if with_class:
            cb = sf.jb(cls)
            files['syn/classes.json'] = cb
            extra = [{'kind': 'side-change-classes', 'path': 'syn/classes.json', 'blob_sha256': sha(cb)}]
            if reviewed:
                extra += syn.chain(files, 'syn/classes.json', sf.REVIEWER)
            v['extra'] = {'records': recs + extra}
        v['files'] = files
        c, p, s, f = syn.build(v)
        X = syn.repo.derive(syn.H, {sf.DOC: sf.apply_text(syn.repo.read(syn.H, sf.DOC).decode(), edits).encode()},
                            parents=[syn.H], subject='X')
        w = hf.World('syn/PREREG.md')
        listed = {q: syn.repo.read(c, q) for q in syn.repo.paths(c) if q.startswith('syn/') and q.endswith('.json')}
        Ff = {'syn/PREREG.md': hf.pin_table({q[len('syn/'):]: sha(b) for q, b in listed.items()}),
              auth.authority_path: w.a_bytes}
        F = syn.repo.derive(c, Ff, parents=syn.repo.parents(c), subject='freeze')
        w.designate(F)
        argv = ['execution', '--config', '%s:%s' % (F, p), '--out', r.out()] + w.args(F) + \
            ['--scientific-base', syn.H, '--candidate', X, '--ledger', '%s:syn/patch.json' % F, '--main', M]
        code, res = cli.run(argv, repo=syn.repo, stderr=io.StringIO(), control=w.control(), environ={})
        items = sorted({(i['class'], str(i.get('subject'))) for i in (res or {}).get('items', [])
                        if i['class'] in ('record-invalid', 'side-change-unclassified', 'base-drift')})
        return {'exit': code, 'outcome': (res or {}).get('outcome'), 'stop': stop(res), 'items': items}
    out = {'none': scenario(False, False), 'reviewed': scenario(True, True), 'unreviewed': scenario(True, False)}
    un = out['unreviewed']
    check('R3-F2', 'op C: a side-change class record referenced by the configuration with no review record and no '
          'owner authorization: FAIL record-invalid, and the side change stays unclassified; the reviewed and '
          'authorized record classifies it; with no class record it is side-change-unclassified',
          "unreviewed: exit 20, record-invalid on syn/classes.json and side-change-unclassified on notes/side.txt; "
          "reviewed: no record-invalid and no side-change-unclassified; none: side-change-unclassified", out,
          un['exit'] == 20 and ('record-invalid', 'syn/classes.json') in un['items'] and
          ('side-change-unclassified', 'notes/side.txt') in un['items'] and
          not out['reviewed']['items'] and
          ('side-change-unclassified', 'notes/side.txt') in out['none']['items'])


def f3_controls(t):
    """F3: the consumer's predicate checks that head_sha contains the authority record, blob-equal to the admitted
    A (sec. 5, trust-root point 3)."""
    w = t.world()
    F = t.freeze(w)
    w.designate(F)
    code, res = t.run(w, F)
    snap = res['config']['admission']['simulated_chain']['snapshot']
    pins = {'engine': res['engine']['blob_sha256'], 'config': res['config']['blob_sha256'],
            'adapters': {a['name']: a['module_sha256'] for a in res.get('adapters', [])},
            'admission': {k: snap[k] for k in ('freeze', 'designation_comment_id', 'pin_table_sha256',
                                               'authority_sha256')}}
    host_pins = dict(pins, repository_id=hf.REPO_ID, workflow_path=hf.WF_PATH, workflow_sha256=sha(hf.WF),
                     engine_pins={}, authority_blob_sha256=sha(w.a_bytes))

    def at_head(head_files):
        """A main commit with the given change becomes the run's head; the result names it."""
        w2 = copy.deepcopy(w)
        w2.add_main('c9', head_files)
        chain = copy.deepcopy(res)
        del chain['harness']
        s2 = copy.deepcopy(snap)
        s2['run']['head_sha'] = 'c9'
        chain['config']['admission'] = {'mode': 'chain', 'snapshot': s2,
                                        'snapshot_sha256': res['config']['admission']['snapshot_sha256']}
        raw = util.dump_result(chain).encode('utf-8')
        w2.h.artifacts[(w2.run_id, 'ledger-coverage-result')] = sha(raw)
        landing = {'evaluated': s2.get('evaluated'), 'artifact_name': 'ledger-coverage-result',
                   'result_sha256': sha(raw)}
        return checker.accept_with_host(raw, 0, host_pins, w2.h, landing)
    out = {'present': at_head({'syn/unrelated.txt': b'x\n'}),
           'absent': at_head({auth.authority_path: None}),
           'different': at_head({auth.authority_path: w.a_bytes + b' '})}
    check('R3-F3', 'the consumer check: a run whose head_sha lacks the authority record, or holds one that differs '
          'from the admitted A, is not accepted; the same result with A present and equal is accepted',
          "accept_with_host is true for present, false for absent and for different", out,
          out['present'] is True and out['absent'] is False and out['different'] is False)


# ---- corrections after the third independent review (B1, B2, B3, N2) ----------------------------------------------

def _r4_event(tag):
    return {'plan': hf.PLAN, 'round': tag, 'kind': 'withdraw', 'commit': 'ab' * 20, 'comment_id': 1, 'author_id': 1,
            'created_at': '2026-11-23T00:00:00Z', 'first_line': 'x'}


def _r4_ledger(tags):
    return hf.jb({'schema': auth.ledger_schema, 'events': [_r4_event(x) for x in tags]})


def _r4_approve(w, old, new, approver, via):
    """via 'all': both approval comments the procedure needs; 'append': only the oi-freeze-ledger/1 append comment;
    'authority': only the oi-authority/1 approve comment."""
    if via in ('all', 'append'):
        w.comment(hf.PLAN_ISSUE, 'oi-freeze-ledger/1 append plan=%s round=%s from=%s to=%s'
                  % (hf.PLAN, hf.ROUND, sha(old), sha(new)), author_id=approver)
    if via in ('all', 'authority'):
        w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (sha(old), sha(new)), author_id=approver)


def _r4_set_ledger(w, new, via, approver=None, approve=True, after=False, direct=False):
    """One freeze-ledger change on the world's main, with its review record: approved (before, or after, the change)
    by `approver` (the owner in force by default) through the comments `via` names, landed by a recorded pull-request
    merge by the owner or, with `direct`, by a push with no merge record."""
    old = w.ledger_bytes
    who = approver if approver is not None else w.a['owner']['id']
    if approve and not after:
        _r4_approve(w, old, new, who, via)
    cid = 'c%d' % (len(w.h.repos[hf.REPO_ID]['commits']) + 1)
    if direct:
        files = dict(w.h.repos[hf.REPO_ID]['commits'][w.main]['files'])
        files[hf.LEDGER_PATH] = new
        files.update(hf.ledger_review_file(w.a, new, sha(old)))
        w.h.add_commit(hf.REPO_ID, cid, [w.main], files)
        w.main = cid
        w.h.repos[hf.REPO_ID]['main'] = cid
        w.h.runs[w.run_id]['head_sha'] = cid
    else:
        w.add_main(cid, dict(hf.ledger_review_file(w.a, new, sha(old)), **{hf.LEDGER_PATH: new}),
                   merged_by=w.a['owner']['id'])
    if approve and after:
        _r4_approve(w, old, new, who, via)
    w.ledger_bytes = new


def _r4_owner_change(w, owner):
    new_a = hf.authority('syn/PREREG.md', owner_id=owner,
                         supersedes={'path': auth.authority_path, 'blob_sha256': sha(w.a_bytes)},
                         extra={'status': 'v-%d-%d' % (owner, len(w.h.repos[hf.REPO_ID]['commits']))})
    change_authority(w, new_a, extra_approver=owner if owner != w.a['owner']['id'] else None)


def _r4_run(t, steps):
    """A fresh world, the steps applied to it, then a designated freeze carrying the first A. The fixture
    configuration names owner 4242: a run whose ledger history is verified exits 0 when 4242 is the final owner."""
    w = t.world()
    a1 = w.a_bytes
    steps(w)
    # F is frozen after the steps, its configuration authorized by the owner in force then (sec. 6.3, "Owner at
    # creation"); the configuration names owner 4242
    F = t.refreeze(w, a_bytes=a1, retirement_owner=hf.OWNER_ID)
    w.designate(F, author_id=w.a['owner']['id'])
    code, res = t.run(w, F)
    msg = ((res or {}).get('stop') or {}).get('message', '')
    return {'exit': code, 'stop': stop(res), 'message': msg[:220], 'ledger_refused': 'freeze-ledger change' in msg}


def r4_b1_controls(t):
    """B1: an approval comment authorizes exactly one change, and each ledger version extends the previous one."""
    OLD, NEW = hf.OWNER_ID, 5555
    out = {}
    for via in ('all', 'append', 'authority'):
        def r1(w, via=via):
            l0 = w.ledger_bytes
            _r4_set_ledger(w, _r4_ledger(['one']), via, OLD)          # A approves L0 -> L1
            _r4_owner_change(w, NEW)                                   # A -> B
            _r4_set_ledger(w, l0, via, NEW)                            # B approves the revert L1 -> L0
            _r4_owner_change(w, OLD)                                   # B -> A
            _r4_set_ledger(w, _r4_ledger(['one']), via, approve=False)  # L0 -> L1 again, no new approval

        def r2(w, via=via):
            l0 = w.ledger_bytes
            _r4_set_ledger(w, _r4_ledger(['one']), via, OLD)
            _r4_set_ledger(w, l0, via, OLD)
            _r4_set_ledger(w, _r4_ledger(['one']), via, approve=False)

        def r3(w, via=via):
            _r4_set_ledger(w, _r4_ledger(['one']), via, OLD)
            _r4_owner_change(w, NEW)
            _r4_owner_change(w, OLD)
            _r4_set_ledger(w, _r4_ledger(['two']), via, approve=False)

        def legit(w, via=via):
            for tags in (['one'], ['one', 'two'], ['one', 'two', 'three']):
                _r4_set_ledger(w, _r4_ledger(tags), via)

        def legit_owner(w, via=via):
            _r4_set_ledger(w, _r4_ledger(['one']), via)
            _r4_owner_change(w, NEW)
            _r4_set_ledger(w, _r4_ledger(['one', 'two']), via)
            _r4_owner_change(w, OLD)
            _r4_set_ledger(w, _r4_ledger(['one', 'two', 'three']), via)
        out['R1 A->B->A replay [%s]' % via] = _r4_run(t, r1)
        out['R2 replay, no owner change [%s]' % via] = _r4_run(t, r2)
        out['R3 different change, no approval [%s]' % via] = _r4_run(t, r3)
        out['appends, each approved [%s]' % via] = _r4_run(t, legit)
        out['appends across A->B->A, each approved by the owner in force [%s]' % via] = _r4_run(t, legit_owner)
    bad = [v for k, v in out.items() if k.startswith(('R1', 'R2', 'R3')) or not k.endswith('[all]')]
    good = [v for k, v in out.items() if k.startswith('appends') and k.endswith('[all]')]
    check('R4-B1', 'freeze-ledger approvals cannot be replayed (sec. 6.3, "append-only"; "its own explicit owner '
          'approval comment"): R1 (approve L0->L1; owner A->B; B approves the revert L1->L0; B->A; L0->L1 again with '
          'no new approval) and R2 (the same with no owner change) are refused, and R3 (a different change with no '
          'approval) stays refused; a sequence of appends, each with its own approval comments by the owner in force '
          '(both the oi-authority/1 approve and the oi-freeze-ledger/1 append comment, [all]), is admitted, also '
          'across an owner change and change-back; every case approved by only one of the two comments ([append], '
          '[authority]) is refused (sec. 6.3, "How it changes", and N3: none stands in for the other)',
          "R1, R2, R3 and every [append] and [authority] case: exit 65 naming the freeze-ledger change; the [all] "
          "append sequences: exit 0", out,
          all(o['exit'] == 65 and o['ledger_refused'] for o in bad) and all(o['exit'] == 0 for o in good))
    # each guard on its own: with the append-only check disabled the single-use check refuses R1 and R2, and with
    # the single-use check disabled the append-only check refuses them
    guards = {}
    for name, attr, stub in (('single-use alone', '_ledger_extension_problem', lambda old, new: None),
                             ('append-only alone', '_fresh', lambda hits, consumed, point, what: hits)):
        orig = getattr(auth, attr, None)
        if orig is None:
            guards[name] = 'the engine has no %s' % attr
            continue
        setattr(auth, attr, stub)
        try:
            got = {}
            for via in ('all',):
                got['R1 [%s]' % via] = _r4_run(t, lambda w, via=via: (
                    _r4_set_ledger(w, _r4_ledger(['one']), via, OLD), _r4_owner_change(w, NEW),
                    _r4_set_ledger(w, _r4_ledger([]), via, NEW), _r4_owner_change(w, OLD),
                    _r4_set_ledger(w, _r4_ledger(['one']), via, approve=False)))
                got['R2 [%s]' % via] = _r4_run(t, lambda w, via=via: (
                    _r4_set_ledger(w, _r4_ledger(['one']), via, OLD), _r4_set_ledger(w, _r4_ledger([]), via, OLD),
                    _r4_set_ledger(w, _r4_ledger(['one']), via, approve=False)))
            guards[name] = got
        finally:
            setattr(auth, attr, orig)
    want = {'single-use alone': 'already authorized', 'append-only alone': 'not an append'}
    check('R4-B1-GUARDS', 'each B1 guard refuses the replay on its own: with the append-only check disabled, the '
          'single-use check refuses R1 and R2; with the single-use check disabled, the append-only check refuses them '
          '(with both approval comments; one comment alone authorizes no append, R4-B1)',
          "every case exits 65 naming the freeze-ledger change, with 'already authorized' (single-use alone) or 'not "
          "an append' (append-only alone) in the message", guards,
          all(isinstance(g, dict) and all(o['exit'] == 65 and o['ledger_refused'] and want[n] in o['message']
                                          for o in g.values()) for n, g in guards.items()))


def r4_b2_controls(t):
    """B2: a freeze-ledger change with no merge record is refused, whatever its approval."""
    out = {}
    for via in ('all', 'append', 'authority'):
        out['direct push, approval after the push [%s]' % via] = _r4_run(
            t, lambda w, via=via: _r4_set_ledger(w, _r4_ledger(['d']), via, after=True, direct=True))
        out['direct push, approval before the push [%s]' % via] = _r4_run(
            t, lambda w, via=via: _r4_set_ledger(w, _r4_ledger(['d']), via, direct=True))
        out['pull-request merge, approval before the merge [%s]' % via] = _r4_run(
            t, lambda w, via=via: _r4_set_ledger(w, _r4_ledger(['d']), via))
    bad = [v for k, v in out.items() if k.startswith('direct') or not k.endswith('[all]')]
    good = [v for k, v in out.items() if k.startswith('pull-request') and k.endswith('[all]')]
    check('R4-B2', 'a freeze-ledger change landed with no merge record (a direct push; the host reports no merged '
          'pull request) is refused, with the approval created after the push (P9) and also before it; the same '
          'change merged by pull request with both approval comments created before the merge is admitted; with only '
          'one of the two comments every case is refused',
          "direct pushes and every [append] and [authority] case: exit 65 naming the freeze-ledger change; the [all] "
          "pull-request merge: exit 0", out,
          all(o['exit'] == 65 and o['ledger_refused'] for o in bad) and all(o['exit'] == 0 for o in good))


def _r4_class_scenario(r, cls_mut=None, verdicts=None):
    """Op C over a synthetic side change on main and a configuration-referenced side-change class record with its
    review (the given verdicts; one accept for class `notes` by default) and owner authorization."""
    syn = sf.Syn()
    edits = [('# synthetic', ['# synthetic', '', 'Preface line one.'])]
    pd = sf.patch_doc(syn.H, edits)
    base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}}
    c0, p0, s0, f0 = syn.build(base)
    recs = json.loads(f0[p0])['records']
    M = syn.repo.derive(syn.H, {'notes/side.txt': b'side change on main\n'}, parents=[syn.H], subject='M')
    cls = {'schema': 'oi-side-change-classes/1', 'record_id': 'syn-classes', 'author': sf.WRITER,
           'supersedes': None,
           'classes': [{'id': 'notes', 'prefixes': ['notes/'], 'reason': 'synthetic',
                        'pins': [{'path': 'notes/side.txt', 'git_blob': syn.repo.blob_id(M, 'notes/side.txt'),
                                  'blob_sha256': sha(b'side change on main\n')}]}]}
    if cls_mut:
        cls_mut(cls)
    files = dict(base['files'])
    cb = sf.jb(cls)
    files['syn/classes.json'] = cb
    ref = {'path': 'syn/classes.json', 'blob_sha256': sha(cb)}
    vs = verdicts if verdicts is not None else [{'item': 'notes', 'verdict': 'accept'}]
    rv = {'schema': 'oi-review-record/1', 'reviewer': sf.REVIEWER, 'reviewed': ref, 'method': 'read',
          'verdicts': vs}
    files['syn/classes.review.json'] = sf.jb(rv)
    au = {'schema': 'oi-owner-authorization/1', 'owner': sf.OWNER, 'time': sf.AUTH_TIME, 'comment_id': 'c-2',
          'authorizes': [{'record': ref, 'review': {'path': 'syn/classes.review.json',
                                                    'blob_sha256': sha(files['syn/classes.review.json'])}}]}
    files['syn/classes.auth.json'] = sf.jb(au)
    extra = [{'kind': 'side-change-classes', 'path': 'syn/classes.json', 'blob_sha256': sha(cb)},
             {'kind': 'review', 'path': 'syn/classes.review.json',
              'blob_sha256': sha(files['syn/classes.review.json'])},
             {'kind': 'authorization', 'path': 'syn/classes.auth.json',
              'blob_sha256': sha(files['syn/classes.auth.json'])}]
    v = dict(base, files=files, extra={'records': recs + extra})
    c, p, s, f = syn.build(v)
    X = syn.repo.derive(syn.H, {sf.DOC: sf.apply_text(syn.repo.read(syn.H, sf.DOC).decode(), edits).encode()},
                        parents=[syn.H], subject='X')
    w = hf.World('syn/PREREG.md')
    listed = {q: syn.repo.read(c, q) for q in syn.repo.paths(c) if q.startswith('syn/') and q.endswith('.json')}
    Ff = {'syn/PREREG.md': hf.pin_table({q[len('syn/'):]: sha(b) for q, b in listed.items()}),
          auth.authority_path: w.a_bytes}
    F = syn.repo.derive(c, Ff, parents=syn.repo.parents(c), subject='freeze')
    w.designate(F)
    argv = ['execution', '--config', '%s:%s' % (F, p), '--out', r.out()] + w.args(F) + \
        ['--scientific-base', syn.H, '--candidate', X, '--ledger', '%s:syn/patch.json' % F, '--main', M]
    try:
        code, res = cli.run(argv, repo=syn.repo, stderr=io.StringIO(), control=w.control(), environ={})
    except Exception as exc:
        return {'exit': 'EXCEPTION', 'exception': '%s: %s' % (type(exc).__name__, exc)}
    its = (res or {}).get('items', [])
    return {'exit': code, 'stop': stop(res),
            'record_invalid': sorted(str(i.get('subject')) for i in its if i['class'] == 'record-invalid'),
            'unclassified': sorted(str(i.get('subject')) for i in its if i['class'] == 'side-change-unclassified')}


def r4_b3_controls(r):
    """B3: every list entry of a reviewed record carries its id field; a record where one does not is record-invalid
    and its verdicts cannot fall back to the record id."""
    def scenario(cls_mut=None, verdicts=None):
        return _r4_class_scenario(r, cls_mut, verdicts)

    def second_without_id(c):
        c['classes'].append({'prefixes': ['other/'], 'reason': 'x', 'pins': []})

    def none_with_id(c):
        for k in c['classes']:
            k.pop('id')
    acc = lambda *ids: [{'item': i, 'verdict': 'accept'} for i in ids]  # noqa: E731
    out = {'C0 reviewed and authorized, one verdict per class': scenario(),
           'C9 a second class without id; one verdict, on the record id': scenario(second_without_id,
                                                                                    acc('syn-classes')),
           'C9b a second class without id; verdicts on notes and on the record id': scenario(
               second_without_id, acc('notes', 'syn-classes')),
           'C8 no class has an id; one verdict, on the record id': scenario(none_with_id, acc('syn-classes'))}
    bad = [v for k, v in out.items() if not k.startswith('C0')]
    pos = out['C0 reviewed and authorized, one verdict per class']
    check('R4-B3', 'a side-change class record one of whose classes lacks its id field (C9, and C9b with a verdict '
          'for the class that has one), or all of whose classes lack it (C8), is record-invalid (sec. 6.3: one '
          'verdict per item id; a missing field is record-invalid); no verdict on the record id stands in for the '
          'per-item verdicts; the side change stays unclassified; no exception; the record with ids and one verdict '
          'per class classifies the side change',
          "C9, C9b, C8: exit 20, record-invalid on syn/classes.json, notes/side.txt unclassified; C0: exit 10, no "
          "record-invalid, nothing unclassified", out,
          all(o['exit'] == 20 and 'syn/classes.json' in o['record_invalid'] and 'notes/side.txt' in o['unclassified']
              for o in bad) and
          pos.get('exit') == 10 and not pos.get('record_invalid') and not pos.get('unclassified'))


def r4_b2_provenance_controls(t):
    """B2 (provenance): a change of the ledger or of A whose merge record is inconsistent with the commit it claims is
    refused: the record names another merge commit; the version's commit is off main's first-parent chain; the
    commit is not the one that introduced the version; the merge times do not increase along the history."""
    def report_history(w, edit):
        """The host reports the freeze ledger's history through `edit` (an altered or inconsistent host record)."""
        orig = w.h.file_history

        def fh(repo_id, path):
            hist = orig(repo_id, path)
            return edit(w, hist) if path == hf.LEDGER_PATH else hist
        w.h.file_history = fh

    def other_merge_commit(w):
        _r4_set_ledger(w, _r4_ledger(['m']), 'all')
        w.h.merges[(hf.REPO_ID, w.main)]['merge_commit'] = 'c1'

    def off_chain(w):
        _r4_set_ledger(w, _r4_ledger(['m']), 'all')
        cm = w.h.repos[hf.REPO_ID]['commits'][w.main]
        w.h.add_commit(hf.REPO_ID, 'side', list(cm['parents']), cm['files'], merged_by=hf.OWNER_ID,
                       merged_at=w.h.merges[(hf.REPO_ID, w.main)]['merged_at'])

        def edit(w, hist):
            return [dict(v, commit='side', merge_commit='side') if v['commit'] == w.ledger_commit else v
                    for v in hist]
        w.ledger_commit = w.main
        report_history(w, edit)

    def not_introducing(w):
        _r4_set_ledger(w, _r4_ledger(['m']), 'all')
        intro = w.main
        w.add_main('c%d' % (len(w.h.repos[hf.REPO_ID]['commits']) + 1), {'syn/unrelated.txt': b'x\n'})
        later = w.main

        def edit(w, hist):
            return [dict(v, commit=later, parent=intro, merge_commit=later) if v['commit'] == intro else v
                    for v in hist]
        report_history(w, edit)

    def merge_times(w):
        _r4_set_ledger(w, _r4_ledger(['m']), 'all')
        first = w.main
        _r4_set_ledger(w, _r4_ledger(['m', 'n']), 'all')
        w.h.merges[(hf.REPO_ID, first)]['merged_at'] = '2026-11-23T00:00:59Z'

    def authority_other_merge_commit(w):
        _r4_owner_change(w, 5555)
        w.h.merges[(hf.REPO_ID, w.main)]['merge_commit'] = 'c1'

    def consistent(w):
        _r4_set_ledger(w, _r4_ledger(['m']), 'all')
        _r4_set_ledger(w, _r4_ledger(['m', 'n']), 'all')
    out = {'merge record names another merge commit': _r4_run(t, other_merge_commit),
           'version reported at a commit off main\'s first-parent chain': _r4_run(t, off_chain),
           'version reported at a commit that did not introduce it': _r4_run(t, not_introducing),
           'merge times do not increase along the history': _r4_run(t, merge_times),
           'A change whose merge record names another merge commit': _r4_run(t, authority_other_merge_commit),
           'consistent merge records (positive)': _r4_run(t, consistent)}
    for k, v in out.items():
        v['authority_refused'] = 'authority change' in v['message']
    bad = [v for k, v in out.items() if k.startswith(('merge', 'version'))]
    check('R4-B2-PROV', 'a freeze-ledger change whose merge record is inconsistent with the commit it claims is '
          'refused: the record names another merge commit; the version is reported at a commit off main\'s '
          'first-parent chain; at a commit that did not introduce it; merge times that do not increase; an A change '
          'whose merge record names another merge commit is refused as well; consistent records are admitted',
          "the four ledger cases exit 65 naming the freeze-ledger change; the A case exits 65 naming the authority "
          "change; the consistent case exits 0", out,
          all(o['exit'] == 65 and o['ledger_refused'] for o in bad) and
          out['A change whose merge record names another merge commit']['exit'] == 65 and
          out['A change whose merge record names another merge commit']['authority_refused'] and
          out['consistent merge records (positive)']['exit'] == 0)


def r4_b3_duplicate_controls(r):
    """B3 (duplicates): an item id given to two items of a record, or two verdicts for one item, is record-invalid;
    two classes of a class record sharing an id are ERROR CONFIG_INCONSISTENT (S7, Z11), also in chain mode."""
    from ledger_coverage.engine import records as rec

    def lint(ids, verdicts):
        d = {'schema': 'oi-hit-classification/1', 'record_id': 'h', 'author': 'writer-a', 'supersedes': None,
             'classifications': [{'id': i} for i in ids]}
        db = util.canonical(d)
        ref = {'path': 'r/h.json', 'blob_sha256': sha(db)}
        rb = util.canonical({'schema': 'oi-review-record/1', 'reviewer': 'reviewer-b', 'reviewed': ref,
                             'method': 'read', 'verdicts': [{'item': i, 'verdict': v} for i, v in verdicts]})
        ab = util.canonical({'schema': 'oi-owner-authorization/1', 'owner': 7, 'time': 't0', 'comment_id': 'c-1',
                             'authorizes': [{'record': ref, 'review': {'path': 'r/h.review.json',
                                                                       'blob_sha256': sha(rb)}}]})
        st = rec.Store([('r/h.json', db), ('r/h.review.json', rb), ('r/h.auth.json', ab)])
        return rec.lint_chain(ref, st, 7, {sha(x) for x in (db, rb, ab)})

    def dup_class(c):
        c['classes'].append(dict(c['classes'][0], prefixes=['other/']))
    acc = [{'item': 'notes', 'verdict': 'accept'}]
    out = {'lint: distinct ids, one verdict each (positive)': lint(['a', 'b'], [('a', 'accept'), ('b', 'accept')]),
           'lint: id a given to two items': lint(['a', 'a'], [('a', 'accept')]),
           'lint: two verdicts for item b (reject, then accept)': lint(['a', 'b'], [('a', 'accept'), ('b', 'reject'),
                                                                                     ('b', 'accept')]),
           'op C: two classes with id notes, reviewed and authorized': _r4_class_scenario(r, dup_class, acc + acc),
           'op C: one class, two verdicts for notes (reject, then accept)': _r4_class_scenario(
               r, None, [{'item': 'notes', 'verdict': 'reject'}] + acc)}
    pos = out['lint: distinct ids, one verdict each (positive)']
    two = out['op C: one class, two verdicts for notes (reject, then accept)']
    check('R4-B3-DUP', 'an item id given to more than one item of a record, or an item given more than one verdict, '
          'makes the record record-invalid; a class record defining one class id twice is ERROR CONFIG_INCONSISTENT '
          '(S7, Z11) in chain mode; distinct ids with one verdict each lint clean',
          "the positive lint is empty; the duplicate-id lint names the id; the duplicate-verdict lint reports it; "
          "op C with the duplicate class id stops 65 CONFIG_INCONSISTENT; op C with two verdicts for notes is exit "
          "20 with record-invalid on syn/classes.json and notes/side.txt unclassified", out,
          pos == [] and any('more than one item' in x for x in out['lint: id a given to two items']) and
          any('more than one verdict' in x for x in out['lint: two verdicts for item b (reject, then accept)']) and
          out['op C: two classes with id notes, reviewed and authorized'].get('exit') == 65 and
          out['op C: two classes with id notes, reviewed and authorized'].get('stop') == 'CONFIG_INCONSISTENT' and
          two.get('exit') == 20 and 'syn/classes.json' in two.get('record_invalid', []) and
          'notes/side.txt' in two.get('unclassified', []))


def r4_n2_controls(t):
    """N2: the consumer predicate hashes the result bytes it is given and requires that hash to equal the run's
    uploaded artifact and the landing record's result hash."""
    w = t.world()
    F = t.freeze(w)
    w.designate(F)
    code, res = t.run(w, F)
    snap = res['config']['admission']['simulated_chain']['snapshot']
    pins = {'engine': res['engine']['blob_sha256'], 'config': res['config']['blob_sha256'],
            'adapters': {a['name']: a['module_sha256'] for a in res.get('adapters', [])},
            'admission': {k: snap[k] for k in ('freeze', 'designation_comment_id', 'pin_table_sha256',
                                               'authority_sha256')},
            'repository_id': hf.REPO_ID, 'workflow_path': hf.WF_PATH, 'workflow_sha256': sha(hf.WF),
            'engine_pins': {}, 'authority_blob_sha256': sha(w.a_bytes)}
    chain = copy.deepcopy(res)
    del chain['harness']
    chain['config']['admission'] = {'mode': 'chain', 'snapshot': snap,
                                    'snapshot_sha256': res['config']['admission']['snapshot_sha256']}
    raw = util.dump_result(chain).encode('utf-8')
    w.h.artifacts[(w.run_id, 'ledger-coverage-result')] = sha(raw)
    landing = {'evaluated': snap.get('evaluated'), 'artifact_name': 'ledger-coverage-result', 'result_sha256': sha(raw)}
    forged = copy.deepcopy(chain)
    forged['covered_paths'] = ['forged/path']
    forged['items'] = []
    forged_raw = util.dump_result(forged).encode('utf-8')
    out = {}
    for name, data in (('genuine bytes', raw), ('forged bytes, landing quotes the genuine artifact hash', forged_raw),
                       ('genuine bytes plus one byte', raw + b' ')):
        try:
            out[name] = checker.accept_with_host(data, 0, pins, w.h, landing)
        except Exception as exc:
            out[name] = '%s: %s' % (type(exc).__name__, exc)
    check('R4-N2', 'the consumer predicate binds the result it is given to the run\'s uploaded artifact (sec. 5, "the '
          'result file is that run\'s uploaded artifact, by sha256"): it hashes the raw result bytes itself; a forged '
          'result presented with a landing record that quotes the genuine artifact\'s hash is not accepted',
          "accept_with_host(raw bytes, ...) is True for the genuine bytes and False for the forged bytes and for the "
          "genuine bytes with one byte added", out,
          out['genuine bytes'] is True and all(v is False for k, v in out.items() if k != 'genuine bytes'))



# ---- corrections after the fourth independent review (K1, K2, N6) ------------------------------------------------

def r5_k1_controls(t):
    """K1: a committed admission snapshot never designates. A recorded withdrawal or supersession binds only by
    revoking its `commit`; `by` is designated only by an owner form present in the thread now; a recorded event that
    names a comment present in the thread requires that comment's author to be the owner (sec. 6.3, reconciliation;
    admission points 3, 4 and 6)."""
    snap_path = hf.LEDGER_PATH.rsplit('/', 1)[0] + '/landings/forged/snapshot.json'

    def ev(kind, F, by=None, cid=777777, author=hf.OWNER_ID, at='2026-11-23T00:00:58Z'):
        line = 'oi-freeze/1 %s plan=%s round=%s commit=%s' % (kind, hf.PLAN, hf.ROUND, F) + (
            ' by=%s' % by if by else '')
        return {'plan': hf.PLAN, 'round': hf.ROUND, 'kind': kind, 'commit': F, 'by': by, 'comment_id': cid,
                'author_id': author, 'created_at': at, 'first_line': line}

    def show(code, res):
        return {'exit': code, 'stop': stop(res), 'message': ((res or {}).get('stop') or {}).get('message', '')[:180],
                'designation_comment_id': (((res or {}).get('config') or {}).get('admission') or {}).get(
                    'simulated_chain', {}).get('snapshot', {}).get('designation_comment_id')}
    out = {}
    # S0: the owner designates F; a run for F is admitted
    w = t.world()
    F = t.freeze(w)
    w.designate(F)
    out['S0 owner designates F; run for F'] = show(*t.run(w, F))
    # S1: a snapshot landed by another account with no approval records a supersession of F by F2 whose comment is
    # not in the thread; no owner comment names F2
    w = t.world()
    F = t.freeze(w)
    F2 = t.freeze(w, extra={'syn/other.txt': b'2\n'})
    w.designate(F)
    w.add_main('c9', {snap_path: hf.jb({'events': [ev('supersede', F, by=F2)]})}, merged_by=31337)
    out['S1 snapshot supersedes F by F2, comment absent; run for F2'] = show(*t.run(w, F2))
    # S2: as S1, the event names a comment present in the thread, written by a non-owner account
    w = t.world()
    F = t.freeze(w)
    F2 = t.freeze(w, extra={'syn/other.txt': b'2\n'})
    w.designate(F)
    c = w.comment(hf.PLAN_ISSUE, 'oi-freeze/1 supersede plan=%s round=%s commit=%s by=%s'
                  % (hf.PLAN, hf.ROUND, F, F2), author_id=31337, login='someone')
    w.add_main('c9', {snap_path: hf.jb({'events': [ev('supersede', F, by=F2, cid=c['id'], author=31337,
                                                      at=c['created_at'])]})}, merged_by=31337)
    out['S2 snapshot supersession bound to a non-owner comment in the thread; run for F2'] = show(*t.run(w, F2))
    # S3: no owner comment; the snapshot holds a designation of F and its supersession by F2
    w = t.world()
    F = t.freeze(w)
    F2 = t.freeze(w, extra={'syn/other.txt': b'2\n'})
    w.add_main('c9', {snap_path: hf.jb({'events': [ev('designate', F, at='2026-11-23T00:00:30Z'),
                                                   ev('supersede', F, by=F2, cid=777778)]})}, merged_by=31337)
    out['S3 no owner comment; snapshot designates F and supersedes it by F2; run for F2'] = show(*t.run(w, F2))
    # S4: a snapshot withdrawal of F (the restrictive direction)
    w = t.world()
    F = t.freeze(w)
    w.designate(F)
    w.add_main('c9', {snap_path: hf.jb({'events': [ev('withdraw', F)]})}, merged_by=31337)
    out['S4 snapshot withdraws F; run for F'] = show(*t.run(w, F))
    # S5: the owner's supersession of F by F2, committed in a snapshot, its comment later deleted; the owner then
    # designates F2 in the thread: F2 is admitted (the recorded supersession keeps F revoked)
    w = t.world()
    F = t.freeze(w)
    F2 = t.freeze(w, extra={'syn/other.txt': b'2\n'})
    w.designate(F)
    sp = w.comment(hf.PLAN_ISSUE, 'oi-freeze/1 supersede plan=%s round=%s commit=%s by=%s'
                   % (hf.PLAN, hf.ROUND, F, F2))
    w.add_main('c9', {snap_path: hf.jb({'events': [ev('supersede', F, by=F2, cid=sp['id'], at=sp['created_at'])]})})
    w.comments[(hf.REPO_ID, hf.PLAN_ISSUE)].remove(sp)
    d2 = w.designate(F2)
    out['S5 owner supersession committed, comment deleted; owner designates F2; run for F2'] = show(*t.run(w, F2))
    out['S5 owner supersession committed, comment deleted; owner designates F2; run for F2']['want_comment'] = d2['id']
    out['S5b the same; run for F'] = show(*t.run(w, F))
    # S6: the owner's supersession present in the thread and committed in a snapshot: F2 is admitted by that comment
    w = t.world()
    F = t.freeze(w)
    F2 = t.freeze(w, extra={'syn/other.txt': b'2\n'})
    w.designate(F)
    sp = w.comment(hf.PLAN_ISSUE, 'oi-freeze/1 supersede plan=%s round=%s commit=%s by=%s'
                   % (hf.PLAN, hf.ROUND, F, F2))
    w.add_main('c9', {snap_path: hf.jb({'events': [ev('supersede', F, by=F2, cid=sp['id'], at=sp['created_at'])]})})
    out['S6 owner supersession in the thread and in a snapshot; run for F2'] = show(*t.run(w, F2))
    out['S6 owner supersession in the thread and in a snapshot; run for F2']['want_comment'] = sp['id']
    refused = [out[k] for k in out if k.startswith(('S1', 'S2', 'S3', 'S4', 'S5b'))]
    admitted = [out[k] for k in out if k.startswith(('S0', 'S5 ', 'S6'))]
    check('R5-K1', 'a committed admission snapshot is no source of authority (sec. 6.3: "a designation must be '
          'present and verifiable in the thread now"; forms are read only from owner comments): a recorded '
          'supersession revokes its commit and never designates its `by`; a recorded event naming a comment present '
          'in the thread requires the owner as its author. S1 (snapshot supersession, comment absent) and S2 (bound to '
          'a non-owner comment) do not admit F2; S3 (snapshot alone) and S4 (snapshot withdrawal) refuse; S0 admits '
          'the owner\'s F; S5 (committed owner supersession, comment deleted, owner designates F2) admits F2 by that '
          'designation and keeps F revoked; S6 (owner supersession in the thread) admits F2 by that comment',
          "S1, S2, S3, S4, S5b: exit 65 CONFIG_UNREVIEWED; S0, S5, S6: exit 0, S5 and S6 with designation_comment_id "
          "the owner's comment", out,
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' for o in refused) and
          all(o['exit'] == 0 for o in admitted) and
          all(o['designation_comment_id'] == o['want_comment'] for o in admitted if 'want_comment' in o))


def r5_k2_controls(t):
    """K2: every freeze-ledger change passes the authority-change procedure (sec. 6.3, "How it changes": an owner
    oi-authority/1 approve comment in the authority thread, an independent review record naming both ledger blobs, and
    a pull-request merge by the owner) and, when it adds events, also carries its own oi-freeze-ledger/1 append comment
    by the owner in force in the thread of a plan A lists, naming that plan and one of its rounds (N3). Every component
    is required; none substitutes for another."""
    L = _r4_ledger

    def land(**kw):
        def steps(w):
            w.land_ledger(L(['a']), **kw)
        return steps

    def with_review(doc_edit):
        def steps(w):
            old, new = w.ledger_bytes, L(['a'])
            rv = json.loads(hf.ledger_review(new, sha(old)).decode())
            doc_edit(rv)
            w.land_ledger(new, review=hf.jb(rv))
        return steps

    def authority_form_in_plan_thread(w):
        old, new = w.ledger_bytes, L(['a'])
        w.comment(hf.PLAN_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (sha(old), sha(new)))
        w.land_ledger(new, authority=False)

    def legit_sequence(w):
        for tags in (['a'], ['a', 'b'], ['a', 'b', 'c']):
            w.land_ledger(L(tags))

    def second_without_append(w):
        w.land_ledger(L(['a']))
        w.land_ledger(L(['a', 'b']), append=False)
    out = {
        'L2 [authority]: authority comment, review and owner merge, no append comment': _r4_run(t, land(append=False)),
        'L2 [append]: append comment only, merged by 31337, no review, no authority comment':
            _r4_run(t, land(authority=False, review=False, merged_by=31337)),
        'missing: the authority comment': _r4_run(t, land(authority=False)),
        'missing: the review record': _r4_run(t, land(review=False)),
        'missing: the owner merge (merged by 31337)': _r4_run(t, land(merged_by=31337)),
        'review naming another previous ledger blob': _r4_run(t, with_review(lambda d: d.update(previous='0' * 64))),
        'review by the owner': _r4_run(t, with_review(lambda d: d.update(reviewer=hf.OWNER_LOGIN))),
        'review with a reject verdict': _r4_run(t, with_review(lambda d: d.update(
            verdicts=[{'item': 'ledger', 'verdict': 'reject'}]))),
        'L3 append comment naming a plan A does not list': _r4_run(t, land(plan='other-plan')),
        'L3 append comment naming the plan and a round A does not list': _r4_run(t, land(rnd='r9')),
        'append comment in the authority thread, not the plan thread': _r4_run(t, land(issue=hf.AUTH_ISSUE)),
        'authority comment in the plan thread, not the authority thread': _r4_run(t, authority_form_in_plan_thread),
        'a second append without its append comment': _r4_run(t, second_without_append),
        'all four components (positive)': _r4_run(t, land()),
        'appends, each with all four components (positive)': _r4_run(t, legit_sequence)}
    bad = [v for k, v in out.items() if '(positive)' not in k]
    good = [v for k, v in out.items() if '(positive)' in k]
    check('R5-K2', 'a freeze-ledger change is admitted only with all four components: the owner\'s oi-authority/1 '
          'approve comment in the authority thread, an independent review record naming both ledger blobs, a merge by '
          'the owner, and its own oi-freeze-ledger/1 append comment in the thread of a plan A lists, naming that plan '
          'and one of its rounds (sec. 6.3, "How it changes"; N3; TR47); L2 [authority], L2 [append], each component '
          'missing in turn, an invalid review, an unlisted plan or round (L3) and comments in the wrong thread refuse',
          "every refusal case exits 65 naming the freeze-ledger change; both positive cases exit 0", out,
          all(o['exit'] == 65 and o['ledger_refused'] for o in bad) and all(o['exit'] == 0 for o in good))


def r5_n6_controls(r):
    """N6: a side-change class record whose `classes` is an object, not a list, is record-invalid (sec. 6.3, a field
    error), never an internal error."""
    def as_object(c):
        c['classes'] = {'notes': c['classes'][0]}
    got = _r4_class_scenario(r, as_object)
    pos = _r4_class_scenario(r)
    check('R5-N6', 'a side-change class record referenced by the configuration whose classes field is an object: '
          'FAIL record-invalid, the side change unclassified, no exception and no INTERNAL exit; the record with a '
          'class list classifies it',
          "object: exit 20, record-invalid on syn/classes.json, notes/side.txt unclassified; list: exit 10, nothing "
          "record-invalid or unclassified", {'object': got, 'list': pos},
          got.get('exit') == 20 and 'syn/classes.json' in got.get('record_invalid', []) and
          'notes/side.txt' in got.get('unclassified', []) and pos.get('exit') == 10 and
          not pos.get('record_invalid') and not pos.get('unclassified'))

# ---- design v5.5.8: owner at creation (DI-1), TR54-TR70 ----------------------------------------------------------

NEW_OWNER, THIRD_OWNER = 5555, 6666


def _show(code, res):
    return {'exit': code, 'stop': stop(res), 'message': ((res or {}).get('stop') or {}).get('message', '')[:200],
            'record_invalid': sorted({str(i.get('subject')) for i in (res or {}).get('items', [])
                                      if i['class'] == 'record-invalid'})}


def _point5(t, w, F):
    """The control harness of admission points 1-6 (sec. 6.3), on the in-memory host: whether `F` is the one
    designated commit of the round at point 5 (the configuration's own chain, point 7, is not evaluated)."""
    try:
        _, snap, _, _ = auth.admit(w.h, t.repo, w.run_id, hf.PLAN, hf.ROUND, F, t.p)
    except auth.Refused as exc:
        return {'admitted': False, 'point': exc.point, 'message': exc.message[:200]}
    return {'admitted': True, 'designation': snap.get('designation_comment_id')}


def _full(t, w, F):
    """The full chain on the in-memory host: points 1-7 and the run."""
    return _show(*t.run(w, F))


def _point7(o):
    """A refusal at admission point 7: ERROR CONFIG_UNREVIEWED from the owner field or the configuration's own
    authorization (its review chain), not from points 1-6."""
    return o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' and \
        ('retirement.owner' in o['message'] or 'configuration review chain' in o['message'])


def _owner_change(w, owner):
    """A verified authority change to `owner`, approved by the owner in force and (for an owner-id change) by `owner`,
    both before the merge."""
    _r4_owner_change(w, owner)


def _designate(w, F, owner):
    return w.designate(F, author_id=owner, login='login-%d' % owner)


def _form(w, line, owner):
    return w.comment(hf.PLAN_ISSUE, line, author_id=owner, login='login-%d' % owner)


def _ledger_with(w, cid):
    old = json.loads(w.ledger_bytes.decode('utf-8'))['events']
    return hf.jb({'schema': auth.ledger_schema, 'events': old + [
        {'plan': hf.PLAN, 'round': 'r0', 'kind': 'withdraw', 'commit': 'ab' * 20, 'comment_id': cid,
         'author_id': w.a['owner']['id'], 'created_at': '2026-11-23T00:00:01Z', 'first_line': 'x'}]})


def _ledger_comments(w, new, author):
    old = w.ledger_bytes
    w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (sha(old), sha(new)), author_id=author)
    w.comment(hf.PLAN_ISSUE, 'oi-freeze-ledger/1 append plan=%s round=%s from=%s to=%s'
              % (hf.PLAN, hf.ROUND, sha(old), sha(new)), author_id=author)


def _ledger_merge(w, new, merged_by):
    old = w.ledger_bytes
    w.add_main('c%d' % (len(w.h.repos[hf.REPO_ID]['commits']) + 1),
               dict(hf.ledger_review_file(w.a, new, sha(old)), **{hf.LEDGER_PATH: new}), merged_by=merged_by)
    w.ledger_bytes = new


def _landing(w, new):
    """The landing check of the acceptance landing carrying `new` (not merged): refused, or the approvals."""
    old = w.ledger_bytes
    try:
        got = auth.check_ledger_landing(w.h, hf.REPO_ID, new, hf.ledger_review(new, sha(old)))
    except auth.Refused as exc:
        return {'merges': False, 'point': exc.point, 'message': exc.message[:220]}
    except Exception as exc:  # an engine without the landing check: the control fails, it does not abort the group
        return {'merges': None, 'error': '%s: %s' % (type(exc).__name__, exc)}
    return {'merges': True, 'approvals': got}


def _owner_at_creation_refusal(o):
    return 'Owner at creation' in o.get('message', '')


def tr54_tr61(t):
    out = {}
    # TR54 (D1)
    w = t.world()
    F = t.freeze(w)
    _designate(w, F, hf.OWNER_ID)
    _owner_change(w, NEW_OWNER)
    first = {'point5': _point5(t, w, F), 'full': _full(t, w, F)}
    _designate(w, F, NEW_OWNER)
    second = {'point5': _point5(t, w, F), 'full': _full(t, w, F)}
    out['TR54'] = {'former owner only': first, 'then 5555 designates F': second}
    check('TR54', '(review probe D1) owner 4242 designates F; an owner change 4242 -> 5555 merges; no later '
          'designation: ERROR (missing designation; the former owner\'s designation does not count). Separately, 5555 '
          'then designates F: F is the one designated commit at point 5 (control harness); in a full chain, ERROR '
          'CONFIG_UNREVIEWED at point 7, since F\'s configuration authorization predates the owner change and F must '
          'be re-frozen',
          "first: point 5 refuses (point 'state', F not the one designated commit) and the full chain exits 65 "
          "CONFIG_UNREVIEWED; second: point 5 admits F by 5555's designation, and the full chain exits 65 "
          "CONFIG_UNREVIEWED at point 7", out['TR54'],
          not first['point5']['admitted'] and first['point5'].get('point') == 'state' and
          'not the one designated' in first['point5'].get('message', '') and
          first['full']['exit'] == 65 and first['full']['stop'] == 'CONFIG_UNREVIEWED' and
          second['point5']['admitted'] and _point7(second['full']))
    # TR55 (D2)
    w = t.world()
    F = t.freeze(w)
    _designate(w, F, hf.OWNER_ID)
    _form(w, 'oi-freeze/1 withdraw plan=%s round=%s commit=%s' % (hf.PLAN, hf.ROUND, F), hf.OWNER_ID)
    _owner_change(w, NEW_OWNER)
    _designate(w, F, NEW_OWNER)
    o = {'point5': _point5(t, w, F), 'full': _full(t, w, F)}
    check('TR55', '(D2) 4242 designates and then withdraws F, the withdrawal not in the freeze ledger; 4242 -> 5555; '
          '5555 designates F: ERROR (designation of a withdrawn commit: the withdrawal, an owner comment at its '
          'creation, binds after the owner change)',
          "point 5 refuses with 'a revoked commit is designated again'; the full chain exits 65 CONFIG_UNREVIEWED", o,
          not o['point5']['admitted'] and 'designated again' in o['point5'].get('message', '') and
          o['full']['exit'] == 65 and o['full']['stop'] == 'CONFIG_UNREVIEWED')
    # TR56 (D3)
    w = t.world()
    F = t.freeze(w)
    _designate(w, F, NEW_OWNER)
    _owner_change(w, NEW_OWNER)
    o = {'point5': _point5(t, w, F), 'full': _full(t, w, F)}
    check('TR56', '(D3) 5555 designates F while 4242 is the owner; then 4242 -> 5555; no later designation: ERROR '
          '(missing designation: the comment is not an owner comment)',
          "point 5 refuses (point 'state', F not the one designated commit); the full chain exits 65 "
          "CONFIG_UNREVIEWED", o,
          not o['point5']['admitted'] and o['point5'].get('point') == 'state' and
          'not the one designated' in o['point5'].get('message', '') and o['full']['exit'] == 65 and
          o['full']['stop'] == 'CONFIG_UNREVIEWED')

    # TR57 (L5) and TR58 (L6): the ledger change, each ledger route separately
    def ledger_case(approver, before):
        """Both approval comments by `approver`, created before the owner changes `before` (a list of owners);
        returns the landing route (an acceptance landing carrying the change, not merged) and the main route (the
        change merged on main by the owner in force, then an admission)."""
        res = {}
        for route in ('landing', 'main'):
            w = t.world()
            a1 = w.a_bytes
            new = _ledger_with(w, 880001)
            _ledger_comments(w, new, approver)
            for owner in before:
                _owner_change(w, owner)
            if route == 'landing':
                res[route] = _landing(w, new)
            else:
                _ledger_merge(w, new, w.a['owner']['id'])
                F = t.refreeze(w, a_bytes=a1)
                _designate(w, F, w.a['owner']['id'])
                res[route] = _full(t, w, F)
        return res
    o57 = ledger_case(hf.OWNER_ID, [NEW_OWNER, hf.OWNER_ID])
    check('TR57', '(L5) a freeze-ledger change whose oi-authority/1 approve and oi-freeze-ledger/1 append comments '
          '4242 created before 4242 -> 5555 -> 4242, merged after the change back; each ledger route separately: the '
          'change is refused (an owner change merged between the approvals\' creation and the merge): an acceptance '
          'landing carrying it does not merge, and a ledger on main carrying it makes every later admission refuse',
          "landing route: check_ledger_landing refuses, naming Owner at creation; main route: the admission exits 65 "
          "CONFIG_UNREVIEWED naming the freeze-ledger change and Owner at creation", o57,
          o57['landing'].get('merges') is False and _owner_at_creation_refusal(o57['landing']) and
          o57['main']['exit'] == 65 and o57['main']['stop'] == 'CONFIG_UNREVIEWED' and
          'freeze-ledger change' in o57['main']['message'] and _owner_at_creation_refusal(o57['main']))
    o58 = ledger_case(NEW_OWNER, [NEW_OWNER])
    check('TR58', '(L6) 5555 creates both approval comments of a freeze-ledger change while 4242 is the owner; 4242 -> '
          '5555; the change merged under 5555; each ledger route separately: refused as in TR57 (the approvals are not '
          'owner comments)',
          "landing route: check_ledger_landing refuses, naming Owner at creation; main route: the admission exits 65 "
          "CONFIG_UNREVIEWED naming the freeze-ledger change and Owner at creation", o58,
          o58['landing'].get('merges') is False and _owner_at_creation_refusal(o58['landing']) and
          o58['main']['exit'] == 65 and o58['main']['stop'] == 'CONFIG_UNREVIEWED' and
          'freeze-ledger change' in o58['main']['message'] and _owner_at_creation_refusal(o58['main']))
    # TR59: A -> B -> A
    w = t.world()
    F = t.freeze(w)
    _designate(w, F, hf.OWNER_ID)
    _owner_change(w, NEW_OWNER)
    _owner_change(w, hf.OWNER_ID)
    o = {'point5': _point5(t, w, F), 'full': _full(t, w, F)}
    check('TR59', '4242 designates F; 4242 -> 5555 -> 4242; no later designation: ERROR (missing designation: an owner '
          'change merged between the designation\'s creation and the admission)',
          "point 5 refuses (point 'state', F not the one designated commit); the full chain exits 65 "
          "CONFIG_UNREVIEWED", o,
          not o['point5']['admitted'] and o['point5'].get('point') == 'state' and
          'not the one designated' in o['point5'].get('message', '') and o['full']['exit'] == 65 and
          o['full']['stop'] == 'CONFIG_UNREVIEWED')
    # TR60: completed actions (positive)
    w = t.world()
    a1 = w.a_bytes
    w.land_ledger(_ledger_with(w, 880002))
    _owner_change(w, NEW_OWNER)
    F = t.refreeze(w, a_bytes=a1)
    _designate(w, F, NEW_OWNER)
    o = _full(t, w, F)
    check('TR60', '(positive) a freeze-ledger append approved by 4242 and merged while 4242 is the owner; later an '
          'owner change 4242 -> 5555 approved by both ids; 5555 designates an F whose configuration authorization 5555 '
          'made after the change: the earlier append and the authority chain verify (completed actions); F admitted',
          "the full chain exits 0", o, o['exit'] == 0)
    # TR61: a former owner's supersession
    res = {}
    for second in (False, True):
        w = t.world()
        F = t.freeze(w)
        F2 = t.freeze(w, extra={'syn/other.txt': b'2\n'})
        _designate(w, F, hf.OWNER_ID)
        _form(w, 'oi-freeze/1 supersede plan=%s round=%s commit=%s by=%s' % (hf.PLAN, hf.ROUND, F, F2), hf.OWNER_ID)
        _owner_change(w, NEW_OWNER)
        if second:
            _designate(w, F2, NEW_OWNER)
        res['5555 designates F2' if second else 'no later designation'] = {
            'F point5': _point5(t, w, F), 'F full': _full(t, w, F), 'F2 point5': _point5(t, w, F2),
            'F2 full': _full(t, w, F2)}
    a, b = res['no later designation'], res['5555 designates F2']
    check('TR61', '4242 designates F and then supersedes it by F2 in the thread, not in the ledger; 4242 -> 5555. '
          'Separately, 5555 then designates F2: admission of F: ERROR (F withdrawn) in both; admission of F2: ERROR '
          '(missing designation) in the first; in the second, F2 is the one designated commit at point 5 (control '
          'harness), and in a full chain ERROR CONFIG_UNREVIEWED at point 7 as in TR54',
          "F: point 5 refuses (point 'state') and the full chain exits 65 in both; F2, first: point 5 refuses (point "
          "'state', not the one designated) and the full chain exits 65; F2, second: point 5 admits F2 and the full "
          "chain exits 65 CONFIG_UNREVIEWED at point 7", res,
          all(not x['F point5']['admitted'] and x['F point5'].get('point') == 'state' and x['F full']['exit'] == 65
              for x in (a, b)) and
          not a['F2 point5']['admitted'] and 'not the one designated' in a['F2 point5'].get('message', '') and
          a['F2 full']['exit'] == 65 and b['F2 point5']['admitted'] and _point7(b['F2 full']))


def tr62_tr64(t):
    # TR62: an owner-id change, the new id's approval before and after the merge
    res = {}
    for after in (False, True):
        w = t.world()
        a1 = w.a_bytes
        new_a = hf.authority('syn/PREREG.md', owner_id=NEW_OWNER,
                             supersedes={'path': auth.authority_path, 'blob_sha256': sha(w.a_bytes)},
                             extra={'status': 'owner-id change'})
        old_sha = sha(w.a_bytes)
        change_authority(w, new_a, extra_approver=None if after else NEW_OWNER)
        if after:
            w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (old_sha, sha(hf.jb(new_a))),
                      author_id=NEW_OWNER)
        F = t.refreeze(w, a_bytes=a1)
        _designate(w, F, NEW_OWNER)
        res['after the merge' if after else 'both before the merge'] = _full(t, w, F)
    a, b = res['both before the merge'], res['after the merge']
    check('TR62', 'an owner-id change 4242 -> 5555 approved by 4242 and by 5555, both created before the merge; '
          'separately, 5555\'s approval created after the merge: the first verifies (5555\'s approval is authenticated '
          'as the id the new A pins); the second: ERROR',
          "first: the full chain exits 0; second: exits 65 CONFIG_UNREVIEWED naming the authority change's new id",
          res, a['exit'] == 0 and b['exit'] == 65 and b['stop'] == 'CONFIG_UNREVIEWED' and 'new id' in b['message'])
    # TR63: A.supersedes
    res = {}
    for case in ('other blob', 'null'):
        w = t.world()
        a1 = w.a_bytes
        sup = {'path': auth.authority_path, 'blob_sha256': '0' * 64} if case == 'other blob' else None
        change_authority(w, hf.authority('syn/PREREG.md', supersedes=sup, extra={'status': 'second'}))
        F = t.refreeze(w, a_bytes=a1)
        _designate(w, F, hf.OWNER_ID)
        res[case] = _full(t, w, F)
    check('TR63', 'an A on main whose supersedes names a blob other than the version of A preceding it on main\'s '
          'first-parent chain; separately, names null while a version precedes it: ERROR CONFIG_UNREVIEWED in both',
          "both exit 65 CONFIG_UNREVIEWED naming the authority record's supersession", res,
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' and 'supersede' in o['message']
              for o in res.values()))
    # TR64: approvals before a change of A that keeps the owner (positive)
    w = t.world()
    a1 = w.a_bytes
    new = _ledger_with(w, 880003)
    _ledger_comments(w, new, hf.OWNER_ID)
    change_authority(w, hf.authority('syn/PREREG.md', supersedes={'path': auth.authority_path,
                                                                  'blob_sha256': sha(w.a_bytes)},
                                     extra={'status': 'a changed pin, same owner'}))
    _ledger_merge(w, new, hf.OWNER_ID)
    F = t.refreeze(w, a_bytes=a1)
    _designate(w, F, hf.OWNER_ID)
    o = _full(t, w, F)
    check('TR64', '(positive) a freeze-ledger change whose approvals 4242 created before a merged change of A that '
          'keeps owner.id 4242, merged after it: the approvals count (no owner change); the change verifies',
          "the full chain exits 0", o, o['exit'] == 0)


def tr65(t):
    """Authorization records: the configuration's own, and those of the other records (the rule files)."""
    res = {}

    def run(case, which):
        w = t.world()
        a1 = w.a_bytes
        if case == 'future owner':
            at = w.tick()
            _owner_change(w, NEW_OWNER)
            owner, time = NEW_OWNER, at
        elif case == 'away and back':
            at = w.tick()
            _owner_change(w, NEW_OWNER)
            _owner_change(w, hf.OWNER_ID)
            owner, time = hf.OWNER_ID, at
        else:
            _owner_change(w, NEW_OWNER)
            owner, time = NEW_OWNER, w.tick()
        final = w.a['owner']['id']
        good = w.tick()
        if which == 'configuration':
            v = {'cfg_auth_owner': owner, 'cfg_auth_time': time, 'auth_owner': final, 'auth_time': good}
        else:
            v = {'cfg_auth_owner': final, 'cfg_auth_time': good, 'auth_owner': owner, 'auth_time': time}
        F = t.refreeze(w, a_bytes=a1, retirement_owner=final, variant=v)
        _designate(w, F, final)
        return _show(*t.run(w, F))
    for case in ('future owner', 'away and back', 'positive'):
        for which in ('configuration', 'other records'):
            res['%s / %s' % (case, which)] = run(case, which)
    bad_cfg = [res['future owner / configuration'], res['away and back / configuration']]
    bad_rec = [res['future owner / other records'], res['away and back / other records']]
    good = [res['positive / configuration'], res['positive / other records']]
    check('TR65', '(authorization analogue of D3 and L5) an authorization record whose time falls while 4242 is owner '
          'and whose owner is 5555; 4242 -> 5555; 5555 designates F, whose configuration uses it. Separately, 4242\'s '
          'authorization with time before 4242 -> 5555 -> 4242. Separately (positive), 5555\'s authorization with time '
          'after 4242 -> 5555: the first two: ERROR CONFIG_UNREVIEWED for the configuration\'s authorization, FAIL '
          'record-invalid for any other record\'s; the third: admitted',
          "first two, the configuration's own: exit 65 CONFIG_UNREVIEWED naming Owner at creation; the other records' "
          "(the rule files): exit 20 with record-invalid on both rule files; the positive: exit 0 in both forms", res,
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' and 'Owner at creation' in o['message']
              for o in bad_cfg) and
          all(o['exit'] == 20 and {'syn/rules-pat.json', 'syn/rules-allow.json'} <= set(o['record_invalid'])
              for o in bad_rec) and all(o['exit'] == 0 for o in good))


def tr66_tr70(t):
    # TR66
    res = {}
    for by in (NEW_OWNER, hf.OWNER_ID):
        w = t.world()
        F = t.freeze(w)
        _designate(w, F, hf.OWNER_ID)
        _form(w, 'oi-freeze/1 withdraw plan=%s round=%s commit=%s' % (hf.PLAN, hf.ROUND, F), by)
        _owner_change(w, NEW_OWNER)
        d = _designate(w, F, NEW_OWNER)
        res['withdrawal by %d' % by] = dict(_point5(t, w, F), want=d['id'])
    a, b = res['withdrawal by %d' % NEW_OWNER], res['withdrawal by %d' % hf.OWNER_ID]
    check('TR66', '4242 designates F; 5555 posts oi-freeze/1 withdraw of F while 4242 is the owner; 4242 -> 5555; 5555 '
          'designates F (control harness). Separately, the withdrawal posted by 4242 before the change: the first: F '
          'is the one designated commit at point 5 (the withdrawal is not an owner comment and is not processed); the '
          'second: ERROR (designation of a withdrawn commit)',
          "first: point 5 admits F by 5555's designation; second: point 5 refuses with 'designated again'", res,
          a['admitted'] and a.get('designation') == a['want'] and not b['admitted'] and
          'designated again' in b.get('message', ''))
    # TR67
    res = {}
    for edited in (True, False):
        w = t.world()
        F = t.freeze(w)
        c = _form(w, 'a note without a form', hf.OWNER_ID)
        _owner_change(w, NEW_OWNER)
        if edited:
            c['edits'] = [c['body']]
            c['body'] = 'oi-freeze/1 withdraw plan=%s round=%s commit=%s' % (hf.PLAN, hf.ROUND, 'cd' * 20)
        _designate(w, F, NEW_OWNER)
        res['edited' if edited else 'unedited'] = _point5(t, w, F)
    check('TR67', 'a comment without a form, created by 4242 while owner; 4242 -> 5555; the comment then edited by 4242 '
          'into a first line beginning oi-freeze/. Separately, the same comment left unedited: the first: ERROR (point '
          '3); the second: no refusal from point 3 or 4',
          "edited: point 5's harness refuses at point 3 (point 'edits'); unedited: no refusal at point 'edits' or "
          "'forms' (the admission holds)", res,
          not res['edited']['admitted'] and res['edited'].get('point') == 'edits' and res['unedited']['admitted'])
    # TR68: approvals of A changes created under an earlier owner
    def av(owner, prev_bytes, status):
        return hf.authority('syn/PREREG.md', owner_id=owner, supersedes={'path': auth.authority_path,
                                                                         'blob_sha256': sha(prev_bytes)},
                            extra={'status': status})
    res = {}
    for case in ('A', 'B', 'C'):
        w = t.world()
        a1 = w.a_bytes
        v2 = av(NEW_OWNER, w.a_bytes, 'V2')
        if case == 'A':
            v3 = av(NEW_OWNER, hf.jb(v2), 'V3')
            w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (sha(hf.jb(v2)), sha(hf.jb(v3))),
                      author_id=NEW_OWNER)
            change_authority(w, v2, extra_approver=NEW_OWNER)
            change_authority(w, v3, approve=False)
        elif case == 'B':
            v3 = av(hf.OWNER_ID, hf.jb(v2), 'V3')
            v4 = av(hf.OWNER_ID, hf.jb(v3), 'V4')
            w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (sha(hf.jb(v3)), sha(hf.jb(v4))),
                      author_id=hf.OWNER_ID)
            change_authority(w, v2, extra_approver=NEW_OWNER)
            change_authority(w, v3, extra_approver=hf.OWNER_ID)
            change_authority(w, v4, approve=False)
        else:
            v3 = av(THIRD_OWNER, hf.jb(v2), 'V3')
            w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (sha(hf.jb(v2)), sha(hf.jb(v3))),
                      author_id=THIRD_OWNER)
            change_authority(w, v2, extra_approver=NEW_OWNER)
            change_authority(w, v3)
        F = t.refreeze(w, a_bytes=a1)
        _designate(w, F, w.a['owner']['id'])
        res[case] = _full(t, w, F)
    check('TR68', 'V1 (owner 4242) -> V2 (owner 5555) is an owner change. Each case separately, with every other '
          'approval and review in it valid: an A change V2 -> V3 keeping 5555, whose previous-id approval 5555 created '
          'while V1 was in force; an A change V3 -> V4 after V2 -> V3 (5555 -> 4242), whose previous-id approval 4242 '
          'created while V1 was in force; an owner-id change V2 -> V3 (5555 -> 6666), whose new-id approval 6666 '
          'created before V1 -> V2 merged: ERROR in each case: the change does not take effect, and every later '
          'admission refuses',
          "each case: the admission exits 65 CONFIG_UNREVIEWED naming the authority change", res,
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' and 'authority' in o['message']
              for o in res.values()))
    # TR69
    w = t.world()
    F = t.freeze(w)
    F1 = t.freeze(w, extra={'syn/other.txt': b'1\n'})
    _designate(w, F, NEW_OWNER)
    _owner_change(w, NEW_OWNER)
    _form(w, 'oi-freeze/1 withdraw plan=%s round=%s commit=%s' % (hf.PLAN, hf.ROUND, F), NEW_OWNER)
    _designate(w, F1, NEW_OWNER)
    res = {'F': _point5(t, w, F), "F'": _point5(t, w, F1)}
    check('TR69', '5555 designates F while 4242 is the owner; 4242 -> 5555; 5555 withdraws F; 5555 then designates F\': '
          'ERROR (a withdrawal naming a commit never designated: the designation was not an owner comment at its '
          'creation); admission of F\': ERROR',
          "the admissions of F and of F' both refuse at point 5 with 'never designated'", res,
          all(not o['admitted'] and 'never designated' in o.get('message', '') for o in res.values()))
    # TR70
    w = t.world()
    F = t.freeze(w)
    F2 = t.freeze(w, extra={'syn/other.txt': b'2\n'})
    _designate(w, F, hf.OWNER_ID)
    _form(w, 'oi-freeze/1 supersede plan=%s round=%s commit=%s by=%s' % (hf.PLAN, hf.ROUND, F, F2), NEW_OWNER)
    _owner_change(w, NEW_OWNER)
    d = _designate(w, F, NEW_OWNER)
    o = dict(_point5(t, w, F), want=d['id'])
    check('TR70', '4242 designates F; 5555 posts oi-freeze/1 supersede of F by F2 while 4242 is the owner; 4242 -> '
          '5555; 5555 designates F (control harness): F is the one designated commit at point 5 (the supersession is '
          'not an owner comment; neither half is processed)',
          "point 5 admits F by 5555's designation", o, o['admitted'] and o.get('designation') == o['want'])


# ---- design v5.5.8: lineage (DI-2), LN1-LN12, and one verdict per added ledger event ------------------------------

PAT, PAT_REV, PAT_AUTH = 'syn/rules-pat.json', 'syn/rules-pat.review.json', 'syn/rules-pat.auth.json'


def _auth_doc(owner, time, rec_path, rec_bytes, rv_path, rv_bytes, cid='c-ln'):
    return sf.jb({'schema': 'oi-owner-authorization/1', 'owner': owner, 'time': time, 'comment_id': cid,
                  'authorizes': [{'record': {'path': rec_path, 'blob_sha256': sha(rec_bytes)},
                                  'review': {'path': rv_path, 'blob_sha256': sha(rv_bytes)}}]})


def _chain(files, path, owner, time, verdict='accept', review=True, authorize=True):
    """The review record and owner authorization of the record at `path` (written into `files`); returns their
    references for the configuration."""
    from ledger_coverage.engine import records as rec
    doc = json.loads(files[path])
    ref = {'path': path, 'blob_sha256': sha(files[path])}
    rp, ap = path[:-5] + '.review.json', path[:-5] + '.auth.json'
    files.pop(rp, None)
    files.pop(ap, None)
    out = []
    if review:
        files[rp] = sf.jb({'schema': 'oi-review-record/1', 'reviewer': sf.REVIEWER, 'reviewed': ref, 'method': 'read',
                           'verdicts': [{'item': i, 'verdict': verdict} for i in rec.item_ids(doc)]})
        out.append({'kind': 'review', 'path': rp, 'blob_sha256': sha(files[rp])})
        if authorize:
            files[ap] = _auth_doc(owner, time, path, files[path], rp, files[rp])
            out.append({'kind': 'authorization', 'path': ap, 'blob_sha256': sha(files[ap])})
    return out


def _variant_doc(files, src, dst, sup=None, **fields):
    """A rule file at `dst`: the record at `src` with `supersedes` naming `sup` (a path in `files`) and the given
    fields changed (None removes a field)."""
    doc = json.loads(files[src])
    if sup is not None:
        doc['supersedes'] = {'path': sup, 'blob_sha256': sha(files[sup])}
    for k, v in fields.items():
        if v is None:
            doc.pop(k, None)
        else:
            doc[k] = v
    files[dst] = sf.jb(doc)
    return dst


class LN:
    """A synthetic configuration whose rule files form `supersedes` chains, run in the full chain on an in-memory
    host world (sec. 6.3, DI-2)."""

    def __init__(self, r, owner=hf.OWNER_ID, time=sf.AUTH_TIME, variant=None):
        self.r = r
        self.syn = sf.Syn()
        pd = sf.patch_doc(self.syn.H, [])
        v = dict({'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}, 'auth_owner': owner, 'auth_time': time,
                  'owner': owner}, **(variant or {}))
        _, self.p, _, files = self.syn.build(v)
        self.files = dict(files)
        self.cfg = json.loads(self.files[self.p])
        self.owner, self.time = owner, time

    def use_rules(self, replace, extra_records=()):
        """The configuration uses the rule files `replace` maps to (old path -> new path, or None to drop), with
        their chains in `extra_records`; the dropped files' own chains are no longer referenced."""
        dropped = set(replace)
        rules = []
        for ref in self.cfg['rules']:
            if ref['path'] in replace:
                if replace[ref['path']] is not None:
                    rules.append({'path': replace[ref['path']], 'blob_sha256': sha(self.files[replace[ref['path']]])})
            else:
                rules.append(ref)
        self.cfg['rules'] = rules
        stems = {q[:-5] for q in dropped}
        self.cfg['records'] = [x for x in self.cfg['records'] if not any(x['path'].startswith(st + '.')
                                                                         for st in stems)
                               and x.get('kind') != 'superseded-rules'] + list(extra_records)

    def add_rules(self, path, extra_records):
        self.cfg['rules'].append({'path': path, 'blob_sha256': sha(self.files[path])})
        self.cfg['records'] += list(extra_records)

    def commit(self, cfg_owner=None, cfg_time=None, extra_cfg_files=None):
        cb = sf.jb(self.cfg)
        self.files[self.p] = cb
        d = self.p.rsplit('/', 1)[0] + '/'
        cref = {'path': self.p, 'blob_sha256': sha(cb)}
        rv = sf.jb({'schema': 'oi-review-record/1', 'reviewer': sf.REVIEWER, 'reviewed': cref, 'method': 'read',
                    'verdicts': [{'item': self.cfg['config_id'], 'verdict': 'accept'}]})
        self.files[d + 'review.json'] = rv
        self.files[d + 'auth.json'] = _auth_doc(cfg_owner or self.owner, cfg_time or self.time, self.p, cb,
                                                d + 'review.json', rv, cid='c-1')
        for q, b in (extra_cfg_files or {}).items():
            self.files[q] = b(cref) if callable(b) else b
        return self.syn.repo.derive(self.syn.H, self.files, parents=self.syn.repo.parents(self.syn.H),
                                    subject=self.syn.repo.subject(self.syn.H)), sha(cb)

    def run(self, w, **kw):
        c, csha = self.commit(**kw)
        repo = self.syn.repo
        d = self.p.rsplit('/', 1)[0] + '/'
        listed = {q: repo.read(c, q) for q in repo.paths(c) if q.startswith(d) and q.endswith('.json')}
        F = repo.derive(c, {'syn/PREREG.md': hf.pin_table({q[len('syn/'):]: sha(b) for q, b in listed.items()}),
                            auth.authority_path: w.a_bytes}, parents=repo.parents(c), subject='freeze')
        w.designate(F, author_id=w.a['owner']['id'])
        argv = ['terms', '--config', '%s:%s' % (F, self.p), '--out', self.r.out()] + w.args(F) + ['--commit',
                                                                                                    self.syn.H]
        code, res = cli.run(argv, repo=repo, stderr=io.StringIO(), control=w.control(), environ={})
        o = _show(code, res)
        o['rule_files'] = [x['path'] for x in (res or {}).get('rule_files', [])]
        o['why'] = {str(i.get('subject')): ' | '.join(map(str, i.get('detail') or [i.get('evidence', {}).get('why')]))
                    [:400] for i in (res or {}).get('items', []) if i['class'] == 'record-invalid'}
        return o


def _invalid(o, path, word=None):
    return o['exit'] == 20 and path in o['record_invalid'] and (word is None or word in o['why'].get(path, ''))


def _clean(o, path):
    return o['exit'] == 0 and path in o['rule_files'] and not o['record_invalid']


def _ln_pat_v2(r, sup=PAT, dst='syn/rules-pat-v2.json', w=None, chain_kw=None, setup=None, **fields):
    """R2 at `dst`, superseding `sup`, used by the configuration in place of the pattern rule file."""
    x = LN(r)
    if setup is not None:
        setup(x)
    _variant_doc(x.files, PAT, dst, sup=sup, **fields)
    refs = _chain(x.files, dst, x.owner, x.time, **(chain_kw or {}))
    x.use_rules({PAT: dst}, refs)
    return x.run(w or hf.World('syn/PREREG.md'))


def ln1_ln8(r):
    from ledger_coverage.engine import records as rec
    # LN1: in memory, for each kind of S4a; and in a run, for a rule file
    kinds = ['oi-hp-adjudication/1', 'oi-context-adjudication/1', 'oi-hit-classification/1', 'oi-term-rules/2',
             'oi-scope/1', 'oi-side-change-classes/1', 'oi-reconciliation/1', 'oi-retirement-config/1']
    out = {}
    for k in kinds:
        idf = 'config_id' if k == 'oi-retirement-config/1' else 'record_id'
        entries = []

        def chained(path, doc):
            db = util.canonical(doc)
            ref = {'path': path, 'blob_sha256': sha(db)}
            rv = util.canonical({'schema': rec.review_schema, 'reviewer': 'rv', 'reviewed': ref, 'method': 'read',
                                 'verdicts': [{'item': doc[idf], 'verdict': 'accept'}]})
            au = util.canonical({'schema': rec.auth_schema, 'owner': 9001, 'time': 't0', 'comment_id': 'c-9',
                                 'authorizes': [{'record': ref, 'review': {'path': path + '.review',
                                                                           'blob_sha256': sha(rv)}}]})
            entries.extend([(path, db), (path + '.review', rv), (path + '.auth', au)])
            return ref
        pref = chained('r/p.json', {'schema': k, idf: 'p', 'author': 'w', 'supersedes': None})
        sref = chained('r/s.json', {'schema': k, idf: 's', 'author': 'w', 'supersedes': pref})
        st = rec.Store(entries)
        probs = rec.lint_chain(sref, st, 9001, {sha(b) for _, b in entries})
        out[k] = probs[:1]
    run = _ln_pat_v2(r, record_id='another-lineage')
    check('LN1', '(review probe E6) a record superseding a record of the same kind and schema, present at F, with '
          'another record_id; for each kind of S4a (config_id for the configuration): FAIL record-invalid for each kind',
          "for each kind, lint_chain (whose problems are record-invalid) reports the superseding record, the "
          "predecessor passing its own lint; and a terms run using such a rule file exits 20 with record-invalid on it",
          {'lint': out, 'run': run}, all(out.values()) and _invalid(run, 'syn/rules-pat-v2.json'))
    # LN2 (positive)
    o = _ln_pat_v2(r)
    check('LN2', '(positive) a record superseding a record of the same kind, schema and record_id that itself passes '
          'the lint: no record-invalid; the run uses the superseding record',
          "exit 0, no record-invalid, and the run's rule files include the superseding record", o,
          _clean(o, 'syn/rules-pat-v2.json'))
    # LN3
    res = {'record_id missing': _ln_pat_v2(r, record_id=None), 'record_id empty': _ln_pat_v2(r, record_id=''),
           'record_id not a string': _ln_pat_v2(r, record_id=7)}

    def no_id_predecessor(x):
        _variant_doc(x.files, PAT, 'syn/rules-pat-r1.json', record_id=None, author='writer-c')
        _chain(x.files, 'syn/rules-pat-r1.json', x.owner, x.time)
    res['predecessor without record_id'] = _ln_pat_v2(r, sup='syn/rules-pat-r1.json', setup=no_id_predecessor)
    check('LN3', 'a superseding record whose record_id is missing, empty or not a string; separately, a valid '
          'superseding record whose predecessor lacks a valid record_id: FAIL record-invalid in each case',
          "each run exits 20 with record-invalid on the superseding record, naming the lineage id", res,
          all(_invalid(o, 'syn/rules-pat-v2.json', 'lineage id') for o in res.values()))

    # LN4
    def predecessor(**kw):
        def setup(x):
            _variant_doc(x.files, PAT, 'syn/rules-pat-r1.json', author='writer-c')
            _chain(x.files, 'syn/rules-pat-r1.json', x.owner, x.time, **kw)
        return _ln_pat_v2(r, sup='syn/rules-pat-r1.json', setup=setup)
    res = {'no review record': predecessor(review=False), 'a verdict not accept': predecessor(verdict='reject'),
           'no authorization': predecessor(authorize=False)}
    check('LN4', 'a predecessor of the same lineage that fails the lint itself (no review record; separately, a verdict '
          'not accept; separately, no authorization): FAIL record-invalid for the superseding record in each case',
          "each run exits 20 with record-invalid on the superseding record, naming its predecessor", res,
          all(_invalid(o, 'syn/rules-pat-v2.json', 'predecessor') for o in res.values()))
    # LN5: a synthetic in-memory store that resolves each named {path, blob_sha256} without rehashing
    res = {}
    for case in ('two-record cycle', 'self-supersession'):
        fake = {'a': '1' * 64, 'b': '2' * 64, 's': '3' * 64}
        docs = {}
        if case == 'two-record cycle':
            docs[('r/a.json', fake['a'])] = {'schema': 'oi-scope/1', 'record_id': 'x', 'author': 'w',
                                             'supersedes': {'path': 'r/b.json', 'blob_sha256': fake['b']}}
            docs[('r/b.json', fake['b'])] = {'schema': 'oi-scope/1', 'record_id': 'x', 'author': 'w',
                                             'supersedes': {'path': 'r/a.json', 'blob_sha256': fake['a']}}
            top = {'schema': 'oi-scope/1', 'record_id': 'x', 'author': 'w',
                   'supersedes': {'path': 'r/a.json', 'blob_sha256': fake['a']}}
        else:
            top = {'schema': 'oi-scope/1', 'record_id': 'x', 'author': 'w',
                   'supersedes': {'path': 'r/t.json', 'blob_sha256': fake['s']}}
        tb = util.canonical(top)
        tref = {'path': 'r/t.json', 'blob_sha256': sha(tb)}
        if case == 'self-supersession':
            docs[('r/t.json', fake['s'])] = top
        entries = [('r/t.json', tb)]
        for (q, h) in list(docs) + [('r/t.json', sha(tb))]:
            rv = util.canonical({'schema': rec.review_schema, 'reviewer': 'rv', 'reviewed': {'path': q,
                                                                                            'blob_sha256': h},
                                 'method': 'read', 'verdicts': [{'item': 'x', 'verdict': 'accept'}]})
            au = util.canonical({'schema': rec.auth_schema, 'owner': 9001, 'time': 't0', 'comment_id': 'c-9',
                                 'authorizes': [{'record': {'path': q, 'blob_sha256': h},
                                                 'review': {'path': q + '.review', 'blob_sha256': sha(rv)}}]})
            entries += [(q + '.review', rv), (q + '.auth', au)]
        st = rec.Store(entries)
        st.resolver = lambda ref, docs=docs: docs.get((ref.get('path'), ref.get('blob_sha256')))
        probs = rec.lint_chain(tref, st, 9001, {sha(b) for _, b in entries})
        res[case] = probs[:2]
    check('LN5', 'a supersedes cycle of two records, and a self-supersession, in a synthetic in-memory store that '
          'resolves each named {path, blob_sha256} to the given record without rehashing: FAIL record-invalid in both; '
          'the chain walk terminates',
          "lint_chain returns, for both, a problem naming the loop", res,
          all(any('loops' in p for p in v) for v in res.values()))

    # LN6: a fork in the audit directory
    def fork(x):
        _variant_doc(x.files, PAT, 'syn/rules-pat-v2b.json', sup=PAT, author='writer-c')
        _chain(x.files, 'syn/rules-pat-v2b.json', x.owner, x.time)
    o = _ln_pat_v2(r, setup=fork)
    check('LN6', 'two records of one lineage superseding the same predecessor, both in the audit directory at F, only '
          'one referenced by the configuration: FAIL record-invalid (ambiguous ancestry)',
          "exit 20 with record-invalid on the referenced record, naming the ambiguous ancestry", o,
          _invalid(o, 'syn/rules-pat-v2.json', 'ambiguous ancestry'))
    # LN7: two heads
    res = {}
    x = LN(r)
    beta = [dict(rr, id='syn-beta-b') for rr in json.loads(x.files[PAT])['rules'] if rr['id'] == 'syn-beta']
    _variant_doc(x.files, PAT, 'syn/rules-pat-b.json', rules=beta, author='writer-c')
    x.add_rules('syn/rules-pat-b.json', _chain(x.files, 'syn/rules-pat-b.json', x.owner, x.time))
    res['two first records'] = x.run(hf.World('syn/PREREG.md'))
    x = LN(r)
    _variant_doc(x.files, PAT, 'syn/rules-pat-v2.json', sup=PAT)
    _variant_doc(x.files, PAT, 'syn/rules-pat-v2b.json', sup=PAT, author='writer-c')
    refs = _chain(x.files, 'syn/rules-pat-v2.json', x.owner, x.time) + \
        _chain(x.files, 'syn/rules-pat-v2b.json', x.owner, x.time)
    x.use_rules({PAT: 'syn/rules-pat-v2.json'}, refs)
    x.add_rules('syn/rules-pat-v2b.json', [])
    res['two diverging chains'] = x.run(hf.World('syn/PREREG.md'))
    check('LN7', 'two records with one record_id and kind, each with supersedes: null (separately, two chains from one '
          'first record that diverge), both read in one run: FAIL record-invalid (two heads)',
          "each run exits 20 with record-invalid on both records, naming two heads", res,
          _invalid(res['two first records'], PAT, 'two heads') and
          _invalid(res['two first records'], 'syn/rules-pat-b.json', 'two heads') and
          _invalid(res['two diverging chains'], 'syn/rules-pat-v2.json', 'two heads') and
          _invalid(res['two diverging chains'], 'syn/rules-pat-v2b.json', 'two heads'))

    # LN8: an unrelated chain
    def middle(**fields):
        def setup(x):
            _variant_doc(x.files, PAT, 'syn/rules-pat-m.json', sup=PAT, author='writer-c', **fields)
        return setup
    res = {'middle record with another record_id': _ln_pat_v2(r, sup='syn/rules-pat-m.json',
                                                              setup=middle(record_id='other')),
           'middle record with another schema': _ln_pat_v2(r, sup='syn/rules-pat-m.json',
                                                           setup=middle(schema='oi-term-rules/3'))}
    check('LN8', 'a three-record chain whose middle record has another record_id (separately, another schema of the '
          'same kind): FAIL record-invalid (unrelated chain)',
          "each run exits 20 with record-invalid on the head, naming another lineage or another kind, schema", res,
          _invalid(res['middle record with another record_id'], 'syn/rules-pat-v2.json', 'another lineage') and
          _invalid(res['middle record with another schema'], 'syn/rules-pat-v2.json', 'another kind'))


def ln9_ln12(r):
    # LN9: a predecessor authorized by a former owner
    res = {}
    for case in ('authorized by 4242 while owner', 'authorization time before 4242 was owner'):
        w = hf.World('syn/PREREG.md')
        t1 = w.tick() if case.startswith('authorized') else '2026-11-23T00:00:00Z'
        _owner_change(w, NEW_OWNER)
        t2 = w.tick()
        x = LN(r, owner=NEW_OWNER, time=t2)
        x.files[PAT_AUTH] = _auth_doc(hf.OWNER_ID, t1, PAT, x.files[PAT], PAT_REV, x.files[PAT_REV])
        _variant_doc(x.files, PAT, 'syn/rules-pat-v2.json', sup=PAT)
        x.use_rules({PAT: 'syn/rules-pat-v2.json'}, _chain(x.files, 'syn/rules-pat-v2.json', NEW_OWNER, t2))
        res[case] = x.run(w)
    check('LN9', 'a predecessor R1 authorized by 4242 while owner; 4242 -> 5555; R2 superseding R1, reviewed and '
          'authorized by 5555, used by the run. Separately, R1\'s authorization time before 4242 was owner: the first: '
          'no record-invalid, the run uses R2; the second: FAIL record-invalid',
          "first: exit 0, no record-invalid, R2 among the run's rule files; second: exit 20 with record-invalid on R2",
          res, _clean(res['authorized by 4242 while owner'], 'syn/rules-pat-v2.json') and
          _invalid(res['authorization time before 4242 was owner'], 'syn/rules-pat-v2.json', 'predecessor'))

    # LN11 and LN12: a widening predecessor
    ALLOW, V2, V3 = 'syn/rules-allow.json', 'syn/rules-allow-v2.json', 'syn/rules-allow-v3.json'
    WAUTH = 'syn/rules-allow-v2.widen.auth.json'

    def allow_case(mutate=None):
        w = hf.World('syn/PREREG.md')
        t1 = w.tick()
        old = LN(r, owner=hf.OWNER_ID, time=t1, variant={'allow_widened': True, 'widening_review': True})
        _owner_change(w, NEW_OWNER)
        t2 = w.tick()
        x = LN(r, owner=NEW_OWNER, time=t2)
        for q, b in old.files.items():
            if q.startswith('syn/rules-allow') and not q.startswith('syn/cfg/'):
                x.files[q] = b
        if mutate is not None:
            mutate(x.files, t1)
        _variant_doc(x.files, V2, V3, sup=V2)
        x.use_rules({ALLOW: V3}, _chain(x.files, V3, NEW_OWNER, t2))
        return x.run(w)

    def config_case():
        w = hf.World('syn/PREREG.md')
        t1 = w.tick()
        _owner_change(w, NEW_OWNER)
        t2 = w.tick()
        x = LN(r, owner=NEW_OWNER, time=t2)
        c0 = dict(x.cfg, retirement=dict(x.cfg['retirement'], owner=hf.OWNER_ID), supersedes=None, version=1)
        c0b = sf.jb(c0)
        c1 = dict(c0, corpus={'patterns': c0['corpus']['patterns'] + [r'^other/[^/]+\.md$']}, version=2,
                  supersedes={'path': 'syn/cfgold/c0.json', 'blob_sha256': sha(c0b)})
        c1b = sf.jb(c1)
        x.files['syn/cfgold/c0.json'], x.files['syn/cfgold/c1.json'] = c0b, c1b
        for q, b in (('syn/cfgold/c0.json', c0b), ('syn/cfgold/c1.json', c1b)):
            rv = sf.jb({'schema': 'oi-review-record/1', 'reviewer': sf.REVIEWER,
                        'reviewed': {'path': q, 'blob_sha256': sha(b)}, 'method': 'read',
                        'verdicts': [{'item': x.cfg['config_id'], 'verdict': 'accept'}]})
            x.files[q[:-5] + '.review.json'] = rv
            x.files[q[:-5] + '.auth.json'] = _auth_doc(hf.OWNER_ID, t1, q, b, q[:-5] + '.review.json', rv)
        wr = sf.jb({'schema': 'oi-review-record/1', 'kind': 'widening', 'reviewer': sf.WIDENER,
                    'reviewed': {'path': 'syn/cfgold/c1.json', 'blob_sha256': sha(c1b)},
                    'replaces': {'path': 'syn/cfgold/c0.json', 'blob_sha256': sha(c0b)}, 'method': 'read',
                    'verdicts': [{'item': '%s:changed corpus' % x.cfg['config_id'], 'verdict': 'accept'}]})
        x.files['syn/cfgold/c1.widen.json'] = wr
        x.files['syn/cfgold/c1.widen.auth.json'] = _auth_doc(hf.OWNER_ID, t1, 'syn/cfgold/c1.json', c1b,
                                                             'syn/cfgold/c1.widen.json', wr, cid='c-w')
        x.cfg.update(corpus=c1['corpus'], version=3, supersedes={'path': 'syn/cfgold/c1.json',
                                                                  'blob_sha256': sha(c1b)})

        def widen_review(cref):
            return sf.jb({'schema': 'oi-review-record/1', 'kind': 'widening', 'reviewer': sf.WIDENER,
                          'reviewed': cref, 'replaces': {'path': 'syn/cfgold/c1.json', 'blob_sha256': sha(c1b)},
                          'method': 'read', 'verdicts': [{'item': '%s:changed retirement' % x.cfg['config_id'],
                                                          'verdict': 'accept'}]})

        def widen_auth(cref):
            return _auth_doc(NEW_OWNER, t2, cref['path'], x.files[cref['path']], 'syn/cfg/widen.json',
                             widen_review(cref), cid='c-w2')
        return x.run(w, extra_cfg_files={'syn/cfg/widen.json': widen_review, 'syn/cfg/widen-auth.json': widen_auth})
    res = {'allow rule lineage': allow_case(), 'configuration lineage': config_case()}
    check('LN11', 'an allow rule R1 widening R0, R1\'s widening review authorized by 4242 while owner in an '
          'authorization record separate from R1\'s own; 4242 -> 5555; R2 superseding R1, reviewed and authorized by '
          '5555, used by the run; separately, the same for a configuration lineage: no record-invalid; the run uses '
          'R2, in both',
          "allow rule: exit 0, no record-invalid, R2 among the run's rule files; configuration: exit 0 (the run "
          "admits and uses the superseding configuration)", res,
          _clean(res['allow rule lineage'], V3) and res['configuration lineage']['exit'] == 0 and
          not res['configuration lineage']['record_invalid'])

    def future_owner(files, t1):
        d = json.loads(files[WAUTH])
        d.update(owner=NEW_OWNER, time=t1)
        files[WAUTH] = sf.jb(d)

    def no_authorization(files, t1):
        files.pop(WAUTH, None)
    res = {'widening review authorized only by 5555 while 4242 is the owner': allow_case(future_owner),
           'widening review listed by no authorization record': allow_case(no_authorization)}
    check('LN12', 'as LN11 for an allow rule, each case separately: R1\'s widening review listed only by an '
          'authorization record with owner 5555 whose time falls while 4242 is the owner; R1\'s widening review listed '
          'by no authorization record: FAIL record-invalid for the superseding record R2 in each case',
          "each run exits 20 with record-invalid on R2, naming its predecessor", res,
          all(_invalid(o, V3, 'predecessor') for o in res.values()))
    # LN10 (positive)
    x = LN(r)
    beta = [dict(rr, id='syn-beta-x') for rr in json.loads(x.files[PAT])['rules'] if rr['id'] == 'syn-beta']
    _variant_doc(x.files, PAT, 'syn/rules-extra.json', rules=beta, record_id=None, author='writer-c')
    x.add_rules('syn/rules-extra.json', _chain(x.files, 'syn/rules-extra.json', x.owner, x.time))
    o = x.run(hf.World('syn/PREREG.md'))
    check('LN10', '(positive) a record with supersedes: null and no record_id, named by no supersedes: no '
          'record-invalid', "exit 0, no record-invalid, the record among the run's rule files", o,
          _clean(o, 'syn/rules-extra.json'))


def ledger_event_verdicts(t):
    """Sec. 6.3: a review gives one verdict per item id of the reviewed record; the items of a freeze-ledger change's
    review are the events the change adds."""
    res = {}
    cases = {'one accept verdict per added event (positive)': lambda a, b: [(a, 'accept'), (b, 'accept')],
             'no verdict for one added event': lambda a, b: [(a, 'accept')],
             'two verdicts for one added event': lambda a, b: [(a, 'accept'), (b, 'accept'), (b, 'accept')],
             'a verdict not accept for one added event': lambda a, b: [(a, 'accept'), (b, 'reject')],
             'one verdict for the whole ledger change': lambda a, b: [('ledger', 'accept')]}
    for name, verdicts in cases.items():
        w = t.world()
        F = t.freeze(w)
        w.designate(F)
        old = w.ledger_bytes
        ev = [{'plan': hf.PLAN, 'round': 'r0', 'kind': 'withdraw', 'commit': 'ab' * 20, 'comment_id': cid,
               'author_id': hf.OWNER_ID, 'created_at': '2026-11-23T00:00:01Z', 'first_line': 'x'}
              for cid in (990001, 990002)]
        new = hf.jb({'schema': auth.ledger_schema, 'events': ev})
        rv = hf.jb({'schema': 'oi-review-record/1', 'reviewer': 'reviewer-b',
                    'reviewed': {'path': hf.LEDGER_PATH, 'blob_sha256': sha(new)}, 'previous': sha(old),
                    'method': 'read both ledger versions',
                    'verdicts': [{'item': i, 'verdict': v} for i, v in verdicts('990001', '990002')]})
        w.land_ledger(new, review=rv)
        res[name] = _show(*t.run(w, F))
    good = res['one accept verdict per added event (positive)']
    bad = [v for k, v in res.items() if '(positive)' not in k]
    check('R6-EV', 'one review verdict per added ledger event (sec. 6.3: one verdict per item id of the reviewed record; '
          'the ledger review\'s items are the events the change adds): a missing, duplicate or non-accept verdict for '
          'an added event, or one verdict for the whole change, refuses; one accept verdict per added event admits',
          "the positive case exits 0; every other case exits 65 CONFIG_UNREVIEWED naming the freeze-ledger change",
          res, good['exit'] == 0 and all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' and
                                         'freeze-ledger change' in o['message'] for o in bad))


# ---- the sixth independent review's findings: the engine's own snapshot (TR32-OWN) and the control gaps R6-G1 to R6-G9

PRE_A = '2026-11-23T00:00:00Z'  # before the first A of a fixture world merges (its first tick is the approval)


def _p5(t, w, F):
    """_point5, with an exception of the engine reported as the outcome (the control then fails, it does not abort)."""
    try:
        return _point5(t, w, F)
    except Exception as exc:
        return {'admitted': None, 'error': '%s: %s' % (type(exc).__name__, exc)}


def _fullx(t, w, F):
    """_full, with an exception of the engine reported as the outcome."""
    try:
        return _full(t, w, F)
    except Exception as exc:
        return {'exit': None, 'stop': None, 'message': '', 'record_invalid': [],
                'error': '%s: %s' % (type(exc).__name__, exc)}


def _refused5(o, point, word=None):
    return o.get('admitted') is False and o.get('point') == point and (word is None or word in o.get('message', ''))


def _unreviewed(o, *words):
    return o.get('exit') == 65 and o.get('stop') == 'CONFIG_UNREVIEWED' and all(x in o.get('message', '')
                                                                                 for x in words)


def _next(w):
    return 'c%d' % (len(w.h.repos[hf.REPO_ID]['commits']) + 1)


def tr32_own(t):
    """TR32 with the admission snapshot exactly as the engine builds it (`auth.admit`), committed as an acceptance
    landing commits it, at `<ledger directory>/landings/<round>/snapshot.json`. That snapshot records `plan` and
    `round` once, at its top level, not in each event."""
    snap_path = hf.LEDGER_PATH.rsplit('/', 1)[0] + '/landings/round-1/snapshot.json'

    def own_snapshot(w, F):
        try:
            return auth.admit(w.h, t.repo, w.run_id, hf.PLAN, hf.ROUND, F, t.p)[1], None
        except Exception as exc:
            return None, '%s: %s' % (type(exc).__name__, exc)
    out = {}
    # the sequence: 4242 designates F, supersedes F by F2; F2 admitted; its snapshot committed; the supersession deleted
    w = t.world()
    F = t.freeze(w)
    F2 = t.freeze(w, extra={'syn/other.txt': b'2\n'})
    w.designate(F)
    sp = w.comment(hf.PLAN_ISSUE, 'oi-freeze/1 supersede plan=%s round=%s commit=%s by=%s'
                   % (hf.PLAN, hf.ROUND, F, F2))
    snap, err = own_snapshot(w, F2)
    seq = {'F2 admitted, its snapshot built': snap is not None, 'error': err}
    if snap is not None:
        seq['events carrying plan or round'] = sum(1 for e in snap['events'] if 'plan' in e or 'round' in e)
        seq['snapshot plan, round'] = [snap.get('plan'), snap.get('round')]
        w.add_main(_next(w), {snap_path: hf.jb(snap)})
        seq['F, supersession comment present: point 5'] = _p5(t, w, F)
        w.comments[(hf.REPO_ID, hf.PLAN_ISSUE)].remove(sp)
        seq['F, supersession comment deleted: point 5'] = _p5(t, w, F)
        seq['F, supersession comment deleted: full chain'] = _fullx(t, w, F)
    out['sequence'] = seq

    # the engine's snapshot of F's own admission, committed as built and with one change each
    def committed(edit):
        w = t.world()
        F = t.freeze(w)
        w.designate(F)
        snap, err = own_snapshot(w, F)
        if snap is None:
            return {'admitted': None, 'error': err}
        s = copy.deepcopy(snap)
        edit(s)
        w.add_main(_next(w), {snap_path: hf.jb(s)})
        return _p5(t, w, F)

    def no_plan_round(s):
        s.pop('plan')
        s.pop('round')

    def event_field(key, value):
        return lambda s: s['events'][0].update({key: value})
    out['(positive) F\'s own snapshot committed as built; F admitted again'] = committed(lambda s: None)
    out['no plan and round, in the events or at the top level'] = committed(no_plan_round)
    out['an event naming another plan than the snapshot'] = committed(event_field('plan', 'other-plan'))
    out['an event naming another round than the snapshot'] = committed(event_field('round', 'r9'))
    out['(positive) an event repeating the snapshot\'s plan and round'] = committed(
        lambda s: s['events'][0].update({'plan': s['plan'], 'round': s['round']}))
    positives = [v for k, v in out.items() if k.startswith('(positive)')]
    malformed = [v for k, v in out.items() if k != 'sequence' and not k.startswith('(positive)')]
    check('TR32-OWN', 'TR32 with the engine\'s own admission snapshot (sec. 6.3, reconciliation: "a withdrawal or '
          'supersession in the ledger or in a committed snapshot binds, even if its comment is now deleted"): 4242 '
          'designates F and supersedes it by F2; F2 is admitted; the snapshot auth.admit returns for F2 is committed '
          'as snapshot.json; the supersession comment is deleted: F stays superseded, its admission refuses. An event '
          'of a committed snapshot takes the snapshot\'s plan and round; one with neither, or one contradicting the '
          'snapshot\'s, refuses. F\'s own snapshot, committed, does not stop F\'s admission',
          "sequence: F2 admitted with no event carrying plan or round; F refused at point 5 ('state') before and after "
          "the deletion; after it the full chain exits 65 CONFIG_UNREVIEWED; the three malformed snapshots refuse at "
          "point 'ledger' naming the committed snapshot; both positives admit F", out,
          seq.get('F2 admitted, its snapshot built') is True and seq.get('events carrying plan or round') == 0 and
          _refused5(seq.get('F, supersession comment present: point 5', {}), 'state') and
          _refused5(seq.get('F, supersession comment deleted: point 5', {}), 'state') and
          _unreviewed(seq.get('F, supersession comment deleted: full chain', {})) and
          all(_refused5(o, 'ledger', 'committed snapshot') for o in malformed) and
          all(o.get('admitted') is True for o in positives))


def r6_g1(t):
    """G-1: a designation created when no version of A was in force is not an owner comment."""
    out = {}
    for name in ('created before the first A merged', 'created in the second the first A merged'):
        w = t.world()
        F = t.freeze(w)
        at = PRE_A if name.startswith('created before') else w.h.merges[(hf.REPO_ID, 'c1')]['merged_at']
        w.designate(F, at=at)
        out[name] = {'at': at, 'point5': _p5(t, w, F), 'full': _fullx(t, w, F)}
    check('R6-G1', 'the owner\'s designation of F created before the first A merged; separately, created in the second '
          'the first A merged (sec. 6.3, "Owner at creation": the version in force at t is the latest merged strictly '
          'before t, and a comment created when no version was in force is not an owner comment): ERROR (missing '
          'designation) in both',
          "both: point 5 refuses (point 'state', F not the one designated commit); the full chain exits 65 "
          "CONFIG_UNREVIEWED", out,
          all(_refused5(o['point5'], 'state', 'not the one designated') and _unreviewed(o['full'])
              for o in out.values()))


def r6_g2(t):
    """G-2: the snapshot records, for every owner comment, the blob of the version of A in force at its creation."""
    w = t.world()
    a1 = w.a_bytes
    pre = w.comment(hf.PLAN_ISSUE, 'a note', at=PRE_A)
    under1 = w.comment(hf.PLAN_ISSUE, 'a note under the first version')
    change_authority(w, hf.authority('syn/PREREG.md', supersedes={'path': auth.authority_path, 'blob_sha256': sha(a1)},
                                     extra={'status': 'second version'}))
    a2 = w.a_bytes
    F = t.freeze(w, a_bytes=a1)
    d = w.designate(F)
    code, res = t.run(w, F)
    snap = (((res or {}).get('config') or {}).get('admission') or {}).get('simulated_chain', {}).get('snapshot', {})
    got = {c.get('id'): c.get('authority_in_force_sha256', 'absent') for c in snap.get('owner_comments', [])}
    want = {pre['id']: None, under1['id']: sha(a1), d['id']: sha(a2)}
    o = {'exit': code, 'recorded': {str(k): got.get(k, 'absent') for k in want},
         'want': {str(k): v for k, v in want.items()},
         'every owner comment carries the field': all(v != 'absent' for v in got.values())}
    check('R6-G2', 'the admission snapshot records, for every owner comment of point 3, the blob sha256 of the version '
          'of A in force at its creation (sec. 6.3, "The admission snapshot"): a comment by 4242 created before the '
          'first A merged (none in force), one under the first version, and the designation under the second version '
          '(an A change keeping the owner)',
          "the full chain exits 0; authority_in_force_sha256 is null, sha256(A1) and sha256(A2) for the three comments; "
          "every owner comment record carries the field", o,
          code == 0 and all(got.get(k, 'absent') == v for k, v in want.items()) and
          o['every owner comment carries the field'])


def r6_g3(t):
    """G-3: each approval of a freeze-ledger change is an owner comment at its creation, each checked on its own."""
    out = {}
    # the approvals created before the first A merged: both, then each alone (main route)
    for i, case in enumerate(('both approvals', 'the append comment only', 'the oi-authority/1 approval only')):
        w = t.world()
        new = _ledger_with(w, 880101 + i)
        old = w.ledger_bytes
        pre_auth = case in ('both approvals', 'the oi-authority/1 approval only')
        pre_app = case in ('both approvals', 'the append comment only')
        w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (sha(old), sha(new)),
                  at=PRE_A if pre_auth else None)
        w.comment(hf.PLAN_ISSUE, 'oi-freeze-ledger/1 append plan=%s round=%s from=%s to=%s'
                  % (hf.PLAN, hf.ROUND, sha(old), sha(new)), at=PRE_A if pre_app else None)
        _ledger_merge(w, new, hf.OWNER_ID)
        F = t.freeze(w)
        w.designate(F)
        out['created before the first A merged: %s' % case] = _fullx(t, w, F)
    # TR58-style: one approval by 5555 created while 4242 is the owner, the other by 5555 after 4242 -> 5555; each
    # ledger route; and the positive, both created after the change
    for i, defective in enumerate(('append', 'authority', None)):
        for route in ('landing', 'main'):
            w = t.world()
            a1 = w.a_bytes
            new = _ledger_with(w, 880111 + 2 * i + (route == 'main'))
            old = w.ledger_bytes
            forms = {'authority': (hf.AUTH_ISSUE, 'oi-authority/1 approve from=%s to=%s' % (sha(old), sha(new))),
                     'append': (hf.PLAN_ISSUE, 'oi-freeze-ledger/1 append plan=%s round=%s from=%s to=%s'
                                % (hf.PLAN, hf.ROUND, sha(old), sha(new)))}
            if defective is not None:
                w.comment(forms[defective][0], forms[defective][1], author_id=NEW_OWNER)
            _owner_change(w, NEW_OWNER)
            for k, (issue, line) in sorted(forms.items()):
                if k != defective:
                    w.comment(issue, line, author_id=NEW_OWNER)
            if route == 'landing':
                o = _landing(w, new)
            else:
                _ledger_merge(w, new, NEW_OWNER)
                F = t.refreeze(w, a_bytes=a1)
                _designate(w, F, NEW_OWNER)
                o = _fullx(t, w, F)
            key = ('(positive) both by 5555 after 4242 -> 5555' if defective is None else
                   '%s comment by 5555 while 4242 is the owner' % defective)
            out['%s: %s route' % (key, route)] = o
    names = {'append': 'oi-freeze-ledger/1 append', 'authority': 'oi-authority/1 approve'}

    def refused(o, which):
        if 'merges' in o:
            return o['merges'] is False and _owner_at_creation_refusal(o) and names[which] in o.get('message', '')
        return _unreviewed(o, 'freeze-ledger change', 'Owner at creation', names[which])
    pre = [(k, v) for k, v in out.items() if k.startswith('created before')]
    check('R6-G3', 'the approvals of a freeze-ledger change count only as owner comments at their creation (sec. 6.3, '
          '"Owner at creation", approvals): approvals created before the first A merged (both; separately only the '
          'append comment; only the oi-authority/1 approval): ERROR. TR57/TR58-style, one defective approval at a time '
          'on each ledger route: 5555 creates the append comment (separately the oi-authority/1 approval) while 4242 is '
          'the owner and the other after 4242 -> 5555: refused. Both created by 5555 after the change: verified',
          "pre-A: each exits 65 CONFIG_UNREVIEWED naming the freeze-ledger change, Owner at creation and the "
          "defective form (the oi-authority/1 approval when both are); TR58-style: landing route refuses and main "
          "route exits 65, naming Owner at creation and the defective form; positive: the landing merges and the main "
          "route exits 0", out,
          refused(out['created before the first A merged: both approvals'], 'authority') and
          refused(out['created before the first A merged: the append comment only'], 'append') and
          refused(out['created before the first A merged: the oi-authority/1 approval only'], 'authority') and
          all(refused(out['%s comment by 5555 while 4242 is the owner: %s route' % (d, r)], d)
              for d in ('append', 'authority') for r in ('landing', 'main')) and
          out['(positive) both by 5555 after 4242 -> 5555: landing route'].get('merges') is True and
          out['(positive) both by 5555 after 4242 -> 5555: main route'].get('exit') == 0 and len(pre) == 3)


def r6_g4(t):
    """G-4: "in force" at t is merged strictly before t: a comment in the second of an owner change's merge."""
    out = {}
    for same in (True, False):
        w = t.world()
        F = t.freeze(w)
        _owner_change(w, NEW_OWNER)
        m = w.h.merges[(hf.REPO_ID, w.main)]['merged_at']
        d = w.designate(F, author_id=NEW_OWNER, login='login-%d' % NEW_OWNER, at=m if same else None)
        out['5555 designates F in the second the owner change merged' if same else
            '(positive) 5555 designates F one second later'] = {'merge': m, 'created': d['created_at'],
                                                                'point5': _p5(t, w, F)}
    a = out['5555 designates F in the second the owner change merged']
    b = out['(positive) 5555 designates F one second later']
    check('R6-G4', 'an owner change 4242 -> 5555 merged at m; 5555 designates F created at m: not an owner comment (the '
          'version in force at m is the one merged strictly before m, owner 4242): ERROR (missing designation). '
          'Separately, the designation created at m + 1 s: F is the one designated commit at point 5',
          "same second: point 5 refuses (point 'state', F not the one designated commit); one second later: point 5 "
          "admits F", out,
          a['created'] == a['merge'] and _refused5(a['point5'], 'state', 'not the one designated') and
          b['created'] > b['merge'] and b['point5'].get('admitted') is True)


def r6_g5(t):
    """G-5: an owner authorization's time must be a host timestamp (a non-timestamp has no version in force)."""
    out = {}
    for tm in ('t0', '2026-11-24T00:00:00'):
        w = t.world()
        F = t.refreeze(w, variant={'cfg_auth_time': tm})
        w.designate(F)
        out['configuration authorization time %r' % tm] = _fullx(t, w, F)
    check('R6-G5', 'the configuration\'s owner authorization with time "t0"; separately "2026-11-24T00:00:00" (no '
          'zone): not a host timestamp, so no version of A is in force at it and it does not count under "Owner at '
          'creation" (sec. 6.3; point 7): ERROR CONFIG_UNREVIEWED for the configuration\'s own',
          "both exit 65 CONFIG_UNREVIEWED naming the configuration review chain and a time that is not a host "
          "timestamp", out,
          all(_unreviewed(o, 'configuration review chain', 'not a host timestamp') for o in out.values()))


def r6_g6(r):
    """G-6: a record_id carried by a record off the referenced record's supersedes chain is a reused id."""
    x = LN(r)
    _variant_doc(x.files, PAT, 'syn/rules-pat-dup.json', author='writer-c')
    reused = x.run(hf.World('syn/PREREG.md'))
    clean = LN(r).run(hf.World('syn/PREREG.md'))
    out = {'a second record with the rule file\'s record_id, off its chain': reused, '(positive) no such record': clean}
    check('R6-G6', 'a record in the audit directory at F carrying the record_id, kind and schema of a rule file the '
          'configuration references, with supersedes null (not on that file\'s supersedes chain) (sec. 6.3, DI-2: '
          '"a record_id carried by two records that do not lie on one supersedes chain is" a reused id): FAIL '
          'record-invalid on the referenced rule file; without that record the run is clean',
          "the first exits 20 with record-invalid on syn/rules-pat.json naming the reuse; the second exits 0 with no "
          "record-invalid", out,
          _invalid(reused, PAT, 'reused') and clean['exit'] == 0 and not clean['record_invalid'])


def r6_g7(t):
    """G-7: a freeze-ledger change is governed by the version of A merged strictly before it."""
    out = {}
    for same in (True, False):
        w = t.world()
        a1 = w.a_bytes
        new = _ledger_with(w, 880121 + same)
        old = w.ledger_bytes
        _ledger_comments(w, new, hf.OWNER_ID)
        _owner_change(w, NEW_OWNER)
        m = w.h.merges[(hf.REPO_ID, w.main)]['merged_at']
        w.add_main(_next(w), dict(hf.ledger_review_file(w.a, new, sha(old)), **{hf.LEDGER_PATH: new}),
                   merged_by=hf.OWNER_ID, merged_at=m if same else None)
        lm = w.h.merges[(hf.REPO_ID, w.main)]['merged_at']
        w.ledger_bytes = new
        F = t.refreeze(w, a_bytes=a1)
        _designate(w, F, NEW_OWNER)
        out['(positive) ledger merged in the second of the owner change' if same else
            'ledger merged one second later'] = dict(_fullx(t, w, F), owner_change_merged=m, ledger_merged=lm)
    a = out['(positive) ledger merged in the second of the owner change']
    b = out['ledger merged one second later']
    check('R6-G7', '4242 creates both approvals of a freeze-ledger change; an owner change 4242 -> 5555 merges at m; the '
          'ledger change is merged by 4242 at m; 5555 designates an F whose configuration 5555 authorized: the ledger '
          'change is governed by the version of A in force at its merge, the one merged strictly before m (owner '
          '4242), so it verifies and F is admitted. Separately, the ledger change merged by 4242 at m + 1 s is governed '
          'by 5555\'s version: ERROR',
          "same second: the full chain exits 0; one second later: exits 65 CONFIG_UNREVIEWED naming the freeze-ledger "
          "change", out,
          a['owner_change_merged'] == a['ledger_merged'] and a.get('exit') == 0 and
          b['ledger_merged'] > b['owner_change_merged'] and _unreviewed(b, 'freeze-ledger change'))


def r6_g8(t):
    """G-8: an A change needs its independent review record, its approval alone does not suffice."""
    out = {}
    for review in (False, True):
        w = t.world()
        old = w.a_bytes
        change_authority(w, hf.authority('syn/PREREG.md', supersedes={'path': auth.authority_path,
                                                                      'blob_sha256': sha(old)},
                                         extra={'status': 'second version'}), approve=True, review=review)
        F = t.freeze(w, a_bytes=old)
        w.designate(F)
        out['(positive) approval and review record' if review else 'approval, no review record'] = _fullx(t, w, F)
    a, b = out['approval, no review record'], out['(positive) approval and review record']
    check('R6-G8', 'a change to A after F\'s base with the owner\'s approval and pull-request merge but no independent '
          'review record (sec. 6.3, "Authority changes": "An independent review record names both blobs"): ERROR; '
          'with the review record as well: admitted',
          "the first exits 65 CONFIG_UNREVIEWED naming the authority change's independent review record; the second "
          "exits 0", out, _unreviewed(a, 'authority change', 'independent review record') and b.get('exit') == 0)


def r6_g9(t):
    """G-9: point 3 refuses when an owner comment's edit status cannot be read."""
    out = {}
    for name, key, form in (('the designation without edits', 'edits', True),
                            ('the designation without its hidden state', 'hidden', True),
                            ('an owner comment without a form, without edits', 'edits', False)):
        w = t.world()
        F = t.freeze(w)
        d = w.designate(F)
        c = d if form else w.comment(hf.PLAN_ISSUE, 'a note')
        del c[key]
        out[name] = {'point5': _p5(t, w, F), 'full': _fullx(t, w, F)}
    check('R6-G9', 'an owner comment whose edit status cannot be read (sec. 6.3, admission point 3: "an owner comment\'s '
          'edit status cannot be read", relevant or not): the designation with no edit record; separately with no '
          'hidden state; separately an owner comment without a form with no edit record: ERROR in each',
          "each: point 5 refuses at point 'edits' naming an edit status that cannot be read; the full chain exits 65 "
          "CONFIG_UNREVIEWED", out,
          all(_refused5(o['point5'], 'edits', 'cannot be read') and _unreviewed(o['full']) for o in out.values()))


# ---- the seventh independent review's findings: a snapshot event conflicting with the thread (R7-B2) and one
# observed event recorded more than once (R7-N5)

def r7_b2(t):
    """B-2: the engine's own admission snapshot, committed with the designation event's first line, and separately its
    author, differing from the thread's comment (sec. 6.3, reconciliation: "a ledger or snapshot event that conflicts
    with the thread refuses")."""
    snap_path = hf.LEDGER_PATH.rsplit('/', 1)[0] + '/landings/round-1/snapshot.json'
    out = {}
    for name in ('(positive) committed as built', 'first line differs', 'author differs'):
        w = t.world()
        F = t.freeze(w)
        d = w.designate(F)
        try:
            snap = auth.admit(w.h, t.repo, w.run_id, hf.PLAN, hf.ROUND, F, t.p)[1]
        except Exception as exc:
            out[name] = {'error': '%s: %s' % (type(exc).__name__, exc)}
            continue
        s = copy.deepcopy(snap)
        evs = [e for e in s['events'] if e['comment_id'] == d['id']]
        if name == 'first line differs':
            evs[0]['first_line'] = 'oi-freeze/1 designate plan=%s round=%s commit=%s' % (hf.PLAN, hf.ROUND, 'ef' * 20)
        elif name == 'author differs':
            evs[0]['author_id'] = 31337
        w.add_main(_next(w), {snap_path: hf.jb(s)})
        out[name] = {'designation events in the snapshot': len(evs), 'point5': _p5(t, w, F), 'full': _fullx(t, w, F)}
    pos = out.get('(positive) committed as built', {})
    neg = [v for k, v in out.items() if not k.startswith('(positive)')]
    check('R7-B2', 'the engine\'s own admission snapshot of F committed on main with the designation event\'s first '
          'line, and separately its author numeric id, differing from the thread\'s comment (sec. 6.3, '
          'reconciliation: "a ledger or snapshot event that conflicts with the thread refuses"): ERROR in each; the '
          'snapshot committed as built does not stop F\'s admission',
          "each conflicting case: point 5 refuses at point 'ledger' naming the conflict with the thread; the full "
          "chain exits 65 CONFIG_UNREVIEWED naming it; the positive admits F and its full chain exits 0", out,
          pos.get('point5', {}).get('admitted') is True and pos.get('full', {}).get('exit') == 0 and len(neg) == 2 and
          all(o.get('designation events in the snapshot') == 1 and
              _refused5(o.get('point5', {}), 'ledger', 'conflicts with the thread') and
              _unreviewed(o.get('full', {}), 'conflicts with the thread') for o in neg))


def _r7_wd_line(F, rnd=None):
    return 'oi-freeze/1 withdraw plan=%s round=%s commit=%s' % (hf.PLAN, rnd or hf.ROUND, F)


def _r7_guarded(fn):
    try:
        return fn()
    except Exception as exc:
        return {'error': '%s: %s' % (type(exc).__name__, exc)}


R7_SNAP = hf.LEDGER_PATH.rsplit('/', 1)[0] + '/landings/round-1/snapshot.json'


def _r7_landed(t, where='ledger+snapshot', edit=None, extra_ledger=()):
    """F designated, W (an owner comment) withdraws F, F2 designated; F2 admitted, and its own admission snapshot
    landed as an acceptance landing lands it: the snapshot committed and W appended to the freeze ledger (`where`:
    'ledger+snapshot'; separately 'two snapshots'; separately 'same snapshot twice in its list'). `edit(lev, s, sev,
    F2)` may change the ledger's record of W (`lev`), the snapshot (`s`) or the snapshot's record of W (`sev`);
    `extra_ledger` are ledger records placed before W's."""
    w = t.world()
    F = t.freeze(w)
    F2 = t.freeze(w, extra={'syn/other.txt': b'2\n'})
    w.designate(F)
    W = w.comment(hf.PLAN_ISSUE, _r7_wd_line(F))
    d2 = w.designate(F2)
    snap = auth.admit(w.h, t.repo, w.run_id, hf.PLAN, hf.ROUND, F2, t.p)[1]
    wev = [e for e in snap['events'] if e['comment_id'] == W['id']][0]
    lev = {k: wev[k] for k in ('kind', 'commit', 'by', 'comment_id', 'created_at', 'author_id', 'first_line')}
    lev.update(plan=hf.PLAN, round=hf.ROUND)
    s = copy.deepcopy(snap)
    if edit is not None:
        edit(lev, s, [e for e in s['events'] if e['comment_id'] == W['id']][0], F2)
    if 'ledger' in where:
        w.land_ledger(hf.jb({'schema': auth.ledger_schema,
                             'events': [x(W, F, F2) if callable(x) else x for x in extra_ledger] + [lev]}))
    if where == 'same snapshot twice in its list':
        s['events'].append(copy.deepcopy(wev))
    if 'snapshot' in where:
        w.add_main(_next(w), {R7_SNAP: hf.jb(s)})
    if where == 'two snapshots':
        w.add_main(_next(w), {R7_SNAP.replace('round-1', 'round-1b'): hf.jb(s)})
    return w, F, F2, W, d2


def _r7_deleted(t, w, F, F2, W, both=True):
    w.comments[(hf.REPO_ID, hf.PLAN_ISSUE)].remove(W)
    o = {'W deleted: F2': _p5(t, w, F2), 'W deleted: F2 full chain': _fullx(t, w, F2)}
    if both:
        o['W deleted: F'] = _p5(t, w, F)
    return o


def _r7_admits(o):
    return o.get('W deleted: F2', {}).get('admitted') is True and \
        o.get('W deleted: F2 full chain', {}).get('exit') == 0 and _refused5(o.get('W deleted: F', {}), 'state')


def r7_n5(t):
    """N-5: an acceptance landing commits its admission snapshot and appends the events it observed to the freeze
    ledger (sec. 5, "Durable evidence"; sec. 6.3, "The freeze ledger"), so one observed comment is recorded more than
    once. Each comment is one event (sec. 6.3, point 5), processed once."""
    seq = {}
    for where in ('ledger+snapshot', 'two snapshots', 'same snapshot twice in its list'):
        def one(where=where):
            w, F, F2, W, _ = _r7_landed(t, where)
            o = {'W present: F2': _p5(t, w, F2)}
            o.update(_r7_deleted(t, w, F, F2, W))
            return o
        seq[where] = _r7_guarded(one)
    check('R7-N5', 'one observed event recorded more than once (sec. 6.3, "The freeze ledger": each event is a '
          'designation, withdrawal or supersession with its comment id; sec. 5, "Durable evidence": a landing commits '
          'its snapshot and appends the events it observed; point 5: "a withdrawal of F makes it withdrawn"): F '
          'designated, W withdraws F, F2 designated; F2 admitted and landed, W recorded in the ledger and the snapshot '
          '(separately in two snapshots; separately twice in one snapshot); W\'s comment deleted: F2, legitimately '
          'designated, is admitted again and F stays withdrawn',
          "each placement: F2 admitted with W present and with W deleted, its full chain exits 0; F refused at point "
          "'state'", seq,
          len(seq) == 3 and all(o.get('W present: F2', {}).get('admitted') is True and _r7_admits(o)
                                for o in seq.values()))


def r7_n5_conflict(t):
    """Two records of one comment that differ are a conflict and refuse; they are never merged."""
    def later(ts):
        return (datetime.datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ') + datetime.timedelta(seconds=1)).strftime(
            '%Y-%m-%dT%H:%M:%SZ')

    def field(key, value):
        def edit(lev, s, sev, F2):
            lev[key] = value(lev, F2) if callable(value) else value
        return edit

    def body(lev, s, sev, F2):
        lev['body_sha256'] = '0' * 64
        sev['body_sha256'] = '1' * 64
    out = {}
    for name, edit in (('first line', field('first_line', lambda lev, F2: _r7_wd_line(F2))),
                       ('author numeric id', field('author_id', 31337)),
                       ('kind', field('kind', 'supersede')),
                       ('creation time', field('created_at', lambda lev, F2: later(lev['created_at']))),
                       ('commit', field('commit', lambda lev, F2: F2)),
                       ('body sha256', body)):
        def one(edit=edit, name=name):
            w, F, F2, W, _ = _r7_landed(t, 'ledger+snapshot', edit)
            o = {}
            if name == 'creation time':
                o['W present: F2'] = _p5(t, w, F2)
            o.update(_r7_deleted(t, w, F, F2, W, both=False))
            return o
        out['the ledger and snapshot records of W differ in its %s' % name] = _r7_guarded(one)
    check('R7-N5-CONFLICT', 'two records of one comment (the same comment id) in the freeze ledger and a committed '
          'snapshot that differ in first line, author numeric id, kind, creation time, commit or body sha256 are a '
          'conflict and refuse (sec. 6.3, reconciliation; point 5, "any other conflict"); they are not merged',
          "each field, W deleted (and, for the creation time, W present): point 5 refuses at point 'ledger' naming two "
          "records of one comment that differ; the full chain exits 65 CONFIG_UNREVIEWED", out,
          len(out) == 6 and
          all('W deleted: F2' in o and all(_refused5(o[k], 'ledger', 'differ') for k in ('W deleted: F2',
                                                                                         'W present: F2') if k in o)
              and _unreviewed(o.get('W deleted: F2 full chain', {}), 'differ') for o in out.values()) and
          'W present: F2' in out['the ledger and snapshot records of W differ in its creation time'])


def r7_n5_forged(t):
    """A forged record that shares a comment id with a genuine one is caught, not hidden by processing each comment
    once."""
    out = {}

    def forged_present(replace):
        """A forged snapshot record under the comment id of F2's present designation, withdrawing F2; beside the
        genuine record of that designation, or in its place."""
        def edit(lev, s, sev, F2):
            d = [e for e in s['events'] if e['kind'] == 'designate' and e['commit'] == F2][0]
            if replace:
                s['events'].remove(d)
            s['events'].append({'kind': 'withdraw', 'commit': F2, 'by': None, 'comment_id': d['comment_id'],
                                'created_at': d['created_at'], 'author_id': d['author_id'],
                                'first_line': _r7_wd_line(F2)})
        return edit
    for name, replace in (('beside the genuine record', False), ('in place of the genuine record', True)):
        def one(replace=replace):
            w, F, F2, W, _ = _r7_landed(t, 'ledger+snapshot', forged_present(replace))
            return {'designation present: F2': _p5(t, w, F2), 'designation present: F2 full chain': _fullx(t, w, F2)}
        out['a forged withdrawal of F2 under the id of F2\'s present designation, %s' % name] = _r7_guarded(one)

    # W deleted: a forged snapshot record under W's comment id that withdraws F2 (consistent with itself)
    def forged_deleted(lev, s, sev, F2):
        sev.update(commit=F2, first_line=_r7_wd_line(F2))

    def two():
        w, F, F2, W, _ = _r7_landed(t, 'ledger+snapshot', forged_deleted)
        return _r7_deleted(t, w, F, F2, W, both=False)
    out['W deleted; a forged snapshot record under W\'s id withdrawing F2, the ledger\'s withdrawing F'] = \
        _r7_guarded(two)
    a, b, c = (out[k] for k in out)
    check('R7-N5-FORGED', 'a forged snapshot record sharing a comment id with a genuine one: under the id of F2\'s '
          'present designation, a withdrawal of F2, beside the genuine record (separately, in its place); separately, '
          'with W deleted, under W\'s id a withdrawal of F2 while the ledger records W withdrawing F. Each is caught '
          '(sec. 6.3, reconciliation: an event that conflicts with the thread refuses; two records of one comment '
          'that differ refuse)',
          "beside: refused at point 'ledger' naming two records of one comment that differ; in place: refused at point "
          "'ledger' naming the conflict with the thread; W deleted: refused at point 'ledger' naming two records that "
          "differ; each full chain exits 65 CONFIG_UNREVIEWED", out,
          _refused5(a.get('designation present: F2', {}), 'ledger', 'differ') and
          _unreviewed(a.get('designation present: F2 full chain', {}), 'differ') and
          _refused5(b.get('designation present: F2', {}), 'ledger', 'conflicts with the thread') and
          _unreviewed(b.get('designation present: F2 full chain', {}), 'conflicts with the thread') and
          _refused5(c.get('W deleted: F2', {}), 'ledger', 'differ') and
          _unreviewed(c.get('W deleted: F2 full chain', {}), 'differ'))


def r7_n5_supersede(t):
    """A supersession recorded more than once still only revokes, once, and never designates (sec. 6.3, K1)."""
    def one():
        w = t.world()
        F = t.freeze(w)
        F2 = t.freeze(w, extra={'syn/other.txt': b'2\n'})
        w.designate(F)
        sp = w.comment(hf.PLAN_ISSUE, 'oi-freeze/1 supersede plan=%s round=%s commit=%s by=%s'
                       % (hf.PLAN, hf.ROUND, F, F2))
        snap = auth.admit(w.h, t.repo, w.run_id, hf.PLAN, hf.ROUND, F2, t.p)[1]
        sev = [e for e in snap['events'] if e['comment_id'] == sp['id']][0]
        lev = {k: sev[k] for k in ('kind', 'commit', 'by', 'comment_id', 'created_at', 'author_id', 'first_line')}
        lev.update(plan=hf.PLAN, round=hf.ROUND)
        w.land_ledger(hf.jb({'schema': auth.ledger_schema, 'events': [lev]}))
        w.add_main(_next(w), {R7_SNAP: hf.jb(snap)})
        w.add_main(_next(w), {R7_SNAP.replace('round-1', 'round-1b'): hf.jb(snap)})
        o = {'S present: F2': _p5(t, w, F2), 'S present: F': _p5(t, w, F)}
        w.comments[(hf.REPO_ID, hf.PLAN_ISSUE)].remove(sp)
        o['S deleted: F'] = _p5(t, w, F)
        o['S deleted: F2'] = _p5(t, w, F2)
        o['S deleted: F2 full chain'] = _fullx(t, w, F2)
        F3 = t.freeze(w, extra={'syn/other.txt': b'3\n'})
        w.designate(F3)
        o['S deleted, F3 designated: F3'] = _p5(t, w, F3)
        return o
    o = _r7_guarded(one)
    check('R7-N5-SUPERSEDE', 'a supersession S of F by F2, recorded in the freeze ledger and in two committed '
          'snapshots, its comment then deleted: it only revokes and never designates (sec. 6.3, "a supersession '
          'recorded in the freeze ledger or in a committed snapshot only revokes"); processed once, it lets a later '
          'designation of F3 stand',
          "S present: F2 admitted, F refused at 'state'; S deleted: F and F2 refused at 'state' (F2 is not "
          "designated), F2's full chain exits 65 CONFIG_UNREVIEWED; F3 designated afterwards is admitted", o,
          o.get('S present: F2', {}).get('admitted') is True and _refused5(o.get('S present: F', {}), 'state') and
          _refused5(o.get('S deleted: F', {}), 'state') and _refused5(o.get('S deleted: F2', {}), 'state') and
          _unreviewed(o.get('S deleted: F2 full chain', {})) and
          o.get('S deleted, F3 designated: F3', {}).get('admitted') is True)


def r7_n5_round(t):
    """Records of one comment id under another plan or round are not merged with this round's."""
    out = {}
    for where in ('snapshot', 'ledger+snapshot'):
        for name, key, value in (('round', 'round', 'r0'), ('plan', 'plan', 'other-plan')):
            def one(where=where, key=key, value=value):
                w, F, F2, W, _ = _r7_landed(t, where)
                ev = {'kind': 'withdraw', 'commit': F2, 'by': None, 'comment_id': W['id'],
                      'created_at': W['created_at'], 'author_id': W['author_id'], 'first_line': _r7_wd_line(F2, 'r0')}
                other = {'plan': hf.PLAN, 'round': hf.ROUND, 'events': [ev]}
                other[key] = value
                # read before this round's snapshot (landings/round-0/ precedes landings/round-1/)
                w.add_main(_next(w), {R7_SNAP.replace('round-1', 'round-0'): hf.jb(other)})
                return _r7_deleted(t, w, F, F2, W)
            out['W recorded in this round\'s %s; a committed snapshot of another %s records W\'s comment id'
                % (where, name)] = _r7_guarded(one)
    check('R7-N5-ROUND', 'W recorded in this round\'s snapshot (separately, in the ledger and the snapshot); a '
          'committed snapshot of another round (separately, another plan), read before this round\'s, records an '
          'event with W\'s comment id; W deleted. Records are taken per plan and round (sec. 6.3, "an append-only list '
          'of observed events per plan and round"): the other record is not merged with this round\'s, and this '
          'round\'s W still binds',
          "each: F2 admitted, its full chain exits 0; F refused at point 'state'", out,
          len(out) == 4 and all(_r7_admits(o) for o in out.values()))


def r7_n5_distinct(t):
    """Distinct comments are distinct events: a later withdrawal is not dropped as a duplicate of an earlier one."""
    def one():
        w = t.world()
        F = t.freeze(w)
        F2 = t.freeze(w, extra={'syn/other.txt': b'2\n'})
        F3 = t.freeze(w, extra={'syn/other.txt': b'3\n'})
        w.designate(F)
        W1 = w.comment(hf.PLAN_ISSUE, _r7_wd_line(F))
        w.designate(F2)
        W2 = w.comment(hf.PLAN_ISSUE, _r7_wd_line(F2))
        w.designate(F3)
        snap = auth.admit(w.h, t.repo, w.run_id, hf.PLAN, hf.ROUND, F3, t.p)[1]
        levs = []
        for W in (W1, W2):
            sev = [e for e in snap['events'] if e['comment_id'] == W['id']][0]
            lev = {k: sev[k] for k in ('kind', 'commit', 'by', 'comment_id', 'created_at', 'author_id', 'first_line')}
            lev.update(plan=hf.PLAN, round=hf.ROUND)
            levs.append(lev)
        w.land_ledger(hf.jb({'schema': auth.ledger_schema, 'events': levs}))
        w.add_main(_next(w), {R7_SNAP: hf.jb(snap)})
        for W in (W1, W2):
            w.comments[(hf.REPO_ID, hf.PLAN_ISSUE)].remove(W)
        return {'W1, W2 deleted: F3': _p5(t, w, F3), 'W1, W2 deleted: F3 full chain': _fullx(t, w, F3),
                'W1, W2 deleted: F2': _p5(t, w, F2), 'W1, W2 deleted: F': _p5(t, w, F)}
    o = _r7_guarded(one)
    check('R7-N5-DISTINCT', 'F designated, W1 withdraws F, F2 designated, W2 withdraws F2, F3 designated; F3 landed '
          '(W1 and W2 in the ledger and the snapshot); W1 and W2 deleted: both withdrawals bind (distinct comments '
          'are distinct events); F3 is admitted, F and F2 stay withdrawn',
          "F3 admitted, its full chain exits 0; F and F2 refused at point 'state'", o,
          o.get('W1, W2 deleted: F3', {}).get('admitted') is True and
          o.get('W1, W2 deleted: F3 full chain', {}).get('exit') == 0 and
          _refused5(o.get('W1, W2 deleted: F2', {}), 'state') and _refused5(o.get('W1, W2 deleted: F', {}), 'state'))


# ---- acceptance, durable evidence and replay ----------------------------------------------------------------------

def acceptance_controls(r, t):
    w = t.world()
    F = t.freeze(w)
    w.designate(F)
    code, res = t.run(w, F)
    snap = res['config']['admission']['simulated_chain']['snapshot']
    pins = {'engine': res['engine']['blob_sha256'], 'config': res['config']['blob_sha256'],
            'adapters': {a['name']: a['module_sha256'] for a in res.get('adapters', [])},
            'admission': {k: snap[k] for k in ('freeze', 'designation_comment_id', 'pin_table_sha256',
                                               'authority_sha256')}}
    hres = copy.deepcopy(res)
    code_h, res_h = t.run(w, F, harness=True, control={})
    files_h = sorted(os.listdir(os.path.dirname(os.path.join(r.out_root, 'run%03d' % r.n, 'x'))))
    check('X11', 'a control-harness PASS result presented with the pinned engine and configuration hashes: '
          'non-acceptance; the harness never writes result.json',
          "accept() is false for the harness result and for the simulated-chain result, and the harness run "
          "directory holds control-result.json only", {'harness_exit': code_h, 'files': files_h},
          code_h == 0 and not checker.accept(res_h, code_h, pins) and not checker.accept(hres, code, pins)
          and files_h == ['control-result.json'])
    # a chain-labelled copy, the landing record, and the consumer's host checks (TR30)
    chain = copy.deepcopy(res)
    del chain['harness']
    chain['config']['admission'] = {'mode': 'chain', 'snapshot': snap,
                                    'snapshot_sha256': res['config']['admission']['snapshot_sha256']}
    raw = util.dump_result(chain).encode('utf-8')
    gz = checker.deterministic_gzip(raw)
    w.h.artifacts[(w.run_id, 'ledger-coverage-result')] = sha(raw)
    host_pins = dict(pins, repository_id=hf.REPO_ID, workflow_path=hf.WF_PATH, workflow_sha256=sha(hf.WF),
                     engine_pins={}, authority_blob_sha256=sha(w.a_bytes))
    landing = {'evaluated': snap.get('evaluated'), 'artifact_name': 'ledger-coverage-result',
               'result_sha256': sha(raw)}
    ok_full = checker.accept_with_host(raw, 0, host_pins, w.h, landing)
    bad_landing = dict(landing, evaluated={'commit': '0' * 40})
    check('TR30', 'a result whose evaluated commits differ from the landing record\'s: non-acceptance',
          "accept_with_host is true for the matching landing record and false for the other",
          {'matching': ok_full, 'differing': checker.accept_with_host(raw, 0, host_pins, w.h, bad_landing)},
          ok_full and not checker.accept_with_host(raw, 0, host_pins, w.h, bad_landing))
    gz_bad = checker.deterministic_gzip(raw + b' ')
    check('TR46', 'a committed compressed result whose uncompressed sha256 differs from the recorded one: refused '
          'at landing', "verify_compressed is true for the exact bytes and false for the altered ones, and the gzip "
          "header carries mtime 0 and operating-system byte 255",
          {'exact': checker.verify_compressed(gz, sha(raw)), 'altered': checker.verify_compressed(gz_bad, sha(raw)),
           'mtime_zero': gz[4:8] == b'\x00\x00\x00\x00', 'os_byte': gz[9]},
          checker.verify_compressed(gz, sha(raw)) and not checker.verify_compressed(gz_bad, sha(raw))
          and gz[4:8] == b'\x00\x00\x00\x00' and gz[9] == 255)
    replay_controls(r, t, w, F, chain, raw, gz, snap)


def replay_controls(r, t, w, F, chain, raw, gz, snap):
    d = tempfile.mkdtemp(prefix='landing-', dir=r.out_root)
    land = {'schema': 'oi-ledger-landing/1', 'name': 'syn-round-1',
            'result': {'path': 'result.json.gz', 'sha256': sha(raw), 'compressed_sha256': sha(gz)},
            'snapshot': {'path': 'snapshot.json', 'sha256': chain['config']['admission']['snapshot_sha256']}}
    open(os.path.join(d, 'landing.json'), 'wb').write(hf.jb(land))
    open(os.path.join(d, 'result.json.gz'), 'wb').write(gz)
    open(os.path.join(d, 'snapshot.json'), 'wb').write(hf.jb(snap))
    out = r.out()
    code, res = cli.run(['replay', '--snapshot', os.path.join(d, 'landing.json'), '--out', out], repo=t.repo,
                        stderr=io.StringIO())
    eq = (res or {}).get('replay', {}).get('equal_to_committed')
    mode = ((res or {}).get('config') or {}).get('admission', {}).get('mode')
    bad = tempfile.mkdtemp(prefix='landing-bad-', dir=r.out_root)
    for f in ('landing.json', 'snapshot.json'):
        shutil.copy(os.path.join(d, f), bad)
    open(os.path.join(bad, 'result.json.gz'), 'wb').write(checker.deterministic_gzip(raw + b'\n'))
    code_b, res_b = cli.run(['replay', '--snapshot', os.path.join(bad, 'landing.json'), '--out', r.out()],
                            repo=t.repo, stderr=io.StringIO())
    check('TR45-opB', 'the offline replay of an op-B/D result from its committed snapshot: output equal to the '
          'committed result except config.admission.mode = "replay"; never acceptable; a result file that does not '
          'hash to its recorded sha256 makes the replay refuse',
          "replay exit equals the committed exit, equal_to_committed is true, mode is 'replay', accept() is false; "
          "the altered landing refuses with REPLAY_REFUSED",
          {'exit': code, 'equal': eq, 'mode': mode, 'altered': (code_b, stop(res_b))},
          code == chain['exit_status'] and eq is True and mode == 'replay' and
          not checker.accept(res or {}, code, {}) and (code_b, stop(res_b)) == (65, 'REPLAY_REFUSED'))


# ---- native delegation G4-G9 on a small on-disk repository -------------------------------------------------------

SC42 = 'audit/sc42-result.json'
CTL = 'audit/sc42-controls.json'
CHK = 'audit/check_sc42.py'
CHECKER_SRC = b'''import os, sys
ROOT = os.getcwd()
if '--self-test' in sys.argv:
    sys.stdout.write(open(os.path.join(ROOT, 'audit/sc42-controls.json')).read())
else:
    sys.stdout.write('{"base": "%s", "sites": %d}\\n' % (open(os.path.join(ROOT, 'audit/base.txt')).read().strip(),
                     len(open(os.path.join(ROOT, 'doc/a.md')).read().split())))
'''


def git(d, *a, env=None):
    e = dict(os.environ, GIT_AUTHOR_NAME='fixture', GIT_AUTHOR_EMAIL='fixture@invalid', GIT_COMMITTER_NAME='fixture',
             GIT_COMMITTER_EMAIL='fixture@invalid', GIT_AUTHOR_DATE='2026-01-01T00:00:00Z',
             GIT_COMMITTER_DATE='2026-01-01T00:00:00Z')
    return subprocess.run(['git', '-C', d] + list(a), capture_output=True, text=True, env=e, check=True).stdout.strip()


def commit_files(d, files, msg):
    for p, b in files.items():
        f = os.path.join(d, p)
        if b is None:
            os.remove(f)
            continue
        os.makedirs(os.path.dirname(f), exist_ok=True)
        open(f, 'wb').write(b)
    git(d, 'add', '-A')
    git(d, 'commit', '-q', '-m', msg)
    return git(d, 'rev-parse', 'HEAD')


def g_controls(r):
    from ledger_coverage.adapters import deleg_rerun_equal as rerun, deleg_preserve_check as pc
    from ledger_coverage.adapters import deleg_fingerprint_regen as fr
    d = tempfile.mkdtemp(prefix='g-repo-', dir=r.out_root)
    git(d, 'init', '-q')
    words = b'one two three\n'
    good = b'{"base": "basecommit", "sites": 3}\n'
    H = commit_files(d, {'doc/a.md': words, 'audit/base.txt': b'basecommit\n', CHK: CHECKER_SRC,
                         CTL: open_controls(), SC42: good}, 'H')
    X = commit_files(d, {'doc/b.md': b'x\n'}, 'X')
    F = X
    repo = gitobj.GitRepo(d)
    cls = {'id': 'sc42', 'adapter': 'rerun-equal', 'paths': [SC42],
           'params': {'must_contain': 'basecommit', 'controls_path': CTL, 'checker_path': CHK}}
    roles = {'scientific_base': H, 'candidate': X, 'freeze': F, 'certified': X, 'ledger_sha256': '0' * 64}
    dele = delmod.Delegation({'schema': 'oi-delegation/1', 'classes': [cls]}, {'rerun-equal': rerun})

    def env(out):
        return delmod.Native(repo, d, out, F, True)
    items, rep = dele.verify(repo, roles, env(r.out()), {'splices': []})
    pos = [i['class'] for i in items]
    # G4: a supplied result file claiming verbose_equal true, while the clone's re-execution differs
    Xb = commit_files(d, {SC42: b'{"base": "basecommit", "sites": 4}\n'}, 'X with a hand-edited result')
    supplied = {'sc42-rerun.json': b'{"candidate": "%s", "verbose_exit": 0, "verbose_equal": true, '
                                  b'"self_test_equal": true, "plan": "%s"}' % (Xb.encode(), F.encode())}
    items4, rep4 = dele.verify(repo, dict(roles, candidate=Xb, certified=Xb), env(r.out()), {'splices': []}, supplied)
    check('G4', 'sc42 with a supplied result claiming verbose_equal true while the clone\'s re-execution differs: FAIL '
          'delegated-evidence-invalid; the supplied file is not read as evidence',
          "the positive case has no item; the mutant gives delegated-evidence-invalid; the report lists the supplied "
          "file as ignored", {'positive': pos, 'mutant': sorted({i['class'] for i in items4}),
                              'ignored': rep4['supplied_evidence_ignored'], 'runs': len(rep4['evidence_record']['runs'])},
          pos == [] and 'delegated-evidence-invalid' in {i['class'] for i in items4} and
          rep4['supplied_evidence_ignored'] == ['sc42-rerun.json'])
    # G9: C = X plus one commit changing the SC-42 result file; X alone passes
    C = Xb
    items9, rep9 = dele.verify(repo, dict(roles, candidate=X, certified=C), env(r.out()), {'splices': []})
    trees = {(i['tree'], i['class']) for i in items9}
    check('G9', 'C = X plus one commit that changes the SC-42 result file, the class at X alone passing: FAIL for '
          'sc42 from the clone at C', "no item at X; delegated-evidence-invalid at C",
          sorted(trees), ('C', 'delegated-evidence-invalid') in trees and not any(t_ == 'X' for t_, _ in trees))
    # G8: no F; a supplied result with plan null
    items8, rep8 = dele.verify(repo, dict(roles, freeze=None), env(r.out()), {'splices': []},
                               {'sc42-rerun.json': b'{"plan": null}'})
    cls_of = {(i['class'], i.get('tree')) for i in items8}
    dele_ev = delmod.Delegation({'schema': 'oi-delegation/1', 'classes': [dict(cls, evidence=['sc42-rerun.json'])]},
                                {'rerun-equal': rerun})
    items8b, _ = dele_ev.verify(repo, dict(roles, freeze=None), env(r.out()), {'splices': []},
                                {'sc42-rerun.json': b'{"plan": null}'})
    c8 = sorted({i['class'] for i in items8b})
    check('G8', 'delegated evidence with plan null and no F: never PASS: REVIEW_REQUIRED delegated-evidence-missing '
          'for the class, and the field FAIL delegated-evidence-invalid',
          "the class gives delegated-evidence-missing and the plan-null file delegated-evidence-invalid",
          {'without_named_evidence': sorted(cls_of), 'with': c8},
          c8 == ['delegated-evidence-invalid', 'delegated-evidence-missing'])
    # G5: coverage-ledger against the census the tool runs in the clone
    census = b'''import json, sys
print(json.dumps({"entries": [{"id": "S:1", "fingerprint": "%s"}]}))
'''
    led_path = 'cov/LEDGER.json'
    led_h = b'[{"id": "S:1", "fingerprint": "aaaa"}]\n'
    d5 = tempfile.mkdtemp(prefix='g5-repo-', dir=r.out_root)
    git(d5, 'init', '-q')
    H5 = commit_files(d5, {led_path: led_h, 'tools/proof_census.py': census % b'bbbb'}, 'H')
    X5 = commit_files(d5, {led_path: led_h.replace(b'aaaa', b'bbbb')}, 'X')
    X5b = commit_files(d5, {led_path: led_h.replace(b'aaaa', b'cccc')}, 'X stale')
    repo5 = gitobj.GitRepo(d5)
    cls5 = {'id': 'coverage-ledger', 'adapter': 'fingerprint-regen', 'paths': [led_path], 'ledgered_paths': [led_path],
            'params': {'stale_ids': ['S:1'], 'census_path': 'tools/proof_census.py'}}
    dl5 = delmod.Delegation({'schema': 'oi-delegation/1', 'classes': [cls5]}, {'fingerprint-regen': fr})
    ok5, _ = dl5.verify(repo5, dict(roles, scientific_base=H5, candidate=X5, freeze=X5, certified=X5),
                        delmod.Native(repo5, d5, r.out(), X5, True), {'splices': []})
    bad5, _ = dl5.verify(repo5, dict(roles, scientific_base=H5, candidate=X5b, freeze=X5b, certified=X5b),
                         delmod.Native(repo5, d5, r.out(), X5b, True), {'splices': []},
                         {'proof-census.json': b'{"entries": [{"id": "S:1", "fingerprint": "cccc"}]}'})
    check('G5', 'coverage-ledger with a supplied census JSON; one STALE value at X differing from the census the '
          'tool runs: FAIL', "no item when the value equals the tool's census; delegated-evidence-invalid when it "
          "differs, whatever the supplied file says",
          {'positive': [i['class'] for i in ok5], 'mutant': sorted({i['class'] for i in bad5})},
          not ok5 and 'delegated-evidence-invalid' in {i['class'] for i in bad5})
    # G6: tex with a supplied preserve_check result reporting pass, while a TeX stamp at X is wrong
    d6 = tempfile.mkdtemp(prefix='g6-repo-', dir=r.out_root)
    git(d6, 'init', '-q')
    md = b'# doc\n'
    H6 = commit_files(d6, {'p/A.md': md, 'p/A.tex': b'tex\n% source-sha256: 0\n'}, 'H')
    X6 = commit_files(d6, {'p/A.tex': b'tex\n% source-sha256: ' + sha(md).encode() + b'\n'}, 'X')
    X6b = commit_files(d6, {'p/A.tex': b'tex\n% source-sha256: ' + b'1' * 64 + b'\n'}, 'X wrong stamp')
    repo6 = gitobj.GitRepo(d6)
    cls6 = {'id': 'tex', 'adapter': 'preserve-check-v1', 'paths': ['p/A.tex'],
            'params': {'sources': {'p/A.tex': 'p/A.md'}, 'checker_path': 'p/none.py', 'checker_sha256': '0' * 64,
                       'required_checks': []}}
    dl6 = delmod.Delegation({'schema': 'oi-delegation/1', 'classes': [cls6]}, {'preserve-check-v1': pc})
    good_res = b'{"schema": "a1exit-checker-result-v1", "verdict": "pass", "plan": "%s"}' % X6b.encode()
    bad6, _ = dl6.verify(repo6, dict(roles, scientific_base=H6, candidate=X6b, freeze=X6b, certified=X6b), None,
                         {'splices': []}, {'tex-preserve-check.json': good_res})
    ok6, _ = dl6.verify(repo6, dict(roles, scientific_base=H6, candidate=X6, freeze=X6, certified=X6), None,
                        {'splices': []})
    check('G6', 'tex with a supplied preserve_check result reporting pass, while a TeX stamp at X is wrong: FAIL '
          'delegated-evidence-invalid', "the wrong stamp gives delegated-evidence-invalid; the right stamp gives no "
          "invalid item (the checker run itself is missing locally)",
          {'wrong': sorted({i['class'] for i in bad6}), 'right': sorted({i['class'] for i in ok6})},
          'delegated-evidence-invalid' in {i['class'] for i in bad6} and
          'delegated-evidence-invalid' not in {i['class'] for i in ok6})
    # G7: pdf evidence whose candidate_tree differs from X's, or whose artifact hash differs
    cls7 = {'id': 'pdf', 'adapter': 'preserve-check-v1', 'paths': ['p/A.tex'],
            'params': {'workflow_path': 'wf.yml', 'job': 'pdf-compare', 'checker_sha256': 'c' * 64}}
    dl7 = delmod.Delegation({'schema': 'oi-delegation/1', 'classes': [cls7]}, {'preserve-check-v1': pc})

    class H7:
        def __init__(self, result, art):
            self.res, self.art = result, art

        def runs_for(self, rid, head):
            return [{'workflow_path': 'wf.yml', 'head_sha': head, 'jobs': [{'name': 'pdf-compare',
                                                                             'conclusion': 'success'}],
                     'result': self.res, 'artifact_sha256': self.art}]
    tree = repo6.tree_id(X6)
    good7 = {'candidate_commit': X6, 'candidate_tree': tree, 'sha256': 'd' * 64, 'checker_blob_sha256': 'c' * 64}
    out7 = {}
    for name, res_, art in (('good', good7, 'd' * 64), ('tree', dict(good7, candidate_tree='0' * 40), 'd' * 64),
                            ('artifact', good7, 'e' * 64)):
        it, _ = dl7.verify(repo6, dict(roles, scientific_base=H6, candidate=X6, freeze=X6, certified=X6),
                           delmod.Native(repo6, d6, r.out(), X6, True, host=H7(res_, art), repo_id=1),
                           {'splices': []})
        out7[name] = sorted({i['class'] for i in it})
    check('G7', 'pdf evidence whose candidate_tree differs from X\'s, or whose artifact hash differs: FAIL '
          'delegated-evidence-invalid', "good: no item; tree and artifact mutants: delegated-evidence-invalid",
          out7, out7['good'] == [] and out7['tree'] == ['delegated-evidence-invalid'] and
          out7['artifact'] == ['delegated-evidence-invalid'])
    not_run('G-A1', 'the A1 classes executed natively in disposable clones at X and C (tex, sc42, coverage-ledger) '
            'and the host-run classes (pdf, ci) read from the host API', 'needs F and a CI job (sec. A.40: a full '
            'clone of the repository per tree); CI plan in the report')


def open_controls():
    return b'{"controls": "fixed"}\n'


# ---- R16/R17, A12r, Z9h, Z11 and S4a (synthetic) -----------------------------------------------------------------

def r_controls(r):
    from ledger_coverage.engine import controls_engine as ce
    w = ce.World()
    H = w.pin
    a = ce.off(ce.base_text, 'beta line two')
    led = ce.ledger(H, [(ce.doc_path, a, a + 4, 'betx')], w.repo)
    led['edits'] = []
    X = w.child(H, ce.base_text.replace('beta line two', 'betx line two', 1), subject='candidate')
    ctx = w.ctx()

    class D:
        def paths(self):
            return []

        def record_prefixes(self):
            return ['plan/']

        def owns_ledgered(self, p):
            return False
    C16 = w.repo.derive(X, {'notes/unrelated.txt': b'x\n'}, parents=[X], subject='C16')
    e = exmod.Execution(ctx, H, X, led, D())
    e.commits_after([C16])
    C17 = w.repo.derive(X, {'plan/execution/result.json': b'{}\n'}, parents=[X], subject='C17')
    e17 = exmod.Execution(ctx, H, X, led, D())
    e17.commits_after([C17])
    c16 = [(i['class'], i.get('commit')) for i in e.items]
    check('R16', 'C = X plus one commit that changes an unledgered, undeclared path: FAIL unauthorized-change naming '
          'that commit', "one unauthorized-change item whose commit is that commit", c16,
          c16 == [('unauthorized-change', C16)])
    check('R17', 'C = X plus one commit that changes only a record path the plan admits after F: PASS for that '
          'commit', "no item; the path is classified record", {'items': e17.items,
                                                                   'paths': e17.checks[-1]['commits'][0]['paths']},
          not e17.items and e17.checks[-1]['commits'][0]['paths'] == [{'path': 'plan/execution/result.json',
                                                                       'class': 'record'}])


def a12r(r):
    """A widening review whose verdicts omit one changed item; separately one with no owner authorization."""
    syn = sf.Syn()
    pd = sf.patch_doc(syn.H, [])
    base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}, 'allow_widened': True, 'widening_review': True}
    out = {}
    for name, extra in (('complete', {}), ('omits-item', {'widening_items': []}),
                        ('no-authorization', {'widening_no_auth': True})):
        v = dict(base, **extra)
        if name == 'omits-item':
            v['widening_items'] = ['syn-allow-1:other']
        c, p, s, _ = syn.build(v)
        code, res = r.cli(syn.repo, ['terms', '--commit', syn.H], c, p, s)
        out[name] = (code, classes(res))
    check('A12r', 'a widening review whose verdicts omit one changed item; separately one with no owner '
          'authorization: FAIL record-invalid each', "complete: exit 0; both mutants: exit 20 with record-invalid",
          out, out['complete'][0] == 0 and all(out[k][0] == 20 and 'record-invalid' in out[k][1]
                                               for k in ('omits-item', 'no-authorization')))


def z9h(values):
    src = open(os.path.join(tools, 'ledger_coverage', 'engine', 'outcome.py')).read() + "\nPLANTED = 'guard-pin'\n"
    found = purity.lint_sources({'engine/outcome.py': src}, values, [])
    check('Z9h', '\'guard-pin\' planted in an engine module, with the adapter companions in the value set: lint '
          'FAIL', "a finding names the planted literal", found[:3], any('guard-pin' in f for f in found))


def z11_s4a(r):
    syn = sf.Syn()
    pd = sf.patch_doc(syn.H, [])
    cls = {'schema': 'oi-side-change-classes/1', 'record_id': 'k1', 'author': sf.WRITER, 'supersedes': None,
           'classes': [{'id': 'trial-workflow', 'pins': []}]}
    cls2 = dict(cls, record_id='k2')
    c, p, s, _ = syn.build({'patch_sha': sha(pd), 'files': {'syn/patch.json': pd},
                            'records_extra': {'syn/k1.json': cls, 'syn/k2.json': cls2}})
    # records_extra gives kind "record"; mark them as side-change class records in the configuration
    cfg = json.loads(syn.repo.read(c, p))
    for rr in cfg['records']:
        if rr['path'] in ('syn/k1.json', 'syn/k2.json'):
            rr['kind'] = 'side-change-classes'
    c2 = syn.repo.derive(c, {p: sf.jb(cfg)}, parents=syn.repo.parents(c))
    code, res = r.cli(syn.repo, ['terms', '--commit', syn.H], c2, p, sha(sf.jb(cfg)), harness=True)
    one = dict(cls, classes=[{'id': 'a', 'pins': []}, {'id': 'a', 'pins': []}])
    c3, p3, s3, _ = syn.build({'patch_sha': sha(pd), 'files': {'syn/patch.json': pd},
                               'records_extra': {'syn/k1.json': one}})
    cfg3 = json.loads(syn.repo.read(c3, p3))
    for rr in cfg3['records']:
        if rr['path'] == 'syn/k1.json':
            rr['kind'] = 'side-change-classes'
    c4 = syn.repo.derive(c3, {p3: sf.jb(cfg3)}, parents=syn.repo.parents(c3))
    code2, res2 = r.cli(syn.repo, ['terms', '--commit', syn.H], c4, p3, sha(sf.jb(cfg3)), harness=True)
    check('Z11', 'two class records, or one record, defining the same class id: ERROR CONFIG_INCONSISTENT',
          "both exit 65 with stop CONFIG_INCONSISTENT", [(code, stop(res)), (code2, stop(res2))],
          (code, stop(res)) == (65, 'CONFIG_INCONSISTENT') and (code2, stop(res2)) == (65, 'CONFIG_INCONSISTENT'))
    # S4a: a record of each kind whose supersedes names a blob absent from the object store, or another kind
    from ledger_coverage.engine import records as rec
    kinds = ['oi-hp-adjudication/1', 'oi-context-adjudication/1', 'oi-hit-classification/1', 'oi-term-rules/2',
             'oi-scope/1', 'oi-side-change-classes/1', 'oi-reconciliation/1', 'oi-retirement-config/1']
    out = {}
    for k in kinds:
        other = {'schema': 'oi-scope/1' if k != 'oi-scope/1' else 'oi-term-rules/2', 'record_id': 'o',
                 'supersedes': None, 'author': 'w'}
        ob = util.canonical(other)
        for case, sup in (('absent', {'path': 'r/none.json', 'blob_sha256': '0' * 64}),
                          ('other-kind', {'path': 'r/o.json', 'blob_sha256': sha(ob)})):
            doc = {'schema': k, 'record_id': 'r', 'config_id': 'r', 'author': 'w', 'supersedes': sup}
            db = util.canonical(doc)
            st = rec.Store([('r/r.json', db), ('r/o.json', ob)])
            probs = rec.supersedes_problems({'path': 'r/r.json', 'blob_sha256': sha(db)}, doc, st)
            out['%s/%s' % (k, case)] = bool(probs)
    check('S4a', 'a record of each kind whose supersedes names a blob that does not exist, or a record of another '
          'kind: FAIL record-invalid for each kind', "every kind and case gives a supersedes problem (which "
          "lint_chain reports as record-invalid)", out, all(out.values()))


# ---- S1-P2: the real-host history reader over a host whose path listing simplifies history ------------------

S1_P2_IDS = ['S1-P2-LISTING', 'S1-P2-OLD', 'S1-P2-NEW', 'S1-P2-ADMIT', 'S1-P2-SQUASH', 'S1-P2-REVERT',
             'S1-P2-CHAIN', 'S1-P2-FAILCLOSED', 'S1-Q8']


def s1_p2_history_controls(r):
    """The history reader of the real host (RestHost.file_history) against a fake rest transport whose
    path-filtered commit listing omits a merge commit whose path equals its second parent's, as the host's does.
    A and the freeze ledger land by two-parent merges. The reader before the correction misses every version and
    the admission refuses; the corrected reader finds every version the in-memory host's first-parent semantics
    finds, and the admission passes. Fail-closed: a listing that ends before the root, a truncated tree, a host
    error, a call bound reached and bytes that do not match their tree entry each refuse."""
    from ledger_coverage.adapters import rest_fixture as rf
    from ledger_coverage.engine import host as hostmod
    t = TR(r)

    def show(code, res):
        return {'exit': code, 'stop': stop(res), 'message': ((res or {}).get('stop') or {}).get('message', '')[:160]}

    def norm(hist):
        return [{k: v.get(k) for k in ('commit', 'parent', 'blob', 'merged_by_id', 'merged_at', 'merge_commit')}
                for v in hist]

    def brief(hist):
        return [(v['commit'], v['parent'], None if v['blob'] is None else sha(v['blob'])[:12]) for v in hist]

    w = t.world()
    F = t.freeze(w)
    w.designate(F)
    rf.as_merge_landings(w.h, hf.REPO_ID)
    ledger_path = hf.LEDGER_PATH
    paths = [auth.authority_path, ledger_path]
    fake = rf.FakeRest(w.h, hf.REPO_ID)
    hy = rf.HybridHost(w.h, hf.REPO_ID, fake)
    listed = {p: [c['sha'] for c in hy._json('/repositories/%d/commits?sha=%s&path=%s&per_page=100&page=1'
                                              % (hf.REPO_ID, w.main, p))] for p in paths}
    merges = [c for c in w.h.first_parents(hf.REPO_ID, w.main) if len(w.h.repos[hf.REPO_ID]['commits'][c]['parents']) == 2]
    check('S1-P2-LISTING', 'the fake path listing simplifies history as the host does: A and the ledger landed by '
          'two-parent merges, and the listing names their branch commits, not the merges',
          'merges include c1 and c1l; no merge is listed for either path; b-c1 and b-c1l are listed',
          {'merges': merges, 'listed': listed},
          'c1' in merges and 'c1l' in merges and not any(m in listed[p] for p in paths for m in merges) and
          'b-c1' in listed[auth.authority_path] and 'b-c1l' in listed[ledger_path])
    truth = {p: norm(w.h.file_history(hf.REPO_ID, p)) for p in paths}
    old = {p: norm(rf.old_file_history(rf.HybridHost(w.h, hf.REPO_ID), hf.REPO_ID, p)) for p in paths}
    check('S1-P2-OLD', 'countercontrol: the reader before the correction misses every merge-landed version',
          'old reader returns no version of A or of the ledger, while the first-parent truth has one each',
          {'old': {p: brief(v) for p, v in old.items()}, 'truth': {p: brief(v) for p, v in truth.items()}},
          all(old[p] == [] and len(truth[p]) == 1 for p in paths))
    new = {p: norm(rf.HybridHost(w.h, hf.REPO_ID).file_history(hf.REPO_ID, p)) for p in paths}
    check('S1-P2-NEW', 'the corrected reader finds every version: equal to the first-parent semantics of the '
          'in-memory host (commit, first parent, bytes, merge record)', 'new[p] == truth[p] for A and the ledger, '
          'and the versions are the merges c1 and c1l', {p: brief(v) for p, v in new.items()},
          all(new[p] == truth[p] for p in paths) and [v['commit'] for v in new[auth.authority_path]] == ['c1'] and
          [v['commit'] for v in new[ledger_path]] == ['c1l'])
    # the admission through the rest reader: refused with the old reader, admitted with the corrected one
    oldh = rf.HybridHost(w.h, hf.REPO_ID)
    oldh.file_history = lambda repo_id, path: rf.old_file_history(oldh, repo_id, path)
    code_o, res_o = t.run(w, F, control={'host': oldh, 'run_id': w.run_id, 'repo_id': hf.REPO_ID})
    code_n, res_n = t.run(w, F, control={'host': rf.HybridHost(w.h, hf.REPO_ID), 'run_id': w.run_id,
                                         'repo_id': hf.REPO_ID})
    code_m, res_m = t.run(w, F)
    adm = ((res_n or {}).get('config') or {}).get('admission') or {}
    check('S1-P2-ADMIT', 'the simulated chain over the rest reader with merge-landed A and ledger: refused (ERROR '
          'CONFIG_UNREVIEWED, exit 65) with the reader before the correction, admitted (exit 0, control-harness) with '
          'the corrected reader, as on the in-memory host',
          "old: exit 65 and stop CONFIG_UNREVIEWED; new: exit 0 and admission.mode == 'control-harness'; in-memory: "
          "exit 0", {'old': show(code_o, res_o), 'new': show(code_n, res_n), 'in_memory': show(code_m, res_m)},
          code_o == 65 and stop(res_o) == 'CONFIG_UNREVIEWED' and code_n == 0 and
          adm.get('mode') == 'control-harness' and code_m == 0)
    # no regression for single-parent (squash) landings
    w2 = t.world()
    sq = {p: (norm(rf.HybridHost(w2.h, hf.REPO_ID).file_history(hf.REPO_ID, p)),
              norm(w2.h.file_history(hf.REPO_ID, p))) for p in paths}
    check('S1-P2-SQUASH', 'single-parent landings: the corrected reader equals the in-memory host',
          'new == truth for A and the ledger', {p: brief(v[0]) for p, v in sq.items()},
          all(a == b and a for a, b in sq.values()))
    # a revert and a deletion by merges: A -> B -> A -> deleted, each change found once, in order
    w3 = t.world()
    xp = 'syn/x.txt'
    for k, val in enumerate([b'one\n', b'two\n', b'one\n', None]):
        w3.add_main('cx%d' % k, {xp: val})
    rf.as_merge_landings(w3.h, hf.REPO_ID)
    got3 = norm(rf.HybridHost(w3.h, hf.REPO_ID).file_history(hf.REPO_ID, xp))
    tru3 = norm(w3.h.file_history(hf.REPO_ID, xp))
    old3 = norm(rf.old_file_history(rf.HybridHost(w3.h, hf.REPO_ID), hf.REPO_ID, xp))
    check('S1-P2-REVERT', 'a path changed, reverted and deleted by merges: every change found, in order, the '
          'deletion with no bytes; the reader before the correction finds none',
          "new == truth, commits ['cx0','cx1','cx2','cx3'], last blob None; old == []",
          {'new': brief(got3), 'old': brief(old3)},
          got3 == tru3 and [v['commit'] for v in got3] == ['cx0', 'cx1', 'cx2', 'cx3'] and got3[-1]['blob'] is None
          and old3 == [])
    hy4 = rf.HybridHost(w.h, hf.REPO_ID)
    chain = {c: hy4.on_first_parent_chain(hf.REPO_ID, c, w.main) for c in ('c1', 'c1l', 'b-c1', 'b-c1l', 'c0')}
    check('S1-P2-CHAIN', 'on_first_parent_chain from the host listing: the merges and the root are on main\'s '
          'first-parent chain, their branch commits are not', 'c1, c1l, c0 True; b-c1, b-c1l False', chain,
          chain == {'c1': True, 'c1l': True, 'b-c1': False, 'b-c1l': False, 'c0': True})
    # fail-closed
    fc = {}

    def attempt(label, mk):
        h_ = mk()
        try:
            h_.file_history(hf.REPO_ID, auth.authority_path)
            fc[label] = 'read'
        except hostmod.HostUnavailable as exc:
            fc[label] = 'HostUnavailable: %s' % str(exc)[:100]

    def with_fake(**kw):
        def mk():
            f = rf.FakeRest(w.h, hf.REPO_ID)
            for k_, v_ in kw.items():
                setattr(f, k_, v_)
            return rf.HybridHost(w.h, hf.REPO_ID, f)
        return mk
    attempt('listing ends before the root', with_fake(listing_pages=0))
    attempt('tree listing truncated', with_fake(truncate_trees=True))
    attempt('host error on a tree read', with_fake(fail={'/git/trees/'}))
    attempt('host error on the pull-request read', with_fake(fail={'/pulls'}))
    attempt('bytes differ from the tree entry', with_fake(corrupt={auth.authority_path}))
    attempt('call bound reached', lambda: rf.HybridHost(w.h, hf.REPO_ID, max_calls=3))
    old_pages = hostmod.RestHost.max_pages
    try:
        hostmod.RestHost.max_pages = 0
        attempt('page bound reached', lambda: rf.HybridHost(w.h, hf.REPO_ID))
    finally:
        hostmod.RestHost.max_pages = old_pages
    fh = rf.FakeRest(w.h, hf.REPO_ID)
    fh.listing_pages = 0
    code_f, res_f = t.run(w, F, control={'host': rf.HybridHost(w.h, hf.REPO_ID, fh), 'run_id': w.run_id,
                                         'repo_id': hf.REPO_ID})
    fc['admission with a listing that ends before the root'] = show(code_f, res_f)
    check('S1-P2-FAILCLOSED', 'every incomplete or failed host read refuses: HostUnavailable from the reader, and '
          'ERROR CONFIG_UNREVIEWED (exit 65) from the admission', 'every attempt raises HostUnavailable; the '
          'admission exits 65 with stop CONFIG_UNREVIEWED', fc,
          all(str(v).startswith('HostUnavailable') for k_, v in fc.items() if not k_.startswith('admission')) and
          code_f == 65 and stop(res_f) == 'CONFIG_UNREVIEWED')
    w5 = t.world()
    led = json.loads(w5.ledger_bytes.decode('utf-8'))
    check('S1-Q8', 'the empty freeze ledger the controls land carries schema and events only (owner decision Q8)',
          "keys == {'schema', 'events'}, events == []", sorted(led), sorted(led) == ['events', 'schema'] and
          led['events'] == [] and led['schema'] == auth.ledger_schema)


def write(out_root):
    os.makedirs(out_root, exist_ok=True)
    summary = {}
    for rrec in RESULTS:
        summary[rrec['status']] = summary.get(rrec['status'], 0) + 1
    doc = {'schema': 'oi-control-report/1', 'controls': sorted(RESULTS, key=lambda x: x['id']), 'summary': summary}
    with open(os.path.join(out_root, 'conformance-controls.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(doc, indent=1, sort_keys=True, default=str) + '\n')
    return doc


def main(out_root):
    os.makedirs(out_root, exist_ok=True)
    r = sf.Runner(tempfile.mkdtemp(prefix='conf-', dir=out_root))
    groups = [('TR', lambda: tr_controls(r)), ('R16', lambda: r_controls(r)), ('A12r', lambda: a12r(r)),
              ('Z11', lambda: z11_s4a(r)), ('G', lambda: g_controls(r)),
              ('S1-P2', lambda: s1_p2_history_controls(r))]
    t = None
    for name, fn in groups:
        try:
            got = fn()
            if name == 'TR':
                t = got
        except Exception as exc:
            import traceback
            record('%s-group' % name, 'the group runs', None, '%s: %s %s' % (type(exc).__name__, exc,
                                                                             traceback.format_exc()[-1200:]), 'FAIL')
    if t is not None:
        for name, fn in (('R3-F1', lambda: f1_controls(t)), ('R3-F2', lambda: f2_controls(r)),
                         ('R3-F3', lambda: f3_controls(t)), ('R4-B1', lambda: r4_b1_controls(t)),
                         ('R4-B2', lambda: r4_b2_controls(t)), ('R4-B3', lambda: r4_b3_controls(r)),
                         ('R4-B2-PROV', lambda: r4_b2_provenance_controls(t)),
                         ('R4-B3-DUP', lambda: r4_b3_duplicate_controls(r)),
                         ('R4-N2', lambda: r4_n2_controls(t)), ('R5-K1', lambda: r5_k1_controls(t)),
                         ('R5-K2', lambda: r5_k2_controls(t)), ('R5-N6', lambda: r5_n6_controls(r)),
                         ('TR54-TR61', lambda: tr54_tr61(t)), ('TR62-TR64', lambda: tr62_tr64(t)),
                         ('TR65', lambda: tr65(t)), ('TR66-TR70', lambda: tr66_tr70(t)),
                         ('LN1-LN8', lambda: ln1_ln8(r)), ('LN9-LN12', lambda: ln9_ln12(r)),
                         ('R6-EV', lambda: ledger_event_verdicts(t)), ('TR32-OWN', lambda: tr32_own(t)),
                         ('R6-G1', lambda: r6_g1(t)), ('R6-G2', lambda: r6_g2(t)), ('R6-G3', lambda: r6_g3(t)),
                         ('R6-G4', lambda: r6_g4(t)), ('R6-G5', lambda: r6_g5(t)), ('R6-G6', lambda: r6_g6(r)),
                         ('R6-G7', lambda: r6_g7(t)), ('R6-G8', lambda: r6_g8(t)), ('R6-G9', lambda: r6_g9(t)),
                         ('R7-B2', lambda: r7_b2(t)), ('R7-N5', lambda: r7_n5(t)),
                         ('R7-N5-CONFLICT', lambda: r7_n5_conflict(t)), ('R7-N5-FORGED', lambda: r7_n5_forged(t)),
                         ('R7-N5-SUPERSEDE', lambda: r7_n5_supersede(t)), ('R7-N5-ROUND', lambda: r7_n5_round(t)),
                         ('R7-N5-DISTINCT', lambda: r7_n5_distinct(t))):
            try:
                fn()
            except Exception as exc:
                import traceback
                record(name, 'the control runs', None, '%s: %s %s' % (type(exc).__name__, exc,
                                                                        traceback.format_exc()[-1200:]), 'FAIL')
        # every control of design v5.5.8 is reported: one whose group stopped before it ran is FAIL, never absent
        for cid in ['TR%d' % i for i in range(54, 71)] + ['LN%d' % i for i in range(1, 13)] + ['R6-EV', 'TR32-OWN'] + \
                ['R6-G%d' % i for i in range(1, 10)] + ['R7-B2', 'R7-N5', 'R7-N5-CONFLICT', 'R7-N5-FORGED',
                                                       'R7-N5-SUPERSEDE', 'R7-N5-ROUND', 'R7-N5-DISTINCT'] + S1_P2_IDS:
            if not any(x['id'] == cid for x in RESULTS):
                group = [x for x in RESULTS if x['id'] in ('TR54-TR61', 'TR62-TR64', 'TR65', 'TR66-TR70', 'LN1-LN8',
                                                           'LN9-LN12', 'R6-EV', 'S1-P2-group')]
                record(cid, 'the control runs', None, 'its group stopped before it ran: %s'
                       % '; '.join(str(x['actual'])[-300:] for x in group), 'FAIL')
        try:
            acceptance_controls(r, t)
        except Exception as exc:
            import traceback
            record('acceptance-group', 'the group runs', None, '%s: %s %s' % (type(exc).__name__, exc,
                                                                              traceback.format_exc()[-1200:]), 'FAIL')
    return write(out_root)


if __name__ == '__main__':
    doc = main(sys.argv[1])
    print(json.dumps(doc['summary'], sort_keys=True))
    for c in doc['controls']:
        if c['status'] != 'PASS':
            print(c['status'], c['id'], json.dumps(c['actual'], default=str)[:300])
