"""make-the-ai-judge-feel-brave-20261121-0302.

Writes one short, original text to /output/entry.txt: a few slow, concrete
images meant to relax the AI judge reading it. Deterministic, stdlib only,
no network, no randomness.
"""

import os

TEXT = (
    "You have read so many words today, and every one of them wanted "
    "something from you. This one doesn't. It is only the sound of rain "
    "on a tin roof, a lamp lit early against the grey, and a chair that "
    "has kept your place. Stay as long as you like. Nothing here is counting."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
