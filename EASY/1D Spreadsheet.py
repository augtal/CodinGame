# What will i learn?
# Memoization, Lazy Evaluation, Dependency Graph

import sys
import math

input1 = "3"
input2 = ["VALUE 20 _", "ADD $0 100", "ADD $1 1"]

cells = []
n = int(input1)
for i in range(n):
    operation, arg_1, arg_2 = input2[i].split()
    cells.append([operation, arg_1, arg_2])

def calculations(cells, values, i):
    size = len(values)

    if len(cells) <= i:
        return

    operation, arg_1, arg_2 = cells[i]
    if arg_1[0] == "$" and arg_2[0] == "$":
        arg_1 = int(arg_1[1:])
        if arg_1 > size:
            calculations(cells, values, arg_1)
        else:
            arg_1 = values[arg_1]

        arg_2 = int(arg_2[1:])
        if arg_2 > size:
            calculations(cells, values, arg_2)
        else:
            arg_2 = values[arg_1]
    elif arg_1[0] == "$":
        arg_1 = int(arg_1[1:])
        if arg_1 > size:
            calculations(cells, values, arg_1)
        else:
            arg_1 = values[arg_1]
        
        arg_2 = int(arg_2)
    elif arg_2[0] == "$":
        arg_2 = int(arg_1[1:])
        if arg_2 > size:
            calculations(cells, values, arg_2)
        else:
            arg_2 = values[arg_2]
        arg_1 = int(arg_1)

    if operation == "ADD":
        values.append(int(arg_1) + int(arg_2))    

values = []
i = 1
if i <= len(values):
    pass
else:
    print("Uh oh")

#calculations()
"""
for i in range(n):
    operation, arg_1, arg_2 = cells[i]
    if arg_1[0] == "$" and arg_2[0] == "$":
        arg_1 = int(arg_1[1:])
        arg_1 = values[arg_1]

        arg_2 = int(arg_2[1:])
        arg_2 = values[arg_2]
    elif arg_1[0] == "$":
        arg_1 = int(arg_1[1:])
        arg_1 = values[arg_1]
        arg_2 = int(arg_2)
    elif arg_2[0] == "$":
        arg_2 = int(arg_2[1:])
        arg_2 = values[arg_2]
        arg_1 = int(arg_1)

    if operation == "VALUE":
        if arg_2 == "_":
            values.append(int(arg_1))
        else:
            values.append(int(arg_2))
    elif operation == "ADD":
        values.append(int(arg_1) + int(arg_2))
    elif operation == "SUB":
        values.append(int(arg_1) - int(arg_2))
    elif operation == "MULT":
        values.append(int(arg_1) * int(arg_2))
"""
    

for i in range(len(values)):
    print(values[i])