#!/usr/bin/env python3
"""check_objects.py -- verifies the retained off-main git objects of the evidence-retention archive.

From the repository root:

    python3 -I verification/audits/evidence-retention/check_objects.py                 # tree mode, no git
    python3 -I verification/audits/evidence-retention/check_objects.py --reconstitute  # history mode, uses git
    python3 -I verification/audits/evidence-retention/check_objects.py --self-test     # needs git and history
    python3 -I verification/audits/evidence-retention/check_objects.py --materialize   # history mode, then adds the
                                                    # stored objects to this repository's object store (no refs)

Each object in objects/manifest.json is a commit, tree or blob that main's records cite (or that a cited object
needs) and that main does not reach. A stored file holds it in one of two forms: `raw`, the object's content without
git's header (a blob's bytes, a commit's text, a tree's entries), or `zlib`, a git loose object.

Tree mode (no git, no network):
  O1  every stored entry's file exists with its recorded size and sha256, and its content hashes to its id as
      sha1("<type> <size>\\0" + content); a zlib file's header names the recorded type and size;
  O2  every file under objects/ is listed, or is manifest.json;
  O3  the manifest is well formed: known schema, mechanisms and forms, unique 40-hex ids, stored entries with a
      file and withheld entries without one, a commit's mechanism consistent with its parent and withheld lists
      (withheld_blobs only on raw:partial-tree and inclusion-proof commits); every entry's tranche is an exact
      int, and tranche membership is pinned by id in this checker (TRANCHE_MEMBERS: tranche 2's 920 entries and
      tranche 4's 66, each set checked against its count and sha256): a pinned entry carries its pinned tranche,
      and any other entry a later tranche that has a base in tranche_bases. Which commits O7 holds to the citation
      rule is decided by id against the same pin, never by the label;
  O4  closure: every id a stored commit or fully retained tree names is stored, withheld, or outside the retained
      set (expected on main, which history mode checks); a path tree (raw:proof-path) names its entries off the
      inclusion path without retaining them, and never lies under a fully retained tree; an inclusion path walks
      from its commit through stored trees; a connected commit's parents are retained connected commits or (H3) on
      main; a raw:tree commit has a parent that is neither; parents_not_retained lists only parents that are not
      retained; a raw:partial-tree commit's tree, and an inclusion-proof commit's inclusion paths, withhold exactly
      the commit's listed blobs, and no other commit's tree withholds any;
  O5  excerpt guard: no stored, named or listed id, and no stored file's own blob id, has its sha256 in the
      deny-list (the list holds sha256 digests of ids, so it cites no object itself);
  O6  scan: no stored object's content, decoded, and no file here matches the secret patterns, an IPv4 address or
      an e-mail address, outside the declared exemptions (commit identity lines and Co-Authored-By trailers whose
      address digest is listed; a commit's gpgsig block; reserved example domains);
  O7  every citation's file exists and its cited line holds one of the recorded tokens; a recorded run is on the
      line as a whole word, and a recorded hex token (7 to 40 digits, not all decimal) is a prefix of the entry's
      own id. A lifecycle commit (any commit outside tranche 2's pinned membership: the tranches that carry the
      pending lifecycle, O10) is held to O10's citation rule once cited: it has a run citation; no location is
      mapped twice; each hex token is a word on its line that is a form of the id; a token citation's line names no
      other id; each run citation is a free-standing citation of its run that states the id as the run's head, and
      a run retained under ci/ has the id as its head; and in every file its citations name, every line holding a
      form of the id and every free-standing citation of a recorded run is mapped, and every line naming such a run
      obeys the citation rule below. Tranche 2's entries map frozen records that name several heads beside one
      run, and keep the token rule. Every recorded id discrepancy
      (a cited full id that names no object, mapped to the retained head of the cited run) holds the cited id on
      its line, maps to a stored object with the same eight-digit prefix, and that object carries the run; and
      the provenance-errata entry it names records the same location, cited id, real head and run;
  O8  every id recorded as missing is retained nowhere here, and each of its citing lines still holds it;
  O9  the withheld entries are exactly APPROVED_WITHHELD (id, mechanism, paths), each non-empty; every one is
      named by a retained tree of a commit that lists it (for an inclusion proof, under
      its inclusion paths); its recorded paths are exactly where those trees name it, each of a file type its
      mechanism covers (.log, .out or .err for a raw log, .txt for a raw output, .pdf for a build output); its
      needed_by entries are among them; and it records a size (which no tree records, so the size is as read from
      the recovery copy when the archive was built, and is not checked). An approval that names commits (archive
      tranche 4) is also bound to them: the commits whose retained trees name the blob are exactly those, and the
      entry records each instance with its commit, path, size, blob id, sha256 and reason;
  O10 the citation lifecycle. A commit carries recorded citations (`cited`, which O7 verifies) or a pending one
      (`awaiting_citation`: pull request, round, the record's path outside this archive, the run the record names
      the id as the head of, and optionally the record's citing lines and the forms of the id it uses), never both
      and never neither; any other entry may carry a pending citation, which is checked alike. The run is
      required: without it any mention of the id anywhere in the record would make the entry eligible, and every
      entry the lifecycle serves is a run's head or source. A pending citation is judged against the tree under
      check, never against a pull request:
        pending   the named record is not in the tree. This passes, and the entry counts as not cited, however
                  long it stays so: a pull request that never lands leaves it pending, never cited;
        eligible  the named record is in the tree and cites the id (the full id, or a hex word of 7 or more digits
                  that is a prefix of it), on exactly the recorded lines and with the recorded forms when the entry
                  names them; it cites the recorded run free-standing at least once; and every line naming the run
                  obeys the citation rule. This passes and is printed as eligible for promotion, with its
                  qualifying lines (the id's lines and the run's free-standing citations): the commit that lands the
                  record need not touch this manifest, and a later archive commit replaces awaiting_citation with
                  citations of exactly those lines, which O7 then verifies by the same rule;
        failing   the record is in the tree and does not cite the id, cites it on other lines or in other forms
                  than recorded, does not cite the recorded run free-standing, or a line naming the run breaks the
                  citation rule; or the recorded run is retained under ci/ with another head commit, or its
                  run.json is not readable JSON with a head commit.
      The citation rule (run_citations; R13 in check_retention.py applies the same code). A run is matched as a
      number with no digit beside it. An occurrence is embedded when an ASCII letter stands beside it, or a joiner
      (- _ .) that is itself beside an ASCII letter or digit, so that it is part of one identifier or file name
      (`run1-39043849411.json`); any other occurrence is free-standing (a word, a link text, a /runs/ URL). A line
      with a free-standing occurrence is a citation of the run: on it and on the line either side, every hex id
      word is a form of the id and the full id is among them (the head rule). A line naming the run only embedded
      is not a citation: it need not state the id, is never mapped, and on it and the line either side no hex id
      word may name another head. Hex id words are read case-folded: a word of 7 to 40 digits names another head
      unless it is a form of the id (a word of decimal digits alone counts only at 40 digits), and a word of 41 to
      63 digits always does. A hex word of 64 digits or more is an opaque value: it names no head and never states
      the id (the full id counts only as a 40-digit lowercase word), and never makes a mention a citation.
      Limitation: since such a word is opaque, another commit's id written as part of one (the last 40 digits of
      a 64-digit word, say) is not read as a head; the self-test records that case with its passing verdict.
      No other rule reads a commit's citation state: its object checks (O1-O9, H1-H7) are the same whether it is
      pending, eligible or cited.
History mode (--reconstitute) adds, in a temporary repository that borrows this repository's objects (H0: a git
command that fails fails the check, rather than leaving a rule to read empty output):
  H1  the base, and each later tranche's base in tranche_bases, is in the repository and an ancestor of HEAD;
  H2  every stored object, written with git, gets exactly its recorded id;
  H3  every id the retained objects name that is not retained or withheld is reachable from the base;
  H4  connectivity, relative to the archive and the base, never to what else this clone holds: with a ref at
      every raw:connected and raw:tree commit and every complete cited tree, every raw:tree commit a shallow
      boundary, git fsck --connectivity-only passes and every object the refs reach is retained or reachable from
      the base; each raw:connected commit's history reaches its own tranche's base only through retained
      raw:connected commits; what a raw:partial-tree commit's tree, or an inclusion-proof commit's inclusion
      paths, names beyond the archive and the base is exactly its withheld blobs; every inclusion path resolves to
      a retained or withheld object;
  H5  every listed identity digest is the digest of an address in the base's history;
  H6  no deny-listed id is reachable from HEAD of this repository, or from any reconstituted object;
  H7  no entry, stored or withheld, is reachable from its own tranche's base, and no id recorded as missing is
      reachable from the base: what main already holds is never retained here. H3 and H4 count as on main what
      the latest tranche base reaches.
"""
import bisect
import hashlib
import json
import os
import re
import shutil
import string
import subprocess
import sys
import tempfile
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
OBJ = os.path.join(HERE, 'objects')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
MECH = {'commit': ('raw:connected', 'raw:tree', 'raw:partial-tree', 'inclusion-proof', 'identity-anchor'),
        'tree': ('raw', 'raw:proof-path'),
        'blob': ('byte-copy', 'withheld:raw-log', 'withheld:raw-output', 'withheld:build-pdf')}
WITHHELD = ('withheld:raw-log', 'withheld:raw-output', 'withheld:build-pdf')
# the file types each withholding mechanism covers: a blob is withheld only at paths of its mechanism's kind
WITHHELD_SUFFIXES = {'withheld:raw-log': ('.log', '.out', '.err'), 'withheld:raw-output': ('.txt',),
                     'withheld:build-pdf': ('.pdf',)}
