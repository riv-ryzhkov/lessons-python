def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 10)


def check_winner(board, player):
    """Check if the current player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    """Check if the board is full."""
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    """Play a game of Tic-Tac-Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)

        # Get the player's move
        row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))

        # Check if the chosen cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move. The cell is already occupied. Try again.")
            continue

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break

        # Check if the board is full (a tie)
        if is_board_full(board):
            print_board(board)
            print("It's a tie! The board is full.")
            break

        # Switch to the other player for the next turn
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()