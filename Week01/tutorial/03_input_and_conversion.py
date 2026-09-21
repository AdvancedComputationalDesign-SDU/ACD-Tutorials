"""03 — Input and Conversion

Convert text input before using it in numerical expressions.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

# --- 01: Fixed text behaves like the text returned by input() ---
length_text = "2.4"
width_text = "1.2"
# To test your own values, uncomment these two lines:
# length_text = input("Panel length in meters: ")
# width_text = input("Panel width in meters: ")
print("Before conversion:", type(length_text), type(width_text))

# --- 02: Convert, calculate, report ---
length_m = float(length_text)
width_m = float(width_text)
area_m2 = length_m * width_m
print("Area:", area_m2, "m²")

# --- 03: Conversion has a meaning and can fail ---
panel_count = int("53")
print("Count:", panel_count)
print("int(2.9):", int(2.9))  # Truncation toward zero, not rounding.
print("Text again:", str(panel_count))
print('"2" + "3":', "2" + "3")
print('int("2") + int("3"):', int("2") + int("3"))
# float("wide") would raise ValueError. We handle that explicitly in W03.
