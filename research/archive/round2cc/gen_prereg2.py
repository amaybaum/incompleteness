src = open('/home/user/incompleteness/verification/audits/manuscript/round-cc-1-corpus-correction/preregistration.md', encoding='utf-8').read()
def rep(s, old, new):
    assert s.count(old) == 1, ('MISSING/AMBIGUOUS: ' + old[:70], s.count(old))
    return s.replace(old, new)
s = src
s = rep(s, "# Corpus correction round CC-1 — the premise ledger's 27 drift and tension items: PREREGISTRATION",
        "# Corpus correction round CC-2 — the premise ledger's 27 drift and tension items, with the verification surfaces they move: PREREGISTRATION")
s = rep(s, "round CC-1\nkind non-sealing\nrecord-directory verification/audits/manuscript/round-cc-1-corpus-correction/",
        "round CC-2\nkind non-sealing\nrecord-directory verification/audits/manuscript/round-cc-2-corpus-correction/")
s = rep(s, "record AM verification/audits/manuscript/round-cc-1-corpus-correction/\nrecord AM verification/receipts/CC-1.json",
        "record AM verification/audits/manuscript/round-cc-2-corpus-correction/\nrecord AM verification/receipts/CC-2.json")
s = rep(s, "execution M book/The-Incompleteness-of-Observation-FULL.pdf\n```",
        "execution M book/The-Incompleteness-of-Observation-FULL.pdf\nexecution M verification/coverage/LEDGER.json\nexecution M verification/lean/edge_rigidity_probe.py\n```")
s = rep(s, "result note. The receipt path is `verification/receipts/CC-1.json`. Every other path the round changes is an\nexecution path listed above: eleven manuscript sources and the sixteen built artifacts regenerated from them.\nNo Lean module, no verification tool, `verification/ROADMAP.md`, the workflow, and no other round's record change\nunder any outcome.",
        "result note. The receipt path is `verification/receipts/CC-2.json`. Every other path the round changes is an\nexecution path listed above: eleven manuscript sources, the sixteen built artifacts regenerated from them, and\nthe two verification surfaces the release gate reads against those sources — the proof-coverage ledger and the\nedge-rigidity probe. No Lean module, no other verification tool, `verification/ROADMAP.md`, the workflow, and no\nother round's record change under any outcome.")
s = rep(s, "- **`D`** = `0f2687b7b87925b53c6e3d8c6d1a233f36624dea`, the head of `main` after `OPACT-1` landed (push run\n  37035333423, every job green), identical to the premise ledger's audited base, so every ledger anchor is a live\n  line and no manuscript has moved since the audit.",
        "- **`D`** = `D-CC-2-PLACEHOLDER`, the head of `main` after `CC-1`'s halted record landed. Every execution\n  path of this round is byte-identical at `D` to its state at `0f2687b7`, the premise ledger's audited base (the\n  halted landing changed record paths only), so every ledger anchor is a live line and no manuscript, the ledger\n  or the probe has moved since the audit.")
s = rep(s, "## 1. Scope and boundary\n\n**In scope.**",
        "## 1. Scope and boundary\n\n**Provenance.** Round `CC-1` (`verification/receipts/CC-1.json`, halted under the specification's `S12`) froze\nthe same 27 items with the same dispositions and the same 60 substitutions, applied them at its candidate `E`\n`342fb68f0196a77c9085ac981f01266fd86eb869`, and halted because that candidate's exact-head run 37143464345 failed\ntwo checks reading files its governed paths did not name: the release gate's `coverage` step and the\n`edge_rigidity_probe` guard `R7-A6P`. This round governs those two files and carries, as frozen instances\n(§3.2), exactly the consequences the 60 substitutions have on them. Nothing else is added: no item, no\nsubstitution, no disposition changes from `CC-1`'s freeze.\n\n**In scope.**")
s = rep(s, "exactly one of three dispositions (§2), and nothing else.",
        "exactly one of three dispositions (§2); the six verification-surface instances of §3.2 that those dispositions\nforce; and nothing else.")
