#!/usr/bin/env python3
"""Throwaway prototype of the withdrawn-claim checker, revision r3 (paper-only, Issue #1565).

Not for the repository. Implements DESIGN-r3.md with regular expressions, to measure the design.

Architecture (DESIGN-r3 section 3): conservative detection, then revision-bound independent review.
  * A sentence is a CANDIDATE for a rule when every argument set of the rule and every cue set of
    the rule match somewhere in it, in any order, negated or not (code C), or when its cue sets
    match, an argument is missing, an anaphor is present and the missing arguments occur in the
    window (code A).
  * A candidate is FAIL (code B) when a bare template of the rule matches and the rest of the
    sentence contains no token of the risk lexicon; a literal-formula match is FAIL (code L).
  * Every other candidate is REVIEW.  Nothing else is decided automatically: no hypothesis,
    licence, frame or qualifier ever produces PASS.  PASS means "no candidate".
  * A REVIEW is resolved only by a review record bound to rule, path, sentence hash, code (and the
    window hash for code A) and a full commit; what a record may decide is checked mechanically
    (section 3.6): it can never resolve a FAIL, a 'governed' decision needs an owner-adopted
    licence entry (the deployed list is empty), and an 'unrelated' decision needs a basis whose
    evidence passes a mechanical check and contains no qualifier token.

Modes
  --controls FILE                     per-control verdicts and the r3 outcome classes
  --self-test                          every control file; exit 0 iff no silent miss and no FAIL on a
                                       control expected PASS or REVIEW; validates licences-r3.json (the deployed licences.json of DESIGN-r3)
  --scan ROOT --json OUT [--licences FILE] [--reviews FILE] [--repo GITDIR --main REF]
Exit status: 0 clean; 1 FAIL in active material; 2 unresolved REVIEW in active material and no FAIL;
3 invalid or stale licence or review record, or records given without --repo; 4 self-test failure,
usage error or internal error.  Precedence 4 > 3 > 1 > 2.
"""
import re, sys, os, json, hashlib, subprocess
from collections import Counter

I = re.I

# ------------------------------------------------------------------ frozen lexicons (DESIGN-r3 3.2)
# Argument sets: the anchor's subject (and object, for a relational claim), widened to the r2
# equivalence and near-miss subject sets and the bare head noun.
TEMP_ARG = (r"T_Q|T_\{?\\(?:rm|mathrm)\{?\s*(?:dS|H)\}?\}?|"
            r"\b(?:Hawking|Gibbons[- ]Hawking|de Sitter|horizon|Unruh|KMS|Bekenstein[- ]Hawking)\s+temperatures?\b|"
            r"\btemperatures? of the (?:[\w-]+ )?horizon\b|\bthermality\b|\bthermal (?:ratio|spectrum|character)\b")
QM_ARG = (r"\bQM\b|\bquantum (?:mechanics|theory|theories|formalism|structure|statistics|rules|description|"
          r"physics|kinematics|behaviou?r)\b")
OI_ARG = r"\bOI\b|\bobservation(?:al)? incompleteness\b|\bincompleteness of observation\b|\bignorance\b"
HIDDEN_ARG = r"\bhidden\b|\bsub-?quantum\b"
QFT_ARG = r"\bQFTs?\b|\bquantum field theor(?:y|ies)\b|\bfield theor(?:y|ies)\b"
CONE_ARG = r"\bfree-level\b"
BM_ARG = (r"\bcubic\b|\bequivarian\w*|\bsymmetr\w*|\bquadratic symbol\b|\bpropagation geometry\b|"
          r"\bprojected memory\b|\bsubstratum\b")
# Cue sets: the anchor predicate's stems and object noun, plus the closed relation family of the
# claim's type (invariance, necessity, causation, selection, property).
STATE_OBJ = r"\bstates?\b|\bvacu(?:a|um|ums)\b|\bα-vacu|\balpha-vacu"
UNIVERSAL = (r"\buniversal\w*|\binvarian\w*|\bsingle value\b|\bone value\b|\bunique\w*|\bregardless\b|"
             r"\birrespective\b|\bwhatever\b|\bblind\b|\bagnostic\b")
