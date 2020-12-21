# %%
import time
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day9/input.txt") as f:
    lines = f.read().split("\n")


def loopThrough(new_list, val):
    for ipos, i in enumerate(new_list):
        i = int(i)
        for j in new_list[ipos+1:]:
            j = int(j)
            if i + j == val:
                print(f"Sum found: {i} + {j} = {i + j} ({val})")
                return True
    return False


def findSet(new_list, err_num):
    err_list = []
    for number in new_list:
        err_list.append(number)

        while sum(err_list) > err_num:
            err_list.pop(0)
        if sum(err_list) == err_num:
            print(f"sum({err_list}) = {err_num}")
            return min(err_list) + max(err_list)


# %%
lines = [int(i) for i in lines]
start = time.time()
preamble = 25
new_list = lines[:preamble]
for val in lines[preamble:]:
    val = int(val)
    sum_found = loopThrough(new_list, val)
    new_list.pop(0)
    new_list.append(val)
    if not sum_found:
        print(f"No sum found for {val}. Calculating Weakness")
        weakness = findSet(lines, val)
        break

print(f"Weakness of {weakness} found")
print(f"Code executed in {time.time() - start} seconds")
# %%
