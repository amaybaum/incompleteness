"""NP-AVG-1 Stage 0 Layer 2: the v8 authorization (certificate item 6).

The default refuses. A V8Grant (s0geom) and a RefGrant (s0ref) are issued only by
issue_grant, and only when every check of decide() passes on:
- the authorization artifact, a JSON file supplied outside the frozen tree (a dispatch
  input), whose fields name the exact commit, the manifest's code_digest, the
  configuration digest and the owner's designation; and
- the owner check, a JSON file the workflow writes from the host's API record of the
  designation comment (its author login and whether its body contains the required line),
  so that the author check reads structured host data (section A.44); and
- the facts of the checkout: HEAD's commit, a clean Layer-2 directory, the manifest
  verification and the configuration digest.

decide() is a pure function of those three inputs, so every refusal path is tested without
minting a grant (l2selftest L2-AUTH). No repository file other than this one constructs a
grant (static check L2-S1). A grant, or an owner-check file, can be forged in-process: the
lock prevents accidental runs, and the authoritative gates are the CI owner-check job and the
post-hoc re-verification of the designation at landing (l2landing.py). The engine and the
reference accept a grant only if its digests equal the running digests that l2cert.startup
binds after verifying the manifest.
"""
import json
import os
import subprocess

import l2config as CFG
import l2manifest as MAN

SCHEMA = 'np-avg-1/stage0/v8-authorization/1'
OWNER_SCHEMA = 'np-avg-1/stage0/v8-owner-check/1'
SCOPE = 'NP-AVG-1 Stage 0, k <= 2 enumeration of v8\'s configuration class under Layer 2 as frozen'
OWNER = 'amaybaum'
REPO_URL = 'https://github.com/amaybaum/incompleteness/'
ART_KEYS = {'schema', 'scope', 'commit', 'code_digest', 'config_sha256', 'owner', 'designation_url', 'designated_at'}
OWN_KEYS = {'schema', 'comment_url', 'author_login', 'body_sha256', 'body_contains_required_line', 'commit'}


def required_line(commit, code_digest):
    return 'NP-AVG-1 Stage 0 v8 enumeration authorized at %s code_digest %s' % (commit, code_digest)


def _hex(s, n):
    return type(s) is str and len(s) == n and all(c in '0123456789abcdef' for c in s)


def decide(art, own, facts):
    """'ok' or 'refused: <reason>'. art, own: parsed JSON objects or None; facts: dict with
    head_commit, tree_clean, manifest_ok, code_digest, config_sha256."""
    if art is None:
        return 'refused: no authorization artifact (default)'
    if type(art) is not dict or set(art) != ART_KEYS:
        return 'refused: artifact fields'
    if art['schema'] != SCHEMA:
        return 'refused: artifact schema'
    if art['scope'] != SCOPE:
        return 'refused: scope'
    if not _hex(art['commit'], 40):
        return 'refused: commit is not a full lowercase SHA-1'
    if art['commit'] != facts.get('head_commit'):
        return 'refused: commit is not the checked-out HEAD'
    if facts.get('tree_clean') is not True:
        return 'refused: Layer-2 directory differs from HEAD'
    if facts.get('manifest_ok') is not True:
        return 'refused: manifest verification failed (item 1)'
    if art['code_digest'] != facts.get('code_digest'):
        return 'refused: code_digest differs from the manifest'
    if art['config_sha256'] != facts.get('config_sha256'):
        return 'refused: configuration digest differs'
    if art['owner'] != OWNER:
        return 'refused: owner'
    if type(art['designation_url']) is not str or not art['designation_url'].startswith(REPO_URL):
        return 'refused: designation URL'
    if own is None:
        return 'refused: no owner check (host record of the designation)'
    if type(own) is not dict or set(own) != OWN_KEYS or own['schema'] != OWNER_SCHEMA:
        return 'refused: owner-check fields'
    if own['comment_url'] != art['designation_url']:
        return 'refused: owner check names another comment'
    if own['author_login'] != OWNER:
        return 'refused: designation not written by the owner'
    if own['commit'] != art['commit']:
        return 'refused: owner check names another commit'
    if own['body_contains_required_line'] is not True:
        return 'refused: designation lacks the required line'
    return 'ok'


def git_facts(code_dir):
    def git(*a):
        p = subprocess.run(['git', '-c', 'gc.auto=0', '-c', 'maintenance.auto=false', '-C', code_dir] + list(a),
                           capture_output=True, text=True)
        return p.returncode, p.stdout.strip()
    rc, head = git('rev-parse', 'HEAD')
    rc2, st = git('status', '--porcelain', '--untracked-files=all', '--', os.path.dirname(code_dir))
    ok, _, rec = MAN.verify(code_dir)
    return {'head_commit': head if rc == 0 else None, 'tree_clean': rc2 == 0 and st == '',
            'manifest_ok': ok, 'code_digest': rec.get('code_digest') if rec else None,
            'config_sha256': CFG.config_sha256()}


def _load(path):
    if not path:
        return None
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {'unreadable': True}


def issue_grant(art_path, own_path, code_dir):
    """(decision, V8Grant or None, RefGrant or None, echo). Mints only on 'ok'."""
    art, own = _load(art_path), _load(own_path)
    facts = git_facts(code_dir)
    decision = decide(art, own, facts)
    echo = {'decision': decision, 'artifact': art, 'owner_check': own, 'facts': facts}
    if decision != 'ok':
        return decision, None, None, echo
    import s0geom as G
    import s0ref as REF
    grant = G.V8Grant(art['commit'], facts['code_digest'], facts['config_sha256'], art['designation_url'])
    refgrant = REF.RefGrant(art['commit'], facts['code_digest'], facts['config_sha256'])
    return decision, grant, refgrant, echo
