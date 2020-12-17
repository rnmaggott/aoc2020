# %%
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day4/input.txt") as f:
    lines = f.read().split("\n\n")


# %%
def check_codes(entry, expected_codes):
    for batch in entry.replace("\n", " ").split(" "):
        code = batch.split(":")[0]
        try:
            expected_codes.pop(expected_codes.index(code))
        except ValueError:
            pass

    if len(expected_codes) > 0:
        if len(expected_codes) == 1:
            if expected_codes[0] == "cid":
                return True
        else:
            return False
    else:
        return True


# %%
expected_codes = ["byr",
                  "iyr",
                  "eyr",
                  "hgt",
                  "hcl",
                  "ecl",
                  "pid",
                  "cid"]

valid_passports = 0

for entry in lines:
    if check_codes(entry, expected_codes.copy()):
        valid_passports += 1

print(f"There are {valid_passports} valid passports.")

# %%
