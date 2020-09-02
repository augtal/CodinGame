import sys
import math


input1 = "5"
input2 = "1"

input3 = ["0.0.0"]

width = int(input1)  # the number of cells on the X axis
height = int(input2)  # the number of cells on the Y axis

lines = []
for i in range(height):
    line = list(input3[i])  # width characters, each either 0 or .
    lines.append(line)


def findNodes(board, cur_pos):
    cur_y, cur_x = cur_pos
    answer = ""
    for x in range(cur_x + 1, width + 1):
        if x == width:
            answer += "-1 -1 "
            break
        elif board[cur_y][x] == ".":
            continue
        elif board[cur_y][x] == "0":
            answer += f"{x} {cur_y} "
            break

    for y in range(cur_y + 1, height + 1):
        if y == height:
            answer += "-1 -1"
            break
        elif board[y][cur_x] == ".":
            continue
        elif board[y][cur_x] == "0":
            answer += f"{cur_x} {y}"
            break

    return answer


for y in range(height):
    for x in range(width):
        cords = ""
        if lines[y][x] == "0":
            cords += f"{x} {y} "
            cords += findNodes(lines, (y, x))
            print(cords)
        else:
            continue
