#!/usr/bin/env python3
"""Throwaway prototype of the redesigned withdrawn-claim checker (paper-only, issue 1565).
Not for the repository. Implements the DESIGN.md mechanism approximately with regexes."""
import re, sys, os, json, hashlib

I = re.I
TEMP_SUBJ = (r"T_Q|T_\{?\\(?:rm|mathrm)\{?\s*dS\}?\}?|T_\{\\rm dS\}|T_\{\\rm H\}|"
             r"(?:Hawking|Gibbons[- ]Hawking|de Sitter|horizon|Unruh|KMS)\s+temperatures?|"
             r"thermality|thermal (?:ratio|spectrum|character)|the temperature")
GENERIC_HEAD = r"(?:quantity|quantities|value|values|one|result|answer|object|expression)"
HYP_GENERIC = (r"\b(?:conditional(?:ly)?(?! *ly)|assum\w*|premise\w*|hypothes\w+|in the [\w-]+ sense|"
               r"on the [\w-]+ reading|under|if|given|provided|when|on the [^,;]{0,40}?branch)\b")
NEG = r"\b(?:not|never|no longer|cannot|can't|fails? to|failing to|failed to|rather than)\b"
DISCOURSE_NOT = r"\bnot (?:surprisingly|coincidentally|only|least|just|unexpectedly)\b"

RULES = [
 dict(id="W-GR-TQ-STATE", kind="adj", subj=TEMP_SUBJ, heads=r"temperatures?|thermality|ratio",
      pred=r"state[- ]independent|independent of the (?:quantum )?state",
      lic=r"H-balance|H-spectrum|H-slope"),
 dict(id="W-GR-TQ-STATE", kind="verb", subj=TEMP_SUBJ,
      verb=r"(?:does not|doesn't|do not) depend on|is independent of|are independent of",
      obj=r"the (?:quantum |horizon |observer's )?states?\b", lic=r"H-balance|H-spectrum|H-slope", inherent_neg=True),
 dict(id="W-GR-THERM-KIN", kind="adj", subj=TEMP_SUBJ, heads=r"temperatures?|thermality|spectrum", pred=r"purely kinematic(?:al)?",
      lic=r"H-balance|H-spectrum|H-slope"),
 dict(id="W-GR-KMS", kind="verb",
      subj=r"\bany QFT|\bevery QFT|\ban? QFT|\bany quantum field theory|\bthe QFT",
      verb=r"must (?:therefore )?(?:be|remain) (?:periodic|KMS|a KMS state)|is (?:periodic in imaginary time|a KMS state|KMS\b)",
      obj=None, lic=r"H-Hawking", flags=I, foreign="review"),
 dict(id="W-GR-CONE", kind="adj", subj=r"free-level (?:light )?cone", pred=r"exact(?: per channel)?",
      lic=r"(?!x)x", nongov=r"on the normalized \$d ?= ?3\$[^,;]*?branch"),
 dict(id="W-GR-EPSKAPPA", kind="literal", pat=r"(\\v?arepsilon|\\epsilon)\s*\\kappa\s*/\s*c\b(?!\^)", flags=0),
 dict(id="W-BM-EUCLID", kind="verb",
      subj=r"cubic (?:equivariance|symmetry)|equivariance|projected memory|the (?:lattice|substratum|symmetry)",
      verb=r"forc(?:es|ing|e) an? Euclidean", obj=None, foreign="review",
      lic=r"b_m\s*(?:\\neq|\\ne|≠)\s*0|nondegenerate|non-degenerate|normalized canonical branch"),
 dict(id="W-BM-EUCLID", kind="adj", subj=r"(?:leading )?scalar propagation geometry|quadratic symbol",
      pred=r"Euclidean", lic=r"b_m\s*(?:\\neq|\\ne|≠)\s*0|nondegenerate|non-degenerate|normalized canonical branch",
      copular_only=True),
 dict(id="W-KDEG", kind="verb", subj=r"coupling-degree minimi[sz]ation",
      verb=r"(?:fix(?:es|ing)?|determin(?:es?|ing)|select(?:s|ing)?|deriv(?:es?|ing)|forc(?:es?|ing)|establish(?:es|ing)?|yield(?:s|ing)?|giv(?:es?|ing)|implies|produc(?:es?|ing))",
      obj=r"\$?K\b|2d|m\s*=\s*1|single-copy|\bsites?\b|carrier|six|it\b|this\b",
      lic=r"(?!x)x", flags=I),
 dict(id="W-KDEG", kind="passive", subj=r"coupling-degree minimi[sz]ation",
      lead=r"(?:\$?K\s*=\s*(?:2d|6)\$?|\$m\s*=\s*1\$|the single-copy clause)\s*(?:follows|is (?:derived|fixed|selected|forced))\s+(?:from|by)\s*$|"
           r"\bderiv\w*\s+[^;]{0,80}?\bfrom\s*$|\b(?:consequence|result) of\s*$",
      lic=r"(?!x)x", flags=I),
 dict(id="W-KDEG", kind="literal", pat=r"framework's answer is \$K = 2d", flags=0, negslot=True),
 dict(id="W-OI-REQ", kind="verb", subj=r"\b(?:QM|quantum mechanics|quantum theory|the quantum formalism)\b",
      verb=r"(?:requires?|needs?|presuppos(?:es|e)|depends? on)",
      obj=r"(?:bare )?(?:OI\b|observation(?:al)? incompleteness)",
      lic=r"core-containment|containment sense|qm_implies_oiCore|realizes the (?:sealed )?OI core", flags=I),
 dict(id="W-OI-HIDDEN", kind="verb", subj=r"\b(?:QM|quantum mechanics|quantum theory)\b",
      verb=r"(?:requires?|needs?)", obj=r"hidden (?:information|variables?|states?|ontology|sub-quantum level|level)",
      lic=r"(?!x)x", flags=I),
 dict(id="W-OI-NOEXIST", kind="verb", subj=r"\b(?:QM|quantum mechanics|quantum theory)\b",
      verb=r"cannot exist without|could not exist without", obj=None, lic=r"(?!x)x", inherent_neg=True, flags=I),
 dict(id="W-OI-EXPLAINS", kind="verb", subj=r"\b(?:OI|observation(?:al)? incompleteness|ignorance)\b",
      verb=r"(?:causes|produces|explains|generates|gives rise to|cause|produce|explain|generate|give rise to)",
      obj=r"\b(?:QM|quantum)", lic=r"(?!x)x", flags=I),
 dict(id="W-OI-CONTRA", kind="literal",
      pat=r"\bwithout (?:OI|observation(?:al)? incompleteness) there (?:is|would be) no (?:QM|quantum)", flags=I,
      negslot=False),
]

