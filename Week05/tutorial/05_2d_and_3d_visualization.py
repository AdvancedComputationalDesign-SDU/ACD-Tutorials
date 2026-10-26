"""05 — 2D and 3D Visualization

Compare representations of one composition while keeping coordinates, heights, and colors aligned.
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

# --- 01: Recreate the previous composition so this file runs independently ---
import numpy as np
import matplotlib.pyplot as plt

n, m = 320, 96
N = n + 2 * m
coords = np.arange(-m, n + m) * 2 / (n - 1) - 1
X, Y = np.meshgrid(coords, coords)
distance = np.sqrt(X**2 + Y**2)
second_distance = np.sqrt((X - 0.60)**2 + (Y + 0.40)**2)
field = 0.5 + 0.25 * (np.sin(8 * np.pi * distance) + np.sin(8 * np.pi * second_distance))
rgb = np.zeros((N, N, 3))
rgb[:, 12:, 0] = field[:, :-12]
rgb[8:, :, 1] = field[:-8, :]
rgb[:, :-12, 2] = field[:, 12:]
echo = np.zeros_like(rgb)
echo[24:, 72:] = rgb[:-24, :-72]
blended = 0.55 * rgb + 0.45 * echo
final = blended[m:m+n, m:m+n].copy()

# --- 02: Derive heights and sample every array consistently ---
from skimage.color import rgb2gray

height_field = rgb2gray(final)
view_X = X[m:m+n, m:m+n]
view_Y = Y[m:m+n, m:m+n]
plot_X = view_X[::4, ::4]
plot_Y = view_Y[::4, ::4]
plot_Z = height_field[::4, ::4]
plot_rgb = final[::4, ::4]
print("Sample shapes:", plot_X.shape, plot_Z.shape, plot_rgb.shape)
OUTPUT_DIR.mkdir(exist_ok=True)

# --- 03: Pixel color and contour views encode the same composition ---
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(final, origin="lower")
ax.axis("off")
plt.show()
plt.close(fig)
fig, ax = plt.subplots(figsize=(5, 4))
contour = ax.contourf(view_X, view_Y, height_field, levels=np.linspace(0, 1, 11), cmap="viridis")
ax.set(xlabel="x coordinate", ylabel="y coordinate", aspect="equal")
fig.colorbar(contour, ax=ax, label="Intensity")
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "composition_contours.png", dpi=150)
plt.show()
plt.close(fig)

# --- 04: Scatter: one colored point per sampled pixel ---
fig = plt.figure(figsize=(6, 4.5))
ax = fig.add_subplot(projection="3d")
ax.scatter(plot_X.ravel(), plot_Y.ravel(), plot_Z.ravel(),
           c=plot_rgb.reshape(-1, 3), s=2, depthshade=False)
ax.set(xlabel="x", ylabel="y", zlabel="Intensity", zlim=(0, 1))
ax.set_zticks([0, 1])
ax.view_init(elev=40, azim=-55)
ax.set_box_aspect((1, 1, 0.12))
fig.savefig(OUTPUT_DIR / "composition_scatter.png", dpi=150)
plt.show()
plt.close(fig)

# --- 05: Wireframe: connect sampled rows and columns ---
fig = plt.figure(figsize=(6, 4.5))
ax = fig.add_subplot(projection="3d")
ax.plot_wireframe(plot_X, plot_Y, plot_Z, rstride=4, cstride=4, color="#2878B5", linewidth=0.5)
ax.set(xlabel="x", ylabel="y", zlabel="Intensity", zlim=(0, 1))
ax.set_zticks([0, 1])
ax.view_init(elev=40, azim=-55)
ax.set_box_aspect((1, 1, 0.12))
fig.savefig(OUTPUT_DIR / "composition_wireframe.png", dpi=150)
plt.show()
plt.close(fig)

# --- 06: Surface: height from intensity, color from the image ---
fig = plt.figure(figsize=(6, 4.5))
ax = fig.add_subplot(projection="3d")
ax.plot_surface(plot_X, plot_Y, plot_Z, facecolors=plot_rgb,
                rstride=1, cstride=1, shade=False, linewidth=0, antialiased=False)
ax.set(xlabel="x", ylabel="y", zlabel="Intensity", zlim=(0, 1))
ax.set_zticks([0, 1])
ax.view_init(elev=40, azim=-55)
ax.set_box_aspect((1, 1, 0.12))
fig.savefig(OUTPUT_DIR / "composition_surface.png", dpi=150)
plt.show()
plt.close(fig)
# Intensity is a visual height encoding, not a physical elevation measurement.
# The shallow box changes display proportions, not the stored intensity values.
