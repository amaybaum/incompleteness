"""Check draft patch bytes without importing or executing candidate programs.

This is a staging audit, not controls.py, a fixture harness, or a freeze gate.
Only the exact one-file patches in this package are accepted.
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
    """Splice ordered hunks at their declared positions, without offset or fuzz."""
    lines = patch.decode('utf-8').splitlines(keepends=True)
    if len(lines) < 4 or lines[:2] != ['--- a/' + target + '\n', '+++ b/' + target + '\n']:
        raise ValueError('headers')
    original = source.decode('utf-8').splitlines(keepends=True)
    result, cursor, index = [], 0, 2
    while index < len(lines):
        match = re.fullmatch(r'@@ -(\d+),(\d+) \+(\d+),(\d+) @@\n', lines[index])
        if match is None:
            raise ValueError('hunk header')
        old_start, old_count, new_start, new_count = map(int, match.groups())
        at = old_start - 1
        if at < cursor or at > len(original) or old_count < 1:
            raise ValueError('hunk position')
        result.extend(original[cursor:at])
        if new_start != len(result) + 1:
            raise ValueError('new position')
        index += 1
        old, new = [], []
        while index < len(lines) and not lines[index].startswith('@@'):
            line = lines[index]
            if not line.endswith('\n') or line[:1] not in (' ', '-', '+'):
                raise ValueError('hunk line')
            if line[0] in ' -':
                old.append(line[1:])
            if line[0] in ' +':
                new.append(line[1:])
            index += 1
        if len(old) != old_count or len(new) != new_count:
            raise ValueError('hunk counts')
        if original[at:at + old_count] != old:
            raise ValueError('exact context')
        result.extend(new)
        cursor = at + old_count
    return ''.join(result + original[cursor:]).encode('utf-8')


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def main():
    package = Path(__file__).resolve().parent
    repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=package).decode().strip())
    manifest = json.loads((package / 'manifest.json').read_bytes())
    require(manifest['status'] == 'REVIEWED_PRE_F_CANDIDATES_NOT_FROZEN', 'status')
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
    workflow = manifest['workflow_proposal']
    source = subprocess.check_output(['git', 'show', workflow['source_commit'] + ':' + workflow['target']], cwd=repo)
    blob = subprocess.check_output(['git', 'rev-parse', workflow['source_commit'] + ':' + workflow['target']], cwd=repo).decode().strip()
    patch = (repo / workflow['patch']).read_bytes()
    require(blob == workflow['source_blob'] and digest(source) == workflow['source_sha256'], 'workflow source')
    require(digest(patch) == workflow['patch_sha256'], 'workflow patch hash')
    changed = apply_exact(source, patch, workflow['target'])
    expected = source
    for edit in workflow['edits']:
        old, new = edit['old_text'].encode(), edit['new_text'].encode()
        require(expected.count(old) == 1, 'workflow unique edit')
        expected = expected.replace(old, new, 1)
    require(changed == expected and digest(changed) == workflow['patched_sha256'], 'workflow exact edits')
    require(workflow['applied_to_workflow'] is False, 'workflow remains proposal')
    print(json.dumps(dict(schema='k1p1-draft-patch-static-validation', version=2,
                         status='STATIC_PASS', final_freeze_pins=False,
                         candidate_code_executed=False,
                         mutation_kills_tested=False, entries=results,
                         workflow_proposal=dict(exact_application=True, intended_edits_only=True,
                                                workflow_changed=False)), indent=2) + '\n', end='')


if __name__ == '__main__':
    main()
