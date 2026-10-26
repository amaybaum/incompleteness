"""NP-AVG-1 Stage 0 Layer 2: post-hoc verification of the owner's designation at landing
(L2-R4 c; certificate item 6).

Usage: python3 -I -B l2landing.py --result result.json --fetched fetched.json
fetched.json is written by the landing (or evidence-retention) step from the host's API, at
landing time, for the comment the run's authorization names:
  {"schema": "np-avg-1/stage0/v8-designation-fetch/1", "comment_url": ..., "author_login": ...,
   "body_sha256": ..., "body_contains_required_line": true|false}
The check compares it with the owner check and the artifact echoed in result.json: the same
comment, written by the owner, with the same body SHA-256, containing the required line for the
run's commit and code_digest. It reads structured fields only (section A.44). Exit 0 iff the
designation verifies; otherwise it prints the reasons and exits 2, and the result does not land.
A grant or an owner-check file can be forged in-process; this re-fetch from the host is the
check that a forgery cannot pass.
"""
import json
import sys

OWNER = 'amaybaum'
FETCH_SCHEMA = 'np-avg-1/stage0/v8-designation-fetch/1'


def verify(result, fetched):
    """List of reasons the designation does not verify (empty when it does)."""
    why = []
    auth = (result or {}).get('authorization') or {}
    art, own = auth.get('artifact') or {}, auth.get('owner_check') or {}
    if auth.get('decision') != 'ok' or not art or not own:
        return ['result.json carries no granted authorization with its owner check']
    if not auth.get('ci_run'):
        why.append('result.json carries no CI run identity')
    if type(fetched) is not dict or fetched.get('schema') != FETCH_SCHEMA:
        return why + ['fetched designation: schema']
    if fetched.get('comment_url') != art.get('designation_url') or fetched.get('comment_url') != own.get('comment_url'):
        why.append('fetched comment is not the designated one')
    if fetched.get('author_login') != OWNER or own.get('author_login') != OWNER:
        why.append('designation not written by the owner')
    if fetched.get('body_sha256') != own.get('body_sha256'):
        why.append('designation body changed since the run, or the echoed owner check differs')
    if fetched.get('body_contains_required_line') is not True:
        why.append('designation lacks the required line')
    if own.get('commit') != art.get('commit') or result.get('commit') != art.get('commit'):
        why.append('commit differs between artifact, owner check and result')
    return why


def main():
    args = sys.argv[1:]
    with open(args[args.index('--result') + 1]) as f:
        result = json.load(f)
    try:
        with open(args[args.index('--fetched') + 1]) as f:
            fetched = json.load(f)
    except (OSError, ValueError):
        fetched = None
    why = verify(result, fetched)
    print(json.dumps({'designation_verified': not why, 'reasons': why}, sort_keys=True))
    sys.exit(0 if not why else 2)


if __name__ == '__main__':
    main()
