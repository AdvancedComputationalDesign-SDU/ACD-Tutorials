"""Function fundamentals: predict, run, explain, then test a small change.

ACD examples plus adaptations of CMU 15-112 Variables and Functions:
https://www.kosbie.net/cmu/fall-19/15-112/notes/notes-variables-and-functions.html
The double/cubed demonstrations and digit helpers adapt those teaching patterns.
Other examples match the completed W06 lecture. No extra libraries are needed.

This is a lesson script: run cells in order, including each definition and its
calls. Run imports first. Import geometry_tools.py when you need reusable
geometry helpers; importing this lesson also executes its demonstrations.
"""
import math
from decimal import Decimal, ROUND_HALF_UP


# %% Names refer to values. An expression produces a value; assignment binds it.
step = 3
step = step + 2
is_positive = step > 0
print("Names and expressions:", step, is_positive)  # 5, True
# A bare expression evaluates without displaying anything in a script.
# print(...) displays a value; assignment binds a name to a value.
print("Built-ins:", abs(-3), min(2, 5), max(2, 5), int(2.8))
print("Module function:", math.sqrt(9))  # 3.0


# %% Defining stores the function body. Calling executes it.
def session_label():
    return "Functions"


def scale_size(value, factor=2.0):
    return value * factor


def add_margin(value, margin=1.0):
    return value + margin


# Predict positional, keyword and omitted-argument calls before running.
label_function = session_label  # The function object; the body has not run.
print("No arguments:", label_function())  # Functions
print("Positional:", scale_size(3, 4))  # 12
print("Keyword:", scale_size(factor=4, value=3))  # 12
print("Default:", scale_size(3))  # 6.0
# Uncomment ONE at a time, read the TypeError, then comment it again:
# scale_size()             # Missing required value.
# scale_size(3, 4, 5)      # Too many arguments.
# scale_size(3, value=4)   # The value argument was supplied twice.


# %% Return supplies a value and immediately exits this call.
def positive_size(value):
    if value <= 0:
        return False
    return True
    # A statement here would never run.


def report_size(value):
    print("Displayed size:", value)
    # Falling off the end returns None. Printing does not return value.


def rectangle_size(width, height):
    return width * height, 2 * (width + height)


shown = report_size(3)
print("Returned by report_size:", shown)  # None
print("Early returns:", positive_size(0), positive_size(3))  # False, True
area, perimeter = rectangle_size(3, 2)
print("Tuple unpacking:", area, perimeter)  # 6, 10


# %% CMU adaptation: a returned value can be part of another expression.
def double(value):
    return 2 * value


def display_cube(value):
    print(value**3)  # Deliberate print-versus-return comparison.


def cubed(value):
    return value**3


print("Returned expression:", double(4) + 1)  # 9
printed_cube = display_cube(2)  # Displays 8, returns None.
print("Printed result:", printed_cube)  # None
print("Reusable result:", 2 * cubed(3))  # 54
# 2 * display_cube(3) would print 27 and then raise TypeError.
# A returned value is still produced when you do not print or assign it.


# %% Each call has its own local parameter binding.
def shift(value):
    value = value + 5
    return value


value = 3
print("Independent locals:", shift(value), shift(10), value)  # 8, 15, 3

DEFAULT_SCALE = 2


def scaled_with_global(value):
    return value * DEFAULT_SCALE  # A hidden dependency on a module-level name.


def scaled_explicitly(value, factor):
    return value * factor


print("Read module context:", scaled_with_global(3))  # 6
print("Explicit context:", scaled_explicitly(3, 4))  # 12

# Assignment inside a function normally makes that name local. Reading it
# before local assignment raises UnboundLocalError. Pass and return the state
# rather than introducing a global counter into a geometric calculation.


# %% Composition: the inner call returns before the outer call executes.
print("Nested calls:", scale_size(add_margin(3, 2), 2))  # 10
print("Changed order:", add_margin(scale_size(3, 2), 2))  # 8
# Trace: add_margin(3, 2) -> 5; scale_size(5, 2) -> 10.
# The second expression instead scales 3 to 6 before adding the margin.


# %% CMU adaptation: reuse a helper instead of duplicating a calculation.
def ones_digit(number):
    """Return the last digit of an integer's magnitude, including negatives."""
    return abs(number) % 10


def larger_ones_digit(first, second):
    return max(ones_digit(first), ones_digit(second))


print("Digit helpers:", larger_ones_digit(247, -183))  # 7
print("Negative input:", ones_digit(-183))  # 3
# The abs call makes the stated negative-input policy explicit.
# Practice: predict larger_ones_digit(-420, 56), then run it.


# %% A mutable default is created once when the definition executes.
def shared_labels(label, labels=[]):  # Deliberately broken teaching example.
    labels.append(label)
    return labels


def fresh_labels(label, labels=None):
    result = [] if labels is None else list(labels)
    result.append(label)
    return result


# The broken example is intentional. Watch the SECOND call.
print("Shared default, first:", shared_labels("A"))  # ['A']
print("Shared default, second:", shared_labels("B"))  # ['A', 'B']
print("Fresh defaults:", fresh_labels("A"), fresh_labels("B"))
# Rerunning this entire cell recreates the default list at def time.
# Rerunning only the calls keeps adding to the same broken default.


# %% A helper has a small contract: inputs, returned value and domain.
def rectangle_area(width, height):
    """Return area for nonnegative width/height; reject negative dimensions."""
    if width < 0 or height < 0:
        raise ValueError(
            "Dimensions must be nonnegative")
    return width * height


print("Area:", rectangle_area(3, 2))  # 6
print("Zero-area policy:", rectangle_area(0, 4))  # 0
# rectangle_area(-1, 2) raises ValueError under this stated contract.
# A Shapely polygon helper may require strictly positive dimensions instead.


# %% Numerical comparison: select tolerances for the units of your calculation.
def almost_equal(a, b, tolerance=1e-9):
    """An absolute tolerance helper, suitable for the units chosen here."""
    return abs(a - b) <= tolerance


print("Exact float comparison:", 0.1 + 0.2 == 0.3)  # False
print("Within tolerance:", math.isclose(
    0.1 + 0.2, 0.3, rel_tol=1e-9, abs_tol=1e-12))  # True
print("Near zero:", almost_equal(0.0, 1e-12))  # True
print("Round ties to even:", round(2.5), round(3.5))  # 2, 4
# Rounding policy and a geometric distance tolerance are separate decisions.


# %% Optional reference: an explicit decimal tie policy.
def round_half_away(value):
    """Optional: round to an integer, with exact decimal ties away from zero."""
    decimal_value = Decimal(str(value))
    return int(decimal_value.quantize(Decimal("1"), rounding=ROUND_HALF_UP))

print("Explicit tie policy:", round_half_away(2.5), round_half_away(-2.5))
# 3, -3: exact decimal ties go away from zero.

# Finish: explain one nested call, one returned value and one scope decision.
