"""03 Geometry values: construct, query, and draw simple planar objects."""
from pathlib import Path
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon, box

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

# %% 1. Coordinates have no automatic physical unit. Here one unit is one unit.
point = Point(1, 1)
route = LineString([(0, 0), (3, 0), (3, 4)])
triangle = Polygon([(0, 0), (3, 0), (0, 2)])
region = box(0, 0, 3, 2)  # min x, min y, max x, max y
print("Point:", point.x, point.y)
print("Route length:", route.length)  # 7, not 5
print("Triangle area:", triangle.area)  # 3
print("Box bounds:", region.bounds)  # (0, 0, 3, 2)
print("Box perimeter:", region.length)  # 10
print("Point bounds:", Point(0, 0).bounds)  # (0, 0, 0, 0), not empty.
# The original lecture's valid/invalid polygon diagram illustrates this check.
bow_tie = Polygon([(0, 0), (2, 2), (0, 2), (2, 0)])
print("Triangle valid, bow tie valid:", triangle.is_valid, bow_tie.is_valid)
assert triangle.is_valid and not bow_tie.is_valid

# %% 2. Geometry stores data. Matplotlib displays the data.
fig, ax = plt.subplots(figsize=(6, 4))
x, y = region.exterior.xy
ax.fill(x, y, facecolor="#eeeeee", edgecolor="#555555", label="box")
x, y = triangle.exterior.xy
ax.fill(x, y, alpha=0.35, color="#d08d44", label="triangle")
x, y = route.xy
ax.plot(x, y, color="#256d82", linewidth=2, label="route")
ax.scatter([point.x], [point.y], color="#b24c39", label="point")
ax.set_aspect("equal")
ax.set_xlim(-0.5, 4)
ax.set_ylim(-0.5, 4.5)
ax.legend(loc="upper right")
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "03_geometry.png", dpi=160)
plt.show()
plt.close(fig)
