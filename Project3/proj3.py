# File: proj3.py
# Author: MAHMOOD UL MOHASIN AZIZ
# Description: This  file contains the python program code
# which runs the minesweeper game, using loops, two dimensional lists,
# calling functions and recursion to solve the board.

############################### CONSTANTS ###################################

# start message.
BEGIN_MSG = "\tThis program allows you to play Minesweeper.\n\tThe object of the \
game is to flag every mine,\n\tusing clues about the number of neighboring \n\tmines \
in each field.  To win the game, flag\n\tall of the mines (and don't incorrectly flag \
\n\tany non-mine fields).  Good luck!"

# get file message.
GET_FILE = "\nEnter the file to load the board from: "

# row and columns messages.
CHOOSE_ROW = "Please choose a row: "
CHOOSE_COL = "Please choose the column: "

GET_ROW_COL = "Enter a number between 1 and "
INC = " (inclusive): "

# reveal and flag messages.
R_AND_F = "Enter 'r' to reveal the space, or \nenter 'f' to mark the space with flag: "
F_RMVD = "\tFlag removed from "

# error messages.
ERROR = "This number is not allowed. Please try again!"
NOT_VALID = "\tThat's not a valid action." 

# win and lost message.
WIN_MSG = "You won! Congratulations, and good game!"
LOST_MSG = "You detonated a mine! Game Over!"

# input validation.
MINN = 1

# characters that will be used for input validation.
ROW = "R"
COL = "C"

# characters.
FLAG = "f"
REVEAL = "r"

MINE = "*"
DET = "X"

FLAGGED = "F"
BORDER = "#"

DOT = "."
EMPTY = ""
NEW_LINE = "\n"
SPACE = " "

#####################################################################################
# fileExecute():        reads a file, and converts the file lines into a 2D list.
# Parameters:           None;     opens the file with in the fucntion.
# Return:               newList;  a 2D list containing the board.

def fileExecute():
    
    # the list where the intial board will be contained.
    newList = []
    
    # printing the statement.
    print(BEGIN_MSG)    
    # getting file name.
    getInput = input(GET_FILE)
    
    # opening and reading the file.
    openFile = open(getInput)
    readLine = openFile.readline()
    
    # running the loop to read line after line.
    while readLine != EMPTY:
        
        # list to contain every single character.
        myList = []
        
        # running for loop to add every single character.
        for i in range(len(readLine)):
            
            # condition to avoid adding "\n" to the list.
            if readLine[i] != NEW_LINE:
                myList.append(readLine[i])
        
        # adding up the line of characters as a 2d list. 
        if len(myList) != 0:
            newList.append(myList)
        readLine = openFile.readline()
    
    # closing the file once the loop ends.
    closeFile = openFile.close()
    
    return newList

#####################################################################################
# prettyPrintBoard():   prints the board with row and column labels,  and spaces the
#                       board out so that it looks square.
# Parameters:           board;   the rectangular 2d gameboard to print.
# Return:               None;    prints the board in a pretty way.
    
