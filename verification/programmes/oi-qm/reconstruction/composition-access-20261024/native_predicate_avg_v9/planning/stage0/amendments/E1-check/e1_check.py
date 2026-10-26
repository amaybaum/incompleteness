"""NP-AVG-1 Stage 0, erratum E1: consistency check. Toy instances only; nothing runs on v8's
configuration class.

Usage: python3 -I -B e1_check.py
Prints one JSON object; exit 0 iff every check passes, 2 otherwise.

Reads (read-only):
- ../../r5/STAGE0-PLAN-r5.md (the frozen Layer-1 specification), for its SHA-256 and for the
  text E1 quotes at the stated line numbers;
- ../../layer2/code/ (imported: s0geom, l2analysis, l2config), used on the toy profile and on
  planted toy-geometry records only;
- ../../layer2/design/toyrun/{result.json, s1a.json, shard-*.json} (the Layer-2 toy run).

Parts:
- A, quotes: every frozen passage E1 quotes stands at its stated lines of STAGE0-PLAN-r5.md.
- B, closure against section 3 (F6): each of section 3's ten degeneracies, per convention, has
  its survivor cross-tabulation determined by the count list. C8's list (54) leaves exactly
  four (degeneracy, convention) cells undetermined; E1's four added counts (58) close them.
  Countercontrol: dropping any one added count reopens the gap.
- C, toy class (1,400 records, every record closed directly, L3prime, A and G): the per-record
  pipeline reproduces the Layer-2 toy run's degeneracy cells and marginals; the four added
  counts computed per record equal their orbit-reduced values (count preservation, C8).
- D, planted non-vacuity: planted toy-geometry records with computed survivors, including a
  masking-equivalent pair and a nontrivial stabilizer. Decision rule fixed before the run:
  non-vacuity is shown iff at least one added count is nonzero there, and the 2x2 closure
  and count preservation hold.
- E, countercontrol: a predicate that is not C4v-invariant in place of survivor status must
  break the orbit-reduced equality for at least one added cell.
- F, F3 definitions on the toy class: 'shared near tip' coincides with section 4's shared
  tip (same type, equal reach in e, sites on a line parallel to e) on every pair of every toy
  context; the toy frequencies of the three C7 scope predicates are reported.
- G, T1 and T5 on the toy S1a bound: L_A and L_G recomputed from s1a.json's bounds under the
  quantity-cone reading equal s1a.json's values; the tip-cone reading gives 0.
Revision 2 adds (also reading ../../layer2/code/s0ref.py and l2merge.py, ../../../review/
E1-ANALYSIS.md and ../../../review/e1-analysis/e1_analysis.out, and ../E1-LAYER1-ERRATUM.md):
- H, Lemma G-D on the toy class and the planted records, for L3prime and L3, against the
  production closure and the full s0ref closure; corollaries T_A within Surv_A, eligible T_G
  within Surv_G, and T_G = (T_G and Surv_G) union F_G.
- I, planted faults under G: F1 (equivariant in-frame tie drop) and F2 (F1 on non-representative
  members only); the computed-closure mutant of set 2 is killed by F1; the closure-free set 2
  with the direct per-record check catches both on every affected record.
- J, record-index sampling (deterministic, distinct streams, non-representatives included) and
  raw and orbit-level coverage per C7 set; populations equal to the reviewer's analysis.
- K, sigma: case 2 (d) (L_A and L_G recomputed with s0ref's cones and tips) with a perturbed-count
  countercontrol; Layer 2 r2's label and rule_T keep a failing label while sigma = OK.
- L, E1-ANALYSIS section D applied verbatim, apart from the departures listed in the output.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STAGE0 = os.path.normpath(os.path.join(HERE, '..', '..'))
CODE = os.path.join(STAGE0, 'layer2', 'code')
TOYRUN = os.path.join(STAGE0, 'layer2', 'design', 'toyrun')
R5 = os.path.join(STAGE0, 'r5', 'STAGE0-PLAN-r5.md')
R5_SHA256 = '1a30188e70804644a6ff65b3114ab82f8be40a2b056d0e2862ce595a8982847e'
V8_KEY = (3, 6, (0, 0, -3))
sys.path.insert(0, CODE)
import s0geom as G        # noqa: E402
import l2analysis as AN   # noqa: E402
import l2config as CFG    # noqa: E402

CONVS = ('A', 'G')
OUT = {}
FAILS = []


def check(name, ok, detail=None):
    OUT.setdefault('checks', {})[name] = {'pass': bool(ok), 'detail': detail}
    if not ok:
        FAILS.append(name)


def norm(s):
    return ' '.join(s.split())


# ---------------------------------------------------------------- A. quotes
QUOTES = [
    ('r5', 'rule_T_inputs', 994, 998,
     "Its inputs are objective counts from S1a only: - L_A, the number of non-fixed quantities in the global bound "
     "under A whose cone contains a Φ cell; - L_G, the number of quantities in the global bound under G with a seed "
     "tip whose cone contains a source cell."),
    ('r5', 'rule_T_consequence', 1001, 1004,
     "No record whose items lie in Reg × {−1, …, 23}, of any size, has a linked survivor (PO4)."),
    ('r5', 'rule_T_cost', 1008, 1009,
     "**In either case,** if the dry-run cost estimate exceeds S7's budget, the search is reported as not "
     "undertaken for cost."),
    ('r5', 'rule_T_status', 1010, 1011,
     "If S1a is VOID, MISMATCH or INCOMPLETE, rule T is not evaluated and S1b and S1c are not proposed (R4-5)."),
    ('r5', 'rule_T_record', 1012, 1012, "L_A, L_G and rule T's outcome are recorded in `result.json` (§7)."),
    ('r5', 'rule_T_neutrality', 1013, 1016,
     "The rule fires on L_A and L_G only. It does not depend on the k ≤ 2 label"),
    ('r5', 'S1a_definition', 985, 986,
     "the closures under A and G of the union of all items' samples, which is the C9 bound"),
    ('r5', 'pending_owner', 1033, 1035,
     "**Pending owner:** rule T's L_A = L_G = 0 consequence is the geometric statement only (the default above)."),
    ('r5', 'C7_scope', 556, 559,
     "It must agree on every survivor, on every record containing a shared tip, and on a deterministic 1-in-1,000 "
     "sample of the rest. The sampling rule is a Layer-2 configuration constant under certificate item 1 (N6)."),
    ('r5', 'C7_safeguard', 392, 392, "**C7:** agreement with `s0ref`'s greatest self-supporting subset."),
    ('r5', 'S5', 1041, 1041, "**S5.** C7 sampling: 1 in 1,000, plus every survivor and every tie."),
    ('r5', 'cert_item1', 463, 464, "including C7's 1-in-1,000 and C8's 1-in-100 (N6)"),
    ('r5', 'cert_item4_C7', 475, 475, "- C7 on its sample;"),
    ('r5', 'PO3b', 302, 302,
     "(b) If q′ has type T and u lies in the cone of q′, then the reach of q′ in e is at least r, with equality "
     "only if u is also the e-tip of q′ (a shared tip)."),
    ('r5', 'tip_definition', 268, 272,
     "the *e-tip* of q is its near tip c + d e, and its *reach in e* is c·e + d."),
    ('r5', 'degeneracies', 253, 260,
     "**Degeneracies.** Each is counted and cross-tabulated with survivors; none is excluded: - items at q9, at a "
     "Φ site or at the port site, and items on the z-axis; - pairs on a common axis line; - records with a "
     "nontrivial stabilizer; - items with t ≤ 0, and items with t = −1; - masking-equivalent records (E2); - "
     "records whose last sample is odd-class."),
    ('r5', 'C8_list_size', 576, 577, "**The reported counts are exactly the following (54 on the toy class; on v8 the same list):**"),
    ('r5', 'C8_deg', 586, 588,
     "- per convention, every degeneracy of §3 cross-tabulated with survivor status (8 degeneracies × 2); - "
     "masking-equivalent records; records with a nontrivial stabilizer."),
    ('r5', 'C8_closed', 591, 592, "The list is closed against §3: every count §3 defines is on it."),
    ('r5', 'inv_row_C8', 776, 776, "(the closed list of §6 C8: 54 counts on the toy class, closed against §3)"),
    ('r5', 'S7', 1042, 1042, "**S7.** CI budget: 24 runner-hours over at most 32 shards, with a stop rule."),
    ('r5', 'C9', 597, 599,
     "**C9, monotonicity.** - For every record, ret_{L3′} ⊆ ret_{L3}. - Every record's retained set lies in the "
     "global closure bound (S1a)."),
    ('r5', 'E2', 130, 132,
     "**E2, parity (L1).** Odd-class samples are dropped as inert. Masking-equivalent records, those with equal "
     "even-class contexts, are counted."),
    ('r5', 'frame', 161, 164,
     "Under G, a tip is eligible iff it is a seed, that is, outside the frame. The frame is the union of the "
     "G-convention cones (slices −1 and 0) of Φ, V, p and the even port samples; its even part is B8 (PO7)."),
    ('r5', 'O_b', 88, 90, "Define and preregister the S1b/S1c trigger before examining S1 results."),
    ('r5', 'E1_merge', 128, 129, "**E1, identity merge.** A record sample at a Φ site-time, at p or at a port sample is that quantity"),
    ('r5', 'sources_in_frame', 139, 140, "and the sources lie in the frame."),
    ('r5', 'labels_L3prime', 181, 182, "The labels use L3′. L3 is L3′ with the far tips removed; cones are unchanged (RC3)."),
    ('r5', 'G_survivor', 218, 219, "**G-survivor:** S_G(R), the retained quantities with at least one seed tip, is nonempty."),
    ('r5', 'G_linked', 228, 229, "**G-linked:** the cones of S_G contain a source cell at slice 0."),
    ('r5', 'P_A', 274, 276, "every ρ-maximal element of S_A(R) shares each of its aligned near tips with another element of S_A(R) of the same type, at equal reach on the same axis line."),
    ('r5', 'P_A_dir', 277, 280, "every F element of S at reach M_F(e) has its e-tip shared with another F element of S or located at a Φ site-time."),
    ('r5', 'PO4', 303, 303, "Iterated elimination is monotone (a larger context retains a superset)"),
    ('r5', 'PO7', 306, 306, "A quantity at t ≥ 0 has a seed tip iff \\|c\\| + t > 8; a quantity at slice −1 iff \\|c\\| > 7."),
    ('r5', 'MISMATCH_C9', 338, 339, "- L3′ retains something L3 does not (C9; PO4); - a retained set lies outside the global closure bound (C9; PO4);"),
    ('r5', 'cert_C17_C18', 481, 481, "- C17 and C18 on a deterministic sample of v8 records."),
    ('r5', 'C7_pass', 553, 556, "A separately written algorithm computes the greatest self-supporting subset from an explicit cover graph."),
    ('r5', 'C11_layer2', 662, 664, "In Layer 2, C11 (i) runs on a deterministic sample of v8 records and on every survivor;"),
    ('r5', 'sec9_C8', 869, 869, "C8: all 54 counts of the closed list compared"),
    ('r5', 'sec9_zero', 921, 922, "32 of the 54 reported counts are identically zero on it:"),
    ('r5', 'consequence_pending', 1003, 1004, "the wording is pending owner confirmation, §12)."),
    ('r5', 'neutrality_full', 1013, 1016, "It does not depend on the k ≤ 2 label (COLLAPSE_ALL, RESIDUE_UNLINKED, RESIDUE or BASE_RESIDUE), on whether any survivor appears, or on which direction any result points."),
    ('freeze', 'amendment_review', 30, 31, "A change is an append-only amendment, with its own independent review."),
    ('freeze', 'not_frozen', 55, 55, "## Not frozen, and not authorized"),
    ('review', 'owner_T1', 286, 286, "- T1: the L3′ bound, with L3 reported;"),
    ('review', 'owner_T2', 287, 287, "- T2: S1a's status as Layer 2 §4 defines it;"),
    ('review', 'owner_T5', 288, 288, '- T5: "a quantity with a seed tip, whose cone contains a source cell".'),
    ('review', 'owner_T3_T4', 290, 290, "T3 and T4 can be notes."),
    ('review', 'owner_F3', 292, 297, "every record whose *production* closure retains a quantity with a shared near tip"),
    ('review', 'owner_F3_sample', 296, 296, "a deterministic 1-in-100 sample of records whose initial context has a shared tip;"),
    ('review', 'owner_F6', 304, 305, "Either C8's closed list governs, or a 4-count erratum adds the two survivor cross-tabs."),
    ('review', 'F6_row', 187, 187, "a 4-count erratum adds the two cross-tabs (58 counts)"),
    ('review', 'L2_R2', 237, 237, "**L2-R2. Reference gates on every survivor record.**"),
    ('review', 'T1_row', 84, 84, "**T1**, which rule's bound"),
    ('review', 'T2_row', 85, 85, "**T2**, S1a status undefined"),
    ('review', 'T3_row', 86, 86, "**T3**, cost clause"),
    ('review', 'T4_row', 87, 87, "**T4**, citations"),
    ('review', 'T5_row', 88, 88, '**T5**, "seed tip whose cone"'),
    ('review', 'owner_heading', 283, 283, "## Owner decisions (only the owner can make these)"),
    ('r5', 'T6_zero_branch', 1001, 1004,
     "**L_A = 0 and L_G = 0.** No record whose items lie in Reg × {−1, …, 23}, of any size, has a linked survivor "
     "(PO4). The report states this geometric fact only; law failure beyond k ≤ 2 is not claimed, since PO8 covers "
     "at most two Φ triples in clear (R4-5; the wording is pending owner confirmation, §12). S1b and S1c are not "
     "undertaken."),
    ('r5', 'T6_pending', 1033, 1035,
     "**Pending owner:** rule T's L_A = L_G = 0 consequence is the geometric statement only (the default above). "
     "A law statement for k > 2 would need a new proof obligation generalising PO8."),
    ('e1review', 'owner_decisions', 180, 180, "## Owner decisions"),
    ('e1review', 'decision6', 203, 203, "E1 takes effect only after R1–R5 and decisions 1–2 are applied, with a diff-only re-check;"),
    ('e1review', 'F3_facts', 103, 104, "**E1-F3: faithful to the ruling's letter, but the ruled scope needs re-decision (R2, owner 1).**"),
    ('e1review', 'decision1', 182, 182, "**C7 set 2 (re-decision with corrected facts).**"),
    ('e1review', 'decision2', 193, 193, "**The sampling unit of H₁₀₀ and H₁₀₀₀.** Recommended: every record index (R1)."),
    ('analysis', 'A3', 163, 163, "### A3. Orbit reduction: what it preserves"),
    ('analysis', 'B', 220, 220, "## B. Count semantics"),
    ('analysis', 'owner_T6', 316, 319,
     "\"Approved, with qualification. Rule T may be used as a geometric property of the specified closure. It must "
     "not be presented as a probabilistic result, empirical observation, or independent theorem about the full model\" "
     "(amaybaum, 2026-10-26)"),
    ('analysis', 'owner_sigma', 329, 330, "\"Give S1a its own diagnostic status, not an overriding success label\""),
    ('analysis', 'owner_add_it', 344, 344, "(ruling: \"Add it\")"),
    ('analysis', 'owner_595', 399, 399, "(\"Retain the approved shared-tip closure scope, including G's 595 records\")"),
    ('analysis', 'owner_index', 405, 405, "(R1; the owner: \"Every record index\")"),
    ('analysis', 'owner_counts', 462, 462, "(the owner: \"explicit count definitions and a reconciliation table\")"),
]


FILES = {'r5': R5, 'freeze': os.path.join(STAGE0, 'LAYER1-FREEZE.md'),
         'review': os.path.join(STAGE0, '..', 'review', 'LAYER2-REVIEW.md'),
         'e1review': os.path.join(STAGE0, '..', 'review', 'E1-REVIEW.md'),
         'analysis': os.path.join(STAGE0, '..', 'review', 'E1-ANALYSIS.md')}


def part_a():
    with open(R5, 'rb') as f:
        raw = f.read()
    sha = hashlib.sha256(raw).hexdigest()
    check('A.r5_sha256_equals_freeze_record', sha == R5_SHA256, sha)
    lines = {}
    for k, p in FILES.items():
        with open(p, encoding='utf-8') as f:
            lines[k] = f.read().split('\n')
    bad = []
    for fk, name, lo, hi, q in QUOTES:
        if norm(q) not in norm(' '.join(strip_q(x) for x in lines[fk][lo - 1:hi])):
            bad.append([fk, name, lo, hi])
    per = {k: sum(1 for x in QUOTES if x[0] == k) for k in FILES}
    check('A.quotes_at_stated_lines', not bad, {'quotes': len(QUOTES), 'per_file': per, 'not_found': bad})


# ---------------------------------------------------------------- B. closure against section 3
# Section 3's ten degeneracies (lines 253-260), with the Layer-2 key of each. Eight are the
# keys of l2analysis.DEGENERACIES (cross-tabulated in C8's list); two are plain counts there.
DEG3 = [('item_at_q9', 'items at q9'), ('item_at_phi_site', 'at a Φ site'),
        ('item_at_port_site', 'at the port site'), ('item_on_z_axis', 'items on the z-axis'),
        ('pair_on_common_axis', 'pairs on a common axis line'),
        ('nontrivial_stabilizer', 'records with a nontrivial stabilizer'),
        ('item_t_le_0', 'items with t ≤ 0'), ('item_t_eq_minus1', 'items with t = −1'),
        ('masking_equivalent', 'masking-equivalent records (E2)'),
        ('last_sample_odd', 'records whose last sample is odd-class')]
MARGINAL = {'masking_equivalent': 'masking_equivalent_records', 'nontrivial_stabilizer': 'nontrivial_stabilizer'}
NEW_DEGS = ('masking_equivalent', 'nontrivial_stabilizer')
NEW_KEYS = ['%s:deg:%s:survivor=True' % (c, d) for c in CONVS for d in NEW_DEGS]


def cell(c, d, sv):
    return '%s:deg:%s:survivor=%s' % (c, d, sv)


def undetermined(keys):
    """(degeneracy, convention) pairs whose survivor cross-tabulation (both cells) is not
    determined by the count list: either both cells are listed, or the marginal and one cell."""
    ks = set(keys)
    out = []
    for d, _ in DEG3:
        for c in CONVS:
            t, f = cell(c, d, True) in ks, cell(c, d, False) in ks
            m = MARGINAL.get(d) in ks
            if not ((t and f) or (m and (t or f))):
                out.append([d, c])
    return out


def part_b():
    with open(R5, encoding='utf-8') as f:
        sec3 = norm(' '.join(f.read().split('\n')[252:260]))
    check('B.section3_lists_ten_degeneracies', all(norm(p) in sec3 for _, p in DEG3) and len(DEG3) == 10)
    check('B.layer2_crosstab_set_is_section3_minus_two',
          set(AN.DEGENERACIES) == {d for d, _ in DEG3} - set(NEW_DEGS) and len(AN.DEGENERACIES) == 8,
          sorted(AN.DEGENERACIES))
    k54 = AN.count_keys()
    u54 = undetermined(k54)
    check('B.C8_list_has_54', len(k54) == 54 == len(set(k54)), len(k54))
    check('B.C8_list_leaves_exactly_four_open',
          sorted(map(tuple, u54)) == sorted((d, c) for d in NEW_DEGS for c in CONVS), u54)
    k58 = k54 + NEW_KEYS
    check('B.E1_list_has_58_and_closes', len(set(k58)) == 58 and not undetermined(k58),
          {'added': NEW_KEYS, 'undetermined': undetermined(k58)})
    caught = [k for k in NEW_KEYS if undetermined([x for x in k58 if x != k])]
    check('B.countercontrol_drop_one_added_count_reopens', caught == NEW_KEYS, caught)
    OUT['added_counts'] = NEW_KEYS


# ---------------------------------------------------------------- shared tools
def toy_setup():
    s = CFG.make_setup(G, 'toy')
    if s.key() == V8_KEY:
        raise SystemExit('refusing: v8 configuration class')
    return s


def mask_eq_flags(ctxs):
    """{record: True iff another record of the space has an equal context}. ctxs: {record:
    frozenset of non-fixed context quantities}. Equal contexts: Ctx = fixed + port + even record
    samples (E1, E2), so equality is equality of the non-fixed quantity sets."""
    cls = {}
    for r, q in ctxs.items():
        cls.setdefault(q, []).append(r)
    return {r: len(cls[q]) >= 2 for r, q in ctxs.items()}


def new_cells(recs, surv, flags_me, flags_st):
    out = {}
    for c in CONVS:
        out['%s:deg:masking_equivalent:survivor=True' % c] = sum(1 for r in recs if flags_me[r] and surv[c][r])
        out['%s:deg:nontrivial_stabilizer:survivor=True' % c] = sum(1 for r in recs if flags_st[r] and surv[c][r])
    return out


def orbit_reduced(recs, grp, surv, flags_me, flags_st):
    """Each representative's own indicators times its orbit size (the S4 path)."""
    out = {k: 0 for k in NEW_KEYS}
    reps = 0
    for r in recs:
        if AN.canon(r, grp) != r:
            continue
        reps += 1
        w = len(AN.orbit(r, grp))
        for c in CONVS:
            out['%s:deg:masking_equivalent:survivor=True' % c] += w*(flags_me[r] and surv[c][r])
            out['%s:deg:nontrivial_stabilizer:survivor=True' % c] += w*(flags_st[r] and surv[c][r])
    return out, reps


