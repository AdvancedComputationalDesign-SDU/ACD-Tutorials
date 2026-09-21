"""03 — Lists and Copies — Worked Exercise

1. In [2.4, 1.8, 3.0, 2.1], replace the second value with 2.0 and append 2.7.
   Print the first/last values, first three values, and updated length.
2. Create an alias, a shallow copy, and a deep copy of [[1, 2], [3, 4]].
3. Change the original's first inner value to 9, then append [5, 6] to the original.
4. Predict and print the alias and both copies. Explain the shared inner list.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

from copy import deepcopy

lengths = [2.4, 1.8, 3.0, 2.1]
lengths[1] = 2.0
lengths.append(2.7)
print(lengths[0], lengths[-1], lengths[:3], len(lengths))
original = [[1, 2], [3, 4]]
alias = original
shallow = original.copy()
deep = deepcopy(original)
original[0][0] = 9
original.append([5, 6])
print("Alias:", alias)      # [[9, 2], [3, 4], [5, 6]]
print("Shallow:", shallow)  # [[9, 2], [3, 4]]
print("Deep:", deep)        # [[1, 2], [3, 4]]
# Only alias shares the outer list; shallow shares existing inner lists.
