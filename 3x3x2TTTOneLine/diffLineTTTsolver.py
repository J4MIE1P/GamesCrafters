initialPosition = "XO---------|---------"

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

def get_line(filepath, line_number):
    for i, row in enumerate(open(filepath)):
        if i == line_number:
            return row

def file_Solve(position):
    index = hashTTT(position)
    #do [:-1] to strip the \n character
    value = get_line("HashedDiffLines.txt", index)[:-1]
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
