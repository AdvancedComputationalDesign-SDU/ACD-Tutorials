"""03 — While Loops and Control

Make the changing state and termination condition explicit.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

# --- 01: Repeat until a target is reached or exceeded ---
height_mm = 0
layer_mm = 12
target_mm = 100
layers = 0
if not 0 < layer_mm < float("inf"):
    raise ValueError("Layer thickness must be positive and finite")
if not 0 <= target_mm < float("inf"):
    raise ValueError("Target height must be nonnegative and finite")
while height_mm < target_mm:
    height_mm += layer_mm
    layers += 1
    print("Layer:", layers, "Height:", height_mm)
print("Final height and layer count:", height_mm, layers)

# --- 02: break stops the loop immediately ---
remaining = 5
while remaining > 0:
    if remaining == 3:
        break
    print("Remaining:", remaining)
    remaining -= 1

# --- 03: continue skips the rest of this iteration ---
candidate = 0
even_numbers = []
while candidate < 10:
    candidate += 1  # Update before continue so progress cannot be skipped.
    if candidate % 2 != 0:
        continue
    even_numbers.append(candidate)
print(even_numbers)
# A zero layer thickness cannot make progress; the initial check rejects it.

# --- 04: The same control statements work in a for loop ---
values = [3, -1, 5, 0, 8]
for value in values:
    if value < 0:
        continue
    if value == 0:
        break  # Exits the nearest enclosing loop.
    print("Kept before zero:", value)
# Prints 3 and 5. The final 8 is never visited.
