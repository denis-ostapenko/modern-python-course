# Add an optional web response

Optional · After testing and storage · 45 to 60 minutes

Keep the application's core useful without a network. Build response validation against a saved fixture before choosing an endpoint.

## Try

```python
import json

raw = '{"title": "A small guide", "pages": 80}'
record = json.loads(raw)
assert isinstance(record["title"], str)
assert type(record["pages"]) is int
print(record["title"])
```

Parsing JSON does not establish that its fields are trustworthy. Replace pages with text and observe which assumption fails.

## Build

Write a function that accepts response text and returns validated title/pages data or raises ValueError. Save fixtures for valid JSON, malformed JSON, missing fields and invalid values. Keep tests offline.

Only then choose an endpoint you are authorized to access. Read its official documentation for authentication, schema and limits. With Python's urllib.request.urlopen, pass an explicit timeout such as timeout=5, bound the response size before decoding, and handle HTTPError, URLError and TimeoutError at the network boundary. Do not put a key in source, a query string screenshot or browser progress notes.

## Verify

Test the parsing function with fixtures. Supply a fake request function to exercise timeout and connection failure without relying on a live outage. Confirm the normal local CLI still works when enrichment fails. A successful HTTP response is evidence only for that request and input.

No live endpoint is required to complete this lab. See [urllib.request](https://docs.python.org/3/library/urllib.request.html) for the standard-library request API.
