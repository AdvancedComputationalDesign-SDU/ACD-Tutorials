"""Add one influence: attraction

Write turn_toward(start, angle, target, strength). Inputs: an XY tuple,
a heading in degrees, a Shapely Point and strength in [0, 1]. Return a
heading in degrees: strength 0 keeps the input; strength 1 faces the target.
Use the shortest signed turn, and keep the heading if start equals target.
Predict a 90-degree heading turning toward Point(10, 0) from (0, 0).
Then identify where this belongs in the baseline recursive call, before
creating its segment. Keep the branching and length rules unchanged.

Attempt this before opening the matching solutions/ file.
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

from shapely.geometry import Point

def turn_toward(start, angle, target, strength):
    """Return a heading in degrees; inputs are described above."""
    # TODO: Find the target bearing and return a partially turned heading.
    return None

if __name__ == "__main__":
    print(__doc__)
    print("Implement the function, then add your prediction and small checks.")