FRAME_PRE = re.compile(
    r"(?:\bnot claimed\b|\bit is not (?:proved|shown|established|the case)\b|\bis not proved\b|"
    r"\b(?:no|neither|none of|nothing in)\b[^;:]{0,60}?\b(?:shows?|proves?|establish\w*|derives?|says?|implies)\b|"
    r"\b(?:does|do|did) not (?:show|establish|prove|imply|say|claim)\b|\bunproved\b|\bnothing (?:shows|proves)\b|\bwhether\b|"
    r"\bthe (?:necessity|strong) reading\b)[^;]*?(?:\bthat\b|:|\bwhether\b)?[^;]*$", I)
FRAME_POST = re.compile(r"^[^;]*?\b(?:is|was|remains)\s+(?:withdrawn|false|unproved|not proved|not established|unsupported|not a theorem)\b", I)
CLAIM_THAT = re.compile(r"\b(?:claim|statement|reading|assertion) that\s*$", I)

COPULA = re.compile(r"\b(?:is|are|was|were|be|been|being|remains?|becomes?|stays?)\b((?:\s+(?!state)[\w-]+){0,3}?)\s*$", I)

# ------------------------------------------------------------------ segmentation
MASK = re.compile(r"\$\$.*?\$\$|\$[^$]*\$|`[^`]*`", re.S)

def masked(s):
    return MASK.sub(lambda m: re.sub(r"[.;:,!?()—]", "\x00", m.group(0)), s)

ABBR = re.compile(r"\b(?:e\.g|i\.e|cf|vs|et al|Fig|Eq|Ref|resp|approx|No)\.$")

