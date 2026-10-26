"""03 — Image Processing — Worked Exercise

1. Load the supplied RGB image and convert it to grayscale.
2. Compare Gaussian sigma=1 and sigma=3 with fixed grayscale limits.
3. Compare Sobel edges before and after sigma=3 smoothing with shared color limits.
4. Save the comparison figure. State which details disappear and one useful application.
5. Explain why channel_axis=-1 matters when blurring an RGB image.

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

import matplotlib.pyplot as plt

from skimage import io, color, filters
from skimage.util import img_as_float

photo = img_as_float(io.imread(DATA_DIR / "Lenna.png"))
gray = color.rgb2gray(photo)
sigma_1 = filters.gaussian(gray, sigma=1)
sigma_3 = filters.gaussian(gray, sigma=3)
edges_before = filters.sobel(gray)
edges_after = filters.sobel(sigma_3)
edge_max = max(edges_before.max(), edges_after.max())
fig, axes = plt.subplots(2, 2, figsize=(7, 7))
images = [sigma_1, sigma_3, edges_before, edges_after]
titles = ["Sigma 1", "Sigma 3", "Sobel", "Blur then Sobel"]
for i, (ax, image, title) in enumerate(zip(axes.ravel(), images, titles)):
    upper = 1 if i < 2 else edge_max
    ax.imshow(image, cmap="gray", vmin=0, vmax=upper)
    ax.set_title(title)
    ax.axis("off")
fig.tight_layout()
OUTPUT_DIR.mkdir(exist_ok=True)
fig.savefig(OUTPUT_DIR / "exercise_filter_comparison.png", dpi=160)
plt.show()
plt.close(fig)
# Smoothing suppresses fine texture and weak edges; useful before identifying
# larger boundaries, but it can also remove meaningful small features.
# channel_axis=-1 identifies channels so the blur operates spatially,
# rather than mixing the red, green, and blue intensities together.
