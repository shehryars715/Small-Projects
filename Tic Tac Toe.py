def print_board(board):
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")

def check_win(board, player):
    win_conditions = [(0,1,2),(3,4,5),(6,7,8),
                      (0,3,6),(1,4,7),(2,5,8),
                      (0,4,8),(2,4,6)]
    for condition in win_conditions:
        if board[condition[0]]==board[condition[1]]==board[condition[2]]==player:
            return True
    return False

def comp_move(board):
    win_conditions = [(0,1,2),(3,4,5),(6,7,8),
                      (0,3,6),(1,4,7),(2,5,8),
                      (0,4,8),(2,4,6)]
    for cond in win_conditions:
                        if board[cond[0]] == 'O' and board[cond[1]] == 'O' and board[cond[2]] == " ":
                            return cond[2]
                        elif board[cond[0]] == 'O' and board[cond[2]] == 'O' and board[cond[1]] == " ":
                            return cond[1]
                        elif board[cond[2]] == 'O' and board[cond[1]] == 'O' and board[cond[0]] == " ":
                            return cond[0]
                        else: return random.randit(0,8)

def check_draw(board):
    for i in board:
        if i == " ":
            return False
    return True


def tic_tac_toe():
    board = [' ' for i in range(9)]
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    player = 'X'
    import random
    import time

    print("Welcome to the screen")
    print_board(board)

    while True:
        if player == 'X':
            move = int(input((f"Play your turn"))) - 1
            if board[move] != " ":
                print("This is filled, choose another number")
                continue
            board[move] = 'X'
            print(f"You played {move + 1}")
            print("Computer is thinking")
            time.sleep(2)

        elif player == 'O':
            for cond in win_conditions:
                sides = [0, 2, 6, 8]
                opposite_sides = {
                    "0": (2, 6),
                    "2": (0, 8),
                    "6": (0, 8),
                    "8": (6, 2)}
                if board[4] == ' ':
                    board[4] = 'O'
                    break
                elif board[cond[0]] == 'O' and board[cond[1]] == 'O' and board[cond[2]] == " ":
                    board[cond[2]] = 'O'
                    break
                elif board[cond[0]] == 'O' and board[cond[2]] == 'O' and board[cond[1]] == " ":
                    board[cond[1]] = 'O'
                    break
                elif board[cond[2]] == 'O' and board[cond[1]] == 'O' and board[cond[0]] == " ":
                    board[cond[0]] = 'O'
                    break
                elif board[cond[0]] == 'X' and board[cond[1]] == 'X' and board[cond[2]] == " ":
                    board[cond[2]] = 'O'
                    break
                elif board[cond[0]] == 'X' and board[cond[2]] == 'X' and board[cond[1]] == " ":
                    board[cond[1]] = 'O'
                    break
                elif board[cond[2]] == 'X' and board[cond[1]] == 'X' and board[cond[0]] == " ":
                    board[cond[0]] = 'O'
                    break
            else:
                while True:
                    x = random.choice(sides)
                    if board[x] == ' ':
                        board[x] = 'O'
                        break
            print_board(board)

        if check_win(board, player):
            if player == 'O':
                print("Computer won")
                break
            elif player == 'X':
                print("You won")
            break

        if check_draw(board):
            print("Draw")
            print_board(board)
            break

        player = 'O' if player == 'X' else 'X'


tic_tac_toe()