"""The single source of act 42's frozen strings: the preregistration generator and the controls generator both import
this file, so the two cannot drift apart."""
import os, subprocess

S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/'
WT = S + 'wt-a42P/'
D = '0e87c4a129d91276c10f0438d03c1bcca3a0a3b8'
RDIR = 'verification/programmes/oi-qm/track-b/act-42-support-minimality/'
PROBE = 'verification/lean/dita_support_minimality_probe.py'
TOOLS = 'verification/lean/a42/'
WORKFLOW = '.github/workflows/verify.yml'
ROADMAP = 'verification/ROADMAP.md'
LABEL = 'A42-D1-MINIMUM-40'

TOOL_FILES = ['Rle13_39.txt', 'c6_control.py', 'classify42.py', 'ctrl16.py', 'cvsize.py', 'dfs01.py', 'dfs42.py',
              'dfsR.py', 'dfsR2.py', 'lemmas42.py', 'lib42.py', 'minsupp_exact.py', 'pairtypes.py', 'r2a_landed.py',
              'r2b2_census.py', 'r2b_independent.py', 'r3_run.py', 'r5_family.py', 'sat42.py', 'sat_hr.py', 'spanAll.py',
              'triples.py']
# where each tool came from: the rerun directory (the pre-L41 tools, copied unchanged) or the revalidation directory
RERUN, REVAL = 'research/a42-rerun/', 'research/a42-revalidation/'
SOURCE_DIR = {f: (REVAL if f in ('c6_control.py', 'minsupp_exact.py', 'r2a_landed.py', 'r2b2_census.py',
                                 'r2b_independent.py', 'r3_run.py', 'r5_family.py', 'triples.py') else RERUN)
              for f in TOOL_FILES}
RELOCATED = {  # the one edited line of each relocated tool, old and new
    'lib42.py': ('REPO = os.path.dirname(os.path.dirname(HERE))',
                 'REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))'),
    'r2a_landed.py': ('REPO = os.path.dirname(os.path.dirname(HERE))',
                      'REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))'),
    'r2b2_census.py': ('HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(HERE))',
                       'HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))'),
    'r2b_independent.py': ('HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(HERE))',
                           'HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))'),
}
RESEARCH_HEAD = '1f19a3477a6e2a4c4f5f6b3a8a5cb5d9e8e0a1c2'  # replaced by the real id below


def git(*a, cwd=None):
    return subprocess.run(('git',) + a, capture_output=True, text=True, cwd=cwd, check=True).stdout.strip()


RESEARCH_HEAD = git('rev-parse', '1f19a347', cwd=S + 'wt-a42r')


def blob_of(path):
    return git('hash-object', path)


TOOL_BLOBS = {f: blob_of(WT + TOOLS + f) for f in TOOL_FILES}
SOURCE_BLOBS = {f: git('rev-parse', '%s:%s%s' % (RESEARCH_HEAD, SOURCE_DIR[f], f), cwd=S + 'wt-a42r') for f in TOOL_FILES}
PROBE_BLOB = blob_of(WT + PROBE)

# ---- the workflow edit: five replacements on D's file ----------------------------------------------------------------
JOBS = open(S + 'a42/workflow_jobs.txt').read()
WORKFLOW_EDITS = [
    ('  probes_foundations:\n    name: Numerical probes / foundations\n',
     JOBS + '  probes_foundations:\n    name: Numerical probes / foundations\n'),
    ('probes_a45, probes_foundations]',
     'probes_a45, probes_a42_witness, probes_a42_census01, probes_a42_exclusion, probes_foundations]'),
    ('          A45_RESULT: ${{ needs.probes_a45.result }}\n',
     '          A45_RESULT: ${{ needs.probes_a45.result }}\n'
     '          A42W_RESULT: ${{ needs.probes_a42_witness.result }}\n'
     '          A42C_RESULT: ${{ needs.probes_a42_census01.result }}\n'
     '          A42X_RESULT: ${{ needs.probes_a42_exclusion.result }}\n'),
    ('          echo "a45=${A45_RESULT}"\n',
     '          echo "a45=${A45_RESULT}"\n'
     '          echo "a42_witness=${A42W_RESULT}"\n'
     '          echo "a42_census01=${A42C_RESULT}"\n'
     '          echo "a42_exclusion=${A42X_RESULT} (event ${GITHUB_EVENT_NAME})"\n'),
    ('          test "${A45_RESULT}" = success\n',
     '          test "${A45_RESULT}" = success\n'
     '          test "${A42W_RESULT}" = success\n'
     '          test "${A42C_RESULT}" = success\n'
     '          if [ "${GITHUB_EVENT_NAME}" = workflow_dispatch ]; then\n'
     '            test "${A42X_RESULT}" = success\n'
     '          else\n'
     '            test "${A42X_RESULT}" = skipped\n'
     '          fi\n'),
]

# ---- the ROADMAP propagation: replacements on D's file, each with its exact count -----------------------------------
P0_SENTENCE = ("Among straight lines through the certified rational stratum point, with class support the least number of "
               "nonzero exponent entries over the orbit under the gauge, the point's stabilizer and sign, and among the "
               "classes that have a least-support representative with entries in `{−1, 0, 1}`, the least class support of "
               "a line lying identically in no Diţă structure of the point is exactly 40, attained by act 42's `E40`, and "
               "act 38's witness has class support 44 (act 42: exact computation over a case split stated in its record, "
               "with the no-zero-line case and the zero-row case with at least fourteen nonzero rows closed by SAT "
               "verdicts carried without proof logs); classes outside that domain and the class supports 41 to 43 and 45 "
               "to 47 are not determined, and no line or support value is adopted as a physical symmetry, principle or law. ")
