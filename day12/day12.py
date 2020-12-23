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


def p2():
    ship_e = 0
    ship_n = 0
    wp_e = 10
    wp_n = 1
    for inst in instructions:
        cmd, num = inst
        if cmd == "N":
            wp_n += num
        elif cmd == "S":
            wp_n -= num
        elif cmd == "E":
            wp_e += num
        elif cmd == "W":
            wp_e -= num
        elif cmd == "L":
            rotation = -num*np.pi/180
            wp_e_old = wp_e
            wp_n_old = wp_n
            wp_e = round(np.cos(rotation)*wp_e_old + np.sin(rotation)*wp_n_old)
            wp_n = round(-np.sin(rotation)*wp_e_old +
                         np.cos(rotation)*wp_n_old)
        elif cmd == "R":
            rotation = num*np.pi/180
            wp_e_old = wp_e
            wp_n_old = wp_n
            wp_e = round(np.cos(rotation)*wp_e_old + np.sin(rotation)*wp_n_old)
            wp_n = round(-np.sin(rotation)*wp_e_old +
                         np.cos(rotation)*wp_n_old)
        elif cmd == "F":
            ship_n += num*(wp_n)
            ship_e += num*(wp_e)
    print(f"X: {ship_e}\nY: {ship_n}\nDist: {abs(ship_e) + abs(ship_n)}")


# %%
p1()
p2()

# %%
