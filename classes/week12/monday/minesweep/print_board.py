import globals
def print_board(board: list, level: int):
    
    '''
    board =[
        [('0','?? '),('0','?? '),('0',"?  "),('0',"?  "),('0',' '),('0','5')], 
        [('1','0'),('1','1'),('1','2'),('1','3'),('1','4'),('1','5')],
        [('2','0'),('2','1'),('2','2'),('2','3'),('2','4'),('2','5')],
    ]

    The above representation is actually a 2D board with a 2 element 
    tuple in each column. Each row has 6 tuples

    We could also represent the board as a true 3D:

    board = [
    [   # row 0
        [ ('0', '??') ],       # col 0
        [ (' ', '  ') ],       # col 1
        [ (' ', '  ') ],       # col 2
        [ ('0', '??') ],       # col 3
        [ (' ', '  ') ],       # col 4
        [ (' ', '  ') ]        # col 5
    ],
    [   # row 1
        [ ('0', '??') ],       # col 0
        [ (' ', '  ') ],       # col 1
        [ (' ', '  ') ],       # col 2
        [ ('0', '??') ],       # col 3
        [ (' ', '  ') ],       # col 4
        [ (' ', '  ') ]        # col 5
    ],
    [   # row 2
        [ ('0', '??') ],       # col 0
        [ (' ', '  ') ],       # col 1
        [ (' ', '  ') ],       # col 2
        [ ('0', '??') ],       # col 3
        [ (' ', '  ') ],       # col 4
        [ (' ', '  ') ]        # col 5
    ],
]

The depth dimension is a tuple in each column. 
Each row has 6 column lists and each column has a tuple



    
    globals.COLS = 6
    globals.ROWS = 3
    '''

    line_hash = '|-----'    

    print('      ', end = '')        
    for idx in range(globals.COLS):
        print(f'   {idx}  ', end = '')
        
    print(f'\n      {line_hash * globals.COLS}|')    

    for row in range(globals.ROWS):
        print(f'  {row}   ', end = '') 
        for col in range(globals.COLS): 
            symbol = board[row][col][level]

            if symbol == '??':
                print(f'| {symbol:3}' , end = '')
            else: print(f'| {symbol:3} ' , end = '')            
        print('|')

        print(f'      {line_hash * globals.COLS}|')

#print_board([],1)