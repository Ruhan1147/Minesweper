import random

class board:
    def __init__(self, dim_size, num_bombs):

        self.dim_size = dim_size
        self.num_bombs = num_bombs 

        self.board = self.make_new_board


        self.dug = set()
    
    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)] 
        
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            
            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            bombs_planted += 1
        return  board
    
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                     continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r,c)
    
    def get_num_neighbouring(self, row, col):


        num_neighbouring_bombs = 0
        for r in range(max(0,row-1), min(self.dim_size-1,row + 1)+1):
            for c in range(max(0, col-1), min(self.dim_size, col+1)+1):
                if r == row and c == col:
                    #org location - dont check
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1
    
    def dig(self, row, col):

        #dig at loc
        #return true if successful, else false if bomb

        #secnarios:
        #dig = bomb = game over
        #dig = no neighbouring bombs = recursively dig neighboring
        
        self.dug.add(row,col)

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def __str__(self):


        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' ' 


        
def play(dim_size=10, num_bombs=19):
    #1. create board and plant bombs.
    board =  board(dim_size, num_bombs)
    #2. show board and ask user where they want to dig
    #3a. if bomb, show game over
    #3b. if not bomb, recursively dig until each square near bomb
    #4. repeat 2 and 3a/b until no more spaces left to dig
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = input("Where would you like to dig? input a row,col")
        row, col = int(user_input[0]), int(user_input(-1))
        if row < 0 or row >= board.dim_size or col < 0 or col  >= dim_size:
            print("Invalid location, try agaim")
            continue

        safe = board.dig(row,col)
        if not safe:
            break
    
    if safe:
        print("u win")

    else:
        print("u lose")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main_':
    play()