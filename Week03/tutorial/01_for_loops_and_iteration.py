"""01 — For Loops and Iteration

Apply one rule to many values, and track the state accumulated by a loop.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

# --- 01: Iterate over values directly ---
widths_m = [1.2, 1.5, 0.9, 1.8]
height_m = 2.4
areas_m2 = []
for width_m in widths_m:
    area_m2 = width_m * height_m
    areas_m2.append(area_m2)
    print(f"{width_m:.1f} m -> {area_m2:.2f} m²")
print("Complete")  # Once, after the loop.

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# --- 02: An index is useful when position is part of the task ---
print(list(range(4)))  # [0, 1, 2, 3]
print(list(range(2, 8, 2)))  # [2, 4, 6]; the stop value is excluded.
for i in range(len(widths_m)):
    print("Position:", i, "Width:", widths_m[i])
for number, width_m in enumerate(widths_m, start=1):
    print("Panel", number, "width", width_m)

measurements = [2, 4, 6]
for measurement in measurements:
    measurement = measurement * 2
print("Reassigned loop variable:", measurements)  # [2, 4, 6]
for i in range(len(measurements)):
    measurements[i] = measurements[i] * 2
print("Replaced list elements:", measurements)  # [4, 8, 12]

# --- 03: Pair related sequences ---
widths = [1, 2, 3]
heights = [2, 3, 4]
if len(widths) == len(heights):
    for number, (width, height) in enumerate(zip(widths, heights), start=1):
        print(number, width * height)
else:
    print("Cannot pair every measurement: lengths differ")
print("Short zip:", list(zip(widths, heights[:-1])))
# zip stops at the shortest sequence; compare lengths first when every pair matters.

# --- 04: Count, total, and maximum remember previous iterations ---
values = [3, 41, 12, 9, 74, 15]
count = 0
total = 0
largest = None
for value in values:
    count += 1
    total += value
    if largest is None or value > largest:
        largest = value
    print("value:", value, "total:", total, "largest:", largest)
if count > 0:
    average = total / count
else:
    average = None
print("Count, total, average, largest:", count, total, average, largest)
# For an empty input, the count/total are 0 and average/largest stay None.

# --- 05: Dictionaries and records keep labels with measurements ---
widths_by_id = {"A": 1.2, "B": 1.5}
for label in widths_by_id:
    print("Key:", label)  # Direct iteration visits keys.
for label, width_m in widths_by_id.items():
    print(label, width_m)  # items() supplies key-value pairs.

panels = [
    {"id": "A", "width": 1.2},
    {"id": "B", "width": 1.5},
]
for panel in panels:
    print(panel["id"], panel["width"])
# The panel-data exercise combines these records with validation and totals.
