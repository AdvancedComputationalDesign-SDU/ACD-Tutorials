"""Reference: bounded variation, changing one control at a time.

Each build_design call creates its own random.Random(seed). The generator
shares it across descendants instead of reseeding every recursive call.
This is still the branching baseline: no target or spatial response yet.
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


from recursive_tools import build_design, default_params, draw_result, signature


def main():
    settings = [(0, 0.0), (5, 0.0), (5, 0.08)]
    fig, axes = plt.subplots(1, 3, figsize=(11, 4))
    for ax, (angle_jitter, length_jitter) in zip(axes, settings):
        params = default_params()
        params.update(angle_jitter=angle_jitter, length_jitter=length_jitter)
        records = build_design(params)
        repeat = build_design(params)
        assert signature(records) == signature(repeat)
        draw_result(ax, records)
        ax.set(xlim=(-100, 100), ylim=(-5, 155))
        ax.set_title(f"angle +/-{angle_jitter}°, length +/-{length_jitter:.0%}")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "03_seeded_tree.png", dpi=180)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
