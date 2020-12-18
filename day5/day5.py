# %%
import numpy as np
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day5/input.txt") as f:
    lines = f.read().split("\n")


# %%
def findRow(input_data):
    row_s = 0
    row_e = 127
    for var in input_data[:7]:
        if var == "F":
            row_e = row_e - np.ceil((row_e-row_s)/2)
        if var == "B":
            row_s = row_s + np.ceil((row_e-row_s)/2)

    return row_s


def findCol(input_data):
    col_l = 7
    col_r = 0
    for var in input_data[7:]:
        if var == "R":
            col_r = col_r + np.ceil((col_l - col_r)/2)
        if var == "L":
            col_l = col_l - np.ceil((col_l - col_r)/2)

    return col_l


# %%
max_id = 0
for input_data in lines:
    row = int(findRow(input_data))
    col = int(findCol(input_data))
    idx = int((row * 8) + col)
    max_id = int(np.max((max_id, idx)))

print(f"{input_data}: row {row}, column {col}, seat ID {max_id}")

# %%
