## V9 -- WITH get_blank_squares -- 9/24/19 4:00pm 
class TicTacToe( object ):

    def __init__( self, dim):
        self.dimensions = dim
        self.square = [['_']*self.dimensions for dim in range(self.dimensions)]

    def print_small( self ):
        for i in range(self.dimensions):
            print (' '.join( self.square[i] ))
        print
    
    def print_large( self ):
        for i in range(self.dimensions):
            temp = ['  ' if x == '_' else ' ' + x for x in self.square[i]]
            print(' |'.join( temp))
            if i < len(self.square) - 1:
                print('---'+'+---'*(self.dimensions-1))
        print
    
    def get_blank_squares( self ):
        blank_squares = [(i, ii) for ii in range(ttt.dimensions)
                         for i in range(ttt.dimensions)
                         if ttt.square[i][ii] == '_' ]
        return(blank_squares)
        
    def automove( self ):
        result = self.get_blank_squares()
        print(result)
#         print('moving here:', list(result)[0])
        
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
            if all( [ self.square[row][col] == player for col in range(self.dimensions) ] ): return True
        for col in range(self.dimensions):
            if all( [ self.square[row][col] == player for row in range(self.dimensions) ] ): return True 
        if all( [ self.square[col][col] == player for col in range(self.dimensions) ] ): return True
        for r,c in zip(range(self.dimensions), reversed(range(self.dimensions))):
            if all( [self.square[r][c] == player ] ): return True
        return False

ttt = TicTacToe(3)
ttt.print_large()
# to test blank squares
for i in range(ttt.dimensions): ttt.set(0,i,'X')
ttt.automove()
