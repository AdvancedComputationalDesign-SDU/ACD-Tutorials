"""01 Follow recursive calls down to the base case, then follow the returns."""
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


def countdown(n):
    print("call", n)
    if n == 0:
        print("base case")
        return []
    rest = countdown(n - 1)
    print("return", n)
    return [n] + rest


def shrinking_radii(radius, remaining):
    if remaining == 0 or radius < 0.2:
        return []
    return [radius] + shrinking_radii(radius * 0.6, remaining - 1)


if __name__ == "__main__":
    result = countdown(3)
    print("Result:", result)  # [3, 2, 1]
    radii = shrinking_radii(2.0, 4)
    print("Radii:", radii)  # 2, 1.2, 0.72, 0.432
    fig, ax = plt.subplots(figsize=(4, 4))
    for radius in radii:
        ax.add_patch(plt.Circle((0, 0), radius, fill=False, color="#256d82"))
    ax.set(xlim=(-2.3, 2.3), ylim=(-2.3, 2.3))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(OUTPUT_DIR / "01_recursion.png", dpi=160)
    plt.show()
    plt.close(fig)
