"""01 — Array Operations — Worked Exercise

1. Create three separate floating-point arrays with shape (32, 32).
2. Make an 8-by-8 white square centered on the first array.
3. Make white vertical stripes every fourth column on the second.
4. On the third, make white rows every fourth row and columns every sixth column.
5. Display all three with fixed grayscale limits. Count the white pixels.
6. Change spacing or thickness and predict the result before running.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

import numpy as np
import matplotlib.pyplot as plt

square = np.zeros((32, 32), dtype=float)
stripes = np.zeros_like(square)
lattice = np.zeros_like(square)
square[12:20, 12:20] = 1
stripes[:, ::4] = 1
lattice[::4, :] = 1
lattice[:, ::6] = 1
print("White pixels:", square.sum(), stripes.sum(), lattice.sum())
# Grid: 8*32 + 6*32 - 8*6; intersections must not be counted twice.
fig, axes = plt.subplots(1, 3, figsize=(9, 3))
for ax, image in zip(axes, [square, stripes, lattice]):
    ax.imshow(image, cmap="gray", vmin=0, vmax=1, origin="lower", interpolation="nearest")
    ax.axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)
# One variation: two-pixel stripes. Adjacent offset slices widen each stripe.
thick = np.zeros((32, 32))
thick[:, ::4] = 1
thick[:, 1::4] = 1
print("Two-pixel stripes:", thick.sum())  # 512 instead of 256.