s = rep(s, "occurring exactly once at `D` (verified before this freeze, all 60 instances, 59 distinct old literals), and nothing else changes.",
        "occurring exactly once at `D` (verified before this freeze, all 60 manuscript instances, 59 distinct old literals, and\nthe six verification-surface instances of §3.2), and nothing else changes.")
sec32 = '''### 3.2 Verification-surface instances (frozen)

The release gate reads two files against the manuscript sources, and the substitutions above move both. Each
consequence is an instance of the same form, applied in S1 together with the substitution that forces it. The
`new` text of V-3 is empty: the entry is removed.

**V-1** `verification/coverage/LEDGER.json` — forced by T-A1-1.1. The census (`tools/proof_census.py`)
fingerprints the statement text of the corollary at `papers/Substratum.md` line 262; the entry
`SUBSTRATUM:C-effective-finiteness-gauge-class-transfer` is re-affirmed on the rewritten corollary with its
mapping unchanged: `kernel` `GAP`, `delta` `not formalized`, no checks. The corollary's claim narrows (the
transfer across the gauge class is stated for what the accessible-timescale transition law expresses); what the
ledger records of it does not change.

old:

```text
      "fingerprint": "9330e1f409e986c0",
```

new:

```text
      "fingerprint": "f7e912991de09137",
```

**V-2** `verification/coverage/LEDGER.json` — forced by T-A3-1 (the area-law lemma at `papers/SM.md` line
118). The lemma is unnamed in the census's sense, so its id is derived from its statement text and moves with
it; the entry keeps its mapping (`GAP`, `not formalized`, no checks). Two instances:

old:

```text
      "id": "SM:L-unnamed-332dde89",
```

new:

```text
      "id": "SM:L-unnamed-ff7b7d06",
```

old:

```text
      "fingerprint": "332dde89a60f07d3",
```

new:

```text
      "fingerprint": "ff7b7d068e326e1f",
```

**V-3** `verification/coverage/LEDGER.json` — forced by T-A6-2.1, which removes the `**Theorem**` header at
`papers/SM.md` line 140. The statement leaves the census; its entry (`GAP`, `not formalized`, no checks, named by
no backlog row and by no `unattached` row) is removed. The ledger's entry count and the census's canonical count
both go from 130 to 129; no document records the count.

old:

```text
    {
      "id": "SM:T-unnamed-f1d3c661",
      "paper": "papers/SM.md",
      "line": 140,
      "kind": "Theorem",
      "label": "",
      "fingerprint": "f1d3c6619bfdb644",
      "area": "sm",
      "assumptions": "see the statement",
      "checks": [],
      "kernel": "GAP",
      "delta": "not formalized",
      "note": ""
    },
```

new: (empty)

**V-4** `verification/lean/edge_rigidity_probe.py` — forced by T-A6-1.1. Guard `R7-A6P`'s sub-check P5
delimits the gauge passage of `papers/SM.md` section 3.1 by the phrase T-A6-1.1 removes; the delimiter becomes
the closing sentence T-A6-1.1 writes, which occurs exactly once in the section at `E`. The passage the sub-check
requires kernel-free is unchanged in extent (the heading through the sentence before the delimiter); every text
the guard pins is unchanged by this round (measured at `CC-1`'s candidate: every pinned passage present, the
delimiter the only failing component).

old:

```text
    _end = _31.find('now derived rather than postulated.')
```

new:

```text
    _end = _31.find('That the link dynamics is governed by this functional is not derived here.')
```

**V-5** `verification/lean/edge_rigidity_probe.py` — the same sub-check's docstring names the old delimiter.

old:

```text
    the word is absent from the gauge passage (the heading through the Wilson action "now derived
    rather than postulated"), and no proof-kernel language appears anywhere in the section. The
```

new:

```text
    the word is absent from the gauge passage (the heading through the plaquette functional, up to
    its closing sentence), and no proof-kernel language appears anywhere in the section. The
```

'''
s = rep(s, "## 4. Guardrails (frozen)", sec32 + "## 4. Guardrails (frozen)")
s = rep(s, "   hit in an added line blocks E.\n\nOrder of work:",
        "   hit in an added line blocks E.\n9. **Verification surfaces** — at E: `tools/coverage_check.py` passes; the census carries the two re-affirmed\n   entries at the predicted line and fingerprint and no longer carries the removed one, with 129 canonical\n   statements and 129 ledger entries; the probe's new delimiter occurs exactly once in SM.md section 3.1; and\n   `verification/lean/edge_rigidity_probe.py` prints `ALL CHECKS PASS`.\n\nOrder of work:")
