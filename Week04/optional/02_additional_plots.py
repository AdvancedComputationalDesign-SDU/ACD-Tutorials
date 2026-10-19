"""02 — Additional Plots — Optional
Run independently after the core topics; this is not another required exercise.
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
import seaborn as sns

measurements = pd.read_excel(DATA_DIR / "beam_measurements.xlsx")
# Keep the inherited stacked-bar example on additive harvest quantities.
# Adding two alternative beam deflections would not express a meaningful total.
years = [2010, 2011, 2012, 2013, 2014, 2015]
apples = np.array([0.895, 0.910, 0.919, 0.926, 0.929, 0.931])
oranges = np.array([0.962, 0.941, 0.930, 0.923, 0.918, 0.880])
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
axes[0].bar(years, apples, label="Apples")
axes[0].bar(years, oranges, bottom=apples, label="Oranges")
axes[0].set(xlabel="Year", ylabel="Harvest per shared area (t/ha)", title="Illustrative additive quantities")
axes[0].legend()
rng = np.random.default_rng(26)
samples = rng.normal(0, 1, 500)
axes[1].hist(samples, bins=20)
axes[1].set(xlabel="Sample value", ylabel="Count", title="Seeded distribution")
fig.tight_layout()
plt.show()
plt.close(fig)

long = measurements.melt(id_vars="x_m", value_vars=["a_mm", "b_mm"], var_name="series", value_name="deflection_mm")
print(long.groupby("series")["deflection_mm"].mean())
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
sns.barplot(data=long, x="series", y="deflection_mm", errorbar=None, ax=axes[0])
axes[0].set(xlabel="Series", ylabel="Mean deflection (mm)")
rolling = measurements["a_mm"].rolling(window=3, center=True).mean()
axes[1].plot(measurements["x_m"], measurements["a_mm"], "o-", label="Original")
axes[1].plot(measurements["x_m"], rolling, "s--", label="3-sample mean")
axes[1].set(xlabel="Position (m)", ylabel="Deflection (mm)")
axes[1].legend()
fig.tight_layout()
plt.show()
plt.close(fig)
print("Unfilled rolling endpoints:", rolling.tolist())
