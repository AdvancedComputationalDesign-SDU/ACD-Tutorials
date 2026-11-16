"""Optional Sierpinski triangle: a different recursive representation.

Adapted from ACD-Tutorials dev_oz:week07/serpinski.py. Explicit leaf counts and
area checks make the geometrical consequence of replacement visible.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from shapely.affinity import rotate
from shapely.geometry import LineString, Point, Polygon

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


def sierpinski_triangle(remaining, points):
    if remaining == 0:
        return [Polygon(points)]
    a, b, c = points
    ab = LineString([a, b]).interpolate(0.5, normalized=True).coords[0]
    bc = LineString([b, c]).interpolate(0.5, normalized=True).coords[0]
    ca = LineString([c, a]).interpolate(0.5, normalized=True).coords[0]
    return (sierpinski_triangle(remaining - 1, [a, ab, ca])
            + sierpinski_triangle(remaining - 1, [ab, b, bc])
            + sierpinski_triangle(remaining - 1, [ca, bc, c]))


if __name__ == "__main__":
    apex = rotate(Point(10, 0), 60, origin=(0, 0))
    points = [(0, 0), apex.coords[0], (10, 0)]
    initial_area = Polygon(points).area
    fig, axes = plt.subplots(1, 3, figsize=(9, 3.4))
    for ax, depth in zip(axes, [0, 1, 3]):
        triangles = sierpinski_triangle(depth, points)
        assert len(triangles) == 3**depth
        expected_area = initial_area * (0.75**depth)
        assert abs(sum(t.area for t in triangles) - expected_area) < 1e-9
        for triangle in triangles:
            x, y = triangle.exterior.xy
            ax.fill(x, y, color="#256d82")
        ax.set_aspect("equal")
        ax.set_title(f"order {depth}: {len(triangles)} leaves")
        ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "optional_sierpinski.png", dpi=160)
    plt.show()
    plt.close(fig)
