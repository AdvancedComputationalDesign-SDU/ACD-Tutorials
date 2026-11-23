#! python 3
#r: numpy
"""Sample the fixed roof. Optional inputs x = U count and y = V count."""
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


def sample_roof(roof, nu, nv):
    """Return XYZ rows in V order, each with nu points in U order."""
    if min(nu, nv) < 2:
        raise ValueError("Use at least two samples in each direction.")
    grid = []
    for j in range(nv):
        row = []
        for i in range(nu):
            uv = i / (nu - 1), j / (nv - 1)
            u, v = rs.SurfaceParameter(roof, uv)
            row.append(rs.EvaluateSurface(roof, u, v))
        grid.append(row)
    return grid


amplitude = 2.0
u_count = 5.0 if x is None else float(x)
v_count = 3.0 if y is None else float(y)
if not all(count.is_integer() and count >= 2 for count in (u_count, v_count)):
    raise ValueError("Use whole sample counts of at least two in U and V.")
nu, nv = int(u_count), int(v_count)
# The source grid stays fixed when the panel density changes.
U, V = np.meshgrid(
    np.linspace(0, 1, 9),
    np.linspace(0, 1, 5),
    indexing="xy",
)
H = heightmap(U, V, amplitude)
roof = interpolate_roof(source_grid(U, V, H))

grid = sample_roof(roof, nu, nv)
a = None
if grid is not None:
    a = rs.AddPoints([point for row in grid for point in row])
    print(nv, "rows of", nu, "points")
    if nu % 2 == 1 and nv % 2 == 1:
        centre = grid[nv // 2][nu // 2]
        xyz = tuple(round(value, 3) for value in (centre.X, centre.Y, centre.Z))
        print("Centre XYZ", xyz)
