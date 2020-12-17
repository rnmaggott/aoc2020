# %%

def findTwoSum(number_list):
    for posi, i in enumerate(number_list):
        # number_list.pop(posi)
        i = int(i)
        for posj, j in enumerate(number_list):
            j = int(j)
            if 2020 == i + j:
                return (i, j, posi, posj)


# %%
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day1/input.txt") as f:
    lines = f.read().splitlines()

# %%
i, j, posi, posj = findTwoSum(lines)

print(f"The first number is {i} on line {posi}")
print(f"The second number is {j} on line {posj}")
print(f"{i} + {j} = {i+j}")
print(f"\nThe answer is: {i} * {j} = {i * j}")
# %%
