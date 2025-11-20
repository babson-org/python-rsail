import globals
import utils
from get_validated_input import get_validated_input
from place_random_mines import place_random_mines
from count_adjacent_bombs import count_adjacent_bombs




def initialize_board():
    '''
Before we start playing the game we need to initalize the board. Let's
consider the player board to be the first element in the tuple and the 
base board to be the second element in the tuple. To initalize the player 
board we need to fill it with diamonds.  To iniitalize the base board we
need to fill it first with random mines, and then for each other cell fill
it with number of adjacent mines or empty space for 0. We use '   ' for 
0 or a blank so formatting in print_board works correctly


'''
    utils.clear_screen() 

    # using get_validated_input ask user for 3 inputs
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

    board = []     # we create an empty board
    
    for _ in range(globals.ROWS):
        row = []                      # create an empty row
        for _ in range(globals.COLS):
            col = (" \u2666" , '   ')  # for each col in row create a tuple
            row.append(col)            # append tuple to row
            
        board.append(row)              # apend row to board

    # remember tuples are immutable

    board = place_random_mines(board)  # place random mines on board

    board = count_adjacent_bombs(board) # place the number of adjacent bombs for each cell 

    # NOTE there are 12 functions in this lab. we just covered 9 of them!
    # We need to define two more functions before we play the game.
   
    return board