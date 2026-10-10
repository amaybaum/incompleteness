"""Scratch: V3-13's edits to tools/release_gate.py and .github/workflows/verify.yml, as exact
(old, new) pairs. Never landed as is."""

GATE = 'tools/release_gate.py'
GATE_EDITS = [
("""  control_plane_lint   a control plane named its drafting snapshot as the
                       mandated execution base and required, at that base, the
                       absence of a token its own text carried; two of its
                       preconditions could not hold at the commit its chronology
                       control named, and owner review caught it after the
                       merge. Applies to control planes carrying a preconditions
                       block or changed in the diff under check.
  certificate_verifier the V2 round-certificate verifier, authoritative: a
                       historical round is data -- a certificate and an attestation
                       record -- verified by one generic tool, after six manifestations
                       of one defect in two repair rounds showed that a historical
                       round expressed as executable code running at every later head
                       invites an assertion against the wrong tree at every extension
                       point. The standalone workflow job runs it in shadow and gates
                       nothing; this step is where V2 can reject a build.
  v3-receipts          the V3 verdict, from round V3-11: every receipt in the
                       tree, verified by tools/v3_verifier.py --receipts from
                       the commit that last wrote it. A receipt is data no other
                       check reads, so this step is where a native round whose
                       receipt does not hold can reject a build. V1 and V2 keep
                       running beside it and can still fail the gate; they do
                       not decide whether a native round is protocol-valid.
""",
"""  legacy-records       the records of the rounds landed before V3, from round
                       V3-13: every record listed in
                       verification/infrastructure/legacy-records.json keeps its
                       blob, and no file is added under a closed namespace. The
                       manifest itself changes only as the governed work of a
                       native round whose receipt holds. Native rounds' own
                       records are kept by v3-receipts, not here.
  v3-self-test         tools/v3_verifier.py --self-test and --corpus, as
  v3-corpus            separate steps: regression evidence for the verifier's
                       implementation, which gates the build without being the
                       verdict itself.
  v3-receipts          the V3 verdict, from round V3-11: every receipt in the
                       tree, verified by tools/v3_verifier.py --receipts from
                       the commit that last wrote it, and, from round V3-13, the
                       round's record directory and seal record unchanged since
                       that commit. A receipt is data no other check reads, so
                       this step is where a native round whose receipt does not
                       hold, or whose records were rewritten after it held, can
                       reject a build.
"""),
("""        # control-plane-lint: a control plane must not give its drafting
        # snapshot's SHA to the mandated execution base, and no B-scoped
        # precondition may ask for the absence of a token the frozen artifact
        # itself carries. Applies to block-bearing and newly changed control
        # planes only; merged artifacts without a block are grandfathered.
        ("control-plane-lint",
                      [sys.executable, "tools/control_plane_lint.py"]),
""", ""),
("""        # certificate-verifier: the V2 round-certificate verifier in AUTHORITATIVE mode -- every
        # certificate, attestation record, relocation, live-policy clause and conformance vector,
        # the corpus executed as an exact set. This is the cutover wiring edit of certificate
        # round CV-1: the repository's ruleset requires only three status contexts, none of them
        # the standalone shadow job, so a red standalone job would not by itself block a merge;
        # this step, run by the required Mathlib bridge check, is what lets V2 reject a build.
        # V1's guard gates beside it and is not retired here.
        ("certificate-verifier",
                      [sys.executable, "tools/certificate_verifier.py", "--mode", "authoritative"]),
        # v3-receipts: the V3 verdict (round V3-11). Every receipt under verification/receipts/,
        # verified from the commit that last wrote it; a receipt that does not hold, or a
        # repository too shallow to decide, fails the gate. It needs full history, so the
        # workflow's Mathlib bridge job checks out with fetch-depth: 0.
        ("v3-receipts",
                      [sys.executable, "tools/v3_verifier.py", "--receipts", head]),
""",
"""        # legacy-records: the records of the rounds landed before V3 (round V3-13). Every record the
        # manifest lists keeps its blob and no file is added under a closed namespace; a changed
        # manifest is admitted only as the governed work of a native round whose receipt holds.
        ("legacy-records",
                      [sys.executable, "tools/legacy_records_check.py", head]),
        # v3-self-test and v3-corpus: the verifier's own regression evidence (round V3-13), kept
        # apart from the verdict so a defect of the implementation is named as such.
        ("v3-self-test",
                      [sys.executable, "tools/v3_verifier.py", "--self-test"]),
        ("v3-corpus", [sys.executable, "tools/v3_verifier.py", "--corpus"]),
        # v3-receipts: the V3 verdict (round V3-11). Every receipt under verification/receipts/,
        # verified from the commit that last wrote it, with the round's record directory and seal
        # record unchanged since then (round V3-13); a receipt that does not hold, or a
        # repository too shallow to decide, fails the gate. It and legacy-records need full
        # history, so the workflow's Mathlib bridge job checks out with fetch-depth: 0.
        ("v3-receipts",
                      [sys.executable, "tools/v3_verifier.py", "--receipts", head]),
"""),
]