NECESSITY = (r"\brequir\w*|\bneed\w*|\bpresuppos\w*|\bprerequisite\w*|\bprecondition\w*|\bnecess\w*|"
             r"\bdepend\w*|\brest(?:s|ing|ed)? (?:up)?on\b|\brel(?:y|ies|ying|ied) (?:up)?on\b|\bimpossible\b|"
             r"\bpossible\b|\bwithout\b|\bdemand\w*|\bentail\w*|\bimpl(?:y|ies|ied|ying)\b|\bcondition for\b|"
             r"\bground\w*|\bcalls? for\b|\bmandat\w*|\bcompel\w*|\bindispensab\w*|\bessential\b|"
             r"\bexist\w*|\bdo without\b|\bbasis\b|\bpresence\b|\babsence\b")
CAUSATION = (r"\bexplain\w*|\bexplanat\w*|\bcaus\w*|\bproduc\w*|\bgenerat\w*|\bgiv\w* rise\b|\bgave rise\b|"
             r"\baccount\w* for\b|\bunderl\w*|\borigin\w*|\bsource\w*|\byield\w*|\bderiv\w*|\bconsequen\w*|"
             r"\bresult\w* (?:from|of)\b|\bemerg\w*|\bfollow\w* from\b|\blead\w* to\b|\bdue to\b|\bresponsib\w*")
SELECTION = (r"(?-i:\bK\b)|\b2d\b|\bsix\b|m\s*=\s*1|\bsingle-copy\b|\bsites?\b|\bcarrier\w*|\bfix\w*|"
             r"\bdetermin\w*|\bselect\w*|\bderiv\w*|\bforc\w*|\bestablish\w*|\byield\w*|\bgiv\w*|\bimpl\w*|"
             r"\bproduc\w*|\bpick\w*|\bsingl\w* out\b|\bentail\w*|\bfollow\w*|\bconsequen\w*|\bresult\w*")

RULES = [
 dict(id="W-GR-TQ-STATE", args=[TEMP_ARG], cues=[STATE_OBJ + "|" + UNIVERSAL],
      strong=r"state[- ]independen\w*|independent of the (?:quantum |choice of (?:the )?)?states?|(?:does|do)(?: not|n't) depend on the (?:quantum )?states?"),
 dict(id="W-GR-THERM-KIN", args=[TEMP_ARG + r"|\bhorizon\b"], cues=[r"\bkinematic\w*"],
      strong=r"\b(?:purely|entirely|wholly|solely|merely|just) kinematic\w*"),
 dict(id="W-GR-KMS", args=[QFT_ARG], cues=[r"\bKMS\b|\bperiodic\w*|\bimaginary[- ]time\b"],
      strong=r"\b(?:is|are|be) (?:a |in a )?KMS\b|\bperiodic in imaginary time\b"),
 dict(id="W-GR-CONE", args=[CONE_ARG], cues=[r"\bexact\w*|\bcones?\b"], strong=r"\bexact per channel\b"),
 dict(id="W-GR-EPSKAPPA", literal=r"(\\v?arepsilon|\\epsilon)\s*\\kappa\s*/\s*c\b(?!\^)"),
 dict(id="W-BM-EUCLID", args=[BM_ARG], cues=[r"\bEuclid\w*"], strong=r"\bEuclidean (?:quadratic |observer )*(?:symbol|metric)\b"),
 dict(id="W-KDEG", args=[r"\bcoupling\b", r"\bminim\w*"], cues=[SELECTION]),
 dict(id="W-KDEG", args=[r"\bframework'?s answer\b|\bthe answer\b"], cues=[r"(?-i:\bK\b)\s*=|\b2d\b|\bsix\b"]),
 dict(id="W-OI-REQ", args=[QM_ARG, OI_ARG], cues=[NECESSITY]),
 dict(id="W-OI-HIDDEN", args=[QM_ARG, HIDDEN_ARG], cues=[NECESSITY]),
 dict(id="W-OI-NOEXIST", args=[QM_ARG], strong=r"\b(?:cannot|could not|would not) exist without\b", cues=[r"\bexist\w*",
                                            r"\bwithout\b|\babsence\b|\bno\b|\bnot\b"]),
 dict(id="W-OI-EXPLAINS", args=[OI_ARG, QM_ARG], cues=[CAUSATION]),
 dict(id="W-OI-CONTRA", args=[OI_ARG, QM_ARG], cues=[r"\bwithout\b|\babsence\b|\babsent\b", r"\bno\b|\bnot\b|\bnever\b|\bcannot\b"]),
]
RULE_IDS = sorted({r["id"] for r in RULES})

