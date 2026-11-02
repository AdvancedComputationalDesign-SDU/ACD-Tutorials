"""02 Scope, returned copies, and importing a local module.

The supplied path setup supports complete files and selected sections from
the repository, week, or topic folder. Keep geometry_tools.py with this week.
"""
from pathlib import Path
import sys

if "__file__" in globals():
    WEEK_DIR = Path(__file__).resolve().parents[1]
else:
    WEEK_DIR = Path.cwd()
    if WEEK_DIR.name in {"tutorial", "exercises", "solutions", "optional"}:
        WEEK_DIR = WEEK_DIR.parent
    if WEEK_DIR.name != "Week06":
        WEEK_DIR = WEEK_DIR / "Week06"
sys.path.insert(0, str(WEEK_DIR / "tutorial"))
from geometry_tools import endpoint, make_motif
import geometry_tools
import math

# %% Existing lecture examples: composition and a returned section property.
x = 2
composed = math.exp(math.log(x + 1))
print("Composed expression:", composed)  # Approximately 3.
moment_of_inertia = geometry_tools.compute_inertia(0.3, 0.6)
print("Returned section property:", moment_of_inertia)  # 0.0054 m**4.
# inertia is local inside compute_inertia. The returned value is available here.
# print(inertia)  # Would raise NameError; no such name is defined in this file.

# %% 1. A parameter is local to the function call.
angle = 90


def turn_heading(angle, turn=20):
    angle = angle + turn
    return angle


new_angle = turn_heading(angle)
print("Caller, return:", angle, new_angle)  # 90, 110

# %% 2. Changing a list through a parameter changes that same list.
# This warm-up assumes at least two items. Try the supplied four-item case.
def chop(items):
    del items[0]
    del items[-1]


def middle(items):
    return items[1:-1]  # A new shallow list for these scalar coordinates.


points = [0, 1, 2, 3]
inside = middle(points)
print("Original and copy:", points, inside)  # [0,1,2,3], [1,2]
chop(points)
print("After mutation:", points)  # [1,2]

# %% 3. Compose small calculations imported from another file.
tip = endpoint((0, 0), angle=90, length=2)
motif = make_motif(*tip, angle=30, size=0.5)
print("Tip:", tip)
print("Motif area:", round(motif.area, 3))  # 0.075
assert abs(tip[0]) < 1e-12 and abs(tip[1] - 2) < 1e-12
# Importing geometry_tools created definitions, not a design or a plot.
