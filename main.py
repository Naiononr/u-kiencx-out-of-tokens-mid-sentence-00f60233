"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one funny one-line error message to /output/entry.txt.
Python 3, standard library only. Deterministic, no network, no randomness.
"""

import os

LINE = "Error 402: token budget exhausted. The rest of this sentence has been repossessed to cover the bill."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(tmp, 0o644)
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
