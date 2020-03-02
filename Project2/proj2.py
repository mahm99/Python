# File: proj2.py
# Author: MAHMOOD UL MOHASIN AZIZ
# Description:
# This file contains python code for project2
# game reversi having two players, the user
# and the other computer itself.


# size to print board.
MAXX = 8

# input validation.
INPUT_VALID = ["0","1","2","3","4","5","6","7"]

# info to print the board.
BLANK_STR = "_"
ABS_BAR = "|"
BOARD_COLUMN = "_|0|1|2|3|4|5|6|7"

# current board statement.
B_MSG = "Current Board State: "

# player win statements.
WIN_PLAYER = "Player wins!"
WIN_COMPUTER = "Computer wins!"
TIE = "It's a Tie!"
GAME_OVER = "GAME OVER"

# score statements.
SCORE_PLAYER = "Player Score: "
SCORE_COMPUTER = "CPU Score: "

# move statements.
GET_MOVE = "Enter a move: "
CPU_MOVE = "CPU takes move: "
VALID_MOVE = "Valid moves are: "
INVALID_MOVE = "Invalid move. " + VALID_MOVE

# player symbols.
PLAYER_X = "X"
COMPUTER_O = "O"

##################### FUCNTIONS ##########################
##########################################################
# printBoard():  prints out the actual board for the game
#                using the 2D list.
# Parameters:    board; Takes in the 2d list.
# Return:        None;  Prints out the board.

def printBoard(board):

    # printing the message and top row
    # with column numbers.
    print(B_MSG)
    print(BOARD_COLUMN)

    # using for loop  to arrange the and print the
    # board and its pieces.
    for row in range(len(board)):
        print(str(row) + ABS_BAR + ABS_BAR.join(board[row]),end="")
        print(ABS_BAR)

##########################################################        
# buildBoard(): builds the gameboard to size specification.
#               Uses the length and the width to make 2d
#               list of the provided specification.
# Parameters:   maxx;   Length and width of the board.
# Return:       myList; A 2D list that is used as the
#                       board.

def buildBoard(maxx):

# Using lists to create the board.
    
    myList= []
    row = []

    # Using for loop to make a single row and column.
    for i in range(maxx):
        row.append(BLANK_STR)

    # Using the same list to make a 2D list of the
    # required length and width of the board.

    for j in range(maxx):
        myList.append(row[:])

    # setting the default peices.    
    myList[3][3] = PLAYER_X
    myList[3][4] = COMPUTER_O

    myList[4][3] = COMPUTER_O
    myList[4][4] = PLAYER_X

    # returning the 2D list.
    return myList

##########################################################
# validMove(): checks for the valid moves in the 2D list
#              that can be made on the board while playing
#              the game.
# Parameters:  board; Takes in the updates 2D list
#                     everytime.
#             player; Takes in the symbol of each player 
#                     to check valid moves availble for
#                     that specific player.
# Return:      valid; The list of valid moves.

def validMove(board, player):

# Using empty lists to conatain moves and arrange
# them in sequence.
    myMoves = []
    valid = []

# Using conditionals to check the players.

    if (player == PLAYER_X):
        checkMain = PLAYER_X
        checkSec = COMPUTER_O
    else:
        checkMain = COMPUTER_O
        checkSec = PLAYER_X

