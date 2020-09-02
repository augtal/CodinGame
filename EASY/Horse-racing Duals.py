import sys
import math

input1 = "3"
input2 = ["5", "8", "9"]

n = int(input1)

horse_stren = []
D = None
for i in range(n):
    pi = int(input2[i])
    horse_stren.append(pi)

horse_stren.sort()

for i in range(len(horse_stren) - 1):
    strength = abs(horse_stren[i] - horse_stren[i + 1])
    if D is None:
        D = strength
    else:
        if D > strength:
            D = strength

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("answer")
