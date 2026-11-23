#! python 3
#r: numpy
"""Go from a height field to regular NURBS panels.

Optional inputs x = number of U samples and y = number of V samples.
Output a previews the panel surfaces. Output out reports counts and the first face.
"""
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


def quad_indices(nu, nv):
    """Return one cyclic face tuple per cell in row order."""
    faces = []
    for j in range(nv - 1):
        for i in range(nu - 1):
            a = j * nu + i
            faces.append((a, a + 1, a + nu + 1, a + nu))
    return faces


amplitude = 2.0
triangles = False
other_diagonal = False
u_count = 5.0 if x is None else float(x)
v_count = 3.0 if y is None else float(y)
if not all(count.is_integer() and count >= 2 for count in (u_count, v_count)):
    raise ValueError("Use whole sample counts of at least two in U and V.")
nu, nv = int(u_count), int(v_count)

# 1. Build the roof from height values.
# The source grid stays fixed when the panel density changes.
U, V = np.meshgrid(
    np.linspace(0, 1, 9),
    np.linspace(0, 1, 5),
    indexing="xy",
)
H = heightmap(U, V, amplitude)
source = source_grid(U, V, H)
roof = interpolate_roof(source)

# 2. Sample a new grid at uniform UV fractions.
grid = sample_roof(roof, nu, nv)
vertices = [point for row in grid for point in row]

# 3. Connect each cell in cyclic order.
faces = quad_indices(nu, nv)
if triangles:
    triangle_faces = []
    for p0, p1, p2, p3 in faces:
        if other_diagonal:
            triangle_faces.extend(((p0, p1, p3), (p1, p2, p3)))
        else:
            triangle_faces.extend(((p0, p1, p2), (p0, p2, p3)))
    faces = triangle_faces

a = [rs.AddSrfPt([vertices[i] for i in face]) for face in faces]
print(len(vertices), "vertices", len(faces), "NURBS panels")
print("First face", faces[0])