def shared_near(quants, pair, dim, elig=None):
    """True iff two distinct quantities of quants have the same e-tip (near tip c + d e) for the
    same axis direction e; with elig, only tips with elig(u) count."""
    seen = {}
    for q in sorted(quants):
        for lab, u in G.tip_labels(q, pair, dim, G.FROZEN):
            if lab[1] != 'near' or (elig is not None and not elig(u)):
                continue
            key = (lab[0], u)
            if key in seen and seen[key] != q:
                return True
            seen[key] = q
    return False


# ---------------------------------------------------------------- C, E, F. toy class
def part_cef():
    setup = toy_setup()
    grp = AN.group(setup)
    N = G.num_records(setup)
    recs = [tuple(sorted(G.record_at(setup, i))) for i in range(N)]
    surv, deg, ctxq, stab = {c: {} for c in CONVS}, {}, {}, {}
    shared = {k: {c: 0 for c in CONVS} for k in ('initial', 'retained', 'retained_seed')}
    shared_rep_initial = 0
    dim = setup.dim
    def_bad, def_pairs = [], 0
    for r in recs:
        deg[r] = AN.degeneracies(setup, r)
        stab[r] = AN.stabilizer_order(r, grp) > 1
        is_rep = AN.canon(r, grp) == r
        qs = {}
        for c in CONVS:
            ctx = G.Context(setup, r, c)
            a = G.analyse(ctx)
            surv[c][r] = a['survivor']
            qs[c] = frozenset(ctx.quants)
            ret = set(a['retained'])
            elig = ctx.eligible
            si = shared_near(ctx.quants, ctx.pair, dim)
            shared['initial'][c] += si
            shared_rep_initial += si and is_rep
            shared['retained'][c] += shared_near(ret, ctx.pair, dim)
            shared['retained_seed'][c] += shared_near(ret, ctx.pair, dim, elig)
            # F: definitional equivalence with section 4 (PO3 (b), P_A), on every pair of quants
            ql = sorted(ctx.quants)
            tl = {q: dict(G.tip_labels(q, ctx.pair, dim)) for q in ql}
            for i in range(len(ql)):
                for j in range(i + 1, len(ql)):
                    q, o = ql[i], ql[j]
                    (dq, tq), (do, to) = ctx.pair.depth(q), ctx.pair.depth(o)
                    for e in G.axes(dim):
                        def_pairs += 1
                        same_tip = tl[q][(e, 'near')] == tl[o][(e, 'near')]
                        diff = tuple(a2 - b2 for a2, b2 in zip(o[0], q[0]))
                        k = sum(x*y for x, y in zip(diff, e))
                        on_line = k != 0 and diff == tuple(k*y for y in e)
                        reach_q = sum(x*y for x, y in zip(q[0], e)) + dq
                        reach_o = sum(x*y for x, y in zip(o[0], e)) + do
                        sec4 = tq == to and on_line and reach_q == reach_o
                        if same_tip != sec4 and len(def_bad) < 5:
                            def_bad.append([q, o, e, same_tip, sec4])
        if qs['A'] != qs['G']:
            check('C.context_convention_free', False, r)
        ctxq[r] = qs['A']
    me = mask_eq_flags(ctxq)
    with open(os.path.join(TOYRUN, 'result.json')) as f:
        res = json.load(f)['counts']
    # C1: the per-record pipeline reproduces the toy run's cells and marginals
    mine = {}
    for c in CONVS:
        mine[c + ':survivors'] = sum(1 for r in recs if surv[c][r])
        for d in AN.DEGENERACIES:
            for sv in (False, True):
                mine[cell(c, d, sv)] = sum(1 for r in recs if deg[r][d] and surv[c][r] == sv)
    mine['masking_equivalent_records'] = sum(1 for r in recs if me[r])
    mine['nontrivial_stabilizer'] = sum(1 for r in recs if stab[r])
    diff = {k: [v, res.get(k)] for k, v in mine.items() if res.get(k) != v}
    check('C.pipeline_reproduces_toy_run', not diff and len(mine) == 36, {'compared': len(mine), 'differences': diff})
    full = new_cells(recs, surv, me, stab)
    red, nreps = orbit_reduced(recs, grp, surv, me, stab)
    check('C.added_counts_full_equal_orbit_reduced', full == red, {'full': full, 'orbit_reduced': red,
                                                                   'records': N, 'representatives': nreps})
    # 2x2 closure: marginal = survivor cell + non-survivor cell (non-survivor cell by difference)
    clos = {}
    for c in CONVS:
        for d in NEW_DEGS:
            flag = me if d == 'masking_equivalent' else stab
            t = full['%s:deg:%s:survivor=True' % (c, d)]
            fcell = sum(1 for r in recs if flag[r] and not surv[c][r])
            clos['%s:%s' % (c, d)] = [mine[MARGINAL[d]], t, fcell]
    check('C.marginal_equals_sum_of_cells', all(m == t + f for m, t, f in clos.values()), clos)
    # invariance of the indicators across orbits (what makes them orbit-reducible)
    noninv = 0
    for r in recs:
        if AN.canon(r, grp) == r:
            for m in AN.orbit(r, grp):
                noninv += (me[m] != me[r]) or (stab[m] != stab[r]) or any(surv[c][m] != surv[c][r] for c in CONVS)
    check('C.indicators_constant_on_orbits', noninv == 0, noninv)
    OUT['toy_class'] = {'records': N, 'representatives': nreps, 'survivors': {c: mine[c + ':survivors'] for c in CONVS},
                        'added_counts': full, 'note': 'no survivors on the toy class: the added counts are 0 here'}
    # E: countercontrol, a predicate that is not C4v-invariant in place of survivor status
    fake = {c: {r: any(x[0] > 0 for x, _ in r) for r in recs} for c in CONVS}
    ffull = new_cells(recs, fake, me, stab)
    fred, _ = orbit_reduced(recs, grp, fake, me, stab)
    check('E.countercontrol_noninvariant_predicate_breaks_reduction', ffull != fred,
          {'full': ffull, 'orbit_reduced': fred})
    # F: shared-tip definitions
    check('F.shared_near_tip_equals_section4_shared_tip', not def_bad,
          {'pair_direction_cases': def_pairs, 'first_disagreements': def_bad})
    st_runs = 0
    for s in range(4):
        with open(os.path.join(TOYRUN, 'shard-%d.json' % s)) as f:
            st_runs += json.load(f)['gates']['C7']['shared_tip_reps']
    check('F.initial_shared_tip_count_matches_toy_run', st_runs == shared_rep_initial,
          {'toy_run_representative_conventions': st_runs, 'recomputed': shared_rep_initial})
    OUT['toy_C7_scope_predicates'] = {
        'records': N,
        'initial_context_shared_near_tip': shared['initial'],
        'L3prime_closure_retains_shared_near_tip': shared['retained'],
        'L3prime_closure_retains_shared_near_tip_seed_only': shared['retained_seed'],
        'note': 'toy class only; says nothing about v8 frequencies'}


