# W04 — Collections, Arrays, Tables, and Plots

This folder develops a workflow from collections and numerical arrays to labeled
tables and plots. Examples and exercises use beam measurements to connect data
representation, cleaning, calculation, and visual comparison.

## Work through the tutorial

Follow the numbered files in `tutorial/` alongside the lecture slides. Predict
what each section will do before running it. The file with the same name in
`exercises/` contains the task and full solution: read the task, sketch your own
approach, then compare it with the worked code.

Open `tutorial/01_collections.py` first. Each worked example and solution runs independently. Run the numbered sections within a file in order. Start a fresh Python session when changing files; do not depend on variables from an earlier topic. The plain `.py` files need no Jupyter installation.

Examples use fixed values. Where keyboard input is relevant, uncomment the adjacent `input()` line to replace the fixed value. Do not leave both alternatives active in a way that unintentionally overwrites the value you entered.

In VS Code, select the course interpreter, then use **Run Python File in Terminal**. To work section by section, select a complete section and use **Run Selection/Line in Python Terminal**. For file-based examples, run the supplied location setup first and open the repository root, this week folder, or its `tutorial/`, `exercises/`, or `optional/` folder.

Close a plot window to continue when running a whole file. Figures are created by the code; saved results go under `outputs/`, never into the supplied data.

## Topic order

| Topic | Relevant slide titles | Files |
|---|---|---|
| 01 — Collections | DICTIONARIES; RECORDS AND NAMED FIELDS; SET OPERATIONS; STACKS AND QUEUES; CHOOSING A COLLECTION | [Example](tutorial/01_collections.py) · [Worked exercise](exercises/01_collections.py) |
| 02 — NumPy Arrays | ARRAYS VS. LISTS; ARRAY AXES AND IMAGE SHAPE; VIEWS AND COPIES; CALCULATIONS AND AGGREGATION | [Example](tutorial/02_numpy_arrays.py) · [Worked exercise](exercises/02_numpy_arrays.py) |
| 03 — Tabular Data | DATAFRAMES; LOAD DATA FROM EXCEL; NON-NUMERIC AND MISSING VALUES; SELECTING AND CHECKING DATA | [Example](tutorial/03_tabular_data.py) · [Worked exercise](exercises/03_tabular_data.py) |
| 04 — Plotting Measurements | FIGURES AND AXES; LABELS AND LINE SETTINGS; SCATTER PLOTS; MULTIPLE PLOTS; SAVING A FIGURE | [Example](tutorial/04_plotting_measurements.py) · [Worked exercise](exercises/04_plotting_measurements.py) |

## Predictions and checks

### 01 — Collections

Choose a collection based on how the algorithm accesses and updates its data.

**Check after attempting the exercise:** Areas [2, 6], total 8, average 4; invalid ID C. Stack removes C; queue removes A.

### 02 — NumPy Arrays

Represent regular numerical data with explicit axes, units, and a common dtype.

**Check after attempting the exercise:** Row means [0.002, 0.005] m; column maxima [0.004, 0.005, 0.006] m. Original first value remains 1.

### 03 — Tabular Data

Load a labeled measurement table, inspect it, and derive a comparison without overwriting the source.

**Check after attempting the exercise:** Columns x_m, a_mm, b_mm; no missing values. Largest difference ≈1.2 mm at x=2 and x=3 m; shape (6, 2).

### 04 — Plotting Measurements

Use the measurement question to choose and label a plot, then verify it against the numbers.

**Check after attempting the exercise:** Largest difference at 2 and 3 m. Interior B/A ratios are 1.5; do not divide by zero at the endpoints.

## Independent explanation

Before adapting an example, state the intention, inputs and representation, operations, constraints, and how you will check the result. Predict one small case. Change a meaningful rule, inspect the result, and explain the difference to a partner.

**Ready to continue:** Explain an array axis, inspect a DataFrame selection, and relate a labeled plot back to its source values.

If you use AI assistance, specify the intended rule and verify the suggested code; being able to explain the result is part of the exercise.

## Optional exploration

The files in `optional/` extend the core topics. They are optional and do not
have matching exercise files.

- [01 — Word Counts](optional/01_word_counts.py)
- [02 — Additional Plots](optional/02_additional_plots.py)

## Study notes

Review list copying and loops before starting the collection examples. Ask how
you need to access and update your data before choosing a structure.

Follow the beam measurements from NumPy arrays to a pandas table and labeled
plots. Check units and array axes at each step. The cleaning example changes an
in-memory copy so you can inspect missing or invalid values without altering
the supplied workbook. Word counts and additional chart types are optional.