# Bare templates (code B): the plain, unqualified canonical assertion with tight binding.  Used only to
# raise a candidate from REVIEW to FAIL; they never produce PASS.
TQ_STRICT = (r"(?:\$?T_Q\$?|(?:the )?(?:Hawking|Gibbons[- ]Hawking|de Sitter|horizon|Unruh|KMS) temperatures?"
             r"(?:\s*\$[^$]*\$)?|(?:the )?temperature of the (?:de Sitter |black[- ]hole )?horizon)")
TQ_PRED = (r"(?:state[- ]independent|independent of the (?:quantum |choice of (?:the )?)?states?|"
           r"(?:the same|identical|unchanged) (?:in|for|across) (?:every|all|any|each) (?:[\w-]+ )?states?|"
           r"insensitive to the (?:quantum |choice of (?:the )?)?states?)")
ADV = r"(?:(?:unconditionally|always|exactly|strictly|manifestly|completely|entirely|therefore|thus|hence|also)\s+)?"
QM_S = r"(?:QM|quantum mechanics|quantum theory|the quantum formalism)"
OI_S = r"(?:bare )?(?:OI\b|observational incompleteness|observation incompleteness)"
KDEG_S = (r"(?:coupling[- ]degree minimi[sz]ation|minimi[sz]ation of the coupling degree|minimi[sz]ing the coupling degree|"
          r"coupling[- ]degree minimum)")
KDEG_O = r"(?:\$?K\s*=\s*(?:2d|6)\$?|\$m\s*=\s*1\$|the single-copy clause|K\b)"
BARE = {
 "W-GR-TQ-STATE": [TQ_STRICT + r"\s+(?:is|are|remains|stays)\s+" + ADV + TQ_PRED,
                   TQ_STRICT + r"\s+(?:does not|doesn't|do not) depend on the (?:quantum |choice of (?:the )?)?states?"],
 "W-GR-THERM-KIN": [r"(?:" + TQ_STRICT + r"|(?:horizon )?thermality|the thermal spectrum)\s+(?:is|are)\s+(?:purely|entirely|wholly|solely|merely|just)\s+kinematic(?:al)?"],
 "W-GR-KMS": [r"(?:any|every|each|all) (?:QFTs?|quantum field theor(?:y|ies))\b[^.;,]{0,60}?\b(?:must|is|are)\s+(?:(?:therefore|necessarily|always)\s+)?(?:be\s+)?"
              r"(?:periodic in imaginary time|KMS\b|a KMS state|in a KMS state)"],
 "W-GR-CONE": [r"(?:the )?free-level (?:light )?cone\s+(?:is|remains)\s+exact"],
 "W-BM-EUCLID": [r"(?:cubic (?:equivariance|symmetry)|equivariance|substratum symmetry|projected memory)(?:\s+alone)?\s+(?:forces|implies|guarantees|entails)\s+(?:an? |the )?(?:[\w-]+ )?Euclidean",
                 r"(?:the )?(?:leading )?(?:scalar propagation geometry|quadratic symbol)\s+is\s+Euclidean"],
 "W-KDEG": [KDEG_S + r"\s+(?:is what\s+)?(?:fixes|determines|selects|derives|forces|establishes|yields|gives|implies|produces|picks out|singles out|entails)\s+" + KDEG_O,
            KDEG_O + r"\s*(?:follows|is (?:derived|fixed|selected|forced))\s+(?:from|by)\s+" + KDEG_S,
            r"framework's answer is \$K = 2d"],
 "W-OI-REQ": [QM_S + r"\s+(?:requires|needs|presupposes|depends on|necessitates|demands|is impossible without)\s+" + OI_S],
 "W-OI-HIDDEN": [QM_S + r"\s+(?:requires|needs|presupposes|depends on|necessitates)\s+(?:an? )?hidden (?:information|variables?|states?|ontology|sub-quantum level|level)"],
 "W-OI-NOEXIST": [QM_S + r"\s+(?:cannot|could not|would not) exist without"],
 "W-OI-EXPLAINS": [r"(?:OI|observational incompleteness|ignorance)\s+(?:causes|produces|explains|generates|gives rise to|accounts for|underlies)\s+(?:QM|quantum)"],
 "W-OI-CONTRA": [r"without (?:OI|observational incompleteness) there (?:is|would be) no (?:QM|quantum)"],
}