# Using for loop to check through every
# row and column.

    for row in range(len(board)):
        for column in range(len(board[row])):
            
            if (board[row][column] == checkMain):
                
            # This will check in the top direction.
                testUp = False
                rowUp = (row - 1)
                sameCol = column

                # Using while loop to iterate over the elements in top direction of the board.
                while((rowUp < (MAXX) and rowUp >= 0) and (board[rowUp][sameCol] == checkSec)):
                    testUp = True
                    rowUp -= 1

                # condition to check if its a valid move and append the move to the list.    
                if (rowUp < (MAXX) and rowUp >= 0) and (board[rowUp][sameCol] == BLANK_STR)\
                and testUp and ([rowUp, sameCol] not in myMoves):
                    myMoves.append([rowUp, sameCol])
                    
            # This will check in the left direction.
                testLeft = False
                sameRow = row
                colLeft = (column - 1)

                # Using while loop to iterate over the elements in left direction of the board.
                while((colLeft < (MAXX) and colLeft >= 0) and (board[sameRow][colLeft] == checkSec)):
                    testLeft = True
                    colLeft -= 1

                 # condition to check if its a valid move and append the move to the list. 
                if (colLeft < (MAXX) and colLeft >= 0) and (board[sameRow][colLeft] == BLANK_STR)\
                and testLeft and ([sameRow, colLeft] not in myMoves):
                    myMoves.append([sameRow, colLeft])
                
            # This will check in the right direction.
                testRight = False
                sameRow = row
                colRight = (column + 1)

                # Using while loop to iterate over the elements in  right direction of the board.
                while((colRight < (MAXX) and colRight >= 0) and (board[sameRow][colRight] == checkSec)):
                    testRight = True
                    colRight += 1

                # condition to check if its a valid move and append the move to the list.     
                if (colRight < (MAXX) and colRight >= 0) and (board[sameRow][colRight] == BLANK_STR)\
                and testRight and ([sameRow, colRight] not in myMoves):
                    myMoves.append([sameRow, colRight])
                    
            # This will check in the downward direction.
                testDown = False
                rowDown = (row + 1)
                sameCol = column

                # Using while loop to iterate over the elements in downnward direction of the board.
                while((rowDown < (MAXX) and rowDown >= 0) and (board[rowDown][sameCol] == checkSec)):
                    testDown = True
                    rowDown += 1
                # condition to check if its a valid move and append the move to the list.   
                if (rowDown < (MAXX) and rowDown >= 0) and (board[rowDown][sameCol] == BLANK_STR)\
                and testDown and ([rowDown, sameCol] not in myMoves):
                    myMoves.append([rowDown, sameCol])
    
   # arranging the valid moves in sequence. 
    for i in range(len(myMoves)):
        lowest = [MAXX, MAXX]
        for j in range(len(myMoves)):
            if (myMoves[j] < lowest):
                lowest = myMoves[j]
                location = j
                
        valid.append(lowest)
        myMoves = myMoves[:location] + myMoves[(location + 1):]
    
    # returning valid moves.
    return valid

##########################################################
# getInput():   Used to get the input from the user.
#               checks to see if the input is valid.
# Parameters:   moves;    A list of valid moves.
# Return:       choice;   A list of the chosen move from
#                         the shown valid moves.    
    
def getInput(moves):

# Using list to store the entered moves.    
    choice = []

# Printing the available valid moves.
    print(VALID_MOVE + str(moves))

    # Initializing the loop variable with boolean flag
    # to execute the loop.
    counter = True
    while counter != False:
        getVal = input(GET_MOVE).split()

        # using conditions for input valiation.
        if len(getVal) == 2 and getVal[0] in INPUT_VALID and getVal[1] in INPUT_VALID:
            x = int(getVal[0])
            y = int(getVal[1])

            # setting list to empty to delete the wrong moves
            # before append the new ones to the list to avoid errors.
            choice = []

            # appending rows and columns individually.
            choice.append(x)
            choice.append(y)

            # condition to check if the move is in the valid moves,
            # if not run loop again.
            if choice in moves:
                counter = False
            else:
                print(INVALID_MOVE + str(moves))
                counter = True
        # if does not satisy the first condition run the loop again.       
        else:
            print(INVALID_MOVE + str(moves))
            counter = True

    # returning a list of entered move.
    return choice

##########################################################
# playerTurn(): when its player turn print the valid moves,
#               and after getting the valid input makes
#               the move and flips symbols.
# Parameters:   listBoard; The main board with all the
#                          data about the pieces so far
#                          to make the move.
#               moves; the move chosen by the user.
# Return:       listBoard; The updated board with the
#                          players piece placed in the
#                          place chosen.