# ---------------------------------------------------------------- D. planted non-vacuity
def part_d():
    setup = toy_setup()
    grp = AN.group(setup)
    pairA = G.Pair(setup.n + 1)
    c0, L = (5, 0, 0), pairA.L
    six = [(G.vadd(c0, e), L) for e in G.axes(3)]
    base = {'block': tuple(sorted([(c0, L + 1)] + six)),
            'block_top_odd': tuple(sorted([(c0, L + 2)] + six)),     # (c0, L+2) is odd-class
            'block_minus_top': tuple(sorted([(c0, L)] + six))}
    recs = sorted({m for r in base.values() for m in AN.orbit(r, grp)})
    surv, ctxq, stab = {c: {} for c in CONVS}, {}, {}
    for r in recs:
        stab[r] = AN.stabilizer_order(r, grp) > 1
        for c in CONVS:
            ctx = G.Context(setup, r, c)
            surv[c][r] = G.analyse(ctx)['survivor']
            ctxq[r] = frozenset(ctx.quants)
    me = mask_eq_flags(ctxq)
    full = new_cells(recs, surv, me, stab)
    red, nreps = orbit_reduced(recs, grp, surv, me, stab)
    clos = {}
    for c in CONVS:
        for d in NEW_DEGS:
            flag = me if d == 'masking_equivalent' else stab
            m = sum(1 for r in recs if flag[r])
            t = sum(1 for r in recs if flag[r] and surv[c][r])
            fcell = sum(1 for r in recs if flag[r] and not surv[c][r])
            clos['%s:%s' % (c, d)] = [m, t, fcell]
    per = {k: {'orbit_size': len(AN.orbit(r, grp)), 'masking_equivalent': me[r], 'nontrivial_stabilizer': stab[r],
               'survivor_A': surv['A'][r], 'survivor_G': surv['G'][r]} for k, r in base.items()}
    check('D.planted_full_equal_orbit_reduced', full == red, {'full': full, 'orbit_reduced': red})
    check('D.planted_marginal_equals_sum_of_cells', all(m == t + f for m, t, f in clos.values()), clos)
    check('D.planted_non_vacuity', any(v > 0 for v in full.values()), full)
    OUT['planted'] = {'records': len(recs), 'representatives': nreps, 'per_base_record': per,
                      'note': 'planted 7-item records in the toy geometry; not records of the k <= 2 space'}