# Risk lexicon: any token of it outside the bare-template span keeps a candidate at REVIEW.
NEGWORD = (r"\bnot\b|n't\b|\bno\b|\bnever\b|\bnone\b|\bnothing\b|\bnobody\b|\bno one\b|\bneither\b|\bnor\b|"
           r"\bcannot\b|\bfail\w*|\bfalse\w*|\bwithout\b|\bden(?:y|ies|ied|ial)\b|\bdoubt\w*|\brefut\w*")
RISK = re.compile(
    NEGWORD + r"|\black\w*|\babsen\w*|\bwrong\w*|\bincorrect\w*|\bmistak\w*|\berroneous\w*|\bwithdraw\w*|\bretract\w*|"
    r"\bunlike\b|\bexcept\w*|\brather\b|\binstead\b|\bcontrary\b|\bviolat\w*|\bbreak\w*|\bbroken\b|\binvalid\w*|"
    r"\bun(?:proved|proven|supported|established|known|clear)\b|\bopen\b|\bsupersed\w*|\bobsolete\b|\bformer\w*|\bearlier\b|"
    r"\bH-[A-Za-z]|\bif\b|\bunless\b|\bunder\b|\bgiven\b|\bassum\w*|\bprovid\w*|\bwhen\w*|\bonce\b|\bonly\b|"
    r"\bconditional\w*|\bhypothe\w*|\bpremise\w*|\bposit\w*|\bsense\b|\breading\b|\bbranch\w*|\bregime\b|\blimit\w*|"
    r"\bscope\w*|\bsubject to\b|\bas long as\b|\bso long as\b|\bin case\b|"
    r"\bthat\b|\bwhether\b|\bclaim\w*|\bconjectur\w*|\bsuppos\w*|\bmight\b|\bmay\b|\bcould\b|\bwould\b|\bshould\b|"
    r"\bperhaps\b|\bpossibl\w*|\bpropos\w*|\bsuggest\w*|\bargu\w*|\bbeliev\w*|\bsa(?:y|ys|id)\b|\bread\b|\bquot\w*|"
    r"\bassert\w*|\bthink\w*|\bexpect\w*|\bask\w*|\bquestion\w*|\bwonder\w*|\bspeculat\w*|\bimagin\w*|\bhypothetic\w*|"
    r"\bwere\b|\bbut\b|\balthough\b|\bthough\b|\bwhereas\b|\bwhile\b|\byet\b|\bhowever\b|\beven\b|\bstill\b|"
    r"\bregardless\b|\birrespective\b|\bindependently\b|\?|[\"“”«»`]", I)
QUALIFIER = re.compile(r"\bH-[A-Za-z]|\bif\b|\bunless\b|\bunder\b|\bgiven\b|\bassum\w*|\bprovided\b|\bwhen\w*|\bonce\b|"
                       r"\bonly\b|\bconditional\w*|\bhypothe\w*|\bpremise\w*|\bposit\w*|\bsense\b|\breading\b|\bbranch\w*|"
                       r"\bregime\b|\bsubject to\b|\bas long as\b|\bso long as\b|\bin case\b", I)
CONCESSIVE = re.compile(r"\bstill\b|\beven\b|\bregardless\b|\birrespective\b|\bnevertheless\b|\bnonetheless\b|\banyway\b|"
                        r"\bwhether or not\b|\bwith or without\b|\balso\b|\bboth\b|\bdo not\b[^.]{0,30}\balso\b", I)
