"""06 Compose a geometric study from a small imported function.

Change one parameter, predict the effect, then compare. This is a loop-driven
composition; recursive generation is next week's topic.
"""
from pathlib import Path
import sys
import math
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
from geometry_tools import make_motif
OUTPUT_DIR = WEEK_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def make_composition(turn_amplitude=45):
    """Return fresh geometry. Rows/columns locate each motif's local origin."""
    motifs = []
    for row in range(5):
        for column in range(8):
            angle = turn_amplitude * math.sin(column * math.pi / 4)
            motifs.append(make_motif(column * 1.5, row * 1.5, angle, size=0.9))
    return motifs


def draw_composition(ax, motifs):
    for motif in motifs:
        x, y = motif.exterior.xy
        ax.fill(x, y, facecolor="#256d82", edgecolor="white", linewidth=0.4)
    ax.set_aspect("equal")
    ax.set(xlim=(-1, 12), ylim=(-1, 8))
    ax.axis("off")


if __name__ == "__main__":
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for ax, amplitude in zip(axes, [0, 60]):
        motifs = make_composition(amplitude)
        assert len(motifs) == 40
        draw_composition(ax, motifs)
        ax.set_title(f"turn_amplitude = {amplitude}")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "06_composition.png", dpi=180)
    plt.show()
    plt.close(fig)

# Optional design study after the baseline run:
# 1. Change only the second amplitude (60), predict, then run again.
# 2. Or edit the local triangle in geometry_tools.make_motif; restart the
#    Python session so the updated module is imported, then rerun this file.
# 3. Keep placements/axes fixed and use a new output filename for your study.
# Explain the inputs and returned geometry of the function you changed.
