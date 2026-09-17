# Advanced Computational Design — Tutorials

Python examples and exercises for computational design, covering programming
fundamentals, data processing, and visualization.

## Setup

Complete these steps in order. The linked guides in ACD-Reference provide the
full Windows and macOS walkthroughs, along with troubleshooting and everyday use.

1. **Set up GitHub Desktop and clone this repository.** Create a GitHub account
   if needed, verify your email, install GitHub Desktop, sign in, and configure
   your Git name and email. Clone `AdvancedComputationalDesign-SDU/ACD-Tutorials`
   to a local folder. [GitHub Desktop walkthrough](https://github.com/AdvancedComputationalDesign-SDU/ACD-Reference/blob/main/dev_tools/github_desktop/README.md).
2. **Install Miniconda and create the Python environment.** Open Anaconda Prompt
   on Windows or Terminal on macOS, navigate to the cloned repository, and run
   `conda env create -f environment.yml`, followed by `conda activate acd`.
   The [environment file](environment.yml) specifies Python and the required
   libraries. [Miniconda walkthrough](https://github.com/AdvancedComputationalDesign-SDU/ACD-Reference/blob/main/dev_tools/miniconda/README.md).
3. **Install and configure Visual Studio Code.** Install Microsoft's **Python**
   extension (`ms-python.python`), open the cloned repository folder, and use
   **Python: Select Interpreter** to choose `acd`. Open a new terminal and verify
   that it uses the same environment. [VS Code walkthrough](https://github.com/AdvancedComputationalDesign-SDU/ACD-Reference/blob/main/dev_tools/vscode/README.md).
4. **Verify the setup.** Follow [Week00](Week00/README.md) to run
   `hello_world.py` from both the terminal and VS Code. Both should print
   `Hello ACD!`.

For additional libraries, the [pip guide](https://github.com/AdvancedComputationalDesign-SDU/ACD-Reference/blob/main/dev_tools/pip/README.md)
explains installation into the selected environment and how to specify versions.

## Organization

Week folders contain the following subdirectories as needed.

| Directory | Contents |
| --- | --- |
| `tutorial/` | Numbered examples organized by topic. |
| `exercises/` | Problems and worked solutions. |
| `optional/` | Additional examples and extensions. |
| `data/` | Input files and source information. |
| `outputs/` | Generated results, excluded from version control. |

Each week's README gives the topic sequence. Run complete scripts independently;
when executing sections, run their imports and path setup first. Keep the full
week directory when copying examples so data and helper-file paths remain valid.
Preserve local edits before pulling repository updates.
