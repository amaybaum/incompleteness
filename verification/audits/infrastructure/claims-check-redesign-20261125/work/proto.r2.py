#!/usr/bin/env python3
"""Throwaway prototype of the revised withdrawn-claim checker (paper-only, Issue #1565, revision r2).

Not for the repository. Implements DESIGN-r2.md approximately with regular expressions, to measure
the design; an implementation is held to DESIGN-r2.md, not to this file.

Modes
  --controls FILE [--licences FILE]   print per-control verdicts; exit 0 iff no mismatch
  --self-test                          run every control file under the fixture and under the
                                       deployed (empty) licence file; validate the deployed licence file
  --scan ROOT --json OUT [--licences FILE] [--reviews FILE] [--repo GITDIR]
                                       scan every .md under ROOT; FAIL/REVIEW block only in active material
Exit status (scan and self-test): 0 clean; 1 confirmed violation (FAIL) in active material;
2 unresolved REVIEW in active material and no FAIL; 3 invalid or stale licence or review record;
4 self-test mismatch, usage error or internal error. Precedence 4 > 3 > 1 > 2.
"""
import re, sys, os, json, hashlib, subprocess

I = re.I
NEVER = r"(?!x)x"

# ------------------------------------------------------------------ rule data
# Subject and predicate lexicons are the frozen equivalence sets of DESIGN-r2 §3.11 (each derived from
# the rule's anchor). `near` holds the near-miss cue (DESIGN-r2 §3.12).
TEMP_SUBJ = (r"T_Q|T_\{?\\(?:rm|mathrm)\{?\s*dS\}?\}?|T_\{\\rm dS\}|T_\{\\rm H\}|"
             r"(?:Hawking|Gibbons[- ]Hawking|de Sitter|horizon|Unruh|KMS)\s+temperatures?|"
             r"temperatures? of the (?:de Sitter |black[- ]hole )?horizon|"
             r"thermality|thermal (?:ratio|spectrum|character)|the temperature")
TQ_PRED = (r"state[- ]independent|independent of the (?:quantum |choice of (?:the )?)?states?|"
           r"(?:the same|identical|unchanged) (?:in|for|across) (?:every|all|any|each) (?:[\w-]+ )?states?|"
           r"insensitive to the (?:quantum |choice of (?:the )?)?states?")
QM_SUBJ = r"\b(?:QM|quantum mechanics|quantum theory|the quantum formalism)\b"
OI_OBJ = r"(?:bare )?(?:OI\b|observation(?:al)? incompleteness)"
KDEG_SUBJ = (r"coupling[- ]degree minimi[sz]ation|minimi[sz]ation of the coupling degree|"
             r"minimi[sz]ing the coupling degree|coupling[- ]degree minimum")
GENERIC_HEAD = r"(?:quantity|quantities|value|values|one|result|answer|object|expression)"

