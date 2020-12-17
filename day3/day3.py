# %%
def wrapLine(line, position):
    return position % len(line)


# %%
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day3/input.txt") as f:
    lines = f.read().splitlines()

# %%
pos = 0
trees_found = 0
for line in lines:
    pos = wrapLine(line, pos)
    if line[pos] == "#":
        trees_found += 1
    pos += 3

# %%
print("You will encounter {trees_found} trees.")
# %%
