#! python 3
"""Loft one canopy surface

The three open profiles are supplied in order with corresponding ends. Write
loft_profiles(profiles) to create a loft through all three and return its
single surface ID. Report a clear error if the loft fails or creates more
than one surface.

The starter previews the three section curves. Once the loft works, look
for one surface spanning Y = 0 to Y = 8. Increase lift and check that
the middle of the roof rises.

Loft three matching profiles. Optional input x = profile lift.
"""
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
    print("TODO. Loft the ordered curves and return the single surface ID.")
    return None


lift = 2.0 if x is None else float(x)
profiles = make_profiles(lift)
surface = loft_profiles(profiles)
a = profiles if surface is None else surface
if surface is not None:
    print("Lofted", len(profiles), "ordered curves")
