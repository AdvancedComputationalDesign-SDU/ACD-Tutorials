"""01 Functions: wrap a familiar W05 field and check the returned values.

Run the imports and location setup before selecting lesson sections.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

if "__file__" in globals():
    WEEK_DIR = Path(__file__).resolve().parents[1]
else:
    WEEK_DIR = Path.cwd()
    if WEEK_DIR.name in {"tutorial", "exercises", "solutions", "optional"}:
        WEEK_DIR = WEEK_DIR.parent
    if WEEK_DIR.name != "Week06":
        WEEK_DIR = WEEK_DIR / "Week06"
OUTPUT_DIR = WEEK_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# %% Warm-up from the existing lecture: defining and composing small functions.
def greet():
    print("Hello, welcome to Python functions!")


def repeat_greet():
    greet()
    greet()


def personalized_greet(name="Alice"):
    print(f"Hello, {name}!")


repeat_greet()
personalized_greet()
personalized_greet("Sam")

# %% 1. A definition stores a reusable calculation. Calling it does the work.
def ring_field(x, y, frequency=4.0):
    distance = np.sqrt(x**2 + y**2)
    return 0.5 + 0.5 * np.sin(frequency * np.pi * distance)


print("Known value at the center:", ring_field(0.0, 0.0))  # 0.5
value = ring_field(0.25, 0.0, frequency=2.0)
print("Known quarter-unit value:", value)  # 1.0

# %% 2. Return makes a value available to the caller. Print displays it.
def show_value(x):
    print("Inside show_value:", x)


printed = show_value(3)
print("No explicit return gives:", printed)  # None

# %% 3. The same function accepts arrays. Compare the original expression.
coords = np.linspace(-1, 1, 160)
X, Y = np.meshgrid(coords, coords)
original = 0.5 + 0.5 * np.sin(4 * np.pi * np.sqrt(X**2 + Y**2))
wrapped = ring_field(X, Y)
assert np.allclose(original, wrapped)
print("Same field:", np.allclose(original, wrapped))
fig, axes = plt.subplots(1, 2, figsize=(7, 3.5))
for ax, field, title in zip(axes, [wrapped, ring_field(X, Y, frequency=2)],
                          ["frequency = 4", "frequency = 2"]):
    ax.imshow(field, cmap="gray", vmin=0, vmax=1, origin="lower")
    ax.set_title(title)
    ax.axis("off")
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "01_functions.png", dpi=160)
plt.show()
plt.close(fig)
# Checkpoint: explain why a frequency argument changes both array calls.
