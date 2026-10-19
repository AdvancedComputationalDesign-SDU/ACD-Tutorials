"""03 — Tabular Data

Load a labeled measurement table, inspect it, and derive a comparison without overwriting the source.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
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

import numpy as np
import pandas as pd

# --- 01: Named columns carry meaning and units ---
measurements = pd.read_excel(DATA_DIR / "beam_measurements.xlsx")
print(measurements)
print(measurements.dtypes)
print("Missing values:", measurements.isna().sum())
# These are illustrative deflections, positive downward, not a calibrated model.

# --- 02: Select and calculate deliberately ---
comparison = measurements.copy()
comparison["difference_mm"] = comparison["b_mm"] - comparison["a_mm"]
middle = comparison.loc[comparison["x_m"].between(1, 4), ["x_m", "difference_mm"]]
print(middle)
values = comparison[["a_mm", "b_mm"]].to_numpy(dtype=float)
print("Values and shape:", values, values.shape)
print("All finite:", np.isfinite(values).all())

# --- 03: Inspect a deliberately altered copy ---
messy = measurements.copy()
messy["a_mm"] = messy["a_mm"].astype(object)
messy.loc[1, "a_mm"] = "missing"
messy.loc[2, "b_mm"] = np.nan
for column in ["x_m", "a_mm", "b_mm"]:
    messy[column] = pd.to_numeric(messy[column], errors="coerce")
invalid = messy[["x_m", "a_mm", "b_mm"]].isna().any(axis=1)
print("Rows needing attention:", messy.loc[invalid])
clean = messy.loc[~invalid].copy()
print("Rows retained:", len(clean))
# Dropping missing rows is a choice, not a universal cleaning rule.
# Filling with zero would invent a deflection measurement.

# --- 04: Export a derived table separately ---
OUTPUT_DIR.mkdir(exist_ok=True)
comparison.to_excel(OUTPUT_DIR / "beam_comparison.xlsx", index=False)
print("Saved:", OUTPUT_DIR / "beam_comparison.xlsx")
