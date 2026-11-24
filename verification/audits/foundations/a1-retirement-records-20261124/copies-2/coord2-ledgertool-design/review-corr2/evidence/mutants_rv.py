"""Reviewer: U01 adapted to the post-B-1 rule (any x@y admitted)."""
K = 'ledger_coverage/engine/checker.py'
MUTANTS = [('U01a', K, [("_uses = re.compile(r'^\\s*(- )?uses: [A-Za-z0-9](?:-?[A-Za-z0-9])*/[A-Za-z0-9_.-]+(/[^@\\s]+)?@[0-9a-f]{40}\\s*$')",
                         "_uses = re.compile(r'^\\s*(- )?uses: \\S+@\\S+\\s*$')")], 'EI7 clause 1 (U01 on the B-1 rule)')]
