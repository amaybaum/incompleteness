#!/usr/bin/env python3
"""claims_check_r4.py - are withdrawn results still asserted? (revision r4, report-only in the gate)

Status in the release gate.  tools/claims_check.py remains the blocking withdrawn-claim check.  This
checker runs beside it in report-only mode (step claims-r4-report): its findings are reported, in the
log and as a JSON file, and do not fail the step; its own failures (self-test, an invalid or stale
licence or review record, an unreadable record file, a usage or internal error) do.  Its controls
(tools/claims_check_r4_test.py, step claims-controls) block.  Making it the blocking check is a
separate reviewed change that needs the owner's approval (owner decision, amaybaum,
2026-11-26T04:39:58Z, #1169 comment 7182798225), and is not made while known coverage regressions
against tools/claims_check.py remain unresolved (owner decision, 2026-11-26).

Coverage against tools/claims_check.py.  It is compared on specific finite sets only
(tools/claims_check_r4_test.py): the findings in the current corpus, test cases generated from the
old patterns' alternatives, and the controls.  The sentences of those sets that the old checker
flags and this one passes are known, unresolved coverage gaps, listed in
tools/claims_check_r4_gap.json and in the report.  No finite set of generated cases shows that
coverage of the old patterns is preserved.

What this checker does, and what it does not.
  The checker flags defined patterns and enforces the structure of review records.  Independent
  scientific review is responsible for detecting reworded claims outside those patterns: a claim
  restated in words outside the frozen argument and cue sets is not flagged, and no lexical scanner
  closes that class.  A review record that stays within the mechanical bounds below is not thereby
  correct; the bounds limit what a record can claim, they do not make its claim true.

Design: verification/audits/infrastructure/claims-check-redesign-20261125/, DESIGN-r3.md as amended
by DESIGN-r4.md (Issue #1565).  Conservative detection, then revision-bound independent review.

Withdrawn results (rule identifiers are stable and never reused):
  W-GR-TQ-STATE   the horizon temperature T_Q asserted state-independent
  W-GR-THERM-KIN  horizon thermality asserted purely kinematic
  W-GR-KMS        any QFT on the background asserted KMS / periodic in imaginary time
  W-GR-CONE       the free-level cone asserted exact (per channel)
  W-GR-EPSKAPPA   the formula epsilon*kappa/c, which should carry c^2
  W-BM-EUCLID     cubic equivariance asserted to force a Euclidean quadratic symbol (b_m may vanish)
  W-KDEG, W-KDEG-ANSWER
                  coupling-degree minimization asserted to fix the component count K = 2d
  W-OI-REQ, W-OI-HIDDEN, W-OI-NOEXIST, W-OI-EXPLAINS, W-OI-CONTRA
                  quantum mechanics asserted to require observational incompleteness or a hidden
                  sub-quantum level, or OI asserted to explain quantum structure.  The kernel proves
                  containment (qm_implies_oiCore) and forward redundancy (completedOI_iff_physical)
                  only.  The OI rules are a separate list, OI_RULES; no marker word, negation or
                  qualifier ever accepts one of them automatically.

Detection, per sentence unit (a table row is one unit):
  code C  every argument set and every cue set of a rule match in the unit, in any order, negated
          or not;
  code A  every cue set matches, an argument is missing, the unit has an anaphor, and the missing
          arguments occur in the immediately preceding unit;
  code P  the rule's strong cue (the anchor's own predicate phrase) matches, whatever the subject;
  code L  the literal formula of W-GR-EPSKAPPA.
Outcome: FAIL (code B) for a code-C candidate containing a bare template of the plain canonical
assertion whose remainder has no token of the risk lexicon; FAIL for every literal match (code L);
REVIEW for every other candidate.  PASS means no candidate.  No hypothesis, licence, frame or
qualifier ever produces PASS.

Review records.  A REVIEW is resolved only by a record in
verification/infrastructure/claims-check/reviews.json, bound to rule, path, sentence and its hash,
code (and the window hash for code A) and a full commit that is an ancestor of the main ref.  What a
record may decide is checked mechanically: a record never resolves a FAIL; 'governed' needs an
owner-adopted entry of verification/infrastructure/claims-check/licences.json for the same rule (the
deployed list is empty, so every 'governed' record is refused); 'unrelated' is refused when the
sentence contains a hypothesis token H-..., and otherwise needs a basis (negated, mention, question,
supposition, other-subject) whose evidence passes its check, contains no qualifier token, and, for
mention, supposition and question, carries the match that raised the finding.

Scope.  Every .md file under the root is scanned.  FAIL and REVIEW set the exit status only in active
material: papers/, book/, README.md files outside verification/ and verification/README.md, and
AGENTS.md outside its level-two sections whose heading ends with "(record)".  Findings elsewhere are
reported with active: false and do not change the exit status.

Counting the outstanding review work.  The report gives four numbers, which count different things:
  findings          one per (rule, sentence unit) in active material that is not resolved.  A
                    sentence carries one finding for every rule it is a candidate for (a sentence
                    naming quantum mechanics, OI and "requires ... without" can be a candidate for
                    W-OI-REQ, W-OI-NOEXIST and W-OI-CONTRA at once);
  sentences         distinct (path, sentence hash) pairs among the findings: the sentences to read;
  texts             distinct sentence hashes: the same sentence in several files, chiefly a book
                    chapter and its mirror in book/The-Incompleteness-of-Observation-FULL.md,
                    counts once;
  records needed    distinct record keys, the unit one review record resolves: (rule, path, sentence
                    hash, code, and for code A the window hash).  One record per rule, per file and
                    per mirror; a repeat of the same sentence in the same file needs no second record.
  The findings that contain a hypothesis token (H-...) are counted separately: with the licence list
  empty, no record can clear them; they need rewording or an owner-adopted licence.

Usage
  python3 tools/claims_check_r4.py [--root DIR] [--repo GITDIR] [--main REF] [--licences FILE]
                                   [--reviews FILE] [--json OUT] [--report-only]
      self-test, then scan.  With --report-only, findings (exits 1 and 2) give exit 0; exits 3 and 4
      are kept.  --root defaults to the repository root, --main to origin/main, and
      the record files to the deployed licence and review files.  Without --repo a review record or
      licence entry is refused, because its revision's ancestry cannot be checked; the release gate
      passes --repo and --main explicitly, from a checkout with full history, and if the main ref
      is absent every record is refused.
  python3 tools/claims_check_r4.py --self-test     the control suite
                                                   tools/claims_check_r4_controls.json and the
                                                   deployed licence file only
  python3 tools/claims_check_r4.py --controls FILE  per-control verdicts for a control file
Exit status: 0 clean; 1 FAIL in active material; 2 unresolved REVIEW in active material and no FAIL;
3 invalid or stale licence or review record, an unreadable or missing record file, or records or
licences given without --repo; 4 self-test failure, usage error or internal error.  Precedence
4 > 3 > 1 > 2.  The exit-code and record controls are tools/claims_check_r4_test.py.
"""
import re, sys, os, json, hashlib, subprocess
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)

