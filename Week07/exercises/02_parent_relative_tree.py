"""Branches relative to their parent

Write tree(start, angle, length, depth, max_depth). Return a fresh
list of Shapely lines. Include the current segment if depth<=max_depth.
Each tip gets children at angle+30 and angle-30, length*0.7.
Predict counts 1,3,7 and check each child starts at its parent tip.

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

from shapely.geometry import LineString
from recursive_tools import endpoint

def tree(start, angle, length, depth, max_depth):
    # TODO: return a fresh list. Keep depth inclusive.
    return None

if __name__ == "__main__":
    print(__doc__)
    print("Implement the function, then add your prediction and small checks.")
