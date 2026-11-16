"""Reference: record an experiment and compare geometry with fixed axes.

Compare the branching baseline with attraction only. Keep the target, seed,
branching and length settings fixed. Use the saved images and settings to
explain the added capability.
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


import json
from shapely.geometry import Point
from recursive_tools import build_design, default_params, draw_result, signature


def run_study():
    target = Point(35, 100)
    params = default_params()
    all_records = []
    metadata = []
    fig, axes = plt.subplots(1, 2, figsize=(8, 4.4))
    for ax, (label, strength) in zip(axes, [("baseline", 0.0), ("attraction", 0.3)]):
        records = build_design(params, target, attraction_strength=strength)
        all_records.append(records)
        metadata.append({"case": label, "parameters": params.copy(),
                         "target_wkt": target.wkt,
                         "attraction_strength": strength,
                         "segment_count": len(records),
                         "total_length": sum(r["geometry"].length for r in records)})
        draw_result(ax, records, target)
        ax.set(xlim=(-100, 100), ylim=(-5, 155))
        ax.set_title(label)
    assert signature(all_records[0]) != signature(all_records[1])
    # Same count/total length can conceal a different spatial arrangement.
    print([(m["segment_count"], round(m["total_length"], 3)) for m in metadata])
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "05_comparison.png", dpi=180)
    (OUTPUT_DIR / "05_comparison.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    plt.show()
    plt.close(fig)
    return metadata


if __name__ == "__main__":
    run_study()