def prettyPrintBoard(board):
    
    print() # empty line

    # if enough columns, print a "tens column" line above
    if len(board[0])-2 >= 10:
        print("{:25s}".format(""), end="")  # empty space for 1 - 9
        for i in range(10, len(board[0])-1 ):
            print( str(i // 10), end =" ")
        print()

    # create and print top numbered line
    print("       ", end="")
    
    # only go from 1 to len - 1, so we don't number the borders
    for i in range(1, len(board[0])-1 ):
        
        # only print the last digit (so 15 --> 5)
        print(str(i % 10), end = " ")
    
    print()

    # create the border row
    borderRow = "     "
    for col in range(len(board[0])):
        borderRow += board[0][col] + " "

    # print the top border row
    print(borderRow)

    # print all the interior rows
    for row in range(1, len(board) - 1):
        
        # print the row label
        print("{:3d}  ".format(row), end="")

        # print the row contents
        for col in range(len(board[row])):
            print(str(board[row][col]), end = " ")
        print()

    # print the bottom border row and an empty line
    print(borderRow, NEW_LINE)
    
#####################################################################################
# arrangeBoard():       makes a hard copy of the actual board and replaces empty
#                       spaces and mines with dots.
# Parameters:           board;     the actual board chosen by the user.
# Return:               gameBoard; a 2D list of board that will be used while playing
#                                  the game.

def arrangeBoard(board):

    # 2D list that will hold the deep copy of actual 
    # board replaced by dots(game board).
    gameBoard = []
    
    # using for loop to go through the 2D list of actual board.
    for x in range(len(board)):
        
        # list that will hold a row at a time.
        myList = []
        
        for y in range(len(board[x])):
            
            # using conditions to  replace with dots.
            if board[x][y] == BORDER:
                myList.append(board[x][y])
            
            else:
                myList.append(DOT)    
        
        # appending the row to final 2D list after replacing
        # and setting the row list to empty after each row.
        gameBoard.append(myList[:])
        myList = []

    return gameBoard

#####################################################################################
# inputValidation():    prompts the user for an input and checks if it is a valid
#                       one.
# Parameters:           message; a character to determine if its a row call or column
#                                call. 
#                       board;   the board to get available values.
# Return:               move;    the valid row and column.

def inputValidation(message, board):
    
    # printing messages using conditionals.
    if (message == ROW):
        print(CHOOSE_ROW)
    else:
        print(CHOOSE_COL)
        
    # using conditionals to get valid row and column number.    
    if (message == ROW):
        getInput = int(input(GET_ROW_COL + str(len(board)-2) + INC))
        
        # running loop check if the entered row value is valid.
        while (getInput < MINN) or (getInput > (len(board)-2)):
            
            # print error message if input is not valid.
            print(ERROR)
            getInput = int(input(GET_ROW_COL + str(len(board)-2) + INC))
        
    else:
        getInput = int(input(GET_ROW_COL + str(len(board[0]) - 2) + INC))
        
        # running loop check if the entered column value is valid.
        while (getInput < MINN) or (getInput > (len(board[0]) - 2)):
            
            # print error message if not input is not valid.
            print(ERROR)
            getInput = int(input(GET_ROW_COL + str(len(board[0]) - 2) + INC))
    
    return getInput

#####################################################################################
# revealOrFlag():       determines whether to reveal or flag based on the user input.
# Parameters:           None;    it is only to get the right input from the user.
# Return:               choice;  the letter chosen by the user.

def revealOrFlag():
    
    # getting user choice whether to reveal or flag from the user.
    choice = input(R_AND_F)
    
    # loop checking if the entered input is valid, and if not keep
    # running the loop until the user enters the right input.
    index = 0
    while index != 1:

        if (choice != REVEAL) and (choice != FLAG):
            # printing error message if invalid input and setting index to 0.
            print(NOT_VALID)
            choice = input(R_AND_F)
            index = 0
            
        else:
            index = 1
    
    return choice

#####################################################################################
# checkWin():           determines if the player has won or lost the game.
# Parameters:           actualBoard;  the board in the beginning with mines.
#                       playedBoard;  the board after the user had made the move.
# Return:               winner;       a boolean value ruling if the game was won or lost.

def checkWin(actualBoard, playedBoard):
    
    # initializing variables that return boolean
    # flags according to the conditionals.
    winner = True
    lost = False
    
    # running loop to iterate over the 2D list.
    for x in range(len(actualBoard)):        
        
        # running loop to iterate over each element of the 2D list.
        for y in range(len(actualBoard[x])):
            
            # conditionals checking if the flags are placed correctly, and
            # if not returns false.
            if actualBoard[x][y] == MINE and playedBoard[x][y] != FLAGGED:
                return lost
            
            elif actualBoard[x][y] != MINE and playedBoard[x][y] == FLAGGED:
                return lost

    # returning true if the user won.
    return winner

#####################################################################################
# numberBoard():        determines where to place the number clues on the board.
# Parameters:           board;    takes in the board as 2D list.
# Return:               numberedboard; the updated board with number clues..

def numberBoard(board):
    
    # a list that will hold numbered board copy 
    # and will return it at the end.
    numberedBoard = []
    
    # initializing for loops to access each element of the 2D list
    # of actual board.
    for x in range(len(board)):
        
        # a list that will hold a row at a time
        numRow = []
        
        for y in range(len(board[x])):
            
            # initializing variable that will hold the clue values.
            clues = 0
            

            if (board[x][y] != BORDER) and (board[x][y] != MINE):
            
            
                    
                # conditions to check in every direction and if there is a mine
                # add up the clue value by one.
                
                if (board[x][y-1] == MINE):
                    clues += 1
                        
                if (board[x-1][y] == MINE):
                    clues += 1
                        
                if (board[x][y+1] == MINE):
                    clues += 1
                        
                if (board[x+1][y] == MINE):
                    clues += 1
                        
                if (board[x+1][y+1] == MINE):
                    clues += 1
                    
                if (board[x+1][y-1] == MINE):
                    clues += 1
                    
                if (board[x-1][y+1] == MINE):
                    clues += 1
                        
                if (board[x-1][y-1] == MINE):
                    clues += 1
                
                # if any of the above conditions are satisified and the value is greater
                # than 0 before moving to next column, append that clue value in place 
                # of the checked column.
                if (clues > 0):
                    numRow.append(clues)
                
                # if not append the space.
                else:
                    numRow.append(SPACE)
            
            # to append the borders and mines back.     
            else:
                
                if (board[x][y] == MINE):
                    numRow.append(MINE)
            
                elif (board[x][y] == BORDER):
                    numRow.append(BORDER)
        
        # appending the list of rows to the 2D list that will be returned.     
        numberedBoard.append(numRow)
                    
    return numberedBoard

#####################################################################################
# countMines():         determines how many mines are still left on the board after
#                       the player move.
# Parameter:            takeBoard;  the played board after the move.
# Return:               count;      the number of remaining mines on the board.

def countMines(initialBoard, takeBoard):
    
    # initializing variable that will hold 
    # the number of mines.
    count = 0
    
    # running a for loop to access the rows.
    for x in range(len(initialBoard)):
        
        # running a for loop to iterate over every
        # single column in a row.
        for y in range(len(initialBoard[x])):
            
            # using conditional to add up the number of
            # mines on actual board.
            if (initialBoard[x][y] == MINE):
                count += 1
            
            # using conditional to subtract the number of
            # mines if the playing board has a flag on it.    
            if (takeBoard[x][y] == FLAGGED):
                count -= 1
                
    return count

#####################################################################################
# recurIsland():        determines where the island is on the board using recursion.
# Parameters:           row;       the row where user took the move.
#                       col;          the column where user took the move.
#                       board;        the ongoing game board.
#                       actualBoard;  the actual board.
# Return:               board;        the updated game board with island in place.

def recurIsland(row, col, board, actualBoard):
    
    # base case.
    if (actualBoard[row][col] == BORDER) and (actualBoard[row][col] == MINE):

        return board
    
    # recursive case.
    else:
        
        # updating the board every time entering the recursive case.
        board[row][col] = actualBoard[row][col] 
        
        # if the game board column is a space.
        if board[row][col] == SPACE:
            
            # check row above is a DOT and row value is greater than 0 then, recursively checking
            # and updating the rows above accordingly.
            if (board[row-1][col] == DOT) and (row - 1 >= 0):
                board = recurIsland((row - 1), col, board, actualBoard)

            # check row below is a DOT and row value is less than the board length, then recursively checking
            # and updating the island.
            if board[row+1][col] == DOT and (row + 1 < len(board)):
                board = recurIsland((row + 1), col, board, actualBoard)
            
            # check row above and col on right is a DOT and row value is greater than 0, and col on right 
            # is less than the length of the row then, recursively checking and updating the island.
            if (board[row-1][col+1] == DOT) and (row - 1 >= 0) and (col + 1 < len(board[row])):
                board = recurIsland((row - 1), (col + 1), board, actualBoard)
                
            # check row below and col on right is a DOT and row value is less than board length, and col on right 
            # is less than the length of the row then, recursively checking and updating the island.
            if (board[row+1][col+1] == DOT) and (row + 1 < len(board)) and (col + 1 < len(board[row])):
                board = recurIsland((row + 1), (col + 1), board, actualBoard)
                
            # check if left columns is a DOT and col value is greater than 0 then, recursively checking
            # and updating the island.
            if (board[row][col-1] == DOT) and (col - 1 >= 0):
                board = recurIsland(row, (col - 1), board, actualBoard)
            
            # check if right columns is a DOT and col value is less than row length then, recursively checking
            # and updating the island.
            if (board[row][col+1] == DOT) and (col+1 < len(board[row])):
                board = recurIsland(row, (col + 1), board, actualBoard)
            
            # check row above and col on left is a DOT and row value is greater than 0, and col on left 
            # is greater than 0 then, recursively checking and updating the island.
            if (board[row-1][col-1] == DOT) and (row - 1 >= 0) and  (col - 1 >= 0):
                board = recurIsland((row - 1), (col - 1), board, actualBoard)

            # check row below and col on left is a DOT and row value is less than board length, and col on left 
            # is greater than 0 then, recursively checking and updating the island.
            if (board[row+1][col-1] == DOT) and (row + 1 < len(board)) and (col - 1 >= 0):
                board = recurIsland((row + 1), (col - 1), board, actualBoard)
                
    return board

#####################################################################################
# changeBoard():        updates all the characters in place after every move.
# Parameters:           row;          the row chosen by the user.
#                       col;          the column chosen by the user.
#                       choice;       user chosen character.
#                       currentBoard; the board where game is being played.
#                       actualBoard;  the actual board with mines.
# Return:               currentBoard; the game board with updated peices.

def changeBoard(row, col, choice, currentBoard, actualBoard):
    
    # condition checking to reveal the spot and update the game board.
    if (choice == REVEAL) and (actualBoard[row][col] != MINE) and (actualBoard[row][col] != BORDER):
        currentBoard[row][col] = actualBoard[row][col]
    
    # condition to flag a spot and update the game board.
    elif (choice == FLAG) and (currentBoard[row][col] != FLAGGED):
        currentBoard[row][col] = FLAGGED
    
    # condition to unflag the spot and update the game board.    
    elif (choice == FLAG) and (currentBoard[row][col] == FLAGGED):
        currentBoard[row][col] = DOT
    
    # condition to reveal the detonated spot and update the game board.
    elif (choice == REVEAL) and (actualBoard[row][col] == MINE):
        currentBoard[row][col] = DET
        
    return currentBoard

#####################################################################################
# gamePlay():        determines the revealing, and flagging part of the game play.
# Parameters:        row;         the user entered row.
#                    col;         the user entered column.
#                    choice;      a character entered by the user to reveal or flag.
#                    playBoard;   the board where game is being played.
#                    actualBoard; the actual board.
# Return:            loopStop;    a boolean flag, if the user lost.
#                    playBoard;   the updated board on which the game is being played.
    
def gamePlay(row, col, choice, playBoard, actualBoard):
    
    # initializing variable with a boolean value to
    # return if the user has revealed a mine, helping stop the game.
    loopStop = True
    
    # if user has chosen to reveal and that column has a mine then the user lost.
    if (choice == REVEAL) and (actualBoard[row][col] == MINE):
        
        # updating board with a detonated mine and printing the lost message out and
        # returning the boolean flag.
        playBoard = changeBoard(row, col, choice, playBoard, actualBoard)
        prettyPrintBoard(playBoard)
        print(LOST_MSG)
        return loopStop
    
    # if user has chosen to reveal and the column is already flagged by the user
    # printing the board and letting the user know that it must be unflagged first.
    elif (choice == REVEAL) and (playBoard[row][col] == FLAGGED):
        
        prettyPrintBoard(playBoard)
        print("\tField " + str(row) + ", " + str(col) + " must be unflagged before it can be revealed.")
    
    # if the user has chosen to reveal and the column is a empty space, then calling
    # recursive island function to check there is a island around the revealed space 
    # and update the board accordingly.
    elif (choice == REVEAL) and (actualBoard[row][col] == SPACE):
            
        playBoard = recurIsland(row, col, playBoard, actualBoard)
        prettyPrintBoard(playBoard)
        
    # if the user has chosen to flag the column and the column is already flagged,
    # then updating board and printing the board and also checking if the user has
    # won or not.
    elif (choice == FLAG) and (playBoard[row][col] == FLAGGED):
        
        playBoard = changeBoard(row, col, choice, playBoard, actualBoard)
        prettyPrintBoard(playBoard)
        
        # checking for the win to stop the game.
        makeSure = checkWin(actualBoard, playBoard) 
        
        # if not win then print the message flag removed.
        if (makeSure != loopStop) :
            print(F_RMVD + str(row)+  ", " + str(col) + DOT)
    
    # everything else update and print the board after each move accordingly.
    else:
        playBoard = changeBoard(row, col, choice, playBoard, actualBoard)
        prettyPrintBoard(playBoard)
        
    return playBoard
    
def main():
    
    # calling function to open and read the file.
    initialBoard = fileExecute()

    # calling and sending in the board to set the number clues 
    # on actual board.
    numberKey = numberBoard(initialBoard)
    
    # calling function and sending in the board to make a deep copy of the
    # board and replace everything with the DOTS.
    arrange = arrangeBoard(numberKey)

    # printing out the board.
    prettyPrintBoard(arrange)
    
    # calling the function and printing the number of mines.
    count = countMines(initialBoard, numberKey)
    print("\tThere are " + str(count) + " mines left to find\n")
    
    # setting the loop variable to run the loop and boolean
    # variable that will be used in the loop to stop the loop.
    index = 0
    loopStop = True
    
    # running the loop.
    while index != 1:
        
        # calling function to get the valid input from user for
        # both row and columns.
        getRow = inputValidation(ROW, initialBoard)
        getColumn = inputValidation(COL, initialBoard)
        
        # calling function to get the valid input from user whether
        # to reveal or flag.
        getChoice = revealOrFlag()
        
        # after getting the row,col & choice from the user calling the function
        # that will handle the moves accordingly.
        callPlay = gamePlay(getRow, getColumn, getChoice, arrange, numberKey)
        
        
        # if the recent called function returns true the loop will end
        # and a lost message will be printed out.
        if (callPlay == loopStop):
            index = 1
        
        # if it is not equal to true the game will continue.
        elif (callPlay != loopStop):

            # calling the function to check if the user won the game.
            winner = checkWin(numberKey, callPlay)

            # if won it will print the won message and end the loop.
            if (winner == loopStop):
                print(WIN_MSG)
                index = 1

            # if not then it will check the mines left and keeps the
            # game running.
            else:
                count = countMines(numberKey, callPlay)
                print("\tThere are " + str(count) + " mines left to find\n")
                index = 0

main()
