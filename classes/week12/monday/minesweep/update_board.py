from get_adjacent_cells import get_adjacent_cells
def update_board(board: list, coord: tuple):
    '''
    update_board involves the most computational thinking. When a cell is 
    uncovered on the player's board we check what that cell is on the base
    board.  It can be one of three things. 1) a bomb/mine, 2) a number or
    3) blank space. If it is a bomb/mine play_minesweep will terminate the
    game before we get here. If the base board cell is (2) or (3) we set the 
    player board's corrosponding cell to base board's cell.

    Here's where it get's interesting. If the cell is a blank we know all 
    surrounding cells do not contain a bomb/mine. All of those can be
    uncovered.  If any of those cells are blank we need to uncover their
    adjacent cells.  This process repeats untill all 'connected' black spaces
    are uncovered.   
    
    '''
    #create an empty list of cells that need to be checked
    stack = []
    # add the uncovered cell
    stack.append(coord)

    # while there are cells to check continue this loop
    while stack:
        
        # get the row and col of first item in stack, pop it off the stack
        row, col = stack.pop(0) 
        # assign player board cell  to base board cell      
        board[row][col] = (board[row][col][1], board[row][col][1])

        # if a number  return. If space continue
        if board[row][col][0] == "   ":
            
            # get adjacent squares
            squares = get_adjacent_cells((row, col))

            # remove uncovered cell from squares
            squares = [s for s in squares if s != (row, col)]

            # if the cell has not been revealed, add it to the stack    
            for square in squares:
                r, c = square
                # Check if the cell is not yet revealed
                if board[r][c][0] != board[r][c][1]:
                    stack.append((r, c))

    