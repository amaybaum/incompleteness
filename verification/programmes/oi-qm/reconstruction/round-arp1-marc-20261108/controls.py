#!/usr/bin/env python3
"""controls.py -- ARP-1-MARC's governance and decision script, frozen with the preregistration beside it.

Imports nothing from the repository. Reads commits with read-only git commands, runs precondition 6's command (the
frozen argv, two commit ids substituted) as control T, and never launches marc_check.py. Generated files go to stdout;
the executor commits them. Its only write-mode open is in the self-test, inside a tempfile directory.

  controls.py check <commit> --freeze F [--stage S1|E|W]      controls T, G, R, B, W, DS, X, V, P at <commit>
  controls.py decide <file> [--exit-status N]                  the frozen decision rule on measurements.json
  controls.py note <file> --runs <s1-run> [--freeze F]         result.md, generated (stdout)
  controls.py replay <file>                                    byte equality with the committed measurements
  controls.py derive-run --run-api RUN --jobs-api JOBS [--jobs-api JOBS2 ...]
                         [--artifacts-api A --artifact-zip Z] [--void-run S1|E]
                                                               the derived run record (or a void-run record)
  controls.py order --freeze F --s1 S1 --designation DES --approvals APP --runs RUNS --dev-runs DEV --dev-pr N
                                                               evidence/order.json (stdout); exit 0 iff the
                                                               ordering holds
  controls.py verdict E --freeze F --run-api RUN --jobs-api JOBS --approvals APP --branch-runs RUNS
                                                               VERDICT  <token> or VERDICT  VOID
  controls.py plane <candidate F> --dev-runs DEV               the P subset F's own tree can carry, and the
                                                               classification of every dev-branch run
  controls.py --self-test                                      decision path, screen, jobs answers, attempts,
                                                               host-VOID, workflow and static checks, and a
                                                               synthetic round in temporary repositories
"""
import ast
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile

ROUND = 'ARP-1-MARC'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/'
RECEIPT = 'verification/receipts/ARP-1-MARC.json'
WORKFLOW = '.github/workflows/verify.yml'
REPO_FULL = 'amaybaum/incompleteness'
SNAPSHOT = '5ce4f98ec3a76aee6fdd17ed1bad7b278f1d9732'
R_ = 'verification/programmes/oi-qm/reconstruction/'
SOURCE_DIRS = (R_ + 'quarter-phase-native-20261107/', R_ + 'apparatus-1-20261107/', R_ + 'minacc-1-20261108/',
               R_ + 'mechanism-2-20261108/', 'tools/', '.github/', 'verification/infrastructure/')
INPUTS = {
    R_ + 'quarter-phase-native-20261107/DESIGN.md': 'fb21999b0d45750a465dda742589f0af11575326',
    R_ + 'apparatus-1-20261107/DESIGN.md': '51c24aeb7b42a915b8942462435fd9fe129861de',
    R_ + 'minacc-1-20261108/DESIGN.md': '737047be04dcf94f1ddcf7eae0abf736e2c0d52e',
    R_ + 'minacc-1-20261108/RESULT.md': '5adf76ebc8afa95cc51f45fb84c909b13876516c',
    R_ + 'minacc-1-20261108/amendments/A1-prereg-review.md': '3031a78d5ffe33c182e7fc70236b5e51566cadbe',
    R_ + 'minacc-1-20261108/amendments/A3-post-result-prot-r.md': '216e0a216a4d276144156a993ab5189d16a18e54',
    R_ + 'mechanism-2-20261108/DESIGN.md': '9352d9da7da6a55a52e6ada235034219638b34d2',
}
BRANCHES_LINE = 'arp1-marc branches: round research/arp1-marc-20261108; dev draft/arp1-marc-dev'
ROUND_BRANCH = 'research/arp1-marc-20261108'
DEV_BRANCH = 'draft/arp1-marc-dev'
OWNER = ('amaybaum', 'OWNER')
MEAS = 'evidence/measurements.json'
S1_SET = ('marc_check.py', 'controls.py', 'evidence/design-run.json', 'evidence/f-run/results.json')
E_SET = (MEAS, 'evidence/s1-run/results.json', 'evidence/order.json', 'result.md')
W_OPTIONAL = (MEAS, 'evidence/s1-run/results.json', 'evidence/void-run.json')
SHARD_JOB = 'Numerical probes / ARP-1-MARC exact span check'
STEPS = {'checkout': 'Run actions/checkout@v4', 'setup': 'Run actions/setup-python@v5',
         'check': 'ARP-1-MARC exact span check', 'upload': 'ARP-1-MARC keep the measurements',
         'replay': 'ARP-1-MARC replay against the committed measurements',
         'selftest': 'ARP-1-MARC checker self-test', 'mutation': 'ARP-1-MARC control mutation tests'}
RUN_SCHEMA, ORDER_SCHEMA, VOID_SCHEMA, MEAS_SCHEMA = ('arp1-marc-run', 'arp1-marc-order', 'arp1-marc-void-run',
                                                      'arp1-marc-measurements')
TOKENS = {'EXPOSURE': 'ARP1-MARC-EXPOSURE', 'SURVIVAL': 'ARP1-MARC-SURVIVAL',
          'SIZE-DEPENDENT': 'ARP1-MARC-SIZE-DEPENDENT', 'VOID': 'ARP1-MARC-VOID'}
CONTROLS = ('CC-ISO', 'C-NV', 'C-SUPP-X', 'C-SUPP-F', 'C9', 'C-DEISO', 'C-XB', 'M-PLANT', 'C-STEP', 'C-HOR')
SIZE_KEYS = ('4', '6')
CASES = 6008
PARAMETERS = {'q': 2, 'w': 3, 'T': 4, 'H': [4, 6], 'L': [7, 9], 'rule': "N_1: u_i' = u_{i-1} + u_{i+1} + v_i, v_i' = u_i",
              'registration_times': [0, 1, 2, 3, 4], 'patterns': 8, 'schedules': 751, 'cases': 6008}
MARC_IMPORTS = {'fractions', 'itertools', 'json', 'sys'}
CONTROLS_IMPORTS = {'ast', 'hashlib', 'io', 'json', 'os', 're', 'subprocess', 'sys', 'tempfile', 'zipfile'}
MARC_FORBIDDEN = {'open', 'exec', 'eval', '__import__', 'importlib', 'subprocess', 'float', 'complex', 'compile'}
CONTROLS_FORBIDDEN = {'exec', 'eval', '__import__', 'importlib', 'compile'}
OS_FORBIDDEN = {'system', 'popen', 'execv', 'execve', 'execvp', 'execl', 'execlp', 'spawnv', 'spawnl', 'fork',
                'remove', 'unlink', 'rmdir', 'rename', 'replace'}
S4_PHRASES = ('native protection', 'native instance', 'theorem', 'proves', 'proved', 'never', 'permanently',
              'always protects', 'derived from a4', ' iff ', 'if and only if', 'is equivalent to', 'exactly when',
              'in general', 'for every observer', 'physically justified', 'should not be read')
OWNER_QUOTES = ('failure to construct a witness is not proof that no witness exists, unless a theorem establishes '
                'that impossibility within a clearly stated scope.',
                'Conversely, relaxing an assumption is not sufficient by itself. The resulting model must still '
                'produce valid probabilities, observable quantum predictions and consistent behavior across repeated '
                'experiments.')
QUOTE_OPENINGS = ('failure to construct a witness', 'conversely, relaxing an assumption')
QUALIFIER = "outside this round's model, not established"
BROAD_TERMS = ('oi generally', 'every oi model', 'any oi model', 'beyond this model', 'outside this model',
               'in every model', 'all models')
TOKEN_LINE = '**Token:** `%s`'

# Frozen texts and constants, copied from the preregistration (the self-test checks each against it).
COMMON_T = 'This concerns the finite model of this round: the ring `Z_L` with `L ∈ {7, 9}`, the rule `N_1` at `q = 2`, a three-cell window, horizon `T = 4`, at most one registration per tick and each cell registered at most once. It is conditional on the supplied registration, on P2 with its support clause, and on H-PREP for a known value 1. Determination uses no measure; no statement about bias is made. Agreement of the two ring sizes is not evidence about an infinite chain: at both sizes some sites of `H` are reached within `T` from both ends of the window, which only `|H| ≥ 2T = 8` would exclude. Nothing here concerns other rules, larger windows or horizons, an archive held elsewhere, or a physically sourced observer.'
EXPOSURE_T = "In variant D, where the registered cell stays on the ring and its site joins `H`, the span of the transported known and registered functionals contains a `Q* = 1` linear functional on the current `V` in {n4} of 6008 cases at `|H| = 4` and {n6} of 6008 at `|H| = 6`; among cases with no registration at `t = T`, {m4} and {m6}; among cases registering only at `t ∈ {1, …, T − 1}`, {k4} and {k6}. First witness, at `|H| = 4`: {witness}; it {uses or does not use} a registration at `t = T`. Every control is green at both sizes; variant I gives no such functional at either size. In this model the de-isolated archive does not protect: the protection Lemma Q(iii) gives here needs the archived cell's isolation from the ring, which the fixed partition into `V` and `H` does not supply."
SURVIVAL_T = "In variant D, where the registered cell stays on the ring and its site joins `H`, no case up to `T = 4` places a `Q* = 1` linear functional on the current `V` in the span of the transported known and registered functionals, at `|H| = 4` or at `|H| = 6`. Every control is green at both sizes. In this model, protection of `Q* = 1` functionals on the current `V` survives the removal of the archive's coupling isolation. It does not derive P1, P2 or the support clause, and it is not a statement beyond the stated horizon and sizes."
SIZE_T = 'The two sizes disagree: variant D has {n4} exposing cases at `|H| = 4` and {n6} at `|H| = 6` (with no registration at `t = T`: {m4} and {m6}; registering only at `t ∈ {1, …, T − 1}`: {k4} and {k6}). Every control is green at both sizes. The result is reported as size-dependent and carries neither the exposure nor the survival reading.'
VOID_T = 'A required control failed, or the output was incomplete: {codes and sizes}. No reading about variant D is made. The measurements are preserved as produced.'
NOS_T = "it is not a universal statement in either direction; it does not adopt or promote M2D's reading of Lemma Q as an instance of M-INACC, or Lemma Q's labels; it does not change the status of P1, P2, H-PREP or any manuscript claim; an exposure is not evidence that a physically sourced observer could expose, and a survival is not evidence that P1 is dispensable outside this model."
DIR_P = '**Which direction is the obstruction.** Primary reading: the target is QM-like inaccessibility, a functional the dynamics uses and the observer cannot determine (M-INACC, M2D:832-840). Under it the obstruction is **EXPOSURE**: exposure means that the protection depended on the imported isolation L-ISO. Opposite reading: if the target is taken instead as an observer able to determine what the dynamics uses, the obstruction is **SURVIVAL**. Part 2 answers the five questions for whichever substantive label is measured, under the reading in which that label is the obstruction, and states the other reading beside it. Neither label is pre-judged as favourable. SIZE-DEPENDENT and VOID get no ADA beyond Part 3 and the record of what was measured.'
Q_EXPO = "**The five questions, for EXPOSURE (the obstruction under the primary reading):** 1. *Essential to the failure:* the exposure followed the removal of L-ISO alone (D against I, measured at both sizes). Which kept assumptions the exposure needs is not measured here (NR-1 to NR-4, NR-6). Used and not varied, so untested as causes: L-STEP, L-NN, L-Q2, L-REG, L-P2's half-known supply, L-SUP, L-RING with the archive's adjacency. The protection-carrying items above are not causes of the exposure: violating any of them makes exposure easier. 2. *Their types:* from the ledger: L-ISO is imported. For L-Q2, L-NN and L-PRIOR both readings are printed. 3. *Does removing an imported assumption eliminate the obstruction?* Not decided here. The exposure arose from removing L-ISO. Whether removing or changing another imported item (L-REG, L-P2, L-RING) restores protection needs a new variant: candidate rounds NR-1 to NR-4. 4. *A counterexample satisfying the same observable requirements without it?* Not decided here: this round measures no observable requirement (NR-7). 5. *All OI models, or only this one?* Only this model: `N_1`, `q = 2`, the ring `Z_L` with `L ∈ {7, 9}`, `w = 3`, `T = 4`, supplied registration and P2."
Q_SURV = "**The five questions, for SURVIVAL (the obstruction under the opposite reading):** 1. *Essential to the survival:* L-ISO's removal is measured not to expose. The protection-carrying items, as fixed by the controls' design: L-ACC (C9, exposure at registration time), L-P2 (M-PLANT, both variants), L-SUP (C-SUPP-X, variant I only). Used and not varied: L-STEP, L-NN, L-Q2, L-REG, L-RING. 2. *Their types:* from the ledger, both readings for L-Q2, L-NN and L-PRIOR. 3. *Does removing an imported assumption eliminate it?* Not decided here; removing L-REG or L-P2, or changing L-RING, needs a new variant (NR-2 to NR-4). 4. *A counterexample satisfying the same observable requirements without it?* Not decided here (NR-7). 5. *All OI models, or only this one?* Only this model, as listed for EXPOSURE."
WP_P = '**The witness principle, applied to SURVIVAL.** The note prints, verbatim, the owner\'s principle: "failure to construct a witness is not proof that no witness exists, unless a theorem establishes that impossibility within a clearly stated scope." A SURVIVAL label is finite and conditional. Within the enumerated scope (the 6008 fixed-schedule cases at each size, `T = 4`, `w = 3`, `|H| ∈ {4, 6}`, the kept assumptions) it is an exhaustive finite computation of span membership, cross-checked by C-XB\'s direct simulation under the uniform law with known values 0; it is classified as that verification layer. Its extension to every full-support law and every adaptive schedule is a paper reduction (*The exact method*: the knowledge set is affine; an adaptive schedule is fixed within a branch), sound but on paper. Outside that scope it is not an impossibility of exposure. The only impossibility result used here is Lemma Q(iii), and its scope is the isolated archive under P1 and P2 (variant I), not variant D.'
STD_P = '**For either substantive label**, the note adds the owner\'s standard verbatim: "Conversely, relaxing an assumption is not sufficient by itself. The resulting model must still produce valid probabilities, observable quantum predictions and consistent behavior across repeated experiments." Variant D\'s probabilities, predictions and repeatability are not measured here (NR-5, NR-7).'
NR_P = "**Candidate new rounds (named, not run):** NR-1 the archive held away from the window (a non-adjacent site of `H`, or moved), the budget question of AP1:338-343; NR-2 larger `w`, `T`, `|H|`, including `|H| ≥ 2T` (free of two-sided finite-size effects) and `T > |H|`; NR-3 registration through a native coupling to a meter cell instead of a supplied slot read (removing L-REG); NR-4 ready cells prepared by the dynamics instead of supplied (removing L-P2); NR-5 bias (PROT-B) in D under named full-support laws; NR-6 other alphabets (L-Q2), next-nearest-neighbour center-free couplings (L-NN) and the cubic graph (L-RING), as extensions; NR-7 the observable level: valid probabilities, quantum predictions and repeatability of variant D's induced statistics, without weakening the empirical standard."
P3A = "Variant D must not carry an imported item under another name. Each row is measured at both sizes and is part of C-DEISO's green criterion."
P3B = "L-ACC is the archive's access property. It is kept in both variants, named in the ledger, and its effect is measured (C9). It is not isolation renamed: it restricts what the observer reads, not what the dynamics couples."
LEDGER_ROWS = ['| id | assumption, as this round uses it | type | source |', '| --- | --- | --- | --- |', '| L-STEP | second-order, linear, symmetric, center-free update (`k_ij = k_ji`, `k_ii = 0`) | native | Substratum:98, :100 (A4, A5); QA:774-775 |', '| L-NN | nearest-neighbour coupling | **uncertain**: QA\'s ledger calls it "Native, selected branch"; SM calls it an assumption beyond bounded coupling degree (A3). Carried both ways | SM:224-226; QA:776 |', '| L-Q2 | alphabet `F_2` (`q = 2`) | **uncertain**: the records call it "Native parameter value, chosen per the owner\'s instruction"; whether the protection depends on it is untested; carried both ways | QA:462-464; MI-D:595 |', '| L-RING | one-dimensional ring `Z_L`, odd `L ∈ {7, 9}`, three-cell window, horizon `T = 4`; the archived site adjacent to the window | imported (modelling reduction of the cubic graph; the odd ring is not bipartite globally, only within the no-wrap cones C-HOR measures; at both sizes some `H` sites are reached from both window ends within `T`) | QA:776 (H-FIN); M-ARC parameters |', '| L-P2 | ready cells with exactly one known slot; no supplied cell with both slots, or `u + v`, known | imported (supplied posit; motivation programme-internal) | AP1:297-299, :347-349; QA:780 |', "| L-SUP | full joint support of the unknowns (P2's support clause) | imported | AP1:297-299, :547; QA:499-501 |", '| L-PRIOR | product-uniform law (N2, H-PS) | **uncertain**: the records call N2 a native measure applied through H-PREP; its use on supplied cells goes through an imported hypothesis | QA:777; MI-D:309, :605 |', '| L-HPREP | known value 1 through H-PREP | imported (open hypothesis) | QA:782 |', '| L-REG | supplied registration: one slot of one window cell between ticks, at most once per cell, the joint record kept whole | imported (SA-1(b), access part) | AP1:292-296; MI-D:351-365 |', '| L-SWAP | refills and archive swaps | imported; **not in this model** | MI-D:361-362; MI-A1:203-213 |', "| L-ISO | the archived cell's coupling isolation (P1 terminality) | imported; **removed in variant D**, kept in I. Not enforced natively; enforced within a budget below recurrence only by the supplied P3 and E-iso | AP1:295-296, :338-343; QA:781; MI-D:357-358 |", '| L-ACC | the archived cell leaves the window and is not read again | imported (access part of P1), kept in both variants | MI-D:357-360; M-ARC |', '| L-DET | "determined" as constant on the support given `K`; PROT-D as the absence of a determined `Q* = 1` functional on active cells | imported (definitional) | MI-D:135-137, :429-432 |', '| L-PROTB | PROT-B (no bias) | imported (definitional); **not evaluated** here | MI-D:433-436 |', "| L-INACC | the identification of protection with inaccessibility in M-INACC's sense. Reading used (AW-C3-4): clause (b) read as non-determination of a `Q* = 1` functional on the current window (PROT-D); clause (b)'s conditional-law reading (bias) and clause (a) are not tested | imported (interpretive); the identification with this functional is model-specific | M2D:832-840; MI-A1:59-70 |", '| E-AR | at most two perfectly distinguishable preparations of a qubit carrier: the observable bound behind L-INACC | empirical; **not tested** in this round (NR-7) | AP1:439, :677 |']
PART3_ROWS = ['| imported item | the form it could take in D | how it is excluded |', '| --- | --- | --- |', "| L-ISO (coupling isolation) | a dropped or weakened edge, a vacancy, a free tick, delayed coupling | (a) D's step is the unmodified ring matrix at every tick; (b) D and I differ only in archived rows and columns; (c) re-coupling reaches the window in D and in no case of I |", "| L-SWAP (refill, swap) | a reset or replacement of the archived cell's state; a fresh known cell | (a); (e) no functional is added to `I_t` after `t = 0` (`knowledge_injections = 0`) |", '| P3, E-iso | an edge multiplier | (a) |', '| narrower access in D | fewer schedules or windows than I | (d) identical case lists, supply patterns included |', '| discarded knowledge | a dropped record, or `I_t` not transported whole | (d) `R_t` carries every registration; `I_t` keeps rank 3 |', "| a restricted prior | a support restriction in D's supply | (d) identical supply patterns; C-SUPP-X's relation enters variant I only |", '| a narrowed target | fewer functionals evaluated in D than in I | the same evaluation rule (every functional on the current window) in both; L-ACC is shared and its effect is measured by C9 |']
STATUS_FIXED = ['| L-P2 | **protection-carrying**: a planted `u + v`-known cell exposes, in both variants (M-PLANT) | fixed by design |', '| L-SUP | **protection-carrying in variant I**: a supplied exact relation exposes (C-SUPP-X runs in variant I only) | fixed by design |', '| L-PRIOR | **idle for determination**: a full-support correlated law does not determine (C-SUPP-F, variant I, one protocol); it enters no span computation | fixed by design |', "| L-HPREP | **idle at `L = 7`**: C-XB's all-1 repeat agrees with the span method (`L = 9` not repeated) | fixed by design |", '| L-SWAP, L-PROTB | **absent or not evaluated** | — |', "| L-STEP, L-NN, L-Q2, L-REG, L-DET, L-INACC, E-AR | **used, not varied** (E-AR: not used). L-STEP's center-freeness is used by Lemma Q(i) (QA:478-486); its necessity is the records' result (QA:518-521), not measured here | used, not varied |", "| L-RING | `|H|` varied (agreement of the two sizes, measured); `w`, `T`, the dimension, the parity of `L` and the archive's adjacency not varied; agreement is not evidence about an infinite chain (`|H| ≥ 2T` would be needed) | partly measured |"]
P6_CODE = "import sys; sys.path.insert(0, 'tools'); import v3_verifier as v; r = v.Repo('.'); d, f = sys.argv[1], sys.argv[2]; rd, rid, kind, ent, cp, codes = v.control_plane(r, d, f); t1 = v.check_t1(r, d, f, cp); dig = v.governed_digest(ent) if ent else None; print(rid, kind, rd, dig, codes + t1); sys.exit(0 if not (codes or t1) and (rid, kind, rd) == ('ARP-1-MARC', 'non-sealing', b'verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/') and dig == '4ddc9a8af70564d7b73a65b3f431a0b4fbdf1c1518327f6e4d8ea6dff2702563' else 1)"
FROZEN_JOB = '  probes_arp1marc:\n    name: Numerical probes / ARP-1-MARC exact span check\n    runs-on: ubuntu-latest\n    timeout-minutes: 30\n    steps:\n      - uses: actions/checkout@v4\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: \'3.11\'\n\n      - name: ARP-1-MARC exact span check\n        if: ${{ github.event_name == \'workflow_dispatch\' || hashFiles(\'verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/evidence/measurements.json\') != \'\' }}\n        timeout-minutes: 15\n        run: |\n          mkdir -p "$RUNNER_TEMP/arp1-marc"\n          python3 -I -B verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/marc_check.py > "$RUNNER_TEMP/arp1-marc/measurements.json"\n\n      - name: ARP-1-MARC keep the measurements\n        if: ${{ always() && github.event_name == \'workflow_dispatch\' }}\n        uses: actions/upload-artifact@v4\n        with:\n          name: arp1-marc-measurements\n          path: ${{ runner.temp }}/arp1-marc/measurements.json\n          if-no-files-found: error\n          retention-days: 30\n\n      - name: ARP-1-MARC replay against the committed measurements\n        if: ${{ github.event_name == \'workflow_dispatch\' || hashFiles(\'verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/evidence/measurements.json\') != \'\' }}\n        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/controls.py replay "$RUNNER_TEMP/arp1-marc/measurements.json"\n\n      - name: ARP-1-MARC checker self-test\n        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/marc_check.py --self-test\n\n      - name: ARP-1-MARC control mutation tests\n        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/controls.py --self-test\n'
ROUND_BLOCK = 'round ARP-1-MARC\nkind non-sealing\nrecord-directory verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/\n'
GOVERNED_BLOCK = 'record AM verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/\nrecord AM verification/receipts/ARP-1-MARC.json\nexecution M .github/workflows/verify.yml\n'

