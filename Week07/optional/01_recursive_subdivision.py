"""Optional representation: recursively split the longest side.

Compare cell counts, areas and partition boundaries as the depth changes.
"""
from pathlib import Path
import sys
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


from shapely.geometry import box


def subdivide(region, remaining, min_area=0.5):
    if remaining == 0 or region.area <= min_area:
        return [region]
    xmin, ymin, xmax, ymax = region.bounds
    if xmax - xmin >= ymax - ymin:
        middle = region.centroid.x
        first = box(xmin, ymin, middle, ymax)
        second = box(middle, ymin, xmax, ymax)
    else:
        middle = region.centroid.y
        first = box(xmin, ymin, xmax, middle)
        second = box(xmin, middle, xmax, ymax)
    return (subdivide(first, remaining - 1, min_area)
            + subdivide(second, remaining - 1, min_area))


if __name__ == "__main__":
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.6))
    for ax, depth in zip(axes, [1, 3, 5]):
        cells = subdivide(box(0, 0, 8, 5), depth)
        assert abs(sum(cell.area for cell in cells) - 40) < 1e-9
        print("Remaining, leaf cells:", depth, len(cells))
        for i, cell in enumerate(cells):
            x, y = cell.exterior.xy
            ax.fill(x, y, color=plt.cm.viridis(i / max(1, len(cells) - 1)),
                    edgecolor="white", linewidth=0.8)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(f"remaining = {depth}")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "06_subdivision.png", dpi=180)
    plt.show()
    plt.close(fig)
