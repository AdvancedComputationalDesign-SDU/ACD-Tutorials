"""04 — Debugging and Validation — Worked Exercise

1. Fix the reset-inside-loop error shown below. Test a different list and an empty list.
2. Validate the fixed text input "1.2" as a positive finite width.
3. Distinguish a conversion failure from a numeric value outside the permitted range.
4. Test "wide", "0", "-1", "1.2", "nan", and "inf". Then test keyboard input
   in the separate interactive section, including another valid width such as "2.4".
5. Explain where you would place a breakpoint to inspect the running total.
6. Process the lecture's panel records: A has width 1 and height 2; B has
   width 2 and height 3; C has width -1 and height 4. Skip invalid panels,
   print their IDs, and collect the valid areas. Report the total and average.
   Repeat when every panel is invalid and when the list is empty.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

# --- 01: Diagnose the faulty algorithm, then compare the correction ---
# Run this commented snippet alone in a fresh session after predicting its result:
# values = [2, 4, 6]
# for value in values:
#     total = 0
#     total += value
# print(total)
# It prints 6. With an empty list, total is never defined in a fresh session.

totals = []
for values in [[2, 4, 6], [1, 3], []]:
    total = 0
    for value in values:
        total += value  # Break here to inspect the accumulated state.
    print(values, "->", total)
    totals.append(total)
assert totals == [12, 4, 0]

# --- 02: Check the fixed reference inputs ---
test_values = ["wide", "0", "-1", "1.2", "nan", "inf"]
accepted = []
for text in test_values:
    try:
        width_m = float(text)
    except ValueError:
        print(text, "-> Enter a numeric value")
        continue
    if not 0 < width_m < float("inf"):
        print(text, "-> Width must be positive and finite")
        continue
    accepted.append(width_m)
    print(text, "-> Valid width")
assert accepted == [1.2]
# The positive-finite interval also rejects nan and inf without accepting
# a numerically invalid dimension as a usable panel measurement.

# --- 03: Keyboard input is independent of the fixed reference check ---
width_text = "1.2"
# width_text = input("Positive width in meters: ")
try:
    width_m = float(width_text)
except ValueError:
    print("Enter a numeric value")
else:
    if not 0 < width_m < float("inf"):
        print("Width must be positive and finite")
    else:
        print("Valid width:", width_m)

# --- 04: Validate records and summarize only accepted panels ---
panels = [
    {"id": "A", "width": 1, "height": 2},
    {"id": "B", "width": 2, "height": 3},
    {"id": "C", "width": -1, "height": 4},
]
invalid_panels = [
    {"id": "D", "width": 0, "height": 2},
    {"id": "E", "width": 1, "height": -2},
]
for case_number, records in enumerate([panels, invalid_panels, []], start=1):
    areas_m2 = []
    for panel in records:
        width_m = panel["width"]
        height_m = panel["height"]
        if not 0 < width_m < float("inf") or not 0 < height_m < float("inf"):
            print("Skipped panel:", panel["id"])
            continue
        areas_m2.append(width_m * height_m)
    total_m2 = sum(areas_m2)
    if areas_m2:
        average_m2 = total_m2 / len(areas_m2)
    else:
        average_m2 = None  # No valid area exists to average.
    print("Panel case:", case_number, "Areas:", areas_m2)
    print("Total:", total_m2, "Average:", average_m2)
# First case: skip C; areas [2, 6], total 8, average 4.0.
# All-invalid and empty cases: areas [], total 0, average None.
