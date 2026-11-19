#! python 3
"""Build three profile curves. Optional input x = profile lift."""
import rhinoscriptsyntax as rs


def make_profiles(lift):
    """Return three matching curve IDs ordered from Y=0 to Y=8."""
    profiles = []
    for section_y, scale in ((0, 0.50), (4, 1.0), (8, 0.75)):
        points = [(section_x, section_y, 1.0 + lift * scale * h)
                  for section_x, h in ((0, 0), (3, 0.7), (6, 1), (9, 0.7), (12, 0))]
        profiles.append(rs.AddInterpCurve(points, degree=3))
    return profiles


lift = 2.0 if x is None else float(x)
a = make_profiles(lift)
if a:
    print(len(a), "profiles from Y=0 to Y=8")
