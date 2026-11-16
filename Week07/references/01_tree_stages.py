"""Reference: root, children and descendants with inclusive maximum depth.

Read endpoint() and the baseline generate_fractal() in recursive_tools.py.
Implement the tree exercise before reading its solution. Use the debugger
on the depth=1 case before increasing the depth. No spatial influence yet.
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


from recursive_tools import build_design, default_params, draw_result


def main():
    fig, axes = plt.subplots(1, 4, figsize=(12, 3.6))
    for ax, depth in zip(axes, range(4)):
        params = default_params()
        params["max_depth"] = depth
        records = build_design(params)
        expected = 2 ** (depth + 1) - 1
        assert len(records) == expected
        print("max_depth, segments:", depth, len(records))
        draw_result(ax, records)
        ax.set(xlim=(-80, 80), ylim=(-5, 145))
        ax.set_title(f"depth {depth}: {len(records)} segments")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "02_tree_stages.png", dpi=180)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
