"""Worked solution: A recursive alternative with one influence

Write cells(region,target,remaining). Return [region] when remaining
is zero OR the region does not cover target. Otherwise split the
longest side in half, recurse on each half and join the returned lists.
Use box(0,0,8,5), target Point(1,1), remaining=3. Predict four leaves.
Check leaf area sum=40 and union equals the input. Move the target
onto a split boundary and explain how covers changes which cells divide.

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

from shapely.geometry import Point, box
from shapely.ops import unary_union

def cells(region, target, remaining):
    if remaining == 0 or not region.covers(target):
        return [region]
    xmin, ymin, xmax, ymax = region.bounds
    if xmax - xmin >= ymax - ymin:
        middle = region.centroid.x
        a, b = box(xmin, ymin, middle, ymax), box(middle, ymin, xmax, ymax)
    else:
        middle = region.centroid.y
        a, b = box(xmin, ymin, xmax, middle), box(xmin, middle, xmax, ymax)
    return cells(a, target, remaining - 1) + cells(b, target, remaining - 1)

if __name__ == "__main__":
    region = box(0, 0, 8, 5)
    leaves = cells(region, Point(1, 1), 3)
    assert len(leaves) == 4
    assert abs(sum(leaf.area for leaf in leaves) - 40) < 1e-9
    assert unary_union(leaves).equals(region)
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.5))
    for ax, target in zip(axes, [Point(1, 1), Point(4, 2.5)]):
        leaves = cells(region, target, 3)
        for i, leaf in enumerate(leaves):
            x, y = leaf.exterior.xy
            ax.fill(x, y, color=plt.cm.viridis(i / max(1, len(leaves) - 1)),
                    edgecolor="white", linewidth=1)
        ax.scatter([target.x], [target.y], color="red", marker="+")
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(f"{len(leaves)} leaves")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "solution_04_adaptive_subdivision.png", dpi=160)
    print("Checks passed: 04_adaptive_subdivision")
    plt.show()
    plt.close(fig)
