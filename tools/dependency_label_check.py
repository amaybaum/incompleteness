#!/usr/bin/env python3
"""dependency_label_check.py - does a "(derived)" label cite a section that is
itself conditional?

Dependency labels do not update themselves. When an upstream result is scoped
to a named condition (H-slope, H-Hawking, ...), every downstream paragraph that
cites that section as its derivation keeps the label it had when the upstream
result was unconditional. claims_check cannot see this: it matches an
enumerated phrase list, and "(derived)" is not a wrong phrase, only a stale
one. The GR dark-sector chain shipped past a green gate in exactly this
state: Step 1 "(derived)" citing T_dS "derived, sec 3.2", after sec 3.2 had
become conditional. The same pattern was then found one level down (the
"Epistemic status" paragraph beneath the relabelled steps) and one level up
(sec 8.5 stating the Tier 1 universality theorem that sec 1 had already
retired).

Rule. For every file, a section CARRIES A CONDITION if its text (including
subsections) contains a named-condition token or the word "conditional". A
paragraph is a HIT if it (a) cites such a section, (b) uses derivation-
strength language about it, and (c) carries no conditionality marker of its
own. Paragraph scope, as in claims_check: a file-level or section-preamble
scope note does not rescue a later paragraph that re-asserts the result.

This is deliberately an over-approximation. A hit is either a stale label
(relabel it) or a paragraph whose scoping lives one paragraph away (restate
the condition where the claim sits). Both are the defect the guard exists to
find. Cross-file citations ([Main, sec 3.1]) are not resolved in this version.

Usage:  python3 tools/dependency_label_check.py [--root DIR] [--selftest] [--notes] [--strict]
Default is ADVISORY (hits printed, exit 0) while the inherited backlog is
worked down; --strict exits 1 on any hit and is the intended gate mode once
the count reaches zero. The self-test runs on every invocation.
The self-test exits 1 on failure regardless of mode.
"""
import os, re, sys

# Named conditions and hypotheses. A section containing one of these, or the
# scoping phrase "conditional on", is treated as carrying a condition. The bare
# word "conditional" is NOT enough: classification sections use it to define
# categories ("Class C, conditional structural") and citing such a section for
# a category is not citing it for a derivation. Add new names here when they
# are introduced: the guard knows an enumerated list, not meaning.
CONDITION_TOKENS = re.compile(
    r'\bH-(?:slope|frame|Hawking|balance|spectrum|scramble|shell|local-lift|'
    r'cone|top|det|Bell|link|spin|energy|state|theorem|cust|blind)\b'
    r'|\bconditional on\b|\bCONDITIONAL on\b')

# Status labels that assert derivation strength for what is cited. These GATE:
# a stale one of these is exactly the defect.
DERIVATION_GATE = re.compile(
    r'\(derived[\),;]|\bderived, not\b|\bTier [12]\b|\bEpistemic status\b|'
    r'\bparameter-free\b|\bunconditional(?:ly)?\b|\bthe proof is\b|'
    r'\bis a theorem\b|\|\s*exact\s*\|', re.I)

# Prose verbs of derivation. These are ADVISORY: reported as NOTE, never fail.
# They over-fire on adverbial "exactly" and negated "not a derivation of", so
# a human reads them; promote a phrase to DERIVATION_GATE once it has shipped
# a real stale label.
DERIVATION_NOTE = re.compile(
    r'\bis derived\b|\bare derived\b|\bderived from\b|\bderived in\b|'
    r'\bderives from\b|\bderivation of\b|\bfollows? (?:directly )?from\b|'
    r'\bproved in\b|\bestablished in\b|\btheorem of\b|\bexact(?:ly)?\b', re.I)

# A paragraph that carries one of these scopes its own claim locally.
LOCAL_MARKERS = re.compile(
    r'\bconditional\b|\bCONDITIONAL\b|\bconditional on\b|\bH-[A-Za-z][A-Za-z-]*\b|'
    r'\bimported\b|\bnot (?:presently )?derived\b|\bnot a proof\b|'
    r'\bassumption\b|\bpremise\b|\bopen\b|\bnamed condition|\bhypothes[ie]s\b|'
    r'\bwithdrawn\b|\bdoes not hold\b|\bdoes not follow\b|\brelative to\b|'
    r'\bCondition \d+\b|\bCond\.? ?\d+\b|\binherit|'
    r'\bempirically selected\b|\bpinned by observation\b|\bself-consistency strength\b')

HEADING = re.compile(r'^(#{1,4})\s+(\d+(?:\.\d+)*)\.?\s+\S', re.M)
CROSSREF = re.compile(r'\[[A-Z][A-Za-z]*,?\s*§[^\]]*\]')
CITE = re.compile(
    r'(?:§§?|\bSections?\s)\s*(\d+(?:\.\d+)*)'
    r'(?:\s*[–—-]\s*(?:§\s*)?(\d+(?:\.\d+)*))?'
    r'((?:\s*,\s*(?:and\s+)?\d+(?:\.\d+)*)*)')


def sections(text):
    """Map section id -> text span (heading to next heading of any level).
    A parent id with no heading of its own (e.g. '2' when only 2.1, 2.2
    exist) spans its subsections. Returns (spans, order)."""
    heads = [(m.start(), m.group(2)) for m in HEADING.finditer(text)]
    spans = {}
    for i, (pos, sid) in enumerate(heads):
        end = heads[i + 1][0] if i + 1 < len(heads) else len(text)
        spans.setdefault(sid, []).append((pos, end))
    # implied parents
    for sid in list(spans):
        parent = sid.rsplit('.', 1)[0]
        while '.' in sid and parent not in spans:
            spans.setdefault(parent, []).extend(spans[sid])
            sid, parent = parent, parent.rsplit('.', 1)[0] if '.' in parent else parent
    # parents span their children too
    for sid in list(spans):
        for other, sp in spans.items():
            if other.startswith(sid + '.'):
                spans[sid].extend(sp)
    return {k: sorted(set(v)) for k, v in spans.items()}


