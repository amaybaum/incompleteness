#!/usr/bin/env python3
"""Source-side facts the hardening design relies on (#1162).

Reads the Lean sources under verification/lean-mathlib/ (skipping .lake) and
prints one JSON object. It reads no build log, runs no Lean and imports
nothing from tools/. Counts:

  print_lines            lines whose first token is `#print axioms`
  col0 / indented        of those, starting at column 0 / after whitespace
  current_pattern_miss   prints the current checker's declared pattern
                         (^#print axioms [A-Za-z0-9_.']+\\s*$) does not collect
  non_ascii_names        prints whose written name has a non-ASCII character
  name_on_next_line      `#print axioms` with nothing after it on the line
  trailing_text          a name followed by further non-whitespace text
  escaped_names          written names containing «
  short_names_multi_module  final components (current checker's reduction of
                         the names it collects) printed in more than one module
  written_names_multi_module  written names (as written) printed in more than
                         one module

Usage: python3 -I source_facts.py [--root DIR]
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
PRINT = re.compile(r'^([ \t]*)#print[ \t]+axioms(?![^ \t\n])(.*)$')
CURRENT = re.compile(r"^#print axioms ([A-Za-z0-9_.']+)\s*$")


def main():
    root = ROOT
    if '--root' in sys.argv:
        root = os.path.abspath(sys.argv[sys.argv.index('--root') + 1])
    src = os.path.join(root, 'verification', 'lean-mathlib')
    c = dict(print_lines=0, col0=0, indented=0, current_pattern_miss=0,
             non_ascii_names=0, name_on_next_line=0, trailing_text=0,
             escaped_names=0)
    short, written = {}, {}
    for dp, dns, fs in os.walk(src):
        dns[:] = sorted(d for d in dns if d != '.lake')
        for f in sorted(fs):
            if not f.endswith('.lean'):
                continue
            path = os.path.join(dp, f)
            mod = os.path.relpath(path, src).replace(os.sep, '/')
            for line in open(path, encoding='utf-8').read().split('\n'):
                m = PRINT.match(line)
                if not m:
                    continue
                c['print_lines'] += 1
                c['indented' if m.group(1) else 'col0'] += 1
                if not CURRENT.match(line):
                    c['current_pattern_miss'] += 1
                rest = m.group(2).strip()
                if not rest:
                    c['name_on_next_line'] += 1
                    continue
                parts = rest.split(None, 1)
                name = parts[0]
                if len(parts) > 1:
                    c['trailing_text'] += 1
                if '«' in name:
                    c['escaped_names'] += 1
                if any(ord(ch) > 127 for ch in name):
                    c['non_ascii_names'] += 1
                cm = CURRENT.match(line)
                if cm:
                    short.setdefault(cm.group(1).split('.')[-1], set()).add(mod)
                written.setdefault(name, set()).add(mod)
    c['short_names_multi_module'] = sum(1 for v in short.values() if len(v) > 1)
    c['written_names_multi_module'] = sum(1 for v in written.values() if len(v) > 1)
    print(json.dumps(c, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