def sentences(par):
    m = masked(par)
    out, start = [], 0
    for x in re.finditer(r"(?:[.!?][\"'\u201d)\]]*(?:\*\*|\*)?|\.\$\$|\x00\$\$|\$\$)(?=\s+[A-Z*_`$\[(\"']|\s*$)|\s\|(?=\s)|\n(?=\s*(?:[-*+]\s|\d+\.\s|\||\$\$))", m):
        end = x.end()
        if ABBR.search(m[start:x.start() + 1]):
            continue
        out.append((start, end)); start = end
    if start < len(par):
        out.append((start, len(par)))
    return [(a, b) for a, b in out if par[a:b].strip()]

def clauses(sent):
    """Return list of (offset, text). Parentheticals, dash pairs and comma-relative clauses are
    their own clauses; the remainder is split at ; and at comma-coordinators."""
    m = masked(sent)
    spans = []
    blank = list(m)
    for rx in (r"\([^()]*\)", r"\s—\s[^—]*?\s—\s", r",\s(?:which|whose|who|where)\b[^,;]*(?=,|;|$)"):
        for x in re.finditer(rx, m):
            if any(blank[i] == "\x01" for i in range(x.start(), x.end())):
                continue
            spans.append((x.start(), x.end()))
            for i in range(x.start(), x.end()):
                blank[i] = "\x01"
    rem = "".join(blank)
    cuts = [0]
    for x in re.finditer(r";|:\**\s|\s\u2014\s|,\s(?:and|but|while|whereas|so|though|although|yet)\s|\sbut\s", rem):
        cuts += [x.start(), x.end()]
    cuts.append(len(rem))
    out = []
    for i in range(0, len(cuts), 2):
        a, b = cuts[i], cuts[i + 1]
        txt = "".join(sent[k] if rem[k] != "\x01" else " " for k in range(a, b))
        out.append((a, txt))
    for a, b in spans:
        out.append((a, sent[a:b]))
    return out

# ------------------------------------------------------------------ decision
def fl(r): return r.get("flags", I) if r["kind"] != "literal" else r.get("flags", 0)

def neg_slot(between):
    b = re.sub(DISCOURSE_NOT, "", between, flags=I)
    return re.search(NEG, b, I) is not None

def generic_or_neg_in(text, rule, exclude_spans=()):
    t = text
    for a, b in exclude_spans:
        t = t[:a] + " " * (b - a) + t[b:]
    t = re.sub(DISCOURSE_NOT, "", t, flags=I)
    t = re.sub(r"\bunconditional\w*", "", t, flags=I)
    if rule.get("nongov"):
        t = re.sub(rule["nongov"], "", t, flags=I)
    if re.search(HYP_GENERIC, t, I):
        return "generic-qualifier"
    return None

def governed(rule, sent, s_off, cl_text, a_start, a_end, neg_between):
    """Return ('PASS', why) | ('REVIEW', why) | ('FAIL', why) for a bound assertion."""
    if neg_between:
        return "PASS", "G1 negation in the assertion's slot"
    pre = sent[:s_off + a_start]
    pre_s = pre.split(";")[-1]
    if FRAME_PRE.search(pre_s):
        return "PASS", "G2 assertion inside a negative/non-assertive frame"
    if CLAIM_THAT.search(pre_s) and FRAME_POST.search(sent[s_off + a_end:]):
        return "PASS", "G2 claim-that frame with negative predicate"
    if re.search(rule["lic"], cl_text, fl(rule)) or (
            re.match(r"\s*\**(?:if|under|given|assuming|provided|when)\b[^,]*,", sent, I)
            and re.search(rule["lic"], re.match(r"\s*\**[^,]*,", sent).group(0), fl(rule))):
        return "PASS", "G3 licensed hypothesis governs the clause"
    g = generic_or_neg_in(cl_text, rule, [(a_start, a_end)])
    if g:
        return "REVIEW", "R3 " + g + " in the assertion's clause, not licensed"
    # unattached negation before the subject in the same clause
    lead = re.sub(DISCOURSE_NOT, "", cl_text[:a_start], flags=I)
    if re.search(NEG, lead, I) and not neg_between:
        return "REVIEW", "R3 negation in the clause outside the assertion's slot"
    return "FAIL", "asserted; no governing qualifier"

