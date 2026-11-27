"""Operations B (coverage) and D (terms) over one run context."""
import re

from . import context as ctxmod
from . import outcome as oc
from . import rules as rulemod
from . import segments as sg
from . import util


class RunContext:
    """Everything a run reads, resolved in the integrity stage."""

    def __init__(self, repo, config, profiles, allow_rules, records, indicators, sitemap=None, ledger=None):
        self.repo = repo
        self.config = config
        self.profiles = profiles            # {name: Profile}
        self.allow_rules = allow_rules      # [rule dict]
        self.records = records              # {kind: [doc]}
        self.indicators = indicators
        self.sitemap = sitemap
        self.ledger = ledger
        self.abbrev = config['sentence']['abbreviations']
        self.splitter = config['sentence']['splitter_version']
        self._ft = {}
        self._sent = {}
        corpus = config['corpus']
        self.corpus_rx = [re.compile(p) for p in corpus.get('patterns', [])]
        self.corpus_exact = set(corpus.get('paths', []))
        roles = config['roles']
        self.retired_form_trees = {roles.get('pin'), roles.get('scientific_base')} - {None}

    def in_corpus(self, path):
        return path in self.corpus_exact or any(rx.search(path) for rx in self.corpus_rx)

    def ft(self, commit, path):
        key = (commit, path)
        if key not in self._ft:
            self._ft[key] = sg.FileText(self.repo.read(commit, path), '%s:%s' % (commit[:12], path))
        return self._ft[key]

    def corpus(self, commit):
        return sorted(p for p in self.repo.paths(commit)
                      if p in self.corpus_exact or any(rx.search(p) for rx in self.corpus_rx))

    def sentences(self, commit, path):
        key = (commit, path)
        if key not in self._sent:
            self._sent[key] = util.sentences_of(self.ft(commit, path).lines, self.abbrev, self.splitter)
        return self._sent[key]

    def check(self, cid):
        for c in self.config['checks']:
            if c['id'] == cid:
                return c
        return None



# ---- sites ------------------------------------------------------------------------------------------------

def build_sites(ctx):
    pin = ctx.config['roles']['pin']
    mapping = ctx.config['context_mapping']
    out = []
    for s in ctx.sitemap['sites']:
        ft = ctx.ft(pin, s['file'])
        line = ft.lines[s['line'] - 1]
        same = [i for i, l in enumerate(ft.lines) if l == line]
        ind = ctx.indicators.evaluate(line, s.get('quote'))
        eff = ctx.indicators.effects(ind)
        value = s['context_field_value']
        site = {'site_id': '%s:%d@%s' % (s['file'], s['line'], pin[:8]), 'file': s['file'], 'pin_lineno': s['line'],
                'pin_line': line, 'anchor_sha256': util.sha256(line), 'pin_count': len(same),
                'ordinal': same.index(s['line'] - 1) + 1, 'carried': s['carried'], 'context_value': value,
                'pin_context_sha256': util.context_hash(ft.lines, s['line'] - 1), 'indicators': ind,
                'effects': sorted(eff), 'meaning_context': ctxmod.meaning_required(mapping, value, eff),
                'pin_structure_sha256': ctx.indicators.structure(eff, ft.lines, s['line'] - 1)}
        out.append(site)
    return out


def held_lines(states):
    """{(file, line)} of lines held by resolved sites whose classified bytes are unchanged."""
    out = {}
    for st in states:
        if st.resolved and st.text_unchanged and not st.hp:
            for k in range(len(st.block)):
                out[(st.file, st.start + 1 + k)] = st.site['site_id']
    return out


# ---- coverage (op B) -------------------------------------------------------------------------------------