SUPPOS = re.compile(r"\bsuppos\w*|\bwere\b|\bwould\b|\bhypothetic\w*|\bimagine\b|\bcounterfactual\w*", I)
ANAPHOR = re.compile(r"\b(?:it|this|these|they|such|the latter|the former|"
                     r"(?:this|that|the|its|their) (?:temperatures?|quantity|value|result|spectrum|minimi[sz]ation|"
                     r"principle|argument|theory|framework|incompleteness|cone|symbol|geometry|symmetry|equivariance))\b", I)
QUOTE = re.compile(r"`[^`]+`|\"[^\"]+\"|“[^”]+”|«[^»]+»")

# ------------------------------------------------------------------ segmentation
MASK = re.compile(r"\$\$.*?\$\$|\$[^$]*\$|`[^`]*`", re.S)

def masked(s):
    return MASK.sub(lambda m: re.sub(r"[.;:,!?()—]", "\x00", m.group(0)), s)

ABBR = re.compile(r"\b(?:e\.g|i\.e|cf|vs|et al|Fig|Figs|Eq|Eqs|Ref|Refs|Sec|Secs|Thm|Prop|Lem|Def|App|Ch|resp|approx|"
                  r"No|etc|al|vol|pp|p)\.$")

def sentences(par):
    """Sentence units.  Unlike r2, a table row is one unit (cells are not split), so a subject in one
    cell and a predicate in another remain a co-occurrence."""
    m = masked(par)
    out, start = [], 0
    for x in re.finditer(r"(?:[.!?][\"'”)\]]*(?:\*\*|\*)?|\.\$\$|\x00\$\$|\$\$|\$\\(?:square|blacksquare|Box)\$|∎)(?=\s+[A-Z*_`$\[(\"'“§#]|\s*$)"
                         r"|\n(?=\s*(?:[-*+]\s|\d+\.\s|\||\$\$|#))", m):
        end = x.end()
        if ABBR.search(m[start:x.start() + 1]):
            continue
        out.append((start, end)); start = end
    if start < len(par):
        out.append((start, len(par)))
    return [(a, b) for a, b in out if par[a:b].strip()]

ORDER = {"FAIL": 2, "REVIEW": 1, "PASS": 0}

def norm_hash(s):
    return hashlib.sha256(" ".join(s.split()).encode()).hexdigest()

# ------------------------------------------------------------------ detection (DESIGN-r3 3.3-3.4)
def _all(rxs, s):
    return all(re.search(rx, s, I) for rx in rxs)

def check_sentence(rule, sent, window):
    """Return (verdict, code, match) or None."""
    if "literal" in rule:
        m = re.search(rule["literal"], sent)
        return ("FAIL", "L", m.group(0)) if m else None
    if not _all(rule["cues"], sent):
        return None
    if _all(rule["args"], sent):
        for b in BARE.get(rule["id"], []):
            m = re.search(b, sent, I)
            if m:
                rest = sent[:m.start()] + " " + sent[m.end():]
                if not RISK.search(rest):
                    return ("FAIL", "B", m.group(0))
        return ("REVIEW", "C", "")
    missing = [a for a in rule["args"] if not re.search(a, sent, I)]
    if ANAPHOR.search(sent) and all(re.search(a, window, I) for a in missing):
        return ("REVIEW", "A", "")
    return None

def check_strong(rule, sent):
    """Code P: the anchor's own predicate phrase, flagged whatever its subject (DESIGN-r3 3.3)."""
    m = rule.get("strong") and re.search(rule["strong"], sent, I)
    return ("REVIEW", "P", m.group(0)) if m else None

def prev_sentence(prev1, par1, sents, k):
    """Anaphora window: the immediately preceding sentence unit (the last unit of the previous paragraph
    for the first sentence of a paragraph)."""
    if k > 0:
        a, b = sents[k - 1]
        return par1[a:b]
    ps = sentences(prev1)
    return prev1[ps[-1][0]:ps[-1][1]] if ps else ""

