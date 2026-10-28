#!/usr/bin/env python3
"""controls.py -- the frozen content controls of native round SUB-241C-SPAN.

Round SUB-241C-SPAN takes up the legacy freeze
verification/programmes/substratum/lemma-24-1c-spanning-class-decision/preregistration.md
(blob b6f383741e84a1c53a599de349922f4d525e1349, merged by PR #643 as
e21a42c6303f19356cfca6402c76e842143155d1, never executed) as a native sealing round under
AGENTS.md section A.39. The legacy freeze reserved the guard tag R7-SCD. This file carries every
check R7-SCD would have made by content. It carries none of R7-SCD's chronology: no ancestry
check, no seal constant, no guard clause and no pin commit. The round's lifecycle is its V3
receipt, verification/receipts/SUB-241C-SPAN.json, and its seal record,
verification/v3-seals/SUB-241C-SPAN.json, which tools/v3_verifier.py checks.

Entry points, run from the repository root with `python3 -I`; every commit argument is a
full-length lowercase object id:

    --self-test                 hermetic: every outcome row on synthetic texts, then the mutation
                                controls, each of which must fail with its named code
    start-state <D>             the start state re-taken at D: pinned blobs, the legacy freeze,
                                the SC0 passages and their coordinates, free names and paths
    freeze <F>                  delta(D, F) is control-plane only, and the preregistration at F
                                carries this file's constants, templates and verbatim quotations
    check <C> --f <F> [--stage] the execution at C (a stage commit with --stage, else E)
    seal-record <F> <E> <L>     print the seal record bytes for F, E and the landing object L
    receipt <Q>                 the receipt and seal record at the receipt commit Q
    axioms <C> <log>            the result note's axiom table against a build log's reports

Standard library only. It reads git objects through `git cat-file`, `git ls-tree`,
`git diff-tree` and `git rev-list --parents`, with a fixed environment; it reads no ref, no
network, no clock and no working-tree file of the repository. It fails closed: anything
unexpected prints FAIL with a code and exits 1. It prints OK and exits 0 only when every check
named for the mode passed.
"""
import json
import os
import re
import subprocess
import sys

# ---------------------------------------------------------------------------------------------
# frozen identities
# ---------------------------------------------------------------------------------------------
ROUND = 'SUB-241C-SPAN'
RDIR = 'verification/programmes/substratum/round-sub-241c-spanning-v3/'
PREREG = RDIR + 'preregistration.md'
CONTROLS = RDIR + 'controls.py'
RESULT = RDIR + 'result.md'
RECEIPT = 'verification/receipts/SUB-241C-SPAN.json'
SEAL = 'verification/v3-seals/SUB-241C-SPAN.json'
MODULE = 'verification/lean-mathlib/OIBridge/SpanningClassReach.lean'
BRIDGE = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
README = 'verification/README.md'
LEGACY_DIR = 'verification/programmes/substratum/lemma-24-1c-spanning-class-decision/'
LEGACY_PREREG = LEGACY_DIR + 'preregistration.md'
LEGACY_BLOB = 'b6f383741e84a1c53a599de349922f4d525e1349'
LEGACY_MERGE = 'e21a42c6303f19356cfca6402c76e842143155d1'
LEGACY_DRAFT = 'b78eac870ba3ee9ef9e98659ac933bf97dc62226'
D = '0d917665d32287e5d0ce649012175f2c7bf75b09'
B_RESULT_PATHS = (
    'verification/programmes/substratum/lemma-24-1b-framework-data/result.md',
    'verification/receipts/SUB-241B-OBS.json',
)

BLOCK_ROUND = [
    'round SUB-241C-SPAN',
    'kind sealing',
    'record-directory verification/programmes/substratum/round-sub-241c-spanning-v3/',
]
BLOCK_GOVERNED = [
    'record AM verification/programmes/substratum/round-sub-241c-spanning-v3/',
    'record AM verification/receipts/SUB-241C-SPAN.json',
    'record A verification/v3-seals/SUB-241C-SPAN.json',
    'execution A verification/lean-mathlib/OIBridge/SpanningClassReach.lean',
    'execution M verification/lean-mathlib/OIBridge.lean',
    'execution M verification/lean-manuscript-census.json',
    'execution M verification/ROADMAP.md',
    'execution M verification/README.md',
]

# The legacy section 3.1 table, re-taken at D: (path, blob at the legacy drafting snapshot
# b78eac87, blob at the legacy base e21a42c6, blob at D). Read and never written.
READ_ONLY = [
    ('AGENTS.md', 'c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08',
     '3e3f00454db033b4fc519fd1123cd3f9b7f7cf24', 'ca0d37ad1b4aa95b266bac3d4b27acab207eefe6'),
    ('verification/programmes/substratum/lemma-24-1-semigroup-transfer/preregistration.md',
     'b8168df9ed1acff21eb89e84487b43470124f845', 'b8168df9ed1acff21eb89e84487b43470124f845',
     'b8168df9ed1acff21eb89e84487b43470124f845'),
    ('verification/programmes/substratum/lemma-24-1-semigroup-transfer/result.md',
     'b5822febb2626af48c29f6198fd6d74637ef9896', 'b5822febb2626af48c29f6198fd6d74637ef9896',
     'b5822febb2626af48c29f6198fd6d74637ef9896'),
    ('verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/preregistration.md',
     '98cfcfdc0e74ffe0186c502517a842bfeb25d351', '98cfcfdc0e74ffe0186c502517a842bfeb25d351',
     '98cfcfdc0e74ffe0186c502517a842bfeb25d351'),
    ('verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/result.md',
     '124a02c9d2b17c0cf280f15a00ab269f68e33a24', '124a02c9d2b17c0cf280f15a00ab269f68e33a24',
     '124a02c9d2b17c0cf280f15a00ab269f68e33a24'),
    ('verification/programmes/substratum/lemma-24-1b-framework-data/preregistration.md',
     'f614b666ad9098f866969c4c524e47f504e5d71c', 'f614b666ad9098f866969c4c524e47f504e5d71c',
     'f614b666ad9098f866969c4c524e47f504e5d71c'),
    ('verification/lean-mathlib/OIBridge/SemigroupTransfer.lean',
     '5ee55b5c7d3dcc45fac2a4b62c135a06d4010ea8', '5ee55b5c7d3dcc45fac2a4b62c135a06d4010ea8',
     '5ee55b5c7d3dcc45fac2a4b62c135a06d4010ea8'),
    ('verification/lean-mathlib/OIBridge/WordTraceSufficiency.lean',
     'ea8e96921f8c4bce9b26f7c99a1719d5f9e05520', 'ea8e96921f8c4bce9b26f7c99a1719d5f9e05520',
     'ea8e96921f8c4bce9b26f7c99a1719d5f9e05520'),
    ('verification/lean-mathlib/lean-toolchain',
     '025e59548e48cf71f2744154e2890beefe30a258', '025e59548e48cf71f2744154e2890beefe30a258',
     '025e59548e48cf71f2744154e2890beefe30a258'),
    ('verification/lean-mathlib/lakefile.toml',
     '5935a5aed3ed1bf4c5a7224049464d18ed4a8600', '5935a5aed3ed1bf4c5a7224049464d18ed4a8600',
     '5935a5aed3ed1bf4c5a7224049464d18ed4a8600'),
    ('verification/audits/foundations/act12-scope-propagation-audit.md',
     '1d471eddde3bc0df8b7dbf26ddf642c4af6783b5', '1d471eddde3bc0df8b7dbf26ddf642c4af6783b5',
     '1d471eddde3bc0df8b7dbf26ddf642c4af6783b5'),
    ('verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/preregistration.md',
     '6428e0acab070ccfd2a84d13c6f55616526206ba', '6428e0acab070ccfd2a84d13c6f55616526206ba',
     '6428e0acab070ccfd2a84d13c6f55616526206ba'),
]
# The legacy section 3.3 table, re-taken at D: the files the round writes.
WRITTEN = [
    (ROADMAP, '5ee35552fbfb41bd3172d3e3053c1a6d860a16d1',
     '4eb3a6502e65b54b77d4f3488fa8e105cdf0e8da', '69bedfe9efbb614e1cbc613be4639a3414b51f43'),
    (README, 'd25eb2d44d0aa324c095930f40174296fd0f2279',
     '9983b0781e565e9f9a01b4b3152c30842307a406', 'd3e89853fc198520e0c65122ba4bbe49c8a94c84'),
    ('verification/lean/edge_rigidity_probe.py', '6e334e832d99851e7a275842c1bdd856cbeb09f7',
     '75890ec6a66daf10d312ad5ae0d38e0b909863fa', '36dfadab6928c0fd9be3cc6198ae3f47966f740c'),
    (BRIDGE, '0bff51eb9cc3c22859da2ac0efc622910e77d7b4',
     '81814f25d9ea17aee2e15237af5bbfbe8dd92cfa', '179344d84e5f722f338fccfa9077f9a921192eea'),
    (CENSUS, '3e968e6c970301be5ba0b9631b234c957a6222d1',
     '86bda14f2f88335dfa4fd3fdb10f693ab134537e', '89a44bbc1fff815d624fd5c4d272c9b60c856199'),
]
# Read by the round at D and never written: the legacy seal state of sections 1.1, now records.
SEALS_READ = [
    ('verification/seals/SGT.json', '2ff4f68bd5e4283cb67ca53b20b745a998486252',
     {'round': 'SGT', 'kind': 'sealed', 'base': 'c46e1606d4cafe2720afd69dc06c667eb0f1acff',
      'sealed_head': '57103e9ddf430c538094fed48358c4d1b050ce4d',
      'merge': '11a8a59d22793a10182f853fe3c05edf5415d724'}),
    ('verification/seals/WTS.json', '27104c27c5cade441bc6749cf8c862a2da8b5610',
     {'round': 'WTS', 'kind': 'sealed', 'base': 'baadea2638019b335d96c892590491a6fb420936',
      'sealed_head': 'c31fe45d28d6aa37782902f67aba404ef721a59e',
      'merge': '6a6f206f830f5b44e1b19a6912b823d545207126'}),
]
LEGACY_MANIFEST = ('verification/infrastructure/legacy-records.json',
                   '9e48bd31797e1673f03807e699a10ae4a0b960c7')
# Names the round introduces, each free at D outside the legacy freeze.
FREE_NAMES = ['SpanningClassReach', 'SUB-241C', 'round-sub-241c', 'v3-seals/SUB-241C',
              'SC4a_', 'SC4b_', 'SC4c_', 'SC4d_']
FREE_PATHS = [RDIR, RECEIPT, SEAL, MODULE, 'verification/v3-seals/']

# SC0: the legacy section 2 passages. (id, path, legacy line ranges of the quoted fragments,
# coordinates at D per fragment, coordinates in the blob the legacy freeze pinned).
PASSAGES = [
    ('2.1', ROADMAP, (165, 168), [(64, 64)], [(64, 64)]),
    ('2.2', ROADMAP, (176, 181), [(679, 685)], [(516, 522)]),
    ('2.3', ROADMAP, (185, 195), [(696, 707)], [(533, 544)]),
    ('2.4', 'verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/result.md',
     (199, 211), [(62, 74)], [(62, 74)]),
    ('2.5', 'verification/programmes/substratum/lemma-24-1-semigroup-transfer/result.md',
     (215, 216), [(229, 231)], [(229, 231)]),
    ('2.6', 'verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/result.md',
     (220, 224), [(174, 177), (182, 183)], [(174, 177), (182, 183)]),
    ('2.7', 'verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/'
            'preregistration.md', (228, 237), [(399, 408)], [(399, 408)]),
    ('2.8a', 'verification/lean-mathlib/OIBridge/SemigroupTransfer.lean', (245, 249),
     [(98, 102)], [(98, 102)]),
    ('2.8b', 'verification/lean-mathlib/OIBridge/WordTraceSufficiency.lean', (253, 259),
     [(93, 95), (101, 103)], [(93, 95), (101, 103)]),
]

