# %%
from collections import Counter
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day10/input.txt") as f:
    lines = f.read().split("\n")

# %%
lines.append(0)
lines = [int(i) for i in lines]
lines.append(max(lines)+3)
slines = sorted(lines)

# %%
differences = []
prev_line = slines[0]
for line in slines[1:]:
    differences.append(line - prev_line)
    prev_line = line
diffs = Counter(differences)
output = diffs[1] * diffs[3]
print(f"Differences: {Counter(differences)}")
print(f"Output: {output}")

# %%
