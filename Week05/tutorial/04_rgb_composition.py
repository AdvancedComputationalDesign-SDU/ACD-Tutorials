"""04 — RGB Composition

Build a richer image through small, explainable changes while keeping boundary artifacts outside the final crop.
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

# --- 01: Grayscale rings on a larger canvas ---
n, m = 320, 96  # Final side length and safety margin, in pixels.
N = n + 2 * m
coords = np.arange(-m, n + m) * 2 / (n - 1) - 1
X, Y = np.meshgrid(coords, coords)
distance = np.sqrt(X**2 + Y**2)
field = 0.5 + 0.5 * np.sin(8 * np.pi * distance)
a, b = m - 0.5, m + n - 0.5  # Pixel edges around the future crop.
OUTPUT_DIR.mkdir(exist_ok=True)
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(field, cmap="gray", vmin=0, vmax=1, origin="lower")
ax.plot([a,b,b,a,a], [a,a,b,b,a], "r-", lw=1.5)
ax.axis("off")
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "composition_01_rings.png", dpi=130)
plt.show()
plt.close(fig)

# --- 02: RGB separation without wrapping ---
# Positive row shifts appear upward because the origin is lower.
rgb = np.zeros((N, N, 3))
rgb[:, 12:, 0] = field[:, :-12]  # Red right.
rgb[8:, :, 1] = field[:-8, :]   # Green up.
rgb[:, :-12, 2] = field[:, 12:] # Blue left.
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(rgb, origin="lower")
ax.plot([a,b,b,a,a], [a,a,b,b,a], "r-", lw=1.5)
ax.axis("off")
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "composition_02_rgb.png", dpi=130)
plt.show()
plt.close(fig)

# --- 03: A second center changes the spatial field ---
second_distance = np.sqrt((X - 0.60)**2 + (Y + 0.40)**2)
field = 0.5 + 0.25 * (np.sin(8 * np.pi * distance) + np.sin(8 * np.pi * second_distance))
rgb = np.zeros((N, N, 3))
rgb[:, 12:, 0] = field[:, :-12]
rgb[8:, :, 1] = field[:-8, :]
rgb[:, :-12, 2] = field[:, 12:]
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(rgb, origin="lower")
ax.plot([a,b,b,a,a], [a,a,b,b,a], "r-", lw=1.5)
ax.axis("off")
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "composition_03_centers.png", dpi=130)
plt.show()
plt.close(fig)

# --- 04: Blend a shifted echo on the full canvas ---
echo = np.zeros_like(rgb)
echo[24:, 72:] = rgb[:-24, :-72]
blended = 0.55 * rgb + 0.45 * echo
# Largest accumulated shift: 12 + 72 = 84, less than the 96-pixel margin.
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(blended, origin="lower")
ax.plot([a,b,b,a,a], [a,a,b,b,a], "r-", lw=1.5)
ax.axis("off")
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "composition_04_echo.png", dpi=130)
plt.show()
plt.close(fig)

# --- 05: Crop only now; export pixels without the crop outline ---
final = blended[m:m+n, m:m+n].copy()
assert final.shape == (n, n, 3)
assert np.isfinite(final).all()
assert 0 <= final.min() <= final.max() <= 1
print("Final shape and range:", final.shape, final.min(), final.max())
plt.imsave(OUTPUT_DIR / "composition_final.png", final, origin="lower")
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(final, origin="lower")
ax.axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)
