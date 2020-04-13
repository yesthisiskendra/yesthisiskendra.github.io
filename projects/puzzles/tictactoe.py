
def calculate_winner(array, direction):
    if array.count(array[0]) == len(array) and array[0] != 0:
        print(f"Player {array[0]} is the winner {direction}!")


def horizontal_winner(current_game):
    for row in current_game:
        calculate_winner(row, 'horizontally')


def vertical_winner(current_game):
    for col in range(len(current_game[0])):
        check = []
        for row in current_game:
            check.append(row[col])
        calculate_winner(check, 'vertically')


def diagonal_winner(current_game):
    check = []
    for i in range(len(current_game)):
        check.append(current_game[i][i])
    calculate_winner(check, 'diagonally')
    check_2 = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        check_2.append(current_game[col][row])
    calculate_winner(check_2, 'diagonally')


game_board = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]


def display_board(current_board):
    print("   0  1  2")
    for i, row in enumerate(current_board):
        print(i, row)


def check_for_wins(current_board):
    horizontal_winner(current_board)
    vertical_winner(current_board)
    diagonal_winner(current_board)


def get_and_store_input(current_board, player, row, column):
    current_board[row][column] = player
    display_board(current_board)
    check_for_wins(current_board)
    return(current_board)

# Horizontal check
# board = game_board
# board = get_and_store_input(board, 1, 1, 1)
# board = get_and_store_input(board, 2, 0, 0)
# board = get_and_store_input(board, 1, 1, 0)
# board = get_and_store_input(board, 2, 0, 2)
# board = get_and_store_input(board, 1, 1, 2)


# Diagonal check
board = game_board
board = get_and_store_input(board, 1, 1, 1)
board = get_and_store_input(board, 2, 0, 2)
board = get_and_store_input(board, 1, 0, 0)
board = get_and_store_input(board, 2, 2, 0)
board = get_and_store_input(board, 1, 2, 2)