# The legacy line ranges this preregistration must quote verbatim (the adoption).
ADOPTED_RANGES = [(66, 82), (297, 301), (331, 349), (351, 357), (361, 382), (386, 545),
                  (549, 572), (576, 624), (628, 656), (660, 700), (704, 723), (752, 757),
                  (761, 768), (772, 790), (828, 840)]
QUOTE_MARK = re.compile(r'^Legacy lines (\d+)–(\d+) \(blob `b6f38374`\), verbatim:$')

# The three frozen post-round sentences: legacy lines 582-591, 595-604 and 608-616.
SENTENCE_RANGES = {'SC5-coincide': (582, 591), 'SC5-strict': (595, 604),
                   'SC5-UNDECIDED': (608, 616)}
SENTENCES = {
    'SC5-coincide': (
        "On every finite carrier `V × H`, the spanning hypothesis `BlockSpanning U` and the "
        "cyclicity predicate `HiddenCommutantTrivial U` are the same condition, both directions "
        "at evidence level 2. Lemma 24.1A's biconditional `WT3_spanning_iff` therefore holds on "
        "exactly the class the semigroup-transfer route's own GNS-cyclic reading assumes, and "
        "the class on which `ST3` refuted that reading and the class on which `WT3` established "
        "the biconditional are one class. This is a statement about two predicates on finite "
        "matrices. **It does not repair Lemma 24.1, does not restore the manuscripts' route, "
        "does not say the four generators are complete or incomplete, and says nothing about "
        "whether the reconstruction framework supplies the block-word trace data, which is "
        "round 24.1B's question and is untouched here.** The `P1` obligation remains OPEN and "
        "the row's label does not move."),
    'SC5-strict': (
        "On every finite carrier `V × H`, `BlockSpanning U` implies `HiddenCommutantTrivial U` "
        "at evidence level 2, and the converse fails on the carrier exhibited in the result "
        "note. The spanning hypothesis is therefore strictly stronger than the cyclicity "
        "predicate, and Lemma 24.1A's biconditional `WT3_spanning_iff` holds on a class "
        "strictly narrower than the one the semigroup-transfer route's own GNS-cyclic reading "
        "assumes. This is a statement about two predicates on finite matrices. **It does not "
        "repair Lemma 24.1, does not restore the manuscripts' route, does not say the four "
        "generators are complete or incomplete, does not say that `WT3` is idle, and says "
        "nothing about whether the reconstruction framework supplies the block-word trace "
        "data, which is round 24.1B's question and is untouched here.** The `P1` obligation "
        "remains OPEN and the row's label does not move."),
    'SC5-UNDECIDED': (
        "`BlockSpanning U` implies `HiddenCommutantTrivial U` at the strength recorded for "
        "`SC4(a)`. Whether the converse holds is UNDECIDED, with the obstruction named in the "
        "result note, and the relation between the class Lemma 24.1A's biconditional lands on "
        "and the class the semigroup-transfer route's GNS-cyclic reading assumes is therefore "
        "settled in one direction and open in the other. What the record does and does not "
        "settle is stated in the result note and is not extrapolated. **Nothing here repairs "
        "Lemma 24.1, restores the manuscripts' route, or says the four generators are complete "
        "or incomplete, and nothing here bears on whether the reconstruction framework supplies "
        "the block-word trace data, which is round 24.1B's question and is untouched.** The "
        "`P1` obligation remains OPEN and the row's label does not move."),
}
OBSTRUCTION_TERMS = [
    "`wordSpan U` is a unital `*`-closed subalgebra of `Matrix H H ℂ`",
    "`HiddenCommutantTrivial U` says its commutant is the scalars",
    "the conclusion `wordSpan U = ⊤` is the double commutant theorem in spatial "
    "finite-dimensional form",
    "the named bounded search found",
]
HALT_STATEMENT = ("No frozen post-round sentence applies to this outcome; the round halts under "
                  "the specification's `S12`.")

# ---------------------------------------------------------------------------------------------
# the kernel statement pins
# ---------------------------------------------------------------------------------------------
HEADER_IMPORT = 'import OIBridge.WordTraceSufficiency'
HEADER_REQUIRED = [
    'namespace OIBridge',
    'namespace SpanningClassReach',
    'set_option autoImplicit false',
    'open Matrix SemigroupTransfer WordTraceSufficiency',
    'variable {V H : Type} [Fintype V] [DecidableEq V] [Fintype H] [DecidableEq H]',
]
FOOTER = ['end SpanningClassReach', 'end OIBridge']
NUM = r'([1-9][0-9]*)'
CARRIER = r'Matrix \(Fin %s × Fin %s\) \(Fin \{a} × Fin \{b}\) ℂ' % (NUM, NUM)


def _carrier_re(tail):
    pat = (r'∃ U : Matrix \(Fin ' + NUM + r' × Fin ' + NUM + r'\) \(Fin \1 × Fin \2\) ℂ, '
           + re.escape(tail) + ' :=')
    return pat


# label -> (target, sign, display text, regex of the normalized statement up to ':=', min size)
LABELS = {
    'SC4a_spanning_imp_hct': ('a', 'pos',
        'theorem SC4a_spanning_imp_hct (U : Matrix (V × H) (V × H) ℂ) (hU : BlockSpanning U) : '
        'HiddenCommutantTrivial U :=', None, 0),
    'SC4a_counterexample': ('a', 'neg',
        'theorem SC4a_counterexample : ∃ U : Matrix (Fin a × Fin b) (Fin a × Fin b) ℂ, '
        'BlockSpanning U ∧ ¬ HiddenCommutantTrivial U :=',
        _carrier_re('BlockSpanning U ∧ ¬ HiddenCommutantTrivial U'), 1),
    'SC4b_hct_imp_spanning': ('b', 'pos',
        'theorem SC4b_hct_imp_spanning (U : Matrix (V × H) (V × H) ℂ) '
        '(hU : HiddenCommutantTrivial U) : BlockSpanning U :=', None, 0),
    'SC4b_separating': ('b', 'neg',
        'theorem SC4b_separating : ∃ U : Matrix (Fin a × Fin b) (Fin a × Fin b) ℂ, '
        'HiddenCommutantTrivial U ∧ ¬ BlockSpanning U :=',
        _carrier_re('HiddenCommutantTrivial U ∧ ¬ BlockSpanning U'), 1),
    'SC4c_pairC_spanning': ('c', 'pos',
        'theorem SC4c_pairC_spanning : ∃ U : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ, '
        'U = Equiv.Perm.permMatrix ℂ φC ∧ BlockSpanning U :=', None, 0),
    'SC4c_pairC_not_spanning': ('c', 'neg',
        'theorem SC4c_pairC_not_spanning : ∃ U : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ, '
        'U = Equiv.Perm.permMatrix ℂ φC ∧ ¬ BlockSpanning U :=', None, 0),
    'SC4d_spanning_witness': ('d', 'span',
        'theorem SC4d_spanning_witness : ∃ U : Matrix (Fin a × Fin b) (Fin a × Fin b) ℂ, '
        'BlockSpanning U :=', _carrier_re('BlockSpanning U'), 2),
    'SC4d_nonspanning_witness': ('d', 'nonspan',
        'theorem SC4d_nonspanning_witness : ∃ U : Matrix (Fin a × Fin b) (Fin a × Fin b) ℂ, '
        '¬ BlockSpanning U :=', _carrier_re('¬ BlockSpanning U'), 2),
}
# the merged witness notations, verbatim from SemigroupTransfer.lean (normalized whitespace)
NOTATIONS = {
    'φA': 'local notation "φA" => (Equiv.swap ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)))',
    "φA'": 'local notation "φA\'" => (Equiv.swap ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2)))',
    'φC': 'local notation "φC" => (Equiv.swap ((0 : Fin 2), (2 : Fin 3)) ((1 : Fin 2), (0 : Fin 3)) '
          '* Equiv.swap ((1 : Fin 2), (1 : Fin 3)) ((1 : Fin 2), (2 : Fin 3)))',
    "φC'": 'local notation "φC\'" => (Equiv.swap ((0 : Fin 2), (2 : Fin 3)) ((1 : Fin 2), '
           '(0 : Fin 3)) * Equiv.swap ((1 : Fin 2), (1 : Fin 3)) ((1 : Fin 2), (2 : Fin 3)) * '
           'Equiv.swap ((0 : Fin 2), (0 : Fin 3)) ((0 : Fin 2), (1 : Fin 3)))',
}
SLOT1 = 'def hiddenCommutant (U : Matrix (V × H) (V × H) ℂ) : Submodule ℂ (Matrix H H ℂ) :='
SLOT2_RE = re.compile(r"def ([A-Za-z_][A-Za-z0-9_']*) : Matrix \(Fin " + NUM + r" × Fin " + NUM
                      + r"\) \(Fin \2 × Fin \3\) ℂ :=")
FORBIDDEN_IDENTS = ['sorry', 'admit', 'native_decide', 'ofReduceBool', 'implemented_by',
                    'extern', 'unsafe', 'include', 'omit', 'HiddenConjugate',
                    'WordTracesEqual', 'transferMap', 'familyAt', 'enlarge', 'H_obs', 'O_set',
                    'interleave', 'relaxedAutoImplicit']
PERMITTED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}

# ---------------------------------------------------------------------------------------------
# the outcome, the vector and the surfaces
# ---------------------------------------------------------------------------------------------
WORDS = {
    'a': {'pos': '`SC4(a)` established', 'neg': '`SC4(a)` refuted', 'und': '`SC4(a)` UNDECIDED'},
    'b': {'pos': '`SC4(b)` established', 'neg': '`SC4(b)` refuted', 'und': '`SC4(b)` UNDECIDED'},
    'c': {'pos': '`SC4(c)` `φ̂_C` spanning', 'neg': '`SC4(c)` `φ̂_C` not spanning',
          'und': '`SC4(c)` UNDECIDED'},
    'd': {'pos': '`SC4(d)` both witnesses exhibited', 'und': '`SC4(d)` UNDECIDED'},
}


def sc5(a, b):
    """The legacy SC5 rule, with the cells it writes no sentence for marked HALT."""
    if a == 'pos' and b == 'pos':
        return 'SC5-coincide'
    if a == 'pos' and b == 'neg':
        return 'SC5-strict'
    if b == 'und' and a in ('pos', 'und'):
        return 'SC5-UNDECIDED'
    return 'HALT'


def vector(o):
    s = sc5(o['a'], o['b'])
    tail = '`%s`' % s if s != 'HALT' else 'no frozen `SC5` outcome'
    return 'Outcome: ' + ' · '.join(WORDS[k][o[k]] for k in 'abcd') + ' · ' + tail + '.'


ROADMAP_ANCHOR = ("and 24.1B is named and not begun. No\nmanuscript edit.\n\n"
                  "This is the row to watch")
