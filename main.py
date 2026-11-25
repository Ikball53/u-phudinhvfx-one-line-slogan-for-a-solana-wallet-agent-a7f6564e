import os

# Deterministic single-line slogan, no trailing newline.
line = "I guard your SOL while you sleep, then spend it on coffee before you wake."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
