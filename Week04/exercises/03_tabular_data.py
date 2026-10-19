"""03 — Tabular Data — Worked Exercise

1. Load data/beam_measurements.xlsx and inspect its columns and missing values.
2. On a copy, add difference_mm = b_mm - a_mm.
3. Find every position with the largest difference (there can be a tie).
4. Select a_mm and b_mm as a numerical array and report its shape.
5. Save the comparison under outputs/, leaving the supplied workbook unchanged.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

# Supplied file-location setup. Run this before the lesson sections.
from pathlib import Path

if "__file__" in globals():
    WEEK_DIR = Path(__file__).resolve().parents[1]
else:
    # For selected lines: start in the repository, week, or script folder.
    WEEK_DIR = Path.cwd()
    if WEEK_DIR.name in {"tutorial", "exercises", "optional"}:
        WEEK_DIR = WEEK_DIR.parent
    if WEEK_DIR.name != "Week04":
        WEEK_DIR = WEEK_DIR / "Week04"
DATA_DIR = WEEK_DIR / "data"
OUTPUT_DIR = WEEK_DIR / "outputs"

import pandas as pd
import numpy as np

measurements = pd.read_excel(DATA_DIR / "beam_measurements.xlsx")
print(measurements.columns.tolist(), measurements.isna().sum())
comparison = measurements.copy()
comparison["difference_mm"] = comparison["b_mm"] - comparison["a_mm"]
largest_mm = comparison["difference_mm"].max()
at_maximum = np.isclose(comparison["difference_mm"], largest_mm)
positions_m = comparison.loc[at_maximum, "x_m"].tolist()
values = comparison[["a_mm", "b_mm"]].to_numpy(dtype=float)
print("Largest difference and positions:", largest_mm, positions_m)
print("Array shape:", values.shape)
OUTPUT_DIR.mkdir(exist_ok=True)
comparison.to_excel(OUTPUT_DIR / "exercise_beam_comparison.xlsx", index=False)
