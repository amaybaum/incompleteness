"""The record directories the tool authorizes for the record-directory rule (design amendment r4, A.3).

A configuration's directory is admitted to the rule only if it equals a member of this tuple by string equality. The
tuple is part of the tool's files: no configuration, record or command-line argument adds to it, and changing it is a
tool revision. It lies outside the engine, which carries no retirement constant (design sec. 16.1).
"""

authorized_record_directories = ('verification/audits/foundations/a1exit-deletion-20261121',)

# The root under which reconciliation directories lie (design r6 as amended, R6.RECON.1 and the post-freeze route of
# R6.RECON.2): a repository placement fact (AGENTS.md sec. A.36), kept outside the engine for the same reason.
reconciliation_root = 'verification/audits/'

# The owner identities of formal adjudication (design r4 of PR #1605, R6.ADJ.3; adopted with OD-1 to OD-7 at their
# defaults): an adjudication's authorization is attributed to one of these identity strings. Changed only by a tool
# revision, as the admitted record directories are (R6.RDIR.2). Attribution, not verification of the owner's approval.
OWNER_IDENTITIES = ('amaybaum',)

# The id of the side-change class that describes this tool's landing (design r6 R6.TREE.5): the domain the post-freeze
# route keeps reconciliation records out of is that class of the side-change class record the configuration pins.
tool_landing_class_id = 'tool-landing'

# The one-time transition to independently reviewed roots (A1 staging amendment r2, sec. 2, amending R6.PLACE.4 and
# R6.A1CFG.1 for this transition only). Each role names its namespace (a directory and a file-name prefix selecting
# candidate record paths directly in it), its root path, the designated `record_id` and the record schema. A file
# name supplies no authority or ordering. The plan directory of the allow role is the admitted record directory above.
# No configuration, record or command-line argument chooses or widens these selectors; changing them is a tool
# revision under separate authority.
transition_roles = (
    {'role': 'class', 'directory': 'verification/audits/foundations/ledger-coverage-tool-20261123/records/',
     'prefix': 'a1-staging-class-', 'root': 'a1-staging-class-root.json', 'record_id': 'a1-staging-tool-landing',
     'schema': 'oi-side-change-classes/1'},
    {'role': 'allow', 'directory': authorized_record_directories[0] + '/',
     'prefix': 'a1-staging-allow-', 'root': 'a1-staging-allow-root.json', 'record_id': 'a1-staging-w1-w2',
     'schema': 'oi-term-rules/2'},
)
# The frozen control metadata of the transition, read only through the plan's Record pins table (sec. 2): the
# activation descriptor and the prior-freeze declaration, each a direct file of the admitted record directory.
transition_descriptor = 'a1-staging-transition.json'
transition_descriptor_schema = 'oi-a1-staging-transition/1'
transition_prior = 'a1-staging-prior.json'
transition_prior_schema = 'oi-a1-staging-prior/1'

# OBL-29 custody (design c7, R6.CUST.1, R6.CUST.3): the single path of the custody record, and the git blob id of its
# bootstrap version. The bootstrap blob id is a placeholder until the owner designates B0 and the bootstrap version is
# built and independently verified (sec. 3); while it is the placeholder no chain can end at the bootstrap, so custody
# is never established and every cited discharge stays inapplicable (fail closed). Changing either is a tool revision.
custody_path = 'verification/audits/foundations/a1exit-obl29-custody/custody.json'
custody_bootstrap_blob = 'PLACEHOLDER-UNTIL-B0-IS-DESIGNATED'
