# %%
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day6/input.txt") as f:
    batches = f.read().split("\n\n")


# %%
def anyoneYes(batches):
    answers = []
    for batch in batches:
        people = batch.split("\n")
        output_list = list(people[0])
        people.pop(0)
        for person in people:
            output_list.extend(x for x in person if x not in output_list)

        answers.append(len(output_list))

    return sum(answers)


# %%
def everyoneYes(batches):
    answers = []
    for batch in batches:
        sets = []
        people = batch.split("\n")
        for person in people:
            sets.append(set(person))

        outset = sets[0]
        sets.pop(0)
        for pset in sets:
            outset = outset & pset

        answers.append(len(outset))

    return sum(answers)


# %%
print(f"Sum of anyone yes: {anyoneYes(batches)}.")
print(f"Sum of everyone yes: {everyoneYes(batches)}.")

# %%