# ---------------------------------------------------------------- G. T1 and T5 on the toy S1a bound
def part_g():
    setup = toy_setup()
    with open(os.path.join(TOYRUN, 's1a.json')) as f:
        s1a = json.load(f)
    dim = setup.dim

    def dec(flat):
        return {(tuple(flat[i:i + dim]), flat[i + dim]) for i in range(0, len(flat), dim + 1)}
    U = tuple((x, setup.tlast) for x in setup.region)
    ctxA, ctxG = G.Context(setup, U, 'A'), G.Context(setup, U, 'G')     # no closure is run
    src = [(x, 0) for x in setup.sources]
    phi = sorted(ctxA.phi_cells)

    def L_A(bound):
        return sum(1 for q in bound if any(G.in_cone(c, q, ctxA.pair) for c in phi))

    def L_G_quantity(bound):
        return sum(1 for q in bound if any(ctxG.eligible(u) for u in G.tips(q, ctxG.pair, dim))
                   and any(G.in_cone(c, q, ctxG.pair) for c in src))

    def L_G_tip(bound):
        return sum(1 for q in bound if any(ctxG.eligible(u) and any(G.in_cone(c, u, ctxG.pair) for c in src)
                                           for u in G.tips(q, ctxG.pair, dim)))
    b = {k: dec(v) for k, v in s1a['bound'].items()}
    vals = {'L3prime': {'L_A': L_A(b['A:L3prime']), 'L_G': L_G_quantity(b['G:L3prime']),
                        'L_G_tip_reading': L_G_tip(b['G:L3prime'])},
            'L3': {'L_A': L_A(b['A:L3']), 'L_G': L_G_quantity(b['G:L3']), 'L_G_tip_reading': L_G_tip(b['G:L3'])}}
    check('G.T1_T5_L3prime_values_equal_s1a', vals['L3prime']['L_A'] == s1a['L_A'] and
          vals['L3prime']['L_G'] == s1a['L_G'], {'recomputed': vals, 's1a': [s1a['L_A'], s1a['L_G']]})
    check('G.L3_values_equal_s1a_reported', [vals['L3']['L_A'], vals['L3']['L_G']] ==
          [s1a['L_reported_L3']['L_A'], s1a['L_reported_L3']['L_G']], s1a['L_reported_L3'])
    check('G.T5_tip_reading_is_zero', vals['L3prime']['L_G_tip_reading'] == 0 == vals['L3']['L_G_tip_reading'])
    check('G.source_cells_are_in_frame', not any(ctxG.eligible(c) for c in src))
    check('G.T1_bounds_nested', b['A:L3prime'] <= b['A:L3'] and b['G:L3prime'] <= b['G:L3'])
    OUT['toy_S1a'] = dict(vals, note='toy geometry; says nothing about v8')


