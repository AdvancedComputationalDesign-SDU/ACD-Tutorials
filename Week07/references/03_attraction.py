"""Reference: extend the baseline with attraction toward a point.

Read attraction_heading() and generate_attracted_fractal() in recursive_tools.
The new line turns the current heading before creating the segment; children
inherit that adjusted heading. Compare with generate_fractal(): the stopping,
branching and length rules have not changed. No obstacle or second influence.
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


from shapely.geometry import Point
from recursive_tools import (attraction_heading, build_design, default_params,
                             draw_result, signature)


def main():
    target = Point(35, 100)
    params = default_params()  # Zero jitter keeps this comparison easy to read.
    baseline = build_design(params)
    fig, axes = plt.subplots(1, 3, figsize=(11, 4))
    for ax, strength in zip(axes, [0.0, 0.2, 0.4]):
        records = build_design(params, target, attraction_strength=strength)
        assert len(records) == len(baseline)
        if strength == 0:
            assert signature(records) == signature(baseline)
        else:
            assert signature(records) != signature(baseline)
        draw_result(ax, records, target)
        ax.set(xlim=(-100, 100), ylim=(-5, 155))
        ax.set_title("baseline" if strength == 0 else f"attraction {strength:.1f}")
    print("Heading 90°, target to the right, strength 0.5:",
          attraction_heading((0, 0), 90, Point(10, 0), 0.5))  # 45°
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "04_attraction.png", dpi=180)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