# The withholding approved by the owner on 2026-10-17 (non-empty raw logs and captured .out/.err output; the three
# raw outputs below; build PDFs), as exact entries. A withheld entry must be one of these, with this mechanism and
# exactly these paths, so neither a file type nor a coordinated manifest and list edit can authorize withholding:
# changing the withheld set changes this checker.
APPROVED_WITHHELD = {
    '12095f6f3a739c988e5d5da28667d1761e352ad5': ('withheld:build-pdf',
        ['book/The-Incompleteness-of-Observation-FULL.pdf']),
    '196d096d52d42ee2df3b4824f5ab6bc3e0939ca0': ('withheld:raw-log',
        ['research/a42-revalidation/c6_control.log']),
    '325c825566c37679bf09ec463a29c96572640cb9': ('withheld:raw-log',
        ['research/round7-channel/CI-REPAIR.log']),
    '38077af8485cb0e1f52c2d69863e1a4ac6ca1d16': ('withheld:raw-log',
        ['research/a42-rerun/ctrl16.log']),
    '3a61f0ca7aefe695fb028dfbaa7acbc594f260bb': ('withheld:raw-log',
        ['research/a42-rerun/lemmas42.log']),
    '43e18150962622cdd84daf5d46cc6f52d7638ee3': ('withheld:raw-log',
        ['research/a42-rerun/quarantine/m0all_b39_b.log']),
    '5c1bf575ba52f67d4d2e31077a5766e8b4c307eb': ('withheld:raw-log',
        ['research/a42-rerun/m0all_b39_a.log']),
    '609e70ae7d669939d25e90edd90ff140dc798668': ('withheld:raw-log',
        ['research/a42-rerun/sat_hr39.log']),
    '68a70d013148a04066a149cb8a45092c6d5baed4': ('withheld:raw-log',
        ['research/a42-rerun/n18_in_a41.log']),
    '6a7a010ab29ab09fc79e0d199222cade753ee505': ('withheld:raw-log',
        ['research/a42-rerun/d01_zero.log']),
    '71f55213eb0bc7c6fbc375c397739354a784ad86': ('withheld:raw-log',
        ['research/round7-channel/native-controls.selftest.final.out']),
    '74badd4d5082acb54b6a8c673a92541f4fd11dd7': ('withheld:raw-log',
        ['research/a42-rerun/d01_two.log']),
    '74bc976f85a728fa905124a63108d40f53bb4e6b': ('withheld:build-pdf',
        ['papers/Main.pdf']),
    '7792971561f0fb122e7742fc23df26ff9c277e2e': ('withheld:raw-output',
        ['research/a42-rerun/Rle13_39_a.txt']),
    '7c9aa5e4481c37eeb582ee4290894173a48599b4': ('withheld:raw-log',
        ['research/a42-revalidation/r5.log']),
    '8a0da161222b988e5300c95de129abf3cbbadf54': ('withheld:raw-log',
        ['research/a42-revalidation/r2b2.log']),
    '8b73bdb948d7f2dfdc05eae8c31ddfb5ca8d6602': ('withheld:raw-log',
        ['research/a42-rerun/spanAll77.log']),
    '95e474b742286e20a60485fc3b65a1a6f6676418': ('withheld:raw-log',
        ['research/a42-rerun/sat_cubes39.log']),
    '9ef11ead5816d767e7f6bf15bfd4104e0d6d9e94': ('withheld:raw-output',
        ['research/a42-rerun/Rle13_39_b.txt']),
    'a1c82766fc8fee04a11ab84477f766c76c10965b': ('withheld:raw-output',
        ['research/a42-rerun/Rall_39.txt']),
    'a4d6527933d6e55612199dfe1e463762694de822': ('withheld:raw-log',
        ['research/a42-revalidation/r2a.log']),
    'aa639a024172876bb9b6dad5e00a180e0dfa4bb8': ('withheld:raw-log',
        ['research/AUDITS/2026-10-11-round6/CI-FAILED-B23.log']),
    'b3a6c133d46819a168393aaeb74af9b51a3b349b': ('withheld:raw-log',
        ['research/round7-channel/channel_check.replay.out', 'research/round7-channel/channel_check.run1.out']),
    'bcdefc3c7091a6f50c1a52f5bb7c198a17538edb': ('withheld:build-pdf',
        ['papers/Explainer.pdf']),
    'd68ca300d27823f5df11c7aeb15dab3d7448129c': ('withheld:raw-log',
        ['research/a42-rerun/cvsize.log']),
    'de2e4b294a5181b28f8d54663641de416ed02978': ('withheld:raw-log',
        ['research/a42-rerun/quarantine/sat_cubes39.log']),
    'ecd7c48de5cb22ca19fa7a4b43fd7c990276e613': ('withheld:raw-log',
        ['research/a42-rerun/quarantine/m0all_b39_a.log']),
    'fbc82c68dd2493e547e45b2fd948638cd325eb93': ('withheld:raw-log',
        ['research/a42-rerun/m0all_b39_b.log']),
    # Archive tranche 4, approved by the owner on 2026-10-17 for exactly these paths in exactly these two commits
    # (#831's research sources): a third element binds the approval to the commits whose trees name the blob.
    'c697b82b8a7d6719d78dfc74bc8183c85fa12255': ('withheld:raw-output',
        ['verification/programmes/oi-qm/reconstruction/preservation-induction-design/exact-output.txt'],
        ['e684897da41b1c3d066b880194c9beb87a19b7ad', 'febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3']),
    '8cdf3a83f78059d81a701c2e4951e54f3a2b06bd': ('withheld:raw-output',
        ['verification/programmes/oi-qm/reconstruction/preservation-induction-design/independent-output.txt'],
        ['e684897da41b1c3d066b880194c9beb87a19b7ad', 'febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3']),
}
# Tranche membership, pinned by id (CN-1): the 920 entries of tranche 2 and the 66 of tranche 4, as the archive
# holds them. A tranche label is the manifest's and can be edited; this pin is the checker's. O3 requires each
# pinned entry to carry its pinned tranche and every other entry a later tranche, and O7's lifecycle rule applies
# to every commit outside tranche 2's pinned set, whatever its label. Each set is checked against its count and
# sha256 (of the sorted ids, one per line). Changing a tranche's membership changes this checker.
_TRANCHE2 = """
0004afc9360117ba61523b72854de1aaf63705f0 0034ddb593bd3d1d2709db1ad8d0f43b5d7882bb
00b4874af2f7dbe00560c645320e60bb6401c7d3 00e3b897d47de24529058e6c80d9d6679f1c45ad
016e542872383b296bb0255d8e9ff1561d36fbcc 017f94c99f924e1252632122a86a6a7e021f1379
024b4679ccf451842cf0d75fa2364f5203233a51 02c0fd3823b6fb33b909060495aa7293b9652b4a
02de538a3c7959cfe1e182c2e08a1d61c3a7eb83 0380e4f4c25b533d4db1c04b77c704489bd681df
03916406cd3d1949bf6b364796c9ece67d5835b1 03a65ae952b64b23621c1b28131834708f003f5c
03d28272c9fdb5a0674778ff53295f0b3122086d 03e94be29c911fcd1a0408b7236dd043a5de8e79
04e8774fdd106540831e825d557a7bc093788830 052ff9b0b8529fa57578339f5be01e03d3b921e6
05513b448d3a51aede222afa8e30ac62cf1462fd 0570327f3a89927e803f3d6b68fdb5142c766b08
05744c2b6dae0323de335500d6ad48fa0f96c060 058279276bc9d76a2593a17cbeb275b8179152de
05b9801a069a8f41f4921c4dffb1afedc69c0fed 05d95ab5dceeacd9dae8d3612d1255e39b968fef
05dc99b7fdee24c9aa214514fcc16236bb39296c 05ec5592a4900971a11266b5663b508a789d844b
05f16f5b13bc9e3f6d125f298f4d72b5c5324d22 0636a781c308961e5f639aee5eba859089251d78
069e33c4eaf422f8ac53930f00c03259069dda19 071df3092ee3d7096dcaeb05188a0617c7b2ce73
077775bf18ac26f8ac9417dc34fb00a6d05032e9 07941868099a6b1d01832228a0a8de8112d61fb2
07dfbc02c3374092b0365075dfbd82193a1c8dd5 0828c3b9ce8ca9d4eeff01b3bde1dcd3bb23b116
0923a38e6eadc8f2bf83f9bd2d40a1696eb60a51 0949f3af22e14a487cb8a8b79429fb6bd341bb2e
09a2728985d76e125acade9c397f462143f80291 09a74b8c2a80418d6da6815f93d1f08bcafafc10
0a509ca2cd202368b333174c912d894b8b33beb5 0a5c2f52119e6a1ad64dbb22cebcffadc842ac8c
0a62f9d1f4340aec128320b485e51f39b1e1e324 0b42f4f89d6f75ef875e658dd6e469c1fd30a947
0b4b0d30cefb67aa8711ca6635c091a81d3458f9 0b621abfac0e518f90d5a66f42dae3bb03c7629e
0b8100a5491999c82890c0afa16b35c249a27b30 0bba658f5b6b424e83b02589c12db81ac55b989d
0c2dc7a582b8ab5447bc3ccba21374ce06852839 0c9d28844046420256b66eced788f92fb2cbca51
0d42d28e992f0b056d8341e17b0c768933e39f18 0d432e812364da0ccceb479f1e0ff8497b2d1302
0d4894458cf493aac0b876b4eab5b03594d16a9a 0d865c73f68d80dabb7fef56980709b580daa7a5
0db05aa8e9d48cd3c1b0b2e616274057b720cda4 0db0601abbe50954832968cf81996b61fc5fc2fe
0dc10f1384794fa80c5eb8787a4b1657144e509b 0e240f5755714922d17d0400e03e7efd96fcc191
0e6376eb8ad8e03415d624c38d522ced4f071bd4 0e7b3f3f93544a4ccc9774a5710a88cc89d02974
0ea03bf4d628b0451cd23790174287a99bba983a 0f50fe8f84ee8d874381f4ad8b9194aa5b68cf40
103ae3cf2bae5279defa79d2845a9fb85b418958 10781e7560210e9625076d9cc47d8f2c295317b0
10a988ff5f1a1a1a2834c40f099ea63bdf2eb2ba 111d167be00f9fe0f70878150dd80d87cf417e8c
112b18e2cf3d9bd0996e0141c81145789c6e3069 116d2287e708b83314b6c42444b20b00502e62b2
11be4d26c6077cbb46fce2c7ceba21027a56e09b 11cace6333bc96bcfe19bad0ebd59af038ef8d22
12033cd8c8289bb595a3748dc4d1409f45d7c17b 12095f6f3a739c988e5d5da28667d1761e352ad5
120e6de20271ed67cf12b90cf0ab3e55124078a7 124ccc66810e1728915f18be49e79f3c8dbe23c4
12a695df15fcfc0634f6b0d7953c03482d980101 12d5c93d89114aee45f27edce254fcbc7f3b5d10
133c9d17d6de18076873e2b0aa8bc58e140858cf 1391b9a6a3522087146ab34655e6ca248429f0c4
13d0cb6969a6e80863943e4d8b2fa0091210751a 13dc39e0037c3b71de0cc846969c5c10cacf32d4
140552fb1bf05fc2adf18cbc37875118e719dd99 14731ab5766f7b0097ba5dc19dcaaff73047fc50
14ba1913a0d01d9fd1495665149405743af15500 14f8dd8f443207c84f0d6093c3b049beb39f8aac
154c2999c3f4d6a177132b136c8b1432a74cc8c6 157f448548387b5a78c950b228d3d76d6a70a416
15e065a8afc79d2a27ac85777b90901f4972f12e 16cf96a53fe6526a0ca0ecc1d73f57328582e992
176b9584c01b3bbfb442899ffe159d9d47abc045 17de29c27ed43d7f105aa8518451d8ed61c59937
17e3cf4bcee471ab7adb6ee5bc7a5489606b0360 1892bd2ff0837fa06b0b11b2f67871e2bf57793f
18b450171bffdc846e246f409687e3585e493ba9 194769418883a62c9c808b18b60113dd9b959c22
196d096d52d42ee2df3b4824f5ab6bc3e0939ca0 197f7664d85894139278d20fe6ff45eb7c9df67b
198bb9188481e69d93407fced8c4d9f2ca4a0b81 1998542461fff0f7b0e03d0b98278d72a7770f50
1b5c44893410be330d7663ab2c71abdf46446805 1b77be2bd582d491301b6750af0aab17396c9f85
1c29812c19f47d39e75a5ca2983823047f2ec5a7 1c498598e751b57dda480abbb57ebf529aea6b32
1c98b0dfde722f8aaeebebd88119423cae4e477c 1cf5c32e5fe609901b6ba198afdfa306df6f1d24
1d1a358980bc6c9760219a418e3d86e8a8b30da5 1d1a8d44fa1cfeabec6ea24650e488910ee913a9
1dd963ba4b64e791bddf6afc6c37fda29226e72b 1df1a912476b18d59761ad924453331e1988e3b9
1dfff6f3f6f54b96af308d314af880aeea367480 1e00c3b92617679ddc9db3fdf0ba1ecf177d0117
1e4810a5473e5ae0f7fd70bffe2069e7125d1124 1e9f72879d0f2931737b348d8a2779c94e3e93db
1f06541f70d611af1f8c31dfbf339bec4992f745 1f19a347108e4e017c33362e6a3f47e091ba84e5
1f5aed1854898c89c063fe827ce84cbb31ff573b 1fcc2140463f44760a410af78c25dee0166663a2
1ffe2d6fb839066479a6d9819a6ce17b87db7d65 200107a67635314d77d1c37d01742a23c1719045
204e01cf31999fb583e0b68055baaa6a384d6356 2082c0f7fd4e88f608ce3bd5a973908085e6f1ee
20aa1eadf1fc1c250b41d3d700be1d4f0a900c74 20ccab419c05c7026175ad11004bedfbb0c97609
20efa9e52059a0c90bf6107fd85d2e9ba7151c58 215d60fc88754b4d40c49f71bd474e71b32887b3
215e3c7f91f4d261a76be4b7400a36826e0a65ad 217a95dec29045c745cb9b3daa30a998e20ef58f
21d4c3858f38b030598a5eebd113df7b0674de35 22167fb14331258894bf7bf2a6ae847aff899e46
228b635a39d8e002565d58b555c5672ef362b1a8 22dd2b63638eff7944a2eac1c3a6af94c05b17bd
230213081906dc59b112f328be308eb0b44181d8 23db7fcecc9e41c3639022e8b8230721c3faf34d
23ddaf02eb50809f4d87cf426c20c81a8e30cf18 23ee9485992862e16ab859512c9a7f530d769f59
241bf60ee9876dda37b0561101dc6bd506b8507f 2420bbb5b15b282831958bd630270c51b35b645c
24507d676879f95acd31755a5af82ecd678ae53a 2496ee6fad349e6d07a7dcb2fd335a8701fc0723
24f69c1fac5d21fb8c31a7cc56f97be53abd1cdf 2508f5ea7cd4ea0ac3e2a5116a5eef6385789f2b
256e057ac1cf18d6afc213f5a79ff92c6ed5a249 25e85cae6c9ab9a103a9d3845ce8119ea9e565ca
2617882a26d18b261fb09f4fe9630bec155b1f1e 2690f68d81b505bacef8b8e2ccb63d4d0919e90e
2744d87aca0847eba1e00339cc1bb2e40e15fc6e 27785544a7bba2077df8e7e02293906a714cb88b
27f1792746416e44246545a7c36aca56756734c9 28722569dc13b010f53b30fe19afc2415174ed23
28787ef7a898112eb0e7a357d2765c259e3a6e6d 287f8128986ef2961cb72b116bd887752159734a
289b2bdea68bc1512b207feeb2dbdd494cf37dc7 28d9978b9a309d79886fc5f44690d25de8c81e85
28e9bb2df6281f38a56aa2a263a9887833c859a2 2940548f782c29f24d2fcc7c0b465d778f20c1c1
2948c65d57b332e159ce008a956eadd6016cef70 29ca2b903bca1fafc5254380a4e63f8a17777e2b
2a0ff60b2bcec67825fc6c022e16ba99e726ebac 2a123a49dab1c39870552afebf4388a97a72ec4c
2a2067858990882c338e2400c987b4185e1ccebd 2a454b5c5da5b3c5a761af7f45ca5d6a326516ab
2a5b84555cbae02481c4fe5e5a48ff9959522129 2aa1ec96017ca878a2e8f0b260b030a95d23b262
2ae4dbeeceae2b2e66bd43658045b67da0f0e650 2b1bfb971c4ecbcbdcd0d72519259099aa76deb8
2b8264fa18ad7a9442bdac507ad7aa2bbd52dad7 2bb548a36b238495d5535f18a9c3df13532fa3bf
2bd384c06382d0ec4bac6afb08b55d830f34acf2 2c0054744b887561d04130bb7ea82287d881b139
2c8995f8693ab7f0b504540d3405a0bbd22192de 2cc3f1cd312de1668ff0584e3321a92ae385c6d6
2ccf277db201168d3d22a254c7aa93950cd93f17 2d79cf0507dddfd2fd72ef6059c559770cd3a7bf
2d9f5175633d8d6d968a83423bec45ce79642caa 2daac6f8e3e7e8a4b130855572e133f2d4409d0e
2e6b537af3c2f363b9400d7b0fae71e82060a741 2e7ee6aed785c25bca5e6c9a7615ca6c85178098
2e8357b90fff68ecb7bd807d7b1857151e0219a6 2e841a02c603fcb11d64e22a4953abb78ceaa678
2f9707a16757f110b7244fe4b48cd96593f69b44 2fe5a203287917bf6b29ae3daf473cc3a998ca3c
304f89e4eb79123e5311f2ef2ff502121b8d6232 3136763dbad744cf3f1006ca9f5e6a2916597353
31e5da66c8d96352ca5b6fce6fa3bc4e7240bab0 320c68d7be57e5f7b6301b845a18e068b29da864
3218e8d052e01650baae645e7eb92355e56e7b34 325c825566c37679bf09ec463a29c96572640cb9
32d86859097483104620fb04137f906fcebcede3 33b9e082d990f7a23bd6e2046aa4865a89073d6f
3428e239b4c12e790be30e1411a24a50abfb3d13 34efa117c80ab13c789e0282fc9b3abfdc3fb807
350030824c21456dfb680c5ee8d64121530b48b1 3513010f0cc396cd6f1acf15f9c0cab1dc36f451
353d25b75b79ad22b687406f4424ab8f791f01c4 35452a7ea01d7a6df2486ca0441601ca0457dfe3
36070a5d2479030637414668e2f6d9959459aece 3641125e17fb0b439c02d6a60a991158fc70ee9f
367555580baa55f1d18e02bf5cbe742fbd239374 36a7321831cf1886a318f9cbaa9629a41de1798a
3712a7bf515524ce8a98bf30a7dd6b4730de04cf 374e6500a721975919e80075514d3bc8b0e2a0fa
3766b2328e2fdfba60702e01e594eb4478ee2c31 38077af8485cb0e1f52c2d69863e1a4ac6ca1d16
38b70cb636fe44c2983926cd09a9627f07abda67 3905ae21445d6ba6221d96325b3ace18dbf0b777
3905d0c4bcda0e89f1eb3fa94522ccc890360704 390b12383796ab4e6ad5578373dbbf031f1e5eba
39ef06594009ba109da8638e93bba404fe105c4a 39f879fcf852a0ae38a4e27196b59038c2b01da6
3a5f83a0b727cbb1143d6d7951ee3655e15d0f4b 3a61f0ca7aefe695fb028dfbaa7acbc594f260bb
3a73e874afe6130d8425ef31a197263acf9d0b0f 3a8b14607001901e6e2fbd4c8bd495d172f23ba7
3ab80c16f1d86ed6e503de3d23cc35664ec2f172 3bdaa5e47331d918b58d7bf1fee890099630a293
3bff3f5656df4e0f2179265c3fae2252f9b1ae14 3c36d77efa1bbe20463a17ef709deb16d560d4dc
3c3b32dcca1368d6fc74354a0f206cc2e3e3b331 3c58478f8b76db8616bd5a4c8de21988747e684f
3c7cbd1048748455090fc130aa2ce6e499fbd37e 3c8eb13cb684341449f025f15013f7d564a2c6f4
3cc173500a291219f4001ca3bd2d64612768cfe5 3cc65f4ea0b5ebdf2250af221a997556cac90a15
3ce7a2964c1ab46c30b321c21d8fb131f64b4a7a 3d31771285b78bc0f83123e52e9cc9d89b263df7
3dca1e378ba38e174497886cb0453d6427334661 3e0e0ebe462a6bff8d841aa86dad3bcb81283e38
3e6434100e6ecbc114e38b1b1ceffc04cb6f2d58 3e902363268dc7c9a18a8416ff3381616968ccdf
3ee238acfd3451a698c9026bd12d378a1f61cde5 3ef193e2cd215cea63116250aaeffa879e493289
4012ee35acebcb35c76be7a368a684967a064720 4099a62d26987adeac80506fba4fb9ef91c04cee
411315226349cfd140cf1d7a2c46ebfdd67b8332 4151e7c65fbb9ceb331636cb5becce876eddacfa
4170563cb40e8fb8806caa63abb39c47eee9aa1f 419279970f65e461cd3ffb7e68561d250ac641ec
41ee6255e1f3c9aea70528b23803f26ce586293a 424fba5480a00cc23e1403fde748632017554174
42fdeff426d1839cd3abe48934b203e59738e878 4313c90e84d422c4d4a5c5cd7b959bcd65724804
432820d0fc16832108bedfc751bfc1248f2cf7c1 43e18150962622cdd84daf5d46cc6f52d7638ee3
43e3b7b52186593fe8ec3c2ac3f8ebbe103cdd10 44494685bf4eeb8a4d0ab5461977ad92ce3c38a3
449400f0d8ffa3fa1215b70d78134db7e7135479 44a55c3d211576a62cc4354fe4d5643501153ec8
44b2bf9bcc6f8eac64dc59c00119574d90d482d0 459ad32c163a00de0bafa93a56c70bf6f0311c35
45bda26ab02ab160bf147590ab63ccd2520453b5 46349c11118781f5cfa3993203fde136e7aee246
4681171d74726e5b2af0d51870779785ece7a2c8 46c2ddecb385660097e7a91a10992b266d53799d
477356370a9f14908ecd9873117d498c8e248e1a 477bd0b9b1b0740fdda92fc827edff1dd0e526f7
47ca9fce1492ae5e51065ce485bbf9a0c5f384cb 47f148ecc626165de6e7af6366739b2ec5cbf190
48991563a617e3088a1691d012d1e57fb9f88ac7 489b61c34ab16bffe466ebd6d3a40dbe0d681bab
48ee559b132e38408dd4c7ad056217a79dd39b30 49ba13f02957d2d34ac775fe5695d110998ef66a
4a4dd35e78ac4f5e51f0118b65c3e53c530d17d0 4a8d4a3bed90c2b3120b9fb6475035812767ae40
4a9b15bc7eefaf2e4027bdb94ff8c55636ed0cc7 4aa2e8bdd1d67cefdff8db495f8f9988c07c382b
4acf22fb88021b23b4b1c6dd88b0d53b5e42decd 4ad2037476059119524c03356ce9aeeae736e0a0
4b5129285ec932b17886373f04a60c900ab8810d 4b8afb6712f5f9a523e460fdc909d94385877ccb
4c348e23a1c65a303fec3afd107ca916ee6cdbaf 4c4155da059388a4724039fd5e60aaa96965f7c3
4c7a86da8a0cf0da06dc3f89c819d2bd8581eddd 4cca91f6d017dd038130372f52957cf0713657dd
4cefb665a3a36e7575449dcdcd6864276d969917 4d1bf7403de93cfe7ddd2c6cb97c2035f1a034be
4d64cdde5987016541390e9beac29affd5050942 4d9e98d319becc7dc90355637d7f7c88b4e472ee
4e79d2cf1ee1b7daee2c3b4f80f64481dbad8538 4ee9362fa6e76a65cdb8bee7231d18120469eb80
4f08873278b8da5624803099d23c23f324ba8e66 4f0beac9a161c286f7bcab9655b7edc0974ed73c
4f0fe7fb80f7bdf693cc3d974b8f83085cc84679 4f1d1938dd7370971d8985889b83c9bdd1642ba0
4f474526e3e3884b39d65df963713fa64fa0bf71 4fbce744eec79124ea1e3d451952f17d5c713c1e
4fe2fda03cf0b7ab20a3a6e1d4dd6973d5a55149 4fe3c46a5581a61cad63c35123712080ba5b7f85
4ff06ac88f53334f00db2b615d64f35724098fed 50388ddd8cfa80ab9534d777a6b017a9eb6907a5
507f343eed8176d220113d21e7b6f155d14dad1d 509aeb7570f0e324d50c71a370f74ee54092c312
5103154aeb754d4b83ea116f56a3d31fb8ab33b1 5134402499720b405dc4e0c1bf8e3b52c55b6972
518b395b548c787d453b959363248232c8363d69 51bec3d5060c73b8afd5f3664b29ffb3b8838c96
51dab9fbdb9360c042fe999029ddaca5559e4fb6 5267310d43f5dc1a6ee2830b046a2f890e0fa7ed
529103e8bd18337dffd9c5698ffe133ab0d451d8 5296cbe602ca018dd66273ceccf214d4b2a8fe91
52b64009419cc32c89dc1d37de183764b33476a1 52bd7d28b8d520923e86e6978024f463010fa940
52ef3fb2dc4be0bc5fcaf3207b103e3096c676f7 530db526d48520759e971a1eeceaafc283dc0a56
532080a23a3d0c30a9833f234477319c99cbe242 53356f7eaeb515276ce1a42648406ce57db13836
5339ffd4e59004b46957bd5f13a83bbf67a930f0 535972ce4ca7cbb734345542e5e35c5a6ca9ae1c
53f3de80fc3fda98164d1aa9b05e3bfecf8b6b62 54324ade409c63067542846f7d5495f08b4477e1
548adfd4be009ae308c02e4c4d4c3247bc6e6cd3 55bd05c983b8bf3a29c36d3b53ee30cc7bd8dcaf
55c72286ab31641a4a5908c7946794318cbb8e03 5657b2eb81249432624375d9086a24164d0bb8e0
56a0f5d71a83b645852d1bf619b7061483ad6be3 57013d3169ed4d5088a86da7c27cb1bd278cfa6d
5766d1c63959bc3000e3092acea4bad98b8d0d82 58290a70be5d3bdec683bad63cd618f1336f1d6b
58319c3c9f4f0bf19d5d73ef5fa418b9a8ae3144 586c73d0f157ada5d0bda2e9aa313404b77b0f41
58efcaf697a22ddc82b460d335a394ee47dd5fde 59188131811f2183340b2970653278aaf7ef277a
5973875493d49a1c40ab63b0212a99e055104701 59d13b06c0741753655a32b2e6135e3a170fc71d
5a8cf92246ff7623d7587ecbd9a395c759e94a3d 5a8fd4619da02b3dae9b6998c03f688877154589
5b16b5fd23814dace128ca6fd3ff1b22ab06f192 5b2a310d1481ded5d017bf004a0e242a52fd25ef
5b9a067fba6252efcf405bedbe7e411382dc92ee 5be258009617965557756741b9af759a61d04440
5c1bf575ba52f67d4d2e31077a5766e8b4c307eb 5c26a258954d98d0757c5c93fe48f31208f72368
5c86e92c57a343d05d5cc38766249ed447c34d68 5c94631bb33afbb92efd57d8efe633e7bafcc38f
5d278d31382ed06e08a9cd6a82c0075ee62f88e1 5d2ae102339170b5664eb88762bc701da9bb69f4
5d43a92306cbce93713cb4051a14688c55ba0fab 5debfed5467e738a0dcf1d6bd13ec310cc60e32f
5e0601012c0eb91734a0a07dbaa4f880acd62c5e 5e13d17d065d8f2c080a80060364312f39454518
5e566b2ba17222565bd225183cd5b03bd095a52e 5e5a529c6b93470cc2726eb908eb814bfd19a444
5e9a11484c76fecd634756c6367fc3b15b444cb2 5ea1c0b96d2787303d060e6b40de9cb3fc902fb0
5eec100c794f2a4461ab345f83b8eec0ce8bbd35 5faf85ed6c0fbcd3d2a628d7affc4cf86c887985
5fec9263c5fcfc1ae5aa37d295688c77db0318bd 60789db1cf30cc0056ad8cdbf628cbd8d5e689e7
608c9c321457a0bd8f3ecb4c4a53b6fd685d464f 609e70ae7d669939d25e90edd90ff140dc798668
60bc261d91f4738628d5199fc6393c05115e8908 60f2408af64f037a6ca5c03250ecc7105f3c04a2
61fc1275db4ea8f2d608c323e0054a1656f9fa9c 61ff6229313666b89b881e417c967596aac57b89
62026d6199f845100585584bcbaffe80f5c3b81d 62ad3a5f9320fcea6ccd7d0ac08a8ded17c7e30f
62cdd79871c0fd78215be69f4d4ea630e178273d 6395843510c8f90574b487e7cf51d9151450cf6c
63f8c72abae675218373450878749059de20a245 6456a463ddfe84b9a91d4d398a2d757f65cf31cb
648abbb8651f54e40b8408cb1dc4afa8d721f7fb 648caa5da1cead0de82be313b93c19cd888b4dcd
64dd71c93b91aa3bbf2d028dd8da402b471fac4c 653c0aceaec89c707fbf3f3afbf399febefed459
65df7d4c3086585b60cdd8623e3f2d1e1696c977 661532cbee2c5c6a2daab558238e00ecb90f9664
661596721d69a48dc528297500ec88e76f3977a2 6646b4f34a8132701108577daace8e3ded1937bc
66636da666e0cc57404e66aaa285d8414aff1ab4 66c653859680dc9a9a4808ce1235f6648b2e1c6e
67b5ace134cda026df54e002b27dff56159dbad5 67d08548fe18c8eb019bd6892545eca973574019
68a70d013148a04066a149cb8a45092c6d5baed4 68cf459699f891a222fbe9afe0c90bcd3a3fef77
68ecafd299e62161664464a83e2ffc2f9a6099e3 68fab89b6632dc600210e1d45cf40926907f58d2
6920c3b22d1673e71787b4e7f351f1918b2fc97e 692b5595bef7ce6adc3076730c586d83f86aa792
6936bb7ee5fc112d6315cf4ee3f328568d399b3e 693ac351f797566fd278188b6ee5fe0c4e007d96
69758c2c0575e7b221df76dce9ad12d328a6ecad 697b9059ffd6afaf926d5daf67194d67925fe0ea
69d2dfd7ac903535c0b2be65636e01324f4b11a1 69e6d154f0b6b1136cfcb7a2324aa2e8dd28ed9e
6a0bb615339ad983c5ca72b8f9bd765586178286 6a7794af6f1b93ff4614847c653aeae22f464055
6a7a010ab29ab09fc79e0d199222cade753ee505 6afcd4871e74187b27ae330d3f5fa94615be1dd4
6b7f3823ac9e0c743c3a1224a7e311c6520dc908 6bc68527d6d1d9cc04fe1b1077f46ad79b230120
6bf808523b6bad01ca48bd9b14e5f56dded28966 6c160ad26a9831448e6e4cfca5761efb876a1baf
6c19c3ccb3d0c79217d8c4e808e4be3e05c98891 6c226bb06d9f04bdbf94c9ceae8eba89e53874c1
6c30c61369dfa7245f080533099813b233e07d8b 6e0f8b0d4a28641d2abe006c8f52846ecb1c78bb
6e2c587fe61c2db84ea5a30c02a8d85ba1d6706d 6e750005df366c71f66406bdd05bb0cbe0dbf19d
6eb219110fbbcc749dc3fea7a00392f9b6272614 6f03dc42cc35e8a18b2ffe4dd0b1b0967b3e364d
6f085904c367405cf587bc6f7d3f3bc1cc0ef798 6fe2f48b85d9edef6bda8c2db07934b16d1f0c2e
7096e86415d689611dbb071dc60ca186561e6450 70bc6f138524f1cc95d9b39d5334d08762ddabac
70e623c824672d50cd05d96eb18b49ee2c06d1a7 7131936e11b894fc561055859b25e247f66eb891
713606acd3992a28be656e81c2aa6e8fd3a07b83 715f7a96e616c5e3e185e3ae0495f13134e7cd1a
71b7be28b3b1d3ec318c3d259e5ed09e88d7b3b0 71e5b1cc2ff85582d4bc2594c541adc38309c02a
71f55213eb0bc7c6fbc375c397739354a784ad86 72704c5aea513c10c6a61f37e0020b50452ac13f
72e1f195d789eec718d5024423e7bff294402567 72fb606e5ac5afd0ba54d5b37665d2b74d80e90b
734d8e54e249547b511595fc0a7db87a7c93f26e 736353be1825c40288b56cba884cdc13efabf647
73e537a8e75f5117a91d394f916dd192055ff9fb 743caf402767cb2df213b122498a93646641d53a
744397dd1bea336ba616a341c8d8627bb114abf0 7487e7565a7868853e3e2899fa285d0761f2e1bc
74badd4d5082acb54b6a8c673a92541f4fd11dd7 74bc976f85a728fa905124a63108d40f53bb4e6b
74ddd18ff51d76ab3ceaca41b463bb1d49945275 7509b0abbc2e7e88c92e07fdfa44e9d829188b1f
755d4801dcbfeee8e990f32990bfce8ded9103b1 7588cacc526bb953e7cabd9120b1da35c978b17f
75f29a7d3117500511fcd11c878e487e2a78b2ab 761c276e38f10099623b4ee0108ad49d600e966d
762545d92ae3797da82afa8ba39bacf66252922e 764de3e873657d8860c60e382a903e4675ae6f76
76548dab109faf1da02b22cacd073a5e047f64c5 7685a4c145b3157b906ff74bc2e51819acb5a2c2
76a5c98c4e2831f571294201f14842b209bb9aae 76bf328a19c7354cbb0a120b4a374c16369aa1a1
76fa9b80f85de08f4777e84631a64f788ea2fc3a 7792971561f0fb122e7742fc23df26ff9c277e2e
78aa5b25415cf1cd26994cb2280343ab86cd72d9 79620657b658792204ef50c404c3ab9081c35f6c
79b2f4f26d9b9e0566b3ca078086ff44addbc7c2 79e18c46e4fa1ecf67ac9683ad315909e963b698
79e27abfc1f7b785f25851f278d333adcf8d7cd3 79e4854fd815ffefa0d9d82f0bfd015157058d77
7a0f6177e22b41e61b5df7c311d1d04a41fb6b4e 7a58663b087f37af8041c8d3a28229514ec45f21
7aac433568780718dc8d7f45a7fba0a2269e56bd 7ab1d8fe768e1977a0c9b53f4a13cd45e627a080
7ac742e8389487be7374f44863ac4cb391d0c3fa 7b6f49eefdc942e40a62bd22b9518cef54697ae7
7b9c1ecf1ce2d95e8069ec41036354dfe0db7e6f 7bf515de7efe26f3e01a676dcacf15bd1acc84bd
7c0acd94c0ed2f1499ba0e5dcd215fe891036cf6 7c2178bbbf076d02340ab7f3b471058fdddcd710
7c6126985038efd033ea3151a69307b0a12c0f39 7c66d5a463ff3a0da99e37ab5d7b77bf8cfdf0f8
7c9aa5e4481c37eeb582ee4290894173a48599b4 7ca13d9d95d0c50a5d01a9acdfda48266381646d
7ca1a3898c4d3c19f87ec6b022b957de31adedc2 7cb43b52e36549647607fd3b19c1ac3df0b4d34e
7cb8d94eb16b5c39d35ac8afa81fd46e00413136 7cc82bbfb6c4b136ed6829b16b9257086ef615de
7d004271b58d78c9680416b3fa972c8355096ad2 7d0efc39f100f0cee30de2a0f3a7ae878f5821f6
7d4f8a907f7fee48bc1b1232644d37f453435828 7d5967fc7e218334a0c03961e8a82788f6e03b3a
7dacbc0f0ef478ff026835fe52e3894fcabe4000 7de2d5496057c5784e67c146368a02cc31a10fb5
7e1e7a3d3b6b9146932febddca88cebb5619e2fe 7f495d9a61f2d9198e180f2a1d1fcce43a68141a
7f55ace465d1b7a485a75e535795ae0327c7d0e4 7f7ffd5d4030f07d65088f2eb2ccbcebf64a6e72
8090fb941ad54a00e0de4f1e8bdeeffbe69b8ba5 80af7d37255c66dc4d9f5f37d9d1c1bdbdbfec0a
815758075e6dcc1600629d3a4e6a4a23337ee84d 8336c07933284c8e7ade4b8f5096494ba080c391
839ab43411c6414083b0776674ced939558812d0 83ca34a17211e0c68be55f64e8ecd25d1381eb52
8407da7bf79adfb3d9af56ce7a18d6ee28a4560f 85ea768a5f72201f2e1b8d1da990261e4aca0773
8646a545eb691e65e9d2972b79e89873942f86eb 8668efc9f082834c88e0847fbb016994e3cab8fe
8674b69ea5af7fe5d088effda253415b91154654 867bf901037d2fba895d8fbfdd14d949f6e82ee2
8698fb016b7c1e02c535091cbe3229bbf3f76e6b 86a3471ef310ac5f3d69b5b4705cf96e5a04e743
86b1e884dfa80ef867a719763015471e233994c8 86da85d2a128c561949898a948c976c780f5bfd0
87678f14793863b73dca931bb1f9bb13e08a9df4 87850fc31977040364f6e436c4e451395fb91745
8813479a56c33421f6bd14c2d424753e3c150aa3 885b293bfa31b2c11cb4fbcdf51a8aa5924a4720
8863c9c9d54d04413d7fe615cc1a4a25445931bf 886ec8e898adb3ab7b9dc0f17fd59ae42d8d5104
888e4fb6c5e3012eac949ba040d295ce0a11f5e9 89383f4509f5319a2b199ab4440b04e08f73b8c8
89b4b73f1d50f67e2e6785ee8fcc30ae5bd41c2c 89bb195ce66b783640b0a3bf71dc1875e0cb680f
8a0da161222b988e5300c95de129abf3cbbadf54 8a6755197f6b0dc2418656bb061615c5db75812e
8aa82b46b0c0950ffdd6cf6e52427b6fb4aef7c8 8b131bd6a520f3b008c58544160d6eceaf4713e5
8b1876722500dd2141c0d72048eb451c3203c31f 8b73bdb948d7f2dfdc05eae8c31ddfb5ca8d6602
8b885731c892b17d6365e0252a7a40a7fb9519f7 8bae58ccb008249c9e2844167de2a56a06ee2e6b
8bc262ddbe0c36a1ff822c8229b7b4aefdd8ee9b 8c657ff3139ac46d5be32c8fbd5a1c3bb505f14f
8cb05454599e881c09fa349b6c132b1b3a7bb0d5 8d2e3b9b14b99e6397a3533d9cf326e8820cf061
8d33345407705fabab155be1830de587ac412d6b 8d4dc939d980127a23bce8f32dae941ee75bdc8d
8de745b3c0260fb55c12c4a309536c7c7291b1ed 8e20a0a5fee223cfaf3d2ad0ff5de91523a69172
8ec95d902ccffe04bba2089e1d7afc43b88a37bf 8f747f8ba9656e4ae1e442e28ab64cd2e28c9913
8fad9ffba131c0e7b3ebfbf22e77a0681b4a5c42 8fb7e1ed82d48c8bbc1de7622095058e4987016a
9023593ccb51837b245387e39afb3941f58cbe5c 90ed4638cf9ee289baf2545db3d7fc88bbee28a2
91725db7bca398e5279fdd8659a9622d92a2c4e4 918895e8b5c037d8e4c691f611c76a1e51dcf0ae
91aa73adfa02a87bee723e884c7d53c1299e09d0 91e97940d5625679d6eca9793cf7965f279595ad
9255e1f91ce58ded6fe4dacc6b0a2e30c4ba22b6 925dc970d16e08e3f9e81b9bf98056aa3b9098de
931a8aa042b089b046d56f832c4c65834b4343f2 93346883183dbde00ca398b736f316bb56c29ed3
9339655831f22ef915a67a18045bbeb99ae635fe 933fe823efd54545628b76d078adf4ef405e136e
9342b9ae99b54b6c75990b72b01c78e6b994b4d1 93afb2d97c1ce1b91d163e1250341aa69ded04c3
93d0f2e35a51b8a5a1f9ad69dc32cd9ab2f76b39 93de5b91a4a7841e44539e3279dd55c615836a72
9416bddade5b9236da07bb237423086e0e6eb42b 947f99c61955b4161980d93f6ece1e9b5e69196d
947fe87c7d63165fde04ba8a6b76c1363a2a7ac5 94c98fedccd8ea0a4e07a2ceaf271ac460692686
94eddd215b919715b32e7d0d14f4974f77aba677 952516abab6dba1eedd9c4703cc8c1329baa6a67
95e474b742286e20a60485fc3b65a1a6f6676418 962fdce606335605da2aaf7c117586166f7e0d8c
9659b29701199286c048d909db4cb7bf12ddb329 97481d1ebb28989b3c78f06863b31e2fbf8bcbcb
97a8805fd3d503b1710aa997d2fa5f9e5f8b349d 97ff4d111041af1003ce67137cf5ce16806d966e
9967c97cba9b245dcdfabc6b0f3a2d1a8b063bb2 9975c8dbe5502a488dd1c60a0b7bb7dd4f2ce0d5
99a7a3200d67656a96a8e8c64d3552e6d0fbb943 99a927ff9b94d296b332b686ac87aa0ee1e73055
99ab924c8a316ff25a983e8e65f00433a086eef7 9a16311e7a28bd96c50318c36053f87f427936ec
9a39dd8940a8b1c399eed7e4535c787deb0ede37 9a9a828e6d580425b627827ec187943b6d2018a5
9ad97241ffa47c01e4987a4a992fdd50f842eaaf 9addec5588b1aaa8a2d7df1582afd6c32527833f
9b0e1ff747e243affbe6fb68940f4edb28d353f2 9b3dca9967f2dfcd18aa31589b307c6df6d51859
9b40343291d9eb48d4b5f4c099e43b4e61f2e0fa 9bbae15c70f1e0f1439108da294912bb4862f40e
9bbbde0d86b936e73287d2574431bde8b2c203fd 9cda6638e82c5f20da0b35312f67fa0ce8f60b42
9d3d8a394f4c14d5a229343009ffcfa618416269 9d63ce6f7bb50c187456abc91373b2b070012e1c
9d77ce8d410c10419325857e7d841069e5c3e54a 9dcd16d772a55939fa886709ff41f6958567950f
9e2a0d31a4ea41954e41ed8cf599a8e21066948f 9e7f230fb3cbabc29f24c5e2698c3bfa4a8b25b0
9ec8a3416d2d602e461061cd7383aca39777a3ce 9eed5998222817e21187c06c4a5d10c7bde183e9
9ef11ead5816d767e7f6bf15bfd4104e0d6d9e94 9f64a7c3828fea0269b6c05ae978d71e143f7d0f
9f809623037d8b8ede766fa2eabee882aa290942 9f947d4bd41c16a8d67b654e8334201cdfa5f7f0
9fd6118cd18156b66b0cc7ee07dcade8b539585a a10a6cfd58e92379a0748500a16058b4cd4b1d4d
a1230f0192693555298f6c24e8c13de04078a679 a1c82766fc8fee04a11ab84477f766c76c10965b
a201385eac0a93c9c2838c11612e00f8ccf1b97a a23573723c7191c3e24882244cdf210dfc87cd8f
a2a2a7762446225c91ef1bfa17af98d14ecece26 a2c803be75640b392d7fb7ba39ea121586051c60
a31872b59b0339e24f601f5d060424b4c3a472c3 a3269eb565e4670e976b79a32393bbdc9debecb3
a3405193ff12b068bf396b5d3f9a09484b305194 a364c1e4304c9d45d6603a1494d0cab9dfba31ce
a3b53a47e3cda5b6d992bf1723e1f50dd1b72307 a3d2bf248c499378546242cc6600ded3de66f382
a3ed5dd4200e08346e714d896fee1b6861518eb2 a4c8493b30b7d8adac622dfa3592ce57c75cfc4e
a4d6527933d6e55612199dfe1e463762694de822 a5015f6a6b4ace5cc1a694b535bd7e8bf29ac3a2
a55baba9f5e1710d94c316fd83c954e4e3d080d0 a5d1d29561b064601167357c768eecf9abb56165
a627f3d76506c4155d8d639656f5536e8dafcaa2 a645560bba9cab854d0df3bb8ec1473de2359170
a664f93d73f5c6bbc14ba5a18bfbc779fdea6141 a6cc274293ff5a8eca71ecae41c661b1b14b651f
a77a7dfd7b373cbecd35d5eabfe971d0b5438924 a7e8c252169bc685dbe1fe1c6a64115e747f2ca8
a8363d65a75197b0f89e567b537956a403a3b3b0 a8ac234d1c1dc027861bdc7bdad3a73d4936eda6
a8dd4668bc77c74a95d05afd6fee9211067eebd9 a936230b29a445088a53a6f64d0e93cb5f91ab2e
a94d68ded619d3f8526a605e84545890e8b49b62 a96e21cf52ceb20509d4b6999520cfb54269118e
a985af1979848f9ce2693adee493dfac60aef519 aa2e8d5a1c9e235bb9693ff5e417853f64960498
aa3c40cd430d860d64c80be681f5811f377937e1 aa4c123721c1b5e216710f696e297d357c19ff95
aa639a024172876bb9b6dad5e00a180e0dfa4bb8 aae328a1d51cc16c4968c35f081a3300565c4667
ab524b13e0810e48a383d35c18a9b0cd27ed3fc0 ab765980f60b875b14e5060adaa10a56c71abaa7
abee38af2b1a499e660eaa8c764edc352b475eb3 ac48f4cd037fa84f475dc748063da2c6a21003a2
ad0d7fd5eabb294a24e1d42a78b0c9984e65a955 ad17438eb3dfe385fd5e198b8dd55084737ebadb
ad2dcfc82f83158b8e6898f3e097302108bf1ca8 ad64b603b7a1dac18b7246d339abaf43a3642dd3
ae1e671754c75583ff6c3b00e849bb055ce5d628 ae43933ab036aadc4bd50bc8947a37d76609ba7e
ae4a80cbdb2dab297da371b7a85d0b03bf96e2bf ae983580a38dd416e8fb6a95795f1976eecabe62
aeabf589a6832fb6c06c8b46af3862a10f924d42 aeb1606dd4cfd960030613ade9f6f1d42cc31626
af5b5875a53f1cb0d11e57567507ceedc5a52d80 af6a6f8206fe7b915599b65c7a877438eaf23db0
af7844f223fe2cf1a5934ad92f1e2134cb6cbd5d af83c28ff62e330466b581e10ad5164f61c5acd1
b067e9e0ece92ffd6daa6caeed9b4b9b9c6970b1 b08da9824e2b0ef4bb42562871ff3b7dcd9a0878
b093663831715e38d5d60f7eba13a28c11ce2cda b0e59120b6f028914944506f2bb4af8f2ad8ec0b
b10bfe18b11e41dbd63b9c2f2b788e4ba1c2f01e b13de3ac91809ce9680670eecc53331de21d6137
b177eef4a9d9ceae608e94c6061cd55c5f473825 b18410b264ffe822ef00787d96e894e6b18f9ed3
b19447c80676a1cd2e6c196419b2317bdd256924 b1dda0d4ee6899e83f2c4e2fb1e06c3f093661d1
b212ec0b8257f80373a6d9217ca1594ee98e3491 b295f4bd1c9a1139466a89b65d7a65b441351c7c
b2af04ce52fbf588cf215e1bb0c11a064bf81539 b355f72926a8747be69239d24fe2b0819438f953
b3644bc41cd81740570b1966ab86fa64cb9c56ad b37904d19412356a04aa221de47c142d491be24d
b3a6c133d46819a168393aaeb74af9b51a3b349b b412ceef178154218ae795e100777137515a8558
b4bdf70d2b7363aa1afd8b799e98be64562feebc b4fa1ac9e637c8175f40209645ac54fb1fa61dd9
b507a2c55dc63d22dc54217520e8a052f517584a b554cb91460f794e89bfc684fa5ed2433a4ef11b
b55d41db2ebf6d136ccc7aa85658443c61c8f24a b5700e43af3feccf2d9852bcc93f2c9f0f9b0ec5
b6187119e72f6171bb81b078739176d3d5913900 b6976bb1f977bb5d2e962802fe264ef9c738e69e
b69828711023dbfefb9fa802c754245919750907 b70be921a2570501b3d819e764da224f077fd596
b7508085eb4d8aabe1d8f114bb85e5665cf91cb2 b83fbe1b10108dbf69c2a5772ce81fa530b2a5ad
b87b7314785f8b6a6062688a9380297e4683620d b89081cb823a35a8030c58d270bccc4b84340258
b8bf4076ef5813318de449fda0f935f63d85e6f3 b8d202e97f42a93a75fb1d9f7a64f56713d10cab
b9de5301d6fbc56d88ddaf6b940641da01f1c658 ba0ff04d5b6450631909f8bcb3bc59ee9b310208
baf76aa327a8cea603fc1fff9516a0effc006be1 bb1dfce71a21fa11dc21d25c3460f2116980e548
bb38fa6a70e365ddf8e145b0d8ecfffcd3cbf16c bbbec96eea9741644d4e45bcb220b406e29d8ab7
bbf68e495b3362c1f9bbfced96dc77239a9505b8 bc1a444e0d8c012559db4ccb808d05554d0d7bce
bc84fa322005b7e8e69f91ab8d4f04ab88d8e2d0 bcb851ad48e245f32c6221404f67ddeec5484443
bcc3835af50c3962f23a91b7f8de69825d921c73 bcdefc3c7091a6f50c1a52f5bb7c198a17538edb
bcf6ee799b42e0b0c49ffeeb3370dd0723b6a2f0 bd40e7676e7e0262cefc010ed469c6cb49357793
bd5184b18023e32849c91c1252f821bf969f8aff bd8b5287b30bfc427eca92ef0bb7de5ec002394c
bda4f18e37cddd5089819ac26af5e1f9c4325f60 bded7eb6a533d237e6142bfc8c4a5f73e6ab7c7c
bdf605bb1a265fe3c693823b2f68c13291a31cde be36785042e529d440ab2d4fac6e8b9f348d9c5e
bebdb7cbd3177fb81a394058a2907ea1dd68bb3a bf78910f73f68f0d2c6348849c1a3f1cf7230131
bf7bfa3e0d5f434d4c8ff062600bb674194e9f03 bf9a453fd842385d34f47979cdc0e2c868d48c95
c054ca355e7c9fdfe49a015d22c57b11387ba49f c14efbae802a5409d4d333f862747ac369fdc580
c1632114913e8ad66c935bb03d60b4681d1bc600 c1d73a48b5f764bd94ccccc61da7a839f8d11516
c2541d7142048201b45024231a818e628fe934a8 c2c4baa98f75145a8c1353e52be2e6da1e498bee
c2c7fb80d215c7f73e5b4cc936306ab72b856124 c3733e00cd41d38c623772422ebfe0a7eac6126f
c3821642f90c442dca898bc7a94709ac9f7472b7 c3a593222417b17ab94efa9fa4c4e3ac7e810e9c
c3cd662b661068e72be2c3b4d7afb7ea6ac1159b c42e0904c54e9aaf40c6f581026b9f92867bf344
c44b265366087d1dd47f29dbfa5164af478e5815 c4748dd151c55a14d7ad29dcef3e0389950112bf
c4bfda5a2cd259a1791c075ef732463bc7809e31 c4c33e488524aa6f93947e19ddc5d934bd97f4be
c546ac3d4c55fc87128d4a6cb766610d52fb2ad0 c56fe94852da146a007277f90cbafeaf7715b671
c59b19776fa5e898543b140b055c124b7d59836e c5a247bbee757aa65deee1a174bb6d9ce313098b
c6122fad022ad2b0c8f73b723507a88c3b9847c4 c6699f744492cc737ac44355a78a104b2818e3a1
c67c31db6f69694f7e696a1617585f6506baa701 c6a8c14b693c32283a9610df8ca0fc2b9d121a5f
c6f2c7eeab8af4120d5d0cdd461b744c958e7f65 c7613bf725ea5f705bc00917bb47c0b908700b07
c76c1161cf41a82ab4935e614e22895f25aa768c c7f1d812fba1e29d366aaec366ee9299fa46605c
c85d7cf39b3a300b80cb41112df2d03810f815ef c8ad1967e13c21d27dde5b89073b415595e4f11b
c8c8cf15a77eb422c404eb9a59cfb9570f541b76 c8f10470c16ee7ee2a39dff198ff7e6f84604c6c
c9283e336a94bef580c300ee792fe7f53eea29fa c932cba5ebec7e0d4cf45fb304b6c053bb7f5ca8
c95dbde5019b8f5942e22d033054ee8f5e8769db caaa6ef8f891e683eb8461ad28e81ef0bae713fb
cadbf3b7e91a9dabe2c5934709e6a3fc80ff6e8b cae50d1b1d380dec2d052955f27d03727b41a35f
cb016eb52d056498e1ab63a130d770a87aa3140b cb5e063d7be6b18d4bfb83ddf91ad1a8155b5744
cb7653eb026a933329cc974faf36cdacc5fc4250 cb86c127033f130053209005deafec256b96a7fe
cbfb15d220f535464dc6f0de1602629055cc5b20 cc40d60b482f1c08a9407b5f11637d6664527e30
cc52b5a2b71a6e7e4a5fac84e84d03befaed73d7 cd8db89844ec9ec80562bc1cd1bbe233163b2ac6
cdd606e153320b8a6996a11b15158c8be5dabac6 ce2e94be4832dd3dd818c4ec2a0b8cb9e5c77f0b
cf910de032f761a432e7c53b55a6534b645693be cff3c1566228158acbf6cb710dbdf4ba4c5db91f
d037374ba07470420b93f1d4504ba95efde55cee d06391d2859ce4385ac88780426b10e4f95b2285
d084375e093dc90f248c66f151ebf02bffc1792f d0c3fbce821d5f02e20317d56f624a1c06f89e85
d10385a30081233f315eda98a9da5440c9009352 d136f30375bd3fde92e8d3bae8288a3545b30a5d
d1bdc2c087da9b1ad6a62971e720dba988e7c5d7 d1e1148e6b83bdfd7e914ed12ba722370e1998b4
d1e9566507b80b0c32b8892a49e8d4b09aaf0df1 d204841a6108a9fc85bfd6d372058f0d498e9804
d26a813b8b5f9dce6f20c226fabe64d4bd83659a d2953a3370e06535b10fb4ab3a09a4a64645076e
d361a90fbab255234404fb2c28e0ab0c25887507 d3fe85ea31f1b295da1589a02889d0856ba39af4
d46d84efe8a2e49f8f37210825a059173b81b6f7 d4aed92753ea66ff908c9d71fcb387e7ac3938d4
d4b049ffb6aabdbff600b68d1808bf90838491be d4cdbc01c7942ead708fd76b7965bd98afdbd15b
d4da605576a08307d60b7405102d7d858b83c8a1 d576573408b0c044e2e08c608e33105d2919dbbe
d5a2ddd7a48f5229b22dcc599aad48c01cf5e1d1 d5d6e7c1b4f4855561a631ef5c50467f80bf96ad
d5ef8df03d3ddb49541c4f3733a815609ab892c3 d64cce4f28d733ad3bd70b843c2dec9251f46159
d66b662bebc1b8207d6934703128ef704d707f8f d67d7b68d71fe2fff3b137e982a48e56abfc9c30
d68ca300d27823f5df11c7aeb15dab3d7448129c d69a088e3421122b2d6ed75106d8c52b8b9148e5
d6a1620acb079e6a911c0f9024b6afb068ea2a26 d6d95cdaab8001b17d1028abebb4e5baf5cf57f5
d7008f9bcb9b1955de39ab786727710174c324a2 d79ac73c85ab51b06cd6541f3770a684e6d50ee8
d7f331581a59fe6214c98ab463ad3cb788042e69 d8178304317e0a2dee8a30d68bd6d8c18a136810
d82eedb82e895217113e366bd26528e5920c4db1 d86bd0122249669cc731ee2fe122361eb2ea46a4
d8c8ddfbcedf5464ac0dc629033fa8e986fffc87 d8cd433e0bee6e816fb398720258f26633ee2c94
d8da367948453400ef8ea391a7a5cb8b22fc8672 d93bc2ae7243c5cd4c740fc4b3b88577025b2741
d961cd137291e6f2f86916d8de1b795263f78e41 d994876bccae9ef340b016915ffcd8d2291b8d14
d9ced9719300f4c9eb88eb729e8bb957d2b55fc3 d9e13482650f309619141337deecf86178d86668
da1d76c42ad647dc748f69132a17c6d90422dd94 da25da7ca587d0d9496e4665309dc1b8699d3b4d
da6520c57405efbbe3cd2a15737c2a53e61057b1 da83b04dc46d179eab53045c01b0c2bfdb5be629
daa87b6337c65f76a1c58c885a75af6e078109b0 dab367581d63ef2f0fd5713a278cc904211dbe8d
db445d7b261b21018e17810f5d543009defd9947 db87065b8faf797fbf59adfbbbab8255c692690a
dcc34be8432cb39c276d673f947c863e70540f12 dce6a6d14d96f94b3cba1790b2bdfc088e2bb84e
dd9204c531abdaf23520269d774f5cd9f89c9d42 dda14af07f862ee459a803e4e888c286b1f6bd57
de26fe68ba1741f34da5c98b3c3178ae91886e0b de2e4b294a5181b28f8d54663641de416ed02978
de4a035e6aeda4934713b9697e12c8f54d160296 de594772d65f60114677608049008d502c734933
de6ae46d58a4b8b1d2db303307a4851695430fea defa74fd3d143361383385626bcd427d3cdcfe5a
df2ec210419c8dbe471ca721d8366019d715fa4b df2f35cc0f25d6d895b792ddd61560049bb78c47
dfa1c8573e509e1239bcb8b2c346279ed183f670 dfa5047fb482a33010426bddbf90f4bed2be637a
e022e0e5b4285fcb03f28a9483b15e649ff20c0a e02774eba4da20f718a4a292562ba0907e614c07
e0716899d5fa437c0f9cb3b77eaba31273cb3f4a e08bf0f0550af19ee48435c9d58bd3b330ff871e
e0bdf127b27d174720ffce9f9cb99a7e637810cd e0edc79b70e970060a28c0c5e1b9ee64930fe254
e14b54332f63238bb44dbfe016c88d0db07b7f2b e1ca23f3cb8bcad27cd5b05f4ca9bdfcc086c5a3
e1d107065df49dc5eade41fc731fab79144f7658 e2916dd618de0882453d0fb5c71b78f495a9dc92
e2d497aebd409f006120c18f0d745e85f8903215 e3827d4f359a8e845b721092c5fbf69681b97ff4
e3b7553ffdcbb97861b777ce5b9be9fa8b119fca e3ef9358d6690220c21a9b32924af9b3f70cb890
e4266bf406a41c4ac75294032670bdfb70094d46 e4315491d1c935d4c02b684bee43ce94d518bfb8
e4d7ec1fa2f1a6764415433081309708ae165075 e55fcc65f3a06b456b378e5b565760663c47754f
e576fbc6e71ff19b7458014dbf127a7f206b992c e5e70bc53a1c23a7b83ed902d9879868292cf5d9
e601ab8f2c4c8e85020f578324f2baff7b7bf6db e60bbfa90a85b609ddd6cac7b1b8ef33131eba15
e6177ac9da784bd9e3c770f87155726e59b7cb5e e61cb5df2c12b15db2f905da0c5138658eb49d11
e62a082e16600e412b07bdcda7f9b21d636ef953 e6437ebeea2756ada5dd1ae1d5e50208a08581d2
e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 e6f17882aa069433d0610e07074424970d88f840
e6fc25844b43e4ebbe2a8b7c185b12a0173f47ba e73f298a5a82e6b6dc6c8fa58f519eb5c044c0d2
e75b4bf215ff16e532096b7f7b492252362e9796 e76c1de2b4d9ad494d6b1cb16143475c8e852bcd
e7d380fcb9881e3063243aaa149e85be3cd0a914 e85e148250df7989d58f8e8e4891a3d1fff3de36
e866558971f4399174e95166e1ab70d9299bce43 e86fbfa0dd3b3c4e85af0c83b0d0b62866e32730
e87f8c1ecb70e6c79a73f3617f09745e635f3515 e8e9a726ad688afc447214cbdc52b96675513307
e8eb250a510f7a90f09343f40799dac8e0206f5a e945fb1a87bc06b68a77aaffc6b4859850cf0484
e95c407ab3dad56cb18e597a62edf47a3d7a83e1 e95c8ffdfc770ca14799b5f1897cb4e54554fe87
e9be2561b92f747e79b9b67a6029477779c96cd3 e9fab781c07ebcbef6a4a335a1749bbfc4a79fd5
ea0cd8f365453bcb61b2682981299ffe64ec58c8 ea12762c9f5c19234b4fa1b966f9effde130bb7f
ea19ffa3f67b842771f228f0f8c596adec6b05f1 ea7ab1d0b43a53b41f67875c40004f8affa0dbc7
ea86bc4f2c035b58fed30d16368934cc0737c2ec ea8f9edd73ca9fc8076c0978983babcd94969961
eaef4ad5a2468110e9ce4b33776f00b65d4a2699 eb068252c0b6ef32627410c2130c4fbd5582067b
ebbf89bfa86b252dbdb6ff94fd4a4c01ba6357f4 ebc3a0aa3b6b3e02d7d94b070e2a72f07cd7a8d9
ebd41e1720f2a28e30ffb567c4c474836317c4d0 ebf3842bd9a51d7498de9aedcef4cf1a2fcb17be
ec29b2f0e0be97ea633103cb92fd9fa25b588a4f ec9f1dfef1cffd27fa54efa0601f11f930fc630f
ecab3ec558af7c31e0106de50fd434e1c3a6edfd ecd7c48de5cb22ca19fa7a4b43fd7c990276e613
ed3732de2ff42cbde7345db99077cba4a91be4aa ed3ec55845f4bf5c3a543bb92b7ccea7ba4698ca
ed55a5dae39f48030332b09a3089d09e9a395e23 ee002bd112e1358182301319589a65decfe58b07
ee3463dd9cf810026add733def1e6c3fa9730dd3 ee91dbb416a6229c665c2b63481eb8a534c608ad
ef00111fa2dfe81d3022bc68b4880f87c84f7c2c ef491414db973d46da7a7599c801fa165e075b58
f0b036d6797c8f1fd9e1f976e30539e6521e0add f0c2c8c6c14b1e22c894c902f2578546378e22d4
f1519a0d3e863504e4471c4870c06b11c6d6415e f15d3260189ab997f5b960de485ad4d922c44c5b
f17261a83be6aaf597925adfcc7e91a937c3b2b6 f1a9a01f76ab10c1e50e3fda34f56aabfd913036
f1d011f9804e5ddd4d1074c955670cc8b5f9e6eb f253b602adc3a28a426581d9e5b4d708c62f8755
f25a9601a94f22ddd7d37c78fc3101899b786c2d f288f9254aa7e539109ecb8713383480e02ded0c
f2fd5d90da341b4c8acf59633164bec309ea8713 f34feea0bae1cd3d28a83755cfd6cd8d4dbb019d
f3aeed1a3950e2f179f58dc485b08d4dafb3ed36 f3c0c62cbdb7ce5f57bb86a023d2024f154c3465
f3f8921615113a374a44f03407637a7a3395d035 f41946312d56978569392a54e86f7e301bb7b029
f4ec2fc8763c98757a5d7e07d5b464ce3e0ba2e4 f521d8d4f6cc851a5872d2f474242e7e5710294c
f55c39d84a985ef307ba9ca8554a3893df2cde68 f58cde0502cf1ca4570a960308c414870dc58d19
f5983ad780a1c7b2cd534bfb7f49f9eae94bf5af f5ceda70e6814ba3f86dd4b9117aba3a76a04b3a
f66bb016b4e9265f443f2d3e545a5f24221d260b f69c45ebe29e9262b31c53612d323a5b4d8fca41
f6d073b2a95b60b126fff83fa07c7204094a5b54 f6e06fcb2c17e5af26c7460506d2bb871540bdb6
f7042861b741c353e989fc0f390a525bd1604a45 f77418ce26d9e0674a7564fb4260b054e8e5d91f
f77bccc8318d934d81e970d78cc8106262db610c f7b563dd372ed086751c6090dc0360b232625592
f819db962914213fca9f1378ad36d4d4959a5862 f83473b4d42a41b5130a9c05e822462deae5fbc8
f85468689ec0608d88e814cc01e362ac55f2ff2a f8e29331c181ad8039e26312fdb4f7e2b18a1080
f9a5ea437f91509c1dc0bb2161418c7c781f6ccd fa26d6a306c9894adfa2e6f74458722e4b991ae6
fa5125a637f0a36ce192e754b7f2d045fcc25838 fa72b6dc6d0718cf43d6f49232e0a48ab26ae4c6
fabc2691764b619cb0ffbcaa4260d9247cd4a872 faf0e3ae4946436bbc05ece2889e081bd9e441b7
fb182f01b32db9257a91783bcbdf250beceed895 fb7c4f63d17566f227a106f4aeab8c31942fe28c
fbb2c962bf37f3efeae9ade0e7730a9fb64015e9 fbc82c68dd2493e547e45b2fd948638cd325eb93
fc0dd5e578a66f50603fcdca9d551393132df71c fc4f062a6010673b2ad01c0b9b464e6855ef9fa9
fc7b27c0bd97d1ae9b4933ce6416a98407a3b73c fce623f1ddb84c463463ecb289ee65b09ef7f5ee
fd54c7afd9800da2b69c5f5e710cb84d65997168 fd5bc69b5dedd824937d44ce6a1097066cbcc936
fd5cec3916905fc791b96ada3b77b019e8a5fa8f fd6b3aee187050e3b5327f6550700cb1a2ec62d2
fdf778b935500bdadd709f9343a67048ffac2bd1 fe232681fab0f098c261e04d51bff4900b0d05f1
fecc35bb262a49f94280548b191d2260f556e510 ffe814845e8f5af6799123ac713826df1e1d3f54
"""
_TRANCHE4 = """
0026dcc86cdce39c5ec7f1777656f75c22853591 01c9f247f18a9f88065dd9cbc73e6e8464679dc2
04580c5104eaa4cf7eaa5fc32614582442f538e1 0ef6c2591da8a89186d066b3387c09343fdeb374
1053a9575c61ce162e8965326c29a6c73c53928f 14bb9fc07bf65e59e3f412ac7270ffb734a30069
1a32cbe7191d1d353801a6827ee3cefef1c001c4 1a927660cf7a4c0c12eaad4a3409f6fe131909d9
1ab0fd9dd2c6701197f2e0ab18401cafb76a090d 1cb44de4a0ec25b69266e644e7c562c4fdf49655
1db810b428d4cb3c571da8e776bc3d5dab477e6a 275e6040a14480b8538a8afdc9366be2a135d347
3070898ea830425c84026a77b81099ff014e6c56 324863d5ddf4a1f830c2d1ed8f49a8399f5a8b3e
354bd7ce18119da451883ab5189010a5113ffa16 37831abfdea676d6de5dfd13a104501e028450eb
3873ba62324e7d72397f9f9ade9ec18f84e75475 3b9fe1e90e9edae47a5bf400a8914f13273354fd
3f4e02f983e5b9e8db8136f4777cc6e8c20eab44 3fa2a3a0fd08be5f797d16f43ae4e3e3162265f2
436e8c21ae6c2a4f84f71e2aad3e0ee7d0b9da2b 467c0b4cb23e8f06784d87dd17b5eb2a33cb3f7b
49246652408b787d94947f0829ae1c24fcfac5e9 4d15b09700186f6ffd9e16379e87c71c326bbc11
576af944d2e6c638bb5f9c760552fa5a4ce4574d 5aec2b905f782b7772c11c8e05f93f8b489c4c9a
62b606b41ce89251c12bb2556af2a41eafda99ce 65c3950876df1ff078f337cd986f499871a71572
67fcd3eb36f11fefad4e1f56deb8d1c5a3e3fb84 6959ced4c327ebb800cf6d463a049e4066e37288
6a3eedb936eca546902471e216712b7cd883e8b3 6a9b117d89a186161abd7460bcfba02ed650514a
72d698f3749d126baec7eb7ccac00054462373f4 739bdbbfd0419b499056670c59b221b4147ac295
73da3bda7e21b464a7bbacb0843dcc2bcd221211 7e886e50d645b1f094e3e7f66e5a97ac9d1fb92d
824e55d0b185c7d1ff2e6e1f7832eac961355733 8c8eb522623ee4c5da1d4ab9e40e10c20fd0bf69
8cdf3a83f78059d81a701c2e4951e54f3a2b06bd 8d6fa9e61772a05b43161ff970762fc818a60b59
8efa6158547fb0e5d7cc483ef38c0badbce67e1e 93c89b366d421a5d4c5488a9bb8bced800fe6b6a
952ef0b56201051bec8198ef4795d28a66eb923b 9fc229f8779dff80ebcc891d72fb208c08d99fb5
a02b3cc158c2875d620d81d51ab075b20e020009 aaecdece5184723fe66e0514a971befd15e9aa65
ac3174ce0d156b215466955bb3fd0e9dc8d03461 b0d646c176108319e33aa4870c0db7541dc2c59e
b41736d4375cca5dfa934c38f057bc979910df22 c03a59557e763834731a41b84f012ca374bc6b22
c13f556a418ba1d9067598fb16e0d4a494538af3 c697b82b8a7d6719d78dfc74bc8183c85fa12255
cbef6d1a265caf59a269e05f79763925c609d17c cf8f6b77103ae28f998075d9f6b2bdaa7b1d5024
dc6c77d1f4b8326fcea095103c5cb98295f4fad7 df74d4701ed3e8f9edf8b158779623943de0aceb
e684897da41b1c3d066b880194c9beb87a19b7ad e8fc508c75e1fc079ef401517cdf0bf5fd6273a7
e9d77b4d665a1cc110aeff38e4ecba74d0bf501b eee518d465ac2002491e6186a146c8f1267ea038
f4501a2d2a2267998f9608ffd7b40e7e34080815 f61e6a1ed03c20d81ea374cfb39353af0cb53990
f673d3cee0cc7d46fa056da5973f2060f399774a f77f9011d268fde7956eea23a8b43752b5f96778
f83b96d33b07b0d3c680e4176a310ddf5f9c5558 febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3
"""
TRANCHE_MEMBERS = {2: frozenset(_TRANCHE2.split()), 4: frozenset(_TRANCHE4.split())}
TRANCHE_PINS = {2: (920, '3e1800891ab153d53046f742f2e5557f36c2febfd1508c7039baa67b22cf937f'),
                4: (66, 'e05c857702a55756c8d6dbc8fed29c4d2ac94b010bba745c1e23172fbd4add47')}