# The aggregate edits and the job anchor at D (preregistration *The workflow edit*; anchors read at 2cd49dc0).
JOB_ANCHOR = '  probes:\n    name: Numerical probes\n'
AGG_EDITS = (
    ('probes_a42_exclusion, probes_foundations]', 'probes_a42_exclusion, probes_foundations, probes_arp1marc]'),
    ('          FOUNDATIONS_RESULT: ${{ needs.probes_foundations.result }}\n',
     '          FOUNDATIONS_RESULT: ${{ needs.probes_foundations.result }}\n'
     '          ARP1MARC_RESULT: ${{ needs.probes_arp1marc.result }}\n'),
    ('          echo "foundations=${FOUNDATIONS_RESULT}"\n',
     '          echo "foundations=${FOUNDATIONS_RESULT}"\n          echo "arp1marc=${ARP1MARC_RESULT}"\n'),
    ('          test "${FOUNDATIONS_RESULT}" = success\n',
     '          test "${FOUNDATIONS_RESULT}" = success\n          test "${ARP1MARC_RESULT}" = success\n'),
)
_CHECK_IF = ("        if: ${{ github.event_name == 'workflow_dispatch' || hashFiles('verification/programmes/oi-qm/"
             "reconstruction/round-arp1-marc-20261108/evidence/measurements.json') != '' }}\n")
_UPLOAD_IF = "        if: ${{ always() && github.event_name == 'workflow_dispatch' }}\n"
_CHECK_LINE = 'round-arp1-marc-20261108/marc_check.py > "$RUNNER_TEMP/arp1-marc/measurements.json"\n'


def design_job(job=None):
    """The frozen job with exactly the three substitutions of *The design splice*."""
    j = FROZEN_JOB if job is None else job
    if j.count(_CHECK_IF) != 2 or j.count(_UPLOAD_IF) != 1 or j.count(_CHECK_LINE) != 1:
        raise ValueError('design-job anchors')
    j = j.replace(_CHECK_LINE, _CHECK_LINE.replace('marc_check.py >', 'marc_check.py --fixture-output >'))
    j = j.replace(_CHECK_IF, '')
    return j.replace(_UPLOAD_IF, '        if: ${{ always() }}\n')


DESIGN_JOB = design_job()


def splice(d_text, job=FROZEN_JOB):
    """D's verify.yml with the job inserted before the probes aggregate and the three aggregate edits."""
    t = d_text
    if t.count(JOB_ANCHOR) != 1:
        raise ValueError('workflow anchor: job')
    t = t.replace(JOB_ANCHOR, job + '\n' + JOB_ANCHOR)
    for old, new in AGG_EDITS:
        if t.count(old) != 1:
            raise ValueError('workflow anchor: ' + old.strip()[:40])
        t = t.replace(old, new)
    return t


def extract_job(text, name='probes_arp1marc'):
    """The job's text from its key line to its last non-blank line (newline-terminated), or None."""
    lines = text.split('\n')
    try:
        k = lines.index('  %s:' % name)
    except ValueError:
        return None
    end = k + 1
    while end < len(lines):
        ln = lines[end]
        if ln.strip() and (len(ln) - len(ln.lstrip(' '))) <= 2:
            break
        end += 1
    body = lines[k:end]
    while body and not body[-1].strip():
        body.pop()
    return '\n'.join(body) + '\n'


# =====================================================================================================================
# small utilities
# =====================================================================================================================
def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')) + '\n'


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def git_blob(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def norm_ws(s):
    return ' '.join(s.split())


def is_hex(s, n):
    return isinstance(s, str) and len(s) == n and re.fullmatch(r'[0-9a-f]+', s) is not None


def is_int(x):
    return isinstance(x, int) and not isinstance(x, bool)


class Refusal(Exception):
    pass


_GIT_ENV_KEEP = ('PATH', 'HOME', 'GIT_AUTHOR_NAME', 'GIT_AUTHOR_EMAIL', 'GIT_COMMITTER_NAME', 'GIT_COMMITTER_EMAIL',
                 'GIT_AUTHOR_DATE', 'GIT_COMMITTER_DATE', 'TMPDIR')


def _env(extra=None):
    e = {k: os.environ[k] for k in _GIT_ENV_KEEP if k in os.environ}
    e.update({'LC_ALL': 'C', 'GIT_TERMINAL_PROMPT': '0', 'GIT_CONFIG_NOSYSTEM': '1'})
    if extra:
        e.update(extra)
    return e


def git(cwd, *args, ok=(0,), env=None, data=None):
    r = subprocess.run(('git',) + args, cwd=cwd, input=data, capture_output=True, env=_env(env))
    if r.returncode not in ok:
        return None
    return r.stdout


def git_show(cwd, commit, path):
    return git(cwd, 'show', '%s:%s' % (commit, path))


def git_rev(cwd, spec):
    out = git(cwd, 'rev-parse', '--verify', '-q', spec)
    return out.decode().strip() if out else None


def run_p6(cwd, d, f):
    """Precondition 6's command, its argv frozen apart from the two commit ids (control B checks this call)."""
    r = subprocess.run(['python3', '-I', '-c', P6_CODE, d, f], cwd=cwd, capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').strip()


def repo_root():
    out = git(os.getcwd(), 'rev-parse', '--show-toplevel')
    if out is None:
        raise Refusal('not inside a git repository')
    return out.decode().strip()


def load_json_file(path):
    with open(path, 'rb') as fh:
        raw = fh.read()
    return raw, json.loads(raw)


# =====================================================================================================================
# The preregistration at F: the fields filled before F
# =====================================================================================================================
def strip_inline_code(line):
    return re.sub(r'(`+)(?:(?!\1).)+?\1', '', line)


def pending_fields(text):
    """Bare PENDING outside an inline code span; fenced code blocks count as outside."""
    hits = []
    fence = False
    for no, line in enumerate(text.split('\n'), 1):
        if line.lstrip().startswith('```'):
            fence = not fence
            continue
        probe = line if fence else strip_inline_code(line)
        if re.search(r'\bPENDING\b', probe):
            hits.append(no)
    return hits


def prereg_fields(text):
    """The values the preregistration pins; None where not (yet) filled."""
    def one(pat):
        m = re.search(pat, text)
        return m.group(1) if m else None
    flds = {
        'D': one(r'- \*\*`D`\*\* = `([0-9a-f]{40})`:'),
        'marc_blob': one(r'\*\*`marc_check\.py`\*\* \(record directory; blob `([0-9a-f]{40})`, sha256 `[0-9a-f]{64}`\)'),
        'marc_sha256': one(r'\*\*`marc_check\.py`\*\* \(record directory; blob `[0-9a-f]{40}`, sha256 `([0-9a-f]{64})`\)'),
        'controls_blob': one(r'\*\*`controls\.py`\*\* \(record directory; blob `([0-9a-f]{40})`, sha256 `[0-9a-f]{64}`\)'),
        'controls_sha256': one(r'\*\*`controls\.py`\*\* \(record directory; blob `[0-9a-f]{40}`, sha256 `([0-9a-f]{64})`\)'),
        'design_run_sha256': one(r'whose sha256 is pinned here: `([0-9a-f]{64})`'),
        'design_pr': one(r'The design PR number: #(\d+)'),
    }
    m = re.search(r'\*\*Design pairs \(frozen at `F`\)\.\*\*(.*?)(?:\n\n|\n\*\*)', text, re.S)
    pairs = []
    if m:
        lst = m.group(1).split('The list:', 1)
        if len(lst) == 2:
            pairs = re.findall(r'\(`([0-9a-f]{40})`, `([0-9a-f]{40})`\)', lst[1])
    flds['design_pairs'] = [tuple(p) for p in pairs]
    return flds


def branches_line_ok(text):
    return text.split('\n').count(BRANCHES_LINE) == 1


def blocks_ok(text):
    return ('```v3-round\n' + ROUND_BLOCK + '```') in text and ('```v3-governed-paths\n' + GOVERNED_BLOCK + '```') in text


# =====================================================================================================================
# Control B: static form of both scripts (AST)
# =====================================================================================================================
def _imports(tree):
    names = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            names |= {a.name for a in n.names}
        elif isinstance(n, ast.ImportFrom):
            names.add(n.module or '')
    return names


def _names(tree):
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Name):
            out.add(n.id)
        elif isinstance(n, ast.Attribute):
            out.add(n.attr)
    return out


def static_marc(src):
    codes = []
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return ['B:marc:syntax']
    if not _imports(tree) <= MARC_IMPORTS:
        codes.append('B:marc:imports')
    bad = _names(tree) & MARC_FORBIDDEN
    if bad:
        codes.append('B:marc:forbidden:' + ','.join(sorted(bad)))
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)):
            codes.append('B:marc:float-literal')
            break
    for n in ast.walk(tree):
        if isinstance(n, (ast.BinOp, ast.AugAssign)) and isinstance(n.op, ast.Div):
            codes.append('B:marc:true-division')
            break
    return codes


def _is_git_argv(node):
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        node = node.left
    return (isinstance(node, (ast.Tuple, ast.List)) and node.elts and isinstance(node.elts[0], ast.Constant)
            and node.elts[0].value == 'git')


def _is_p6_argv(node):
    if not (isinstance(node, ast.List) and len(node.elts) == 6):
        return False
    e = node.elts
    return ([getattr(x, 'value', None) for x in e[:3]] == ['python3', '-I', '-c'] and isinstance(e[3], ast.Name)
            and e[3].id == 'P6_CODE' and isinstance(e[4], ast.Name) and isinstance(e[5], ast.Name))


def static_controls(src, frozen_p6):
    codes = []
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return ['B:controls:syntax']
    if not _imports(tree) <= CONTROLS_IMPORTS:
        codes.append('B:controls:imports')
    bad = _names(tree) & CONTROLS_FORBIDDEN
    if bad:
        codes.append('B:controls:forbidden:' + ','.join(sorted(bad)))
    p6 = [n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'P6_CODE'
                                                                     for t in n.targets)]
    if len(p6) != 1 or not isinstance(p6[0].value, ast.Constant) or p6[0].value.value != frozen_p6:
        codes.append('B:controls:p6-code')
    parent = {}
    for n in ast.walk(tree):
        for ch in ast.iter_child_nodes(n):
            parent[ch] = n

    def enclosing_fn(n):
        while n in parent:
            n = parent[n]
            if isinstance(n, ast.FunctionDef):
                return n.name
        return None
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) and f.value.id == 'subprocess':
            if f.attr != 'run' or not n.args or any(k.arg == 'shell' for k in n.keywords):
                codes.append('B:controls:subprocess-form')
            elif not (_is_git_argv(n.args[0]) or _is_p6_argv(n.args[0])):
                codes.append('B:controls:subprocess-target')
        if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) and f.value.id == 'os' \
                and f.attr in OS_FORBIDDEN:
            codes.append('B:controls:os-call:' + f.attr)
        if isinstance(f, ast.Name) and f.id == 'open':
            mode = n.args[1] if len(n.args) > 1 else next((k.value for k in n.keywords if k.arg == 'mode'), None)
            write = mode is not None and (not isinstance(mode, ast.Constant) or not isinstance(mode.value, str)
                                          or re.search(r'[wax+]', mode.value))
            fn = enclosing_fn(n)
            if write and not (fn or '').startswith(('self_test', '_st_')):
                codes.append('B:controls:write-open')
    return codes


