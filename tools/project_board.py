#!/usr/bin/env python3
"""Read, and optionally update one card's Status on, the OI Research Programme board (#1079).

The board is the GitHub Project users/amaybaum/projects/3. It shows tracking only: under
AGENTS.md §A.45 the Issues hold priorities, readiness and authorization, and Project Status grants
no authorization. This tool is run by .github/workflows/project-board.yml (workflow_dispatch only).

  python3 -I tools/project_board.py read  --out DIR
  python3 -I tools/project_board.py write --out DIR --number N --expected S --status T [--apply]
  python3 -I tools/project_board.py --self-test

`read` writes DIR/board.json. `write` changes the Status of the single board item whose content is
Issue or PR #N of amaybaum/incompleteness, and only if its current Status equals S
(compare-and-set) and T is one of the Status field's options. Without --apply it is a dry run:
every check runs and DIR/plan.json records the change that would be made. With --apply it writes,
reads the item back, and fails unless the Status now equals T; DIR/before.json and DIR/after.json
record both reads. Only the Status field can be written. Nothing is created, deleted or renamed.

The verdict is the exit status (0 = every check passed) and the JSON files (AGENTS.md §A.44).
The token is read from the GH_PROJECTS_TOKEN environment variable and is never printed.
"""
import json
import os
import sys
import urllib.request

OWNER = "amaybaum"          # the board's owner (a user account)
PROJECT_NUMBER = 3          # fixed target: no input can select another project
REPO = "amaybaum/incompleteness"
FIELD = "Status"
SCHEMA = "oi-board/1"
API = "https://api.github.com/graphql"
NONE = "(none)"             # an item with no Status value

READ_QUERY = """
query($owner: String!, $number: Int!, $after: String) {
  user(login: $owner) {
    projectV2(number: $number) {
      id title number
      field(name: "Status") {
        ... on ProjectV2SingleSelectField { id name options { id name } }
      }
      views(first: 50) { nodes { number name layout } }
      items(first: 100, after: $after) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          content {
            __typename
            ... on Issue { number repository { nameWithOwner } }
            ... on PullRequest { number repository { nameWithOwner } }
            ... on DraftIssue { title }
          }
          fieldValueByName(name: "Status") {
            ... on ProjectV2ItemFieldSingleSelectValue { name optionId }
          }
        }
      }
    }
  }
}
"""

WRITE_MUTATION = """
mutation($project: ID!, $item: ID!, $field: ID!, $option: String!) {
  updateProjectV2ItemFieldValue(input: {
    projectId: $project, itemId: $item, fieldId: $field,
    value: { singleSelectOptionId: $option }
  }) { projectV2Item { id } }
}
"""


class Fail(Exception):
    """A failed check: the run stops with a nonzero exit and no further writes."""


