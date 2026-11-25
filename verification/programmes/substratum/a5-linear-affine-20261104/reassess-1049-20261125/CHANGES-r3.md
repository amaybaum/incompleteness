# #1049 report: changes from r2 to r3

**Basis.** Owner decision (amaybaum, 2026-11-25, #1169 comment 7167242160): "#1561 — Linearity | Apply F1–F3 and the remaining minor scope and labelling corrections."; "For #1561, use the reviewer's proposed wording for F1. The distinction between an observable difference at a defined interface and a physically meaningful difference is scientifically important, particularly while the gauge question remains unresolved."; "Produce a minimal r3 addressing only the identified findings. ... Do not reopen previously accepted results without new evidence of a defect."

**Input.** REPORT-r2.md at `0c058645b1cb0a642f0de6afa7cab129f383dc2e`, and the delta review of r2 on PR #1561 (verdict ACCEPT-WITH-NITS; findings F1–F3 and five nits). Manuscript pin unchanged: `main` = `e2e2a623265187a28ebec604ab8bcc672742888f`.

**Scope.** Only the changes below were made. Every other line of REPORT-r2.md is carried into REPORT-r3.md byte for byte.

***

## F1. §2.2, "Conclusion (A), stated per readout class", Main's-absolute-interface bullet

Reviewer's proposed wording, fitted into the existing sentence.

- Old: "At that interface labelled statistics are observable, so this is an observational difference, not a coordinate artefact."
- New: "At that interface labelled statistics are observable, so this is an observational difference at that interface as defined; whether it is physical turns on the gauge reading below."

## F2. §2.1, "Necessity for results", first bullet

- Old: "those uses need only the affine condition (POSIT-MIN T1), [P]."
- New: "those uses need only the affine condition (POSIT-MIN T1), [P]; affine sufficiency [R]/[A]."

## F3. §2.1, same bullet

Checked at the pin: Main:364 is the heading "### 3.3 Bell Inequality Violations"; Main:368 contains "a graph that differs between state classes requires an update outside (vii)"; Main:424 contains "the update of this branch lies outside ledger item (vii)".

- Old: "Main also uses (vii) to state what it excludes, at Main:364 and Main:424."
- New: "Main also uses (vii) to state what it excludes, at Main:368 and Main:424."

## Nit 1. §1.2, OA-1 D6 bullet

- Old: "- **OA-1 D6:** non-affine rules at configuration level do not close the quantum gap."
- New: "- **OA-1 D6:** non-affine rules at configuration level do not close the quantum gap at the configuration-level interface as defined; [R]."

## Nit 2. §5, decision rule, first outcome

- Old: "outcome "unnecessary at stated scope" (criterion 2)."
- New: "outcome "unnecessary in sense (1) at stated scope" (criterion 2)."

## Nit 3. §0, Status paragraph: label list

The sentence on new steps ([A], [W]) is kept; one sentence listing the labels of cited support is appended.

- Old: "Every new step below is labelled [A] (exact algebra by hand in this report, unreviewed) or [W] (reasoning in this report, unreviewed)."
- New: "Every new step below is labelled [A] (exact algebra by hand in this report, unreviewed) or [W] (reasoning in this report, unreviewed). Cited support is labelled [K] (kernel theorem; statement read at the pin, nothing built), [K, definitional] (a kernel theorem that holds by definition, `rfl` or `Iff.rfl`), [P] (manuscript statement), [D] (derivation in a model-reviewed record), [R] (reviewed research record) or [background] (literature, not retrieved). A combined label such as [K]+[W], [D]/[R], [R]/[A] or [A]/[W] gives the support of the parts of one statement; the statement takes its weakest part."

## Nit 4. §2.2, body bullet "Off the resonant locus": "exactly if" harmonized to "only if"

"Only if" is chosen, matching §2.2 Conclusion (A), the §2.3 table ("only if amplitude-scale gauge is physical") and §4 ("licensed only if amplitude-scale gauge is physical"). The record supports the necessary condition: the static uniform shift is the amplitude-scale (uniform-shift) gauge transformation, and owner ruling Q2 treats it as a mathematical relabelling unless that gauge is justified. "Exactly if" would also assert the converse, that physical amplitude-scale gauge suffices for physical equivalence at Main's absolute interface; r2 does not establish that separately, so the weaker statement is kept.

- Old: "It becomes physical equivalence exactly if amplitude-scale gauge is physical, which is open."
- New: "It becomes physical equivalence only if amplitude-scale gauge is physical, which is open."

## Status line. §0, new paragraph after "Revision r2."

- Old: (none)
- New: "**Revision r3.** Revision r3 applies the owner decision "#1561 — Linearity | Apply F1–F3 and the remaining minor scope and labelling corrections." (amaybaum, 2026-11-25, #1169 comment 7167242160), with the reviewer's proposed wording for F1, as a minimal revision addressing only the findings F1–F3 and the nits of the delta review of r2 on PR #1561. The edited passages are §0 (this line and the label list), §1.2 (OA-1 D6), §2.1 (one bullet), §2.2 (one body bullet and Conclusion (A)) and §5 (one outcome). CHANGES-r3.md lists each change."

***

## Not changed

- **Nit 5 (partial application of R7 in r2).** The review finds it acceptable; no change, per the owner's instruction.
- **The other citations of Main:364** (§2.2 "Structural limitations": "Main:364 holds verbatim for affine"; §2.4 (A): "the Bell ceiling at Main:364") are outside F3, which concerns the exclusion clause of §2.1 only. Main:364 is the heading of Main §3.3, the Bell section, so these read as section references; they are left unchanged.
- No result, grading or conclusion accepted in r2 is reopened.
