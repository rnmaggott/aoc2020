# %%
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day6/input.txt") as f:
    batches = f.read().split("\n\n")

# %%
answers = []
for batch in batches:
    line = batch.split("\n")
    # print(line)

    people = batch.split("\n")
    output_list = list(people[0])
    people.pop(0)
    for person in people:
        output_list.extend(x for x in person if x not in output_list)

    answers.append(len(output_list))

print(sum(answers))


# %%
