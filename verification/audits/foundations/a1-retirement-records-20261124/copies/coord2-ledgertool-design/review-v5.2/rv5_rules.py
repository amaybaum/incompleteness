"""v5 active deny set (DR-1a/b/c, DR-3, DR-4, DR-5), retired DR-1d/DR-2 (history), widened resid
(resid-a/b/c) and splitter version 2, transcribed by the reviewer from DESIGN-v5 sec. 6.1, 6.4, 6.4.1, 6.6."""
import re
N = r'(?:assumptions?|axioms?|posits?|premises?|conditions?)'
CNT = r'(?:six|seven|sixth|seventh)'
def LBL(k): return r'(?:\(\s*A%s\s*\)|\bA%s\b)' % (k, k)
SEP = r'(?:\s*(?:-{1,3}|–|—|\bthrough\b|\bto\b|\$?\\(?:text)?(?:endash|emdash)\$?)\s*|\s*,\s*(?:\.{3}|…|\$?\\l?dots\$?|\$?\\cdots\$?)\s*,?\s*)'
DR = {
 'DR-1a': r"(?i)\b%s\b[^.;]{0,40}\b(?:structural|substratum(?:'s|’s)?)\s+%s" % (CNT, N),
 'DR-1b': r'(?i)\b%s\b[^.;]{0,40}\bstructural\s+propert(?:y|ies)\s+of\s+the\s+substratum\b' % CNT,
 'DR-1c': r'(?i)' + LBL(1) + SEP + LBL(6),
 'DR-4': r'(?i)(?:\(\s*A1\s*\)|\bposit\s+A1\b|\bA1\b\s*(?:\(|:))[^.;]{0,60}(?:\.[^.;]{0,80})?\b(?:finit\w*|configuration\s+space|substratum)',
 'DR-5': r'(?i)\b(?:fourteen|14)\b[^.;]{0,40}\b(?:items|posits|entries|premises|assumptions)\b',
}
RETIRED = {
 'DR-1d': r"(?i)\b(?:structural|substratum(?:'s|’s)?)\s+(?:sixth|seventh)\s+(?:assumption|axiom|posit|premise|condition|property)\b",
 'DR-2': r'(?i)\b(?:sixth|seventh)\b[^.;]{0,40}\bstructural\s+(?:property|assumption|axiom|posit|premise|condition)\b[^.;]{0,80}\bfinit',
}
DR3_COUNT = re.compile(r'(?i)structural\s+propert|structural\s+assumption|structural\s+axiom|structural\s+posit|\bposits?\b|\bpremises?\b|\baxioms?\b')
DR3_TAIL = re.compile(r'(?i)(?:one of which|one of its|one of the|among|includ\w*|the first being|first of which|namely)[^.;]{0,60}?(?:total[- ]finiteness|finite in total|totally finite|finiteness of (?:\$?\\?(?:mathcal\{)?S\}?\$?|the (?:configuration|state) space)|finiteness\b)')
DRC = {k: re.compile(v) for k, v in DR.items()}
RETC = {k: re.compile(v) for k, v in RETIRED.items()}
RESID_A = re.compile(r'(?i)\b(?:configuration|state|phase)\s+spaces?\b[^.;]{0,40}\b(?:is|be|being|are|remains?)\s+(?:\w+\s+)?finite\b|\b(?:posits?|premises?|axioms?|assumptions?|hypothes[ie]s)\b[^.;]{0,60}\bfinit\w*|\bfinit\w*[^.;]{0,60}\b(?:posits?|premises?|axioms?|assumptions?|hypothes[ie]s)\b')
RESID_B = re.compile(r'(?i)\bfinite\s+(?:\w+\s+)?set\b|\b(?:substratum|universe|world)\b[^.;]{0,40}\b(?:is|be|being|are)\s+(?:a\s+)?(?:\w+\s+)?finite\b')
RESID_C = re.compile(r'(?i)\bfinite\s+(?:number|count)\s+of\s+(?:\w+\s+)?(?:states|configurations|elements|points|sites)\b')
def resid(s): return bool(RESID_A.search(s) or RESID_B.search(s) or RESID_C.search(s))

def deny_line(s, retired=False):
    d = dict(DRC); d.update(RETC if retired else {})
    return sorted(k for k, rx in d.items() if rx.search(s))
def deny_sentence(s, retired=False):
    out = deny_line(s, retired)
    if DR3_COUNT.search(s) and DR3_TAIL.search(s): out.append('DR-3')
    return sorted(out)

ABBR = ['sec.', 'Sec.', 'e.g.', 'i.e.', 'cf.', 'Fig.', 'Eq.', 'Eqs.', 'No.', 'vs.', 'et al.', 'Ch.', 'App.', 'Thm.', 'Prop.', 'Lem.']
LISTITEM = re.compile(r'^\s*(>\s*)*([-*+]|\d+[.)])\s+')
def paragraphs(lines, v=2):
    cur = []
    def flush():
        if cur:
            yield list(cur), ' '.join((lines[j - 1].strip() if v == 2 else lines[j - 1]) for j in cur)
    for i, l in enumerate(lines, 1):
        if not l.strip():
            yield from flush(); cur.clear(); continue
        if v == 2 and cur and LISTITEM.match(l):
            yield from flush(); cur.clear()
        cur.append(i)
    yield from flush()

def split_sentences(p, v=2):
    out, start, i, n = [], 0, 0, len(p)
    in_math = in_code = False
    while i < n:
        ch = p[i]
        if ch == '`' and not in_math: in_code = not in_code
        elif ch == '$' and not in_code: in_math = not in_math
        elif ch in '.?!' and not in_math and not in_code:
            j = i + 1
            if v == 2:
                while j < n and p[j] in '*_': j += 1
            if j == n or p[j].isspace():
                k = j
                while k < n and p[k].isspace(): k += 1
                if k == n or p[k].isupper() or p[k] == '*':
                    seg = p[start:i + 1]; ok = True
                    if ch == '.':
                        if any(seg.endswith(' ' + a) or seg == a or seg.endswith('(' + a) for a in ABBR): ok = False
                        if re.search(r'(?:^|[\s(])([A-Z])\.$', seg): ok = False
                    if ok:
                        out.append(p[start:j].strip()); start = k; i = k; continue
        i += 1
    if start < n and p[start:].strip(): out.append(p[start:].strip())
    return out
