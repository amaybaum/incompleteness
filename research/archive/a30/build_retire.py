"""Derive A30's guard-retirement splice ledger from the guard at D, by anchors, and write
ledger.json plus the retired guard. Each old span must occur exactly once in D's guard."""
import hashlib, json, sys

D = open(sys.argv[1], encoding='utf-8').read()


def span(start, end):
    """The text from the line beginning `start` through the end of the line containing `end`
    (first occurrence after start), inclusive of the trailing newline."""
    i = D.index(start)
    assert D.count(start) == 1, start
    j = D.index(end, i) + len(end)
    j = D.index('\n', j - 1) + 1 if not end.endswith('\n') else j
    return D[i:j]


def line(prefix):
    i = D.index('\n' + prefix) + 1
    j = D.index('\n', i) + 1
    return D[i:j]


E = []

# ---- R7-PFR (act 28)
E.append(('pfr-road-standing', line('_PFR_ROAD_STANDING = '), '',
          "R7-PFR's ROADMAP standing-clause constant, read only by its ROADMAP leg"))
E.append(('pfr-p0', line('_PFR_P0 = '), '',
          "R7-PFR's frozen P0 sentence constant, read only by its ROADMAP leg"))
E.append(('pfr-p0-cell-and-road-ok',
          span('def _pfr_p0_cell(road):\n', '    return n.count(p0) == 1\n\n\n'), '',
          "the P0-cell reader (read only by R7-PFR's and R7-PRA's ROADMAP legs) and R7-PFR's "
          'ROADMAP gating predicate'))
E.append(('pfr-road-read', line('_PFRROAD = '), '', "R7-PFR's read of verification/ROADMAP.md"))
E.append(('pfr-road-leg',
          span("_pfr_checks['roadmap'] = _pfr_road_ok(_PFRROAD)\n",
               "    _pfr_checks['road-mut:' + _nm] = not _pfr_road_ok(_fn(_PFRROAD))\n"
               "    _pfr_mutations += 1\n\n"), '',
          "R7-PFR's ROADMAP check entry and its seven road-mut mutation controls"))
_old = span("check('R7-PFR', not _pfr_bad,\n", "'configuration and act 21 predicate verbatim.')\n")
_new = ("check('R7-PFR', not _pfr_bad,\n"
        "      'Act 28: the DECODED census entry read through ONE gating predicate that every '\n"
        "      'mutation is passed through. Each frozen requirement is pinned to its COMPLETE content, '\n"
        "      'not a heading: ten census records and the census clause in full. Mutations: a module '\n"
        "      'that gains a definition, each record deleted, the census clause truncated or '\n"
        "      'duplicated, and the census note re-escaped or its entry removed. PLACEMENT AND COUNT, '\n"
        "      'not only presence: exactly one mention of the census clause with that mention opening '\n"
        "      'the COMPLETE clause, with the census clause duplicated or given an incomplete second '\n"
        "      'copy failing closed. Twelve pinned statements each mutation-tested, the frozen '\n"
        "      'configuration and act 21 predicate verbatim.')\n")
E.append(('pfr-description', _old, _new,
          "R7-PFR's check description, less its statements that the ROADMAP cell is read"))

# ---- R7-PRA (act 29)
E.append(('pra-road-constants',
          line('_PRA_P0 = ') + line('_PRA_ROAD_STANDING = ') + line('_PRA_ROAD_ANCHOR = '), '',
          "R7-PRA's frozen P0 sentence, standing-clause and anchor constants, read only by its "
          'ROADMAP leg'))
E.append(('pra-road-ok',
          span('def _pra_road_ok(road):\n', '    return _pra_n(road).count(p0) == 1\n\n\n'), '',
          "R7-PRA's ROADMAP gating predicate"))
E.append(('pra-road-read', line('_PRAROAD = '), '', "R7-PRA's read of verification/ROADMAP.md"))
E.append(('pra-road-leg',
          span("_pra_checks['roadmap'] = _pra_road_ok(_PRAROAD)\n",
               "_pra_checks['road-successor-tolerated'] = _pra_road_ok(_PRAROAD.replace(\n"
               "    _PRA_P0 + ' ' + _PRA_ROAD_STANDING,\n"
               "    _PRA_P0 + ' ' + _PRA_ROAD_STANDING + ' A successor sentence. ' + _PRA_ROAD_STANDING, 1))\n"
               "_pra_mutations += 1\n\n"), '',
          "R7-PRA's ROADMAP check entry, its nine road-mut mutation controls and its "
          'road-successor-tolerated positive control'))
_old = span("check('R7-PRA', not _pra_bad,\n", "\"after act 28's. Six pinned statements each mutation-tested.\")\n")
_new = _old
for a, b in (
        ("'Act 29: the DECODED census entry and the ROADMAP cell each read through ONE gating '\n"
         "      'predicate that every mutation is passed through.",
         "'Act 29: the DECODED census entry read through ONE gating '\n"
         "      'predicate that every mutation is passed through."),
        ("      \"duplicated, fails in the census. The ROADMAP contract reads this round's BOUNDED ENTRY and \"\n"
         "      'tolerates a successor, with a positive control proving it. Each frozen requirement is '\n",
         "      'duplicated, fails in the census. Each frozen requirement is '\n"),
        ("      're-escaped or its entry removed, and the ROADMAP standing clause removed or detached. '\n",
         "      're-escaped or its entry removed. '\n"),
        ("      'mention opening the COMPLETE clause, and the frozen sentence read out of the ACTUAL P0 cell '\n"
         "      \"after act 28's. Six pinned statements each mutation-tested.\")\n",
         "      'mention opening the COMPLETE clause. Six pinned statements each mutation-tested.')\n")):
    assert _new.count(a) == 1, a
    _new = _new.replace(a, b)
E.append(('pra-description', _old, _new,
          "R7-PRA's check description, less its statements that the ROADMAP cell is read"))

out = D
ledger = []
for key, old, new, why in E:
    assert old and D.count(old) == 1, key
    assert out.count(old) == 1, key
    out = out.replace(old, new, 1)
    ledger.append({'id': key, 'old_sha256': hashlib.sha256(old.encode()).hexdigest(),
                   'old': old, 'new': new,
                   'new_sha256': hashlib.sha256(new.encode()).hexdigest(), 'reason': why})
for n in ('_pfr_p0_cell', '_PFR_ROAD_STANDING', '_PFR_P0', '_pfr_road_ok', '_PFRROAD', '_PRA_P0',
          '_PRA_ROAD_STANDING', '_PRA_ROAD_ANCHOR', '_pra_road_ok', '_PRAROAD'):
    assert n not in out, n
json.dump(ledger, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(sys.argv[3], 'w', encoding='utf-8').write(out)
print(len(ledger), 'splices;', D.count('\n') - out.count('\n'), 'lines removed')
