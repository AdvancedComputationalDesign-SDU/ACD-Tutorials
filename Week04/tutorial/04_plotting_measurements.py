"""04 — Plotting Measurements

Use the measurement question to choose and label a plot, then verify it against the numbers.
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

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({"font.family": "IBM Plex Sans", "font.size": 12})

measurements = pd.read_excel(DATA_DIR / "beam_measurements.xlsx")
position_m = measurements["x_m"]
a_mm = measurements["a_mm"]
b_mm = measurements["b_mm"]

# --- 01: Two labeled measurement series ---
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(position_m, a_mm, "o-", label="Series A")
ax.plot(position_m, b_mm, "s--", label="Series B")
ax.set_xlabel("Position along beam (m)")
ax.set_ylabel("Deflection, positive downward (mm)")
ax.set_title("Illustrative beam measurements")
ax.legend()
ax.grid(alpha=0.25)
fig.tight_layout()
OUTPUT_DIR.mkdir(exist_ok=True)
fig.savefig(OUTPUT_DIR / "beam_measurements.png", dpi=160)
plt.show()  # Close the window to continue when running the whole file.
plt.close(fig)

# --- 02: Two questions, two views of the same data ---
difference_mm = b_mm - a_mm
fig, axes = plt.subplots(1, 2, figsize=(9, 3.8))
axes[0].plot(position_m, difference_mm, "o-")
axes[0].set(xlabel="Position (m)", ylabel="B − A (mm)", title="Difference by position")
axes[1].scatter(a_mm, b_mm)
axes[1].set(xlabel="A (mm)", ylabel="B (mm)", title="Paired deflections")
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "beam_comparisons.png", dpi=160)
plt.show()
plt.close(fig)
# Discuss: a scatter plot tests a relationship; it does not show spatial order.
