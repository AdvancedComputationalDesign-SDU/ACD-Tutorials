"""02 — NumPy Arrays

Represent regular numerical data with explicit axes, units, and a common dtype.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

import numpy as np

# --- 01: Python lists may mix types; numerical arrays use a common dtype ---
record = ["P01", 2.4, True]
lengths = [1, 2, 3]
print(record, lengths * 2)  # List repetition, not numerical scaling.
numbers = np.array(lengths, dtype=float)
print(numbers * 2, numbers.dtype)
measurements_mm = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
print(measurements_mm.shape, measurements_mm.ndim, measurements_mm.size)
# Shape (2, 3): two rows, three columns, six scalar elements.
rgb_example = np.zeros((4, 7, 3))
print("RGB shape:", rgb_example.shape)  # Third axis means channels, not depth.

# --- 02: Create and select numerical values ---
print(np.zeros((2, 3)), np.ones((2, 3)))
print(np.arange(0, 6, 2), np.linspace(0, 1, 5))
print(measurements_mm[1, 2], measurements_mm[:, 1])
print(measurements_mm[0:1, :].shape)  # A slice preserves the row axis.

# --- 03: Views share data; copies are independent ---
original = np.arange(6, dtype=float).reshape(2, 3)
view = original[:, :2]
separate = view.copy()
view[0, 0] = 99
print(original, separate)
ints = np.array([1, 2, 3])
ints[0] = 0.5
print("Integer storage:", ints)  # The fraction is lost.

# --- 04: One expression can operate on every element ---
measurements_m = measurements_mm / 1000
row_means_m = measurements_m.mean(axis=1)
column_max_m = measurements_m.max(axis=0)
print("Meters:", measurements_m)
print("One mean per row:", row_means_m)
print("One maximum per column:", column_max_m)
print("Reduction shapes:", row_means_m.shape, column_max_m.shape)
loop_result = []
for value in [1000, 2000, 3000]:
    loop_result.append(value / 1000)
print(loop_result, np.array([1000, 2000, 3000]) / 1000)
