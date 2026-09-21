# W02 — Decisions and Sequences

This folder covers decisions and ordered data: conditions, strings, lists, and
tuples. The examples and exercises show how to select values, describe alternatives,
and distinguish a copied collection from shared data.

## Work through the tutorial

Follow the numbered files in `tutorial/` alongside the lecture slides. Predict
what each section will do before running it. The file with the same name in
`exercises/` contains the task and full solution: read the task, sketch your own
approach, then compare it with the worked code.

Open `tutorial/01_logic_and_conditionals.py` first. Each worked example and solution runs independently. Run the numbered sections within a file in order. Start a fresh Python session when changing files; do not depend on variables from an earlier topic. The plain `.py` files need no Jupyter installation.

Examples use fixed values. In `exercises/01_logic_and_conditionals.py`, uncomment the `input()` line to enter a different area. Enter numeric text; handling invalid input is covered in Week 03.

In VS Code, select the course interpreter, then use **Run Python File in Terminal**. To work section by section, select a complete section and use **Run Selection/Line in Python Terminal**. These examples use only the Python standard library and need no data files or path setup.

## Topic order

| Topic | Relevant slide titles | Files |
|---|---|---|
| 01 — Logic and Conditionals | COMPARISON OPERATORS; LOGICAL OPERATORS; BRANCH ORDER AND BOUNDARIES; EXERCISE: CONDITIONALS | [Example](tutorial/01_logic_and_conditionals.py) · [Worked exercise](exercises/01_logic_and_conditionals.py) |
| 02 — Strings | STRINGS; INDEXING AND SLICING; STRING METHODS; FORMATTED STRINGS | [Example](tutorial/02_strings.py) · [Worked exercise](exercises/02_strings.py) |
| 03 — Lists and Copies | LISTS; COMMON STRING AND LIST OPERATIONS; NESTED LISTS; REFERENCES AND COPIES; SHALLOW COPIES; DEEP COPIES | [Example](tutorial/03_lists_and_copies.py) · [Worked exercise](exercises/03_lists_and_copies.py) |
| 04 — Tuples and Unpacking | TUPLES; UNPACKING SEQUENCES; EXERCISE: TUPLES AND UNPACKING | [Example](tutorial/04_tuples_and_unpacking.py) · [Worked exercise](exercises/04_tuples_and_unpacking.py) |

## Predictions and checks

### 01 — Logic and Conditionals

Express a rule as Boolean conditions, then choose the matching branch.

**Check after attempting the exercise:** The four checks are True. Area 2.88 is Medium. Areas -1.0, 0.0, 1.5, 2.0, 4.9, and 5.0 produce Invalid, Invalid, Small, Medium, Medium, and Large.

### 02 — Strings

Treat text as an immutable sequence and make deliberate cleaning choices.

**Check after attempting the exercise:** A, 6; ACD, 26; COMPUTATIONAL THINKING has 22 characters; formatted length is 2.40 m.

### 03 — Lists and Copies

Choose and edit sequences while tracking which objects share data.

**Check after attempting the exercise:** List length 5; alias gains the new row, shallow does not, and deep keeps the original inner values.

### 04 — Tuples and Unpacking

Use a fixed coordinate record and unpack its components by position.

**Check after attempting the exercise:** Original (2.0, 5.0); shifted (5.0, 4.0); a trailing comma makes the one-item tuple.

## Independent explanation

Before adapting an example, state the intention, inputs and representation, operations, constraints, and how you will check the result. Predict one small case. Change a meaningful rule, inspect the result, and explain the difference to a partner.

**Ready to continue:** Classify a boundary value, explain a slice, and predict which nested structure changes after an edit.

If you use AI assistance, specify the intended rule and verify the suggested code; being able to explain the result is part of the exercise.

## Study notes

Use the list examples to distinguish equality (`==`, equal values) from identity
(`is`, the same object). Before modifying a nested list, predict what an alias,
a shallow copy, and a deep copy will contain afterward. Focus on which objects
are shared; you do not need to know how `deepcopy` is implemented yet.

Week 03 builds on these sequences by processing their items with loops.
