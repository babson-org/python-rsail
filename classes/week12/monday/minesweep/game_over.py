import globals
def game_over(board:list) -> bool:
    '''
    The game is over when either a cell is choosen that has bomb/mine
    on it or when the number of diamnonds on the player board is
    equal globals.MINES.  We check the first condition directly
    when we play the game and the latter condition here   
    
    '''
    # count the number of diamonds
    cnt = 0
    for row in range(globals.ROWS):
        for col in range(globals.COLS):
            if board[row][col][0]  == " \u2666" : cnt += 1

    #print(cnt)
    # compare
    if cnt == globals.MINES: return True
    else: return False

    