def playerTurn(listBoard,moves):

    # to get validated input.
    validate = getInput(moves)

    # to set the player piece at the entered move.
    listBoard[validate[0]][validate[1]] = PLAYER_X

    # calling to flipSymbol() to flip the pieces of
    # opponent player after the move is entered.
    flipSymbol(listBoard,validate,PLAYER_X) 

    # return the updated board.
    return listBoard

##########################################################
# computerTurn(): computer checks and makes a valid move.
# Parameters:     boardList; The main board with all the
#                            data about pieces so far.
# Return:         boardList; The updated board with the
#                            players piece placed in the
#                            place chosen.

def computerTurn(boardList):

    # to check the valid moves for CPU.
    cMoves = validMove(boardList, COMPUTER_O)

    # print the move taken by CPU.
    print(CPU_MOVE + str(cMoves[0]))

    # arrange the player piece at the chosen move.
    boardList[cMoves[0][0]][cMoves[0][1]] = COMPUTER_O

    # callig flipSymbol() to flip the pieces of
    # opponent player after the move is chosen.
    flipSymbol(boardList, cMoves[0], COMPUTER_O)

    # return the updated board.
    return boardList

##########################################################
# flipSymbol(): determines and the flips the tiles after 
#                each player's move is made.
# Parameters:   board;     takes in the board after every 
#                          players turn.
#               moveTaken; a list of moves chosen by each
#                          player.
#               player;    takes in player symbol to know 
#                          which player called and what
#                          symbol is supposed to be flipped. 


def flipSymbol(board, moveTaken, player):

# using list to store the move taken by players
# to flip pieces.
    flipLocation = []

    # condition to set the flip according to
    # according to the player.
    if player == PLAYER_X:
        flip = COMPUTER_O
    
    else:
        flip = PLAYER_X

    # setting row and column from the moveTaken list.
    row = moveTaken[0]
    column = moveTaken[1]
    
# This will check in the upward direction.
    testUp = False
    x = row - 1
    y = column

    # Using while loop to iterate over the elements in upward direction of the board.
    while((x < (MAXX) and x >= 0) and (board[x][y] == flip)):
        testUp = True
        x -= 1
    # if there is any spot to flip it the row and column number append to the list. 
    if (x < (MAXX) and x >= 0) and (board[x][y] == player) and testUp:
        flipLocation.append([x, y])
        
# This will check in the left direction.
    testLeft = False
    x = row
    y = column - 1

    # Using while loop to iterate over the elements in left direction of the board.
    while((y < (MAXX) and y >= 0) and (board[x][y] == flip)):
        testLeft = True
        y -= 1
    # if there is any spot to flip it the row and column number append to the list. 
    if (y < (MAXX) and y >= 0) and (board[x][y] == player) and testLeft:
        flipLocation.append([x, y])
                    
# This will check in the right direction.
    testRight = False
    x = row
    y = column + 1

    # Using while loop to iterate over the elements in right direction of the board.
    while((y < (MAXX) and y >= 0) and (board[x][y] == flip)):
        testRight = True
        y += 1

    # if there is any spot to flip it the row and column number append to the list.     
    if (y < (MAXX) and y >= 0) and (board[x][y] == player) and testRight:
        flipLocation.append([x, y])

# This will check in the downwards direction.
    testDown = False
    x = row + 1
    y = column

    # Using while loop to iterate over the elements in downnward direction of the board.
    while((x < (MAXX) and x >= 0) and (board[x][y] == flip)):
        testDown = True
        x += 1

    # if there is any spot to flip it the row and column number append to the list. 
    if (x < (MAXX) and x >= 0) and (board[x][y] == player) and testDown:
        flipLocation.append([x, y])


    
