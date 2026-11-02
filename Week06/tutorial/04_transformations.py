"""04 Store transformed geometry and choose its rotation/scaling origin."""
from pathlib import Path
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.affinity import rotate, scale, translate

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

# %% 1. A new result leaves the original geometry available.
motif = Polygon([(1, 0), (3, 0), (1, 1)])
about_tip = rotate(motif, 90, origin=(1, 0))  # Degrees by default.
about_center = rotate(motif, 90, origin="center")  # Bounds center.
smaller = scale(motif, xfact=0.5, yfact=0.5, origin=(1, 0))
placed = translate(smaller, xoff=0, yoff=2)
assert motif.area == 1.0 and smaller.area == 0.25
print("Original area, scaled area:", motif.area, smaller.area)

# %% 2. Compare the SAME input and the effect of the stated origin.
fig, axes = plt.subplots(1, 3, figsize=(10, 3.4))
for ax, result, title in zip(axes, [about_tip, about_center, placed],
                           ["Rotate about (1, 0)", "Rotate about bounds center",
                            "Scale, then translate"]):
    for geometry, color, label in [(motif, "#bbbbbb", "input"),
                                   (result, "#256d82", "result")]:
        x, y = geometry.exterior.xy
        ax.fill(x, y, color=color, alpha=0.5, label=label)
    ax.set(xlim=(-0.5, 4), ylim=(-1, 3.5), title=title)
    ax.set_aspect("equal")
axes[0].legend()
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "04_transformations.png", dpi=160)
plt.show()
plt.close(fig)
