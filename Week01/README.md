# W01 — Variables, Expressions, and Program Execution

This folder introduces Python variables, expressions, types, and program
execution. Worked examples and exercises develop small calculations with explicit
inputs, units, and outputs, including conversion between text and numeric values.

## Work through the tutorial

Follow the numbered files in `tutorial/` alongside the lecture slides. Predict
what each section will do before running it. The file with the same name in
`exercises/` contains the task and full solution: read the task, sketch your own
approach, then compare it with the worked code.

Open `tutorial/01_variables_and_types.py` first. Each worked example and solution runs independently. Run the numbered sections within a file in order. Start a fresh Python session when changing files; do not depend on variables from an earlier topic. The plain `.py` files need no Jupyter installation.

Examples use fixed values. Where keyboard input is relevant, uncomment the adjacent `input()` line to replace the fixed value. Do not leave both alternatives active in a way that unintentionally overwrites the value you entered.

In VS Code, select the course interpreter, then use **Run Python File in Terminal**. To work section by section, select a complete section and use **Run Selection/Line in Python Terminal**. For file-based examples, run the supplied location setup first and open the repository root, this week folder, or its `tutorial/`, `exercises/`, or `optional/` folder.

## Topic order

| Topic | Relevant slide titles | Files |
|---|---|---|
| 01 — Variables and Types | RUNNING A PYTHON FILE; ALGORITHMS AND SEQUENCE; VARIABLES AND ASSIGNMENT; TYPES AND DYNAMIC TYPING | [Example](tutorial/01_variables_and_types.py) · [Worked exercise](exercises/01_variables_and_types.py) |
| 02 — Arithmetic and Units | NAMES AND UNITS; ARITHMETIC OPERATORS; EXERCISE: ARITHMETIC OPERATORS | [Example](tutorial/02_arithmetic_and_units.py) · [Worked exercise](exercises/02_arithmetic_and_units.py) |
| 03 — Input and Conversion | TYPE CONVERSION; INPUT AND OUTPUT; EXERCISE: INPUT AND TYPE CONVERSION | [Example](tutorial/03_input_and_conversion.py) · [Worked exercise](exercises/03_input_and_conversion.py) |

## Predictions and checks

### 01 — Variables and Types

Trace how names, values, and execution order determine a result.

**Check after attempting the exercise:** Stored area 12; recalculated area 16.0 (float).

### 02 — Arithmetic and Units

Translate a panel transport question into arithmetic with explicit units.

**Check after attempting the exercise:** Area 2.88 m²; perimeter 7.2 m; total 152.64 m²; 6 full racks and 5 panels. With 56: 7 and 0.

### 03 — Input and Conversion

Convert text input before using it in numerical expressions.

**Check after attempting the exercise:** The fixed inputs produce 7.0 m². Nonnumeric text causes ValueError; recovery is taught in W03.

## Independent explanation

Before adapting an example, state the intention, inputs and representation, operations, constraints, and how you will check the result. Predict one small case. Change a meaningful rule, inspect the result, and explain the difference to a partner.

**Ready to continue:** Explain why reassignment does not recompute a stored result; distinguish text input from a numeric value.

If you use AI assistance, specify the intended rule and verify the suggested code; being able to explain the result is part of the exercise.

## Optional exploration

The files in `optional/` extend the core topics. They are optional and do not
have matching exercise files.

- [01 — Numerical Details](optional/01_numerical_details.py)

## Study notes

Connect each program to the algorithm it represents: identify the inputs, put
operations in order, and describe the output. Complex numbers in the optional
reference file are not needed for the image assignment.

For the everyday-algorithm exercise, first write a sequence in plain language.
Add a decision with explicit alternatives and identify any repetition and its
stopping condition. For example, to prepare tea: obtain a cup, water, and tea;
heat the water; choose a teabag or an infuser; pour the water; steep for a chosen
duration; remove the tea; serve. Which instructions need quantities or conditions
to become precise enough for someone else to follow?
