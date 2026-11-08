"""Check draft patch bytes without importing or executing candidate programs.

This is a staging audit, not controls.py, a fixture harness, or a freeze gate.
Only the single-hunk, one-file patches in this package are accepted.
"""

import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess


def digest(data):
    return hashlib.sha256(data).hexdigest()


def apply_exact(source, patch, target):
    """Splice one hunk at its declared position, without offset or fuzz."""
    lines = patch.decode('utf-8').splitlines(keepends=True)
    if len(lines) < 4 or lines[:2] != ['--- a/' + target + '\n', '+++ b/' + target + '\n']:
        raise ValueError('headers')
    match = re.fullmatch(r'@@ -(\d+),(\d+) \+(\d+),(\d+) @@\n', lines[2])
    if match is None:
        raise ValueError('hunk header')
    old_start, old_count, new_start, new_count = map(int, match.groups())
    if old_start < 1 or new_start != old_start:
        raise ValueError('hunk position')
    old, new = [], []
    for line in lines[3:]:
        if not line.endswith('\n') or line[:1] not in (' ', '-', '+'):
            raise ValueError('hunk line')
        if line[0] in ' -':
            old.append(line[1:])
        if line[0] in ' +':
            new.append(line[1:])
    if len(old) != old_count or len(new) != new_count:
        raise ValueError('hunk counts')
    original = source.decode('utf-8').splitlines(keepends=True)
    at = old_start - 1
    if original[at:at + old_count] != old:
        raise ValueError('exact context')
    return ''.join(original[:at] + new + original[at + old_count:]).encode('utf-8')


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def main():
    package = Path(__file__).resolve().parent
    repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=package).decode().strip())
    manifest = json.loads((package / 'manifest.json').read_bytes())
    require(manifest['status'] == 'PROVISIONAL_AGAINST_UNREVISED_DRAFTS', 'status')
    require(manifest['final_freeze_pins'] is False, 'not final pins')
    require(manifest['candidate_code_executed'] is False, 'static scope')
    require([e['id'] for e in manifest['entries']] == ['MU-C1', 'MU-C2', 'MU-C3'], 'roster')
    results = []
    for entry in manifest['entries']:
        blob = subprocess.check_output(['git', 'rev-parse', entry['source_commit'] + ':' + entry['target']], cwd=repo).decode().strip()
        require(blob == entry['source_blob'], 'source blob')
        source = subprocess.check_output(['git', 'cat-file', 'blob', blob], cwd=repo)
        patch = (repo / entry['patch']).read_bytes()
        require(digest(source) == entry['source_sha256'], 'source hash')
        require(digest(patch) == entry['patch_sha256'], 'patch hash')
        changed = apply_exact(source, patch, entry['target'])
        old, new = entry['old_text'].encode(), entry['new_text'].encode()
        require(source.count(old) == 1, 'unique edit site')
        require(changed == source.replace(old, new, 1), 'only intended text edit')
        require(digest(changed) == entry['patched_sha256'], 'patched hash')
        ast.parse(source)
        ast.parse(changed)

        # Negative tests of patch mechanics only. These are not MU-C kill tests.
        lines = patch.splitlines(keepends=True)
        header = re.fullmatch(rb'@@ -(\d+),(\d+) \+(\d+),(\d+) @@\n', lines[2])
        a, b, c, d = map(int, header.groups())
        cases = {
            'wrong_target': (source, patch.replace(('--- a/' + entry['target']).encode(), b'--- a/other.py', 1)),
            'old_offset': (source, b''.join(lines[:2] + [('@@ -%d,%d +%d,%d @@\n' % (a + 1, b, c + 1, d)).encode()] + lines[3:])),
            'new_offset': (source, b''.join(lines[:2] + [('@@ -%d,%d +%d,%d @@\n' % (a, b, c + 1, d)).encode()] + lines[3:])),
            'count_mismatch': (source, b''.join(lines[:2] + [('@@ -%d,%d +%d,%d @@\n' % (a, b + 1, c, d)).encode()] + lines[3:])),
            'truncated': (source, b''.join(lines[:-1])),
            'extra_header': (source, patch + b'--- a/extra.py\n'),
            'changed_context': (b'# shifted source\n' + source, patch),
            'missing_final_lf': (source, patch[:-1]),
        }
        rejected = []
        for name, (test_source, test_patch) in cases.items():
            try:
                apply_exact(test_source, test_patch, entry['target'])
            except ValueError:
                rejected.append(name)
            else:
                raise ValueError('accepted malformed patch: ' + name)
        results.append(dict(id=entry['id'], exact_application=True,
                            intended_edit_only=True, syntax=True,
                            malformed_patch_controls_rejected=rejected))
    print(json.dumps(dict(schema='k1p1-draft-patch-static-validation', version=1,
                         status='STATIC_PASS', final_freeze_pins=False,
                         candidate_code_executed=False,
                         mutation_kills_tested=False, entries=results), indent=2) + '\n', end='')


if __name__ == '__main__':
    main()
