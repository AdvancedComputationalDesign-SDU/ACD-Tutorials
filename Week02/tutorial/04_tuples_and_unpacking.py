"""04 — Tuples and Unpacking

Use a fixed coordinate record and unpack its components by position.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

# --- 01: A tuple is an ordered immutable sequence ---
point = (2.0, 5.0)
print(point[0], point[-1], len(point))
x, y = point
shifted = (x + 3, y - 1)
print("Original:", point, "Shifted:", shifted)
one_item = (2.0,)  # The comma creates the single-item tuple.
print(type(one_item), type((2.0)))

# --- 02: Unpacking also works with other sequences ---
width_m, height_m = [1.2, 2.4]
print("Area:", width_m * height_m)
x, y = y, x
print("Swapped coordinates:", x, y)
# Three names cannot unpack a two-item point: that raises ValueError.

# --- 03: Immutable outer structure does not freeze contained objects ---
grouped = ("A", [1, 2])
grouped[1].append(3)
print(grouped)
# grouped[0] = "B" would fail, but the contained list is still mutable.
