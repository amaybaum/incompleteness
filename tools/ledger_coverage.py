#!/usr/bin/env python3
"""Ledger and terminology verification tool: entry point.

The wrapper is installed before the package is imported. Any exception, including the exit exception raised by
code the tool calls and a keyboard interrupt, becomes the internal outcome with exit 71 and a result.json.

Usage: python3 -I -B tools/ledger_coverage.py {record,coverage,execution,terms,self-test,purity-lint} ...
Exit codes: 0 pass, 10 review required, 20 fail, 64 usage, 65 error, 70 void, 71 internal.
"""
import json
import os
import sys


def _out_from(argv):
    for i, a in enumerate(argv):
        if a == '--out' and i + 1 < len(argv):
            return argv[i + 1]
        if a.startswith('--out='):
            return a[6:]
    return None


def _internal(argv, exc):
    doc = {'schema': 'oi-ledger-coverage/4', 'outcome': 'INTERNAL', 'exit_status': 71,
           'stop': {'class': type(exc).__name__, 'message': str(exc)[:2000]},
           'preflight': [], 'record_checks': None, 'items': []}
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


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        if here not in sys.path:
            sys.path.insert(0, here)
        from ledger_coverage.engine import cli
        code, _ = cli.run(argv)
        return code
    except BaseException as exc:
        return _internal(argv, exc)


if __name__ == '__main__':
    sys.exit(main())
