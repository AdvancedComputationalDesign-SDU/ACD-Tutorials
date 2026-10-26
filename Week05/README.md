# W05 — Array Operations and Visual Composition

This folder explores visual composition through array operations, coordinate
fields, masks, and RGB channels. Examples and exercises connect numerical image
construction with filtering and 2D and 3D visualization.

## Work through the tutorial

Follow the numbered files in `tutorial/` alongside the lecture slides. Predict
what each section will do before running it. The file with the same name in
`exercises/` contains the task and full solution: read the task, sketch your own
approach, then compare it with the worked code.

Open `tutorial/01_array_operations.py` first. Each worked example and solution runs independently. Run the numbered sections within a file in order. Start a fresh Python session when changing files; do not depend on variables from an earlier topic. The plain `.py` files need no Jupyter installation.

Examples use fixed values. Where keyboard input is relevant, uncomment the adjacent `input()` line to replace the fixed value. Do not leave both alternatives active in a way that unintentionally overwrites the value you entered.

In VS Code, select the course interpreter, then use **Run Python File in Terminal**. To work section by section, select a complete section and use **Run Selection/Line in Python Terminal**. For file-based examples, run the supplied location setup first and open the repository root, this week folder, or its `tutorial/`, `exercises/`, or `optional/` folder.

Close a plot window to continue when running a whole file. Figures are created by the code; saved results go under `outputs/`, never into the supplied data.

## Topic order

| Topic | Relevant slide titles | Files |
|---|---|---|
| 01 — Array Operations | ARRAY SLICING: ROWS AND COLUMNS; ARRAY SLICING: STEPS; SLICES: VIEWS AND COPIES; RESHAPING AND BROADCASTING | [Example](tutorial/01_array_operations.py) · [Worked exercise](exercises/01_array_operations.py) |
| 02 — Coordinate Fields and RGB | COORDINATE GRIDS; PIXEL INDICES AND COORDINATES; DISTANCE FIELDS; BOOLEAN MASKS; RGB CHANNELS; RANDOM ARRAY VALUES | [Example](tutorial/02_coordinate_fields_and_rgb.py) · [Worked exercise](exercises/02_coordinate_fields_and_rgb.py) |
| 03 — Image Processing | SCIKIT-IMAGE; IMAGE PROCESSING: SHARED INPUT; GAUSSIAN BLUR: COLOR CHANNELS; SOBEL AND CANNY EDGES | [Example](tutorial/03_image_processing.py) · [Worked exercise](exercises/03_image_processing.py) |
| 04 — RGB Composition | COMPOSITION: GRAYSCALE RINGS; COMPOSITION: TWO WAVE CENTERS; COMPOSITION: A SHIFTED ECHO; COMPOSITION: THE FINAL CROP | [Example](tutorial/04_rgb_composition.py) · [Worked exercise](exercises/04_rgb_composition.py) |
| 05 — 2D and 3D Visualization | FILLED CONTOURS; COMPOSITION: COLOR AND HEIGHT; COMPOSITION: 3-D SCATTER; COMPOSITION: 3-D WIREFRAME; COMPOSITION: 3-D SURFACE | [Example](tutorial/05_2d_and_3d_visualization.py) · [Worked exercise](exercises/05_2d_and_3d_visualization.py) |

## Predictions and checks

### 01 — Array Operations

Predict the selected values and result shape before turning array operations into an image.

**Check after attempting the exercise:** White pixel counts: 64, 256, 400. Two-pixel stripes cover 512 pixels.

### 02 — Coordinate Fields and RGB

Separate spatial coordinates, scalar values, selection masks, and color channels.

**Check after attempting the exercise:** RGB shape (80, 120, 3), finite values in [0, 1]; same seed reproduces the phase. X+Y changes band direction.

### 03 — Image Processing

Compare processing operations by the information they preserve or remove.

**Check after attempting the exercise:** All grayscale/filter arrays keep the image dimensions. Compare edge maps with the same maximum intensity.

### 04 — RGB Composition

Build a richer image through small, explainable changes while keeping boundary artifacts outside the final crop.

**Check after attempting the exercise:** Full canvas (512, 512, 3); final crop (320, 320, 3), finite in [0, 1]. The largest shift is 84 pixels.

### 05 — 2D and 3D Visualization

Compare representations of one composition while keeping coordinates, heights, and colors aligned.

**Check after attempting the exercise:** X/Y/Z sample shapes (80, 80); RGB (80, 80, 3). All views preserve the same coordinate/color correspondence.

## Independent explanation

Before adapting an example, state the intention, inputs and representation, operations, constraints, and how you will check the result. Predict one small case. Change a meaningful rule, inspect the result, and explain the difference to a partner.

**Ready to continue:** Explain the composition order, boundary treatment, random seed, RGB range, and the difference between array axes and display dimensions.

If you use AI assistance, specify the intended rule and verify the suggested code; being able to explain the result is part of the exercise.

## Optional exploration

The files in `optional/` extend the core topics. They are optional and do not
have matching exercise files.

- [01 — Boundary Rules](optional/01_boundary_rules.py)
- [02 — Additional Filters](optional/02_additional_filters.py)
- [03 — Noise and Attractors](optional/03_noise_and_attractors.py)

## Study notes

Work through the RGB composition, then develop a variation by changing one
spatial rule. Explain what you expect before running it. Additional filters,
noise, and attractor examples offer optional directions for exploration.

The main composition uses a larger canvas and crops once at the end. The red
box marks the future crop; it is not part of the exported image. Compare this
boundary treatment with wrapping in the optional reference example.

Generated fields use a lower origin; photographs use an upper origin. Check
that the displayed and saved images use the same orientation. In the 3D views,
intensity becomes height: this is a chosen visual mapping, not a physical
measurement. Keep coordinates, heights, and colors aligned when sampling.
