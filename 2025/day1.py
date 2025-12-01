import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# dial starts at 50


with open("ADC2025files/day1.txt", "r") as file:
    rows = file.read().splitlines()

N = 100
pos = 50

p1=0
cross = 0
for op in rows:
    direction = op[0]
    steps = int(op[1:])

    if direction == "R":
        k0 = (N - pos) % N
        if k0 == 0:
            k0 = N  # first crossing happens after full loop

        if steps < k0:
            crossings = 0
        else:
            crossings = 1 + (steps - k0) // N

        end_pos = (pos + steps) % N

        # If we ENDED at 0, last hit is not a crossing
        # if end_pos == 0:
        #     crossings -= 1

        pos = end_pos

    else:  # LEFT movement
        k0 = pos % N  # distance to reach 0 when moving left
        if k0 == 0:
            k0 = N 

        if steps < k0:
            crossings = 0
        else:
            crossings = 1 + (steps - k0) // N

        end_pos = (pos - steps) % N

        # if end_pos == 0:
        #     crossings -= 1

        pos = end_pos
    if pos==0:
        p1+=1
    cross += crossings
    # print(f"{op}: ended at {pos}, crossed 0 → {crossings} times")
print(p1) # for 1st question
print(cross) # for second question