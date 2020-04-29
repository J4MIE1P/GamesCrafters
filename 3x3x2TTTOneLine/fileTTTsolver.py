from TTT3D3by3by2 import *

f = open("HashedOneLine.txt", "r")
s = f.readline()
f.close()

def hashTTT(position):
    index = 0
    s = position[2:11] + position[12:21]
    for i in range(len(s)):
        if s[i] == "-":
            index += (3**i) * 0
        elif s[i] == "X":
            index += (3**i) * 1
        elif s[i] == "O":
            index += (3**i) * 2
    return index

def file_Solve(position):
    index = hashTTT(position)
    value = s[index]
    if value == "0":
        value = "lose"
    elif value == "1":
        value = "tie"
    elif value == "2":
        value = "win"
    else:
        print('uh oh weird')
    return value

board = initialPosition
file_Solve(board)
