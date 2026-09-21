"""04 — Tuples and Unpacking — Worked Exercise

1. Unpack point = (2.0, 5.0) into x and y.
2. Create a new point shifted by +3 in X and -1 in Y; keep the original unchanged.
3. Print both points and explain why you constructed a new tuple.
4. Create a single-item tuple containing 2.0 and inspect its type.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

point = (2.0, 5.0)
x, y = point
shifted = (x + 3, y - 1)
print("Original:", point)
print("Shifted:", shifted)  # (5.0, 4.0)
single = (2.0,)
print(single, type(single))
# A tuple cannot have an element replaced; a new tuple represents the new point.
