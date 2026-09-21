"""01 — Logic and Conditionals

Express a rule as Boolean conditions, then choose the matching branch.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

# --- 01: Comparisons produce Boolean values ---
width_m = 1.2
height_m = 2.4
material = "timber"
print("Positive dimensions:", width_m > 0 and height_m > 0)
print("At least one dimension above 2 m:", width_m > 2 or height_m > 2)
print("Timber or steel:", material == "timber" or material == "steel")
print("Not concrete:", not (material == "concrete"))
print("Same check with !=:", material != "concrete")
print("Timber and positive:", material == "timber" and width_m > 0 and height_m > 0)
print("Width in [1, 2):", 1 <= width_m < 2)
count = 0
print("Safe division check:", count != 0 and 10 / count > 2)
# and skips the division because the first condition is False.

# --- 02: Test the broad invalid condition first ---
area_m2 = width_m * height_m
if area_m2 <= 0:
    category = "Invalid"
elif area_m2 < 2:
    category = "Small"
elif area_m2 < 5:
    category = "Medium"
else:
    category = "Large"
print("Area and category:", area_m2, category)
# Try area_m2 = -1.0, 0.0, 1.5, 2.0, 4.9, and 5.0 in separate runs.
# Which branch includes each value, including the exact boundaries?

# --- 03: A nested condition expresses a second decision ---
if width_m > 0 and height_m > 0:
    if material == "timber":
        print("Valid timber panel")
    else:
        print("Valid dimensions; another material")
else:
    print("Invalid dimensions")
# = assigns a value; == compares values. Use == for material labels.
