import random

# Define constants
BOARD_SIZE = 3
PLAYER_1_SYMBOL = "X"
PLAYER_2_SYMBOL = "O"

# Define the board as a 2D list of empty strings
board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board():
    """Print the current state of the board."""
    for row in board:
        print("|".join(row))

def get_winner():
    """Return the symbol of the winning player (if any) or None."""
    # Check rows
    for row in board:
        if all(cell == row[0] and cell != "" for cell in row):
            return row[0]
    # Check columns
    for j in range(BOARD_SIZE):
        if all(board[i][j] == board[0][j] and board[i][j] != "" for i in range(BOARD_SIZE)):
            return board[0][j]
    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] != "" for i in range(BOARD_SIZE)):
        return board[0][0]
    if all(board[i][BOARD_SIZE-1-i] == board[0][BOARD_SIZE-1] and board[i][BOARD_SIZE-1-i] != "" for i in range(BOARD_SIZE)):
        return board[0][BOARD_SIZE-1]
    # No winner yet
    return None

def get_move(player):
    """Ask the specified player for their move and return it."""
    while True:
        # Ask the player for their move
        move = input(f"{player}, enter your move as row,column: ")
        # Parse the move
        try:
            row, col = map(int, move.split(","))
        except ValueError:
            print("Invalid input, please enter row,column.")
            continue
        # Check that the move is valid
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            print("Invalid move, please choose a cell within the board.")
            continue
        if board[row][col] != "":
            print("Invalid move, that cell is already taken.")
            continue
        # Move is valid
        return row, col

def play_game():
    """Play a game of Tic-Tac-Toe."""
    # Initialize the board
    global board
    board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    # Choose the starting player
    current_player = random.choice([PLAYER_1_SYMBOL, PLAYER_2_SYMBOL])
    # Main game loop
    while True:
        print_board()
        # Get the current player's move
        row, col = get_move(current_player)
        board[row][col] = current_player
        # Check for a winner
        winner = get_winner()
        if winner is not None:
            print_board()
            print(f"{winner} wins!")
            return
        # Check for a tie
        if all(board[i][j] != "" for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
            print_board()
            print("Tie game!")
            return
        # Switch to the other player
        current_player = PLAYER_1_SYMBOL if current_player == PLAYER_2_SYMBOL else PLAYER_2_SYMBOL

# Play a game of Tic-Tac-Toe
play_game()
