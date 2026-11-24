# Owner decision: authorization model (owner amaybaum, 2026-11-24, in session; not yet recorded on GitHub)

Quoted: "No, let's remove automated historical authorization verification entirely while retaining explicit
owner authorization as a procedural requirement."

Context: the v5.5.10 correction cycle was paused by the owner the same day ("I would pause the design correction
cycle and reconsider the authorization model itself"). v5.5.10 (fae222cd…) and v5.5.10a (b7e45218…) and their
reviews (78dc33d3…, f8eeb9c2…) are kept unchanged as records; neither was adopted. v5.5.10b was not produced
(unrun build script work-v5510/apply_b.py, 670997a5…).

## v6.0 flags (owner amaybaum, 2026-11-24, in session)
Quoted: "Confirm that the authorization-lint portion of acceptance condition 8 is superseded. All its remaining
scientific and technical requirements remain in force.
For F6, retain existing test identifiers to avoid unnecessary migration. Clearly document their technical meaning
and ensure that human-readable results never imply owner authorization.
Leave F1–F4 to independent review, with particular attention to ambiguous pin-table selection, mandatory consumer
verification and binding the actual executed workflow to the identified tool commit.
Do not introduce replacement authorization machinery."
Key review question: "whether an incorrect scientific result could pass verification under v6.0 when it would have
been rejected under v5.5.9."
