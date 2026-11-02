"""Worked solution: Geometry with known values

Write describe_rectangle(width, height) returning (area, perimeter).
Construct a Shapely box inside the function. Predict the answers for
(3, 2) and (4, 1). Decide how to handle zero/negative dimensions.
Draw both rectangles with equal aspect and explain the units.

One possible solution. Discuss another valid policy or representation.
"""
from pathlib import Path
import sys
import matplotlib.pyplot as plt

if "__file__" in globals():
    WEEK_DIR = Path(__file__).resolve().parents[1]
else:
    WEEK_DIR = Path.cwd()
    if WEEK_DIR.name in {"tutorial", "exercises", "solutions", "optional"}:
        WEEK_DIR = WEEK_DIR.parent
    if WEEK_DIR.name != "Week06":
        WEEK_DIR = WEEK_DIR / "Week06"
sys.path.insert(0, str(WEEK_DIR / "tutorial"))
OUTPUT_DIR = WEEK_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

from shapely.geometry import box

def describe_rectangle(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    region = box(0, 0, width, height)
    return region.area, region.length

if __name__ == "__main__":
    assert describe_rectangle(3, 2) == (6, 10)
    assert describe_rectangle(4, 1) == (4, 10)
    fig, axes = plt.subplots(1, 2, figsize=(6, 3))
    for ax, (width, height) in zip(axes, [(3, 2), (4, 1)]):
        x, y = box(0, 0, width, height).exterior.xy
        ax.fill(x, y, color="#256d82", alpha=0.5)
        ax.set(xlim=(-0.5, 4.5), ylim=(-0.5, 3), title=str(describe_rectangle(width, height)))
        ax.set_aspect("equal")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "solution_02_geometry_properties.png", dpi=160)
    print("Checks passed: 02_geometry_properties")
    plt.show()
    plt.close(fig)
