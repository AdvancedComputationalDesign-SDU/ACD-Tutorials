"""02 — Additional Filters — Optional
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
    if WEEK_DIR.name != "Week05":
        WEEK_DIR = WEEK_DIR / "Week05"
DATA_DIR = WEEK_DIR / "data"
OUTPUT_DIR = WEEK_DIR / "outputs"

import numpy as np
import matplotlib.pyplot as plt

from skimage import io, color, filters, feature, morphology, exposure, transform
from skimage.util import img_as_float

photo = img_as_float(io.imread(DATA_DIR / "Lenna.png"))
gray = color.rgb2gray(photo)
rng = np.random.default_rng(26)
noise = rng.random(gray.shape)
noisy = gray.copy()
noisy[noise < 0.03] = 0
noisy[noise > 0.97] = 1
median = filters.median(noisy, morphology.disk(1))
canny = feature.canny(gray, sigma=2)
brighter = exposure.adjust_gamma(gray, gamma=0.5)
resized = transform.resize(gray, (64, 64), anti_aliasing=True, preserve_range=True)
sampled = gray[::8, ::8]
rotated = transform.rotate(photo, angle=30, resize=True, preserve_range=True)
images = [noisy, median, canny, brighter, sampled, resized, photo, rotated]
titles = ["Impulse noise", "Median", "Canny", "Gamma 0.5", "Subsample", "Resize", "RGB", "Rotate"]
fig, axes = plt.subplots(2, 4, figsize=(11, 6))
for ax, image, title in zip(axes.ravel(), images, titles):
    ax.imshow(image, cmap="gray", vmin=0, vmax=1)
    ax.set_title(title)
    ax.axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)
mask = np.zeros((64, 64), dtype=bool)
mask[16:48, 16:48] = True
mask[8:10, 8:10] = True
mask[30:33, 30:33] = False
opened = morphology.opening(mask, morphology.disk(2))
closed = morphology.closing(opened, morphology.disk(2))
fig, axes = plt.subplots(1, 3, figsize=(8, 3))
for ax, image, title in zip(axes, [mask, opened, closed], ["Mask", "Opening", "Then closing"]):
    ax.imshow(image, cmap="gray", vmin=0, vmax=1)
    ax.set_title(title)
    ax.axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)
# Each filter encodes a different rule. Choose based on your intention,
# not on the number of library functions you can chain together.
