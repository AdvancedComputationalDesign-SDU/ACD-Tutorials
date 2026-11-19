#! python 3
"""Build a parametric truss. Optional inputs x = bay count and y = height."""
import math
import rhinoscriptsyntax as rs


def make_nodes(width, height, bays):
    """Return bottom and top XYZ lists in the world XZ plane.

    bays counts intervals. Each row has bays+1 coordinates, ordered by X.
    These lists contain coordinates; no model objects are added here.
    """
    if type(bays) is not int or bays < 1:
        raise ValueError('Use an integer bay count of at least one.')
    if not all(math.isfinite(v) for v in (width, height)) or min(width, height) <= 0:
        raise ValueError('Use positive finite width and height.')
    spacing = width / bays
    bottom, top = [], []
    for i in range(bays + 1):
        bottom.append((i * spacing, 0.0, 0.0))
        top.append((i * spacing, 0.0, height))
    return bottom, top


def make_members(bottom, top, crossed=False):
    """Add chords, verticals and diagonals; return their line IDs.

    A left-half bay connects top[i] to bottom[i+1], and a right-half bay
    connects bottom[i] to top[i+1]. With an odd count, the mirrored pattern
    leaves the middle bay without a diagonal. With crossed=True, every
    bay receives both diagonals.
    """
    if len(bottom) != len(top) or len(bottom) < 2:
        raise ValueError('Use equally sized rows with at least two nodes each.')
    bays = len(bottom) - 1
    members = []
    for i in range(bays):
        members.append(rs.AddLine(bottom[i], bottom[i + 1]))
        members.append(rs.AddLine(top[i], top[i + 1]))
    for i in range(bays + 1):
        members.append(rs.AddLine(bottom[i], top[i]))
    middle = (bays - 1) / 2
    for i in range(bays):
        if crossed or i < middle:
            members.append(rs.AddLine(top[i], bottom[i + 1]))
        if crossed or i > middle:
            members.append(rs.AddLine(bottom[i], top[i + 1]))
    return members


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
