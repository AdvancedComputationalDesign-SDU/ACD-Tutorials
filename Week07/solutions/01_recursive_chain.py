"""Worked solution: A shrinking recursive chain

Write lengths(length, remaining). Return [] if remaining==0 or
length<0.5. Otherwise return the current length followed by a call
with length*0.5 and remaining-1. Predict lengths(4,5). Draw the
returned sequence as connected horizontal segments. Explain both stops.

One possible solution. Discuss another valid policy or representation.
"""
from pathlib import Path
import sys
import matplotlib.pyplot as plt

if "__file__" in globals():
    WEEK_DIR = Path(__file__).resolve().parents[1]
else:
    WEEK_DIR = Path.cwd()
    if WEEK_DIR.name in {"tutorial", "references", "exercises", "solutions", "optional"}:
        WEEK_DIR = WEEK_DIR.parent
    if (WEEK_DIR / "Week07" / "tutorial").is_dir():
        WEEK_DIR = WEEK_DIR / "Week07"
sys.path.insert(0, str(WEEK_DIR / "tutorial"))
OUTPUT_DIR = WEEK_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def lengths(length, remaining):
    if remaining == 0 or length < 0.5:
        return []
    return [length] + lengths(length * 0.5, remaining - 1)

if __name__ == "__main__":
    assert lengths(4, 5) == [4, 2, 1, 0.5]
    assert lengths(4, 0) == []
    fig, ax = plt.subplots(figsize=(7, 2))
    start = 0
    for i, length in enumerate(lengths(4, 5)):
        ax.plot([start, start + length], [0, 0], linewidth=5, color=plt.cm.viridis(i / 4))
        ax.scatter([start], [0], color="black")
        start += length
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "solution_01_recursive_chain.png", dpi=160)
    print("Checks passed: 01_recursive_chain")
    plt.show()
    plt.close(fig)
