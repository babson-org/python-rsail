import globals
import utils
from get_validated_input import get_validated_input
from place_random_mines import place_random_mines
from count_adjacent_bombs import count_adjacent_bombs
def initialize_board():
    utils.clear_screen()    

    txt1 = "Enter the width of the board: "
    txt2 = "width must be between 2 and 10 (inclusive), re-enter: "  
    low = 2
    high = 10  
    globals.COLS = get_validated_input(txt1, txt2, low, high)

    txt1 = "Enter the height of the board: "
    txt2 = "Height must be between 2 and 10 (inclusive), re-enter: "    
    globals.ROWS = get_validated_input(txt1, txt2, low, high)

    txt1 = "Enter the number of random mines: "
    low = 1
    high = globals.ROWS * globals.COLS - 1
    txt2 = f"Mines must be between 1 and {high} (inclusive), re-enter: "    
    globals.MINES = get_validated_input(txt1, txt2, low, high)   

    board = []
    
    for _ in range(globals.ROWS):
        row = []
        for _ in range(globals.COLS):
            col = (" \u2666" , '   ')
            row.append(col)
            
        board.append(row)    

    board = place_random_mines(board)  

    board = count_adjacent_bombs(board)  
   
    return board