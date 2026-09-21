"""02 — Strings — Worked Exercise

1. From "ACD-E26", print the first/last characters, "ACD", and integer 26.
2. Clean " computational design ", make it uppercase, replace DESIGN with THINKING.
3. Print the final string and its character count; check the original is unchanged.
4. Format length_m = 2.4 with two decimal places and the unit m.

One worked solution, not the only possible algorithm.
Compare the steps and the explanation, not just the final values.
"""

label = "ACD-E26"
print(label[0], label[-1])
print(label[:3], int(label[-2:]))
original = " computational design "
cleaned = original.strip().upper()
changed = cleaned.replace("DESIGN", "THINKING")
print(changed, len(changed))
print("Original:", repr(original))
length_m = 2.4
print(f"Length: {length_m:.2f} m")
