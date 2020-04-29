#Code for the game Tic Tac Toe
#Blank spaces are -, the first player is X, and the second player is O.
#Index 0 is reserved for the player whose turn it is, X or O.
#Index 1 is reserved for the player whose turn it will be next, O or X.

initialPosition = "XO---------|---------"
# Position indices are represented as
# Player move: 0
# Next Player: 1
#     Top layer:   [[2,3,4],
#                   [5,6,7],
#                   [8,9,10]]
#     Bottom Layer:[[12,13,14],
#                  [15,16,17],
#                  [18,19,20]]


#Returns a new position, the result of making the given move from the given position
#Requires: position is not a primitive position and move is a legal move from position
def DoMove(position, move):
    return move

#Returns the set of moves avaliable from the position
#Requires: position is not a primitive position
def GenerateMoves(position):
    moves = []
    for i in range(2, len(position)):
        if position[i] == "-":
            moves.append(position[1] + position[0] + position[2:i] + position[0] + position[i+1:])
    return moves

#If the position is primitive, then based on win/lose/tie conditions, return its value
#If the position is not primitive, return not_primitive
def PrimitiveValue(position):
    for i in [2, 5, 8, 12, 15, 18]: #check rows for 3 in a row
        if position[i] != "-" and position[i] == position[i+1] == position[i+2]:
            return "lose"
    for i in [2, 3, 4, 12, 13, 14]: #check columns for 3 in a row
        if position[i] != "-" and position[i] == position[i+3] == position[i+6]:
            return "lose"
    if position[6] != "-": #check diagonals for 3 in a row
        if position[2] == position[6] == position[10] or position[4] == position[6] == position[8]:
            return "lose"
    if position[16] != "-": #check diagonals for 3 in a row
        if position[12] == position[16] == position[20] or position[14] == position[16] == position[18]:
            return "lose"
    if "-" not in position: #the board is full
        return "tie"
    return "not_primitive"

#Reduces a move to its simplest form in all possible rotations and mirrors
def WORMDoMove(position, move):
    permutations = []
    permutations.append(move)
    permutations.append(mirror(move))
    p = move
    for i in range(3):
        p = rotateX(p)
        permutations.append(p)
        pm = mirror(p)
        permutations.append(pm)
    return min(permutations)

def mirror(position):
    return position[0:2] + position[4] + position[3] + position[2] + position[7] + position[6] + position[5] + position[10] + position[9] + position[8] + position[11]+ position[14] + position[13] + position[12] + position[17] + position[16] + position[15] + position[20] + position[19] + position[18]

def rotateX(position):
    return position[0:2] + position[8] + position[5] + position[2] + position[9] + position[6] + position[3] + position[10] + position[7] + position[4] + position[11] + position[18] + position[15] + position[12] + position[19] + position[16] + position[13] + position[20] + position[17] + position[14]
