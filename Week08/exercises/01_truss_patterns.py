#! python 3
"""Build a parametric truss. Optional inputs x = bay count and y = height."""
import math
import rhinoscriptsyntax as rs


def make_nodes(width, height, bays):
    """Return bottom and top XYZ lists in the world XZ plane.

    bays counts intervals. Each row has bays+1 coordinates, ordered by X.
    These lists contain coordinates; no model objects are added here.
    """
    # TODO. Space bays + 1 corresponding nodes along the top and bottom.
    return None


def make_members(bottom, top, crossed=False):
    """Add chords, verticals and diagonals; return their line IDs.

    A left-half bay connects top[i] to bottom[i+1], and a right-half bay
    connects bottom[i] to top[i+1]. With an odd count, the mirrored pattern
    leaves the middle bay without a diagonal. With crossed=True, every
    bay receives both diagonals.
    """
    # TODO. Build the chords, verticals and the chosen diagonals.
    return None


width = 12.0
bays = 4 if x is None else int(x)
height = 3.0 if y is None else float(y)
crossed = False

rows = make_nodes(width, height, bays)
a = []
if rows is None:
    print("Complete make_nodes to lay out the truss.")
else:
    bottom, top = rows
    members = make_members(bottom, top, crossed)
    if members is None:
        a = rs.AddPoints(bottom + top)
        print("Complete make_members to connect the truss.")
    else:
        a = members
        print("Node count", len(bottom) + len(top))
        print("Member count", len(a))