class Coverage:
    def __init__(self, ctx, commit, segments, check, adjudications, hit_records):
        self.ctx = ctx
        self.commit = commit
        self.segments = segments
        self.check = check
        self.hp_records = {a['site_id']: a for a in adjudications.get('hp', [])}
        self.context_adj = adjudications.get('context', [])
        self.hit_records = hit_records
        self.items = []
        self.site_out = {}
        self.states = []
        self.snapshots = []
        self.region_lines = {}

    def item(self, obligation, cls, subject, segment, fp=None, **kw):
        self.items.append(oc.make_item(obligation, cls, subject, segment, fp, **kw))

    def run(self, sweep_files=None):
        ctx = self.ctx
        sites = build_sites(ctx)
        self.sites = sites
        for s in sites:
            st = sg.SiteState(s, s['file'], s['pin_lineno'] - 1, [s['pin_line']], s['pin_count'])
            self.states.append(st)
            self.site_out[s['site_id']] = {
                'site_id': s['site_id'], 'file': s['file'], 'pin_count': s['pin_count'], 'ordinal': s['ordinal'],
                'pin_context_sha256': s['pin_context_sha256'], 'meaning_context': s['meaning_context'],
                'context_required': s['pin_count'] > 1, 'indicators': s['indicators'],
                # R6.CTX.10: a PARTIAL site (a quote indicator holds) carries partial_quote: true, informational only
                'partial_quote': any(s['indicators'].get(d['name']) for d in ctx.indicators.defs if d['on'] == 'quote'),
                'structure_context_sha256': s['pin_structure_sha256'], 'provenance': None,
                'region_shared_with': None, 'hp_overlap': False, 'region_splices': [], 'line_splices': [],
                'carried': s['carried'], 'statuses': [], 'context_changed': False}
        prev = ctx.config['roles']['pin']
        for seg in self.segments:
            if seg['from'] != prev:
                raise oc.Stop(oc.usage, 'USAGE', 'segment chain is not contiguous at %s' % seg['from'])
            name = '%s..%s' % (seg['from'][:8], seg['to'][:8])
            seg['name'] = name
            if seg['kind'] == 'hp':
                self.hp_segment(seg)
            elif seg['kind'] == 'ledgered':
                self.ledgered_segment(seg)
            else:
                self.unledgered_segment(seg)
            self.snapshots.append((seg, held_lines(self.states)))
            prev = seg['to']
        if prev != self.commit:
            raise oc.Stop(oc.usage, 'USAGE', 'segment chain does not end at the commit')
        # R6.REC.10: an HP adjudication entry whose site_id no tracked site carries is FAIL stale-adjudication (an
        # entry naming an existing site but disagreeing with it is decided by that site's own rule); R6.HP.7: a site
        # its adjudication resolves carries the distinct state provenance-adjudicated
        resolved = {st.site['site_id'] for st in self.states if getattr(st, 'adjudicated', False)}
        tracked = set(self.site_out)
        for sid in sorted(self.hp_records):
            if sid not in tracked:
                rec = self.hp_records[sid]
                self.item('HP', 'stale-adjudication', sid, None, {'entry': util.sha256(util.canonical(
                    {k: v for k, v in rec.items() if not k.startswith('_')}))}, record=rec.get('_ref'))
        for sid in resolved:
            self.site_out[sid]['provenance_adjudicated'] = True
        for st in self.states:
            so = self.site_out[st.site['site_id']]
            so['current'] = ({'file': st.file, 'lines': [st.start + 1, st.start + len(st.block)],
                              'sha256': sg.block_sha(st.block)} if st.resolved else None)
            so['current_context_sha256'] = (util.context_hash_block(ctx.ft(self.commit, st.file).lines, st.start,
                                                                    st.start + len(st.block)) if st.resolved else None)
        return self

    # -- segments --
    def _context_check(self, st, seg, frm, to, obligation):
        """Context decision for a site whose identity is verified and whose bytes are unchanged."""
        s = st.site
        ctx = self.ctx
        lt = ctx.ft(to, st.file).lines
        to_ctx = util.context_hash_block(lt, st.start, st.start + len(st.block))
        if seg.get('ctx_from') is None:
            return
        from_ctx, from_struct = seg['ctx_from'][s['site_id']]
        to_struct = ctx.indicators.structure(set(s['effects']), lt, st.start) if from_struct is not None else None
        cls, det = ctxmod.decide(s, from_ctx, to_ctx, from_struct, to_struct, self.context_adj, seg['name'])
        so = self.site_out[s['site_id']]
        if det.get('context_changed'):
            so['context_changed'] = True
        if cls:
            self.item(obligation, cls, s['site_id'], seg['name'], {'from': from_ctx, 'to': to_ctx,
                                                                   'from_structure': from_struct,
                                                                   'to_structure': to_struct},
                      file=st.file, line=st.start + 1, detail=det)

    def _capture_ctx(self, seg):
        out = {}
        for st in self.states:
            if st.resolved and not st.hp:
                lf = self.ctx.ft(seg['from'], st.file).lines
                c = util.context_hash_block(lf, st.start, st.start + len(st.block))
                struct = self.ctx.indicators.structure(set(st.site['effects']), lf, st.start) \
                    if st.text_unchanged else None
                out[st.site['site_id']] = (c, struct)
        seg['ctx_from'] = out

    def hp_segment(self, seg):
        ctx = self.ctx
        repo = ctx.repo
        chain = seg['chain']
        parent_of = seg['parent_of']
        merges = seg['merges']
        self._capture_ctx(seg)
        name = seg['name']
        groups = {}

        def decoded(c, p):
            return ctx.ft(c, p)

        for st in self.states:
            if not st.resolved:
                continue
            s = st.site
            status, steps, region, det = sg.walk_region(repo, chain, parent_of, st.file, st.block, decoded)
            so = self.site_out[s['site_id']]
            if status == 'carried':
                occ = ctx.ft(seg['to'], st.file).occurrences(st.block)
                old = st.start
                st.start = occ[0]
                so['statuses'].append({'segment': name, 'status': 'moved' if occ[0] != old else 'unchanged'})
                self._context_check(st, seg, seg['from'], seg['to'], 'HP')
                continue
            st.hp = True
            st.text_unchanged = False
            so['hp_steps'] = [{k: v for k, v in x.items() if k != 'post'} for x in steps]
            foreign = [x['commit'] for x in steps if x['commit'] not in merges]
            if status == 'provenance-ambiguous':
                st.resolved = False
                self.item('HP', 'provenance-ambiguous', s['site_id'], name, det, file=st.file, line=s['pin_lineno'])
                continue
            for x in steps:
                groups.setdefault((st.file, x['commit'], x['post_sha256']), []).append((s['site_id'], x))
            if foreign:
                st.resolved = False
                self.item('HP', 'provenance-foreign', s['site_id'], name, {'commits': foreign}, file=st.file,
                          line=s['pin_lineno'], detail={'commits': foreign})
                continue
            st.line_range = track_lines(repo, ctx, chain, parent_of, st.file, s['pin_lineno'])
            st.block = region
            occ = ctx.ft(seg['to'], st.file).occurrences(region) if region else []
            st.start = occ[0] if occ else 0
            st.region_found = bool(occ)
            st.hp_removed = not region
            rec = self.hp_records.get(s['site_id'])
            if rec is None:
                st.adjudicated = False
                self.item('HP', 'hp-unadjudicated', s['site_id'], name, {'steps': [x['post_sha256'] for x in steps]},
                          file=st.file, line=s['pin_lineno'], steps=len(steps))
            else:
                cls, why = check_hp_record(rec, s, steps)
                if cls:
                    st.adjudicated = False
                    self.item('HP', cls, s['site_id'], name, {'why': why}, file=st.file, line=s['pin_lineno'],
                              detail=why)
                else:
                    st.adjudicated = True
                    so['provenance'] = rec.get('_ref')
        shared = {}
        for key, members in groups.items():
            ids = sorted({m[0] for m in members})
            if len(ids) > 1:
                for sid in ids:
                    shared[sid] = {'with': [x for x in ids if x != sid], 'step': key[1], 'region_sha256': key[2]}
        for sid, v in shared.items():
            self.site_out[sid]['region_shared_with'] = v
        by_region = {}
        for st in self.states:
            if st.hp and getattr(st, 'adjudicated', False):
                rec = self.hp_records[st.site['site_id']]
                cls = check_hp_shared(rec, self.site_out[st.site['site_id']], st, ctx.ft(seg['to'], st.file))
                if cls:
                    st.adjudicated = False
                    self.item('HP', 'record-invalid', st.site['site_id'], name, {'why': cls}, detail=cls)
                elif self.site_out[st.site['site_id']]['region_shared_with']:
                    by_region.setdefault((st.file, sg.block_sha(st.block)), []).append(st)
        for key, sts in by_region.items():
            group = set(self.site_out[sts[0].site['site_id']]['region_shared_with']['with']) | {sts[0].site['site_id']}
            have = {s_.site['site_id'] for s_ in sts}
            missing = assign_own_lines([self.hp_records[s_.site['site_id']] for s_ in sts], sts[0].block)
            if group - have or missing:
                why = 'shared region: a site without an adjudication' if group - have else \
                    'shared region: own_lines leave a non-blank line unassigned'
                for s_ in sts:
                    s_.adjudicated = False
                    self.item('HP', 'record-invalid', s_.site['site_id'], name, {'why': why}, detail=why)
        self.merger_groups = sorted({(k[0], k[1], k[2]) for k, m in groups.items() if len({x[0] for x in m}) > 1})

    def unledgered_segment(self, seg):
        ctx = self.ctx
        self._capture_ctx(seg)
        name = seg['name']
        by_file = {}
        for st in self.states:
            if st.resolved and st.block and (not st.hp or getattr(st, 'adjudicated', False)):
                by_file.setdefault(st.file, []).append(st)
        for path, sts in sorted(by_file.items()):
            if ctx.repo.blob_id(seg['from'], path) == ctx.repo.blob_id(seg['to'], path):
                for st in sts:
                    self.site_out[st.site['site_id']]['statuses'].append({'segment': name, 'status': 'unchanged'})
                    if not st.hp:
                        self._context_check(st, seg, seg['from'], seg['to'], seg.get('obligation', 'RET'))
                continue
            ff, ft = ctx.ft(seg['from'], path), ctx.ft(seg['to'], path)
            for st in sts:
                self._search(st, ff, ft, seg)

    def _search(self, st, ff, ft, seg):
        name = seg['name']
        before = list(st.block)
        cf = seg['ctx_from'].get(st.site['site_id'])
        if cf is None:
            cf = (util.context_hash_block(ff.lines, st.start, st.start + len(st.block)), None)
        status, cls, det = sg.search_relocate(st, ff, ft, cf[0])
        so = self.site_out[st.site['site_id']]
        so['statuses'].append({'segment': name, 'status': status if status != 'unresolved' else cls})
        site_fields(so, status, det)
        if status == 'unresolved':
            st.resolved = False
            self.item(seg.get('obligation', 'RET'), cls, st.site['site_id'], name,
                      {'from_sha256': sg.block_sha(before), 'file': st.file},
                      file=st.file, line=st.start + 1, detail=det)
        elif not st.hp:
            self._context_check(st, seg, seg['from'], seg['to'], seg.get('obligation', 'RET'))

    def ledgered_segment(self, seg):
        ctx = self.ctx
        led = seg['ledger']
        self._capture_ctx(seg)
        name = seg['name']
        frm, to = seg['from'], seg['to']
        by_file = {}
        for sp in led['splices']:
            by_file.setdefault(sp['file'], []).append(sp)
        seg['splices_by_file'] = by_file
        sites_by_file = {}
        for st in self.states:
            sites_by_file.setdefault(st.file, []).append(st)
        files = sorted(set(ctx.corpus(frm)) | set(ctx.corpus(to)))
        self.file_conformance = []
        for path in files:
            sts = sites_by_file.get(path, [])
            ff, ft = ctx.ft(frm, path), ctx.ft(to, path)
            if path in led['files']:
                expected = sg.apply_splices(ff.data, by_file.get(path, []))
                if ft.data != expected or not ft.exists:
                    self.file_conformance.append({'segment': name, 'file': path, 'status': 'unauthorized-edit',
                                                  'ranges': sg.diff_ranges(expected, ft.data)})
                    self.item('RET', 'unauthorized-edit', path, name,
                              {'expected_sha256': util.sha256(expected), 'actual_sha256': util.sha256(ft.data)},
                              file=path, detail={'ranges': sg.diff_ranges(expected, ft.data)})
                    for st in sts:
                        if st.resolved and not st.hp:
                            self._search(st, ff, ft, seg)
                    self._hp_overlap(sts, ff, by_file.get(path, []), seg)
                    continue
                self.file_conformance.append({'segment': name, 'file': path, 'status': 'conforms', 'ranges': []})
                self._hp_overlap(sts, ff, by_file.get(path, []), seg)
                live = [st for st in sts if st.resolved and (not st.hp or getattr(st, 'adjudicated', False))
                        and st.block]
                for st, status, cls, det in sg.ledgered_file(live, ff, ft, by_file.get(path, []), path):
                    so = self.site_out[st.site['site_id']]
                    so['statuses'].append({'segment': name, 'status': status if status != 'unresolved' else cls,
                                           'splice_ids': det.get('splice_ids', [])})
                    site_fields(so, status, det, by_file.get(path, []))
                    if status == 'unresolved':
                        st.resolved = False
                        self.item('RET', cls, st.site['site_id'], name, {'file': path}, file=path,
                                  line=st.start + 1, detail=det)
                    elif status in ('unchanged', 'moved'):
                        self._context_check(st, seg, frm, to, 'RET')
                    if status == 'authorized-removal':
                        so['removed_at'] = det.get('offset_line')
                    elif status == 'authorized-replacement':
                        # the replacement region at `to`, whole lines, from the LF-inclusive site span (sec. 5)
                        first, last = det['lines']
                        self.region_lines.setdefault(name, set()).update((path, k) for k in range(first, last + 1))
                continue
            if ff.data != ft.data or ff.exists != ft.exists:
                self.file_conformance.append({'segment': name, 'file': path, 'status': 'unledgered-file-change',
                                              'ranges': sg.diff_ranges(ff.data, ft.data)})
                self.item('RET', 'unledgered-file-change', path, name,
                          {'from_sha256': util.sha256(ff.data), 'to_sha256': util.sha256(ft.data)}, file=path)
                for st in sts:
                    if st.resolved and not st.hp:
                        self._search(st, ff, ft, seg)
                continue
            for st in sts:
                if st.resolved and not st.hp:
                    self.site_out[st.site['site_id']]['statuses'].append({'segment': name, 'status': 'unchanged'})
                    self._context_check(st, seg, frm, to, 'RET')

    def _hp_overlap(self, sts, ff, splices, seg):
        for st in sts:
            if not st.hp or not st.block or not getattr(st, 'region_found', False):
                continue
            a = ff.spans[st.start][0]
            b = ff.spans[st.start + len(st.block) - 1][1]
            hit = sorted(sp['id'] for sp in splices if sg.overlaps(sp['start'], sp['end'], a, b))
            so = self.site_out[st.site['site_id']]
            so['region_splices'] = hit
            if hit:
                so['hp_overlap'] = True
                lr = getattr(st, 'line_range', None)
                if lr is not None and lr[0] <= lr[1]:
                    la, lb = ff.spans[lr[0] - 1][0], ff.spans[min(lr[1], len(ff.spans)) - 1][1]
                    so['line_splices'] = sorted(sp['id'] for sp in splices if sg.overlaps(sp['start'], sp['end'],
                                                                                          la, lb))
                if not getattr(st, 'adjudicated', False):
                    st.resolved = False
                    self.item('RET', 'untracked-hp-overlap', st.site['site_id'], seg['name'], {'splices': hit},
                              file=st.file, line=st.start + 1, hp_overlap=True, splices=hit)
                elif so['region_shared_with']:
                    attributed = set()
                    for sid in [st.site['site_id']] + so['region_shared_with']['with']:
                        r = self.hp_records.get(sid, {})
                        for sp_id, sids in (r.get('splice_attribution') or {}).items():
                            if sids:
                                attributed.add(sp_id)
                    if set(hit) - attributed:
                        st.adjudicated = False
                        self.item('HP', 'record-invalid', st.site['site_id'], seg['name'],
                                  {'why': 'unattributed splice', 'splices': sorted(set(hit) - attributed)},
                                  detail='a splice overlapping the shared region is attributed to no site')