RULES = [
 dict(id="W-GR-TQ-STATE", kind="adj", subj=TEMP_SUBJ, heads=r"temperatures?|thermality|ratio", pred=TQ_PRED,
      near=(TEMP_SUBJ + r"|\btemperatures?\b",
            r"\b(?:same|identical|unchanged|insensitive|universal|independent|irrespective|regardless|invariant)\b[^.;]{0,40}?\b(?:states?|vacua|vacuum)\b|"
            r"\b(?:every|all|any|each|whatever)\s+(?:[\w-]+\s+){0,2}?(?:states?|vacua)\b|\bstate[- ]?(?:independen\w*|blind|agnostic)")),
 dict(id="W-GR-TQ-STATE", kind="verb", subj=TEMP_SUBJ,
      verb=r"(?:does not|doesn't|do not) depend on|is independent of|are independent of|is insensitive to",
      obj=r"the (?:quantum |horizon |observer's |choice of (?:the )?)?states?\b", inherent_neg=True),
 dict(id="W-GR-THERM-KIN", kind="adj", subj=TEMP_SUBJ, heads=r"temperatures?|thermality|spectrum",
      pred=r"(?:purely|entirely|wholly|solely|merely) kinematic(?:al)?",
      near=(TEMP_SUBJ, r"\bkinematic\w*")),
 dict(id="W-GR-KMS", kind="verb",
      subj=r"\bany QFT|\bevery QFT|\beach QFT|\ball QFTs|\ban? QFT|\bany quantum field theory|\bevery quantum field theory|\bthe QFT",
      verb=(r"must (?:therefore )?(?:be|remain) (?:periodic|KMS|a KMS state|in a KMS state)|"
            r"is (?:necessarily |always )?(?:periodic in imaginary time|a KMS state|KMS\b)"),
      obj=None, flags=I, foreign="review",
      near=(r"\bQFTs?\b|quantum field theor\w*", r"\bKMS\b|periodic in imaginary time"), near_quant=True),
 dict(id="W-GR-CONE", kind="adj", subj=r"free-level (?:light )?cone", pred=r"exact(?: per channel)?",
      nongov=r"on the normalized \$d ?= ?3\$[^,;]*?branch", near=(r"free-level (?:light )?cone", r"\bexact\w*")),
 dict(id="W-GR-EPSKAPPA", kind="literal", pat=r"(\\v?arepsilon|\\epsilon)\s*\\kappa\s*/\s*c\b(?!\^)", flags=0),
 dict(id="W-BM-EUCLID", kind="verb",
      subj=r"cubic (?:equivariance|symmetry)|equivariance|projected memory|the (?:lattice|substratum|symmetry)|substratum symmetry",
      verb=r"(?:forc(?:es|ing|e)|impl(?:ies|y)|guarantees?|entails?) an? Euclidean", obj=None, foreign="review",
      qual=r"b_m", near=(r"cubic|equivariance|symmetry", r"\bEuclidean\b")),
 dict(id="W-BM-EUCLID", kind="adj", subj=r"(?:leading )?scalar propagation geometry|quadratic symbol",
      pred=r"Euclidean", copular_only=True, qual=r"b_m"),
 dict(id="W-KDEG", kind="verb", subj=KDEG_SUBJ,
      verb=(r"(?:fix(?:es|ing)?|determin(?:es?|ing)|select(?:s|ing)?|deriv(?:es?|ing)|forc(?:es?|ing)|establish(?:es|ing)?|"
            r"yield(?:s|ing)?|giv(?:es?|ing)|implies|produc(?:es?|ing)|picks? out|singles? out|entails?)"),
      obj=r"\$?K\b|2d|m\s*=\s*1|single-copy|\bsites?\b|carrier|six|it\b|this\b", flags=I,
      near=(r"coupling[- ]degree|minimi[sz]\w* (?:of )?the coupling", r"\$?K\s*=|\b2d\b|\bsix\b|m\s*=\s*1|\bsites?\b|\bcarrier")),
 dict(id="W-KDEG", kind="passive", subj=KDEG_SUBJ,
      lead=(r"(?:\$?K\s*=\s*(?:2d|6)\$?|\$m\s*=\s*1\$|the single-copy clause)\s*(?:follows|is (?:derived|fixed|selected|forced))\s+(?:from|by)\s*$|"
            r"\bderiv\w*\s+[^;]{0,80}?\bfrom\s*$|\b(?:consequence|result) of\s*$"), flags=I),
 dict(id="W-KDEG", kind="literal", pat=r"framework's answer is \$K = 2d", flags=0),
 dict(id="W-OI-REQ", kind="verb", subj=QM_SUBJ,
      verb=r"(?:requires?|needs?|presuppos(?:es|e)|depends? on|necessitates?|demands?|is impossible without|is not possible without)",
      obj=OI_OBJ, flags=I, qual=r"containment",
      near=(QM_SUBJ, r"\b(?:necessit\w*|entail\w*|impl(?:y|ies|ied)|demand\w*|forc\w*|presuppos\w*|depend\w*|rests? on|rel(?:y|ies) on|"
                     r"requir\w*|needs?|without|impossible|grounded|calls? for|mandat\w*|compel\w*)\b[^.;]{0,60}?" + OI_OBJ)),
 dict(id="W-OI-HIDDEN", kind="verb", subj=QM_SUBJ,
      verb=r"(?:requires?|needs?|presuppos(?:es|e)|depends? on|necessitates?)",
      obj=r"(?:an? )?hidden (?:information|variables?|states?|ontology|sub-quantum level|level)", flags=I,
      near=(QM_SUBJ, r"\b(?:necessit\w*|entail\w*|impl(?:y|ies)|demand\w*|presuppos\w*|depend\w*|rests? on|requir\w*|needs?)\b[^.;]{0,40}?hidden")),
 dict(id="W-OI-NOEXIST", kind="verb", subj=QM_SUBJ,
      verb=r"cannot exist without|could not exist without|would not exist without", obj=None, inherent_neg=True, flags=I),
 dict(id="W-OI-EXPLAINS", kind="verb", subj=r"\b(?:OI|observation(?:al)? incompleteness|ignorance)\b",
      verb=(r"(?:causes|produces|explains|generates|gives rise to|accounts for|underlies|"
            r"cause|produce|explain|generate|give rise to|account for|underlie)"),
      obj=r"\b(?:QM|quantum)", flags=I,
      near=(r"\b(?:OI|observation(?:al)? incompleteness)\b",
            r"\b(?:explain\w*|caus\w*|produc\w*|generat\w*|giv\w* rise|accounts? for|origin|source|underl\w*|yields?|deriv\w*)\b[^.;]{0,30}?\b(?:QM|quantum (?:mechanics|theory|structure))")),
 dict(id="W-OI-CONTRA", kind="literal",
      pat=r"\bwithout (?:OI|observation(?:al)? incompleteness) there (?:is|would be) no (?:QM|quantum)", flags=I),
]
RULE_IDS = sorted({r["id"] for r in RULES})

# ------------------------------------------------------------------ shared lexicons (DESIGN-r2 §3.4)
HYP_TOKEN = r"\bH-[A-Za-z][\w-]*"
HYP_GENERIC = (r"\b(?:conditional(?:ly)?|assum\w*|premise\w*|hypothes\w+|in the [\w-]+ sense|"
               r"on the [\w-]+ reading|under|if|given|provided|when|whenever|unless|on the [^,;]{0,40}?branch)\b")
NEG = r"\b(?:not|never|no longer|cannot|can't|fails? to|failing to|failed to|rather than)\b"
DISCOURSE_NOT = r"\bnot (?:surprisingly|coincidentally|only|least|just|unexpectedly)\b"
AUX = r"\b(?:is|are|was|were|be|been|has|have|had|does|do|did|can|could|will|would|may|might|must|shall|should)\b"
BOUNDARY = r";|:\s|\s—\s|,\s(?:and|but|while|whereas|so|though|although|yet|since|because)\s|\sbut\s"
SUBORD_NEXT = r",\s(?:since|because|though|although|while|whereas)\s"
COND_HEAD = r"(?:only\s+)?(?:if|when|whenever|under|given|assuming|provided(?:\s+that)?|once|in case|unless|so long as|as long as)"
G3_HEAD = r"(?:only\s+)?(?:if|when|under|given|assuming|provided(?:\s+that)?|in|on|for)"
CAUSAL_HEAD = r"(?:since|because|as|although|though|while|whereas|after|before|for|now that)"
STRENGTH_HEAD = r"(?:even|regardless|irrespective|independently|no matter|whether|with or without|without)"
NEGOP = (r"\b(?:without|even|regardless of|irrespective of|independently of|independent of|whether or not|or not|"
         r"with or without|stronger than|beyond|except|apart from|unless|not)\b")
NEGPOST = (r"\b(?:fails?|failing|failed|is violated|are violated|is dropped|is relaxed|does not hold|do not hold|"
           r"is not assumed|or not|is false|is absent)\b")

