# %%
import time
import sys
import numpy as np
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day13/input_test.txt") as f:
    input_data = f.read().split("\n")
    # input_data = [line.split() for line in f]
# %%


def p1():
    earliest_departure = int(input_data[0])
    busses = [int(x) for x in input_data[1].split(",") if x != "x"]

    soonest_departure = sys.maxsize
    bus_no = -1
    for bus in busses:
        before_arrival = earliest_departure - earliest_departure % bus
        if (before_arrival + bus) < soonest_departure:
            soonest_departure = before_arrival + bus
            bus_no = bus

    print(f"Bus ID: {bus_no}\nWait Time:" +
          f" {(soonest_departure - earliest_departure)}" +
          f"\nMath: {bus_no*(soonest_departure - earliest_departure)}")


# %%
def p2_bruteForce():
    start = time.time()
    busses_raw = input_data[1]
    busses = [int(x) if x != "x" else 0 for x in busses_raw.split(",")]
    indices = []

    max_index = busses.index(max(busses))
    for pos in range(len(busses)):
        indices.append(pos - max_index)

    indices = np.array(indices)
    busses = np.array(busses)
    indices = np.delete(indices, np.where(busses == 0))
    new_busses = np.delete(busses, np.where(busses == 0))

    counter = 1
    while True:
        ts = max(busses)*counter
        if all(np.mod((indices+ts), new_busses) == 0):
            break
        counter += 1
        if counter % 1000000 == 0:
            print(counter)

    print(f"Common Timestamp: {ts + indices[0]}")
    print(f"Time Taken: {time.time() - start}")


# %%
# Solution adapted from Youtube comments on
# https://www.youtube.com/watch?v=x40aLK9KjYQ
def p2():
    busFactor = 1

    busPos = 1
    busTime = 0
    busses = [x for x in input_data[1].split(",")]
    for bus in busses:
        if bus == 'x':
            busPos += 1
            continue

        # Find a time where the busses are synced up, and use this as a new
        # addition factor on the busTime
        while (busPos + busTime) % int(bus) > 0:
            busTime += busFactor

        # When we find the matching bus, integrate this into the factor
        busFactor *= int(bus)

        # Increment the bus position
        busPos += 1

    # The starting position is where the first bus starts
    print(f"Start Time: {busTime + 1}")


# %%
print("Part1:")
p1()
print("\nPart2:")
p2()

# %%
