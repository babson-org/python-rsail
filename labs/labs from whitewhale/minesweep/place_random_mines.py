import globals
import random
def place_random_mines(board:list):

    cnt = 0
    while cnt < globals.MINES:
        col = random.randint(0, globals.COLS - 1)
        row = random.randint(0, globals.ROWS - 1)
           
        if board[row][col][1] == '   ':
            board[row][col] =  (board[row][col][0], '\U0001F4A3')
            cnt += 1

    
    return board