I = re.I

# ------------------------------------------------------------------ frozen lexicons (DESIGN-r3 3.2)
# Argument sets: the anchor's subject (and object, for a relational claim), widened to the r2
# equivalence and near-miss subject sets and the bare head noun.
TEMP_ARG = (r"T_Q|T_\{?\\(?:rm|mathrm)\{?\s*(?:dS|H)\}?\}?|"
            r"\b(?:Hawking|Gibbons[- ]Hawking|de Sitter|horizon|Unruh|KMS|Bekenstein[- ]Hawking)\s+temperatures?\b|"
            r"\btemperatures? of the (?:[\w-]+ )?horizons?\b|\bthermality\b|\bthermal (?:ratios?|spectr(?:um|a)|characters?)\b")
QM_ARG = (r"\bQM\b|\bquantum (?:mechanics|theory|theories|formalisms?|structures?|statistics|rules?|descriptions?|"
          r"physics|kinematics|behaviou?rs?)\b")
OI_ARG = r"\bOI\b|\bobservation(?:al)? incompleteness\b|\bincompleteness of observation\b|\bignorance\b"
HIDDEN_ARG = r"\bhidden\b|\bsub-?quantum\b"
QFT_ARG = r"\bQFTs?\b|\bquantum field theor(?:y|ies)\b|\bfield theor(?:y|ies)\b"
CONE_ARG = r"\bfree-level\b"
BM_ARG = (r"\bcubic\b|\bequivarian\w*|\bsubstratum symmetr(?:y|ies)\b|\bquadratic symbols?\b|\bpropagation geometr(?:y|ies)\b|"
          r"\bprojected memor(?:y|ies)\b")
