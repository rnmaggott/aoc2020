# %%

def findTwoSum(number_list):
    for posi, i in enumerate(number_list):
        number_list_i = number_list[posi:]
        i = int(i)
        for posj, j in enumerate(number_list_i):
            j = int(j)
            if 2020 == i + j:
                return (i, j)


def findThreeSum(number_list):
    for posi, i in enumerate(number_list):
        number_list_i = number_list[posi:]
        i = int(i)
        for posj, j in enumerate(number_list_i):
            number_list_j = number_list_i[posj:]
            j = int(j)
            for k in number_list_j:
                k = int(k)
                if 2020 == i + j + k:
                    return (i, j, k)


# %%
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day1/input.txt") as f:
    lines = f.read().splitlines()

# %%
i, j = findTwoSum(lines)

print("Find Two:")
print(f"The first number is {i}")
print(f"The second number is {j}")
print(f"{i} + {j} = {i+j}")
print(f"\nThe answer is: {i} * {j} = {i * j}")
# %%
i, j, k = findThreeSum(lines)

print("Find Three:")
print(f"The first number is {i}")
print(f"The second number is {j}")
print(f"The third number is {k}")
print(f"{i} + {j} + {k}= {i+j+k}")
print(f"\nThe answer is: {i} * {j} * {k} = {i * j * k}")

# %%
