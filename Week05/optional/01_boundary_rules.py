"""01 — Boundary Rules — Optional
Run independently after the core topics; this is not another required exercise.
"""

import numpy as np
import matplotlib.pyplot as plt

marker = np.zeros((4, 7))
marker[1, 6] = 1
wrapped = np.roll(marker, shift=2, axis=1)
clipped = np.zeros_like(marker)
clipped[:, 2:] = marker[:, :-2]
print("Wrap preserves the marker:", wrapped.sum())
print("Clipped shift loses the out-of-frame marker:", clipped.sum())
fig, axes = plt.subplots(1, 3, figsize=(9, 3))
for ax, image, title in zip(axes, [marker, wrapped, clipped], ["Original", "Wrap", "Zero fill"]):
    ax.imshow(image, cmap="gray", vmin=0, vmax=1, origin="lower", interpolation="nearest")
    ax.set_title(title)
    ax.axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)
# A larger procedural domain plus a final crop supplies continuous content.
# Padding an already generated small image with zeros does not create that content.
