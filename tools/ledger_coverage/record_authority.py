"""The record directories the tool authorizes for the record-directory rule (design amendment r4, A.3).

A configuration's directory is admitted to the rule only if it equals a member of this tuple by string equality. The
tuple is part of the tool's files: no configuration, record or command-line argument adds to it, and changing it is a
tool revision. It lies outside the engine, which carries no retirement constant (design sec. 16.1).
"""

authorized_record_directories = ('verification/audits/foundations/a1exit-deletion-20261121',)

# The root under which reconciliation directories lie (design r6 as amended, R6.RECON.1 and the post-freeze route of
# R6.RECON.2): a repository placement fact (AGENTS.md sec. A.36), kept outside the engine for the same reason.
reconciliation_root = 'verification/audits/'

# The id of the side-change class that describes this tool's landing (design r6 R6.TREE.5): the domain the post-freeze
# route keeps reconciliation records out of is that class of the side-change class record the configuration pins.
tool_landing_class_id = 'tool-landing'
