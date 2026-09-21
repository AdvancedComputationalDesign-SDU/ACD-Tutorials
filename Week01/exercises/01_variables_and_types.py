"""01 — Variables and Types — Worked Exercise

1. Assign length_m = 6 and width_m = 2, then store their area.
2. Change length_m to 8.0. Predict the stored area, then print it.
3. Recalculate the area and print its value and type.
4. Explain why the first stored area did not update automatically.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

length_m = 6
width_m = 2
area_m2 = length_m * width_m
length_m = 8.0
print("Stored:", area_m2)  # 12: this expression was evaluated earlier.
area_m2 = length_m * width_m
print("Recalculated:", area_m2, type(area_m2))  # 16.0, float