ERRATA = 'verification/audits/provenance-errata/errata.json'
TOKENS = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat[_]|AKIA[0-9A-Z]{16}|-{5}BEGIN|bearer [a-z0-9]'
                    r'|x-access-toke[n]|[?&](sig|signature|sv|se|token)=|passw(or)?d\s*[:=]|api[_-]?key\s*[:=]'
                    r'|private[_-]?key|xox[baprs]-[A-Za-z0-9-]{10,}|sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{35}', re.I)
IPV4 = re.compile(r'(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])')
EMAIL_ANY = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
# the union is check_retention.py's SECRET pattern (its R5) plus four token shapes
SECRET = re.compile(TOKENS.pattern + r'|' + IPV4.pattern + r'|' + EMAIL_ANY.pattern, re.I)
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})')
RESERVED = re.compile(r'(^|\.)(example\.(com|org|net|invalid)|[a-z0-9-]+\.(test|invalid))$', re.I)
SIG_BEGIN = re.compile(r'^gpgsig(-sha256)? -{5}BEGIN (SSH|PGP) SIGNATURE-{5}$')


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def git_id(typ, content):
    return hashlib.sha1(typ.encode() + b' %d\0' % len(content) + content).hexdigest()


def tree_entries(data):
    out, i = [], 0
    while i < len(data):
        sp = data.index(b' ', i)
        nul = data.index(b'\0', sp)
        out.append((data[i:sp].decode(), data[sp + 1:nul].decode('utf-8', 'surrogateescape'), data[nul + 1:nul + 21].hex()))
        i = nul + 21
    return out


