#A generic Tic Tac Toe solver.
#Change the variables on lines 15-19 to the values you want and run!

#Files need to have these variables and functions:
#initialPosition = "---------" (can change - to whatever, but position needs X and O characters in it)
#gameName = "Tic-Tac-Toe" (change to your game name!)
#def DoMove(position, move):
#def GenerateMoves(position):
#def PrimitiveValue(position):
#def WORMDoMove(position, move): (only if you want to do SYMMETRY = True)

import numpy as np
import matplotlib.pyplot as plt

from TicTacToe import * #Change TicTacToe to the name of the file to run!
SYMMETRY = True #Change to True if you have implemented symmmetries!
PRINTREMOTENESS = True #Change to True if you want to print remoteness statistics
GRAPHPOSITIONS = True #Change to True if you want to graph the number of positions x remoteness
GRAPHAVERAGE = True #Change to True if you want to graph the avg number of pieces x remoteness

if SYMMETRY:
    sym = "on"
else:
    sym = "off"
cache = {}
stats = {"lose": 0, "win": 0, "tie": 0}
p_stats = {"lose": 0, "win": 0, "tie": 0}
remoteWin = {}
remoteLose = {}
remoteTie = {}
remotenessStats = {}

primValue = PrimitiveValue
genMoves = GenerateMoves
doMove = DoMove
if SYMMETRY:
    doMove = WORMDoMove

def dictionary_add(dict, key, value):
    try:
        dict[key] += value
    except:
        dict[key] = value

def Solve(position):
    if position in cache:
        return cache[position]
    value, remoteness = help_Solve(position)
    cache[position] = (value, remoteness)
    stats[value] += 1
    if value == "win":
        winlosetie = (1, 0, 0)
    elif value == "lose":
        winlosetie = (0, 1, 0)
    elif value == "tie":
        winlosetie = (0, 0, 1)
    dictionary_add(remoteWin, remoteness, winlosetie[0])
    dictionary_add(remoteLose, remoteness, winlosetie[1])
    dictionary_add(remoteTie, remoteness, winlosetie[2])

    numX = position.count('X')
    numO = position.count('O')
    try:
        remotenessStats[remoteness][0] += numX
        remotenessStats[remoteness][1] += numO
        remotenessStats[remoteness][2] += 1
    except:
        remotenessStats[remoteness] = [numX, numO, 1]

    return (value, remoteness)

def help_Solve(position):
    value = primValue(position)
    if value == "not_primitive":
        remoteness = float("inf")
        lossRemoteness = 0
        for move in genMoves(position):
            childValue, childRemoteness = Solve(doMove(position, move))
            lossRemoteness = max(lossRemoteness, childRemoteness)
            if childValue == "lose":
                value = "win"
                remoteness = min(remoteness, childRemoteness)
            elif value != "win" and childValue == "tie":
                value = "tie"
                remoteness = min(remoteness, childRemoteness)
        if value != "win" and value != "tie":
            value = "lose"
            remoteness = lossRemoteness
        remoteness += 1
    else:
        p_stats[value] += 1
        remoteness = 0
    return (value, remoteness)

def print_remoteness():
    print(gameName + " analysis (symmetries is " + sym + ")")
    print("")
    print("Remote  Win     Lose    Tie     Total")
    print("----------------------------------------")
    r = max(remoteWin)
    while r >= 0:
        info = str(r).ljust(8) + str(remoteWin[r]).ljust(8) + str(remoteLose[r]).ljust(8) + str(remoteTie[r]).ljust(8)
        info = info + str(remoteWin[r] + remoteLose[r] + remoteTie[r]).ljust(8)
        print(info)
        r -= 1
    print("----------------------------------------")
    print("Total   " + str(sum(remoteWin.values())).ljust(8) + str(sum(remoteLose.values())).ljust(8) + str(sum(remoteTie.values())).ljust(8) + str(sum(remoteWin.values()) + sum(remoteLose.values()) + sum(remoteTie.values())))

    print("")
    print("Remote  Avg # of X     Avg # of O     Avg # of Both")
    print("---------------------------------------------------------")
    r = max(remoteWin)
    while r >= 0:
        info = str(r).ljust(8) + str(round(remotenessStats[r][0]/remotenessStats[r][2], 2)).ljust(15) + str(round(remotenessStats[r][1]/remotenessStats[r][2], 2)).ljust(15) + str(round((remotenessStats[r][0] + remotenessStats[r][1])/remotenessStats[r][2], 2)).ljust(15)
        print(info)
        r -= 1
    print("---------------------------------------------------------")

start = initialPosition
Solve(start)

def graph_num_remote():
    objects = range(max(remoteWin)+1)
    index = np.arange(len(objects))
    numWin = [remoteWin[obj] for obj in objects]
    numLose = [remoteLose[obj] for obj in objects]
    numTie = [remoteTie[obj] for obj in objects]
    numTotal = [remoteWin[obj] + remoteLose[obj] + remoteTie[obj] for obj in objects]

    fig, ax = plt.subplots()
    bar_width = 0.125
    opacity = 0.8

    rects1 = plt.bar(index, numWin, bar_width, alpha=opacity, color="b", label="Wins")
    rects2 = plt.bar(index + bar_width, numLose, bar_width, alpha=opacity, color="r", label="Losses")
    rects3 = plt.bar(index + 2*bar_width, numTie, bar_width, alpha=opacity, color="g", label="Ties")
    rects4 = plt.bar(index + 3*bar_width, numTotal, bar_width, alpha=opacity, color="k", label="Total")

    plt.xlabel("Remoteness")
    plt.ylabel("# of Positions")
    plt.title(gameName + " position analysis (symmetries is " + sym + ")")
    plt.xticks(index, objects)
    plt.legend()

    plt.tight_layout()
    plt.show()

def graph_avg_pieces():
    objects = range(max(remoteWin)+1)
    index = np.arange(len(objects))
    avgX = [round(remotenessStats[r][0]/remotenessStats[r][2], 2) for r in objects]
    avgO = [round(remotenessStats[r][1]/remotenessStats[r][2], 2) for r in objects]
    avgBoth = [round((remotenessStats[r][0] + remotenessStats[r][1])/remotenessStats[r][2], 2) for r in objects]

    fig, ax = plt.subplots()
    bar_width = 0.25
    opacity = 0.8

    rects1 = plt.bar(index, avgX, bar_width, alpha=opacity, color="b", label="X")
    rects2 = plt.bar(index + bar_width, avgO, bar_width, alpha=opacity, color="r", label="O")
    rects3 = plt.bar(index + 2*bar_width, avgBoth, bar_width, alpha=opacity, color="purple", label="Both")

    plt.xlabel("Remoteness")
    plt.ylabel("Average # of Pieces")
    plt.title(gameName + " average piece analysis (symmetries is " + sym + ")")
    plt.xticks(index, objects)
    plt.legend()

    plt.tight_layout()
    plt.show()

if PRINTREMOTENESS:
    print_remoteness()
if GRAPHPOSITIONS:
    graph_num_remote()
if GRAPHAVERAGE:
    graph_avg_pieces()
