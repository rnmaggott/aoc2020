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
def partOne(np_arr):
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


def findClosest(arr, reverse=False):
    if reverse:
        arr = np.flip(arr)

    for i, val in enumerate(arr):
        if val == "#":
            return 1
        if val == "L":
            return 0
    return 0


# %%
def partTwo(np_arr):
    new_plan = np_arr.copy()

    while True:
        # Loop through rows
        for rowpos, line in enumerate(np_arr):
            # Loop through columns
            for colpos, element in enumerate(line):

                adjacent = 0
                if "." == np_arr[rowpos, colpos]:
                    continue
                # Scan L
                adjacent += findClosest(np_arr[rowpos, 0:colpos], True)
                # Scan U
                adjacent += findClosest(np_arr[0:rowpos, colpos], True)
                # Scan R
                adjacent += findClosest(np_arr[rowpos, colpos+1:len(np_arr)])
                # Scan D
                adjacent += findClosest(np_arr[rowpos+1:len(np_arr), colpos])
                # Scan LU
                window = np_arr[0:rowpos, 0:colpos]
                sside = min(np.shape(window))
                window = window[-sside:, -sside:]
                adjacent += findClosest(window.diagonal(), True)
                # Scan RU
                window = np_arr[0:rowpos, colpos+1:len(np_arr)]
                sside = min(np.shape(window))
                window = window[-sside:, :sside]
                adjacent += findClosest(np.fliplr(window).diagonal(), True)
                # Scan RD
                window = np_arr[rowpos+1:len(np_arr), colpos+1:len(np_arr)]
                sside = min(np.shape(window))
                window = window[:sside, :sside]
                adjacent += findClosest(window.diagonal())
                # Scan LD
                window = np_arr[rowpos+1:len(np_arr), 0:colpos]
                sside = min(np.shape(window))
                window = window[:sside, -sside:]
                adjacent += findClosest(np.fliplr(window).diagonal())

                if adjacent == 0:
                    new_plan[rowpos][colpos] = "#"
                elif adjacent >= 5:
                    new_plan[rowpos][colpos] = "L"
        new_unique, new_counts = np.unique(new_plan, return_counts=True)
        old_unique, old_counts = np.unique(np_arr, return_counts=True)
        np_arr = new_plan.copy()

        if dict(zip(new_unique, new_counts)) == dict(zip(old_unique, old_counts)):
            counts = dict(zip(new_unique, new_counts))
            print(f"Occupied: {counts['#']}\nFree: {counts['L']}")
            break


# %%
partOne(np_arr)
partTwo(np_arr)
# %%
