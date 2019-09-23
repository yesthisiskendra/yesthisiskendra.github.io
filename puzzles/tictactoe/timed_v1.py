# TIMED V1:
# -- only calculating horizontal
# -- not optimized
# --------------
# make gameboard
# get input
# calculate winner
# display input


def create_gameboard(board_size):
    return [[0 for i in range(board_size)] for i in range(board_size)]


def display_board(board):
    for row in board:
        print(row)


def calculate_winner(row):
    if row.count(row[0]) == len(row) and row[0] != 0:
        print('winner')


board = create_gameboard(3)


def do_the_thing(board):
    display_board(board)

    board[0][0] = 1
    calculate_winner(board)
    display_board(board)

    board[1][1] = 2
    [calculate_winner(row) for row in board]
    display_board(board)

    board[0][1] = 1
    [calculate_winner(row) for row in board]
    display_board(board)

    board[2][2] = 2
    [calculate_winner(row) for row in board]
    display_board(board)

    board[0][2] = 1
    [calculate_winner(row) for row in board]
    display_board(board)


do_the_thing(board)
