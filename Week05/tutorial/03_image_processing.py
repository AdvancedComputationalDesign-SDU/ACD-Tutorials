"""03 — Image Processing

Compare processing operations by the information they preserve or remove.
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

from skimage import io, color, filters
from skimage.util import img_as_float

# --- 01: Read RGB and convert its intensities deliberately ---
photo = img_as_float(io.imread(DATA_DIR / "Lenna.png"))
gray = color.rgb2gray(photo)
print("RGB / grayscale:", photo.shape, gray.shape)
print("Float range:", photo.min(), photo.max())
# A single red channel is not the same calculation as RGB-to-grayscale.

# --- 02: Sigma controls spatial smoothing, in pixels ---
soft = filters.gaussian(gray, sigma=1)
smooth = filters.gaussian(gray, sigma=3)
rgb_blur = filters.gaussian(photo, sigma=3, channel_axis=-1)
fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for ax, image, title in zip(axes, [gray, soft, smooth], ["Original", "Sigma 1", "Sigma 3"]):
    ax.imshow(image, cmap="gray", vmin=0, vmax=1)
    ax.set_title(title)
    ax.axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)

# --- 03: Compare edge strength with a shared color scale ---
edges_before = filters.sobel(gray)
edges_after = filters.sobel(smooth)
edge_max = max(edges_before.max(), edges_after.max())
fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for ax, image, title in zip(axes[:2], [edges_before, edges_after], ["Sobel", "Blur then Sobel"]):
    ax.imshow(image, cmap="magma", vmin=0, vmax=edge_max)
    ax.set_title(title)
    ax.axis("off")
axes[2].imshow(rgb_blur)
axes[2].set_title("Spatial RGB blur")
axes[2].axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)

# --- 04: A threshold returns a region, not an object identity ---
threshold = filters.threshold_otsu(gray)
mask = gray > threshold
print("Threshold and mask dtype:", threshold, mask.dtype)
fig, ax = plt.subplots()
ax.imshow(mask, cmap="gray", vmin=0, vmax=1)
ax.axis("off")
plt.show()
plt.close(fig)
# Bright regions, shadows, and texture do not automatically identify objects.