def check_clause(rule, par, sent, s_off, cl_off, cl, window_has_subj, sent_has_subj, prev_cl=""):
    res = []
    f = fl(rule)
    k = rule["kind"]
    if k == "literal":
        for m in re.finditer(rule["pat"], cl, f):
            if rule.get("negslot"):
                tail = cl[m.end():m.end() + 0]
            between = ""
            if rule.get("negslot") and re.search(r"\bis not\b", cl[m.start():m.end()]):
                between = "not"
            if rule["id"] == "W-GR-EPSKAPPA":
                res.append((m, "FAIL", "formula error; no qualifier repairs it"))
            else:
                v, why = governed(dict(rule, lic=r"(?!x)x"), sent, cl_off, cl, m.start(), m.end(), bool(between))
                res.append((m, v, why))
        return res
    if k == "adj":
        for m in re.finditer(r"(?<![\w-])(?:" + rule["pred"] + r")(?![\w-])", cl, f):
            after = cl[m.end():]
            before = cl[:m.start()]
            # attributive: predicate directly modifying a following noun phrase
            att = re.match(r"\s+((?:[\w$\\{}^_-]+\s*){1,3})", after)
            cop = COPULA.search(before)
            if not rule.get("copular_only") and att and not cop:
                head = att.group(1)
                if re.search(rule["subj"], head, f):
                    v, why = governed(rule, sent, cl_off, cl, m.start(), m.end(),
                                      bool(re.search(r"\b(?:no|not|rather than)\s+(?:an?\s+)?$", before, I)))
                    res.append((m, v, "attributive; " + why))
                elif re.match(r"\s*" + GENERIC_HEAD, head, I) and window_has_subj:
                    res.append((m, "REVIEW", "R1 attributive head is generic; subject unresolved"))
                else:
                    res.append((m, "PASS", "unrelated: predicate modifies '%s'" % head.strip()[:40]))
                continue
            if rule.get("copular_only") and not cop:
                continue
            caus = re.search(r"\b(nothing|no \w+)?\s*\b(?:(?:does|do|did|can) not\s+)?(?:makes?|renders?|keeps?|make|render)\s+((?:\S+\s+){0,3}?)$", before, I)
            if caus and re.search(rule["subj"], caus.group(2), f):
                neg = bool(caus.group(1)) or bool(re.search(r"\bnot\b", caus.group(0), I))
                v, why = governed(rule, sent, cl_off, cl, caus.start(), m.end(), neg)
                res.append((m, v, "causative; " + why)); continue
            if cop:
                subjseg = before[:cop.start()]
                between = cop.group(0)
                toks = re.findall(r"[^\s]+", subjseg)
                win = " ".join(toks[-7:])
                last = toks[-1] if toks else ""
                if re.search(rule["subj"], win, f) or (re.search(rule["subj"], subjseg, f) and len(toks) <= 12):
                    if re.fullmatch(r"\W*" + GENERIC_HEAD + r"\W*", last, I):
                        res.append((m, "REVIEW", "R2 copular subject has a generic head")); continue
                    neg = neg_slot(between) or bool(re.search(r"\b(?:no|nothing|neither|none)\s+(?:\w+\s+){0,1}$",
                                                       subjseg[:re.search(rule['subj'], subjseg, f).start()], I))
                    sst = len(before[:cop.start()]) - len(subjseg) + list(re.finditer(rule["subj"], subjseg, f))[-1].start()
                    v, why = governed(rule, sent, cl_off, cl, sst, m.end(), neg)
                    res.append((m, v, "copular; " + why))
                elif re.fullmatch(r"\W*(?:it|this|that|these|they|which|both|each)\W*", last, I) or not toks:
                    if neg_slot(between):
                        res.append((m, "PASS", "G1 negated; subject unresolved"))
                    elif window_has_subj:
                        res.append((m, "REVIEW", "R1 pronoun/elided subject; rule subject in window"))
                    else:
                        res.append((m, "PASS", "unrelated: pronoun subject, no rule subject in window"))
                elif rule.get("heads") and re.search(r"\b(?:this|that|these|those|such|the same)\s+(?:\S+\s+){0,2}?(?:" + rule["heads"] + r")\W*$", subjseg, I):
                    res.append((m, "REVIEW", "R1 demonstrative noun phrase of the subject class; antecedent unresolved"))
                elif re.fullmatch(r"\W*" + GENERIC_HEAD + r"\W*", last, I) and sent_has_subj:
                    res.append((m, "REVIEW", "R2 copular subject has a generic head"))
                else:
                    res.append((m, "PASS", "unrelated: copular subject '%s'" % win[-40:]))
                continue
            if re.search(rule["subj"], after[:40], f) and not rule.get("copular_only"):
                # predicate then subject after a determiner/adverb gap ("exact free-level cone")
                v, why = governed(rule, sent, cl_off, cl, m.start(), m.end(), False)
                res.append((m, v, "attributive; " + why)); continue
            if sent_has_subj:
                res.append((m, "REVIEW", "R2 rule subject in sentence, binding unidentified"))
            else:
                res.append((m, "PASS", "unrelated: no rule subject bound"))
        return res
    if k == "verb":
        for m in re.finditer(r"(?<![\w-])(?:" + rule["verb"] + r")(?![\w-])", cl, f):
            after = cl[m.end():]
            if rule.get("obj") and not re.match(r"[^;]{0,60}?(?:" + rule["obj"] + ")", after, f):
                continue
            before = cl[:m.start()]
            sm = list(re.finditer(rule["subj"], before, f))
            negb = bool(re.search(r"(?:\b(?:does|do|did|can|could|would|will|need|must|is|are)\s+not|\bnot|"
                                  r"\bfail(?:s|ed|ing)? to|\brather than|\bnever)\s+(?:\w+\s+)?$", before, I))
            if sm:
                s = sm[-1]
                gap = before[s.end():]
                if len(gap.split()) > 8:
                    relx = re.search(r"((?:[\w-]+\s+){1,3})(?:that|which|who)\s+$", before, I)
                    if relx and not re.search(rule["subj"], relx.group(1), f):
                        res.append((m, "PASS", "unrelated: relative pronoun with antecedent '%s'" % relx.group(1).strip())); continue
                    if not negb:
                        gv, gwhy = governed(rule, sent, cl_off, cl, s.start(), m.end(), False)
                        if gv == "PASS":
                            res.append((m, "PASS", "binding undetermined, but governed if bound: " + gwhy)); continue
                        res.append((m, "REVIEW", "R2 rule subject in the clause beyond the binding distance")); continue
                    sm = []
                else:
                    detneg = bool(re.search(r"\b(?:no|nothing|neither|none)\s+$", before[:s.start()], I))
                    obj_pron = rule.get("obj") and re.match(r"\s*(?:it|this)\b", after, I)
                    v, why = governed(rule, sent, cl_off, cl, s.start(), m.end(), negb or detneg or neg_slot(gap))
                    if v == "FAIL" and obj_pron:
                        v, why = "REVIEW", "R1 object is a pronoun"
                    res.append((m, v, why)); continue
            if negb:
                res.append((m, "PASS", "G1 negated; subject elided")); continue
            if not before.strip() and prev_cl and re.search(rule["subj"], prev_cl, f):
                # VP coordination: the clause starts with the verb; inherit the preceding clause's subject
                v, why = governed(rule, sent, cl_off, cl, 0, m.end(), False)
                res.append((m, v, "inherited subject; " + why)); continue
            if re.match(r"\s*(?:nothing|no)\b", after, I):
                res.append((m, "PASS", "G1 negative object quantifier")); continue
            rel = re.search(r"((?:[\w-]+\s+){1,3})(?:that|which|who)\s+$", before, I)
            if rel and not re.search(rule["subj"], rel.group(1), f) and rel.group(1).split()[-1].lower() not in ("and", "but", "so", "not"):
                res.append((m, "PASS", "unrelated: relative pronoun with antecedent '%s'" % rel.group(1))); continue
            pv = re.findall(r"[A-Za-z$][\w$\\{}=-]*", before)
            if pv and not re.fullmatch(r"(?:it|this|which|that|and|but|also|then|therefore|thus|so)", pv[-1], I):
                if rule.get("foreign") == "review" and re.search(r"KMS|imaginary time|Euclidean", m.group(0)):
                    res.append((m, "REVIEW", "R2 claim-specific predicate with a subject outside the lexicon")); continue
                res.append((m, "PASS", "unrelated: verb has another subject")); continue
            if sent_has_subj or (window_has_subj and re.search(r"\b(?:it|this|which)\s+$", before, I)):
                res.append((m, "REVIEW", "R2 subject not bound to the verb"))
        return res
    if k == "passive":
        for m in re.finditer(rule["subj"], cl, f):
            before = cl[:m.start()]
            lm = re.search(rule["lead"], before, f)
            if not lm:
                continue
            negb = bool(re.search(r"(?:\bnot|\brather than|\bfail\w* to|\bno)\b[^;]{0,80}$", before[:lm.end()], I)
                        and re.search(NEG + r"|\bno\b", before[max(0, lm.start() - 40):lm.end()], I))
            v, why = governed(rule, sent, cl_off, cl, lm.start(), m.end(), negb)
            res.append((m, v, "passive/nominal; " + why))
        return res
    return res