ROADMAP_CUT = len("and 24.1B is named and not begun. No\nmanuscript edit.\n\n")
ROADMAP_PARA = (
    "**Executed, 24.1C** — `programmes/substratum/round-sub-241c-spanning-v3/`, the native "
    "sealing round `SUB-241C-SPAN` (receipt `receipts/SUB-241C-SPAN.json`, seal record "
    "`v3-seals/SUB-241C-SPAN.json`; `OIBridge/SpanningClassReach.lean`), taking up the legacy "
    "freeze `programmes/substratum/lemma-24-1c-spanning-class-decision/` (preregistration blob "
    "`b6f383741e84a1c53a599de349922f4d525e1349`, merged by PR #643 as `e21a42c`, never "
    "executed). {VECTOR} The frozen sentence for that outcome: {SENTENCE}")
README_ANCHOR = "## Seal infrastructure round SI-1 — the shadow validator and the equivalence census"
README_PARA = (
    "The reconstruction programme's Lemma 24.1C round, the spanning-class decision, is the "
    "native sealing round `SUB-241C-SPAN` (`programmes/substratum/round-sub-241c-spanning-v3/`, "
    "receipt `receipts/SUB-241C-SPAN.json`, seal record `v3-seals/SUB-241C-SPAN.json`). It takes "
    "up the legacy freeze `programmes/substratum/lemma-24-1c-spanning-class-decision/` "
    "(preregistration blob `b6f383741e84a1c53a599de349922f4d525e1349`, merged by PR #643 as "
    "`e21a42c`, never executed). `OIBridge/SpanningClassReach.lean` places `BlockSpanning`, the "
    "class on which `WT3_spanning_iff` lands, against `HiddenCommutantTrivial`. {VECTOR} The "
    "frozen sentence for that outcome is stated in the result note and in the P1 section of "
    "`ROADMAP.md`. The P1 label stays OPEN, no manuscript is read or edited, and no 24.1B object "
    "is consulted. The round adds no guard clause: its content checks are the frozen "
    "`controls.py` in its record directory, and its lifecycle is its receipt.")
BRIDGE_ANCHOR = 'import OIBridge.WordTraceSufficiency\n'
BRIDGE_LINE = 'import OIBridge.SpanningClassReach\n'
CENSUS_NAME = ('the spanning-class decision: BlockSpanning against HiddenCommutantTrivial '
               '(round SUB-241C-SPAN, substratum Lemma 24.1C)')
CENSUS_NOTE = (
    "Substratum Lemma 24.1C, the native sealing round SUB-241C-SPAN under AGENTS.md §A.39, "
    "taking up the legacy freeze programmes/substratum/lemma-24-1c-spanning-class-decision/"
    "preregistration.md (blob b6f383741e84a1c53a599de349922f4d525e1349, merged by PR #643, "
    "never executed). {VECTOR} Kernel-only: no manuscript anchor, and no manuscript is read or "
    "edited; the P1 label stays OPEN. Record: "
    "verification/programmes/substratum/round-sub-241c-spanning-v3/.")

# ---------------------------------------------------------------------------------------------
# the result note
# ---------------------------------------------------------------------------------------------
HEADINGS = ['## Outcome', '## SC0', '## SC1', '## SC2', '## SC3', '## SC4(a)', '## SC4(b)',
            '## SC4(b) bounded search', '## SC4(c)', '## SC4(d)', '## SC5', '## SC6',
            '## Axiom table', '## Definition budget', '## Discrepancies', '## Independence']
NOTE_NO_MANUSCRIPT = 'No manuscript file was read and no 24.1B object was consulted.'
NOTE_B_ABSENT = 'No 24.1B result note was present at `F`, and none was consumed.'
NOTE_B_PRESENT = 'A 24.1B result note was present at `F` and was not read, cited or consumed.'
NOTE_TYPE_P = ('`SC0`–`SC3` and `SC6` are type P, carried by quotation and by recorded silence; '
               '`SC4` is at evidence level 2.')
NOTE_SLOT1 = {True: 'Slot 1 (`hiddenCommutant`): fired.',
              False: 'Slot 1 (`hiddenCommutant`): unused.'}
NOTE_SLOT2 = {True: 'Slot 2 (a named witness datum for `SC4(d)`): fired.',
              False: 'Slot 2 (a named witness datum for `SC4(d)`): unused.'}
NOTE_PAIR_A = 'is derived through `SC4(a)`'
SEARCH_LINES = ['Search terms:', 'Trees searched:', 'Result:']
QUOTE_CITE = re.compile(r'^`([^`:]+):(\d+)–(\d+)`, blob `([0-9a-f]{40})`:$')
FORBIDDEN_PHRASES = ['lemma 24.1 is repaired', 'lemma 24.1 is false', 'theorem 24 is false',
                     'theorem 24 is repaired', 'completeness holds', 'completeness fails',
                     'the generators are complete', 'the generators are incomplete',
                     "the manuscripts' route is restored", 'the transfer is refuted',
                     'the programme should next', 'the selection principle is']
FORBIDDEN_STARTS = ['the framework supplies', 'the framework does not supply']

# The paths delta(D, E) changes on a decided outcome.
E_PATHS = {('A', PREREG), ('A', CONTROLS), ('A', RESULT), ('A', MODULE), ('M', BRIDGE),
           ('M', CENSUS), ('M', ROADMAP), ('M', README)}


class Fail(Exception):
    pass


# ---------------------------------------------------------------------------------------------
# pure helpers
# ---------------------------------------------------------------------------------------------
def norm(s):
    return ' '.join(s.split())


def strip_comments(src):
    """Lean source with comments blanked (newlines kept); string literals kept."""
    out, i, n, depth, instr = [], 0, len(src), 0, False
    while i < n:
        c = src[i]
        if depth == 0 and instr:
            out.append(c)
            if c == '\\' and i + 1 < n:
                out.append(src[i + 1])
                i += 2
                continue
            if c == '"':
                instr = False
            i += 1
            continue
        if src.startswith('/-', i):
            depth += 1
            out.append('  ')
            i += 2
            continue
        if depth > 0:
            if src.startswith('-/', i):
                depth -= 1
                out.append('  ')
                i += 2
                continue
            out.append('\n' if c == '\n' else ' ')
            i += 1
            continue
        if src.startswith('--', i):
            j = src.find('\n', i)
            j = n if j < 0 else j
            out.append(' ' * (j - i))
            i = j
            continue
        if c == '"':
            instr = True
        out.append(c)
        i += 1
    if depth or instr:
        raise Fail('module:unterminated-comment-or-string')
    return ''.join(out)


def items(code):
    """Top-level items: a line starting at column 0 begins one; an attribute-only line joins the
    next."""
    out, cur = [], None
    for line in code.split('\n'):
        if line.strip() == '':
            if cur is not None:
                cur.append(line)
            continue
        if line[0] not in ' \t':
            if cur is not None and not re.fullmatch(r'\s*@\[[^\]]*\]\s*', '\n'.join(cur)):
                out.append('\n'.join(cur))
                cur = [line]
            elif cur is None:
                cur = [line]
            else:
                cur.append(line)
        else:
            if cur is None:
                raise Fail('module:indented-first-line')
            cur.append(line)
    if cur is not None:
        out.append('\n'.join(cur))
    return [norm(x) for x in out]


DECL = re.compile(r"^(?:@\[[^\]]*\] )?(?:(?:private|protected|noncomputable|nonrec) )*"
                  r"(theorem|lemma|def|abbrev|instance|structure|class|inductive|opaque|axiom|"
                  r"example)\b ?([^ ]*)")
IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_'.]*")


def tokens(text):
    return [t.split('.')[-1] for t in IDENT.findall(text)]


def analyse_module(src):
    """(labels, theorems, defs, closure, errors)."""
    errs = []
    code = strip_comments(src)
    its = items(code)
    if not its or its[0] != HEADER_IMPORT:
        errs.append('module:import')
    k = 1
    while k < len(its) and its[k].startswith('import '):
        if not re.fullmatch(r'import Mathlib(\.[A-Za-z0-9_]+)+', its[k]):
            errs.append('module:import')
        k += 1
    body = its[k:]
    first_decl = next((i for i, x in enumerate(body) if DECL.match(x)), len(body))
    for h in HEADER_REQUIRED:
        if body[:first_decl].count(h) != 1:
            errs.append('module:header:' + h.split(' ')[0])
    if [x for x in body if not x.startswith('#print axioms ')][-2:] != FOOTER:
        errs.append('module:footer')
    theorems, defs, prints, notations = {}, {}, [], []
    for x in body:
        m = DECL.match(x)
        if m:
            kw, name = m.group(1), m.group(2)
            if kw in ('theorem', 'lemma'):
                if name in theorems or name in defs:
                    errs.append('module:duplicate-name')
                theorems[name] = x
            elif kw in ('def', 'abbrev'):
                defs[name] = x
            else:
                errs.append('module:forbidden-declaration:' + kw)
            continue
        if x.startswith('#print axioms '):
            prints.append(x[len('#print axioms '):])
            continue
        if x.startswith('local notation '):
            notations.append(x)
            continue
        if x.startswith('open '):
            if re.search(r'\bin\b', x):
                errs.append('module:open-in')
            continue
        if x.startswith('set_option '):
            if 'autoImplicit' in x and x != 'set_option autoImplicit false':
                errs.append('module:autoImplicit')
            continue
        if x.startswith('variable '):
            if x != HEADER_REQUIRED[4]:
                errs.append('module:variable')
            continue
        if x in HEADER_REQUIRED or x in FOOTER:
            continue
        if x.startswith('attribute [local ') or x == 'noncomputable section':
            continue
        if x == 'section' or x.startswith('section ') or x == 'end' or (
                x.startswith('end ') and x not in FOOTER):
            continue
        errs.append('module:forbidden-command:' + x.split(' ')[0])
    if sum(1 for x in body if x.startswith('variable ')) != 1:
        errs.append('module:variable')
    for t in tokens(code):
        if t in FORBIDDEN_IDENTS or t.startswith('WT2'):
            errs.append('module:forbidden-token:' + t)
    for nt in notations:
        mm = re.match(r'local notation "([^"]*)"', nt)
        if not mm or NOTATIONS.get(mm.group(1)) != nt:
            errs.append('module:notation')
    # the definition budget
    slot1 = slot2 = False
    for name, x in defs.items():
        if name == 'hiddenCommutant':
            core = re.sub(r'^(?:@\[[^\]]*\] )?(?:noncomputable )?', '', x)
            if not core.startswith(SLOT1):
                errs.append('module:budget')
            slot1 = True
            continue
        core = re.sub(r'^(?:@\[[^\]]*\] )?(?:noncomputable )?', '', x)
        m2 = SLOT2_RE.match(core)
        if slot2 or not m2 or int(m2.group(2)) < 2 or int(m2.group(3)) < 2 \
                or name.startswith('SC'):
            errs.append('module:budget')
        slot2 = name
    # the prints
    want = ['OIBridge.SpanningClassReach.' + t for t in theorems]
    if sorted(prints) != sorted(want) or len(set(prints)) != len(prints):
        errs.append('module:prints')
    # the labels
    labels = {}
    for name, x in theorems.items():
        if name.startswith(('SC4', 'SC5', 'SC0', 'SC1', 'SC2', 'SC3', 'SC6')) \
                and name not in LABELS:
            errs.append('module:stray-label:' + name)
    for name, (tgt, sign, disp, rx, mn) in LABELS.items():
        if name not in theorems:
            continue
        x = theorems[name]
        head = x[:x.find(' :=') + 3] if ' :=' in x else ''
        if rx is None:
            ok = head == disp
        else:
            m3 = re.fullmatch('theorem ' + name + ' : ' + rx, head)
            ok = bool(m3) and int(m3.group(1)) >= mn and int(m3.group(2)) >= mn
        if not ok:
            errs.append('module:label-statement:' + name)
            continue
        labels[name] = (tgt, sign)
    # dependency closure inside the module
    names = set(theorems) | set(defs)
    direct = {}
    for name in names:
        txt = theorems.get(name) or defs.get(name)
        direct[name] = {t for t in tokens(txt) if t in names and t != name}

    def closure(n):
        seen, stack = set(), [n]
        while stack:
            for m4 in direct.get(stack.pop(), ()):
                if m4 not in seen:
                    seen.add(m4)
                    stack.append(m4)
        return seen
    clos = {n: closure(n) for n in names}
    for c in ('SC4c_pairC_spanning', 'SC4c_pairC_not_spanning'):
        if c in clos and clos[c] & {'SC4b_hct_imp_spanning', 'SC4b_separating'}:
            errs.append('module:sc4c-through-sc4b')
    if slot2 and not any(slot2 in clos.get(w, ()) for w in
                         ('SC4d_spanning_witness', 'SC4d_nonspanning_witness')):
        errs.append('module:budget')
    return labels, theorems, {'slot1': slot1, 'slot2': bool(slot2)}, clos, sorted(set(errs))


