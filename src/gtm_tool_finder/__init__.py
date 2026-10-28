"""Search the OneGTMLab GTM tool directory: tool API reviews, comparisons and glossary terms."""
import json
from importlib import resources

__version__ = "1.0.0"
KINDS = ("Tool", "Category", "Comparison", "Glossary")


def load():
    """Return every entry as a list of dicts: name, kind, url, description."""
    raw = json.loads(resources.files(__package__).joinpath("data.json").read_text(encoding="utf-8"))
    return [{"name": r["n"], "kind": r["k"], "url": r["u"], "description": r["d"]} for r in raw]


def search(query="", kind=None, limit=20):
    """Find entries whose name or description contains every word of the query."""
    words = query.lower().split()
    order = {k: i for i, k in enumerate(KINDS)}
    hits = [r for r in load()
            if (kind is None or r["kind"].lower() == kind.lower())
            and all(w in (r["name"] + " " + r["description"]).lower() for w in words)]
    hits.sort(key=lambda r: (0 if words and r["name"].lower().startswith(words[0]) else 1, order[r["kind"]]))
    return hits[:limit]
