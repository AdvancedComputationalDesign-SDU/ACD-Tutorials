"""03 — While Loops and Control — Worked Exercise

1. Starting at 0 mm, add 12-mm layers until the height reaches or exceeds 100 mm.
2. Print each height, the final height, and the number of layers.
3. Repeat with a 96-mm target, then a 0-mm target.
4. Explain why a zero layer thickness would prevent termination without a check.
   Reject zero or negative thickness before entering the loop.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

layer_mm = 12
if not 0 < layer_mm < float("inf"):
    raise ValueError("Layer thickness must be positive and finite")
for target_mm in [100, 96, 0]:
    if not 0 <= target_mm < float("inf"):
        raise ValueError("Target height must be nonnegative and finite")
    height_mm = 0
    layers = 0
    while height_mm < target_mm:
        height_mm += layer_mm
        layers += 1
        print("Height:", height_mm)
    print("Target:", target_mm, "Final:", height_mm, "Layers:", layers)
# Results: 108/9, 96/8, and 0/0. Invalid thickness is rejected before looping.