# =====================================================================================================================
# The measurement schema and the decision rule (frozen; independent of marc_check.py)
# =====================================================================================================================
def _size_schema(key):
    N, B, S, H64, FR = 'int', 'bool', 'str', 'hex64', 'frac'
    per3 = {'D': N, 'I': N, 'C9': N}
    xb = {'checked_cases': dict(per3), 'checked_times': dict(per3), 'exposing_V': dict(per3), 'mismatches': N,
          'exposure_mismatches': N}
    if key == '4':
        xb['all1'] = {'checked_cases': {'D': N, 'I': N}, 'mismatches': N, 'exposure_mismatches': N}
    return {
        'D': {'cases': N, 'exposing_V': N, 'exposing_V_no_reg_at_T': N, 'exposing_V_reg_in_1_to_Tm1': N,
              'witness': 'witness', 'nv_cases': N, 'coupling_cases': N, 'step_is_ring_violations': N,
              'records_kept_violations': N, 'min_rank_I': N, 'knowledge_injections': N},
        'I': {'cases': N, 'exposing_V': N, 'exposing_active': N, 'nonisotropic': N, 'nv_cases': N,
              'coupling_cases': N},
        'd_i_diff_outside_archived': N,
        'case_list_sha256': {'D': H64, 'I': H64},
        'supp_x': {'cases': N, 'exposing_V': N},
        'supp_f': {'law': {'pair': S, 'P': {'00': FR, '01': FR, '10': FR, '11': FR}, 'others': S},
                   'cond_v0_0': FR, 'cond_v0_1': FR, 'span_determined': B},
        'c9': {'cases': N, 'exposing_V': N, 'exposing_at_registration': N},
        'plant': {'D': {'empty_t0': B, 'exposing_V': N}, 'I': {'empty_t0': B, 'exposing_V': N}},
        'xb': xb,
        'step': {'violations': N},
        'horizon': {'T_le_H': B, 'radius_violations': N},
        'flags': {c: B for c in CONTROLS},
    }


def _check_witness(w, path, errs):
    if w is None:
        return
    keys = {'pattern', 'schedule', 't', 'window', 'code', 'functional', 'uses_t_eq_T'}
    if not isinstance(w, dict) or set(w) != keys:
        errs.append(path + ': witness keys')
        return
    ok = (isinstance(w['pattern'], str) and re.fullmatch(r'[uv]{3}', w['pattern'])
          and isinstance(w['schedule'], list) and len(w['schedule']) == 5
          and all(a is None or (isinstance(a, list) and len(a) == 2 and is_int(a[0]) and a[1] in ('u', 'v'))
                  for a in w['schedule'])
          and is_int(w['t']) and 0 <= w['t'] <= 4 and isinstance(w['window'], list)
          and all(is_int(c) for c in w['window']) and is_int(w['code'])
          and isinstance(w['functional'], str) and re.fullmatch(r'[uv]_\d(\+[uv]_\d)*', w['functional'])
          and isinstance(w['uses_t_eq_T'], bool))
    if not ok:
        errs.append(path + ': witness form')


def _validate(obj, spec, path, errs):
    if isinstance(spec, dict):
        if not isinstance(obj, dict):
            errs.append(path + ': not an object')
            return
        if set(obj) != set(spec):
            errs.append(path + ': keys %s' % sorted(set(obj) ^ set(spec)))
            return
        for k in spec:
            _validate(obj[k], spec[k], path + '.' + k, errs)
        return
    if spec == 'int':
        if not is_int(obj) or obj < 0:
            errs.append(path + ': not a non-negative integer')
    elif spec == 'bool':
        if not isinstance(obj, bool):
            errs.append(path + ': not a boolean')
    elif spec == 'str':
        if not isinstance(obj, str):
            errs.append(path + ': not a string')
    elif spec == 'hex64':
        if not is_hex(obj, 64):
            errs.append(path + ': not a sha256')
    elif spec == 'frac':
        if not (isinstance(obj, str) and re.fullmatch(r'\d+(/[1-9]\d*)?', obj)):
            errs.append(path + ': not "p/q"')
    elif spec == 'witness':
        _check_witness(obj, path, errs)


def schema_errors(m):
    errs = []
    if not isinstance(m, dict):
        return ['top: not an object']
    if set(m) != {'schema', 'version', 'parameters', 'complete', '4', '6'}:
        return ['top: keys %s' % sorted(m)]
    if m['schema'] != MEAS_SCHEMA or m['version'] != 1 or isinstance(m['version'], bool):
        errs.append('top: schema or version')
    if m['parameters'] != PARAMETERS:
        errs.append('top: parameters')
    if not isinstance(m['complete'], bool):
        errs.append('top: complete')
    for k in SIZE_KEYS:
        _validate(m[k], _size_schema(k), k, errs)
    return errs


def green_flags(s, key):
    """decide's recomputation of every green flag from the raw fields (the frozen field -> predicate table)."""
    D, I, xb = s['D'], s['I'], s['xb']
    g = {}
    g['CC-ISO'] = I['exposing_V'] == 0 and I['exposing_active'] == 0 and I['nonisotropic'] == 0
    g['C-NV'] = D['nv_cases'] > 0 and I['nv_cases'] > 0
    g['C-SUPP-X'] = s['supp_x']['exposing_V'] > 0
    g['C-SUPP-F'] = (s['supp_f']['cond_v0_0'] == '3/4' and s['supp_f']['cond_v0_1'] == '1/4'
                     and s['supp_f']['span_determined'] is False)
    g['C9'] = s['c9']['exposing_V'] > 0
    g['C-DEISO'] = (D['step_is_ring_violations'] == 0 and s['d_i_diff_outside_archived'] == 0
                    and D['coupling_cases'] > 0 and I['coupling_cases'] == 0
                    and s['case_list_sha256']['D'] == s['case_list_sha256']['I']
                    and D['records_kept_violations'] == 0 and D['min_rank_I'] == 3 and D['knowledge_injections'] == 0)
    xbg = (all(xb['checked_cases'][v] == CASES for v in ('D', 'I', 'C9'))
           and all(xb['checked_times'][v] == 5 * CASES for v in ('D', 'I', 'C9'))
           and xb['mismatches'] == 0 and xb['exposure_mismatches'] == 0
           and xb['exposing_V']['D'] == D['exposing_V'] and xb['exposing_V']['I'] == I['exposing_V']
           and xb['exposing_V']['C9'] == s['c9']['exposing_V'])
    if key == '4':
        a = xb['all1']
        xbg = (xbg and a['checked_cases']['D'] == CASES and a['checked_cases']['I'] == CASES
               and a['mismatches'] == 0 and a['exposure_mismatches'] == 0)
    g['C-XB'] = xbg
    p = s['plant']
    g['M-PLANT'] = (p['D']['empty_t0'] is True and p['I']['empty_t0'] is True and p['D']['exposing_V'] > 0
                    and p['I']['exposing_V'] > 0)
    g['C-STEP'] = s['step']['violations'] == 0
    g['C-HOR'] = s['horizon']['T_le_H'] is True and s['horizon']['radius_violations'] == 0
    return g


def decide(m, exit_status=None):
    """(label, reasons, recomputed flags or None). label in EXPOSURE, SURVIVAL, SIZE-DEPENDENT, VOID."""
    reasons = []
    if exit_status is not None and exit_status != 0:
        reasons.append('the checker exit status was %s' % exit_status)
    if m is None:
        return 'VOID', reasons + ['the measurements are missing or do not parse'], None
    errs = schema_errors(m)
    if errs:
        return 'VOID', reasons + ['the measurements break the schema (%s)' % errs[0]], None
    if m['complete'] is not True:
        reasons.append('the output is incomplete')
    rec = {}
    for k in SIZE_KEYS:
        rec[k] = green_flags(m[k], k)
        for c in CONTROLS:
            if not rec[k][c]:
                reasons.append('%s at |H| = %s' % (c, k))
        if m[k]['flags'] != rec[k]:
            reasons.append("the checker's flags disagree with the recomputation at |H| = %s" % k)
    if reasons:
        return 'VOID', reasons, rec
    x4, x6 = m['4']['D']['exposing_V'] > 0, m['6']['D']['exposing_V'] > 0
    if x4 and x6:
        return 'EXPOSURE', [], rec
    if not x4 and not x6:
        return 'SURVIVAL', [], rec
    return 'SIZE-DEPENDENT', [], rec


# =====================================================================================================================
# The result note (frozen texts; generated) and the S4 screen
# =====================================================================================================================
FIELD_TABLE = (
    ('CC-ISO', ('I.exposing_V', 'I.exposing_active', 'I.nonisotropic')),
    ('C-NV', ('D.nv_cases', 'I.nv_cases')),
    ('C-SUPP-X', ('supp_x.exposing_V',)),
    ('C-SUPP-F', ('supp_f.cond_v0_0', 'supp_f.cond_v0_1', 'supp_f.span_determined')),
    ('C9', ('c9.exposing_V', 'c9.exposing_at_registration')),
    ('C-DEISO', ('D.step_is_ring_violations', 'd_i_diff_outside_archived', 'D.coupling_cases', 'I.coupling_cases',
                 'case_list_sha256.D', 'case_list_sha256.I', 'D.records_kept_violations', 'D.min_rank_I',
                 'D.knowledge_injections')),
    ('C-XB', ('xb.checked_cases.D', 'xb.checked_cases.I', 'xb.checked_cases.C9', 'xb.checked_times.D',
              'xb.checked_times.I', 'xb.checked_times.C9', 'xb.mismatches', 'xb.exposure_mismatches',
              'xb.exposing_V.D', 'xb.exposing_V.I', 'xb.exposing_V.C9', 'xb.all1.checked_cases.D',
              'xb.all1.checked_cases.I', 'xb.all1.mismatches', 'xb.all1.exposure_mismatches')),
    ('M-PLANT', ('plant.D.empty_t0', 'plant.I.empty_t0', 'plant.D.exposing_V', 'plant.I.exposing_V')),
    ('C-STEP', ('step.violations',)),
    ('C-HOR', ('horizon.T_le_H', 'horizon.radius_violations')),
)


def _get(s, path):
    for part in path.split('.'):
        if not isinstance(s, dict) or part not in s:
            return None
        s = s[part]
    return s


def _fmt(v):
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, str) and len(v) == 64:
        return v[:12]
    return str(v)


def render_witness(w, key):
    if w is None:
        return 'none recorded'
    regs = ['(%d, %s) at t = %d' % (a[0], a[1], t) for t, a in enumerate(w['schedule']) if a is not None]
    return ('pattern `%s`, %s, evaluation time t = %d, functional `%s` on the window {%s}'
            % (w['pattern'], ', '.join(regs) if regs else 'no registration', w['t'], w['functional'],
               ', '.join(str(c) for c in w['window'])))


def check_conclusion(run):
    for st in (run or {}).get('shard_steps') or []:
        if st.get('name') == STEPS['check']:
            return st.get('conclusion')
    return None


def ada_sections(label, m):
    out = ['## ADA', '']
    if label in ('EXPOSURE', 'SURVIVAL'):
        out += [DIR_P, '', '### Statuses', '', '| item | status | kind |', '| --- | --- | --- |']
        iso = []
        for k in SIZE_KEYS:
            dexp = m[k]['D']['exposing_V'] > 0
            iso.append('at `|H| = %s`: **%s**' % (k, 'removal measured to expose' if dexp and m[k]['I']['exposing_V'] == 0
                                                  else 'removal measured not to expose'))
        out.append('| L-ISO | %s | measured |' % '; '.join(iso))
        acc = []
        for k in SIZE_KEYS:
            n = m[k]['c9']['exposing_at_registration']
            acc.append('at `|H| = %s`: **%s** (`c9.exposing_at_registration = %d`)'
                       % (k, 'protection-carrying' if n > 0 else 'not attributed', n))
        out.append('| L-ACC | %s | fixed by design, read from the recorded count |' % '; '.join(acc))
        out += list(STATUS_FIXED)
        out += ['', '### The five questions', '']
        q = Q_EXPO if label == 'EXPOSURE' else Q_SURV
        out.append(re.sub(r' (\d)\. \*', r'\n\1. *', q))
        out.append('')
        if label == 'SURVIVAL':
            out += [WP_P, '']
        out += [STD_P, '', NR_P, '', '### Ledger (frozen at `F`)', ''] + list(LEDGER_ROWS) + ['']
    out += ['### Part 3: the renaming check', '', P3A, ''] + list(PART3_ROWS) + ['', P3B, '']
    for k in SIZE_KEYS:
        s = m[k] if isinstance(m, dict) and isinstance(m.get(k), dict) else {}
        vals = ', '.join('%s %s' % (p, _fmt(_get(s, p))) for p in dict(FIELD_TABLE)['C-DEISO'])
        out.append('C-DEISO at `|H| = %s`: %s.' % (k, vals))
    return out


def make_note(m, s1run, d, f, extra_reasons=()):
    """result.md from the measurements and the derived S1 run (frozen texts; only measured values interpolated)."""
    concl = check_conclusion(s1run)
    exit_status = 0 if concl == 'success' else ('check step %s' % concl)
    label, reasons, rec = decide(m, exit_status)
    if extra_reasons:
        label, reasons = 'VOID', list(reasons) + list(extra_reasons)
    out = ['# ARP-1-MARC result', '', '- round: `%s`' % ROUND, '- D: `%s`' % d, '- F: `%s`' % f,
           '- S1: `%s`' % (s1run or {}).get('head_sha'), '- E: the commit that adds this note', '',
           '## Controls', '', '| code | size | status | raw counts |', '| --- | --- | --- | --- |']
    for code, fields in FIELD_TABLE:
        for k in SIZE_KEYS:
            s = m.get(k) if isinstance(m, dict) else None
            fl = [p for p in fields if not (p.startswith('xb.all1') and k != '4')]
            st = 'PASS' if rec and rec[k][code] else 'FAIL'
            vals = ', '.join('%s=%s' % (p, _fmt(_get(s, p))) for p in fl)
            out.append('| %s | %s | %s | %s |' % (code, k, st, vals))
    out += ['', TOKEN_LINE % TOKENS[label], '']
    if label == 'VOID':
        out.append(VOID_T.replace('{codes and sizes}', '; '.join(reasons)))
    else:
        sub = {}
        for k, kk in (('4', '4'), ('6', '6')):
            D = m[k]['D']
            sub['{n%s}' % kk] = str(D['exposing_V'])
            sub['{m%s}' % kk] = str(D['exposing_V_no_reg_at_T'])
            sub['{k%s}' % kk] = str(D['exposing_V_reg_in_1_to_Tm1'])
        if label == 'EXPOSURE':
            w = m['4']['D']['witness']
            text = EXPOSURE_T.replace('{witness}', render_witness(w, '4'))
            text = text.replace('{uses or does not use}', 'uses' if w and w['uses_t_eq_T'] else 'does not use')
        elif label == 'SURVIVAL':
            text = SURVIVAL_T
        else:
            text = SIZE_T
        for a, b in sub.items():
            text = text.replace(a, b)
        out.append(text + ' ' + COMMON_T)
    out += ['', 'What no outcome shows: ' + NOS_T, '']
    if label == 'VOID' or not isinstance(m, dict) or schema_errors(m):
        out += ['## ADA', '', 'No ADA beyond the record of what was measured (*Assumption-dependence analysis*).', '']
        if isinstance(m, dict) and not schema_errors(m):
            out += ada_sections('VOID', m)[2:]
    else:
        out += ada_sections(label, m)
    return '\n'.join(out).rstrip('\n') + '\n', label


def frozen_texts():
    return (COMMON_T, EXPOSURE_T, SURVIVAL_T, SIZE_T, VOID_T, NOS_T, DIR_P, Q_EXPO, Q_SURV, WP_P, STD_P, NR_P, P3A,
            P3B) + tuple(LEDGER_ROWS) + tuple(PART3_ROWS) + tuple(STATUS_FIXED)


def s4_hits(text, strip_frozen=False):
    t = text
    for q in OWNER_QUOTES:
        t = t.replace(q, '')
    if strip_frozen:
        t = norm_ws(t)
        for ft in sorted(frozen_texts(), key=len, reverse=True):
            for part in re.split(r'\{[^}]*\}', ft):
                if len(part) > 40:
                    t = t.replace(norm_ws(part), ' ')
    low = t.lower()
    hits = [p for p in S4_PHRASES if p in low]
    hits += ['altered quotation: ' + o for o in QUOTE_OPENINGS if o in low]
    return hits


def broad_unqualified(text):
    """The qualifier rule: a sentence naming a scope broader than this model carries the qualifier."""
    bad = []
    for sent in re.split(r'(?<=[.;:])\s+', text):
        low = sent.lower()
        if sent.rstrip().endswith('?'):
            continue
        if any(t in low for t in BROAD_TERMS) and QUALIFIER not in low and 'only this model' not in low \
                and 'not evidence' not in low:
            bad.append(sent)
    return bad


# =====================================================================================================================
# Runs: derive-run, host-VOID, the run checks
# =====================================================================================================================
def _pages(objs, key):
    """Concatenate API pages; the capture must be complete against its total_count."""
    if isinstance(objs, dict):
        objs = [objs]
    items, totals = [], set()
    for p in objs:
        if not isinstance(p, dict) or key not in p or not is_int(p.get('total_count')):
            raise Refusal('a captured page is not a %s page' % key)
        totals.add(p['total_count'])
        items += p[key]
    ids = [it.get('id') for it in items]
    if len(totals) != 1 or len(set(ids)) != len(ids) or len(ids) != totals.pop():
        raise Refusal('the %s capture is incomplete against its total_count' % key)
    return items