s = rep(s, "build (step 5) → re-grep (6) → scans (7–8) → result note → E.",
        "build (step 5) → re-grep (6) → scans (7–8) → verification surfaces (9) → result note → E.")
s = rep(s, "- **C1** — `controls.py` is added to the record directory: it embeds §3's substitutions verbatim as declared\n  (file, old, new) instances — 60 instances, 59 distinct old literals, the duplicate being a chapter/`FULL.md` pair —\n  and validates each instance by itself:",
        "- **C1** — `controls.py` is added to the record directory: it embeds §3's substitutions verbatim as declared\n  (file, old, new) instances — 60 manuscript instances, 59 distinct old literals, the duplicate being a\n  chapter/`FULL.md` pair, and the six verification-surface instances of §3.2 — and validates each instance by itself:")
s = rep(s, "  edited paper's `.tex` `% source-sha256:` stamp against its source. Its blob is recorded in the result note.",
        "  edited paper's `.tex` `% source-sha256:` stamp against its source, and runs closure step 9's census, ledger and\n  delimiter checks. Its blob is recorded in the result note.")
s = rep(s, "- **S1** — the substitutions of §3 are applied, in one commit, to all eleven sources;",
        "- **S1** — the substitutions of §3 are applied, in one commit, to all eleven sources, and with them the six\n  verification-surface instances of §3.2 to the ledger and the probe;")
s = rep(s, "- **`CC-1-CORRECTED`**", "- **`CC-2-CORRECTED`**")
s = rep(s, "- **`CC-1-PARTIAL`**", "- **`CC-2-PARTIAL`**")
s = rep(s, "- **`CC-1-HALTED`**", "- **`CC-2-HALTED`**")
s = rep(s, "- **Gate steps that read the manuscripts** (`voice`, `claims`, `citation`, `duplicate`, `lean-manuscript`,\n  `staleness`): no citation key, kernel identifier or census anchor is added or removed by §3; `staleness` is\n  satisfied by the rebuild. Any failure at `E` is a halt, not a repair of text.",
        "- **Every check that reads the manuscripts, measured.** `CC-1`'s candidate `E` carried exactly the 60\n  substitutions of §3 with the artifacts rebuilt; its exact-head run 37143464345 ran all 32 jobs, and the only\n  failures were the release gate's `coverage` step (four findings: the stale corollary fingerprint, the area-law\n  lemma's moved id reported as one missing and one orphaned entry, and the removed theorem's orphaned entry) and\n  guard `R7-A6P` of `edge_rigidity_probe` (the delimiter alone; every pinned passage present). Every other gate\n  step (`voice`, `claims`, `citation`, `duplicate`, `mirror`, `lean-manuscript`, `staleness`, `v3-receipts`, …),\n  every other guard and every other probe shard passed on that tree. §3.2 carries exactly those findings'\n  consequences, and the predicted `E` tree (that candidate's tree with §3.2 applied) passes `coverage_check`\n  (129 canonical statements) and the probe (`ALL CHECKS PASS`) at `D`. Any failure at `E` is a halt, not a\n  repair of text.")
s = s.replace('verified before this freeze, all 60', 'verified before this freeze, all 60')
open('PREREG-CC-2.md', 'w', encoding='utf-8').write(s)
print('PREREG-CC-2.md written:', len(s.splitlines()), 'lines; CC-1 mentions:', s.count('CC-1'))
