from get_adjacent_cells import get_adjacent_cells
def update_board(board: list, coord: tuple):

    stack = []
    stack.append(coord)

    while stack:

        row, col = stack.pop(0)        
        board[row][col] = (board[row][col][1], board[row][col][1])

       
        if board[row][col][0] == "   ":
            

            squares = get_adjacent_cells((row, col))

            squares = [s for s in squares if s != (row, col)]
                
            for square in squares:
                r, c = square
                # Check if the cell is not yet revealed
                if board[r][c][0] != board[r][c][1]:
                    stack.append((r, c))

    