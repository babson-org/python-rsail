def get_validated_input(txt1, txt2, low_int, high_int):
    """
    KEY INSIGHT: 
    In the game we need to get 5 inputs. 
        1) height of board
        2) width of board
        3) number of mines
        4) column selection
        5) row selection

        We are always asking for an integer and need to check
        input falls within range.  Rather then write the same 
        code 5 times we can create a generic function.

    Prompt the user for an integer input within a specified range.

    Continuously prompts the user using `txt1` until a valid integer within
    the range [`start`, `finish`] is entered. If the input is invalid,
    `txt2` is shown in subsequent prompts until valid input is received.

    Parameters:
    txt1 (str)    : Initial prompt message for user input.
    txt2 (str)    : Prompt message shown after invalid input.
    low_int (int) : Minimum acceptable value (inclusive).
    high_int (int): Maximum acceptable value (inclusive).

    Returns:
    int: A validated integer input from the user within the specified range.
    """
    txt = txt1
    while True:
        try:
            value = int(input(txt))
            if not (low_int <= value <= high_int): raise ValueError
            break
        except ValueError:
            txt = txt2

    return value
