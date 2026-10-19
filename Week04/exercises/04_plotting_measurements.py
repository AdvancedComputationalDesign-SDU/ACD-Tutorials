"""04 — Plotting Measurements — Worked Exercise

1. Plot b_mm - a_mm against x_m with labels and units; save the figure.
2. Identify all positions with the largest difference and verify them numerically.
3. Ask an additional question: is B proportional to A at the sampled positions?
4. Make a scatter plot and compare B/A only where A is nonzero. Explain the endpoints.
   The resulting relationship describes this illustrative dataset, not every beam.

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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({"font.family": "IBM Plex Sans", "font.size": 12})

measurements = pd.read_excel(DATA_DIR / "beam_measurements.xlsx")
difference_mm = measurements["b_mm"] - measurements["a_mm"]
maximum_mm = difference_mm.max()
positions_m = measurements.loc[np.isclose(difference_mm, maximum_mm), "x_m"].tolist()
nonzero = measurements["a_mm"] != 0
ratios = measurements.loc[nonzero, "b_mm"] / measurements.loc[nonzero, "a_mm"]
print("Largest difference:", maximum_mm, "at", positions_m)
print("Ratios where A is nonzero:", ratios.tolist())
fig, axes = plt.subplots(1, 2, figsize=(9, 3.8))
axes[0].plot(measurements["x_m"], difference_mm, "o-")
axes[0].set(xlabel="Position (m)", ylabel="B − A (mm)", title="Difference")
axes[1].scatter(measurements["a_mm"], measurements["b_mm"])
axes[1].set(xlabel="A (mm)", ylabel="B (mm)", title="Paired measurements")
fig.tight_layout()
OUTPUT_DIR.mkdir(exist_ok=True)
fig.savefig(OUTPUT_DIR / "exercise_measurement_plots.png", dpi=160)
plt.show()
plt.close(fig)
# B/A is 1.5 for nonzero A. Both endpoints are zero, so their ratios are undefined.
