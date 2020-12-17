# %%
def decodeRequirements(input_line):
    letter_const = input_line.split(" ")[1][0]
    minmax = input_line.split(" ")[0].split("-")
    minimum = int(minmax[0])
    maximum = int(minmax[1])

    return (letter_const, minimum, maximum)


def checkPassword(input_line):
    letter_const, minimum, maximum = decodeRequirements(input_line)
    password = input_line.split(" ")[-1]

    occurances = sum(1 for p in password if p == letter_const)
    if (occurances >= minimum) & (occurances <= maximum):
        return True
    return False


# %%
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day2/input.txt") as f:
    lines = f.read().splitlines()

# %%
val_pw = 0
for line in lines:
    if checkPassword(line):
        val_pw += 1

# %%
print(f"There are {val_pw} passwords.")
# %%
