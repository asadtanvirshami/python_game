def solve_nqueen(n):
    def is_safe(board,row,col):
        for i in range(row):
            if board[i] == col or \
                board[i]==col-(row-i) or\
                    board[i]==col+(row-i):
               return False
        return True
    
    def place_queen(board,row):
        if row == n:
            print(board)
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row]= col
                place_queen(board, row+1)
    
    board = [-1] * n
    place_queen(board, 0)
    
n=4
solve_nqueen(n)