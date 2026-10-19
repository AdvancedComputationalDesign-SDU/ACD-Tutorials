"""01 — Collections — Worked Exercise

1. Store a panel's area, change its width, and recalculate the area.
2. Process the panel records below: print invalid IDs, collect valid areas,
   and calculate their total and average. Use None when no valid areas remain.
3. Find the union, intersection, and difference of the two material sets.
4. Add A, B, C to a stack and a queue; remove one item from each and explain the result.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

from collections import deque

panel = {"width": 1.2, "height": 2.4}
panel["area"] = panel["width"] * panel["height"]
panel["width"] = 1.5
print("Stored:", panel["area"])
panel["area"] = panel["width"] * panel["height"]
print("Recalculated:", panel["area"])
panels = [
    {"id": "A", "width": 1, "height": 2},
    {"id": "B", "width": 2, "height": 3},
    {"id": "C", "width": -1, "height": 4},
]
areas = []
for panel in panels:
    if panel["width"] <= 0 or panel["height"] <= 0:
        print("Invalid:", panel["id"])
        continue
    areas.append(panel["width"] * panel["height"])
total = sum(areas)
average = total / len(areas) if areas else None
print(areas, total, average)
design_a = {"timber", "steel", "glass"}
design_b = {"timber", "concrete"}
print(sorted(design_a | design_b), sorted(design_a & design_b), sorted(design_a - design_b))
stack = []
queue = deque()
for label in ["A", "B", "C"]:
    stack.append(label)
    queue.append(label)
print("Stack:", stack.pop(), "Queue:", queue.popleft())  # C, A
