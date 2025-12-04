import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


with open("ADC2025files/input_day4.txt", "r") as file:
    rows = file.read().split()

# print(rows)

directions = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1, -1)]

n = len(rows)
m = len(rows[0])


roll_lift_p2 = 0
roll_lift_p1 = 0

iterator = 0
while True:
    roll_lift = 0

    lift_positions = []
    for i in range(n):
        for j in range(m):
            if rows[i][j] == '@':
                ct_roll = 0
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and rows[x][y] == '@':
                        ct_roll +=1
                if ct_roll <4:
                    roll_lift +=1
                    lift_positions.append((i, j))

    for i, j in lift_positions:
        row_list = list(rows[i])
        row_list[j] = '.'   # <-- replace with whatever you want
        rows[i] = ''.join(row_list)

    # print(roll_lift)
    roll_lift_p2 += roll_lift

    if iterator == 0:
        roll_lift_p1 = roll_lift
        iterator = 1
    if roll_lift == 0:
        break


print(roll_lift_p1)
print(roll_lift_p2)
