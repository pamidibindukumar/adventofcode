import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


with open("ADC2025files/input_day6.txt", "r") as file:
    rows = file.read().split("\n")
    
# print(rows)
width = len(rows[0])
length = len(rows)


global_number = [] # add all the numbers based on right to left for each column part 2
for j in range(width-1,-1,-1):
    number = ''
    number_ = []
    for i in range(length-1):
        number+=rows[i][j]
    if number.strip() != '':
        number_.append(int(number))
    global_number.append(number_)
# print(global_number)

operations = rows[length-1].split()
operations.reverse()
# print(operations)

# below is to keep all numbers in single list for each column pat two
result = []
current = []

for item in global_number:
    if item == []:  # separator
        if current:
            result.append(current)
            current = []
    else:
        current.append(item[0])  # extract the number from [x]

# add last group if not empty
if current:
    result.append(current)

total_sum = 0
for i in range(len(operations)):
    if operations[i] == '*':
        total_sum += math.prod(result[i])
    else:
        total_sum += math.fsum(result[i])
    
print(f"Solution for part2 is {total_sum}")

'''
Below code is to solve for Part 1 solution
'''      
matrix = []
for i in rows:
    matrix.append(i.split())


m = len(matrix[0])
n = len(matrix)

all_add = 0
for j in range(m):
    operation = 1
    for i in range(n-1):
        if matrix[-1][j] == "*":
            operation = operation * int(matrix[i][j])
        if matrix[-1][j] == "+":
            operation = operation + int(matrix[i][j])
    if matrix[-1][j] == "+":
        operation = operation - 1
    # print(operation)
    all_add += operation

print(f"Part 1 Solution is {all_add}") # part 1 Solution


