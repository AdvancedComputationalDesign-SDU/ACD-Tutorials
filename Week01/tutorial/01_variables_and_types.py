"""01 — Variables and Types

Trace how names, values, and execution order determine a result.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

# --- 01: Assignment names a value ---
length_m = 6
width_m = 2
area_m2 = length_m * width_m
print("Area:", area_m2, "m²")

# --- 02: A calculation is not a permanently linked formula ---
length_m = 8.0
print("Stored area:", area_m2)  # Predict before running: still 12.
area_m2 = length_m * width_m
print("Recalculated area:", area_m2)  # 16.0

# --- 03: Values have types; names can be rebound ---
count = 4
thickness_m = 0.12
material = "timber"
approved = True
result = None  # No result has been supplied yet.
print(type(count), type(thickness_m), type(material))
print(type(approved), type(result))
label = "Panel A"
old_label = label
label = "Panel B"
print(old_label, label)  # Rebinding label does not rebind old_label.

# --- 04: Calling a function can produce a result ---
magnitude = abs(-3)
print("Magnitude:", magnitude)
print_result = print("print displays this text")
print("The returned value is:", print_result)  # None
# Discuss: which names tell you their units and purpose?
