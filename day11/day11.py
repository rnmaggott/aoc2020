# %%
import numpy as np
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day11/input.txt") as f:
    # input_data = f.read().split("\n")
    input_data = [line.split() for line in f]

# %%
new_arr = []
for pos, line in enumerate(input_data):
    new_arr.append([])
    for element in line[0]:
        new_arr[pos].append(element)
np_arr = np.array(new_arr)
del new_arr

# %%
new_plan = np_arr.copy()
while True:
    # Loop through rows
    for rowpos, line in enumerate(np_arr):
        rs = max(0, rowpos-1)
        re = min(len(np_arr), rowpos+2)
        # Loop through columns
        for colpos, element in enumerate(line):
            cs = max(0, colpos-1)
            ce = min(len(np_arr), colpos+2)

            temp = np_arr[rowpos, colpos]
            np_arr[rowpos, colpos] = " "

            window = np_arr[rs:re, cs:ce]
            # Count occupied seats
            win_unique, win_counts = np.unique(window, return_counts=True)
            win_inf = dict(zip(win_unique, win_counts))
            np_arr[rowpos, colpos] = temp
            if "." == np_arr[rowpos, colpos]:
                continue
            elif (win_inf.get("#", 0) == 0):
                new_plan[rowpos][colpos] = "#"
            elif win_inf.get("#", 0) >= 4:
                new_plan[rowpos][colpos] = "L"
    new_unique, new_counts = np.unique(new_plan, return_counts=True)
    old_unique, old_counts = np.unique(np_arr, return_counts=True)
    np_arr = new_plan.copy()

    if dict(zip(new_unique, new_counts)) == dict(zip(old_unique, old_counts)):
        counts = dict(zip(new_unique, new_counts))
        print(f"Occupied: {counts['#']}\nFree: {counts['L']}")
        break

# %%
