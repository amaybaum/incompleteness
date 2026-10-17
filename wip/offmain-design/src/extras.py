"""Collect sizes, control results, the not-retained list and the unrecoverable list into work/extras.json."""
import json, os, re

O = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(O, 'work')
R = lambda f: open(os.path.join(W, f)).read()
man = json.load(open(os.path.join(O, 'layout/verification/audits/evidence-retention/objects/manifest.json')))
E = man['objects']
forms = {}
for l in R('form-sizes.txt').split('\n'):
    m = re.match(r'(raw|zlib|hybrid) apparent bytes incl. manifest (\d+)', l)
    if m:
        forms.setdefault(m.group(1), {})['on_disk_bytes_incl_manifest'] = int(m.group(2))
    m = re.match(r'(raw|zlib|hybrid) pack default (\d+)  aggressive (\d+)', l)
    if m:
        forms[m.group(1)].update({'pack_bytes_default': int(m.group(2)), 'pack_bytes_window250': int(m.group(3))})
st = [e for e in E if e.get('file')]
sizes = {
    'stored_objects': len(st),
    'content_bytes_uncompressed': sum(e['content_bytes'] for e in st),
    'zlib_bytes_all_objects_as_loose': forms['zlib']['on_disk_bytes_incl_manifest'] - os.path.getsize(
        os.path.join(O, 'layout/verification/audits/evidence-retention/objects/manifest.json')),
    'hybrid_layout': {'raw_files': sum(1 for e in st if e['form'] == 'raw'),
                      'raw_bytes': sum(e['bytes'] for e in st if e['form'] == 'raw'),
                      'zlib_files': sum(1 for e in st if e['form'] == 'zlib'),
                      'zlib_bytes': sum(e['bytes'] for e in st if e['form'] == 'zlib'),
                      'manifest_bytes': os.path.getsize(os.path.join(O, 'layout/verification/audits/evidence-retention/objects/manifest.json'))},
    'forms': forms,
    'exact_object_pack_window250_bytes': os.path.getsize(os.path.join(W, 'exact-objects.pack')),
    'withheld_bytes': {'raw-log': sum(e['bytes'] for e in E if e['mechanism'] == 'withheld:raw-log'),
                       'build-pdf': sum(e['bytes'] for e in E if e['mechanism'] == 'withheld:build-pdf')},
    'for_comparison': {'main_checkout_bytes': 54793581, 'main_checkout_files': 1641, 'r1_archive_bytes': 4058560,
                       'main_history_pack_MiB': 527.48},
}
selftest = R('selftest.txt') if os.path.exists(os.path.join(W, 'selftest.txt')) else ''
controls = {
    'tree_mode': R('check-tree.txt').strip().split('\n')[:2],
    'history_mode': R('check-history.txt').strip().split('\n')[:3],
    'self_test': [l.rstrip() for l in selftest.split('\n') if l.strip() and not l.startswith(('real', 'user', 'sys'))],
    'independent_reconstitution': R('independent-control.txt').strip().split('\n'),
    'excerpt_controls_real_excerpts': json.load(open(os.path.join(W, 'excerpt-controls.json'))),
    'excerpt_injection_real_excerpts': R('inject-real.txt').strip().split('\n') + R('inject-head.txt').strip().split('\n')[:1],
    'og1_frozen_self_test': {'main_only': R('og1-mainonly.txt').strip().split('\n')[-1],
                             'main_plus_layout': R('og1-proto.txt').strip().split('\n')[-1]},
    'bg3_recorded_check_after_materialize': R('bg3-check-e3ef.txt').strip().split('\n'),
    'r1_check_retention_on_prototype': R('r1check-proto.txt').strip().split('\n')[-1],
    'host_by_sha_reprobe_of_refused': '24 of 24 still refused at ' + R('reprobe.time').strip(),
}
not_retained = {
    'withheld_objects': [{'oid': e['oid'], 'type': e['type'], 'mechanism': e['mechanism'], 'bytes': e['bytes'],
                          'paths': e.get('paths')} for e in E if not e.get('file')],
    'parents_named_not_retained': sorted({p for e in E for p in e.get('parents_not_retained', [])}),
    'chain_option': {'uncited_offmain_ancestors_of_raw_tree_commits': 38, 'commit_object_bytes': 38967,
                     'their_trees_and_blobs_beyond_the_plan': 186, 'content_bytes': 4093593, 'logs': 0, 'pdfs': 0},
}
unrec = [
    {'id': 'd5178e2fe0f1f1351168b689c9a3f7f4c9dfc465', 'what': 'GR-1 stage 1',
     'cited_at': ['verification/infrastructure/round-gr-1-roadmap-entry-scoping/amendments/amendment-1.md:52']},
    {'id': '70e34e82841074037409b12852694733a1ef458f', 'what': 'GR-1 stage 2',
     'cited_at': ['verification/infrastructure/round-gr-1-roadmap-entry-scoping/amendments/amendment-1.md:53']},
    {'id': '2a67dfcab4ba443ec3b980335ce0a59e1b3e4a3b', 'what': 'GR-1 attempt-1 candidate E',
     'cited_at': ['verification/infrastructure/round-gr-1-roadmap-entry-scoping/amendments/amendment-1.md:54',
                  'verification/infrastructure/round-gr-1-roadmap-entry-scoping/amendments/amendment-2.md:63',
                  'verification/infrastructure/round-gr-1-roadmap-entry-scoping/result.md:16']},
    {'id': '73f505974674e76b1bb425bc9f605ed5feab3a0f', 'what': 'GR-1 attempt-2 candidate landing',
     'cited_at': ['verification/infrastructure/round-gr-1-roadmap-entry-scoping/amendments/amendment-2.md:68',
                  'verification/infrastructure/round-gr-1-roadmap-entry-scoping/result.md:24']},
    {'id': '52009e086a3079b8c3bf50621d6f68d8f35c7530', 'what': "act 35's first frozen controls.py blob, superseded by amendment 1",
     'cited_at': ['verification/programmes/oi-qm/track-b/act-35-dita-hull/preregistration.md:1193',
                  'verification/programmes/oi-qm/track-b/act-35-dita-hull/amendments/amendment-1.md:128']},
    {'id': '46fb79d1e2cfaa47493d96184961c7bc90da7fbc', 'what': 'CV-2, "committed in scratch"',
     'cited_at': ['verification/infrastructure/round-cv-2-v1-retirement/amendments/amendment-1.md:82']},
    {'id': '7de2d549', 'what': '"claude/trb1-dev at 7de2d549" (abbreviated; not on that branch; the reference blob it names is on main)',
     'cited_at': ['verification/programmes/oi-qm/reconstruction/round-trb-1-transitive-body/preregistration.md:110']},
]
unresolvable_not_missing = [
    {'id': x['cited_id'], 'retained_as': x['retained_id'], 'cited_at': x['location'], 'run': x['run']}
    for x in man['id_discrepancies']] + [
    {'id': '0850281a', 'retained_as': '0850281082f0dd1cf2c6c906afa57726ab31b076', 'run': '37494787556',
     'cited_at': 'verification/programmes/oi-qm/reconstruction/round-k1-sharp-tests-1/preregistration.md:214',
     'note': 'abbreviation names no object; the run head (prefix 08502810) is retained as a branch-only run head'}]
json.dump({'sizes': sizes, 'controls': controls, 'not_retained': not_retained,
           'unrecoverable': {'host_refuses_and_no_local_copy': unrec,
                             'unresolvable_but_evidence_retained': unresolvable_not_missing,
                             'refused_external': '14: 12 action/toolchain SHAs in the retained BG-3 design log, Mathlib db584cd6, '
                                                 'prefix constant e07d4056',
                             'method': 'full SHA by git fetch from the host (2026-10-17) and eight-digit prefix by the '
                                       'commits API; all local object stores searched'}},
          open(os.path.join(W, 'extras.json'), 'w'), indent=1)
print(json.dumps(sizes, indent=1))
