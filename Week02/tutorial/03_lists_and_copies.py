"""03 — Lists and Copies

Choose and edit sequences while tracking which objects share data.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

from copy import deepcopy

# --- 01: Lists are ordered and mutable; types may differ ---
record = ["P01", 2.4, True]
lengths = [2.4, 1.8, 3.0, 2.1]
print(record, lengths[0], lengths[-1], lengths[:3])
lengths[1] = 2.0
lengths.append(2.7)
print(lengths, len(lengths), 3.0 in lengths)

# --- 02: Common operations have different effects ---
labels = ["A", "B"]
labels.extend(["C", "D"])
labels.insert(1, "X")
labels.remove("X")  # Removes the first equal value.
removed = labels.pop()  # Removes and returns the last value.
print(labels, removed, labels.index("B"), labels.count("A"))
print([1, 2] + [3, 4], [0] * 3)
unsorted = [3, 1, 2]
ordered = sorted(unsorted)
print("New sorted list:", ordered, "Original:", unsorted)
result = unsorted.sort()
print("In-place sort:", unsorted, "Return:", result)  # None
unsorted.reverse()
print("Reversed:", unsorted)

# --- 03: Assignment and a flat copy ---
source = [1, 2]
alias = source
separate = source.copy()
print("Equal values:", source == separate, "Same object:", source is separate)
# Equal lists can be different objects.
alias[0] = 9
print(source, alias, separate)  # [9, 2], [9, 2], [1, 2]
print(source == alias, source is alias, source is separate)

# --- 04: A shallow copy still shares the inner lists ---
original = [[1, 2], [3, 4]]
alias = original
shallow = original.copy()
deep = deepcopy(original)
original[0][0] = 9
original.append([5, 6])
print("Alias:", alias)
print("Shallow:", shallow)
print("Deep:", deep)
# A shallow copy has its own outer list, but retains references to inner lists.
