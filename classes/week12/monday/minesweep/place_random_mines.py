import globals
import random
def place_random_mines(board:list):
    '''
    To place random mines we use random.randint to get col and row.
    We then check if board[row][col][1] is empty. We need to reassign
    the tuple so both the first and second element need to be assigned.
    We do this in a while loop until we've placed globals.mines on the board
    
    '''

    cnt = 0
    while cnt < globals.MINES:
        col = random.randint(0, globals.COLS - 1)   # get random col number 
        row = random.randint(0, globals.ROWS - 1)   # get random row number
        '''
        when you first enter this routine the player board has a diamond
        and the base board has '   '
        '''   
        if board[row][col][1] == '   ': # if base board is blank we can place a bomb
            '''
            board[row][col] contain a tuple. we can not change a tuple but
            we can replace it. so board[row][col] needs a tuple whose
            player board has a diamond and base board has a bomb
            '''
            board[row][col] =  (board[row][col][0], '\U0001F4A3')
            cnt += 1

    
    return board