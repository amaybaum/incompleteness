"""Text, hashing and serialization helpers shared by every engine stage."""
import hashlib
import json
import re


def sha256(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    """Canonical json bytes: sorted keys, no whitespace, utf-8."""
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')


def fingerprint(obj):
    return sha256(canonical(obj))


def dump_result(obj):
    return json.dumps(obj, sort_keys=True, indent=1, ensure_ascii=True) + '\n'


class EncodingFault(Exception):
    pass


def decode(data, where):
    if data is None:
        return None
    if b'\r' in data:
        raise EncodingFault('%s: carriage return present' % where)
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError as exc:
        raise EncodingFault('%s: not utf-8 (%s)' % (where, exc))


def lines_of(text):
    """Lines without their LF; a last line without LF is a line."""
    if text == '':
        return []
    parts = text.split('\n')
    if text.endswith('\n'):
        parts = parts[:-1]
    return parts


def line_starts(data):
    """Byte offsets of each line start in a bytes object."""
    out = [0]
    i = data.find(b'\n')
    while i >= 0:
        if i + 1 < len(data):
            out.append(i + 1)
        i = data.find(b'\n', i + 1)
    return out


def line_spans(data):
    """[(start, end_including_lf)] per line of a bytes object."""
    starts = line_starts(data) if data else []
    spans = []
    for k, s in enumerate(starts):
        e = starts[k + 1] if k + 1 < len(starts) else len(data)
        spans.append((s, e))
    return spans


def line_of_offset(data, off):
    """1-based line holding byte offset off (an offset at end of data maps to the last line)."""
    if not data:
        return 1
    if off >= len(data):
        off = len(data) - 1 if not data.endswith(b'\n') or off > len(data) else len(data) - 1
    return data.count(b'\n', 0, off) + 1


def context_pair(lines, idx):
    """Nearest non-blank line above and below a 0-based index, with sentinels."""
    above = 'BOF'
    for j in range(idx - 1, -1, -1):
        if lines[j].strip():
            above = lines[j]
            break
    below = 'EOF'
    for j in range(idx + 1, len(lines)):
        if lines[j].strip():
            below = lines[j]
            break
    return above, below


def context_hash(lines, idx):
    above, below = context_pair(lines, idx)
    return sha256(above.encode('utf-8') + b'\x00' + below.encode('utf-8'))


def context_hash_block(lines, i0, i1):
    """Context of a block lines[i0:i1]: nearest non-blank above i0 and below i1-1."""
    above = 'BOF'
    for j in range(i0 - 1, -1, -1):
        if lines[j].strip():
            above = lines[j]
            break
    below = 'EOF'
    for j in range(i1, len(lines)):
        if lines[j].strip():
            below = lines[j]
            break
    return sha256(above.encode('utf-8') + b'\x00' + below.encode('utf-8'))


# ---- sentence splitter (version 2) ---------------------------------------------------------------------

_item_rx = re.compile(r'^\s*(?:>\s*)*(?:[-*+]|\d+[.)])\s+')
_end_rx = re.compile(r'[.?!][*_]*(?=\s+(?:[A-Z*]|$))|[.?!][*_]*$')
_mask_rx = re.compile(r'\$[^$]*\$|`[^`]*`')
_initial_rx = re.compile(r'(?:^|\s)[A-Z]\.$')


def paragraphs(lines):
    """Paragraphs as lists of 1-based line numbers: runs of non-blank lines, broken before list items."""
    cur = []
    out = []
    for i, line in enumerate(lines, 1):
        if not line.strip():
            if cur:
                out.append(cur)
            cur = []
            continue
        if cur and _item_rx.match(line):
            out.append(cur)
            cur = []
        cur.append(i)
    if cur:
        out.append(cur)
    return out


def _mask(text):
    out = list(text)
    for m in _mask_rx.finditer(text):
        for j in range(m.start(), m.end()):
            if out[j] in '.?!':
                out[j] = '\x00'
    return ''.join(out)


def split_sentences(text, abbreviations):
    masked = _mask(text)
    out = []
    start = 0
    for e in _end_rx.finditer(masked):
        end = e.end()
        prev = masked[start:e.start() + 1]
        if any(prev.endswith(a) for a in abbreviations) or _initial_rx.search(prev):
            continue
        out.append((start, end))
        start = end
    if text[start:].strip():
        out.append((start, len(text)))
    return out


def sentences_of(lines, abbreviations, version):
    """[(sentence text, first line, last line)] for a file's lines, splitter version 2."""
    if version != 2:
        raise ValueError('unsupported splitter version %r' % (version,))
    result = []
    for para in paragraphs(lines):
        pieces = []
        offsets = []
        pos = 0
        for ln in para:
            t = lines[ln - 1].strip()
            if pieces:
                pos += 1
            offsets.append((pos, pos + len(t), ln))
            pieces.append(t)
            pos += len(t)
        joined = ' '.join(pieces)
        for a, b in split_sentences(joined, abbreviations):
            seg = joined[a:b]
            lead = len(seg) - len(seg.lstrip())
            a2 = a + lead
            s = seg.strip()
            if not s:
                continue
            b2 = a2 + len(s)
            first = next((ln for (x, y, ln) in offsets if y > a2), offsets[-1][2])
            last = first
            for (x, y, ln) in offsets:
                if x < b2:
                    last = ln
            result.append((s, first, last))
    return result