def http_transport(query, variables):
    token = os.environ.get("GH_PROJECTS_TOKEN", "")
    if not token:
        raise Fail("GH_PROJECTS_TOKEN is not set")
    body = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(API, data=body, method="POST", headers={
        "Authorization": "bearer " + token,
        "Content-Type": "application/json",
        "User-Agent": "oi-project-board",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    if data.get("errors"):
        # GraphQL error messages do not contain the token; print only their messages.
        raise Fail("GraphQL error: " + "; ".join(str(e.get("message")) for e in data["errors"]))
    return data["data"]


def read_board(transport):
    """Return the board as a dict in the oi-board/1 schema, plus the item ids needed to write."""
    after, items, ids, project = None, [], {}, None
    while True:
        data = transport(READ_QUERY, {"owner": OWNER, "number": PROJECT_NUMBER, "after": after})
        p = ((data or {}).get("user") or {}).get("projectV2")
        if not p:
            raise Fail("project %s/%d not found or not readable" % (OWNER, PROJECT_NUMBER))
        project = project or p
        for node in p["items"]["nodes"]:
            c = node.get("content") or {}
            kind = c.get("__typename", "Unknown")
            fv = node.get("fieldValueByName") or {}
            entry = {"type": kind, "status": fv.get("name") or NONE}
            if kind in ("Issue", "PullRequest"):
                entry["repo"] = c["repository"]["nameWithOwner"]
                entry["number"] = c["number"]
                if entry["repo"] == REPO:
                    key = entry["number"]
                    if key in ids:
                        raise Fail("#%d appears twice on the board" % key)
                    ids[key] = node["id"]
            else:
                entry["title"] = c.get("title", "")
            items.append(entry)
        info = p["items"]["pageInfo"]
        if not info["hasNextPage"]:
            break
        after = info["endCursor"]
    field = project.get("field") or {}
    if field.get("name") != FIELD or not field.get("options"):
        raise Fail("the project has no single-select %r field" % FIELD)
    options = [o["name"] for o in field["options"]]
    counts = {name: 0 for name in options}
    counts[NONE] = 0
    for e in items:
        if e["status"] not in counts:
            raise Fail("an item carries a Status %r that is not an option" % e["status"])
        counts[e["status"]] += 1
    if not items:
        raise Fail("the board returned no items")
    items.sort(key=lambda e: (e["type"], e.get("repo", ""), e.get("number", 0), e.get("title", ""),
                              e["status"]))
    board = {
        "schema": SCHEMA,
        "project": {"owner": OWNER, "number": PROJECT_NUMBER, "title": project["title"]},
        "status_field": {"name": FIELD, "options": options},
        "views": sorted(({"number": v["number"], "name": v["name"], "layout": v["layout"]}
                         for v in project["views"]["nodes"]), key=lambda v: v["number"]),
        "items": items,
        "counts": counts,
    }
    handles = {"project": project["id"], "field": field["id"],
               "options": {o["name"]: o["id"] for o in field["options"]}, "items": ids}
    return board, handles


def item_status(board, number):
    for e in board["items"]:
        if e.get("repo") == REPO and e.get("number") == number:
            return e["status"]
    raise Fail("#%d of %s is not on the board" % (number, REPO))


def dump(out, name, obj):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, sort_keys=True, ensure_ascii=False)
        f.write("\n")


def do_read(out, transport):
    board, _ = read_board(transport)
    dump(out, "board.json", board)
    return board


def do_write(out, number, expected, status, apply, transport):
    board, h = read_board(transport)
    if status not in h["options"]:
        raise Fail("target Status %r is not an option (%s)" % (status, ", ".join(h["options"])))
    current = item_status(board, number)
    if current != expected:
        raise Fail("#%d has Status %r, not the expected %r: nothing written" % (number, current, expected))
    if status == expected:
        raise Fail("#%d already has Status %r: nothing to write" % (number, status))
    plan = {"schema": SCHEMA, "number": number, "from": current, "to": status, "applied": False}
    if not apply:
        dump(out, "plan.json", plan)
        return plan
    dump(out, "before.json", board)
    try:
        transport(WRITE_MUTATION, {"project": h["project"], "item": h["items"][number],
                                   "field": h["field"], "option": h["options"][status]})
    except Exception as e:
        after, _ = read_board(transport)
        dump(out, "after.json", after)
        raise Fail("mutation failed (%s); after.json records the board" % type(e).__name__)
    after, _ = read_board(transport)
    dump(out, "after.json", after)
    now = item_status(after, number)
    if now != status:
        raise Fail("readback: #%d has Status %r, not %r" % (number, now, status))
    changed = [(a, b) for a, b in zip(board["items"], after["items"]) if a != b]
    if (len(board["items"]) != len(after["items"]) or len(changed) != 1
            or changed[0][1].get("repo") != REPO or changed[0][1].get("number") != number):
        raise Fail("readback: the write did not change exactly item #%d" % number)
    plan["applied"] = True
    dump(out, "plan.json", plan)
    return plan


# ---------------------------------------------------------------- self-test (no network)

class FakeBoard:
    """An in-memory stand-in for the GraphQL API, used only by --self-test."""

    def __init__(self, page=2):
        self.options = [("o1", "Planned"), ("o2", "Active"), ("o3", "In review"),
                        ("o4", "Closed (administrative)")]
        self.items = [{"id": "i%d" % n, "number": n, "repo": REPO, "kind": "Issue", "status": s}
                      for n, s in [(1032, "Planned"), (914, "Planned"), (941, "In review")]]
        self.items.append({"id": "d1", "kind": "DraftIssue", "title": "note", "status": None})
        self.page = page
        self.writes = 0

    def __call__(self, query, v):
        if query is WRITE_MUTATION:
            self.writes += 1
            name = dict(self.options)[v["option"]]
            next(i for i in self.items if i["id"] == v["item"])["status"] = name
            return {"updateProjectV2ItemFieldValue": {"projectV2Item": {"id": v["item"]}}}
        start = int(v["after"] or 0)
        chunk = self.items[start:start + self.page]
        nodes = []
        for i in chunk:
            if i["kind"] == "DraftIssue":
                content = {"__typename": "DraftIssue", "title": i["title"]}
            else:
                content = {"__typename": i["kind"], "number": i["number"],
                           "repository": {"nameWithOwner": i["repo"]}}
            fv = {"name": i["status"], "optionId": "x"} if i["status"] else None
            nodes.append({"id": i["id"], "content": content, "fieldValueByName": fv})
        more = start + self.page < len(self.items)
        return {"user": {"projectV2": {
            "id": "P", "title": "OI Research Programme", "number": PROJECT_NUMBER,
            "field": {"id": "F", "name": FIELD, "options": [{"id": a, "name": b} for a, b in self.options]},
            "views": {"nodes": [{"number": 2, "name": "Activity", "layout": "BOARD_LAYOUT"}]},
            "items": {"pageInfo": {"hasNextPage": more, "endCursor": str(start + self.page)},
                      "nodes": nodes}}}}


def self_test():
    import tempfile
    d = tempfile.mkdtemp()
    ok = True

    def check(cond, what):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + what)
        ok &= bool(cond)

    def fails(fn):
        try:
            fn()
        except Fail:
            return True
        return False

    fb = FakeBoard()
    b = do_read(d, fb)
    check(len(b["items"]) == 4 and b["counts"]["Planned"] == 2 and b["counts"][NONE] == 1,
          "read: paginates and counts (incl. an item with no Status)")
    p = do_write(d, 1032, "Planned", "Active", False, fb)
    check(fb.writes == 0 and p["applied"] is False, "dry run writes nothing")
    check(fails(lambda: do_write(d, 1032, "Active", "In review", True, fb)) and fb.writes == 0,
          "compare-and-set: wrong expected Status refuses to write")
    check(fails(lambda: do_write(d, 1032, "Planned", "Held", True, fb)) and fb.writes == 0,
          "an unknown target Status refuses to write")
    check(fails(lambda: do_write(d, 9999, "Planned", "Active", True, fb)) and fb.writes == 0,
          "an item not on the board refuses to write")
    p = do_write(d, 1032, "Planned", "Active", True, fb)
    check(fb.writes == 1 and p["applied"] and item_status(do_read(d, fb), 1032) == "Active",
          "apply: one write, read back, Status changed")

    class Liar(FakeBoard):
        def __call__(self, query, v):
            if query is WRITE_MUTATION:
                self.writes += 1
                return {"updateProjectV2ItemFieldValue": {"projectV2Item": {"id": v["item"]}}}
            return FakeBoard.__call__(self, query, v)
    check(fails(lambda: do_write(d, 914, "Planned", "Active", True, Liar())),
          "readback detects a write that did not take effect")

    class Spill(FakeBoard):
        def __call__(self, query, v):
            r = FakeBoard.__call__(self, query, v)
            if query is WRITE_MUTATION:
                self.items[1]["status"] = "Closed (administrative)"
            return r
    check(fails(lambda: do_write(d, 1032, "Planned", "Active", True, Spill())),
          "readback detects a write that changed another item")

    noop = FakeBoard()
    check(fails(lambda: do_write(d, 914, "Planned", "Planned", True, noop)) and noop.writes == 0,
          "a write to the current Status is refused")

    class LiarSpill(Liar):
        def __call__(self, query, v):
            r = Liar.__call__(self, query, v)
            if query is WRITE_MUTATION:
                self.items[1]["status"] = "Closed (administrative)"
            return r
    check(fails(lambda: do_write(d, 1032, "Planned", "Active", True, LiarSpill())),
          "readback detects a missed write masked by another item's change")

    class Wrong(FakeBoard):
        def __call__(self, query, v):
            if query is WRITE_MUTATION:
                v = dict(v, option="o3")
            return FakeBoard.__call__(self, query, v)
    check(fails(lambda: do_write(d, 1032, "Planned", "Active", True, Wrong())),
          "readback detects a write that set another Status")

    other = FakeBoard()
    other.items.append({"id": "x1", "number": 1032, "repo": "a/other", "kind": "Issue",
                        "status": "Active"})
    check(not fails(lambda: do_write(d, 1032, "Planned", "Active", True, other))
          and [i["status"] for i in other.items if i.get("number") == 1032] == ["Active", "Active"]
          and other.writes == 1, "an item of another repository is neither matched nor written")

    dup = FakeBoard()
    dup.items.append(dict(dup.items[1], id="i914b"))
    check(fails(lambda: do_read(d, dup)), "an Issue that appears twice fails")

    class Boom(FakeBoard):
        def __call__(self, query, v):
            if query is WRITE_MUTATION:
                self.writes += 1
                raise OSError("timeout")
            return FakeBoard.__call__(self, query, v)
    check(fails(lambda: do_write(d, 1032, "Planned", "Active", True, Boom()))
          and os.path.exists(os.path.join(d, "after.json")),
          "a failed mutation still leaves after.json")

    empty = FakeBoard()
    empty.items = []
    check(fails(lambda: do_read(d, empty)), "an empty board fails")
    print("self-test: " + ("ALL PASS" if ok else "FAILED"))
    return 0 if ok else 1


def main(argv):
    if argv[1:] == ["--self-test"]:
        return self_test()
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["read", "write"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--number", type=int)
    ap.add_argument("--expected")
    ap.add_argument("--status")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args(argv[1:])
    try:
        if a.mode == "read":
            b = do_read(a.out, http_transport)
            print("read: %d items; counts %s" % (len(b["items"]), json.dumps(b["counts"], sort_keys=True)))
        else:
            if a.number is None or a.expected is None or a.status is None:
                raise Fail("write needs --number, --expected and --status")
            p = do_write(a.out, a.number, a.expected, a.status, a.apply, http_transport)
            print("write: #%d %r -> %r, applied=%s" % (p["number"], p["from"], p["to"], p["applied"]))
    except Fail as e:
        print("FAIL: " + str(e))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