def commit_fields(data):
    head = data.split(b'\n\n', 1)[0].decode('utf-8', 'surrogateescape').split('\n')
    tree = next(l[5:] for l in head if l.startswith('tree '))
    return tree, [l[7:] for l in head if l.startswith('parent ')]


def read_stored(objdir, e, F):
    """Content bytes of a stored entry, or None (after recording the failure)."""
    path = os.path.join(objdir, e['file'])
    try:
        body = open(path, 'rb').read()
    except OSError:
        F('O1 %s: stored file %s is missing' % (e['oid'][:12], e['file']))
        return None
    if len(body) != e.get('bytes') or sha256(body) != e.get('sha256'):
        F('O1 %s: %s does not have its recorded size and sha256' % (e['oid'][:12], e['file']))
        return None
    if e['form'] == 'zlib':
        try:
            full = zlib.decompress(body)
        except zlib.error:
            F('O1 %s: %s is not a zlib stream' % (e['oid'][:12], e['file']))
            return None
        hdr, _, content = full.partition(b'\0')
        if hdr != e['type'].encode() + b' %d' % len(content):
            F('O1 %s: %s has the header %r' % (e['oid'][:12], e['file'], hdr[:40]))
            return None
    else:
        content = body
    if git_id(e['type'], content) != e['oid']:
        F('O1 %s: the content of %s hashes to %s' % (e['oid'][:12], e['file'], git_id(e['type'], content)[:12]))
        return None
    return content


LOCAL = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._%+-')
DOMAIN = re.compile(r'[A-Za-z0-9.-]+\.[A-Za-z]{2,}')


def candidates(text):
    """(offset, match) of every secret-pattern match: the token shapes, IPv4 addresses and e-mail addresses (found
    from each '@', which is the same set SECRET finds, without its cost on long texts)."""
    for m in TOKENS.finditer(text):
        yield m.start(), m.group(0)
    for m in IPV4.finditer(text):
        yield m.start(), m.group(0)
    k = text.find('@')
    while k != -1:
        a = k
        while a > 0 and text[a - 1] in LOCAL:
            a -= 1
        m = DOMAIN.match(text, k + 1)
        if a < k and m:
            yield a, text[a:m.end()]
        k = text.find('@', k + 1)


# Within one self-test run, the O6 verdict on a text is memoised under the sha256 of the text itself, as decoded in
# that check, and of the identity digests: the scan is a function of these alone, so a mutated byte or manifest
# is a new key and is scanned afresh. Nothing is keyed by an object id. None outside a self-test run.
_SCAN_MEMO = None
# Within one self-test run, the lookups that depend only on this repository's history, keyed by the base and HEAD.
_HISTORY_MEMO = None


def scan_text(label, text, is_commit, idents, F):
    """O6: report the first line with a match that no declared exemption covers."""
    if _SCAN_MEMO is None:
        n = first_unexempt_line(text, is_commit, idents)
    else:
        key = (sha256(text.encode('utf-8', 'surrogatepass')), is_commit, sha256(json.dumps(sorted(idents)).encode()))
        if key not in _SCAN_MEMO:
            _SCAN_MEMO[key] = first_unexempt_line(text, is_commit, idents)
        n = _SCAN_MEMO[key]
    if n is not None:
        F('O6 %s:%d matches a secret pattern' % (label, n + 1))


def first_unexempt_line(text, is_commit, idents):
    """The index of the first line with a match that no declared exemption covers, or None."""
    starts = [0] + [m.end() for m in re.finditer('\n', text)]
    lines = text.split('\n')
    exempt = set()
    if is_commit:                                   # header lines: identities and the signature block
        insig = False
        for n, l in enumerate(lines):
            if l == '':
                body = n + 1
                break
            if insig:
                exempt.add(n)
                insig = not l.strip().startswith('-----END')
            elif SIG_BEGIN.match(l):
                exempt.add(n)
                insig = True
            elif re.match(r'(author|committer|tagger) ', l):
                m = re.search(r'<([^>]*)>', l)
                if m and sha256(m.group(1).encode()) in idents and not TOKENS.search(l) and not IPV4.search(l) \
                        and l.count('@') == 1:
                    exempt.add(n)
        else:
            body = len(lines)
        for n in range(body, len(lines)):
            l = lines[n]
            if l.lower().startswith('co-authored-by:'):
                m = re.search(r'<([^>]*)>', l)
                if m and sha256(m.group(1).encode()) in idents and l.count('@') == 1 and not TOKENS.search(l) \
                        and not IPV4.search(l):
                    exempt.add(n)
    for off, mt in sorted(candidates(text)):
        n = bisect.bisect_right(starts, off) - 1
        if n in exempt:
            continue
        em = EMAIL.fullmatch(mt)
        if em and RESERVED.search(em.group(1)):
            continue
        return n
    return None


ARCHIVE_REL = os.path.relpath(HERE, ROOT).replace(os.sep, '/')
HEXWORD = re.compile(r'(?<![0-9A-Fa-f])[0-9a-f]{7,40}(?![0-9A-Fa-f])')
# a hex word of any length and either case: the words the citation rule reads as heads, case-folded
HEXANY = re.compile(r'(?<![0-9A-Fa-f])[0-9A-Fa-f]{7,}(?![0-9A-Fa-f])')
RUNLIKE = re.compile(r'(?<![0-9])[0-9]{9,20}(?![0-9])')
PENDING_KEYS = {'pull_request', 'round', 'record', 'note', 'run', 'lines', 'tokens'}
# what joins a run to the rest of an identifier or file name, and what it joins it to
JOINERS = frozenset('-_.')
LETTERS = frozenset(string.ascii_letters)
ALNUM = frozenset(string.ascii_letters + string.digits)


def id_forms(oid, line):
    """The forms of oid that line holds: hex words of 7 to 40 digits that are prefixes of oid (a word of decimal
    digits alone counts only at 40, so a run number is never read as an abbreviated id)."""
    return [w for w in HEXWORD.findall(line) if oid.startswith(w) and (len(w) == 40 or not w.isdigit())]


def other_ids(oid, line):
    """The hex words of line that name another commit, compared case-folded: a 40-digit word that is not oid, a
    shorter one, not all decimal, that is not a prefix of it, and any word of 41 to 63 digits (no commit id or
    sha256 has that length, and it can hold a 40-digit id). A word of 64 digits or more is an opaque value and
    names no head."""
    out = []
    for w in HEXANY.findall(line):
        lw = w.lower()
        if len(w) < 64 and (len(w) > 40 or (lw != oid if len(w) == 40 else not w.isdigit() and not oid.startswith(lw))):
            out.append(w)
    return out


def run_word(run):
    """run as a whole word: no digit or letter beside it, so it never matches inside a longer number or hex word."""
    return re.compile(r'(?<![0-9A-Za-z])%s(?![0-9A-Za-z])' % re.escape(run))


def head_rule(oid, L, n):
    """None if lines n-1..n+1 of L state oid as the head of the run on line n: every hex id word on them is a form
    of oid and the full id is among them; otherwise the reason."""
    win = [L[k - 1] for k in (n - 1, n, n + 1) if 1 <= k <= len(L)]
    bad = sorted({w for l in win for w in other_ids(oid, l)})
    if bad:
        return 'names another head beside the run on line %d (%s)' % (n, ', '.join(bad))
    if not any(oid in HEXWORD.findall(l) for l in win):
        return 'does not state the full id beside the run on line %d' % n
    return None


def run_occurrences(run, line):
    """Each occurrence of run in line, matched with no digit beside it (as R13 has always matched a run): 'free',
    or 'embedded' when an ASCII letter stands beside it, or a joiner (- _ .) that is itself beside an ASCII letter
    or digit, so that the run is part of one identifier or file name."""
    out = []
    for m in re.finditer(r'(?<![0-9])%s(?![0-9])' % re.escape(run), line):
        s, e = m.start(), m.end()
        b = line[s - 1] if s >= 1 else ''
        b2 = line[s - 2] if s >= 2 else ''
        a, a2 = line[e:e + 1], line[e + 1:e + 2]
        out.append('embedded' if b in LETTERS or a in LETTERS or (b in JOINERS and b2 in ALNUM) or
                   (a in JOINERS and a2 in ALNUM) else 'free')
    return out


def run_line_class(run, line):
    """'free' if line cites run free-standing, 'embedded' if it names run only embedded, None if it does not."""
    occ = run_occurrences(run, line) if run in line else []
    return None if not occ else 'free' if 'free' in occ else 'embedded'


def embedded_rule(oid, L, n):
    """None if no hex id word on lines n-1..n+1 of L names another head beside the embedded mention of the run on
    line n; otherwise the reason."""
    win = [L[k - 1] for k in (n - 1, n, n + 1) if 1 <= k <= len(L)]
    bad = sorted({w for l in win for w in other_ids(oid, l)})
    return 'names another head beside the run\'s embedded mention on line %d (%s)' % (n, ', '.join(bad)) if bad else None


def run_citations(oid, run, L):
    """The citation rule, shared by O10, O7 and R13 (check_retention.py loads it from this file): (free, embedded,
    reason). free are the lines of L that cite run free-standing, its citations, each held to the head rule;
    embedded the lines that name run only embedded, which are not citations and are held to embedded_rule; reason
    is the first line's failure, or None."""
    free, emb = [], []
    for n, l in enumerate(L, 1):
        c = run_line_class(run, l)
        if c:
            (free if c == 'free' else emb).append(n)
    for n in sorted(free + emb):
        r = head_rule(oid, L, n) if n in free else embedded_rule(oid, L, n)
        if r:
            return free, emb, r
    return free, emb, None


def ci_head(root, run):
    """(ok, head): the head commit of run as retained under ci/<run>/run.json; (True, None) when the run is not
    retained there; (False, reason) when the file exists and is not readable JSON naming a head commit."""
    p = os.path.join(root, ARCHIVE_REL, 'ci', run, 'run.json')
    if not os.path.lexists(p):
        return True, None
    try:
        h = json.load(open(p, encoding='utf-8')).get('head_sha')
    except (OSError, ValueError, AttributeError):
        return False, 'ci/%s/run.json is not readable JSON' % run
    if not isinstance(h, str) or not re.fullmatch(r'[0-9a-f]{40}', h):
        return False, 'ci/%s/run.json names no head commit' % run
    return True, h


