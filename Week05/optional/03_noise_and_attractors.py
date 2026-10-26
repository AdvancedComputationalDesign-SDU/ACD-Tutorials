"""03 — Noise and Attractors — Optional
Run independently after the core topics; this is not another required exercise.
"""

import numpy as np
import matplotlib.pyplot as plt

from skimage import filters

coords = np.linspace(-1, 1, 128)
X, Y = np.meshgrid(coords, coords)
rng = np.random.default_rng(26)
noise = rng.random(X.shape)
coherent = filters.gaussian(noise, sigma=5)
span = coherent.max() - coherent.min()
if span == 0:
    raise ValueError("A constant field cannot be rescaled by its range")
coherent = (coherent - coherent.min()) / span
warped = 0.5 + 0.5 * np.sin(6 * np.pi * X + 8 * coherent)
# This is spatially correlated, smoothed random noise, not Perlin noise.
points = rng.uniform(-1, 1, size=(12, 2))
nearest = np.full(X.shape, np.inf)
for px, py in points:
    distance = np.sqrt((X - px)**2 + (Y - py)**2)
    nearest = np.minimum(nearest, distance)
rings = np.sin(45 * nearest)
keep = (np.abs(points[:, 0]) < 0.6) & (np.abs(points[:, 1]) < 0.6)
chosen = points[keep]
if len(chosen) == 0:
    raise ValueError("No attractors selected; change the selection rule")
restricted = np.full(X.shape, np.inf)
for px, py in chosen:
    distance = np.sqrt((X - px)**2 + (Y - py)**2)
    restricted = np.minimum(restricted, distance)
fig, axes = plt.subplots(1, 4, figsize=(12, 3))
for ax, image, title in zip(axes, [coherent, warped, rings, restricted],
                           ["Smooth noise", "Warped wave", "Nearest rings", "Selected attractors"]):
    ax.imshow(image, cmap="viridis", origin="lower")
    ax.set_title(title)
    ax.axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)
# Optional equivalent calculation: inspect the extra axes before using it.
coordinates = np.stack([X, Y], axis=-1)
offsets = coordinates[:, :, None, :] - points[None, None, :, :]
distances = np.sqrt((offsets**2).sum(axis=-1))
print("Loop and broadcast agree:", np.allclose(nearest, distances.min(axis=-1)))
