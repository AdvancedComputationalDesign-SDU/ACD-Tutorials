#! python 3
#r: numpy
"""Shape a canopy with one crest

The 12 × 8 roof starts at Z = 1. Write heightmap(U, V, amplitude) to give
the 9 × 5 source grid one crest at its centre and zero rise along all four
edges. Combine one sine arch along U and one along V. Return heights above
the base in the same array shape as U and V.

At the centre, the rise equals amplitude. The preview’s centre Z is 3 at
amplitude 2 and 5 at amplitude 4. The source boundary stays at Z = 1.

The starter previews the 45 flat source points. Complete the field to
preview the roof and its lifted source points. Input x sets amplitude.
"""
import numpy as np
import rhinoscriptsyntax as rs


def heightmap(U, V, amplitude):
    """Return heights above the base in model units."""
    print("TODO. Return a height array with the shape of U and V.")
    return None


def source_grid(U, V, H):
    """Map normalised U,V to a 12 by 8 footprint and lift the Z coordinates."""
    return np.stack((12.0 * U, 8.0 * V, 1.0 + H), axis=-1)


def interpolate_roof(grid):
    """Return an interpolating surface ID from the XYZ source grid."""
    nv, nu, _ = grid.shape
    ordered = [tuple(map(float, grid[j, i])) for i in range(nu) for j in range(nv)]
    return rs.AddSrfPtGrid((nu, nv), ordered, degree=(3, 3))


amplitude = 2.0 if x is None else float(x)
if not np.isfinite(amplitude):
    raise ValueError("Use a finite amplitude.")
# The source grid stays fixed when the panel density changes.
U, V = np.meshgrid(
    np.linspace(0, 1, 9),
    np.linspace(0, 1, 5),
    indexing="xy",
)
H = heightmap(U, V, amplitude)

if H is None:
    flat = source_grid(U, V, np.zeros_like(U))
    a = rs.AddPoints([tuple(map(float, point)) for row in flat for point in row])
else:
    grid = source_grid(U, V, H)
    roof = interpolate_roof(grid)
    xyz = [tuple(map(float, point)) for row in grid for point in row]
    a = [roof] + rs.AddPoints(xyz)
    print("Source grid", U.shape, "centre Z", round(float(grid[2, 4, 2]), 3))
