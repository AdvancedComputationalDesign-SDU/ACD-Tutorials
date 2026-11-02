"""Small reusable calculations for W06. Importing this module draws nothing."""

import math
import numpy as np
from shapely.affinity import rotate, scale, translate
from shapely.geometry import Polygon


def ring_field(x, y, frequency=4.0):
    """Return values in [0, 1] for scalar or array coordinates."""
    distance = np.sqrt(x**2 + y**2)
    return 0.5 + 0.5 * np.sin(frequency * np.pi * distance)


def endpoint(start_point, angle, length):
    """Return an (x, y) endpoint. Angle is degrees from the positive x axis."""
    radians = math.radians(angle)
    return (start_point[0] + length * math.cos(radians),
            start_point[1] + length * math.sin(radians))


def compute_inertia(width, height):
    """Return the rectangular area second moment about its centroidal axis.

    Reused lecture example: width and height in metres give a result in m**4.
    This isolated section property does not establish structural performance.
    """
    inertia = width * height**3 / 12
    return inertia


def chop(items):
    """Legacy warm-up: mutate a list of at least two items, returning None."""
    del items[0]
    del items[-1]


def middle(items):
    """Legacy warm-up: return a new shallow list without its two end items."""
    return items[1:-1]


def make_motif(x, y, angle=0.0, size=1.0):
    """Scale and rotate a local triangle about (0, 0), then place it."""
    local = Polygon([(0, 0), (1, 0), (0.25, 0.6)])
    sized = scale(local, xfact=size, yfact=size, origin=(0, 0))
    turned = rotate(sized, angle, origin=(0, 0))
    return translate(turned, xoff=x, yoff=y)


def accepts_candidate(candidate, obstacle, clearance=0.0):
    """Reject touching/crossing, then require at least the requested gap.

    A zero clearance still rejects touching. Distance alone cannot distinguish
    contact from overlap because both return zero.
    """
    if clearance < 0:
        raise ValueError("clearance must be nonnegative")
    return (not candidate.intersects(obstacle)
            and candidate.distance(obstacle) >= clearance)
