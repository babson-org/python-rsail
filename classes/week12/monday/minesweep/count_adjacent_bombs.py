from is_bomb_at import is_bomb_at
from get_adjacent_cells import get_adjacent_cells
import globals
def count_adjacent_bombs(board: list ) -> list:
    '''
    Now that bombs/mines have been placed on the board we check every
    cell on the board. If the cell is a bomb/mine we skip over it.
    We call get_adjacent_cells and get back a list of cell coordinates.
    We remove the current cell from the list and count the number of bombs/
    mines we have in adjacent cells.
    
    
    '''

    for r in range(globals.ROWS):
        for c in range(globals.COLS):
            coord = (r, c)
            '''
            is_bomb_at has parameters board and a tuple that contain the row and col we
            want to check. It returns true if there is a bomb/mine and false otherwise

            '''
            if is_bomb_at(board, (r, c)): continue #if there is a bomb go back to the inner for loop


            squares = get_adjacent_cells(coord) # not a bomb get list of coordinates of ajacent cells
            squares = [s for s in squares if s != (r, c)] # remove the current cell from the list   

            

            cnt = 0
            for  square in (squares):
                '''
                count the number of bombs/mines in adjacent cells
                '''
                if board[square[0]][square[1]][1] == '\U0001F4A3' : cnt += 1    
            '''
            replace the tuple at board[r][c] with tuple(diamond,cnt) or (diamond,'   ') 
            '''

            if cnt != 0:
                board[r][c] = (board[r][c][0], cnt)
            else:
                board[r][c] = (board[r][c][0], '   ')

            # or with list comprehension

            board[r][c] = (board[square[0]][square[1]][0], cnt) if cnt != 0 else (board[square[0]][square[1]][0], '   ')

    return board