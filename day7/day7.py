# %%
import re
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day7/input.txt") as f:
    lines = f.read().split("\n")

with open("/mnt/c/Users/Ryan/Documents/aoc2020/day7/input.txt") as f:
    nested_bag_input = f.read().split("\n")


# %%
def bagCheck(bag, bag_dict, bag_list=[]):
    found_list = []
    for bagkey in bag_dict:
        if not bag_dict[bagkey]:
            continue
        elif bag in bag_dict[bagkey]:
            found_list.append(bagkey)

    if not found_list:
        return
    for bagkey in found_list:
        if bagkey not in bag_list:
            bag_list.append(bagkey)
        bagCheck(bagkey, bag_dict, bag_list)

    return bag_list


# %%
def createBagDict(lines):
    bag_dict = {}
    for line in lines:
        criteria = re.split(" contain |, ", line)
        holding_bag = criteria[0]
        holding_bag = holding_bag.rsplit(" ", 1)[0]
        criteria.pop(0)

        bag_dict[holding_bag] = {}
        for subbags in criteria:
            subbags = subbags.rsplit(" ", 1)[0]
            try:
                bag_dict[holding_bag][re.sub(
                    "[0-9]+ ", "", subbags)] = int(re.findall("[0-9]+",
                                                              subbags)[0])
            except IndexError:
                bag_dict[holding_bag] = None

    return bag_dict


# %%
def countBagsInChildren(parent, bag_dict):
    print(f"Counting bags in parent: {parent}")
    if bag_dict[parent] is None:
        print(f"Parent {parent} has no more children")
        return 0
    bags = 0
    print("Looking through children")
    for child in bag_dict[parent]:
        child_bags = countBagsInChildren(child, bag_dict)
        print(
            f"Child {child} has {child_bags}, " +
            f"adding {bag_dict[parent][child]*child_bags} to total")
        bags += bag_dict[parent][child]*child_bags + bag_dict[parent][child]

    return bags


# %%
bag_dict = createBagDict(lines)
input_criteria = "shiny gold bag"
input_criteria = input_criteria.rsplit(" ", 1)[0]
output = bagCheck(input_criteria, bag_dict)

print(
    f"There are {len(output)} color options to contain your {input_criteria} "
    "bag.")
# %%
# input_criteria = "dark green bag"
# input_criteria = input_criteria.rsplit(" ", 1)[0]
nested_bag_dict = createBagDict(nested_bag_input)
# print(findNestedBags(input_criteria, nested_bag_dict))
print(countBagsInChildren(input_criteria, nested_bag_dict))

# %%
