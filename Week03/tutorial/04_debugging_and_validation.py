"""04 — Debugging and Validation

Find a wrong result, then distinguish conversion failures from invalid numeric values.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

# --- 01: Find the first incorrect state ---
values = [2, 4, 6]
total = 0  # Must be initialized before the loop, not during each iteration.
for value in values:
    print("Before:", value, total)
    total += value  # Set a breakpoint here and inspect value and total.
    print("After:", total)
assert total == 12
# A logic error would be to move total = 0 inside the loop.

# --- 02: Read and explain a specific runtime error ---
# A syntax error prevents parsing; a missing colon is one example:
# if width > 0
# A logic error can run successfully and still calculate the wrong answer:
# area = 4 + 2  # 6, although a 4-by-2 rectangle has an area of 8.
width_text = "2.4"
# print(width_text + 1)  # Uncomment alone to inspect the TypeError traceback.
print(float(width_text) + 1)

# --- 03: Signal an invalid numeric input explicitly ---
layer_mm = 12
# layer_mm = 0  # Activate to see the explicit validation failure.
if layer_mm <= 0:
    raise ValueError(f"Layer thickness must be positive: {layer_mm}")

# --- 04: Catch expected conversion errors, not every programming error ---
width_text = "1.2"
# width_text = input("Positive panel width in meters: ")
try:
    width_m = float(width_text)
except ValueError:
    print("Enter a numeric value")
else:
    if not 0 < width_m < float("inf"):
        print("Width must be positive and finite")
    else:
        print("Valid width:", width_m)
# Try "wide", "0", "-1", "1.2", "nan", and "inf".
# To signal a new error, use raise ValueError(...); a bare raise needs an active error.

# --- 05: Check outcomes, not merely successful execution ---
areas = [width * 2 for width in [1, 2, 3]]
assert len(areas) == 3
assert areas == [2, 4, 6]
# assert supports development checks; explicit validation handles external input.
