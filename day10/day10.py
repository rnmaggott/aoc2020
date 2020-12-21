# %%
from collections import Counter
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day10/input.txt") as f:
    lines = f.read().split("\n")

# Add initial device of 0
lines.append(0)
# Convert to ints
lines = [int(i) for i in lines]
# Add final device of max+3
lines.append(max(lines)+3)
slines = sorted(lines)


# %%
def calcDifferences(input_lines):
    differences = []
    prev_line = input_lines[0]
    for line in input_lines[1:]:
        differences.append(line - prev_line)
        prev_line = line
    diffs = Counter(differences)
    output = diffs[1] * diffs[3]
    print(f"Differences: {Counter(differences)}")
    print(f"Output: {output}")


# Shamelessly adapted from: https://www.youtube.com/watch?v=cE88K2kFZn0
def dynP(location):
    # if we reach the end of the sorted list there's only 1 possible connection
    if location == len(slines)-1:
        return 1
    if location in DP:
        return DP[location]
    ans = 0
    for i in range(location+1, len(slines)):
        if slines[i] - slines[location] <= 3:
            ans += dynP(i)
    DP[location] = ans
    return ans


# %%
print()
calcDifferences(slines)
DP = {}
print(f"Total combinations is: {dynP(0)}")

# %%
