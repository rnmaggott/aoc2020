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


def findMissingVal(input_list):
    for id in range(len(input_list)-1):
        if input_list[id + 1] - input_list[id] != 1:
            print(
                f"Missing ID between: {input_list[id]} & {input_list[id + 1]}")


# %%
max_id = 0
id_list = []
for input_data in lines:
    row = int(findRow(input_data))
    col = int(findCol(input_data))
    idx = int((row * 8) + col)
    max_id = int(np.max((max_id, idx)))

    id_list.append(int(idx))

print(f"Highest ID: {input_data}: row {row}, column {col}, seat ID {max_id}")

findMissingVal(sorted(id_list))

# %%
