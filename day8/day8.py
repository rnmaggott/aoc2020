# %%
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day8/input.txt") as f:
    instructions = f.read().split("\n")


def decodeInstruction(instruction):
    print(f"Decoding instruction: {instruction}")
    inst, operation = instruction.split(" ")

    if inst == "acc":
        return acc(operation)
    if inst == "nop":
        return nop()
    if inst == "jmp":
        return jmp(operation)


def acc(operation):
    global accumulator
    print(
        f"Executing accumulate instruction. Accumulator: {accumulator}, " +
        f"operation: {operation}")
    accumulator += int(operation)
    print(f"New accumulator value: {accumulator}")
    return 1


def nop():
    print("Nop instruction, continuing")
    return 1


def jmp(operation):
    print(f"Jump instruction. Operation: {operation}")
    print(f"Jumping {operation} lines")
    return int(operation)


# %%
accumulator = 0

# for position, instruction in enumerate(instructions):
new_pos = 0
executed_instructions = [0]
while True:
    print(f"Executing instruction: {instructions[new_pos]}")
    pos_offset = decodeInstruction(instructions[new_pos])
    if pos_offset:
        new_pos += pos_offset
        if new_pos in executed_instructions:
            break
        executed_instructions.append(new_pos)

print(f"Tried to execute {instructions[new_pos]} on line {new_pos} again.")
print(f"Accumulator value: {accumulator}")


# %%
