#! python 3
#r: numpy
"""Build the source roof. Optional input x = amplitude."""
import numpy as np
import rhinoscriptsyntax as rs


def heightmap(U, V, amplitude):
    """Return heights above the base in model units."""
    return amplitude * np.sin(np.pi * U) * np.sin(np.pi * V)


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

a = None
if H is not None:
    grid = source_grid(U, V, H)
    roof = interpolate_roof(grid)
    xyz = [tuple(map(float, point)) for row in grid for point in row]
    a = [roof] + rs.AddPoints(xyz)
    print("Source grid", U.shape, "centre Z", round(float(grid[2, 4, 2]), 3))
