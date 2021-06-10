

#  # Project #1: A Simple Game

# Details: 
# Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro company. 
# In this project, your task is create a Connect 4 game in Python. 
# Before you get started, please watch this video on the rules of Connect 4:

# https://youtu.be/utXzIFEVPjA

# Once you've got the rules down, your assignment should be fairly straightforward. 
# You'll want to draw the board, and allow two players to take turns placing their pieces on the board 
# (but as you learned above, they can only do so by choosing a column, not a row). 
# The first player to get 4 across or diagonal should win!
# Normally the pieces would be red and black, but you can use X and O instead.
'''
Extra Credit:
Want to try colorful pieces instead of X and O? 
First you'll need to figure out how to import a package like termcolor into your project. 
We're going to cover importing later in the course, 
but try and see if you can figure it out on your own. 
Or you might be able to find unicode characters to use instead, 
depending on what your system supports. Here's a hint: print(u'\u2B24')
'''

from time import sleep

instructions = "1-2-3-4-5-6-7"

# Create 7 column and 7 row
field = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],\
         [" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]   

def drawBoard(field):
    for row in range(13):
        if row % 2 == 0:
            tempRow = int(row / 2)
            for column in range(13):
                if column % 2 == 0:
                    tempCol = int(column / 2)                   
                    tile = field[tempCol][tempRow]
                    if column != 12:
                        print(tile, end = "") 
                    else:
                        print(tile) 
                else:
                    print("|", end = "")
        else:
            print("-------------")
    print(instructions)
    
def updateBoard(num, player):
    column = field[num]
    index = ""
    reverseCol = column[::-1]
    for row in reverseCol:
        if row == " ":
            index = reverseCol.index(row)
            reverseCol[index] = "X" if player == 1 else "O"
            break
    if index == "":
        return False
    column = reverseCol[::-1]
    field[num] = column
    drawBoard(field) 
    return True

def fourRow():
    win = False
    for column in field:
        counter = 0
        length = len(column)
        for i in range(1, length):
            if column[i - 1] != " " and column[i] != " " and column[i - 1] == column[i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                win = column[i - 1]
                return win    
    return win

def fourColumn(colMatrix):
    win = False
    for column in colMatrix:
        counter = 0
        length = len(column)
        for i in range(1, length):
            if column[i - 1] != " " and column[i] != " " and column[i - 1] == column[i]:
                 counter += 1
            else:
                counter = 0
            if counter == 3:
                win = column[i - 1]
                return win
    return win

def fourDiagonal(colMatrix, player):
    for i in range(0, len(colMatrix)):
        for j in range(0, len(colMatrix[i])):
            try:
                if (colMatrix[i][j] == player and colMatrix[i + 1][j - 1] == player \
                    and colMatrix[i + 2][j - 2] == player and colMatrix[i + 3][j - 3] == player) \
                    or (colMatrix[i][j] == player and colMatrix[i + 1][j + 1] == player \
                        and colMatrix[i + 2][j + 2] == player and colMatrix[i + 3][j + 3] == player):                    
                    return True
            except IndexError:
                next
    return False

def move(colNum):
    if colNum >= 1 and colNum <= 7:
        return True
    else:
        return False

def columnMatrix():
    colMatrix = [[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],\
                 [" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "]]   
    for i in range(7):
        for j in range(len(field[i])):
            colMatrix[i][j] = field[i][j]
    return colMatrix
    
def startConnect():
    player = 1
    lose = True
    win = ""
    while(lose):
        ask_column = 'Player' + ' ' + str(player) + ' ' + 'enter the number:\n'
        colNum = input(ask_column)
        if colNum:
            colNum = int(colNum)     
            if move(colNum) == False:
                print('This isn\'t a right move. Try again.\n')
            else:
                update = updateBoard(colNum - 1, player)
                if update:
                    print("")
                    currentPlayer = player
                    tile = "X" if player == 1 else "O"
                    player = 2 if player == 1 else 1
                    win = fourRow()
                    if win:
                        lose = False
                    else:
                        colMatrix = columnMatrix()
                        win = fourColumn(colMatrix)
                        if win:
                            lose = False
                        if fourDiagonal(colMatrix, tile):
                            win = currentPlayer
                            lose = False                              
                else:
                    print('This isn\'t a right move. Try again.\n')
        
    if win == "X":
        win = "1"
    else:
        win = "2"
    print('PLAYER' + ' ' + str(win) + ' ' + 'WIN\n')

print('Starting...\nGet ready!\n')
sleep(1)
drawBoard(field)
startConnect()
