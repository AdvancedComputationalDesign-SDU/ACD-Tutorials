"""W07: Branching starter.

Run the working baseline first. Complete randomize_branch() and
attraction_heading(), then add them to tree().
Follow the week README for the steps and use 02b_branching_solution.py to check your work.
"""

# %% Setup and drawing
import math
import random
from pathlib import Path

import matplotlib.pyplot as plt
from shapely.affinity import rotate, translate
from shapely.geometry import LineString, Point

# Prepared setup: find the week folder and save figures in its outputs folder.
SCRIPT_DIR = Path(__file__).resolve().parent if '__file__' in globals() else Path.cwd()
if (SCRIPT_DIR / 'Week07').is_dir():
    SCRIPT_DIR = SCRIPT_DIR / 'Week07'
if SCRIPT_DIR.name in {
        'tutorial', 'references', 'exercises', 'solutions', 'optional'}:
    WEEK_DIR = SCRIPT_DIR.parent
else:
    WEEK_DIR = SCRIPT_DIR
OUTPUT_DIR = WEEK_DIR / 'outputs'
OUTPUT_DIR.mkdir(exist_ok=True)

START = (0.0, 0.0)
INITIAL_ANGLE = 90.0
INITIAL_LENGTH = 40.0
MAX_DEPTH = 5  # Try 0, 1 and 2 first. Depth 0 includes the root segment.


def endpoint(start, angle, length):
    """Take an XY start, angle in degrees and length; return an XY endpoint."""
    step = rotate(Point(length, 0), angle, origin=(0, 0))
    return translate(step, xoff=start[0], yoff=start[1]).coords[0]


def draw_tree(ax, lines, title):
    """Draw a list of Shapely lines on the supplied axes; return None."""
    for line in lines:
        x, y = line.xy
        ax.plot(x, y, color='#244b43', linewidth=1)
    ax.set(xlim=(-100, 100), ylim=(-5, 155), title=title)
    ax.set_aspect('equal')
    ax.axis('off')


# %% Working baseline
def tree(start, angle, length, depth, max_depth):
    """Return a flat list of Shapely LineStrings for this branch and its children.

    start is XY, angle is in degrees, and length is positive.
    depth starts at 0; max_depth is the last level to include.
    """
    if depth > max_depth or length < 0.5:
        return []

    tip = endpoint(start, angle, length)
    lines = [LineString([start, tip])]
    if depth == max_depth:
        return lines

    for turn in (28.0, -28.0):
        child_angle = angle + turn
        child_length = length * 0.72
        child_lines = tree(tip, child_angle, child_length, depth + 1, max_depth)
        lines.extend(child_lines)
    return lines


# %% Functions to complete
def randomize_branch(angle, length, angle_jitter, length_jitter):
    """Return a (varied_angle, varied_length) tuple.

    Inputs: angle in degrees, positive length, angle bound in degrees and
    fractional length bound (for example, 0.08 means up to 8% either way).
    Zero bounds should return the input angle and length unchanged.
    """
    # TODO: choose a bounded angle offset and length factor; return both values.
    return None


def attraction_heading(start, angle, target, strength):
    """Return an adjusted heading in degrees.

    Inputs: XY start, heading in degrees, target Point and strength in [0,1].
    Strength 0 keeps the heading; strength 1 faces the target.
    Keep the heading unchanged when the start equals the target.
    """
    # TODO: turn partway toward the target along the shorter angular direction.
    return None


# TODO: after completing the functions, extend tree() to use them.
# Randomize each child's angle/length; apply attraction before drawing a segment.
# Pass the new controls to the recursive child calls.


# %% Run the baseline
# Try MAX_DEPTH 0, 1 and 2: expect 1, 3 and 7 segments.
baseline = tree(START, INITIAL_ANGLE, INITIAL_LENGTH, 0, MAX_DEPTH)
print('Maximum depth:', MAX_DEPTH, 'Segment count:', len(baseline))

fig, ax = plt.subplots(figsize=(5, 5))
draw_tree(ax, baseline, 'Baseline branching')
fig.tight_layout()
fig.savefig(OUTPUT_DIR / '02_branching_starter_baseline.png', dpi=160)
plt.show()
plt.close(fig)