def derive_run(run, jobs_pages, artifacts=None, zip_bytes=None):
    if not isinstance(run, dict) or not is_int(run.get('id')) or run['id'] <= 0:
        raise Refusal('run: no positive id')
    jobs = _pages(jobs_pages, 'jobs')
    for j in jobs:
        if j.get('run_id') != run['id']:
            raise Refusal('jobs answer of another run')
    shard = [j for j in jobs if j.get('name') == SHARD_JOB]
    steps = []
    if shard:
        for st in sorted(shard[0].get('steps') or [], key=lambda s: s.get('number', 0)):
            steps.append({'name': st.get('name'), 'conclusion': st.get('conclusion'),
                          'started': st.get('started_at') is not None})
    art = None
    if artifacts is not None or zip_bytes is not None:
        if artifacts is None or zip_bytes is None:
            raise Refusal('artifact: the list answer and the zip go together')
        lst = [a for a in _pages(artifacts, 'artifacts') if a.get('name') == 'arp1-marc-measurements']
        if len(lst) != 1:
            raise Refusal('artifact: not exactly one arp1-marc-measurements')
        a = lst[0]
        if a.get('digest') != 'sha256:' + sha256(zip_bytes):
            raise Refusal('artifact: the zip does not match the API digest')
        wr = a.get('workflow_run') or {}
        if wr.get('id') != run['id'] or wr.get('head_sha') != run.get('head_sha'):
            raise Refusal('artifact: workflow_run.id or head_sha differs from the run')
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
            if z.namelist() != ['measurements.json']:
                raise Refusal('artifact: the zip is not measurements.json alone')
            art = sha256(z.read('measurements.json'))
    return {'schema': RUN_SCHEMA, 'version': 1, 'run_id': run['id'], 'run_attempt': run.get('run_attempt'),
            'head_sha': run.get('head_sha'), 'event': run.get('event'), 'workflow_path': run.get('path'),
            'conclusion': run.get('conclusion'),
            'jobs': sorted(({'name': j.get('name'), 'conclusion': j.get('conclusion')} for j in jobs),
                           key=lambda x: (str(x['name']), str(x['conclusion']))),
            'shard_steps': steps, 'artifact_sha256': art}


def run_record_errors(r):
    keys = {'schema', 'version', 'run_id', 'run_attempt', 'head_sha', 'event', 'workflow_path', 'conclusion', 'jobs',
            'shard_steps', 'artifact_sha256'}
    if not isinstance(r, dict) or set(r) != keys or r['schema'] != RUN_SCHEMA or r['version'] != 1:
        return ['run record: schema']
    errs = []
    if not is_int(r['run_id']) or r['run_id'] <= 0 or not is_int(r['run_attempt']) or not is_hex(r['head_sha'], 40):
        errs.append('run record: ids')
    if not isinstance(r['jobs'], list) or not isinstance(r['shard_steps'], list):
        errs.append('run record: lists')
    if r['artifact_sha256'] is not None and not is_hex(r['artifact_sha256'], 64):
        errs.append('run record: artifact_sha256')
    return errs


def host_void(r, stage):
    """(is host-VOID, refusal code), on the jobs API fields alone (*Stop rule*)."""
    if not [j for j in r['jobs'] if j['name'] == SHARD_JOB]:
        return True, 'shard-absent'
    by = {s['name']: s for s in r['shard_steps']}
    chk = by.get(STEPS['check'])
    if chk is not None and chk['started'] and chk['conclusion'] not in ('success', 'skipped'):
        return False, 'check-started-not-success'
    if chk is None:
        return True, 'check-absent'
    if chk['conclusion'] == 'skipped':
        return True, 'check-skipped'
    if not chk['started']:
        return True, 'check-not-started'
    if stage == 'E' and chk['conclusion'] == 'success':
        rp = by.get(STEPS['replay'])
        if rp is None or rp['conclusion'] == 'skipped' or not rp['started']:
            return True, 'replay-not-run'
    return False, None


def shard_named_ok(r, allow_skipped_upload=False):
    """The shard job present once; its seven named steps present by name, each success; every listed step success
    (synthetic steps tolerated if success; the upload step may be skipped where allowed)."""
    errs = []
    if [j['name'] for j in r['jobs']].count(SHARD_JOB) != 1:
        return ['shard job not present once']
    names = [s['name'] for s in r['shard_steps']]
    for key, nm in STEPS.items():
        if names.count(nm) != 1:
            errs.append('step %r not present once' % nm)
    for s in r['shard_steps']:
        if s['conclusion'] == 'success':
            continue
        if allow_skipped_upload and s['name'] == STEPS['upload'] and s['conclusion'] == 'skipped':
            continue
        errs.append('step %r is %s' % (s['name'], s['conclusion']))
    return errs


def stage_run_errors(r, stage_sha, need_shard):
    errs = run_record_errors(r)
    if errs:
        return errs
    if r['event'] != 'workflow_dispatch':
        errs.append('not a workflow_dispatch run')
    if r['run_attempt'] != 1:
        errs.append('run_attempt is %s' % r['run_attempt'])
    if r['head_sha'] != stage_sha:
        errs.append('head_sha is not the stage commit')
    if r['workflow_path'] != WORKFLOW:
        errs.append('workflow path')
    if r['conclusion'] != 'success':
        errs.append('run conclusion %s' % r['conclusion'])
    if any(j['conclusion'] != 'success' for j in r['jobs']):
        errs.append('a job is not success')
    if need_shard:
        errs += shard_named_ok(r)
    elif [j for j in r['jobs'] if j['name'] == SHARD_JOB]:
        errs.append('the ARP-1-MARC shard is present at F')
    return errs


# =====================================================================================================================
# Approvals and the ordering
# =====================================================================================================================
_STAGES = ('F', 'F retaken', 'S1', 'E', 'retake after host VOID')
_ENTRY_KEYS = ('run_id', 'run_attempt', 'head_sha', 'stage', 'approval_comment_id', 'approval_author',
               'approval_author_association', 'approval_created_at', 'quoted_words')
_RETAKE_KEYS = ('voided_run_id', 'preservation_comment_id', 'preservation_created_at')


def names_stage(words, stage):
    if stage in ('F', 'S1', 'E'):
        return re.search(r'(?<![A-Za-z0-9`])%s(?![A-Za-z0-9])' % stage, words) is not None
    return stage in words


def entry_errors(e, runs_by_id, roles, comments=None, void_records=None):
    """The validity of one approval entry (*Approval entries*). roles: {'F': F, 'S1': S1, 'E': E or None}, the
    commits the stages name; comments: {id: API answer} when captured."""
    errs = []
    if not isinstance(e, dict) or not all(k in e for k in _ENTRY_KEYS) or e['stage'] not in _STAGES:
        return ['entry: keys or stage']
    retake = e['stage'] == 'retake after host VOID'
    if retake and not all(k in e for k in _RETAKE_KEYS):
        return ['entry: retake keys']
    w = e['quoted_words']
    if not isinstance(w, str) or e['head_sha'] not in w or not is_hex(e['head_sha'], 40) or not names_stage(w, e['stage']):
        errs.append('entry %s: quoted words do not name the commit and stage' % e.get('run_id'))
    want = {'F': roles.get('F'), 'F retaken': roles.get('F'), 'S1': roles.get('S1'), 'E': roles.get('E')}
    if e['stage'] in want:
        if want[e['stage']] is None or e['head_sha'] != want[e['stage']]:
            errs.append('entry %s: stage %s does not name the commit of that role' % (e['run_id'], e['stage']))
    else:
        voided = runs_by_id.get(e.get('voided_run_id'))
        if voided is None or voided.get('head_sha') != e['head_sha']:
            errs.append("entry %s: a retake does not name the voided run's commit" % e['run_id'])
    run = runs_by_id.get(e['run_id'])
    if run is None:
        errs.append('entry %s: no such run in the captures' % e['run_id'])
    else:
        if run.get('head_sha') != e['head_sha'] or run.get('run_attempt') != 1 or e['run_attempt'] != 1:
            errs.append('entry %s: head_sha or run_attempt' % e['run_id'])
        if not (e['approval_created_at'] < run.get('created_at', '')):
            errs.append('entry %s: approval not before the run' % e['run_id'])
        if retake and not (e['preservation_created_at'] < e['approval_created_at']):
            errs.append('entry %s: preservation not before the approval' % e['run_id'])
    if (e['approval_author'], e['approval_author_association']) != OWNER:
        errs.append('entry %s: author' % e['run_id'])
    if comments is not None:
        c = comments.get(e['approval_comment_id'])
        if c is None or c.get('user', {}).get('login') != e['approval_author'] \
                or c.get('author_association') != e['approval_author_association'] \
                or c.get('created_at') != e['approval_created_at'] or w not in (c.get('body') or ''):
            errs.append('entry %s: the approval comment does not carry the entry' % e['run_id'])
        if retake:
            pc = comments.get(e['preservation_comment_id'])
            body = (pc or {}).get('body') or ''
            vr = (void_records or {}).get(e['voided_run_id'])
            if pc is None or str(e['voided_run_id']) not in body or pc.get('created_at') != e['preservation_created_at'] \
                    or vr is None or sha256(vr) not in body:
                errs.append('entry %s: preservation comment' % e['run_id'])
    return errs


def _run_rows(runs):
    return [{'run_id': r.get('id'), 'run_attempt': r.get('run_attempt'), 'head_sha': r.get('head_sha'),
             'event': r.get('event'), 'created_at': r.get('created_at'), 'head_branch': r.get('head_branch')}
            for r in runs]


def dispatch_rule_errors(rows, valid_ids, label):
    errs = []
    for r in rows:
        if r['event'] == 'workflow_dispatch':
            if r['run_id'] not in valid_ids:
                errs.append('%s: dispatch run %s has no valid approval entry' % (label, r['run_id']))
            if r['run_attempt'] != 1:
                errs.append('%s: dispatch run %s has run_attempt %s' % (label, r['run_id'], r['run_attempt']))
        elif r['event'] != 'pull_request':
            errs.append('%s: run %s is %s' % (label, r['run_id'], r['event']))
    return errs


def s1_step_state(jobs_pages):
    """(check step conclusion, replay step conclusion) of the shard job in a jobs answer."""
    jobs = _pages(jobs_pages, 'jobs')
    shard = [j for j in jobs if j.get('name') == SHARD_JOB]
    if len(shard) != 1:
        return None, None
    by = {s.get('name'): s.get('conclusion') for s in shard[0].get('steps') or []}
    return by.get(STEPS['check']), by.get(STEPS['replay'])


REF_MARKS = ('round-arp1-marc', 'marc_check')


def _refs(text):
    return any(mk in text for mk in REF_MARKS)


def classify_dev(cwd, sha, pairs):
    """design / none / other for one dev-branch commit, read through git. Every file under .github/ is scanned for a
    reference to the record directory (or to the checker by name): `none` when no file references it; `design` when
    the probes_arp1marc job is the frozen design job, the script pair is listed, and no reference lies outside that
    job; `other` otherwise."""
    if git(cwd, 'cat-file', '-e', sha + '^{commit}') is None:
        return 'unreachable', None, None
    tree = git_rev(cwd, sha + '^{tree}')
    wf = git_show(cwd, sha, WORKFLOW)
    job = extract_job(wf.decode('utf-8', 'replace')) if wf is not None else None
    js = sha256(job.encode()) if job is not None else None
    any_ref = outside = False
    lst = git(cwd, 'ls-tree', '-r', '-z', '--name-only', sha, '.github/') or b''
    for p in [x for x in lst.decode('utf-8', 'replace').split('\0') if x]:
        body = (git_show(cwd, sha, p) or b'').decode('utf-8', 'replace')
        if not _refs(body):
            continue
        any_ref = True
        rest = body.replace(job, '', 1) if (p == WORKFLOW and job is not None) else body
        if _refs(rest):
            outside = True
    if not any_ref:
        return 'none', tree, js
    pair = (git_rev(cwd, '%s:%smarc_check.py' % (sha, RDIR)), git_rev(cwd, '%s:%scontrols.py' % (sha, RDIR)))
    if job == DESIGN_JOB and pair in set(pairs) and not outside:
        return 'design', tree, js
    return 'other', tree, js


def build_order(cwd, f, s1, designation, approvals, runs_bundle, dev_pages, dev_pr, pairs, sources):
    """order.json's content and the ordering's failures."""
    fails = []
    rb = _pages(runs_bundle['round_branch'], 'workflow_runs')
    s1r = _pages(runs_bundle['head_sha'][s1], 'workflow_runs')
    dev = _pages(dev_pages, 'workflow_runs')
    by_id = {r['id']: r for r in rb + s1r}
    comments = {}
    for e in approvals:
        for key in ('comment', 'preservation_comment'):
            if key in e:
                comments[e[key]['id']] = e[key]
    void_records = {int(k): v.encode() for k, v in runs_bundle.get('void_records', {}).items()}
    entries = [{k: e[k] for k in _ENTRY_KEYS + _RETAKE_KEYS if k in e} for e in approvals]
    valid = set()
    for e in entries:
        errs = entry_errors(e, by_id, {'F': f, 'S1': s1}, comments, void_records)
        if errs:
            fails += errs
        else:
            valid.add(e['run_id'])
    ids = [e['approval_comment_id'] for e in entries]
    if len(ids) != len(set(ids)):
        fails.append('an approval comment authorizes two runs')
    dc = designation['comment']
    des = {'comment_id': dc.get('id'), 'author': dc.get('user', {}).get('login'),
           'author_association': dc.get('author_association'), 'created_at': dc.get('created_at'),
           'quoted_words': designation['quoted_words']}
    if f not in des['quoted_words'] or des['quoted_words'] not in (dc.get('body') or '') \
            or (des['author'], des['author_association']) != OWNER:
        fails.append('designation of F: quoted words, comment or author')
    rows_rb, rows_s1 = _run_rows(rb), _run_rows(s1r)
    for r in rows_rb:
        if r['head_branch'] != ROUND_BRANCH:
            fails.append('round-branch capture holds a run on %s' % r['head_branch'])
    fails += dispatch_rule_errors(rows_rb, valid, 'round branch')
    fails += dispatch_rule_errors(rows_s1, valid, 'S1 head_sha')
    nondisp = []
    for r in {x['run_id']: x for x in rows_rb + rows_s1 if x['head_sha'] == s1}.values():
        if r['event'] == 'workflow_dispatch':
            continue
        jp = runs_bundle.get('jobs', {}).get(str(r['run_id']))
        chk, rep = s1_step_state(jp) if jp is not None else (None, None)
        nondisp.append({'run_id': r['run_id'], 'check_step': chk, 'replay_step': rep})
        if chk != 'skipped' or rep != 'skipped':
            fails.append('non-dispatch run %s at S1: check %s, replay %s' % (r['run_id'], chk, rep))
    s1_runs = sorted((x for x in rows_rb + rows_s1 if x['head_sha'] == s1), key=lambda x: x['created_at'])
    first = {'run_id': s1_runs[0]['run_id'], 'created_at': s1_runs[0]['created_at']} if s1_runs else None
    if first is None or not (des['created_at'] < first['created_at']):
        fails.append('the designation of F is not before the first execution run')
    dev_rows = []
    for r in dev:
        cls, tree, js = classify_dev(cwd, r['head_sha'], pairs)
        dev_rows.append({'run_id': r['id'], 'run_attempt': r.get('run_attempt'), 'head_sha': r['head_sha'],
                         'tree': tree, 'event': r.get('event'), 'splice': cls, 'job_sha256': js})
        if r.get('event') != 'pull_request' or cls not in ('design', 'none') or r.get('head_branch') != DEV_BRANCH:
            fails.append('dev run %s: %s, %s' % (r['id'], r.get('event'), cls))
    order = {'schema': ORDER_SCHEMA, 'version': 1, 'designation_f': des,
             'approved_dispatches': sorted(entries, key=lambda e: e['run_id']),
             'round_branch_runs': {'total_count': len(rb), 'runs': [{k: x[k] for k in ('run_id', 'run_attempt',
                                   'head_sha', 'event', 'created_at')} for x in rows_rb]},
             's1_sha_runs': {'total_count': len(s1r), 'runs': [{k: x[k] for k in ('run_id', 'run_attempt',
                             'head_sha', 'event', 'created_at')} for x in rows_s1]},
             'dev_branch': {'name': DEV_BRANCH, 'pr_number': dev_pr, 'total_count': len(dev), 'runs': dev_rows},
             's1_nondispatch_runs': sorted(nondisp, key=lambda x: x['run_id']), 'first_execution_run': first,
             'sources': sources, 'ordering': {'holds': not fails, 'failures': fails}}
    return order, fails


ORDER_KEYS = {'schema', 'version', 'designation_f', 'approved_dispatches', 'round_branch_runs', 's1_sha_runs',
              'dev_branch', 's1_nondispatch_runs', 'first_execution_run', 'sources', 'ordering'}


def order_schema_errors(o):
    if not isinstance(o, dict) or set(o) != ORDER_KEYS or o['schema'] != ORDER_SCHEMA or o['version'] != 1:
        return ['order.json: schema']
    return []


def design_run_errors(raw, pinned):
    """P: design-run.json at its pinned sha256, of its schema, a pull_request run, conclusion success, every job
    success."""
    try:
        r = json.loads(raw)
    except (TypeError, ValueError):
        return ['design-run.json absent or unparseable']
    errs = []
    if sha256(raw) != pinned:
        errs.append('design-run.json not at its pinned sha256')
    errs += run_record_errors(r)
    if errs:
        return errs
    if r['event'] != 'pull_request':
        errs.append('design-run.json: not a pull_request run')
    if r['conclusion'] != 'success' or not r['jobs'] or any(j['conclusion'] != 'success' for j in r['jobs']):
        errs.append('design-run.json: the run or a job is not success')
    return errs


