"""A shrinking recursive chain

Write lengths(length, remaining). Return [] if remaining==0 or
length<0.5. Otherwise return the current length followed by a call
with length*0.5 and remaining-1. Predict lengths(4,5). Draw the
returned sequence as connected horizontal segments. Explain both stops.

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

def lengths(length, remaining):
    # TODO: base case, current value, smaller call.
    return None

if __name__ == "__main__":
    print(__doc__)
    print("Implement the function, then add your prediction and small checks.")