# design r6 R6.OUT.18 site fields from the segment rule that set the site's status: `line_delta` of a moved site
# (R6.ANCH.11); `splice_ids`, each splice's old_sha256 and new_sha256 (`per_splice_hashes`) and `new_region_sha256`
# of an authorized replacement (R6.ANCH.13); `whitespace_only` of a site the unledgered search leaves unresolved
# (R6.ANCH.6). A field a later segment's rule does not set is dropped, so each describes the site's last status.
def site_fields(so, status, det, splices=()):
    for k in ('line_delta', 'splice_ids', 'per_splice_hashes', 'new_region_sha256', 'whitespace_only'):
        so.pop(k, None)
    if status == 'moved':
        so['line_delta'] = det['line_delta']
    elif status == 'authorized-replacement':
        by_id = {sp['id']: sp for sp in splices}
        so['splice_ids'] = list(det['splice_ids'])
        so['per_splice_hashes'] = {i: {'old_sha256': by_id[i]['old_sha256'], 'new_sha256': by_id[i]['new_sha256']}
                                   for i in det['splice_ids']}
        so['new_region_sha256'] = det['new_region_sha256']
    elif status == 'unresolved' and 'whitespace_only' in det:
        so['whitespace_only'] = det['whitespace_only']


def check_hp_record(rec, site, steps):
    """Sec. 3.3: compare an HP adjudication with the recomputed walk."""
    carried = rec.get('carried', {})
    if any(carried.get(k) != site['carried'].get(k) for k in ('row', 'code', 'owner')):
        return 'adjudication-row-changed', 'carried row, code or owner differ from the frozen values'
    rs = rec.get('steps', [])
    if len(rs) != len(steps):
        return 'provenance-gap', 'record lists %d steps, the walk finds %d' % (len(rs), len(steps))
    for a, b in zip(rs, steps):
        for k in ('commit', 'parent', 'position', 'pre_sha256', 'post_sha256'):
            if a.get(k) != b.get(k):
                return 'provenance-mismatch', 'step %s: %s differs' % (b['position'], k)
    if not rec.get('semantic_classification') or not rec.get('author'):
        return 'record-invalid', 'semantic classification or author missing'
    return None, None


