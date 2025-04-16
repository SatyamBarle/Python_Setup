import math

# Function to print the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for winner
def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if moves are left
def moves_left(board):
    return any(cell == ' ' for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if not moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best

# Function to find the best move for AI (O)
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Main driver
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Tic-Tac-Toe Game (You: X, AI: O)")
    print_board(board)

    while moves_left(board):
        # Player move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Invalid move! Try again.")
            continue

        print_board(board)

        if check_winner(board, 'X'):
            print("Congratulations! You win.")
            return

        if not moves_left(board):
            print("It's a draw!")
            return

        # AI move
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'O'
        print("\nAI has made its move:")
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            return

    print("It's a draw!")

# Start the game
play_game()
