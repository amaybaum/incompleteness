"""Controls added for the frozen design v5.5.2 (sec. 10.4, 13.2): admission TR1-TR47 on an in-memory host, the
acceptance predicate X11 and the durable evidence TR45/TR46, native delegation G4-G9 on a small on-disk
repository, commits after X R16/R17, widening A12r, purity Z9h, and the synthetic parts of S4a and Z11.

Every control is reported as {id, expected, predicate, actual, status} with status PASS, FAIL, SKIP or NOT RUN
(sec. 10.4, B6). A control that needs the real host (a CI job with the host's API) is NOT RUN here, never PASS.

Usage: python3 -I -B tools/ledger_coverage/adapters/conformance_controls.py OUT_DIR
"""
import copy
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
        self.c, self.p, self.s, self.files = self.syn.build({'patch_sha': sha(self.pd),
                                                              'files': {'syn/patch.json': self.pd}})
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
    w25.h.repos[hf.REPO_ID]['commits']['c1']['files'].pop(auth.authority_path)
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
    # TR48-TR53 (K7, v5.5.3): the files permitted under the tool directory at head_sha
    k7(t, check, show)
    # TR29: head_sha not on main's first-parent chain; head_sha = X (no workflow, no tool)
    out29 = []
    for mut in ('branch', 'x'):
        w29 = t.world()
        F29 = t.freeze(w29)
        w29.designate(F29)
        if mut == 'branch':
            w29.h.add_commit(hf.REPO_ID, 'b1', ['c1'], dict(w29.h.repos[hf.REPO_ID]['commits']['c1']['files']))
            w29.h.runs[w29.run_id]['head_sha'] = 'b1'
        else:
            w29.h.add_commit(hf.REPO_ID, 'xx', ['c1'], {'doc/s.md': b'x\n'})
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
    w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=none to=%s' % sha(w.a_bytes), author_id=owner_id)
    w.comment(hf.AUTH_ISSUE, 'oi-authority/1 approve from=none to=%s' % sha(w.ledger_bytes), author_id=owner_id)
    files = {auth.authority_path: w.a_bytes, hf.LEDGER_PATH: w.ledger_bytes, hf.WF_PATH: hf.WF,
             auth.review_path(a, sha(w.a_bytes)): w.review}
    files.update(hf.ledger_review_file(a, w.ledger_bytes, 'none'))
    files.update(extra_files)
    w.main = 'c1'
    w.h.add_commit(hf.REPO_ID, 'c0', [], {})
    w.h.add_commit(hf.REPO_ID, 'c1', ['c0'], files, merged_by=owner_id, merged_at=w.tick())
    w.h.repos[hf.REPO_ID]['main'] = 'c1'
    w.run_id = 501
    w.h.runs[w.run_id] = {'repository_id': hf.REPO_ID, 'fork': False, 'workflow_path': hf.WF_PATH,
                          'head_sha': 'c1'}
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
    F = t.freeze(w, a_bytes=a1)
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
    au = {'schema': 'oi-owner-authorization/1', 'owner': sf.OWNER, 'time': 't0', 'comment_id': 'c-2',
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
              ('Z11', lambda: z11_s4a(r)), ('G', lambda: g_controls(r))]
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
                         ('R5-K2', lambda: r5_k2_controls(t)), ('R5-N6', lambda: r5_n6_controls(r))):
            try:
                fn()
            except Exception as exc:
                import traceback
                record(name, 'the control runs', None, '%s: %s %s' % (type(exc).__name__, exc,
                                                                        traceback.format_exc()[-1200:]), 'FAIL')
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
