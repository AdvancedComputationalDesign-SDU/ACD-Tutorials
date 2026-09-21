"""02 — Arithmetic and Units — Worked Exercise

You have 53 panels, each 2.4 m by 1.2 m. A rack holds 8 panels.
1. Calculate one panel's area and perimeter, and the total area.
2. Calculate rack equivalents, completely filled racks, and remaining panels.
3. Reconstruct the panel count from the quotient and remainder.
4. Repeat with 56 panels. Explain the change in the remainder.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

panel_count = 53
length_m = 2.4
width_m = 1.2
rack_capacity = 8
area_m2 = length_m * width_m
perimeter_m = 2 * (length_m + width_m)
total_area_m2 = panel_count * area_m2
equivalents = panel_count / rack_capacity
full_racks = panel_count // rack_capacity
remainder = panel_count % rack_capacity
print("Area, perimeter, total area:", area_m2, perimeter_m, total_area_m2)
print("Rack equivalents, full racks, remaining panels:", equivalents, full_racks, remainder)
print("Check:", full_racks * rack_capacity + remainder)
panel_count = 56
print("56 panels:", panel_count // rack_capacity, "full racks and", panel_count % rack_capacity, "remaining")
# Floating-point arithmetic may display tiny differences in trailing digits.
