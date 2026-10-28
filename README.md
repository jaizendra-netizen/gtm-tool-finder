# gtm-tool-finder

Search the [OneGTMLab](https://www.onegtmlab.dev) GTM tool directory from your terminal or from Python:

- API reviews for 66 sales and marketing tools: pricing, rate limits, keys and MCP support
- 99 head-to-head tool comparisons, such as Apollo vs Clay
- 110 plain-English definitions of GTM terms

```bash
pip install gtm-tool-finder
gtm-tool-finder apollo
gtm-tool-finder clay --kind comparison
```

```python
from gtm_tool_finder import search

for r in search("enrichment", kind="tool"):
    print(r["name"], r["url"])
```

Every result links to the full page on [onegtmlab.dev/tool-directory](https://www.onegtmlab.dev/tool-directory). The list ships inside the package, so it works offline and sends no data anywhere.

Built by [OneGTMLab](https://www.onegtmlab.dev), a GTM engineering agency. Also available as a [Microsoft Edge extension](https://www.onegtmlab.dev/tool-directory).
