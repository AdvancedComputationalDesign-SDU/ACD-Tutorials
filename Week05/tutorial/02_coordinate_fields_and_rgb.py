"""02 — Coordinate Fields and RGB

Separate spatial coordinates, scalar values, selection masks, and color channels.
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
    if WEEK_DIR.name != "Week05":
        WEEK_DIR = WEEK_DIR / "Week05"
DATA_DIR = WEEK_DIR / "data"
OUTPUT_DIR = WEEK_DIR / "outputs"

import numpy as np
import matplotlib.pyplot as plt

# --- 01: A rectangular grid exposes accidental axis swaps ---
height, width = 80, 120
x_coords = np.linspace(-1, 1, width)
y_coords = np.linspace(-1, 1, height)
X, Y = np.meshgrid(x_coords, y_coords)
print("Coordinate shapes:", X.shape, Y.shape)
rows, columns = np.mgrid[0:height, 0:width]
print(np.allclose(X, columns / (width - 1) * 2 - 1))

# --- 02: Different fields use the same coordinate arrays ---
gradient = (X + 1) / 2
wave = 0.5 + 0.5 * np.sin(4 * np.pi * X)
distance = np.sqrt(X**2 + Y**2)
ring = (distance > 0.3) & (distance < 0.7)
masked = np.where(ring, wave, 0.0)
print("Mask and selected values:", ring.shape, wave[ring].shape)

# --- 03: One scalar per channel per pixel ---
rgb = np.stack([gradient, masked, 1 - gradient], axis=-1)
print("RGB:", rgb.shape, rgb.min(), rgb.max())
fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for ax, image in zip(axes, [wave, masked, rgb]):
    ax.imshow(image, cmap="gray", vmin=0, vmax=1, origin="lower")
    ax.axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)
# Here each coordinate axis spans [-1, 1]; square display pixels make a
# coordinate-space circle appear stretched on this rectangular canvas.

# --- 04: Seeded random parameters and independent pixel noise ---
seed = 26
rng = np.random.default_rng(seed)
phase = rng.uniform(0, 2 * np.pi)
varied_wave = 0.5 + 0.5 * np.sin(4 * np.pi * X + phase)
noise = rng.random(wave.shape)
noisy_wave = 0.8 * varied_wave + 0.2 * noise
print("Seed and phase:", seed, phase)
fig, axes = plt.subplots(1, 2, figsize=(7, 3))
for ax, image in zip(axes, [varied_wave, noisy_wave]):
    ax.imshow(image, cmap="magma", vmin=0, vmax=1, origin="lower")
    ax.axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)
# A random parameter changes the rule coherently; pixel noise varies each sample.
