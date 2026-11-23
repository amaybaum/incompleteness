"""Outcomes, exit codes, items and the outcome function (sec. 5)."""
from . import util

pass_ = 'PASS'
review = 'REVIEW_REQUIRED'
fail = 'FAIL'
usage = 'USAGE'
error = 'ERROR'
void = 'VOID'
internal = 'INTERNAL'

exit_codes = {pass_: 0, review: 10, fail: 20, usage: 64, error: 65, void: 70, internal: 71}
result_schema = 'oi-ledger-coverage/4'

fail_classes = frozenset([
    'unauthorized-change', 'missing', 'duplicated', 'ambiguous', 'context-meaning-unverified', 'retained-changed',
    'unauthorized-edit', 'unledgered-file-change', 'hp-unadjudicated', 'untracked-hp-overlap', 'provenance-mismatch',
    'provenance-gap', 'provenance-foreign', 'provenance-ambiguous', 'adjudication-row-changed', 'deny-match',
    'item7-literal-match', 'rule-negative-match', 'rule-overreach', 'record-invalid', 'stale-adjudication',
    'final-unclassified', 'pin-broken', 'pin-target-missing', 'mirror-mismatch', 'lean-code-change',
    'delegated-evidence-invalid', 'candidate-parent', 'landing-parents', 'landing-first-parent-not-M',
    'landing-drops-main-change', 'landing-conflict-unresolved', 'landing-extra-change', 'base-drift',
])
review_classes = frozenset([
    'unclassified', 'new-pattern-in-replacement', 'unclassified-in-replacement', 'rule-fingerprint-mismatch',
    'rule-stale', 'context-structure-changed', 'delegated-evidence-missing', 'side-change-unclassified',
])
error_classes = frozenset([
    'PIN_MISMATCH', 'RECORD_TREE_MISMATCH', 'SCIENTIFIC_BASE_MISMATCH', 'MAIN_NOT_DESCENDANT', 'SOURCE_CHANGED',
    'LEDGER_INTEGRITY', 'EDITS_HASH_MISMATCH', 'ENCODING', 'UNRESOLVABLE', 'CONFIG_INVALID', 'CONFIG_UNSUPPORTED',
    'CONFIG_UNREVIEWED', 'CONFIG_INCONSISTENT',
])
void_classes = frozenset(['CONFIG_NO_CONTROLS', 'PREFLIGHT_FAILED'])


class Stop(Exception):
    """Ends the pipeline with an outcome other than the evaluated one (error, void, usage)."""

    def __init__(self, outcome, cls, message, detail=None):
        Exception.__init__(self, message)
        self.outcome = outcome
        self.cls = cls
        self.message = message
        self.detail = detail or {}


def decision_of(cls):
    if cls in fail_classes:
        return fail
    if cls in review_classes:
        return review
    raise ValueError('unknown item class %r' % cls)


def make_item(obligation, cls, subject, segment=None, fp_fields=None, **extra):
    """An item: its decision follows from its class; its fingerprint from fields no diagnostic algorithm sets."""
    fp = {'obligation': obligation, 'class': cls, 'subject': subject, 'segment': segment}
    if fp_fields:
        fp.update(fp_fields)
    item = {'obligation': obligation, 'class': cls, 'decision': decision_of(cls), 'subject': subject,
            'segment': segment, 'fingerprint': util.fingerprint(fp)}
    item.update(extra)
    return item


def sort_items(items):
    return sorted(items, key=lambda i: (i['obligation'], i['class'], i['subject'], i['segment'] or '',
                                        i['fingerprint']))


def compute(preflight, record_checks, items):
    """The outcome as a pure function of preflight, record_checks and items."""
    if any(not p['passed'] for p in preflight):
        return void
    if record_checks is not None and not record_checks.get('holds', False):
        return fail
    if any(i['decision'] == fail for i in items):
        return fail
    if any(i['decision'] == review for i in items):
        return review
    return pass_


def apply_final(items, final_profiles):
    """--final: review items of the check's final profiles become final-unclassified failures; nothing else changes."""
    out = []
    for it in items:
        if it['decision'] == review and it.get('profiles') and set(it['profiles']) & set(final_profiles):
            new = dict(it)
            new['class'] = 'final-unclassified'
            new['decision'] = fail
            new['converted_from'] = it['class']
            fp = {'obligation': it['obligation'], 'class': 'final-unclassified', 'subject': it['subject'],
                  'segment': it['segment'], 'from': it['fingerprint']}
            new['fingerprint'] = util.fingerprint(fp)
            out.append(new)
        else:
            out.append(it)
    return out
