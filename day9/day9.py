# %%
import time
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day9/input.txt") as f:
    lines = f.read().split("\n")


def loopThrough(new_list):
    for ipos, i in enumerate(new_list):
        i = int(i)
        for j in new_list[ipos+1:]:
            j = int(j)
            if i + j == line:
                print(f"Sum found: {i} + {j} = {i + j} ({line})")
                return True
    return False


# %%
start = time.time()
preamble = 25
new_list = lines[:preamble]
for line in lines[preamble:]:
    line = int(line)
    sum_found = loopThrough(new_list)
    new_list.pop(0)
    new_list.append(line)
    if not sum_found:
        print(f"No sum found for {line}")
        break

print(f"Code executed in {time.time() - start} seconds")
# %%