# Cue sets: the anchor predicate's stems and object noun, plus the closed relation family of the
# claim's type (invariance, necessity, causation, selection, property).
STATE_OBJ = r"\bstates?\b|\bvacu(?:a|um|ums)\b|\bα-vacu|\balpha-vacu"
UNIVERSAL = (r"\buniversal\w*|\binvarian\w*|\bsingle values?\b|\bone value\b|\bunique\w*|\bregardless\b|"
             r"\birrespective\b|\bwhatever\b|\bblind\b|\bagnostic\b")
NECESSITY = (r"\brequir\w*|\bneed\w*|\bpresuppos\w*|\bprerequisite\w*|\bprecondition\w*|\bnecess\w*|"
             r"\bdepend\w*|\brest(?:s|ing|ed)? (?:up)?on\b|\brel(?:y|ies|ying|ied) (?:up)?on\b|\bimpossible\b|"
             r"\bpossible\b|\bwithout\b|\bdemand\w*|\bentail\w*|\bimpl(?:y|ies|ied|ying)\b|\bconditions? for\b|"
             r"\bground\w*|\bcalls? for\b|\bmandat\w*|\bcompel\w*|\bindispensab\w*|\bessential\b|"
             r"\bexist\w*|\bdo without\b|\bbasis\b|\bpresence\b|\babsence\b")
CAUSATION = (r"\bexplain\w*|\bexplanat\w*|\bcaus\w*|\bproduc\w*|\bgenerat\w*|\bgiv\w* rise\b|\bgave rise\b|"
             r"\baccount\w* for\b|\bunderl\w*|\borigin\w*|\bsource\w*|\byield\w*|\bderiv\w*|\bconsequen\w*|"
             r"\bresult\w* (?:from|of)\b|\bemerg\w*|\bfollow\w* from\b|\blead\w* to\b|\bled to\b|\bdue to\b|\bresponsib\w*")
SELECTION = (r"(?-i:\bK\b)|\b2d\b|\bsix\b|m\s*=\s*1|\bsingle-copy\b|\bsites?\b|\bcarrier\w*|\bfix\w*|"
             r"\bdetermin\w*|\bselect\w*|\bderiv\w*|\bforc\w*|\bestablish\w*|\byield\w*|\bgiv\w*|\bimpl\w*|"
             r"\bproduc\w*|\bpick\w*|\bsingl\w* out\b|\bentail\w*|\bfollow\w*|\bconsequen\w*|\bresult\w*")