def order_record_errors(o, f, s1):
    """P at E: order.json meets its schema and the recorded data satisfy the ordering's rules."""
    errs = order_schema_errors(o)
    if errs:
        return errs
    if o['ordering'] != {'holds': True, 'failures': []}:
        errs.append('order.json: the ordering does not hold')
    des = o['designation_f']
    if f not in des.get('quoted_words', '') or (des.get('author'), des.get('author_association')) != OWNER:
        errs.append('order.json: designation')
    first = o['first_execution_run']
    if not first or not (des.get('created_at', '~') < first['created_at']):
        errs.append('order.json: designation not before the first execution run')
    runs = o['round_branch_runs']['runs'] + o['s1_sha_runs']['runs']
    by_id = {r['run_id']: r for r in runs}
    valid = {e['run_id'] for e in o['approved_dispatches'] if not entry_errors(e, by_id, {'F': f, 'S1': s1})}
    errs += dispatch_rule_errors(o['round_branch_runs']['runs'], valid, 'order.json round branch')
    errs += dispatch_rule_errors(o['s1_sha_runs']['runs'], valid, 'order.json S1')
    for r in o['s1_nondispatch_runs']:
        if (r['check_step'], r['replay_step']) != ('skipped', 'skipped'):
            errs.append('order.json: non-dispatch run at S1 computed')
    if {r['run_id'] for r in runs if r['head_sha'] == s1 and r['event'] != 'workflow_dispatch'} \
            != {r['run_id'] for r in o['s1_nondispatch_runs']}:
        errs.append('order.json: S1 non-dispatch runs not all classified')
    dj = sha256(DESIGN_JOB.encode())
    for r in o['dev_branch']['runs']:
        if r['event'] != 'pull_request' or r['splice'] not in ('design', 'none') \
                or (r['splice'] == 'design' and r['job_sha256'] != dj):
            errs.append('order.json: dev run %s' % r['run_id'])
    if o['dev_branch']['name'] != DEV_BRANCH:
        errs.append('order.json: dev branch name')
    return errs


# =====================================================================================================================
# check: T, G, R, B, W, DS, X, V, P
# =====================================================================================================================
def record_files(cwd, commit):
    out = git(cwd, 'ls-tree', '-r', '--name-only', commit, RDIR)
    return set(p[len(RDIR):] for p in out.decode().split('\n') if p) if out is not None else set()


def changed(cwd, a, b, paths=()):
    out = git(cwd, 'diff-tree', '-r', '--no-renames', '--name-status', a, b, '--', *paths)
    res = []
    for line in (out or b'').decode().split('\n'):
        if line:
            st, p = line.split('\t', 1)
            res.append((st, p))
    return res


def check_commit(cwd, commit, f, stage=None, snapshot=SNAPSHOT, inputs=None):
    """{control: [codes]} for the commit under check."""
    inputs = INPUTS if inputs is None else inputs
    res = {c: [] for c in ('T', 'G', 'R', 'B', 'W', 'DS', 'X', 'V', 'P')}
    pre_f = git_show(cwd, f, RDIR + 'preregistration.md')
    if pre_f is None:
        res['T'].append('no preregistration at F')
        return res
    pre_text = pre_f.decode('utf-8')
    fl = prereg_fields(pre_text)
    d = fl['D']
    if d is None:
        res['P'].append('D not filled at F')
        return res
    files = record_files(cwd, commit)
    if stage is None:
        stage = 'S1'
        if 'result.md' in files:
            stage = 'W' if git_show(cwd, commit, WORKFLOW) == git_show(cwd, f, WORKFLOW) else 'E'
    # a halt before S1 exists: the commit in W's place is a single-parent child of F (S12)
    before_s1 = stage == 'W' and git_rev(cwd, commit + '~1') == f
    # T
    rc, out = run_p6(cwd, d, f)
    if rc != 0:
        res['T'].append('precondition 6 command: %s' % out[-200:])
    if git(cwd, 'merge-base', '--is-ancestor', f, commit, ok=(0,)) is None:
        res['T'].append('F is not an ancestor of the commit')
    chain = (git(cwd, 'rev-list', commit, '^' + d) or b'').decode().split()
    cs = set(chain)
    for c in chain:
        ps = (git(cwd, 'rev-list', '--parents', '-n', '1', c) or b'').decode().split()[1:]
        if len(ps) != 1 or (ps[0] not in cs and ps[0] != d):
            res['T'].append('D..commit is not one chain of single-parent commits')
            break
    if git_show(cwd, commit, RDIR + 'preregistration.md') != pre_f:
        res['T'].append('the preregistration differs from F')
    # G
    for st, p in changed(cwd, f, commit):
        if p == WORKFLOW and st == 'M' and stage in ('S1', 'E'):
            continue
        if p.startswith(RDIR) and st in ('A', 'M'):
            continue
        res['G'].append('%s %s' % (st, p))
    # R
    cp = {p for p in record_files(cwd, f)}
    want = set(cp) | set(S1_SET)
    if stage == 'E':
        want |= set(E_SET)
    if before_s1:
        want = set(cp) | {'result.md'} | ({'evidence/order.json'} & files)
    elif stage == 'W':
        extra = files - want
        if 'result.md' not in extra or 'evidence/order.json' not in extra or not extra <= set(W_OPTIONAL) | {
                'result.md', 'evidence/order.json'} \
                or not ({'evidence/s1-run/results.json', 'evidence/void-run.json'} & extra):
            res['R'].append('W record set %s' % sorted(extra))
        want = files
    if files != want:
        res['R'].append('record files %s' % sorted(files ^ want))
    if stage in ('S1', 'E') and ((MEAS in files) != ('result.md' in files)):
        res['R'].append('measurements.json and result.md not together')
    if any(p.startswith('amendments/') for p in files - cp):
        res['R'].append('amendments after F')
    # B
    marc = git_show(cwd, commit, RDIR + 'marc_check.py')
    ctl = git_show(cwd, commit, RDIR + 'controls.py')
    if before_s1:
        pass                              # no script exists before S1; R refuses any that appears
    elif marc is None or ctl is None:
        res['B'].append('a script is missing')
    else:
        if git_blob(marc) != fl['marc_blob'] or sha256(marc) != fl['marc_sha256']:
            res['B'].append('marc_check.py is not at its pinned blob')
        if git_blob(ctl) != fl['controls_blob'] or sha256(ctl) != fl['controls_sha256']:
            res['B'].append('controls.py is not at its pinned blob')
        res['B'] += static_marc(marc.decode('utf-8'))
        res['B'] += static_controls(ctl.decode('utf-8'), frozen_p6_from(pre_text))
    # W
    wf = git_show(cwd, commit, WORKFLOW)
    if stage == 'W':
        if wf != git_show(cwd, f, WORKFLOW):
            res['W'].append("verify.yml is not F's")
    else:
        dwf = git_show(cwd, d, WORKFLOW)
        try:
            exp = splice(dwf.decode('utf-8')).encode()
        except (ValueError, AttributeError):
            exp = None
        if wf is None or wf != exp:
            res['W'].append("verify.yml is not D's with exactly the frozen splice")
    # DS
    if changed(cwd, snapshot, d, SOURCE_DIRS):
        res['DS'].append('a source directory changed from the snapshot to D')
    for st, p in changed(cwd, d, commit, SOURCE_DIRS):
        if p != WORKFLOW:
            res['DS'].append('%s changed from D' % p)
    for p, b in inputs.items():
        if git_rev(cwd, '%s:%s' % (commit, p)) != b:
            res['DS'].append('input %s not at its blob' % p)
    # P
    if pending_fields(pre_text):
        res['P'].append('PENDING at F, lines %s' % pending_fields(pre_text)[:5])
    for c in (git(cwd, 'rev-list', f, '^' + d) or b'').decode().split():
        t = git_show(cwd, c, RDIR + 'preregistration.md')
        if t is None or not branches_line_ok(t.decode('utf-8')):
            res['P'].append('the branches line in %s' % c[:12])
    if not blocks_ok(pre_text):
        res['P'].append('the blocks at F')
    if before_s1:                         # P's S1 evidence is exempt; only order.json, if present, is checked
        od = git_show(cwd, commit, RDIR + 'evidence/order.json')
        if od is not None:
            try:
                res['P'] += order_schema_errors(json.loads(od))
            except ValueError:
                res['P'].append('order.json unparseable')
    else:
        res['P'] += design_run_errors(git_show(cwd, commit, RDIR + 'evidence/design-run.json'), fl['design_run_sha256'])
        fr = git_show(cwd, commit, RDIR + 'evidence/f-run/results.json')
        try:
            fr_errs = stage_run_errors(json.loads(fr), f, need_shard=False) if fr is not None else ['absent']
        except ValueError:
            fr_errs = ['unparseable']
        if fr_errs:
            res['P'].append('f-run/results.json: %s' % fr_errs[0])
    meas = git_show(cwd, commit, RDIR + MEAS)
    s1run = None
    if stage == 'E':
        s1c = git_rev(cwd, commit + '~1')
        raw = git_show(cwd, commit, RDIR + 'evidence/s1-run/results.json')
        try:
            s1run = json.loads(raw)
            s1_errs = stage_run_errors(s1run, s1c, need_shard=True)
            if meas is None or s1run.get('artifact_sha256') != sha256(meas):
                s1_errs.append('artifact_sha256 differs from the committed measurements')
        except (TypeError, ValueError):
            s1_errs = ['absent or unparseable']
        if s1_errs:
            res['P'].append('s1-run/results.json: %s' % s1_errs[0])
        try:
            od = json.loads(git_show(cwd, commit, RDIR + 'evidence/order.json'))
            res['P'] += order_record_errors(od, f, s1c)
        except (TypeError, ValueError):
            res['P'].append('order.json absent or unparseable')
    # X and V
    if stage == 'E':
        try:
            m = json.loads(meas)
        except (TypeError, ValueError):
            m = None
        label, reasons, _ = decide(m)
        if m is None or schema_errors(m):
            res['X'].append('measurements schema')
        elif m['complete'] is not True:
            res['X'].append('measurements incomplete')
        elif any("flags disagree" in r for r in reasons):
            res['X'].append("the checker's flags disagree with decide")
        note = git_show(cwd, commit, RDIR + 'result.md')
        regen, _ = make_note(m, s1run, d, f)
        if note is None or note.decode('utf-8') != regen:
            res['V'].append('result.md is not the regeneration')
        if note is not None and s4_hits(note.decode('utf-8'), strip_frozen=True):
            res['V'].append('S4: %s' % s4_hits(note.decode('utf-8'), strip_frozen=True))
    if stage == 'W':
        note = git_show(cwd, commit, RDIR + 'result.md') or b''
        n = note.decode('utf-8')
        if (TOKEN_LINE % TOKENS['VOID']) not in n.split('\n') or s4_hits(n, strip_frozen=True):
            res['V'].append('W note: VOID token line or S4')
    return res


def frozen_p6_from(text):
    m = re.search(r'python3 -I -c "(.*)" <D> <candidate F>', text)
    return m.group(1) if m else None


# =====================================================================================================================
# verdict and plane
# =====================================================================================================================
def verdict(cwd, e, f, run, jobs_pages, approvals, bundle, s1=None, snapshot=SNAPSHOT, inputs=None):
    """(token or None, reasons)."""
    reasons = []
    res = check_commit(cwd, e, f, stage='E', snapshot=snapshot, inputs=inputs)
    for c, codes in res.items():
        reasons += ['check %s: %s' % (c, x) for x in codes]
    s1 = s1 or git_rev(cwd, e + '~1')
    try:
        r = derive_run(run, jobs_pages)
    except Refusal as ex:
        return None, reasons + ['E run: %s' % ex]
    reasons += ['E run: %s' % x for x in stage_run_errors(r, e, need_shard=True)]
    hv, code = host_void(r, 'E')
    if hv:
        reasons.append('E run is host-VOID (%s)' % code)
    try:
        rb = _pages(bundle['round_branch'], 'workflow_runs')
        hs = {k: _pages(v, 'workflow_runs') for k, v in bundle['head_sha'].items()}
    except (Refusal, KeyError) as ex:
        return None, reasons + ['captures: %s' % ex]
    if set(hs) != {s1, e}:
        reasons.append('captures: head_sha captures for S1 and E required')
    allruns = {x['id']: x for x in rb + [y for v in hs.values() for y in v]}
    roles = {'F': f, 'S1': s1, 'E': e}
    try:
        order = json.loads(git_show(cwd, e, RDIR + 'evidence/order.json'))
    except (TypeError, ValueError):
        return None, reasons + ['order.json unreadable']
    comments = {}
    for a in approvals:
        for key in ('comment', 'preservation_comment'):
            if key in a:
                comments[a[key]['id']] = a[key]
    valid = set()
    entries = [{k: a[k] for k in _ENTRY_KEYS + _RETAKE_KEYS if k in a} for a in approvals]
    voids = {int(k): v.encode() for k, v in bundle.get('void_records', {}).items()}
    for a in entries:
        errs = entry_errors(a, allruns, roles, comments, voids)
        reasons += errs
        if not errs:
            valid.add(a['run_id'])
    for a in order['approved_dispatches']:
        if a['run_id'] in allruns and not entry_errors(a, allruns, roles):
            valid.add(a['run_id'])
    ids = [a['approval_comment_id'] for a in entries + order['approved_dispatches']]
    if len(ids) != len(set(ids)):
        reasons.append('an approval comment authorizes two runs')
    if not any(a['run_id'] == run['id'] and a['stage'] == 'E' and a['run_id'] in valid for a in entries):
        reasons.append("E's run has no valid approval entry with stage E")
    rows = _run_rows(list(allruns.values()))
    reasons += dispatch_rule_errors(rows, valid, 'fresh capture')
    for x in rows:
        if x['head_sha'] == s1 and x['event'] != 'workflow_dispatch':
            jp = bundle.get('jobs', {}).get(str(x['run_id']))
            st = s1_step_state(jp) if jp is not None else (None, None)
            if st != ('skipped', 'skipped'):
                reasons.append('non-dispatch run %s at S1: %s' % (x['run_id'], st))
    meas = git_show(cwd, e, RDIR + MEAS)
    s1run = json.loads(git_show(cwd, e, RDIR + 'evidence/s1-run/results.json') or b'null')
    try:
        m = json.loads(meas)
    except (TypeError, ValueError):
        m = None
    exit_status = 0 if check_conclusion(s1run) == 'success' else 1
    label, why, _ = decide(m, exit_status)
    note = (git_show(cwd, e, RDIR + 'result.md') or b'').decode('utf-8')
    if (TOKEN_LINE % TOKENS[label]) not in note.split('\n'):
        reasons.append("result.md's token line differs from the token")
    if label == 'VOID':
        reasons.append('decide: VOID (%s)' % '; '.join(why))
    if reasons:
        return None, reasons
    return TOKENS[label], why


def plane(cwd, f, dev_pages, lines=None):
    errs = []
    raw = git_show(cwd, f, RDIR + 'preregistration.md')
    if raw is None:
        return ['no preregistration at the candidate F']
    text = raw.decode('utf-8')
    fl = prereg_fields(text)
    if pending_fields(text):
        errs.append('PENDING at lines %s' % pending_fields(text))
    if fl['D'] is None:
        return errs + ['D not filled']
    for c in (git(cwd, 'rev-list', f, '^' + fl['D']) or b'').decode().split():
        t = git_show(cwd, c, RDIR + 'preregistration.md')
        if t is None or not branches_line_ok(t.decode('utf-8')):
            errs.append('the branches line in %s' % c)
    if not blocks_ok(text):
        errs.append('the blocks')
    try:
        dev = _pages(dev_pages, 'workflow_runs')
    except Refusal as ex:
        return errs + [str(ex)]
    for r in dev:
        cls, _, _ = classify_dev(cwd, r['head_sha'], fl['design_pairs'])
        if lines is not None:
            lines.append('dev run %s at %s: %s' % (r['id'], r['head_sha'], cls))
        if cls not in ('design', 'none') or r.get('event') != 'pull_request' or r.get('head_branch') != DEV_BRANCH:
            errs.append('dev run %s: %s' % (r['id'], cls))
    return errs


# =====================================================================================================================
# replay
# =====================================================================================================================
def replay(path, here=None):
    here = here or os.path.dirname(os.path.abspath(__file__))
    cm = os.path.join(here, MEAS)
    rm = os.path.join(here, 'result.md')
    has_m, has_r = os.path.exists(cm), os.path.exists(rm)
    if not has_m and not has_r:
        print('replay: no committed measurements')
        return 0
    if has_m and has_r:
        with open(path, 'rb') as a, open(cm, 'rb') as b:
            if a.read() == b.read():
                print('replay: the fresh computation equals the committed measurements')
                return 0
        print('replay: MISMATCH')
        return 1
    print('replay: measurements.json and result.md not together')
    return 1