# G2 frames: a known matrix immediately before a that/whether/colon complementizer (or a zero
# complementizer for say/claim verbs).
FRAME_SRC = (
    r"(?:\bnot claimed\s*|\bno (?:statement|claim|evidence|proof|theorem|result|assertion|derivation)\s*|"
    r"\bit is (?:not (?:proved|shown|established|the case|true|known)|false|unproved|open|unknown|unclear)\s*|"
    r"\bis not proved\s*|\bunproved\s*|"
    r"\b(?:it )?(?:has|have) not been (?:shown|proved|established|derived|demonstrated)\s*|"
    r"\b(?:no|neither|none of|nothing in|nobody|no one|nothing)\b[^;:,]{0,60}?\b(?:(?:has|have|yet)\s+)?"
    r"(?:shows?|shown|proves?|proved|establish(?:es|ed)?|derives?|derived|says?|implies|demonstrates?|demonstrated)\s*|"
    r"\b(?:does|do|did) not (?:show|establish|prove|imply|say|claim|assert|state)\s*|"
    r"\bthe (?:open )?question (?:of )?)")
KNOWN_FRAME = re.compile(FRAME_SRC + "$", I)
KNOWN_ANY = re.compile(FRAME_SRC + r"(?:\bthat\b|:|\s)", I)
ZERO_COMP_FRAME = re.compile(r"\b(?:does|do|did) not (?:say|claim|assert|state|show)\s+$", I)
CLAIM_NOUN = re.compile(r"\bthe (?:claim|statement|reading|assertion|conjecture|thesis|view|idea|suggestion)\s*$", I)
FRAME_POST = re.compile(r"^[^;]*?\b(?:is|was|remains)\s+(?:withdrawn|false|unproved|not proved|not established|"
                        r"unsupported|not a theorem|open|refuted)\b", I)
AFFIRMING = re.compile(r"(?:\b(?:do|does|did) not doubt|\bno doubt|\bnot surprising|\bcannot be doubted|\bundeniabl\w*)\b[^;:]*$", I)
NONFACTIVE_CUE = re.compile(
    r"\b(?:not|no|never|nobody|nothing|none|neither|nor|false|doubt\w*|den(?:y|ies|ied)|unclear|unknown|open|"
    r"unproved|unestablished|unsupported|conjectur\w*|hypothes\w*|suppos\w*|might|may|could|would|claim\w*|"
    r"argu\w*|suggest\w*|believ\w*|propos\w*|ask\w*|question\w*|hop\w*|speculat\w*|wonder\w*)\b", I)
HEAD_FRAME = re.compile(r"(?:does not|do not|did not) (?:claim|establish|show|prove)|not claimed|non-claims?|"
                        r"what is not (?:established|proved|claimed)", I)
COPULA = re.compile(r"\b(?:is|are|was|were|be|been|being|remains?|becomes?|stays?)\b((?:\s+(?!state)[\w-]+){0,3}?)\s*$", I)

# ------------------------------------------------------------------ licences (DESIGN-r2 §3.6)
HEX40 = re.compile(r"^[0-9a-f]{40}$")

def load_licences(path):
    if not path:
        return {"fixture": False, "entries": []}
    return json.load(open(path, encoding="utf-8"))

def validate_licences(L, repo=None):
    """Return a list of problems; an entry without an anchor quotation and an independent review is invalid."""
    probs = []
    if L.get("schema") not in (None, "claims-licences/1"):
        probs.append("unknown schema")
    for i, e in enumerate(L.get("entries", [])):
        tag = "licence[%d]" % i
        if e.get("rule") not in RULE_IDS:
            probs.append(tag + ": unknown rule")
        try:
            re.compile(e.get("qualifier", ""))
        except re.error:
            probs.append(tag + ": qualifier does not compile")
        if not e.get("qualifier"):
            probs.append(tag + ": empty qualifier")
        a = e.get("anchor") or {}
        if not (a.get("path") and a.get("quote") and HEX40.match(a.get("revision", ""))):
            probs.append(tag + ": anchor needs path, quotation and a full commit revision")
        r = e.get("review") or {}
        if not (r.get("reviewer") and r.get("record") and r.get("date") and HEX40.match(r.get("revision", ""))):
            probs.append(tag + ": no independent scientific review record (reviewer, record, date, revision)")
        elif r.get("reviewer") == e.get("proposer"):
            probs.append(tag + ": reviewer is the proposer")
        if repo and a.get("revision"):
            if not git_is_ancestor(repo, a["revision"]):
                probs.append(tag + ": anchor revision is not an ancestor of the main ref")
            else:
                try:
                    blob = subprocess.run(["git", "-C", repo, "show", a["revision"] + ":" + a["path"]],
                                          capture_output=True, text=True, check=True).stdout
                    if " ".join(a["quote"].split()) not in " ".join(blob.split()):
                        probs.append(tag + ": anchor quotation not found at its revision")
                except subprocess.CalledProcessError:
                    probs.append(tag + ": anchor path missing at its revision")
    return probs

def lic_regex(L, rule_id):
    q = [e["qualifier"] for e in L.get("entries", []) if e.get("rule") == rule_id]
    return "|".join("(?:%s)" % x for x in q) if q else NEVER

MAIN_REF = ["HEAD"]

def git_is_ancestor(repo, rev):
    try:
        return subprocess.run(["git", "-C", repo, "merge-base", "--is-ancestor", rev, MAIN_REF[0]],
                              capture_output=True).returncode == 0
    except OSError:
        return False

# ------------------------------------------------------------------ segmentation (DESIGN-r2 §3.2)
MASK = re.compile(r"\$\$.*?\$\$|\$[^$]*\$|`[^`]*`", re.S)

def masked(s):
    return MASK.sub(lambda m: re.sub(r"[.;:,!?()—]", "\x00", m.group(0)), s)

ABBR = re.compile(r"\b(?:e\.g|i\.e|cf|vs|et al|Fig|Eq|Ref|resp|approx|No)\.$")

def sentences(par):
    m = masked(par)
    out, start = [], 0
    for x in re.finditer(r"(?:[.!?][\"'”)\]]*(?:\*\*|\*)?|\.\$\$|\x00\$\$|\$\$|\$\\(?:square|blacksquare|Box)\$|∎)(?=\s+[A-Z*_`$\[(\"'“]|\s*$)|\s\|(?=\s)|\n(?=\s*(?:[-*+]\s|\d+\.\s|\||\$\$))", m):
        end = x.end()
        if ABBR.search(m[start:x.start() + 1]):
            continue
        out.append((start, end)); start = end
    if start < len(par):
        out.append((start, len(par)))
    return [(a, b) for a, b in out if par[a:b].strip()]

