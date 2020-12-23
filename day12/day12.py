# %%
import numpy as np
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day12/input.txt") as f:
    input_data = f.read().split("\n")
    # input_data = [line.split() for line in f]

# %%
instructions = []
for line in input_data:
    instructions.append((line[0], int(line[1:])))


def p1():
    current_x = 0
    current_y = 0
    heading = 0
    for inst in instructions:
        cmd, num = inst
        if cmd == "N":
            current_y += num
        elif cmd == "S":
            current_y -= num
        elif cmd == "E":
            current_x += num
        elif cmd == "W":
            current_x -= num
        elif cmd == "L":
            heading += (num*np.pi/180)
        elif cmd == "R":
            heading -= (num*np.pi/180)
        elif cmd == "F":
            # opposite = hypoteneuse*arcsin(heading)
            current_y += int(np.sin(heading)*num)
            # adjacent = hypoteneuse*arcsin(heading)
            current_x += int(np.cos(heading)*num)

    print(f"X: {current_x}\nY: {current_y}\nDist: {abs(current_x) + abs(current_y)}")


# %%
p1()

# %%
