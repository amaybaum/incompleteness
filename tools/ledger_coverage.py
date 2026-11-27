#!/usr/bin/env python3
"""Ledger and terminology verification tool: entry point.

Before any import of a module not already loaded at interpreter start (only `sys` and `os` precede it), the entry
point refuses with exit 65 unless the interpreter runs in isolated mode and no `sys.path` entry lies inside the
checkout (sec. 6.3, execution identity point 5). It then installs the wrapper and loads the package
`tools/ledger_coverage/` by its location; no directory of the checkout is put on `sys.path`. Any exception, including
the exit exception raised by code the tool calls and a keyboard interrupt, becomes the internal outcome with exit 71
and a result.json.

Usage: python3 -I -S -B tools/ledger_coverage.py {record,coverage,execution,terms,replay,self-test,purity-lint} ...
Exit codes: 0 pass, 10 review required, 20 fail, 64 usage, 65 error, 70 void, 71 internal.
"""
import os
import sys

_here = os.path.dirname(os.path.abspath(__file__))
_checkout = os.path.dirname(_here)


def _inside(p):
    for q in {os.path.abspath(p or os.curdir), os.path.realpath(p or os.curdir)}:
        for root in {_checkout, os.path.realpath(_checkout)}:
            if q == root or q.startswith(root.rstrip(os.sep) + os.sep):
                return True
    return False


if not sys.flags.isolated or any(_inside(p) for p in sys.path):
    # R6.OUT.4, R6.REC.20: ERROR, exit 65, no result.json; one line to stderr, one JSON object with the stop class
    # NOT_ISOLATED and the reason (written as a literal: no module may be imported before this check)
    sys.stderr.write('{"schema": "oi-ledger-coverage/5", "outcome": "ERROR", "exit_status": 65, "stop": {"class": '
                     '"NOT_ISOLATED", "message": "the entry point runs only as python3 -I, with no sys.path entry '
                     'inside the checkout"}}\n')
    sys.exit(65)

import json  # noqa: E402  (after the isolation check)

_meaning = {
    'authorized-replacement': 'a site replaced by a splice of the frozen ledger',
    'authorized-removal': 'a site removed by a splice of the frozen ledger',
    'unauthorized-edit': "a ledgered file whose bytes differ from H with the frozen ledger's splices applied",
    'unauthorized-change': 'a change that no splice of the frozen ledger and no declared class specifies',
}


def _out_from(argv):
    for i, a in enumerate(argv):
        if a == '--out' and i + 1 < len(argv):
            return argv[i + 1]
        if a.startswith('--out='):
            return a[6:]
    return None


def _internal(argv, exc):
    doc = {'schema': 'oi-ledger-coverage/5', 'outcome': 'INTERNAL', 'exit_status': 71,
           'stop': {'class': type(exc).__name__, 'message': str(exc)[:2000]},
           'preflight': [], 'record_checks': None, 'items': [], 'class_meaning': dict(_meaning)}
    out = _out_from(argv)
    try:
        if out:
            if not os.path.exists(out):
                os.makedirs(out)
            names = set(os.listdir(out))
            if names <= {'result.json', 'replay'}:
                with open(os.path.join(out, 'result.json'), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(doc, sort_keys=True, indent=1, ensure_ascii=True) + '\n')
    except BaseException:
        pass
    try:
        sys.stderr.write(json.dumps(doc, sort_keys=True) + '\n')
    except BaseException:
        pass
    return 71


def _load_package():
    """The package `ledger_coverage` from its location beside this file, without a search of sys.path."""
    import importlib.util
    pkg = os.path.join(_here, 'ledger_coverage')
    spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(pkg, '__init__.py'),
                                                  submodule_search_locations=[pkg])
    mod = importlib.util.module_from_spec(spec)
    sys.modules['ledger_coverage'] = mod
    spec.loader.exec_module(mod)
    return mod


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        _load_package()
        from ledger_coverage.engine import cli
        code, _ = cli.run(argv)
        return code
    except BaseException as exc:
        return _internal(argv, exc)


if __name__ == '__main__':
    sys.exit(main())