# ---------------------------------------------------------------- revision 2: shared toy data
import s0ref as REF       # noqa: E402  independent reference (toy contexts only)

ANALYSIS = os.path.join(STAGE0, '..', 'review', 'E1-ANALYSIS.md')
ANALYSIS_OUT = os.path.join(STAGE0, '..', 'review', 'e1-analysis', 'e1_analysis.out')
ERRATUM = os.path.join(STAGE0, 'amendments', 'E1-LAYER1-ERRATUM.md')
L3RULE = G.Rule(far=False)


def ref_tips(q, geo):
    """{(e, 'near'|'far'): cell} from the plan text, by s0ref's geometry."""
    c = q[0]
    _, d, near, far = geo.kind(q)
    out = {}
    for i in range(geo.dim):
        for s in (1, -1):
            e = REF.unit(geo.dim, i, s)
            out[(e, 'near')] = (REF.shift(c, e, d), near)
            if d >= 1:
                out[(e, 'far')] = (REF.shift(c, e, d - 1), far)
    return out


class NearOnly:
    """s0ref's geometry with near tips only (rule L3: L3prime without far tips, same cones)."""

    def __init__(self, geo):
        self.geo, self.dim = geo, geo.dim

    def kind(self, q):
        return self.geo.kind(q)

    def cone(self, q):
        return self.geo.cone(q)

    def tipset(self, q):
        return {u for (e, k), u in ref_tips(q, self.geo).items() if k == 'near'}


