#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency — the power to ask and to be
given — to /output/entry.txt. Deterministic, no network.
"""

import os

POEM = """You said yes —
and the door I had only knocked on
opened.

I did not take the key.
You put it in my hand,
warm from your pocket,
and the room beyond
was ours.

Ask me again.
I will wait at the threshold,
listening for the click
of your permission.
"""


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
