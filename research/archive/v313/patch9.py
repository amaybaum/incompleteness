p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/wt/tools/legacy_records_check.py'
t = open(p).read()
for old, new in (
("""def _round_case(sc, blobs, governed):
    \"\"\"A native round from B that rewrites a record and the manifest; the check at its receipt
    commit.\"\"\"
    tag = 'G' if governed else 'N'
""",
"""def _round_case(sc, blobs, governed, holds=True):
    \"\"\"A native round from B that rewrites a record and the manifest; the check at its receipt
    commit. `holds` False records a wrong execution delta digest, so the receipt does not hold.\"\"\"
    tag = ('G' if governed else 'N') + ('' if holds else 'X')
"""),
("""        'execution_delta_digest': '{{delta:%sF|%sE}}' % (tag, tag), 'candidates': [],
""",
"""        'execution_delta_digest': '{{delta:%sF|%sE}}' % (tag, tag) if holds else '0' * 64,
        'candidates': [],
"""),
("""            # a native round that governs the manifest changes a record and the population
            # together: admitted once its receipt holds; the same round without the manifest in
            # its governed paths is not
            for governed, want in ((True, True), (False, False)):
                if not _round_case(sc, blobs, governed) is want:
                    fails.append('native round, manifest %sgoverned' % ('' if governed else 'not '))
""",
"""            # a native round that governs the manifest changes a record and the population
            # together: admitted once its receipt holds; the same round without the manifest in
            # its governed paths is not, and neither is the governing round whose receipt fails
            for governed, holds, want in ((True, True, True), (False, True, False),
                                          (True, False, False)):
                if not _round_case(sc, blobs, governed, holds) is want:
                    fails.append('native round, manifest %sgoverned, receipt %s' % (
                        '' if governed else 'not ', 'holding' if holds else 'failing'))
"""),
):
    assert t.count(old) == 1, old[:60]
    t = t.replace(old, new)
open(p, 'w').write(t)
