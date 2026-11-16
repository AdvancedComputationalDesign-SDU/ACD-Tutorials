"""Further recursion patterns: searching, sorting and backtracking.

Trace how each function combines returned values or explores a choice.
"""
from pathlib import Path
from tempfile import TemporaryDirectory


def find_path(graph, start, goal, path=None):
    path = [] if path is None else path
    if start in path:
        return None
    current = path + [start]
    if start == goal:
        return current
    for neighbor in graph.get(start, []):
        answer = find_path(graph, neighbor, goal, current)
        if answer is not None:
            return answer
    return None




def list_paths(folder):
    """Read a directory tree; ignore symlinks to avoid cyclic traversal."""
    if folder.is_symlink():
        return []
    if folder.is_file():
        return [folder]
    files = []
    for child in sorted(folder.iterdir()):
        files.extend(list_paths(child))
    return files


def merge_sort(values):
    if len(values) < 2:
        return list(values)
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def quick_sort(values):
    if len(values) < 2:
        return list(values)
    pivot, rest = values[0], values[1:]
    low = [v for v in rest if v < pivot]
    high = [v for v in rest if v >= pivot]
    return quick_sort(low) + [pivot] + quick_sort(high)


def hanoi(count, source, target, spare):
    if count == 0:
        return []
    before = hanoi(count - 1, source, spare, target)
    after = hanoi(count - 1, spare, target, source)
    return before + [(source, target)] + after


def subsets(values):
    if not values:
        return [[]]
    smaller = subsets(values[1:])
    with_first = [
        [values[0]] + subset
        for subset in smaller
    ]
    return smaller + with_first


def permutations(values):
    if not values:
        return [[]]
    result = []
    for index, value in enumerate(values):
        rest = values[:index] + values[index + 1:]
        for order in permutations(rest):
            result.append([value] + order)
    return result


def subset_sum(values, target):
    """Nonnegative values only: their partial sums can safely prune overshoot."""
    if target == 0:
        return []
    if target < 0 or not values:
        return None
    used = subset_sum(
        values[1:], target - values[0])
    if used is not None:
        return [values[0]] + used
    return subset_sum(values[1:], target)


def queens(size, rows=()):
    """Tuple position is the column; stored value is the row."""
    col = len(rows)
    if col == size:
        return rows
    for row in range(size):
        if all(
            row != old and
            abs(row - old) != col - old_col
            for old_col, old in enumerate(rows)
        ):
            result = queens(size, rows + (row,))
            if result is not None:
                return result
    return None




if __name__ == "__main__":
    print("Backtracking path:", find_path({"S": ["X", "A"], "A": ["G"]}, "S", "G"))
    print("Subset choices:", subsets([1, 2]))
    print("Try another small input and explain each returned result.")