def section_text(text, spans, sid):
    return '\n'.join(text[a:b] for a, b in spans.get(sid, []))


def expand(sid_a, sid_b, known):
    """Expand a range §a–§b over the known ids at the same depth."""
    if not sid_b:
        return [sid_a]
    da, db = sid_a.count('.'), sid_b.count('.')
    if da != db:
        # '§7.1–7.3' style where b lacks the prefix is caught by equal depth;
        # '§3–§5' likewise. Mixed depth: take both endpoints only.
        return [sid_a, sid_b]
    def key(s): return tuple(int(x) for x in s.split('.'))
    lo, hi = key(sid_a), key(sid_b)
    out = [s for s in known if s.count('.') == da and lo <= key(s) <= hi]
    return out or [sid_a, sid_b]


def check_file(path, text, report, notes=None):
    spans = sections(text)
    if not spans:
        return 0
    conditional = {sid for sid in spans
                   if CONDITION_TOKENS.search(section_text(text, spans, sid))}
    hits = 0
    pos = 0
    for para in text.split('\n\n'):
        g = DERIVATION_GATE.search(para)
        n = None if g else DERIVATION_NOTE.search(para)
        if (g or n) and not LOCAL_MARKERS.search(para):
            cited = set()
            local = CROSSREF.sub(' ', para)
            for m in CITE.finditer(local):
                ids = expand(m.group(1), m.group(2), sorted(spans))
                for extra in re.findall(r'\d+(?:\.\d+)*', m.group(3) or ''):
                    ids.append(extra)
                cited.update(i for i in ids if i in spans)
            bad = sorted(cited & conditional)
            if bad:
                ln = text.count('\n', 0, pos) + 1
                d = g or n
                sep = ', \u00a7'
                msg = (f"{path}:{ln}  cites \u00a7{sep.join(bad)} "
                       f"(conditional) with '{d.group(0)}' and no local marker\n"
                       f"        ...{para[max(0, d.start()-70):d.start()+90].strip()}...")
                if g:
                    report.append("  STALE-LABEL " + msg)
                    hits += 1
                elif notes is not None:
                    notes.append("  NOTE        " + msg)
        pos += len(para) + 2
    return hits


def selftest():
    doc = """## 1. Intro

### 2.1 The temperature

The temperature T is conditional on H-frame and H-slope.

### 3.1 Unconditional counting

The count N = A/eps^2 holds exactly by construction.

### 4.1 Downstream

**Step 1 (derived).** From T (§2.1) we obtain the displacement.

**Step 2 (conditional on the above).** From T (§2.1, conditional) we obtain the scale.

**Step 3 (derived).** From the count (§3.1) we obtain the area law.

The chain follows from §§2, 3 together.

The proof is the §2–§3 derivations themselves.

A statement about sec 2.1 that merely discusses it without claiming derivation.

**Step 4 (derived).** This follows from [Other §2.1], a companion paper's section.
"""
    rep, notes = [], []
    n = check_file('selftest', doc, rep, notes)
    lines = [r.split('\n')[0] for r in rep]
    nlines = [r.split('\n')[0] for r in notes]
    want_flagged = ['selftest:13', 'selftest:21']   # Step 1 "(derived)", "§2–§3 ... proof is"
    want_noted = ['selftest:19']                    # "follows from §§2, 3" is advisory
    want_clean = ['selftest:15', 'selftest:17', 'selftest:23', 'selftest:25']  # Step 2, Step 3, discussion, cross-file
    ok = True
    for w in want_noted:
        if not any(w in l for l in nlines):
            print(f"  SELFTEST FAIL: expected a NOTE at {w}"); ok = False
        if any(w in l for l in lines):
            print(f"  SELFTEST FAIL: NOTE at {w} must not gate"); ok = False
    for w in want_flagged:
        if not any(w in l for l in lines):
            print(f"  SELFTEST FAIL: expected a hit at {w}"); ok = False
    for w in want_clean:
        if any(w in l for l in lines):
            print(f"  SELFTEST FAIL: unexpected hit at {w}"); ok = False
    if n != 2:
        print(f"  SELFTEST FAIL: expected 2 gating hits, got {n}"); ok = False
    print("dependency_label_check: self-test " + ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def main():
    if '--selftest' in sys.argv:
        return selftest()
    root = '.'
    if '--root' in sys.argv:
        root = sys.argv[sys.argv.index('--root') + 1]
    # self-test runs every time: a guard that cannot find its own synthetic
    # positive is not a guard
    if selftest():
        return 1
    report, notes, total, files = [], [], 0, 0
    for sub in ('papers', 'book'):
        d = os.path.join(root, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md') or f == 'The-Incompleteness-of-Observation-FULL.md':
                continue
            p = os.path.join(d, f)
            text = open(p, encoding='utf-8', errors='replace').read()
            files += 1
            total += check_file(p, text, report, notes)
    for r in report:
        print(r)
    if notes:
        print(f"\n  {len(notes)} advisory NOTE(s) (prose derivation verbs citing a "
              f"conditional section; not gating). Show with --notes.")
        if '--notes' in sys.argv:
            for r in notes:
                print(r)
    if total:
        strict = '--strict' in sys.argv
        print(f"\ndependency_label_check: {'FAILED' if strict else 'ADVISORY'} "
              f"({total} status label(s) cite a conditional section without a "
              f"local marker, {files} files)")
        return 1 if strict else 0
    print(f"dependency_label_check: OK (no stale dependency label, {files} files)"
          " -- promote to --strict in release_gate.py")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
