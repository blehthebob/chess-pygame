BOARD_LENGTH = 8
BOARD_HEIGHT = 8
PIECE_ROW = 0
PAWN_ROW = 1

# Converts notation for a square to the numeric location on the representation
# of the board.
# Assumes notation is of the form <lowercase_letter><number>
# Returns a pair of ints representing the position in the board nested list.
def position_numeric(pos: str):
    x = ord(pos[0]) - ord("a")
    y = int(pos[1]) - 1
    if 0 <= x < BOARD_LENGTH and 0 <= BOARD_HEIGHT:
        return (x, y)
    raise ValueError("Invalid square")