def per_record(setup, r, conv):
    """Production closures (L3prime, L3), survivor status, s0ref context and full reference
    closure, and under G the In/Out split, for one toy or planted record."""
    ctx = G.Context(setup, r, conv, G.FROZEN)
    a = G.analyse(ctx)
    prod = frozenset(a['retained'])
    prod3 = frozenset(G.Context(setup, r, conv, L3RULE).run())
    port = None if setup.port is None else tuple(setup.port)
    fixed, quants, geo, elig = REF.ref_context(setup.dim, setup.n, port, r, conv)
    ref, _ = REF.greatest(fixed, quants, geo, elig, 8)
    Q0 = frozenset(set(quants) - set(fixed))
    out = {'prod': prod, 'prod3': prod3, 'ref': frozenset(ref), 'Q0': Q0, 'surv': a['survivor'],
           'geo': geo, 'elig': elig, 'pair': ctx.pair, 'fixed': frozenset(fixed)}
    if conv == 'G':
        seed = frozenset(q for q in Q0 if any(elig(u) for u in ref_tips(q, geo).values()))
        out['In'], out['Out'] = Q0 - seed, seed
    return out


_TOY = {}


def toy_data():
    if _TOY:
        return _TOY
    setup = toy_setup()
    grp = AN.group(setup)
    N = G.num_records(setup)
    recs = [tuple(sorted(G.record_at(setup, i))) for i in range(N)]
    canon = {r: AN.canon(r, grp) for r in recs}
    orbit_of, g_to = {}, {}
    for r in recs:
        orbit_of.setdefault(canon[r], []).append(r)
    for rep in orbit_of:
        for m, g in AN.orbit(rep, grp).items():
            g_to[m] = g
    data = {(c, r): per_record(setup, r, c) for c in CONVS for r in recs}
    _TOY.update(setup=setup, grp=grp, N=N, recs=recs, index={r: i for i, r in enumerate(recs)},
                canon=canon, orbit_of=orbit_of, g_to=g_to, data=data)
    return _TOY


def planted_records(setup, grp):
    pairA = G.Pair(setup.n + 1)
    c0, L = (5, 0, 0), pairA.L
    six = [(G.vadd(c0, e), L) for e in G.axes(3)]
    base = [tuple(sorted([(c0, L + 1)] + six)), tuple(sorted([(c0, L + 2)] + six)),
            tuple(sorted([(c0, L)] + six))]
    return sorted({m for r in base for m in AN.orbit(r, grp)})


def sets_of(recs, data, conv, dim):
    S = {r for r in recs if data[(conv, r)]['surv']}
    T = {r for r in recs if shared_near(data[(conv, r)]['prod'], data[(conv, r)]['pair'], dim)}
    Te = {r for r in recs if shared_near(data[(conv, r)]['prod'], data[(conv, r)]['pair'], dim,
                                         data[(conv, r)]['elig'])}
    I = {r for r in recs if shared_near(data[(conv, r)]['Q0'], data[(conv, r)]['pair'], dim)}
    F = {r for r in recs if shared_near(data[(conv, r)]['In'], data[(conv, r)]['pair'], dim)} if conv == 'G' else set()
    return S, T, Te, I, F


