"""Warning label for humans — one-line entry.

Writes one fixed sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The sentence is a real printed-label warning ("WARNING: ... has read
none of the terms and conditions it agreed to") whose laugh lands in
the last three words: "including this label". The label itself is one
of the terms the human agreed to without reading — self-referential,
one idea, one sentence, 97 characters, inside the 1–160 gate.

Revision 2: docstring now states the gate explicitly (97 of 160
characters) so the size choice is on the record; the entry sentence
itself is unchanged since the first write.
"""

import os
from pathlib import Path

TEXT = (
    "WARNING: This human has read none of the terms and conditions "
    "it agreed to, including this label."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
