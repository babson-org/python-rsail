import globals
import utils
from initialize_board import initialize_board
from print_board import print_board
from game_over import game_over
from get_validated_input import get_validated_input
from is_bomb_at import is_bomb_at
from update_board import update_board

def play_minesweep():
    '''
    Before we can begin to play we need to initalize the board. Then
    enter a while loop until the game is over. Get input from user and 
    end the game if bomb/mine choosen. If not, update board'
    
    '''

    board = initialize_board()


    utils.clear_screen()   
    print()   
    
    while not game_over(board):
        #utils.clear_screen()
        print_board(board, 0)
        #print_board(board,1)
        #print(board)
        print()

        txt1 = "How many over do you want to dig: "
        txt2 = f"You have to stay on the board. Enter 0 - {globals.COLS - 1}: "  
        low = 0
        high = globals.COLS - 1  
        col = get_validated_input(txt1, txt2, low, high)

        txt1 = "How many down do you want to dig: "
        txt2 = f"You have to stay on the board. Enter 0 - {globals.ROWS - 1}: "  
        low = 0
        high = globals.ROWS - 1  
        row = get_validated_input(txt1, txt2, low, high)

        if is_bomb_at(board, (row, col)):
            print('\n\nYou lost! You blew up the board!\n')            
            print_board(board, 1)
            print() 
                      
            break

        update_board(board, (row, col))

    if game_over(board):
        print('\nYou won, congratulatons!\n\n') 
        print_board(board, 0) 
        


    
play_minesweep()