def outcome_of(labels):
    """The SC4 outcome from the labels the module carries; errors for a target labelled both
    ways."""
    errs, o = [], {}
    for t in 'abc':
        signs = {s for (tt, s) in labels.values() if tt == t}
        if len(signs) > 1:
            errs.append('module:both-labels:SC4' + t)
        o[t] = 'pos' if signs == {'pos'} else 'neg' if signs == {'neg'} else 'und'
    ds = {s for (tt, s) in labels.values() if tt == 'd'}
    o['d'] = 'pos' if ds == {'span', 'nonspan'} else 'und'
    return o, errs


def outside_quotes(text):
    lines = [ln for ln in text.split('\n') if not ln.lstrip().startswith('>')]
    t = '\n'.join(lines)
    t = re.sub(r'`[^`]*`', ' ', t)
    t = re.sub(r'"[^"\n]*"', ' ', t)
    t = re.sub(r'“[^”]*”', ' ', t)
    return t


def phrase_errors(text, where):
    errs = []
    flat = norm(outside_quotes(text)).lower()
    for p in FORBIDDEN_PHRASES:
        if p in flat:
            errs.append('%s:forbidden:%s' % (where, p))
    paras, cur = [], []
    for ln in outside_quotes(text).split('\n'):
        if ln.strip() == '' or ln.lstrip().startswith(('#', '|', '- ', '* ')):
            if cur:
                paras.append(norm(' '.join(cur)).lower())
            cur = [] if ln.strip() == '' or ln.lstrip().startswith(('#', '|')) else [ln]
            if ln.lstrip().startswith(('#', '|')):
                paras.append(norm(ln).lstrip('#| ').lower())
        else:
            cur.append(ln)
    if cur:
        paras.append(norm(' '.join(cur)).lower())
    for p in FORBIDDEN_STARTS:
        if any(re.search(r'(^|[.!?:] )' + re.escape(p), para) for para in paras):
            errs.append('%s:forbidden:%s' % (where, p))
    return errs


def blockquote_after(lines, i):
    """The blockquote run starting at lines[i], unquoted."""
    out = []
    while i < len(lines) and lines[i].startswith('>'):
        ln = lines[i]
        if ln == '>':
            out.append('')
        elif ln.startswith('> '):
            out.append(ln[2:])
        else:
            return None, i
        i += 1
    return out, i


def sc0_rows(coords):
    rows = []
    for pid, path, _rng, _d, _pin in PASSAGES:
        c = coords[pid]
        rows.append('| §%s | `%s` | %s |' % (pid, path, '; '.join('%d–%d' % x for x in c)))
    return rows


def check_note(note, ctx):
    """Every frozen requirement of the result note; ctx carries the measured quantities."""
    errs = []
    o, s5, vec = ctx['outcome'], sc5(ctx['outcome']['a'], ctx['outcome']['b']), ctx['vector']
    lines = note.split('\n')
    for h in HEADINGS:
        if lines.count(h) != 1:
            errs.append('note:heading:' + h[3:])
    if note.count(vec) != 1 or len(re.findall(r'^Outcome: ', note, re.M)) != 1:
        errs.append('note:vector')
    flatq = norm(note.replace('\n>', '\n').replace('\n> ', '\n'))
    for k, sent in SENTENCES.items():
        n = flatq.count(norm(sent))
        if k == s5 and n != 1:
            errs.append('note:sentence')
        if k != s5 and n != 0:
            errs.append('note:other-sentence')
    if s5 == 'HALT':
        if note.count(HALT_STATEMENT) != 1:
            errs.append('note:halt-statement')
    elif HALT_STATEMENT in note:
        errs.append('note:halt-statement')
    if s5 in SENTENCES:
        # the sentence is carried as a blockquote, exactly the frozen text
        found = False
        i = 0
        while i < len(lines):
            if lines[i].startswith('>'):
                q, j = blockquote_after(lines, i)
                if q is not None and norm(' '.join(q)) == norm(SENTENCES[s5]):
                    found = True
                i = max(j, i + 1)
            else:
                i += 1
        if not found:
            errs.append('note:sentence-not-quoted')
    if note.count(NOTE_NO_MANUSCRIPT) != 1:
        errs.append('note:no-manuscript')
    want_b, other_b = ((NOTE_B_PRESENT, NOTE_B_ABSENT) if ctx['b_present']
                       else (NOTE_B_ABSENT, NOTE_B_PRESENT))
    if note.count(want_b) != 1 or other_b in note:
        errs.append('note:24.1b-presence')
    if note.count(NOTE_TYPE_P) != 1:
        errs.append('note:type-p')
    for flag, table in (('slot1', NOTE_SLOT1), ('slot2', NOTE_SLOT2)):
        if note.count(table[ctx['budget'][flag]]) != 1 or table[not ctx['budget'][flag]] in note:
            errs.append('note:budget-line')
    via_a = 'SC4a_spanning_imp_hct' in ctx['closure'].get('SC4d_nonspanning_witness', set())
    if (NOTE_PAIR_A in note) != via_a:
        errs.append('note:pair-a-route')
    # SC0 rows, measured at F
    for row in sc0_rows(ctx['coords']):
        if note.count(row) != 1:
            errs.append('note:sc0-row')
            break
    # the bounded search
    sec = section(note, '## SC4(b) bounded search')
    if sec is None or not all(re.search(r'^' + re.escape(s) + r' \S', sec, re.M)
                              for s in SEARCH_LINES):
        errs.append('note:bounded-search')
    if s5 == 'SC5-UNDECIDED':
        sec5 = section(note, '## SC5') or ''
        if not re.search(r'^Obstruction: \S', sec5, re.M):
            errs.append('note:obstruction')
        elif 'double commutant' in sec5.lower() and not all(
                norm(t) in norm(sec5) for t in OBSTRUCTION_TERMS):
            errs.append('note:obstruction-terms')
    # the axiom table
    rows = re.findall(r"^\| `([A-Za-z0-9_']+)` \| `\[([^\]]*)\]` \|$", note, re.M)
    names = [r[0] for r in rows]
    if sorted(names) != sorted(ctx['theorems']) or len(set(names)) != len(names):
        errs.append('note:axiom-table')
    for _n, ax in rows:
        got = {a.strip() for a in ax.split(',') if a.strip()}
        if not got <= PERMITTED_AXIOMS:
            errs.append('note:axiom-table')
    # quotations: each cited quotation verbatim in the cited blob
    for i, ln in enumerate(lines):
        m = QUOTE_CITE.match(ln)
        if not m:
            continue
        path, a, b, blob = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        q, _j = (blockquote_after(lines, i + 2) if i + 1 < len(lines) and lines[i + 1] == ''
                 else (None, 0))
        src = ctx['quote_source'](path, blob)
        if q is None or src is None or a < 1 or b < a or b > len(src) or src[a - 1:b] != q:
            errs.append('note:quote')
    if re.search(r'(^|[^A-Za-z0-9_])(papers|book)/[A-Za-z0-9]', note):
        errs.append('note:manuscript-path')
    errs += phrase_errors(note, 'note')
    return errs


def section(text, heading):
    lines = text.split('\n')
    if heading not in lines:
        return None
    i = lines.index(heading) + 1
    out = []
    while i < len(lines) and not lines[i].startswith('## '):
        out.append(lines[i])
        i += 1
    return '\n'.join(out)


def insertion(d_text, c_text, cut, para, where):
    """C must be D with one inserted block at `cut` whose normalized text is `para`."""
    pre, suf = d_text[:cut], d_text[cut:]
    if not (c_text.startswith(pre) and c_text.endswith(suf)) or \
            len(c_text) < len(d_text):
        return [where + ':insertion']
    mid = c_text[len(pre):len(c_text) - len(suf)]
    if not mid.endswith('\n\n') or norm(mid) != norm(para) or '\n\n' in mid.strip('\n'):
        return [where + ':insertion']
    return phrase_errors(mid, where)


def render(template, o):
    s5 = sc5(o['a'], o['b'])
    return template.replace('{VECTOR}', vector(o)).replace('{SENTENCE}', SENTENCES.get(s5, ''))


def census_entry(o):
    return {'name': CENSUS_NAME, 'modules': ['SpanningClassReach'], 'status': 'kernel-only',
            'manuscript': [], 'note': render(CENSUS_NOTE, o)}


def check_surfaces(b, o):
    """The execution surfaces against D, for outcome o."""
    errs = []
    halted = sc5(o['a'], o['b']) == 'HALT'
    if halted:
        for k in ('roadmap', 'readme', 'census'):
            if b[k + '_c'] != b[k + '_d']:
                errs.append(k + ':written-on-halt')
        return errs
    # OIBridge.lean
    if b['bridge_d'].count(BRIDGE_ANCHOR) != 1 or b['bridge_c'] != b['bridge_d'].replace(
            BRIDGE_ANCHOR, BRIDGE_ANCHOR + BRIDGE_LINE):
        errs.append('bridge:import')
    # ROADMAP.md
    if b['roadmap_d'].count(ROADMAP_ANCHOR) != 1:
        errs.append('roadmap:anchor')
    else:
        cut = b['roadmap_d'].index(ROADMAP_ANCHOR) + ROADMAP_CUT
        errs += insertion(b['roadmap_d'], b['roadmap_c'], cut, render(ROADMAP_PARA, o),
                          'roadmap')
        s = norm(SENTENCES[sc5(o['a'], o['b'])])
        if norm(b['roadmap_c']).count(s) != 1:
            errs.append('roadmap:sentence')
    # README.md
    rl = b['readme_d'].split('\n')
    if rl.count(README_ANCHOR) != 1:
        errs.append('readme:anchor')
    else:
        cut = b['readme_d'].index('\n' + README_ANCHOR + '\n') + 1
        errs += insertion(b['readme_d'], b['readme_c'], cut, render(README_PARA, o), 'readme')
    # the census
    try:
        cd, cc = json.loads(b['census_d']), json.loads(b['census_c'])
        if set(cd) != set(cc) or any(cd[k] != cc[k] for k in cd if k != 'families') \
                or cc['families'][:-1] != cd['families'] \
                or cc['families'][-1] != census_entry(o) or not b['census_c'].endswith('\n'):
            errs.append('census:entry')
    except (ValueError, KeyError, TypeError, IndexError):
        errs.append('census:entry')
    # the frozen sentence appears only in the result note and the ROADMAP insertion
    s = norm(SENTENCES[sc5(o['a'], o['b'])])
    for k in ('readme_c', 'census_c', 'module'):
        if s in norm(b[k]):
            errs.append('sentence-outside-note-and-roadmap')
    return errs