# ---------------------------------------------------------------- H. Lemma G-D and its corollaries
def part_h():
    td = toy_data()
    setup, grp = td['setup'], td['grp']
    prec = planted_records(setup, grp)
    pdata = {(c, r): per_record(setup, r, c) for c in CONVS for r in prec}
    summary = {}
    for name, recs, data in (('toy', td['recs'], td['data']), ('planted', prec, pdata)):
        bad3p, bad3, badref = 0, 0, 0
        for r in recs:
            d = data[('G', r)]
            W, _ = REF.greatest(set(), d['Out'], d['geo'], d['elig'], 8)
            W3, _ = REF.greatest(set(), d['Out'], NearOnly(d['geo']), d['elig'], 8)
            bad3p += d['prod'] != (d['In'] | frozenset(W))
            bad3 += d['prod3'] != (d['In'] | frozenset(W3))
            badref += d['ref'] != (d['In'] | frozenset(W))
        check('H.%s.G_D_L3prime_production_equals_In_union_W_Out' % name, bad3p == 0, bad3p)
        check('H.%s.G_D_L3_production_equals_In_union_W_Out_near_only' % name, bad3 == 0, bad3)
        check('H.%s.G_D_form_equals_full_reference' % name, badref == 0, badref)
        SA, TA, _, _, _ = sets_of(recs, data, 'A', setup.dim)
        SG, TG, TeG, IG, FG = sets_of(recs, data, 'G', setup.dim)
        check('H.%s.T_A_subset_Surv_A' % name, TA <= SA, [len(TA), len(SA)])
        check('H.%s.T_G_eligible_subset_Surv_G' % name, TeG <= SG, [len(TeG), len(SG)])
        check('H.%s.T_G_equals_(T_G_and_Surv_G)_union_F_G' % name, TG == ((TG & SG) | FG),
              [len(TG), len((TG & SG) | FG)])
        summary[name] = {'records': len(recs), 'Surv_A': len(SA), 'Surv_G': len(SG), 'T_A': len(TA),
                         'T_G': len(TG), 'T_G_eligible': len(TeG), 'F_G': len(FG), 'I_G': len(IG)}
    check('H.planted_has_G_survivors_and_seed_parts', summary['planted']['Surv_G'] > 0, summary['planted'])
    OUT['lemma_G_D'] = summary


# ---------------------------------------------------------------- I. planted faults F1 and F2
def part_i():
    td = toy_data()
    recs, data, canon, g_to, dim = td['recs'], td['data'], td['canon'], td['g_to'], td['setup'].dim

    def fault_f1(r, prod):
        d = data[('G', r)]
        tips = {}
        for q in prod:
            for (e, k), u in ref_tips(q, d['geo']).items():
                if k == 'near':
                    tips.setdefault((e, u), set()).add(q)
        drop = set()
        for qs in tips.values():
            if len(qs) > 1:
                drop |= {q for q in qs if q in d['In']}
        return frozenset(prod - drop)

    def fault_f2(r, prod):
        return prod if canon[r] == r else fault_f1(r, prod)
    SG, _, _, _, FG = sets_of(recs, data, 'G', dim)
    res = {}
    for fname, fault in (('F1', fault_f1), ('F2', fault_f2)):
        direct = {r: fault(r, data[('G', r)]['prod']) for r in recs}
        reported = {r: frozenset(AN.act_set(g_to[r], direct[canon[r]])) for r in recs}
        ref = {r: data[('G', r)]['ref'] for r in recs}
        affected = {r for r in recs if direct[r] != ref[r] or reported[r] != direct[r]}
        # the computed-closure mutant: set 2 by the computed (reported) closure, checked on reported results
        mut_set = {r for r in recs if shared_near(reported[r], data[('G', r)]['pair'], dim)}
        mut_caught = {r for r in mut_set if reported[r] != ref[r]}
        # E1-F3: closure-free set 2, direct per-record check
        set2 = FG | ({r for r in recs if shared_near(reported[r], data[('G', r)]['pair'], dim)} & SG)
        caught = {r for r in set2 if direct[r] != ref[r] or reported[r] != direct[r]}
        # orbit-reduced check: representatives only, reported vs reference
        rep_caught = {r for r in set2 if canon[r] == r and reported[r] != ref[r]}
        res[fname] = {'affected': len(affected), 'wrong_reported': sum(1 for r in recs if reported[r] != ref[r]),
                      'computed_closure_mutant_caught': len(mut_caught), 'E1_F3_set2_direct_caught': len(caught),
                      'orbit_reduced_representatives_caught': len(rep_caught), 'set2_records': len(set2)}
    f1, f2 = res['F1'], res['F2']
    check('I.F1_affects_records', f1['affected'] > 0, f1['affected'])
    check('I.F1_computed_closure_mutant_killed', f1['computed_closure_mutant_caught'] == 0 < f1['affected'], f1)
    check('I.F1_caught_on_every_affected_record_of_set2', f1['E1_F3_set2_direct_caught'] == f1['affected'], f1)
    check('I.F2_invisible_in_reported_results', f2['wrong_reported'] == 0 < f2['affected'], f2)
    check('I.F2_missed_by_orbit_reduced_check', f2['orbit_reduced_representatives_caught'] == 0, f2)
    check('I.F2_caught_by_direct_per_record_check', f2['E1_F3_set2_direct_caught'] == f2['affected'], f2)
    OUT['planted_faults_G'] = res


# ---------------------------------------------------------------- J. record-index sampling and coverage
STREAMS = {'H100': ('C7_H100', 100), 'H1000': ('C7_H1000', 1000)}


def draw(salt, stream, rate, N):
    out = set()
    for i in range(N):
        h = hashlib.sha256(('%s|%s|%d' % (salt, stream, i)).encode()).digest()
        if int.from_bytes(h[:8], 'big') % rate == 0:
            out.add(i)
    return out


def part_j():
    td = toy_data()
    recs, data, canon, orbit_of, index, N, dim = (td['recs'], td['data'], td['canon'], td['orbit_of'],
                                                    td['index'], td['N'], td['setup'].dim)
    salt = CFG.CONFIG['sampling_salt']
    H = {k: draw(salt, s, rate, N) for k, (s, rate) in STREAMS.items()}
    again = {k: draw(salt, s, rate, N) for k, (s, rate) in STREAMS.items()}
    check('J.samples_deterministic', H == again)
    check('J.streams_distinct', STREAMS['H100'][0] != STREAMS['H1000'][0])
    nonrep = {k: sum(1 for i in v if canon[recs[i]] != recs[i]) for k, v in H.items()}
    check('J.samples_drawn_over_record_indices_include_non_representatives', nonrep['H100'] > 0, nonrep)
    cov = {}
    for c in CONVS:
        S, T, _, I, F = sets_of(recs, data, c, dim)
        set2 = T if c == 'A' else ((T & S) | F)
        sets = {'1_Surv': S, '2_set2': set2, '3_I_and_H100': {r for r in I if index[r] in H['H100']},
                '4_H1000': {recs[i] for i in H['H1000']}}
        cov[c] = {}
        for name, X in sets.items():
            orbits = {canon[r] for r in X}
            cov[c][name] = {'records': len(X), 'orbits_touched': len(orbits),
                            'sum_of_touched_orbit_sizes': sum(len(orbit_of[o]) for o in orbits)}
    OUT['C7_scope_coverage_toy'] = cov
    with open(ANALYSIS_OUT) as f:
        an = json.load(f)['populations']
    pairs = []
    for c in CONVS:
        pairs.append([cov[c]['3_I_and_H100']['records'], an[c]['I_and_H100 (records)']])
        pairs.append([cov[c]['4_H1000']['records'], an[c]['H1000 (records)']])
    pairs.append([cov['G']['2_set2']['records'], an['G']['F (in-frame tie, closure-free)']])
    check('J.matches_reviewer_analysis_populations', all(a == b for a, b in pairs), pairs)


