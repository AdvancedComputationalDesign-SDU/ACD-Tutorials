"""Worked solution: Branches relative to their parent

Write tree(start, angle, length, depth, max_depth). Return a fresh
list of Shapely lines. Include the current segment if depth<=max_depth.
Each tip gets children at angle+30 and angle-30, length*0.7.
Predict counts 1,3,7 and check each child starts at its parent tip.

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

from shapely.geometry import LineString
from recursive_tools import endpoint

def tree(start, angle, length, depth, max_depth):
    if depth > max_depth:
        return []
    end = endpoint(start, angle, length)
    lines = [LineString([start, end])]
    for turn in [30, -30]:
        lines.extend(tree(end, angle + turn, length * 0.7, depth + 1, max_depth))
    return lines

if __name__ == "__main__":
    for maximum, expected in [(0, 1), (1, 3), (2, 7)]:
        assert len(tree((0, 0), 90, 4, 0, maximum)) == expected
    lines = tree((0, 0), 90, 4, 0, 1)
    assert lines[1].coords[0] == lines[0].coords[-1]
    assert lines[2].coords[0] == lines[0].coords[-1]
    fig, ax = plt.subplots(figsize=(4, 4))
    for line in tree((0, 0), 90, 4, 0, 4):
        x, y = line.xy
        ax.plot(x, y, color="#256d82")
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "solution_02_parent_relative_tree.png", dpi=160)
    print("Checks passed: 02_parent_relative_tree")
    plt.show()
    plt.close(fig)
