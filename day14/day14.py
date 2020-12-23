# %%
import time
import sys
import numpy as np
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day14/input.txt") as f:
    input_data = f.read().split("\n")
    # input_data = [line.split() for line in f]

# %%
mask = None
mem = {}
for line in input_data:
    if line.startswith("mask"):
        # mem = {}
        mask = np.array([int(x) if x != "X" else -
                         1 for x in line.split(" = ")[-1]])
        mask = np.flip(mask)
        continue

    exec(line)
    value = bin(eval(line.split(" = ")[0]))
    value = "0b" + "0"*(36-len(value) + 2) + value[2:]
    value = value[::-1]
    print(f"Value: {value}")
    for i in range(len(value)-2):
        if mask[i] != -1:
            value = value[:i] + str(mask[i]) + value[i+1:]

    value = value[::-1]
    exec(line.split("=")[0] + "=" + str(eval(value)))
    print(f"Value: {value}")

print(f"Sum: {sum(mem.values())}")

# %%
