"""01 — Word Counts — Optional
Run independently after the core topics; this is not another required exercise.
"""

# Supplied file-location setup. Run this before the lesson sections.
from pathlib import Path

if "__file__" in globals():
    WEEK_DIR = Path(__file__).resolve().parents[1]
else:
    # For selected lines: start in the repository, week, or script folder.
    WEEK_DIR = Path.cwd()
    if WEEK_DIR.name in {"tutorial", "exercises", "optional"}:
        WEEK_DIR = WEEK_DIR.parent
    if WEEK_DIR.name != "Week04":
        WEEK_DIR = WEEK_DIR / "Week04"
DATA_DIR = WEEK_DIR / "data"
OUTPUT_DIR = WEEK_DIR / "outputs"

# A file is useful here because the text is too long to type into the script.
text = (DATA_DIR / "alice_in_wonderland.txt").read_text(encoding="utf-8")
counts = {}
for raw_word in text.split():
    word = "".join(ch for ch in raw_word if ch.isalnum()).lower()
    if not word:
        continue
    counts[word] = counts.get(word, 0) + 1
# Order tuples by count first, then word, without requiring a lambda function.
ranked = sorted([(count, word) for word, count in counts.items()], reverse=True)
print("Most frequent cleaned tokens:")
for count, word in ranked[:10]:
    print(word, count)
unique_words = set(counts)
print("Unique tokens:", len(unique_words))
print("Alphabetical sample:", sorted(unique_words)[:10])
# This rule deletes punctuation inside tokens: "don't" becomes "dont".
# It counts the supplied file, including headings. It is not a language parser.
# Discuss whether splitting hyphenated words would better suit your question.