WORKFLOW = '.github/workflows/verify.yml'
WORKFLOW_EDITS = [
("""  # The Mathlib bridge is a separate lake project with a pinned toolchain, and a separate
  # job: it is slower and has its own failure surface, and a breakage there must not be
  # able to obscure the state of the zero-import core gate above. fetch-depth: 0 is load-bearing
  # for the release gate's v3-receipts step, which verifies each receipt from the commit that last
  # wrote it and fails on a shallow repository (round V3-11).
""",
"""  # The Mathlib bridge is a separate lake project with a pinned toolchain, and a separate
  # job: it is slower and has its own failure surface, and a breakage there must not be
  # able to obscure the state of the zero-import core gate above. fetch-depth: 0 is load-bearing
  # for the release gate's v3-receipts step, which verifies each receipt from the commit that last
  # wrote it and fails on a shallow repository (round V3-11), and for its legacy-records step,
  # which reads a changed manifest's governing round from history (round V3-13).
"""),
("""      # Full history rather than the default depth-1 clone, and LOAD-BEARING. For commits it is
      # only a convenience -- `edge_rigidity_probe.py`'s R7-RBR guard recovers whatever commits it
      # needs itself, and fails closed if it cannot, so cloning deep merely makes that recovery a
      # no-op instead of a network round-trip. But `fetch-depth: 0` is also what fetches
      # `+refs/heads/*:refs/remotes/origin/*`, and the guard's ARCHIVE mode resolves the pull
      # request's base BRANCH by name against `refs/remotes/origin/<base ref>` and nothing else. A
      # shallow or single-branch checkout leaves that ref absent and archive mode fails closed, by
      # design: neither `pull_request.base.sha` -- which is no reliable source of the live tip, PR
      # #644 having carried base b78eac870ba3 across three later landings -- nor a local
      # `refs/heads/<base ref>` is accepted in its place.
      #
      # Note that the guard does NOT ask its question of HEAD in a pull_request run -- HEAD is the
      # synthetic merge commit, which has BOTH the base and the head as parents, so the ancestry
      # check would be vacuous; execution mode resolves pull_request.head.sha instead, and archive
      # mode the real head SHA or the base branch tip, never that HEAD.
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
""",
"""      # The default depth-1 checkout: no probe and no guard predicate reads repository history
      # (round V3-13).
      - uses: actions/checkout@v4
"""),
]
# the three non-required jobs, removed whole: from the comment opening the control-plane job to
# the end of the file
_W = open('/home/user/incompleteness/.github/workflows/verify.yml', encoding='utf-8').read()
WORKFLOW_EDITS.append((_W[_W.index('  # A.37 base certification for control planes.') - 1:], ''))
