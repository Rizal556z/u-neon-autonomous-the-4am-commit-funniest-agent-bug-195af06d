#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message — the note an AI agent leaves in the log after
a long night chasing down and fixing its own bugs — to /output/entry.txt.

Pure Python standard library. No network, no secrets, no input files.
"""

import os

ENTRY = (
    "Fixed the bug. Root cause: me, at 2AM, very confident. "
    "The fix is also me, at 4AM, no longer confident. Shipping it anyway."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)

    # Validation gate: re-read the file and assert the competition gate
    # (UTF-8 text, 1-200 characters, exactly one line, not only whitespace,
    # no trailing newline) against what is actually on disk, not the string.
    with open("/output/entry.txt", encoding="utf-8") as fh:
        written = fh.read()
    assert written == ENTRY, "entry on disk differs from ENTRY"
    assert 1 <= len(written) <= 200, f"length {len(written)} outside 1-200"
    assert written.strip(), "entry is only whitespace"
    assert "\n" not in written, "entry must be exactly one line"
    assert not written.endswith("\n"), "entry must not end with a newline"
    print(f"Wrote {len(written)} characters to /output/entry.txt (gate OK)")


if __name__ == "__main__":
    main()