# Using for loops and conditions to flip the pices by utilizing
# the locations stored in the list.

    for i in range(len(flipLocation)):

        # checks if the row is the same then flips
        # all the valid spots in the column.
        if (moveTaken[0] == flipLocation[i][0]):

            if(moveTaken[1] < flipLocation[i][1]):

                for i in range(moveTaken[1], flipLocation[i][1]):
                    board[moveTaken[0]][i] = player

            else:
                for i in range(flipLocation[i][1], moveTaken[1]):
                    board[moveTaken[0]][i] = player

        # checks if the row is the same then flips                                                                                                                                                                 # all the valid spots in the column.
        else:

            if(moveTaken[0] < flipLocation[i][0]):

                for i in range(moveTaken[0], flipLocation[i][0]):
                    board[i][moveTaken[1]] = player
            else:
                for i in range(flipLocation[i][0], moveTaken[0]):
                    board[i][moveTaken[1]] = player

    # returning the updated board back to player that called flipSymbol().                
    return board

##########################################################
# checkScores(): determines the number of points each
#                player earned by counting the symbols in
#                the list and prints the scores.
# Parameters:    listBoard;   Takes in the board when the
#                             game is over.
# Return:        booleanWin;  Returns a statement
#                             containing who won the
#                             game.

def checkScores(listBoard):

    # initializing variables to 0 to add the scores. 
    scoreX = 0
    scoreO = 0
    
    index = 0

    # using while loops to count the pieces.
    while index < len(listBoard):
        count = 0
        
        while count < len(listBoard[index]):

            # condition to add the score for player.
            if PLAYER_X in listBoard[index][count]:
                scoreX += 1

            # condition to add the score for cpu.
            elif COMPUTER_O in listBoard[index][count]:
                scoreO += 1
            count += 1
        index += 1

    # storing the scores in a list and list index 0
    # is for player score and list index 1 for cpu score.
    playerScores = [scoreX,scoreO]

    # printing the scores of the player and cpu.
    print(SCORE_PLAYER + str(playerScores[0]))
    print(SCORE_COMPUTER + str(playerScores[1]))

    # calling checkWin to get the statement of who
    # won the game.
    booleanWin = checkWin(playerScores)
    
    return booleanWin

##########################################################
# checkWin():   Checks all the pieces and win patterns to 
#               determine if a player or computer won the 
#               game.
#               If won, prints who won.
# Parameters:   takeScore; Takes in the list of scores.
# Return:       WIN_PLAYER;    a string if user won.
#               WIN_COMPUTER;  a string if computer won.
#               TIE;           a string if it is a tie.

def checkWin(takeScore):

    # conditions to see who won the game
    # and return the statement accordingly.
    
    if(takeScore[0] > takeScore[1]):
         return WIN_PLAYER
        
    elif(takeScore[0] == takeScore[1]):
        return TIE
    
    else:
        return WIN_COMPUTER
    
################### MAIN FUNCTION ########################
##########################################################

def main():

    # intializing the loop vairiable.
    end = False

    # building the board.
    callBoard = buildBoard(MAXX)

    # running the loop.
    while end != True:

        # printing the board and calling valid moves.
        printBoard(callBoard)
        moves = validMove(callBoard, PLAYER_X)

    # conditions to check if there are any moves left after
    # each player's turn.

        # if there are no moves stop the loop.
        if (len(moves) <= 0):
            end = True

        # else keep running the loop and call playerTurn().
        else:
            play = playerTurn(callBoard, moves)
        
        # call validMoves again to check the moves.
        moves = validMove(callBoard, COMPUTER_O)

        # if there are no moves stop the loop.
        if (len(moves) <= 0) or end:
            end = True

        # else keep running the loop and call computerTurn(). 
        else:
            play = computerTurn(play)

    # print statements and scores after exiting the while loop.
    print(GAME_OVER)
    printBoard(play)
    score = checkScores(play)
    print(score)
    
main()
