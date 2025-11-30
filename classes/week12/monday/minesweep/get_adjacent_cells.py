import globals
def get_adjacent_cells(coord: tuple) -> list:
    """
    Returns a list of valid board coordinates adjacent to a given cell.

    The result includes the given coordinate itself and all surrounding 
    cells (up to 8 neighbors). Coordinates that would fall outside the 
    board are excluded.

    Parameters:
        coord (tuple): A tuple (row, col) representing the cell of interest.        

    Returns:
        list: A list of (row, col) tuples for valid surrounding cells, 
              including the original cell.
    """
    squares = []

    # All relative positions around the given cell, including itself
    adjustments = [(-1, -1), (-1, 0), (-1, 1),
                   ( 0, -1), ( 0, 0), ( 0, 1),
                   ( 1, -1), ( 1, 0), ( 1, 1)]

    for dr, dc in adjustments:
        # Apply the offset to the original coordinate
        new_row = coord[0] + dr
        new_col = coord[1] + dc

        # Check if the new coordinate is within the bounds of the board
        if 0 <= new_row < globals.ROWS and 0 <= new_col < globals.COLS:
            squares.append((new_row, new_col))

    return squares