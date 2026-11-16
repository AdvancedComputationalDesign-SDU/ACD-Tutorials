"""A recursive alternative with one influence

Write cells(region,target,remaining). Return [region] when remaining
is zero OR the region does not cover target. Otherwise split the
longest side in half, recurse on each half and join the returned lists.
Use box(0,0,8,5), target Point(1,1), remaining=3. Predict four leaves.
Check leaf area sum=40 and union equals the input. Move the target
onto a split boundary and explain how covers changes which cells divide.

Attempt this before opening 03_adaptive_subdivision_solution.py.
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
    # TODO: base case, split, return recursive results.
    return None

if __name__ == "__main__":
    print(__doc__)
    print("Implement the function, then add your prediction and small checks.")
