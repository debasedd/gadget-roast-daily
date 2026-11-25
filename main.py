#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — writes one line to /output/entry.txt.

The roast targets a gadget worn every day — a smartwatch — and the joke
is a specific behaviour anyone who owns one recognises: it congratulates
you for standing up, then immediately warns you that your heart rate is
dangerously high... from standing up. The device praises and panics
about the same action in the same breath, which is both the sting of
recognition and the fresh angle: not "the battery dies" or "it needs an
update", but a health gadget that cannot tell exercise from getting out
of a chair. One line, 115 of 200 characters.
"""

import os

LINE = "My smartwatch congratulates me for standing up, then warns me my heart rate is dangerously high \u2014 from standing up."


def main() -> None:
    assert len(LINE) <= 200, f"entry is {len(LINE)} chars, over the 200-char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
