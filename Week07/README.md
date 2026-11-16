# W07 — Recursion and Spatial Systems

Build a recursive branching structure, add controlled variability to its
lengths and angles, then add one spatial influence: attraction toward a point.
Predict small results and compare the geometry after each change.

## Before you start

Use the existing `acd` environment with Shapely `2.0.7`, as described in
[W06](https://github.com/AdvancedComputationalDesign-SDU/ACD-Tutorials/blob/main/Week06/README.md).
Open a saved file in VS Code and select the `acd` interpreter.

Run the whole file, or run the `# %%` cells in order. Run the imports and
function definitions before their examples. If you change a function's inputs,
update its calls too. Close a plot to continue. Figures are saved in
`outputs/` inside the week folder. Shared plot limits make comparisons readable;
adjust them together if you change the design scale.

Comments give expected small results. Compare these with the printed values
and plots as you work through each stage.

Use the three-stage tutorial as the main route. The refreshers, separate
exercises and optional examples below support further practice.

## Tutorial files

Use the files in `tutorial/` in the order below. Start with small recursion
examples, then develop the branching starter. Open the solved version after
your own attempt.

| File | Use |
| --- | --- |
| [00_recursion_fundamentals.py](tutorial/00_recursion_fundamentals.py) | Small examples of calls, stopping conditions and returned results. |
| [01_recursion_trace.py](tutorial/01_recursion_trace.py) | Trace calls down to the base case and follow their returns. |
| [02a_branching_starter.py](tutorial/02a_branching_starter.py) | Your starting file: a working baseline and two TODO functions for randomization and attraction. |
| [02b_branching_solution.py](tutorial/02b_branching_solution.py) | The solved version: complete randomization, attraction and recursive integration, with all comparisons ready to run. |

Use `exercises/` for practice after the corresponding lesson stage and
`solutions/` after attempting each task. `references/` contains additional
worked demonstrations; `optional/` contains alternative representations and
further exploration. `tutorial/recursive_tools.py` supplies shared functions
for the reference examples and exercises.

The starter runs **only the baseline**. The Shapely endpoint, plotting
and baseline recursion are ready to use. `randomize_branch()` and
`attraction_heading()` have input/return contracts and TODO bodies; the baseline
does not call them yet.

Work through the steps below one at a time. Complete the TODO functions,
connect them to the recursive tree, then compare with the solved version.
Rerun from the top after editing a function.

The complete version defines each function once. It shows the baseline,
angle variability, angle-plus-length variability, then the same varied tree
with attraction. The seed, geometry settings and plot limits stay fixed
within each comparison. Each example calls `tree()` directly. The random seed,
generation, plotting and saving steps are visible below the function definitions.

## Work through the tutorial

### 1. Baseline recursive branching

Run the starter unchanged. Trace one call through the stop, current segment
and two child calls. Each child starts at its parent's tip, turns by
`+28` or `-28` degrees and uses `0.72` of its parent's length.

Try inclusive depths 0, 1 and 2: expect **1, 3 and 7 segments**.
Read the printed count and inspect where the child branches begin.
The function returns a fresh flat list of Shapely `LineString` objects.

### 2. Controlled variability in angle and length

Complete `randomize_branch()` first. It takes an angle, length and their
variation bounds, and returns a pair: `(varied_angle, varied_length)`.
With zero bounds, `(90,10)` should remain `(90,10)`. Bounds 5 and 0.08 allow
angles 85–95 degrees and lengths 9.2–10.8.

Add `angle_jitter=0.0` and `length_jitter=0.0` to `tree()`'s inputs. In the
child loop, pass the child angle and length to `randomize_branch()` and use
its two returned values. Pass the bounds into the recursive child calls too.
Zero defaults keep the existing baseline calls working.

The comparison examples reset `random.seed(SEED)` before each starting
`tree()` call. Keep the seed outside the recursive function. Compare angle
variability alone, then angle and length variability together. Repeat a run
to check that it reproduces the same geometry. Keep the largest possible child
shorter than its parent; the supplied maximum child-to-parent length ratio is
`0.72 * 1.08 = 0.7776`.

### 3. Attraction toward one point

After the varied tree works, complete `attraction_heading()`.
Inputs are an XY start, heading in degrees, a Shapely target `Point` and a
strength in `[0,1]`. Return the adjusted heading, preserving the input angle
when the start equals the target.

Check the response by itself. From `(0,0)`, heading `90`, toward `Point(10,0)`,
strengths `0`, `0.5` and `1` should return **90, 45 and 0 degrees**.

Add `target=None` and `strength=0.0` to `tree()`'s inputs. Apply the response
before constructing each segment, then pass the new inputs down the child
calls. Skip steering when no target is supplied. Compare strength 0 with 0.3,
keeping the seed and variation bounds fixed. Attraction changes direction;
it does not guarantee that a branch reaches the target.

## Recursion refreshers and exercises

[Function contracts and call frames](tutorial/00_recursion_fundamentals.py)
and [a small recursion trace](tutorial/01_recursion_trace.py) support the
lecture's recursion foundations. Read them if you need to revisit calls,
returns, progress or fresh state.

| Practice | Starter | Worked solution |
| --- | --- | --- |
| Base cases and returned values | [Shrinking chain](exercises/01_recursive_chain.py) | [Solution](solutions/01_recursive_chain.py) |
| Parent-relative child branches | [Tree exercise](exercises/02_parent_relative_tree.py) | [Solution](solutions/02_parent_relative_tree.py) |
| An isolated attraction response | [Heading exercise](exercises/03_attraction_heading.py) | [Solution](solutions/03_attraction_heading.py) |

Attempt an exercise before opening its solution. The tree exercise uses
`+/-30` degrees and length scale `0.7`; these are another simple branching
rule. The same state, stopping and continuity checks apply.

## Reference examples

Use these worked examples to compare individual controls and record results:

- [Tree depths](references/01_tree_stages.py) compares the root, children
  and descendants at small depths.
- [Seeded variability](references/02_seeded_variation.py) changes the
  angle bound first, then adds length variation.
- [Attraction](references/03_attraction.py) compares an isolated spatial
  response with the baseline.
- [Comparison and export](references/04_comparison_and_export.py) saves
  matching images and a JSON settings record.

The main lesson returns a list of `LineString` objects. These references use
`tutorial/recursive_tools.py`, which returns records containing a `geometry`
and its `depth`. Their supplied `build_design()` starts a fresh local
`random.Random(seed)` for each run; the main lesson instead resets
`random.seed(SEED)` before calling `tree()`. Both approaches use the same
branching geometry when their settings match.

## Optional examples

- [Recursive subdivision](optional/01_recursive_subdivision.py) partitions
  a region as an alternative to branching.
- Try the [adaptive subdivision exercise](optional/02_adaptive_subdivision_exercise.py)
  before its [worked solution](optional/03_adaptive_subdivision_solution.py).
- [Koch](optional/04_koch.py) and
  [Sierpinski](optional/05_sierpinski.py) retain classic recursive examples.
- [Clipping result types](optional/06_clipping.py) and
  [further recursive patterns](optional/07_recursive_patterns.py) extend
  the spatial-query and recursion foundations.

Keep the whole week folder when using these examples or the separate
exercises: they share `tutorial/recursive_tools.py`. Completing every optional
reference is not required.

## Independent explanation

Before adapting an example, state the intention, recursive state, stopping
conditions and child rules. Predict a small case, run it and inspect the
coordinates as well as the segment count.

Change one meaningful control at a time. Keep the seed and plot limits fixed,
compare the results and explain the effect of the spatial response. If a rule
prunes branches, check which random choices still correspond between runs.

## References

The examples adapt the existing ACD branching and fractal materials.
Shapely `rotate` and `translate` construct endpoints in degrees; `atan2`
converts the target direction into a bearing. Shapely's analysis is planar.

Further reading: [CMU recursion, part 1](https://www.kosbie.net/cmu/fall-19/15-112/notes/notes-recursion-part1.html),
[part 2](https://www.kosbie.net/cmu/fall-19/15-112/notes/notes-recursion-part2.html),
[Shapely manual](https://shapely.readthedocs.io/en/2.0.7/manual.html),
[Python functions](https://docs.python.org/3.9/tutorial/controlflow.html#defining-functions)
and [random numbers and seeds](https://docs.python.org/3.9/library/random.html).