def pending_citation(oid, a, root, F):
    """O10 for an entry that records awaiting_citation: ('pending', None) while its record is not in the tree,
    ('eligible', (citing lines, run lines)) once the record is in the tree and cites it as the entry names, and None
    after recording a failure."""
    rec = a.get('record') if isinstance(a, dict) else None
    run, lines, toks = (a.get(k) for k in ('run', 'lines', 'tokens')) if isinstance(a, dict) else (None,) * 3
    if not isinstance(a, dict) or not set(a) <= PENDING_KEYS or type(a.get('pull_request')) is not int or \
            not isinstance(a.get('round'), str) or not a['round'] or not isinstance(rec, str) or \
            not rec.endswith('.md') or rec.startswith('/') or '..' in rec.split('/') or \
            (rec + '/').startswith(ARCHIVE_REL + '/') or \
            not (isinstance(run, str) and re.fullmatch(r'[0-9]{1,20}', run)) or \
            not (lines is None or isinstance(lines, list) and lines and len(set(lines)) == len(lines) and
                 all(type(n) is int and n > 0 for n in lines)) or \
            not (toks is None or isinstance(toks, list) and toks and
                 all(isinstance(t, str) and id_forms(oid, t) == [t] for t in toks)):
        F('O10 %s: its pending citation is malformed (pull request, round, a record outside the archive, run, lines '
          'or id forms)' % oid[:12])
        return None
    ok, rhead = ci_head(root, run)
    if not ok:
        F('O10 %s: its pending citation names run %s, and %s' % (oid[:12], run, rhead))
        return None
    if rhead not in (None, oid):
        F('O10 %s: its pending citation names run %s, whose head in ci/%s/run.json is %s'
          % (oid[:12], run, run, rhead[:12]))
        return None
    path = os.path.join(root, rec)
    if not os.path.isfile(path):
        return 'pending', None
    try:
        L = open(path, encoding='utf-8').read().split('\n')
    except (OSError, UnicodeDecodeError):
        F('O10 %s: its record %s is in the tree and cannot be read' % (oid[:12], rec))
        return None
    at = {n: f for n, f in ((n, id_forms(oid, l)) for n, l in enumerate(L, 1)) if f}
    if not at:
        other = sorted({w for n in (lines or []) if n <= len(L) for w in HEXWORD.findall(L[n - 1]) if not w.isdigit()})
        F('O10 %s: its record %s is in the tree and does not cite it%s' % (
            oid[:12], rec, '; the recorded line(s) hold %s' % ', '.join(other) if other else ''))
        return None
    bad = []
    if lines is not None and sorted(at) != sorted(lines):
        bad.append('cites it on line(s) %s, not on the recorded %s' % (sorted(at), sorted(lines)))
    if toks is not None and not set(toks) <= {w for f in at.values() for w in f}:
        bad.append('does not cite it as %s' % ', '.join(sorted(set(toks) - {w for f in at.values() for w in f})))
    # the citation rule, on every line of the record that names the run
    free, emb, why = run_citations(oid, run, L)
    if not free:
        near = sorted({x for n in at for m in (n - 1, n, n + 1) if 1 <= m <= len(L) for x in RUNLIKE.findall(L[m - 1])})
        bad.append('does not name run %s beside it%s%s' % (
            run, ' (beside it: %s)' % ', '.join(near) if near else '',
            '; it names it only inside an identifier, on line(s) %s, which is not a citation'
            % ','.join(map(str, emb)) if emb else ''))
    elif why:
        bad.append(why)
    if bad:
        F('O10 %s: its record %s is in the tree and %s' % (oid[:12], rec, '; '.join(bad)))
        return None
    # the qualifying lines a promotion maps: the id's lines and the run's free-standing citations
    return 'eligible', (sorted(set(at) | set(free)), free, emb)


def lifecycle(e):
    """Whether an entry is a commit that O7 holds to O10's citation rule: every commit outside tranche 2's pinned
    membership. Decided by the entry's id against TRANCHE_MEMBERS, never by its tranche label (O3 checks that)."""
    return e.get('type') == 'commit' and e.get('oid') not in TRANCHE_MEMBERS[2]


def tranche_failures(ents, tbases):
    """O3 for the tranche labels: each an exact int; a pinned entry's its pinned tranche; any other entry's a
    tranche later than the pinned ones with a base in tranche_bases. Also checks each pinned set against its count
    and sha256, so an edit to the pin itself fails here."""
    out = []
    for t, (n, d) in sorted(TRANCHE_PINS.items()):
        s = sorted(TRANCHE_MEMBERS[t])
        if len(s) != n or sha256(''.join(o + '\n' for o in s).encode()) != d:
            out.append('O3 the checker\'s pinned tranche-%d membership is not its recorded count and sha256' % t)
    pinned = {o: t for t, s in TRANCHE_MEMBERS.items() for o in s}
    later = {int(k) for k in tbases if re.fullmatch(r'[1-9][0-9]*', str(k)) and int(k) > max(TRANCHE_PINS)}
    for oid, e in sorted(ents.items()):
        t = e.get('tranche')
        if type(t) is not int:
            out.append('O3 %s: its tranche %r is not an exact tranche number' % (oid[:12], t))
        elif oid in pinned and t != pinned[oid]:
            out.append('O3 %s: labelled tranche %d, but this checker pins it in tranche %d' % (oid[:12], t, pinned[oid]))
        elif oid not in pinned and t not in later:
            out.append('O3 %s: labelled tranche %d, %s' % (oid[:12], t, 'whose pinned membership does not include it'
                                                           if t in TRANCHE_PINS else
                                                           'which is neither pinned nor a later tranche with a base'))
    return out


def cited_by_rule(oid, c, L, n, root):
    """O7 for a citation of a lifecycle entry, at line n of L: None, or the reason it fails O10's rule."""
    line = L[n - 1]
    hexes = [t for t in c.get('tokens') or [] if isinstance(t, str) and re.fullmatch(r'[0-9a-f]{7,40}', t) and
             not t.isdigit()]
    if any(t not in id_forms(oid, line) for t in hexes):
        return 'does not hold its token as a word that is a form of its id'
    if not c.get('run') and other_ids(oid, line):
        return 'names another id (%s)' % ', '.join(sorted(set(other_ids(oid, line))))
    if c.get('run'):
        if run_line_class(str(c['run']), line) != 'free':
            return 'names run %s only inside an identifier, which is not a citation of it' % c['run']
        r = head_rule(oid, L, n)
        if r:
            return r
        ok, h = ci_head(root, str(c['run']))
        if not ok:
            return h
        if h not in (None, oid):
            return 'cites run %s, whose head in ci/%s/run.json is %s' % (c['run'], c['run'], h[:12])
    return None


def lifecycle_coverage(oid, cites, lines_of):
    """O7's completeness for a lifecycle commit: no location mapped twice; and in every file its citations name,
    every line naming a recorded run obeys the citation rule, and every qualifying line (a form of the id, or a
    free-standing citation of a recorded run) is mapped. lines_of(path) gives a file's lines, or None. Returns the
    reasons."""
    out = []
    locs = [str(c.get('location', '')) for c in cites]
    out += ['%s is mapped twice' % x for x in sorted({x for x in locs if locs.count(x) > 1})]
    runs = sorted({str(c['run']) for c in cites if c.get('run')})
    files = {}
    for x in locs:
        f, _, ln = x.rpartition(':')
        if ln.isdigit():
            files.setdefault(f, set()).add(int(ln))
    for f, mapped in sorted(files.items()):
        L = lines_of(f)
        if L is None:
            continue                    # its citing locations fail as missing
        q = {n for n, l in enumerate(L, 1) if id_forms(oid, l)}
        for r in runs:
            free, _, why = run_citations(oid, r, L)
            if why:
                out.append('%s %s' % (f, why))
            q |= set(free)
        if q - mapped:
            out.append('%s cites it at line(s) %s, which no citation maps' % (f, ','.join(map(str, sorted(q - mapped)))))
    return out


def o7_entry(oid, e, lines_of, root, F):
    """O7 for one entry's recorded citations. lines_of(path) gives a citing file's lines, or None."""
    for c in e.get('cited', []):
        f, _, ln = c.get('location', '').rpartition(':')
        lines = lines_of(f)
        toks = list(c.get('tokens') or []) + ([c['run']] if c.get('run') else [])
        if lines is None or not ln.isdigit() or int(ln) > len(lines):
            F('O7 %s: citing location %s does not exist' % (oid[:12], c.get('location')))
        elif not toks or not any(t in lines[int(ln) - 1] for t in toks):
            F('O7 %s: %s does not hold its token' % (oid[:12], c.get('location')))
        elif c.get('run') and not run_word(str(c['run'])).search(lines[int(ln) - 1]):
            F('O7 %s: %s does not hold its run %s' % (oid[:12], c.get('location'), c['run']))
        elif any(isinstance(t, str) and re.fullmatch(r'[0-9a-f]{7,40}', t) and not t.isdigit() and
                 not oid.startswith(t) for t in toks):
            F('O7 %s: %s records a hex token that is not a prefix of its id' % (oid[:12], c.get('location')))
        elif lifecycle(e):
            r = cited_by_rule(oid, c, lines, int(ln), root)
            if r:
                F('O7 %s: %s %s' % (oid[:12], c.get('location'), r))
    if lifecycle(e) and e.get('cited'):
        if not any(c.get('run') for c in e['cited']):
            F('O7 %s: a lifecycle commit (outside tranche 2) is cited without a run citation' % oid[:12])
        for r in lifecycle_coverage(oid, e['cited'], lines_of):
            F('O7 %s: %s' % (oid[:12], r))


def citation_summary(states):
    """The printed count of O10's states: an eligible entry is counted apart, never as cited."""
    count = lambda s: sum(1 for v in states.values() if v[0] == s)
    return 'citations (O10): %d cited, %d pending (record not in the tree), %d eligible for promotion' % (
        count('cited'), count('pending'), count('eligible'))


