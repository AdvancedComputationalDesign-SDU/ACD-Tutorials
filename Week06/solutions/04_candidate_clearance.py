"""Worked solution: A deliberate clearance policy

Write keep(candidate, obstacle, clearance=0), returning a Boolean.
Reject crossing and touching. Other candidates need a gap at least
clearance. Test a crossing, a boundary touch, distance 0.5 and 1.0
from box(-1,-1,1,1). Use clearance=0.5. Explain endpoint-test failure.

One possible solution. Discuss another valid policy or representation.
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
    if clearance < 0:
        raise ValueError("clearance must be nonnegative")
    return (not candidate.intersects(obstacle)
            and candidate.distance(obstacle) >= clearance)

if __name__ == "__main__":
    obstacle = box(-1, -1, 1, 1)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    x, y = obstacle.exterior.xy
    ax.fill(x, y, color="#dddddd")
    for height, expected in [(0, False), (1, False), (1.5, True), (2, True)]:
        line = LineString([(-2, height), (2, height)])
        actual = keep(line, obstacle, 0.5)
        assert actual == expected
        x, y = line.xy
        ax.plot(x, y, color="#256d82" if actual else "#b24c39",
                label=f"y={height}: {actual}")
    assert keep(LineString([(-2, 1), (2, 1)]), obstacle, 0) is False
    ax.set_aspect("equal")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "solution_04_candidate_clearance.png", dpi=160)
    print("Checks passed: 04_candidate_clearance")
    plt.show()
    plt.close(fig)