def check_hp_shared(rec, so, st, ft):
    """own_lines and splice attribution for shared regions (sec. 3.3)."""
    if so.get('region_shared_with') and not rec.get('own_lines'):
        return 'shared region without own_lines'
    return None


def assign_own_lines(records, region_lines):
    """Every non-blank line of a shared region assigned to some site; returns unassigned hashes."""
    have = set()
    for r in records:
        have.update(r.get('own_lines', []))
    return [util.sha256(l) for l in region_lines if l.strip() and util.sha256(l) not in have]


# ---- hits and terms (sec. 6, 8; op D) --------------------------------------------------------------------

def added_lines(ctx, commit, ledger, paths):
    """{path: set(line)} of lines of commit holding a byte of a non-empty splice image."""
    out = {}
    by = {}
    for sp in ledger['splices']:
        by.setdefault(sp['file'], []).append(sp)
    for path in paths:
        sps = sorted(by.get(path, []), key=lambda x: (x['start'], x['end']))
        if not sps:
            continue
        data = ctx.ft(commit, path).data
        d = 0
        acc = set()
        for sp in sps:
            a = sp['start'] + d
            n = len(sp['new_bytes'])
            d += n - (sp['end'] - sp['start'])
            if n == 0:
                continue
            first = data.count(b'\n', 0, a) + 1
            last = data.count(b'\n', 0, a + n - 1) + 1
            acc.update(range(first, last + 1))
        out[path] = acc
    return out


