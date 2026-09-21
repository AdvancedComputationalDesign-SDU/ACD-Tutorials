"""02 — Arithmetic and Units

Translate a panel transport question into arithmetic with explicit units.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

# --- 01: Measurements and counts represent different quantities ---
panel_count = 53
length_m = 2.4
width_m = 1.2
rack_capacity = 8
area_m2 = length_m * width_m
perimeter_m = 2 * (length_m + width_m)
total_area_m2 = panel_count * area_m2
print("One panel:", area_m2, "m²; perimeter:", perimeter_m, "m")
print("All panels:", total_area_m2, "m²")

# --- 02: Division answers three different questions ---
rack_equivalents = panel_count / rack_capacity
full_racks = panel_count // rack_capacity
remaining_panels = panel_count % rack_capacity
print("Rack equivalents:", rack_equivalents)  # 6.625
print("Full racks:", full_racks, "Left over:", remaining_panels)  # 6, 5
print("Reconstructed count:", full_racks * rack_capacity + remaining_panels)
# For these nonnegative counts, // gives the number of full racks.
# In general, floor division rounds toward negative infinity.
print("Negative example:", -7 // 3, -7 % 3)  # -3, 2

# --- 03: Parentheses and powers ---
print("Squared length:", length_m ** 2, "m²")
print("2 + 3 * 4:", 2 + 3 * 4)
print("(2 + 3) * 4:", (2 + 3) * 4)
print("Space left on an extra rack:", rack_capacity - remaining_panels)
# Discuss the exact-multiple case before deciding whether another rack is needed.
