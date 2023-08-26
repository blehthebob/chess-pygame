# Converts notation for a square to the numeric location on the representation
# of the board.
# Assumes notation is of the form <lowercase_letter><number>
# Returns a pair of integers.
def position_numeric(pos: str):
    return (ord(pos[0]) - ord("a"), int(pos[1]) - 1)