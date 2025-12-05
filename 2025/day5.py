import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


with open("ADC2025files/input_day5.txt", "r") as file:
    rows = file.read().split("\n")


fresh_ingredient_ranges = []

fresh_ingredients_check = 0
for row in rows:
    row = row.strip()

    if not row:
        continue

    if '-' in row:
        l, u = map(int, row.split('-'))
        fresh_ingredient_ranges.append((l, u))   # store interval only
    else:
        x = int(row)
        # Check if x falls inside ANY stored interval
        for low, high in fresh_ingredient_ranges:
            if low <= x <= high:
                fresh_ingredients_check += 1
                break   # no need to check further ranges

fresh_ingredient_ranges.sort()
fresh_ingredient_ranges_merged = []

cur_l, cur_u = fresh_ingredient_ranges[0]
for low, high in fresh_ingredient_ranges[1:]:
    if low <= cur_u :
        cur_u = max(cur_u, high)
    else:
        fresh_ingredient_ranges_merged.append((cur_l, cur_u))
        cur_l, cur_u = low, high

fresh_ingredient_ranges_merged.append((cur_l, cur_u))

total_unique = sum(u - l + 1 for l, u in fresh_ingredient_ranges_merged)


print(fresh_ingredients_check) # for part 1
print(total_unique) # for part 2


