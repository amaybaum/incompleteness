`tools/v3_receipt.py` builds a V3 receipt from a round's exact object ids and the attestation
records the host holds, deriving every repository fact with the verifier's own functions; it is a
builder, not a verifier (`infrastructure/round-v3-9-operationalization/`). A round the owner
authorizes as a provisional V3 pilot under `AGENTS.md` §A.39 runs in one pull request, its receipt
`receipts/<round>.json` is its protocol record, and `tools/v3_verifier.py --verify-round` must hold
on its receipt commit before the pull request lands.
