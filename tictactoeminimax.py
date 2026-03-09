import math

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board():
    for row in board:
        print("|".join(row))
        print("-"*5)

def check_winner():
    # rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def is_moves_left():
    for row in board:
        if ' ' in row:
            return True
    return False


def minimax(is_max):
    winner = check_winner()

    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif not is_moves_left():
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(False))
                    board[i][j] = ' '
        return best

    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(True))
                    board[i][j] = ' '
        return best


def best_move():
    best_val = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(False)
                board[i][j] = ' '

                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val

    board[move[0]][move[1]] = 'O'


def play():
    while True:
        print_board()

        x = int(input("Enter row (0-2): "))
        y = int(input("Enter col (0-2): "))

        if board[x][y] == ' ':
            board[x][y] = 'X'
        else:
            print("Invalid move")
            continue

        if check_winner() or not is_moves_left():
            break

        best_move()

        if check_winner() or not is_moves_left():
            break

    print_board()

    winner = check_winner()
    if winner:
        print("Winner:", winner)
    else:
        print("Draw")


play()
