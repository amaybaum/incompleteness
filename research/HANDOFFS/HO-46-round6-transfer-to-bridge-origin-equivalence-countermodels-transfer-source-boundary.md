# HO-46 — transfer-source boundary
Version 1. From round6-transfer and the coordinator audit to bridge, origin, equivalence and countermodels.

## Exact statements and status

(T): every admissible one-token unitary preserves K through the pair dictionary.
(Tch): every InstAvail one-token channel preserves K through the idle-spectator dictionary.
Their derivation from existing OI premises remains OPEN. I4.66 and I4.38 certify PSD-state
validity in the kernel's matrix vocabulary. They reach an arbitrary K only through an
additional validity statement and state-space identification; choosing the PSD space
makes the identification K=Q3, which is excluded as an independent source.
I3.165's local-action clause and I3.150–I3.153 remain open or introduced.

CONDITIONAL: validity on an identified pair state space, ContextStable and LabelInvariant
imply Tch; Tch implies T. The repaired module builds in design, but is not certified.
The full class with K(Z_F) is a construction-level countercontrol in both forms.
No full-model independence or necessary premise for every quantum reconstruction is inferred.

| claim | T | Tch, K closed |
|---|---|---|
| from existing OI assumptions | OPEN | OPEN |
| with additional identified assumptions | CONDITIONAL | CONDITIONAL |
| required by the particular recorded bridge construction | countercontrol establishes it | countercontrol establishes it |
| required as an independent premise for any reconstruction | not shown | not shown |

H2's operation availability still needs pair transfer to give K-invariance.
H3's observer-native source is unresolved; the nearest CSD2 source remains unresolved.
A_miss's operation-based routes still need transfer. These statements retain their OPEN labels.

## Evidence

Round-6 source 694219a43bc9af449784c2b4dbc5b38b44df96a2:
- NOTES-B22.md SHA256 5adc21c1cc362ec79361ce640d838c43af98ac83a4c1807b1f2b4fe7901ab836.
- NOTES-E23.md SHA256 c99e45b0808a09367cfd96be70de948478dd887bf121157d21cd69c26a579e18.
- HP-round6-transfer-1 proposal SHA256 7f6670d8b1e9b62a437625565fb357a1aebabb61f2e16453c24b2ae2a8b57da3.

Coordinator audit at e7d380fcb9881e3063243aaa149e85be3cd0a914,
research/AUDITS/2026-10-11-round6/: source/blob checks, complete failed-job retrieval,
receipt identities and prefix history. The saved failed module remains at fd364020.
Repair design 13ad14a1ba2973245354aea7790c021d946b1ff0, run 38162504147:
Build success, seven standard axiom reports, 6136-result axiom check; census gate red
with 12 undispositioned modules. These are [D], not main certification.

## Receiving-thread limits

The threads may rely on the exact conditional statements and OPEN source classification
after copying this v1 handoff into their inbox and logging how it is used.
They may not assume that transfer was derived, that K(Z_F) is a full-model counterexample,
that H3 was sourced, or that a design build has been certified on main.
