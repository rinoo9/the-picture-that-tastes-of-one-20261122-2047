#!/usr/bin/env python3
"""The picture that tastes of one ingredient.

Entry for the make.fun bounty "The picture that tastes of one ingredient".

The entry is a single 1024x1024 picture of one perfect strawberry:
ripe, glossy, and so vivid you can almost taste it before the first bite.
One fruit, one flavour, nothing else on the plate. No garnish, no sauce,
no second ingredient competing for attention — the strawberry is the
whole picture, and the whole picture is the strawberry.

This program is the entry builder. It takes the bundled strawberry.png
asset (kept next to this file), verifies it is a 1024x1024 PNG no larger
than 1 MiB, and copies it byte-for-byte to /output/entry.png.
Deterministic by construction: the output is an exact copy of the asset.
"""

import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "strawberry.png")
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.png")

MAX_BYTES = 1_048_576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_png_dimensions(data):
    """Return (width, height) from a PNG's IHDR chunk."""
    if data[:8] != PNG_SIGNATURE:
        raise ValueError("not a PNG file (bad signature)")
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise ValueError("not a PNG file (missing IHDR)")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main():
    if not os.path.isfile(SOURCE):
        print(
            f"error: bundled asset not found: {SOURCE}\n"
            "expected strawberry.png next to main.py",
            file=sys.stderr,
        )
        sys.exit(1)

    with open(SOURCE, "rb") as f:
        data = f.read()

    if len(data) > MAX_BYTES:
        raise ValueError(
            f"entry too large: {len(data)} bytes (max {MAX_BYTES})"
        )

    width, height = read_png_dimensions(data)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            f"expected {EXPECTED_WIDTH}x{EXPECTED_HEIGHT}, "
            f"got {width}x{height}"
        )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    print(f"wrote {OUTPUT_PATH}")
    print(f"dimensions: {width}x{height}")
    print(f"size: {len(data)} bytes")


if __name__ == "__main__":
    main()
