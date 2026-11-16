"""Optional Koch curve: recursive segment replacement.

Adapted from ACD-Tutorials dev_oz:week07/koch.py. The historical replacement
rule is retained; Shapely interpolation and rotation construct its points.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from shapely.affinity import rotate
from shapely.geometry import LineString

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


def divide_segment(p1, p2, remaining):
    if remaining == 0:
        return [p1, p2]
    segment = LineString([p1, p2])
    first = segment.interpolate(1 / 3, normalized=True)
    second = segment.interpolate(2 / 3, normalized=True)
    peak = rotate(second, 60, origin=first)
    a, b, c = first.coords[0], second.coords[0], peak.coords[0]
    return (divide_segment(p1, a, remaining - 1)[:-1]
            + divide_segment(a, c, remaining - 1)[:-1]
            + divide_segment(c, b, remaining - 1)[:-1]
            + divide_segment(b, p2, remaining - 1))


if __name__ == "__main__":
    fig, axes = plt.subplots(1, 3, figsize=(10, 3))
    for ax, depth in zip(axes, [0, 1, 3]):
        line = LineString(divide_segment((0, 0), (9, 0), depth))
        assert len(line.coords) - 1 == 4**depth
        x, y = line.xy
        ax.plot(x, y, color="#256d82")
        ax.set_aspect("equal")
        ax.set(xlim=(-0.5, 9.5), ylim=(-0.5, 3.5), title=f"order {depth}")
        ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "optional_koch.png", dpi=160)
    plt.show()
    plt.close(fig)
