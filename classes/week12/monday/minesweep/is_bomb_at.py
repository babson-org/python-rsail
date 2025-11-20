def is_bomb_at(board: list, coord: tuple) -> bool:
    '''
    this routine checks if there is a mine/bomb at given
    coordinates on the base board
    
    '''

    bomb = False
    if board[coord[0]][coord[1]][1] == '\U0001F4A3': bomb = True    

    return bomb