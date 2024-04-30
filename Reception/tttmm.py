import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def evaluate(board):
    # Check rows
    for row in board:
        if row.count("X") == 3:
            return 10
        elif row.count("O") == 3:
            return -10
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == "X":
                return 10
            elif board[0][col] == "O":
                return -10
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return 10
        elif board[0][0] == "O":
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return 10
        elif board[0][2] == "O":
            return -10
    
    # No winner
    return 0

def is_moves_left(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return True
    return False

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score - depth
    elif score == -10:
        return score + depth
    elif not is_moves_left(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = True

    print("Let's play Tic Tac Toe!\n")
    print_board(board)

    while is_moves_left(board):
        if player_turn:
            row, col = map(int, input("Enter row and column (0-2): ").split())
            if board[row][col] != " ":
                print("Cell already occupied. Try again.")
                continue
            board[row][col] = "O"
        else:
            print("AI's turn:")
            row, col = find_best_move(board)
            board[row][col] = "X"

        print_board(board)
        winner = evaluate(board)
        if winner != 0:
            if winner == 10:
                print("AI wins! Better luck next time.")
            else:
                print("Congratulations! You win!")
            return
        player_turn = not player_turn
    
    print("It's a draw!")

play_game()
