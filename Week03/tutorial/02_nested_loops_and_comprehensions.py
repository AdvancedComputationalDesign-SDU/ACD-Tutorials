"""02 — Nested Loops and Comprehensions

Construct a grid and recognize when a comprehension expresses an existing loop more compactly.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

# --- 01: One outer iteration creates one independent row ---
row_count, column_count = 2, 3
grid = []
for row in range(row_count):
    values = []
    for column in range(column_count):
        values.append(row + column)
    grid.append(values)
print("Grid:", grid)
for r, row in enumerate(grid):
    for c, value in enumerate(row):
        print("Row, column, value:", r, c, value)
# Each row is traversed independently, even when rows have different lengths.

# --- 02: Repeating an inner list repeats a reference ---
shared = [[0] * 3] * 2
shared[0][0] = 1
independent = [[0] * 3 for row in range(2)]
independent[0][0] = 1
print("Shared rows:", shared)
print("Independent rows:", independent)

# --- 03: An expression and iteration can build a list ---
numbers = [1, 2, 3, 4, 5]
squares_loop = []
for number in numbers:
    squares_loop.append(number ** 2)
squares = [number ** 2 for number in numbers]
evens_loop = []
for value in squares:
    if value % 2 == 0:
        evens_loop.append(value)
evens = [value for value in squares if value % 2 == 0]
print(squares_loop == squares, squares, evens, sum(evens))
print("Loop and filter agree:", evens_loop == evens)
# Filtering changes which items remain; replacement preserves the count.
clamped = [value if value >= 0 else 0 for value in [-2, 0, 3]]
print("Replaced:", clamped)

# --- 04: Nested construction and flattening are different operations ---
grid_compact = [[r + c for c in range(3)] for r in range(2)]
flat = [value for row in grid_compact for value in row]
print(grid_compact, flat)

# --- 05: Filter characters after learning explicit iteration ---
word = "fa@miliar."
letters = []
for character in word:
    if character.isalpha():
        letters.append(character)
cleaned = "".join(letters)
print(cleaned)
# join also accepts a generator expression: no list is constructed here.
compact_text = "".join(ch for ch in word if ch.isalpha())
print(cleaned == compact_text)
