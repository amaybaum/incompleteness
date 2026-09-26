"""Derive A32's guard-retirement splice ledger from the guard at D and write ledger.json plus the
retired guard. Each old span must occur exactly once in D's guard; nothing outside the ledger
changes. Usage: build_retire32.py <guard at D> <ledger.json> <retired guard>"""
import hashlib, json, sys

D = open(sys.argv[1], encoding='utf-8').read()
E = []


def once(s):
    assert D.count(s) == 1, s[:80]
    return s


# ---- R7-OGC (act 25)
E.append(('ogc-road-read', once("_OGCROAD = ' '.join(open(_artifact('ROADMAP.md'), encoding='utf-8').read().split())\n"), '',
          "R7-OGC's read of verification/ROADMAP.md, read only by its ROADMAP conjuncts and mutation"))
E.append(('ogc-p0-road-conjuncts', once(
    'def _ogc_p0(t=None, road=None):\n'
    '    """N10 -- the frozen P0 sentence for Case A, present VERBATIM in the note and in the ROADMAP\'s P0\n'
    '    row after act 24\'s sentence, the row\'s label staying OPEN."""\n'
    '    t = _OGC1 if t is None else t\n'
    '    road = _OGCROAD if road is None else road\n'
    '    p0, p0_ogs = _ogc_frozen(1476, 1476), _ogs_frozen(1385, 1385)\n'
    "    return (p0.startswith('Act 25 tests, in one gated round with four separately frozen targets')\n"
    '            and p0 in t and p0 in road and p0_ogs in road and road.find(p0_ogs) < road.find(p0)\n'
    "            and '| **P0** | What additional structure determines the relative quantum evolution OI leaves free | OI→QM / Track B | **OPEN**' in road\n"),
    'def _ogc_p0(t=None):\n'
    '    """N10 -- the frozen P0 sentence for Case A, present VERBATIM in the note."""\n'
    '    t = _OGC1 if t is None else t\n'
    '    p0 = _ogc_frozen(1476, 1476)\n'
    "    return (p0.startswith('Act 25 tests, in one gated round with four separately frozen targets')\n"
    '            and p0 in t\n',
    "R7-OGC's P0 predicate, less its ROADMAP parameter and its four ROADMAP conjuncts; its result-note "
    'conjuncts unchanged'))
E.append(('ogc-road-mut', once(
    "_ogc_m11 = _OGCROAD.replace(_ogc_frozen(1476, 1476), 'P0 is closed on its trajectory part.')\n"
    'ok_ogc &= _ogc_m11 != _OGCROAD and not _ogc_p0(road=_ogc_m11)                   # the P0 sentence absent from the ROADMAP\n'),
    '', "R7-OGC's ROADMAP mutation control"))
E.append(('ogc-description', once(
    "      \"relation and four-shape conclusion, and the import wired after act 24's; and the frozen P0 \"\n"
    "      \"sentence VERBATIM in the ROADMAP after act 24's.\")\n"),
    "      \"relation and four-shape conclusion, and the import wired after act 24's; and the frozen P0 \"\n"
    "      'sentence VERBATIM in the result note.')\n",
    "R7-OGC's check description, with the ROADMAP reading replaced by the result-note reading it keeps"))

# ---- R7-CGR (act 26)
E.append(('cgr-road-read', once("_CGRROAD = ' '.join(open(_artifact('ROADMAP.md'), encoding='utf-8').read().split())\n"), '',
          "R7-CGR's read of verification/ROADMAP.md, read only by its ROADMAP conjuncts and mutation"))
E.append(('cgr-p0-road-conjuncts', once(
    'def _cgr_p0(t=None, road=None):\n'
    '    """N10 -- the frozen P0 sentence for Case A with its one substitution, present VERBATIM in the note\n'
    '    and in the ROADMAP\'s P0 row after act 25\'s sentence, the row\'s label staying OPEN."""\n'
    '    t = _CGR1 if t is None else t\n'
    '    road = _CGRROAD if road is None else road\n'
    '    p0, p0_ogc = _cgr_p0_sentence(), _ogc_frozen(1476, 1476)\n'
    "    return (p0 is not None and p0.startswith('Act 26 tests, in one gated round with four separately frozen targets')\n"
    '            and p0 in t and p0 in road and p0_ogc in road and road.find(p0_ogc) < road.find(p0)\n'
    "            and '| **P0** | What additional structure determines the relative quantum evolution OI leaves free | OI→QM / Track B | **OPEN**' in road\n"),
    'def _cgr_p0(t=None):\n'
    '    """N10 -- the frozen P0 sentence for Case A with its one substitution, present VERBATIM in the\n'
    '    note."""\n'
    '    t = _CGR1 if t is None else t\n'
    '    p0 = _cgr_p0_sentence()\n'
    "    return (p0 is not None and p0.startswith('Act 26 tests, in one gated round with four separately frozen targets')\n"
    '            and p0 in t\n',
    "R7-CGR's P0 predicate, less its ROADMAP parameter and its four ROADMAP conjuncts; its result-note "
    'conjuncts unchanged'))
E.append(('cgr-road-mut', once(
    "_cgr_m11 = _CGRROAD.replace(_cgr_p0_sentence() or '\\0', 'P0 is closed on its trajectory part.')\n"
    'ok_cgr &= _cgr_m11 != _CGRROAD and not _cgr_p0(road=_cgr_m11)                   # the P0 sentence absent from the ROADMAP\n'),
    '', "R7-CGR's ROADMAP mutation control"))
E.append(('cgr-description', once(
    "      \"after act 25's; and the frozen P0 sentence with its one substitution VERBATIM in the \"\n"
    "      \"ROADMAP after act 25's.\")\n"),
    "      \"after act 25's; and the frozen P0 sentence with its one substitution VERBATIM in the \"\n"
    "      'result note.')\n",
    "R7-CGR's check description, with the ROADMAP reading replaced by the result-note reading it keeps"))

h = lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()
R = D
for name, old, new, why in E:
    assert R.count(old) == 1, name
    R = R.replace(old, new, 1)
json.dump([{'entry': n, 'reason': w, 'old': o, 'new': nw, 'old_sha256': h(o), 'new_sha256': h(nw)}
           for n, o, nw, w in E], open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(sys.argv[3], 'w', encoding='utf-8').write(R)
for n, o, nw, w in E:
    print(f'{n:24} old {h(o)[:12]}  new {h(nw)[:12]}  -{o.count(chr(10))} +{nw.count(chr(10))}')
