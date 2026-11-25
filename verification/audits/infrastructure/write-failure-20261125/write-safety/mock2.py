"""Mock transport extensions for gate2 controls. mock.py is unchanged; this subclasses it.
No network, no subprocess."""
import copy
from mock import MockGitHub, MockGit  # noqa: F401


class MockGitHub2(MockGitHub):
    """Adds scripted transformations on top of MockGitHub's modes:
    transforms: {"patch"|"comment"|"create": f(body) -> stored body}, applied to bodies on that
    kind of write; title_transform: f(title) -> stored title, applied on create and PATCH;
    after_write: f(issues, number) applied to the stored objects after a successful write that
    names an object (for example labels emptied or state changed by the same request);
    before_get: f() called before every GET (for example another process halting meanwhile)."""

    def __init__(self, issues=None, mode="verbatim", transforms=None, title_transform=None,
                 after_write=None, before_get=None):
        super().__init__(issues, mode)
        self.transforms = dict(transforms or {})
        self.title_transform = title_transform
        self.after_write = after_write
        self.before_get = before_get
        self._kind = None

    def _alter(self, body):
        f = self.transforms.get(self._kind)
        return f(body) if f else super()._alter(body)

    def request(self, method, path, payload):
        if method == "GET" and self.before_get:
            self.before_get()
        parts = path.split("/")
        self._kind = ("comment" if method == "POST" and parts[-1] == "comments" else
                      "create" if method == "POST" and parts[-1] in ("issues", "pulls") else
                      "patch" if method == "PATCH" else None)
        status, resp = super().request(method, path, payload)
        if self.title_transform and method in ("POST", "PATCH") and payload \
                and "title" in payload and status in (200, 201):
            n = resp["number"]
            self.issues[n]["title"] = self.title_transform(copy.copy(payload["title"]))
        if self.after_write and method != "GET" and status in (200, 201):
            n = (resp.get("number", resp.get("id")) if isinstance(resp, dict)
                 else int(parts[-3] if method == "DELETE" else parts[-2]))
            self.after_write(self.issues, n)
        return status, resp
