# %%
import string
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day4/input.txt") as f:
    lines = f.read().split("\n\n")


# %%
def check_codes(entry, expected_codes):
    for batch in entry.replace("\n", " ").split(" "):
        code = batch.split(":")[0]
        value = batch.split(":")[1]

        if code == "byr":
            if (int(value) < 1920) or (int(value) > 2002):
                return False
        if code == "iyr":
            if (int(value) < 2010) or (int(value) > 2020):
                return False
        if code == "eyr":
            if (int(value) < 2020) or (int(value) > 2030):
                return False
        if code == "hgt":
            unit = value[-2:]
            value = value[:-2]
            if unit == "cm":
                if (int(value) < 150) or (int(value) > 193):
                    return False
            elif unit == "in":
                if (int(value) < 59) or (int(value) > 76):
                    return False
            else:
                return False
        if code == "hcl":
            try:
                if value[0] != "#":
                    return False
                value = value[1:]
                if len(value) != 6:
                    return False
                if not all(c in string.hexdigits for c in value):
                    return False
            except ValueError:
                return False
        if code == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        if code == "pid":
            if len(value) != 9:
                return False
            try:
                int(value)
            except ValueError:
                return False

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

for pos, entry in enumerate(lines):
    if check_codes(entry, expected_codes.copy()):
        valid_passports += 1

print(f"There are {valid_passports} valid passports.")

# %%