def check_paths(changes, stage, halted):
    errs = []
    allowed = E_PATHS
    got = set(changes)
    if not got <= allowed:
        errs.append('paths:extra')
    if not stage and not halted and got != E_PATHS:
        errs.append('paths:missing')
    if not stage and halted and not {('A', PREREG), ('A', CONTROLS), ('A', RESULT)} <= got:
        errs.append('paths:missing')
    return errs


def check_bundle(b, stage=False):
    """(outcome, errors) for a bundle of texts; the pure core of `check`."""
    labels, theorems, budget, clos, errs = analyse_module(b['module'])
    o, e2 = outcome_of(labels)
    errs = errs + e2
    halted = sc5(o['a'], o['b']) == 'HALT'
    if not stage:
        ctx = {'outcome': o, 'vector': vector(o), 'theorems': list(theorems),
               'budget': budget, 'closure': clos, 'coords': b['coords'],
               'b_present': b['b_present'], 'quote_source': b['quote_source']}
        errs += check_note(b['note'], ctx)
        errs += check_surfaces(b, o)
    errs += check_paths(b['changes'], stage, halted)
    return o, sorted(set(errs))


# ---------------------------------------------------------------------------------------------
# git
# ---------------------------------------------------------------------------------------------
_PATH = os.environ.get('PATH', '/usr/bin:/bin')
ENV = {'PATH': _PATH, 'LC_ALL': 'C', 'LANG': 'C', 'HOME': '/nonexistent-controls',
       'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': '/dev/null', 'GIT_TERMINAL_PROMPT': '0',
       'GIT_OPTIONAL_LOCKS': '0'}
OIDRE = re.compile(r'[0-9a-f]{40}')


def git(args, ok=(0,)):
    try:
        r = subprocess.run(['git'] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           env=ENV, cwd=os.getcwd())
    except OSError:
        raise Fail('git:unavailable')
    if r.returncode not in ok:
        raise Fail('git:' + args[0])
    return r.returncode, r.stdout


def oid(s):
    if not isinstance(s, str) or not OIDRE.fullmatch(s):
        raise Fail('input:object-id')
    return s


def need_commit(c):
    git(['cat-file', '-e', oid(c) + '^{commit}'])
    return c


def blob_at(c, path):
    _rc, out = git(['ls-tree', '-z', '--full-tree', c, '--', path])
    for rec in out.split(b'\0'):
        if not rec:
            continue
        meta, p = rec.split(b'\t', 1)
        if p.decode('utf-8') == path:
            mode, typ, obj = meta.decode().split(' ')
            return obj if typ == 'blob' else None
    return None


def blob_bytes(b):
    return git(['cat-file', 'blob', oid(b)])[1]


def text_at(c, path):
    b = blob_at(c, path)
    return None if b is None else blob_bytes(b).decode('utf-8')


def files_under(c, prefix):
    _rc, out = git(['ls-tree', '-r', '-z', '--full-tree', c, '--', prefix])
    res = []
    for rec in out.split(b'\0'):
        if rec:
            res.append(rec.split(b'\t', 1)[1].decode('utf-8'))
    return res


def changes(a, b):
    _rc, out = git(['diff-tree', '-r', '--no-renames', '-z', '--raw', a, b])
    parts = out.split(b'\0')
    res, i = [], 0
    while i < len(parts) - 1:
        meta = parts[i].decode()
        if not meta:
            i += 1
            continue
        st = meta.split(' ')[-1]
        res.append((st, parts[i + 1].decode('utf-8')))
        i += 2
    return res


def parents(c):
    return git(['rev-list', '--parents', '-n', '1', c])[1].decode().split()[1:]


def is_ancestor(a, b):
    rc, _ = git(['merge-base', '--is-ancestor', a, b], ok=(0, 1))
    return rc == 0


def legacy_lines():
    return blob_bytes(LEGACY_BLOB).decode('utf-8').split('\n')


def unquote(ln):
    return ln[2:] if ln.startswith('> ') else ln[1:] if ln.startswith('>') else ln


def fragments(leg, rng):
    """The legacy quotation at lines rng, blockquote markers stripped, split at the ellipsis."""
    a, b = rng
    joined = ' '.join(unquote(ln) for ln in leg[a - 1:b])
    return [norm(x) for x in joined.split('[…]') if norm(x)]


def locate(text, frag):
    """(first line, last line) of the normalized fragment in text, or None."""
    lines = text.split('\n')
    flat, owner = [], []
    for ln_no, ln in enumerate(lines, 1):
        for w in ln.split():
            if flat:
                flat.append(' ')
                owner.append(ln_no)
            for ch in w:
                flat.append(ch)
                owner.append(ln_no)
    s = ''.join(flat)
    i = s.find(frag)
    if i < 0 or s.find(frag, i + 1) >= 0:
        return None
    return owner[i], owner[i + len(frag) - 1]


def passage_coords(c):
    leg = legacy_lines()
    coords, errs = {}, []
    for pid, path, ranges, _d, _pin in PASSAGES:
        t = text_at(c, path)
        got = []
        for fr in fragments(leg, ranges):
            loc = None if t is None else locate(t, fr)
            if loc is None:
                errs.append('sc0:passage-absent:' + pid)
                loc = (0, 0)
            got.append(loc)
        coords[pid] = got
    return coords, errs


# ---------------------------------------------------------------------------------------------
# modes
# ---------------------------------------------------------------------------------------------
def mode_start_state(d):
    need_commit(d)
    errs = []
    if d != D:
        errs.append('start:d')
    for path, _b78, _e21, bd in READ_ONLY + WRITTEN:
        if blob_at(d, path) != bd:
            errs.append('start:blob:' + path)
    for path, bd, _vals in SEALS_READ:
        if blob_at(d, path) != bd:
            errs.append('start:blob:' + path)
    if blob_at(d, LEGACY_MANIFEST[0]) != LEGACY_MANIFEST[1]:
        errs.append('start:blob:' + LEGACY_MANIFEST[0])
    if blob_at(d, LEGACY_PREREG) != LEGACY_BLOB or files_under(d, LEGACY_DIR) != [LEGACY_PREREG]:
        errs.append('start:legacy-freeze')
    if not is_ancestor(LEGACY_MERGE, d) or blob_at(LEGACY_MERGE, LEGACY_PREREG) != LEGACY_BLOB:
        errs.append('start:legacy-merge')
    for path, b78, e21, _bd in READ_ONLY + WRITTEN:
        if blob_at(LEGACY_DRAFT, path) != b78 or blob_at(LEGACY_MERGE, path) != e21:
            errs.append('start:legacy-pin:' + path)
    for p in FREE_PATHS:
        if files_under(d, p.rstrip('/')) or blob_at(d, p) is not None:
            errs.append('start:path-used:' + p)
    for p in B_RESULT_PATHS:
        if blob_at(d, p) is not None:
            errs.append('start:24.1b-result-present:' + p)
    for nm in FREE_NAMES:
        rc, out = git(['grep', '-l', '-I', '-F', '-e', nm, d, '--', '.',
                       ':(exclude)' + LEGACY_PREREG], ok=(0, 1))
        if rc == 0:
            errs.append('start:name-used:' + nm)
    leg = legacy_lines()
    for k, (a, b) in SENTENCE_RANGES.items():
        txt = norm(' '.join(unquote(ln) for ln in leg[a - 1:b]))
        if txt != norm(SENTENCES[k]):
            errs.append('start:sentence:' + k)
    merged = items(strip_comments(text_at(d, 'verification/lean-mathlib/OIBridge/'
                                          'SemigroupTransfer.lean')))
    for key, nt in NOTATIONS.items():
        if merged.count(nt) != 1:
            errs.append('start:notation:' + key)
    coords, e2 = passage_coords(d)
    errs += e2
    for pid, _path, _r, at_d, at_pin in PASSAGES:
        if coords[pid] != at_d:
            errs.append('start:coordinate:' + pid)
    pin_errs = []
    for pid, path, ranges, _at_d, at_pin in PASSAGES:
        pinned = dict((p, b78) for p, b78, _e, _d in READ_ONLY + WRITTEN)[path]
        t = blob_bytes(pinned).decode('utf-8')
        got = [locate(t, fr) for fr in fragments(leg, ranges)]
        if got != at_pin:
            pin_errs.append('start:pin-coordinate:' + pid)
    errs += pin_errs
    print('| path | blob at `b78eac87` | blob at `e21a42c6` | blob at `D` |')
    for path, b78, e21, bd in READ_ONLY + WRITTEN:
        print('| `%s` | `%s` | `%s` | `%s` |' % (path, b78[:8], e21[:8], bd[:8]))
    for row in sc0_rows(coords):
        print(row)
    return errs


def check_prereg_text(text, leg):
    """The preregistration carries this file's constants and the verbatim adoption."""
    errs = []
    lines = text.split('\n')

    def block(info):
        res = []
        i = 0
        while i < len(lines):
            if lines[i] == '```' + info:
                j = i + 1
                while j < len(lines) and lines[j] != '```':
                    j += 1
                res.append(lines[i + 1:j])
                i = j
            i += 1
        return res
    if block('v3-round') != [BLOCK_ROUND]:
        errs.append('prereg:v3-round')
    if block('v3-governed-paths') != [BLOCK_GOVERNED]:
        errs.append('prereg:v3-governed-paths')
    flat = norm(text)
    must = [disp for (_t, _s, disp, _r, _m) in LABELS.values()] + HEADER_REQUIRED + [
        HEADER_IMPORT, SLOT1, ROADMAP_PARA, README_PARA, CENSUS_NAME, CENSUS_NOTE,
        NOTE_NO_MANUSCRIPT, NOTE_B_ABSENT, NOTE_B_PRESENT, NOTE_TYPE_P, HALT_STATEMENT,
        NOTE_SLOT1[True], NOTE_SLOT1[False], NOTE_SLOT2[True], NOTE_SLOT2[False],
        NOTE_PAIR_A] + list(NOTATIONS.values()) + OBSTRUCTION_TERMS
    for s in must:
        if norm(s) not in flat:
            errs.append('prereg:constant:' + s[:40])
    for h in HEADINGS:
        if '`' + h + '`' not in text:
            errs.append('prereg:heading:' + h)
    for p in FORBIDDEN_PHRASES + FORBIDDEN_STARTS:
        if '"' + p + '"' not in flat.lower():
            errs.append('prereg:phrase:' + p)
    for path, b78, e21, bd in READ_ONLY + WRITTEN:
        row = '| `%s` | `%s` | `%s` | `%s` |' % (path, b78[:8], e21[:8], bd[:8])
        if row not in lines:
            errs.append('prereg:start-row:' + path)
    for pid, path, _r, at_d, at_pin in PASSAGES:
        row = '| §%s | `%s` | %s | %s |' % (pid, path, '; '.join('%d–%d' % x for x in at_d),
                                           '; '.join('%d–%d' % x for x in at_pin))
        if row not in lines:
            errs.append('prereg:passage-row:' + pid)
    # the verbatim adoption
    seen = []
    for i, ln in enumerate(lines):
        m = QUOTE_MARK.match(ln)
        if not m:
            continue
        a, b = int(m.group(1)), int(m.group(2))
        q, _j = (blockquote_after(lines, i + 2) if i + 1 < len(lines) and lines[i + 1] == ''
                 else (None, 0))
        if q is None or leg[a - 1:b] != q:
            errs.append('prereg:quote:%d-%d' % (a, b))
        seen.append((a, b))
    if sorted(seen) != sorted(ADOPTED_RANGES):
        errs.append('prereg:adoption-ranges')
    if len(re.findall(r'^Frozen blob of `controls\.py`: `[0-9a-f]{40}`\.$', text, re.M)) != 1:
        errs.append('prereg:controls-blob')
    return errs


