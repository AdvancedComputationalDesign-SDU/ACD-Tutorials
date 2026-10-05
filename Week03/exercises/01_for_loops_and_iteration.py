"""01 — For Loops and Iteration — Worked Exercise

1. Calculate areas for widths [1.2, 1.5, 0.9, 1.8] and height 2.4; print Complete once.
2. Pair widths [1, 2, 3] and heights [2, 3, 4]; number the calculated areas from 1.
   Remove one height and detect the mismatch before processing the pairs.
3. Find the largest value in [3, 41, 12, 9, 74, 15] using a loop, not max().
   Repeat with [-8, -3, -12, -1] and an empty list. Define the empty result.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

widths_m = [1.2, 1.5, 0.9, 1.8]
height_m = 2.4
areas_m2 = []
for width_m in widths_m:
    area_m2 = width_m * height_m
    areas_m2.append(area_m2)
    print(width_m, area_m2)
print("Complete")
widths = [1, 2, 3]
heights = [2, 3, 4]
if len(widths) == len(heights):
    for number, pair in enumerate(zip(widths, heights), start=1):
        width, height = pair
        print(number, width * height)
heights.pop()
if len(widths) != len(heights):
    print("Mismatched measurement counts; no pairs processed")
for values in [[3, 41, 12, 9, 74, 15], [-8, -3, -12, -1], []]:
    largest = None
    for value in values:
        if largest is None or value > largest:
            largest = value
    print(values, "->", largest)
# None explicitly represents the absence of a maximum for an empty list.
