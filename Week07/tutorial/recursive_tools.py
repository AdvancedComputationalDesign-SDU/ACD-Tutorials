"""W07 worked example: build a branching baseline, then add attraction.

Read generate_fractal() first: it has no spatial influence. The separate
generate_attracted_fractal() shows the same rule with one addition: turn the
heading toward a point before creating the current segment. Their similar
bodies make that change visible without introducing a general rule framework.

Coordinates are planar (x, y), headings are degrees counterclockwise from +x,
and depth counts upward: max_depth=0 includes the root segment.
Each record contains a Shapely LineString and its recursion depth.
"""

import math
import random

from shapely.affinity import rotate, translate
from shapely.geometry import LineString, Point


def endpoint(start_point, angle, length):
    """Return an XY tuple using Shapely rotation and translation (degrees)."""
    step = rotate(Point(length, 0), angle, origin=(0, 0))
    return translate(step, xoff=start_point[0], yoff=start_point[1]).coords[0]


def generate_fractal(start_point, angle, length, depth, params, rng):
    """Return this branch and its descendants as a new list of records.

    Stage 1: params holds the branching and variation settings.
    rng is created once by build_design(), then shared by the recursive calls.
    The recursive state is position, heading, length, and depth.
    """
    if depth > params["max_depth"] or length < params["min_length"]:
        return []

    end_point = endpoint(start_point, angle, length)
    candidate = LineString([start_point, end_point])
    records = [{"geometry": candidate, "depth": depth}]
    if depth == params["max_depth"]:
        return records

    for turn in (params["branch_angle"], -params["branch_angle"]):
        child_angle = angle + turn + rng.uniform(
            -params["angle_jitter"], params["angle_jitter"])
        child_length = length * params["length_scale"] * rng.uniform(
            1 - params["length_jitter"], 1 + params["length_jitter"])
        records.extend(generate_fractal(
            end_point, child_angle, child_length, depth + 1, params, rng))
    return records


def attraction_heading(start_point, angle, target, strength):
    """Return a heading turned partway toward target, in degrees.

    Inputs: XY start_point, current heading, Shapely Point target and
    strength in [0, 1]. Zero preserves the heading; one faces the target.
    At the target, preserve the heading because no direction is defined.
    """
    if not math.isfinite(strength) or not 0 <= strength <= 1:
        raise ValueError("Attraction strength must be between 0 and 1.")
    dx, dy = target.x - start_point[0], target.y - start_point[1]
    if dx == 0 and dy == 0:
        return angle
    bearing = math.degrees(math.atan2(dy, dx))
    turn = (bearing - angle + 180) % 360 - 180  # Shortest signed turn.
    return angle + strength * turn


def generate_attracted_fractal(start_point, angle, length, depth, params, rng,
                              target, strength):
    """Stage 2: return the same branching system with attraction only.

    The new inputs are a target Point and strength in [0, 1]. The output is
    still a fresh list of geometry/depth records. Stopping, child count,
    length scaling and randomness stay the same as the baseline.
    """
    if depth > params["max_depth"] or length < params["min_length"]:
        return []

    # The one geometric change: steer before constructing this segment.
    angle = attraction_heading(start_point, angle, target, strength)
    end_point = endpoint(start_point, angle, length)
    records = [{"geometry": LineString([start_point, end_point]), "depth": depth}]
    if depth == params["max_depth"]:
        return records

    for turn in (params["branch_angle"], -params["branch_angle"]):
        child_angle = angle + turn + rng.uniform(
            -params["angle_jitter"], params["angle_jitter"])
        child_length = length * params["length_scale"] * rng.uniform(
            1 - params["length_jitter"], 1 + params["length_jitter"])
        records.extend(generate_attracted_fractal(
            end_point, child_angle, child_length, depth + 1, params, rng,
            target, strength))
    return records


def build_design(params, target=None, attraction_strength=0.0):
    """Return a fresh seeded baseline, or add attraction when target is supplied."""
    if type(params["max_depth"]) is not int or not 0 <= params["max_depth"] <= 10:
        raise ValueError("Use integer max_depth from 0 to 10 (start small).")
    numeric_keys = ("angle", "length", "branch_angle", "length_scale",
                    "angle_jitter", "length_jitter", "min_length")
    if not all(math.isfinite(params[key]) for key in numeric_keys):
        raise ValueError("Numeric settings must be finite.")
    if len(params["start_point"]) != 2 or not all(
            math.isfinite(value) for value in params["start_point"]):
        raise ValueError("start_point must contain two finite coordinates.")
    if params["length"] <= 0 or params["min_length"] < 0:
        raise ValueError("Use positive initial length and nonnegative min_length.")
    if (params["length_scale"] <= 0 or params["angle_jitter"] < 0
            or not 0 <= params["length_jitter"] < 1):
        raise ValueError("Check length_scale and the jitter ranges.")
    if params["length_scale"] * (1 + params["length_jitter"]) >= 1:
        raise ValueError("This baseline uses child lengths smaller than the parent.")
    if not math.isfinite(attraction_strength) or not 0 <= attraction_strength <= 1:
        raise ValueError("Attraction strength must be between 0 and 1.")
    if target is None and attraction_strength != 0:
        raise ValueError("Supply a target Point for attraction.")
    rng = random.Random(params["seed"])
    if target is None:
        return generate_fractal(params["start_point"], params["angle"],
                                params["length"], 0, params, rng)
    return generate_attracted_fractal(params["start_point"], params["angle"],
                                     params["length"], 0, params, rng,
                                     target, attraction_strength)


def draw_result(ax, records, target=None):
    """Draw the records and an optional target marker; return None."""
    for record in records:
        x, y = record["geometry"].xy
        ax.plot(x, y, color="#244b43", linewidth=1)

    if target is not None:
        ax.scatter([target.x], [target.y], marker="+", color="#b24c39", s=70, zorder=3)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

def default_params():
    """Return fresh settings for each experiment."""
    return {"start_point": (0.0, 0.0), "angle": 90.0, "length": 40.0,
            "max_depth": 5, "branch_angle": 28.0, "length_scale": 0.72,
            "angle_jitter": 0.0, "length_jitter": 0.0,
            "min_length": 0.5, "seed": 42}


def signature(records):
    """Coordinates/depth let us compare geometry independently of its image."""
    return [(record["geometry"].wkt, record["depth"]) for record in records]
