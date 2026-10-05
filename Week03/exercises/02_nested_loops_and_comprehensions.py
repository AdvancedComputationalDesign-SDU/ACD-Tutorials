"""02 — Nested Loops and Comprehensions — Worked Exercise

1. Build a 2-row, 3-column grid where each value is row + column using nested loops.
2. Build the same grid using a nested comprehension; compare the results.
3. For numbers 1 through 10: square them, keep the even squares, and sum those values.
4. Change the first cell of one row and verify the other rows are independent.
5. Repeat the grid construction with 3 rows and 4 columns.
6. Extension: flatten the larger grid and keep only values greater than 1.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

row_count, column_count = 2, 3
grid = []
for row in range(row_count):
    values = []
    for column in range(column_count):
        values.append(row + column)
    grid.append(values)
compact = [[r + c for c in range(column_count)] for r in range(row_count)]
print(grid, compact, grid == compact)
numbers = list(range(1, 11))
squared = [value ** 2 for value in numbers]
filtered = [value for value in squared if value % 2 == 0]
total = sum(filtered)
print(squared, filtered, total)
grid[0][0] = 99
print(grid)  # Only the first row changes.

row_count, column_count = 3, 4
extended_grid = []
for row in range(row_count):
    values = []
    for column in range(column_count):
        values.append(row + column)
    extended_grid.append(values)
extended_compact = [
    [r + c for c in range(column_count)] for r in range(row_count)
]
print("Larger grid:", extended_grid)
assert extended_grid == extended_compact
flat = [value for row in extended_grid for value in row]
greater_than_one = [value for value in flat if value > 1]
print("Flattened:", flat)
print("Values greater than 1:", greater_than_one)
