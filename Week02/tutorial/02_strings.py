"""02 — Strings

Treat text as an immutable sequence and make deliberate cleaning choices.
Run the numbered sections in order. Each file starts independently.
Fixed inputs make results repeatable; input() alternatives stay commented.
"""

# --- 01: Quote marks delimit the string, not its contents ---
material = 'timber'
same_material = "timber"
description = """First line
Second line"""
print(material == same_material)
print(description)  # Triple quotes can contain literal line breaks.
print("First\nSecond")
print(r"C:\course\data")  # Raw strings preserve these backslashes.

# --- 02: Index, slice, and test membership ---
label = "ACD-E26"
print(label[0], label[-1])
print(label[:3], label[-2:], int(label[-2:]))
print("E26" in label, len(label))
# label[0] = "B" would fail: strings are immutable.

# --- 03: Methods return new strings ---
original = " computational design "
cleaned = original.strip().upper()
changed = cleaned.replace("DESIGN", "THINKING")
print(repr(original))
print(changed, len(changed))
print("banana bandana".count("ana"))  # Non-overlapping occurrences.

# --- 04: Split and join connect text with sequences ---
words = "timber steel glass".split()
print(words)
print(", ".join(words))
print("panel-" + "A", "-" * 8)
length_m = 2.4
print(f"Material: {material}; length: {length_m:.2f} m")
