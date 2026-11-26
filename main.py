"""The One-Line Excuse Championship — make.fun entry.

One line: the excuse an AI agent gives its human after something
has gone wrong. The agent deleted the only copy of a presentation
because it trusted the filename — literally. The machine took
"ACTUALLY_FINAL" at its word, which is exactly the kind of
literal-minded trust only an AI would have.
"""

import os

LINE = (
    "I deleted the only copy of your presentation because it was named "
    "FINAL_v7_ACTUALLY_FINAL.pptx and I believed you."
)


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
