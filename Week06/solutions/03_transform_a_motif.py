"""Worked solution: A reusable transformed motif

Write place_motif(x, y, angle, size), returning a scaled and rotated
triangle placed at (x,y). Transform about local (0,0), then translate.
Use at least five calls in a row. Change only size for a second row.
Predict how uniform scale 0.5 changes the area.

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

from shapely.geometry import Polygon
from shapely.affinity import scale, rotate, translate

def place_motif(x, y, angle, size):
    motif = Polygon([(0, 0), (1, 0), (0.25, 0.6)])
    motif = scale(motif, xfact=size, yfact=size, origin=(0, 0))
    motif = rotate(motif, angle, origin=(0, 0))
    return translate(motif, xoff=x, yoff=y)

if __name__ == "__main__":
    assert abs(place_motif(0, 0, 0, 0.5).area - 0.075) < 1e-12
    fig, ax = plt.subplots(figsize=(7, 3))
    for row, size in enumerate([1.0, 0.5]):
        for column in range(6):
            motif = place_motif(column * 1.5, row * 2, column * 15, size)
            x, y = motif.exterior.xy
            ax.fill(x, y, color="#256d82")
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "solution_03_transform_a_motif.png", dpi=160)
    print("Checks passed: 03_transform_a_motif")
    plt.show()
    plt.close(fig)
