# The Game Board
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    if position in board:
        board[position] = mark

# TODO: print the game board as described at the top of this code skeleton
def printBoard():
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[7] + " | " + board[8] + " | " + board[9])
    
# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
def validateMove(position):
    pos = int(position)
    if pos < 1 or pos > 9:
        return False
    if board[pos] != ' ':
        return False
    return True

# TODO: list out all the combinations of winning
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

# TODO: implement a logic to check if the previous winner just win
def checkWin(player):
    for combo in winCombinations:
        combo_matched = True
        for position in combo:
            if board[position] != player:
                combo_matched = False
                break
        if combo_matched:
            return True
    return False


# TODO: implement a function to check if the game board is already full
def checkFull():
    for position in board:
        if board[position] == ' ':
            return False
    return True

# Function to reset the game board
def resetBoard():
    for key in board.keys():
        board[key] = ' '


#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################


def playGame():
    gameEnded = False
    currentTurnPlayer = 'X'

# Entry point of the whole program
    print('Game started: \n\n' +
            ' 1 | 2 | 3 \n' +
            ' --------- \n' +
            ' 4 | 5 | 6 \n' +
            ' --------- \n' +
            ' 7 | 8 | 9 \n')

        # Complete the game play logic below
        # Reference the following flow:
        # 1. Ask for user input and validate the input
        # 2. Update the board
        # 3. Check win or tie situation
        # 4. Switch User

    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9:
                if validateMove(move):
                    markBoard(move, currentTurnPlayer)
                    printBoard()
                    if checkWin(currentTurnPlayer):
                        print(currentTurnPlayer +  " wins!")
                        gameEnded = True
                    elif checkFull():
                        print("It's a tie!")
                        gameEnded = True
                    else:
                        if currentTurnPlayer == 'X': 
                            currentTurnPlayer = 'O' 
                        else :
                            currentTurnPlayer = 'X'
                else:
                    print("Invalid move. The position is already occupied.")
            else:
                print("Invalid move. Enter a number between 1 and 9.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

    restart = input("Do you want to play again? (Y/N): ")
    if restart == ('Y'or 'Yes' or 'yes' or 'YES'):
        resetBoard()
        playGame()
    else:
        print("Thanks for playing!")

# Start the game
playGame()