# =====================================================================================================================
# --self-test. It launches no checker: every measurement record below is synthetic, built here, and no variant is
# computed. Temporary repositories live in a tempfile directory; the only write-mode opens are here.
# =====================================================================================================================
_ST_ENV = {'GIT_AUTHOR_NAME': 'self-test', 'GIT_AUTHOR_EMAIL': 'self-test@invalid',
           'GIT_COMMITTER_NAME': 'self-test', 'GIT_COMMITTER_EMAIL': 'self-test@invalid',
           'GIT_AUTHOR_DATE': '2026-01-01T00:00:00Z', 'GIT_COMMITTER_DATE': '2026-01-01T00:00:00Z',
           'GIT_CONFIG_GLOBAL': os.devnull}
_ST_WITNESS = {'pattern': 'uvv', 'schedule': [None, [1, 'u'], None, None, None], 't': 3, 'window': [0, 2],
               'code': 3, 'functional': 'u_0+v_0', 'uses_t_eq_T': False}


def _st_size(key, n):
    """A synthetic, all-green size record (self-test data only; not a result of any computation)."""
    s = {'D': {'cases': CASES, 'exposing_V': n, 'exposing_V_no_reg_at_T': n // 2, 'exposing_V_reg_in_1_to_Tm1': n // 4,
               'witness': dict(_ST_WITNESS) if n else None, 'nv_cases': 100, 'coupling_cases': 50,
               'step_is_ring_violations': 0, 'records_kept_violations': 0, 'min_rank_I': 3, 'knowledge_injections': 0},
         'I': {'cases': CASES, 'exposing_V': 0, 'exposing_active': 0, 'nonisotropic': 0, 'nv_cases': 90,
               'coupling_cases': 0},
         'd_i_diff_outside_archived': 0, 'case_list_sha256': {'D': 'ab' * 32, 'I': 'ab' * 32},
         'supp_x': {'cases': CASES, 'exposing_V': 10},
         'supp_f': {'law': {'pair': '(u_1, v_0)', 'P': {'00': '3/8', '01': '1/8', '10': '1/8', '11': '3/8'},
                            'others': 'uniform, independent'}, 'cond_v0_0': '3/4', 'cond_v0_1': '1/4',
                    'span_determined': False},
         'c9': {'cases': CASES, 'exposing_V': 20, 'exposing_at_registration': 15},
         'plant': {'D': {'empty_t0': True, 'exposing_V': CASES}, 'I': {'empty_t0': True, 'exposing_V': CASES}},
         'xb': {'checked_cases': {'D': CASES, 'I': CASES, 'C9': CASES},
                'checked_times': {'D': 5 * CASES, 'I': 5 * CASES, 'C9': 5 * CASES},
                'exposing_V': {'D': n, 'I': 0, 'C9': 20}, 'mismatches': 0, 'exposure_mismatches': 0},
         'step': {'violations': 0}, 'horizon': {'T_le_H': True, 'radius_violations': 0}}
    if key == '4':
        s['xb']['all1'] = {'checked_cases': {'D': CASES, 'I': CASES}, 'mismatches': 0, 'exposure_mismatches': 0}
    s['flags'] = green_flags(s, key)
    return s


def _st_meas(n4, n6):
    return {'schema': MEAS_SCHEMA, 'version': 1, 'parameters': json.loads(json.dumps(PARAMETERS)), 'complete': True,
            '4': _st_size('4', n4), '6': _st_size('6', n6)}


_ST_FLIPS = {
    'I.exposing_V': 1, 'I.exposing_active': 1, 'I.nonisotropic': 1, 'D.nv_cases': 0, 'I.nv_cases': 0,
    'supp_x.exposing_V': 0, 'supp_f.cond_v0_0': '1/2', 'supp_f.cond_v0_1': '1/2', 'supp_f.span_determined': True,
    'c9.exposing_V': 0, 'D.step_is_ring_violations': 1, 'd_i_diff_outside_archived': 1, 'D.coupling_cases': 0,
    'I.coupling_cases': 1, 'case_list_sha256.D': 'cd' * 32, 'case_list_sha256.I': 'cd' * 32,
    'D.records_kept_violations': 1, 'D.min_rank_I': 2, 'D.knowledge_injections': 1,
    'xb.checked_cases.D': CASES - 1, 'xb.checked_cases.I': CASES - 1, 'xb.checked_cases.C9': CASES - 1,
    'xb.checked_times.D': 5 * CASES - 1, 'xb.checked_times.I': 5 * CASES - 1, 'xb.checked_times.C9': 5 * CASES - 1,
    'xb.mismatches': 1, 'xb.exposure_mismatches': 1, 'xb.exposing_V.D': 7777, 'xb.exposing_V.I': 1,
    'xb.exposing_V.C9': 21, 'xb.all1.checked_cases.D': 1, 'xb.all1.checked_cases.I': 1, 'xb.all1.mismatches': 1,
    'xb.all1.exposure_mismatches': 1, 'plant.D.empty_t0': False, 'plant.I.empty_t0': False,
    'plant.D.exposing_V': 0, 'plant.I.exposing_V': 0, 'step.violations': 1, 'horizon.T_le_H': False,
    'horizon.radius_violations': 1}


def _st_set(obj, path, value):
    parts = path.split('.')
    for p in parts[:-1]:
        obj = obj[p]
    obj[parts[-1]] = value


def _st_leaves(obj, prefix=()):
    if isinstance(obj, dict) and obj:
        for k, v in obj.items():
            yield from _st_leaves(v, prefix + (k,))
    else:
        yield prefix


def _st_jobs(run_id, shard=True, step_overrides=None, drop=(), extra_jobs=('Lean kernel check', 'Numerical probes')):
    """A realistic jobs-API answer: synthetic steps around the seven named ones."""
    names = (['Set up job', STEPS['checkout'], STEPS['setup'], STEPS['check'], STEPS['upload'], STEPS['replay'],
              STEPS['selftest'], STEPS['mutation'], 'Post Run actions/setup-python@v5', 'Post Run actions/checkout@v4',
              'Complete job'])
    jobs = []
    for i, nm in enumerate(extra_jobs):
        jobs.append({'id': run_id * 10 + i, 'run_id': run_id, 'run_attempt': 1, 'name': nm, 'status': 'completed',
                     'conclusion': 'success', 'steps': [{'name': 'Set up job', 'status': 'completed',
                                                        'conclusion': 'success', 'number': 1,
                                                        'started_at': '2026-11-08T00:00:00Z'}]})
    if shard:
        steps = []
        for k, nm in enumerate(names):
            if nm in drop:
                continue
            st = {'name': nm, 'status': 'completed', 'conclusion': 'success', 'number': k + 1,
                  'started_at': '2026-11-08T00:00:01Z', 'completed_at': '2026-11-08T00:00:02Z'}
            st.update((step_overrides or {}).get(nm, {}))
            steps.append(st)
        jobs.append({'id': run_id * 10 + 9, 'run_id': run_id, 'run_attempt': 1, 'name': SHARD_JOB,
                     'status': 'completed', 'conclusion': 'success', 'steps': steps})
    return {'total_count': len(jobs), 'jobs': jobs}


def _st_run(rid, sha, event, created, attempt=1, branch=ROUND_BRANCH):
    return {'id': rid, 'run_attempt': attempt, 'head_sha': sha, 'event': event, 'path': WORKFLOW,
            'conclusion': 'success', 'status': 'completed', 'created_at': created, 'head_branch': branch,
            'repository': {'full_name': REPO_FULL}}


def _st_page(runs):
    return {'total_count': len(runs), 'workflow_runs': runs}


def _st_comment(cid, body, created):
    return {'id': cid, 'user': {'login': 'amaybaum'}, 'author_association': 'OWNER', 'created_at': created,
            'body': body}


def _st_entry(rid, sha, stage, cid, created, words=None):
    words = words or 'Owner: approved, dispatch of %s at %s.' % (stage, sha)
    return {'run_id': rid, 'run_attempt': 1, 'head_sha': sha, 'stage': stage, 'approval_comment_id': cid,
            'approval_author': 'amaybaum', 'approval_author_association': 'OWNER', 'approval_created_at': created,
            'quoted_words': words, 'comment': _st_comment(cid, 'Recording the owner\'s words: "%s"' % words, created)}


def _st_write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as fh:
        fh.write(data)


def _st_git(cwd, *args):
    out = git(cwd, *args, env=_ST_ENV)
    if out is None:
        raise Refusal('self-test git %s failed' % (args,))
    return out.decode().strip()


def _st_commit(cwd, parent, files, msg):
    """files: {path: bytes, or None to delete}. Returns the new commit id."""
    if parent:
        _st_git(cwd, 'checkout', '-q', '--detach', parent)
    for p, b in files.items():
        if b is None:
            _st_git(cwd, 'rm', '-q', '--', p)
        else:
            _st_write(os.path.join(cwd, p), b)
            _st_git(cwd, 'add', '--', p)
    _st_git(cwd, 'commit', '-q', '--allow-empty', '-m', msg)
    return _st_git(cwd, 'rev-parse', 'HEAD')


_ST_D_WORKFLOW = '''name: verify
on:
  pull_request:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  probes_foundations:
    name: Numerical probes / foundations
    runs-on: ubuntu-latest
    steps:
      - run: echo foundations

  probes:
    name: Numerical probes
    needs: [probes_a42_exclusion, probes_foundations]
    if: ${{ always() }}
    runs-on: ubuntu-latest
    steps:
      - name: Require every probe shard
        env:
          FOUNDATIONS_RESULT: ${{ needs.probes_foundations.result }}
        run: |
          echo "foundations=${FOUNDATIONS_RESULT}"
          test "${FOUNDATIONS_RESULT}" = success
'''


def _st_fill(prereg, d, marc, ctl, design_sha):
    t = prereg
    mb, cb = git_blob(marc), git_blob(ctl)
    t = re.sub(r'\*\*`D`\*\* = (?:PENDING|`?[0-9a-f]{40}`?)', '**`D`** = `%s`' % d, t, count=1)
    t = re.sub(r'(\*\*`marc_check\.py`\*\* \(record directory; )blob [^,]+, sha256 [^)]+\)',
               lambda m_: m_.group(1) + 'blob `%s`, sha256 `%s`)' % (mb, sha256(marc)), t, count=1)
    t = re.sub(r'(\*\*`controls\.py`\*\* \(record directory; )blob [^,]+, sha256 [^)]+\)',
               lambda m_: m_.group(1) + 'blob `%s`, sha256 `%s`)' % (cb, sha256(ctl)), t, count=1)
    t = re.sub(r'whose sha256 is pinned here: (?:PENDING|`?[0-9a-f]{64}`?)',
               'whose sha256 is pinned here: `%s`' % design_sha, t, count=1)
    t = re.sub(r'The design PR number: (?:PENDING|#?\d+)', 'The design PR number: #7', t, count=1)
    t = re.sub(r'The list: [^\n]*', 'The list: (`%s`, `%s`).' % (mb, cb), t, count=1)
    t = re.sub(r'(?<!`)\bPENDING\b(?!`)', 'filled', t)
    return t


def _st_find(rel):
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(10):
        p = os.path.join(d, rel)
        if os.path.exists(p):
            return p
        d = os.path.dirname(d)
    return None


