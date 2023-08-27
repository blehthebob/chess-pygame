BOARD_LENGTH = 8
BOARD_HEIGHT = 8
W_PIECE_ROW = 0
W_PAWN_ROW = 1
B_PIECE_ROW = BOARD_HEIGHT - W_PIECE_ROW - 1
B_PAWN_ROW = BOARD_HEIGHT - W_PAWN_ROW - 1

# Converts notation for a square to the numeric location on the representation
# of the board.
# Assumes notation is of the form <lowercase_letter><number>
# Returns a pair of ints representing the position in the board nested list.
def position_numeric(pos: str):
    x = ord(pos[0]) - ord("a")
    y = int(pos[1]) - 1
    if 0 <= x < BOARD_LENGTH and 0 <= y < BOARD_HEIGHT:
        return (x, y)
    raise ValueError("Invalid square")

# Converts numeric location on the representation of the board to notation for 
# a square.
# Assumes notation is of the form (x, y)
# Returns a str of form <lowercase_letter><number>
def position_notation(x, y):
    if 0 <= x < BOARD_LENGTH and 0 <= y < BOARD_HEIGHT:
        return chr(ord("a") + x) + str(y + 1)
    raise ValueError("Invalid square")