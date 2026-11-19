#! python 3
"""Loft a wavy strip from two straight guide lines.

Keep the default Grasshopper Python 3 ports. Plug the separation along Y into
x and the wave amplitude into y. With both inputs unwired, the values are 6
and 2. The span is 12 units in X and both rails have 48 equal segments.

The first profile makes one complete cycle across the span. The second makes
two. Their endpoints return to Z = 0. At X = 3, the first profile reaches the
amplitude and the second crosses Z = 0. Set amplitude to zero to check the
flat strip.
"""
import math

import rhinoscriptsyntax as rs


def wave_points(rail, segments, cycles, amplitude):
    """Divide the rail and return lifted XYZ tuples in increasing X order."""
    # TODO 1: Divide the rail into segments. From each sample index, find
    # its fraction of the span and the sine angle for the requested cycles.
    # Keep X and Y and add amplitude times the sine to Z.
    return None


def make_loft(first_row, second_row):
    """Return both interpolated curve IDs followed by the loft surface ID."""
    # TODO 2: Interpolate one curve through each row. Pass the two curve IDs
    # to the loft in the same X direction, then return the preview objects.
    return None


length = 12.0
segments = 48
gap = 6.0 if x is None else float(x)
amplitude = 2.0 if y is None else float(y)
if not math.isfinite(gap) or gap <= 0:
    raise ValueError("Use a positive, finite separation in Y.")
if not math.isfinite(amplitude):
    raise ValueError("Use a finite amplitude.")

first_rail = rs.AddLine((0, 0, 0), (length, 0, 0))
second_rail = rs.CopyObject(first_rail, (0, gap, 0))

first_row = wave_points(first_rail, segments, 1, amplitude)
second_row = wave_points(second_rail, segments, 2, amplitude)
a = [first_rail, second_rail]

if first_row is None or second_row is None:
    print("Complete wave_points to lift the division points.")
else:
    quarter = segments // 4
    print(f"{len(first_row)} and {len(second_row)} samples")
    print(f"At X = 3, Z = {first_row[quarter][2]:.3f} and {second_row[quarter][2]:.3f}")
    geometry = make_loft(first_row, second_row)
    if geometry is None:
        a = rs.AddPoints(first_row + second_row)
        print("Complete make_loft to connect the profiles.")
    else:
        a = geometry
