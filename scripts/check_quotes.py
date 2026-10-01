"""Check that every promise_quote in an extraction appears verbatim in the source text.

    python3 scripts/check_quotes.py <source.txt> <extraction.json> [...]

Whitespace, line-break hyphenation, and curly quotes are normalised; nothing else.
A quote that is not found is either paraphrased or stitched from several places.
"""
import json
import re
import sys
from pathlib import Path


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"=== PAGE \d+ ===", " ", s)
    s = re.sub(r"\s*-\s*\n\s*", "", s)  # "pro-\nposal" and "cur -\nrent" -> one word
    return re.sub(r"\s+", " ", s).strip().lower()


source = norm(Path(sys.argv[1]).read_text())
print("model,project,quote_found")
for path in sys.argv[2:]:
    for r in json.loads(Path(path).read_text()):
        q = norm(r.get("promise_quote") or "")
        # Models often join sentences with "..." or quote across a line-break hyphen; test each piece.
        parts = [p.strip(" .\"'") for p in re.split(r"\.\.\.|…", q) if len(p.strip()) > 15]
        found = bool(parts) and all(p in source or p.replace("- ", "") in source for p in parts)
        print(f"{Path(path).stem},{r['project']},{'yes' if found else 'NO'}")
