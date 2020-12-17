# %%
def decodeRequirements_old(input_line):
    letter_const = input_line.split(" ")[1][0]
    minmax = input_line.split(" ")[0].split("-")
    minimum = int(minmax[0])
    maximum = int(minmax[1])

    return (letter_const, minimum, maximum)


def decodeRequirements(input_line):
    letter_const = input_line.split(" ")[1][0]
    minmax = input_line.split(" ")[0].split("-")
    first = int(minmax[0])
    second = int(minmax[1])

    return (letter_const, first, second)


def checkPassword_old(input_line):
    letter_const, minimum, maximum = decodeRequirements_old(input_line)
    password = input_line.split(" ")[-1]

    occurances = sum(1 for p in password if p == letter_const)
    if (occurances >= minimum) & (occurances <= maximum):
        return True
    return False


def checkPassword(input_line):
    letter_const, first, second = decodeRequirements(input_line)
    password = input_line.split(" ")[-1]

    # check first
    if letter_const == password[first-1]:
        if letter_const == password[second-1]:
            return False
        return True
    elif letter_const == password[second-1]:
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