GENERAL_RULES = [
 dict(id="W-GR-TQ-STATE", args=[TEMP_ARG], cues=[STATE_OBJ + "|" + UNIVERSAL],
      strong=r"state[- ]independen\w*|independent of the (?:quantum |choice of (?:the )?)?states?|(?:does|do)(?: not|n't) depend on the (?:quantum )?states?"),
 dict(id="W-GR-THERM-KIN", args=[TEMP_ARG], cues=[r"\bkinematic\w*"],
      strong=r"\b(?:purely|entirely|wholly|solely|merely|just) kinematic\w*"),
 dict(id="W-GR-KMS", args=[QFT_ARG], cues=[r"\bKMS\b|\bperiodic\w*|\bimaginary[- ]time\b"],
      strong=r"\b(?:is|are|be) (?:a |in a )?KMS\b|\bperiodic in imaginary time\b"),
 dict(id="W-GR-CONE", args=[CONE_ARG], cues=[r"\bexact\w*|\bcones?\b"], strong=r"\bexact per channel\b"),
 dict(id="W-GR-EPSKAPPA", literal=r"(\\v?arepsilon|\\epsilon)\s*\\kappa\s*/\s*c\b(?!\^)"),
 dict(id="W-BM-EUCLID", args=[BM_ARG], cues=[r"\bEuclid\w*"], strong=r"\bEuclidean (?:quadratic |observer )*(?:symbol|metric)\b"),
 dict(id="W-KDEG", args=[r"\bcouplings?\b", r"\bminim\w*"], cues=[SELECTION]),
 dict(id="W-KDEG-ANSWER", family="W-KDEG", args=[r"\bframework'?s answer\b|\bthe answer\b"], cues=[r"(?-i:\bK\b)\s*=|\b2d\b|\bsix\b"]),
]
# The OI rules: a separate list, so that guard R7-FWD can pin it (DESIGN-r3 section 8).  No marker
# word, negation or qualifier accepts an OI assertion; only a review record within the bounds below.
OI_RULES = [
 dict(id="W-OI-REQ", args=[QM_ARG, OI_ARG], cues=[NECESSITY]),
 dict(id="W-OI-HIDDEN", args=[QM_ARG, HIDDEN_ARG], cues=[NECESSITY]),
 dict(id="W-OI-NOEXIST", args=[QM_ARG], strong=r"\bcannot exist without\b|\b(?:could|would) not exist without\b", cues=[r"\bexist\w*",
                                            r"\bwithout\b|\babsence\b|\bno\b|\bnot\b"]),
 dict(id="W-OI-EXPLAINS", args=[OI_ARG, QM_ARG], cues=[CAUSATION]),
 dict(id="W-OI-CONTRA", args=[OI_ARG, QM_ARG], cues=[r"\bwithout\b|\babsence\b|\babsent\b", r"\bno\b|\bnot\b|\bnever\b|\bcannot\b"]),
]
RULES = GENERAL_RULES + OI_RULES
RULE_IDS = sorted({r["id"] for r in RULES})
assert len(RULE_IDS) == len(RULES), "rule identifiers must be unique"   # DESIGN-r4 correction (3)

def family(rule):
    """Controls name a rule family; W-KDEG-ANSWER belongs to the family W-KDEG (DESIGN-r4 correction 3)."""
    return rule.get("family", rule["id"])

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
BARE["W-KDEG-ANSWER"] = BARE["W-KDEG"]   # both rules share the W-KDEG bare templates (DESIGN-r4 correction 3)

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
HYP_TOKEN = re.compile(r"\bH-\w", I)   # DESIGN-r4 correction (1): the hypothesis token H-... (H-slope, H-χ, ...)
QUOTE = re.compile(r"`[^`]+`|\"[^\"]+\"|“[^”]+”|«[^»]+»")

# ------------------------------------------------------------------ segmentation
MASK = re.compile(r"\$\$.*?\$\$|\$[^$]*\$|`[^`]*`", re.S)

def masked(s):
    return MASK.sub(lambda m: re.sub(r"[.;:,!?()—]", "\x00", m.group(0)), s)

ABBR = re.compile(r"\b(?:e\.g|i\.e|cf|vs|et al|Fig|Figs|Eq|Eqs|Ref|Refs|Sec|Secs|Thm|Prop|Lem|Def|App|Ch|resp|approx|"
                  r"No|etc|al|vol|pp|p)\.$")

