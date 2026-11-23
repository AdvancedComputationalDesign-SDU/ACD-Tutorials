# Append to the complete tutorial script with triangles = False.
# Keep output a. Add b for colours, c for centroid gaps, d for fourth-point
# gaps, and e for maximum sampled gaps. All distances use Rhino model units.
from System.Drawing import Color


def distance_to_surface(surface, point):
    """Return the distance from an XYZ point to the closest surface point."""
    u, v = rs.SurfaceClosestPoint(surface, point)
    closest = rs.EvaluateSurface(surface, u, v)
    return rs.Distance(point, closest)


color_limit = 0.40
sample_uv = [(0.5, 0.5), (0.25, 0.25), (0.75, 0.25),
             (0.75, 0.75), (0.25, 0.75)]
colors, centroid_gaps, planarity_gaps, sampled_gaps = [], [], [], []

for panel, face in zip(a, faces):
    # Fit: measure from the area centroid to the reference surface.
    centroid, _ = rs.SurfaceAreaCentroid(panel)
    centroid_gap = distance_to_surface(roof, centroid)
    centroid_gaps.append(centroid_gap)

    # Planarity: use three corners to define a plane, then check the fourth.
    p0, p1, p2, p3 = [vertices[i] for i in face]
    plane = rs.PlaneFromPoints(p0, p1, p2)
    if plane is None:
        raise ValueError("The first three corners do not define a plane.")
    planarity_gaps.append(abs(rs.DistanceToPlane(plane, p3)))

    # Sample the panel itself. Corners already lie on the reference surface.
    distances = [centroid_gap]
    for uv in sample_uv:
        u, v = rs.SurfaceParameter(panel, uv)
        point = rs.EvaluateSurface(panel, u, v)
        distances.append(distance_to_surface(roof, point))
    sampled_gaps.append(max(distances))

    t = min(centroid_gap / color_limit, 1)
    colors.append(Color.FromArgb(round(48 + 180 * t),
                                 round(141 - 62 * t),
                                 round(189 - 128 * t)))

b, c, d, e = colors, centroid_gaps, planarity_gaps, sampled_gaps
print(f"Largest centroid gap: {max(c):.3f}")
print(f"Largest fourth-point gap: {max(d):.3f}")
print(f"Largest sampled gap: {max(e):.3f}")
print(f"Centroid colours from blue at 0 to orange at {color_limit:g} or above")
