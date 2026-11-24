"""Preregistered context rule: meaning mapping, indicators and structure contexts (sec. 4)."""
import re

from . import util


class Indicators:
    """Indicator definitions supplied by the configuration as data."""

    def __init__(self, spec):
        self.strip_steps = [re.compile(p) for p in spec['strip']]
        self.defs = []
        for d in spec['definitions']:
            self.defs.append({'name': d['name'], 'on': d['on'], 'effect': d['effect'],
                              'patterns': [re.compile(p) for p in d.get('patterns', [])]})
        self.item_rx = [re.compile(p) for p in spec['list_item_patterns']]
        self.table_rx = re.compile(spec['table_row_pattern'])
        self.caption_prefixes = list(spec['caption_prefixes'])

    def strip(self, line):
        s = line
        for rx in self.strip_steps:
            s = rx.sub('', s, count=1)
        return s

    def evaluate(self, pin_line, quote):
        out = {}
        for d in self.defs:
            if d['on'] == 'stripped':
                out[d['name']] = any(rx.search(self.strip(pin_line)) for rx in d['patterns'])
            elif d['on'] == 'line':
                out[d['name']] = any(rx.search(pin_line) for rx in d['patterns'])
            elif d['on'] == 'quote':
                out[d['name']] = quote is not None and ' '.join(quote.split()) != ' '.join(pin_line.split())
            else:
                raise ValueError('unknown indicator input %r' % d['on'])
        return out

    def effects(self, flags):
        return {d['effect'] for d in self.defs if flags.get(d['name'])}

    def is_item(self, line):
        return any(rx.search(line) for rx in self.item_rx)

    def list_context(self, lines, idx):
        j = idx - 1
        while j >= 0 and (not lines[j].strip() or self.is_item(lines[j])):
            j -= 1
        lead = lines[j] if j >= 0 else 'BOF'
        k = idx + 1
        while k < len(lines) and (not lines[k].strip() or self.is_item(lines[k])):
            k += 1
        trail = lines[k] if k < len(lines) else 'EOF'
        sib = [lines[x] for x in range(j + 1, k) if x != idx and lines[x].strip()]
        return util.sha256(util.canonical([lead, sib, trail]))

    def table_context(self, lines, idx):
        a = idx
        while a > 0 and self.table_rx.search(lines[a - 1]):
            a -= 1
        b = idx
        while b + 1 < len(lines) and self.table_rx.search(lines[b + 1]):
            b += 1
        header = lines[a]
        above = 'BOF'
        for j in range(a - 1, -1, -1):
            if lines[j].strip():
                above = lines[j]
                break
        below = ''
        for j in range(b + 1, len(lines)):
            if lines[j].strip():
                if any(lines[j].startswith(p) for p in self.caption_prefixes):
                    below = lines[j]
                break
        return util.sha256(util.canonical([header, above, below]))

    def structure(self, effects, lines, idx):
        if 'structure-list' in effects:
            return self.list_context(lines, idx)
        if 'structure-table' in effects:
            return self.table_context(lines, idx)
        return None


def meaning_required(mapping, value, effects):
    """Context required for meaning: the mapped value, or a meaning-setting indicator."""
    if value not in mapping['values']:
        raise KeyError(value)
    return bool(mapping['values'][value]) or ('meaning' in effects)


def decide(site, from_ctx, to_ctx, from_struct, to_struct, adjudications, segment):
    """Returns (class or None, detail) for a site whose identity is verified in a segment (sec. 4.1)."""
    changed = from_ctx != to_ctx
    struct_changed = from_struct is not None and from_struct != to_struct
    adj = [a for a in adjudications if a.get('site_id') == site['site_id'] and a.get('segment') == segment
           and a.get('from_context_sha256') == from_ctx and a.get('to_context_sha256') == to_ctx]
    if changed and site['meaning_context']:
        if adj:
            return None, {'context_changed': True, 'adjudicated': True}
        return 'context-meaning-unverified', {'context_changed': True}
    if from_struct is not None and (changed or struct_changed):
        ok = [a for a in adj if a.get('from_structure_sha256') == from_struct
              and a.get('to_structure_sha256') == to_struct]
        if not ok and not (changed is False and struct_changed is False):
            return 'context-structure-changed', {'context_changed': changed, 'structure_changed': struct_changed}
        return None, {'context_changed': changed, 'structure_changed': struct_changed, 'adjudicated': bool(ok)}
    return None, {'context_changed': changed}