def sentences(par):
    """Sentence units.  A table row is one unit (cells are not split), so a subject in one
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
    # The units and their anaphora windows do not depend on the rule; computed once per paragraph.
    sents = sentences(par)
    units = [(sa, par1[sa:sb], prev_sentence(prev1, par1, sents, k)) for k, (sa, sb) in enumerate(sents)]
    for rule in RULES:
        if only and rule["id"] != only and family(rule) != only:
            continue
        for sa, sent, window in units:
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
    """Outcome classes (DESIGN-r3 section 4): exact, blocked (positive -> REVIEW), load (negative -> REVIEW),
    MISS (positive or ambiguous -> PASS), FPFAIL (negative or ambiguous -> FAIL)."""
    if exp == v:
        return "exact"
    if v == "PASS":
        return "MISS"
    if v == "FAIL":
        return "FPFAIL"
    return "blocked" if exp == "FAIL" else "load"

# ------------------------------------------------------------------ scan scope (DESIGN-r2 3.9)
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
MAIN_REF = ["origin/main"]

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

def own_match(ev, f, rule):
    """DESIGN-r4 correction (2): the evidence carries the match that raised the finding.  Code C: every argument
    set and every cue set.  Code A: every cue set, every argument set present in the sentence, and the
    anaphor that stands for the missing argument.  Code P: the strong-cue match."""
    if f["code"] == "P":
        return bool(f.get("match")) and f["match"] in ev
    if not _all(rule.get("cues", []), ev):
        return False
    if f["code"] == "A":
        present = [a for a in rule["args"] if re.search(a, f["sentence"], I)]
        return _all(present, ev) and bool(ANAPHOR.search(ev))
    return _all(rule["args"], ev)

def record_basis_ok(rec, f, rule):
    """Mechanical bound on what an 'unrelated' decision may rest on.  Returns a problem or None."""
    s, ev, basis = f["sentence"], rec.get("evidence", ""), rec.get("basis")
    if HYP_TOKEN.search(s):
        return ("the sentence contains a hypothesis token (H-...); it is resolved only by a 'governed' record "
                "citing an adopted licence, or by rewording")
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
        if not own_match(ev, f, rule):
            return "mention: the quoted evidence does not contain the rule's own argument and cue match"
    elif basis == "question":
        if not s.rstrip().rstrip("*").endswith("?"):
            return "question: the sentence is not a question"
        if not own_match(ev, f, rule):
            return "question: the evidence does not contain the rule's own argument and cue match"
    elif basis == "supposition":
        if not SUPPOS.search(ev):
            return "supposition: evidence contains no supposition marker"
        if not own_match(ev, f, rule):
            return "supposition: the evidence does not contain the rule's own argument and cue match"
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
# The control suite, beside this file.  Each item carries the verdict it is pinned to (per rule, its
# codes, and over every rule); a changed verdict fails the self-test, in either direction.  On the
# acceptance controls and the review probes a must-not-pass item that passes (MISS) or an item
# expected PASS or REVIEW that fails (FPFAIL) also fails it.  Batch W and the author diagnostics
# record the documented residual of reworded claims (DESIGN-r4 sections 0 and 3); they are pinned,
# and their silent passes are the class that independent scientific review carries.
CONTROLS = os.path.join(HERE, "claims_check_r4_controls.json")
NO_SILENT_PASS = ("acceptance", "probe")


def any_verdict(text, context=""):
    return max((x["verdict"] for x in check_paragraph(text, context)), key=lambda z: ORDER[z], default="PASS")


def evaluate(c):
    v, fs = verdict_for(c["text"], c["rule"], c.get("context", ""))
    return {"verdict": v, "codes": ",".join(x["code"] for x in fs), "any": any_verdict(c["text"], c.get("context", ""))}


def run_controls(items, quiet=False):
    """Returns (problems, Counter of outcome classes)."""
    probs, cnt = [], Counter()
    for c in items:
        got = evaluate(c)
        o = outcome(c["expect"], got["verdict"])
        cnt[o] += 1
        if not quiet:
            print(o.ljust(8), c["id"].ljust(14), c["expect"].ljust(6), got["verdict"].ljust(6), got["codes"])
        pin = c.get("pinned")
        if pin is not None and pin != got:
            probs.append("%s (%s): pinned %s, got %s" % (c["id"], c.get("source", ""), pin, got))
        if c.get("category") in NO_SILENT_PASS and o in ("MISS", "FPFAIL"):
            probs.append("%s (%s): %s" % (c["id"], c.get("source", ""), o))
    return probs, cnt


def self_test(lic_path, quiet=True):
    """Returns (exit status, one-line summary): 4 on a control failure, 3 on a licence problem."""
    try:
        suite = json.load(open(CONTROLS, encoding="utf-8"))
    except (OSError, ValueError) as e:
        return 4, "self-test: control suite unreadable: %s" % e
    probs = []
    if suite.get("schema") != "claims-controls/1":
        probs.append("control suite: schema must be claims-controls/1")
    items = suite.get("controls", [])
    ids = [(c.get("source"), c.get("id")) for c in items]
    if len(set(ids)) != len(ids):
        probs.append("control suite: duplicate (source, id)")
    fams = {family(r) for r in RULES}
    covered = {c["rule"] for c in items if c.get("category") == "acceptance"}
    for f in sorted(fams - covered):
        probs.append("rule family %s has no acceptance control" % f)
    for c in items:
        if c.get("rule") not in fams:
            probs.append("%s: unknown rule %s" % (c.get("id"), c.get("rule")))
    if probs:
        for p in probs:
            print("SELF-TEST", p)
        return 4, "self-test: FAILED (%d problem(s))" % len(probs)
    p2, cnt = run_controls(items, quiet=quiet)
    for p in p2:
        print("SELF-TEST", p)
    if p2:
        return 4, "self-test: FAILED (%d control(s) changed or silently passed)" % len(p2)
    try:
        L = load_json(lic_path, None)
    except (OSError, ValueError) as e:
        print("LICENCE file unreadable:", e)
        return 3, "self-test: licence file unreadable"
    lp = validate_licences(L or {}, None)
    if (L or {}).get("entries"):
        lp.append("deployed licence list is not empty")
    for p in lp:
        print("LICENCE", p)
    if lp:
        return 3, "self-test: licence file invalid"
    return 0, "self-test: OK (%d controls, %s)" % (len(items), dict(sorted(cnt.items())))


# ------------------------------------------------------------------ review workload
def record_key(x):
    """The unit one review record resolves (apply_reviews): rule, path, sentence hash, code, and the
    window hash for code A."""
    return (x["rule"], x["path"], x["sentence_sha256"], x["code"], x["window_sha256"] if x["code"] == "A" else "")


def workload(act):
    """The outstanding review work over the unresolved active findings (module docstring)."""
    rev = [x for x in act if x["verdict"] == "REVIEW"]
    hyp = [x for x in rev if HYP_TOKEN.search(x["sentence"])]
    keys, hkeys = {record_key(x) for x in rev}, {record_key(x) for x in hyp}
    return {
        "findings": len(act),
        "FAIL": len(act) - len(rev),
        "REVIEW": len(rev),
        "sentences": len({(x["path"], x["sentence_sha256"]) for x in act}),
        "texts": len({x["sentence_sha256"] for x in act}),
        "records needed": len(keys),
        "records needed, clearable by a review record": len(keys - hkeys),
        "records needed, hypothesis token (rewording or an adopted licence)": len(hkeys),
        "files": len({x["path"] for x in act}),
    }


# ------------------------------------------------------------------ entry point
DEPLOYED = os.path.join(REPO_ROOT, "verification", "infrastructure", "claims-check")
FLAGS = {"--root", "--repo", "--main", "--licences", "--reviews", "--json", "--controls"}


def parse(argv):
    a, opts, i = argv[1:], {}, 0
    while i < len(a):
        if a[i] in ("--self-test", "--report-only"):
            opts[a[i][2:]] = True; i += 1
        elif a[i] in FLAGS and i + 1 < len(a):
            opts[a[i]] = a[i + 1]; i += 2
        else:
            raise ValueError("unknown or incomplete argument: %s" % a[i])
    return opts


def main(argv):
    try:
        opts = parse(argv)
    except ValueError as e:
        print(e); print(__doc__); return 4
    lic_path = opts.get("--licences", os.path.join(DEPLOYED, "licences.json"))
    if "--controls" in opts:
        items = json.load(open(opts["--controls"], encoding="utf-8"))
        items = items.get("controls", items) if isinstance(items, dict) else items
        probs, cnt = run_controls(items)
        print("outcomes:", dict(cnt), "of", len(items))
        for p in probs:
            print("CONTROL", p)
        return 0 if cnt["MISS"] + cnt["FPFAIL"] == 0 and not probs else 4
    # The self-test validates the deployed licence file, which must be empty (DESIGN-r3 3.7); with
    # --self-test, --licences names the file it validates instead.
    st, summary = self_test(lic_path if opts.get("self-test") else os.path.join(DEPLOYED, "licences.json"))
    print(summary)
    if opts.get("self-test"):
        return st
    if st == 4:
        print("claims_check_r4: FAILED (exit 4: self-test)")
        return 4
    root = opts.get("--root", REPO_ROOT)
    repo = opts.get("--repo")
    MAIN_REF[0] = opts.get("--main", "origin/main")
    try:
        L = load_json(lic_path, None)
        R = load_json(opts.get("--reviews", os.path.join(DEPLOYED, "reviews.json")), None)
        if not isinstance(L, dict) or not isinstance(R, dict):
            raise ValueError("a record file must hold a JSON object")
    except (OSError, ValueError) as e:
        print("RECORD file unreadable:", e)
        print("claims_check_r4: FAILED (exit 3: record file unreadable)")
        return 3
    probs = validate_licences(L, repo)
    findings = scan_tree(root)
    probs += apply_reviews(findings, R, L, repo)
    cnt = Counter(("active" if x["active"] else "record", x["verdict"] if "resolved_by" not in x else "REVIEW-resolved")
                  for x in findings)
    act = [x for x in findings if x["active"] and "resolved_by" not in x]
    load = workload(act)
    if opts.get("--json"):
        out = {"schema": "claims-findings/3", "counts": {"%s/%s" % k: v for k, v in sorted(cnt.items())},
               "workload": load, "record_problems": probs, "findings": findings}
        with open(opts["--json"], "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=1)
    for x in sorted(act, key=lambda z: (z["path"], z["line"], z["rule"])):
        print("  %-6s %s:%d  %s (code %s)" % (x["verdict"], x["path"], x["line"], x["rule"], x["code"]))
        print("         " + x["sentence"][:160])
    for k, v in sorted(cnt.items()):
        print("  %s/%s %d" % (k[0], k[1], v))
    print("  workload: " + ", ".join("%s %d" % (k, v) for k, v in load.items()))
    for x in probs:
        print("RECORD", x)
    nfail = sum(x["verdict"] == "FAIL" for x in act)
    nrev = sum(x["verdict"] == "REVIEW" for x in act)
    if st == 3 or probs:
        print("claims_check_r4: FAILED (exit 3: %d invalid or stale licence or review record(s))" % (len(probs) + (st == 3)))
        return 3
    if opts.get("report-only") and (nfail or nrev):
        print("claims_check_r4: REPORT (exit 0, report-only: %d FAIL and %d unresolved REVIEW finding(s) in active "
              "material; %d sentence(s), %d record(s) needed)" % (nfail, nrev, load["sentences"], load["records needed"]))
        return 0
    if nfail:
        print("claims_check_r4: FAILED (exit 1: %d withdrawn result(s) asserted in active material, %d unresolved REVIEW)"
              % (nfail, nrev))
        return 1
    if nrev:
        print("claims_check_r4: FAILED (exit 2: %d unresolved REVIEW finding(s) in active material need a review record)"
              % nrev)
        return 2
    print("claims_check_r4: OK (no FAIL and no unresolved REVIEW in active material)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except SystemExit:
        raise
    except Exception as e:                     # noqa: BLE001 -- a crash never reads as a verdict
        print("internal error:", repr(e)); sys.exit(4)
