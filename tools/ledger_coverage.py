#!/usr/bin/env python3
"""Ledger and terminology verification tool: entry point.

Before any import of a module not already loaded at interpreter start, the entry point refuses with exit 65
unless the interpreter runs in isolated mode and no `sys.path` entry lies inside the checkout
(sec. 6.3, execution identity point 5). It then installs the wrapper and loads the package
`tools/ledger_coverage/` by its location; no directory of the checkout is put on `sys.path`. Any exception, including
the exit exception raised by code the tool calls and a keyboard interrupt, becomes the internal outcome with exit 71
and a result.json.

Usage: python3 -I -S -B tools/ledger_coverage.py {record,coverage,execution,terms,replay,self-test,purity-lint} ...
Exit codes: 0 pass, 10 review required, 20 fail, 64 usage, 65 error, 70 void, 71 internal.
"""
import sys


def _posix_path(path, cwd, filesystem=None):
    """Resolve a startup path with the already loaded POSIX primitives."""
    if not path.startswith('/'):
        path = cwd + '/' + path
    pending = path.split('/')[::-1]
    parts = []
    links = 0
    while pending:
        part = pending.pop()
        if part in ('', '.'):
            continue
        if part == '..':
            if parts:
                parts.pop()
            continue
        candidate = '/' + '/'.join(parts + [part])
        if filesystem is not None:
            try:
                mode = filesystem.lstat(candidate).st_mode
            except (FileNotFoundError, NotADirectoryError):
                mode = 0
            if mode & 0o170000 == 0o120000:
                links += 1
                if links > 40:
                    raise ValueError('startup path has too many symbolic links')
                target = filesystem.readlink(candidate)
                if target.startswith('/'):
                    parts.clear()
                pending.extend(reversed(target.split('/')))
                continue
        parts.append(part)
    return '/' + '/'.join(parts)


def _isolated():
    if not sys.flags.isolated:
        return False
    host = sys.modules.get('os')
    try:
        if host is not None:
            lexical, real = host.path.abspath, host.path.realpath
            sep = host.sep
            checkout = host.path.dirname(host.path.dirname(lexical(__file__)))
        else:
            filesystem = sys.modules.get('posix')
            if filesystem is None:
                return False
            cwd = filesystem.getcwd()
            lexical = lambda p: _posix_path(p, cwd)
            real = lambda p: _posix_path(p, cwd, filesystem)
            sep = '/'
            checkout = lexical(__file__).rsplit(sep, 2)[0] or sep
        roots = {checkout, real(checkout)}
        for p in sys.path:
            for q in {lexical(p), real(p)}:
                if any(q == root or q.startswith(root.rstrip(sep) + sep) for root in roots):
                    return False
    except (AttributeError, OSError, TypeError, ValueError):
        return False
    return True


if not _isolated():
    # R6.OUT.4, R6.REC.20: ERROR, exit 65, no result.json; one line to stderr, one JSON object with the stop class
    # NOT_ISOLATED and the reason, formatted here without importing a JSON encoder.
    sys.stderr.write('{"schema": "oi-ledger-coverage/5", "outcome": "%s", "exit_status": 65, "stop": {"class": '
                     '"%s", "message": "the entry point runs only as python3 -I, with no sys.path entry '
                     'inside the checkout"}}\n' % ('ERROR', 'NOT_ISOLATED'))
    sys.exit(65)

import json  # noqa: E402  (after the isolation check)
import os  # noqa: E402

_here = os.path.dirname(os.path.abspath(__file__))

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
