"""03 — Input and Conversion — Worked Exercise

1. Start with the text values "3.5" and "2.0" for a rectangle's dimensions.
2. Convert them, calculate the area, and print the value with m².
3. Add commented input() alternatives so someone can enter other dimensions.
4. Explain why the conversion is necessary. What happens with "wide"?

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

length_text = "3.5"
width_text = "2.0"
# length_text = input("Length in meters: ")
# width_text = input("Width in meters: ")
length_m = float(length_text)
width_m = float(width_text)
area_m2 = length_m * width_m
print("Area:", area_m2, "m²")  # 7.0
# input() returns text; float converts numeric text into a number.
# "wide" is not numeric text, so float("wide") raises ValueError.
