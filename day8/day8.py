# %%
import time
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day8/input.txt") as f:
    instructions_orig = f.read().split("\n")


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


def flipOperation(instruction):
    inst, operation = instruction.split(" ")
    if inst == "jmp":
        return "nop " + str(operation)
    if inst == "nop":
        return "jmp " + str(operation)
    else:
        return instruction


def executeBoot(instructions):
    new_pos = 0
    executed_instructions = [0]
    while True:
        if new_pos >= len(instructions):
            return True
        print(f"Executing instruction: {instructions[new_pos]}")
        pos_offset = decodeInstruction(instructions[new_pos])
        if pos_offset is not None:
            new_pos += pos_offset
            if new_pos in executed_instructions:
                print("Failed, try again")
                print(
                    f"Tried to execute {instructions[new_pos]} on line " +
                    f" {new_pos} again.")
                # instructions = instructions_orig.copy()
                return False
            executed_instructions.append(new_pos)


# %%
start = time.time()
changed_ops = []
instructions = instructions_orig.copy()
run_orig = False
for pos, instruction in enumerate(instructions):
    accumulator = 0
    if pos not in changed_ops:
        instructions[pos] = flipOperation(instruction)
    changed_ops.append(pos)
    if (instructions != instructions_orig) or not run_orig:
        if instructions == instructions_orig:
            run_orig = True
        if executeBoot(instructions):
            break
        else:
            instructions = instructions_orig.copy()

print(f"Accumulator value: {accumulator}")
print(f"Took {time.time() - start} to complete")

# %%
