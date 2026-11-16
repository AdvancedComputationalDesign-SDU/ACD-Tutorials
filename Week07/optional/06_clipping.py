"""Optional: clipping may return several pieces, or nothing.

Adapted from the historical Shapely demo's set operations and clipping topic.
Inspect the type before reading coordinates. This example handles line parts.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from shapely.geometry import LineString, box

if "__file__" in globals():
    WEEK_DIR = Path(__file__).resolve().parents[1]
else:
    WEEK_DIR = Path.cwd()
    if WEEK_DIR.name in {"tutorial", "references", "exercises", "solutions", "optional"}:
        WEEK_DIR = WEEK_DIR.parent
    if (WEEK_DIR / "Week07" / "tutorial").is_dir():
        WEEK_DIR = WEEK_DIR / "Week07"
OUTPUT_DIR = WEEK_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def line_parts(geometry):
    if geometry.is_empty:
        return []
    if geometry.geom_type == "LineString":
        return [geometry]
    if hasattr(geometry, "geoms"):
        parts = []
        for child in geometry.geoms:
            parts.extend(line_parts(child))
        return parts
    return []  # Point contacts do not provide drawable line segments here.


if __name__ == "__main__":
    obstacle = box(-1, -1, 1, 1)
    crossing = LineString([(-3, 0), (3, 0)])
    result = crossing.difference(obstacle)
    print("Result type:", result.geom_type)  # MultiLineString
    assert len(line_parts(result)) == 2
    assert line_parts(crossing.intersection(box(5, 5, 6, 6))) == []
    fig, ax = plt.subplots(figsize=(6, 3))
    x, y = obstacle.exterior.xy
    ax.fill(x, y, color="#dddddd")
    for line in line_parts(result):
        x, y = line.xy
        ax.plot(x, y, linewidth=3, color="#256d82")
    ax.set_aspect("equal")
    ax.set(xlim=(-3.5, 3.5), ylim=(-1.5, 1.5))
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "optional_clipping.png", dpi=160)
    plt.show()
    plt.close(fig)
