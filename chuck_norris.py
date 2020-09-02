import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = "C"

binary = ""
for i in message:
    binary += bin(ord(i))[2:].zfill(7)

count = 1
items = []
size = len(binary)
for i in range(len(binary)):
    if i == len(binary) - 1:
        items.append([binary[i], count])
        continue

    if binary[i] == binary[i + 1]:
        count += 1
    elif binary[i] != binary[i + 1]:
        items.append([binary[i], count])
        count = 1


answer = ""
for i in items:
    if i[0] == "0":
        answer += "00 "
    elif i[0] == "1":
        answer += "0 "

    string = "0" * i[1]
    answer += string + " "

answer[:-1]

print(answer)
