"""02 — NumPy Arrays — Worked Exercise

1. Make a floating-point array with rows [1, 2, 3] and [4, 5, 6], in millimeters.
2. Convert it to meters without changing the original measurements.
3. Calculate the mean of each row and the maximum of each column. Predict shapes first.
4. Copy the first row, change its first value, and show that the original is unchanged.
5. Compare [1, 2, 3] * 2 with np.array([1, 2, 3]) * 2.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

import numpy as np

measurements_mm = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
measurements_m = measurements_mm / 1000
row_means_m = measurements_m.mean(axis=1)
column_max_m = measurements_m.max(axis=0)
print(measurements_mm, measurements_m)
print(row_means_m, row_means_m.shape)  # [0.002, 0.005], (2,)
print(column_max_m, column_max_m.shape)  # [0.004, 0.005, 0.006], (3,)
first_row = measurements_mm[0].copy()
first_row[0] = 99
print(measurements_mm[0, 0], first_row[0])  # 1, 99
print([1, 2, 3] * 2, np.array([1, 2, 3]) * 2)