def image_lines(ctx, commit, ledger, paths):
    """{path: {line: [splice ids]}} for every splice image, empty images included (their offset line)."""
    out = {}
    by = {}
    for sp in ledger['splices']:
        by.setdefault(sp['file'], []).append(sp)
    for path in paths:
        sps = sorted(by.get(path, []), key=lambda x: (x['start'], x['end']))
        data = ctx.ft(commit, path).data
        d = 0
        acc = {}
        for sp in sps:
            a = sp['start'] + d
            n = len(sp['new_bytes'])
            d += n - (sp['end'] - sp['start'])
            first = data.count(b'\n', 0, a) + 1
            last = data.count(b'\n', 0, a + max(n, 1) - 1) + 1 if n else first
            for k in range(first, last + 1):
                acc.setdefault(k, []).append(sp['id'])
        if acc:
            out[path] = acc
    return out


class Terms:
    """Hits of review profiles, deny matches, rule and record application on one tree."""

    def __init__(self, ctx, commit, review_profiles, deny_profiles, added=None, hit_records=(), check=None,
                 scope_paths=None, splice_texts=None):
        self.ctx = ctx
        self.commit = commit
        self.review_profiles = review_profiles
        self.deny_profiles = deny_profiles
        self.added = added or {}
        self.hit_records = list(hit_records)
        self.check = check
        self.scope_paths = scope_paths
        self.splice_texts = splice_texts
        self.deny_line_set = {}
        self.items = []
        self.hits = []
        self.rule_counts = {}
        self.evaluated = []

    def paths_for(self, profile):
        if profile.spec.get('scope') == 'repo' and self.scope_paths is not None:
            return self.scope_paths
        return self.ctx.corpus(self.commit)

    def sentence_at(self, path, line, span_line_text=None):
        """Sentences overlapping a line (with index)."""
        sents = self.ctx.sentences(self.commit, path)
        return [(k, s) for k, s in enumerate(sents) if s[1] <= line <= s[2]]

    def deny_added(self, p):
        """An added-text deny profile on each splice image: a match counts unless an equal match (case and
        whitespace normalized) occurs in the text the splice replaces."""
        kinds = p.spec.get('splice_kinds')
        keys = [(re.compile(k['pattern']), k['key']) for k in p.spec.get('match_keys', [])]
        rewrite = [(re.compile(r['pattern']), r['replacement']) for r in p.spec.get('replaced_text_rewrite', [])]
        prm = getattr(self.ctx, 'edit_params', None)
        norm = None
        if prm is not None and p.name in prm['profiles'].values():
            norm = re.compile(prm['key_normalize'])
            # the reviewed params rule decides these, for both units (sec. 6.1)
            kinds = prm['caps_kinds'] if p.name == prm['profiles']['caps_profile'] else None
            if p.name == prm['profiles']['infinity_profile']:
                keys = [(re.compile(k['pattern']), k['key']) for k in prm['key_rules']]
                rewrite = [(re.compile(prm['old_rewrite']['pattern']), prm['old_rewrite']['replacement'])]
            else:
                keys, rewrite = [], []
        for sp in self.splice_texts or []:
            if p.spec.get('scope') == 'corpus' and sp['file'] not in self.ctx.corpus(self.commit):
                continue
            if kinds is not None and sp.get('kind') not in kinds:
                continue
            old_text = sp['old']
            for rx, rep in rewrite:
                old_text = rx.sub(rep, old_text)
            new = [match_key(sp['new'][a:b], keys, norm) for _, a, b in p.matches(sp['new'])]
            old = [match_key(old_text[a:b], keys, norm) for _, a, b in p.matches(old_text)]
            pool = {}
            for k in old:
                pool[k] = pool.get(k, 0) + 1
            for k in new:
                if pool.get(k, 0) > 0:
                    pool[k] -= 1
                    continue
                self.items.append(oc.make_item('TERMS', 'deny-match', '%s@%s' % (sp['id'], sp['file']), None,
                                               {'rule': p.name, 'level': 'splice', 'match': k, 'splice': sp['id']},
                                               file=sp['file'], line=sp['line'], rule_id=p.name, level='splice',
                                               splice=sp['id'], match=k))

    def deny(self):
        """Deny matches on every line and every sentence (per the profile's levels)."""
        out = {}
        for p in self.deny_profiles:
            if p.applies_to == 'added-text':
                self.deny_added(p)
                continue
            for path in self.paths_for(p):
                lines = self.ctx.ft(self.commit, path).lines
                only = None
                if 'line' in p.levels:
                    for ln, m in sg_scan(p, lines, only).items():
                        out.setdefault((path, ln, ln), set()).add(p.name)
                        self.deny_line_set.setdefault((path, ln), set()).add(p.name)
                        self.items.append(oc.make_item('TERMS', 'deny-match', '%s:%d' % (path, ln), None,
                                                       {'rule': p.name, 'level': 'line', 'text': lines[ln - 1]},
                                                       file=path, line=ln, rule_id=p.name, level='line',
                                                       alternatives=sorted({k for k, _, _ in m})))
                if 'sentence' in p.levels:
                    for k, (s, a, b) in enumerate(self.ctx.sentences(self.commit, path)):
                        if only is not None and not any(a <= x <= b for x in only):
                            continue
                        m = p.matches(s)
                        if m:
                            out.setdefault((path, a, b), set()).add(p.name)
                            self.items.append(oc.make_item('TERMS', 'deny-match', '%s:%d-%d' % (path, a, b), None,
                                                           {'rule': p.name, 'level': 'sentence',
                                                            'sha': util.sha256(s)},
                                                           file=path, line=a, last_line=b, rule_id=p.name,
                                                           level='sentence',
                                                           alternatives=sorted({x for x, _, _ in m})))
        self.deny_spans = out
        return out

    def deny_on_sentence(self, sentence):
        return [p.name for p in self.deny_profiles if p.applies_to == 'tree' and p.matches(sentence)]

    def review(self, held=None, region_info=None):
        """Review-profile hits; held lines pass; others are classified by records and rules or stay for review."""
        held = held or {}
        region_info = region_info or {}
        by_line = {}
        for p in self.review_profiles:
            for path in self.paths_for(p):
                try:
                    lines = self.ctx.ft(self.commit, path).lines
                except util.EncodingFault:
                    if p.spec.get('scope') == 'repo':
                        continue
                    raise
                only = None
                if p.applies_to == 'added-text':
                    only = sorted(self.added.get(path, ()))
                    if not only:
                        continue
                for ln, m in sg_scan(p, lines, only).items():
                    by_line.setdefault((path, ln), []).append((p.name, m))
        rec_index = {}
        for r in self.hit_records:
            rec_index.setdefault((r['file'], r['line_sha256']), []).append(r)
        for (path, ln), plist in sorted(by_line.items()):
            line = self.ctx.ft(self.commit, path).lines[ln - 1]
            profs = sorted({n for n, _ in plist})
            hit = {'file': path, 'line': ln, 'line_sha256': util.sha256(line), 'profiles': profs,
                   'tree': self.commit, 'keys': {n: sorted({k for k, _, _ in m}) for n, m in plist}}
            if (path, ln) in held:
                hit.update(state='PASS', held_by=held[(path, ln)])
                self.hits.append(hit)
                continue
            if (path, ln) in self.deny_line_set:
                hit.update(state='FAIL', cls='deny-match', rule_id=sorted(self.deny_line_set[(path, ln)]))
                self.hits.append(hit)
                continue
            info = region_info.get((path, ln), {})
            recs = rec_index.get((path, util.sha256(line)), [])
            lines = self.ctx.ft(self.commit, path).lines
            if recs and lines.count(line) == 1 and set(profs) <= set(recs[0].get('profiles', [])):
                hit.update(state='PASS', classified_by=recs[0].get('_ref'))
                self.hits.append(hit)
                continue
            # allow rules: sentence by sentence
            decided = None
            for pn, m in plist:
                for key, a, b in m:
                    for k, (s, sa, sb) in self.sentence_at(path, ln):
                        sents = self.ctx.sentences(self.commit, path)
                        pos = s.find(line[a:b])
                        if pos < 0:
                            continue
                        neigh = [sents[j][0] for j in (k - 1, k + 1) if 0 <= j < len(sents)]
                        csha = rulemod.sentence_context_sha(sents, k)
                        dh = bool(self.deny_on_sentence(s))
                        state, cls, rid = rulemod.apply_allow(self.ctx.allow_rules, path, s, neigh, csha,
                                                              [(pos, pos + b - a)], dh, self.rule_counts,
                                                              (path, sa), self.granted(path, k))
                        rank = {'fail': 3, 'review': 2, 'pass': 1}[state]
                        if decided is None or rank > decided[0] or (rank == decided[0] == 2 and decided[2] is None
                                                                    and rid is not None):
                            decided = (rank, cls, rid)
            if decided is None:
                decided = (2, 'unclassified', None)
            rank, cls, rid = decided
            if rank == 1:
                hit.update(state='PASS', rule_id=rid)
                self.hits.append(hit)
                continue
            if rank == 2 and cls == 'unclassified' and 'from_region' in info:
                frm = info['from_region']
                absent = any(not any(rx.search(frm) for k2, rx in self._profile(pn).patterns if k2 == key)
                             for pn, m in plist for key, _, _ in m)
                cls = 'new-pattern-in-replacement' if absent else 'unclassified-in-replacement'
            elif rank == 2 and cls == 'unclassified' and info.get('class'):
                cls = info['class']
            hit.update(state='FAIL' if rank == 3 else 'REVIEW_REQUIRED', cls=cls, rule_id=rid)
            hit.update({k: v for k, v in info.items() if k not in ('class', 'from_region')})
            self.hits.append(hit)
            self.items.append(oc.make_item(info.get('obligation', 'TERMS'), cls, '%s:%d' % (path, ln),
                                           info.get('segment'), {'line_sha256': hit['line_sha256'],
                                                                 'profiles': profs, 'rule': rid},
                                           file=path, line=ln, profiles=profs, rule_id=rid,
                                           pre_existing=info.get('pre_existing'),
                                           resolution_needed=None if rank == 3 else
                                           {'record': 'oi-hit-classification/1',
                                            'fields': ['file', 'line_sha256', 'segment', 'profiles',
                                                       'semantic_classification', 'author']}))
        return self

    def granted(self, path, k):
        """One grant per fingerprint (V5): to the sentence with the smallest byte offset among those of the file
        whose text and context equal the fingerprint's; sentences are in file order, so the smallest index."""
        def g(fp):
            sents = self.ctx.sentences(self.commit, path)
            for j in range(len(sents)):
                if util.sha256(sents[j][0]) == fp['sentence_sha256'] and \
                        rulemod.sentence_context_sha(sents, j) == fp['context_sha256']:
                    return j == k
            return False
        return g

    def _profile(self, name):
        for p in self.review_profiles:
            if p.name == name:
                return p
        return self.ctx.profiles[name]

    def stale_rules(self):
        """A fingerprinted instance that occurs nowhere in the tree: rule-stale, for review."""
        evaluated = {p.name for p in self.review_profiles}
        for r in self.ctx.allow_rules:
            if not set(r.get('profiles', [])) & evaluated:
                continue
            rec_at = r.get('recorded_at')
            if rec_at and self.commit != rec_at and self.ctx.repo.is_ancestor(self.commit, rec_at):
                continue  # a tree older than the fingerprints cannot hold them
            for fp in r.get('fingerprints', []):
                sents = self.ctx.sentences(self.commit, fp['file']) if self.ctx.repo.blob_id(self.commit, fp['file']) \
                    else []
                # a fingerprint bound to its location (context required, or a negative allowance, which is
                # granted only at the approved location) is stale when its sentence is absent there (WB5)
                located = r.get('context_required') or bool(fp.get('negative_allowance'))
                if not any(util.sha256(s) == fp['sentence_sha256'] and
                           (not located or rulemod.sentence_context_sha(sents, j) == fp['context_sha256'])
                           for j, (s, _, _) in enumerate(sents)):
                    self.items.append(oc.make_item('TERMS', 'rule-stale', '%s#%s' % (r['id'], fp['sentence_sha256'][:16]),
                                                   None, {'rule': r['id'], 'fp': fp['sentence_sha256']},
                                                   file=fp['file'], rule_id=r['id']))


