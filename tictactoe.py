"""
Software Construction and Development Lab no 2
Author: Muhammad Hashim
Dated: September 27, 2023
"""

def print_board(board):
    # Print the Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    # Check if the board is full
    return all([cell != ' ' for row in board for cell in row])

def get_move():
    while True:
        try:
            # Get user input for the next move
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8:
                return divmod(move, 3)  # Convert the move to row and column indices
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def tic_tac_toe():
    # Initialize the Tic-Tac-Toe board and current player
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")

    for _ in range(9):
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        row, col = get_move()

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_win(board, current_player):
                # Display the winning board and message
                print_board(board)
                print(f"Player {current_player} wins! Congratulations!")
                break
            elif is_full(board):
                # Display the final board and announce a draw
                print_board(board)
                print("It's a draw! Well played.")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That cell is already occupied. Try again.")

