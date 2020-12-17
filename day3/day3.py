# %%
def wrapLine(line, position):
    return position % len(line)


# %%
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day3/input.txt") as f:
    lines = f.read().splitlines()


# %%
def findTrees(lines, slope):
    xslope = slope[0]
    yslope = slope[1]
    trees_found = 0

    xpos = 0
    for line_number in range(0, len(lines), yslope):
        xpos = wrapLine(lines[0], xpos)
        if lines[line_number][xpos] == "#":
            trees_found += 1
        xpos += xslope

    return trees_found


# %%
slopes = [(1, 1),
          (3, 1),
          (5, 1),
          (7, 1),
          (1, 2)]

# slopes = [(3, 1)]

# %%
# Create a list of the number of trees for each slope
tree_list = []
for slope in slopes:
    tree_list.append(findTrees(lines, slope))

# Calculate the tree math
tree_math = 1
for tree_count in tree_list:
    tree_math *= tree_count

print(f"You will encounter {tree_list} trees.")
print(f"The tree function is {tree_math}")
# %%