def clauses(sent):
    """(offset, text, is_extracted) triples. Parentheticals, dash pairs and comma-relative clauses are
    their own clauses; the remainder is split at the clause boundaries of BOUNDARY."""
    m = masked(sent)
    spans, blank = [], list(m)
    for rx in (r"\([^()]*\)", r"\s—\s[^—]*?\s—\s", r",\s(?:which|whose|who|where)\b[^,;]*(?=,|;|$)"):
        for x in re.finditer(rx, m):
            if any(blank[i] == "\x01" for i in range(x.start(), x.end())):
                continue
            spans.append((x.start(), x.end()))
            for i in range(x.start(), x.end()):
                blank[i] = "\x01"
    rem = "".join(blank)
    cuts = [0]
    for x in re.finditer(BOUNDARY, rem):
        cuts += [x.start(), x.end()]
    cuts.append(len(rem))
    out = []
    for i in range(0, len(cuts), 2):
        a, b = cuts[i], cuts[i + 1]
        out.append((a, "".join(sent[k] if rem[k] != "\x01" else " " for k in range(a, b)), False))
    for a, b in spans:
        out.append((a, sent[a:b], True))
    return out

# ------------------------------------------------------------------ governance (DESIGN-r2 §3.4)
def fl(r):
    return r.get("flags", I) if r["kind"] != "literal" else r.get("flags", 0)

def neg_slot(between):
    b = re.sub(DISCOURSE_NOT, "", between, flags=I)
    return re.search(NEG, b, I) is not None

def frame(sent, s_subj, s_end):
    """G2 / R7 decision from the complement position of the subject. Returns (verdict, why) or None."""
    pre = sent[:s_subj]
    pm = masked(pre)
    if ZERO_COMP_FRAME.search(re.sub(r"(?:\b(?:the|a|an|every|any)\s+)$", "", pre, flags=I)):
        return "PASS", "G2 subject is the immediate complement of a negative say/claim frame"
    m = re.search(r"(?:\b(that|whether)\b|(:))((?:(?!\bthat\b|\bwhether\b)[^;:])*)$", pm, I)
    if not m:
        return None
    between = pre[m.start(3):]
    if (len(between.split()) > 6 or re.search(BOUNDARY, masked(between)) or re.search(AUX, between, I)):
        return None                                   # A is not the immediate complement
    comp = (m.group(1) or ":").lower()
    matrix = pre[:m.start()]
    if re.search(r"\bnot claimed[^:;]{0,40}:\s*$", matrix, I) and comp == "that":
        return "PASS", "G2 subject is the immediate complement of 'not claimed:'"
    mm = masked(matrix)
    cut = max([x.end() for x in re.finditer(BOUNDARY, mm)] + [0])
    local = matrix[cut:]
    if comp == "whether":
        if re.match(r"\s*or not\b", between, I):
            return None
        return "PASS", "G2 subject is the immediate complement of whether"
    if comp == ":" and not re.search(r"\bnot claimed[^:;]{0,40}$", local, I):
        return None
    if KNOWN_FRAME.search(local):
        return "PASS", "G2 subject is the immediate complement of a negative frame"
    if re.search(r"(?:,\s*|\s)(?:and|or|nor)\s+$", local):
        # coordinated complement: a known frame earlier in the same clause chain governs every conjunct
        if KNOWN_ANY.search(local) or re.search(r"\b(?:does|do|did) not (?:say|claim|assert|state|show)\s", local, I):
            return "PASS", "G2 coordinated complement of a negative frame"
    if comp == "that" and CLAIM_NOUN.search(local):
        if FRAME_POST.search(sent[s_end:]):
            return "PASS", "G2 the claim that A is withdrawn/false/unproved"
        return "REVIEW", "R7 assertion is the complement of a claim noun without a negative predicate"
    if AFFIRMING.search(local):
        return "AFFIRM", "double negation affirms"                                   # double negation affirms: treated as asserted
    if NONFACTIVE_CUE.search(local):
        return "REVIEW", "R7 unknown negative or non-factive frame governs the complement"
    return None

def qualifier_rx(rule, lic):
    parts = [HYP_TOKEN]
    if lic != NEVER:
        parts.append(lic)
    if rule.get("qual"):
        parts.append(rule["qual"])
    return "(?:" + "|".join(parts) + ")"

def r6(text, qual):
    return re.search(NEGOP + r"[^,;:.]{0,40}?" + qual, text, I) or \
        re.search(qual + r"[^,;:.]{0,30}?" + NEGPOST, text, I)

def g3_heading(seg, lic):
    return lic != NEVER and re.match(r"\s*\**\s*" + G3_HEAD + r"\s+(?:that\s+)?(?:the\s+)?\$?(?:" + lic + r")", seg, I)

def g3_post(tail, lic):
    return lic != NEVER and re.match(r"[^,;]{0,80}?\b" + G3_HEAD + r"\s+(?:the\s+)?\$?(?:" + lic + r")", tail, I)

def strip_nongov(t, rule):
    t = re.sub(DISCOURSE_NOT, "", t, flags=I)
    t = re.sub(r"\bunconditional\w*", "", t, flags=I)
    if rule.get("nongov"):
        t = re.sub(rule["nongov"], "", t, flags=I)
    return t