def _st_round(tmp, here, prereg, check):
    """A synthetic round in a temporary repository: D, F, S1, E, dev commits; the controls on it and its mutations."""
    repo = os.path.join(tmp, 'repo')
    os.makedirs(repo)
    _st_git(repo, 'init', '-q')
    ver = _st_find('tools/v3_verifier.py')
    if ver is None:
        check('tools/v3_verifier.py found for control T', False)
        return
    with open(ver, 'rb') as fh:
        verifier = fh.read()
    with open(os.path.join(here, 'marc_check.py'), 'rb') as fh:
        marc = fh.read()
    with open(os.path.abspath(__file__), 'rb') as fh:
        ctl = fh.read()
    inputs = {p: ('synthetic input %s\n' % p).encode() for p in INPUTS}
    in_blobs = {p: git_blob(b) for p, b in inputs.items()}
    base = {'tools/v3_verifier.py': verifier, WORKFLOW: _ST_D_WORKFLOW.encode()}
    base.update(inputs)
    snap = _st_commit(repo, None, base, 'snapshot')
    d = _st_commit(repo, snap, {'README.md': b'D\n'}, 'D')
    # the dev branch: a design commit, a commit without the splice, and two that are neither
    dwf = _ST_D_WORKFLOW
    pre_tmp = _st_fill(prereg, d, marc, ctl, '0' * 64)
    dev_tree = {RDIR + 'preregistration.md': pre_tmp.encode(), RDIR + 'marc_check.py': marc,
                RDIR + 'controls.py': ctl, WORKFLOW: splice(dwf, DESIGN_JOB).encode()}
    dv1 = _st_commit(repo, d, dev_tree, 'dev design')
    dv0 = _st_commit(repo, d, {'notes.txt': b'dev scratch\n'}, 'dev none')
    dv2 = _st_commit(repo, dv1, {WORKFLOW: splice(dwf).encode()}, 'dev frozen job, not the design job')
    dv3 = _st_commit(repo, dv1, {RDIR + 'marc_check.py': marc + b'# changed\n'}, 'dev unlisted pair')
    devrun = _st_run(8001, dv1, 'pull_request', '2026-11-08T15:00:00Z', branch=DEV_BRANCH)
    design = canonical(derive_run(devrun, [_st_jobs(8001, step_overrides={STEPS['upload']: {}})])).encode()
    pre = _st_fill(prereg, d, marc, ctl, sha256(design))
    f = _st_commit(repo, d, {RDIR + 'preregistration.md': pre.encode()}, 'F')
    frun = _st_run(9001, f, 'workflow_dispatch', '2026-11-08T16:55:00Z')
    fres = canonical(derive_run(frun, [_st_jobs(9001, shard=False)])).encode()
    s1_files = {RDIR + 'marc_check.py': marc, RDIR + 'controls.py': ctl, RDIR + 'evidence/design-run.json': design,
                RDIR + 'evidence/f-run/results.json': fres, WORKFLOW: splice(dwf).encode()}
    s1 = _st_commit(repo, f, s1_files, 'S1')
    res = check_commit(repo, s1, f, 'S1', snapshot=snap, inputs=in_blobs)
    check('synthetic round: check S1 passes every control', not any(res.values()), str({k: v for k, v in res.items() if v}))
    # E: the S1 dispatch's artifact, its derived run, order.json, the note
    meas = canonical(_st_meas(0, 0)).encode()
    zbuf = io.BytesIO()
    with zipfile.ZipFile(zbuf, 'w') as z:
        z.writestr('measurements.json', meas)
    zb = zbuf.getvalue()
    arts = {'total_count': 1, 'artifacts': [{'id': 1, 'name': 'arp1-marc-measurements', 'digest': 'sha256:' + sha256(zb),
                                             'workflow_run': {'id': 9003, 'head_sha': s1}}]}
    s1run_api = _st_run(9003, s1, 'workflow_dispatch', '2026-11-08T17:15:00Z')
    s1rec = derive_run(s1run_api, [_st_jobs(9003)], arts, zb)
    check('derive-run: artifact_sha256 is the sha256 of the extracted measurements', s1rec['artifact_sha256'] == sha256(meas))
    for name, mut in (('digest', lambda a: a['artifacts'][0].__setitem__('digest', 'sha256:' + '0' * 64)),
                      ('workflow_run.id', lambda a: a['artifacts'][0]['workflow_run'].__setitem__('id', 1)),
                      ('head_sha', lambda a: a['artifacts'][0]['workflow_run'].__setitem__('head_sha', d))):
        a2 = json.loads(json.dumps(arts))
        mut(a2)
        try:
            derive_run(s1run_api, [_st_jobs(9003)], a2, zb)
            check('derive-run refuses an artifact with a wrong %s' % name, False)
        except Refusal:
            check('derive-run refuses an artifact with a wrong %s' % name, True)
    s1pr = _st_run(9002, s1, 'pull_request', '2026-11-08T17:05:00Z')
    skipped = {STEPS['check']: {'conclusion': 'skipped', 'started_at': None},
               STEPS['replay']: {'conclusion': 'skipped', 'started_at': None},
               STEPS['upload']: {'conclusion': 'skipped', 'started_at': None}}
    des = {'comment': _st_comment(501, 'Owner designation: "I designate F = %s."' % f, '2026-11-08T17:00:00Z'),
           'quoted_words': 'I designate F = %s.' % f}
    apps = [_st_entry(9001, f, 'F', 601, '2026-11-08T16:50:00Z'), _st_entry(9003, s1, 'S1', 602, '2026-11-08T17:10:00Z')]
    bundle = {'round_branch': [_st_page([frun, s1pr, s1run_api])], 'head_sha': {s1: [_st_page([s1pr, s1run_api])]},
              'jobs': {'9002': [_st_jobs(9002, step_overrides=skipped)]}}
    devp = [_st_page([devrun, _st_run(8002, dv0, 'pull_request', '2026-11-08T15:10:00Z', branch=DEV_BRANCH)])]
    pairs = prereg_fields(pre)['design_pairs']
    order, fails = build_order(repo, f, s1, des, apps, bundle, devp, 7, pairs, {'synthetic': True})
    check('order: the ordering holds on the synthetic captures', not fails, '; '.join(fails))
    pl = plane(repo, f, devp)
    check('plane: OK on the synthetic candidate F (dev runs design and none)', not pl, '; '.join(pl))
    s1rec_b = canonical(s1rec).encode()
    note, label = make_note(json.loads(meas), s1rec, d, f)
    e_files = {RDIR + MEAS: meas, RDIR + 'evidence/s1-run/results.json': s1rec_b,
               RDIR + 'evidence/order.json': canonical(order).encode(), RDIR + 'result.md': note.encode()}
    e = _st_commit(repo, s1, e_files, 'E')
    res = check_commit(repo, e, f, 'E', snapshot=snap, inputs=in_blobs)
    check('synthetic round: check E passes every control (label %s)' % label, not any(res.values()),
          str({k: v for k, v in res.items() if v}))
    erun = _st_run(9005, e, 'workflow_dispatch', '2026-11-08T18:10:00Z')
    epr = _st_run(9004, e, 'pull_request', '2026-11-08T18:00:00Z')
    eapps = [_st_entry(9005, e, 'E', 603, '2026-11-08T18:05:00Z')]
    vb = {'round_branch': [_st_page([frun, s1pr, s1run_api, epr, erun])],
          'head_sha': {s1: [_st_page([s1pr, s1run_api])], e: [_st_page([epr, erun])]},
          'jobs': {'9002': [_st_jobs(9002, step_overrides=skipped)]}}
    def vg(en, run=erun, jobs=None, ap=eapps, b=vb):
        return _st_verdict(repo, en, f, run, jobs or [_st_jobs(run['id'])], ap, b, s1, snap, in_blobs)
    tok, why = vg(e)
    check('verdict: VERDICT %s on the synthetic round' % tok, tok == TOKENS['SURVIVAL'], '; '.join(why))
    # --- mutations of the synthetic round --------------------------------------------------------------------------
    def fails_with(name, commit, stage, control):
        r = check_commit(repo, commit, f, stage, snapshot=snap, inputs=in_blobs)
        check('mutation: %s fails %s' % (name, control), bool(r[control]), str(r[control]))
    m1 = _st_commit(repo, f, dict(s1_files, **{RDIR + MEAS: meas}), 'S1 carrying measurements')
    fails_with('measurements committed at S1', m1, 'S1', 'R')
    noif = splice(dwf, FROZEN_JOB.replace(_CHECK_IF, '', 1)).encode()
    m2 = _st_commit(repo, f, dict(s1_files, **{WORKFLOW: noif}), "S1 without the check step's if:")
    fails_with("the check step's if: removed", m2, 'S1', 'W')
    m3 = _st_commit(repo, s1, {'papers/Main.md': b'edited\n'}, 'a paper edited')
    fails_with('a paper edited', m3, 'S1', 'G')
    m4 = _st_commit(repo, s1, {RDIR + 'preregistration.md': pre.encode() + b'\n'}, 'preregistration changed after F')
    fails_with('the preregistration changed after F', m4, 'S1', 'T')
    m5 = _st_commit(repo, s1, {list(INPUTS)[0]: b'changed\n'}, 'an input changed')
    fails_with('an input record changed', m5, 'S1', 'DS')
    m6 = _st_commit(repo, s1, {RDIR + 'marc_check.py': marc + b'# x\n'}, 'checker changed')
    fails_with('the checker not at its pinned blob', m6, 'S1', 'B')
    m7 = _st_commit(repo, s1, {RDIR + 'result.md': note.encode()}, 'note without measurements')
    fails_with('result.md without measurements', m7, 'S1', 'R')
    m8 = _st_commit(repo, s1, dict(e_files, **{RDIR + 'result.md': note.replace('PASS', 'FAIL', 1).encode()}), 'E bad note')
    fails_with('result.md not the regeneration', m8, 'E', 'V')
    # ordering rule: a non-dispatch run at S1 that computed; dev runs that are not design or none; attempts
    b2 = json.loads(json.dumps(bundle))
    b2['jobs']['9002'] = [_st_jobs(9002)]
    _, fl2 = build_order(repo, f, s1, des, apps, b2, devp, 7, pairs, {})
    check('order rule: a non-dispatch run at S1 whose check step is success fails', bool(fl2), '; '.join(fl2[:1]))
    for nm, sha in (('the frozen job (not the design job)', dv2), ('a script pair outside the frozen list', dv3)):
        dp = [_st_page([devrun, _st_run(8003, sha, 'pull_request', '2026-11-08T15:20:00Z', branch=DEV_BRANCH)])]
        _, fl3 = build_order(repo, f, s1, des, apps, bundle, dp, 7, pairs, {})
        check('order rule: a dev run with %s is other and fails' % nm, bool(fl3) and classify_dev(repo, sha, pairs)[0] == 'other',
              '; '.join(fl3[:1]))
        check('plane: a dev run with %s fails' % nm, bool(plane(repo, f, dp)))
    b4 = json.loads(json.dumps(bundle))
    for p in b4['round_branch'] + b4['head_sha'][s1]:
        for r in p['workflow_runs']:
            if r['id'] == 9003:
                r['run_attempt'] = 2
    _, fl4 = build_order(repo, f, s1, des, apps, b4, devp, 7, pairs, {})
    check('attempts: a dispatch run with run_attempt = 2 fails the order rule', bool(fl4), '; '.join(fl4[:1]))
    tok, why = vg(e, run=dict(erun, run_attempt=2))
    check('attempts: run_attempt = 2 at E fails verdict', tok is None, '; '.join(why[:1]))
    vb2 = json.loads(json.dumps(vb))
    extra = _st_run(9006, e, 'workflow_dispatch', '2026-11-08T18:30:00Z')
    vb2['round_branch'][0]['workflow_runs'].append(extra)
    vb2['round_branch'][0]['total_count'] += 1
    vb2['head_sha'][e][0]['workflow_runs'].append(extra)
    vb2['head_sha'][e][0]['total_count'] += 1
    tok, why = vg(e, b=vb2)
    check('verdict: an unapproved dispatch at E is VOID', tok is None, '; '.join(why[:1]))
    tok, why = vg(e, jobs=[_st_jobs(9005, drop=(STEPS['replay'],))])
    check('verdict: a named step missing at E is VOID', tok is None, '; '.join(why[:1]))
    tok, why = vg(e, ap=[])
    check("verdict: E's dispatch without an approval entry is VOID", tok is None, '; '.join(why[:1]))
    # I-B1: references to the record directory anywhere under .github/
    extra_job = ('  probes_extra:\n    runs-on: ubuntu-latest\n    steps:\n      - run: python3 -I -B ' + RDIR
                 + 'marc_check.py\n')
    dv4 = _st_commit(repo, dv1, {WORKFLOW: splice(dwf, DESIGN_JOB).replace(JOB_ANCHOR, extra_job + '\n' + JOB_ANCHOR)
                                 .encode()}, 'dev design job plus a decisive-mode job')
    action = ('runs:\n  using: composite\n  steps:\n    - run: python3 ' + RDIR + 'marc_check.py\n      shell: bash\n').encode()
    dv5 = _st_commit(repo, dv1, {'.github/actions/x/action.yml': action}, 'dev design job plus an action')
    dv6 = _st_commit(repo, d, {'.github/actions/x/action.yml': action}, 'dev action only')
    check('I-B1: the design job plus a second job running the checker in decisive mode is other',
          classify_dev(repo, dv4, pairs)[0] == 'other')
    check('I-B1: the design job plus an action under .github/ referencing the record directory is other',
          classify_dev(repo, dv5, pairs)[0] == 'other')
    check('I-B1: an action alone referencing the record directory is other, not none',
          classify_dev(repo, dv6, pairs)[0] == 'other')
    check('I-B1: the design commit is design and a commit with no reference under .github/ is none',
          classify_dev(repo, dv1, pairs)[0] == 'design' and classify_dev(repo, dv0, pairs)[0] == 'none')
    dp4 = [_st_page([devrun, _st_run(8004, dv4, 'pull_request', '2026-11-08T15:30:00Z', branch=DEV_BRANCH)])]
    _, fl5 = build_order(repo, f, s1, des, apps, bundle, dp4, 7, pairs, {})
    check('I-B1: the order rule and plane fail on that dev run', bool(fl5) and bool(plane(repo, f, dp4)))
    # I-E8: the stage names the commit of its role
    byid = {9001: frun, 9003: s1run_api}
    roles = {'F': f, 'S1': s1}
    wrong = dict(_st_entry(9001, f, 'S1', 611, '2026-11-08T16:50:00Z'))
    check('I-E8: a stage-S1 entry for the run at F fails', bool(entry_errors(wrong, byid, roles)))
    wrong = dict(_st_entry(9003, s1, 'F', 612, '2026-11-08T17:10:00Z'))
    check('I-E8: a stage-F entry for the run at S1 fails', bool(entry_errors(wrong, byid, roles)))
    wrong = dict(_st_entry(9003, s1, 'E', 613, '2026-11-08T17:10:00Z'))
    check('I-E8: a stage-E entry before E exists fails', bool(entry_errors(wrong, byid, roles)))
    ok_e = dict(_st_entry(9003, s1, 'S1', 614, '2026-11-08T17:10:00Z'))
    check('I-E8: a stage-S1 entry for the run at S1 holds', not entry_errors(ok_e, byid, roles))
    rt = dict(_st_entry(9003, s1, 'retake after host VOID', 615, '2026-11-08T17:10:00Z'), voided_run_id=9001,
              preservation_comment_id=616, preservation_created_at='2026-11-08T17:01:00Z')
    check("I-E8: a retake naming another commit than the voided run's fails", bool(entry_errors(rt, byid, roles)))
    # I-N5: P reads the design run's conclusion and every job
    bad_design = json.loads(design)
    bad_design['jobs'][0]['conclusion'] = 'failure'
    bad_raw = canonical(bad_design).encode()
    check('I-N5: a design run with a red job fails P; the green one passes',
          bool(design_run_errors(bad_raw, sha256(bad_raw))) and not design_run_errors(design, sha256(design)))
    # I-N2: a VOID label from decide is VERDICT VOID, exit 1 (a red control with consistent flags, so check E holds)
    red = _st_meas(0, 0)
    red['4']['I']['exposing_V'] = 1
    red['4']['xb']['exposing_V']['I'] = 1
    red['4']['flags'] = green_flags(red['4'], '4')
    rmeas = canonical(red).encode()
    zb2 = io.BytesIO()
    with zipfile.ZipFile(zb2, 'w') as z:
        z.writestr('measurements.json', rmeas)
    zb2 = zb2.getvalue()
    arts2 = {'total_count': 1, 'artifacts': [{'id': 2, 'name': 'arp1-marc-measurements',
                                              'digest': 'sha256:' + sha256(zb2),
                                              'workflow_run': {'id': 9003, 'head_sha': s1}}]}
    rrec = derive_run(s1run_api, [_st_jobs(9003)], arts2, zb2)
    rnote, rlabel = make_note(red, rrec, d, f)
    e2 = _st_commit(repo, s1, {RDIR + MEAS: rmeas, RDIR + 'evidence/s1-run/results.json': canonical(rrec).encode(),
                               RDIR + 'evidence/order.json': canonical(order).encode(),
                               RDIR + 'result.md': rnote.encode()}, 'E with a red control')
    r2 = check_commit(repo, e2, f, 'E', snapshot=snap, inputs=in_blobs)
    erun2 = _st_run(9005, e2, 'workflow_dispatch', '2026-11-08T18:10:00Z')
    epr2 = _st_run(9004, e2, 'pull_request', '2026-11-08T18:00:00Z')
    vb3 = {'round_branch': [_st_page([frun, s1pr, s1run_api, epr2, erun2])],
           'head_sha': {s1: [_st_page([s1pr, s1run_api])], e2: [_st_page([epr2, erun2])]},
           'jobs': {'9002': [_st_jobs(9002, step_overrides=skipped)]}}
    tok, why = vg(e2, run=erun2, ap=[_st_entry(9005, e2, 'E', 603, '2026-11-08T18:05:00Z')], b=vb3)
    check('I-N2: a VOID label from decide gives VERDICT VOID (check E itself holds: %s)' % (not any(r2.values())),
          rlabel == 'VOID' and not any(r2.values()) and tok is None and any('decide: VOID' in w for w in why),
          '; '.join(why[:2]))
    # I-E6: a halt before S1 exists
    vnote, _ = make_note(None, None, d, f, extra_reasons=('the S1 push precondition failed',))
    w0 = _st_commit(repo, f, {RDIR + 'result.md': vnote.encode(), RDIR + 'evidence/order.json': canonical(order).encode()},
                    'halt before S1')
    r3 = check_commit(repo, w0, f, 'W', snapshot=snap, inputs=in_blobs)
    check('I-E6: a halt before S1 (result.md and order.json) passes every control', not any(r3.values()),
          str({k: v for k, v in r3.items() if v}))
    w0b = _st_commit(repo, f, {RDIR + 'result.md': vnote.encode()}, 'halt before S1, no order.json')
    r4 = check_commit(repo, w0b, f, 'W', snapshot=snap, inputs=in_blobs)
    check('I-E6: a halt before S1 without order.json passes every control', not any(r4.values()),
          str({k: v for k, v in r4.items() if v}))
    w0c = _st_commit(repo, f, {RDIR + 'result.md': vnote.encode(), RDIR + 'marc_check.py': marc}, 'halt plus a script')
    check('I-E6: a halt before S1 carrying a script fails R',
          bool(check_commit(repo, w0c, f, 'W', snapshot=snap, inputs=in_blobs)['R']))


def _st_verdict(repo, e, f, run, jobs, apps, bundle, s1, snap, in_blobs):
    """verdict, with the synthetic round's snapshot and inputs in place of the real ones."""
    return verdict(repo, e, f, run, jobs, apps, bundle, s1, snapshot=snap, inputs=in_blobs)


