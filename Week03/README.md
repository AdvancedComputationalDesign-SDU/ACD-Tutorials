# W03 — Iteration and Debugging

This folder covers iteration and debugging: for loops, nested loops,
comprehensions, dictionary iteration, while loops, and validation. The examples
and exercises develop repeated calculations, process panel records, and show how
to inspect state and diagnose incorrect results.

## Work through the tutorial

Follow the numbered files in `tutorial/` alongside the lecture slides. Predict
what each section will do before running it. The file with the same name in
`exercises/` contains the task and full solution: read the task, sketch your own
approach, then compare it with the worked code.

Open `tutorial/01_for_loops_and_iteration.py` first. Each file runs independently.
Run the numbered sections within a file in order. Start a fresh Python session
when changing files. The plain `.py` files need no Jupyter installation or input
data files.

Examples use fixed values. Where keyboard input is relevant, uncomment the
adjacent `input()` line to replace the fixed value. The debugging exercise keeps
its fixed reference checks and keyboard-input example in separate sections.
Try both invalid input and another valid width, such as `2.4`.

In VS Code, select the `acd` interpreter, then use **Run Python File in Terminal**.
To work section by section, select a complete section and use **Run Selection/Line
in Python Terminal**. Intentional error demonstrations stay commented. Run a
marked faulty snippet alone in a fresh session when investigating its traceback.

## Topic order

| Topic | Relevant slide titles | Files |
|---|---|---|
| 01 — For Loops and Iteration | FOR LOOPS; RANGE AND INDICES; VALUES AND LIST ELEMENTS; ENUMERATE; ZIP AND PAIRED DATA; ACCUMULATORS; ITERATING OVER DICTIONARIES | [Example](tutorial/01_for_loops_and_iteration.py) · [Worked exercise](exercises/01_for_loops_and_iteration.py) |
| 02 — Nested Loops and Comprehensions | MAPPING VALUES; FILTERING VALUES; REPLACING VALUES; NESTED LOOPS; TRAVERSING A NESTED LIST; BUILDING INDEPENDENT ROWS; LIST COMPREHENSIONS; EXERCISE: GRID AND COMPREHENSION; EXERCISE: FILTERING AND MAPPING | [Example](tutorial/02_nested_loops_and_comprehensions.py) · [Worked exercise](exercises/02_nested_loops_and_comprehensions.py) |
| 03 — While Loops and Control | WHILE LOOPS; BREAK AND CONTINUE; CHOOSING A LOOP; EXERCISE: WHILE LOOPS | [Example](tutorial/03_while_loops_and_control.py) · [Worked exercise](exercises/03_while_loops_and_control.py) |
| 04 — Debugging and Validation | TRACING A LOOP; ERRORS AND UNEXPECTED RESULTS; READING AN ERROR MESSAGE; DEBUGGING WITH BREAKPOINTS; ASSERTIONS AND VALIDATION; RAISING AN EXCEPTION; HANDLING INVALID INPUT; EXERCISE: PANEL DATA; EXERCISE: INPUT VALIDATION | [Example](tutorial/04_debugging_and_validation.py) · [Worked exercise](exercises/04_debugging_and_validation.py) |

## Predictions and checks

### 01 — For Loops and Iteration

Apply one rule to many values, and track the state accumulated by a loop.

**Check after attempting the exercise:** Areas 2.88, 3.6, 2.16, 4.32; paired areas
2, 6, 12; maxima 74, -1, None. Dictionary iteration visits keys; `items()` gives
the label and measurement together.

### 02 — Nested Loops and Comprehensions

Construct a grid and recognize when a comprehension expresses an existing loop more compactly.

**Check after attempting the exercise:** Grid [[0, 1, 2], [1, 2, 3]]; even squares
[4, 16, 36, 64, 100]; total 220. The larger grid is
[[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]]. Flattening it gives 12 values;
filtering those values for `value > 1` keeps 9.

### 03 — While Loops and Control

Make the changing state and termination condition explicit.

**Check after attempting the exercise:** 100-mm target: 108 mm and 9 layers; 96: 96 and 8; 0: 0 and 0.

### 04 — Debugging and Validation

Find a wrong result, then distinguish conversion failures from invalid numeric values.

**Check after attempting the exercise:** The faulty loop prints 6 for [2, 4, 6].
The corrected totals are 12, 4, 0. Of the six fixed input cases, only 1.2 is
accepted; conversion and range failures receive different messages. Other
positive finite widths are valid in the keyboard-input section.

For the lecture's panel records, skip C and collect areas [2, 6]. The total is
8 and the average is 4.0. With no valid panels, the total is 0 and the average is
None. Test both an empty list and a list containing only invalid panels.

## Independent explanation

Before adapting an example, state the intention, inputs and representation, operations, constraints, and how you will check the result. Predict one small case. Change a meaningful rule, inspect the result, and explain the difference to a partner.

**Ready to continue:** Trace a small loop, justify termination, iterate over
records, handle invalid text, and check an empty input.

If you use AI assistance, specify the intended rule and verify the suggested code; being able to explain the result is part of the exercise.

## Optional exploration

The files in `optional/` extend the core topics. They are optional and do not
have matching exercise files.

- [01 — Prime Check](optional/01_prime_check.py)

## Study notes

Write and trace an explicit loop before expressing the same operation as a list
comprehension. Distinguish filtering items from replacing values conditionally.
For a `while` loop, identify the state that changes and why the loop will stop.

When handling input errors, catch the specific exception you expect. A broad
`except Exception` can hide unrelated bugs. Read the traceback and inspect a
small failing case before changing code. A bare `raise` needs an active exception
to re-raise; use an explicit exception when signaling a new validation failure.
Assertions check development assumptions and can be disabled, so external input
needs explicit validation. Week 04 develops collections and records further.
