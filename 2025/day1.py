import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# dial starts at 50
"""
I optimized the solution by eliminating the step-by-step simulation of the dial movement.
Instead, I derived a direct mathematical formula to compute the number of zero-crossings in O(1) time for each command.

For each operation, the algorithm calculates:

    the first step index (k0) at which zero is crossed,

    how many full 100-step cycles remain afterward,

    the final position using modular arithmetic.

This replaces the original O(steps) loop with a constant-time formula using only modulo and integer division.
As a result, the entire problem now runs in O(1) time per operation, making it highly efficient for large inputs.



"""

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
        pos = end_pos
    if pos==0:
        p1+=1
    cross += crossings
print(p1) # for 1st question
print(cross) # for second question