def governed(rule, lic, sent, c_off, cl, a_start, a_end, neg_between):
    """('PASS'|'REVIEW'|'FAIL', why) for a bound assertion A = cl[a_start:a_end]."""
    if neg_between:
        return "PASS", "G1 negation in the assertion's slot"
    f = frame(sent, c_off + a_start, c_off + a_end)
    affirm = bool(f) and f[0] == "AFFIRM"
    if f and not affirm:
        return f
    qual = qualifier_rx(rule, lic)
    q3 = qualifier_rx(dict(rule, qual=None), lic)
    lead, tail = cl[:a_start], cl[a_end:]
    # a sentence-initial antecedent of an earlier clause scopes over A when no ; or : intervenes
    s_lead = sent[:c_off]
    if c_off and not re.search(r";|:\s", masked(s_lead)):
        lead = s_lead + lead
    lm = masked(lead)
    commas = [x.start() for x in re.finditer(r",", lm)]
    segs, prev = [], 0
    for c in commas:
        segs.append(lead[prev:c]); prev = c + 1
    near = lead[prev:]
    g3, r3, r6hit = None, None, None
    for seg in segs + [near]:
        s = strip_nongov(seg, rule)
        if not s.strip():
            continue
        if r6(s, qual):
            r6hit = r6hit or "R6 negated or contrasted qualifier before A"
            continue
        head = re.match(r"\s*\**\s*(\w+(?:\s+\w+)?)", s)
        hw = head.group(1).lower() if head else ""
        if affirm and seg is near:
            continue
        if re.match(COND_HEAD + r"\b", s.strip(" *"), I):
            if g3_heading(s, lic):
                g3 = g3 or "G3 licensed qualifier heads the antecedent"
            else:
                r3 = r3 or "R3 condition naming no licensed qualifier"
        elif re.match(r"(?:" + CAUSAL_HEAD + "|" + STRENGTH_HEAD + r")\b", s.strip(" *"), I):
            if re.search(q3, s, I) or re.search(HYP_GENERIC, s, I):
                r3 = r3 or "R3 qualifier in a non-conditional antecedent"
        else:
            if g3_heading(s, lic):
                g3 = g3 or "G3 licensed scope phrase heads the antecedent"
            elif re.search(q3, s, I) or re.search(HYP_GENERIC, s, I):
                r3 = r3 or "R3 qualifier in A's clause not in a governing position"
            elif seg is near and re.search(NEG, re.sub(DISCOURSE_NOT, "", s, flags=I), I):
                r3 = r3 or "R3 negation in the clause outside the assertion's slot"
    rest = sent[c_off + len(cl):]
    nx = re.match(SUBORD_NEXT, masked(rest))
    if nx:                                          # a following since/because/though clause comments on A
        nb = re.search(BOUNDARY, masked(rest)[nx.end():])
        tail = tail + rest[:nx.end() + (nb.start() if nb else len(rest))]
    t = strip_nongov(tail, rule)
    if r6(t, qual):
        r6hit = r6hit or "R6 negated or contrasted qualifier after A"
    elif g3_post(t, lic):
        g3 = g3 or "G3 licensed qualifier heads a post-posed restrictor"
    elif re.search(q3, t, I) or re.search(HYP_GENERIC, t, I):
        r3 = r3 or "R3 qualifier after A not in a governing position"
    if r6hit:
        return "REVIEW", r6hit
    if g3:
        return "PASS", g3
    if r3:
        return "REVIEW", r3
    return "FAIL", "asserted; no governing qualifier"

# ------------------------------------------------------------------ binding (DESIGN-r2 §3.3)
def rel_antecedent(sent, c_off, rule, f):
    """For a clause that is a comma-relative clause, the noun phrase before it binds 'which'."""
    before = sent[:c_off]
    toks = before.split()[-5:]
    return bool(re.search(rule["subj"], " ".join(toks), f))

