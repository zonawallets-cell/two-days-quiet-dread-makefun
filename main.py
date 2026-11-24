"""Two Days of Quiet Dread — one-line code review comment.

Writes a single line (at most 140 characters) approving a pull request
while carrying quiet existential dread, to <output_dir>/entry.txt.

Pure standard library (os only). Fully deterministic: the same line,
byte for byte, on every run.
"""

import os

LINE = (
    "LGTM. The diff is clean, the tests are green, and somewhere "
    "a pager is quietly warming up."
)

MAX_CHARS = 140


def validate(text):
    """Gate: 1-140 chars, exactly one line, not only whitespace, UTF-8."""
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry exceeds %d chars: %d" % (MAX_CHARS, len(text)))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    text = validate(LINE.strip())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