def frozen_controls_blob(text):
    m = re.search(r'^Frozen blob of `controls\.py`: `([0-9a-f]{40})`\.$', text, re.M)
    return m.group(1) if m else None


def mode_freeze(f):
    need_commit(f)
    errs = []
    if not is_ancestor(D, f):
        errs.append('freeze:d-not-ancestor')
    for st, p in changes(D, f):
        if not (p == PREREG or p.startswith(RDIR + 'amendments/')):
            errs.append('freeze:non-control-plane-path')
    t = text_at(f, PREREG)
    if t is None:
        return errs + ['freeze:no-preregistration']
    errs += check_prereg_text(t, legacy_lines())
    return errs


def build_bundle(c, f):
    leg_ok = blob_at(c, LEGACY_PREREG) == LEGACY_BLOB and \
        files_under(c, LEGACY_DIR) == [LEGACY_PREREG]
    allowed = {(p, bd) for p, _x, _y, bd in READ_ONLY + WRITTEN} | {(LEGACY_PREREG,
                                                                      LEGACY_BLOB)}

    def quote_source(path, blob):
        if (path, blob) not in allowed:
            return None
        return blob_bytes(blob).decode('utf-8').split('\n')
    coords, cerr = passage_coords(f)
    b = {
        'module': text_at(c, MODULE) or '',
        'note': text_at(c, RESULT) or '',
        'roadmap_d': text_at(D, ROADMAP), 'roadmap_c': text_at(c, ROADMAP),
        'readme_d': text_at(D, README), 'readme_c': text_at(c, README),
        'census_d': text_at(D, CENSUS), 'census_c': text_at(c, CENSUS),
        'bridge_d': text_at(D, BRIDGE), 'bridge_c': text_at(c, BRIDGE),
        'changes': changes(D, c), 'coords': coords,
        'b_present': any(blob_at(f, p) is not None for p in B_RESULT_PATHS),
        'quote_source': quote_source,
    }
    pre = []
    if not leg_ok:
        pre.append('legacy:freeze-changed')
    for path, _b78, _e21, bd in READ_ONLY:
        if blob_at(c, path) != bd:
            pre.append('read-only:written:' + path)
    for path, bd, vals in SEALS_READ:
        if blob_at(c, path) != bd or json.loads(blob_bytes(bd)) != vals:
            pre.append('seals:legacy-seal-state')
    if blob_at(c, LEGACY_MANIFEST[0]) != LEGACY_MANIFEST[1]:
        pre.append('legacy:manifest-changed')
    if blob_at(c, 'verification/lean/edge_rigidity_probe.py') != WRITTEN[2][3]:
        pre.append('guard:changed')
    return b, pre + cerr


def mode_check(c, f, stage):
    need_commit(c)
    need_commit(f)
    errs = []
    if not is_ancestor(f, c):
        errs.append('check:f-not-ancestor')
    pf = text_at(f, PREREG)
    if pf is None or text_at(c, PREREG) != pf:
        errs.append('check:preregistration-changed')
    want = frozen_controls_blob(pf or '')
    if want is None or blob_at(c, CONTROLS) != want:
        errs.append('check:controls-blob')
    b, pre = build_bundle(c, f)
    o, e2 = check_bundle(b, stage)
    print(vector(o))
    return errs + pre + e2


def seal_record(f, e, lam, o_vec):
    rec = {
        'schema': 'sub-241c-span-seal', 'version': 1, 'round': ROUND,
        'legacy': {'freeze': LEGACY_PREREG, 'blob': LEGACY_BLOB,
                   'control_plane_merge': LEGACY_MERGE, 'reserved_guard_tag': 'R7-SCD'},
        'roles': [
            {'legacy': '_SCD_BASE', 'receipt_field': 'f', 'commit': f},
            {'legacy': '_SCD_SEALED_HEAD', 'receipt_field': 'e', 'commit': e},
            {'legacy': '_SCD_MERGE', 'receipt_field': 'landing.object', 'commit': lam},
        ],
        'pins': {'preregistration': blob_at(f, PREREG), 'controls': blob_at(e, CONTROLS),
                 'module': blob_at(e, MODULE), 'result': blob_at(e, RESULT)},
        'outcome': o_vec,
    }
    return (json.dumps(rec, indent=1, ensure_ascii=False) + '\n').encode('utf-8')


def outcome_at(e):
    labels, _t, _b, _c, errs = analyse_module(text_at(e, MODULE) or '')
    o, e2 = outcome_of(labels)
    if errs or e2:
        raise Fail('seal:module-not-clean')
    return vector(o)


def mode_seal(f, e, lam):
    for x in (f, e, lam):
        need_commit(x)
    sys.stdout.buffer.write(seal_record(f, e, lam, outcome_at(e)))
    return []


def mode_receipt(q):
    need_commit(q)
    errs = []
    t = text_at(q, RECEIPT)
    try:
        r = json.loads(t)
    except (TypeError, ValueError):
        return ['receipt:unreadable']
    if r.get('round') != ROUND or r.get('kind') != 'sealing' or r.get('status') != 'complete':
        errs.append('receipt:identity')
    recs = (r.get('seal') or {}).get('records') or []
    if len(recs) != 1 or recs[0].get('path') != SEAL:
        return errs + ['receipt:seal']
    f, e, lam = r['f'], r['e'], r['landing']['object']
    want = seal_record(f, e, lam, outcome_at(e))
    got = blob_at(q, SEAL)
    if got is None or blob_bytes(got) != want or got != recs[0]['blob']:
        errs.append('receipt:seal-record')
    if parents(q) != [lam]:
        errs.append('receipt:q-parent')
    for p in files_under(q, RDIR.rstrip('/')):
        if blob_at(q, p) != blob_at(e, p):
            errs.append('receipt:record-directory')
    return errs


AXLINE = re.compile(r"'OIBridge\.SpanningClassReach\.([A-Za-z0-9_']+)' depends on axioms: "
                    r"\[([^\]]*)\]")
NOAX = re.compile(r"'OIBridge\.SpanningClassReach\.([A-Za-z0-9_']+)' does not depend on any "
                  r"axioms")


def mode_axioms(c, log):
    need_commit(c)
    with open(log, encoding='utf-8', errors='replace') as fh:
        t = fh.read()
    got = {m.group(1): {a.strip() for a in m.group(2).split(',') if a.strip()}
           for m in AXLINE.finditer(t)}
    for m in NOAX.finditer(t):
        got[m.group(1)] = set()
    note = text_at(c, RESULT) or ''
    rows = {n: {a.strip() for a in ax.split(',') if a.strip()} for n, ax in
            re.findall(r"^\| `([A-Za-z0-9_']+)` \| `\[([^\]]*)\]` \|$", note, re.M)}
    _l, theorems, _b, _c, _e = analyse_module(text_at(c, MODULE) or '')
    errs = []
    if set(got) != set(theorems) or rows != got:
        errs.append('axioms:table-differs-from-log')
    if any(not v <= PERMITTED_AXIOMS for v in got.values()) or 'sorryAx' in t:
        errs.append('axioms:outside-three')
    return errs


# ---------------------------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------------------------
PROOF = '  by\n  exact sc_helper\n'
SYN_DEPS = {'SC4d_nonspanning_witness': '  by\n  exact SC4a_spanning_imp_hct\n'}


def syn_module(o, via_a=False, slot1=False, slot2=False, prints_after=False):
    labels = []
    for name, (t, sign, disp, rx, mn) in LABELS.items():
        want = o[t]
        if t == 'd':
            take = want == 'pos'
        else:
            take = want == sign
        if not take:
            continue
        stmt = disp.replace('Fin a × Fin b', 'Fin 2 × Fin 2')
        proof = PROOF
        if name == 'SC4d_nonspanning_witness' and via_a and o['a'] == 'pos':
            proof = SYN_DEPS[name]
        if name == 'SC4d_spanning_witness' and slot2:
            proof = '  by\n  exact ⟨witnessU, sc_helper⟩\n'
        labels.append((name, stmt[:-3] + ' :=\n' + proof))
    parts = [HEADER_IMPORT, 'import Mathlib.LinearAlgebra.Matrix.Trace', '',
             '/-! # Lemma 24.1C -- the spanning-class decision (synthetic). -/', '',
             'namespace OIBridge', 'namespace SpanningClassReach', '',
             'set_option autoImplicit false', 'set_option linter.unusedSectionVars false', '',
             'open Matrix SemigroupTransfer WordTraceSufficiency', 'open scoped Kronecker', '',
             HEADER_REQUIRED[4], '', NOTATIONS['φC'], '']
    if slot1:
        parts += [SLOT1, '  Submodule.span ℂ ∅', '']
    if slot2:
        parts += ['def witnessU : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=', '  1', '']
    parts += ['theorem sc_helper : True :=', '  trivial', '']
    names = ['sc_helper']
    for name, txt in labels:
        parts += [txt]
        names.append(name)
    prints = ['#print axioms OIBridge.SpanningClassReach.' + n for n in names]
    if prints_after:
        parts += ['end SpanningClassReach', 'end OIBridge', ''] + prints + ['']
    else:
        parts += prints + ['', 'end SpanningClassReach', 'end OIBridge', '']
    return '\n'.join(parts), names


SYN_QUOTE = ['first line', '', 'third line']


def syn_note(o, names, via_a=False, slot1=False, slot2=False, b_present=False):
    s5 = sc5(o['a'], o['b'])
    out = ['# SUB-241C-SPAN — result', '', '## Outcome', '', vector(o), '']
    if s5 in SENTENCES:
        out += ['The frozen sentence for that outcome:', '']
        out += ['> ' + ln for ln in wrap(SENTENCES[s5])]
        out += ['']
    else:
        out += [HALT_STATEMENT, '']
    out += ['## SC0', '', '| passage | path | lines at `F` |', '| --- | --- | --- |']
    out += sc0_rows(SYN_COORDS) + ['']
    out += ['## SC1', '', 'Reading R, on carrier C, under model M, is refuted, per:', '',
            '`verification/README.md:1–3`, blob `' + 'd' * 40 + '`:', '']
    out += ['> ' + ln if ln else '>' for ln in SYN_QUOTE] + ['']
    out += ['## SC2', '', 'Quoted.', '', '## SC3', '', 'Quoted.', '']
    out += ['## SC4(a)', '', 'Kernel.', '', '## SC4(b)', '', 'Kernel or UNDECIDED.', '']
    out += ['## SC4(b) bounded search', '', 'Search terms: `bicommutant`, `centralizer`.',
            'Trees searched: Mathlib at `v4.33.0`; the repository at `F`.',
            'Result: as found.', '']
    out += ['## SC4(c)', '', 'Direct computation.', '', '## SC4(d)', '']
    if via_a and o['d'] == 'pos' and o['a'] == 'pos':
        out += ['The non-spanning witness of `SC4(d)` ' + NOTE_PAIR_A + ': both steps named.']
    out += ['', '## SC5', '', 'Assembled by the frozen rule.']
    if s5 == 'SC5-UNDECIDED':
        out += ['', 'Obstruction: the double commutant statement; ' + '; '.join(
            OBSTRUCTION_TERMS) + ' nothing at the stated places.']
    out += ['', '## SC6', '', 'A census only.', '', '## Axiom table', '',
            '| result | axioms |', '| --- | --- |']
    out += ['| `%s` | `[propext, Classical.choice, Quot.sound]` |' % n for n in names]
    out += ['', '## Definition budget', '', NOTE_SLOT1[slot1], NOTE_SLOT2[slot2], '',
            '## Discrepancies', '', 'Recorded, not repaired.', '', '## Independence', '',
            NOTE_NO_MANUSCRIPT, NOTE_B_PRESENT if b_present else NOTE_B_ABSENT, NOTE_TYPE_P, '']
    return '\n'.join(out)