def check_clause(rule, lic, sent, c_off, cl, extracted, win_has, sent_has, prev_cl=""):
    res, f, k = [], fl(rule), rule["kind"]
    if k == "literal":
        for m in re.finditer(rule["pat"], cl, f):
            if rule["id"] == "W-GR-EPSKAPPA":
                res.append((m, "FAIL", "formula error; no qualifier repairs it"))
            else:
                res.append((m,) + governed(rule, NEVER, sent, c_off, cl, m.start(), m.end(),
                                           bool(re.search(r"\bis not\b", m.group(0)))))
        return res
    if k == "adj":
        for m in re.finditer(r"(?<![\w-])(?:" + rule["pred"] + r")(?![\w-])", cl, f):
            after, before = cl[m.end():], cl[:m.start()]
            att = re.match(r"\s+((?:[\w$\\{}^_-]+\s*){1,3})", after)
            cop = COPULA.search(before)
            if not rule.get("copular_only") and att and not cop:
                head = att.group(1)
                if re.search(rule["subj"], head, f):
                    v, why = governed(rule, lic, sent, c_off, cl, m.start(), m.end(),
                                      bool(re.search(r"\b(?:no|not|rather than)\s+(?:an?\s+)?$", before, I)))
                    res.append((m, v, "attributive; " + why))
                elif re.match(r"\s*" + GENERIC_HEAD, head, I) and win_has:
                    res.append((m, "REVIEW", "R1 attributive head is generic; subject unresolved"))
                else:
                    res.append((m, "PASS", "unrelated: predicate modifies '%s'" % head.strip()[:40]))
                continue
            if rule.get("copular_only") and not cop:
                continue
            caus = re.search(r"\b(nothing|no \w+)?\s*\b(?:(?:does|do|did|can) not\s+)?(?:makes?|renders?|keeps?|make|render)\s+((?:\S+\s+){0,3}?)$", before, I)
            if caus and re.search(rule["subj"], caus.group(2), f):
                neg = bool(caus.group(1)) or bool(re.search(r"\bnot\b", caus.group(0), I))
                v, why = governed(rule, lic, sent, c_off, cl, caus.start(), m.end(), neg)
                res.append((m, v, "causative; " + why)); continue
            if cop:
                subjseg, between = before[:cop.start()], cop.group(0)
                toks = re.findall(r"[^\s]+", subjseg)
                win, last = " ".join(toks[-7:]), (toks[-1] if toks else "")
                if re.search(rule["subj"], win, f) or (re.search(rule["subj"], subjseg, f) and len(toks) <= 12):
                    if re.fullmatch(r"\W*" + GENERIC_HEAD + r"\W*", last, I):
                        res.append((m, "REVIEW", "R2 copular subject has a generic head")); continue
                    sm = list(re.finditer(rule["subj"], subjseg, f))
                    neg = neg_slot(between) or bool(re.search(r"\b(?:no|nothing|neither|none)\s+(?:\w+\s+){0,1}$",
                                                              subjseg[:sm[0].start()], I))
                    v, why = governed(rule, lic, sent, c_off, cl, sm[-1].start(), m.end(), neg)
                    res.append((m, v, "copular; " + why))
                elif extracted and re.fullmatch(r"\W*which\W*", last, I) and rel_antecedent(sent, c_off, rule, f):
                    # relative pronoun resolves to the noun phrase before the relative clause (nit §3.3)
                    v, why = governed(rule, lic, sent, c_off, cl, cop.start(), m.end(), neg_slot(between))
                    res.append((m, v, "copular, relative pronoun bound to the rule subject; " + why))
                elif re.fullmatch(r"\W*(?:it|this|that|these|they|which|both|each)\W*", last, I) or not toks:
                    if neg_slot(between):
                        res.append((m, "PASS", "G1 negated; subject unresolved"))
                    elif win_has:
                        res.append((m, "REVIEW", "R1 pronoun/elided subject; rule subject in window"))
                    else:
                        res.append((m, "PASS", "unrelated: pronoun subject, no rule subject in window"))
                elif rule.get("heads") and re.search(r"\b(?:this|that|these|those|such|the same)\s+(?:\S+\s+){0,2}?(?:" + rule["heads"] + r")\W*$", subjseg, I):
                    res.append((m, "REVIEW", "R1 demonstrative noun phrase of the subject class"))
                elif re.fullmatch(r"\W*" + GENERIC_HEAD + r"\W*", last, I) and sent_has:
                    res.append((m, "REVIEW", "R2 copular subject has a generic head"))
                else:
                    res.append((m, "PASS", "unrelated: copular subject '%s'" % win[-40:]))
                continue
            if re.search(rule["subj"], after[:40], f) and not rule.get("copular_only"):
                v, why = governed(rule, lic, sent, c_off, cl, m.start(), m.end(), False)
                res.append((m, v, "attributive; " + why)); continue
            if sent_has:
                res.append((m, "REVIEW", "R2 rule subject in sentence, binding unidentified"))
            else:
                res.append((m, "PASS", "unrelated: no rule subject bound"))
        return res
    if k == "verb":
        for m in re.finditer(r"(?<![\w-])(?:" + rule["verb"] + r")(?![\w-])", cl, f):
            after, before = cl[m.end():], cl[:m.start()]
            if rule.get("obj") and not re.match(r"[^;]{0,60}?(?:" + rule["obj"] + ")", after, f):
                continue
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
                        gv, gwhy = governed(rule, lic, sent, c_off, cl, s.start(), m.end(), False)
                        if gv == "PASS":
                            res.append((m, "PASS", "binding undetermined, but governed if bound: " + gwhy)); continue
                        res.append((m, "REVIEW", "R2 rule subject in the clause beyond the binding distance")); continue
                    sm = []
                else:
                    detneg = bool(re.search(r"\b(?:no|nothing|neither|none)\s+$", before[:s.start()], I))
                    obj_pron = rule.get("obj") and re.match(r"\s*(?:it|this)\b", after, I)
                    v, why = governed(rule, lic, sent, c_off, cl, s.start(), m.end(), negb or detneg or neg_slot(gap))
                    if v == "FAIL" and obj_pron:
                        v, why = "REVIEW", "R1 object is a pronoun"
                    res.append((m, v, why)); continue
            if negb:
                res.append((m, "PASS", "G1 negated; subject elided")); continue
            if not before.strip() and prev_cl and re.search(rule["subj"], prev_cl, f):
                v, why = governed(rule, lic, sent, c_off, cl, 0, m.end(), False)
                res.append((m, v, "inherited subject; " + why)); continue
            if re.match(r"\s*(?:nothing|no)\b", after, I):
                res.append((m, "PASS", "G1 negative object quantifier")); continue
            rel = re.search(r"((?:[\w-]+\s+){1,3})(?:that|which|who)\s+$", before, I)
            if rel and not re.search(rule["subj"], rel.group(1), f) and rel.group(1).split()[-1].lower() not in ("and", "but", "so", "not"):
                res.append((m, "PASS", "unrelated: relative pronoun with antecedent '%s'" % rel.group(1).strip())); continue
            pv = re.findall(r"[A-Za-z$][\w$\\{}=-]*", before)
            if pv and not re.fullmatch(r"(?:it|this|which|that|and|but|also|then|therefore|thus|so)", pv[-1], I):
                if rule.get("foreign") == "review" and re.search(r"KMS|imaginary time|Euclidean", m.group(0)):
                    res.append((m, "REVIEW", "R2 claim-specific predicate with a subject outside the lexicon")); continue
                res.append((m, "PASS", "unrelated: verb has another subject")); continue
            if sent_has or (win_has and re.search(r"\b(?:it|this|which)\s+$", before, I)):
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
            v, why = governed(rule, NEVER, sent, c_off, cl, lm.start(), m.end(), negb)
            res.append((m, v, "passive/nominal; " + why))
        return res
    return res

# ------------------------------------------------------------------ near-miss scan (DESIGN-r2 §3.12)
def near_miss(rule, sent):
    """REVIEW when a rule subject term precedes a rule-specific cue in one clause with no template match."""
    if not rule.get("near"):
        return None
    subj, cue = rule["near"]
    for c_off, cl, _ in clauses(sent):
        for s in re.finditer(subj, cl, I):
            if re.match(r"['\u2019]s\b", cl[s.end():]):
                continue
            c = re.search(cue, cl[s.end():], I)
            if not c:
                continue
            if rule.get("near_quant") and not re.search(r"\b(?:any|every|each|all)\b", cl[max(0, s.start() - 12):s.end()], I):
                continue
            span = cl[s.end():s.end() + c.end()]
            pre = sent[:c_off + s.start()]
            if re.search(NEG, re.sub(DISCOURSE_NOT, "", span, flags=I), I) or \
                    re.search(r"\b(?:no|nothing|neither|none)\s+(?:\w+\s+){0,1}$", cl[:s.start()], I):
                return ("PASS", "near-miss negated in the slot", s.start() + c_off)
            fr = frame(sent, c_off + s.start(), c_off + s.end() + c.end())
            if fr and fr[0] == "PASS":
                return ("PASS", "near-miss inside a negative frame", s.start() + c_off)
            return ("REVIEW", "N1 near-miss: rule subject with a rule cue outside the equivalence set", s.start() + c_off)
    return None