P0_ANCHOR = ("`P0`'s cross-time parts are untouched, no relation is adopted as the physical one, and nothing here names, "
             "endorses or excludes a selection principle. ")
SECTION_OLD = """**Future classification, not an A38 result, and independent of the census and of the three-parameter
family.** Act 38's witness `E = A + B + C` has 48 nonzero entries. Whether a straight line through the
certified stratum point that lies identically in none of the Diţă structures of the point can have smaller
support, in any gauge and after the stabilizer action, is open. The question is a minimisation over
stabilizer orbits of straight exponent matrices; an answer would say whether act 38 found a smallest
escape direction or one among escapes of several sizes. A minimality statement requires either an
exhaustive search below a stated support bound, which does not presuppose the full census, or a
structural lower bound.
"""
SECTION_NEW = """**Future classification beyond act 42's domain, independent of the census and of the three-parameter
family.** The class support of a straight line through the certified stratum point is the least number of
nonzero entries of its exponent matrix over the orbit under the gauge, the stabilizer of the point and
sign. Among the classes that have a least-support representative with entries in `{−1, 0, 1}`, the least
class support of a line lying identically in none of the Diţă structures of the point is exactly 40,
attained by act 42's exponent matrix `E40`, whose entries lie in `{−1, 0, 1}`; act 38's witness
`E = A + B + C`, with 48 nonzero entries, has class support 44. Open: whether a class all of whose
least-support representatives have an entry of absolute value at least 2 has class support below 40, and
which of the class supports 41 to 43 and 45 to 47 occur. A minimality statement beyond that domain
requires either an exhaustive search below a stated support bound, which does not presuppose the full
census, or a structural lower bound.
"""
ROADMAP_EDITS = [
    ("Which points of the family admit a Diţă structure, the census of exponent matrices with entries in `{0, 1}` and "
     "the minimality of support 48 stay open,",
     "Which points of the family admit a Diţă structure and the census of exponent matrices with entries in `{0, 1}` "
     "stay open,", 1),
    ("The census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open,",
     "The census of exponent matrices with entries in `{0, 1}` stays open,", 2),
    (P0_ANCHOR + '|', P0_ANCHOR + P0_SENTENCE + '|', 1),
    (SECTION_OLD, SECTION_NEW, 1),
]

CLAUSE = ("Act 42 settles, by exact computation, a case split stated in its preregistration and SAT verdicts carried "
          "without proof logs, the least class support of a straight line through the certified rational stratum point "
          "that lies identically in no Diţă structure of the point, within the domain D1 of classes having a "
          "least-support representative with entries in {−1, 0, 1}; the value is 40. It says nothing about classes "
          "outside D1, determines none of the class supports 41 to 43 and 45 to 47, re-derives none of the "
          "general-integer exclusions of the pre-freeze analysis, revises no earlier verdict, adopts no line, family or "
          "support value as a physical symmetry, principle or law, and leaves `P0` open; nothing here names, endorses "
          "or excludes a selection principle.")
SENTENCE = ("Within D1, the least class support of a non-Diţă straight line is exactly 40. Here a straight line is an "
            "integer exponent matrix `E` with `SIG ∘ u^E` complex Hadamard for every unit `u`; its class is its orbit "
            "under the gauge, the stabilizer of `SIG` and sign; its class support is the least number of nonzero "
            "entries over the class; D1 is the set of classes having a least-support representative with entries in "
            "{−1, 0, 1}; and non-Diţă means lying identically in no Diţă structure of `SIG` under act 41's semantics. "
            "The value is attained by `E40 = −P + Q − T`, straight by two exact methods, of class support exactly 40 "
            "by exact enumeration, and non-Diţă by two independent paths. No class of D1 has class support at most 39 "
            "and is non-Diţă: in the zero-row case with at most thirteen nonzero rows by an exact exhaustive search "
            "whose every leaf lies in one of eighteen subspaces, each equal by exact rank to the relaxed identity "
            "subspace of one of act 41's 976 realizing triples; in the zero-row case with at least fourteen nonzero "
            "rows and in the case with no zero line by SAT verdicts (UNSAT) carried without proof logs. Act 38's "
            "witness has class support 44. The lemmas of the case split are stated and argued in the preregistration "
            "and are not kernel-checked, the general-integer exclusions of the pre-freeze analysis are not "
            "re-derived, and nothing is claimed outside D1 or about the class supports 41 to 43 and 45 to 47.")
CLAUSE_MENTION = '**THE CLAUSE, carried at this mention — the result.**'

PARTS = ['witness', 'wlog', 'd01span', 'paths', 'r5', 'n18:0', 'n18:1', 'n18:2', 'dfs:0', 'dfs:1', 'dfs:2', 'dfs:3',
         'dfs:4', 'dfs:5', 'sathr', 'cubes:0', 'cubes:1', 'cubes:2']
PART_CHECKS = None  # filled from the measured local runs by the generator
