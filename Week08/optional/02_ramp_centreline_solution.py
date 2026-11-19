#! python 3
"""Draw a line at Y = -4. Optional input x sets the rise."""
import rhinoscriptsyntax as rs


def make_line(rise):
    """Return the ID of a line with run 6 and the supplied rise."""
    return rs.AddLine((0, -4, 0), (6, -4, rise))


rise = 2.0 if x is None else float(x)
a = make_line(rise)
if a is not None:
    print("Line length", round(rs.CurveLength(a), 3))