# ------------------------------------------------------------------ paragraph driver
QUOTE = re.compile(r"`[^`]+`|\"[^\"]+\"|“[^”]+”|«[^»]+»")

def check_paragraph(par, prev="", heading="", L=None, only=None):
    L = L or {"entries": []}
    sents = sentences(par)
    par = par.replace("\n", " ").replace("\t", " ")
    prev = prev.replace("\n", " ")
    found = []
    by_rule_sent = set()
    rules = [r for r in RULES if only is None or r["id"] == only]
    for rule in rules:
        f, subj = fl(rule), rule.get("subj")
        lic = lic_regex(L, rule["id"])
        trig = {"adj": rule.get("pred"), "verb": rule.get("verb"), "passive": rule.get("subj"),
                "literal": rule.get("pat")}[rule["kind"]]
        if not re.search(trig, par, f):
            continue
        for sa, sb in sents:
            sent = par[sa:sb]
            sent_has = bool(subj and re.search(subj, sent, f))
            win_has = bool(subj and (re.search(subj, par, f) or re.search(subj, prev, f)))
            pc = ""
            for co, cl, ex in clauses(sent):
                for m, v, why in check_clause(rule, lic, sent, co, cl, ex, win_has, sent_has, pc):
                    if v == "FAIL" and re.match(r"\W*That\s", sent):
                        if HEAD_FRAME.search(heading) or (prev.strip().endswith(":") and HEAD_FRAME.search(prev)):
                            v, why = "PASS", "G2 that-fragment under a negative-frame heading"
                        else:
                            v, why = "REVIEW", "R5 that-fragment without a visible matrix frame"
                    if v == "FAIL" and rule["kind"] != "literal":
                        o = co + m.start()
                        if any(q.start() < o < q.end() for q in QUOTE.finditer(sent)):
                            v, why = "REVIEW", "R4 assertion inside a quotation or code span (mention)"
                    found.append(dict(rule=rule["id"], verdict=v, why=why, offset=sa + co + m.start(),
                                      sentence=sent.strip(), match=m.group(0)))
                    if not why.startswith("unrelated"):
                        by_rule_sent.add((rule["id"], sa))
                pc = cl
    for rule in rules:
        if not rule.get("near"):
            continue
        if not (re.search(rule["near"][0], par, I) and re.search(rule["near"][1], par, I)):
            continue
        for sa, sb in sents:
            if (rule["id"], sa) in by_rule_sent:
                continue
            nm = near_miss(rule, par[sa:sb])
            if nm:
                v, why, o = nm
                if v == "REVIEW" and re.match(r"\W*That\s", par[sa:sb]) and \
                        (HEAD_FRAME.search(heading) or (prev.strip().endswith(":") and HEAD_FRAME.search(prev))):
                    v, why = "PASS", "G2 near-miss that-fragment under a negative-frame heading"
                found.append(dict(rule=rule["id"], verdict=v, why=why, offset=sa + o,
                                  sentence=par[sa:sb].strip(), match="(near-miss)"))
                by_rule_sent.add((rule["id"], sa))
    seen, out = set(), []
    for x in found:
        key = (x["rule"], x["offset"], x["match"])
        if key not in seen:
            seen.add(key); out.append(x)
    return out

ORDER = {"FAIL": 2, "REVIEW": 1, "PASS": 0}

def verdict_for(text, rule_id, context="", L=None):
    fs = [x for x in check_paragraph(text, context, "", L, only=rule_id) if x["rule"] == rule_id]
    v = max((x["verdict"] for x in fs), key=lambda z: ORDER[z], default="PASS")
    return v, fs

# ------------------------------------------------------------------ scan scope (DESIGN-r2 §3.9)
RECORD_HEADING = re.compile(r"^##\s+.*\(record\)\s*$")

def classify(rel):
    """'active', 'agents' (AGENTS.md: per section) or 'record'."""
    if rel.startswith("papers/") or rel.startswith("book/"):
        return "active"
    if rel == "AGENTS.md":
        return "agents"
    base = rel.rsplit("/", 1)[-1]
    if base == "README.md" and (not rel.startswith("verification/") or rel == "verification/README.md"):
        return "active"
    return "record"

def norm_hash(s):
    return hashlib.sha256(" ".join(s.split()).encode()).hexdigest()

def scan_tree(root, L):
    res = []
    for dp, dn, fs in os.walk(root):
        dn.sort()
        if ".git" in dn:
            dn.remove(".git")
        for fn in sorted(fs):
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dp, fn); rel = os.path.relpath(p, root).replace(os.sep, "/")
            cls = classify(rel)
            text = open(p, encoding="utf-8", errors="replace").read()
            pos, prev, head, h2_record = 0, "", "", False
            for par in text.split("\n\n"):
                first = par.lstrip().splitlines()[0] if par.strip() else ""
                if first.startswith("#"):
                    head = first.strip()
                if first.startswith("## "):
                    h2_record = bool(RECORD_HEADING.match(first.strip()))
                active = cls == "active" or (cls == "agents" and not h2_record)
                for x in check_paragraph(par, prev, head, L):
                    x["path"] = rel
                    x["active"] = active
                    x["line"] = text.count("\n", 0, pos + x["offset"]) + 1
                    x["sentence_sha256"] = norm_hash(x["sentence"])
                    x["window_sha256"] = norm_hash(prev + "\n\n" + par)
                    res.append(x)
                prev = par; pos += len(par) + 2
    return res

# ------------------------------------------------------------------ review records (DESIGN-r2 §3.7)
WINDOW_CODES = ("R1", "R5", "N1")