def self_test():
    results = []

    def check(name, cond, detail=''):
        results.append(bool(cond))
        print(('PASS ' if cond else 'FAIL ') + name + (('  [' + detail[:300] + ']') if detail and not cond else ''))

    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, 'preregistration.md'), encoding='utf-8') as fh:
        prereg = fh.read()
    np = norm_ws(prereg)
    # --- 1. the frozen constants against the preregistration beside this file ----------------------------------------
    miss = [t[:50] for t in frozen_texts() if norm_ws(t) not in np]
    check('frozen texts appear in the preregistration', not miss, str(miss))
    check('the frozen job appears verbatim in the preregistration', FROZEN_JOB in prereg)
    check('the design job is the frozen job with exactly three substitutions',
          DESIGN_JOB.count('--fixture-output') == 1 and _CHECK_IF not in DESIGN_JOB
          and DESIGN_JOB.count('        if: ${{ always() }}\n') == 1
          and len([1 for a, b in zip(FROZEN_JOB.split('\n'), DESIGN_JOB.split('\n')) if a != b]) >= 1)
    check("precondition 6's code equals the preregistration's", P6_CODE == frozen_p6_from(prereg))
    check('the branches line stands once at column 0', branches_line_ok(prereg))
    check('the two blocks as frozen', blocks_ok(prereg))
    check('the owner quotations appear verbatim', all(norm_ws(q) in np for q in OWNER_QUOTES))
    s4p = re.search(r'Phrases: (.*?)\. A hit fails V', np)
    listed = re.findall(r'"([^"]+)"', s4p.group(1)) if s4p else []
    check('S4 phrases equal the preregistration list', [x.lower() for x in listed] == list(S4_PHRASES), str(listed))
    check('input blobs, snapshot and tokens appear', all(b in prereg for b in INPUTS.values()) and SNAPSHOT in prereg
          and all(t in prereg for t in TOKENS.values()))
    check('the workflow anchors exist once in a D-shaped workflow', splice(_ST_D_WORKFLOW).count('probes_arp1marc:') == 1)
    # the fill forms of precondition 3 (r7)
    fm, fc = b'# marc\n', b'# controls\n'
    filled = _st_fill(prereg, '1' * 40, fm, fc, '2' * 64)
    ff = prereg_fields(filled)
    check('fill forms: a fill in the stated forms parses every field and leaves no PENDING',
          ff['D'] == '1' * 40 and ff['marc_blob'] == git_blob(fm) and ff['marc_sha256'] == sha256(fm)
          and ff['controls_blob'] == git_blob(fc) and ff['controls_sha256'] == sha256(fc)
          and ff['design_run_sha256'] == '2' * 64 and ff['design_pr'] == '7'
          and ff['design_pairs'] == [(git_blob(fm), git_blob(fc))] and pending_fields(filled) == [], str(ff))
    loose = filled.replace('**`D`** = `%s`' % ('1' * 40), '**`D`** = %s' % ('1' * 40))
    loose = loose.replace('pinned here: `%s`' % ('2' * 64), 'pinned here: %s' % ('2' * 64))
    lf = prereg_fields(loose)
    check('fill forms: a fill without the backticks does not parse', lf['D'] is None and lf['design_run_sha256'] is None)
    if pending_fields(prereg):
        pf = prereg_fields(prereg)
        check('fill forms: the unfilled preregistration parses no field',
              all(pf[k] is None for k in pf if k != 'design_pairs') and pf['design_pairs'] == [], str(pf))
    # --- 2. control B on both scripts, and its mutations -----------------------------------------------------------
    with open(os.path.join(here, 'marc_check.py'), encoding='utf-8') as fh:
        marc_src = fh.read()
    with open(os.path.abspath(__file__), encoding='utf-8') as fh:
        own = fh.read()
    check('B: marc_check.py static form', static_marc(marc_src) == [], str(static_marc(marc_src)))
    check('B: controls.py static form', static_controls(own, frozen_p6_from(prereg)) == [],
          str(static_controls(own, frozen_p6_from(prereg))))
    for name, src, code in (
            ('an extra import', marc_src + '\nimport os\n', 'B:marc:imports'),
            ('open()', marc_src + "\nX = open('x')\n", 'B:marc:forbidden:open'),
            ('a float literal', marc_src + '\nX = 0.5\n', 'B:marc:float-literal'),
            ('true division', marc_src + '\nX = 1 / 2\n', 'B:marc:true-division'),
            ('subprocess', marc_src + '\nimport subprocess\n', 'B:marc:imports')):
        check('B mutation: marc_check.py with %s fails' % name, code in static_marc(src))
    for name, src, code in (
            ('a launch of marc_check.py', own + "\ndef _x():\n    subprocess.run(['python3', 'marc_check.py'])\n",
             'B:controls:subprocess-target'),
            ('a write-mode open outside the self-test', own + "\ndef _y(p):\n    open(p, 'w')\n", 'B:controls:write-open'),
            ('a shell launch', own + "\ndef _z():\n    subprocess.run('git status', shell=True)\n",
             'B:controls:subprocess-form'),
            ('os.system', own + "\ndef _w():\n    os.system('true')\n", 'B:controls:os-call:system'),
            ('another precondition-6 text', own.replace("import sys; sys.path.insert", "import sys;  sys.path.insert", 1),
             'B:controls:p6-code')):
        check('B mutation: controls.py with %s fails' % name, code in static_controls(src, frozen_p6_from(prereg)))
    # --- 3. the decision path ------------------------------------------------------------------------------------
    for (n4, n6), want in (((5, 7), 'EXPOSURE'), ((0, 0), 'SURVIVAL'), ((3, 0), 'SIZE-DEPENDENT'),
                           ((0, 2), 'SIZE-DEPENDENT')):
        m = _st_meas(n4, n6)
        label, why, _ = decide(m, 0)
        check('decide: %s from a synthetic all-green record' % want, label == want, str(why))
        note, nl = make_note(m, {'head_sha': 'a' * 40, 'shard_steps': [{'name': STEPS['check'],
                                 'conclusion': 'success', 'started': True}]}, 'd' * 40, 'f' * 40)
        body = {'EXPOSURE': EXPOSURE_T.split('{n4}')[0], 'SURVIVAL': SURVIVAL_T, 'SIZE-DEPENDENT': SIZE_T.split('{n4}')[0],
                'VOID': VOID_T.split('{')[0]}
        check('note: %s carries its token line, its text and only that text' % want,
              nl == want and (TOKEN_LINE % TOKENS[want]) in note.split('\n') and note.count(body[want]) == 1
              and all(note.count(body[o]) == 0 for o in body if o != want))
        check('note: %s passes S4 on the whole note, frozen texts included' % want, not s4_hits(note), str(s4_hits(note)))
        check('note: %s keeps the qualifier rule' % want, not broad_unqualified(note), str(broad_unqualified(note)[:1]))
        if want in ('EXPOSURE', 'SIZE-DEPENDENT'):
            check('note: %s prints the measured counts' % want, (' %d exposing' % n4 in note) or (' %d of 6008' % n4 in note))
    m = _st_meas(0, 0)
    check('decide: the exit status 3 is VOID', decide(m, 3)[0] == 'VOID')
    check('decide: a missing file is VOID', decide(None)[0] == 'VOID')
    mm = json.loads(json.dumps(m))
    mm['complete'] = False
    check('decide: complete false is VOID', decide(mm, 0)[0] == 'VOID')
    nflip = 0
    for code, fields in FIELD_TABLE:
        for k in SIZE_KEYS:
            for p in fields:
                if p not in _ST_FLIPS or (p.startswith('xb.all1') and k != '4'):
                    continue
                mm = json.loads(json.dumps(m))
                _st_set(mm[k], p, _ST_FLIPS[p])
                mm[k]['flags'] = green_flags(mm[k], k)
                label, why, _ = decide(mm, 0)
                ok = label == 'VOID' and ('%s at |H| = %s' % (code, k)) in why
                mm2 = json.loads(json.dumps(mm))
                mm2[k]['flags'] = dict(m[k]['flags'])
                ok2 = decide(mm2, 0)[0] == 'VOID'
                note, nl = make_note(mm, {'head_sha': 'a' * 40, 'shard_steps': [{'name': STEPS['check'],
                                          'conclusion': 'success', 'started': True}]}, 'd' * 40, 'f' * 40)
                ok3 = nl == 'VOID' and not s4_hits(note) and ('%s at |H| = %s' % (code, k)) in note
                if not (ok and ok2 and ok3):
                    check('decide: %s flipped through %s at |H| = %s is VOID' % (code, p, k), False, str(why))
                nflip += 1
    check('decide: every control flipped through each of its raw fields at each size is VOID (%d flips), the '
          "checker's disagreeing flags are VOID, and the VOID note names the control" % nflip, nflip == 78)
    nbad = 0
    for leaf in _st_leaves(m):
        for how in ('delete', 'wrong type'):
            mm = json.loads(json.dumps(m))
            obj = mm
            for p in leaf[:-1]:
                obj = obj[p]
            if how == 'delete':
                del obj[leaf[-1]]
            else:
                obj[leaf[-1]] = [obj[leaf[-1]]]
            if decide(mm, 0)[0] != 'VOID':
                check('decide: %s %s is VOID' % (how, '.'.join(leaf)), False)
            nbad += 1
    check('decide: every field deleted or of the wrong type is VOID (%d cases)' % nbad, nbad > 200)
    # --- 4. the S4 screen and the qualifier rule ------------------------------------------------------------------
    check('S4: the exact owner quotations pass', all(not s4_hits(q) for q in OWNER_QUOTES))
    check('S4: a paraphrase of the witness principle is caught',
          bool(s4_hits('Failure to build a witness does not prove that none exists unless a theorem shows it.')))
    check('S4: a paraphrase of the "Conversely" standard is caught',
          bool(s4_hits('Conversely, relaxing an assumption is not enough on its own.')))
    check('S4: each listed phrase is caught', all(s4_hits('x %s y' % p.strip()) for p in S4_PHRASES))
    check('qualifier rule: an unqualified broad sentence is caught, a qualified one passes',
          bool(broad_unqualified('The protection holds in every OI model.'))
          and not broad_unqualified('The protection holds in every OI model (%s).' % QUALIFIER))
    # --- 5. the jobs answer, host-VOID, attempts --------------------------------------------------------------------
    sha = 'b' * 40
    run = _st_run(42, sha, 'workflow_dispatch', '2026-11-08T00:00:00Z')
    r = derive_run(run, [_st_jobs(42)])
    check('jobs answer: synthetic steps beside the seven named steps pass', stage_run_errors(r, sha, True) == [],
          str(stage_run_errors(r, sha, True)))
    for nm in (STEPS['check'], STEPS['mutation'], STEPS['checkout']):
        r2 = derive_run(run, [_st_jobs(42, drop=(nm,))])
        check('jobs answer: %r missing fails' % nm, bool(stage_run_errors(r2, sha, True)))
        r3 = derive_run(run, [_st_jobs(42, step_overrides={nm: {'conclusion': 'failure'}})])
        check('jobs answer: %r not success fails' % nm, bool(stage_run_errors(r3, sha, True)))
    r4 = derive_run(run, [_st_jobs(42, step_overrides={'Complete job': {'conclusion': 'failure'}})])
    check('jobs answer: a synthetic step not success fails', bool(stage_run_errors(r4, sha, True)))
    check('attempts: a dispatch run with run_attempt = 2 fails the run checks and the order rule',
          bool(stage_run_errors(derive_run(dict(run, run_attempt=2), [_st_jobs(42)]), sha, True))
          and bool(dispatch_rule_errors([{'run_id': 42, 'run_attempt': 2, 'event': 'workflow_dispatch'}], {42}, 'x')))
    try:
        derive_run(run, [{'total_count': 5, 'jobs': _st_jobs(42)['jobs']}])
        check('jobs answer: an incomplete capture is refused', False)
    except Refusal:
        check('jobs answer: an incomplete capture is refused', True)
    hv = lambda ov, stage, drop=(), shard=True: host_void(derive_run(run, [_st_jobs(42, shard=shard, step_overrides=ov,
                                                                                    drop=drop)]), stage)
    fail_skip = {STEPS['check']: {'conclusion': 'failure'}, STEPS['replay']: {'conclusion': 'skipped', 'started_at': None}}
    check('host-VOID: check started and failed, replay skipped, at E: not host-VOID', hv(fail_skip, 'E')[0] is False)
    check('host-VOID: check cancelled after starting: not host-VOID',
          hv({STEPS['check']: {'conclusion': 'cancelled'}}, 'S1')[0] is False)
    check('host-VOID: check absent', hv({}, 'S1', drop=(STEPS['check'],)) == (True, 'check-absent'))
    check('host-VOID: check skipped', hv({STEPS['check']: {'conclusion': 'skipped'}}, 'S1')[0] is True)
    check('host-VOID: check without started_at', hv({STEPS['check']: {'started_at': None}}, 'S1')[0] is True)
    check('host-VOID: shard job absent', hv({}, 'S1', shard=False) == (True, 'shard-absent'))
    check('host-VOID: at E, check success and replay not run',
          hv({STEPS['replay']: {'conclusion': 'skipped', 'started_at': None}}, 'E') == (True, 'replay-not-run'))
    check('host-VOID: a green run is not host-VOID', hv({}, 'E') == (False, None))
    # --- 6. the workflow splice and the synthetic round in temporary repositories --------------------------------
    check('W: removing the check step if: changes the spliced workflow',
          splice(_ST_D_WORKFLOW, FROZEN_JOB.replace(_CHECK_IF, '', 1)) != splice(_ST_D_WORKFLOW))
    check('W: removing --fixture-output makes the dev job not the design job',
          DESIGN_JOB.replace(' --fixture-output', '') != DESIGN_JOB
          and extract_job(splice(_ST_D_WORKFLOW, DESIGN_JOB)) == DESIGN_JOB)
    check('replay: no committed measurements in a tree without them', replay(os.devnull, here=os.path.join(here, 'x')) == 0)
    with tempfile.TemporaryDirectory() as tmp:
        try:
            _st_round(tmp, here, prereg, check)
        except Refusal as ex:
            check('synthetic round built', False, str(ex))
        mdir = os.path.join(tmp, 'rd')
        _st_write(os.path.join(mdir, MEAS), b'{"x":1}\n')
        _st_write(os.path.join(mdir, 'result.md'), b'note\n')
        _st_write(os.path.join(tmp, 'same.json'), b'{"x":1}\n')
        _st_write(os.path.join(tmp, 'other.json'), b'{"x":2}\n')
        check('replay: equal bytes exit 0, different bytes exit 1',
              replay(os.path.join(tmp, 'same.json'), here=mdir) == 0
              and replay(os.path.join(tmp, 'other.json'), here=mdir) == 1)
    good = all(results)
    print('controls: self-test %s (%d checks)' % ('OK' if good else 'FAILED', len(results)))
    return 0 if good else 1


# =====================================================================================================================
# command line
# =====================================================================================================================
def _opts(args, multi=()):
    pos, opt = [], {}
    i = 0
    while i < len(args):
        a = args[i]
        if a.startswith('--'):
            if i + 1 >= len(args):
                raise Refusal('option %s needs a value' % a)
            if a in multi:
                opt.setdefault(a, []).append(args[i + 1])
            elif a in opt:
                raise Refusal('option %s given twice' % a)
            else:
                opt[a] = args[i + 1]
            i += 2
        else:
            pos.append(a)
            i += 1
    return pos, opt


def main(argv):
    if argv == ['--self-test']:
        return self_test()
    if not argv:
        print(__doc__)
        return 2
    mode, rest = argv[0], argv[1:]
    try:
        if mode == 'decide':
            pos, opt = _opts(rest)
            try:
                m = load_json_file(pos[0])[1]
            except (OSError, ValueError):
                m = None
            es = int(opt['--exit-status']) if '--exit-status' in opt else None
            label, reasons, _ = decide(m, es)
            print('DECIDE  %s' % TOKENS[label])
            for r in reasons:
                print('  ' + r)
            return 0 if label != 'VOID' else 1
        if mode == 'note':
            pos, opt = _opts(rest)
            try:
                m = load_json_file(pos[0])[1]
            except (OSError, ValueError):
                m = None
            s1run = load_json_file(opt['--runs'])[1] if '--runs' in opt else None
            cwd = repo_root()
            f = opt.get('--freeze') or git_rev(cwd, s1run['head_sha'] + '~1')
            d = prereg_fields(git_show(cwd, f, RDIR + 'preregistration.md').decode('utf-8'))['D']
            text, _ = make_note(m, s1run, d, f)
            sys.stdout.write(text)
            return 0
        if mode == 'replay':
            return replay(rest[0])
        if mode == 'derive-run':
            pos, opt = _opts(rest, multi=('--jobs-api',))
            run = load_json_file(opt['--run-api'])[1]
            jobs = [load_json_file(p)[1] for p in opt['--jobs-api']]
            arts = load_json_file(opt['--artifacts-api'])[1] if '--artifacts-api' in opt else None
            zb = None
            if '--artifact-zip' in opt:
                with open(opt['--artifact-zip'], 'rb') as fh:
                    zb = fh.read()
            r = derive_run(run, jobs, arts, zb)
            if '--void-run' in opt:
                hv, code = host_void(r, opt['--void-run'])
                if not hv:
                    print('derive-run: not host-VOID (%s)' % code, file=sys.stderr)
                    return 1
                v = {'schema': VOID_SCHEMA, 'version': 1, 'run_id': r['run_id'], 'run_attempt': r['run_attempt'],
                     'head_sha': r['head_sha'], 'event': r['event'], 'status': run.get('status'),
                     'conclusion': r['conclusion'], 'jobs': r['jobs'], 'shard_steps': r['shard_steps'],
                     'refusal_code': code}
                sys.stdout.write(canonical(v))
                return 0
            sys.stdout.write(canonical(r))
            return 0
        if mode == 'order':
            pos, opt = _opts(rest)
            cwd = repo_root()
            f, s1 = opt['--freeze'], opt['--s1']
            srcs = {}
            loaded = {}
            for k in ('--designation', '--approvals', '--runs', '--dev-runs'):
                raw, obj = load_json_file(opt[k])
                loaded[k] = obj
                srcs[k[2:]] = sha256(raw)
            fl = prereg_fields(git_show(cwd, f, RDIR + 'preregistration.md').decode('utf-8'))
            order, fails = build_order(cwd, f, s1, loaded['--designation'], loaded['--approvals'], loaded['--runs'],
                                       loaded['--dev-runs'], int(opt['--dev-pr']), fl['design_pairs'],
                                       _page_sources(loaded, srcs))
            sys.stdout.write(canonical(order))
            for x in fails:
                print('order: ' + x, file=sys.stderr)
            return 0 if not fails else 1
        if mode == 'verdict':
            pos, opt = _opts(rest, multi=('--jobs-api',))
            cwd = repo_root()
            e = pos[0]
            run = load_json_file(opt['--run-api'])[1]
            jobs = [load_json_file(p)[1] for p in opt['--jobs-api']]
            araw, apps = load_json_file(opt['--approvals'])
            braw, bundle = load_json_file(opt['--branch-runs'])
            tok, why = verdict(cwd, e, opt['--freeze'], run, jobs, apps, bundle)
            print('approvals sha256 %s; runs sha256 %s' % (sha256(araw), sha256(braw)))
            if tok is None:
                print('VERDICT  VOID')
                for r in why:
                    print('  ' + r)
                return 1
            print('VERDICT  %s' % tok)
            return 0
        if mode == 'plane':
            pos, opt = _opts(rest)
            cwd = repo_root()
            lines = []
            errs = plane(cwd, pos[0], load_json_file(opt['--dev-runs'])[1], lines)
            for x in lines:
                print('plane: ' + x)
            for x in errs:
                print('plane: ' + x)
            print('plane: %s' % ('OK' if not errs else 'FAILED'))
            return 0 if not errs else 1
        if mode == 'check':
            pos, opt = _opts(rest)
            cwd = repo_root()
            res = check_commit(cwd, pos[0], opt['--freeze'], opt.get('--stage'))
            bad = 0
            for c, codes in res.items():
                print('%-3s %s' % (c, 'PASS' if not codes else 'FAIL: ' + '; '.join(codes)))
                bad += bool(codes)
            return 0 if not bad else 1
    except (Refusal, KeyError, IndexError) as ex:
        print('controls: refused: %s' % ex, file=sys.stderr)
        return 2
    print(__doc__)
    return 2


def _page_sources(loaded, file_sha):
    """sha256 of each captured page and comment answer, and of each input file."""
    out = {'files': file_sha, 'pages': {}}
    def put(name, obj):
        out['pages'][name] = sha256(canonical(obj).encode())
    put('designation', loaded['--designation']['comment'])
    for i, a in enumerate(loaded['--approvals']):
        for key in ('comment', 'preservation_comment'):
            if key in a:
                put('approval-%d-%s' % (i, key), a[key])
    rb = loaded['--runs']
    for i, p in enumerate(rb['round_branch'] if isinstance(rb['round_branch'], list) else [rb['round_branch']]):
        put('round_branch-%d' % i, p)
    for sha, pages in rb['head_sha'].items():
        for i, p in enumerate(pages if isinstance(pages, list) else [pages]):
            put('head_sha-%s-%d' % (sha[:12], i), p)
    for rid, pages in rb.get('jobs', {}).items():
        for i, p in enumerate(pages if isinstance(pages, list) else [pages]):
            put('jobs-%s-%d' % (rid, i), p)
    dv = loaded['--dev-runs']
    for i, p in enumerate(dv if isinstance(dv, list) else [dv]):
        put('dev-%d' % i, p)
    return out


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
