"""Worked solution: attraction changes direction, not length

turn_toward takes an XY tuple, a heading in degrees, a Shapely Point and
strength in [0, 1]. It returns a heading partway toward the target. Call it
before creating the current segment, then pass the adjusted heading to
children. The baseline branching and length rules stay unchanged.

One possible solution. Discuss another valid policy or representation.
"""
from pathlib import Path
import sys
import math
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
from recursive_tools import endpoint

def turn_toward(start, angle, target, strength):
    if not math.isfinite(strength) or not 0 <= strength <= 1:
        raise ValueError("strength must be between 0 and 1")
    dx, dy = target.x - start[0], target.y - start[1]
    if dx == 0 and dy == 0:
        return angle
    bearing = math.degrees(math.atan2(dy, dx))
    turn = (bearing - angle + 180) % 360 - 180
    return angle + strength * turn

if __name__ == "__main__":
    target = Point(10, 0)
    strengths = [0, 0.25, 0.5, 1]
    headings = [turn_toward((0, 0), 90, target, s) for s in strengths]
    assert headings == [90, 67.5, 45, 0]
    assert turn_toward((0, 0), 90, Point(0, 0), 1) == 90
    fig, ax = plt.subplots(figsize=(6, 3.5))
    for strength, heading in zip(strengths, headings):
        end = endpoint((0, 0), heading, 4)
        ax.plot([0, end[0]], [0, end[1]], label=f"strength {strength}")
    ax.scatter([target.x], [target.y], marker="+", color="#b24c39")
    ax.set(xlabel="X", ylabel="Y", title="One attraction response")
    ax.set_aspect("equal")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "solution_03_attraction.png", dpi=160)
    print("Checks passed: attraction headings")
    plt.show()
    plt.close(fig)
