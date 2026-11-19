#! python 3
"""Loft three matching profiles. Optional input x = profile lift."""
import rhinoscriptsyntax as rs


def make_profiles(lift):
    """Return three matching curve IDs ordered from Y=0 to Y=8."""
    profiles = []
    for section_y, scale in ((0, 0.50), (4, 1.0), (8, 0.75)):
        points = [(section_x, section_y, 1.0 + lift * scale * h)
                  for section_x, h in ((0, 0), (3, 0.7), (6, 1), (9, 0.7), (12, 0))]
        profiles.append(rs.AddInterpCurve(points, degree=3))
    return profiles


def loft_profiles(profiles):
    """Pass ordered open curve IDs to the loft and return its surface ID."""
    surfaces = rs.AddLoftSrf(profiles)
    if not surfaces or len(surfaces) != 1:
        raise ValueError("Expected one loft surface from matching profiles.")
    return surfaces[0]


lift = 2.0 if x is None else float(x)
profiles = make_profiles(lift)
surface = loft_profiles(profiles)
a = profiles if surface is None else surface
if surface is not None:
    print("Lofted", len(profiles), "ordered curves")
