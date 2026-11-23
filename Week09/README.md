# W09 — Panelize NURBS Surfaces

Generate a height field with NumPy, lift a flat XY grid along Z, interpolate a
NURBS surface, and sample it again to build regular NURBS quads and triangles.

## Run in Grasshopper

Use a **Rhino 8 Python 3 Script** component in Script mode. Paste the whole
script and keep the default `x`, `y`, `out`, and `a` ports. View geometry from
`a` and connect a Panel to `out`. Keep the `#r: numpy` line where it appears.

The [complete tutorial script](tutorial/01_heightmap_to_panels.py) defaults to
5 U and 3 V samples, producing 15 grid points and 8 NURBS quads. Use whole-number
sliders of at least 2 to change the counts. Keep one component's preview visible
at a time.

## Exercises

1. **Height field → surface.** Create a crest that returns to base level at
   all four boundaries. Build a 9 × 5 source grid over a 12 × 8 footprint with
   a base Z of 1. Use `x` for amplitude. At amplitude 2, the centre is at Z = 3.
   [Starter](exercises/01_heightmap_to_roof.py) · [Solution](solutions/01_heightmap_to_roof.py)
2. **Surface → regular UV grid.** Sample the same surface at equal UV fractions
   including both endpoints. Store V as rows with U across each row. At 3 × 2
   expect six XYZ points, and at 5 × 3 expect the middle point near (6, 4, 3).
   [Starter](exercises/02_sample_roof.py) · [Solution](solutions/02_sample_roof.py)
3. **UV grid → NURBS quads.** Trace the corners of each cell in cyclic order.
   At 3 × 2 the corner indices are `(0, 1, 4, 3)` and `(1, 2, 5, 4)`.
   Gather the four XYZ corners and call `rs.AddSrfPt` once per cell.
   [Starter](exercises/03_connect_panels.py) · [Solution](solutions/03_connect_panels.py)
4. **Quads → NURBS triangles.** Use the same four samples per cell. In the complete
   script, set `triangles = True` and then change `other_diagonal` to compare
   the two splits. At 5 × 3, both patterns give 16 triangular surfaces from
   the same 15 points. [Four-corner example](optional/01_quad_or_triangles.py)

## Optional comparisons

- **Density.** Compare 5 × 3 and 9 × 3 samples from the same viewpoint. Both
  use the same reference surface and produce 8 and 16 quads, respectively.

## Measure panel fit and planarity

Append the [diagnostics block](optional/02_panel_fit.py) to the complete tutorial script
with `triangles = False`. Keep `a` for the panels and add outputs `b`, `c`, `d`,
and `e` to the Python 3 component. Each list follows the panel order.

| Output | What it measures |
| --- | --- |
| `b` | Colours based on the centroid gap. Connect `a` and `b` to Custom Preview and turn off the script component's own preview. |
| `c` | **Centroid gap.** Find the area centroid with `rs.SurfaceAreaCentroid`. Find its closest UV on the reference surface, evaluate that UV, and measure the XYZ distance. |
| `d` | **Fourth-point gap.** Define a plane through the first three non-collinear corners with `rs.PlaneFromPoints`. Take the absolute perpendicular distance from the fourth corner to that plane. Zero within tolerance means the four corners are coplanar. A warped quad's reported gap depends on which corner you hold out. |
| `e` | **Maximum sampled gap.** Take the largest distance from the centroid and five interior UV samples on the panel to the reference surface. This can pick up gaps away from the centroid. It estimates fit from a few points. |

All distances use model units. Start with amplitude 0 and check that all three gap
outputs are near zero. Then set amplitude to 2 and the sample counts to 2 × 2
for a single quad. The four corners stay coplanar, while the surface rises away
from the panel. Return to 5 × 3 and compare where the centroid and sampled gaps
are largest.

For A3, use the centroid gap as your baseline as described in the brief.
If you also explore the sampled gap, keep the sample locations and tolerances
fixed across comparable runs. Use the fourth-point gap to discuss panel flatness.

[Grasshopper Python 3](https://developer.rhino3d.com/guides/scripting/scripting-gh-python/) · [RhinoScriptSyntax](https://developer.rhino3d.com/api/RhinoScriptSyntax/)
