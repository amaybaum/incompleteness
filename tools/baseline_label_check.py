#!/usr/bin/env python3
"""baseline_label_check.py — does any doc name a superseded baseline archive?

Twice a transfer shipped with NEXT-SESSION.md rewritten to the new state while
README.md still named an older baseline. staleness_check.py cannot see this: it
compares sources against builds, not documents against each other.

Method: collect every `...-bNNN....zip` reference, grouped by archive family
(`incompleteness-dev` and `OI_session_transfer` are numbered independently).
Within each family the highest NNN is taken as current; anything strictly older
is flagged, unless it sits under a heading marked Historical — which is STICKY,
so subheadings inside a provenance section do not reset it.

Usage:  python3 baseline_label_check.py [--root DIR]
Exit 1 if a superseded baseline is named outside a historical section.
"""
import os, re, sys

ARCHIVE = re.compile(r'\b(incompleteness-dev|OI_session_transfer)[-\w]*?-b(\d+)[-\w]*\.zip')
HIST = re.compile(r'^#{1,6}\s.*\bHistorical\b', re.I)

def refs(path):
    """(family, number, line_no, text, in_historical) for each reference."""
    out, historical = [], False
    for n, l in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
        if l.startswith('#') and HIST.match(l):
            historical = True                      # sticky to end of file
        for m in ARCHIVE.finditer(l):
            out.append((m.group(1), int(m.group(2)), n, m.group(0), historical))
    return out

def main():
    root = '.'
    if '--root' in sys.argv:
        root = sys.argv[sys.argv.index('--root') + 1]
    found = []
    for dp, _, fs in os.walk(root):
        if os.sep + 'notes' in dp or os.sep + 'proposals' in dp:
            continue
        for f in sorted(fs):
            if f.endswith(('.md', '.txt')):
                p = os.path.join(dp, f)
                for r in refs(p):
                    found.append((p,) + r)
    if not found:
        print("baseline_label_check: OK (no baseline archives named)")
        return 0
    current = {}
    for _, fam, num, _, _, _ in found:
        current[fam] = max(current.get(fam, 0), num)
    # STRICT MODE. Without it the check only detects docs disagreeing with each
    # other; a tree where EVERY doc names the same superseded baseline passes.
    # That is exactly how a stale README survived two rounds. --label pins the
    # expected current number and fails if the tree's maximum is behind it.
    if '--label' in sys.argv:
        want = int(sys.argv[sys.argv.index('--label') + 1].lstrip('bB'))
        for fam in list(current):
            if current[fam] < want:
                print(f"  BEHIND  {fam}: tree names b{current[fam]}, "
                      f"expected b{want}")
                current[fam] = want
    for fam, num in sorted(current.items()):
        print(f"  current {fam}: b{num}")
    bad = [(p, a, ln) for p, fam, num, ln, a, hist in found
           if num < current[fam] and not hist]
    for p, a, ln in bad:
        print(f"  STALE-LABEL {p}:{ln}  names {a}")
    if bad:
        print(f"\nbaseline_label_check: FAILED ({len(bad)} superseded reference(s) "
              f"outside a 'Historical' section)")
        return 1
    print(f"baseline_label_check: OK ({len(found)} references, all current or "
          f"historical)")
    return 0

def verify_checksum(argv):
    """Verify a shipped archive against CURRENT declarations of that exact
    archive basename in the transfer docs.

    Historical sections are ignored.  A declaration may put the archive name
    and SHA-256 on separate lines of the same Markdown paragraph.  At least one
    current declaration is required; every current declaration must match.

    A transfer ZIP cannot stably contain its own whole-file SHA-256.  Its hash
    is therefore a detached release checksum and is not verified from inside
    that same archive.
    """
    import hashlib, re as _re
    path = argv[argv.index('--verify-archive') + 1]
    root = '.'
    if '--root' in argv:
        root = argv[argv.index('--root') + 1]
    actual = hashlib.sha256(open(path, 'rb').read()).hexdigest()
    base = os.path.basename(path)
    declarations = []

    for dp, _, fs in os.walk(root):
        for f in sorted(fs):
            if not f.endswith(('.md', '.txt')):
                continue
            fp = os.path.join(dp, f)
            lines = open(fp, encoding='utf-8', errors='replace').read().splitlines()
            historical = False
            para = []
            para_start = 1

            def flush_paragraph(buf, start_line, hist):
                if not buf or hist:
                    return
                block = '\n'.join(buf)
                if base not in block:
                    return
                hashes = _re.findall(r'\b([0-9a-f]{64})\b', block)
                for h in hashes:
                    declarations.append((fp, start_line, h))

            for n, line in enumerate(lines, 1):
                if line.startswith('#') and HIST.match(line):
                    flush_paragraph(para, para_start, historical)
                    para = []
                    historical = True
                    para_start = n + 1
                    continue
                if not line.strip():
                    flush_paragraph(para, para_start, historical)
                    para = []
                    para_start = n + 1
                else:
                    if not para:
                        para_start = n
                    para.append(line)
            flush_paragraph(para, para_start, historical)

    print(f"  archive {base}")
    print(f"  actual  {actual}")
    if not declarations:
        print("\nbaseline_label_check: FAILED (no current checksum declaration "
              "for this exact archive basename)")
        return 1
    bad = [(fp, n, h) for fp, n, h in declarations if h != actual]
    for fp, n, h in bad:
        print(f"  MISMATCH {fp}:{n} declares {h}")
    if bad:
        print(f"\nbaseline_label_check: FAILED ({len(bad)} current declaration(s) "
              "do not match the archive)")
        return 1
    print(f"baseline_label_check: OK ({len(declarations)} current declaration(s) match)")
    return 0


if __name__ == '__main__':
    if '--verify-archive' in sys.argv:
        raise SystemExit(verify_checksum(sys.argv))
    raise SystemExit(main())