def sg_scan(profile, lines, only):
    out = {}
    rng = only if only is not None else range(1, len(lines) + 1)
    for ln in rng:
        if 1 <= ln <= len(lines):
            m = profile.matches(lines[ln - 1])
            if m:
                out[ln] = m
    return out


def splice_texts(ctx, frm, commit, ledger):
    """[{id, file, old, new, line}] for every splice: the replaced text at frm and the image line at commit."""
    out = []
    by = {}
    for sp in ledger['splices']:
        by.setdefault(sp['file'], []).append(sp)
    for path, sps in by.items():
        f = ctx.repo.read(frm, path) or b''
        c = ctx.repo.read(commit, path) or b''
        d = 0
        for sp in sorted(sps, key=lambda x: (x['start'], x['end'])):
            a = sp['start'] + d
            d += len(sp['new_bytes']) - (sp['end'] - sp['start'])
            out.append({'id': sp['id'], 'file': path, 'old': f[sp['start']:sp['end']].decode('utf-8', 'replace'),
                        'new': sp['new'], 'line': c.count(b'\n', 0, a) + 1, 'kind': sp.get('kind')})
    return out


_ws = re.compile(r'\s+')


def match_key(text, keys, norm=None):
    """A match normalized for the added-text comparison: lower case, runs matching the params rule's
    normalization (default: whitespace) to one space, then the key rules."""
    k = (norm or _ws).sub(' ', text.lower()).strip()
    for rx, key in keys:
        if rx.search(k):
            return key
    return k


