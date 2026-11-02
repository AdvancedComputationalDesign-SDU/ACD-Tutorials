"""Returns and scope

Write shifted_wave(x, phase=0) returning 0.5 + 0.5*sin(x + phase).
Predict x=0, phase=0 and x=0, phase=pi/2. Check that calling the
function does not overwrite a caller variable named phase. Plot one
comparison with phase 0 and pi/2 using the same x coordinates.

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

import numpy as np

def shifted_wave(x, phase=0):
    # TODO: return the calculated value.
    return None

if __name__ == "__main__":
    print(__doc__)
    print("Implement the function, then add your prediction and small checks.")
