def is_bomb_at(board: list, coord: tuple) -> bool:

    bomb = False
    if board[coord[0]][coord[1]][1] == '\U0001F4A3': bomb = True    

    return bomb