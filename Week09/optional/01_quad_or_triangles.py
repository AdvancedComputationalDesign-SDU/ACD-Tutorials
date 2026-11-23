#! python 3
"""Compare faces in Grasshopper Python 3 or Rhino Script Editor."""
import rhinoscriptsyntax as rs


# Set triangles to True to split the quad along the 0–3 diagonal.
triangles = False
other_diagonal = False
vertices = [(0, 0, 0), (3, 0, 0), (0, 2, 0), (3, 2, 1)]
faces = [(0, 1, 3, 2)]
if triangles:
    faces = [(0, 1, 2), (1, 3, 2)] if other_diagonal else [(0, 1, 3), (0, 3, 2)]

a = [rs.AddSrfPt([vertices[i] for i in face]) for face in faces]
print(len(vertices), "vertices", len(faces), "NURBS panels")
print(faces)