def check_paragraph(par, prev="", only=None):
    par1 = par.replace("\n", " ").replace("\t", " ")
    prev1 = prev.replace("\n", " ")
    found = []
    for rule in RULES:
        if only and rule["id"] != only:
            continue
        sents = sentences(par)
        for k, (sa, sb) in enumerate(sents):
            sent = par1[sa:sb]
            window = prev_sentence(prev1, par1, sents, k)
            r = check_sentence(rule, sent, window) or check_strong(rule, sent)
            if r:
                v, code, mt = r
                found.append(dict(rule=rule["id"], verdict=v, code=code, offset=sa, sentence=sent.strip(), match=mt))
    best = {}
    for x in found:
        k = (x["rule"], x["offset"])
        if k not in best or ORDER[x["verdict"]] > ORDER[best[k]["verdict"]]:
            best[k] = x
    return list(best.values())

def verdict_for(text, rule_id, context=""):
    fs = check_paragraph(text, context, only=rule_id)
    return max((x["verdict"] for x in fs), key=lambda z: ORDER[z], default="PASS"), fs

def outcome(exp, v):
    """r3 outcome classes: exact, blocked (positive -> REVIEW), load (negative -> REVIEW),
    MISS (positive or ambiguous -> PASS), FPFAIL (negative or ambiguous -> FAIL)."""
    if exp == v:
        return "exact"
    if v == "PASS":
        return "MISS"
    if v == "FAIL":
        return "FPFAIL"
    return "blocked" if exp == "FAIL" else "load"

# ------------------------------------------------------------------ scan scope (unchanged from r2)
RECORD_HEADING = re.compile(r"^##\s+.*\(record\)\s*$")

def classify(rel):
    if rel.startswith("papers/") or rel.startswith("book/"):
        return "active"
    if rel == "AGENTS.md":
        return "agents"
    base = rel.rsplit("/", 1)[-1]
    if base == "README.md" and (not rel.startswith("verification/") or rel == "verification/README.md"):
        return "active"
    return "record"

def scan_tree(root):
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
            pos, prev, h2_record = 0, "", False
            for par in text.split("\n\n"):
                first = par.lstrip().splitlines()[0] if par.strip() else ""
                if first.startswith("## "):
                    h2_record = bool(RECORD_HEADING.match(first.strip()))
                active = cls == "active" or (cls == "agents" and not h2_record)
                for x in check_paragraph(par, prev):
                    x.update(path=rel, active=active, line=text.count("\n", 0, pos + x["offset"]) + 1,
                             sentence_sha256=norm_hash(x["sentence"]), window_sha256=norm_hash(prev + "\n\n" + par))
                    res.append(x)
                prev = par; pos += len(par) + 2
    return res

# ------------------------------------------------------------------ licences (DESIGN-r3 3.7)
HEX40 = re.compile(r"^[0-9a-f]{40}$")
MAIN_REF = ["HEAD"]

def git_is_ancestor(repo, rev):
    try:
        return subprocess.run(["git", "-C", repo, "merge-base", "--is-ancestor", rev, MAIN_REF[0]],
                              capture_output=True).returncode == 0
    except OSError:
        return False

