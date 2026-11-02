# W06 — Functions, Modules and Shapely

Package a familiar calculation in a function, reuse it from a module, and use
planar geometry to answer a precise spatial question. These tools prepare the
recursive systems in W07 and Assignment 2.

## Before class

Use the existing `acd` interpreter in VS Code. Shapely is the one new library:

~~~sh
conda activate acd
python -m pip install "shapely==2.0.7"
python -c "import shapely; print(shapely.__version__)"
~~~

New environments created with the repository's `environment.yml` include it.
See the [course pip guide](https://github.com/AdvancedComputationalDesign-SDU/ACD-Reference/blob/main/dev_tools/pip/README.md)
if your terminal and VS Code use different interpreters. Keep the course Python
version. No additional plotting font is required.

## Class session and tutorial coverage

The session runs **12:15–15:45**, including tutorial practice and two
10-minute breaks. Short demonstrations alternate with your edits and checks.

- Start with [Function fundamentals](tutorial/00_function_fundamentals.py):
  definitions/calls, argument binding, returns, scope, safe defaults, helper
  functions, nested calls and numerical comparison.
- Tutorials 01–02 apply functions and modules to a familiar field.
- Tutorials 03–04 construct and measure Shapely geometry, then transform a motif.
- Tutorials 05–06 use geometric queries and combine functions in a composition.

Attempt the four exercise starters before their separate solutions. Save a
composition with one deliberate change and explain a checked spatial decision.
The first break follows the scope/defaults block; the second follows the
known-geometry check. The final part of class includes independent practice.

Further reading: [CMU variables and functions](https://www.kosbie.net/cmu/fall-19/15-112/notes/notes-variables-and-functions.html).
Tutorial 00 includes attributed adaptations of the CMU `double`/`cubed`
print-versus-return examples and digit helper composition. Predict each result
before running its cell. The digit helper explicitly handles negative integers.
The examples here follow the course's Python naming style and use explicit
floating-point tolerances. The optional final section shows a decimal rounding
policy; it does not change geometric precision requirements.

## Work through the tutorial

Run complete files independently with **Run Python File in Terminal**. To run
selected sections, execute the imports and supplied location setup first, then
run each complete function definition before calling it. Start a fresh Python
session for a new topic. Keep the whole week folder, including
`tutorial/geometry_tools.py`. The location setup supports the repository root,
the week folder, and its `tutorial/`, `exercises/`, `solutions/`, or `optional/`
folder. Close each plot window to continue. Saved images go into `outputs/`.

Tutorial 00 is a lesson script with definitions and calls together in `# %%`
cells. Run its import cell first and then work in order. Its deliberately
broken mutable-default example is labelled; rerunning only its calls retains
the shared list. The commented error examples are disabled so a complete run
finishes normally. Use `geometry_tools.py` as the importable helper module.

| Order | Lecture topics | Tutorial | Exercise and worked solution |
| --- | --- | --- | --- |
| 00 | Function fundamentals and numerical helpers | [Fundamentals](tutorial/00_function_fundamentals.py) | Predict the small examples, then continue with task 01 |
| 01 | Greeting examples, definition/call, arguments, defaults, return/print, the familiar field | [Functions](tutorial/01_functions.py) | [Task](exercises/01_returns_and_scope.py), [solution](solutions/01_returns_and_scope.py) |
| 02 | Returned inertia example, local names, mutation/copies, composition, modules | [Scope and modules](tutorial/02_scope_and_modules.py), [module](tutorial/geometry_tools.py) | Revisit task 01 and explain the unchanged caller variable |
| 03 | Point, LineString, Polygon, box, length/area/bounds | [Geometry](tutorial/03_shapely_geometry.py) | [Task](exercises/02_geometry_properties.py), [solution](solutions/02_geometry_properties.py) |
| 04 | Scale, rotation origin, translation, returned geometry | [Transformations](tutorial/04_transformations.py) | [Task](exercises/03_transform_a_motif.py), [solution](solutions/03_transform_a_motif.py) |
| 05 | Whole-segment queries, distance, intersects, covers/contains | [Spatial queries](tutorial/05_spatial_queries.py) | [Task](exercises/04_candidate_clearance.py), [solution](solutions/04_candidate_clearance.py) |
| 06 | Functions working together in a composition | [Composition](tutorial/06_functional_composition.py) | Choose a new motif or change one parameter and compare |

Exercises are separate from solutions this week. Their supplied files run and
print the task while unfinished functions return `None`. Replace each TODO,
add a known-input check, then compare your approach with the worked solution.
The solutions show one valid policy, rather than the only possible design.

The retained modules warm-up asks you to write `chop` and `middle`, move them
into a module, and compare the caller's list before and after each call. Use
`[0,1,2,3]` as a known case. Tutorial 02 and the helper module contain the worked
check after your attempt. The greeting, inertia, composition and geometry
slides reuse existing course examples in the current slide theme.

## Predictions and checks

- The wrapped field matches the W05 expression. At `(0,0)` it returns `0.5`.
- A function without an explicit return gives `None`. Assign a returned value
  when a later calculation needs it.
- The route through `(0,0), (3,0), (3,4)` has length `7`. The triangle with
  vertices `(0,0), (3,0), (0,2)` has area `3`.
- Uniform scale `0.5` multiplies area by `0.25`. Rotation changes according to
  its origin. Store the geometry returned by a transformation.
- A segment can cross a region even when both endpoints lie outside.
  `intersects` includes contact. A boundary point gives `contains=False` and
  `covers=True`. Distance is an unsigned scalar, with zero for contact/overlap.
- A query reports a relationship. A design rule decides what to change.

Before leaving, write a function with explicit inputs and a returned result,
import a helper, and explain one spatial decision using a known geometry.

## Closing design study

Run tutorial 06 unchanged first and inspect the saved comparison. Then change
one control or edit the local triangle in `geometry_tools.make_motif`. Keep the
placement grid and axes fixed, save your comparison under a new filename, and
explain which function caused the geometric change. Check that the returned
motifs remain independent objects and keep the local transform origin visible.
This is practice with functions and composition; recursion follows in W07.

## Reference and reuse

Adapted from the course functions/Shapely lecture and the historical
`dev_oz:week07/week07_demo.py` examples. W05 supplies the familiar field context.
Consult the [Shapely manual](https://shapely.readthedocs.io/en/2.0.7/manual.html),
[Python functions](https://docs.python.org/3.9/tutorial/controlflow.html#defining-functions)
and [Python modules](https://docs.python.org/3.9/tutorial/modules.html).
