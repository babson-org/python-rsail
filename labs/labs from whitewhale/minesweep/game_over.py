import globals
def game_over(board:list) -> bool:
    cnt = 0
    for row in range(globals.ROWS):
        for col in range(globals.COLS):
            if board[row][col][0]  == (" \u2666") : cnt += 1

    print(cnt)
    if cnt == globals.MINES: return True
    else: return False

    