HEAD_FRAME = re.compile(r"(?:does not|do not|did not) (?:claim|establish|show|prove)|not claimed|non-claims?|what is not (?:established|proved|claimed)", I)

def check_paragraph(par, prev="", heading=""):
    sents = sentences(par)
    par = par.replace("\n", " ").replace("\t", " ")
    prev = prev.replace("\n", " ")
    found = []
    for rule in RULES:
        f = fl(rule)
        subj = rule.get("subj")
        trig = {"adj": rule.get("pred"), "verb": rule.get("verb"), "passive": rule.get("subj"),
                "literal": rule.get("pat")}[rule["kind"]]
        if not re.search(trig, par, f):
            continue
        for sa, sb in sents:
            sent = par[sa:sb]
            sent_has = bool(subj and re.search(subj, sent, f))
            win_has = bool(subj and (re.search(subj, par, f) or re.search(subj, prev, f)))
            pc = ""
            for co, cl in clauses(sent):
                for m, v, why in check_clause(rule, par, sent, co, co, cl, win_has, sent_has, pc):
                    if v == "FAIL" and re.match(r"\W*That\s", sent):
                        if HEAD_FRAME.search(heading) or re.search(r":\s*$", prev.strip()[-3:] or "x") and HEAD_FRAME.search(prev):
                            v, why = "PASS", "G2 that-fragment under a negative-frame heading"
                        else:
                            v, why = "REVIEW", "R5 that-fragment without a visible matrix frame"
                    if v == "FAIL" and rule["kind"] != "literal":
                        o = co + m.start()
                        if any(q.start() < o < q.end() for q in re.finditer(r"`[^`]+`|\"[^\"]+\"|\u201c[^\u201d]+\u201d|\u00ab[^\u00bb]+\u00bb", sent)):
                            v, why = "REVIEW", "R4 assertion inside a quotation or code span (mention)"
                    found.append(dict(rule=rule["id"], verdict=v, why=why, offset=sa + co + m.start(),
                                      sentence=sent.strip(), match=m.group(0)))
                pc = cl
    # de-duplicate identical (rule, offset)
    seen, out = set(), []
    for x in found:
        key = (x["rule"], x["offset"], x["match"])
        if key not in seen:
            seen.add(key); out.append(x)
    return out

