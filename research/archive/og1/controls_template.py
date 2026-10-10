#!/usr/bin/env python3
"""controls.py -- round OG-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the candidate blobs; mutation controls that
                                            must fail with their named codes

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  L   continuity  OrbitGeneration.lean is the frozen blob; its byte suffix from the first `import` has the frozen
                  SHA-256, which is the suffix of the design-validated draft (Thread L, blob e9722042)
  N1  decls       OrbitNormalization.lean declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every def/abbrev is the frozen
                  text whole -- a proof may change, a statement or definition may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide in either module; every frozen
                  `#print axioms` line present
  S1  4-ball      the countercontrol is a kernel theorem: `boundaryTransitive_ball4` and `finrank_E4` are theorems
                  with axiom prints, not probe output
  S2  dimension   only `finrank_E4` and the verdict mention `finrank`; no theorem has BoundaryTransitive among its
                  hypotheses and `finrank` in its conclusion
  S3  G-AUT       `preservesBody_words` has exactly one hypothesis, `PreservesBody` on the generators, and `words` is
                  the subgroup closure
  S4  transport   `hypotheses_tr` and `hypotheses_restrict` conclude all four named hypotheses of the transported
                  data (body, seed, automorphisms, available effects) together
  S5  no sourcing no theorem concludes SharpSeed, SeedOrbitAvailable or ElementaryDrivability without the same predicate
                  among its hypotheses; only the two named controls conclude BoundaryTransitive without it; no
                  declaration name or header claims a source for the ellipsoid, the drive, dimension three, SC∞, ELEM
                  or V4′
  I   imports     OIBridge.lean is D's with exactly the two frozen import lines after `import OIBridge.KInfFoundations`
  C   census      the census is D's with exactly the frozen family inserted after the KINF-2 family
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import hashlib, json, re, subprocess, sys

D = '6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-og-1-orbit-generation/'
PREREG = RDIR + 'preregistration.md'
OG = 'verification/lean-mathlib/OIBridge/OrbitGeneration.lean'
ON = 'verification/lean-mathlib/OIBridge/OrbitNormalization.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {OG: 'A', ON: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
L_DRAFT_BLOB = 'e9722042c2fc076ef292cbdb6d800a591ff71eb4'
OG_BLOB = '@@OG_BLOB@@'
ON_REFERENCE_BLOB = '@@ON_BLOB@@'
OG_SUFFIX_SHA256 = '@@OG_SUFFIX@@'
IMPORT_LINES = 'import OIBridge.KInfFoundations\nimport OIBridge.OrbitGeneration\nimport OIBridge.OrbitNormalization\n'
CENSUS_FAMILY = json.loads(r'''@@CENSUS_FAMILY@@''')
KINF2_FAMILY_PREFIX = 'the corrected field-neutral vocabulary of the pre-quantum completion'
ON_DECLS = json.loads(r'''@@ON_DECLS@@''')
ON_TEXTS = json.loads(r'''@@ON_TEXTS@@''')
ON_PRINTS = json.loads(r'''@@ON_PRINTS@@''')
NAMED = ('PreservesBody', 'SharpSeed', 'BoundaryTransitive', 'SeedOrbitAvailable')
CONTROL_TRANSITIVE = {'boundaryTransitive_ball3Drive', 'boundaryTransitive_ball4'}
CONTROL_PRESERVES = {'preservesBody_driveWords', 'preservesBody_driveWords3', 'preservesBody_isom4'}
VERDICT = 'og1_infrastructure_core'
SOURCING_NAME = re.compile(r'(substratum|ellipsoid|scInf|SCInf|stageConsist|ELEM|elementaryDrivability_of|'
                           r'dim(ension)?Three|sourced|seedOrbitAvailable_of|sharpSeed_of_stage)')
SOURCING_PROSE = re.compile(r'(OI (supplies|derives|sources)|is sourced|are sourced by|derives? the drive|'
                            r'sources? (the|a) (seed|drive|dimension))', re.I)
DISCLAIMER_ON = 'Nothing here is a hypothesis about OI.'
DISCLAIMER_OG = 'proved\n  nowhere in the corpus'

DECL = re.compile(r'^(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure|instance)\s+(\S+)',
                  re.M)
FAILS, COUNT = [], [0]


def check(code, name, cond):
    COUNT[0] += 1
    print(('  PASS  ' if cond else '  FAIL  ') + code + ' ' + name, flush=True)
    if not cond:
        FAILS.append(code)


def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True)


def show(commit, path):
    r = git('show', '%s:%s' % (commit, path))
    return r.stdout if r.returncode == 0 else None


def blob(text):
    data = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def suffix_sha(text):
    i = text.index('\nimport ') + 1
    return hashlib.sha256(text[i:].encode('utf-8')).hexdigest()


def decls(text):
    return [(m.group(1), m.group(2)) for m in DECL.finditer(text)]


def decl_texts(text):
    """theorem/lemma: signature up to the first ' :=' ; def/abbrev/structure/instance: the declaration whole, up to
    the next blank line followed by a doc comment, a section marker, a declaration, '#print' or 'end'."""
    out = {}
    ms = list(DECL.finditer(text))
    for k, m in enumerate(ms):
        start = m.start()
        nxt = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        chunk = text[start:nxt]
        for stop in ('\n/--', '\n/-!', '\n#print', '\nend '):
            j = chunk.find(stop)
            if j != -1:
                chunk = chunk[:j]
        chunk = chunk.rstrip()
        if m.group(1) in ('theorem', 'lemma'):
            j = chunk.find(' :=')
            chunk = chunk[:j] if j != -1 else chunk
        out[m.group(2)] = chunk
    return out


def split_statement(stmt):
    """(binders, conclusion) at the first colon at bracket depth 0 after the name."""
    i = len(stmt.split(None, 2)[0]) + 1 + len(stmt.split(None, 2)[1])
    depth = 0
    for j in range(i, len(stmt)):
        c = stmt[j]
        if c in '({[⦃':
            depth += 1
        elif c in ')}]⦄':
            depth -= 1
        elif c == ':' and depth == 0 and stmt[j:j + 2] != ':=':
            return stmt[i:j], stmt[j + 1:]
    return stmt[i:], ''


def code_only(text):
    text = re.sub(r'/-.*?-/', ' ', text, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', text)


def module_checks(og, on, tag=''):
    check('L', 'OrbitGeneration is the frozen blob' + tag, og is not None and blob(og) == OG_BLOB)
    check('L', 'OrbitGeneration suffix from the first import is the design-validated suffix' + tag,
          og is not None and suffix_sha(og) == OG_SUFFIX_SHA256)
    if on is None:
        check('N1', 'OrbitNormalization present' + tag, False)
        return
    check('N1', 'OrbitNormalization declares exactly the frozen declarations' + tag,
          [list(x) for x in decls(on)] == ON_DECLS)
    texts = decl_texts(on)
    bad = sorted(n for n in ON_TEXTS if texts.get(n) != ON_TEXTS[n])
    check('N2', 'every frozen statement and definition unchanged%s%s' % (tag, (' (changed: %s)' % ', '.join(bad[:4]))
                                                                        if bad else ''), not bad)
    for name, text in (('OrbitGeneration', og or ''), ('OrbitNormalization', on)):
        c = code_only(text)
        check('N3', '%s has no sorry, admit, axiom or native_decide%s' % (name, tag),
              not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M))
    prints = re.findall(r'^#print axioms (\S+)', on, re.M)
    check('N3', 'every frozen #print axioms line present' + tag, all(p in prints for p in ON_PRINTS))
    kinds = dict((n, k) for k, n in decls(on))
    check('S1', 'the 4-ball countercontrol is a kernel theorem with axiom prints' + tag,
          kinds.get('boundaryTransitive_ball4') == 'theorem' and kinds.get('finrank_E4') == 'theorem'
          and 'OIBridge.OrbitNormalization.boundaryTransitive_ball4' in prints
          and 'OIBridge.OrbitNormalization.finrank_E4' in prints)
    fin = sorted(n for n, t in texts.items() if 'finrank' in t)
    dimbad = [n for n, t in texts.items() if kinds.get(n) in ('theorem', 'lemma')
              and 'BoundaryTransitive' in split_statement(t)[0] and 'finrank' in split_statement(t)[1]]
    check('S2', 'only finrank_E4 and the verdict mention finrank; no transitivity-to-dimension statement' + tag,
          fin == sorted(['finrank_E4', VERDICT]) and not dimbad)
    pbw = texts.get('preservesBody_words', '')
    b, c = split_statement(pbw) if pbw else ('', '')
    check('S3', 'preservesBody_words: one PreservesBody hypothesis on the generators, words = subgroup closure' + tag,
          b.count('PreservesBody') == 1 and not any(p in b for p in NAMED if p != 'PreservesBody')
          and c.strip() == 'PreservesBody Ω (words S)'
          and 'Subgroup.closure S' in texts.get('words', ''))
    ok4 = True
    for n, objs in (('hypotheses_tr', ('conjTr T', 'effTr T r', 'T \'\' Ω', 'effTr T \'\' avail')),
                    ('hypotheses_restrict', ('autR L p0 G', 'effR L p0 r', 'bodyR L p0 Ω', 'effR L p0 \'\' avail'))):
        bb, cc = split_statement(texts.get(n, n + ' : '))
        ok4 = ok4 and all(p in cc for p in NAMED) and all(o in cc for o in objs) and all(p in bb for p in NAMED)
    check('S4', 'the transport theorems carry body, seed, automorphisms and available effects together' + tag, ok4)
    viol = []
    for n, t in texts.items():
        if kinds.get(n) not in ('theorem', 'lemma') or n == VERDICT:
            continue
        bb, cc = split_statement(t)
        for p in ('SharpSeed', 'SeedOrbitAvailable', 'ElementaryDrivability'):
            if p in cc and p not in bb and not (p == 'ElementaryDrivability' and 'IsEmpty' in cc):
                viol.append((n, p))
        if 'BoundaryTransitive' in cc and 'BoundaryTransitive' not in bb and n not in CONTROL_TRANSITIVE:
            viol.append((n, 'BoundaryTransitive'))
        if 'PreservesBody' in cc and 'PreservesBody' not in bb and n not in CONTROL_PRESERVES:
            viol.append((n, 'PreservesBody'))
    names = [n for _, n in decls(on)] + [n for _, n in decls(og or '')]
    hdr_on = on[:on.index('-/')]
    hdr_og = (og or '')[:(og or '-/').index('-/')]
    check('S5', 'no sourcing conclusion, name or header claim%s%s' % (tag, (' %s' % viol[:3]) if viol else ''),
          not viol and not any(SOURCING_NAME.search(n) for n in names)
          and not SOURCING_PROSE.search(hdr_on) and not SOURCING_PROSE.search(hdr_og)
          and DISCLAIMER_ON in hdr_on and DISCLAIMER_OG in hdr_og)


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and \
        e_text == d_text.replace('import OIBridge.KInfFoundations\n', IMPORT_LINES, 1) and \
        d_text.count('import OIBridge.KInfFoundations\n') == 1


def census_ok(d_text, e_text):
    try:
        d, e = json.loads(d_text), json.loads(e_text)
    except Exception:
        return False
    fam = d['families']
    k = [i for i, f in enumerate(fam) if f['name'].startswith(KINF2_FAMILY_PREFIX)]
    if len(k) != 1:
        return False
    want = dict(d)
    want['families'] = fam[:k[0] + 1] + [CENSUS_FAMILY] + fam[k[0] + 1:]
    return e == want


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    module_checks(show(commit, OG), show(commit, ON))
    check('I', 'OIBridge.lean is D\'s with exactly the two frozen import lines', imports_ok(show(D, IMPORTS),
                                                                                         show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family', census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def self_test():
    og = git('cat-file', '-p', OG_BLOB).stdout
    on = git('cat-file', '-p', ON_REFERENCE_BLOB).stdout
    draft = git('cat-file', '-p', L_DRAFT_BLOB).stdout
    check('T', 'the candidate blobs and the draft blob are readable', bool(og) and bool(on) and bool(draft))
    check('T', 'the frozen suffix digest is the design-validated draft\'s suffix', suffix_sha(draft) == OG_SUFFIX_SHA256)
    check('T', 'the draft blob is not the landed blob (only the header differs)', blob(draft) != OG_BLOB)
    module_checks(og, on, ' [candidate]')
    base = len(FAILS)

    def must_fail(code, label, og2, on2):
        before = list(FAILS)
        sys.stdout_backup = sys.stdout
        import io
        sys.stdout = io.StringIO()
        try:
            module_checks(og2, on2)
        finally:
            sys.stdout = sys.stdout_backup
        new = FAILS[len(before):]
        del FAILS[len(before):]
        check('M', 'mutation %s fails with %s' % (label, code), code in new)

    must_fail('L', 'OrbitGeneration body byte', og.replace('theorem seedOrbit_ball3_eq',
                                                           'theorem seedOrbit_ball3_eq ', 1), on)
    must_fail('L', 'OrbitGeneration header', og.replace('round OG-1', 'round OG-2', 1), on)
    must_fail('N1', 'a removed declaration', og, re.sub(r'\ntheorem finrank_E4[^\n]*\n', '\n', on, 1))
    must_fail('N2', 'a strengthened statement', og,
              on.replace('(hK : BoundaryTransitive Ω G) :\n    seedOrbit G r =',
                         '(hK : BoundaryTransitive Ω G) (h3 : True) :\n    seedOrbit G r =', 1))
    must_fail('N2', 'a changed definition', og, on.replace('(Subgroup.closure S : Set', '(Subgroup.closure (S ∪ S) : Set', 1))
    must_fail('N3', 'a sorry', og, on.replace('  refine ⟨fun D => ?_⟩', '  sorry\n  refine ⟨fun D => ?_⟩', 1))
    must_fail('S2', 'a transitivity-to-dimension theorem', og,
              on.replace('\nend OrbitNormalization',
                         '\ntheorem dim_of_bt {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (h : BoundaryTransitive Ω G) :'
                         '\n    Module.finrank ℝ V = 3 := sorry\n\nend OrbitNormalization', 1))
    must_fail('S5', 'a sourcing conclusion', og,
              on.replace('\nend OrbitNormalization',
                         '\ntheorem seed_free {Ω : Set V} (r : V →ᵃ[ℝ] ℝ) : SharpSeed Ω r := sorry'
                         '\n\nend OrbitNormalization', 1))
    must_fail('S5', 'a sourcing name', og,
              on.replace('\nend OrbitNormalization', '\ntheorem ellipsoid_of_drive : True := trivial'
                         '\n\nend OrbitNormalization', 1))
    must_fail('S3', 'a stronger G-AUT premise', og,
              on.replace('theorem preservesBody_words {Ω : Set V} {S : Set (V ≃ᵃ[ℝ] V)} (h : PreservesBody Ω S) :',
                         'theorem preservesBody_words {Ω : Set V} {S : Set (V ≃ᵃ[ℝ] V)} (h : PreservesBody Ω S)'
                         ' (h2 : BoundaryTransitive Ω S) :', 1))
    must_fail('S1', 'the 4-ball control demoted', og, on.replace('theorem boundaryTransitive_ball4',
                                                                 'def boundaryTransitive_ball4', 1))
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace('import OIBridge.KInfFoundations\n', IMPORT_LINES, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, good_imp.replace('import OIBridge.OrbitNormalization\n',
                                                                                 '', 1)))
    d_cen = show(D, CENSUS)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['name'].startswith(KINF2_FAMILY_PREFIX)][0]
    good = dict(dd)
    good['families'] = dd['families'][:k + 1] + [CENSUS_FAMILY] + dd['families'][k + 1:]
    bad = json.loads(json.dumps(good))
    bad['families'][k + 1]['status'] = 'carried'
    check('M', 'census: the frozen family passes and a changed status fails',
          census_ok(d_cen, json.dumps(good)) and not census_ok(d_cen, json.dumps(bad)))
    return base


def main(argv):
    if argv == ['--self-test']:
        self_test()
    elif len(argv) >= 2 and argv[0] == 'check':
        freeze = argv[3] if len(argv) == 4 and argv[2] == '--freeze' else None
        run_check(argv[1], freeze)
    else:
        print(__doc__)
        return 2
    if FAILS:
        print('controls: FAILED (%d of %d): %s' % (len(FAILS), COUNT[0], ' '.join(FAILS)))
        return 1
    print('controls: OK -- %d checks' % COUNT[0])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
