# %%
import sys
with open("/mnt/c/Users/Ryan/Documents/aoc2020/day13/input.txt") as f:
    input_data = f.read().split("\n")
    # input_data = [line.split() for line in f]
# %%
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