def scan_tree(root):
    res = []
    for dp, dn, fs in os.walk(root):
        dn.sort()
        for fn in sorted(fs):
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dp, fn); rel = os.path.relpath(p, root)
            text = open(p, encoding="utf-8", errors="replace").read()
            pos, prev, head = 0, "", ""
            for par in text.split("\n\n"):
                if par.lstrip().startswith("#"):
                    head = par.strip().splitlines()[0]
                for x in check_paragraph(par, prev, head):
                    x["rel"] = rel
                    x["line"] = text.count("\n", 0, pos + x["offset"]) + 1
                    x["sha256"] = hashlib.sha256(" ".join(x["sentence"].split()).encode()).hexdigest()
                    res.append(x)
                prev = par; pos += len(par) + 2
    return res

if __name__ == "__main__":
    if sys.argv[1] == "--controls":
        cs = json.load(open(sys.argv[2]))
        bad = 0
        for c in cs:
            fs = [x for x in check_paragraph(c["text"], c.get("context", "")) if x["rule"] == c["rule"]]
            order = {"FAIL": 2, "REVIEW": 1, "PASS": 0}
            v = max((x["verdict"] for x in fs), key=lambda z: order[z], default="PASS")
            ok = v == c["expect"]
            bad += not ok
            print(("ok  " if ok else "BAD ") + c["id"].ljust(14), c["expect"].ljust(6), v.ljust(6),
                  "; ".join(x["why"] for x in fs)[:150])
        print("mismatches:", bad, "of", len(cs))
    else:
        r = scan_tree(sys.argv[1])
        json.dump(r, open(sys.argv[2], "w"), indent=1)
        from collections import Counter
        print(Counter((x["rule"], x["verdict"]) for x in r))