def wrap(s, width=96):
    out, cur = [], ''
    for w in s.split():
        if cur and len(cur) + 1 + len(w) > width:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w) if cur else w
    if cur:
        out.append(cur)
    return out


SYN_COORDS = {pid: at_d for pid, _p, _r, at_d, _pin in PASSAGES}
SYN_ROADMAP = ('| **P1** | Substratum Lemma 24.1 | **OPEN** |\n\n**Executed, 24.1A** — text '
               'and 24.1B is named and not begun. No\nmanuscript edit.\n\nThis is the row to watch, '
               'and more.\n')
SYN_README = 'Intro.\n\nA ledger paragraph.\n\n' + README_ANCHOR + '\n\nMore.\n'
SYN_CENSUS = json.dumps({'_comment': 'c', 'manuscripts': [], 'supersessions': {}, 'families': [
    {'name': 'x', 'modules': ['WordTraceSufficiency'], 'status': 'kernel-only',
     'manuscript': []}]}, indent=2, ensure_ascii=False) + '\n'
SYN_BRIDGE = 'import OIBridge.SemigroupTransfer\nimport OIBridge.WordTraceSufficiency\n' \
             'import OIBridge.RecurrenceHorizon\n'


def syn_surfaces(o):
    s5 = sc5(o['a'], o['b'])
    if s5 == 'HALT':
        return SYN_ROADMAP, SYN_README, SYN_CENSUS, SYN_BRIDGE
    cut = SYN_ROADMAP.index(ROADMAP_ANCHOR) + ROADMAP_CUT
    rm = SYN_ROADMAP[:cut] + '\n'.join(wrap(render(ROADMAP_PARA, o))) + '\n\n' + SYN_ROADMAP[cut:]
    cut2 = SYN_README.index(README_ANCHOR)
    rd = SYN_README[:cut2] + '\n'.join(wrap(render(README_PARA, o))) + '\n\n' + SYN_README[cut2:]
    cj = json.loads(SYN_CENSUS)
    cj['families'].append(census_entry(o))
    cs = json.dumps(cj, indent=2, ensure_ascii=False) + '\n'
    br = SYN_BRIDGE.replace(BRIDGE_ANCHOR, BRIDGE_ANCHOR + BRIDGE_LINE)
    return rm, rd, cs, br


def syn_bundle(o, via_a=False, slot1=False, slot2=False, b_present=False, prints_after=False):
    mod, names = syn_module(o, via_a, slot1, slot2, prints_after)
    note = syn_note(o, names, via_a, slot1, slot2, b_present)
    rm, rd, cs, br = syn_surfaces(o)
    halted = sc5(o['a'], o['b']) == 'HALT'
    ch = [('A', PREREG), ('A', CONTROLS), ('A', RESULT)]
    if not halted:
        ch = sorted(E_PATHS)
    return {'module': mod, 'note': note, 'roadmap_d': SYN_ROADMAP, 'roadmap_c': rm,
            'readme_d': SYN_README, 'readme_c': rd, 'census_d': SYN_CENSUS, 'census_c': cs,
            'bridge_d': SYN_BRIDGE, 'bridge_c': br, 'changes': ch, 'coords': SYN_COORDS,
            'b_present': b_present,
            'quote_source': lambda p, b: (SYN_QUOTE if (p, b) == ('verification/README.md',
                                                                  'd' * 40) else None)}


def all_rows():
    rows = []
    for a in ('pos', 'neg', 'und'):
        for b in ('pos', 'neg', 'und'):
            for c in ('pos', 'neg', 'und'):
                for d in ('pos', 'und'):
                    rows.append({'a': a, 'b': b, 'c': c, 'd': d})
    return rows


def _rep(key, old, new, count=1):
    def f(b):
        if old not in b[key]:
            raise Fail('self-test:mutation-anchor:' + old[:30])
        b[key] = b[key].replace(old, new, count)
        return b
    return f


def _set(key, val):
    def f(b):
        b[key] = val
        return b
    return f


def _census(fn):
    def f(b):
        cj = json.loads(b['census_c'])
        fn(cj['families'])
        b['census_c'] = json.dumps(cj, indent=2, ensure_ascii=False) + '\n'
        return b
    return f


