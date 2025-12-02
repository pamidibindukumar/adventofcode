import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


with open("ADC2025files/input_day2.txt", "r") as file:
    rows = file.read().split(",")


invalid_id_p1 = []
invalid_id_p2 = []


def has_repeating_pattern(n,mode =0):
    s = str(n)
    L = len(s)

    # check for only two equal halves
    if mode == 2:
        if L % 2 != 0:
            return False
        half = L // 2
        return s[:half] == s[half:]

    # Try every possible pattern length from 1 to L//2
    for size in range(1, L // 2 + 1):
        if L % size == 0:           # pattern must divide full length
            pattern = s[:size]
            if pattern * (L // size) == s:   # repeated sequence check
                return True
    return False


for i in rows:
    start_id = int(i.split("-")[0])
    end_id = int(i.split("-")[1].split(" ")[0])
    for j in range(start_id, end_id+1):
        if has_repeating_pattern(j):
            invalid_id_p2.append(j)
        if has_repeating_pattern(j, 2):
            invalid_id_p1.append(j)


print("Sum of all invalid ids for p1 is ", sum(invalid_id_p1))
print("Sum of all invalid ids for p2 is ", sum(invalid_id_p2))

