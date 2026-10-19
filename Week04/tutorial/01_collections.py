"""01 — Collections

Choose a collection based on how the algorithm accesses and updates its data.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

from collections import deque
from copy import deepcopy

# --- 01: A dictionary associates a key with a value ---
panel = {"id": "A", "width": 1.2, "height": 2.4, "material": "timber"}
panel["area"] = panel["width"] * panel["height"]
panel["width"] = 1.5
print("Stored area:", panel["area"])  # Recalculate after changing inputs.
panel["area"] = panel["width"] * panel["height"]
print(panel["area"], panel.get("finish", "unspecified"))
print("finish" in panel)
for key, value in panel.items():
    print(key, value)
locations = {(0, 1): "A", (1, 1): "B"}  # These immutable tuples are hashable.
print(locations[(0, 1)])

# --- 02: A list preserves the order of records ---
panels = [
    {"id": "A", "width": 1, "height": 2},
    {"id": "B", "width": 2, "height": 3},
    {"id": "C", "width": -1, "height": 4},
]
valid_areas = []
for item in panels:
    if item["width"] <= 0 or item["height"] <= 0:
        print("Invalid dimensions:", item["id"])
        continue
    valid_areas.append(item["width"] * item["height"])
average = sum(valid_areas) / len(valid_areas) if valid_areas else None
print("Areas, total, average:", valid_areas, sum(valid_areas), average)
variation = deepcopy(panels)
variation[0]["width"] = 10
print("Original width:", panels[0]["width"])

# --- 03: Sets represent unique members, not positional order ---
design_a = {"timber", "steel", "glass"}
design_b = {"timber", "concrete"}
print("All:", sorted(design_a | design_b))
print("Shared:", sorted(design_a & design_b))
print("Only A:", sorted(design_a - design_b))
print("Exactly one design:", sorted(design_a ^ design_b))
# Sorting is only for predictable display; it is not a property of the set.

# --- 04: A stack and queue differ in removal order ---
history = []
history.append("move")
history.append("rotate")
print("Undo:", history.pop())  # Last in, first out.
pending = deque(["A", "B"])
pending.append("C")
print("Next task:", pending.popleft())  # First in, first out.
# Check whether the collection is nonempty before removing from it.
