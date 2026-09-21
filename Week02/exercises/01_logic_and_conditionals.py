"""01 — Logic and Conditionals — Worked Exercise

1. With width_m = 1.2, height_m = 2.4, material = "timber", check positive
   dimensions, at least one dimension above 2 m, material equal to timber or
   steel, and material not equal to concrete.
2. Classify area: <= 0 Invalid; (0, 2) Small; [2, 5) Medium; >= 5 Large.
3. Test area_m2 = -1.0, 0.0, 1.5, 2.0, 4.9, and 5.0 in separate runs.
   Explain which branch handles each value.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

width_m = 1.2
height_m = 2.4
material = "timber"
print(width_m > 0 and height_m > 0)
print(width_m > 2 or height_m > 2)
print(material == "timber" or material == "steel")
print(not (material == "concrete"))  # Equivalent to material != "concrete".
area_m2 = width_m * height_m
# area_m2 = float(input("Area in m²: "))
if area_m2 <= 0:
    category = "Invalid"
elif area_m2 < 2:
    category = "Small"
elif area_m2 < 5:
    category = "Medium"
else:
    category = "Large"
print(category)
# -1 and 0 -> Invalid; 1.5 -> Small; 2 and 4.9 -> Medium; 5 -> Large.
# Only the first matching branch runs.
