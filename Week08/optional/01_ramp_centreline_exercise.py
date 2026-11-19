#! python 3
"""Draw a ramp centreline

A ramp starts at (0, −4, 0). It runs six units in +X and rises by a given
amount. Write make_line(rise) to calculate the end point and return the ID
of the straight centreline.

Hold the run fixed. At rise 2 the length is about 6.325. At rise 0 it is 6.

Draw a line at Y = -4. Optional input x sets the rise.
"""
import rhinoscriptsyntax as rs


def make_line(rise):
    """Return the ID of a line with run 6 and the supplied rise."""
    print("TODO. Use the two XYZ endpoints and return a line ID.")
    return None


rise = 2.0 if x is None else float(x)
a = make_line(rise)
if a is not None:
    print("Line length", round(rs.CurveLength(a), 3))
