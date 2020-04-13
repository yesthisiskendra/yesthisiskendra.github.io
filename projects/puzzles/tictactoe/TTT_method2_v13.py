# V13 -- with celebrated winner, refactored -- 9/26/19 11:11am
import random


class TicTacToe(object):

    def __init__(self, dim):
        self.dimensions = dim
        self.square = [['_']*self.dimensions for dim in range(self.dimensions)]

    def print_small(self):
        for i in range(self.dimensions):
            print(' '.join(self.square[i]))
        print

    def print_large(self):
        for i in range(self.dimensions):
            temp = ['  ' if x == '_' else ' ' + x for x in self.square[i]]
            print(' |'.join(temp))
            if i < len(self.square) - 1:
                print('---'+'+---'*(self.dimensions-1))
        print

    def get_blank_squares(self):
        blank_squares = [(i, ii) for ii in range(ttt.dimensions)
                         for i in range(ttt.dimensions)
                         if ttt.square[i][ii] == '_']
        return(blank_squares)

    def automove(self):
        result = self.get_blank_squares()
        choice = random.choice(result)
        self.set(choice[0], choice[1], 'O')

    def set(self, row, col, player_marker):
        self.square[row][col] = player_marker

    '''
    wins: 
    checks all rows
    checks all columns
    checks backslash diagonal
    checks forwardslash diagonal
    '''

    def wins(self, player):
        for row in range(self.dimensions):
            if all([self.square[row][col] == player for col in range(self.dimensions)]):
                return True
        for col in range(self.dimensions):
            if all([self.square[row][col] == player for row in range(self.dimensions)]):
                return True
        if all([self.square[col][col] == player for col in range(self.dimensions)]):
            return True
        if all([self.square[r][c] == player for r, c in zip(range(self.dimensions),
                                                            reversed(range(self.dimensions)))]):
                                                               return True
        return False


ttt = TicTacToe(3)
while ttt.get_blank_squares != 0:
    move = input('Where would you like to go?').split(',')
    ttt.set(int(move[0]), int(move[1]), 'X')
    ttt.print_large()
    if ttt.wins('X'):
        print('X IS THE WINNER!')
        break
    ttt.automove()
    ttt.print_large()
    if ttt.wins('O'):
        print('O IS THE WINNER!')
        break