def git_show(repo, rev, path):
    p = subprocess.run(["git", "-C", repo, "show", rev + ":" + path], capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else None

def load_json(path, default):
    return json.load(open(path, encoding="utf-8")) if path else default

def validate_licences(L, repo):
    probs, ids = [], set()
    if L.get("schema") != "claims-licences/3":
        probs.append("licence file: schema must be claims-licences/3")
    ents = L.get("entries", [])
    if ents and not repo:
        probs.append("licence entries present but no --repo: anchors and reviews cannot be verified")
    for i, e in enumerate(ents):
        tag = "licence[%d]" % i
        if not e.get("id") or e["id"] in ids:
            probs.append(tag + ": missing or duplicate id")
        ids.add(e.get("id"))
        if e.get("rule") not in RULE_IDS:
            probs.append(tag + ": unknown rule")
        try:
            re.compile(e.get("qualifier") or "")
        except re.error:
            probs.append(tag + ": qualifier does not compile")
        if not e.get("qualifier"):
            probs.append(tag + ": empty qualifier")
        if not e.get("proposer"):
            probs.append(tag + ": no proposer")
        a, r, o = e.get("anchor") or {}, e.get("review") or {}, e.get("adoption") or {}
        if not (a.get("path") and a.get("quote") and HEX40.match(a.get("revision", ""))):
            probs.append(tag + ": anchor needs path, quotation and a full commit revision")
        if not (r.get("reviewer") and r.get("record") and r.get("date") and HEX40.match(r.get("revision", ""))):
            probs.append(tag + ": no independent scientific review record")
        elif r.get("reviewer") == e.get("proposer"):
            probs.append(tag + ": reviewer is the proposer")
        if not (o.get("author") and o.get("time") and o.get("quote")):
            probs.append(tag + ": no quoted owner adoption (author, time, quote)")
        if repo:
            for rev in (a.get("revision"), r.get("revision")):
                if rev and HEX40.match(rev) and not git_is_ancestor(repo, rev):
                    probs.append(tag + ": revision %s is not an ancestor of the main ref" % rev[:12])
            blob = git_show(repo, a.get("revision", ""), a.get("path", "")) if a.get("path") else None
            if blob is None or " ".join(a.get("quote", "").split()) not in " ".join(blob.split()):
                probs.append(tag + ": anchor quotation not found at its revision")
            if r.get("record") and git_show(repo, MAIN_REF[0], r["record"]) is None:
                probs.append(tag + ": review record path does not exist on the main ref")
    return probs

# ------------------------------------------------------------------ review records (DESIGN-r3 3.6)
BASES = ("negated", "mention", "question", "supposition", "other-subject")

def record_basis_ok(rec, f, rule):
    """Mechanical bound on what an 'unrelated' decision may rest on.  Returns a problem or None."""
    s, ev, basis = f["sentence"], rec.get("evidence", ""), rec.get("basis")
    if basis not in BASES:
        return "basis must be one of " + ", ".join(BASES)
    if not ev or ev not in s:
        return "evidence must be a verbatim substring of the sentence"
    if QUALIFIER.search(ev):
        return "evidence contains a qualifier token; non-assertion cannot rest on a qualifier"
    if basis == "negated":
        if not re.search(NEGWORD, ev, I):
            return "negated: evidence contains no negation word"
        if not _all(rule.get("cues", []), ev):
            return "negated: evidence does not contain the rule's cue"
        if len(re.findall(NEGWORD, s, I)) != 1:
            return "negated: the sentence must contain exactly one negation word"
        if CONCESSIVE.search(s):
            return "negated: the sentence contains a concessive or polarity-flipping token"
    elif basis == "mention":
        if not any(ev in q.group(0) for q in QUOTE.finditer(s)):
            return "mention: evidence is not inside a quotation or code span of the sentence"
    elif basis == "question":
        if not s.rstrip().rstrip("*").endswith("?"):
            return "question: the sentence is not a question"
    elif basis == "supposition":
        if not SUPPOS.search(ev):
            return "supposition: evidence contains no supposition marker"
    elif basis == "other-subject":
        if any(re.search(a, ev, I) for a in rule.get("args", [])):
            return "other-subject: evidence contains the rule's own argument term"
        if _all(rule.get("cues", []), ev):
            return "other-subject: evidence contains the rule's cue"
    return None

def apply_reviews(findings, R, L, repo):
    probs = []
    recs = (R or {}).get("records", [])
    if recs and not repo:
        return ["review records present but no --repo: revisions cannot be verified"]
    lic = {e.get("id"): e for e in L.get("entries", [])}
    rules = {r["id"]: r for r in RULES}
    for i, r in enumerate(recs):
        tag = "review[%d]" % i
        need = ("rule", "path", "sentence_sha256", "sentence", "code", "decision", "reason", "reviewer",
                "revision", "date", "authority", "evidence")
        miss = [k for k in need if not r.get(k)]
        if miss:
            probs.append(tag + ": missing " + ",".join(miss)); continue
        if norm_hash(r["sentence"]) != r["sentence_sha256"]:
            probs.append(tag + ": sentence_sha256 does not match the quoted sentence"); continue
        if not HEX40.match(r["revision"]):
            probs.append(tag + ": revision is not a full commit id"); continue
        if not git_is_ancestor(repo, r["revision"]):
            probs.append(tag + ": revision is not an ancestor of the main ref"); continue
        if r["code"] == "A" and not r.get("window_sha256"):
            probs.append(tag + ": code A needs window_sha256"); continue
        cand = [x for x in findings if (x["rule"], x["path"], x["sentence_sha256"]) == (r["rule"], r["path"], r["sentence_sha256"])]
        if any(x["verdict"] == "FAIL" for x in cand):
            probs.append(tag + ": a review record cannot resolve a FAIL"); continue
        cand = [x for x in cand if x["code"] == r["code"] and (r["code"] != "A" or x["window_sha256"] == r["window_sha256"])]
        if not cand:
            probs.append(tag + ": stale (no matching REVIEW finding at this tree)"); continue
        f = cand[0]
        if r["decision"] == "governed":
            e = lic.get(r.get("licence"))
            if not e:
                probs.append(tag + ": 'governed' needs an owner-adopted licence entry; none is cited or it does not exist"); continue
            if e.get("rule") != r["rule"]:
                probs.append(tag + ": licence entry is for another rule"); continue
            if not re.search(e["qualifier"], r["evidence"]) or r["evidence"] not in f["sentence"]:
                probs.append(tag + ": evidence is not in the sentence or does not contain the licensed qualifier"); continue
        elif r["decision"] == "unrelated":
            p = record_basis_ok(r, f, rules[r["rule"]])
            if p:
                probs.append(tag + ": " + p); continue
        else:
            probs.append(tag + ": decision must be governed or unrelated"); continue
        for x in cand:
            x["resolved_by"] = i
    return probs

# ------------------------------------------------------------------ self-test
CONTROL_FILES = ["controls.json", "heldout.json", "controls_c.json", "controls_d.json",
                 "reviewer-heldout.json", "controls_r2.json", "reviewer-heldout-Y.json"]

def run_controls(path, quiet=False):
    cs = json.load(open(path, encoding="utf-8"))
    rows = []
    for c in cs:
        v, fs = verdict_for(c["text"], c["rule"], c.get("context", ""))
        rows.append((outcome(c["expect"], v), c["id"], c["expect"], v, ",".join(x["code"] for x in fs)))
    if not quiet:
        for o, cid, exp, v, codes in rows:
            print(o.ljust(8), cid.ljust(14), exp.ljust(6), v.ljust(6), codes)
    cnt = Counter(r[0] for r in rows)
    if not quiet:
        print("outcomes:", dict(cnt), "of", len(cs))
    return cnt, rows

def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    a = argv[1:]
    def opt(name, default=None):
        return a[a.index(name) + 1] if name in a else default
    if not a:
        print(__doc__); return 4
    if a[0] == "--controls":
        cnt, _ = run_controls(a[1])
        return 0 if cnt["MISS"] == 0 and cnt["FPFAIL"] == 0 else 4
    if a[0] == "--self-test":
        L = load_json(os.path.join(here, "licences-r3.json"), {})
        probs = validate_licences(L, None)
        if L.get("entries"):
            probs.append("deployed licence list is not empty")
        bad = 0
        for fn in CONTROL_FILES:
            p = os.path.join(here, fn)
            if os.path.exists(p):
                cnt, rows = run_controls(p, quiet=True)
                bad += cnt["MISS"] + cnt["FPFAIL"]
                print(fn.ljust(26), len(rows), dict(sorted(cnt.items())))
        for x in probs:
            print("LICENCE", x)
        if bad:
            return 4
        return 3 if probs else 0
    if a[0] == "--scan":
        repo = opt("--repo")
        MAIN_REF[0] = opt("--main", "HEAD")
        try:
            L = load_json(opt("--licences", os.path.join(here, "licences-r3.json")), {})
            R = load_json(opt("--reviews"), None)
        except (OSError, ValueError) as e:
            print("RECORD file unreadable:", e); return 3
        probs = validate_licences(L, repo)
        findings = scan_tree(a[1])
        probs += apply_reviews(findings, R, L, repo)
        cnt = Counter(("active" if x["active"] else "record", x["verdict"] if "resolved_by" not in x else "REVIEW-resolved")
                      for x in findings)
        out = {"schema": "claims-findings/3", "counts": {"%s/%s" % k: v for k, v in sorted(cnt.items())},
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
    except Exception as e:
        print("internal error:", repr(e)); sys.exit(4)