def check_ledger(repo, frm, led):
    """Ledger integrity against the segment start: base, base blobs and every splice's old bytes."""
    if led['base'] != frm:
        raise oc.Stop(oc.error, 'SCIENTIFIC_BASE_MISMATCH', 'ledger base is not the segment start')
    for path, fl in led['files'].items():
        d = repo.read(frm, path)
        if d is None or util.sha256(d) != fl['base_sha256']:
            raise oc.Stop(oc.error, 'LEDGER_INTEGRITY', '%s: base_sha256 differs' % path)
    for sp in led['splices']:
        d = repo.read(frm, sp['file']) or b''
        if sp['end'] > len(d) or util.sha256(d[sp['start']:sp['end']]) != sp['old_sha256']:
            raise oc.Stop(oc.error, 'LEDGER_INTEGRITY', '%s: old_sha256 does not match its span' % sp['id'])


_hunk = re.compile(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', re.M)


def _map_line(hunks, line, end):
    """Map one old line through unified-diff hunks (git numbering); `end` picks the far edge of a hunk."""
    shift = 0
    for a1, a2, b1, b2 in hunks:
        if a2 and a1 <= line <= a1 + a2 - 1:
            if b2 == 0:
                return b1 if end else b1 + 1
            return b1 + b2 - 1 if end else b1
        before = (a1 + a2 - 1 < line) if a2 else (a1 < line)
        if before:
            shift += b2 - a2
    return line + shift


def track_lines(repo, ctx, chain, parent_of, path, line):
    """A site's own line range carried through each step by `git diff -U0` (myers); a diagnostic only."""
    lo, hi = line, line
    for c in chain:
        p = parent_of[c]
        if repo.blob_id(p, path) == repo.blob_id(c, path):
            continue
        key = (p, c, path)
        if key in _hunk_cache:
            lo, hi = _map_line(_hunk_cache[key], lo, False), _map_line(_hunk_cache[key], hi, True)
            continue
        text = repo.diff_u0(p, c, path) if hasattr(repo, 'diff_u0') else None
        hunks = []
        if text is None:
            import difflib
            a, b = ctx.ft(p, path).lines, ctx.ft(c, path).lines
            for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
                if tag != 'equal':
                    hunks.append((i1 if i2 == i1 else i1 + 1, i2 - i1, j1 if j2 == j1 else j1 + 1, j2 - j1))
        else:
            for m in _hunk.finditer(text):
                hunks.append((int(m.group(1)), int(m.group(2) if m.group(2) is not None else 1),
                              int(m.group(3)), int(m.group(4) if m.group(4) is not None else 1)))
        _hunk_cache[key] = hunks
        lo, hi = _map_line(hunks, lo, False), _map_line(hunks, hi, True)
    return (lo, hi)


_hunk_cache = {}
