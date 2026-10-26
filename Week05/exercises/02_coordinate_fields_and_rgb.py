"""02 — Coordinate Fields and RGB — Worked Exercise

1. On an 80-row, 120-column canvas, create coordinates spanning [-1, 1] on each axis.
2. Use a seed of 26 to choose one phase in [0, 2*pi), then create a vertical sine wave.
3. Keep the wave only where the distance from the origin is less than 0.65.
4. Form RGB channels from the masked wave, an X gradient, and one minus that gradient.
5. Display and save the pixels with the same origin; print shape, range, and seed.
6. Change the spatial rule to diagonal bands, not just a different colormap.

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
    if WEEK_DIR.name != "Week05":
        WEEK_DIR = WEEK_DIR / "Week05"
DATA_DIR = WEEK_DIR / "data"
OUTPUT_DIR = WEEK_DIR / "outputs"

import numpy as np
import matplotlib.pyplot as plt

height, width = 80, 120
X, Y = np.meshgrid(np.linspace(-1, 1, width), np.linspace(-1, 1, height))
seed = 26
rng = np.random.default_rng(seed)
phase = rng.uniform(0, 2 * np.pi)
wave = 0.5 + 0.5 * np.sin(4 * np.pi * X + phase)
distance = np.sqrt(X**2 + Y**2)
mask = distance < 0.65
masked = np.where(mask, wave, 0.0)
gradient = (X + 1) / 2
rgb = np.stack([masked, gradient, 1 - gradient], axis=-1)
diagonal = 0.5 + 0.5 * np.sin(4 * np.pi * (X + Y) + phase)
variant = np.stack([np.where(mask, diagonal, 0.0), gradient, 1 - gradient], axis=-1)
print("Shape, range, seed:", rgb.shape, rgb.min(), rgb.max(), seed)
OUTPUT_DIR.mkdir(exist_ok=True)
plt.imsave(OUTPUT_DIR / "exercise_rgb_field.png", rgb, origin="lower")
fig, axes = plt.subplots(1, 2, figsize=(8, 3))
axes[0].imshow(rgb, origin="lower")
axes[1].imshow(variant, origin="lower")
for ax in axes:
    ax.axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)
