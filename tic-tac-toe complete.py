board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def markBoard(position, mark):
    if position in range(1, 10):
        if board[position] == ' ':
            board[position] = mark
            return True
        else:
            print('Position already marked. Please choose any empty position.')
            return False
    else:
        print('Invalid position. Please choose a position between 1 and 9.')
        return False
    
def printBoard():
    print('{} | {} | {}'.format(board[1], board[2], board[3]))
    print('-----------')
    print('{} | {} | {}'.format(board[4], board[5], board[6]))
    print('-----------')
    print('{} | {} | {}'.format(board[7], board[8],board[9])) 

def validateMove(position):
    if position not in range(1, 10):
        print('Invalid position. Please choose a position between 1 and 9.')
        return False
    if board[position] != ' ':
        print('Position already occupied. Please choose an empty position.')
        return False
    return True

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

def checkWin(player):
    winCombinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
        ]
    
    for combination in winCombinations:
        if all(board[position] == player for position in combination):
            return True
        else:
            return False

def checkFull():
    for position in board.values():
        if position == ' ':
            return False
        else:
            return True

if checkFull():
    print('It"s a tie! The board is full.')
else:
    print('The game is still in progress.')





#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# Define the winning combinations
win_combinations = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
    [1, 5, 9], [3, 5, 7]  # Diagonals
]

# Function to print the game board
def print_board(board):
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('---+---+---')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('---+---+---')
    print(f' {board[7]} | {board[8]} | {board[9]} ')

# Function to check if the game is over and determine the result
def is_game_over(board, player):
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True  # The current player wins
    return ' ' not in board.values()  # It's a tie

# Game loop
while not gameEnded:
    print_board(board)

    move = input(currentTurnPlayer + "'s turn, input (1-9): ")

    if not move.isdigit() or int(move) not in range(1, 10) or board[int(move)] != ' ':
        print('Invalid input. Please choose an empty position between 1 and 9.')
        continue

    board[int(move)] = currentTurnPlayer

    if ' ' not in board.values():  # Check for a tie first
        print_board(board)
        print("It's a tie!")
        gameEnded = True
    elif is_game_over(board, currentTurnPlayer):
        print_board(board)
        print(currentTurnPlayer + " wins!")
        gameEnded = True

    currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
play_again = input("Do you want to play again? (yes/no): ").strip().lower()
if play_again != 'yes':
    play_game = False
