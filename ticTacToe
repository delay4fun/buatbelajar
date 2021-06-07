# # # Tic Tac Toe part A

# #  | |   0
# # -----  1
# #  | |   2
# # -----  3
# #  | |   4


# def drawField(field):
#     for row in range(5): # 0,1,2,3,4
#         if row % 2 == 0:
#             # print writing line
#             for column in range(5): # 0,1,2,3,4
#                 if column % 2 == 0:
#                     if column != 4:
#                         print(' ', end ='')
#                     else:
#                         print(' ')
#                 else:
#                     print('|', end ='')
#         else:
#             print('-----')
# # drawField()
# player = 1
# currentField = [['','',''],['','',''],['','','']]
# print(currentField)
# while(True):
#     print('Players turn :',player)
#     moveRow = int(input('Please enter the row : '))
#     moveColumn = int(input('Please enter the coumn : '))
#     if player == 1:
#         # make move for player 1
#         currentField[moveColumn][moveRow] = 'X'
#         player = 2
#     else:
#         # make move for player 2
#         currentField[moveColumn][moveRow] = 'O'
#         player = 1
#     print(currentField)




# # Tic Tac Toe part B

#  | |   0
# -----  1
#  | |   2
# -----  3
#  | |   4


def drawField(field):
    for row in range(5): # 0,1,2,3,4
                         # 0,.,1,.,2
        if row % 2 == 0: # 0,2,4
            practicalRow = int(row / 2) # 0,1,2
            for column in range(5): # 0,1,2,3,4
                                    # 0,.,1,.,2
                if column % 2 == 0: # 0,2,4
                    practicalColumn = int(column / 2) # 0,1,2
                    if column != 4:
                        print(field[practicalColumn][practicalRow],end ='')
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print('|',end= '')
        else:
            print('-----')
# drawField()
player = 1
currentField = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
# print(currentField)
drawField(currentField)
while(True):
    print('Players turn :',player)
    moveRow = int(input('Please enter the row : \n'))
    moveColumn = int(input('Please enter the column : \n'))
    if player == 1:
        # make move for player 1
        if currentField[moveColumn][moveRow] == ' ':
            currentField[moveColumn][moveRow] = 'X'
            player = 2
    else:
        # make move for player 2
        if currentField[moveColumn][moveRow] == ' ':
            currentField[moveColumn][moveRow] = 'O'
            player = 1
    drawField(currentField)
    # print(currentField)