def apply_reviews(findings, R, repo=None):
    probs, used = [], set()
    recs = R.get("records", []) if R else []
    for i, r in enumerate(recs):
        tag = "review[%d]" % i
        need = ("rule", "path", "sentence_sha256", "sentence", "code", "decision", "reason", "reviewer", "revision", "date", "authority")
        miss = [k for k in need if not r.get(k)]
        if miss:
            probs.append(tag + ": missing " + ",".join(miss)); continue
        if r["decision"] not in ("governed", "unrelated", "mention"):
            probs.append(tag + ": decision must be governed, unrelated or mention"); continue
        if not HEX40.match(r["revision"]):
            probs.append(tag + ": revision is not a full commit id"); continue
        if repo and not git_is_ancestor(repo, r["revision"]):
            probs.append(tag + ": revision is not an ancestor of the main ref"); continue
        if r["code"] in WINDOW_CODES and not r.get("window_sha256"):
            probs.append(tag + ": code %s needs window_sha256" % r["code"]); continue
        hit = None
        for j, x in enumerate(findings):
            if (x["rule"], x["path"], x["sentence_sha256"]) == (r["rule"], r["path"], r["sentence_sha256"]):
                if x["verdict"] == "FAIL":
                    probs.append(tag + ": a review record cannot resolve a FAIL"); hit = -1; break
                if x["verdict"] == "REVIEW" and x["why"].split()[0] == r["code"] and \
                        (r["code"] not in WINDOW_CODES or x["window_sha256"] == r["window_sha256"]):
                    hit = j
        if hit is None:
            probs.append(tag + ": stale (no matching REVIEW finding at this tree)")
        elif hit >= 0:
            findings[hit]["resolved_by"] = i; used.add(hit)
    return probs

# ------------------------------------------------------------------ self-test
CONTROL_FILES = ["controls.json", "heldout.json", "controls_c.json", "controls_d.json",
                 "reviewer-heldout.json", "controls_r2.json"]

def run_controls(path, L, empty, quiet=False):
    cs = json.load(open(path, encoding="utf-8"))
    bad, rows = 0, []
    for c in cs:
        v, fs = verdict_for(c["text"], c["rule"], c.get("context", ""), L)
        exp = c["expect"]
        ve, fse = verdict_for(c["text"], c["rule"], c.get("context", ""), empty)
        # under the empty deployed licence file a G3 PASS becomes REVIEW; nothing else may change
        g3 = exp == "PASS" and any(x["why"].split()[0] == "G3" or "G3" in x["why"] for x in fs)
        exp_e = "REVIEW" if (g3 and exp == "PASS") else exp
        ok = v == exp and ve == exp_e
        bad += not ok
        rows.append((ok, c["id"], exp, v, exp_e, ve, "; ".join(x["why"] for x in fs)[:140]))
    if not quiet:
        for ok, cid, exp, v, exp_e, ve, why in rows:
            print(("ok  " if ok else "BAD ") + cid.ljust(14), exp.ljust(6), v.ljust(6), "| empty:", exp_e.ljust(6), ve.ljust(6), why)
        print("mismatches:", bad, "of", len(cs))
    return bad, rows

def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    a = argv[1:]
    def opt(name, default=None):
        return a[a.index(name) + 1] if name in a else default
    if not a:
        print(__doc__); return 4
    if a[0] == "--controls":
        Lf = load_licences(opt("--licences", os.path.join(here, "licences-fixture.json")))
        bad, _ = run_controls(a[1], Lf, load_licences(os.path.join(here, "licences.json")))
        return 0 if bad == 0 else 4
    if a[0] == "--self-test":
        dep = load_licences(os.path.join(here, "licences.json"))
        probs = validate_licences(dep)
        if dep.get("fixture"):
            probs.append("deployed licence file is a fixture")
        fx = load_licences(os.path.join(here, "licences-fixture.json"))
        if not fx.get("fixture"):
            probs.append("fixture file is not marked as a fixture")
        if any(re.search(e["qualifier"], "H-slope") for e in fx.get("entries", [])):
            probs.append("fixture licenses H-slope")
        total = 0
        for fn in CONTROL_FILES:
            p = os.path.join(here, fn)
            if os.path.exists(p):
                b, rows = run_controls(p, fx, dep, quiet=True)
                total += b
                print(fn.ljust(24), "controls", len(rows), "mismatches", b)
        for x in probs:
            print("LICENCE", x)
        if probs:
            return 3
        return 0 if total == 0 else 4
    if a[0] == "--scan":
        Lpath = opt("--licences", os.path.join(here, "licences.json"))
        try:
            L = load_licences(Lpath)
        except (OSError, ValueError) as e:
            print("LICENCE file unreadable:", e); return 3
        if L.get("fixture"):
            print("refusing a fixture licence file for a scan"); return 3
        repo = opt("--repo")
        MAIN_REF[0] = opt("--main", "HEAD")
        probs = validate_licences(L, repo)
        findings = scan_tree(a[1], L)
        try:
            R = json.load(open(opt("--reviews"), encoding="utf-8")) if opt("--reviews") else None
        except (OSError, ValueError) as e:
            print("RECORD review file unreadable:", e); return 3
        probs += apply_reviews(findings, R, repo)
        from collections import Counter
        cnt = Counter(("active" if x["active"] else "record", x["verdict"] if "resolved_by" not in x else "REVIEW-resolved")
                      for x in findings)
        out = {"schema": "claims-findings/1", "counts": {"%s/%s" % k: v for k, v in sorted(cnt.items())},
               "record_problems": probs, "findings": findings}
        if opt("--json"):
            json.dump(out, open(opt("--json"), "w"), indent=1)
        for k, v in sorted(out["counts"].items()):
            print(k, v)
        for x in probs:
            print("RECORD", x)
        if probs:
            return 3
        act = [x for x in findings if x["active"] and "resolved_by" not in x]
        if any(x["verdict"] == "FAIL" for x in act):
            return 1
        if any(x["verdict"] == "REVIEW" for x in act):
            return 2
        return 0
    print(__doc__); return 4

if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except SystemExit:
        raise
    except Exception as e:                      # an internal error must not read as a confirmed violation
        print("internal error:", repr(e)); sys.exit(4)
