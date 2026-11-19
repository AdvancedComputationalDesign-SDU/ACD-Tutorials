#! python 3
"""Build three canopy sections

Place sections at Y = 0, 4 and 8. Each curve passes through points at X = 0,
3, 6, 9 and 12. Start both ends at Z = 1. The centre rises 0.5 × lift, 1 ×
lift and 0.75 × lift above Z = 1 on the three sections, in that order. Make
each shoulder 70% of its section’s centre rise. Write make_profiles(lift) to
return the curve IDs in increasing Y.

At lift 2, the end heights are all 1 and the three centre heights are 2, 3
and 2.5.

Build three profile curves. Optional input x = profile lift.
"""
import rhinoscriptsyntax as rs


def make_profiles(lift):
    """Return three matching curve IDs ordered from Y=0 to Y=8."""
    print("TODO. Build three profile curves from ordered point lists.")
    return None


lift = 2.0 if x is None else float(x)
a = make_profiles(lift)
if a:
    print(len(a), "profiles from Y=0 to Y=8")
