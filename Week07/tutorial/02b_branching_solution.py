"""W07: Solved recursive branching, controlled variation and attraction.

Run the cells in order, or run the whole file and close each plot to continue.
Use 02a_branching_starter.py for your own implementation and
the week README for the steps to build it up.
The comments explain what to predict and inspect at each stage.
"""

# %% 00 Imports, starting values and drawing
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

SEED = 42
ANGLE_JITTER = 5.0    # Random angle offset between -5 and +5 degrees.
LENGTH_JITTER = 0.08  # Random length factor between 0.92 and 1.08.


# %% 01 Functions used by the tree
def randomize_branch(angle, length, angle_jitter, length_jitter):
    """Return a (varied_angle, varied_length) tuple.

    angle and angle_jitter are degrees; length_jitter is a fraction.
    Zero bounds return the input angle and length unchanged.
    """
    angle_offset = random.uniform(-angle_jitter, angle_jitter)
    length_factor = random.uniform(1 - length_jitter, 1 + length_jitter)
    return angle + angle_offset, length * length_factor


def attraction_heading(start, angle, target, strength):
    """Return a heading turned toward a target Point.

    start is an XY tuple; angle is in degrees.
    Use strength 0 for no turn, 0.5 for half the turn, or 1 to face the target.
    """
    dx = target.x - start[0]
    dy = target.y - start[1]
    if dx == 0 and dy == 0:
        return angle  # At the target, keep the existing heading.

    bearing = math.degrees(math.atan2(dy, dx))
    # Keep the turn between -180 and 180 degrees, so it follows the shorter way.
    turn = (bearing - angle + 180) % 360 - 180
    return angle + strength * turn


def tree(start, angle, length, depth, max_depth,
         angle_jitter=0.0, length_jitter=0.0, target=None, strength=0.0):
    """Return a flat list of Shapely LineStrings for this branch and its children.

    start is XY, angle is in degrees, and length is positive.
    depth starts at 0; max_depth is the last level to include.
    Zero jitter and no target give the baseline.
    """
    # Stop before drawing if this branch is too deep or too short.
    if depth > max_depth or length < 0.5:
        return []

    if target is not None:
        angle = attraction_heading(start, angle, target, strength)

    tip = endpoint(start, angle, length)
    lines = [LineString([start, tip])]
    if depth == max_depth:
        return lines  # Include this segment, but do not add more children.

    for turn in (28.0, -28.0):
        child_angle = angle + turn
        child_length = length * 0.72

        # Replace the two child values with the function's returned values.
        child_angle, child_length = randomize_branch(
            child_angle, child_length, angle_jitter, length_jitter)

        # Each child starts at the parent's tip and receives the same controls.
        child_lines = tree(tip, child_angle, child_length, depth + 1, max_depth,
                           angle_jitter=angle_jitter, length_jitter=length_jitter,
                           target=target, strength=strength)
        lines.extend(child_lines)  # Add the returned child lines to this list.
    return lines


# %% 02 Baseline: one segment, then two children at each new level
# With these starting values, depths 0, 1 and 2 should give 1, 3 and 7 segments.
for maximum in (0, 1, 2):
    small = tree(START, INITIAL_ANGLE, INITIAL_LENGTH, 0, maximum)
    print('Maximum depth:', maximum, 'Segment count:', len(small))

baseline = tree(START, INITIAL_ANGLE, INITIAL_LENGTH, 0, MAX_DEPTH)
fig, ax = plt.subplots(figsize=(5, 5))
draw_tree(ax, baseline, '1. Baseline branching')
fig.tight_layout()
fig.savefig(OUTPUT_DIR / '02_branching_baseline.png', dpi=160)
plt.show()
plt.close(fig)


# %% 03 Controlled variation: change angle first, then length
# A seed repeats the same random choices. Reset it BEFORE each starting call,
# so the comparisons share a sequence. Do not reset it inside the recursion.
random.seed(SEED)
angle_only = tree(START, INITIAL_ANGLE, INITIAL_LENGTH, 0, MAX_DEPTH,
                  angle_jitter=ANGLE_JITTER)

random.seed(SEED)
varied = tree(START, INITIAL_ANGLE, INITIAL_LENGTH, 0, MAX_DEPTH,
              angle_jitter=ANGLE_JITTER, length_jitter=LENGTH_JITTER)

# Keep the largest possible child shorter than its parent.
# Here the largest length factor is 0.72 * 1.08 = 0.7776.
fig, axes = plt.subplots(1, 3, figsize=(12, 5))
draw_tree(axes[0], baseline, 'Baseline: no variation')
draw_tree(axes[1], angle_only, 'Angle variation only')
draw_tree(axes[2], varied, 'Angle and length variation')
fig.tight_layout()
fig.savefig(OUTPUT_DIR / '02_branching_variation.png', dpi=160)
plt.show()
plt.close(fig)


# %% 04 Attraction: keep the random choices and add one spatial influence
# Check the turn on its own: halfway from heading 90 toward the right is 45.
heading = attraction_heading((0, 0), 90, Point(10, 0), 0.5)
print('Attraction check — expect 45 degrees:', heading)

target = Point(35, 100)
strength = 0.3  # Use a value between 0 and 1.

random.seed(SEED)  # Repeat the angle/length choices used for the varied tree.
attracted = tree(START, INITIAL_ANGLE, INITIAL_LENGTH, 0, MAX_DEPTH,
                 angle_jitter=ANGLE_JITTER, length_jitter=LENGTH_JITTER,
                 target=target, strength=strength)

fig, axes = plt.subplots(1, 2, figsize=(8, 5))
draw_tree(axes[0], varied, 'Same varied tree: no attraction')
draw_tree(axes[1], attracted, f'Add attraction: strength {strength}')
for ax in axes:
    ax.scatter([target.x], [target.y], marker='+', color='#b24c39', s=70)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / '02_branching_attraction.png', dpi=160)
plt.show()
plt.close(fig)
