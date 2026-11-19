# Week 08 · Python for Computer-Aided Design

Build two parametric models during the lecture. In Rhino 8, open Grasshopper and add a **Python 3 Script** component for each exercise. Use the default `x`, `y`, `out` and `a` ports. Start with the inputs unwired, watch the geometry from `a`, and connect a Panel to `out` for the printed checks.

## Part 3 · Two truss patterns

Build a 12-unit truss with four equal bays and a height of 3 units.

1. Place two rows of five nodes in the XZ plane. Use consecutive pairs for the top and bottom chords, then connect corresponding nodes with verticals.
2. Mirror the diagonals on either side of the centre. With an odd number of bays, leave the middle bay without a diagonal. Four bays give **10 nodes and 17 members**. Set `x` to seven and check for **16 nodes and 28 members**.
3. For the crossed pattern, set `crossed = True` and add both diagonals in every bay. Expect **21 members** with four bays and **36** with seven. Use `y` to change the height.

[Starter](exercises/01_truss_patterns.py) · [Worked solution](solutions/01_truss_patterns.py)

## Part 4 · Loft two sine profiles

Build a loft from a 12-unit guide line along X with a second guide offset 6 units along Y. Use a wave amplitude of 2 units.

1. Divide each guide into **48 segments**. Check for **49 points** on each guide, including both ends.
2. Change each point’s Z coordinate by amplitude times sine. Fit one complete cycle along the first guide and two along the second. At X = 3, the heights should be **2 and 0**.
3. Interpolate a curve through each point list, then loft the two profiles. Set amplitude to zero to check that the strip becomes flat. Change the gap on `x` and amplitude on `y`.

[Starter](exercises/02_sine_loft.py) · [Worked solution](solutions/02_sine_loft.py)

## Optional practice

Try each exercise in a fresh **Python 3 Script** component. Run the starter,
complete its TODO, and compare the result with the worked solution.

| Exercise | Check | Worked solution |
| --- | --- | --- |
| [Ramp centreline](optional/01_ramp_centreline_exercise.py) | A 6-unit run with a rise of 2 gives a length of 6.325. Set `x` to 0 to get 6. | [Solution](optional/02_ramp_centreline_solution.py) |
| [Three canopy profiles](optional/03_canopy_profiles_exercise.py) | At the default lift, the profiles have centre heights of 2, 3, and 2.5. Their ends sit at Z = 1. | [Solution](optional/04_canopy_profiles_solution.py) |
| [Canopy loft](optional/05_canopy_loft_exercise.py) | Loft one surface across the three supplied profiles from Y = 0 to Y = 8. Increase the lift on `x` and check that the middle of the roof rises. | [Solution](optional/06_canopy_loft_solution.py) |
