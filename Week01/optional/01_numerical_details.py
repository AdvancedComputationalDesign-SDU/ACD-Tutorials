"""01 — Numerical Details — Optional
Run independently after the core topics; this is not another required exercise.
"""

import math

print("Pi:", math.pi, "Square root:", math.sqrt(16))
print("Binary floating-point:", 0.1 + 0.2)
print("Close to 0.3:", math.isclose(0.1 + 0.2, 0.3))
print("Rounded for display:", round(0.1 + 0.2, 2))
z = 2 + 3j
print(z.real, z.imag, abs(z))
# Complex numbers are an available numeric type, not an Assignment 1 prerequisite.
