"""Recursive reasoning with small, testable examples before planar geometry.

Original ACD examples. See the linked CMU recursion notes for further reading.
Use small inputs to trace the recursive calls and returned values.
"""


def sum_values(values):
    """Wrapper: keep the public input simple and initialize the helper state."""
    return sum_from(values, 0)


def sum_from(values, index):
    if index == len(values):
        return 0
    return values[index] + sum_from(values, index + 1)


def trace_sum(lo, hi, depth=0):
    indent = "  " * depth
    print(f"{indent}call [{lo}, {hi}]")
    if lo > hi:
        result = 0
    else:
        rest = trace_sum(lo + 1, hi, depth + 1)
        result = lo + rest
    print(f"{indent}return {result}")
    return result


def sum_to(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError(
            "n must be a nonnegative integer")
    if n == 0:
        return 0
    return n + sum_to(n - 1)


def integer_power(base, exponent):
    """Integer exponents; zero to a negative power is not defined."""
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / integer_power(base, -exponent)
    return base * integer_power(base, exponent - 1)


def interleave(first, second):
    if not first:
        return list(second)
    if not second:
        return list(first)
    rest = interleave(first[1:], second[1:])
    return [first[0], second[0]] + rest


def sum_halves(values):
    if not values:
        return 0
    if len(values) == 1:
        return values[0]
    mid = len(values) // 2
    left = sum_halves(values[:mid])
    right = sum_halves(values[mid:])
    return left + right


def sum_iterative(values):
    total = 0
    for value in values:
        total += value
    return total


def sum_accumulated(values):
    return accumulate_from(values, 0, 0)


def accumulate_from(values, index, total):
    if index == len(values):
        return total
    return accumulate_from(
        values, index + 1, total + values[index])


def leaf_labels(node):
    """A nested dict is a branch; any other value is a leaf label."""
    if not isinstance(node, dict):
        return [node]
    result = []
    for child in node.values():
        result.extend(leaf_labels(child))
    return result




if __name__ == "__main__":
    print("Trace a sum from 2 to 4:")
    assert trace_sum(2, 4) == 9
    print("Wrapper result:", sum_values([2, 3, 4]))
    print("Two recursive calls:", sum_halves([2, 3, 4]))
    print("Unequal lists:", interleave([1], [10, 20]))
    print("Nested leaves:", leaf_labels({"left": [1, 2], "right": "tip"}))
    print("Try another small input before increasing the depth.")
    # Practice: draw the pending additions for sum_from([2, 3], 0).
    # Predict the empty input, one-item input and two consecutive calls.
    # Compare the iterative and recursive results before increasing input size.
