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
    division_points = rs.DivideCurve(rail, segments)
    if not division_points or len(division_points) != segments + 1:
        raise ValueError("Expected both ends and one point per division.")

    lifted = []
    for index, point in enumerate(division_points):
        fraction = index / segments
        angle = 2.0 * math.pi * cycles * fraction
        height = amplitude * math.sin(angle)
        lifted.append((point.X, point.Y, point.Z + height))
    return lifted


def make_loft(first_row, second_row):
    """Return both interpolated curve IDs followed by the loft surface ID."""
    first_profile = rs.AddInterpCurve(first_row, degree=3)
    second_profile = rs.AddInterpCurve(second_row, degree=3)
    profiles = [first_profile, second_profile]
    surfaces = rs.AddLoftSrf(profiles)
    if not surfaces or len(surfaces) != 1:
        raise ValueError("Expected one surface lofted between the profiles.")
    return profiles + surfaces


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
