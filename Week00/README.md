# Week00 — Environment verification

This folder contains a minimal Python program for checking the `acd` environment
and the interpreter selected in VS Code. Run it from both the terminal and the
editor to verify that each uses the intended Python installation.

With `acd` active, run the example from the repository root:

```sh
conda activate acd
python Week00/tutorial/hello_world.py
```

Expected output:

```text
Hello ACD!
```

In VS Code, select the `acd` interpreter, open
[hello_world.py](tutorial/hello_world.py), and run **Python: Run Python File in Terminal**.
The output should match the terminal execution.

To verify interpreter selection, run:

```sh
python -c "import sys; print(sys.executable)"
```

The path should identify the Python executable inside the `acd` environment.
