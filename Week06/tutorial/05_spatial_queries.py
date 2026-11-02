"""05 Predict a query before deciding how a design should respond to it."""
from pathlib import Path
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, box

if "__file__" in globals():
    WEEK_DIR = Path(__file__).resolve().parents[1]
else:
    WEEK_DIR = Path.cwd()
    if WEEK_DIR.name in {"tutorial", "exercises", "solutions", "optional"}:
        WEEK_DIR = WEEK_DIR.parent
    if WEEK_DIR.name != "Week06":
        WEEK_DIR = WEEK_DIR / "Week06"
OUTPUT_DIR = WEEK_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# %% 1. Endpoints outside do not imply the segment stays outside.
obstacle = box(-1, -1, 1, 1)
crossing = LineString([(-2, 0), (2, 0)])
touching = LineString([(-2, 1), (2, 1)])
clear = LineString([(-2, 2), (2, 2)])
for name, candidate in [("crossing", crossing), ("touching", touching),
                        ("clear", clear)]:
    print(name, "intersects:", candidate.intersects(obstacle),
          "distance:", candidate.distance(obstacle))
# Expected: (True, 0), (True, 0), (False, 1).
print("Endpoint covered:", obstacle.covers(Point(-2, 0)))  # False

# %% 2. A boundary policy is a design choice informed by precise predicates.
boundary_point = Point(1, 0)
print("Contains boundary:", obstacle.contains(boundary_point))  # False
print("Covers boundary:", obstacle.covers(boundary_point))  # True
print("Distance to boundary point:", obstacle.distance(boundary_point))  # 0
# Distance is an unsigned scalar. Zero can mean overlap, contact, or inside.

# %% 3. Buffer creates a region for a neighborhood/proximity question.
neighborhood = obstacle.buffer(0.5)
print("Nearby clear segment:", clear.distance(obstacle) < 0.5)  # False
fig, ax = plt.subplots(figsize=(6, 4))
for shape, color in [(neighborhood, "#eeeeee"), (obstacle, "#bbbbbb")]:
    x, y = shape.exterior.xy
    ax.fill(x, y, color=color)
for line, color, label in [(crossing, "#b24c39", "crossing: True"),
                            (touching, "#d08d44", "touching: True"),
                            (clear, "#256d82", "clear: False, distance 1")]:
    x, y = line.xy
    ax.plot(x, y, color=color, linewidth=2, label=label)
ax.scatter([boundary_point.x], [boundary_point.y], color="black", zorder=5)
ax.set_aspect("equal")
ax.set(xlim=(-2.5, 3), ylim=(-2, 3))
ax.legend(loc="lower right", fontsize=8)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "05_queries.png", dpi=160)
plt.show()
plt.close(fig)