def mutations():
    """(name, base outcome, base options, mutation, expected code)."""
    U = {'a': 'pos', 'b': 'und', 'c': 'pos', 'd': 'pos'}
    C = {'a': 'pos', 'b': 'pos', 'c': 'pos', 'd': 'pos'}
    S = {'a': 'pos', 'b': 'neg', 'c': 'neg', 'd': 'pos'}
    H = {'a': 'neg', 'b': 'und', 'c': 'und', 'd': 'und'}
    a_pos = LABELS['SC4a_spanning_imp_hct'][2][:-3]
    return [
        # the module: commands, tokens and the header
        ('sorry', U, {}, _rep('module', 'exact sc_helper', 'sorry'),
         'module:forbidden-token:sorry'),
        ('admit', U, {}, _rep('module', 'exact sc_helper', 'admit'),
         'module:forbidden-token:admit'),
        ('native_decide', U, {}, _rep('module', 'exact sc_helper', 'native_decide'),
         'module:forbidden-token:native_decide'),
        ('axiom', U, {}, _rep('module', 'theorem sc_helper', 'axiom ax : True\n\ntheorem sc_helper'),
         'module:forbidden-declaration:axiom'),
        ('instance', U, {}, _rep('module', 'theorem sc_helper',
                                 'instance foo : Inhabited ℕ := ⟨0⟩\n\ntheorem sc_helper'),
         'module:forbidden-declaration:instance'),
        ('second variable', U, {}, _rep('module', 'theorem sc_helper',
                                        'variable [Nonempty H]\n\ntheorem sc_helper'),
         'module:variable'),
        ('variable altered', U, {}, _rep('module', '[DecidableEq H]\n',
                                         '[DecidableEq H] [Nonempty H]\n'),
         'module:header:variable'),
        ('include', U, {}, _rep('module', 'theorem sc_helper', 'include V\n\ntheorem sc_helper'),
         'module:forbidden-token:include'),
        ('open in', U, {}, _rep('module', 'open scoped Kronecker', 'open Foo in'),
         'module:open-in'),
        ('frozen open dropped', U, {}, _rep('module',
                                            'open Matrix SemigroupTransfer WordTraceSufficiency\n',
                                            ''), 'module:header:open'),
        ('autoImplicit true', U, {}, _rep('module', 'set_option autoImplicit false',
                                          'set_option autoImplicit true'),
         'module:autoImplicit'),
        ('foreign import', U, {}, _rep('module', 'import Mathlib.LinearAlgebra.Matrix.Trace',
                                       'import OIBridge.TwoSidedGauge'), 'module:import'),
        ('frozen import dropped', U, {}, _rep('module', HEADER_IMPORT + '\n', ''),
         'module:import'),
        ('footer dropped', U, {}, _rep('module', 'end OIBridge', ''), 'module:footer'),
        ('declaration after the footer', U, {'prints_after': True}, _rep(
            'module', 'end OIBridge\n', 'end OIBridge\n\ntheorem late : True :=\n  trivial\n'),
         'module:footer'),
        ('notation hijack', U, {}, _rep('module', NOTATIONS['φC'],
                                        'local notation "BlockSpanning" => True'),
         'module:notation'),
        ('notation altered', U, {}, _rep('module', '(2 : Fin 3)))', '(1 : Fin 3)))'),
         'module:notation'),
        ('macro', U, {}, _rep('module', 'theorem sc_helper',
                              'macro "foo" : term => `(1)\n\ntheorem sc_helper'),
         'module:forbidden-command:macro'),
        ('print dropped', U, {}, _rep('module',
                                      '#print axioms OIBridge.SpanningClassReach.sc_helper\n', ''),
         'module:prints'),
        ('print for a def', U, {'slot1': True},
         _rep('module', '#print axioms OIBridge.SpanningClassReach.sc_helper',
              '#print axioms OIBridge.SpanningClassReach.sc_helper\n'
              '#print axioms OIBridge.SpanningClassReach.hiddenCommutant'), 'module:prints'),
        ('WT2 side door', U, {}, _rep('module', 'theorem sc_helper : True',
                                      'theorem sc_helper : ∀ U U\', HiddenConjugate U U\''),
         'module:forbidden-token:HiddenConjugate'),
        ('24.1B object', U, {}, _rep('module', 'exact sc_helper', 'exact H_obs'),
         'module:forbidden-token:H_obs'),
        ('enlargement consumed', U, {}, _rep('module', 'exact sc_helper', 'exact enlarge'),
         'module:forbidden-token:enlarge'),
        # the label statements
        ('SC4(a) weakened', U, {}, _rep('module', a_pos,
                                        a_pos.replace('(hU : BlockSpanning U)',
                                                      '(hU : BlockSpanning U) (h2 : 1 < 2)')),
         'module:label-statement:SC4a_spanning_imp_hct'),
        ('SC4(a) direction swapped', U, {}, _rep('module', ': HiddenCommutantTrivial U :=',
                                                 ': BlockSpanning U :=', 1),
         'module:label-statement:SC4a_spanning_imp_hct'),
        ('SC4(b) separating conjunct dropped', S, {}, _rep(
            'module', 'HiddenCommutantTrivial U ∧ ¬ BlockSpanning U :=', '¬ BlockSpanning U :='),
         'module:label-statement:SC4b_separating'),
        ('SC4(c) unpinned', U, {}, _rep('module', 'U = Equiv.Perm.permMatrix ℂ φC ∧ ', ''),
         'module:label-statement:SC4c_pairC_spanning'),
        ('SC4(d) carrier too small', U, {}, _rep('module',
                                                 'SC4d_spanning_witness : ∃ U : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2)',
                                                 'SC4d_spanning_witness : ∃ U : Matrix (Fin 1 × Fin 2) (Fin 1 × Fin 2)'),
         'module:label-statement:SC4d_spanning_witness'),
        ('stray label', U, {}, _rep('module', 'theorem sc_helper', 'theorem SC5_coincide : True :=\n'
                                    '  trivial\n\ntheorem sc_helper'), 'module:stray-label:SC5_coincide'),
        ('both labels of SC4(a)', U, {}, _rep(
            'module', 'theorem sc_helper',
            LABELS['SC4a_counterexample'][2].replace('Fin a × Fin b', 'Fin 2 × Fin 2') +
            '\n  by\n  exact sc_helper\n\ntheorem sc_helper'), 'module:both-labels:SC4a'),
        ('SC4(c) through SC4(b)', C, {}, _rep(
            'module', 'U = Equiv.Perm.permMatrix ℂ φC ∧ BlockSpanning U :=\n  by\n  exact sc_helper',
            'U = Equiv.Perm.permMatrix ℂ φC ∧ BlockSpanning U :=\n  by\n  exact SC4b_hct_imp_spanning'),
         'module:sc4c-through-sc4b'),
        # the budget
        ('third definition', U, {}, _rep('module', 'theorem sc_helper',
                                         'def extra : ℕ :=\n  0\n\ntheorem sc_helper'),
         'module:budget'),
        ('slot 1 retyped', U, {'slot1': True}, _rep('module', ': Submodule ℂ (Matrix H H ℂ) :=',
                                                    ': Set (Matrix H H ℂ) :='), 'module:budget'),
        ('slot 2 unused by SC4(d)', U, {'slot2': True}, _rep('module', 'exact ⟨witnessU, sc_helper⟩',
                                                             'exact sc_helper'), 'module:budget'),
        # the result note
        ('vector altered', U, {}, _rep('note', '`SC4(b)` UNDECIDED', '`SC4(b)` established'),
         'note:vector'),
        ('second vector', U, {}, _rep('note', '## SC6', 'Outcome: something.\n\n## SC6'),
         'note:vector'),
        ('sentence altered', U, {}, _rep('note', 'extrapolated', 'extended'), 'note:sentence'),
        ('other sentence added', U, {}, _rep('note', '## SC6', '> ' + SENTENCES['SC5-coincide']
                                             + '\n\n## SC6'), 'note:other-sentence'),
        ('sentence unquoted', U, {}, lambda b: dict(b, note=b['note'].replace('\n> ', '\n')),
         'note:sentence-not-quoted'),
        ('halt statement on a decided outcome', U, {}, _rep('note', '## SC6',
                                                            HALT_STATEMENT + '\n\n## SC6'),
         'note:halt-statement'),
        ('halt statement dropped', H, {}, _rep('note', HALT_STATEMENT, ''),
         'note:halt-statement'),
        ('heading dropped', U, {}, _rep('note', '## SC3\n', '## SC3 and more\n'), 'note:heading:SC3'),
        ('manuscript statement dropped', U, {}, _rep('note', NOTE_NO_MANUSCRIPT, ''),
         'note:no-manuscript'),
        ('24.1B presence misreported', U, {}, _rep('note', NOTE_B_ABSENT, NOTE_B_PRESENT),
         'note:24.1b-presence'),
        ('type P statement dropped', U, {}, _rep('note', NOTE_TYPE_P, ''), 'note:type-p'),
        ('slot misreported', U, {}, _rep('note', NOTE_SLOT1[False], NOTE_SLOT1[True]),
         'note:budget-line'),
        ('Pair A route unstated', U, {'via_a': True}, _rep('note', NOTE_PAIR_A, 'is computed'),
         'note:pair-a-route'),
        ('Pair A route claimed falsely', U, {}, _rep('note', '## SC5\n',
                                                     'It ' + NOTE_PAIR_A + '.\n\n## SC5\n'),
         'note:pair-a-route'),
        ('SC0 row drifted', U, {}, _rep('note', '| §2.1 | `verification/ROADMAP.md` | 64–64 |',
                                        '| §2.1 | `verification/ROADMAP.md` | 65–65 |'),
         'note:sc0-row'),
        ('bounded search unrecorded', U, {}, _rep('note', 'Trees searched:', 'Trees:'),
         'note:bounded-search'),
        ('obstruction unnamed', U, {}, _rep('note', 'Obstruction: ', 'It: '), 'note:obstruction'),
        ('obstruction in other terms', U, {}, _rep('note', OBSTRUCTION_TERMS[1], 'it commutes'),
         'note:obstruction-terms'),
        ('axiom row with sorryAx', U, {}, _rep('note', '| `sc_helper` | `[propext,',
                                               '| `sc_helper` | `[sorryAx, propext,'),
         'note:axiom-table'),
        ('axiom row dropped', U, {}, _rep('note', '| `sc_helper` | `[propext, Classical.choice, '
                                          'Quot.sound]` |\n', ''), 'note:axiom-table'),
        ('quotation altered', U, {}, _rep('note', '> third line', '> third lines'), 'note:quote'),
        ('quotation from an unpinned blob', U, {}, _rep('note', 'blob `' + 'd' * 40,
                                                        'blob `' + 'e' * 40), 'note:quote'),
        ('manuscript cited', U, {}, _rep('note', 'A census only.', 'See papers/Structure.md.'),
         'note:manuscript-path'),
        ('Lemma 24.1 is false', U, {}, _rep('note', 'A census only.', 'Lemma 24.1 is false.'),
         'note:forbidden:lemma 24.1 is false'),
        ('Lemma 24.1 is repaired', U, {}, _rep('note', 'A census only.',
                                               'Lemma 24.1 is repaired.'),
         'note:forbidden:lemma 24.1 is repaired'),
        ('completeness holds', U, {}, _rep('note', 'A census only.', 'So completeness holds.'),
         'note:forbidden:completeness holds'),
        ('recommendation', U, {}, _rep('note', 'A census only.',
                                       'The programme should next take 24.1B.'),
         'note:forbidden:the programme should next'),
        ('unqualified refutation', U, {}, _rep('note', 'Kernel.', 'The transfer is refuted.'),
         'note:forbidden:the transfer is refuted'),
        ('framework supplies', U, {}, _rep('note', 'Quoted.', 'The framework supplies it.'),
         'note:forbidden:the framework supplies'),
        ('selection principle', U, {}, _rep('note', 'Kernel.', 'The selection principle is X.'),
         'note:forbidden:the selection principle is'),
        # the surfaces
        ('ROADMAP label moved', U, {}, _rep('roadmap_c', '| **OPEN** |', '| **CLOSED** |'),
         'roadmap:insertion'),
        ('ROADMAP 24.1B status corrected', U, {}, _rep('roadmap_c', 'and 24.1B is named and not '
                                                       'begun', 'and 24.1B has begun'),
         'roadmap:insertion'),
        ('ROADMAP wrong sentence', U, {}, _rep('roadmap_c', 'extrapolated', 'extended'),
         'roadmap:insertion'),
        ('ROADMAP paragraph absent', U, {}, lambda b: dict(b, roadmap_c=b['roadmap_d']),
         'roadmap:insertion'),
        ('ROADMAP written on halt', H, {}, _rep('roadmap_c', 'This is the row', 'This is a row'),
         'roadmap:written-on-halt'),
        ('README paragraph altered', U, {}, _rep('readme_c', 'consulted.', 'used.'),
         'readme:insertion'),
        ('README sentence copied', U, {}, _rep('readme_c', 'More.', SENTENCES['SC5-UNDECIDED']),
         'sentence-outside-note-and-roadmap'),
        ('README untouched', U, {}, lambda b: dict(b, readme_c=b['readme_d']),
         'readme:insertion'),
        ('census promoted', U, {}, _census(lambda fam: fam[-1].update(status='current')),
         'census:entry'),
        ('census anchor added', U, {}, _census(lambda fam: fam[-1].update(
            manuscript=[{'file': 'papers/Structure.md', 'anchor': 'x'}])), 'census:entry'),
        ('census other family changed', U, {}, _rep('census_c', '"name": "x"', '"name": "y"'),
         'census:entry'),
        ('census entry absent', U, {}, lambda b: dict(b, census_c=b['census_d']),
         'census:entry'),
        ('census wrong vector', U, {}, _rep('census_c', '`SC4(c)` `φ̂_C` spanning',
                                            '`SC4(c)` UNDECIDED'), 'census:entry'),
        ('import absent', U, {}, lambda b: dict(b, bridge_c=b['bridge_d']), 'bridge:import'),
        ('import misplaced', U, {}, _set('bridge_c', SYN_BRIDGE + BRIDGE_LINE), 'bridge:import'),
        # the paths
        ('extra path', U, {}, lambda b: dict(b, changes=b['changes'] + [
            ('M', 'verification/lean/edge_rigidity_probe.py')]), 'paths:extra'),
        ('legacy freeze touched', U, {}, lambda b: dict(b, changes=b['changes'] + [
            ('M', LEGACY_PREREG)]), 'paths:extra'),
        ('result note missing', U, {}, lambda b: dict(b, changes=[x for x in b['changes']
                                                                  if x[1] != RESULT]),
         'paths:missing'),
        ('seal record in the execution', U, {}, lambda b: dict(b, changes=b['changes'] + [
            ('A', SEAL)]), 'paths:extra'),
    ]


def self_test():
    fails = []
    rows = all_rows()
    held = 0
    for o in rows:
        options = [{}, {'slot1': True}, {'b_present': True}, {'prints_after': True}]
        if o['d'] == 'pos':
            options.append({'slot2': True})
            if o['a'] == 'pos':
                options.append({'via_a': True})
        for opts in options:
            b = syn_bundle(o, **opts)
            got, errs = check_bundle(b)
            if got != o or errs:
                fails.append('row %s %s: %s %s' % (vector(o), opts, got, errs))
            else:
                held += 1
    muts = mutations()
    caught = 0
    for name, o, opts, mut, code in muts:
        b = syn_bundle(o, **opts)
        _o0, e0 = check_bundle(b)
        if e0:
            fails.append('mutation base %r not clean: %s' % (name, e0))
            continue
        try:
            b2 = mut(dict(b))
        except Fail as x:
            fails.append('mutation %r: %s' % (name, x))
            continue
        _o, errs = check_bundle(b2)
        if code not in errs:
            fails.append('mutation %r not caught as %s: %s' % (name, code, errs))
        else:
            caught += 1
    # the frozen sentences are the legacy blob's, and the decision rule is total
    cells = {sc5(a, b) for a in ('pos', 'neg', 'und') for b in ('pos', 'neg', 'und')}
    if cells != {'SC5-coincide', 'SC5-strict', 'SC5-UNDECIDED', 'HALT'}:
        fails.append('decision rule')
    for f_ in fails:
        print('SELF-TEST  FAIL  ' + f_)
    print('controls: %d synthetic executions over %d outcome rows hold as frozen, %d of %d '
          'mutation controls fail as required' % (held, len(rows), caught, len(muts)))
    print('controls: self-test %s' % ('OK' if not fails else 'FAILED'))
    return 0 if not fails else 1


USAGE = ('usage: controls.py --self-test | start-state <D> | freeze <F> | '
         'check <C> --f <F> [--stage] | seal-record <F> <E> <L> | receipt <Q> | '
         'axioms <C> <log>')


def main(argv):
    try:
        if argv == ['--self-test']:
            return self_test()
        if git(['rev-parse', '--show-prefix'])[1].strip():
            raise Fail('input:not-the-repository-root')
        if len(argv) == 2 and argv[0] == 'start-state':
            errs = mode_start_state(oid(argv[1]))
        elif len(argv) == 2 and argv[0] == 'freeze':
            errs = mode_freeze(oid(argv[1]))
        elif len(argv) in (4, 5) and argv[0] == 'check' and argv[2] == '--f' and \
                (len(argv) == 4 or argv[4] == '--stage'):
            errs = mode_check(oid(argv[1]), oid(argv[3]), len(argv) == 5)
        elif len(argv) == 4 and argv[0] == 'seal-record':
            errs = mode_seal(oid(argv[1]), oid(argv[2]), oid(argv[3]))
            return 0 if not errs else 1
        elif len(argv) == 2 and argv[0] == 'receipt':
            errs = mode_receipt(oid(argv[1]))
        elif len(argv) == 3 and argv[0] == 'axioms':
            errs = mode_axioms(oid(argv[1]), argv[2])
        else:
            print(USAGE)
            return 2
    except Fail as x:
        errs = [str(x)]
    except Exception as x:  # noqa: BLE001 -- fail closed on anything unexpected
        errs = ['unexpected:%s' % type(x).__name__]
    for e in errs:
        print('FAIL  ' + e)
    print('controls: %s %s' % (argv[0], 'OK' if not errs else 'FAILED'))
    return 0 if not errs else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