def check(objdir, root):
    fails = []
    F = fails.append
    try:
        man = json.load(open(os.path.join(objdir, 'manifest.json'), encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return ['O3 manifest unreadable: %s' % exc], {}
    if man.get('schema') != 'oi-evidence-objects' or man.get('version') != 1 or \
            not re.fullmatch(r'[0-9a-f]{40}', str(man.get('base', ''))):
        return ['O3 unknown schema, version or base'], {}
    for k in ('excerpt_denylist_sha256_of_id', 'identities_sha256'):
        if not isinstance(man.get(k), list) or not all(isinstance(x, str) and re.fullmatch(r'[0-9a-f]{64}', x)
                                                        for x in man[k]):
            return ['O3 %s is not a list of sha256 digests' % k], {}
    tb = man.get('tranche_bases', {})
    if not isinstance(tb, dict) or not all(re.fullmatch(r'[0-9]+', str(k)) and re.fullmatch(r'[0-9a-f]{40}', str(v))
                                           for k, v in tb.items()):
        return ['O3 tranche_bases is not a map of tranche numbers to commit ids'], {}
    deny = set(man['excerpt_denylist_sha256_of_id'])
    idents = set(man['identities_sha256'])
    ents, listed = {}, {'manifest.json'}
    for e in man.get('objects', []):
        oid = e.get('oid', '')
        if not re.fullmatch(r'[0-9a-f]{40}', oid) or oid in ents:
            F('O3 bad or duplicate id %r' % oid)
            continue
        if e.get('mechanism') not in MECH.get(e.get('type'), ()):
            F('O3 %s: mechanism %r is not one of a %s' % (oid[:12], e.get('mechanism'), e.get('type')))
            continue
        stored = e['mechanism'] not in WITHHELD
        if stored != bool(e.get('file')) or (stored and e.get('form') not in ('raw', 'zlib')):
            F('O3 %s: a %s entry %s a file' % (oid[:12], e['mechanism'], 'lacks' if stored else 'has'))
            continue
        if stored and e['file'] != ('loose/%s/%s' % (oid[:2], oid[2:]) if e['form'] == 'zlib'
                                    else '%s/%s/%s' % (e['type'], oid[:2], oid)):
            F('O3 %s: file %s is not where its form puts it' % (oid[:12], e['file']))
        ents[oid] = e
        if stored:
            listed.add(e['file'])
    for f in tranche_failures(ents, tb):
        F(f)
    for dirpath, _, names in os.walk(objdir):
        for fn in names:
            rel = os.path.relpath(os.path.join(dirpath, fn), objdir).replace(os.sep, '/')
            if rel not in listed:
                F('O2 unlisted file %s' % rel)
            if sha256(git_id('blob', open(os.path.join(dirpath, fn), 'rb').read()).encode()) in deny:
                F('O5 the file %s is itself a deny-listed blob' % rel)
    scan_text('objects/manifest.json', open(os.path.join(objdir, 'manifest.json'), encoding='utf-8').read(), False,
              idents, F)
    content = {}
    for oid, e in ents.items():
        if sha256(oid.encode()) in deny:
            F('O5 %s: a deny-listed (excerpt) id is in the manifest' % oid[:12])
        if e['mechanism'] in WITHHELD:
            continue
        c = read_stored(objdir, e, F)
        if c is None:
            continue
        content[oid] = c
        if e['type'] == 'tree':
            scan_text(e['file'], '\n'.join(n for _, n, _ in tree_entries(c)), False, idents, F)
        else:
            scan_text(e['file'], c.decode('utf-8', 'replace'), e['type'] == 'commit', idents, F)
    # O4 closure, O5 named ids
    external = set()

    def kind(x):
        return 'stored' if x in content else 'withheld' if x in ents and ents[x]['mechanism'] in WITHHELD else \
            'broken' if x in ents else 'external'

    def walk_tree(t, seen, withheld_ok, origin):
        if t in seen:
            return
        seen.add(t)
        if kind(t) != 'stored':
            if kind(t) == 'external':
                external.add(t)
            else:
                F('O4 %s: tree %s is %s' % (origin[:12], t[:12], kind(t)))
            return
        if ents[t]['mechanism'] == 'raw:proof-path':
            F('O4 %s: tree %s is retained as a path tree but lies under a fully retained tree' % (origin[:12], t[:12]))
            return
        for mode, name, x in tree_entries(content[t]):
            if sha256(x.encode()) in deny:
                F('O5 %s: tree %s names a deny-listed (excerpt) id at %s' % (origin[:12], t[:12], name))
            if mode == '160000':
                continue
            if mode == '40000':
                walk_tree(x, seen, withheld_ok, origin)
            elif kind(x) == 'withheld':
                withheld_ok.add(x)
            elif kind(x) == 'external':
                external.add(x)
            elif kind(x) == 'broken':
                F('O4 %s: blob %s is listed but not readable' % (origin[:12], x[:12]))

    incomplete_trees = set()

    for oid, e in ents.items():
        if e['type'] == 'tree' and oid in content and e['mechanism'] == 'raw':
            twh = set()
            walk_tree(oid, set(), twh, oid)
            if twh:
                incomplete_trees.add(oid)
        if e['type'] != 'commit' or oid not in content:
            continue
        tree, parents = commit_fields(content[oid])
        for x in [tree] + parents:
            if sha256(x.encode()) in deny:
                F('O5 %s: commit names a deny-listed (excerpt) id' % oid[:12])
        if parents != e.get('parents'):
            F('O3 %s: the recorded parents are not the commit\'s' % oid[:12])
        named = e.get('parents_not_retained', [])
        if any(p not in parents or p in ents for p in named):
            F('O3 %s: a parent named as not retained is not a parent, or is retained' % oid[:12])
        m = e['mechanism']
        if e.get('withheld_blobs') and m not in ('raw:partial-tree', 'inclusion-proof'):
            F('O3 %s: a %s commit carries a withheld_blobs list' % (oid[:12], m))
        if m == 'identity-anchor':
            continue
        if m == 'inclusion-proof':
            iwh = set()
            for p in e.get('inclusion_paths') or ['(none)']:
                cur = tree
                for part in [x for x in p.split('/') if x]:
                    if cur not in content:
                        F('O4 %s: inclusion path %s leaves the stored trees' % (oid[:12], p))
                        break
                    nxt = [x for mode, name, x in tree_entries(content[cur]) if name == part]
                    if not nxt:
                        F('O4 %s: inclusion path %s does not exist' % (oid[:12], p))
                        break
                    cur = nxt[0]
                else:
                    if kind(cur) != 'stored' and kind(cur) != 'withheld':
                        F('O4 %s: inclusion path %s ends at an object not retained' % (oid[:12], p))
                    elif kind(cur) == 'withheld':
                        iwh.add(cur)
                    elif cur in content and ents[cur]['type'] == 'tree':
                        if not p.endswith('/') or ents[cur]['mechanism'] != 'raw':
                            F('O4 %s: inclusion path %s ends at a tree not retained in full' % (oid[:12], p))
                        walk_tree(cur, set(), iwh, oid)
            if sorted(iwh) != sorted(e.get('withheld_blobs', [])):
                F('O4 %s: the blobs withheld under its inclusion paths are not exactly the recorded ones' % oid[:12])
            continue
        wh = set()
        walk_tree(tree, set(), wh, oid)
        if m == 'raw:partial-tree':
            if not wh or sorted(wh) != sorted(e.get('withheld_blobs', [])):
                F('O4 %s: its tree\'s withheld blobs are not exactly the recorded ones' % oid[:12])
        elif wh:
            F('O4 %s: a %s commit names withheld blobs' % (oid[:12], m))
        # parents_not_retained names the parents that are neither retained nor (H3 checks) on main
        bad = [p for p in parents if (p in ents and ents[p]['mechanism'] != 'raw:connected') or p in named]
        if m == 'raw:connected' and bad:
            F('O4 %s: raw:connected, but parent %s is not connected' % (oid[:12], bad[0][:12]))
        if m == 'raw:tree' and not bad:
            F('O4 %s: raw:tree, but every parent is connected' % oid[:12])
    # O10 the citation lifecycle: cited (O7 verifies it), or pending against the tree: pending, eligible or failing
    states = {}
    for oid, e in ents.items():
        if 'awaiting_citation' not in e:
            if e['type'] == 'commit' and not e.get('cited'):
                F('O10 %s: an uncited commit names no record, round and pull request that are to cite it' % oid[:12])
            elif e['type'] == 'commit':
                states[oid] = ('cited', None)
            continue
        if 'cited' in e:
            F('O10 %s: carries cited and awaiting_citation together' % oid[:12])
            continue
        st = pending_citation(oid, e['awaiting_citation'], root, F)
        if st:
            states[oid] = st
    # O7 citations
    texts = {}

    def lines_of(f):
        if f not in texts:
            try:
                texts[f] = open(os.path.join(root, f), encoding='utf-8').read().split('\n')
            except (OSError, UnicodeDecodeError):
                texts[f] = None
        return texts[f]
    for oid, e in ents.items():
        o7_entry(oid, e, lines_of, root, F)
    for x in man.get('id_discrepancies', []):
        f, _, ln = x.get('location', '').rpartition(':')
        try:
            line = open(os.path.join(root, f), encoding='utf-8').read().split('\n')[int(ln) - 1]
        except (OSError, ValueError, IndexError):
            line = None
        if line is None or x.get('cited_id', '-') not in line or x.get('run', '-') not in line and \
                not any(x['run'] == c.get('run') for c in ents.get(x.get('retained_id'), {}).get('cited', [])):
            F('O7 id discrepancy at %s: the line does not hold the cited id, or the run is not the retained one\'s'
              % x.get('location'))
        elif x['cited_id'] in ents or x.get('retained_id') not in content or x['retained_id'][:8] != x['cited_id'][:8]:
            F('O7 id discrepancy at %s: the retained id is not stored, or does not share the cited prefix' % x['location'])
        else:
            try:
                errata = {y['id']: y for y in json.load(open(os.path.join(root, ERRATA), encoding='utf-8'))['entries']}
            except (OSError, ValueError, KeyError, TypeError):
                errata = {}
            y = errata.get(x.get('erratum'), {})
            if (y.get('location'), y.get('cited_head'), y.get('real_head'), y.get('run_id')) != \
                    (x['location'], x['cited_id'], x['retained_id'], x['run']):
                F('O7 id discrepancy at %s: the erratum %s does not record the same location, ids and run'
                  % (x['location'], x.get('erratum')))
    # O8 ids recorded as missing
    for g in man.get('missing', []):
        gid = g.get('id', '')
        if not re.fullmatch(r'[0-9a-f]{7,40}', gid) or any(o.startswith(gid) for o in ents) or not g.get('cited_at'):
            F('O8 missing id %r is malformed, retained here, or names no citing location' % gid)
            continue
        for loc in g['cited_at']:
            f, _, ln = loc.rpartition(':')
            try:
                line = open(os.path.join(root, f), encoding='utf-8').read().split('\n')[int(ln) - 1]
            except (OSError, ValueError, IndexError):
                line = None
            if line is None or gid[:8] not in line:
                F('O8 missing id %s: %s does not hold it' % (gid[:12], loc))
    # O9 withheld entries: where the retained trees of the commits that list withheld blobs name each one
    occurs = {}
    for c, e in ents.items():
        if e['type'] != 'commit' or c not in content or not e.get('withheld_blobs'):
            continue
        ips = e.get('inclusion_paths') if e['mechanism'] == 'inclusion-proof' else None
        stack = [(commit_fields(content[c])[0], '')]
        while stack:
            t, pre = stack.pop()
            if t not in content or ents[t]['type'] != 'tree':
                continue
            for mode, name, x in tree_entries(content[t]):
                if mode == '40000':
                    stack.append((x, pre + name + '/'))
                elif x in ents and ents[x]['mechanism'] in WITHHELD:
                    path = pre + name
                    if ips is not None and not any(path == ip.rstrip('/') or (ip.endswith('/') and path.startswith(ip))
                                                   for ip in ips):
                        continue
                    occurs.setdefault(x, set()).add((c, path))
    for w, e in sorted(ents.items()):
        if e['mechanism'] not in WITHHELD:
            continue
        occ = occurs.get(w, set())
        if not occ:
            F('O9 withheld %s: no retained tree of a commit that lists withheld blobs names it' % w[:12])
            continue
        if any(w not in ents[c].get('withheld_blobs', []) for c, _ in occ):
            F('O9 withheld %s: a commit whose tree names it does not list it' % w[:12])
        if not e.get('paths') or set(e['paths']) != {p for _, p in occ}:
            F('O9 withheld %s: its recorded paths are not exactly where the retained trees name it' % w[:12])
        elif not all(p.endswith(WITHHELD_SUFFIXES[e['mechanism']]) for p in e['paths']):
            F('O9 withheld %s: a %s entry at a path of another file type' % (w[:12], e['mechanism']))
        if not e.get('needed_by') or any((n.get('object'), n.get('path')) not in occ for n in e['needed_by']):
            F('O9 withheld %s: its needed_by entries are not where the retained trees name it' % w[:12])
        if type(e.get('bytes')) is not int or e['bytes'] <= 0:
            F('O9 withheld %s: it records no size, or a zero size (empty files are stored, not withheld)' % w[:12])
        appr = APPROVED_WITHHELD.get(w)
        if appr is None or appr[:2] != (e['mechanism'], sorted(e.get('paths') or [])):
            F('O9 withheld %s: not withheld as approved (mechanism and exact paths)' % w[:12])
        elif len(appr) > 2:
            # an approval bound to commits: the commits whose trees name the blob are exactly the approved ones, and
            # each withheld instance is recorded with its commit, path, size, blob id, sha256 and reason
            if {c for c, _ in occ} != set(appr[2]):
                F('O9 withheld %s: not withheld as approved (the commits whose trees name it)' % w[:12])
            inst = e.get('instances') or []
            if {(i.get('commit'), i.get('path')) for i in inst} != occ or len(inst) != len(occ) or any(
                    i.get('blob') != w or i.get('bytes') != e.get('bytes') or i.get('sha256') != e.get('content_sha256')
                    or not re.fullmatch(r'[0-9a-f]{64}', str(i.get('sha256'))) or not i.get('reason') for i in inst):
                F('O9 withheld %s: its instances do not record each commit and path with its size, id, sha256 and '
                  'reason' % w[:12])
    for w in sorted(set(APPROVED_WITHHELD) - {o for o, e in ents.items() if e['mechanism'] in WITHHELD}):
        F('O9 approved withheld %s: not withheld here' % w[:12])
    info = {'entries': len(ents), 'stored': len(content), 'external': external, 'man': man, 'ents': ents,
            'content': content, 'incomplete_trees': incomplete_trees, 'citation_states': states}
    return fails, info


def git(args, cwd, inp=None, env=None):
    return subprocess.run(['git'] + args, cwd=cwd, input=inp, capture_output=True, env=env)


class GitFailed(Exception):
    pass


def gitok(args, cwd, inp=None, env=None):
    """Run git and return the completed process; a non-zero exit raises GitFailed, so no check reads empty output."""
    p = git(args, cwd, inp, env)
    if p.returncode:
        raise GitFailed('git %s exited %d: %s' % (' '.join(args[:3]), p.returncode,
                                                  p.stderr.decode('utf-8', 'replace').strip()[:100]))
    return p


def listing(out):
    """(present, missing) ids from a rev-list --objects --missing=print listing."""
    present, missing = set(), set()
    for l in out.decode().split('\n'):
        if l.startswith('?'):
            missing.add(l[1:].split()[0])
        elif l:
            present.add(l.split()[0])
    return present, missing


def base_history(root, base):
    """main's objects and commits, the digests of the addresses in its history, and the objects HEAD reaches."""
    key = (os.path.realpath(root), base, gitok(['rev-parse', 'HEAD'], root).stdout.decode().strip())
    if _HISTORY_MEMO is not None and key in _HISTORY_MEMO:
        return _HISTORY_MEMO[key]
    main_objs = set(l.split()[0] for l in gitok(['rev-list', '--objects', base], root).stdout.decode().split('\n') if l)
    main_commits = set(gitok(['rev-list', base], root).stdout.decode().split())
    log = gitok(['log', '--format=%ae%n%ce%n%B', base], root).stdout.decode('utf-8', 'replace')
    known = {sha256(a.encode()) for a in re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', log)}
    head = set(l.split()[0] for l in gitok(['rev-list', '--objects', 'HEAD'], root).stdout.decode().split('\n') if l)
    if not main_objs or not main_commits or not head:
        raise GitFailed('git returned no objects for the base or HEAD')
    if _HISTORY_MEMO is not None:
        _HISTORY_MEMO[key] = (main_objs, main_commits, known, head)
    return main_objs, main_commits, known, head


def history_checks(root, info, fails, clone_extra=None):
    """H1-H7. clone_extra (self-test only): {type: [content]} written into the temporary repository as if this
    clone held those objects beside the archive; no verdict may depend on them."""
    F = fails.append
    try:
        _history_checks(root, info, fails, clone_extra or {})
    except GitFailed as exc:
        F('H0 %s' % exc)


def _history_checks(root, info, fails, clone_extra):
    F = fails.append
    man, ents, content, external = info['man'], info['ents'], info['content'], info['external']
    base = man['base']
    # each archive tranche has its base: the manifest's for tranche 2, tranche_bases for a later one
    tbases = {str(k): v for k, v in (man.get('tranche_bases') or {}).items()}
    base_of = lambda e: tbases.get(str(e.get('tranche')), base)
    for b in [base] + sorted(set(tbases.values())):
        if git(['cat-file', '-e', b + '^{commit}'], root).returncode or \
                git(['merge-base', '--is-ancestor', b, 'HEAD'], root).returncode:
            F('H1 the base %s is not an ancestor of HEAD in this repository' % b[:12])
            return
    objects = gitok(['rev-parse', '--path-format=absolute', '--git-path', 'objects'], root).stdout.decode().strip()
    deny = set(man.get('excerpt_denylist_sha256_of_id', []))
    withheld = {o for o, e in ents.items() if e['mechanism'] in WITHHELD}
    tmp = tempfile.mkdtemp(prefix='retained-')
    try:
        g = os.path.join(tmp, 'r.git')
        gitok(['init', '-q', '--bare', g], tmp)
        with open(os.path.join(g, 'objects', 'info', 'alternates'), 'w') as fh:
            fh.write(objects + '\n')
        env = dict(os.environ, GIT_DIR=g)

        def write_objects(typ, blobs):
            paths = []
            for i, data in enumerate(blobs):
                pth = os.path.join(tmp, 'w-%s-%d' % (typ, i))
                with open(pth, 'wb') as fh:
                    fh.write(data)
                paths.append(pth)
            p = git(['hash-object', '-w', '-t', typ, '--stdin-paths'], tmp, inp=('\n'.join(paths) + '\n').encode(), env=env)
            for pth in paths:
                os.remove(pth)
            return p
        # H2: git, not this script, computes each id (hash-object also checks a commit's and a tree's format)
        for typ in ('blob', 'tree', 'commit'):
            oids = sorted(o for o in content if ents[o]['type'] == typ)
            if not oids:
                continue
            p = write_objects(typ, [content[o] for o in oids])
            got = p.stdout.decode().split()
            if p.returncode or got != oids:
                bad = next((o for o, x in zip(oids, got) if o != x), oids[len(got)] if len(got) < len(oids) else '?')
                F('H2 git does not write %s %s with its id: %s' % (typ, bad[:12], p.stderr.decode().strip()[:80]))
                return
        for typ, blobs in sorted(clone_extra.items()):
            if write_objects(typ, blobs).returncode:
                raise GitFailed('the self-test could not stage a clone-held %s' % typ)
        per_base = {b: base_history(root, b) for b in [base] + sorted(set(tbases.values()))}
        main_objs, main_commits, known, head = per_base[base]
        for b, (o2, c2, k2, _) in per_base.items():
            if b != base:
                # main at a later tranche's base contains main at the first base (H1 orders both before HEAD)
                main_objs, main_commits, known = main_objs | o2, main_commits | c2, known | k2
        # what the archive or main holds: every verdict below is relative to this, never to what the clone holds
        held = set(content) | main_objs
        # H7: nothing listed here is already on main at its own tranche's base
        for o in sorted(ents):
            if o in per_base[base_of(ents[o])][0]:
                F('H7 %s (%s) is reachable from the base, so it is not off-main' % (o[:12], ents[o]['mechanism']))
        for mg in man.get('missing', []):
            gid = mg.get('id', '')
            if gid and any(x.startswith(gid) for x in main_objs):
                F('H7 missing id %s names an object reachable from the base' % gid[:12])
        # H3: what the retained objects name and do not retain is on main
        for x in sorted(external):
            if x not in main_objs:
                F('H3 %s is named by a retained object, is neither retained nor withheld, and is not on main' % x[:12])
        for c, e in ents.items():
            if e['type'] != 'commit' or c not in content:
                continue
            for par in commit_fields(content[c])[1]:
                named = par in e.get('parents_not_retained', [])
                if par not in ents and not named and par not in main_commits:
                    F('H3 %s: parent %s is neither retained, nor on main, nor named' % (c[:12], par[:12]))
                if named and par in main_commits:
                    F('H3 %s: parent %s is named as not retained but is on main' % (c[:12], par[:12]))
        if any(f.startswith('H3') for f in fails):
            return
        # H4: connectivity, relative to the archive and main. A ref at every raw:connected and raw:tree commit and
        # every complete cited tree, every raw:tree commit a shallow boundary so nothing walks past it.
        refs = sorted(o for o, e in ents.items() if o in content and (e['mechanism'] in ('raw:connected', 'raw:tree') or
                                                                       (e['type'] == 'tree' and e.get('cited') and
                                                                        o not in info['incomplete_trees'])))
        gitok(['update-ref', '--stdin'], tmp, inp=''.join('create refs/retained/%s %s\n' % (o, o) for o in refs).encode(),
              env=env)
        made = gitok(['for-each-ref', '--format=%(objectname)', 'refs/retained/'], tmp, env=env).stdout.decode().split()
        if sorted(made) != refs:
            F('H4 %d of %d refs were created in the temporary repository' % (len(made), len(refs)))
            return
        shallow = sorted(o for o, e in ents.items() if e['mechanism'] == 'raw:tree' and o in content)
        with open(os.path.join(g, 'shallow'), 'w') as fh:
            fh.write(''.join(x + '\n' for x in shallow))
        fs = git(['fsck', '--connectivity-only', '--no-dangling', '--no-progress'], tmp, env=env)
        if fs.returncode:
            msg = [l for l in (fs.stdout + fs.stderr).decode('utf-8', 'replace').split('\n')
                   if l.strip() and not l.startswith('notice:')]
            F('H4 git fsck --connectivity-only fails: %s' % (msg or ['(no message)'])[0][:120])
        # everything the refs reach is held by the archive or main; an object only this clone holds, or one no store
        # holds, fails, whichever it is
        reached, gone = listing(gitok(['rev-list', '--objects', '--missing=print', '--all'], tmp, env=env).stdout)
        for x in sorted((reached | gone) - held):
            F('H4 %s is reached from the retained refs but neither the archive nor main holds it%s'
              % (x[:12], ' (this clone does)' if x in reached else ''))
            break
        for o, e in sorted(ents.items()):
            if e['mechanism'] == 'raw:connected':
                out = gitok(['rev-list', o, '--not', base_of(e)], tmp, env=env).stdout.decode().split()
                stray = [x for x in out if x not in ents or ents[x]['mechanism'] != 'raw:connected']
                if stray:
                    F('H4 %s: raw:connected, but its history leaves main through %s' % (o[:12], stray[0][:12]))
            if e['mechanism'] == 'raw:partial-tree' and o in content:
                pres, miss = listing(gitok(['rev-list', '--objects', '--no-walk', '--missing=print', o], tmp,
                                           env=env).stdout)
                if sorted((pres | miss) - held) != sorted(e.get('withheld_blobs', [])):
                    F('H4 %s: what its tree names beyond the archive and main is not exactly its withheld blobs' % o[:12])
            if e['mechanism'] == 'inclusion-proof':
                beyond = set()
                for pth in e.get('inclusion_paths', []):
                    r = git(['rev-parse', '--verify', '-q', '%s:%s' % (o, pth.rstrip('/'))], tmp, env=env)
                    tip = r.stdout.decode().strip()
                    if r.returncode or tip not in set(content) | withheld:
                        F('H4 %s: %s does not resolve to a retained or withheld object' % (o[:12], pth))
                    elif tip in withheld:
                        beyond.add(tip)
                    elif ents[tip]['type'] == 'tree':
                        pres, miss = listing(gitok(['rev-list', '--objects', '--missing=print', tip], tmp,
                                                   env=env).stdout)
                        beyond |= (pres | miss) - held
                if sorted(beyond) != sorted(e.get('withheld_blobs', [])):
                    F('H4 %s: what its inclusion paths name beyond the archive and main is not exactly its withheld '
                      'blobs' % o[:12])
        # H5: identities are addresses already public in main's history
        for d in man.get('identities_sha256', []):
            if d not in known:
                F('H5 identity digest %s names no address in the base\'s history' % d[:12])
        # H6: no excerpt reachable from HEAD, or from anything reconstituted
        for name, lst in (('HEAD of this repository', head), ('the reconstituted objects', reached | gone)):
            hit = sorted(x for x in lst if sha256(x.encode()) in deny)
            if hit:
                F('H6 %d deny-listed (excerpt) object(s) reachable from %s, first %s' % (len(hit), name, hit[0][:12]))
        info['reconstituted'] = {'refs': len(made), 'shallow_boundaries': len(shallow)}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


class Fails(list):
    pass


def check_with(objdir, root, history, fails):
    res, info = check(objdir, root)
    fails.extend(res)
    if history and not fails and info:
        history_checks(root, info, fails)
    return fails, info


def self_test(root):
    """Mutate a copy once per failure family, in both directions: the copy passes, each mutation fails as named."""
    global _SCAN_MEMO, _HISTORY_MEMO
    tmp = tempfile.mkdtemp(prefix='objects-selftest-')
    results = []
    _SCAN_MEMO, _HISTORY_MEMO = {}, {}
    try:
        base = os.path.join(tmp, 'objects')
        shutil.copytree(OBJ, base)
        man0 = json.load(open(os.path.join(base, 'manifest.json')))

        def fresh():
            d = os.path.join(tmp, 'case')
            if os.path.isdir(d):
                shutil.rmtree(d)
            shutil.copytree(base, d)
            return d

        def save(d, man):
            json.dump(man, open(os.path.join(d, 'manifest.json'), 'w'), indent=1, sort_keys=True)

        def pick(pred):
            return next(e for e in man0['objects'] if pred(e))

        def expect(name, mutate, rule, history=False):
            d = fresh()
            mutate(d)
            fails, _ = check_with(d, root, history, Fails())
            ok = any(f.startswith(rule) for f in fails)
            results.append((name, rule, 'FAILS as required' if ok else 'NOT DETECTED', fails[:1]))

        def flip(d, rel):
            p = os.path.join(d, rel)
            b = bytearray(open(p, 'rb').read())
            b[len(b) // 2] ^= 0x01
            open(p, 'wb').write(bytes(b))

        def later_tranche(man):
            """The tranche of an object a case adds: later than the pinned ones, with the latest pinned base."""
            man.setdefault('tranche_bases', {})['5'] = man['tranche_bases'].get('4', man['base'])
            return 5

        def new_blob(d, man, data, cited=None):
            oid = git_id('blob', data)
            rel = 'blob/%s/%s' % (oid[:2], oid)
            os.makedirs(os.path.join(d, os.path.dirname(rel)), exist_ok=True)
            open(os.path.join(d, rel), 'wb').write(data)
            man['objects'].append({'oid': oid, 'type': 'blob', 'mechanism': 'byte-copy', 'form': 'raw', 'file': rel,
                                   'bytes': len(data), 'sha256': sha256(data), 'tranche': later_tranche(man)})
            return oid

        for hist in (False, True):
            fails, info = check_with(base, root, hist, Fails())
            results.append(('unmutated copy (%s mode)' % ('history' if hist else 'tree'), '-',
                            'PASSES as required' if not fails else 'FAILS', fails[:3]))
        rawblob = pick(lambda e: e.get('form') == 'raw' and e['type'] == 'blob' and e.get('bytes', 0) > 0)
        rawcommit = pick(lambda e: e.get('form') == 'raw' and e['type'] == 'commit')
        ztree = pick(lambda e: e.get('form') == 'zlib' and e['type'] == 'tree' and not e.get('cited'))
        zblob = pick(lambda e: e.get('form') == 'zlib' and e['type'] == 'blob')
        expect('a corrupted byte in a raw blob', lambda d: flip(d, rawblob['file']), 'O1')
        expect('a corrupted byte in a raw commit', lambda d: flip(d, rawcommit['file']), 'O1')
        expect('a corrupted byte in a zlib tree', lambda d: flip(d, ztree['file']), 'O1')
        expect('a corrupted byte in a zlib blob', lambda d: flip(d, zblob['file']), 'O1')

        def drop_file(d):
            os.remove(os.path.join(d, ztree['file']))
        expect('a missing object file (entry kept)', drop_file, 'O1')

        def drop_object(d):
            os.remove(os.path.join(d, ztree['file']))
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['objects'] = [e for e in man['objects'] if e['oid'] != ztree['oid']]
            save(d, man)
        expect('a missing object (file and entry removed)', drop_object, 'H3', history=True)

        def unlisted(d):
            open(os.path.join(d, 'blob', 'stray'), 'wb').write(b'x\n')
        expect('an unlisted file', unlisted, 'O2')

        def on_main(d):
            # the base's root tree, stored as a fully retained tree: well formed, and on main
            man = json.load(open(os.path.join(d, 'manifest.json')))
            tree = git(['rev-parse', man['base'] + '^{tree}'], root).stdout.decode().strip()
            data = git(['cat-file', 'tree', tree], root).stdout
            rel = 'tree/%s/%s' % (tree[:2], tree)
            os.makedirs(os.path.join(d, os.path.dirname(rel)), exist_ok=True)
            open(os.path.join(d, rel), 'wb').write(data)
            man['objects'].append({'oid': tree, 'type': 'tree', 'mechanism': 'raw', 'form': 'raw', 'file': rel,
                                   'bytes': len(data), 'sha256': sha256(data), 'tranche': later_tranche(man)})
            save(d, man)
        expect('an object already on main, stored here', on_main, 'H7', history=True)

        def deny_stored(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['excerpt_denylist_sha256_of_id'].append(sha256(rawblob['oid'].encode()))
            save(d, man)
        expect('an injected excerpt: a stored blob whose id is deny-listed', deny_stored, 'O5')

        def deny_named(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            data = zlib.decompress(open(os.path.join(d, ztree['file']), 'rb').read()).partition(b'\0')[2]
            man['excerpt_denylist_sha256_of_id'].append(sha256(tree_entries(data)[0][2].encode()))
            save(d, man)
        expect('an injected excerpt: a retained tree that names a deny-listed id', deny_named, 'O5')

        def excerpt_new(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            oid = new_blob(d, man, b'synthetic excerpt stand-in\n')
            man['excerpt_denylist_sha256_of_id'].append(sha256(oid.encode()))
            save(d, man)
        expect('an injected excerpt: a new stored blob on the deny-list', excerpt_new, 'O5')

        def excerpt_head(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            # a blob reachable from HEAD that no retained object names: this checker's own committed blob
            own = git(['rev-parse', 'HEAD:verification/audits/evidence-retention/check_objects.py'], root).stdout.decode().strip()
            man['excerpt_denylist_sha256_of_id'].append(sha256(own.encode()))
            save(d, man)
        expect('an injected excerpt: a deny-listed blob reachable from HEAD', excerpt_head, 'H6', history=True)

        def secret(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            new_blob(d, man, b'token = ghp_' + b'A' * 36 + b'\n')
            save(d, man)
        expect('a secret pattern in a stored blob', secret, 'O6')

        def email(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            new_blob(d, man, b'contact someone' + b'@' + b'example-corp.io\n')
            save(d, man)
        expect('an e-mail address in a stored blob', email, 'O6')

        def ident(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['identities_sha256'] = man['identities_sha256'][1:]
            save(d, man)
        expect('a commit identity whose digest is not listed', ident, 'O6')

        def fake_ident(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['identities_sha256'].append(sha256(b'nobody' + b'@' + b'nowhere.invalid'))
            save(d, man)
        expect('a listed identity absent from main\'s history', fake_ident, 'H5', history=True)

        def relabel(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            e = next(e for e in man['objects'] if e['mechanism'] == 'raw:tree')
            e['mechanism'] = 'raw:connected'
            e.pop('parents_not_retained', None)
            save(d, man)
        expect('a raw:tree commit relabelled raw:connected', relabel, 'O4')

        def drop_withheld(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            e = next(e for e in man['objects'] if e['mechanism'] == 'raw:partial-tree')
            e['withheld_blobs'] = e['withheld_blobs'][1:]
            save(d, man)
        expect('a withheld blob dropped from its commit\'s list', drop_withheld, 'O4')

        def cite(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            e = next(e for e in man['objects'] if e.get('cited'))
            e['cited'][0]['tokens'] = ['f' * 12]
            e['cited'][0].pop('run', None)
            save(d, man)
        expect('a citation whose line lacks its token', cite, 'O7')

        def discrepancy(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['id_discrepancies'][0]['retained_id'] = rawcommit['oid']
            save(d, man)
        expect('an id discrepancy mapped to another commit', discrepancy, 'O7')

        def erratum(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            x = man['id_discrepancies'][0]
            x['erratum'] = next(y['erratum'] for y in man['id_discrepancies'] if y['erratum'] != x['erratum'])
            save(d, man)
        expect('an id discrepancy that names another erratum', erratum, 'O7')

        def missing_moved(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            g = man['missing'][0]
            f, _, ln = g['cited_at'][0].rpartition(':')
            g['cited_at'][0] = '%s:%d' % (f, int(ln) + 1)
            save(d, man)
        expect('a missing id whose citing line does not hold it', missing_moved, 'O8')

        def missing_retained(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['missing'][0]['id'] = rawcommit['oid']
            man['missing'][0]['cited_at'] = [c['location'] for c in rawcommit.get('cited', [])][:1] or \
                man['missing'][0]['cited_at']
            save(d, man)
        expect('a missing id that is retained here', missing_retained, 'O8')
        def bad_mechanism(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            next(e for e in man['objects'] if e['oid'] == rawcommit['oid'])['mechanism'] = 'byte-copy'
            save(d, man)
        expect('a commit entry with a blob\'s mechanism', bad_mechanism, 'O3')

        def bad_digest(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['identities_sha256'].append('not-a-digest')
            save(d, man)
        expect('an identity digest that is not a sha256 digest', bad_digest, 'O3')

        def unknown_base(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['base'] = 'f' * 40
            save(d, man)
        expect('a base this repository does not hold', unknown_base, 'H1', history=True)

        def malformed_commit(d):
            # well formed for tree mode, but git's own format check refuses it: it has no committer line
            man = json.load(open(os.path.join(d, 'manifest.json')))
            data = b'tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904\nauthor A <a> 0 +0000\n\nno committer\n'
            oid = git_id('commit', data)
            rel = 'commit/%s/%s' % (oid[:2], oid)
            os.makedirs(os.path.join(d, os.path.dirname(rel)), exist_ok=True)
            open(os.path.join(d, rel), 'wb').write(data)
            # uncited, so it names a record to cite it (O10), and only git's format check (H2) can refuse it
            man['objects'].append({'oid': oid, 'type': 'commit', 'mechanism': 'identity-anchor', 'form': 'raw',
                                   'file': rel, 'bytes': len(data), 'sha256': sha256(data), 'parents': [],
                                   'awaiting_citation': {'pull_request': 1, 'round': 'SELF-TEST', 'record': 'x.md',
                                                         'run': '1'},
                                   'tranche': later_tranche(man)})
            save(d, man)
        expect('a commit git refuses as malformed', malformed_commit, 'H2', history=True)

        # H4 re-derives connectivity with git. Tree mode (O4) already rejects these states, so each case changes
        # the checked state after tree mode passes, and shows H4 rejects it on its own. clone_extra writes objects
        # into the temporary repository as if this clone held them beside the archive.
        def expect_history(name, mutate, rule, msg=''):
            fails, info = check(base, root)
            if fails:
                results.append((name, rule or '-', 'FAILS in tree mode', fails[:1]))
                return
            extra = mutate(info) or {}
            hf = Fails()
            history_checks(root, info, hf, extra)
            if rule is None:
                results.append((name, '-', 'PASSES as required' if not hf else 'FAILS', hf[:3]))
            else:
                ok = any(f.startswith(rule) and msg in f for f in hf)
                results.append((name, rule, 'FAILS as required' if ok else 'NOT DETECTED', hf[:1]))

        part = next(e for e in man0['objects'] if e['mechanism'] == 'raw:partial-tree')
        conn = {e['oid'] for e in man0['objects'] if e['mechanism'] == 'raw:connected'}
        under_conn = next(e for e in man0['objects'] if e['type'] == 'blob' and e.get('form') == 'zlib' and
                          not e.get('cited') and e.get('needed_by') and
                          all(n['object'] in conn for n in e['needed_by']))
        under_part = next(e for e in man0['objects'] if e['type'] == 'blob' and e.get('file') and
                          not e.get('cited') and [n['object'] for n in e.get('needed_by', [])] == [part['oid']])

        def drop_needed(info):
            del info['content'][under_conn['oid']]
        expect_history('a required stored object dropped from the archive', drop_needed, 'H4')

        def drop_needed_clone_holds(info):
            data = info['content'].pop(under_conn['oid'])
            return {'blob': [data]}
        expect_history('a required object missing from the archive but held by this clone',
                       drop_needed_clone_holds, 'H4')

        def short_withheld(info):
            info['ents'][part['oid']]['withheld_blobs'] = info['ents'][part['oid']]['withheld_blobs'][1:]
        expect_history('a partial tree whose withheld list omits one of its blobs', short_withheld, 'H4')

        def withheld_clone_holds(info):
            # a blob of the partial tree, withheld from the archive, that this clone happens to hold
            data = info['content'].pop(under_part['oid'])
            info['ents'][under_part['oid']] = dict(info['ents'][under_part['oid']], mechanism='withheld:raw-log')
            info['ents'][part['oid']]['withheld_blobs'] = sorted(info['ents'][part['oid']]['withheld_blobs'] +
                                                                 [under_part['oid']])
            return {'blob': [data]}
        expect_history('a withheld blob that this clone holds', withheld_clone_holds, None)

        incl = next(e for e in man0['objects'] if e['mechanism'] == 'inclusion-proof' and e.get('withheld_blobs'))
        under_incl = next(e for e in man0['objects'] if e['type'] == 'blob' and e.get('file') and
                          [n['object'] for n in e.get('needed_by', [])] == [incl['oid']])

        def incl_relabel(d):
            # a retained blob under an inclusion path deleted, its entry turned into a withheld one
            man = json.load(open(os.path.join(d, 'manifest.json')))
            os.remove(os.path.join(d, under_incl['file']))
            e = next(x for x in man['objects'] if x['oid'] == under_incl['oid'])
            for k in ('file', 'form', 'sha256', 'content_sha256', 'content_bytes', 'cited'):
                e.pop(k, None)
            e.update(mechanism='withheld:raw-log', bytes=under_incl['content_bytes'],
                     paths=[under_incl['needed_by'][0]['path']])
            save(d, man)
        expect('a blob under an inclusion path dropped and relabelled withheld', incl_relabel, 'O4')

        def orphan_withheld(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['objects'].append({'oid': 'f' * 40, 'type': 'blob', 'mechanism': 'withheld:raw-log', 'bytes': 1,
                                   'paths': ['x.log'], 'needed_by': [{'object': part['oid'], 'path': 'x.log'}],
                                   'tranche': later_tranche(man)})
            save(d, man)
        expect('a withheld entry that no retained tree names', orphan_withheld, 'O9')

        def withheld_path(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            e = next(x for x in man['objects'] if x['mechanism'] in WITHHELD)
            e['paths'] = [e['paths'][0] + '.moved']
            save(d, man)
        expect('a withheld entry whose recorded path is not where it is named', withheld_path, 'O9')

        def relabel_listed(d):
            # a stored blob of the partial tree deleted, relabelled a raw log and added to its commit's list
            man = json.load(open(os.path.join(d, 'manifest.json')))
            os.remove(os.path.join(d, under_part['file']))
            e = next(x for x in man['objects'] if x['oid'] == under_part['oid'])
            for k in ('file', 'form', 'sha256', 'content_sha256', 'content_bytes', 'cited'):
                e.pop(k, None)
            e.update(mechanism='withheld:raw-log', bytes=under_part['content_bytes'],
                     paths=[under_part['needed_by'][0]['path']])
            c = next(x for x in man['objects'] if x['oid'] == part['oid'])
            c['withheld_blobs'] = sorted(c['withheld_blobs'] + [under_part['oid']])
            save(d, man)
        expect('a stored blob relabelled a raw log, with its commit\'s list edited to match', relabel_listed, 'O9')

        def empty_relabelled(d):
            # the empty blob, stored at log-type paths, deleted and withheld with both commits' lists edited to match
            man = json.load(open(os.path.join(d, 'manifest.json')))
            e = next(x for x in man['objects'] if x['oid'] == 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391')
            os.remove(os.path.join(d, e['file']))
            paths = ['research/a42-rerun/quarantine/r5.log', 'research/round7-channel/channel_check.replay.err',
                     'research/round7-channel/channel_check.run1.err',
                     'research/round7-channel/native-controls.selftest.final.err']
            for k in ('file', 'form', 'sha256', 'content_sha256', 'content_bytes', 'cited'):
                e.pop(k, None)
            e.update(mechanism='withheld:raw-log', bytes=1, paths=paths)
            for c in man['objects']:
                if c['oid'] in {n['object'] for n in e['needed_by']}:
                    c['withheld_blobs'] = sorted(set(c.get('withheld_blobs', [])) | {e['oid']})
            save(d, man)
        expect('a stored log-type blob withheld, with the manifest and lists edited to match', empty_relabelled, 'O9')

        def as_pdf(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            next(x for x in man['objects'] if x['mechanism'] == 'withheld:raw-log')['mechanism'] = 'withheld:build-pdf'
            save(d, man)
        expect('a raw log relabelled a build output', as_pdf, 'O9')

        def git_fails(info):
            return {'commit': [b'not a commit\n']}
        expect_history('a git command that fails while staging objects', git_fails, 'H0')

        def bad_incl_path(info):
            info['ents'][incl['oid']]['inclusion_paths'] = info['ents'][incl['oid']]['inclusion_paths'] + ['no/such']
        expect_history('an inclusion path that does not resolve', bad_incl_path, 'H4')

        def short_incl_withheld(info):
            info['ents'][incl['oid']]['withheld_blobs'] = info['ents'][incl['oid']]['withheld_blobs'][1:]
        expect_history('an inclusion proof whose withheld list omits one of its blobs', short_incl_withheld, 'H4')

        def missing_on_main(info):
            info['man'] = dict(info['man'], missing=[dict(info['man']['missing'][0], id=info['man']['base'][:12])])
        expect_history('a missing id that names an object on main', missing_on_main, 'H7')

        # archive tranche 4: withholding bound to exact paths and commits, the base per tranche, the tranche pin
        bound = sorted(w for w, a in APPROVED_WITHHELD.items() if len(a) > 2)
        third = next((e for e in man0['objects'] if e['type'] == 'blob' and e.get('file') and
                      e.get('needed_by') and all(n['path'].endswith('.txt') for n in e['needed_by']) and
                      all(next(x for x in man0['objects'] if x['oid'] == n['object'])['mechanism'] == 'raw:partial-tree'
                          for n in e['needed_by'])), None)
        t2raw = next((e for e in man0['objects'] if e['type'] == 'blob' and e.get('form') == 'raw' and e.get('tranche') == 2),
                     None)
        # The citation-lifecycle fixture, built in each case's copy so that every case runs whatever the live entries'
        # states are (pending, eligible, partly or fully promoted): the two lowest pinned tranche-4 commits, made
        # pending on a stand-in record that no tree holds, each with a run that is not retained here.
        by_oid = {e['oid']: e for e in man0['objects']}
        stand = sorted(o for o in TRANCHE_MEMBERS[4] if by_oid.get(o, {}).get('type') == 'commit')[:2]
        srec = 'verification/ZZ-SELF-TEST/o10-stand-in.md'
        sruns = ['70000000001', '70000000002']
        fixture_ok = len(stand) == 2 and not os.path.lexists(os.path.join(root, srec)) and not any(
            os.path.lexists(os.path.join(root, ARCHIVE_REL, 'ci', r)) for r in sruns)

        def pend_all(m):
            for x in m['objects']:
                if x['oid'] in stand:
                    x.pop('cited', None)
                    x['awaiting_citation'] = {'pull_request': 1, 'round': 'O10-SELF-TEST', 'record': srec,
                                              'run': sruns[stand.index(x['oid'])]}

        def fixture_edit(fn):
            def go(d):
                man = json.load(open(os.path.join(d, 'manifest.json')))
                pend_all(man)
                fn(man)
                save(d, man)
            return go
        if not bound or third is None or t2raw is None or 'tranche_bases' not in man0 or not fixture_ok:
            results.append(('the tranche-4 cases need a commit-bound approval, a stored .txt under a partial tree, a '
                            'tranche-2 raw blob, tranche bases, two pinned tranche-4 commits, and a stand-in record '
                            'and runs that no tree holds', '-', 'NOT DETECTED', []))
        else:
            def third_txt(d):
                # a third .txt, stored under a partial tree: deleted, relabelled a raw output, its commit's list and
                # the manifest edited to match; the checker's approved list does not name it
                man = json.load(open(os.path.join(d, 'manifest.json')))
                os.remove(os.path.join(d, third['file']))
                e = next(x for x in man['objects'] if x['oid'] == third['oid'])
                for k in ('file', 'form', 'sha256', 'content_sha256', 'content_bytes', 'cited'):
                    e.pop(k, None)
                e.update(mechanism='withheld:raw-output', bytes=third['content_bytes'],
                         paths=sorted({n['path'] for n in third['needed_by']}))
                for c in man['objects']:
                    if c['oid'] in {n['object'] for n in third['needed_by']}:
                        c['withheld_blobs'] = sorted(set(c['withheld_blobs']) | {third['oid']})
                save(d, man)
            expect('a third, unlisted .txt withheld, with the manifest and its commit\'s list edited to match', third_txt,
                   'O9')

            def one_commit(d):
                # the approval narrowed to one of the two commits whose trees name the blob
                w = bound[0]
                APPROVED_WITHHELD[w] = APPROVED_WITHHELD[w][:2] + (APPROVED_WITHHELD[w][2][:1],)
            saved = dict(APPROVED_WITHHELD)
            try:
                expect('an approved .txt withheld in a commit its approval does not name', one_commit, 'O9')
            finally:
                APPROVED_WITHHELD.clear()
                APPROVED_WITHHELD.update(saved)

            def instance_sha(d):
                man = json.load(open(os.path.join(d, 'manifest.json')))
                e = next(x for x in man['objects'] if x['oid'] == bound[0])
                e['instances'][0]['sha256'] = '0' * 64
                save(d, man)
            expect('a withheld instance whose sha256 is not the recorded one', instance_sha, 'O9')

            def instance_dropped(d):
                man = json.load(open(os.path.join(d, 'manifest.json')))
                e = next(x for x in man['objects'] if x['oid'] == bound[0])
                e['instances'] = e['instances'][1:]
                save(d, man)
            expect('a withheld instance not recorded', instance_dropped, 'O9')
            expect('an uncited commit that names no record to cite it', fixture_edit(
                lambda m: next(x for x in m['objects'] if x['oid'] == stand[0]).pop('awaiting_citation')), 'O10')
            expect('a pending citation without its round', fixture_edit(
                lambda m: next(x for x in m['objects'] if x['oid'] == stand[0])['awaiting_citation'].pop('round')), 'O10')

            def bad_bases(d):
                man = json.load(open(os.path.join(d, 'manifest.json')))
                man['tranche_bases'] = dict(man['tranche_bases'], **{'4': 'main'})
                save(d, man)
            expect('a tranche base that is not a commit id', bad_bases, 'O3')

            def base_off_head(d):
                man = json.load(open(os.path.join(d, 'manifest.json')))
                man['tranche_bases'] = dict(man['tranche_bases'], **{'4': stand[0]})
                save(d, man)
            expect('a tranche base that is not an ancestor of HEAD', base_off_head, 'H1', history=True)

            def on_tranche_base(info):
                # a tranche-2 blob stored as a plain file, which main reaches from the later base, counted as tranche 4
                # once tree mode has passed (tree mode refuses the label itself: the next case)
                info['ents'][t2raw['oid']] = dict(info['ents'][t2raw['oid']], tranche=4)
            expect_history('an object its own tranche\'s base already reaches', on_tranche_base, 'H7')

            # H4 walks a raw:connected commit's history back to its own tranche's base. A commit of a new tranche
            # whose parent is the latest tranche base, which the first base does not reach, passes; the same commit
            # recorded against the first base fails, and so does one whose parent is an off-main commit that the
            # archive does not hold (this clone does; the commit names it as a parent not retained).
            tb0 = {str(k): v for k, v in man0['tranche_bases'].items()}
            latest = tb0[max(tb0, key=int)]
            newt = max([int(k) for k in tb0] + [e['tranche'] for e in man0['objects']
                                                if type(e.get('tranche')) is int]) + 1

            def connected_on(parent, what):
                tree = gitok(['rev-parse', parent + '^{tree}'], root).stdout.decode().strip()
                data = ('tree %s\nparent %s\nauthor A <a> 1 +0000\ncommitter A <a> 1 +0000\n\n%s\n'
                        % (tree, parent, what)).encode()
                return git_id('commit', data), data
            mid, mid_data = connected_on(latest, 'an off-main commit the archive does not hold')
            on_latest, on_latest_data = connected_on(latest, 'a raw:connected commit on the latest tranche base')
            on_mid, on_mid_data = connected_on(mid, 'a raw:connected commit on an off-main commit')

            def add_connected(oid, data, tbase, named=()):
                def go(info):
                    info['content'][oid] = data
                    info['ents'][oid] = {'oid': oid, 'type': 'commit', 'mechanism': 'raw:connected', 'tranche': newt}
                    if named:
                        info['ents'][oid]['parents_not_retained'] = list(named)
                    info['man'] = dict(info['man'], tranche_bases=dict(info['man']['tranche_bases'],
                                                                       **{str(newt): tbase}))
                    return {'commit': [mid_data]} if named else None
                return go
            leaves = ': raw:connected, but its history leaves main through '
            expect_history('a raw:connected commit of a new tranche on the latest tranche base, its own base',
                           add_connected(on_latest, on_latest_data, latest), None)
            expect_history('the same commit with the first base recorded as its tranche\'s base',
                           add_connected(on_latest, on_latest_data, man0['base']), 'H4',
                           msg=on_latest[:12] + leaves + latest[:12])
            expect_history('a raw:connected commit whose history reaches its base through a commit the archive '
                           'does not hold', add_connected(on_mid, on_mid_data, latest, named=(mid,)), 'H4',
                           msg=on_mid[:12] + leaves + mid[:12])
            # the tranche pin: a label is an exact int, a pinned entry keeps its pinned tranche, and an entry the pin
            # does not hold carries a later tranche that has a base; the pin itself matches its count and digest
            expect('a pinned tranche-2 entry relabelled tranche 4', fixture_edit(
                lambda m: next(x for x in m['objects'] if x['oid'] == t2raw['oid']).__setitem__('tranche', 4)), 'O3')

            def closed(t):
                def go(d):
                    man = json.load(open(os.path.join(d, 'manifest.json')))
                    o = new_blob(d, man, b'an entry the pin does not hold\n')
                    next(x for x in man['objects'] if x['oid'] == o)['tranche'] = t
                    if t == 6:
                        man['tranche_bases'].pop('5', None)
                    save(d, man)
                return go
            expect('an entry the pin does not hold, labelled tranche 2', closed(2), 'O3')
            expect('an entry the pin does not hold, labelled tranche 4', closed(4), 'O3')
            expect('an entry labelled a later tranche that has no base', closed(6), 'O3')
            # the pin's own count and digest: each edit must fail with that message itself, never only with the
            # per-entry label failures an edit may also cause
            pinmsg = 'O3 the checker\'s pinned tranche-2 membership is not its recorded count and sha256'
            pinned2 = TRANCHE_MEMBERS[2]

            def expect_pin(name, members):
                try:
                    TRANCHE_MEMBERS[2] = frozenset(members)
                    fails, _ = check_with(fresh(), root, False, Fails())
                finally:
                    TRANCHE_MEMBERS[2] = pinned2
                results.append((name, 'O3', 'FAILS as required' if pinmsg in fails else 'NOT DETECTED', fails[:1]))
            expect_pin('the checker\'s tranche-2 pin edited without its count and digest', pinned2 - {t2raw['oid']})
            expect_pin('the checker\'s tranche-2 pin with a pinned tranche-4 commit added', pinned2 | {stand[0]})
            expect_pin('the checker\'s tranche-2 pin with one id swapped for a tranche-4 commit, its count kept',
                       (pinned2 - {t2raw['oid']}) | {stand[0]})

        # O10 and O7, the citation lifecycle, on the fixture above. The stand-in record is laid out as
        # KTOKEN-MAXCONE-1's design evidence is: each head in full on one line, and its run with the head's
        # eight-digit form on the next. Each case checks a copy against a root that shows this repository through
        # symlinks except along the paths the case writes; nothing is written to this repository. Every case named in
        # lifecycle_cases must run: one that does not is a failure (below), never a skip.
        lifecycle_cases = (
            'lifecycle (a): the record not in the tree, the entry pending',
            'lifecycle (b): the record lands citing the id and run, the manifest unchanged (eligible)',
            'lifecycle (c): the entry promoted to the record\'s two lines, which O7 verifies',
            'lifecycle (c-partial): one entry promoted, the other on the same record still awaiting (eligible)',
            'lifecycle (c-full): both entries on the record promoted (cited)',
            'lifecycle (d): the record lands citing another commit id',
            'lifecycle (e): the record removed while the entry is cited',
            'lifecycle (e-full): the record removed while both entries are cited',
            'history mode with the record landed and the citation still pending (eligible)',
            'F1 O10: the record swaps the two full ids, keeping their eight-digit forms',
            'F1 O10: the record mistypes the full id after digit 10',
            'F1 O10: the run line states another head',
            'F1 O7: promoted to the swapped full id and the run line beside the other',
            'F1 O7: promoted to the mistyped full id\'s line and the run line',
            'F1 O7: promoted to the run line that states another head',
            'CN-1: the near-miss head promoted with the token rule and tranche 3',
            'CN-1: the near-miss head promoted with the token rule and tranche \'4\'',
            'CN-1: the near-miss head promoted with the token rule and tranche 2',
            'CN-1: the near-miss head promoted with the token rule and tranche True',
            'CN-1: the near-miss head promoted with the token rule and tranche 4.0',
            'CN-3 f1: a promotion that maps the run line only',
            'CN-3 f5: a second correct citation in the record left unmapped',
            'CN-3 f5: a second correct citation in the record (eligible, both qualifying)',
            'CN-3 f6: the id cited again in the record, unmapped',
            'CN-3: a location mapped twice',
            'CN-3 d-far: a far line cites the run beside another head',
            'CN-3 d-far-nohead: a far line cites the run without its head',
            'CN-3 d-far, promoted: the far line names another head',
            'CN-3: a duplicate free-standing citation with a conflicting full head',
            'CN-3: the run named inside an evidence file name with its digest (eligible)',
            'CN-3: the same, promoted to the citations alone (cited)',
            'CN-3: an embedded mention beside a different full head',
            'CN-3: the run named only inside an identifier',
            'CN-3: an embedded mention mapped as a run citation',
            'N1: the run line states another head in uppercase',
            'N1: another head glued into a file name beside the run (a 52-digit hex word)',
            'N1: an uppercase 64-digit digest beside the file name (eligible)',
            'N2: a seven-digit form of another head beside the run',
            'N2: the head stated beside the run only as its eight-digit form',
            'N2: the summary counts an eligible entry apart, never as cited',
            'the checker\'s tranche-2 pin edited without its count and digest',
            'the checker\'s tranche-2 pin with a pinned tranche-4 commit added',
            'the checker\'s tranche-2 pin with one id swapped for a tranche-4 commit, its count kept',
            'a tranche-2 run citation whose line holds its run as a whole word (cited)',
            'a tranche-2 run citation whose line holds its run only attached to a letter',
            'a lifecycle run citation whose line holds its run only attached to a letter',
            'N1: an all-decimal 45-digit word beside the run\'s file name',
            'boundary (a): a genuine 64-digit digest beside the citation and the file name passes',
            'boundary (b): a file name with a digest never establishes the citation',
            'boundary (b): a 64-digit hex word never states the head',
            'boundary (c): a conflicting head beside the citation fails, even beside a digest',
            'documented limitation: another head as the last 40 digits of a 64-digit word beside a file name passes',
            'a promoted lifecycle entry without a run citation',
            'the id cited in another file than the named record: still pending',
            'a pending entry that also carries cited',
            'a pending entry that carries an empty cited list',
            'a pending entry that records no run (N5)',
            'the record lands citing the id beside another run',
            'the record holds the run only inside a hex word',
            'the record lands on other lines than the entry records',
            'the record lands on exactly the lines the entry records',
            'the record lands without the id form the entry records',
            'a pending entry that records another commit\'s id as its form',
            'a pending entry whose run is retained with a run.json that is not JSON (N4)',
            'a pending entry whose run is retained with a run.json naming no head (N4)',
            'a pending entry whose run is retained with another head',
            'a promoted run citation whose run is retained with another head',
            'a pending record inside the archive',
            'a promoted citation that records another run',
            'a promoted citation that records another commit\'s id the line also holds')
        if fixture_ok:
            oid, sib = stand
            rid, srid = sruns
            rec = srec
            other = hashlib.sha1(b'another commit ' + oid.encode()).hexdigest()
            heads = [(oid, rid), (sib, srid), (other, '9' * 11)]
            digest = sha256(b'a stand-in log\n')

            def record(hs, eight=None):
                """Block i: its head in full on line 3+3i, its run and the head's eight-digit form (or eight[i]) on
                line 4+3i, a blank line."""
                out = '# a stand-in for a record as it lands on main\n\n'
                for i, (h, r) in enumerate(hs):
                    out += ('- `%s`: the head of a design run.\n- The workflow was dispatched on exactly that head: run '
                            '%s, `head_sha` `%s…`.\n\n' % (h, r, (eight or {}).get(i, h[:8])))
                return out

            def line(t, n, new):
                L = t.split('\n')
                L[n - 1] = new
                return '\n'.join(L)
            good = record(heads)
            n1, n2 = 3, 4
            end = good.count('\n') + 1          # the first line an appended text occupies
            # the three mutations of the real record that review a239728f F1 measured, on the stand-in: the full ids
            # of the first two heads swapped, their eight-digit forms kept; the full id mistyped after digit 10; the
            # run line stating another head
            swapped = record([(sib, rid), (oid, srid)] + heads[2:], eight={0: oid[:8], 1: sib[:8]})
            typo_id = oid[:10] + ''.join('1' if ch == '0' else '0' for ch in oid[10:18]) + oid[18:]
            typo = record([(typo_id, rid)] + heads[1:], eight={0: oid[:8]})
            wrong_head = record(heads, eight={0: other[:8]})
            ci_run = '%s/ci/%s/run.json' % (ARCHIVE_REL, rid)
            evrow = '| path | sha256 |\n| --- | --- |\n| `evidence/run1-%s.json` | `%s` |\n' % (rid, digest)
            runline = good.split('\n')[n2 - 1]

            def overlay(files):
                t = os.path.join(tmp, 'root')
                if os.path.isdir(t):
                    shutil.rmtree(t)
                os.makedirs(t)
                for nm in os.listdir(root):
                    os.symlink(os.path.join(root, nm), os.path.join(t, nm))
                for rel, body in files.items():
                    src, dst = root, t
                    for part in rel.split('/')[:-1]:
                        src, dst = os.path.join(src, part), os.path.join(dst, part)
                        if os.path.islink(dst):
                            os.unlink(dst)
                            os.makedirs(dst)
                            for nm in os.listdir(src):
                                os.symlink(os.path.join(src, nm), os.path.join(dst, nm))
                        elif not os.path.isdir(dst):
                            os.makedirs(dst)
                    if os.path.lexists(os.path.join(t, rel)):
                        os.unlink(os.path.join(t, rel))
                    if body is not None:
                        open(os.path.join(t, rel), 'w', encoding='utf-8').write(body)
                return t

            def promoted(cites=None, who=None, tranche=None):
                """The entry who (the first stand-in by default) promoted to citations (line, tokens, run or None);
                by default its own block's two lines."""
                who = who or oid
                k = stand.index(who)
                dflt = [(n1 + 3 * k, [who], None), (n2 + 3 * k, [who[:8]], sruns[k])]

                def fn(m):
                    x = next(y for y in m['objects'] if y['oid'] == who)
                    x.pop('awaiting_citation')
                    x['cited'] = [dict({'class': 'native-record', 'location': '%s:%d' % (rec, n), 'tokens': toks},
                                       **({'role': 'run-head', 'run': run, 'via': 'run'} if run else
                                          {'role': 'other:design-run', 'via': 'token'}))
                                  for n, toks, run in cites or dflt]
                    if tranche is not None:
                        x['tranche'] = tranche
                return fn

            def both(m):
                promoted()(m)
                promoted(who=sib)(m)

            def pending_edit(**kw):
                def fn(m):
                    a = next(y for y in m['objects'] if y['oid'] == oid)['awaiting_citation']
                    a.update(kw)
                    for k in [k for k, v in kw.items() if v is None]:
                        a.pop(k)
                return fn

            def expect_cite(name, files, edit_man, rule, state=None, msg='', states=None, also=None, who=None):
                """rule None: no failure, the stand-ins in the named states, and also(info) when given; otherwise
                rule (a rule, or a list of (rule, message) pairs, each required) with msg in its failure. A rule
                given alone must fail for the entry the case is about (who, the first stand-in by default): its
                message starts with the rule and that entry's id, so another entry's failure never satisfies it.
                A case whose own condition raises fails; it never stops the self-test."""
                d = fresh()
                m = json.load(open(os.path.join(d, 'manifest.json')))
                pend_all(m)
                if edit_man:
                    edit_man(m)
                save(d, m)
                fails, info = check(d, overlay(files))
                cs = info.get('citation_states') or {}
                if rule is None:
                    want = states or {oid: state}
                    off = {o: cs.get(o, ('failing',))[0] for o in want if cs.get(o, ('failing',))[0] != want[o]}
                    try:
                        extra = also is None or bool(also(info))
                        raised = None
                    except Exception as exc:                # reported as this case's failure, not a crash
                        extra, raised = False, exc
                    ok = not fails and not off and extra
                    why = fails[:1] or (['O10 states %s, not %s' % (off, want)] if off else
                                        [] if extra else ['the case\'s own condition does not hold' +
                                                          (' (%r)' % raised if raised else '')])
                    results.append((name, '-', 'PASSES as required' if ok else 'FAILS', why if not ok else []))
                else:
                    rules = rule if isinstance(rule, list) else [('%s %s:' % (rule, (who or oid)[:12]), msg)]
                    ok = all(any(f.startswith(r) and mm in f for f in fails) for r, mm in rules)
                    results.append((name, '/'.join(r for r, _ in rules), 'FAILS as required' if ok else 'NOT DETECTED',
                                    fails[:1]))
                return info

            # (a)-(e): the record absent, then landed with the manifest unchanged, then promoted (one entry, then
            # both); a record that cites another commit; the record removed under promoted entries
            expect_cite('lifecycle (a): the record not in the tree, the entry pending', {rec: None}, None, None, 'pending')
            info_b = expect_cite('lifecycle (b): the record lands citing the id and run, the manifest unchanged (eligible)',
                                 {rec: good}, None, None, states={oid: 'eligible', sib: 'eligible'})
            expect_cite('lifecycle (c): the entry promoted to the record\'s two lines, which O7 verifies', {rec: good},
                        promoted(), None, 'cited')
            expect_cite('lifecycle (c-partial): one entry promoted, the other on the same record still awaiting (eligible)',
                        {rec: good}, promoted(), None, states={oid: 'cited', sib: 'eligible'})
            expect_cite('lifecycle (c-full): both entries on the record promoted (cited)', {rec: good}, both, None,
                        states={oid: 'cited', sib: 'cited'})
            expect_cite('lifecycle (d): the record lands citing another commit id', {rec: record([(other, rid)] + heads[1:])},
                        None, 'O10', msg='does not cite it')
            expect_cite('lifecycle (e): the record removed while the entry is cited', {rec: None}, promoted(), 'O7',
                        msg='does not exist')
            expect_cite('lifecycle (e-full): the record removed while both entries are cited', {rec: None}, both,
                        [('O7 %s' % oid[:12], 'does not exist'), ('O7 %s' % sib[:12], 'does not exist')])
            # the object checks do not read the citation's state: history mode passes with the citation eligible
            hf = Fails()
            if info_b.get('citation_states', {}).get(oid, ('',))[0] == 'eligible':
                history_checks(root, info_b, hf)
            results.append(('history mode with the record landed and the citation still pending (eligible)', '-',
                            'PASSES as required' if not hf and info_b.get('citation_states') else 'FAILS', hf[:1]))
            # a wrong head beside the run (review a239728f F1), pending and promoted
            expect_cite('F1 O10: the record swaps the two full ids, keeping their eight-digit forms', {rec: swapped},
                        None, 'O10', msg='names another head')
            expect_cite('F1 O10: the record mistypes the full id after digit 10', {rec: typo}, None, 'O10',
                        msg='names another head')
            expect_cite('F1 O10: the run line states another head', {rec: wrong_head}, None, 'O10',
                        msg='names another head')
            expect_cite('F1 O7: promoted to the swapped full id and the run line beside the other', {rec: swapped},
                        promoted([(n1 + 3, [oid], None), (n2, [oid[:8]], rid)]), 'O7', msg='names another head')
            expect_cite('F1 O7: promoted to the mistyped full id\'s line and the run line', {rec: typo},
                        promoted([(n1, [oid[:8]], None), (n2, [oid[:8]], rid)]), 'O7', msg='names another head')
            expect_cite('F1 O7: promoted to the run line that states another head', {rec: wrong_head},
                        promoted([(n1, [oid], None), (n2, [rid], rid)]), 'O7', msg='names another head')
            # CN-1: the tranche label never switches the rule off. The near-miss record (the full id mistyped, its
            # eight-digit forms kept) promoted with the token rule's citations and the entry's label edited: O3
            # refuses the label, and O7 still applies the rule to the commit, which the pin decides
            for lab in (3, '4', 2, True, 4.0):
                expect_cite('CN-1: the near-miss head promoted with the token rule and tranche %r' % (lab,), {rec: typo},
                            promoted([(n1, [oid[:8]], None), (n2, [oid[:8]], rid)], tranche=lab),
                            [('O3 %s' % oid[:12], 'tranche'), ('O7 %s' % oid[:12], 'does not hold its token as a word')])
            # CN-3: every qualifying line mapped, nothing mapped twice, every line naming the run checked
            again = '- `%s`: the head again.\n- Run %s again, `head_sha` `%s…`.\n' % (oid, rid, oid[:8])
            expect_cite('CN-3 f1: a promotion that maps the run line only', {rec: good},
                        promoted([(n2, [oid[:8]], rid)]), 'O7', msg='which no citation maps')
            expect_cite('CN-3 f5: a second correct citation in the record left unmapped', {rec: good + again}, promoted(),
                        'O7', msg='which no citation maps')
            expect_cite('CN-3 f5: a second correct citation in the record (eligible, both qualifying)', {rec: good + again},
                        None, None, 'eligible', also=lambda info: (info['citation_states'].get(oid) or ('', ([],)))[1][0] ==
                        [n1, n2, end, end + 1])
            expect_cite('CN-3 f6: the id cited again in the record, unmapped', {rec: good + 'The commit is `%s`.\n' % oid},
                        promoted(), 'O7', msg='which no citation maps')
            expect_cite('CN-3: a location mapped twice', {rec: good},
                        promoted([(n1, [oid], None), (n2, [oid[:8]], rid), (n2, [oid[:8]], rid)]), 'O7', msg='mapped twice')
            dfar = 'Run %s was dispatched on `%s…`.\n' % (rid, other[:8])
            expect_cite('CN-3 d-far: a far line cites the run beside another head', {rec: good + dfar}, None, 'O10',
                        msg='names another head')
            expect_cite('CN-3 d-far-nohead: a far line cites the run without its head', {rec: good + 'Run %s passed.\n' % rid},
                        None, 'O10', msg='does not state the full id')
            expect_cite('CN-3 d-far, promoted: the far line names another head', {rec: good + dfar}, promoted(), 'O7',
                        msg='names another head')
            expect_cite('CN-3: a duplicate free-standing citation with a conflicting full head',
                        {rec: good + '- `%s`: a head.\n- Run %s, `head_sha` `%s…`.\n' % (other, rid, other[:8])}, None,
                        'O10', msg='names another head')
            expect_cite('CN-3: the run named inside an evidence file name with its digest (eligible)', {rec: good + evrow},
                        None, None, 'eligible', also=lambda info: (info['citation_states'].get(oid) or ('', ([], [], [])))[1][2] == [end + 2])
            expect_cite('CN-3: the same, promoted to the citations alone (cited)', {rec: good + evrow}, promoted(), None,
                        'cited')
            expect_cite('CN-3: an embedded mention beside a different full head',
                        {rec: good + '| `evidence/run1-%s.json` | head `%s` |\n' % (rid, other)}, None, 'O10',
                        msg='names another head')
            expect_cite('CN-3: the run named only inside an identifier', {rec: line(
                good, n2, '- The log is `evidence/run1-%s.json`, `head_sha` `%s…`.' % (rid, oid[:8]))}, None, 'O10',
                msg='only inside an identifier')
            expect_cite('CN-3: an embedded mention mapped as a run citation', {rec: good + evrow},
                        promoted([(n1, [oid], None), (n2, [oid[:8]], rid), (end + 2, [rid], rid)]), 'O7',
                        msg='only inside an identifier')
            # N1 and N2: the head rule read case-folded, over-long words, short other forms, the full id required
            expect_cite('N1: the run line states another head in uppercase', {rec: record(heads, eight={0: other[:8].upper()})},
                        None, 'O10', msg='names another head')
            expect_cite('N1: another head glued into a file name beside the run (a 52-digit hex word)',
                        {rec: good + '| `evidence/run1-%sa%s.json` |\n' % (rid, other)}, None, 'O10',
                        msg='names another head')
            expect_cite('N1: an uppercase 64-digit digest beside the file name (eligible)',
                        {rec: good + evrow.replace(digest, digest.upper())}, None, None, 'eligible')
            expect_cite('N2: a seven-digit form of another head beside the run', {rec: record(heads, eight={0: other[:7]})},
                        None, 'O10', msg='names another head')
            expect_cite('N2: the head stated beside the run only as its eight-digit form',
                        {rec: line(good, n1, '- The head of a design run, named on the next line.')}, None, 'O10',
                        msg='does not state the full id')
            expect_cite('N2: the summary counts an eligible entry apart, never as cited', {rec: good}, None, None,
                        'eligible', also=lambda info: citation_summary(
                            {'a': ('cited', None), 'b': ('eligible', None), 'c': ('pending', None)}) ==
                        'citations (O10): 1 cited, 1 pending (record not in the tree), 1 eligible for promotion')
            # a run is held as a whole word: a run attached to a letter is not the run, on the token-rule path O7
            # keeps for tranche 2's pinned commits as on the lifecycle path (its first condition, before the rule)
            leg = next(e for e in man0['objects'] if e['oid'] in TRANCHE_MEMBERS[2] and e['type'] == 'commit' and
                       any(c.get('run') for c in e.get('cited', [])))
            lrun = next(c['run'] for c in leg['cited'] if c.get('run'))
            lrec = 'verification/ZZ-SELF-TEST/o7-legacy-stand-in.md'

            def legacy_cite(m):
                next(y for y in m['objects'] if y['oid'] == leg['oid'])['cited'] = [
                    {'class': 'native-record', 'location': '%s:2' % lrec, 'tokens': [lrun], 'run': lrun, 'via': 'run'}]
            expect_cite('a tranche-2 run citation whose line holds its run as a whole word (cited)',
                        {lrec: '# a legacy stand-in\n- The run %s passed at that head.\n' % lrun}, legacy_cite, None,
                        states={oid: 'pending'})
            expect_cite('a tranche-2 run citation whose line holds its run only attached to a letter',
                        {lrec: '# a legacy stand-in\n- The run%s passed at that head.\n' % lrun}, legacy_cite, 'O7',
                        msg='does not hold its run', who=leg['oid'])
            expect_cite('a lifecycle run citation whose line holds its run only attached to a letter',
                        {rec: good.replace('run %s,' % rid, 'run%s,' % rid, 1)}, promoted(), 'O7',
                        msg='does not hold its run')
            expect_cite('N1: an all-decimal 45-digit word beside the run\'s file name',
                        {rec: good + '| `evidence/run1-%s.json` | `%s` |\n' % (rid, '9' * 45)}, None, 'O10',
                        msg='names another head')
            # the digest boundary: a hex word of 64 digits or more is opaque. A genuine digest passes; a file name with
            # a digest never establishes a citation, and such a word never states the head; a conflicting head beside
            # the citation fails even beside a digest. Another head written as part of such a word is not read: the
            # documented limitation, recorded with its passing verdict so that a change of behaviour shows here
            expect_cite('boundary (a): a genuine 64-digit digest beside the citation and the file name passes',
                        {rec: line(good, n2, runline + ' Log `evidence/run1-%s.json`, sha256 `%s`.' % (rid, digest))},
                        None, None, 'eligible')
            expect_cite('boundary (b): a file name with a digest never establishes the citation', {rec: line(
                good, n2, '- The log is `evidence/run1-%s.json`, sha256 `%s%s`.' % (rid, '0' * 24, oid))}, None, 'O10',
                msg='only inside an identifier')
            expect_cite('boundary (b): a 64-digit hex word never states the head', {rec: line(line(
                good, n1, '- The head of a design run, named on the next line.'), n2,
                runline + ' Digest `%s%s`.' % ('0' * 24, oid))}, None, 'O10', msg='does not state the full id')
            expect_cite('boundary (c): a conflicting head beside the citation fails, even beside a digest', {rec: line(
                wrong_head, n2, wrong_head.split('\n')[n2 - 1] + ' sha256 `%s`.' % digest)}, None, 'O10',
                msg='names another head')
            expect_cite('documented limitation: another head as the last 40 digits of a 64-digit word beside a file name '
                        'passes', {rec: good + '| `evidence/run1-%s.json` | `%s%s` |\n' % (rid, '0' * 24, other)}, None,
                        None, 'eligible')
            expect_cite('a promoted lifecycle entry without a run citation', {rec: good},
                        promoted([(n1, [oid], None)]), 'O7', msg='without a run citation')
            # a pull request is never evidence: the id cited in a file that is not the named record leaves it pending
            expect_cite('the id cited in another file than the named record: still pending',
                        {rec: None, os.path.dirname(rec) + '/ZZ-OTHER.md': good}, None, None, 'pending')
            expect_cite('a pending entry that also carries cited', {rec: good},
                        lambda m: next(y for y in m['objects'] if y['oid'] == oid).__setitem__(
                            'cited', [{'location': '%s:%d' % (rec, n1), 'tokens': [oid]}]), 'O10', msg='together')
            expect_cite('a pending entry that carries an empty cited list', {rec: None},
                        lambda m: next(y for y in m['objects'] if y['oid'] == oid).__setitem__('cited', []), 'O10',
                        msg='together')
            expect_cite('a pending entry that records no run (N5)', {rec: good}, pending_edit(run=None), 'O10',
                        msg='malformed')
            expect_cite('the record lands citing the id beside another run', {rec: record([(oid, '1' + rid)] + heads[1:])},
                        None, 'O10', msg='does not name run %s' % rid)
            expect_cite('the record holds the run only inside a hex word', {rec: good.replace(
                'run %s,' % rid, 'run a%sbc,' % rid, 1)}, None, 'O10', msg='does not name run %s' % rid)
            expect_cite('the record lands on other lines than the entry records', {rec: good}, pending_edit(lines=[n1 + 10]),
                        'O10', msg='not on the recorded')
            expect_cite('the record lands on exactly the lines the entry records', {rec: good},
                        pending_edit(lines=[n1, n2]), None, 'eligible')
            expect_cite('the record lands without the id form the entry records', {rec: good},
                        pending_edit(tokens=[oid[:12]]), 'O10', msg='does not cite it as')
            expect_cite('a pending entry that records another commit\'s id as its form', {rec: None},
                        pending_edit(tokens=[other[:8]]), 'O10', msg='malformed')
            expect_cite('a pending entry whose run is retained with a run.json that is not JSON (N4)',
                        {rec: None, ci_run: '{not json\n'}, None, 'O10', msg='not readable JSON')
            expect_cite('a pending entry whose run is retained with a run.json naming no head (N4)',
                        {rec: None, ci_run: json.dumps({'id': int(rid)})}, None, 'O10', msg='names no head commit')
            expect_cite('a pending entry whose run is retained with another head', {rec: None,
                        ci_run: json.dumps({'head_sha': other})}, None, 'O10', msg='whose head')
            expect_cite('a promoted run citation whose run is retained with another head', {rec: good,
                        ci_run: json.dumps({'head_sha': other})}, promoted(), 'O7', msg='whose head')
            expect_cite('a pending record inside the archive', {rec: None},
                        pending_edit(record=ARCHIVE_REL + '/x.md'), 'O10', msg='malformed')
            # after promotion, O7: a recorded run not on the line, a hex token of another commit on the line
            expect_cite('a promoted citation that records another run', {rec: good},
                        promoted([(n1, [oid], None), (n2, [oid[:8]], '1' + rid)]), 'O7', msg='does not hold its run')
            expect_cite('a promoted citation that records another commit\'s id the line also holds',
                        {rec: good.replace('the head of a design run', 'the head of a design run, not `%s`' % other, 1)},
                        promoted([(n1, [other], None), (n2, [oid[:8]], rid)]), 'O7', msg='not a prefix of its id')
        ran = {r[0] for r in results}
        for name in lifecycle_cases:
            if name not in ran:
                results.append((name + ' [did not run]', '-', 'NOT DETECTED', []))
    finally:
        _SCAN_MEMO = _HISTORY_MEMO = None
        shutil.rmtree(tmp, ignore_errors=True)
    width = max(len(r[0]) for r in results)
    bad = 0
    for name, rule, verdict, f in results:
        print('  %-*s  %-3s  %s%s' % (width, name, rule, verdict, ('  [' + f[0][:90] + ']') if f else ''))
        bad += verdict not in ('FAILS as required', 'PASSES as required')
    print('self-test: %s (%d cases)' % ('OK' if not bad else 'FAILED', len(results)))
    return 1 if bad else 0


def materialize(root, info):
    """Write every stored object into this repository's object store (adds objects only; no ref changes), so that
    tools that need a retained commit in the repository, such as reproduce.py, can check it out."""
    tmp = tempfile.mkdtemp(prefix='materialize-')
    try:
        for typ in ('blob', 'tree', 'commit'):
            oids = sorted(o for o in info['content'] if info['ents'][o]['type'] == typ)
            paths = []
            for o in oids:
                pth = os.path.join(tmp, o)
                with open(pth, 'wb') as fh:
                    fh.write(info['content'][o])
                paths.append(pth)
            p = git(['hash-object', '-w', '-t', typ, '--stdin-paths'], root, inp=('\n'.join(paths) + '\n').encode())
            if p.returncode or p.stdout.decode().split() != oids:
                print('FAIL  materialize: git did not write every %s with its id' % typ)
                return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print('materialized: %d objects written to this repository\'s object store' % len(info['content']))
    return 0


def main(argv):
    if '--self-test' in argv:
        return self_test(ROOT)
    history = '--reconstitute' in argv or '--materialize' in argv
    fails, info = check_with(OBJ, ROOT, history, Fails())
    if '--materialize' in argv and not fails:
        if materialize(ROOT, info):
            return 1
    for f in fails:
        print('FAIL  ' + f)
    if info:
        n = info['man']['objects']
        print('objects: %d entries, %d stored and verified, %d withheld, %d ids expected on main%s'
              % (len(n), info['stored'], sum(1 for e in n if e['mechanism'] in WITHHELD), len(info['external']),
                 ' (verified)' if history and not fails else ''))
        if info.get('reconstituted'):
            print('reconstituted: %(refs)d refs, %(shallow_boundaries)d raw:tree commits as shallow boundaries; fsck --connectivity-only clean' % info['reconstituted'])
        by = {}
        for e in n:
            by[e['mechanism']] = by.get(e['mechanism'], 0) + 1
        print('mechanisms: ' + ', '.join('%s %d' % kv for kv in sorted(by.items())))
        named = sorted({p for e in n for p in e.get('parents_not_retained', [])})
        print('parents named, not retained (%d): %s' % (len(named), ' '.join(p[:12] for p in named)))
        part = [e for e in n if e['mechanism'] == 'raw:partial-tree']
        print('partial trees (%d): %s' % (len(part), ', '.join('%s withholds %d' % (e['oid'][:12], len(e['withheld_blobs']))
                                                          for e in part)))
        st = info.get('citation_states', {})
        print(citation_summary(st))
        for o, (s, where) in sorted(st.items()):
            a = info['ents'][o].get('awaiting_citation') or {}
            if s == 'pending':
                print('  pending   %s  #%s %s, %s' % (o[:12], a['pull_request'], a['round'], a['record']))
            elif s == 'eligible':
                # the qualifying lines a promotion maps, the run's citations among them, and the lines that name
                # the run only inside an identifier (checked, not citations)
                print('  eligible  %s  %s:%s (run %s cited at :%s%s)' % (
                    o[:12], a['record'], ','.join(map(str, where[0])), a['run'], ','.join(map(str, where[1])),
                    '; named in an identifier, not a citation, at :%s' % ','.join(map(str, where[2])) if where[2] else ''))
    print('check_objects: %s' % ('OK' if not fails else 'FAILED (%d)' % len(fails)))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
