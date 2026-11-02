"""Worked solution: Returns and scope

Write shifted_wave(x, phase=0) returning 0.5 + 0.5*sin(x + phase).
Predict x=0, phase=0 and x=0, phase=pi/2. Check that calling the
function does not overwrite a caller variable named phase. Plot one
comparison with phase 0 and pi/2 using the same x coordinates.

One possible solution. Discuss another valid policy or representation.
"""
from pathlib import Path
import sys
import matplotlib.pyplot as plt

if "__file__" in globals():
    WEEK_DIR = Path(__file__).resolve().parents[1]
else:
    WEEK_DIR = Path.cwd()
    if WEEK_DIR.name in {"tutorial", "exercises", "solutions", "optional"}:
        WEEK_DIR = WEEK_DIR.parent
    if WEEK_DIR.name != "Week06":
        WEEK_DIR = WEEK_DIR / "Week06"
sys.path.insert(0, str(WEEK_DIR / "tutorial"))
OUTPUT_DIR = WEEK_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

import numpy as np

def shifted_wave(x, phase=0):
    return 0.5 + 0.5 * np.sin(x + phase)

if __name__ == "__main__":
    phase = 0
    assert np.isclose(shifted_wave(0), 0.5)
    assert np.isclose(shifted_wave(0, np.pi / 2), 1)
    shifted_wave(0, np.pi / 2)
    assert phase == 0
    x = np.linspace(-np.pi, np.pi, 160)
    fig, ax = plt.subplots(figsize=(6, 3))
    for offset in [0, np.pi / 2]:
        ax.plot(x, shifted_wave(x, offset), label=f"phase {offset:.2f}")
    ax.legend()
    ax.set(xlabel="x", ylabel="value", ylim=(0, 1))
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "solution_01_returns_and_scope.png", dpi=160)
    print("Checks passed: 01_returns_and_scope")
    plt.show()
    plt.close(fig)
