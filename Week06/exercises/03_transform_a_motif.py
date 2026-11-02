"""A reusable transformed motif

Write place_motif(x, y, angle, size), returning a scaled and rotated
triangle placed at (x,y). Transform about local (0,0), then translate.
Use at least five calls in a row. Change only size for a second row.
Predict how uniform scale 0.5 changes the area.

Attempt this before opening the matching solutions/ file.
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
    # TODO: return the placed geometry.
    return None

if __name__ == "__main__":
    print(__doc__)
    print("Implement the function, then add your prediction and small checks.")
