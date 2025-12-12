from is_bomb_at import is_bomb_at
from get_adjacent_cells import get_adjacent_cells
import globals
def count_adjacent_bombs(board: list ) -> list:

    for r in range(globals.ROWS):
        for c in range(globals.COLS):
            coord = (r, c)
            if is_bomb_at(board, (r, c)): continue

            squares = get_adjacent_cells(coord)
            squares = [s for s in squares if s != (r, c)]    

            

            cnt = 0
            for  square in (squares):
        
                if board[square[0]][square[1]][1] == '\U0001F4A3' : cnt += 1    
    
            board[r][c] = (board[square[0]][square[1]][0], cnt) if cnt != 0 else (board[square[0]][square[1]][0], '   ')

    return board