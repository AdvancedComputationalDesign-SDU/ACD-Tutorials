"""A deliberate clearance policy

Write keep(candidate, obstacle, clearance=0), returning a Boolean.
Reject crossing and touching. Other candidates need a gap at least
clearance. Test a crossing, a boundary touch, distance 0.5 and 1.0
from box(-1,-1,1,1). Use clearance=0.5. Explain endpoint-test failure.

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

from shapely.geometry import LineString, box

def keep(candidate, obstacle, clearance=0):
    # TODO: query the whole candidate and return a Boolean.
    return None

if __name__ == "__main__":
    print(__doc__)
    print("Implement the function, then add your prediction and small checks.")
