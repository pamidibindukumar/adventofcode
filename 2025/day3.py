import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


with open("ADC2025files/input_day3.txt", "r") as file:
    rows = file.read().split()

# print(rows)

p1 = []
p2=[]


def best_joltage(bank , m=12):
    """
    Takes battery bank as input which consists of betteries with digits from 1 to 9
    m is the number of batteries that has to be selected 
    here we need to select m batteries in such a way that it gives maximum voltage
    """
    n=len(bank)
    if n<=m:
        return bank
    
    k= n-m # how many batteries to remove
    stack=[]

    for battery in bank:
        # while we can remove batteries if the previous battery is smaller voltage
        # pop it to make number larger
        while stack and k>0 and stack[-1]< battery:
            stack.pop()
            k-=1
        stack.append(battery)
    # if we still have removals we can remove from end 
    if k>0:
        stack = stack[:-k]

    return "".join(stack[:m])

for bank in rows:
    p1.append(int(best_joltage(bank , 2)))
    p2.append(int(best_joltage(bank , 12)))

print(sum(p1))
print(sum(p2))