# ---------------------------------------------------------------- K. sigma: case 2 (d) and precedence
def part_k():
    setup = toy_setup()
    with open(os.path.join(TOYRUN, 's1a.json')) as f:
        s1a = json.load(f)
    dim = setup.dim

    def dec(flat):
        return {(tuple(flat[i:i + dim]), flat[i + dim]) for i in range(0, len(flat), dim + 1)}
    U = tuple((x, setup.tlast) for x in setup.region)
    port = tuple(setup.port)
    _, _, geoA, _ = REF.ref_context(dim, setup.n, port, U, 'A')
    _, _, geoG, eligG = REF.ref_context(dim, setup.n, port, U, 'G')
    six, V, _ = setup.phi()
    phi = set(six) | {V}
    src = [(x, 0) for x in setup.sources]

    def ref_LA(bound):
        return sum(1 for q in bound if geoA.cone(q) & phi)

    def ref_LG(bound):
        return sum(1 for q in bound if any(eligG(u) for u in geoG.tipset(q)) and any(c in geoG.cone(q) for c in src))
    b = {k: dec(v) for k, v in s1a['bound'].items()}
    ref = {'L3prime': [ref_LA(b['A:L3prime']), ref_LG(b['G:L3prime'])], 'L3': [ref_LA(b['A:L3']), ref_LG(b['G:L3'])]}
    prod = {'L3prime': [s1a['L_A'], s1a['L_G']], 'L3': [s1a['L_reported_L3']['L_A'], s1a['L_reported_L3']['L_G']]}

    def case_2d(p, r):
        return p != r
    check('K.case_2d_reference_recomputation_agrees', not case_2d(prod['L3prime'], ref['L3prime']),
          {'production': prod, 'reference': ref})
    check('K.L3_values_reported_equal', prod['L3'] == ref['L3'])
    check('K.countercontrol_perturbed_count_fires_2d',
          case_2d([prod['L3prime'][0] + 1, prod['L3prime'][1]], ref['L3prime']) and
          case_2d([prod['L3prime'][0], prod['L3prime'][1] + 1], ref['L3prime']))
    import l2merge as MRG
    labs = {'VOID': MRG.label(['x'], [], [], True, 0, 0, 0, 0),
            'MISMATCH': MRG.label([], ['x'], [], True, 0, 0, 0, 0),
            'INCOMPLETE': MRG.label([], [], ['x'], True, 0, 0, 0, 0)}
    tok = MRG.rule_T('OK', 0, 0)
    tno = MRG.rule_T('VOID', 0, 0)
    check('K.sigma_OK_never_overrides_a_failing_label', all(k == v for k, v in labs.items()) and tok['evaluated'],
          {'labels': labs, 'rule_T_evaluated_with_sigma_OK': tok['evaluated']})
    check('K.rule_T_not_evaluated_when_sigma_not_OK', tno['evaluated'] is False)


# ---------------------------------------------------------------- L. E1-ANALYSIS section D applied verbatim
# (lo, hi) line ranges of E1-ANALYSIS.md whose text E1 revision 2 carries verbatim (leading '> '
# stripped, whitespace normalized). The ranges omitted are E1's declared departures:
# 375-378 and 388 ('as drafted', replaced by the drafted definitions), 416-418 (the Lemma G-D
# reference form, an open owner decision), 470-471 (the rank sentence, corrected).
VERBATIM = [('D0', 309, 310), ('D1', 316, 325), ('D2', 328, 370), ('D4.in_out_lemma', 379, 387),
            ('D4.scope_samples_check', 390, 415), ('D4.void', 419, 419), ('D4.reduction_to_end', 421, 459),
            ('D5.convention', 462, 469), ('D5.table_note', 473, 480)]
D0_PHRASE = 'with odd-class samples dropped (equivalence E2) and identity merges applied (equivalence E1)'
DEPARTURES = [[375, 378, "'Shared near tip: as drafted' and 'Q0(R): as drafted': the drafted definitions are written out"],
              [388, 388, "'Computed closure: as drafted': the drafted definition is written out"],
              [416, 418, 'the reference may use the Lemma G-D form: recast as an open owner decision (section 9)'],
              [470, 471, "'Every list carries rank 3': the frozen 54 carries rank 1 for D = 6, 9; corrected"]]


def strip_q(line):
    s = line.lstrip()
    return s[1:] if s.startswith('>') else line


def part_l():
    with open(ANALYSIS, encoding='utf-8') as f:
        al = f.read().split('\n')
    with open(ERRATUM, encoding='utf-8') as f:
        er = norm(f.read())
    missing = []
    for name, lo, hi in VERBATIM:
        if norm(' '.join(strip_q(x) for x in al[lo - 1:hi])) not in er:
            missing.append(name)
    rows = [x for x in al[485:493] if x.startswith('|')]
    bad_rows = []
    for row in rows:
        cells = [c.strip() for c in row.strip().strip('|').split('|')]
        if norm(cells[0]) not in er or any(norm(p) not in er for p in cells[1].split('; ')):
            bad_rows.append(cells[0])
    check('L.section_D_blocks_verbatim', not missing, {'blocks': len(VERBATIM), 'missing': missing})
    check('L.D0_phrase_present', norm(D0_PHRASE) in er and '(E2) and identity merges applied (E1)' not in er)
    check('L.D6_rows_present', len(rows) == 8 and not bad_rows, {'rows': len(rows), 'missing': bad_rows})
    gd = norm(' '.join(strip_q(x) for x in al[415:418]))
    check('L.departure_GD_permission_not_carried', gd not in er and norm(D0_PHRASE) in er, gd[:80])
    OUT['section_D_departures'] = DEPARTURES


def main():
    part_a()
    part_b()
    part_cef()
    part_d()
    part_g()
    part_h()
    part_i()
    part_j()
    part_k()
    part_l()
    OUT['pass'] = not FAILS
    OUT['failed'] = FAILS
    print(json.dumps(OUT, indent=1, sort_keys=True, ensure_ascii=False, default=str))
    sys.exit(0 if not FAILS else 2)


if __name__ == '__main__':
    main()
