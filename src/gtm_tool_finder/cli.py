import argparse
from . import search, KINDS


def main(argv=None):
    p = argparse.ArgumentParser(prog="gtm-tool-finder", description="Search OneGTMLab's GTM tool directory.")
    p.add_argument("query", nargs="*", help="words to search for, e.g. apollo or 'apollo clay'")
    p.add_argument("--kind", choices=[k.lower() for k in KINDS], help="only this kind of page")
    p.add_argument("--limit", type=int, default=20)
    a = p.parse_args(argv)
    hits = search(" ".join(a.query), a.kind, a.limit)
    if not hits:
        print("Nothing found. Try a tool name like apollo or clay.")
        return 1
    for r in hits:
        print(f"[{r['kind']}] {r['name']}\n    {r['url']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
