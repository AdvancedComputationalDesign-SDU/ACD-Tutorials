"""01 — Array Operations

Predict the selected values and result shape before turning array operations into an image.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- 01: Rows first, columns second; stop is excluded ---
arr = np.arange(15).reshape(3, 5)
print(arr)
print("Row 1, column 3:", arr[1, 3])
print("First two rows:", arr[:2, :])
print("Selected block:", arr[:2, 2:4])
print("Every second column:", arr[:, ::2])
print("Separate steps:", arr[::2, ::3])
print("Reverse columns:", arr[:, ::-1])
print("Reverse rows:", arr[::-1, :])
print("Integer / slice shapes:", arr[2, :].shape, arr[2:3, :].shape)

# --- 02: View, copy, transpose, and reshape have different purposes ---
view = arr[:2, :2]
independent = view.copy()
view[0, 0] = 99
print(arr[0, 0], independent[0, 0])
print(arr.T, arr.T.shape)
print(np.arange(6).reshape(2, 3))
# reshape preserves the number of elements; it does not resize an image.
grid = np.arange(6).reshape(2, 3)
offsets = np.array([10, 20, 30])
print(grid + offsets)  # Corresponding trailing dimensions match.
print(offsets[:, np.newaxis].shape)  # (3, 1)
print(grid.mean(axis=0), grid.max(axis=1))

# --- 03: Three independent arrays, three spatial rules ---
square = np.zeros((32, 32), dtype=float)
stripes = np.zeros_like(square)
lattice = np.zeros_like(square)
square[12:20, 12:20] = 1
stripes[:, ::4] = 1
lattice[::4, :] = 1
lattice[:, ::6] = 1
fig, axes = plt.subplots(1, 3, figsize=(9, 3))
for ax, image in zip(axes, [square, stripes, lattice]):
    ax.imshow(image, cmap="gray", vmin=0, vmax=1, origin="lower", interpolation="nearest")
    ax.axis("off")
fig.tight_layout()
plt.show()
plt.close(fig)
