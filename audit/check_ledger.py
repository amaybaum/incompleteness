#!/usr/bin/env python3
"""Validate audit/claim_ledger.json and reconcile it against the shipped corpus.

Three checks:
  1. Schema — every claim carries the required fields; status and evidence values
     are drawn from the declared vocabularies; dependencies resolve.
  2. Counts — the summary counts the ledger implies, printed so prose that states a
     count can be checked against one source rather than against itself.
  3. Corpus reconciliation — phrases the ledger's statuses forbid ("proved end-to-end",
     "resolved problem" language over claims whose status is conditional or open) are
     reported with file and line.

Deterministic, stdlib only, non-zero exit on failure. Run from anywhere:
    python3 audit/check_ledger.py [--repo <path>]
"""
import argparse, collections, json, os, pathlib, re, sys

REQUIRED = ["id", "statement", "domain", "status", "evidence", "assumptions",
            "depends_on", "free_parameters", "artifact", "empirical", "source"]

# Phrases that assert more than a conditional/open/unsupported status can carry.
# Each is (regex, why). Reported as reconciliation findings, not hard failures --
# some are legitimate in context and the report is for a human to triage.
OVERCLAIM = [
    (r"proved end-to-end", "asserts a discharged chain; several links are conditional"),
    (r"dissolv\w+ the (?:strong CP|cosmological[- ]constant)", "status of both is conditional"),
    (r"\b(?:twelve|eleven|ten|\d+) resolved problems", "counts resolved problems; several are conditional"),
    (r"unique computational class", "withdrawn in 2.7.4; must not reappear"),
    (r"at all energy scales", "withdrawn in 2.7.7; must not reappear outside its own quotation"),
]

# A hit inside one of these is not an overclaim: the corpus is denying, quoting, or
# navigating rather than asserting. Checked against the whole line.
EXEMPT = [
    r"\bnot\s+(?:\w+\s+){0,3}(?:solve|solved|resolve|resolved|dissolve|dissolved)\b",
    r"^#",                       # headings, incl. the ch19 title
    r"^\s*-?\s*\[`",             # README file-list navigation
    r"^\*\*Ambition\.\*\*\s*\u201c",   # the objections chapter quoting a critic
    r"[\"\u201c]Exactly zero at all energy scales[\"\u201d]",  # SM 5.5 quoting what it withdrew
]


def load(repo):
    p = pathlib.Path(repo) / "audit" / "claim_ledger.json"
    return json.loads(p.read_text(encoding="utf-8")), p


def check_schema(led):
    fails = []
    statuses = set(led["status_vocabulary"])
    evidences = set(led["evidence_vocabulary"])
    ids = set()
    for c in led["claims"]:
        cid = c.get("id", "<no id>")
        if cid in ids:
            fails.append(f"duplicate id {cid}")
        ids.add(cid)
        for f in REQUIRED:
            if f not in c:
                fails.append(f"{cid}: missing field {f}")
        if c.get("status") not in statuses:
            fails.append(f"{cid}: status {c.get('status')!r} not in vocabulary")
        if c.get("evidence") not in evidences:
            fails.append(f"{cid}: evidence {c.get('evidence')!r} not in vocabulary")
    for c in led["claims"]:
        for d in c.get("depends_on", []):
            if d not in ids:
                fails.append(f"{c['id']}: depends_on {d} does not resolve")
        a = c.get("alias_of")
        if a and a not in ids:
            fails.append(f"{c['id']}: alias_of {a} does not resolve")
    # A claim with free parameters cannot be 'established'.
    for c in led["claims"]:
        if c.get("free_parameters") and c.get("status") == "established":
            fails.append(f"{c['id']}: status established but carries free parameters "
                         f"{c['free_parameters']}")
    # A claim whose assumptions are undischarged cannot be 'established'.
    for c in led["claims"]:
        if c.get("status") == "established" and any(
                "NOT" in a or "undischarged" in a or "open" in a
                for a in c.get("assumptions", [])):
            fails.append(f"{c['id']}: status established but an assumption is flagged undischarged")
    return fails


def counts(led):
    claims = [c for c in led["claims"] if not c.get("alias_of")]
    by_status = collections.Counter(c["status"] for c in claims)
    by_evidence = collections.Counter(c["evidence"] for c in claims)
    return claims, by_status, by_evidence


def reconcile(repo):
    findings = []
    root = pathlib.Path(repo)
    files = sorted(list((root / "papers").glob("*.md")) + list((root / "book").glob("*.md")))
    for f in files:
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
            if any(re.search(e, line) for e in EXEMPT):
                continue
            for pat, why in OVERCLAIM:
                if re.search(pat, line, re.I):
                    findings.append((str(f.relative_to(root)), n, why,
                                     line.strip()[:100]))
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(pathlib.Path(__file__).resolve().parent.parent))
    a = ap.parse_args()

    led, path = load(a.repo)
    print(f"ledger: {path.name}, {len(led['claims'])} claims, frozen {led['frozen']}")

    fails = check_schema(led)
    print("PASS  schema" if not fails else f"FAIL  schema ({len(fails)})")
    for f in fails:
        print("       ", f)

    claims, by_status, by_evidence = counts(led)
    print(f"\ncounts over {len(claims)} distinct claims (aliases excluded):")
    print("  status:  " + ", ".join(f"{k} {v}" for k, v in sorted(by_status.items())))
    print("  evidence:" + ", ".join(f" {k} {v}" for k, v in sorted(by_evidence.items())))
    fwd = [c["id"] for c in claims if c["evidence"] == "preregistered_forward_prediction"]
    conf = [c["id"] for c in claims
            if c["evidence"] == "preregistered_forward_prediction" and "confirmed" in c["empirical"].lower()]
    print(f"  preregistered forward predictions: {len(fwd)}  ({' '.join(fwd)})")
    print(f"  of which confirmed: {len(conf)}")

    findings = reconcile(a.repo)
    print(f"\nreconciliation: {len(findings)} site(s) asserting more than the ledger carries")
    for fpath, n, why, txt in findings:
        print(f"  {fpath}:{n}  [{why}]")
        print(f"      {txt}")

    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
