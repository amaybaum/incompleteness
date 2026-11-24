"""Scan profiles: extraction from source blobs (never retyped), compilation and scanning (sec. 6.1)."""
import ast
import json
import re

from . import util


class ExtractFault(Exception):
    pass


def _ast_value(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, (ast.Tuple, ast.List)):
        vals = [_ast_value(e) for e in node.elts]
        if all(isinstance(v, str) for v in vals):
            return vals
        raise ExtractFault('non-string element')
    if isinstance(node, ast.Set):
        vals = [_ast_value(e) for e in node.elts]
        if all(isinstance(v, str) for v in vals):
            return sorted(vals)
        raise ExtractFault('non-string element')
    if isinstance(node, ast.Dict):
        out = {}
        for k, v in zip(node.keys, node.values):
            kk, vv = _ast_value(k), _ast_value(v)
            if not isinstance(kk, str) or not isinstance(vv, str):
                raise ExtractFault('non-string dict entry')
            out[kk] = vv
        return out
    if isinstance(node, ast.Call) and getattr(node.func, 'attr', None) == 'compile' and node.args:
        v = _ast_value(node.args[0])
        if not isinstance(v, str):
            raise ExtractFault('compile call without a literal pattern')
        flags = []
        for a in node.args[1:]:
            flags.append(getattr(a, 'attr', None))
        for kw in node.keywords:
            if kw.arg == 'flags':
                flags.append(getattr(kw.value, 'attr', None))
        if flags:
            return {'pattern': v, 'flags': flags}
        return v
    raise ExtractFault('unsupported value node %s' % type(node).__name__)


def _dotted(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        inner = _dotted(node.value)
        return None if inner is None else inner + '.' + node.attr
    return None


def function_literals(data, function):
    """Every string constant in one module-level function's body (for the params lint)."""
    tree = ast.parse(data.decode('utf-8'))
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == function]
    if len(fns) != 1:
        return None
    return [n.value for n in ast.walk(fns[0]) if isinstance(n, ast.Constant) and isinstance(n.value, str)]


def extract(kind, selector, data):
    """Returns the extracted value (a string, list or dict of strings)."""
    if kind == 'json-pointer':
        doc = json.loads(data.decode('utf-8'))
        cur = doc
        for part in [p.replace('~1', '/').replace('~0', '~') for p in selector.split('/')[1:]]:
            if isinstance(cur, list):
                cur = cur[int(part)]
            else:
                if part not in cur:
                    raise ExtractFault('json pointer %s: no %r' % (selector, part))
                cur = cur[part]
        return cur
    if kind == 'python-ast-assign':
        tree = ast.parse(data.decode('utf-8'))
        for node in tree.body:
            if isinstance(node, ast.Assign) and any(getattr(t, 'id', None) == selector for t in node.targets):
                return _ast_value(node.value)
        raise ExtractFault('no module-level assignment to %s' % selector)
    if kind == 'python-ast-call-arg':
        # selector {function, call, arg}: the literal argument of the one call `call` inside function `function`
        if not isinstance(selector, dict) or set(selector) != {'function', 'call', 'arg'}:
            raise ExtractFault('python-ast-call-arg selector must be {function, call, arg}')
        tree = ast.parse(data.decode('utf-8'))
        fns = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == selector['function']]
        if len(fns) != 1:
            raise ExtractFault('no single module-level function %s' % selector['function'])
        calls = [n for n in ast.walk(fns[0]) if isinstance(n, ast.Call) and _dotted(n.func) == selector['call']]
        if len(calls) != 1 or len(calls[0].args) <= selector['arg']:
            raise ExtractFault('no single call %s with argument %d in %s' % (selector['call'], selector['arg'],
                                                                            selector['function']))
        return _ast_value(calls[0].args[selector['arg']])
    if kind == 'literal-list':
        if not isinstance(selector, list) or not all(isinstance(x, str) for x in selector):
            raise ExtractFault('literal-list selector must be a list of strings')
        return list(selector)
    raise ExtractFault('unknown extractor kind %r' % kind)


def pattern_hash(value):
    return util.sha256(util.canonical(value))


def _flags(names):
    f = 0
    for n in names or []:
        f |= getattr(re, n, 0) if n else 0
    return f


def compile_value(value, literal):
    """[(key, compiled)] from an extracted value."""
    out = []
    if literal:
        for i, v in enumerate(value):
            out.append(('L%d' % (i + 1), re.compile(re.escape(v))))
        return out
    if isinstance(value, str):
        return [('', re.compile(value))]
    if isinstance(value, list):
        return [('%d' % (i + 1), re.compile(v)) for i, v in enumerate(value)]
    if isinstance(value, dict):
        if set(value) == {'pattern', 'flags'}:
            return [('', re.compile(value['pattern'], _flags(value['flags'])))]
        return [(k, re.compile(v)) for k, v in value.items()]
    raise ExtractFault('cannot compile %r' % type(value).__name__)


class Profile:
    def __init__(self, spec, value, minus=None):
        self.name = spec['name']
        self.kind = spec['kind']
        self.applies_to = spec['applies_to']
        self.levels = spec.get('levels', ['line'])
        self.combine = spec.get('combine', 'any')
        self.scope = spec.get('scope')
        self.literal = spec['source']['extractor']['kind'] == 'literal-list'
        self.patterns = compile_value(value, self.literal)
        self.minus = minus  # ('tokens', set) or ('spans', [compiled])
        self.spec = spec

    def matches(self, text):
        """[(key, start, end)] of the profile's matches in text, after its exclusions."""
        found = []
        for key, rx in self.patterns:
            for m in rx.finditer(text):
                if self.minus and self.minus[0] == 'tokens' and m.group(0) in self.minus[1]:
                    continue
                if self.minus and self.minus[0] == 'spans':
                    if any(s.start() <= m.start() and m.end() <= s.end()
                           for rxn in self.minus[1] for s in rxn.finditer(text)):
                        continue
                found.append((key, m.start(), m.end()))
        if self.combine == 'all':
            keys = {k for k, _, _ in found}
            if keys != {k for k, _ in self.patterns}:
                return []
        return found


def load_profile(spec, read_source):
    """read_source(source) -> bytes. Checks the extractor output against pattern_sha256."""
    src = spec['source']
    ex = src['extractor']
    data = read_source(src) if ex['kind'] != 'literal-list' else b''
    value = extract(ex['kind'], ex['selector'], data)
    h = pattern_hash(value)
    minus = None
    if spec.get('except'):
        e = spec['except']
        ev = extract(e['source']['extractor']['kind'], e['source']['extractor']['selector'], read_source(e['source']))
        if e['mode'] == 'tokens':
            minus = ('tokens', set(ev if isinstance(ev, list) else [ev]))
        else:
            minus = ('spans', [rx for _, rx in compile_value(ev, False)])
        h = pattern_hash([value, e['mode'], ev])
    return Profile(spec, value, minus), h


def scan_lines(profile, lines, only=None):
    """{line number: [(key, start, end)]} for the profile on each line (or the given line numbers)."""
    out = {}
    rng = only if only is not None else range(1, len(lines) + 1)
    for ln in rng:
        m = profile.matches(lines[ln - 1])
        if m:
            out[ln] = m
    return out
