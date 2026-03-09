import math

board = [' ' for _ in range(9)]

def print_board():
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

def alphabeta(is_maximizing, alpha, beta):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                val = alphabeta(False, alpha, beta)
                board[i] = ' '
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                val = alphabeta(True, alpha, beta)
                board[i] = ' '
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = alphabeta(False, -math.inf, math.inf)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def play():
    print("Tic Tac Toe")
    print("You are X, AI is O")

    while True:
        print_board()
        user = int(input("Enter position (0-8): "))
        if board[user] != ' ':
            print("Invalid move")
            continue

        board[user] = 'X'

        if check_winner('X'):
            print_board()
            print("You Win!")
            break

        if is_draw():
            print_board()
            print("Draw!")
            break

        ai = best_move()
        board[ai] = 'O'
        print("AI chose:", ai)

        if check_winner('O'):
            print_board()
            print("AI Wins!")
            break

        if is_draw():
            print_board()
            print("Draw!")
            break

play()
